Now I have a solid understanding of the paper. Let me run calibration searches to score it properly.**Round 1 bracket: 5–7.** ASVD (6.25) is the closest topical anchor. AdaSVD builds on SVD-LLM and shows larger improvements, but has table inconsistencies. Let me narrow within [5, 7].Now I have enough to write the full review. Let me synthesize.

---

## Summary

AdaSVD proposes two components for post-training SVD-based LLM compression: **adaComp**, which compensates for SVD truncation error by alternately solving for the low-rank factors U and Vᵀ via Moore-Penrose pseudoinverse updates on calibration activations; and **adaCR**, which assigns layer-wise compression ratios based on input-output cosine similarity. Evaluated on LLaMA2, OPT, Vicuna, and Mistral at 40–80% compression ratios against SVD-LLM and other baselines, AdaSVD consistently achieves lower perplexity and higher zero-shot accuracy, with particularly large gains at high (60%+) compression ratios.

---

## Strengths

- **adaComp is technically sound and demonstrably effective.** Reformulating the truncation-error minimization as two decoupled least-squares problems and solving each via Moore-Penrose pseudoinverse (Eqs. 8–13) avoids the numerical instability of the naive matrix-inverse approach. Figure 3(a) shows the pseudoinverse update gives a smooth, monotonically decreasing MSE curve, while the naive update oscillates. The downstream improvements are large and consistent: at 60% compression on LLaMA2-7B, AdaSVD achieves WikiText-2 perplexity 50.33 vs. SVD-LLM's 89.90 (Table 1).

- **Comprehensive, multi-model evaluation.** Table 1 evaluates LLaMA2-7B across eight datasets (three LM benchmarks + five zero-shot reasoning tasks) at five compression ratios. Table 2 covers OPT-6.7B, Vicuna-7B, and Mistral-7B at 60%, and Table 4 combines AdaSVD with GPTQ quantization. This is a broader scope than most prior SVD-LLM compression papers.

- **Thorough ablation study.** Tables 3a–3d isolate contributions of adaComp (vs. no compensation), adaCR (adaptive vs. constant ratio), iteration count, and minimum retention ratio, providing clear interpretability of what each component contributes.

- **Stack-of-batch strategy is a practical contribution.** Averaging mini-batches (Eq. 14–15) allows use of more calibration data without increasing peak GPU memory, and Figure 3(b) shows it yields faster MSE reduction than naive calibration.

---

## Weaknesses

### Fatal

None.

### Major

- **Inconsistent hyperparameter settings (mrr) between main Tables 1 and 4.** Table 1 reports AdaSVD at 60% compression as WikiText-2 = **50.33**, but Table 4 reports the same method/model/dataset without GPTQ as **60.08**. Cross-checking Table 3d reveals that mrr=0.30 yields 50.33 while mrr=0.40 yields 60.08. The paper uses different mrr configurations in different tables without acknowledgment. This makes it unclear which configuration constitutes "AdaSVD" as a system and prevents fair comparison across sections. This inconsistency must be resolved by clarifying the default hyperparameter setting or reporting both configurations explicitly in each table.

- **adaCR importance metric is conceptually ambiguous relative to empirical results.** Eq. (17) defines I(W) = cosine_similarity(X, WX), with higher values indicating greater importance (more parameters retained, Eq. 19). The paper states "the first layer always weighs the most importance" (Figure 4). However, the cited inspiration works (Men et al., 2024; Dumitru et al., 2024) measure layer *redundancy* as cosine similarity, with *low* similarity (large transformation) indicating importance, i.e., they use (1 – cosine_similarity) as the importance signal. If AdaSVD's implementation actually uses high cosine similarity = high importance, then the first layer's prominence in Figure 4 implies it preserves its input (low transformation), which is at odds with typical transformer behavior for the first embedding-processing layer. The paper does not reconcile this with the cited works' opposite framing, creating a reproducibility gap in the metric definition.

### Minor

- **adaComp is effectively a single-step update in practice.** Table 3c shows 1 iteration outperforms 3 and 15 iterations at 40% and 50% compression ratios (14.76 vs. 15.47 vs. 15.84 at 40%). The paper correctly attributes this to overfitting but frames adaComp as an "alternating update" procedure throughout. Given that the best configuration for the most common compression range is a single iteration, the framing should emphasize the single-step pseudoinverse update as the core mechanism rather than the iterative refinement.

- **AdaSVD without adaComp is worse than SVD-LLM at 50% compression.** Table 3a shows AdaSVD (no adaComp) at 50% achieves WikiText-2 = 30.00 vs. SVD-LLM's 27.19. This means adaCR alone—without the compensating update—can hurt performance relative to the uniform-ratio baseline. The paper notes the result briefly but does not explain why applying adaCR without subsequent compensation increases error, nor whether this has implications for how adaCR should be tuned.

- **adaCR formula is unspecified for negative relative importance.** Eq. (19): CR(W) = mrr + I_n(W) × (trr – mrr). The paper states "CR(W) = mrr when I_n(W) = 0," but after mean normalization (Eq. 18), I_n can be negative (when I(W) < mean(I(W))). The paper does not specify whether layers with I_n < 0 are clipped to mrr or allowed to have CR < mrr. This affects the actual parameter budget distribution.

- **VLM evaluation is purely qualitative.** Figure 5 shows four hand-selected captioning examples. Given that COCO CIDEr/BLEU scores are standard and straightforward to compute, the absence of any quantitative VLM metric weakens the claim of generalizability to VLMs. This is a missed opportunity for the stated scope.

### Trivial

- The improvement percentages in Table 1 (e.g., "304.62 (158%)") are not accompanied by a definition of what the percentage measures (relative reduction over SVD-LLM, absolute difference?). Adding a brief note to the caption would prevent confusion.

---

## Nice-to-Haves

- Reporting C4-calibrated (instead of WikiText-2-calibrated) compression results alongside the standard setup would demonstrate that gains do not depend on the calibration corpus matching the evaluation dataset.
- An analysis of *why* one pseudoinverse step recovers so much error—specifically the relationship between the truncated singular value gap and the fraction of error recovered per step—would give adaComp stronger theoretical grounding.
- Providing quantitative VLM captioning scores (CIDEr, BLEU on COCO) for at least one compression ratio would substantiate the VLM generalizability claim.
- A comparison of adaCR's layer-wise compression budget against Hessian-based or sensitivity-based importance measures (e.g., from GPTQ or SparseGPT) would validate the cosine-similarity proxy's effectiveness beyond empirical trends.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Calibration/evaluation overlap on WikiText-2 (Harsh Critic, framed as major gap):** Real, but the paper explicitly follows the same setup as ASVD and SVD-LLM ("we followed ASVD and SVD-LLM to randomly select 256 samples from WikiText-2"). Because all baselines use the same calibration corpus, the comparison remains fair. The gains generalize to C4 and PTB. Demoted: mentioned as a Nice-to-Have (alternative-calibration experiment), not retained as a Major weakness.

- **Stack-of-batch is "an averaging trick with unstated assumptions" (Harsh Critic):** Eq. (14–15) clearly describes the procedure, and N=256 is stated in Section 4.1 ("randomly select 256 samples"). The design choice is adequately explained. Removed as a standalone weakness.

- **Strength: "thorough evaluation across multiple models, tasks, and modalities" (Strength Finder):** Kept only the specific evidence-grounded version above; the generic framing is dropped.

- **Table 3a framing as glossing over a weakness (Harsh Critic):** The paper does acknowledge in Section 4.3 that "AdaSVD already outperforms SVD-LLM without using adaCR, while integrating adaCR can further enhance the performance." However, the Table 3a result for adaCR alone at 50% (30.00 vs. 27.19) contradicts this narrative and is retained as Minor.

- **Missing Table 2 (Harsh Critic):** Table 2 is described in Section 4.2 ("As shown in Table 2, AdaSVD consistently outperforms...") and its content is summarized. Per the hard rules, absent appendix/table content is a parser artifact, not an author omission.

---

## Novel Insights

The most genuinely novel observation—surfaced by the harsh critic and verifiable from the paper—is that iterating adaComp *beyond one step is counterproductive* at common compression ratios (40–50%), indicating the pseudoinverse solution already finds the optimal re-fit in a single pass when the singular value gap is not too large. This implies the "alternating update" framing is a misleading description of what the method actually does and suggests that the core contribution of adaComp is really a *one-shot* closed-form activation-conditioned re-fit of the truncated factors, which is a conceptually simpler and more elegant insight than what the paper presents. The connection between the magnitude of the singular value gap at truncation and the number of beneficial update steps would be a genuinely useful characterization.

---

## Suggestions

1. Reconcile Table 1 and Table 4: pick a single mrr configuration, document it as the default in Section 4.1, and re-run the inconsistent table so all results reflect the same system.
2. Clarify the adaCR importance metric: if the implementation assigns *more retention to layers with higher cosine similarity*, explain explicitly why such layers are "important" from a compression-quality perspective (not from a "transformation magnitude" perspective), reconciling with the cited redundancy-pruning literature.
3. Reframe adaComp's central contribution as the single-step pseudoinverse update; retain the multi-iteration case as an extension for very high compression ratios (60%+) with a note about its sensitivity to calibration data size.
4. Add quantitative COCO captioning metrics for the VLM experiment.
5. Specify in Eq. (19) the clipping behavior for I_n(W) < 0.

---

## Score and Decision — Calibration

**Anchor papers across all rounds:**

| Path | Avg Score | Round | Comparison to AdaSVD |
|---|---|---|---|
| HyPofygOCT.md (ASVD) | 6.25 | R1 | Most topically similar. AdaSVD has broader evaluation and larger improvements; ASVD was rejected for minor incremental novelty. AdaSVD is roughly comparable or slightly better. |
| 3KEwJGYNzH.md (AutoTrunc) | 4.00 | R1 | Also SVD truncation for LLMs; weaker paper with presentation issues and limited model diversity. AdaSVD is clearly stronger. |
| ho7ZUS1z8A.md (MoE-SVD) | 5.00 | R1 | SVD for MoE LLMs; targets a different architecture. Less directly comparable but similar ambition. |
| FVgizbs3o2.md (TensorGPT) | 3.75 | R1 | SVD/tensor decomposition for LLMs; training-free but much weaker evaluation. AdaSVD is stronger. |
| xw29VvOMmU.md (LQ-LoRA) | 6.75 | R2 | Decomposition + low-rank for LLM fine-tuning; accepted. Cleaner methodology, good ablations. AdaSVD is somewhat weaker due to inconsistency issues. |
| BifeBRhikU.md (PB-LLM) | 6.75 | R2 | LLM binarization; accepted. Different compression modality. AdaSVD comparable in breadth. |
| 1RrOtCmuKr.md (Codebooks) | 6.33 | R2 | Quantization-based memory compression; accepted. Similar practical motivation. |
| mMmzHS28ht.md (LLM Pruning+Distill) | 5.00 | R2 | Structured pruning with distillation; weaker baseline comparisons. AdaSVD is stronger. |

**Round 1 bracket**: 5–7.  
**Round 2 narrowing**: AdaSVD is stronger than ASVD (6.25, rejected) in scope and contribution, but has a significant cross-table hyperparameter inconsistency and a conceptual issue with the adaCR metric that ASVD does not have. It is weaker than the accepted papers at 6.75 (LQ-LoRA, PB-LLM) in terms of rigor. The paper sits closer to the 5.5–6.0 range — above ASVD's 6.25 in contribution quality, but pulled down by the inconsistency issues. Settling at **5.5**, borderline below the accept threshold.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>