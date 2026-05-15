Now I have a clear picture. Let me write the consolidated review.

## Summary

The paper addresses the problem that existing video models built on CLIP exhibit degraded out-of-the-box (zero-shot/linear probing) performance compared to their image-backbone counterparts. The authors diagnose the cause as "language supervision distortion" — end-to-end fine-tuning of the CLIP text encoder on noisy ASR transcripts causes it to overfit to language style, losing generalization ability and providing distorted supervision for the video encoder. They propose a simple solution: partially freeze the text encoder (shallow layers frozen, deep layers tunable), combined with the transcript sorting (TVTS) objective and tube masking (FLIP) for scalability. The resulting TVTSv2 models (up to 1B parameters) achieve state-of-the-art zero-shot results on several video retrieval and action recognition benchmarks.

## Strengths

- **Diagnoses and solves a real, underappreciated problem.** The paper convincingly shows (Table 1) that fully fine-tuning the text encoder on ASR transcripts degrades zero-shot performance below the frozen CLIP baseline, while partially freezing the shallow layers recovers and exceeds it. The ablation isolating text-encoder overfitting from domain-gap issues (comparing M₂-FT vs M₂-FF vs M₂-PF) is clean and informative.

- **Simple, effective, and efficient solution.** The partially frozen text encoder requires no additional modules or architectural changes. Combined with tube masking at high ratios (50–70%), the method scales to a 1B-parameter model trained on 8.5M videos with 80 V100 GPUs in one week — a practical and compelling efficiency result.

- **Strong empirical results across multiple benchmarks.** TVTSv2 achieves state-of-the-art zero-shot retrieval on MSR-VTT (+1.4% R@1 over prior dual-stream SOTA), DiDeMo (+6.9%), and LSMDC (+1.8%). On zero-shot action recognition, Ours-H/14 achieves 52.1% on HMDB-51 and 78.0% on UCF-101, surpassing ImageBind and X-Florence. The H/14 linear probing result (73.1% on K400, 91.8% on UCF-101) is genuinely strong among language-supervised video models.

- **Ablation studies verify each design choice.** The ablation of training objectives (Table 5) shows that both the VTC loss and the transcript sorting loss with stop-gradient are necessary. The sensitivity analysis of mask ratio and tunable layers (Figure 2) provides practical design guidance.

## Weaknesses

### Fatal
None.

### Major

- **Unspecified baseline for claimed "absolute gains" in zero-shot action recognition.** The paper states "Our model brings significant improvements, i.e., 8.9%, 9.1%, 11.6%, and 12.9% absolute gain on HMDB-51, UCF-101, Kinetics-400, and SSV2-MC, respectively" without stating what baseline these gains are computed against. Comparing against Table 3, these numbers do not consistently correspond to any single baseline — they match Ours-H/14 vs CLIP for HMDB/UCF/K400 (8.9, 9.1, 11.6) but not for SSV2-MC (where the actual gap vs CLIP is 18.8, not 12.9). For Ours-B/16 vs CLIP, the UCF gain is 0.9%, not 9.1%. This makes the reader unable to verify the claim, and it risks overstating improvements. The authors should explicitly state the baseline and report per-model gains.

- **Selective reporting of negative comparisons.** On UCF-101 zero-shot action recognition (Table 3), X-CLIP (72.0) outperforms Ours-B/16 (69.8), yet the paper claims "significant improvements" without mentioning this underperformance. The text also does not acknowledge that UMT-L ties or outperforms Ours-H/14 on LSMDC retrieval R@1 (20.0 vs 17.3 without DSL post-processing). While the overall results are still strong, these omissions erode confidence in the paper's framing.

- **Missing essential training hyperparameters.** The paper omits total training steps/epochs, batch size, optimizer type, learning rate schedule, warmup, weight decay, and the value of λ in the combined loss L = L_VTC + λ·L_TS. Given that training a 1B model with 80 V100s in one week is a significant logistical claim, these details are needed for reproducibility and fair comparison. The temperature parameter initialization and the exact training cost (total GPU-hours) are also missing.

### Minor

- **The partially frozen text encoder configuration is suboptimal relative to the paper's own ablation.** The paper uses a heuristic of freezing "the first three-quarters of layers" (L_tune = 3 for a 12-layer text encoder). However, Figure 3(b) shows that L_tune = 6 (tuning half the layers) achieves higher performance. The discrepancy is not acknowledged or explained. While the chosen heuristic clearly works better than fully frozen or fully fine-tuned, using the empirically optimal configuration would strengthen the results.

- **The "comparable to DINOv2-g" claim is overstated.** The paper states "surprisingly we achieve comparable performance to DINOv2-g on linear K400 with 40% fewer parameters." DINOv2-g achieves 78.4 vs Ours-H/14 at 73.1 — a 5.3-point gap on a 400-way classification task where differences of 1–2 points are typical among top methods. The gap is meaningful and the claim would benefit from more precise language (e.g., "competitive" rather than "comparable"). This does not undermine the core contribution but is a framing issue.

### Trivial
- None.

## Nice-to-Haves

- Evaluate on additional zero-shot tasks beyond classification and retrieval (e.g., video QA, temporal action localization) to broaden the "out-of-the-box" claim. The paper acknowledges this limitation in the conclusion.
- Report linear probing results for B/16 on HMDB-51 and UCF-101 alongside the H/14 results in Table 4.
- Include variance reporting (multiple runs) for key results.

## Removed Points

These points are flagged for removal — treat them with caution:

1. **Criticism about "missing" BridgeFormer/Frozen from Table 1:** These methods use alt-text only with frozen text encoders, so they are not directly relevant to the paper's study of degradation caused by fine-tuning text encoders on ASR transcripts. Table 1 is a controlled study of the degradation mechanism, not a general benchmark comparison.

2. **Claim that "the gap between VideoMAEv2-H and Ours-H/14 is 1.3 points":** Factually wrong. From Table 4, VideoMAEv2-H scores 25.8 and Ours-H/14 scores 73.1 on K400 linear probing — a 47.3-point gap. The 1.3 figure does not correspond to any comparison in the table.

3. **"Missing" evaluation on detection/segmentation:** The paper scopes its contribution to classification and retrieval (zero-shot and linear probing). Requesting additional task categories is scope creep, and the conclusion honestly acknowledges limitations.

4. **Figure 1 caption not described:** This is a parser artifact — the PDF extraction stripped the caption. The original submission has it.

5. **"Related Work" section not tightly connected:** Editorial preference, not a substantive weakness. The section covers relevant background.

6. **Criticism about CLIP-ViP being "not designed for zero-shot":** CLIP-ViP (ICLR 2023) explicitly evaluates zero-shot performance in its own paper and is standardly used as a zero-shot baseline in the literature.

7. **Request for Grad-CAM/attention map visualizations:** These are nice-to-have but not standard for retrieval/classification papers and not necessary to validate the core claims.

## Novel Insights

None beyond the paper's own contributions. The key insight — that text encoder overfitting to ASR transcript style (as opposed to semantic content) causes zero-shot degradation, and that partially freezing shallow layers preserves generalization while allowing adaptation — is genuinely novel and well-supported by the ablation study. The review process did not surface additional insights beyond what the paper itself articulates.

## Suggestions

1. **Specify the baseline** for the claimed absolute gains in zero-shot action recognition (line 419). Report per-model variant (B/16 and H/14) gains against a clearly named baseline, ideally breaking down by comparison (vs CLIP, vs CLIP-ViP, vs prior SOTA).

2. **Acknowledge the L_tune discrepancy** (heuristic L_tune=3 vs optimal L_tune=6 from Figure 3b). Either adopt the empirical optimum in the main experiments, or explain why the heuristic was preferred (e.g., validation on a different dataset, better generalization across architectures).

3. **Add training hyperparameters** (batch size, optimizer, learning rate schedule, warmup, weight decay, λ value, total steps/epochs, GPU-hours) to the implementation details or appendix.

4. **Replace or qualify the DINOv2-g comparison.** A 5.3-point gap on K400 linear probing is not "comparable"; use phrasing like "competitive" and report the exact gap.

5. **Add a sentence acknowledging X-CLIP's higher UCF-101 score** and contextualize it (e.g., X-CLIP is a single-stream model, or the gap narrows significantly at H/14 scale).

## Score and Decision

The paper has a genuine, well-supported core contribution — diagnosing text-encoder overfitting as the cause of zero-shot degradation and fixing it with a simple partial-freezing strategy. The experimental results are strong across multiple benchmarks, and the scaling recipe is practical. The weaknesses identified above are fixable with revisions: unclear baseline specification, selective reporting of one comparison, missing hyperparameters, a suboptimal default choice, and one overstated claim. None are fatal; the contribution survives intact.

I recommend **conditional acceptance** subject to the authors addressing the major weaknesses (specifying baselines, acknowledging the X-CLIP comparison, and providing missing training details).

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>