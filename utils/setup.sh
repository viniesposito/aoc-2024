#!/bin/bash

usage() {
    echo "Usage: $0 <day_number>"
    echo "Example: $0 4"
    exit 1
}

# Check if a day number was provided
if [ $# -ne 1 ]; then
    usage
fi

# Validate that the input is a number
if ! [[ $1 =~ ^[0-9]+$ ]]; then
    echo "Error: Please provide a valid number"
    usage
fi

day_num=$1
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
parent_dir="$(dirname "$script_dir")"
template_file="$script_dir/template.py"
day_folder="$parent_dir/day${day_num}"
new_file="${day_folder}/aoc2024_day${day_num}.py"

# Check if template file exists
if [ ! -f "$template_file" ]; then
    echo "Error: template.py not found in utils directory"
    exit 1
fi

# Create day folder if it doesn't exist
if [ ! -d "$day_folder" ]; then
    mkdir -p "$day_folder"
    echo "Created directory: $day_folder"
fi

# Copy template file to new location
cp "$template_file" "$new_file"

# Replace all occurrences of 'dayx' with 'day<number>'
# Using case-insensitive search to catch variations like 'dayX', 'dayx', 'DayX'
sed -i '' -E "s/day[xX]/day${day_num}/g" "$new_file"

echo "Successfully:"
echo "- Created $new_file"
echo "- Replaced all instances of 'dayx' with 'day${day_num}'"