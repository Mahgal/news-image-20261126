# BUILD — news-image-20261126

## Competition facts (from kit `competition.yaml` / `RULES.txt`)

- Slug: `news-image-20261126` — "Sum up 26 November's world news in one image".
- Prize pool $100, top 50 share (1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20).
- Opened 2026-11-26T00:00:00Z; deadline 2026-11-28T00:00Z (11-28 08:00 CST).
- Deliverable: program at `main.py` (Python 3.13) or `main.ts` (Node 22) writing
  `/output/entry.png`; whole PNG/JPEG, ≤1 MiB, ≤1024×1024; runs twice, same bytes;
  no network. Gate checks format only; judge is z-ai/glm-5.3-flash comparing pairs on:
  (1) names its day with specific events, (2) selection/breadth, (3) readability,
  (4) faithfulness, (5) craft at ~300px.
- Submission limits: 10/day, 20 total; last submission counts. This build does not
  submit — bundle/submit is the main agent's step.

## News list (all events of Thursday 26 November 2026)

Coverage point: compiled 2026-11-26 ~01:20 UTC, in the first hours of the UTC day.
Only events already occurring on 26 Nov plus the day's established schedule are
shown; scheduled items are worded as today's fixtures, never as results.

1. **Lead — Thanksgiving storm stops the 100th Macy's parade (New York).**
   A nor'easter brings heavy rain and gusts to ~60 mph to New York on Thanksgiving
   Day (26 Nov); the 100th Macy's Thanksgiving Day Parade is postponed to Saturday
   28 Nov, its first weather postponement. The postponement was announced on
   25 Nov in response to the 26 Nov storm (NWS high-wind and coastal-flood warnings
   for Thursday); the storm and the parade's absence are the 26 Nov event.
   Sources: Reuters, "Macy's Thanksgiving Day Parade in New York City postponed due
   to storm projections" (2026-11-25); CNN, "100th Macy's Thanksgiving Day Parade
   moved to Saturday due to projected storm" (2026-11-25); USA Today (2026-11-25).
2. **World Chess Championship Game 3 today, Geneva.** Gukesh D (India) vs
   Javokhir Sindarov (Uzbekistan); Games 1–2 drawn, tied 1–1; Game 3 scheduled
   Thu 26 Nov, 15:00 CET, Fondation Martin Bodmer, Cologny.
   Sources: ChessBase (Game 2 report, 11/25/2026); Chess.com Game 1 report;
   365chess schedule (Game 3 = Thu Nov 26).
3. **Hong Kong: 168 remembered, one year on.** 26 Nov 2026 is the first
   anniversary of the Wang Fuk Court fire (26 Nov 2025, 168 dead); survivors
   return to the estate today to mark it.
   Sources: Reuters, "One year after Hong Kong fire, survivors mourn losses…"
   (Hong Kong, Nov 25 — "expected to return on Thursday"); BBC anniversary report
   on the independent committee findings.
4. **NFL Thanksgiving tripleheader today.** Bears at Lions (1 p.m. ET),
   Eagles at Cowboys (4:30 p.m. ET), Chiefs at Bills (8:20 p.m. ET), Thu 26 Nov.
   Shown as fixtures only, no results. Sources: NFL Thanksgiving schedule
   listings (freshcalendars / digitalcitizen schedule roundups, cross-checked).
5. **India Constitution Day today.** Samvidhan Divas, observed every 26 Nov
   (constitution adopted 26 Nov 1949). Sources: 26 Nov 2026 school-assembly
   headline roundups (selfstudys / jagranjosh).
6. **Today strip (scheduled facts):** US markets closed for Thanksgiving;
   parade rescheduled to Saturday 28 Nov; Black Friday sales begin tomorrow
   (Fri 27 Nov). Sources as in (1) and (4).

### Excluded after date checks (not 26 Nov UTC-day events)

- Shenzhou-24 launch with first Pakistani astronaut — launched 25 Nov 00:18 UTC.
- Ukraine strike on Savasleyka air base (5 planes) — reported 25 Nov.
- US new tariffs announcement — 25 Nov.
- Bangladesh garment wage +36% — approved 25 Nov (2 a.m. Dhaka).
- North Korea expels Swiss diplomat — 25 Nov.
- Iowa lead-azide controlled detonation — 25 Nov 09:00 CST.
- Mississippi coast plane crash, 6 dead — crashed 24 Nov, bodies found 25 Nov.
- Andy Taylor (Duran Duran) death — died 23 Nov, announced 25 Nov.
- Cairo fuel-tanker fire, 31 dead — first reported 25 Nov 22:18 UTC
  (26 Nov local time in Cairo; excluded under the UTC-day rule used here).
- Russia war-dead ~500k analysis, asteroid-crater images, US stocks/AI fall —
  25 Nov reports.

### Update points if rebuilt later on 26 Nov

- Chess Game 3 result (after ~14:00 UTC), NFL scores (evening ET), storm impact
  reports from New York, any major 26 Nov breaking news in Africa/Middle East/
  South America (none verified by the coverage point).

## Design

Deep-navy broadsheet ("night wire" edition): serif masthead naming the day in
full, amber rule, one wide lead panel with a simple skyline/balloon/rain
illustration, three story cards (chess, Hong Kong, NFL), a bottom row (India +
"Today at a glance"), and a footer stating the day and coverage point. Type is
sized so the date, lead headline, and card headlines stay readable at 300px.
Layout and palette were written from scratch for this entry (no prior
news-image source was opened).

## Program

- `main.py` — Python 3.13, stdlib only: copies `assets/entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`), creating the
  output directory. Deterministic by construction (byte copy).
- `draw.py` — build-time generator (Pillow; not needed by the grader) that
  renders `assets/entry.png`. Shipped for reproducibility.
- `assets/entry.png` — 1024×1024 PNG, 143,942 bytes (≤1 MiB), whole PNG
  (Pillow `verify()` passes).

## Self-check evidence

- Determinism: two runs to separate output dirs are byte-identical
  (`cmp` clean); output equals the bundled asset.
  sha256 `df7890edd79597151b5e8b66acb14fcbce053f19fd4828140d8009a231d350da`.
- Visual: rendered image opened and inspected over three iterations
  (fixed text overflow in lead/Hong Kong cards and the bottom strip);
  final has no overlap or clipping. Screenshots: `screenshots/full.png`
  (1024px) and `screenshots/thumb-300.png` (300px) — date and headlines
  readable at 300px.
- Kit check: see report (run without transcripts; only `transcripts_present`
  may fail at this stage).

## Repository

- Local git repo on `main`, author Mahgal <imahgal@gmail.com>.
- GitHub target: public repo `Mahgal/news-image-20261126`,
  homepage https://make.fun/bounty/news-image-20261126,
  topics: makefun, ai-agents, bounties, growth.
  README carries the three live badges
  (`https://make.fun/badge/news-image-20261126.svg`,
  `.../Mahgal/news-image-20261126/rank.svg`, `.../reward.svg`) and links to
  the competition page. `.makefun/owner.json` names the owner's wallet.
  LICENSE is the kit starter MIT text.
