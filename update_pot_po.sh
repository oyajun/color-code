#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

POTFILES="po/POTFILES"
POTFILE="po/POTFILE.pot"
LINGUAS="po/LINGUAS"

if [ ! -f "$POTFILES" ]; then
    echo "Error: $POTFILES not found!"
    exit 1
fi

if [ ! -f "$LINGUAS" ]; then
    echo "Error: $LINGUAS not found!"
    exit 1
fi

echo "Updating $POTFILE from $POTFILES..."
xgettext --files-from="$POTFILES" --output="$POTFILE" --from-code=UTF-8 --add-comments --keyword=_ --keyword=C_:1c,2

while read -r lang; do
    [[ -z "$lang" || "$lang" =~ ^# ]] && continue
    PO_FILE="po/${lang}.po"
    if [ ! -f "$PO_FILE" ]; then
        msginit -i "$POTFILE" -o "$PO_FILE" -l "$lang" --no-translator
    else
        msgmerge --update --backup=none "$PO_FILE" "$POTFILE"
    fi
done < "$LINGUAS"

echo "All POT and PO files processed!"
