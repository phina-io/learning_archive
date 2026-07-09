// Timer API

// 1) setTimeout: 일정 시간 지난 뒤에 특정 함수를 한 번 호출하는 기능
setTimeout(
    // 함수 인자 설정
    () => console.log("3초 경과"),
    3000 // 3000ms = 3s. 3 * 1000으로도 가능. ms 기본 셋팅 단위
)


// 2) setInterval: 일정 시간마다 특정 함수를 반복 실행하는 기능
// 2초마다 반복 출력. 컨트롤c로 멈춤
// setInterval(
//     () => console.log("2초 경과"),
//     2000
// )

// timerId를 사용한 cleanInterval
let counter = 1
const timerId = setInterval(
    () => { 
        if (counter > 3) {
            clearInterval(timerId)
        }
        counter ++
        console.log("2초 경과", counter)
    },
    2000
)