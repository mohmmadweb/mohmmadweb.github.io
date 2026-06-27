---
permalink: /education/
title: "Educational Background"
author_profile: true
redirect_from:
  # - /education/
  # - /education.html
---

## Education

<div class="experiences-timeline">
{% for edu in site.data.education %}
  <div class="experience-card {% if edu.current %}current-academic-experience{% else %}past-academic-experience{% endif %}">
    <div class="experience-header">
      <div class="experience-content">
        <div class="experience-title-line">
          <h3 class="experience-title">{{ edu.area }}</h3>
        </div>
        <div class="experience-details-container">
          <div class="experience-details">
            <span class="dates">{{ edu.start_date }} &ndash; {{ edu.end_date }}</span>
            <span class="title-separator">&bull;</span>
            <span class="institution">{% if edu.institution_url %}<a href="{{ edu.institution_url }}" target="_blank" rel="noopener">{{ edu.institution }}</a>{% else %}{{ edu.institution }}{% endif %}, {{ edu.location }}</span>
          </div>
        </div>
        <div class="honor-description">
          {% if edu.gpa %}<em>Cumulative GPA: {{ edu.gpa }}</em><br>{% endif %}
          {% if edu.thesis_title %}<strong>Thesis Title:</strong> "{{ edu.thesis_title }}"{% if edu.thesis_grade %} &mdash; <em>Thesis Grade: {{ edu.thesis_grade }}</em>{% endif %}<br>{% endif %}
          {% if edu.supervisors.size > 0 %}<strong>{% if edu.supervisors.size > 1 %}Supervisors{% else %}Supervisor{% endif %}:</strong> {% for sup in edu.supervisors %}<a href="{{ sup.url }}" target="_blank" rel="noopener">{{ sup.name }}</a>{% unless forloop.last %} &amp; {% endunless %}{% endfor %}<br>{% endif %}
          {% if edu.highlight %}<em>{{ edu.highlight }}</em>{% endif %}
        </div>
      </div>
    </div>
  </div>
{% endfor %}
</div>

---

## Standardized Test Scores

<!-- - **TOEFL iBT:** 110 / 120 (R: 24, L:28, S: 27, W: 28) -->
- **Iran Language Institute (ILI):** Course Completion Certificate at ILI (Advanced 3) - Above Average - Issued Jul 2018


---

## Research Interests

- Large Language Models (LLMs)
- Machine Learning & Deep Learning
- Natural Language Processing (NLP)
- Social Network Analysis & Complex Networks
- Graph Mining & Graph Neural Networks
- Data Science, Data Mining & Business Intelligence
- Data Analysis & Statistical Modeling
- Software Engineering

---

## Technical Skills

{% for skill in site.data.skills %}- **{{ skill.category }}:** {{ skill.items | join: ", " }}
{% endfor %}

---

## Relevant Coursework

### Master of Science Level
- Linear Algebra (17/20)
- Machine Learning (20/20)
- Natural Language Processing (19.6/20)
- Enterprise Information Technology Architecture (18/20)
- Deep Generative Models
- Machine Learning Theory

### Bachelor of Science Level
- Discrete Mathematics (15/20)
- Fundamentals of Computer and Programming (20/20)
- Advanced Programming (18.9/20)
- Data Structures (18.5/20)
- Algorithm Design (17.1/20)
- Artificial Intelligence (19.92/20)
- Digital Design (19.4/20)
- Computer Architecture (18/20)
- Signal & Systems (18.6/20)
- Database Design Principles (18/20) - *Ranked 1st with Great Distinction*
- Operating Systems (18.5/20)
- Data Mining (17.79/20)
- System Analysis and Design (19.79/20)
- Technical Language (19.75/20)
- Research Method and Presentation (18.63/20)
- Internship (19.75/20)

---

## Nostalgic Grades 

*This section is purely for nostalgic purposes and does not contain professionally relevant information.*

| High School (10th-12th Grade) | Middle School (7th-9th Grade) | Elementary School (1st-6th Grade) |
|:-----------------------------:|:-----------------------------:|:--------------------------------:|
| **Alborz High School**<br>Isfahan, Iran | **Khaghani Middle School**<br>Isfahan, Iran | **Dr. Shariati Elementary School**<br>Isfahan, Iran |
| **Overall GPA:** 19.15 / 20<br>**10th Grade:** 19.50 / 20 (rank 4th)<br>**11th Grade:** 19.14 / 20 (rank 2nd)<br>**12th Grade:** 18.79 / 20 (rank 1st) | **7th Grade:** 19.88 / 20<br>**8th Grade:** 19.88 / 20<br>**9th Grade:** 19.93 / 20 | **1st Grade:** 20.00 / 20<br>**2nd Grade:** 20.00 / 20<br>**3rd Grade:** 20.00 / 20<br>**4th Grade:** 20.00 / 20<br>**5th Grade:** 19.91 / 20<br>**6th Grade:** 20.00 / 20 |