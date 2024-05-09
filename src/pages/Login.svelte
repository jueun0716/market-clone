<script>
  import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
  import { user$ } from "../store";

  const provider = new GoogleAuthProvider();
  const auth = getAuth();

const loginWithGoogle = async () => { //로그인 완료
  try{ 
  const result = await signInWithPopup(auth, provider) //팝업에 결과가 올때까지 기다리고
  const credential = GoogleAuthProvider.credentialFromResult(result); // 인증정보 들어올거고 
  const token = credential.accessToken; //인증정보에는 토큰과 유저가 들어있다.
  const user = result.user;
  user$.set(user); //유저상태 업데이트
  localStorage.setItem("token",token); //로그인이 되면 로컬스토리지에 저장
}catch(error){ //error가 있으면 에러 표시해주세요
    console.error(error);
}   
};

</script>

<div>
  <!-- {#if $user$} : 유저정도가 있을때만 보여주세요
 <div>{$user$?.displayName}로그인됨</div> : ?에러 처리
  {/if}  -->
  <div>로그인하기</div>
  <button class ="login-btn" on:click={loginWithGoogle}>
    <img 
    class = "goole-img"
    src="https://blog.kakaocdn.net/dn/HDY7T/btrY2our4Rw/Fw6bz0QroBUp1YxglkkwEK/img.webp " 
    alt="">
    <div> Google로 시작하기 </div>
  <div />
  </button>
</div>

<style>
.login-btn{
  width: 200px;
  height: 50px;
  border: 1px solid gray;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor : pointer;
  border-radius: 3px;
  font-size: medium;
}

.goole-img{
  width: 50px;
}
</style>