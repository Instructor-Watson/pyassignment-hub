
const $ = (sel, root=document) => root.querySelector(sel);
const $$ = (sel, root=document) => Array.from(root.querySelectorAll(sel));

function qsParam(key){
  const u = new URL(window.location.href);
  return u.searchParams.get(key);
}

function copyToClipboard(text){
  navigator.clipboard?.writeText(text).catch(()=>{});
}

async function fetchText(path){
  const res = await fetch(path);
  if(!res.ok) throw new Error(`Failed to load ${path}`);
  return await res.text();
}

async function fetchJSON(path){
  const res = await fetch(path);
  if(!res.ok) throw new Error(`Failed to load ${path}`);
  return await res.json();
}

function download(filename, content){
  const blob = new Blob([content], {type: "text/plain"});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url; a.download = filename; a.click();
  URL.revokeObjectURL(url);
}

function openInPythonTutor(code){
  const base = "https://pythontutor.com/visualize.html#code=";
  const encoded = encodeURIComponent(code);
  const tail = "&cumulative=false&heapPrimitives=false&textReferences=false&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D";
  window.open(base + encoded + tail, "_blank");
}
