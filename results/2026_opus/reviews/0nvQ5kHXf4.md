Now I'll run calibration search to anchor my score.Now I have enough calibration. Let me write the final review.

Round 1 bracket: Between 3.5 and 6.5 (matches mid-range subspace/low-rank PEFT papers).
Round 2 narrowing: Closest anchors are TinyTrain (5.25, reject), ROSA (6.0, reject), SubZero (4.25, reject), AutoTrunc (4.0, reject), EigenLoRA (5.0, reject). The paper has strong empirical scope (3 transformer families, Pi 5 deployment) like TinyTrain, but has algorithmic ambiguity and attribution issues that make it weaker than ROSA. Final score around 4.5.

## Summary
The paper proposes WASI (Weight-Activation Subspace Iteration), a low-rank training scheme that compresses both weight matrices (via WSI) and activation maps (via the existing ASI) of transformer models during fine-tuning. It demonstrates up to 62× training-memory reduction on SwinT and ~1.4× wall-clock speedup on a Raspberry Pi 5 when fine-tuning ViT, while extending the approach to TinyLlama on BoolQ.

## Strengths
- **Real-hardware demonstration**: Sec. 4.4 / Fig. 8 reports a ~1.4× end-to-end speedup on a Raspberry Pi 5 (Cortex-A76 CPU) even at the least aggressive setting (ε=0.9), which is concrete evidence that the pipeline is deployable rather than only theoretical.
- **WSI vs. full SVD comparison (Fig. 3b)**: At matched accuracy WSI requires 1.36× fewer FLOPs than recomputing SVD each iteration, and at matched FLOPs it reaches ~35% higher accuracy. This directly supports the warm-started subspace iteration design choice.
- **Empirical breadth**: The same recipe is applied to ViT, SwinT (five datasets) and TinyLlama (BoolQ) — Fig. 5, Fig. 6, Fig. 7 — showing the approach is not narrowly tied to one architecture/dataset.
- **Principled accuracy-efficiency control**: The explained-variance threshold ε (Eq. 7) gives a monotonic accuracy-vs-cost curve in Figs. 5–6, which is easier to operate than rank- or budget-based knobs.
- **Subspace stability evidence (Fig. 3a)**: Tracking singular values of W_6 across 40 epochs supports the load-bearing "stable subspace" hypothesis (Sec. 3.3) — see also weakness below on the narrowness of this verification.

## Weaknesses

### Fatal
None.

### Major
- **Ambiguity in what Algorithm 1 actually operates on.** Algorithm 1 takes "weight 𝒲_{i(t)} at iteration t" and applies lines 6–7 to it, while Eq. 11 updates the product L_i R_i. The text never reconciles these: if the working representation is the fixed-rank product L_i R_i and updates stay inside that subspace (Eqs. 8–10), the subspace iteration in lines 6–7 is mathematically inert on a rank-K matrix; if a full-rank 𝒲_{i(t)} is maintained, the headline weight-memory savings during training don't follow. Since "warm-started subspace iteration on weights" is the new component, the reader cannot currently verify what it buys. The authors should state unambiguously what 𝒲_{i(t)} is post-truncation and what additional memory (if any) is paid to keep it.
- **Attribution: headline efficiency numbers are dominated by ASI (prior work), not WSI.** Sec. 4.3 reports 62× memory and 1.5× FLOPs reduction on SwinT at ε=0.9 while matching vanilla accuracy; the breakdown in Fig. 5 makes clear that weight-side savings are much smaller than activation-side. Because ASI is from Nguyen et al. 2025, the new contribution (WSI + 3D-activation extension + DP rank selector) is doing less of the work than the headline suggests. A clean ablation {vanilla, ASI-only, WSI-only, WSI+ASI} on at least one ViT-dataset pair, with weight memory and activation memory broken out, would precisely show what WSI adds.
- **MLP-only measurement protocol vs. whole-model deployment.** Sec. 4.1 explicitly restricts memory/FLOP measurements to "linear layers within multi-perceptron blocks for fair comparison with previous methods", while the Raspberry Pi 5 timing measures the whole model. The result — 62× theoretical memory and 2× FLOPs translating to 1.4× wall-clock — deserves explicit discussion, since attention projections/Q/K/V/O and cached attention maps remain uncompressed in the main protocol. Either WASI's reach across the whole transformer needs to be quantified, or the measured/theoretical gap needs explaining (kernel overhead, BLAS dispatch, memory bandwidth).
- **Missing LoRA-family fine-tuning baselines.** The paper rejects LoRA in Sec. 2 on the grounds that the adapter merges back at inference and that frozen weights + adapter coexist in memory. For the *training-time* memory/accuracy plots in Figs. 5–7, however, LoRA / DoRA / QLoRA are the obvious benchmarks, and the dismissal in Sec. 2 doesn't preclude that comparison. Comparing primarily to SVD-LLM (which the paper itself notes "cannot be directly applied to all vision transformer-based models", Sec. 2) sets up a comparison WASI is favored to win.

### Minor
- **Narrow verification of the "stable subspace" hypothesis.** Sec. 4.2's evidence is Fig. 3a, which shows W_6 of ViT on Pets at a single ε=0.8. The Sec. 1 contribution claims the much broader statement that "the essential information of model parameters resides in a stable subspace throughout fine-tuning". Showing the same plot across early/middle/late layers, attention projections, and at least one more dataset/architecture would substantiate the load-bearing claim instead of relying on a single layer.
- **TinyLlama setup limits comparability.** Sec. 4.3 fine-tunes only the last 5 layers and "log[s] the resource consumption only at the layers that are fine-tuned"; the 953.86× / 30.12× / 13.11× / 30.27× headlines are therefore not directly comparable to full fine-tuning numbers reported elsewhere in the literature. BoolQ accuracy lies in a 64–66% band (Fig. 7), a narrow range; the absence of seed variance/error bars makes it hard to read the gap over vanilla as a real effect.
- **Abstract operating-point opacity.** The "up to 62×" figure should be presented inline with the matching ε and accuracy delta; the maximum reduction does not occur at the configuration that matches vanilla.
- **Update rule (Eq. 11) ambiguity.** It is not specified whether L_i and R_i are updated jointly via the product gradient or separately (and whether one is held fixed, as in LoRA-style schemes). This is reproducibility-relevant and ties to the Major point above.
- **Treatment of non-MLP layers.** Sec. 3 covers linear MLP layers only; nothing in the main text describes how attention layers, LayerNorm, residual connections, or activation nonlinearities are handled when WASI is composed across a residual stream (Appendix B.3 is mentioned but the main paper should sketch it).

### Trivial
None retained.

## Nice-to-Haves
- Provide an explicit explanation for the gap between theoretical (2×/62×) and measured (1.4×) speedup on Cortex-A76: BLAS behavior for low inner dimensions, kernel-launch overhead of low-rank ops, or memory-bandwidth bottlenecks would all be informative for practitioners.
- Add at least one decoder-only LLM result that does *not* restrict fine-tuning to the last 5 layers, so the TinyLlama numbers can be compared to a stronger baseline.
- Report seed variance for the TinyLlama BoolQ experiment in Fig. 7.

## Removed Points
These points are flagged as removed; treat them with caution.
- *Pets citation: "Citing Zhang et al., 2022 for Oxford-IIIT Pets is unusual (canonical is Parkhi et al., 2012)."* — Removed per the rule about questioning existence/citation of cited works; this is a citation-style nit, not a substantive flaw.
- *Hard rule: missing-related-works.* The harsh critic implicitly suggested broader baselines (LoRA et al.) on existence grounds; the retained Major point keeps only the empirical training-time-comparison angle, not any claim about overlooked literature.
- *Strength: "generality across three transformer families."* Kept only with the caveat that the TinyLlama setup is restricted to the last 5 layers (Minor weakness); the strength is not fully independent.

## Novel Insights
None beyond the paper's own contributions. The work is a careful engineering extension of ASI to weights with a few practical add-ons (DP rank search, 3D activation support); the conceptual ingredients (warm-started subspace iteration, intrinsic-subspace stability during fine-tuning) come from prior work and are applied rather than newly established here.

## Suggestions
- State plainly what 𝒲_{i(t)} is in Algorithm 1 after the t=0 truncation, and if updates remain inside the rank-K_i subspace, explain explicitly what Step 2's subspace iteration adds over a LoRA-style update inside a fixed initial subspace.
- Add an ablation matrix {vanilla, WSI-only, ASI-only, WSI+ASI} with weight and activation memory broken out, on at least one ViT-dataset pair, so the WSI contribution is isolated from the ASI contribution.
- Compare against LoRA / DoRA / QLoRA at training-time memory and accuracy in Figs. 5–7. The structural argument against LoRA at inference does not preclude this fine-tuning-time comparison.
- Broaden Fig. 3a across early/middle/late layers and at least two datasets and one non-ViT architecture, and at more aggressive ε.
- Report the Raspberry Pi 5 wall-clock speedup in the abstract alongside the 62× number, and explain the theoretical-vs-measured gap.

## Per-axis Assessment
- **Originality**: Moderate. WSI is a natural transposition of warm-started subspace iteration (already used by ASI on activations) to weights; the DP rank search and 3D-activation extension are incremental.
- **Importance of research question**: Genuine — fine-tuning transformers on edge devices is a useful direction.
- **Claims well supported**: Partially. The on-device speedup and WSI-vs-SVD comparisons are well supported; the headline 62×/953× numbers are supported only under a restricted (MLP-only / last-5-layers) measurement protocol, and the stability hypothesis is verified narrowly.
- **Soundness of experiments**: Mixed. Protocol choices favor the proposed method (no LoRA baseline; MLP-only memory accounting; no error bars), even though the core measurements are sensible.
- **Clarity of writing**: Adequate overall, but Algorithm 1 and Eq. 11 leave the central mechanism genuinely ambiguous.
- **Value to the research community**: Modest. The Raspberry Pi 5 result and the engineering recipe are useful; the conceptual contribution is incremental once ASI is taken as prior work.

## Calibration anchors used

Round 1 (bracketing):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/04RLVxDvig.md` — NanoMoE — avg 3.00 (Round 1, weak band). Weaker than the paper under review.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eqKHuxIpp5.md` — On-Device TL via Mixed-Precision — avg 2.50 (Round 1, weak band). Weaker; less rigorous.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/igGeaxOiFM.md` — HoLoRA — avg 3.00 (Round 1, weak band). Weaker; similar PEFT topic with weaker eval.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/49ti6LOUw5.md` — UnoLoRA — avg 3.00 (Round 1, weak band).
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LvNROciCne.md` — AdaRankGrad — avg 7.00 (Round 1, middle band, accept). Stronger; cleaner theoretical grounding.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/s7DkcgpRxL.md` — LoRAM — avg 6.20 (Round 1, middle band, accept). Stronger by virtue of cleaner formulation and clearer attribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FK6T0U4Mg1.md` — SubZero — avg 4.25 (Round 1, middle band, reject). Comparable concerns: insufficient baselines, unclear isolation of new component.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/cgCKm5DOnu.md` — ROSA — avg 6.00 (Round 1, middle band, reject). Stronger theory; comparable empirical scope.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TwJrTz9cRS.md` — HiRA — avg 8.00 (Round 1, strong band). Stronger; not directly comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/E4Fk3YuG56.md` — Cut Cross-Entropy — avg 8.50 (Round 1, strong band). Stronger contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vf5aUZT0Fz.md` — DEPT — avg 8.00 (Round 1, strong band). Stronger and not comparable scope.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/d8w0pmvXbZ.md` — Small-scale proxies — avg 8.00 (Round 1, strong band). Stronger.

Round 1 bracket: between 3.5 and 6.5; most comparable anchors at 4.25–6.0.

Round 2 (narrowing):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FVgizbs3o2.md` — TensorGPT — avg 3.75 (Round 2). Weaker; training-free LLM compression of embeddings only.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ho7ZUS1z8A.md` — MoE-SVD — avg 5.00 (Round 2). Similar tier; SVD decomposition for MoE; comparable depth.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3KEwJGYNzH.md` — AutoTrunc — avg 4.00 (Round 2). Weaker; addresses a narrower problem.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7Cx05z4pUc.md` — Decomposed Learning and Grokking — avg 5.00 (Round 2). Comparable score, narrower scope.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/E5YmIBvOqV.md` — Filter Subspace tuning — avg 6.00 (Round 2). Stronger; cleaner theoretical positioning.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/mzkpLkd1S8.md` — Nullspace ViT robustness — avg 5.25 (Round 2). Comparable tier; different topic.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xNdE7RiRyP.md` — TinyTrain — avg 5.25 (Round 2, read in full). Closest match: on-device training, real-hardware deployment, similar reviewer pattern of "valuable engineering, limited novelty, attribution concerns".
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KxGGZag9gW.md` — EigenLoRA — avg 5.00 (Round 2). Comparable tier; subspace PEFT.

WASI sits close to TinyTrain (5.25) and SubZero (4.25) — comparable engineering reach but somewhat weaker than TinyTrain because the algorithmic ambiguity in WSI is a concrete mechanistic concern that TinyTrain doesn't have, and the headline numbers are mostly inherited from ASI. It is comparable to or slightly weaker than ROSA (6.0) on theory but stronger on hardware deployment. Final placement: between SubZero (4.25) and TinyTrain (5.25), nearer to TinyTrain because of the Pi 5 measurement and breadth across three transformer families, but pulled down by Major issues 1–4. Score: 4.5.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>