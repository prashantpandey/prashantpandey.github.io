---
layout: page
title: talks
permalink: /talks/
description: Invited talks, conference presentations, and tutorials.
nav: true
nav_order: 3
---

<div class="talks">
{% assign talks = site.talks | sort: "date" | reverse %}
{% assign last_year = "" %}
<ul class="list-unstyled">
{% for talk in talks %}
  {% assign year = talk.date | date: "%Y" %}
  {% if year != last_year %}
    {% unless forloop.first %}</ul>{% endunless %}
    <h2 class="year">{{ year }}</h2>
    <ul class="list-unstyled">
    {% assign last_year = year %}
  {% endif %}
  <li class="mb-3">
    <strong>
      {% if talk.url %}<a href="{{ talk.url }}">{{ talk.title }}</a>{% else %}{{ talk.title }}{% endif %}
    </strong>
    <div class="text-muted">
      {{ talk.event }}{% if talk.location %} &middot; {{ talk.location }}{% endif %} &middot; {{ talk.date | date: "%b %Y" }}
    </div>
    {% if talk.slides or talk.video or talk.pdf %}
    <div>
      {% if talk.slides %}<a href="{{ talk.slides }}">[slides]</a> {% endif %}
      {% if talk.video %}<a href="{{ talk.video }}">[video]</a> {% endif %}
      {% if talk.pdf %}<a href="{{ talk.pdf }}">[pdf]</a>{% endif %}
    </div>
    {% endif %}
  </li>
{% endfor %}
</ul>
</div>
