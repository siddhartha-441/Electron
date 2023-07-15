document.addEventListener('DOMContentLoaded', function() {
  var dropdowns = document.querySelectorAll('.dropdown');
  dropdowns.forEach(function(dropdown) {
    dropdown.addEventListener('click', function(event) {
      event.stopPropagation();
      dropdown.querySelector('.dropdown-menu').classList.toggle('show');
    });
  });

  document.addEventListener('click', function() {
    dropdowns.forEach(function(dropdown) {
      dropdown.querySelector('.dropdown-menu').classList.remove('show');
    });
  });
});
