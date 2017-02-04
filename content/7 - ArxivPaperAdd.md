title: Adding papers on Arxiv
Date:2017-02-03
tags: Arxiv
category: How To
author: Abraham Vinod
summary: Some tips on adding TeX generated papers to Arxiv

Recently, I published one of my [papers](https://arxiv.org/abs/1610.04550) to
Arxiv. You can find an informal discussion on this paper [here]({filename}8 -
hscc2017.md) .

There were a couple of things which I found relevant and omitted in
the Arxiv's wizard. It is there on their FAQs.


1. Arxiv does not accept `.bib` files. Instead, we have to upload the `.bbl`
fle. [^bbl]
1. Arxiv does not accept `.pdf` files when generated using TeX. We have to
upload the tex files, necessary figures, style files, and the `.bbl` file.
[^thingsneeded]
1. Adding multiple items on Arxiv is a pain. The best way to accomplish this is
to `zip` all the required files, and then upload the zip. Arxiv can process
`zip` and `tar.gz`.[^zipping]

[^bbl]: [https://arxiv.org/help/submit_tex#bibtex](https://arxiv.org/help/submit_tex#bibtex)
[^thingsneeded]: [https://arxiv.org/help/submit_tex#wegotem](https://arxiv.org/help/submit_tex#wegotem)
[^zipping]: [https://arxiv.org/help/tar](https://arxiv.org/help/tar)
