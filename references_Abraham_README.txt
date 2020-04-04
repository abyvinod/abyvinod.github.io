conda create -n hugo python=3.7
pip3 install -U academic
academic import --bibtex static/references_Abraham.bib
(Use --overwrite at the end if you want to overwrite)
Add

categories:
- featured_pub

into the top matter to have it show up on the home page.
