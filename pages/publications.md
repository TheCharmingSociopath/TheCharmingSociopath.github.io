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
        <li> <span style="color: black;"> {{ item.title }} </span>
        </li>
        <small> with
        {% for name in item.coauthors %}
        {% if name.url != blank %}
        <a href="{{ name.url }}" target="_blank">{{ name.name }}</a>{% if forloop.last %}.{% else %}, {% endif %}
        {% else %}
        {{ name.name }}{% if forloop.last %}.{% else %}, {% endif %}
        {% endif %}
        {% endfor %}
        </small> <br/>
        <small> <span> {% if item.where != blank %} {% for venue in item.where %} <i class="fa fa-book"></i> {{ venue.name }} &emsp; {% endfor %} {% endif %}
        <i class="fa fa-book"></i> <a href="{{ item.arxiv }}" target="_blank"> arXiv </a> </span></small>
        {% endfor %}
    </ul>
</div>

---

### Academic Writings

- My MS thesis can be found [here](../assets/documents/thesis.pdf) <br/>
- [Notes](../assets/documents/Adiabatic Quantum Computing and Optimization.pdf) on Adiabatic Quantum Computing and Optimization <br/>
- Some [notes](../assets/documents/Open_Quantum_Systems_Project.pdf) on analysing the master equation for qubit systems. <br/>
- My introductory [notes](../assets/documents/Quantum_Notes.pdf) on quantum computing for 2018. <br/>
- A [video](https://youtu.be/zFyy2H_7oOk) introducing PCPs from a hardness of approximation perspective.  <br/>
- [Modelling the stock market using game theory](../assets/documents/Modelling%20the%20stock%20market%20using%20game%20theory.pdf) <br/>
