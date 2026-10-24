// Progress lives in this browser's localStorage only (not synced anywhere).
const KEY = "patternwise";
function load() { try { return Object.assign({done: [], attempts: 0, best: null, last: null}, JSON.parse(localStorage.getItem(KEY))); } catch (e) { return {done: [], attempts: 0, best: null, last: null}; } }
function save(s) { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) {} }
const $ = id => document.getElementById(id);
function render() {
  const s = load(), set = (id, v) => { if ($(id)) $(id).textContent = v; };
  set("s-done", s.done.length); set("s-att", s.attempts); set("s-best", s.best === null ? "–" : s.best + "%"); set("s-last", s.last || "none");
  if ($("bar")) $("bar").style.width = (s.done.length / 8 * 100) + "%";
  document.querySelectorAll("[data-tick]").forEach(e => e.textContent = s.done.includes(+e.dataset.tick) ? "✅" : "");
}
render();
if ($("search")) $("search").addEventListener("input", e => {
  const q = e.target.value.toLowerCase().trim(); let shown = 0;
  document.querySelectorAll(".pat").forEach(c => { const m = c.dataset.s.includes(q); c.hidden = !m; if (m) shown++; });
  $("empty").hidden = shown > 0;
});
if ($("complete")) {
  const n = +$("complete").dataset.n, s = load(); s.last = document.querySelector("h1").textContent; save(s);
  $("complete").onclick = () => { const t = load(); if (!t.done.includes(n)) t.done.push(n); save(t); $("complete").textContent = "Completed ✅"; };
  $("copy").onclick = () => navigator.clipboard.writeText($("code").textContent).then(() => $("copy").textContent = "Copied!");
}
if ($("reset")) $("reset").onclick = () => { if (confirm("Reset all progress in this browser?")) { localStorage.removeItem(KEY); render(); } };
