#! /usr/bin/env python


'''
Cite Extension for Python-Markdown
==================================

Wraps the inline content surrounded by three double quotes into <cite> tags.

Usage
-----

    >>> import markdown
    >>> src = '"""Who Is Killing the Great Chefs of Europe?""" is the last movie I watched.'
    >>> html = markdown.markdown(src, ['cite'])
    >>> print(html)
    <p><cite>Who Is Killing the Great Chefs of Europe?</cite> is the last movie I watched.</p>

Dependencies
------------

* [Markdown 2.0+](http://www.freewisdom.org/projects/python-markdown/)


Copyright
---------

2011, 2012 [The active archives contributors](http://activearchives.org/)
All rights reserved.

This software is released under the modified BSD License. 
See LICENSE.md for details.
'''


import markdown
from markdown.inlinepatterns import SimpleTagPattern


CITE_RE = r'(\"{3})(.+?)\2'


class CiteExtension(markdown.extensions.Extension):
    """Adds cite extension to Markdown class"""

    def extendMarkdown(self, md, md_globals):
        """Modifies inline patterns"""
        md.inlinePatterns.add('cite', SimpleTagPattern(CITE_RE, 'cite'), '<not_strong')


def makeExtension(configs={}):
    return CiteExtension(configs=dict(configs))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
