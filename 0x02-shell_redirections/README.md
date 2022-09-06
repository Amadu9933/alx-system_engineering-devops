echo prints text to the terminal
echo "\"(Ôo)'" prints "(Ôo)'to the terminal \ is used to escape special characters
cat /etc/passwd displays the contents of /etc/passwd, the cat command is short for concatenate
cat /etc/passwd /etc/hosts displays the contents of both files
tail is used to display lines in a file from the end, use -n followed by the number of lines do display eg. tail -n /etc/passwd 10 displays last ten lines of the file
head -n 10 /etc/passwd displays the first 10 lines of the file
head -n -3 iacta | tail -n 1 dispays only the third line of the file
echo "text" > file, overwrites file with text
ls -la > ls_cwd_content is used to write ls -la out to the file
tail -n 1 iacta >> iacta duplicates the last line of iacta
find . -name "*.js" -exec rm -rf {} \; finds and removes all files with .js extention that are present in the current directory and all its subfolders
