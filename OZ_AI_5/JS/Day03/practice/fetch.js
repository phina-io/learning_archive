// FetchAPI(비동기 방식)

// GET 요청
// fetch("https://jsonplaceholder.typicode.com/posts")
//     // 응답 메시지에서 JSON 데이터 추출
//     .then(Response => Response.json())            
//     // 콘솔에 출력
//     .then(data => console.log(data))

// 동기 방식이였다면
// const response = fetch()
// const data = response.json()
// console.log(data)


// POST 요청
fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    // 헤더에 데이터 형식(Content-Type)을 명시
    Headers: {"Content-Type": "application/json"},

    // JSON 문자열로 변환해서 요청 본문에 넣어줌
    body: JSON.stringify({title: "Python", body: "Hello, Python"})
})
    .then(Response => Response.json()) 
    .then(data => console.log(data))