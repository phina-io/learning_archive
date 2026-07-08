let display = document.getElementById("display");
let powerOn = true;

function togglePower() {
    powerOn = !powerOn;

    if (powerOn) {
        display.value = "0";
    } else {
        display.value = "";
    }
}

function appendNumber(number) {
    if (!powerOn) return;

    if (display.value === "0") {
        display.value = number;
    } else {
        display.value += number;
    }
}

function appendOperator(operator) {
    if (!powerOn) return;

    const lastChar = display.value[display.value.length - 1];

    if (["+", "-", "*", "/"].includes(lastChar)) {
        display.value = display.value.slice(0, -1) + operator;
    } else {
        display.value += operator;
    }
}

function clearDisplay() {
    if (!powerOn) return;
    display.value = "0";
}

function performCalculate() {
    if (!powerOn) return;

    try {
        const result = calculate(display.value);
        display.value = result;
    } catch (error) {
        display.value = "Error";
    }
}

function calculate(expression) {
    const tokens = expression.match(/\d+(\.\d+)?|[+\-*/]/g);

    if (!tokens) {
        throw new Error("잘못된 식입니다.");
    }

    const numbers = [];
    const operators = [];

    const priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
    };

function calculateOnce() {
    const operator = operators.pop();
    const b = numbers.pop();
    const a = numbers.pop();

    if (operator === "+") numbers.push(a + b);
    if (operator === "-") numbers.push(a - b);
    if (operator === "*") numbers.push(a * b);
    if (operator === "/") numbers.push(a / b);
}

    for (let token of tokens) {
    if (!isNaN(token)) {
        numbers.push(Number(token));
    } else {
        while (
            operators.length > 0 &&
            priority[operators[operators.length - 1]] >= priority[token]
        ) {
            calculateOnce();
        }

        operators.push(token);
    }
}

    while (operators.length > 0) {
        calculateOnce();
}

    return numbers[0];
}