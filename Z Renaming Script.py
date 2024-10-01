import os

HR_PREFIX = "HR-"
files = os.listdir()

def rename_HR_files(files):
    for filename in files:
        if os.path.isdir(filename):
            continue
        
        file_name, file_extension = os.path.splitext(filename)
        
        if "HR" in filename and file_extension == ".py":
            new_name = file_name.replace(" - HR", "").replace("-HR", "").replace("HR-", "").replace("HR", "")
            new_name = new_name.strip().replace(" ", " ").replace("--", "-")
            new_name = f"{HR_PREFIX}{new_name}{file_extension}"
            os.rename(filename, new_name)
            print(f"Renamed: {filename} -> {new_name}")

rename_HR_files(files)
# /////////////////////////////////////////
import os

LC_SQL_PREFIX = "LC - SQL"
files = os.listdir()

def rename_sql_files(files):
    for filename in files:
        if os.path.isdir(filename):
            continue
        
        file_name, file_extension = os.path.splitext(filename)
        
        if file_extension == ".sql":
            if file_name.startswith(LC_SQL_PREFIX):
                print(f"Skipped: {filename} (Already formatted)")
                continue

            clean_name = file_name.strip()
            final_name = f"{LC_SQL_PREFIX} {clean_name}{file_extension}"
            os.rename(filename, final_name)
            print(f"Renamed: {filename} -> {final_name}")

rename_sql_files(files)