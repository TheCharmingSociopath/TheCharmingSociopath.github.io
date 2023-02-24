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



## Current Landscape 
