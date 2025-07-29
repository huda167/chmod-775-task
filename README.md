# chmod-775-task - Linux & Python

 Task Description

- Understand file permissions in Linux.
- Create a flowchart explaining how permissions are checked.
- Write a Python script that uses chmod to change file permissions to rwxrwxr-x (775).

 Permissions Breakdown

- Owner: Read, Write, Execute (rwx)
- Group: Read, Write, Execute (rwx)
- Others: Read, Execute (r-x)
- Numeric Representation: 775

 Files Included

- change_permission.py: Python script that applies chmod 775 to test.py.
- test.py: Dummy file used for permission modification.
- flowchart.png: Flowchart explaining permission logic.
- README.md: This file.

 How to Run

1. Open terminal in the project folder.
2. Run:
   ```bash
   python change_permission.py
