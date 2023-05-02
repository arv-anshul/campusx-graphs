""" Extra codes require for the project. """

from pathlib import Path

H3C = '<center><h1>%s</h1></center>'
H2C = '<center><h3>%s</h3></center>'
NBSP = '&nbsp;'


def get_readme_txt(fp: Path) -> str:
    with open(fp) as md:
        return md.read()
