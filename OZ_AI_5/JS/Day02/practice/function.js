// 함수 (function)
// 입력 → 처리 → 출력 구조
// 코드를 묶어서 이름을 붙이고, 재사용

// 함수의 특징
// 호출 (call) → 실행 (execute)
// 모든 함수는 반드시 return한다 - return문이 없으면 기본값 반환(undefined)
// return의 기능 - 결과값을 호출한 곳으로 반환 / 함수를 종료
// 호출할 때 적당한 값을 넘겨야 함


function add(n1, n2) {
    let result = n1 + n2;
    return result
}

// 변수 선언없이 바로 return으로 반환 요청 가능
function add(n1, n2) {
    return n1 + n2;
}

// 함수 호출
console.log(add(10, 5))


// 함수 정의 vs 함수 호출
function sayHello() {
    console.log("hello");
};

// 함수를 호출하지 않고 함수 그 자체인 상태 (e.g. 자판기 버튼 그 자체)
// 함수를 변수에 할당 가능
let result = sayHello;
// result()

// 함수 호출 → 실행 (e.g. 자판기 버튼을 누름)
let result2 = sayHello();
console.log(result2);


// 함수를 값처럼 다룰 수 있다
// 함수를 다른 변수에 할당할 수 있다
// 함수를 다른 함수의 인자로 전달할 수 있다
// 함수를 선언한 곳과 호출하는 곳이 달라질 수 있다