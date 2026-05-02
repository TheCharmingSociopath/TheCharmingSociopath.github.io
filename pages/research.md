---
layout: default
title: Research
permalink: /research/
weight: 1
---

### Publications

{% assign pubs = site.data.publications %}

<script>
  function copyBibtex(bibtexId, buttonEl) {
    var bibtexEl = document.getElementById(bibtexId);
    if (!bibtexEl || !buttonEl) {
      return;
    }

    var bibtexText = bibtexEl.textContent || bibtexEl.innerText || "";

    var setCopiedState = function () {
      if (!buttonEl.dataset.originalHtml) {
        buttonEl.dataset.originalHtml = buttonEl.innerHTML;
      }
      buttonEl.innerHTML = '<i class="fa-solid fa-check" aria-hidden="true"></i>';
      buttonEl.setAttribute("title", "Copied");
      buttonEl.setAttribute("aria-label", "Copied");
      window.setTimeout(function () {
        buttonEl.innerHTML = buttonEl.dataset.originalHtml;
        buttonEl.setAttribute("title", "Copy BibTeX");
        buttonEl.setAttribute("aria-label", "Copy BibTeX");
      }, 1200);
    };

    var fallbackCopy = function () {
      var temp = document.createElement("textarea");
      temp.value = bibtexText;
      temp.setAttribute("readonly", "");
      temp.style.position = "absolute";
      temp.style.left = "-9999px";
      document.body.appendChild(temp);
      temp.select();
      document.execCommand("copy");
      document.body.removeChild(temp);
      setCopiedState();
    };

    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(bibtexText).then(function () {
        setCopiedState();
      }).catch(function () {
        fallbackCopy();
      });
      return;
    }

    fallbackCopy();
  }
</script>

<div>
    <ul style="margin-top: 30px;">
        {% for item in pubs %}
        <li style="margin-top: 30px;"> <span style="color: black;"> {{ item.title }} </span></li>
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
        {% if item.arxiv != blank %}<i class="fa fa-book"></i> <a href="{{ item.arxiv }}" target="_blank"> arXiv </a> &emsp; {% endif %}
        {% if item.slides != blank %}<i class="fa fa-display"></i> <a href="{{ item.slides }}" target="_blank"> slides </a> {% endif %}</span>
        {% if item.bibtex != blank %}
        {% assign bibtex_id = item.id | default: forloop.index | slugify %}
        <details><summary>BibTeX</summary>
        <button type="button" onclick="copyBibtex('bibtex-{{ bibtex_id }}', this)" title="Copy BibTeX" aria-label="Copy BibTeX" style="font-size: 0.85rem; border: none; background: transparent; cursor: pointer; padding: 0 0.15rem;"><i class="fa-regular fa-copy" aria-hidden="true"></i></button>
        <pre id="bibtex-{{ bibtex_id }}" style="white-space: pre-wrap;">{{ item.bibtex | strip | escape }}</pre>
        </details>
        {% endif %} 
        <details><summary>Abstract</summary> {{ item.abstract }} </details></small>
        {% endfor %}
    </ul>
</div>

---

### Academic Writings

- Notes on [lattices](../assets/documents/Lattice_Notes.pdf) I helped write. This was when I was a teaching assistant for advanced algorithms (lattice algorithms) course taught by [Divesh](https://sites.google.com/site/diveshhomepage/). You probably also wanna look at Oded Regev's [notes](https://cims.nyu.edu/~regev/teaching/lattices_fall_2009/).
- [Notes](../assets/documents/Pseudoentanglement.pdf) on Quantum Pseudoentanglement and pseudorandom quantum states I wrote with my friends from CQT.
- Some [notes](../assets/documents/ANN25.pdf) on Approximate Nearest Neighbour Search I worked on with my friends from NUS.
- My MS [thesis](../assets/documents/thesis.pdf), "Quantum Algorithms for Regularized Least Squares".
- [Notes](../assets/documents/Adiabatic Quantum Computing and Optimization.pdf) on Adiabatic Quantum Computing and Optimization.
- Some [notes](../assets/documents/Open_Quantum_Systems_Project.pdf) on analysing the master equation for qubit systems.
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
        <span> <i class="fa-solid fa-location-dot"></i> {{ item.where }} &emsp; <i class="fa fa-clock"></i> {{ item.date }} </span>
        <details><summary>Abstract</summary> {{ item.abstract }} </details></small>
        {% endfor %}
    </ul>
</div>


---


### Academic Service

- 2025: Sub-reviewer for AQIS 2025; AsiaCrypt 2025; FSTTCS 2025; TCC 2025; Eurocrypt 2025.
