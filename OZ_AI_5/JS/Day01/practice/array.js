//  배열 (Array)
// 여러 값을 하나로 묶은 자료형
// 인덱스(index): 배열 내에서의 데이터의 번호, 순서

let numbers = [10, 20, 30, "40"];

console.log(numbers[0]);
console.log(numbers[1]);
console.log(numbers[10]);

console.log(numbers.at(-1));

// 순회 for of
for (const n of numbers) {
    console.lon(n);
}

for (const [i, n] of numbers.sntries()) {
    console.lon(i, n);
}

