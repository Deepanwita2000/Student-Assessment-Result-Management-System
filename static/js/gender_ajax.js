const maleCheckbox = document.getElementById('maleCheckbox');
const femaleCheckbox = document.getElementById('femaleCheckbox');
const displayInput = document.getElementById('displayValue');

  // Function to update the display input
  function updateGenderDisplay() {
    if (maleCheckbox.checked) {
      displayInput.value = maleCheckbox.value;
    } else if (femaleCheckbox.checked) {
      displayInput.value = femaleCheckbox.value;
    } else {
      displayInput.value = ''; // Clear if neither is checked
    }
  }

  // Add event listeners to the checkboxes
  maleCheckbox.addEventListener('change', updateGenderDisplay);
  femaleCheckbox.addEventListener('change', updateGenderDisplay);



