Let me read the most topically-similar anchors in full to compare.Now I have enough context. Let me write the final review.

## Summary

The paper proposes AdaSVD, an SVD-based LLM compression method with two contributions: **adaComp**, which alternately updates the truncated singular factors U and V via Moore–Penrose pseudoinverse-based least-squares projections (with a "stack-of-batch" calibration averaging trick), and **adaCR**, which assigns per-layer compression ratios using a cosine-similarity-based layer-importance heuristic. Experiments on LLaMA2-7B, OPT-6.7B, Vicuna-7B, Mistral-7B, and a LLaVA VLM show consistent perplexity improvements over SVD-LLM/ASVD/FWSVD at 40–80% compression and compatibility with GPTQ quantization.

## Strengths

- **adaComp via pseudoinverse update is stable and reduces error**: Figure 3(a) shows the Moore–Penrose update (MPPU) produces a smooth, monotonically decreasing MSE curve while the naive normal-equation update (NU) oscillates and plateaus higher; Equations 8–13 give the derivation.
- **adaCR yields measurable gains over uniform compression**: Table 3(b) shows that at 60% target compression on LLaMA2-7B, switching from constant to adaptive layer-wise ratio drops PPL from 69.46 → 50.33 on WikiText-2 (and 336.90 → 239.18 on C4); Figure 4 documents the layer-importance variation that motivates the design.
- **Consistent gains over SVD-LLM across four model families**: Table 2 shows AdaSVD beats SVD-LLM at 60% compression on OPT-6.7B (34.45 vs. 49.35), Vicuna-7B (61.65 vs. 214.47), Mistral-7B (20.82 vs. 36.18), and LLaMA2-7B (50.33 vs. 89.90).
- **Orthogonality to GPTQ quantization is demonstrated**: Table 4 shows AdaSVD+GPTQ-INT4 beats SVD-LLM+GPTQ-INT4 at every compression ratio (e.g., 22.55 vs. 33.56 PPL on WikiText-2 at 40%).
- **Extension to VLMs**: Figure 5 shows qualitative gains for LLaVA-7B at 40% compression — AdaSVD produces correct captions where SVD-LLM degenerates into nonsense tokens.

## Weaknesses

### Fatal
None.

### Major

- **The "iteration" ablation contradicts the paper's central narrative about adaComp.** Table 3(c) shows that one iteration is best at every compression ratio: at 40% (14.76 / 15.47 / 15.84 for 1/3/15 iters), 50% (25.58 / 27.11 / 27.45), and even at 60% (50.33 / 64.12 / 62.34). Yet the prose on p. 8 states "under higher compression ratios, additional iterations lead to performance improvements" — directly contradicted by the 60% row. The framing in Eq. (16) and Figure 2(d) of "alternately applying [the update] until convergence" describes something the ablation does not support. What actually does the work is a one-shot LSE projection (one update of U onto V and one of V onto U), which is a meaningfully smaller and less novel contribution than what the paper advertises. The narrative around adaComp needs to be reconciled with the ablation.

- **Undefined "(N%)" annotations in Table 1.** AdaSVD entries carry labels like "304.62 (158%)", "239.18 (157%)", and "113.84 (112%)" with no definition in caption or text. Read as percent reduction over SVD-LLM, several values (>100%) are impossible. The reader cannot interpret a headline table. Define the metric (e.g., (SVD-LLM − AdaSVD)/AdaSVD, vs. /SVD-LLM, vs. some other ratio).

### Minor

- **Practical significance at high compression ratios that the paper emphasizes is weak.** At 60% on LLaMA2-7B, the compressed model lands at PPL 50.33 / PTB 1,216.95 / MMLU 24.69 — MMLU is below the 25% random floor. At 70–80% the PPLs run 100–200+. The paper's "narrowing the gap to the original model" framing is overstated for the high-compression regime that is repeatedly highlighted; the gap remains very large. This does not invalidate the SVD-family-internal contribution, but Table 1 and the introduction should acknowledge that several MMLU "wins" are at or below chance.

- **Calibration is drawn entirely from WikiText-2 (256 samples) and the largest relative degradations are on PTB.** Looking at Table 1, AdaSVD at 40% goes from 5.68 → 14.76 on WikiText-2 (~2.6×) but from 8.35 → 304.62 on PTB (~36×). adaComp explicitly minimizes ‖UVᵀX − WX‖² on this single-distribution X (Eq. 5), so calibration overfitting is a foreseeable failure mode. The same issue afflicts SVD-LLM in absolute terms, so this is not a uniqueness problem, but a calibration-shift control — re-running with mixed-domain or PTB-drawn calibration and reporting whether the ranking holds — would strengthen the contribution.

- **"Stack-of-batch" is presented as if it uses more data without memory increase, but Eq. 14–15 average mini_bsz raw samples into one effective sample.** This reduces the effective sample count from N to M (Sec. 3.1). It does use information from N samples through averaging (which empirically helps, Figure 3b), but the technique is best described as variance reduction via mini-batch averaging, not "utilization of more calibration data without increasing memory overhead." For LSE problems, the more standard memory-efficient alternative is incremental accumulation of XXᵀ. The technique is fine; the justification should be reworded.

- **adaCR importance proxy is not validated directly.** Equation 17 equates "layer importance" with cos-sim(X, WX). The intuition that a near-identity layer is unimportant is debatable: residual-stream geometry can make low-transformation layers load-bearing. The paper provides indirect validation through Table 3(b), but a direct check — e.g., correlation between ℐ(W) and per-layer compression-loss sensitivity — would close the gap.

- **Missing GPTQ-only baseline in Table 4.** The table compares AdaSVD+GPTQ to SVD-LLM+GPTQ. A useful and natural reference point would be plain GPTQ-INT4 with no SVD at all, so the reader can see what stacking SVD on top of quantization buys in absolute terms (vs. just using GPTQ at a higher bit budget).

### Trivial

- The text refers to Figure 3(c) showing the distribution of values before/after adaComp, but in the experimental section the *iteration* discussion would benefit from being shown in the same iteration-vs-quality plot rather than only as a table.

## Nice-to-Haves

- Reframe adaComp around what the ablation actually shows: "one alternating sweep of stable LSE projection of U onto V (and V onto U) suffices." This is a cleaner, more honest contribution than "iterative alternating updates until convergence."
- Report variance over calibration seeds (256 samples is small and several rows in Table 1 are within plausible noise of SVD-LLM on QA metrics).
- A calibration-distribution control (WikiText-2 vs. mixed vs. PTB-drawn calibration) would directly address the overfitting concern.

## Removed Points

These points are flagged to be removed; treat them with caution.

- Harsh critic's framing of Eq. 6–7 vs. Eq. 10–13 as "the standard difference between forming an explicit inverse and using a stable pseudoinverse" is *factually correct*, but the paper does not actually claim novelty for the pseudoinverse algorithm itself — it claims novelty for *using* it for post-truncation factor refinement. This is not a real weakness.
- Harsh critic's call to compare against non-SVD methods (GPTQ-only, AWQ-only) at matched memory: this is **scope creep** — the paper is explicitly framed as an advancement within the SVD compression family. It is reasonable to ask for a sanity-check baseline, but the absence is not a substantive flaw — it's a nice-to-have. Demoted to Minor (GPTQ-only baseline in Table 4 specifically).
- Harsh critic's "winning at 60% means MMLU at chance, not deployable" was kept but downgraded from a structural problem to a minor framing issue, since the SVD compression family as a whole shares this limit.
- Strength Finder's "ablation isolates contributions of each component" — kept as the adaComp/adaCR strengths, but the framing as a clean independent decomposition is a bit generous given that Table 3(b) shows AdaSVD without adaCR still beats SVD-LLM, so the components are not strictly additive.

## Novel Insights

None beyond the paper's own contributions. The adaptive layer-importance via cos-sim is a sensible engineering choice but is borrowed from cited prior work; the LSE-via-pseudoinverse refinement is standard numerical linear algebra applied to a new setting.

## Suggestions

- Reconcile the iteration ablation (Table 3c) with the prose. Either remove the "more iterations help at high CR" claim, or explain why one iteration is consistently best in the reported data.
- Define the "(N%)" annotation in Table 1's caption.
- Add a calibration-shift control: rerun adaComp with calibration drawn from PTB or C4 and report whether the WikiText-2 vs. PTB gap shrinks.
- Acknowledge in the main text that MMLU at the highlighted 60–80% compression ratios is at or near chance.
- Add a "GPTQ-INT4 only" row to Table 4 as a non-SVD reference.
- Reframe the stack-of-batch technique honestly as mini-batch averaging for variance reduction; do not describe it as "utilizing more data."

## Axis Evaluation

- **Originality**: Modest. Pseudoinverse-based LSE refinement and cosine-similarity-based layer importance are both standard ingredients; the combination and application to SVD-LLM-style compression is a sensible but incremental engineering contribution.
- **Importance of question**: Reasonable. SVD compression is a meaningful sub-area, though the practical regime where SVD outperforms quantization-based methods remains unclear.
- **Claims well supported**: Mixed. The headline claim that AdaSVD beats SVD-LLM is supported. The narrative claim about iterative updates being central to adaComp is *not* supported by Table 3(c).
- **Soundness of experiments**: Adequate set of models and datasets; ablations are present. However, the calibration set is small and single-distribution, no variance reported, and one ablation directly contradicts a prose claim.
- **Clarity of writing**: Generally clear, but the Table 1 (N%) annotation is undefined and the stack-of-batch description overstates what the technique does.
- **Value to community**: Real but bounded. Within SVD-based compression, AdaSVD pushes the SOTA on the chosen benchmarks; outside that family the relevance is unclear without quantization comparisons.

## Score and Decision

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison to AdaSVD |
|------|-----------|-------|----------------------|
| `0T8vCKa7yu.md` (CVXQ quantization) | 3.00 | 1 | Different sub-area (quantization); not directly comparable but anchors low end. |
| `ZTvUT49JjL.md` (Implicit bias matrix factorization) | 3.40 | 1 | Tangentially related; less applied than AdaSVD. |
| `vw0NurJ7UX.md` (PrefixQuant) | 3.00 | 1 | Different sub-area. AdaSVD has comparable engineering polish but stronger narrative issues. |
| `4QWPCTLq20.md` (IntelLLM KV cache) | 3.00 | 1 | Different sub-area. |
| `3KEwJGYNzH.md` (AutoTrunc — automatic SVD truncation positions) | 4.00 | 1+2 | Closest topical match. AdaSVD has cleaner writing and broader evaluation (4 model families, VLM, GPTQ), but adds an iteration-claim inconsistency AutoTrunc does not have. AdaSVD is somewhat stronger. |
| `ho7ZUS1z8A.md` (MoE-SVD) | 5.00 | 1+2 | MoE-SVD shows SVD for MoE LLMs with sensible technique; reviewers split 3/6/6. AdaSVD comparable in technical depth and breadth of evaluation, with similar critique pattern. |
| `HyPofygOCT.md` (ASVD — a baseline in this paper) | 6.25 | 1 | The baseline ASVD scored higher in its own review than AdaSVD likely will, because ASVD was the first activation-aware SVD approach. AdaSVD's contribution is more incremental on top of SVD-LLM/ASVD. |
| `FVgizbs3o2.md` (TensorGPT — tensor-train) | 3.75 | 1+2 | Weaker baselines; AdaSVD is stronger than this. |
| `TJo6aQb7mK.md` (Spectra/TriLM ternary models) | 7.60 | 1 | Genuinely novel and large-scale; clearly above AdaSVD. |
| `eW4yh6HKz4.md` (CBQ cross-block quantization) | 7.60 | 1 | Stronger contribution; above AdaSVD. |
| `E4Fk3YuG56.md` (Cut Cross-Entropy) | 8.50 | 1 | Clearly above AdaSVD. |
| `tcsZt9ZNKD.md` (Scaling sparse autoencoders) | 8.20 | 1 | Clearly above AdaSVD. |
| `FA3iYp1y6z.md` (Low-Rank Correction for Quantized LLMs) | 5.00 | 2 | Closely related — low-rank correction for quantized LLMs. Similar incremental contribution + ablation-heavy style; AdaSVD comparable in scope. |
| `x83w6yGIWb.md` (Calibration data for pruning LLMs) | 5.50 | 2 | Different angle (calibration data study) but addresses related concerns. |
| `FJiUyzOF1m.md` (Bayesian Low-rank Adaptation) | 6.50 | 2 | Different (LoRA/Bayesian) — less directly comparable. |
| `vg7dECgAw2.md` (Pareto self-supervision calibration) | 5.75 | 2 | Different sub-area. |
| `oXh0939Zzq.md` (Dynamic Low-Rank Sparse Adaptation) | 5.20 | 2 | Sparsity + LoRA hybrid; comparable engineering paper. |

**Round 1 bracket**: Topically similar work clusters in [3.5, 6.5], with AutoTrunc (4.0) and MoE-SVD (5.0) the closest matches.

**Round 2 narrowing**: Read AutoTrunc, MoE-SVD, and Low-Rank Correction for Quantized LLMs in detail. AdaSVD is clearly better-presented and broader in evaluation than AutoTrunc (4.0), comparable to MoE-SVD (5.0) and Low-Rank Correction (5.0) in scope, but has a real, verifiable internal inconsistency between the adaComp narrative and Table 3(c) that the others don't have. This pulls it modestly below the 5.0 cluster — landing around 4.5.

The paper makes a reasonable engineering contribution within the SVD-based LLM compression family with consistent empirical gains over its direct baseline, but has a structural narrative-vs-ablation inconsistency, an undefined headline-table metric, an overstated stack-of-batch justification, and weak practical significance at the high compression ratios it emphasizes. None of these are fatal, and the FUNDAMENTAL ISSUES rule does not trigger — the iteration-narrative problem requires reframing rather than invalidating the method.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>