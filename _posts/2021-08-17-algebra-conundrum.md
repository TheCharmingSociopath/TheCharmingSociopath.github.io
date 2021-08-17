---
title: The Algebra Conundrum
tags: [Math, TIL]
style: default
color: primary
description: Is it a bird? Is it also that bird? What is an `Algebra'?
date: 17-08-2021
updated: 17-08-2021
---

I was reading a paper which mentioned *We may view [a specific] ring as an algebra over the real or over the complex numbers*, and I realised I did not know formally what an *Algebra* was. So thought I'll clear it up for myself. Turns out the word is a bit overused.

#### Algebraic Structures

> An Algebraic Structure is a set $$A$$, along with some operations (functions) on $$A$$ of finite arity and a finite set of axioms that the operations must satisfy.

Examples of algebraic structures are structures of types Groups, Rings, Lattices, Modules and [wait for it...] Algebras.

#### Algebra over a field

That last type of Algebraic Structure, known as an *Algebra* is an Algebra over a field (which, it turns out, the paper I was reading actually meant). It is defined as follows:

Let $$ \mathcal{F} $$ be a field and let $$A$$ be a vector space over $$\mathcal{F}$$ along with a binary operation $$\cdot : A \times A \to A$$. $$A$$ is an algebra over $$\mathcal{F}$$ if $$\forall x, y, z \in A, \forall a,b \in \mathcal{F}$$,
- Right Distributivity of $$\cdot$$ --  $$(x + y) \cdot z = x \cdot z + y \cdot z $$
- Left Distributivity of $$\cdot$$ --   $$z \cdot (x + y) = z \cdot x + z \cdot y $$
- Compatibility with Scalars --    $$(ax)\cdot (by) = (ab)(x \cdot y)$$

The above three axioms basically mean that the binary operation $$\cdot$$ is bilinear.

It turns out these aren't the only contexts in which the term is used. Here is a text snippet from Wikipedia:

> The properties of specific algebraic structures are studied in *abstract algebra*. The general theory of algebraic structures has been formalized in *universal algebra*. The language of *category theory* is used to express and study relationships between different classes of algebraic and non-algebraic objects.

Mathematicians are clearly great at naming things.

### References

1. [Wikipedia](https://en.wikipedia.org/wiki/Algebraic_structure)


