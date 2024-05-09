<script>
  import { onMount } from "svelte";
  import { getDatabase, ref, onValue } from "firebase/database";
  import Nav from "../components/Nav.svelte";
  

    let hour = new Date().getHours();
    let min = new Date().getMinutes();

    $: items = [];//반응형 변수로 바뀐다

    const calcTime = (timestamp) => {
  const curTime = new Date().getTime() - 9 * 60 * 60 * 1000; //과거시간
  const time = new Date(curTime - timestamp); //()묶어 주면 시간 관련된 값으로 바꿔주려고 사용
  const hour = time.getHours();
  const minute = time.getMinutes();
  const second = time.getSeconds();

  if (hour > 0) return `${hour}시간 전`;
  else if (minute > 0) return `${minute}분 전`;
  else if (second > 0) return `${second}초 전`;
  else "방금 전";
};

const db = getDatabase();
const itemsRef = ref(db, "items/");

onMount(()=> { //렌더링 해도 값이 그대로 있음
  onValue(itemsRef, (snapshot) => {
  const data = snapshot.val();
  items = Object.values(data).reverse();
});
});

</script>

<header>
    <div class="info-bar">
      <div class="info-bar__time">{hour}:{min}</div>
      <div class="info-bar__icons">
        <img src="src/assets/chart-bar.svg" alt="chart-bar" />
        <img src="src/assets/wifi.svg" alt="wifi" />
        <img src="src/assets/batter.svg" alt="batter" />
      </div>
    </div>

    <div class="menu-bar">
      <div class="menu-bar__location">
        <div>역삼1동</div>
        <div class="menu-bar__location-icon">
          <img src="src/assets/arrow-donw.svg" alt="" />
        </div>
      </div>

      <div class="menu-bar__icons">
        <img src="src/assets/search.svg" alt="" />
        <img src="src/assets/menu.svg" alt="" />
        <img src="src/assets/alert.svg" alt="" />
      </div>
    </div>
  </header>

  <main>
    {#each items as item }
    <div class = "item-list">
      <div class = "item-list__img">
        <img alt ={item.title} src = {item.imgUrl} />
      </div>
      <div class = "item-list__info">
          <div class = "item-list__info-title">  {item.title} </div>
          <div class = "item-list__info-meta"> {item.place} {calcTime(item.insertAt)} </div> 
           <div class = "item-list__info-price">  {item.price} </div>
          <div> {item.description} </div>  
        </div>
      </div>
    {/each}

    <a class="write-btn" href="#/write">+ 글쓰기</a>
  </main>

  <Nav location="home"/>
 
  <style>
 
  </style>