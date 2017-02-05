Title: General tips regarding Pelican
Date:2016-12-23
tags: Pelican
category: Tips
author: Abraham Vinod
summary: Notes on the margin for using Pelican.

- Markdown syntax can be found at 
  [SourceForge](https://sourceforge.net/p/pelican-edt/wiki/markdown_syntax/#md_ex_lists).
- Commenting:
    - Use the standard HTML comments `<!-- COMMENT_GOES_HERE -->`. (See this [SO answer](http://stackoverflow.com/a/4829998/1846549))
    - Use `{# COMMENT_GOES_HERE #}` for commenting lines inside the template.
- Code highlighting for a particular language can be done by writing the
  language name after the code block command. The first block was created by
  encapsulating the code you see in ``` instead of ~~~.
```
~~~python
# Feed generation
~~~
```
generates
~~~python
# Feed generation
~~~
- Links:
    - For internal linking, use `[specifically]({filename}4 - Verification.md)`.
    - Create HTML tags for navigation within a file as `<a
      name="NAME_YOUR_TAG"></a>`, and then navigate to it via this markdown
      code snippet `[GO_THERE](#NAME_YOUR_TAG)`.
- Lists:
    - Skip a line
    - Use `1.` for numbered
    - Use `+` or `-` for bulleted lists.
- Use `grep -rnw '/path/to/somewhere/' -e "pattern"` to identify any trouble
  some components inside the template.
