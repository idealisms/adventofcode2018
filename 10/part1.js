let FAST_STEP = 10;
let MAP_SIZE = 1000;
let MAP_OFFSET = MAP_SIZE / 2;
let MAP_SCALE = 1;
let current_step = 0;

function draw() {
  ctx.clearRect(0, 0, MAP_SIZE, MAP_SIZE);
  for (let pt of points) {
    x = pt[0] + MAP_OFFSET;
    y = MAP_SIZE - (pt[1] + MAP_OFFSET);
    ctx.fillRect(x * MAP_SCALE, y * MAP_SCALE, 1, 1);
  }
}

function step(s) {
  let dir = s / Math.abs(s);
  for (let i = 0; i < Math.abs(s); ++i) {
    for (let j = 0; j < points.length; ++j) {
      points[j][0] += deltas[j][0] * dir;
      points[j][1] += deltas[j][1] * dir;
    }
  }
  draw();
  current_step += s;
  console.log(current_step);
}

window.onload = function() {
  document.getElementById('backback').onclick = () => {
    step(-FAST_STEP);
  };
  document.getElementById('back').onclick = () => {
    step(-1);
  };
  document.getElementById('forward').onclick = () => {
    step(1);
  };
  document.getElementById('forwardforward').onclick = () => {
    step(FAST_STEP);
  };
  window.ctx = document.getElementById('c').getContext('2d');
  step(10105);
  draw();
};