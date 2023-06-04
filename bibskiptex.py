import re, sys
from argparse import ArgumentParser
from itertools import chain

from pybtex import errors
from pybtex.exceptions import PybtexError
from pybtex.bibtex import format_from_files


citation_pattern = re.compile(
        r'\\(?:cite|citet|citep)'
        r'(?:\[[^\]]*\])*'
        r'{(?P<citation>[^}]*)}')


def trim_citation(citation):
    cits = citation.split(',')
    return map(str.strip, cits)


def get_citations(texfile):
    with open(texfile, encoding='utf=8') as f:
        tex = f.read()

    return chain(*map(trim_citation, citation_pattern.findall(tex)))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-s', "--style", default="plainnat")
    parser.add_argument('-b', "--bibliography", action="append", default=[])
    parser.add_argument('-o', "--out", required=True)
    parser.add_argument("texs", metavar="tex_source", nargs="+")
    args = parser.parse_args()

    citations = list(chain(*map(get_citations, args.texs)))

    errors.set_strict_mode(False)

    format_from_files(
        args.bibliography,
        style = args.style,
        citations = citations,
        output_filename = args.out)

