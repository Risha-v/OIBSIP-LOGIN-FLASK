// Show/hide password functionality
const passwordFields = document.querySelectorAll('input[type="password"]');

passwordFields.forEach(function(field) {
  const toggleBtn = document.createElement('button');
  toggleBtn.type = 'button';
  toggleBtn.textContent = 'Show';
  toggleBtn.classList.add('password-toggle');

  field.parentNode.insertBefore(toggleBtn, field.nextSibling);

  toggleBtn.addEventListener('click', function() {
    if (field.type === 'password') {
      field.type = 'text';
      toggleBtn.textContent = 'Hide';
    } else {
      field.type = 'password';
      toggleBtn.textContent = 'Show';
    }
  });
});

// Disable form submission on Enter key
const forms = document.querySelectorAll('form');

forms.forEach(function(form) {
  form.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
      event.preventDefault();
    }
  });
});