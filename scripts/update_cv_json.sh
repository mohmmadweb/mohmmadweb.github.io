#!/bin/bash

# Script to regenerate _data/cv.json from the site's real content
# (academic-career, industrial-experiences, education.md, publications, talks, etc.)

# Set the base directory to the repository root
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Define file paths
CV_JSON="$BASE_DIR/_data/cv.json"
CONFIG_FILE="$BASE_DIR/_config.yml"

# Check if the Python script exists
PYTHON_SCRIPT="$BASE_DIR/scripts/cv_markdown_to_json.py"
if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "Error: Python script not found at $PYTHON_SCRIPT"
  exit 1
fi

# Run the Python script to (re)generate the CV JSON
echo "Generating CV JSON from site content..."
python3 "$PYTHON_SCRIPT" --output "$CV_JSON" --config "$CONFIG_FILE" --repo-root "$BASE_DIR"

# Check if the conversion was successful
if [ $? -eq 0 ]; then
  echo "Successfully updated CV JSON file at $CV_JSON"
  
  # Optional: Build the Jekyll site to see the changes
  echo "Would you like to build the Jekyll site to see the changes? (y/n)"
  read -r answer
  if [[ "$answer" =~ ^[Yy]$ ]]; then
    echo "Building Jekyll site..."
    cd "$BASE_DIR" && bundle exec jekyll serve
  fi
else
  echo "Error: Failed to update CV JSON file"
  exit 1
fi

exit 0
