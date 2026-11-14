#!/bin/zsh
cd ~/career-hack-lp
claude -p "qc/ADDENDUM.md（追加指示2の画像生成フローを含む）を読み直して取り込み、qc/PROMPT.md のタスクをこれまでの続きから最後（qc/DONE.md 作成と design-polish への push）まで完遂してください。採点は QC_RUBRIC.md の30項目で。" --resume 0a44ec03-7f6b-4088-ba59-4777f19d3200 --model opus --dangerously-skip-permissions --output-format stream-json --verbose > qc/run3.jsonl 2> qc/run3.err
echo "EXIT $?" >> qc/run3.err
