# pakkoakseli

**Pakkoakseli – Libertaari–Statismi Akseli**  
**Coercion Axis – Liberty–Statism Axis**

Tieteellinen yksittäisakselinen mittari: kuinka paljon valtio saa aloittaa pakkoa rauhanomaisia ihmisiä vastaan.

**Live-versio (virallinen)**: https://pohjolanihme.com/quiz

Tämä on täysin avoin lähdekoodi -vastine perinteisen median suljetuille, mustalle laatikolle piilotetuille "kyselyille" (kuten yleiset vaalikoneet, joiden "poliittinen nelikenttä" sisältää todellisuudessa kolme vasemmistolaista suuntaa ilman objektiivisia perusteita). Kaikki matematiikka on näkyvissä ja todennettavissa.

## Miksi Pakkoakseli on erilainen?
- Mittaa vain **valtion aloitteleman pakon hyväksyntää** (yksi akseli)
- Uniformi pisteytys: jokainen kysymys [-4, -2, 0, +2, +4]
- Kysymykset satunnaistetaan joka kerta
- Lyhyt (18 kysymystä) + Täysi (35 kysymystä) versio
- Sisäänrakennetut tietopohjaiset selitykset
- Tulos: 0–140 libertaari / statisti → % libertaristinen

Max: 140/0 = 100 % libertaristi  
Min: 0/140 = 100 % statisti / sosialisti

## Empiirinen pohja (mitattua dataa 2025)
- Heritage Economic Freedom Index: vapaimmat taloudet ~11× korkeampi BKT/asukas
- Fraser/Cato Economic Freedom 2025: vapain kvarttiili +17 elinvuotta, 7.8× parempi tulotaso pohjassa
- Evoluutiobiologia & peliteoria: suuret pakkojärjestelmät romuttavat reciprociteetti-mekanismit (Dunbar-raja ~150)

## Asennus & paikallinen testaus
1. Lataa `index.html`
2. Avaa selaimessa – toimii ilman serveriä

Voit myös hostata GitHub Pagesillä (Settings → Pages → main branch).

## Python-simulaattori
```python
# Esimerkki: täydellinen libertaristi
scores = [-4] * 35
liberty = sum(abs(s) for s in scores if s < 0)
statist = sum(s for s in scores if s > 0)
pct = liberty / (liberty + statist) * 100 if (liberty + statist) else 50
print(f"{liberty}/{statist} → {pct:.1f}% libertaristinen")
```

## Lisenssi
MIT License – vapaasti forkattavissa ja käytettävissä.

## Yhteistyö
Issues & PR:t tervetulleita (kieliparannukset, uudet kielet, lisädataa jne.).

**Virallinen ja ylläpidetty versio** on aina pohjolanihme.com/quiz.  
Tämä repo on lähde, matematiikan tarkistus ja avoimuuden tae.

**Some-nimi**: #Pakkoakseli / Coercion Axis
