# Mamarafiki.cz — pokyny pro agenty

## Hlas autorky
- Zachovejte osobní a autentický hlas Josefíny: máma, která píše otevřeně, slušně a s citem pro styl.
- Zpřehledňujte myšlenky a strukturu bez vymýšlení osobních zážitků nebo tvrzení.
- Anglický text musí být úplným, přirozeným překladem českého originálu, nikoli shrnutím. Zachovejte míru jistoty, osobní perspektivu, zdroje, fotografie a jejich popisky.

## Povinný postup při přidání nebo změně obsahu
1. Každý veřejný článek, zápis do deníku a tematická stránka musí mít českou verzi v `cs/` i anglickou v `en/`. Anglickou verzi vytvořte automaticky v rámci stejného úkolu; nečekejte na zvláštní žádost.
2. Obě verze musí mít správné `lang: cs` / `lang: en` a shodný, jedinečný `translation_key` ve front matter. Použijte stabilní identifikátor, například název souboru bez přípony. Klíč `home` je vyhrazen úvodním stránkám.
3. Přeložte titulky, celý text, popis pro vyhledávače, viditelné datum, popisky a alternativní texty obrázků i navigaci. Pokud je uvedeno datum publikace, obě verze musí mít stejnou hodnotu `date`; nové datum nevymýšlejte.
4. Anglická stránka má mít anglické odkazy na související články, rubriky i návrat domů (`/en/`). Česká používá české protějšky a `/cs/`. Uvnitř webu preferujte Jekyll `link` tagy.
5. Přidejte český odkaz do seznamu na `index.md` i `cs/index.md` a anglický odkaz do `en/index.md`. Dodržte odpovídající rubriku a pořadí. Aktualizujte také související rubriky a odkazy v sériích.
6. Jazykový přepínač musí vést na překlad právě otevřené stránky, nikoli na úvod. Používejte společné include soubory `translation_targets.html`, `language_switcher.html` a `alternate_languages.html`; nepřidávejte samostatné pevně zadané přepínače. Úvodní stránky mají klíč `home`; kořen `/` zůstává českým rozcestníkem.
7. Zachovejte existující veřejné URL, včetně historických výjimek. Překlad propojujte klíčem, nikoli nahrazováním `/cs/` za `/en/` v adrese.
8. Před zveřejněním spusťte `python scripts/check_translations.py`. Opravte chybějící překlady, duplicity klíčů a chybné nebo chybějící odkazy. Kontrolu spouští také GitHub Actions.
9. Po nasazení ověřte na živém webu otevření nových stránek, přepnutí CS → EN → CS se zachováním článku, správný jazyk návratu domů a dostupnost článku z obou přehledů. Zkontrolujte vzhled na počítači i úzké obrazovce.

## Technické souvislosti
- Web používá Jekyll a GitHub Pages; sdílený vzhled článků je v `_layouts/default.html`.
- Přepínač hledá skutečnou adresu protějšku podle `translation_key`. Metadata `hreflang` používají stejné cíle.
- `index.md` a `cs/index.md` jsou české varianty téhož rozcestníku, `en/index.md` je jeho úplná anglická verze.
- Pokyny pro agenty a validační skripty nepatří do veřejného obsahu; ponechte je v `exclude` v `_config.yml`.

## SEO a strojová čitelnost bez změn vzhledu
- Každá jazyková verze potřebuje vlastní věcný `description`, správné `locale` a `seo.type`: články a deník `BlogPosting`, tematické přehledy `CollectionPage`, úvod `WebSite`.
- Metadata musí odpovídat skutečnému textu. Nevymýšlejte data publikace či aktualizace, odbornost autorky, recenze, hodnocení ani profily.
- Použijte existující obrázek článku jako `image` v metadatech včetně přeloženého `alt` a skutečných rozměrů, pokud jej článek obsahuje. Obrázky kvůli SEO nemusíte přidávat.
- V hlavičce musí být právě jeden SEO výstup (`{% seo %}`), sdílená metadata a jazykové alternativy. Neměňte CSS ani viditelný obsah při čistě technické SEO úpravě.
- Český kořen `/` má canonical na `/cs/` a `sitemap: false`; obě jazykové verze jinak mají vlastní canonical. Zachovejte existující URL.
- `sitemap.xml` automaticky zahrnuje stránky s `translation_key`, kromě `sitemap: false`. Nevkládejte do něj interní nástroje nebo umělá data změny.
- `robots.txt` umožňuje procházení veřejného obsahu a odkazuje na mapu webu. Zachovejte `noindex` interního Office. Robots.txt není ochrana soukromí.
- Spusťte také `python scripts/check_seo.py`; po nasazení lze ověřit živé stránky příkazem `python scripts/check_seo.py --live`.
