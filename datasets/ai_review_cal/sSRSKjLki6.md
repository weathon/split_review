- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 3, 5, 5
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

This paper proposes a **Prompt-Aware Adapter** for Multimodal Large Language Models, comprising a global attention component (injecting a prompt-level representation into the visual encoder via self-attention) and a local attention component (computing a text-patch similarity matrix with global normalization). The key insight is that existing cross-attention adapters force every word (including function words) to correspond to some visual region, while a globally-normalized similarity matrix avoids this unrealistic constraint. Controlled experiments on COCO-QA and MME show consistent gains over both prompt-unaware adapters (linear projection) and prompt-aware baselines (cross-attention, Q-Former) under the same backbone and training data.

---

## Strengths

1. **Clear diagnosis of a real limitation in cross-attention adapters.** Section 3.2 (lines 50–52, 157–164) identifies that row-wise softmax in cross-attention forces every word—including function words like "a", "the", "is"—to have total attention summing to 1 across patches. This is a well-motivated critique, and the proposed SOFTMAX over the full matrix (lines 194–196) is a principled alternative that avoids this unrealistic assumption.

2. **Consistent empirical gains in controlled comparisons.** Tables 2 (COCO-QA) and 3 (MME internal rows, lines 285–290) compare adapters under identical conditions (same backbone, same training data). The proposed method outperforms cross-attention on COCO-QA by +5.73% (object), +4.40% (count), +10.22% (color), +4.72% (position), and on MME perception the full model scores 1375.02 vs 668.29 for cross-attention. These are the fairest comparisons and they are strong.

3. **Ablation study validates both components independently.** Tables 4–6 (lines 396–441) show that removing either global attention or local attention degrades performance across nearly all metrics. For example, on MME perception total: full model 1375.02, w/o global 1284.49, w/o local 1217.97. Both components contribute positively.

4. **Attention visualizations support the "coarse-to-fine" design claim.** Figure 4 (lines 256–258) shows global attention maps highlighting entire prompt-relevant regions while local attention zooms in on specific objects, directly illustrating the claimed behavior.

---

## Weaknesses

### Fatal
None.

### Major

1. **Local attention equation is dimensionally inconsistent with the stated N-token output.** The paper explicitly states (line 215) "local attention generates N (the number of patches in the visual input) tokens." However, Eq. 4 (line 201) gives X' = MLP(a^T · I) where a ∈ R^{1×N} (line 203) and I ∈ R^{N×C_i}. The expression a^T · I is dimensionally incompatible as a matrix product — a^T is N×1 and I is N×C_i — and if interpreted as (1×N)·(N×C_i) by treating a as a column vector, it collapses to a single token (1×C_i), contradicting the stated N-token output. While the intended operation (weighting each patch by its row sum, preserving N tokens) is discernible from context, the equation as written is mathematically incorrect, impairing reproducibility. This must be corrected — either fix the dimensionality or clarify whether the operation is element-wise.

### Minor

2. **Mislabeled comparison in the experiments section.** Line 330 writes: "compared to prompt-unaware adapters, our method excels in both perception tasks (1375.02 vs 1299.79)." However, 1299.79 is the LRV-Instruction score — a full MLLM evaluated zero-shot, not a prompt-unaware adapter. The correct controlled comparison for perception would be against Linear✓ (557.82), Cross-Attention✓ (668.29), or the w/o-ablation variants. This mislabeling inflates the apparent gap.

3. **Abstract and text report percentage improvements that do not clearly correspond to numbers in the tables.** The abstract (line 59) states MME perception improves by 59.43% and cognition by 46.91%. These percentages do not cleanly match any baseline comparison in the tables. (For perception: (1375.02 − X)/X = 59.43% gives X ≈ 862, which doesn't appear in Table 1. The prompt-unaware baseline 557.82 gives a 146.5% improvement.) Similarly, the COCO-QA percentages (7.71%, 18.42%, etc.) do not match relative or absolute gains against Linear✓ in Table 2. The claimed gains are therefore unverifiable from the presented data.

4. **Table 1 mixes zero-shot and controlled comparisons without adequate visual separation.** Rows 272–283 (MiniGPT-4 through InstructBLIP) are zero-shot evaluations, while rows 285–288 (Linear✓ through Cross-Attention✓) are fine-tuned controlled comparisons. The caption (line 266) does not indicate this distinction, and the section text only clarifies it belatedly (lines 301–302). An uncareful reader could interpret the raw score comparisons (e.g., 1375.02 vs 1299.79 for LRV-Instruction) as direct competition, when the proposed method benefits from task-specific training that the comparison models did not receive.

5. **Q-Former fine-tuning anomaly is not discussed.** In Table 3 (MME cognition, lines 357–358), fine-tuning the Q-Former reduces performance from 210.31 (frozen Q-Former) to 90.95 (fine-tuned). A similar drop occurs on COCO-QA (49.73% → 29.67% in Table 2). This suggests catastrophic forgetting or negative transfer, and the paper does not acknowledge or explain why the proposed method avoids this issue. Addressing this would strengthen the paper's claims.

6. **"LRV-Instruction" listed as a method in Table 1 (line 278).** LRV-Instruction is a dataset/training strategy, not a model. The entry should reference the specific model variant (e.g., LRV-Instruction-tuned LLaVA or similar).

7. **Output token counts for baseline adapters are not stated.** The paper never specifies how many visual tokens Linear projection, Q-Former, or Cross-Attention produce. This makes it difficult to assess whether performance differences could partly reflect representational capacity (number of tokens) rather than adapter quality.

### Trivial
None.

---

## Nice-to-Haves

- The global attention component injects a prompt token into a frozen visual encoder and runs self-attention, but only the projection layers for the global token are learned. Since the EVA-CLIP self-attention layers were never trained on such injected tokens, a brief justification or ablation showing that this design is preferable to a learnable cross-attention layer would be helpful.
- A brief limitations paragraph discussing computational overhead, whether the dual attention adds latency, and potential failure cases (e.g., noisy or ambiguous prompts) would improve completeness.
- The softmax vs SOFTMAX notational distinction (lines 157, 194) is clear in context but could be made more robust with superscripts to avoid confusion, especially when skim-reading.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- Harsh critic's claim that the output token inconsistency is "structural" / "fatal": The intended behavior (weighting each patch by its row sum to produce N tokens) is clearly stated in the text (line 215) and Fig. 3 caption (line 135). The equation has a notational error, but the intended operation is discernible. Demoted from Fatal to Major.
- Harsh critic's claim that the abstract "cites the MME total score (1375.02 vs. 1299.79) without noting this apples-to-oranges comparison": The abstract does not cite 1299.79; it reports percentage improvements. The 1375.02 vs 1299.79 comparison appears only in the Experiments section (line 330), where it is indeed mislabeled — but this is already captured in Weakness #2 above.
- Strength Finder's strength #4 (attention visualizations): Kept — it is specific and grounded, no conflict with verified weaknesses.
- Strength Finder's generic strength about "addressing an important problem": Not present in the outputs; all four strengths are specific and evidence-grounded.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface presentation and notation issues but do not reveal any flaw or insight that fundamentally changes the paper's contribution.

---

## Suggestions

1. **Fix the local attention equation.** State the exact operation that preserves N tokens. If it is element-wise weighting (each row of I scaled by a_i), write it as `X'_i = a_i · I_i` or use `diag(a) · I` with the correct dimensionality.

2. **Clarify the text in line 330.** If comparing to the prompt-unaware baseline (Linear✓), give those numbers explicitly (1375.02 vs 557.82). If comparing to LRV-Instruction, label it as a zero-shot competitor, not a "prompt-unaware adapter."

3. **Correct or explain the abstract's percentage improvements.** Ensure every claimed percentage in the abstract can be directly verified from a table row. If the baseline is not Linear✓, state which baseline.

4. **Separate zero-shot and controlled comparisons in Table 1**, either with explicit row-block labels or in separate tables. Add a note in the caption indicating which rows are zero-shot.

5. **Discuss the Q-Former fine-tuning collapse** in the experiments section.

6. **Replace "LRV-Instruction" with the actual model name** in Table 1.

7. **State output token counts** for all adapter variants (Linear, Q-Former, Cross-Attention, Ours) to enable capacity-aware comparison.

---
