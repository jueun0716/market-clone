const form = document.querySelector("#login-form");

const handleSubmit = async (event) => {
  event.preventDefault();
  const formData = new FormData(form); //form 데이터 가져오기
  const sha256Password = sha256(formData.get("password")); //암호화
  formData.set("password", sha256Password);

  const res = await fetch("/login", {
    method: "POST",
    body: formData,
  });
  const data = await res.json();

  if (res.status === 200) {
    alert("로그인에 성공했습니다");
    window.location.pathname = "/";
  } else if (res.status === 401) {
    alert("아이디 또는 비밀번호가 틀렸습니다.");
  }
};

form.addEventListener("submit", handleSubmit);
