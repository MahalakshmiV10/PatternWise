let qs = [], i = 0, score = 0, wrong = [], locked = false;
const box = document.getElementById("qbox");
function shuffle(a) { for (let k = a.length - 1; k > 0; k--) { const j = Math.floor(Math.random() * (k + 1)); [a[k], a[j]] = [a[j], a[k]]; } return a; }
async function start() {
  const r = await fetch("/api/quiz"); qs = shuffle(await r.json()); i = 0; score = 0; wrong = []; show();
}
function show() {
  if (i >= qs.length) return finish();
  locked = false; const q = qs[i]; box.innerHTML = "";
  const h = document.createElement("div"); h.innerHTML = "<small>Question " + (i + 1) + " of " + qs.length + " · score " + score + "</small>";
  const t = document.createElement("h3"); t.textContent = q.text; box.append(h, t);
  if (q.code) { const p = document.createElement("pre"); p.textContent = q.code; box.append(p); }
  q.options.forEach((o, k) => { const b = document.createElement("button"); b.className = "opt"; b.textContent = o; b.onclick = () => answer(k, b); box.append(b); });
}
async function answer(k, b) {
  if (locked) return; locked = true; const q = qs[i];
  const res = await (await fetch("/api/quiz/check", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({number: q.number, choice: k})})).json();
  const btns = box.querySelectorAll(".opt"); btns[res.answer].classList.add("ok");
  if (res.correct) score++; else { b.classList.add("bad"); wrong.push({q: q.text, right: q.options[res.answer], why: res.explanation}); }
  const e = document.createElement("p"); e.textContent = (res.correct ? "Correct! " : "Not quite. ") + res.explanation;
  const n = document.createElement("button"); n.className = "btn"; n.textContent = i + 1 < qs.length ? "Next Question" : "See Result";
  n.onclick = () => { i++; show(); }; box.append(e, n);
}
function finish() {
  const pct = Math.round(score / qs.length * 100), s = load();
  s.attempts++; s.best = Math.max(s.best || 0, pct); save(s); render();
  box.innerHTML = "<h2>Score: " + score + "/" + qs.length + " (" + pct + "%)</h2>";
  wrong.forEach(w => { const d = document.createElement("div"); d.className = "card"; d.textContent = "✗ " + w.q + " → " + w.right + ". " + w.why; box.append(d); });
  const r = document.createElement("button"); r.className = "btn"; r.textContent = "Restart Quiz"; r.onclick = start; box.append(r);
}
start();
