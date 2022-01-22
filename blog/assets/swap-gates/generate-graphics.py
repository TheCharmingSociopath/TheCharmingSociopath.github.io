"""

- `pip install latextools drawsvg`
- install qcircuit from CTAN to $HOME/texmf/tex/latex/qcircuit/qcircuit.sty
- Figure out above path using `kpsewhich -var-value TEXMFHOME`
- sudo pacman -S texlive-pictures
- yay -S pdf2svg
- run `python swap.py`

"""


import latextools

pdf = latextools.render_qcircuit(r'''
         \push{\ket{a}} & \ctrl{1} & \targ & \ctrl{1} & \qw & \push{\ket{b}} \\
         \push{\ket{b}} & \targ & \ctrl{-1} & \targ & \qw & \push{\ket{a}} \\
        ''')

pdf.save('swap-using-cnot.pdf')
pdf.rasterize('swap-using-cnot.png', scale=3)


pdf = latextools.render_qcircuit(r'''
        \push{\ket{c}} & \ctrl{1} & \qw & \push{\ket{c}} \\
        \push{\ket{t}} & \targ & \qw & \push{\ket{c \oplus t}} \\
        ''')

pdf.save('cnot.pdf')
pdf.rasterize('cnot.png', scale=3)


pdf = latextools.render_qcircuit(r'''
        \push{\ket{a}} & \qswap & \qw & \push{\ket{b}} \\
        \push{\ket{b}} & \qswap \qwx & \qw & \push{\ket{a}} \\
        ''')

pdf.save('swap.pdf')
pdf.rasterize('swap.png', scale=3)


