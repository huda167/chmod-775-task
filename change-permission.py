import os


filename = "test.py" 

# تغيير صلاحيات الملف إلى 775 (rwxrwxr-x)
os.chmod(filename, 0o775)

print(f"Permissions for {filename} changed to rwxrwxr-x (775)")