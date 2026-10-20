---
layout: page
title: projects
permalink: /projects/
description: Research projects on high-performance data structures and large-scale data systems.
nav: true
nav_order: 5
display_categories: [research]
horizontal: false
compact: true
---

<!-- pages/projects.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.compact %}
  <ul class="projects-compact">
    {% for project in sorted_projects %}
      {% include projects_compact.liquid %}
    {% endfor %}
  </ul>
  {% elsif page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.compact %}

  <ul class="projects-compact">
    {% for project in sorted_projects %}
      {% include projects_compact.liquid %}
    {% endfor %}
  </ul>
  {% elsif page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>

<style>
  .projects-compact { list-style: none; padding: 0; margin: 0 0 2rem; }
  .project-compact { border-bottom: 1px solid var(--global-divider-color); }
  .project-compact:last-child { border-bottom: none; }
  .project-compact a {
    display: flex; gap: 1rem; align-items: center;
    padding: 0.85rem 0.5rem; color: var(--global-text-color); text-decoration: none;
    border-radius: 6px; transition: background-color 0.15s;
  }
  .project-compact a:hover { background-color: var(--global-card-bg-color); }
  .project-compact a:hover .project-compact-title { color: var(--global-theme-color); }
  .project-compact-thumb { flex: 0 0 auto; width: 96px; height: 64px; object-fit: cover; border-radius: 4px; }
  .project-compact-text { display: flex; flex-direction: column; min-width: 0; }
  .project-compact-title { font-weight: 600; font-size: 1.05rem; line-height: 1.3; }
  .project-compact-desc { color: var(--global-text-color-light); font-size: 0.9rem; margin-top: 0.2rem; }
  @media (max-width: 576px) { .project-compact-thumb { width: 64px; height: 48px; } }
</style>
