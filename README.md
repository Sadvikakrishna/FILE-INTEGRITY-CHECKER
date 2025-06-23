# FILE-INTEGRITY-CHECKER
*COMPANY NAME* : CODTECH IT SOLUTIONS

*NAME*	       : PASUPULETI SADVIKA KRISHNA

*INTERN ID*	   : CT06DG3074

*DOMAIN*	     : CYBER SECURITY & EHICAL HACKING

*DURATION*	   : 6 WEEKS

*MENTOR*       : NEELA SANTOSH	

The Description about the task

This Python script is a file integrity checker that monitors a directory for changes in its files by computing and comparing their SHA-256 hashes. When executed, the script 

prompts the user to enter a directory path. It then recursively scans all files within that directory, calculates their SHA-256 hashes in blocks of 4096 bytes to efficiently

handle large files, and compares these hashes to a previously saved set stored in a JSON file (file_hashes.json). If a file is new, it reports it as “[NEW FILE]”; if a    

file’s contents have changed, it flags it as “[MODIFIED]”; and if a previously logged file is no longer found, it marks it as “[REMOVED]”. The script uses Python’s standard 

libraries: hashlib for hashing, os for file system traversal, and json for reading and writing the hash log. This tool is useful in various scenarios such as monitoring      

sensitive configuration files in system administration, detecting unauthorized modifications in cybersecurity, verifying backups, or ensuring codebase integrity in software  

development. It is particularly relevant in compliance-heavy environments like healthcare or finance, where tracking file integrity is critical. One important correction in   
the script is replacing the line if _name_ == '_main_': with if __name__ == '__main__': to ensure the main function runs as expected when the script is executed directly.    

Enhancements such as logging changes to a separate file, filtering by file type, or adding timestamped reports could make this tool even more robust and practical for real-   
world use

*OUTPUT*:

![Image](https://github.com/user-attachments/assets/8c7beb61-f113-4ff2-b738-fb6f42853bdb)
