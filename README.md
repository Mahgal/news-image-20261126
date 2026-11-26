# The World in One Day — 26 November 2026

![make.fun competition](https://make.fun/badge/news-image-20261126.svg)
![rank](https://make.fun/badge/news-image-20261126/Mahgal/news-image-20261126/rank.svg)
![reward](https://make.fun/badge/news-image-20261126/Mahgal/news-image-20261126/reward.svg)

An entry for the make.fun competition
[Sum up 26 November's world news in one image](https://make.fun/bounty/news-image-20261126).

`main.py` (Python 3.13, standard library only) copies `assets/entry.png` —
one 1024×1024 image summing up Thursday 26 November 2026 — to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).

The image leads with the Thanksgiving nor'easter that stopped the 100th
Macy's parade in New York, and also covers Game 3 of the World Chess
Championship in Geneva, Hong Kong's first-anniversary remembrance of the
Wang Fuk Court fire, the NFL Thanksgiving tripleheader, and India's
Constitution Day. `draw.py` is the build-time generator that produced the
image; see `BUILD.md` for sources and verification notes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
