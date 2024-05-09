import { writable } from "svelte/store";

export const user$ = writable(null); //수정할수있는 값, ($)달러는 writable을 가져와야 하기에 꼭 넣어야함
