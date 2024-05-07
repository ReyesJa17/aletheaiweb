document.addEventListener('DOMContentLoaded', function() {
  const header = document.querySelector('header');
  const menuToggle = document.querySelector('.menu-toggle');
  const mobileMenu = document.querySelector('.mobile-menu');

  menuToggle.addEventListener('click', function() {
    mobileMenu.classList.toggle('open');
  });

  let lastScrollPosition = 0;

  window.addEventListener('scroll', function() {
    const currentScrollPosition = window.pageYOffset;

    if (currentScrollPosition > lastScrollPosition) {
      // Scrolling down
      header.classList.add('hide');
    } else {
      // Scrolling up
      header.classList.remove('hide');
    }

    lastScrollPosition = currentScrollPosition;
  });
});