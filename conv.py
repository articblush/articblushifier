#!/usr/bin/env python3

import signal
import argparse
import sys
import os

from pathlib import Path
from ImageGoNord import GoNord
from rich.console import Console
from rich.panel import Panel

mypath=str((Path(os.path.expanduser('~')) / 'Pictures' / 'articblush').absolute())


def main():
    signal.signal(signal.SIGINT, signal_handler)
    console = Console()

    articblushifier = GoNord()
    articblushifier.reset_palette()
    add_articblush_palette(articblushifier)

    # Checks if there's an argument
    if len(sys.argv) > 1:
        image_paths = fromCommandArgument(console)
    else:
        image_paths = fromTui(console)

    for image_path in image_paths:
        if os.path.isfile(image_path):
            process_image(image_path, console, articblushifier)
        else:
            console.print(
                f"❌ [red]We had a problem in the pipeline! \nThe image at '{image_path}' could not be found! \nSkipping... [/]"
            )
            continue


# Gets the file path from the Argument
def fromCommandArgument(console):
    command_parser = argparse.ArgumentParser(
        description="A simple cli to manufacture Articblush themed wallpapers."
    )
    command_parser.add_argument(
        "Path", metavar="path", nargs="+", type=str, help="The path(s) to the image(s)."
    )
    args = command_parser.parse_args()

    return args.Path


# Gets the file path from user input
def fromTui(console):
    console.print(
        Panel(
            "🏭 [bold magenta] Articblushifier [/] 🏭", expand=False, border_style="magenta"
        )
    )

    return [
        os.path.expanduser(path)
        for path in console.input(
            "🖼️ [bold yellow]Which image(s) do you want to manufacture? (image paths separated by spaces):[/] "
        ).split()
    ]


def process_image(image_path, console, articblushifier):
    image = articblushifier.open_image(image_path)
    
    console.print(f"🔨 [blue]manufacturing '{os.path.basename(image_path)}'...[/]")

    # TODO: might be a better idea to save the new Image in the same directory the command is being run from
    save_path = os.path.join(
        mypath, "articblush_" + os.path.basename(image_path)
    )

    articblushifier.convert_image(image, save_path=(save_path))
    console.print(f"✅ [bold green]Done![/] [green](saved at '{save_path}')[/]")


def add_articblush_palette(articblushifier):
    articblushPalette = [
        "#040c16", "#09111b", "#070f19", "#0c141e",
        "#323949", "#3d3e51", "#A2E4B8", "#ecc6e8",
        "#80ffff", "#d2daf4", "#d2daf4", "#cdd5ef",
        "#09111b", "#070f19", "#0c141e", "#E6676B",
        "#FF7377", "#A2E4B8", "#AAF0C1", "#e2d06a",
        "#eadd94", "#92bbed", "#ecc6e8", "#80ffff",
        "#d2daf4", "#d2daf4", "#070f19", "#E6676B",
        "#92bbed", "#ecc6e8", "#80ffff", "#d2daf4",
        "#88b1e3", "#8db6e8", "#92bbed", "#d2daf4"
    ]

    for color in articblushPalette:
        articblushifier.add_color_to_palette(color)


## handle CTRL + C
def signal_handler(signal, frame):
    print()
    sys.exit(0)


if __name__ == "__main__":
    main()
