#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt
pip install -e alibaba1688api

# Convert static asset files
# python manage.py collectstatic --no-input