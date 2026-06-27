/* Client-side filter buttons for the Academic Career and Industrial
   Experiences pages. Pure front-end filtering of cards already rendered
   by Jekyll - no endpoints, data, or page structure are touched. */

document.addEventListener('DOMContentLoaded', function () {
  var bars = document.querySelectorAll('.experience-filter-bar');

  function normalize(v) {
    return (v || '').trim().toLowerCase();
  }

  bars.forEach(function (bar) {
    var timeline = bar.nextElementSibling;
    if (!timeline || !timeline.classList.contains('experiences-timeline')) return;

    var groups = bar.querySelectorAll('.experience-filter-group');
    var active = {};

    function applyFilter() {
      var cards = timeline.querySelectorAll('.experience-card');
      var anyVisible = false;

      cards.forEach(function (card) {
        var visible = true;
        Object.keys(active).forEach(function (field) {
          var want = normalize(active[field]);
          if (!want) return;
          var actual = normalize(card.getAttribute('data-' + field));
          if (actual !== want) visible = false;
        });

        var item = card.closest('.list__item, .archive__item') || card.parentElement;
        item.style.display = visible ? '' : 'none';
        if (visible) anyVisible = true;
      });

      var headings = timeline.querySelectorAll('.experience-year');
      headings.forEach(function (heading) {
        var node = heading.nextElementSibling;
        var hasVisible = false;
        while (node && !node.classList.contains('experience-year')) {
          if (node.style.display !== 'none') hasVisible = true;
          node = node.nextElementSibling;
        }
        heading.style.display = hasVisible ? '' : 'none';
      });

      var emptyMsg = timeline.querySelector('.experience-filter-empty');
      if (!emptyMsg) {
        emptyMsg = document.createElement('p');
        emptyMsg.className = 'experience-filter-empty no-positions';
        emptyMsg.textContent = 'No entries match the selected filters.';
        timeline.appendChild(emptyMsg);
      }
      emptyMsg.style.display = anyVisible ? 'none' : '';
    }

    groups.forEach(function (group) {
      var field = group.getAttribute('data-filter-field');
      active[field] = '';

      group.querySelectorAll('.experience-filter-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
          group.querySelectorAll('.experience-filter-btn').forEach(function (b) {
            b.classList.remove('is-active');
          });
          btn.classList.add('is-active');
          active[field] = btn.getAttribute('data-filter-value') || '';
          applyFilter();
        });
      });
    });
  });
});
