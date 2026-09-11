---
layout: null
title: Mama rafiki
lang: cs
permalink: /cs/
---
<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mama rafiki</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f7f7f7;color:#171717;font-family:Arial,Helvetica,sans-serif;font-size:16px}button,a{-webkit-tap-highlight-color:transparent}button{font:inherit;color:inherit}a{color:inherit}
.languages{position:absolute;top:30px;right:5vw;display:flex;gap:20px;font-size:14px;z-index:2}.languages a{text-decoration:none;padding:8px 0}.languages [aria-current]{border-bottom:1px solid #171717}
main{min-height:100svh;display:grid;place-items:center;padding:100px 24px 70px}
.tiles{width:min(100%,1000px);display:grid;grid-template-columns:1fr 1.5fr 1fr;align-items:center;gap:26px}
.tile{border:1px solid #dedede;background:#fff;cursor:pointer;text-align:left;position:relative;display:flex;flex-direction:column;justify-content:space-between;padding:30px;min-height:230px;border-radius:4px;box-shadow:0 12px 35px #00000004;transition:transform .2s,box-shadow .2s,border-color .2s}
.tile:hover{transform:translateY(-7px);border-color:#999;box-shadow:0 20px 40px #00000009}.tile:focus-visible,a:focus-visible,.close:focus-visible{outline:3px solid #171717;outline-offset:6px}
.tile-name{font-family:Georgia,'Times New Roman',serif;font-size:clamp(28px,3vw,38px);line-height:1.15;font-weight:400}.tile-note{font-size:14px;color:#666}.tile-arrow{position:absolute;bottom:26px;right:26px;font-size:24px;font-weight:400}
.center{min-height:360px;background:#ededed;border-color:#e4e4e4;padding:38px;order:2}.center .tile-name{font-size:clamp(48px,6vw,76px);letter-spacing:-3px}.center .tile-note{color:#555}.write{order:1;transform:translateY(-60px)}.write:hover{transform:translateY(-67px)}.inspire{order:3;transform:translateY(70px)}.inspire:hover{transform:translateY(63px)}
footer{position:absolute;bottom:24px;width:100%;text-align:center;color:#777;font-size:14px;pointer-events:none}
dialog{border:1px solid #ddd;border-radius:6px;background:#fff;color:#171717;padding:44px;width:min(680px,calc(100% - 32px));max-height:85svh;box-shadow:0 30px 100px #0002}dialog::backdrop{background:#0004;backdrop-filter:blur(5px)}dialog h2{font:400 42px/1.15 Georgia,serif;margin:0 50px 30px 0}dialog h3{font:400 26px Georgia,serif;margin-top:36px}.close{position:absolute;right:18px;top:16px;border:0;background:#f1f1f1;width:40px;height:40px;border-radius:50%;font-size:26px;cursor:pointer}.contact{font-size:18px;line-height:1.8}.contact p{margin:12px 0}.contact a{text-underline-offset:5px;overflow-wrap:anywhere}.article-list{list-style:none;padding:0;margin:0}.article-list li{border-bottom:1px solid #e5e5e5}.article-list a{padding:18px 0;display:flex;justify-content:space-between;gap:20px;text-decoration:none;font-size:18px;line-height:1.5}.article-list a:hover{text-decoration:underline;text-underline-offset:4px}.article-list span{flex:none;color:#777}.soon{line-height:1.7;color:#666}
@media(max-width:700px){main{padding:90px 22px 60px}.tiles{max-width:440px;grid-template-columns:1fr 1fr;gap:16px}.center{order:0;grid-column:1/-1;min-height:285px;padding:30px}.center .tile-name{font-size:68px}.write,.inspire{transform:none;min-height:190px;padding:22px}.write:hover,.inspire:hover{transform:translateY(-4px)}.tile-name{font-size:28px}.tile-arrow{right:20px;bottom:20px}.tile-note{max-width:80%}footer{position:static;padding:0 0 22px}dialog{padding:32px 24px}dialog h2{font-size:34px}.languages{top:20px;right:24px}}
@media(prefers-reduced-motion:reduce){.tile{transition:none}}
</style>
</head>
<body>
<nav class="languages" aria-label="Jazyk"><a href="/cs/" lang="cs" aria-current="page">CS</a><a href="/en/" lang="en">EN</a></nav>
<main>
<div class="tiles" aria-label="Mama rafiki — rozcestník">
<button class="tile center" data-dialog="contact" aria-haspopup="dialog"><span class="tile-name">Mama<br>rafiki</span><span class="tile-note">Josefína Drbálková · Kontakt</span><span class="tile-arrow" aria-hidden="true">+</span></button>
<button class="tile write" data-dialog="writing" aria-haspopup="dialog"><span class="tile-name" role="img" aria-label="Píšu">✏️</span><span class="tile-note">Články a deník</span><span class="tile-arrow" aria-hidden="true">+</span></button>
<button class="tile inspire" data-dialog="inspiration" aria-haspopup="dialog"><span class="tile-name">Inspiruju se</span><span class="tile-note">Připravuji</span><span class="tile-arrow" aria-hidden="true">+</span></button>
</div>
</main>
<footer>Mama rafiki</footer>
<dialog id="contact" aria-labelledby="contact-title"><button class="close" aria-label="Zavřít">×</button><h2 id="contact-title">Kontakt</h2><div class="contact"><p>Josefína Drbálková</p><p><a href="tel:+420602316755">+420 602 316 755</a><br><a href="mailto:josefina.drbalkova@email.cz">josefina.drbalkova@email.cz</a></p></div></dialog>
<dialog id="writing" aria-labelledby="writing-title"><button class="close" aria-label="Zavřít">×</button><h2 id="writing-title">Píšu</h2><h3>Články</h3><ul class="article-list"><li><a href="{% link cs/clanek_kdyz_potkas_druzinarku.html %}">Když pak potkáš svoji družinářku na ulici<span aria-hidden="true">↗</span></a></li><li><a href="{% link cs/clanek_uz_se_nebojim_zimy.html %}">Už se nebojím zimy<span aria-hidden="true">↗</span></a></li><li><a href="{% link cs/clanek_kde_si_dobijim_baterky.html %}">Kde si doopravdy dobíjím baterky<span aria-hidden="true">↗</span></a></li><li><a href="{% link cs/clanek_3_posledni_rande_bez_deti.html %}">Poslední rande bez dětí<span aria-hidden="true">↗</span></a></li><li><a href="{% link cs/clanek_materska_jako_sance.html %}">Mateřská jako šance<span aria-hidden="true">↗</span></a></li><li><a href="{% link cs/clanek_kapacita_time_management.html %}">Musím být mistr time managementu, abych si našla 10 minut denně na španělštinu?<span aria-hidden="true">↗</span></a></li></ul><h3>Deník</h3><ul class="article-list"><li><a href="{% link cs/denik_vasik_jako_fotbalista.html %}">Vašík jako fotbalista<span aria-hidden="true">↗</span></a></li></ul></dialog>
<dialog id="inspiration" aria-labelledby="inspiration-title"><button class="close" aria-label="Zavřít">×</button><h2 id="inspiration-title">Inspiruju se</h2><p class="soon">Tuto sekci pro vás připravuji.</p></dialog>
<script>
document.querySelectorAll('[data-dialog]').forEach(button=>button.addEventListener('click',()=>document.getElementById(button.dataset.dialog).showModal()));
document.querySelectorAll('dialog').forEach(dialog=>{
dialog.querySelector('.close').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});
});
</script>
</body>
</html>
