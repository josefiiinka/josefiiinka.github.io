---
layout: homepage
title: Motherhood and family life
lang: en
translation_key: home
description: "Josefína Drbálková’s personal blog about motherhood, family and everyday life. Honest experiences from a mum of three and supportive conversations about motherhood."
locale: en_GB
seo:
  type: WebSite
  name: Mama Rafiki
permalink: /en/
---
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{% seo %}
{% include search_metadata.html %}
{% include alternate_languages.html %}
<style>
*{box-sizing:border-box}body{margin:0;background:#f7f7f7;color:#171717;font-family:Arial,Helvetica,sans-serif;font-size:16px}button,a{-webkit-tap-highlight-color:transparent}button{font:inherit;color:inherit}a{color:inherit}
.languages{position:absolute;top:30px;right:5vw;display:flex;gap:20px;font-size:14px;z-index:2}.languages a{text-decoration:none;padding:8px 0}.languages [aria-current]{border-bottom:1px solid #171717}
main{min-height:100svh;display:grid;place-items:center;padding:100px 24px 70px}
.tiles{width:min(100%,1000px);display:grid;grid-template-columns:1fr 1.5fr 1fr;align-items:center;gap:26px}
.tile{border:1px solid #dedede;background:#fff;cursor:pointer;text-align:left;position:relative;display:flex;flex-direction:column;justify-content:space-between;padding:30px;min-height:230px;border-radius:4px;box-shadow:0 12px 35px #00000004;transition:transform .2s,box-shadow .2s,border-color .2s}
.tile:hover{transform:translateY(-7px);border-color:#999;box-shadow:0 20px 40px #00000009}.tile:focus-visible,a:focus-visible,.close:focus-visible{outline:3px solid #171717;outline-offset:6px}
.tile-name{font-family:Georgia,'Times New Roman',serif;font-size:clamp(28px,3vw,38px);line-height:1.15;font-weight:400}.tile-note{font-size:14px;color:#666}.tile-arrow{position:absolute;bottom:26px;right:26px;font-size:24px;font-weight:400}
.center{width:100%;aspect-ratio:1;min-height:0;border-radius:50%;background:#e3e3e3;border-color:#e3e3e3;padding:30px;order:2;align-items:center;justify-content:center;text-align:center}.center .tile-name{font-size:clamp(48px,6vw,76px);letter-spacing:-3px}.center .tile-note{color:#555}.write{order:1;transform:translateY(-60px)}.write:hover{transform:translateY(-67px)}.inspire{order:3;transform:translateY(70px)}.inspire:hover{transform:translateY(63px)}
footer{position:absolute;bottom:24px;width:100%;text-align:center;color:#777;font-size:14px;pointer-events:none}
dialog{border:1px solid #ddd;border-radius:6px;background:#fff;color:#171717;padding:44px;width:min(680px,calc(100% - 32px));max-height:85svh;box-shadow:0 30px 100px #0002}dialog::backdrop{background:#0004;backdrop-filter:blur(5px)}dialog h2{font:400 42px/1.15 Georgia,serif;margin:0 50px 30px 0}dialog h3{font:400 26px Georgia,serif;margin-top:36px}.close{position:absolute;right:18px;top:16px;border:0;background:#f1f1f1;width:40px;height:40px;border-radius:50%;font-size:26px;cursor:pointer}.contact{font-size:18px;line-height:1.8}.contact p{margin:12px 0}.contact a{text-underline-offset:5px;overflow-wrap:anywhere}.article-list{list-style:none;padding:0;margin:0}.article-list li{border-bottom:1px solid #e5e5e5}.article-list a{padding:18px 0;display:flex;justify-content:space-between;gap:20px;text-decoration:none;font-size:18px;line-height:1.5}.article-list a:hover{text-decoration:underline;text-underline-offset:4px}.article-list span{flex:none;color:#777}.soon{line-height:1.7;color:#666}
@media(max-width:700px){main{padding:90px 22px 60px}.tiles{max-width:440px;grid-template-columns:1fr 1fr;gap:16px}.center{order:0;grid-column:1/-1;min-height:0;width:min(100%,360px);justify-self:center;padding:30px}.center .tile-name{font-size:68px}.write,.inspire{transform:none;min-height:190px;padding:22px}.write:hover,.inspire:hover{transform:translateY(-4px)}.tile-name{font-size:28px}.tile-arrow{right:20px;bottom:20px}.tile-note{max-width:80%}footer{position:static;padding:0 0 22px}dialog{padding:32px 24px}dialog h2{font-size:34px}.languages{top:20px;right:24px}}
@media(prefers-reduced-motion:reduce){.tile{transition:none}}

/* Categories arranged around the central circle. */
main{padding:75px 20px 30px;min-height:calc(100svh - 45px)}
.tiles{display:block;position:relative;width:min(100%,1000px);height:690px}
.tiles .tile{position:absolute;left:var(--x);top:var(--y);width:var(--size);height:var(--size);min-height:0;aspect-ratio:1;padding:22px;border-radius:50%;align-items:center;justify-content:center;text-align:center;gap:12px;transform:translate(-50%,-50%)}
.tiles .tile:hover{transform:translate(-50%,-50%) translateY(-5px)}
.tiles .center{--x:50%;--y:48%;--size:340px;background:#e3e3e3}
.tiles .write{--x:15%;--y:28%;--size:180px}
.tiles .inspire{--x:84%;--y:31%;--size:200px}
.tiles .reading{--x:66%;--y:87%;--size:180px}
.tiles .center .tile-name{font-size:72px}
.tiles .write .tile-name{font-size:48px}
.tiles .inspire .tile-name,.tiles .reading .tile-name{font-size:30px}
.tiles .tile-note{max-width:100%}
.tiles .tile-arrow{position:static;font-size:20px;line-height:1}
footer{position:static;padding:0 0 22px}
@media(min-width:701px) and (max-width:900px){
.tiles .center{--size:280px}.tiles .center .tile-name{font-size:60px}
.tiles .write{--size:150px;--x:14%}.tiles .inspire{--size:170px;--x:86%}
}
@media(max-width:700px){
main{padding:65px 16px 15px}
.tiles{max-width:440px;height:620px}
.tiles .center{--x:50%;--y:49%;--size:230px}
.tiles .center .tile-name{font-size:56px;letter-spacing:-2px}
.tiles .write{--x:19%;--y:14%;--size:112px;padding:12px}
.tiles .write .tile-name{font-size:36px}
.tiles .write .tile-note{font-size:14px}
.tiles .inspire{--x:79%;--y:19%;--size:126px;padding:16px}
.tiles .reading{--x:36%;--y:86%;--size:140px;padding:16px}
.tiles .inspire .tile-name,.tiles .reading .tile-name{font-size:24px}
}

.about-support{width:min(100%,680px);margin:0 auto 55px;text-align:center;line-height:1.75}.about-label{font-size:14px;letter-spacing:.04em;color:#666}.about-support h1{font:400 clamp(28px,5vw,40px)/1.2 Georgia,serif;margin:16px 0 24px}.about-support p{margin:16px 0}.about-scope{font-size:15px;color:#555}.support-contact{border:1px solid #171717;border-radius:30px;padding:13px 26px;background:#171717;color:white;cursor:pointer;margin-top:12px}.support-contact:hover{background:#383838}.support-contact:focus-visible{outline:3px solid #171717;outline-offset:5px}
.tiles .inspire .tile-name{font-size:clamp(22px,3vw,30px);line-height:1.15;max-width:100%;overflow-wrap:normal}.inspiration-names{list-style:none;padding:0;margin:0;font-size:20px;line-height:1.6}.inspiration-names li{padding:14px 0;border-bottom:1px solid #e5e5e5}@media(max-width:700px){.tiles .inspire .tile-name{font-size:22px}.inspiration-names{font-size:18px}}

/* Three circle sizes for the homepage navigation. */
.tiles{height:760px}
.tiles .center{--x:50%;--y:43%;--size:340px}
.tiles .write{--x:15%;--y:24%;--size:180px}
.tiles .offer{--x:85%;--y:24%;--size:180px}
.tiles .work{--x:50%;--y:84%;--size:180px}
.tiles .inspire{--x:18%;--y:67%;--size:120px}
.tiles .reading{--x:82%;--y:67%;--size:120px}
.tiles .write .tile-name,.tiles .offer .tile-name,.tiles .work .tile-name{font-size:36px}
.tiles .inspire .tile-name,.tiles .reading .tile-name{font-size:28px}
.offer-copy{line-height:1.75}.offer-copy .about-scope{font-size:15px;color:#555}
@media(min-width:701px) and (max-width:900px){.tiles .center{--size:280px}.tiles .write,.tiles .offer,.tiles .work{--size:150px}.tiles .write .tile-name,.tiles .offer .tile-name,.tiles .work .tile-name{font-size:30px}}
@media(max-width:700px){
.tiles{height:690px;max-width:440px}
.tiles .center{--x:50%;--y:330px;--size:230px}
.tiles .write{--x:24%;--y:90px;--size:128px}
.tiles .offer{--x:76%;--y:90px;--size:128px}
.tiles .work{--x:50%;--y:610px;--size:128px}
.tiles .inspire{--x:18%;--y:500px;--size:92px}
.tiles .reading{--x:82%;--y:500px;--size:92px}
.tiles .write .tile-name,.tiles .offer .tile-name,.tiles .work .tile-name{font-size:27px}
.tiles .inspire .tile-name,.tiles .reading .tile-name{font-size:23px}
}

/* Larger circles sit near Mama rafiki; smaller circles orbit farther out. */
.tiles .write{--x:25%;--y:23%}
.tiles .offer{--x:75%;--y:23%}
.tiles .work{--x:50%;--y:80%}
.tiles .inspire{--x:12%;--y:70%}
.tiles .reading{--x:88%;--y:70%}
@media(min-width:701px) and (max-width:900px){
.tiles .write{--x:24%;--y:20%}.tiles .offer{--x:76%;--y:20%}
}
@media(max-width:700px){
.tiles{height:750px}
.tiles .write{--x:24%;--y:160px}
.tiles .offer{--x:76%;--y:160px}
.tiles .work{--x:50%;--y:525px}
.tiles .inspire{--x:18%;--y:670px}
.tiles .reading{--x:82%;--y:670px}
}

/* Prevent intrinsic button text width from stretching circles on mobile. */
.tiles .tile{box-sizing:border-box;min-width:0;max-width:none;flex-shrink:0;inline-size:var(--size);block-size:var(--size);padding:12px;border-radius:50%;appearance:none;-webkit-appearance:none}
.tiles .tile .tile-name{min-width:0;max-width:100%;white-space:normal}
@media(max-width:700px){.tiles .offer .tile-name,.tiles .work .tile-name,.tiles .write .tile-name{font-size:25px}.tiles .center{max-width:none}}

/* Fit the English labels within the shared circular navigation. */
.tiles .inspire .tile-name{font-size:21px}
@media(max-width:700px){.tiles .inspire .tile-name{font-size:14px}.tiles .reading .tile-name{font-size:18px}}
.latest-article{width:min(100%,680px);margin:15px auto 20px;padding:24px;text-align:center;background:#fff;border:1px solid #dedede;border-radius:6px}.latest-article p{margin:0 0 12px;line-height:1.6}.latest-article h1{font:400 clamp(24px,4vw,34px)/1.3 Georgia,serif;margin:0 0 20px}.latest-article a{display:inline-block;padding:12px 24px;background:#171717;color:#fff;border-radius:30px;text-decoration:none}.latest-article a:hover{text-decoration:underline}
</style>
<link rel="stylesheet" href="{{ '/assets/css/typography.css?v=' | append: site.github.build_revision | relative_url }}">
</head>
<body>
{% include language_switcher.html homepage=true %}
<main>
<section class="latest-article" aria-label="Latest article"><p>Download the latest article from Thursday, 29 October 2026</p><h1>Everyone keeps complaining about old people, but perhaps they know how to live</h1><a href="{{ '/assets/pdf/vsichni-porad-nadavaji-na-stary-2026-10-29.pdf' | relative_url }}" download>Download PDF (Czech, 1.1 MB)</a></section>

<div class="tiles" aria-label="Mama rafiki — explore">
<button class="tile center" data-dialog="contact" aria-haspopup="dialog" aria-label="Mama rafiki – open contact details"><span class="tile-name">Mama<br>rafiki</span></button>
<button class="tile write" data-dialog="writing" aria-haspopup="dialog"><span class="tile-name">Writing</span></button>
<button class="tile offer" data-dialog="offering" aria-haspopup="dialog"><span class="tile-name">Support</span></button>
<button class="tile work" data-dialog="working" aria-haspopup="dialog"><span class="tile-name">My work</span></button>
<button class="tile inspire" data-dialog="inspiration" aria-haspopup="dialog"><span class="tile-name">Inspiration</span></button>
<button class="tile reading" data-dialog="reading" aria-haspopup="dialog"><span class="tile-name">Reading</span></button>
</div>

</main>
<footer>Mama rafiki</footer>
<dialog id="contact" aria-labelledby="contact-title"><button class="close" aria-label="Close">×</button><h2 id="contact-title">Contact</h2><div class="contact"><p>Josefína Drbálková</p><p><a href="tel:+420602316755">+420 602 316 755</a><br><a href="mailto:josefina.drbalkova@email.cz">josefina.drbalkova@email.cz</a></p></div></dialog>
<dialog id="writing" aria-labelledby="writing-title"><button class="close" aria-label="Close">×</button><h2 id="writing-title">Writing</h2><h3>Articles</h3><ul class="article-list"><li><a href="{{ '/assets/pdf/vsichni-porad-nadavaji-na-stary-2026-10-29.pdf' | relative_url }}" download>Everyone keeps complaining about old people, but perhaps they know how to live<span>PDF · Czech</span></a></li><li><a href="{{ '/assets/pdf/posledni-den-v-druzine-uz-jsem-nic-necitila-2026-10-28.pdf' | relative_url }}" download>On my last day at the after-school club, I no longer felt anything<span>PDF · Czech</span></a></li><li><a href="{{ '/assets/pdf/jak-muze-neci-chyba-ukazat-na-mou-vlastni-2026-10-27.pdf' | relative_url }}" download>How someone else’s “mistake” can reveal my own<span>PDF · Czech</span></a></li><li><a href="{% link en/clanek_skola_v_albanii.html %}">A school for our son? We found one in Albania.<span aria-hidden="true">↗</span></a></li><li><a href="{% link en/clanek_materstvi_jako_profese.html %}">Motherhood as a profession – Finding my own way<span aria-hidden="true">↗</span></a></li><li><a href="{% link en/clanek_navrat_domu.html %}">Coming home – Why I left my job at an after-school club<span aria-hidden="true">↗</span></a></li><li><a href="{% link en/clanek_kdyz_potkas_druzinarku.html %}">When you run into your after-school teacher in the street<span aria-hidden="true">↗</span></a></li><li><a href="{% link en/clanek_uz_se_nebojim_zimy.html %}">I'm no longer afraid of winter<span aria-hidden="true">↗</span></a></li><li><a href="{% link en/clanek_kde_si_dobijim_baterky.html %}">Where I truly recharge my batteries<span aria-hidden="true">↗</span></a></li><li><a href="{% link en/clanek_3_posledni_rande_bez_deti.html %}">Last date without children<span aria-hidden="true">↗</span></a></li><li><a href="{% link en/clanek_materska_jako_sance.html %}">Maternity leave as an opportunity<span aria-hidden="true">↗</span></a></li><li><a href="{% link en/clanek_kapacita_time_management.html %}">Do I need to be a time management master to find 10 minutes a day for Spanish?<span aria-hidden="true">↗</span></a></li></ul><h3><a href="/en/breastfeeding-support/">Breastfeeding support</a></h3><ul class="article-list"><li><a href="/en/the-problem-is-powdered-formula/">The problem isn't the water, but the powdered formula<span aria-hidden="true">↗</span></a></li></ul><h3>Diary</h3><ul class="article-list"><li><a href="{% link en/denik_vasik_jako_fotbalista.html %}">Vasik as a footballer<span aria-hidden="true">↗</span></a></li></ul></dialog>
<dialog id="inspiration" aria-labelledby="inspiration-title"><button class="close" aria-label="Close">×</button><h2 id="inspiration-title">Inspiration</h2><ul class="inspiration-names"><li>Jiří Halda</li><li>Milan Studnička</li><li>Štěpánka Cimlová and Robert Čapek</li><li>Dalibor Špok</li><li>Margit Slimáková</li><li>Barbara Paldus</li></ul></dialog>
<dialog id="reading" aria-labelledby="reading-title"><button class="close" aria-label="Close">×</button><h2 id="reading-title">Reading</h2><h3>Education as a Theoretical Problem by Jiří Pelikán</h3><p style="line-height:1.7">This book explores how education shapes us, what we hope to achieve through it and the conditions that make this possible. It offers an academic reflection on the foundations of education and the relationship between educator and learner.</p></dialog>
<dialog id="offering" aria-labelledby="offering-title"><button class="close" aria-label="Close">×</button><h2 id="offering-title">Support</h2><div class="offer-copy">
<p class="about-label">Josefína Drbálková · journalist and mum</p>
<h3>Space for you and your experience of motherhood</h3>
<p>I offer supportive conversations about breastfeeding and motherhood: space for your questions, a listening ear and shared experiences.</p>
<p class="about-scope">I draw on my own experience of breastfeeding. I have no professional training or certification in lactation counselling. My support does not replace care from a lactation consultant or healthcare professional.</p>
<button class="support-contact" data-dialog="contact" aria-haspopup="dialog">Get in touch</button>
</div></dialog>
<dialog id="working" aria-labelledby="working-title"><button class="close" aria-label="Close">×</button><h2 id="working-title">My work</h2><div class="contact"><p>I'm Josefína Drbálková, a journalist.</p><p><a href="mailto:josefina.drbalkova@email.cz">Email me</a></p></div></dialog>
<script>
document.querySelectorAll('[data-dialog]').forEach(button=>button.addEventListener('click',()=>document.getElementById(button.dataset.dialog).showModal()));
document.querySelectorAll('dialog').forEach(dialog=>{
dialog.querySelector('.close').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});
});
</script>
{% include analytics.html %}
</body>
</html>
