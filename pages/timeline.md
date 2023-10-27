---
layout: default
title: Timeline
permalink: /timeline/
weight: 3
---

<div class="row">
<div class="col mt-4">
  <div class="timeline-body">
    {% for item in site.data.timeline %}
      <div class="timeline-item">
        <div class="content">
          <h3>{{ item.title }}</h3>
          <h6 class="date">{{ item.from }} — {{ item.to }}</h6>
            {% for desc in item.description %}
            - {{ desc }} <br/>
            {% endfor %}
        </div>
      </div>
    {% endfor %}
  </div>
</div>
</div>
