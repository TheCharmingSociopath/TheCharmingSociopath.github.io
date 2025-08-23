---
layout: post
title: Operator Inverse as an Integral and the Sylvester Equation
tags: [Math, Linear Agebra, Functional Analysis]
style: default
color: primary
description: Matrices and Operators as integrals. 
date: 23-08-2025
updated: 23-08-2025
---

I saw a paper by Somma et. al. [Quantum algorithm for linear matrix equations](https://arxiv.org/abs/2508.02822) for solving the [Sylvester equation](https://en.wikipedia.org/wiki/Sylvester_equation). I did not immediately recall that one can write matrix inverse as an integral, so I thought I will recall and write it up here, a short proof of equation 9 in their paper. We assume that the matrix $A$ is positive definite and with to write $A^{-1}$ as an integral. We also mention a simple solution to the Sylvester equation when $A,B \gt 0$.

Let's start with scalars first. For a real number $a>0$, we have that

$$\int_{0}^{\infty} e^{-at} dt = \Big[-\frac{1}{a} e^{-at}\Big]_{0}^{\infty} = \frac{1}{a}.$$

So we have an identity $a^{-1}=\int_0^\infty e^{-at} dt$. We can essentially extend this identity for positive definite matrices. We know that for any square matrix $A$,

$$
e^{-tA} := \sum_{k=0}^{\infty}\frac{(-t)^k}{k!}A^k.
$$

First check that this is well defined. The series converges for every $t$ because the scalar exponential series is absolutely convergent, and matrix norms are sub-multiplicative.

Now notice that

$$
  \frac{d}{dt}e^{-tA}=-\sum_{k=1}^{\infty}\frac{(-t)^{k-1}}{(k-1)!}A^{k}=-A e^{-tA}.
$$

Also notice that $A$ commutes with any polynomial in $A$ (since they diagonalize in the same basis), hence with its exponential also.

By our assumption, all eigenvalues of $A$ are positive, and therefore $\|e^{-tA}\|\to 0$ as $t\to\infty$. Now integrate the derivative identity above

$$
\frac{d}{dt}e^{-tA}=-A e^{-tA}
$$

from $0$ to $T$ to get

$$
e^{-TA}-I = -A\int_{0}^{T} e^{-tA} dt.
$$

Thus

$$
A\int_{0}^{T} e^{-tA} dt = I - e^{-TA}.
$$

Let $T\to\infty$. Because $e^{-TA}\to 0$, we get that

$$
A\left(\int_{0}^{\infty} e^{-tA} dt\right)=I.
$$

Since $A$ commutes with $e^{-tA}$, the same computation on the right gives

$$
\left(\int_{0}^{\infty} e^{-tA} dt\right)A=I.
$$

Therefore

$$
\boxed{ \quad A^{-1}  =  \int_{0}^{\infty} e^{-tA} dt \quad }.
$$

Notice that in the above we only used the fact that all the eigenvalues of $A$ all have positive real part (so that the integral converges). Therefore, this result can extend to all such matrices.

---

The Sylvester equation can be thought of as a linear operator acting on $X$ that acts as $\mathcal{L}(X) = AX + XB$. It has a unique solution iff the spectra of $A$ and $-B$ are disjoint (check wikipedia). In the above case where $A$ and $B$ are PSD (or they have positive real spectra), one can obtain a closed form solution to the inverse of $\mathcal{L}$ (technically I should be writing $\mathcal{L}_{A,B}$) (I thank ChatGPT for this idea 😛.) Define

$$
X^*:=\int_{0}^{\infty} e^{-tA} C e^{-tB} dt.
$$

Let $Y(t):=e^{-tA} C e^{-tB}$. Taking the derivative, we get (recall that $A,B$ commute with their exponentials)

$$
Y'(t) = -A Y(t) - Y(t) B.
$$

Integrate from $0$ to $T$ to get

$$
Y(T)-Y(0) = -\int_{0}^{T}\big(A Y(t)+Y(t)B\big) dt.
$$

Because of our assumption on the spectra of $A$ and $B$, $Y(0)=C$ and $Y(T)\to 0$. Thus

$$
C=\int_{0}^{\infty}\big(A Y(t)+Y(t)B\big) dt
 = A\!\left(\int_{0}^{\infty}\!Y(t) dt\right)+\left(\int_{0}^{\infty}\!Y(t) dt\right)\!B
 = A X^* + X^* B.
$$

Therefore $X^*=\mathcal{L}^{-1}(C)$ is the "operator inverse as an integral” for the operator $X\mapsto AX+XB$.

Notice that one can always truncate the integral and discretize it, and then use Hamiltonian simulation to construct block encodings of the solution.
