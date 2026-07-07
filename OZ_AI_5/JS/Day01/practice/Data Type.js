// 자료형(Data Type)

//---------------------------------------------------------------
// Number: 정수, 실수 구분 없이 모든 수를 나타내는 자료형

const num1 = 10;
const num2 = 5.22;

console.log(num1 + num2);

console.log(typeof num1);
console.log(typeof num2);


//---------------------------------------------------------------
// 문자열(String)

let username = "alex";
let message = 'Hello';

console.log(username);
console.log(message);

console.log(typeof username);
console.log(typeof message);


//---------------------------------------------------------------
// 불리언(Boolean)
// true, false을 나타내는 자료형

let isStudent = true;
let hasTicket = false;

console.log(isStudent);
console.log(hasTicket);

console.log(typeof isStudent);
console.log(typeof hasTicket);


//---------------------------------------------------------------
// Null (NaN, None, Nil)
// "값이 비어있음" 의미하는 값
// 0 → Number & 0값
// "" → String & 빈 문자열 값
// " " → String & 빈 문자열 값

let 당첨자 = null;

console.log(당첨자);
console.log(typeof 당첨자);


//---------------------------------------------------------------
// undefined (정의되지 않은)
// "값이 할당되지 않음", 변수 = 값을 지정하지 않음

// 변수 선언(declaration)
let score;

console.log(score);
console.log(typeof score);