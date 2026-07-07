// 조건문 (if/else문)
// 특정 조건을 만족했을 때만, 코드를 실행하는 문법
// if (조건식) {
//     만족시 실행 코드
// } else { 만족하지 않을시 실행 코드
// }

let age = 20;

if (age >= 20) {
    console.log("성인입니다");
} else {
    console.log("학생입니다");
}

// 참으로 취급되는 값들: truthy
// [] → array
// 거짓으로 취급되는 값들: falsy(6개)
// false, 0, "", null, undefined, NaN
let age = 10;
if (10) {
    console.log("나이를 입력한 사용자입니다")
}