let canvas = document.querySelector('canvas');
let ctx = canvas.getContext('2d');
canvas.width = W = window.innerWidth;
canvas.height = H = window.innerHeight;

let an = 0.04, k = -0.07, no = 5;

function animate() {
    an += k;

    let x = W / 2 + (W - 25) / 2 * Math.sin(an) ** 3;
    let y = H / 2 - (13 * Math.cos(an) - 5 * Math.cos(2 * an) - 2 * Math.cos(3 * an) - Math.cos(4 * an)) * 13;

    ctx.beginPath();
    ctx.strokeStyle = `hsl(${360 * Math.random()}, 100%, 50%)`;
    ctx.moveTo(x, y);
    for (let a = 0; a < 2 * Math.PI; a += 0.01) {
        let xt = x + 8 * Math.cos(no * a) * Math.cos(a);
        let yt = y + 8 * Math.cos(no * a) * Math.sin(a);
        ctx.lineTo(xt, yt);
    }
    ctx.stroke();
    ctx.closePath();

    if (an > 6.5 || an < -6.5) {
        k = -k;
        no = Math.floor(Math.random() * 9) + 2;
        ctx.clearRect(0, 0, W, H);
    }
    requestAnimationFrame(animate);
}

requestAnimationFrame(animate);