## Introduction

This was developed as a portfolio website, ideal for blogging projects as well as hosting notes.
The theme (most of the CSS) was taken from: [YoussefRaafatNasry/portfolYOU](https://github.com/YoussefRaafatNasry/portfolYOU) and the LICENCE has been attached as is.

## How to set up

- Install ruby (Arch): `sudo pacman -S ruby2.7`
- Add the following to your .zshrc
    ```
        # Install Ruby Gems to ~/gems
        export GEM_HOME="$HOME/gems"
        export PATH="$HOME/gems/bin:$PATH"
        export PATH="$HOME/.local/share/gem/ruby/3.0.0/bin:$PATH"
    ```
- `bundle-2.7 install`
- `bundle-2.7 exec jekyll serve`
- Navigate to `http://127.0.0.1:4000/` and check out the page.


Note that we use ruby 2.7 because GitHub pages isn't compatible with ruby 3.

#### I do not remember why this was here :P

```
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/MathJax.js?config=TeX-MML-AM_CHTML%2CSafe.js&amp;ver=5.5.3" id="mathjax-js"></script>
```


