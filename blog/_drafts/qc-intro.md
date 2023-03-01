---
title: Introduction to Quantum Computing for Software Engineers.
tags: [Quantum]
style: default
color: primary
description: An introductory article on quantum computing for the sweet summer children. I try to tell you more than just "0 and 1 at the same time" and try to avoid math (at the expense of me puking) wherever possible. This is an adaptation of a talk I gave to my collegues at work.
date: 29-07-2021
updated: 29-07-2021
---

## Motivation

### Why though?

### Disclaimer

### Contents

This is a rough sketch of how the rest of this post will be like: 

- **What is Computation?** We attempt to extract the basic routines necessary for any programmable computer. 
- **Quantum Mechanics as a generalization of Classical Probability Theory.** We will understand the axioms of Quantum Mechanics necessary to build the above routines.
- **Current Landscape of the Field.** Contains a brief overview of the state of research and industry currently. 

## What is Computation?

How do we generally use a computer to solve any problem? A computer is a machine whose initial state and evolution we can program to reach to a desired gial. We first define the problem mathematically, enough to input it to a computer. We then need to program the inputs into the initial state of the computer. We also define the the evolution of the system (the algorithm to be followed) to get to the answer. We then need a way to read out the results, convert the final state of the computer into the answer we need. To summarize, we need

- A problem definition and a programmable system (computer). 
- A way to input the problems into the initial state of the computer. 
- A way to program the evolution of the system (what computer scientists call an algorithm). 
- A way to read out the results (measure the final state of the computer). 

**What is Quantum Computing?** The computers that you and I are used to are 'classical computers'. They are governed by the laws of classical physics (Newton's laws, etc.)
Once we know that the world around us is actually governed by the laws of Quantum Mechanics, we can try to build a machine that allows us to utilize quantum mechanics and has the above four features. That is what we call a 'quantum computers'. Quantum mechanics allows us to build [correlations](https://en.wikipedia.org/wiki/Correlation) that are not possible classically, which is the source of the (folklore for now) [quantum advantage](https://en.wikipedia.org/wiki/Quantum_supremacy). In the next section we will learn just enough quantum mechanics (at a very high level) to be able to do the above four things, and work with a quantum computer. 

## Quantum Mechanics From Classical Probability Theory

In this section, we will see how quantum mechanics is a generalization of classical probability theory. 

Consider a biased coin that when tossed can land in either heads or tails with probability $p_1$ and $p_2$ respectively. From the axioms of probability, we know that $p_1, p_2 \geq 0$ and $p_1 + p_2 = 1$. We can write the probability distribution as a [stochastic vector](https://en.wikipedia.org/wiki/Probability_vector) 
\[
\bar{p} := \begin{pmatrix}
p_1 \\
p_2 \end{pmatrix}.
\]
If we have two coins instead of one, the configuration space on a toss changes to head-head, head-tails, and so on. In this case, the probability distribution on the configuration space can be described by a 4-dimentional stochastic vector. Similarly, if we have larger, $n$-configuration space, the probability distribution on that configuration space can be described by a $n$ dimentional stochastic vector. 
Now suppose we bias the coin in some manner. For example, tamper with it such that the probability of heads changes somehow. How do we model this action mathematically? We basically transform one stochastic matrix to another, and this transformation is represented by a [stochastic matrix](https://en.wikipedia.org/wiki/Stochastic_matrix). 

In classical computers, the basic unit of computation is a bit. It is a classical object whose state can be described by a 2-dimentional stochastic vector. In deterministic scenarios the bit is described by a 2D vector, one of whose entries is 1. In probabilistic scenarios (randomized algorithms), a bit is described by some 2D stochastic vector. Analogously on quantum computers the basic unit on computation is a **qubit**. It is a quantum object (an object governed by the laws of qunatum mechanics), and its state is described by a 2D vector 
\[
\psi := \begin{pmatrix}
a_0 \\
a_1 \end{pmatrix}
\]
such that $a_i \in \mathbb{C}$ and $\abs{a_0}^2 + \abs{a_1}^2 = 1$ [1]. Here 



## Current Landscape 




[1] Apologies to the mathematicians and physicists out there who know that this is not *technically* correct. Only pure quantum states can be descibed in this manner. For details, refer to the excellent [lecture series](https://www.youtube.com/playlist?list=PLPH7f_7ZlzxQVx5jRjbfRGEzWY_upS5K6) by Prof. Frederic Schuller that covers the axioms of quantum mechanics mathematically and is very accessable. 
