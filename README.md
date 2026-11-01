# arifwoozeer.io

#https://arifwoozeer.github.io/arifwoozeer.io/

Run `python3 books.py` to refresh the bookshelf and the About-page reading sentence
from the same Goodreads feeds. The weekly workflow commits both files. The sentence
uses up to two currently-reading titles and their authors, without AI; an empty
currently-reading shelf leaves the sentence unchanged. Edit outside the
`current-reading` comment markers to keep other About text manual.

Run the reading-update checks with `python3 -m unittest discover -s tests`.
