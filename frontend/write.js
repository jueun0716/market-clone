const form = document.getElementById("write-form");

const handleSubmitForm = async (event) => {
  event.preventDefault(); //제출하자마자 없어지는걸 막아준다.
  const body = new FormData(form); //현재시간은 폼으로 보내기
  //세계시간 기준으로
  body.append("insertAt", new Date().getTime()); //바디에 정보 추가

  try {
    //try 시도 하다가 안되면
    const res = await fetch("/items", {
      method: "POST",
      body,
    });
    const data = await res.json();
    if (data === "200") window.location.pathname = "/";
  } catch (e) {
    //이게 실행
    console.error(e);
  }
};

form.addEventListener("submit", handleSubmitForm);
