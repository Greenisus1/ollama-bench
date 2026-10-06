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
