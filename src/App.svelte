<script>
  import Login from "./pages/Login.svelte";
  import Main from "./pages/Main.svelte";
  import NotFound from "./pages/NotFound.svelte";
  import Signup from "./pages/Signup.svelte";
  import Write from "./pages/Write.svelte";
  import Router from 'svelte-spa-router'
  import "./css/style.css";
  import {user$} from "./store";
  import { GoogleAuthProvider,getAuth,signInWithCredential } from "firebase/auth"; //앱 전체에 소셜네트워크 연동해야함
  import { onMount } from "svelte";
  import Loading from "./pages/Loading.svelte";
  import MyPage from "./pages/MyPage.svelte";

// const provider = new GoogleAuthProvider();
// provider.addScope('https://www.googleapis.com/auth/contacts.readonly');

  let isLoading = true; //맨처음 화면 갔을때는 로딩화면

  const auth = getAuth()

  const checkLogin = async () =>{
    const token = localStorage.getItem("token"); //토큰 가져오기
    if (!token) return (isLoading = false); //토큰이 없으면 아무동작 안함

  const credential = GoogleAuthProvider.credential(null,token);
  const result = await signInWithCredential(auth, credential)
  const user = result.user; //유저정보 가져오기
  user$.set(user); //유저 스토어에 유저정보 업데이트
  isLoading = false;
  };

  const routes = {
    "/":Main,
    "/signup" :Signup,
    "/write":Write,
    "/my" : MyPage,
    "*": NotFound,
  };

  onMount(() => checkLogin()); //이 화면에 렌더링 될때마다 체크로그인
</script>

{#if isLoading}
<Loading/>
{:else if !$user$} <!-- ! 이 표시는 부정 -> 유저가 없으면 login 페이지가 아니면, -->
<Login/>
{:else}
<Router {routes}/> <!-- routes 화면을 보여주세요-->
{/if}
