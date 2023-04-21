function Prime(num) {
  if (num < 2) return false;
  for (let i = 2; i <= num / 2; i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

onmessage = function (e) {
  // 워커 태스크로부터 전달받은 숫자
  let number = e.data;

  // 소수 판별 결과 전송
  postMessage(Prime(number));
};
