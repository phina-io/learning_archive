// arithmetic
// 산술 연산자: 숫자 계산에 사용되는 연산자

let n1 = 10;
let n2 = 4;

console.log(n1 + n2);
console.log(n1 - n2);
console.log(n1 * n2);
console.log(n1 / n2);


//---------------------------------------------------------------
// compare 
// 비교 연산자: 값이 크고 작음을 비교
// 결과가 boolean

console.log(10 > 5);   // true
console.log(10 < 5);   // false

console.log(10 >= 5);   // true
console.log(10 <= 10);   // true

console.log("a" > "b");


//---------------------------------------------------------------
// equal
// 동등 비교

console.log(10 == "10");    // 값만 비교(자동 타입 변환)
console.log(10 === "10");    // 값 + 타입 비교


//---------------------------------------------------------------
// logical
// 논리 연산자
// 여러개의 참/거짓 조건을 조합 → 결과: boolean 
// and: &&, or || 

let age = 20;
let hasId = false;

// 주류 구매 조건
console.log(age >= 20 && hasId);   // false
console.log(age >= 20 || hasId);   // true
console.log(!hasId); // NOT 연산자 → 값을 반대로


//---------------------------------------------------------------
// concat
// 문자열 연산자 (concatenate)
// 문자열을 이어주는 연산자(+)

let firstName = "Alex";
let lastName = "Kim";

// let msg = "Hello, " + firstName + " " + lastName

// 템플릿 리터럴
let msg = `Hello, ${firstName} ${lastName}`
console.log(msg);