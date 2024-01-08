import os
import json
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
    'Ū': 'U', 'ū': 'u',
    'Á': 'A', 'á': 'a',
    'É': 'E', 'é': 'e',
    'Í': 'I', 'í': 'i',
    'Ó': 'O', 'ó': 'o',
    'Ú': 'U', 'ú': 'u',
    'À': 'A', 'à': 'a',
    'È': 'E', 'è': 'e',
    'Ì': 'I', 'ì': 'i',
    'Ò': 'O', 'ò': 'o',
    'Ù': 'U', 'ù': 'u',
    'Â': 'A', 'â': 'a',
    'Ê': 'E', 'ê': 'e',
    'Î': 'I', 'î': 'i',
    'Ô': 'O', 'ô': 'o',
    'Û': 'U', 'û': 'u',
    'Ä': 'A', 'ä': 'a',
    'Ë': 'E', 'ë': 'e',
    'Ï': 'I', 'ï': 'i',
    'Ö': 'O', 'ö': 'o',
    'Ü': 'U', 'ü': 'u',
    'Ã': 'A', 'ã': 'a',
    'Ñ': 'N', 'ñ': 'n',
    'Õ': 'O', 'õ': 'o',
    'Å': 'A', 'å': 'a',
    'Œ': 'OE', 'œ': 'oe',
    'Ç': 'C', 'ç': 'c',
    'Æ': 'AE', 'æ': 'ae'
}

    return ''.join(macron_map.get(c, c) for c in text)

def process_specific_files_and_folders_with_two_zips():
    """Process specific files and folders in the current directory and create two zip files."""
    current_dir = os.getcwd()
    zip_name_normal = 'Lethal Company Latin.zip'
    zip_name_educational = 'Lethal Company Latin Educational.zip'
    zip_name_macron = 'Lethal Company Latin Macron.zip'
    files_and_folders_to_include = ['BepInEx', 'Lethal Company_Data', 'CHANGELOG.md', 'icon.png', 'manifest.json', 'README.md', 'phanfont']

    with tempfile.TemporaryDirectory() as temp_dir_normal, tempfile.TemporaryDirectory() as temp_dir_educational,tempfile.TemporaryDirectory() as temp_dir_macron:
        # Copy specified files and folders to both temporary directories
        for item in files_and_folders_to_include:
            src_path = os.path.join(current_dir, item)
            if os.path.exists(src_path):
                dst_path_normal = os.path.join(temp_dir_normal, item)
                dst_path_educational = os.path.join(temp_dir_educational, item)
                dst_path_macron = os.path.join(temp_dir_macron, item)
                if os.path.isdir(src_path):
                    shutil.copytree(src_path, dst_path_normal)
                    shutil.copytree(src_path, dst_path_macron)
                    shutil.copytree(src_path, dst_path_educational)
                else:
                    shutil.copy2(src_path, dst_path_normal)
                    shutil.copy2(src_path, dst_path_macron)
                    shutil.copy2(src_path, dst_path_educational)

        # Process files in the temporary directory for normal zip (remove macrons)
        for root, dirs, files in os.walk(temp_dir_normal):
            for file in files:
                if file.endswith(('.txt', '.cfg')):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    content = remove_macrons(content)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)

        for root, dirs, files in os.walk(temp_dir_educational):
            for file in files:
                if file.endswith('Weight.txt'):
                    file_path = os.path.join(root, file)
                    with open('weight-nota.txt', 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                elif file.endswith('manifest.json'):
                    file_path = os.path.join(root, file)
                    
                    # Read and parse the JSON content
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = json.load(f)

                    # Modify the 'name' and 'description' properties
                    content['name'] += "_Educational"  # Append "_Educational" to the existing name
                    content['description'] += " - Educational notes like the ordinal number that corresponds to a cardinal number are included. These can be educational, but break immersion"  # Append the additional description

                    # Write the updated content back to the JSON file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(content, f, indent=4, ensure_ascii=False)

        # Create zip file without macrons
        with zipfile.ZipFile(zip_name_normal, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(temp_dir_normal):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, start=temp_dir_normal))

        # Create zip file with macrons (original content)
        with zipfile.ZipFile(zip_name_macron, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(temp_dir_macron):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, start=temp_dir_macron))
        
        with zipfile.ZipFile(zip_name_educational, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(temp_dir_educational):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, start=temp_dir_educational))

    return zip_name_normal, zip_name_macron, zip_name_educational

# Example usage
process_specific_files_and_folders_with_two_zips()
