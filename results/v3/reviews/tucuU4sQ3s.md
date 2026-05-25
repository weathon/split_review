Now I have sufficient anchor data for calibration. Let me produce the final consolidated review.

**Round 1 bracket**: I placed the paper in the range of approximately 4.5 to 6.5 based on the initial calibration queries. The low-band anchors (< 3.5) had fundamental methodological or presentation issues that our paper does not share. The high-band anchors (> 7.5) are exceptional papers far beyond our paper's quality level.

**Round 2 narrowing**: Within the 4.5–6.5 bracket, the most relevant anchors are C-CLIP (6.50, accepted), PROOF (5.67, rejected), Vision & Language Synergy (5.00, accepted), and Task Codebook (4.67, rejected). Our paper is cleaner and more principled than PROOF or Task Codebook, and comparable to C-CLIP though with slightly less comprehensive evaluation. This supports a score of approximately 6.0.

**What did the low-band anchors fail at?** They had fundamentally unsound methodology, very poor experimental design, or no clear contribution. Our paper shares none of these failures — its method is well-motivated, experiments are sound, and contributions are clear.

**What did the weakness-anchored queries reveal?** Papers with missing baseline comparisons or unclear theoretical-empirical connection tended to score in the 4–6 range (RDAC 5.25, PROOF 5.67, CLDyB 5.67). Our paper's weaknesses are milder than these, placing it at the upper end of this band.

---

## Summary

This paper proposes NuSA-CL, a memory-free continual learning method for vision-language models. The core idea is to identify a low-energy (null) subspace of each weight matrix via SVD before each task, then persistently constrain low-rank updates to this subspace. After training, the update is merged into the backbone, keeping the parameter budget fixed across all tasks. Experiments on the MTIL benchmark (11 diverse tasks) and CIFAR100 class-incremental splits show that NuSA-CL outperforms other storage-free methods (LoRA, MiLoRA) by clear margins while using only 1.5M trainable parameters and zero additional storage, and approaches the performance of storage-based methods at a fraction of the cost.

## Strengths

1. **Superior efficiency-performance tradeoff among memory-free methods (Table 1).** NuSA-CL achieves Transfer 68.6%, Avg 75.1%, Last 82.8% on the MTIL benchmark while using only 1.5M parameters, zero additional storage, 6.6 GB peak GPU memory, and 1.21 GPU-hours. This directly outperforms all other storage-free methods (LoRA, MiLoRA) and rivals storage-based methods (MoE-Adapters, DIKI) at 40× fewer parameters and 3× faster training — directly supporting the paper's core claim of a practical, memory-free solution.

2. **Preserves zero-shot generalization in the challenging 5-shot setting (Table 2).** NuSA-CL achieves the highest average Transfer accuracy (68.1%), surpassing all storage-free baselines (LoRA 60.4%, MiLoRA 59.4%) and even exceeding the storage-based InflLoRA (66.8%) and the original zero-shot CLIP (65.3%). This provides concrete evidence that the null-space constraint protects pre-task capabilities under data-limited conditions.

3. **Persistent constraint validated as critical through careful ablation (Table 4a).** Unfreezing the null-space bases degrades Transfer from 68.58% (train only M) to 66.37% (M+Vₙ) and 62.60% (M+Uₙ+Vₙ). This establishes that the *persistent* confinement to the null space — not just initialization — is essential, a key distinction from prior subspace-initialization methods like MiLoRA.

4. **Principled null-space choice validated through subspace ablation (Figure 3a).** The *Tail* (null-like) subspace consistently yields lower forgetting than *Top* or *Random* across all tested ranks (e.g., at r=128: 2.57% vs 4.44% and 4.57%), quantitatively justifying the core design decision.

## Weaknesses

### Fatal

None.

### Major

1. **Missing baseline comparisons on the CIFAR100 long-sequence benchmark (Table 3).** The paper evaluates on CIFAR100 with 10/20/50 task splits but omits the storage-free PEFT baselines (LoRA and MiLoRA) that are the paper's primary competitors in the MTIL experiments. These are the methods most comparable to NuSA-CL in resource usage and are the ones NuSA-CL outperforms on MTIL. Without their results on CIFAR100, the paper's claim that NuSA-CL "scales better to long sequences" relative to other storage-free methods is incompletely tested in this setting. The inclusion of ZSCL (a full fine-tuning method that stores data and models) does not fill this gap. The paper should add these results to make the scalability evidence complete.

2. **No variance estimates for any main results.** Tables 1–3 report only point estimates without standard deviations or number of seeds. Given the modest margins (often 2–3 percentage points) in Tables 1–3, it is impossible to assess the significance of the improvements. This is especially important for the 5-shot results (Table 2), where few-shot learning can be highly variable across seeds and task orders. The paper should report means and standard deviations across multiple runs.

### Minor

3. **Internal inconsistency in the null space dynamics analysis (Section 6.1, Figure 2).** The paper reports that both the effective rank (r₉₅/d) and the null ratio increase across tasks. For the text encoder, effective rank increases from ~57.9% to ~58.8% while null ratio increases from ~41.0% to ~42.2%. These values are close to but do not sum to 100% (98.9% and 101.0% respectively), and — more critically — if both metrics are defined as complementary fractions of the total dimensions (effective rank being the dimensions needed to capture 95% spectral energy), an *increase* in effective rank should be accompanied by a *decrease* in null ratio, not an increase. The paper does not define "null ratio" explicitly, making it unclear whether it is dimension-based (the complement of effective rank) or energy-based. The trend directions as reported are contradictory under the natural interpretation. The authors should clarify the definition and either correct the numbers or explain what the dashed line actually measures.

4. **The theoretical analysis (Section 4, Lemma 1 / Theorem 2) is a parameter-space bound with no established link to functional forgetting.** The paper acknowledges this limitation (calling it a "local stability condition" and deferring function-level bounds to future work), which is good practice. However, the framing of Theorem 2 as "Cumulative Interference Bound" overstates the guarantee: the bound on Frobenius inner products in parameter space does not directly bound how model predictions on past tasks change. The paper would benefit from either (a) empirical verification that the bound correlates with measured forgetting, or (b) a more explicit discussion of where the gap between parameter-space and function-space interference appears, rather than just a one-sentence acknowledgment.

5. **The null space dynamics changes are very small (≈1 percentage point over 11 tasks, Figure 2).** The paper interprets this as evidence of "progressive knowledge accumulation," but such tiny changes are not compelling evidence of substantial utilization of the null space. A more direct measure would be helpful — for example, the cumulative Frobenius norm of updates relative to the null space capacity — to substantiate the "accumulation" narrative.

6. **"Transfer" metric definition is ambiguous (Section 5.1).** The paper defines Transfer as "zero-shot accuracy on unseen tasks" but does not specify how this is aggregated across tasks. It should clarify whether this is the average accuracy across all tasks not yet trained at each evaluation point, or only across tasks that will appear later in the sequence.

### Trivial

7. **The notation for the update rank \(r\) (Eq. 3) is not restated after its definition in Section 3.1.** The text defines \(r = \min(d-k, r_{\max})\) and then uses \(r\) as the dimension of the M matrix in Eq. 3 without explicitly restating this.

8. **"Forgetting" in Figure 3a is defined but its absolute scale (percentage points relative to what?) and whether it is averaged over tasks should be stated directly in the caption or text, not just in the supplementary.**

## Nice-to-Haves

- **Add LoRA and MiLoRA results to Table 3** as discussed in Major weakness #1. This would fully substantiate the scalability claim.
- **Measure the functional interference per task** — after each new task, compute the change in predictions (KL divergence or accuracy) on each previous task, and correlate this with the null-space singular values. This would provide the empirical link between the theoretical bound and actual forgetting that is currently missing.
- **Quantify null space capacity utilization** more directly, e.g., sum of update Frobenius norms relative to the null space Frobenius norm, rather than the small effective-rank changes in Figure 2.
- **Report per-layer SVD time and discuss scaling to larger backbones** (ViT-L, ViT-H) where attention projections are larger and truncated SVD may be needed.

## Removed Points

- **InLoRA initialization time "unusually large" (Section 6.3).** This is a comment about another method's implementation, not a weakness of the paper under review. Removed.
- **Notation clarity about reuse of \(r\).** This is a trivial presentation issue. Removed.
- **Section 3.1 sensitivity to \(\rho\) for \(\sigma_{k+1}\).** The paper already ablate \(\rho\) in Table 4b, showing robustness. The request for \(\sigma_{k+1}\) values is a nice-to-have extension, not a genuine weakness. Demoted to Nice-to-Have (implicitly covered by point about quantifying capacity utilization).

## Novel Insights

The reviews surface two observations that go beyond the paper's own contributions. First, the persistent constraint (freezing \(U_n, V_n\) throughout training) is shown to be critical through ablation — this is more than just the paper's claim, because it directly refutes the hypothesis that subspace initialization alone (as in MiLoRA) could achieve similar results if simply applied sequentially. Second, the fact that both effective rank and null ratio appear to move in the same direction in Figure 2, while almost certainly an artifact of unclear definition rather than a real phenomenon, actually illustrates a subtle point: the "null space" in this method is continually redefined after each merge, so the null space of \(W_t\) is not a superset of the null space of \(W_{t-1}\). This dynamic redefinition means the method does not "fill" a fixed container but instead shifts which directions are considered null at each step — a property that deserves more explicit discussion than it receives in the paper. Otherwise, no genuinely novel insights beyond the paper's own contributions.

## Suggestions

1. **Fix the null ratio definition and correct Figure 2 / Section 6.1.** Define "null ratio" explicitly (dimension-based vs energy-based), and ensure the numbers are consistent. If the null ratio is the complement of effective rank, the trend should move in the opposite direction.

2. **Add LoRA and MiLoRA to Table 3** to complete the storage-free comparison on the CIFAR100 long-sequence benchmark.

3. **Report standard deviations** for all main results (Tables 1–3) across at least 3 seeds.

4. **Clarify the Transfer metric aggregation** in Section 5.1.

5. **Measure and report the cumulative update norm relative to null space capacity** as a more direct test of whether the null space is being filled, rather than relying on the small effective rank changes.

## Score and Decision

**Anchor analysis (all rounds):**

| Anchor | Avg Score | Round & Query | Comparison |
|--------|-----------|---------------|------------|
| C-CLIP (sb7qHFYwBc) | 6.50, Accept | R1-topic-mid | Similar method quality but more comprehensive evaluation; our paper slightly below |
| PROOF (k9NYnsC4Mq) | 5.67, Reject | R1-topic-mid | Inferior method (inference mismatch); our paper is clearly stronger |
| Synergy (9aZ2ixiYGd) | 5.00, Accept | R1-topic-mid | Mixed reviews, fairness concerns; our paper is cleaner |
| TiC-CLIP (TLADT8Wrhn) | 6.25, Accept | R2-narrow | Benchmark paper, different contribution type; ours is comparable in quality |
| Task Codebook (EKfcngSxwD) | 4.67, Reject | R2-narrow | Limited novelty; our paper is significantly stronger |
| RDAC (9vkgAaCI3F) | 5.25, Reject | R1-weakness-null | Analysis-only paper; ours has practical method contribution |
| CLDyB (RnxwxGXxex) | 5.67, Accept | R1-weakness-missing-baselines | Benchmark paper; ours is comparable in quality |
| LVLM-CL (JIlIYIHMuv) | 2.50, Reject | R1-topic-low | Fundamentally flawed; our paper shares no such issues |

**Round-1 bracket:** 4.5–6.5 based on topic-anchored queries. The low-band anchors failed due to fundamentally unsound methodology or lack of clear contributions — our paper shares none of those failures. The weakness-anchored queries confirm that papers with missing baseline comparisons or unclear theoretical-empirical connections score in the 4–6 range; our paper's weaknesses are milder than these peers.

**Round-2 narrowing:** Within the bracket, our paper is stronger than PROOF (5.67), Task Codebook (4.67), and RDAC (5.25), and comparable to C-CLIP (6.50) and TiC-CLIP (6.25) but with slightly less comprehensive evaluation (missing baselines in one table, no cross-backbone experiments). The final score of 6.0 reflects a solid, well-motivated method with strong empirical results and fixable weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>