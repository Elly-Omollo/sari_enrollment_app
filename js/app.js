       

var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    //... and fix the Previous/Next buttons:
    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "Submit";
    } else {
        document.getElementById("nextBtn").innerHTML = "Next";
    }


}

function nextPrev(n) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form...
    if (currentTab >= x.length) {
        // ... the form gets submitted:
        document.getElementById("regForm").submit();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function validateForm() {
// This function deals with validation of the form fields
var x, y, i, valid = true;
x = document.getElementsByClassName("tab");
y = x[currentTab].getElementsByTagName("input");
// A loop that checks every input field in the current tab:
for (i = 0; i < y.length; i++) {
// If a field is empty...
if (y[i].value == "") {
// add an "invalid" class to the field:
y[i].className += " invalid";
// and set the current valid status to false
valid = false;
}
}



// If the valid status is true, mark the step as finished and valid:
if (valid) {
document.getElementsByClassName("step")[currentTab].className += " finish";
}
return valid; // return the valid status
}
//DARK-MODE TOGGLE
function myFunction1() {
    var form = document.getElementById("regForm");
    var element = document.body;

    form.classList.toggle("dark-mode");
    element.classList.toggle("dark-mode");
}

// preventing entering numbers for names
    function preventNumbers(event) {
        var input = event.target;
        var value = input.value;
        var newValue = value.replace(/[0-9]/g, ''); // Remove numeric characters

        if (newValue !== value) {
            input.value = newValue;
        }
    }

//updating dates 
window.onload = function() {
    var dateFields = document.querySelectorAll('input[type="date"].auto-fill-today');
    var today = new Date();
    var formattedDate = today.toISOString().slice(0, 10);

    dateFields.forEach(function(field) {
        field.value = formattedDate;
        field.max = formattedDate;
        field.min = formattedDate;
    });
};


function restrictInput(event) {
    var input = event.target;
    var value = input.value;
    var newValue = value.replace(/\D/g, ''); // Remove non-numeric characters

    if (newValue !== value) {
        input.value = newValue;
    }
}


function autoSelectCheckboxes() {
    var answer1 = document.getElementById('answer1').value;
    var answer2 = document.getElementById('answer2').value;
    var answer3 = document.getElementById('answer3').value;
    var answer4 = document.getElementById('answer4').value;
    var answer5 = document.getElementById('answer5').value;

    // Clear previous selections
    document.getElementById('checkbox1').checked = false;
    document.getElementById('checkbox2').checked = false;
    document.getElementById('checkbox3').checked = false;

    // Auto-select checkboxes based on previous answers
    if ((answer1 === '1' || answer2 === '1') && answer3 === '1' && answer4 === '1' && answer5 === '1') {
        document.getElementById('checkbox1').checked = true;
    } else if  ((answer1 === '1' || answer2 === '1') && answer3 === '1' && answer4 === '1' && answer5 === '2') {
        document.getElementById('checkbox3').checked = true;
    }else if (answer1 === '1' && answer2 === '1' && answer3 === '1' && answer4 === '1' && answer5 === '1'){
        document.getElementById('checkbox2').checked = true;
    }


}

//AUTO APPEND SYMBOLS
  
function appendSymbols() {
    //var rateInput = document.getElementById('');
    var temperatureInput = document.getElementById('temperature');
    var ageInput = document.getElementById('age');
    var yearsInput = document.getElementById('years');
   

    //appendPercentageSymbol(rateInput);
    //appendDegreeSymbol(temperatureInput);
    appendMonthsSymbol(ageInput);
    appendYearSymbol(yearsInput);
    // You can add more functions for other input fields here
}
/*
function appendPercentageSymbol(inputField) {
    var value = inputField.value.trim();
    if (value !== '') {
        if (!value.endsWith('%')) {
            inputField.value = value + '%';
        }
    }
}
*/
function appendDegreeSymbol(inputField) {
    var value = inputField.value.trim();
    if (value !== '') {
        if (!value.endsWith('°C')) {
            inputField.value = value + '°C';
        }
    }
}

function appendMonthsSymbol(inputField) {
    var value = inputField.value.trim();
    if (value !== '') {
        if (!value.endsWith(' months old')) {
            inputField.value = value + ' months old';
        }
    }
}

function appendYearSymbol(inputField) {
    var value = inputField.value.trim();
    if (value !== '') {
        if (!value.endsWith(' years old')) {
            inputField.value = value + ' years old';
        }
    }
}