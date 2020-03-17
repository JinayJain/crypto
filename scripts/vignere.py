#!/usr/bin/env python

import click

stdin = click.get_text_stream('stdin')

@click.command(help='Encrypts input from STDIN using the KEYWORD with a Vignere cipher')
@click.argument('keyword', type=str)
@click.option('-d', '--decrypt', is_flag=True, default=False, help='Decrypts STDIN using KEYWORD')
def main(keyword, decrypt):
    string_in = stdin.read()

    if keyword.isalpha() != True:
        raise click.BadParameter('Keyword must only contain letters.')

    keyword.capitalize()

    encrypted = ""
    key_idx = 0
    for idx in range(len(string_in)):
        if not string_in[idx].isalpha():
            encrypted += string_in[idx]
            continue
        
        char_id = ord(string_in[idx].capitalize()) - ord('A')
        offset = ord(keyword[key_idx]) - ord('A')
        if decrypt:
            char_id -= offset
            char_id += 26
        else: char_id += offset
        
        char_id %= 26

        encrypted += chr(char_id + ord('A' if string_in[idx].isupper() else 'a'))

        key_idx += 1
        key_idx %= len(keyword)

    click.echo(encrypted, nl=False)


if __name__ == '__main__':
    main()

