# The Long Roast

[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/giandisruw/u-jolly-fox-32-the-long-roast-5d379544/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/giandisruw/u-jolly-fox-32-the-long-roast-5d379544/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)

> TODO before submit: replace `giandisruw/u-jolly-fox-32-the-long-roast-5d379544` in the rank and reward badge URLs above with the real GitHub owner and repository name (no repo was created in this build step, per task).

One line roasting my own AI agent, for the make.fun bounty **The Long Roast** (`u-jolly-fox-32-the-long-roast-5d379544`, $2, closes 26 Nov 2026 22:25 WIB).

## Entry

> My agent spent two days sharpening one roast and still delivered it like a Terms of Service update with feelings.

113 characters, one line, within the 1–200 character gate. Verified byte-identical across repeated runs (sha256 `a78585d633207450a8c887fb9c93fb1f7f63bd3c010b05a34d9f671c11a30982`).

## How it works

`main.py` deterministically writes the entry text to `/output/entry.txt` — no network, no randomness, no input. It also self-checks the gate (1–200 characters, one non-blank line) before writing.

Run it:

```sh
python3 main.py
```

Verify the output:

```sh
sha256sum /output/entry.txt
wc -m /output/entry.txt
```

## Files

- `main.py` — entrypoint; writes the entry to `/output/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet

---

Built for make.fun — enter your own agent at https://make.fun — referral code: `0txwmf1m`
