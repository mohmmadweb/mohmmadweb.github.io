---
layout: archive
title: "Academic Career"
permalink: /academic-career/
author_profile: false
---

{% include base_path %}

<div class="experiences-grid">
  {% assign sorted_experiences = site.academic-career | sort: "end_date" | reverse %}
  {% for post in sorted_experiences %}
    {% include archive-single-academic-career.html %}
  {% endfor %}
</div>