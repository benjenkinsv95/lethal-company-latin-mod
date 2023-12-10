import os
import shutil
import tempfile
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

def process_specific_files_and_folders():
    """Process specific files and folders in the current directory and create a zip file 'Lethal Company Latin.zip'."""
    current_dir = os.getcwd()
    zip_name = 'Lethal Company Latin.zip'
    files_and_folders_to_include = ['BepInEx', 'CHANGELOG.md', 'icon.png', 'manifest.json', 'README.md']

    with tempfile.TemporaryDirectory() as temp_dir:
        # Copy specified files and folders
        for item in files_and_folders_to_include:
            src_path = os.path.join(current_dir, item)
            if os.path.exists(src_path):
                dst_path = os.path.join(temp_dir, item)
                if os.path.isdir(src_path):
                    shutil.copytree(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)

        # Process files in the temporary directory
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file.endswith(('.txt', '.cfg')):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    content = remove_macrons(content)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)

        # Create zip file
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, start=temp_dir))

    return zip_name

# Example usage
process_specific_files_and_folders()
