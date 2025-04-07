---
layout: default
title: Publications
permalink: /publications/
weight: 1
---

### Publications

{% assign pubs = site.data.publications %}

<div>
    <ul style="margin-top: 30px;">
        {% for item in pubs %}
        <li> <span style="color: black;"> {{ item.title }} </span></li>
        <small> with
        {% for name in item.coauthors %}
        {% if name.url != blank %}
        <a href="{{ name.url }}" target="_blank">{{ name.name }}</a>{% if forloop.last %}.{% else %}, {% endif %}
        {% else %}
        {{ name.name }}{% if forloop.last %}.{% else %}, {% endif %}
        {% endif %}
        {% endfor %}
        <br/>
        <span> {% if item.where != blank %} {% for venue in item.where %} <i class="fa fa-book"></i> {{ venue.name }} &emsp; {% endfor %} {% endif %}
        <i class="fa fa-book"></i> <a href="{{ item.arxiv }}" target="_blank"> arXiv </a> </span>
        <details><summary>Abstract</summary> {{ item.abstract }} </details></small>
        {% endfor %}
    </ul>
</div>

---

### Academic Writings

- Notes on [lattices](../assets/documents/Lattice_Notes.pdf) I helped write. This was when I was a teaching assistant for advanced algorithms (lattice algorithms) course taught by [Divesh](https://sites.google.com/site/diveshhomepage/). You probably also wanna look at Oded Regev's [notes](https://cims.nyu.edu/~regev/teaching/lattices_fall_2009/).
- Some [notes](../assets/documents/ANN25.pdf) on Approximate Nearest Neighbour Search I worked on with my friends from NUS.
- My MS [thesis](../assets/documents/thesis.pdf), "Quantum Algorithms for Regularized Least Squares".
- [Notes](../assets/documents/Adiabatic Quantum Computing and Optimization.pdf) on Adiabatic Quantum Computing and Optimization.
- Some [notes](../assets/documents/Open_Quantum_Systems_Project.pdf) on analysing the master equation for qubit systems.
- Some introductory [notes](../assets/documents/Quantum_Notes.pdf) on quantum computing for 2018.
- A [video](https://youtu.be/zFyy2H_7oOk) introducing PCPs from a hardness of approximation perspective. You should probably watch Ryan O'Donnell's [lecture](https://www.youtube.com/playlist?list=PLm3J0oaFux3ZYpFLwwrlv_EHH9wtH6pnX).
- [Modelling the stock market using game theory](../assets/documents/Modelling%20the%20stock%20market%20using%20game%20theory.pdf).

---

### Talks

{% assign talks = site.data.talks %}

<div>
    <ul style="margin-top: 30px;">
        {% for item in talks %}
        <li> <span style="color: black;"> {{ item.title }} </span></li>
        <small>
        <span> <i class="fa-solid fa-location-dot"></i> {{ item.where }}, {{ item.location }} &emsp; <i class="fa fa-clock"></i> {{ item.date }} </span>
        <details><summary>Abstract</summary> {{ item.abstract }} </details></small>
        {% endfor %}
    </ul>
</div>
