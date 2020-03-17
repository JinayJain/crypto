#!/usr/bin/env python

import click

stdin = click.get_text_stream('stdin')

def caesar(string_in, shift, decrypt):
    encrypted = ""
    for i in range(len(string_in)):
        c = string_in[i]

        if c.isalpha():
            offset = ord(c.capitalize()[0]) - ord('A')
            if decrypt:
                offset -= shift
                offset += 26
            else: offset += shift
            offset %= 26

            encrypted += chr(offset + ord('A' if c.isupper() else 'a'))
        else:
            encrypted += c

    click.echo(encrypted, nl=False)


@click.command(help="Gives the Caesar cipher encrypted version of STDIN input")
@click.option('-s', '--shift', type=int, help='If set, the number of letters to shift the message')
@click.option('-d', '--decrypt', default=False, is_flag=True, help='Decrypts STDIN by shift or all shifts')
def main(shift, decrypt):
    string_in = stdin.read()

    if shift:
        caesar(string_in, shift, decrypt)
    else:
        for i in range(26): caesar(string_in, i, decrypt)


if __name__ == '__main__':
    main()
