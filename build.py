import tempfile
import os
import shutil
import re
import zipfile

def remove_macrons(text):
    """Remove Latin macrons from the given text."""
    macron_map = {
        'Ā': 'A', 'ā': 'a',
        'Ē': 'E', 'ē': 'e',
        'Ī': 'I', 'ī': 'i',
        'Ō': 'O', 'ō': 'o',
        'Ū': 'U', 'ū': 'u'
    }
    return ''.join(macron_map.get(c, c) for c in text)


def process_directory(source_dir):
    """Process the directory as per the specified requirements with README.md copying feature."""
    if not os.path.isdir(source_dir):
        raise ValueError("The specified directory does not exist.")

    # Path for README.md in the source directory
    readme_src_path = os.path.join(source_dir, 'README.md')

    # Check if README.md exists in the source directory
    if os.path.isfile(readme_src_path):
        # Copy README.md to the current working directory, overwriting if it exists
        shutil.copy2(readme_src_path, os.getcwd())

    # Rest of the process is same as previous
    with tempfile.TemporaryDirectory() as temp_dir:
        build_dir = os.path.join(temp_dir, os.path.basename(source_dir))
        shutil.copytree(source_dir, build_dir)

        for root, dirs, files in os.walk(build_dir):
            for file in files:
                if file.endswith(('.txt', '.cfg')):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    content = remove_macrons(content)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)

        zip_name = os.path.basename(source_dir) + '.zip'
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(build_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, start=build_dir))

    # Temporary directory is automatically cleaned up

    return zip_name
    """Process the directory as per the specified requirements with improvements."""
    if not os.path.isdir(source_dir):
        raise ValueError("The specified directory does not exist.")

    # Create a temporary directory in the system's designated temp area
    with tempfile.TemporaryDirectory() as temp_dir:
        # Step 2: Copy the directory to the temporary build folder
        build_dir = os.path.join(temp_dir, os.path.basename(source_dir))
        shutil.copytree(source_dir, build_dir)

        # Step 3: Remove Latin macrons from .txt and .cfg files
        for root, dirs, files in os.walk(build_dir):
            for file in files:
                if file.endswith(('.txt', '.cfg')):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    content = remove_macrons(content)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)

        # Step 4: Zip the folder
        zip_name = os.path.basename(source_dir) + '.zip'
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(build_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, start=build_dir))

    # The temporary directory is automatically cleaned up upon exiting the 'with' block

    return zip_name
# Example usage (you can replace 'example_directory' with the actual directory you want to process)
process_directory('Lethal_Company_Latin')
