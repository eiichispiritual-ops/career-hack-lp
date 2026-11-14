#!/bin/zsh
cd ~/career-hack-lp
claude -p "PMレビュー qc/PM_FEEDBACK.md を読み、指摘6点をすべて反映してください（自己採点が甘いのでこれらはFAIL扱い）。修正→再撮影→横並べ比較→ qc/score_round4.md で30項目を厳しく再採点→必要ならさらにラウンド→ final/ と compare/final_*.png と DONE.md を更新→ commit して git push origin design-polish。main には触れない。config.js 変更禁止、捏造禁止、電話表現はやわらかく。" --resume 0a44ec03-7f6b-4088-ba59-4777f19d3200 --model opus --dangerously-skip-permissions --output-format stream-json --verbose > qc/run4.jsonl 2> qc/run4.err
echo "EXIT $?" >> qc/run4.err
