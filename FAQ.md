Frequently Asked Questions
==========================

### Doesn't tabnanny handle this already?

Nope. Tabnanny (and similar tools) will helpfully point out where
you've inadvertently used tabs, allowing you to manually fix them,
case-by-case. `tabular_cleanse` actually fixes bad tab/space mixes,
converting them into the indentation seen by the python parser.

### I thought the only solution to bad tabbing was executing the file and dealing with the results?

"execute the broken code!" sounds like a bad solution. In this case,
the solution is simply letting you see (and, presumably, edit) the
code the way the python parser sees it.

### I'm pretty sure that we're supposed to shun people who mix tabs and spaces.

Well, we may shun, but that doesn't change the fact that sometimes we
need to read, or even fix, their code. `tabular_cleanse` simply aims
to make that possible at scales larger than "one or two misplaced
tabs".

