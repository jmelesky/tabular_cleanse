README
=============

We have a million ounces of prevention when it comes to mixing tabs
and spaces in a python file, from tabnanny to pylint to "-tt" to
simply being familiar with your editor configuration.

But, in the unfortunate case where you inherit a tainted file, there
is no cure. You can run "tabify" in emacs, but that just replaces tabs
with a set number of spaces. If you're familiar with the errors that
can result from sloppy tabbing, you know it's not as simple as all
that. In fact,

> First, tabs are replaced (from left to right) by one to eight spaces
> such that the total number of characters up to and including the
> replacement is a multiple of eight (this is intended to be the same
> rule as used by Unix).
> 
> (source: http://docs.python.org/reference/lexical_analysis.html#indentation )

`tabular_cleanse.py` is your pound of cure.

Usage
-----

`tabular_cleanse.py` is a simple python script that interprets tabs
according to the language spec mentioned above. It's so simple that it
takes stdin and sends to stdout:

    cat scriptofpain.py | python tabular_cleanse.py > scriptofjoy.py

And that's all there is to it.

Limitations
-----------

`tabular_cleanse.py` does not perform any prettification or other
reformatting aside from the tab interpretation described in the Python
language spec. In other words, it won't make the code pretty,
readable, or even correct. Instead, it gives you the code, indented as
python sees it, bereft of the terrible plague named "tab".