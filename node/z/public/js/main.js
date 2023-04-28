const form = document.querySelector(".form");

form.addEventListener("submit", (e) => {
  e.preventDefault(); // 폼이 제출되는 것을 막음

  const name = form.name.value;
  const email = form.email.value;

  fetch("/users", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name, email }), // 입력값을 JSON 형식으로 변환하여 body에 담음
  })
    .then((res) => {
      if (res.ok) {
        return res.json();
      } else {
        throw new Error("서버 오류 발생");
      }
    })
    .then((data) => {
      console.log(data);
      form.reset(); // 입력칸을 비움
      alert("사용자 등록 완료");
    })
    .catch((error) => {
      console.log(error);
      alert(error.message);
    });
});
