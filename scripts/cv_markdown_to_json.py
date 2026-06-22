#!/usr/bin/env python3
"""
Build _data/cv.json from the site's real, structured content instead of the
unedited academicpages placeholder _pages/cv.md.

Sources:
- basics      <- _config.yml `author:` block
- education   <- _pages/education.md "## Education" section
- skills      <- _pages/education.md "## Technical Skills" section
- work        <- _academic-career/*.md + _industrial-experiences/*.md front matter
- publications, presentations, teaching, portfolio <- their respective collections
"""

import os
import re
import json
import yaml
import argparse
import glob
from datetime import datetime, date

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

def parse_config(config_file):
    if not os.path.exists(config_file):
        return {}
    with open(config_file, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def extract_author_info(config):
    """Build the `basics` block from _config.yml's author: settings."""
    author_info = {
        "name": config.get('name', ''),
        "email": "",
        "phone": "",
        "website": config.get('url', ''),
        "summary": "",
        "location": {
            "address": "",
            "postalCode": "",
            "city": "",
            "countryCode": "US",
            "region": ""
        },
        "profiles": []
    }

    author = config.get('author', {})
    if not author:
        return author_info

    if author.get('name'):
        author_info['name'] = author.get('name')
    if author.get('email'):
        author_info['email'] = author.get('email')
    if author.get('location'):
        author_info['location']['city'] = author.get('location', '')

    summary_parts = []
    if author.get('bio'):
        summary_parts.append(author.get('bio'))
    if author.get('employer'):
        summary_parts.append(f"Affiliated with {author.get('employer')}")
    author_info['summary'] = '. '.join(summary_parts)

    profiles = []
    if author.get('googlescholar'):
        profiles.append({"network": "Google Scholar", "username": "", "url": author.get('googlescholar')})
    if author.get('orcid'):
        profiles.append({"network": "ORCID", "username": "", "url": author.get('orcid')})
    if author.get('researchgate'):
        profiles.append({"network": "ResearchGate", "username": "", "url": author.get('researchgate')})
    if author.get('github'):
        profiles.append({"network": "GitHub", "username": author.get('github'), "url": f"https://github.com/{author.get('github')}"})
    if author.get('linkedin'):
        profiles.append({"network": "LinkedIn", "username": author.get('linkedin'), "url": f"https://www.linkedin.com/in/{author.get('linkedin')}"})
    if author.get('twitter'):
        profiles.append({"network": "Twitter", "username": author.get('twitter'), "url": f"https://twitter.com/{author.get('twitter')}"})
    author_info['profiles'] = profiles

    return author_info

def extract_section(markdown_text, heading, next_heading_level=2):
    """Return the raw text under `## {heading}` up to the next heading of the same (or higher) level."""
    pattern = rf'^##\s+{re.escape(heading)}\s*$'
    lines = markdown_text.split('\n')
    start = None
    for i, line in enumerate(lines):
        if re.match(pattern, line.strip()):
            start = i + 1
            break
    if start is None:
        return ''

    end = len(lines)
    heading_prefix = '#' * next_heading_level
    for i in range(start, len(lines)):
        if lines[i].strip().startswith(heading_prefix):
            end = i
            break
    return '\n'.join(lines[start:end]).strip()

def parse_education(education_md_path):
    """Parse the '## Education' section of _pages/education.md into JSON Resume entries."""
    if not os.path.exists(education_md_path):
        return []

    with open(education_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    section = extract_section(content, 'Education')
    section = section.split('\n---\n')[0]  # stop at the first horizontal rule

    entries = []
    for block in re.split(r'\n\s*\n', section):
        lines = [l.replace('**', '').strip(' *') for l in block.strip().split('\n') if l.strip()]
        if len(lines) < 3:
            continue

        date_match = re.match(r'(.+?)\s*[–—-]\s*(.+)', lines[0])
        start_date = date_match.group(1).strip() if date_match else lines[0]
        end_date = date_match.group(2).strip() if date_match else ''

        area = lines[1]

        institution_line = lines[2]
        institution_match = re.match(r'\[(.+?)\]\(.*?\)\s*,?\s*(.*)', institution_line)
        if institution_match:
            institution, location = institution_match.groups()
        else:
            institution, location = institution_line, ''

        rest = '\n'.join(lines[3:])
        gpa_match = re.search(r'GPA[:\s]*([\d./]+)', rest)
        gpa = gpa_match.group(1) if gpa_match else None

        entries.append({
            "institution": institution.strip(),
            "area": area.strip(),
            "studyType": "",
            "startDate": start_date,
            "endDate": end_date,
            "location": location.strip(),
            "gpa": gpa,
            "courses": []
        })

    return entries

def parse_technical_skills(education_md_path):
    """Parse the '## Technical Skills' bullet list of _pages/education.md."""
    if not os.path.exists(education_md_path):
        return []

    with open(education_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    section = extract_section(content, 'Technical Skills')

    skills = []
    for line in section.split('\n'):
        match = re.match(r'-\s*\*\*(.+?):\*\*\s*(.+)', line.strip())
        if match:
            category, items = match.groups()
            keywords = [k.strip() for k in items.split(',') if k.strip()]
            skills.append({"name": category.strip(), "level": "", "keywords": keywords})

    return skills

def _format_front_matter_date(value):
    if isinstance(value, (datetime, date)):
        return value.strftime('%Y-%m')
    if value in (None, ''):
        return ''
    return str(value)

def parse_work_collection(collection_dir):
    """Parse front matter from a collection of experience markdown files into JSON Resume work entries."""
    entries = []
    if not os.path.exists(collection_dir):
        return entries

    for md_file in sorted(glob.glob(os.path.join(collection_dir, '*.md'))):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        front_matter_match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
        if not front_matter_match:
            continue

        fm = yaml.safe_load(front_matter_match.group(1)) or {}
        start_date = fm.get('start_date')
        end_date = fm.get('end_date')

        entries.append({
            "company": fm.get('company', ''),
            "position": fm.get('title', ''),
            "website": fm.get('company_url', ''),
            "location": fm.get('location', ''),
            "startDate": _format_front_matter_date(start_date),
            "endDate": "Present" if end_date == "Present" else _format_front_matter_date(end_date),
            "summary": fm.get('description', ''),
            "highlights": [],
            "_sort_key": start_date if isinstance(start_date, (datetime, date)) else date.min,
            "_is_present": end_date == "Present"
        })

    return entries

def parse_work(repo_root):
    entries = parse_work_collection(os.path.join(repo_root, '_academic-career'))
    entries += parse_work_collection(os.path.join(repo_root, '_industrial-experiences'))

    entries.sort(key=lambda e: (not e['_is_present'], e['_sort_key']), reverse=True)
    for e in entries:
        del e['_sort_key']
        del e['_is_present']

    return entries

def parse_publications(pub_dir):
    publications = []
    if not os.path.exists(pub_dir):
        return publications

    for pub_file in sorted(glob.glob(os.path.join(pub_dir, "*.md"))):
        with open(pub_file, 'r', encoding='utf-8') as file:
            content = file.read()
        front_matter_match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
        if front_matter_match:
            front_matter = yaml.safe_load(front_matter_match.group(1)) or {}
            publications.append({
                "name": front_matter.get('title', ''),
                "publisher": front_matter.get('venue', ''),
                "releaseDate": front_matter.get('date', ''),
                "website": front_matter.get('paperurl', ''),
                "summary": front_matter.get('excerpt', '')
            })

    return publications

def parse_talks(talks_dir):
    talks = []
    if not os.path.exists(talks_dir):
        return talks

    for talk_file in sorted(glob.glob(os.path.join(talks_dir, "*.md"))):
        with open(talk_file, 'r', encoding='utf-8') as file:
            content = file.read()
        front_matter_match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
        if front_matter_match:
            front_matter = yaml.safe_load(front_matter_match.group(1)) or {}
            talks.append({
                "name": front_matter.get('title', ''),
                "event": front_matter.get('venue', ''),
                "date": front_matter.get('date', ''),
                "location": front_matter.get('location', ''),
                "description": front_matter.get('excerpt', '')
            })

    return talks

def parse_teaching(teaching_dir):
    teaching = []
    if not os.path.exists(teaching_dir):
        return teaching

    for teaching_file in sorted(glob.glob(os.path.join(teaching_dir, "*.md"))):
        with open(teaching_file, 'r', encoding='utf-8') as file:
            content = file.read()
        front_matter_match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
        if front_matter_match:
            front_matter = yaml.safe_load(front_matter_match.group(1)) or {}
            teaching.append({
                "course": front_matter.get('title', ''),
                "institution": front_matter.get('venue', ''),
                "date": front_matter.get('date', ''),
                "role": front_matter.get('type', ''),
                "description": front_matter.get('excerpt', '')
            })

    return teaching

def parse_portfolio(portfolio_dir):
    portfolio = []
    if not os.path.exists(portfolio_dir):
        return portfolio

    for portfolio_file in sorted(glob.glob(os.path.join(portfolio_dir, "*.md"))):
        with open(portfolio_file, 'r', encoding='utf-8') as file:
            content = file.read()
        front_matter_match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
        if front_matter_match:
            front_matter = yaml.safe_load(front_matter_match.group(1)) or {}
            portfolio.append({
                "name": front_matter.get('title', ''),
                "category": front_matter.get('collection', 'portfolio'),
                "date": front_matter.get('date', ''),
                "url": front_matter.get('permalink', ''),
                "description": front_matter.get('excerpt', '')
            })

    return portfolio

def create_cv_json(config_file, repo_root, output_file):
    config = parse_config(config_file)
    education_md = os.path.join(repo_root, '_pages', 'education.md')

    cv_json = {
        "basics": extract_author_info(config),
        "work": parse_work(repo_root),
        "education": parse_education(education_md),
        "skills": parse_technical_skills(education_md),
        "languages": config.get('languages', []),
        "interests": config.get('interests', []),
        "references": [],
        "publications": parse_publications(os.path.join(repo_root, "_publications")),
        "presentations": parse_talks(os.path.join(repo_root, "_talks")),
        "teaching": parse_teaching(os.path.join(repo_root, "_teaching")),
        "portfolio": parse_portfolio(os.path.join(repo_root, "_portfolio"))
    }

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(cv_json, file, indent=2, cls=DateTimeEncoder)

    print(f"Successfully generated {output_file} from real site content")

def main():
    parser = argparse.ArgumentParser(description='Build _data/cv.json from real site content')
    parser.add_argument('--output', '-o', required=True, help='Output JSON file')
    parser.add_argument('--config', '-c', required=True, help='Jekyll _config.yml file')
    parser.add_argument('--repo-root', '-r', help='Repository root (defaults to parent of this script\'s directory)')
    args = parser.parse_args()

    repo_root = args.repo_root or str((__import__('pathlib').Path(__file__).parent.parent))
    create_cv_json(args.config, repo_root, args.output)

if __name__ == '__main__':
    main()
