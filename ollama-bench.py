#!/usr/bin/env python3
"""ollama-bench: how fast is each of your local Ollama models on this machine?
Pure Python standard library. Prints a table of tokens/second.
Usage: python3 ollama-bench.py [--host http://127.0.0.1:11434] [--models a,b] [--tokens 64]"""
import argparse, json, sys, urllib.request

PROMPT = "Explain in three sentences why the sky is blue."

def call(host, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(host + path, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        return json.loads(r.read())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="http://127.0.0.1:11434")
    ap.add_argument("--models", default="")
    ap.add_argument("--tokens", type=int, default=64)
    a = ap.parse_args()
    try:
        names = [m["name"] for m in call(a.host, "/api/tags")["models"]]
    except Exception as e:
        sys.exit("Cannot reach Ollama at %s: %s" % (a.host, e))
    if a.models:
        names = [n for n in a.models.split(",") if n]
    if not names:
        sys.exit("No models installed. Try: ollama pull llama3.2:1b")
    rows = []
    for n in names:
        print("Testing %s ..." % n, flush=True)
        try:
            r = call(a.host, "/api/generate", {"model": n, "prompt": PROMPT, "stream": False,
                     "think": False, "options": {"num_predict": a.tokens}})
            tps = r["eval_count"] / (r["eval_duration"] / 1e9)
            load = r.get("load_duration", 0) / 1e9
            rows.append((n, tps, r["eval_count"], load))
        except Exception as e:
            rows.append((n, None, 0, 0))
            print("  failed: %s" % e)
    rows.sort(key=lambda x: -(x[1] or 0))
    print("\n%-28s %10s %8s %9s" % ("model", "tokens/s", "tokens", "load (s)"))
    for n, t, c, l in rows:
        print("%-28s %10s %8d %9.1f" % (n, "%.2f" % t if t else "failed", c, l))

if __name__ == "__main__":
    main()
