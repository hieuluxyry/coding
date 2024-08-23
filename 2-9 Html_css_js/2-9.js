const canvas = document.getElementById('codosaovang');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

class Firework {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = canvas.height;
        this.targetY = Math.random() * canvas.height / 2;
        this.speed = Math.random() * 3 + 2;
        this.radius = Math.random() * 3 + 2;
        this.color = `hsl(${Math.random() * 360}, 100%, 50%)`;
        this.boom = false;
        this.particles = [];
    }

    update() {
        if (this.y > this.targetY) {
            this.y -= this.speed;
        } else if (!this.boom) {
            this.boom = true;
            this.explode();
        }
        this.draw();
    }

    draw() {
        if (!this.boom) {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.fill();
        }
    }

    explode() {
        for (let i = 0; i < 30; i++) {
            const angle = Math.random() * Math.PI * 2;
            const speed = Math.random() * 5 + 2;
            this.particles.push(new Particle(this.x, this.y, angle, speed, this.color));
        }
    }
}

class Particle {
    constructor(x, y, angle, speed, color) {
        this.x = x;
        this.y = y;
        this.angle = angle;
        this.speed = speed;
        this.color = color;
        this.radius = Math.random() * 2 + 1;
        this.life = 100;
        this.opacity = 1;
    }

    update() {
        this.x += Math.cos(this.angle) * this.speed;
        this.y += Math.sin(this.angle) * this.speed;
        this.life -= 1;
        this.opacity = this.life / 100;
        this.draw();
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.globalAlpha = this.opacity;
        ctx.fill();
        ctx.globalAlpha = 1;
    }
}

let fireworks = [];

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (Math.random() < 0.05) {
        fireworks.push(new Firework());
    }
    fireworks = fireworks.filter(firework => !firework.boom || firework.particles.length > 0);
    fireworks.forEach(firework => {
        firework.update();
        firework.particles.forEach((particle, index) => {
            particle.update();
            if (particle.life <= 0) {
                firework.particles.splice(index, 1);
            }
        });
    });
    requestAnimationFrame(animate);
}

animate();

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
