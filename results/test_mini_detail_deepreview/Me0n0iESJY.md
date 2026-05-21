Let me carefully compute the averages to verify the critic's claims.

Table 3 (WUDI Merging on Qwen2-VL): 37.19 + 56.45 + 42.96 + 27.63 + 67.34 + 82.54 + 65.56 + 79.72 + 68.34 + 71.99

Sum = 37.19+56.45+42.96+27.63+67.34+82.54+65.56+79.72+68.34+71.99

Let me add: 37.19+56.45=93.64, +42.96=136.60, +27.63=164.23, +67.34=231.57, +82.54=314.11, +65.56=379.67, +79.72=459.39, +68.34=527.73, +71.99=599.72

599.72/10 = 59.97 — but the table states 63.65. Confirmed discrepancy.

Table 3 (OptMerge on Qwen2-VL): 41.61+62.16+48.66+40.79+74.08+81.54+60.06+80.92+65.50+78.23
= 41.61+62.16=103.77, +48.66=152.43, +40.79=193.22, +74.08=267.30, +81.54=348.84, +60.06=408.90, +80.92=489.82, +65.50=555.32, +78.23=633.55
633.55/10 = 63.36 — table states 63.30. Close enough (rounding).

Table 2 (WUDI on InternVL2.5): 31.02+56.96+53.03+17.11+69.19+75.95+46.12+76.06+70.14+74.48
= 31.02+56.96=87.98, +53.03=141.01, +17.11=158.12, +69.19=227.31, +75.95=303.26, +46.12=349.38, +76.06=425.44, +70.14=495.58, +74.48=570.06
570.06/10 = 57.006 — table states 57.00. ✓

OK so the issue is specifically with WUDI's average in Table 3. Let me now write the final review.Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper introduces a model merging benchmark for Multimodal LLMs (MLLMs) with fine-grained task categorization across five capabilities (VQA, Geometry, Chart, OCR, Grounding) and three modalities (vision, audio, video). It also proposes OptMerge, which adds low-rank denoising and improved optimization (SGD + mean initialization) to the WUDI Merging framework. Experiments on InternVL2.5-1B and Qwen2-VL-7B show modest improvements over prior merging methods, and the benchmark includes evaluation on real Hugging Face checkpoints and larger-scale models.

## Strengths

1. **Comprehensive MLLM model merging benchmark with careful construction**: The paper constructs expert models across five distinct capabilities using at least 100k training samples per task, across two base model families (InternVL2.5 and Qwen2-VL) and two fine-tuning paradigms (full FT and LoRA). This is currently the most comprehensive benchmark specifically designed for evaluating model merging methods on MLLMs, with clear task divisions that prior work (AdaMMS, UQ-Merge) lacked. The benchmark also includes modality merging (vision-language, audio-language, video-language), which is a relatively unexplored direction.

2. **Systematic ablation study isolating component contributions**: Table 4 clearly decomposes the effect of each design choice (SGD, mean initialization, low-rank approximation), showing that SGD alone hurts performance (−9.77%) but combining it with mean initialization (+4.43%) and low-rank approximation (+4.65%) yields net gains. This provides genuine insight into why the method works.

3. **Large-scale validation on 32B model and real-world checkpoints**: Table 9 demonstrates OptMerge works on Qwen2.5-VL-32B-Instruct (72.52 average, outperforming all individual experts and the base Instruct model), and Table 6 evaluates on actual Hugging Face checkpoints from different developers, demonstrating practical applicability beyond controlled settings.

4. **Theoretical analysis of fine-tuning dynamics**: Theorem 3.1 provides an upper bound on merging error that separates convergence residual, cross-task interference, and curvature terms, offering a theoretical grounding for why less intensive fine-tuning can yield better merging — even if the proof is deferred to an appendix.

## Weaknesses

### Major

1. **Numerical inconsistency in Table 3 undermines confidence in reported results**: The stated average for WUDI Merging in Table 3 (63.65) does not match the individual per-metric values. Computing the average of the 10 individual numbers (37.19, 56.45, 42.96, 27.63, 67.34, 82.54, 65.56, 79.72, 68.34, 71.99) yields ~59.97, not 63.65. Table 4 reports 58.65 for the same condition, which is much closer to the computed value. This discrepancy means the central comparison between WUDI and OptMerge in Table 3 cannot be trusted as presented. The paper does not explain this discrepancy or the averaging procedure. Until resolved, the claim that OptMerge provides a meaningful improvement over WUDI in the LoRA setting is unsubstantiated.

2. **Overclaimed comparison with mixture training**: The paper states "model merging potentially surpasses mixture training" as a key finding. However: (a) On InternVL2.5, mixture training achieves 57.66 while OptMerge achieves 57.44 — mixture training is actually better. (b) For Qwen2-VL, the "mixture training" baseline is Qwen2-VL-Instruct, which was trained on an unknown, likely much larger, and differently constructed data mixture — not a mixture of the same task-specific data. This is not an apples-to-apples comparison, so the claim that merging "surpasses" mixture training is not supported by the evidence presented. The claim should be substantially softened or removed.

### Minor

3. **Incremental method contribution with modest gains**: OptMerge adds two components to WUDI Merging (SGD + mean initialization, low-rank approximation). The gains over WUDI are modest across settings: +0.44% on InternVL2.5 (Table 2), ~1.9% on Hugging Face checkpoints (Table 6), and the modality merging result (67.00 vs. TSV Merging's 67.34) is actually worse. The 2.48% average improvement claimed in the abstract is not clearly tied to any specific table or calculation. No statistical significance is reported. Given that WUDI Merging was published in 2025, the methodological advance here is incremental.

4. **The "first benchmark" claim overstates novelty**: The paper claims "the first model merging benchmark for MLLMs." Prior works (AdaMMS, UQ-Merge, UniVAL) have evaluated merging methods on MLLMs, even if with different categorizations and scope. The paper acknowledges these works in Section 2, which partially mitigates this issue, but the claim in the abstract and contributions remains stronger than appropriate. A more accurate framing would be "the first benchmark with fine-grained capability categorization for MLLM merging."

5. **Mixture training baseline for Qwen2-VL is not fairly constructed**: The paper uses Qwen2-VL-Instruct as an upper bound for mixture training, but it does not do mixture training on the same task data. This makes it impossible to conclude whether the gap is due to data quantity/quality differences or inherent advantages of merging. A proper baseline would train a model on the same task-specific data used for expert models.

### Trivial

6. **Averaging procedure across evaluation metrics is not clearly specified**: Tables 2, 3, 6, and 8 each average over 10 metrics across 5 task categories, but it is unclear whether this is a simple average of all 10 metrics, a macro-average across categories, or something else. Different procedures could produce slightly different numbers.

## Nice-to-Haves

- Adding confidence intervals or bootstrap estimates for the main comparisons would strengthen confidence in the results, especially given the small margins.
- A clearer justification for the choice of k ratio (rank divided by number of tasks) in the low-rank approximation, beyond the ablation showing robustness.
- A discussion of limitations of model merging (e.g., sensitivity to base model choice, interference with many experts) would improve the paper.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic: "Code and checkpoints cannot be verified"** — Removed per hard rule: criticisms questioning the existence/release status of cited resources are not allowed.
- **Harsh critic: "Proof in the appendix cannot be evaluated"** — Removed per hard rule: missing appendix content is a parser artifact, not an author error.
- **Harsh critic: "Missing related works"** — Removed per hard rule: the reviewer cannot confirm which works are missing.
- **Harsh critic: "Method needs statistical significance"** — Downgraded from Major to Nice-to-Have: requesting confidence intervals is reasonable but not standard practice for this type of benchmark evaluation in the field.
- **Strength Finder: "Model merging surpasses mixture training in several scenarios"** — Removed as a strength because it conflicts with verified weaknesses #2 and #5: the evidence does not support this claim.
- **Strength Finder: "OptMerge outperforms existing methods across multiple settings"** — Weakened: the numerical inconsistency makes this claim unverifiable in the LoRA setting.
- **Strength Finder generics** about "important problem" — Removed per filtering instructions.

## Novel Insights

None beyond the paper's own contributions. The key tension the reviews surface is between a genuinely useful benchmark contribution and an incremental method whose reported results contain a verifiable numerical inconsistency that undermines trust in the central empirical claims. The benchmark itself — with its careful task categorization, two model families, two fine-tuning paradigms, and public release — is the paper's strongest asset, while the method and the overclaimed comparisons detract from it.

## Suggestions

1. **Resolve the numerical inconsistency in Table 3** — verify whether the WUDI average of 63.65 is correct or whether the individual numbers need correction. Clarify the averaging procedure used across the 10 evaluation metrics.
2. **Remove or substantially revise the claim about surpassing mixture training** — either construct a proper mixture training baseline on the same task data for Qwen2-VL, or limit the claim to "merging is competitive with mixture training."
3. **Tone down the "first benchmark" and "novel method" claims** — clearly acknowledge prior MLLM merging evaluations and position OptMerge as an improvement on WUDI Merging with specific engineering contributions.
4. **Make the 2.48% improvement claim traceable** — explicitly state which experiments and which baseline it refers to, or remove it.

## Score and Decision

**Round 1 bracket**: Based on three calibration queries, I retrieved anchors: weak papers (avg ~2.33–3.00), middle papers (avg ~5.33–5.50), and strong papers (avg ~8.00). The paper clearly sits in the middle band: it has a genuine benchmark contribution but suffers from a numerical inconsistency and incremental method. Initial bracket: **4.5–6.0**.

**Round 2 narrowing**: I retrieved additional anchors in the 4.5–7.0 range for closer comparison:
- *UQ-Merge* (5.50): Similar MLLM merging scope. UQ-Merge has a more novel method (uncertainty-guided) but narrower evaluation (LLaVA-1.5 only). OptMerge has a stronger benchmark but a weaker method and a numerical inconsistency. **OptMerge is slightly weaker**.
- *"What Matters for Model Merging at Scale?"* (5.33): Pure empirical study with clean experiments but limited practical takeaways. OptMerge has both benchmark and method, but the inconsistency issue is more severe than anything in this anchor. **Roughly comparable but more problematic**.
- *MMER* (5.50): Training-free modality expansion. Similar modality merging scope but less comprehensive benchmark. MMER's method is more novel. **OptMerge is slightly weaker** due to the inconsistency.
- *WIDEN* (5.67): Extends merging to PT models. Cleaner experiments but narrower scope. **OptMerge is slightly weaker** due to the inconsistency issue.

Based on these comparisons, the paper sits at the lower end of the bracket. The numerical inconsistency is a real issue that would concern any reviewer. The benchmark contribution is genuine, but the method's incremental nature and overclaimed results further weigh against it.

**Final score: 5.0**. This reflects a paper that has useful elements (the benchmark) but whose central empirical claims are undermined by a verifiable numerical inconsistency and significant overclaiming, placing it below the acceptance threshold but above papers with fundamental flaws (like ATM at 3.0).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>