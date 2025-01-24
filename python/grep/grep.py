"""Grep"""

import re

def grep(pattern, flags, files):
    """ Grep
    Args:
        pattern (str): pattern to search
        flags (list): list of flags
        files (list): list of files
    Returns:
        str: results
    """
    results = []
    case_insensitive = "-i" in flags
    match_entire_line = "-x" in flags
    invert_match = "-v" in flags
    line_numbers = "-n" in flags
    file_names_only = "-l" in flags

    if case_insensitive:
        pattern = pattern.lower()

    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            for idx, line in enumerate(lines, start=1):
                original_line = line.rstrip("\n")
                search_line = original_line.lower() if case_insensitive else original_line

                if match_entire_line:
                    match = search_line == pattern
                else:
                    match = re.search(re.escape(pattern), search_line) is not None

                if invert_match:
                    match = not match

                if match:
                    if file_names_only:
                        if file not in results:
                            results.append(file)
                        break
                    result = original_line
                    if line_numbers:
                        result = f"{idx}:{result}"
                    if len(files) > 1:
                        result = f"{file}:{result}"
                    results.append(result)

    return "\n".join(results) + "\n" if results else ""
