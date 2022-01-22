---
title: Exporting Tex Elements As Images Using Python.
tags: [Tex, Scripting, Workflow]
style: default
color: primary
date: 22-01-2022
updated: 22-01-2022
---

Today while writing a blog post on [a quantum circuit trick](https://thecharmingsociopath.github.io/blog/swap-gate), I needed to create some quantum circuit diagrams. First I thought of using Qiskit or Cirq for it, but the overhead to install and setup them didn't seem worth it. So I tried Tikz, and a Tex package called [Qcircuit.]()

I wanted to export the circuit created using Qcircuit as images, and it took a while to figure out an optimal way to do it. I decided to write it here since this method is very versatile and can be used to export tables, tikz images, and a lot more.

##### Note: Commands here are for Arch. You can use apt for debian distros.

You need to have tex installed in your system. Packages I use are
```bash
sudo pacman -S texlive-most texlive-core texlive-science texlive-latexextra texlive-bibtexextra texlive-publishers texlive-pictures
```

Some of these will be useless for you so check with documentation before installing to avoid polluting your system.

You need a python packages [latextools](https://pypi.org/project/latextools/) and `drawsvg`.

```bash
pip install latextools drawsvg
```

You need `pdf2svg` to convert the generated pdf to svg, which can then be converted to png, etc.

```bash
yay -S pdf2svg
```

You need to install `Qcircuit` from CTAN. Create a path `$HOME/texmf/tex/latex/qcircuit`. Then download the `.sty` file into that location.
You can figure out above path using `kpsewhich -var-value TEXMFHOME`

Now you can use latextools to export a latex snippet as an image. Here is a short snippet.

```python
import latextools

pdf = latextools.render_qcircuit(r'''
         \push{\ket{a}} & \ctrl{1} & \targ & \ctrl{1} & \qw & \push{\ket{b}} \\
         \push{\ket{b}} & \targ & \ctrl{-1} & \targ & \qw & \push{\ket{a}} \\
        ''')

pdf.save('swap-using-cnot.pdf')
pdf.rasterize('swap-using-cnot.png', scale=3)
```

The `latextools` documentation lists more examples.


