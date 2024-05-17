document.addEventListener('DOMContentLoaded', () => {
  const navItems = document.querySelectorAll('#category-nav li');
  const jarsList = document.getElementById('jars-list');
  const jarEntries = document.querySelectorAll('.jar-entry');

  function showCategory(category) {
      jarEntries.forEach(entry => {
          if (entry.getAttribute('data-category') === category) {
              entry.classList.add('show');
          } else {
              entry.classList.remove('show');
          }
      });
  }

  navItems.forEach(item => {
      item.addEventListener('click', () => {
          // Remove active class from all nav items
          navItems.forEach(nav => nav.classList.remove('active'));
          // Add active class to the clicked item
          item.classList.add('active');

          // Get the category from the clicked item
          const category = item.getAttribute('data-category');

          // Hide jars list during transition
          jarsList.classList.remove('show');

          setTimeout(() => {
              showCategory(category);

              // Show jars list after transition
              setTimeout(() => {
                  jarsList.classList.add('show');
              }, 50);
          }, 400); // Match the duration of the opacity transition
      });
  });

  // Trigger click on the first category to display it by default
  navItems[0].click();
});
