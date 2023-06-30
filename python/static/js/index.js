document.addEventListener('DOMContentLoaded', () => {
    // Select the form element
    const form = document.getElementById('password-form');
  
    // Function to handle form submission
    const handleSubmit = (event) => {
      event.preventDefault(); // Prevent default form submission behavior
  
      // Retrieve form values
      const name = document.getElementById('name').value;
      const currentDate = document.getElementById('currentDate').value;
      const allMin = document.getElementsByName('allMin')[0].checked;
      const allMaj = document.getElementsByName('allMaj')[0].checked;
      const capital = document.getElementsByName('capital')[0].checked;
      const noAccent = document.getElementsByName('noAccent')[0].checked;
      const leet = document.getElementsByName('leet')[0].checked;
      const dateNumbers = document.getElementsByName('dateNumbers')[0].checked;
      const humanMonth = document.getElementsByName('humanMonth')[0].checked;
      const twoDigitYear = document.getElementsByName('twoDigitYear')[0].checked;
      const fourDigitYear = document.getElementsByName('fourDigitYear')[0].checked;
      const language = document.getElementsByName('language')[0].checked;
      const commonSpecialChars = document.getElementsByName('commonSpecialChars')[0].checked;
      const allSpecialChars = document.getElementsByName('allSpecialChars')[0].checked;
      const maxSpecialChars = document.getElementById('maxSpecialChars').value;
      // Retrieve the current date value
  
      // Create a data object with the form values
      const data = {
        name,
        currentDate,
        optionWord: {
          allMin,
          allMaj,
          capital,
          noAccent,
          leet,
        },
        optionDate: {
          dateNumbers,
          humanMonth,
          twoDigitYear,
          fourDigitYear,
          language,
        },
        optionSpecialChars: {
          commonSpecialChars,
          allSpecialChars,
          maxSpecialChars,
        },
      };
      console.log(data);
  
      // Send the form data to your Flask app using AJAX
      fetch('/results', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
        .then(response => response.json())
        .then(result => {
          // Handle the response from your Flask app
          // You can update the results div with the returned data
          console.log(result);
          const resultsDiv = document.getElementById('results');
          resultsDiv.innerHTML = result.password.join(', ');
        })
        .catch(error => {
          console.error('Error:', error.message);
        });
    };
  
    // Add form submission event listener
    form.addEventListener('submit', handleSubmit);
  });
  