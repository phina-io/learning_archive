// 조건이 true인 동안, 계속 반복 실행
// 무한루프 조심!!
// while (true) { }

let i =0;

while (i < 3) {
    console.log(i)
    i++   // 증감 조건 설정

    if ( i == 5) {
        break
    }
}