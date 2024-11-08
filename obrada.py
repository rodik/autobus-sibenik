import json
import os
from datetime import datetime, timedelta

def calculate_stop_times(departure_times, stops):
    """
    Calculate exact arrival times for each stop based on departure times
    and distances between stops.

    Parameters:
    - departure_times: List of departure times (as strings in "HH:MM" format) from the first stop.
    - stops: Dictionary of stops with keys as stop names and values as distances in minutes to the next stop.

    Returns:
    - A list of lists, where each inner list represents the times at each stop for a particular departure.
    """
    stop_names = list(stops.keys())         # List of stop names in order
    stop_distances = list(stops.values())   # List of distances between stops in order

    all_stop_times = []                     # To hold arrival times for each departure time

    # Iterate over each departure time and calculate arrival times at each stop
    for departure in departure_times:
        # Convert string departure time to a datetime object
        current_time = datetime.strptime(departure, "%H:%M")
        stop_times = [(stop_names[0], current_time.strftime("%H:%M"))]  # Add first stop's time

        # Calculate arrival time for each subsequent stop
        for i in range(1, len(stop_names)):
            current_time += timedelta(minutes=stop_distances[i])    # Add travel time to next stop
            stop_times.append((stop_names[i], current_time.strftime("%H:%M")))  # Append stop and time

        all_stop_times.append(stop_times)    # Add this schedule to the list of all schedules

    return all_stop_times

def convert_to_markdown(line_data):
    """
    Convert bus line data to a markdown string, generating tables for each schedule type (e.g., "ponedjeljak-subota" and "nedjelja").

    Parameters:
    - line_data: Dictionary containing line information (line number, name, direction, stops, departures).

    Returns:
    - A markdown string with tables for each schedule type.
    """
    # Retrieve line number, name, and direction for markdown header
    line_num = line_data.get("broj", "")
    line_name = line_data.get("linija", "")
    stops = line_data.get("stanice", {})
    note = line_data.get("napomena", "")
    departures = line_data.get("polasci", {})

    # Initial header for the bus line
    md_content = f"# Linija {line_num}: {line_name}\n\n"

    # Conditionally add the note if it exists and is not empty
    if note:
        md_content += f"**Napomena**: {note}\n\n"

    # Process each schedule type separately (e.g., "ponedjeljak-subota", "nedjelja")
    for day_type, times in departures.items():
        # Markdown section header for the day type
        md_content += f"## {day_type}\n\n"

        # Construct the markdown table header with stop names
        headers = "| " + " | ".join(stops.keys()) + " |\n"
        separator = "|" + ":------:|" * (len(stops)) + "\n"
        md_content += headers + separator

        # Calculate full schedule (arrival times) for each departure time
        full_schedule = calculate_stop_times(times, stops)
        for schedule in full_schedule:
            # Each row in the table represents arrival times for one departure
            row = "| **" + schedule[0][1] + "** | " + " | ".join([time for _, time in schedule[1:]]) + " |\n"
            md_content += row

        md_content += "\n"  # Add space between tables for readability

    return md_content

def process_files(input_folder="linije", output_folder="timetables"):
    """
    Process all JSON files in the input folder, converting each to a markdown file,
    and compile all markdown outputs into a single combined file.

    Parameters:
    - input_folder: Directory containing JSON files with bus line data.
    - output_folder: Directory where markdown files will be saved.
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over each file in the input folder
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".json"):
                # Load the JSON data for each file
                with open(os.path.join(root, file), "r") as f:
                    line_data = json.load(f)

                    # Convert the JSON data to markdown format
                    markdown_content = convert_to_markdown(line_data)
                    markdown_content += "Povratak na [Linije](#linije)\n"
                    line_num = line_data.get("broj", "unknown")
                    
                    # Save the markdown content to a file in the output folder
                    output_file = os.path.join(output_folder, str(line_num).zfill(3) + '_' + file.replace(".json", ".md"))
                    with open(output_file, "w") as md_file:
                        md_file.write(markdown_content)

    # Combine all individual markdown files into a single file
    combined_file = os.path.join(output_folder, "sve_tablice.md")
    with open(combined_file, "w") as combined:
        
        # Write a timestamp at the beginning of the file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        combined.write(f"### Zadnja izmjena: {timestamp}\n\n")

        combined.write("## Linije\n\n")
        # Generate the TOC with links to headers
        for md_file in sorted(os.listdir(output_folder)):
            if md_file.endswith(".md") and md_file != "sve_tablice.md":
                # Extract line number and line name from the markdown file name
                with open(os.path.join(output_folder, md_file), "r") as f:
                    first_line = f.readline().strip()  # Read the header line
                    if first_line.startswith("# Linija"):
                        header_text = first_line[2:].strip()  # Remove leading "# " to get the header text
                        # Convert header text to a markdown linkable format
                        # Replace spaces with hyphens and make it lowercase
                        anchor_link = header_text.lower().replace(" ", "-").replace(":", "")
                        combined.write(f"- [{header_text}](#{anchor_link})\n")

        combined.write("\n---\n\n")  # Divider after TOC

        # Append the content of each markdown file
        for md_file in sorted(os.listdir(output_folder)):
            if md_file.endswith(".md") and md_file != "sve_tablice.md":
                # Read each markdown file and append its content to the combined file
                with open(os.path.join(output_folder, md_file), "r") as f:
                    combined.write(f.read() + "\n\n")


if __name__ == "__main__":
    process_files()
