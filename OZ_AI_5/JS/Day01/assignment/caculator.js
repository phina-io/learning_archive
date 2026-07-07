function start() {

    const input = prompt("계산식을 입력하세요. 예: 1 + 2 * 3 - 4 / 2");

    if (input === null || input.trim() === "") {
        console.log("계산식이 입력되지 않았습니다.");
        return;
    }

    try {
        const result = calculate(input);
        console.log("결과:", result);
    } catch (error) {
        console.log("잘못된 계산식입니다.");
    }
}

function calculate(expression) {
    const tokens = expression.match(/\d+(\.\d+)?|[+\-*/]/g);

    if (!tokens) {
        throw new Error("Invalid expression");
    }

    const numbers = [];
    const operators = [];

    const priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
    };

    function applyOperator() {
        const operator = operators.pop();
        const b = numbers.pop();
        const a = numbers.pop();

        if (operator === "+") numbers.push(a + b);
        else if (operator === "-") numbers.push(a - b);
        else if (operator === "*") numbers.push(a * b);
        else if (operator === "/") numbers.push(a / b);
    }

    for (let token of tokens) {
        if (!isNaN(token)) {
            numbers.push(Number(token));
        } else {
        while (
            operators.length > 0 &&
            priority[operators[operators.length - 1]] >= priority[token]
        ) {
            applyOperator();
        }

            operators.push(token);
        }
    }

    while (operators.length > 0) {
        applyOperator();
    }

    return numbers[0];
}