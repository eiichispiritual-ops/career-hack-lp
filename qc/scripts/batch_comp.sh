#!/bin/zsh
cd ~/career-hack-lp/qc
while IFS='|' read -r n u; do
  [ -z "$n" ] && continue
  [ -f "specs/$n.json" ] && { echo "skip $n"; continue; }
  python3 scripts/spec_shoot.py "$n" "$u" 2>&1 | tail -1
done < "$1"
