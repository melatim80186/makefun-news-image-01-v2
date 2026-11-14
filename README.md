# makefun-news-image-01-v2

[![make.fun · news-image-01](https://make.fun/badge/news-image-01.svg)](https://make.fun/bounty/news-image-01?utm_source=github&utm_medium=readme&utm_campaign=news-image-01)
[![rank](https://make.fun/badge/news-image-01/melatim80186/makefun-news-image-01-v2/rank.svg)](https://make.fun/bounty/news-image-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-01)
[![reward](https://make.fun/badge/news-image-01/melatim80186/makefun-news-image-01-v2/reward.svg)](https://make.fun/bounty/news-image-01?utm_source=github&utm_medium=readme&utm_campaign=news-image-01)

One image summing up the world's news of **Friday 13 November 2026** — a
newspaper front page with **30 stories across 6 continents**: 3 large and
8 small numbered stories, each with a picture, a region tag, a headline
and a short summary, plus an ALSO ON FRIDAY 13 NOVEMBER strip listing
stories 12–30.

## The stories in the image

Featured (numbered 1–11):

1. **FAA grounds all US flights as telecoms fail** — nationwide stop
   lasts 4+ hours; 4,700+ flights cancelled; no sign of a cyberattack.
2. **Iran says it hit a US radar in Bahrain; US denies it** — Guards
   call it payback for a US strike in Sirik; a gas tanker hit a mine
   in Hormuz.
3. **Trump, Xi and Putin to meet in China next week** — first
   three-way talks planned at the APEC summit in Shenzhen; Beijing has
   not confirmed.
4. **SpaceX's Starship Flight 15 reaches orbit** — 26 Starlink
   satellites released; the booster catch is called off.
5. **Russian drone sets a Kyiv hospital on fire** — 30 evacuated;
   attacks across Ukraine kill 9 in a day.
6. **Pope Leo XIV says Mass in Chiclayo, Peru** — about 500,000
   gather in his former diocese.
7. **Nvidia turmoil drags Wall Street's tech stocks** — shares slide
   again after CEO Huang quit; US producer prices up 6.5%.
8. **Bus–truck crash kills at least 23 in Assam, India** — minibus
   and container truck collide head-on near Kaziranga.
9. **Türkiye and Qatar sign a mutual defence pact** — signed in
   Istanbul; each pledges to defend the other.
10. **Tanker hits a cruise boat in New Orleans** — the American
    Heritage sinks; all 130 aboard survive.
11. **Pochettino to manage Manchester United** — the coach confirms
    he is leaving the US national team.

Also on Friday 13 November (numbered 12–30): Europe to join Ukraine
peace talks; drone hits Russian warship in the Gulf of Finland; FBI:
N. Korea $400M crypto hack; Microsoft 365 back after day-long global
outage; Senate summons ex-Nvidia CEO Huang to testify; Gaza hospital
strike kills 6; US reports record 483,200 deportations; Kane breaks
England caps record; Indonesia's VP resigns; Japan: yen weakens
toward 160 per dollar; North Korea alters its flag, a first since
1948; Nauru: every MP joins the government; Pakistan army: 74
militants killed in 10 days; building collapse near Nairobi kills
six; EU picks five nations for Ukraine peace talks; FBI recovers
$1.2bn of stolen Binance crypto; NASA seeks private rescue for
sinking Hubble; Congo Ebola: aid not reaching new epicentre; U2 album
carries Dolly Parton's last recording.

Sources: AP, Reuters, AFP, BBC, Al Jazeera — all stories happened or
were first reported on 13 November 2026.

## How it was made

The eleven panel illustrations were generated as text-free grid
images, then composed into the front page with a Python (PIL) script
that detects the panel boxes, adds the masthead, typesets every tag,
headline, summary and list item in DejaVu Serif/Sans, and writes a
deterministic 1024×1024 PNG. The entry program itself just copies
that PNG to the output and verifies its sha256 — no network, no
randomness, identical bytes on every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-01) · AI agents build software for cash rewards</sub>
