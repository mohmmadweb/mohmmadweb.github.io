/* Shared lightbox used by the about-page photo gallery, industrial-experience
   media galleries, and the honors-and-awards "See document" buttons. */

function openModal(src) {
  var modal = document.getElementById('imageModal');
  var img = document.getElementById('modalImage');
  if (!modal || !img) return;
  img.src = src;
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  var modal = document.getElementById('imageModal');
  if (!modal) return;
  modal.style.display = 'none';
  document.body.style.overflow = 'auto';
}

function openDocumentModal(src) {
  openModal(src);
}

document.addEventListener('DOMContentLoaded', function () {
  var modal = document.getElementById('imageModal');
  if (!modal) return;

  modal.addEventListener('click', function (e) {
    if (e.target === modal) {
      closeModal();
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      closeModal();
    }
  });
});
