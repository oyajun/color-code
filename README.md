# Color Code

"Color Code" is the app converts to the resistance value from the color code.  
Written with GTK 4 (Python) and libadwaita.
![image](https://raw.githubusercontent.com/oyajun/color-code/main/data/screenshots/screenshot1.png)


# Memo
```bash
xgettext --files-from=po/POTFILES --output=po/POTFILE.pot --from-code=UTF-8 --add-comments --keyword=_ --keyword=C_:1c,2
msginit -i po/POTFILE.pot -o po/ja.po -l ja.utf8
```
