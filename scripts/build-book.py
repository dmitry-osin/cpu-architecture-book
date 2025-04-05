#!/usr/bin/env python3


import os
import re
import glob

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]

def main():
    os.makedirs("build", exist_ok=True)
    
    with open("build/book.md", "w", encoding="utf-8") as outfile:
        if os.path.exists("metadata.yml"):
            with open("metadata.yml", "r", encoding="utf-8") as metadata_file:
                outfile.write(metadata_file.read())
                outfile.write("\n\n")
        
        if os.path.exists("toc.md"):
            with open("toc.md", "r", encoding="utf-8") as toc_file:
                outfile.write(toc_file.read())
                outfile.write("\n\n")
        
        md_files = [f for f in glob.glob("chapter/*.md")]
        
        md_files.sort(key=natural_sort_key)
        
        for md_file in md_files:
            print(f"Add file: {md_file}")
            with open(md_file, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")
    
    print("Merged file created in build/book.md")

if __name__ == "__main__":
    main()