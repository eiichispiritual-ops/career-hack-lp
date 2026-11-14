#!/bin/zsh
cd ~/career-hack-lp
claude -p "$(cat qc/PROMPT.md)" --model opus --dangerously-skip-permissions --output-format stream-json --verbose > qc/run.jsonl 2> qc/run.err
echo "EXIT $?" >> qc/run.err
