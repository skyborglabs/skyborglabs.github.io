const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#main-nav');
toggle?.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));toggle.textContent=open?'Close ×':'Menu +';nav.classList.toggle('open',open)});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&toggle?.getAttribute('aria-expanded')==='true'){toggle.click();toggle.focus()}});
const dialog=document.querySelector('#art-viewer');
document.querySelectorAll('.gallery-card').forEach(button=>button.addEventListener('click',()=>{dialog.querySelector('img').src=button.dataset.full;dialog.querySelector('img').alt=button.querySelector('img').alt;dialog.querySelector('#art-title').textContent=button.dataset.title;dialog.showModal()}));
dialog?.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());
dialog?.addEventListener('click',e=>{const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close()});
