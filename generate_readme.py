"""
Simple script to generate README.md

To create README.md, run `python generate_readme.py > README.md`
"""

import datetime
import random
import urllib.parse


# Type annotations TBD
def cycle_shuffle(iterable):
    used_items = []

    while True:
        if len(iterable) == len(used_items):
            used_items.clear()
        next_item = random.choice([i for i in iterable if i not in used_items])
        used_items.append(next_item)
        yield next_item


# Colors from https://github.com/catppuccin/catppuccin#-palettes
# Flavor: Macchiato
# Not including Text, Subtext1, ..., Mantle, Crust
catpp_colors = {
    "Rosewater": "f4dbd6",
    "Flamingo": "f0c6c6",
    "Pink": "f5bde6",
    "Mauve": "c6a0f6",
    "Red": "ed8796",
    "Maroon": "ee99a0",
    "Peach": "f5a97f",
    "Yellow": "eed49f",
    "Green": "a6da95",
    "Teal": "8bd5ca",
    "Sky": "91d7e3",
    "Sapphire": "7dc4e4",
    "Blue": "8aadf4",
    "Lavender": "b7bdf8",
}
catpp_color_values = cycle_shuffle(catpp_colors.values())


class Badge:
    def __init__(
        self, label: str, logo: None | str = None, bg_color: None | str = None, logo_color: None | str = None
    ):
        self.label = label
        self.logo = logo
        self.bg_color = bg_color
        self.logo_color = logo_color

        if not logo:
            self.logo = self.label

    @property
    def label_url(self) -> str:
        return urllib.parse.quote(self.label)

    @property
    def logo_url(self) -> str:
        # ? Not sure how write this to satisfy the typing issue
        return urllib.parse.quote(self.logo)  # type: ignore

    def __str__(self) -> str:
        url = f"https://img.shields.io/badge/{self.label_url}-{self.bg_color}?"

        params = []

        if self.logo:
            params.append(f"logo={self.logo_url}")

        if self.logo_color:
            params.append(f"logoColor={self.logo_color}")

        params_string = "&".join(params)

        badge_github_ready = f"![{self.label}]({url + params_string})"
        return badge_github_ready


def prep_badges_for_readme(badges: list[Badge], bg_color):
    """Serves three purposes:
    - Make uniform bg_color
    - Add random logo_color if None
    - Cast Badges to strings, ready for README"""
    # 'But functions should only have one role!!'
    # It's out of my hands, kid 😎
    colored_badges = []
    for badge in badges:
        badge.bg_color = bg_color
        if not badge.logo_color:
            badge.logo_color = next(catpp_color_values)
        colored_badges.append(str(badge))

    return colored_badges


# Markdown Styling
def md_heading(text, heading_size=1):
    print(f"{'#' * heading_size} {text}")


def md_text(text):
    """Prints text with extra print() for .md styling; used for paragraphs and linebreaks"""
    print(text)
    print()


def md_url(text, url_link, is_image=False):
    url_hyperlink = f"[{text}]({url_link})"
    if is_image:
        return f"!{url_hyperlink}"
    return url_hyperlink


def md_comment(text):
    print(f"<!-- {text} -->\n")


# README.md

UNIFORM_BG_COLOR = "24273a"

md_comment(f"This README.md was generated @ {datetime.datetime.now()}")
md_heading("Hi! I'm @JoshPaulie")
md_text(
    "I'm a computer science student currently working in special education, hoping to shift gears to something more programming related."
)
md_heading("Skills", 3)
skills_badges = [
    Badge("Python (Fanatic)", logo="Python", logo_color=catpp_colors["Yellow"]),
    Badge("Pycord (Bot Framework)", "Discord", logo_color=catpp_colors["Blue"]),
    Badge("Git", logo_color=catpp_colors["Peach"]),
    Badge("Flask", logo_color=catpp_colors["Green"]),
    Badge("Linux", logo_color=catpp_colors["Teal"]),
    Badge("Bash/Zsh scripting, automation", "GNUBash", logo_color=catpp_colors["Flamingo"]),
    Badge("PowerShell", logo_color=catpp_colors["Rosewater"]),
    Badge("JavaScript", logo_color=catpp_colors["Yellow"]),
    Badge("C++", logo_color=catpp_colors["Sapphire"]),
]
print(" ".join(prep_badges_for_readme(skills_badges, UNIFORM_BG_COLOR)))
interests_badges = [
    Badge("After Effects", logo="Adobe After Effects", logo_color=catpp_colors["Lavender"]),
    Badge("Premiere Pro", logo="Adobe Premiere Pro", logo_color=catpp_colors["Mauve"]),
    Badge("Illustrator", logo="Adobe Illustrator", logo_color=catpp_colors["Peach"]),
    Badge("Blender", logo_color=catpp_colors["Peach"]),
    Badge("Raspberry Pi", logo_color=catpp_colors["Red"]),
]
md_heading("Interests", 3)
print(" ".join(prep_badges_for_readme(interests_badges, UNIFORM_BG_COLOR)))
md_heading("I'm for hire!", 3)
md_text(
    "Proficient (and fixated) with Python. Avaliable for intership opprotunities or full-time remote work."
)
md_text(
    f"Contact via {md_url('LinkedIn', 'https://www.linkedin.com/in/joshua-lee-88a8a5154')} or {md_url('Twitter', 'https://twitter.com/itsbexli')}"
)
