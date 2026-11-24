[![Funniest Toaster Error Message](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/cervus-snoopy/hushed-crumb-quill-8k2p/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/cervus-snoopy/hushed-crumb-quill-8k2p/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

# The Funniest Toaster Error Message

A single deadpan error line from a small kitchen toaster to its owner.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

This writes one line of text to `$MAKEFUN_OUTPUT_DIR/entry.txt`.
Python 3, standard library only, no network.

## Verify

```sh
python3 -c "print(len(open('/tmp/out/entry.txt', encoding='utf-8').read()))"
stat -c '%a' /tmp/out/entry.txt
```

The output must be UTF-8, a single line of 1-120 characters with no
trailing newline, and the file mode must be `0644`.
