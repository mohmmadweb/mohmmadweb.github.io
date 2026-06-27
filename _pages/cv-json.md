---
layout: archive
title: "CV"
permalink: /cv-json/
author_profile: false
redirect_from:
  - /resume-json
---

{% include base_path %}

<link rel="stylesheet" href="{{ base_path }}/assets/css/cv-style.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<style>
  .archive {
    width: 92%;
    max-width: 1000px;
    margin: 0 auto;
    float: none;
    padding-right: 0;
  }

  @media (min-width: 80em) {
    .archive {
      width: 80%;
    }
  }
</style>

{% include cv-template.html %}

<div class="cv-download-links">
  <button type="button" id="cv-download-pdf-btn" class="btn btn--primary">
    <i class="fas fa-file-pdf" aria-hidden="true"></i> Download CV as PDF
  </button>
  <a href="{{ base_path }}/cv/" class="btn btn--inverse">View Markdown CV</a>
</div>

<script>
  (function () {
    var btn = document.getElementById("cv-download-pdf-btn");
    if (!btn) return;
    var originalTitle = document.title;
    btn.addEventListener("click", function () {
      document.title = "{{ site.author.name | default: 'CV' }} - CV";
      window.print();
      setTimeout(function () {
        document.title = originalTitle;
      }, 1000);
    });
  })();
</script>
