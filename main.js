let num1 = null;
let num2 = null; 
let operation = "";
let currentInput = "";

const field = document.querySelector("#field"); 
const reset = document.querySelector("#reset"); 
const digits = document.querySelectorAll(".digit");
const operations = document.querySelectorAll(".operation");

field.textContent = "";


function add(a, b) {
    return a + b;
}

function substract(a, b) {
    return a - b;
}

function multiply(a, b) {
    return a * b;
}

function divide(a, b) {
    if (b === 0) {
        return "Can't divide by zero.";
    }
    return a / b;
}


function calculate() {
    if (num1 !== null && operation && currentInput) {
        num2 = parseFloat(currentInput);
        let result;
        switch (operation) {
            case "+":
                result = add(num1, num2);
                break;
            case "-":
                result = substract(num1, num2);
                break;
            case "*":
                result = multiply(num1, num2);
                break;
            case "/":
                result = divide(num1, num2);
                break;
        }
        field.textContent = result;
        num1 = result;
        currentInput = "";
        num2 = null;
        operation = "";
    }
}

digits.forEach(button => {
    button.addEventListener("click", () => {
        currentInput += button.textContent;
        field.textContent = currentInput;
    });
});

operations.forEach(button => {
    button.addEventListener("click", () => {
        const buttonValue = button.textContent;

        if (buttonValue === "=") {
            calculate();
        } else {
            if (num1 === null) {
                num1 = parseFloat(currentInput);
            } else if (operation && currentInput) {
            }
            operation = buttonValue;
            currentInput = "";
        }
    });
});

reset.addEventListener("click", () => {
    num1 = null;
    num2 = null;
    operation = "";
    currentInput = "";
    field.textContent = "";
});
