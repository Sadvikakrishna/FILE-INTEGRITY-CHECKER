import hashlib
import os
import json
HASH_LOG_FILE = 'file_hashes.json'
BLOCK_SIZE = 4096 
def get_sha256_hash(path_to_file):
    sha256 = hashlib.sha256()
    try:
        with open(path_to_file, 'rb') as file:
            for block in iter(lambda: file.read(BLOCK_SIZE), b''):
                sha256.update(block)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"[ERROR] Cannot locate file: {path_to_file}")
        return None
def load_previous_hashes():
    if os.path.exists(HASH_LOG_FILE):
        with open(HASH_LOG_FILE, 'r', encoding='utf-8') as log_file:
            return json.load(log_file)
    return {}
def save_current_hashes(hashes_to_store):
    with open(HASH_LOG_FILE, 'w', encoding='utf-8') as log_file:
        json.dump(hashes_to_store, log_file, indent=4)
def report_deleted_files(old_hashes, new_hashes):
    deleted = False
    for path in old_hashes:
        if path not in new_hashes:
            print(f"[REMOVED] File no longer exists: {path}")
            deleted = True
    return deleted
def verify_directory_files(folder_path):
    stored_hashes = load_previous_hashes()
    latest_hashes = {}
    changes_found = False
    print(f"\n[NOTICE] Now scanning: {folder_path}")
    for root_dir, subdirs, file_list in os.walk(folder_path):
        for name in file_list:
            path_to_file = os.path.join(root_dir, name)
            file_hash = get_sha256_hash(path_to_file)
            if file_hash:
                latest_hashes[path_to_file] = file_hash
                if path_to_file in stored_hashes:
                    if stored_hashes[path_to_file] != file_hash:
                        print(f"[MODIFIED] Content changed: {path_to_file}")
                        changes_found = True
                else:
                    print(f"[NEW FILE] Added: {path_to_file}")
                    changes_found = True
    if report_deleted_files(stored_hashes, latest_hashes):
        changes_found = True
    save_current_hashes(latest_hashes)
    if not changes_found:
        print("[INFO] No changes found. All files remain unchanged.")
def main():
    folder = input("Please enter the folder path to monitor: ").strip()
    if os.path.isdir(folder):
        verify_directory_files(folder)
    else:
        print("[ERROR] That doesn't appear to be a valid folder path.")
if __name__ == '__main__':
    main()