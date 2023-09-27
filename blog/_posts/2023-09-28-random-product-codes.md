---
title: Nearest Neighbour Search via Random Product Codes
tags: [Algorithms, Lattice Cryptography]
style: default
color: primary
description: A brief introduction to random product codes with applications to nearest neighbour search.
date: 26-09-2023
updated: 26-09-2023
---

I recently started working on lattice based cryptography. I was recently reading a [paper](https://dl.acm.org/doi/10.5555/2884435.2884437) on nearest neighbour search, and came across a really beautiful idea to solve the problem using filtering. I decided to write it up here. I'll first describe the problem, then two aproaches used to solve it. Then I'll write about random product codes and the decoding algorithm for such codes.

### Nearest neighbour search 

Nearest neighbour search (NNS) is an important problem with applications in various fields such as data compression, machine learning, design of search engines and coding theory, among various others. We are given a list of $$n$$ vectors, $$V := \{v_{1}, v_{2}, \ldots v_{n}\} \subset \mathbb{R}^d$$ and we want to process this list such that given a query vector $$q \in \mathbb{R}^d$$, we can return the vector $$v^* \in V$$ that is closest to $$q$$ in time $$\mathcal{O}(n^\rho)$$ such that $$\rho \lt 1$$. (Note that the set $$V$$ and the points $$q,~v^*$$ can be from any metric space $$M(X, d)$$.) In the approximate NNS case, we have to return a vector that is within a distance $$c \cdot d(q,~v^*)$$ from $$v^*$$.

It is easy to see why this problem is important. The list $$V$$ could be a lattice, in which case this is the closest vector problem. Or $$V$$ could be a list of indexed web pages, and the closeness of two vectors in (say) Eucledian norm measures their similarity. Then efficient algorithms for (approx-)NNS would imply efficient algorithms for web search. 

### Locality sensitive hashing

Locality sensitive hashing (LSH) is exactly what it sounds like, you hash values using hash functions that are sensitive to locality. That is, if points are close (local or in a locality), the probability of collission is higher. 

### Locality sensitive filtering

This is a slight modification of LSH. 

### SVP, CVP


### Random Product Codes

For the purpose described above, we need two properties from the the chosen code: it must be efficiently decodable, so that we are able to quickly determine the relevant buckets to which a query vector $q$ belongs; and that it should approximately behave like a fully random code over a sphere when we consider the probabilities of collission between any two vectors on the sphere. 

Consider the code on a sphere formed by the product of random codes on smaller spheres. Such a code has both of these properties. Formally, such a code is described as follows. 

**Definition. (Random Product Codes:)** Suppose $$m = \mathcal{O}(\mathrm{polylog}n)$$, and $$n = m \cdot b$$ for some integer $$b_$$, called the *block size*. The distribution $$\mathcal{R}_{n, m, B}$$ on subsets of $$\mathbb{R}^n$$ of size $$M = B^m$$ is defined as the distribution of codes $C$ of the form 

$$
    C := Q \cdot (C_{1}, C_{2}, \ldots, C_{m}),
$$

where $Q$ is a uniformly random rotation over $\mathbb{R}^n$ and the subcodes $$C_i \subset \sqrt{\frac{1}{m}} \cdot \mathcal{S}^{b-1}$$ for $$i \in [m]$$ are sets of $$B$$ uniformly random and independently sampled vectors over the sphere $$\sqrt{\frac{1}{m}}\cdot \mathcal{S}^{b-1}$$.

Note that there is a slight abuse of notation, informally each codeword in $$C$$ is formed as follows. Take come vector from each $$C_i$$ and stack them. It gives us a vector of size $$n$$. Doing this for all vectors in all of $C_i$'s gives us a set of $$M$$ vectors of size $$n$$, such that each vector is made of of $$m$$ blocks of $$b$$-sized vectors. Then apply the rotation $$Q$$ to each of the larger vectors, to get the final set of codewords. 

#### Efficient Decoding Algorithm for RPC


