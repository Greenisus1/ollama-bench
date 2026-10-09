# ollama-bench

Which of your local Ollama models is actually fastest on your hardware? One file, Python standard library only.

It runs the same short prompt on every installed model and prints a table of tokens per second, sorted fastest first. Handy on a Raspberry Pi, where the gap between a 1B and an 8B model is huge.

## Run

    wget -O ollama-bench.py https://raw.githubusercontent.com/Greenisus1/ollama-bench/main/ollama-bench.py
    python3 ollama-bench.py

Options: `--models a,b` to pick models, `--tokens 128` for longer runs, `--host` for another machine.

Example output:

    model                          tokens/s   tokens  load (s)
    llama3.2:1b                       9.80       64       2.1
    qwen3:8b                          2.10       64      18.4

## Tip

Post your numbers in the issues so we can build a Pi 5 leaderboard.

## License

MIT

## Fullscreen Store launch

Version 1.0.1 adds a full-terminal interface when launched through the Store. Python 3 with curses and an interactive terminal are required. The original source remains available directly. Interactive output wraps and scrolls with PgUp/PgDn. Enter returns after completion. Arguments on `bash app-store.sh run` retain the original command-line path. No administrative/package/transfer action ran during validation. Linux terminal checks passed; physical Raspberry Pi and non-Linux systems are untested.
