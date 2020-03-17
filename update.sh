#!/usr/bin/env sh

# Used to update the scripts

echo "Moving Python scripts to ~/.local/bin/"
for file in *.py; do
    base=$(basename -s .py $file)
    cp $file ~/.local/bin/$base
done

