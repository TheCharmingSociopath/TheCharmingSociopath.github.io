---
layout: default
title: Bookshelf
weight: 2
permalink: /reading/
---

{% assign meta = site.data.books['meta'] %}
{% assign books_read = site.data.books['books_read'] %}
{% assign wishlist = site.data.books['wishlist'] %}
{% assign shorts = site.data.books['short_stories_to_read'] %}

---

<!-- <bibtex src="/assets/references/papers-i-love.bib"></bibtex> -->

<div>
    <div style="text-align: center; margin: 25px;"> <h5> Books I'm Currently Reading </h5> </div>
    <ul style="margin-top: 30px;">
        {% for item in meta.currently_reading %}
        <li> {{ item.title }}<small>, by {{ item.author }} </small></li>
        {% if item.stars != blank %}
        <span><small>{% for i in (1..item.stars) %}&#9733;{% endfor %}</small></span><br/>
        {% endif %}
        {% if item.comments != blank %}
        <span><small>{{ item.comments }}</small></span>
        {% endif %}
        <br/>
        {% endfor %}
    </ul>
</div>

---

<!-- <div> -->
<!--     <div style="text-align: center; margin: 25px;"> <h5> Papers I love </h5> </div> -->
<!--     <div id="bibtex_display"></div> -->
<!-- </div> -->
<!--  -->
<!-- --- -->

<div>
    <div style="text-align: center; margin: 25px;"> <h5> Some Books I've Read in the Past </h5> </div>
    <ul style="margin-top: 30px;">
        {% for item in books_read %}
        {% if item.series == blank %}
        <li> {{ item.title }}<small>, by {{ item.author }} </small></li>
        {% if item.comments != blank %}
        <span><small>{{ item.comments }}</small></span>
        {% endif %}
        {% if item.stars != blank %}
        <div><small>{% for i in (1..item.stars) %}&#9733;{% endfor %}</small></div>
        {% endif %}

        {% else %}
        <li> {{ item.series }}<small>, by {{ item.author }} </small></li>
        {% if item.stars != blank %}
        <span><small>{% for i in (1..item.stars) %}&#9733;{% endfor %}</small></span>
        {% endif %}
        {% if item.comments != blank %}
        <span><small>{{ item.comments }}</small></span>
        {% endif %}
        <ul>
            {% for i in item.titles %}
            <li> {{ i }} </li>
            {% endfor %}
        </ul>
        {% endif %}
        <br/>
        {% endfor %}
    </ul>
</div>

