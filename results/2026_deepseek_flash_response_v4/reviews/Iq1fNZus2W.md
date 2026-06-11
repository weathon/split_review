Now I have a clear picture of the calibration landscape. Let me write my final review.

**Bracket from Round 1:** This paper sits between the weak band (scores ~3.0-3.25, papers with major flaws) and the strong band (scores ~8.0, comprehensive top-venue papers). The most relevant anchors sit in the 4.5-6.5 range.

**Round 2 narrowing:** Comparing against anchors:
- **UniCon (7.0, Accept)**: Stronger than the current paper — cleaner evaluation, comparable contribution
- **Qihoo-T2X (6.4, Accept)**: Slightly stronger — similar efficient-attention contribution with fewer evaluation gaps
- **LinFusion (6.25, Reject)**: Slightly stronger — more thorough comparisons but similar evaluation issues
- **ViCo (5.5, Reject)**: Comparable — both have real contributions and evaluation gaps
- **EDM2+ (5.0, Reject)**: Weaker — lacks technical novelty compared to the current paper

The current paper's clear contributions (attention sparsity diagnosis, PAA, KSA, cache-enabled architecture) and convincing efficiency scaling place it above papers like EDM2+. However, the evaluation issues — particularly the ambiguous baseline training and the downplayed F1 degradation — make it weaker than the 6.0+ papers. I place it at 5.0.

---

## Summary

This paper proposes Patch-wise and Keyword-Aware Attention (PKA), a framework to reduce the computational cost of multi-condition control in Diffusion Transformers. PKA decomposes full multi-modal attention into two specialized modules: Position-Aligned Attention (PAA) for spatial conditions (one-to-one attention between aligned patches) and Keyword-Scoped Attention (KSA) for subject-driven conditions (attention confined to keyword-activated regions). A Condition Cache mechanism reuses KV projections across denoising steps, enabled by a design where condition tokens only self-attend. The paper also introduces an early-timestep sampling strategy for fine-tuning. Experiments on FLUX.1 show up to 10× inference speedup and 5.12× VRAM reduction while maintaining competitive generation quality.

## Strengths

1. **Empirically-motivated design from attention sparsity analysis (Figures 2-3).** The paper first investigates attention patterns in an existing multi-condition DiT and documents that spatial-condition attention is diagonally concentrated and subject-condition attention activates only keyword-relevant regions. This data-driven motivation grounds PAA and KSA in observed behavior rather than architectural convenience, distinguishing this work from prior approaches that adopted "concatenate-and-attend" without questioning its necessity.

2. **Efficiency gains that compound with the number of conditions (Figures 7-8).** PKA's inference time stays nearly flat as conditions grow from 4 to 16, while the full-attention baseline (UniCombine) scales super-linearly from ~25s to over 175s, yielding a 10× speedup at 16 conditions. VRAM reduction reaches 5.12× at 16 conditions. Because the bottleneck grows quadratically with condition count, the fact that PKA's advantage *increases* with more conditions directly substantiates the paper's central claim.

3. **Competitive quality on most metrics (Table 1).** On Subject-Depth and Canny-Depth tasks, PKA achieves the best FID, SSIM, controllability (F1 or MSE), CLIP-I, and DINOv2. On Subject-Canny, PKA wins on FID, SSIM, CLIP-I, and DINOv2 while trailing on edge F1. This demonstrates that the large efficiency gains do not come at a universal cost to generation quality.

4. **Perturbation analysis motivating early-timestep sampling (Figure 5).** The "High-to-Low" vs "Low-to-High" perturbation experiment provides quantitative evidence (SSIM scores across step counts) that visual conditions exert stronger influence at early denoising stages — an interesting empirical finding specific to multi-condition DiT fine-tuning.

## Weaknesses

### Major

- **F1 controllability degradation on Subject-Canny is substantial and downplayed (Table 1).** On the Subject-Canny task, PKA achieves F1=0.414 vs UniCombine's 0.551 — a 25% relative degradation (0.137 absolute gap) in edge-map adherence. The paper describes this as "the minor exception of a narrow margin" and the text fidelity difference as "perceptually negligible." An F1 drop from 0.55 to 0.41 is not narrow; it represents materially worse spatial controllability on this specific task. Since the paper's abstract claims the method "maintains or improves generative quality and controllability," this exception should be honestly characterized and its practical implications discussed, not minimized.

- **Baseline training is not controlled for equivalent comparison (Section 4.1).** The paper states it fine-tunes FLUX.1 with LoRA on a curated Subject200K subset for 20,000 iterations, but does not specify whether OminiControl2 and UniCombine baselines were fine-tuned on the same data and configuration or used in a default pretrained form. The sentence "To ensure a fair comparison, we fine-tune the FLUX.1 model using LoRA" only explicitly describes what the authors did for their method. If the baselines were not equivalently trained, the quantitative advantages claimed in Table 1 (FID, SSIM, CLIP-I, DINOv2) cannot be attributed to the architectural improvements. This ambiguity undermines the quality comparisons.

- **PixelPonder is cited in Related Work but not included as a baseline.** The paper mentions PixelPonder as a related efficient multi-condition method that addresses the same problem using dynamic token pruning, yet never compares against it in the experiments. For a paper whose central claim is efficiency, omitting the most directly comparable efficient method weakens the evaluation.

### Minor

- **Early-timestep sampling strategy is only qualitatively validated (Figure 11).** While the perturbation analysis (Figure 5) motivating the approach is quantitative, the actual evaluation of the shifted logit-normal distribution (μ, δ settings) is shown only as a grid of images with no quantitative metrics — no FID curves across iterations, no controllability metrics for different settings, and no ablation that isolates the sampling contribution. The convergence and control-fidelity claims for this component are unsupported by experimental evidence.

- **No error bars or variance estimates reported.** All metrics in Table 1 are single values. For FID (sensitive to sample composition) and for metrics where differences are tiny (e.g., CLIP-T differences of 0.002–0.004), the absence of any reliability measure makes it impossible to assess whether the claimed improvements are real or within noise.

- **Data curation details are vague (Section 4.1).** The paper says it "curates a subset from Subject200K" ensuring each caption contains a descriptive keyword, but does not report the subset size, the fraction filtered out, or the train/test split breakdown. This makes independent assessment of the evaluation regime difficult.

- **KSA mask stability over timesteps is not analyzed.** KSA computes a mask at step t and reuses it at step t+1, citing "temporal consistency" (Zhou et al., 2025). No analysis is provided of how much the mask actually changes between adjacent timesteps — a core assumption that, if violated, could degrade quality by filtering out relevant regions or including irrelevant ones. The paper references prior work for the temporal consistency property, but validation in this specific setting would strengthen the work.

### Trivial

- The paper states computational complexity as O(c²n²) in the introduction, but the actual quadratic term involves (M+N+N_I)² since text tokens also contribute. The qualitative point is unaffected, but the formalism could be more precise.

## Nice-to-Haves

- A controlled experiment comparing all methods (including OminiControl2 and UniCombine) fine-tuned on the same data with the same LoRA configuration would resolve the training ambiguity.
- Quantitative evaluation of the early-timestep sampling strategy (e.g., FID vs. training iterations for different μ, δ settings) would substantiate the convergence claim.
- Including PixelPonder as a baseline would strengthen the efficiency comparison.
- Discussion of failure cases or scenarios where the sparsity assumption does not hold (e.g., when subject conditions span most of the image).

## Removed Points

These points were raised by reviewers but removed after verifying against the paper:

- *"Headline efficiency numbers conflate a standard engineering trick (KV caching) with the paper's novel modules."* Removed because the Condition Cache is architecturally enabled by the design choice that condition tokens only self-attend — a core part of PKA. The paper attributes the speedup to the PKA framework as a whole, not solely to PAA/KSA. Moreover, the cache cannot be cleanly ablated without reverting the attention structure, so the claim of conflation is not supported by the paper's presentation.
- *"No discussion of limitations."* Removed as a general observation without specific anchor in the paper — the conclusion section is standard for this venue.
- *Various formatting and notation nitpicks.* Removed as parser artifacts or overly pedantic (e.g., "O(c²n²)" imprecision — the qualitative point is unaffected).
- *"The complexity formalism is misleading."* The paper says O(c²n²) for visual condition tokens, which is correct for that subset; the full sequence includes text tokens but this does not change the qualitative conclusion.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify baseline training setup.** State explicitly whether OminiControl2 and UniCombine were fine-tuned on the same data and LoRA configuration as the proposed method. If they were, the ambiguity is easily resolved. If not, add controlled experiments.
2. **Honestly characterize the Subject-Canny F1 trade-off.** Discuss its practical implications and whether different KSA thresholds can mitigate it. A dedicated experiment showing the F1-efficiency Pareto frontier would turn this weakness into a strength.
3. **Quantify the early-timestep sampling contribution.** Add a plot of FID vs. training iterations for different (μ, δ) settings, and report final quality metrics for the best setting vs. the default.
4. **Include PixelPonder as a baseline** or clearly justify its omission (e.g., if it targets a different base model or setting).
5. **Add confidence intervals** for the main quantitative results in Table 1, at minimum for FID.
6. **Report dataset curation statistics** — subset size, filter fraction, train/test split.

## Score and Decision

All retrieved anchors (paths only):

**Round 1 (bracketing):**
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Jt1gGIumJo.md (3.00, weak band) — rejection-level paper with major flaws; current paper is clearly stronger
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/DJSZGGZYVi.md (3.00, weak band, sim 0.72) — not directly comparable topic
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/QKqWnNkwPL.md (3.00, weak band) — distillation paper; current paper is clearly stronger
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/iG7qH9Kdao.md (5.00, middle band) — empirical scaling study without novel technical contributions; current paper has more technical novelty
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/D2as3jDmRA.md (6.25, middle band) — LinFusion: linear attention for diffusion; slightly stronger than current paper
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/kALZASidYe.md (3.75, middle band) — controllability paper with exposition/novelty issues; current paper is stronger
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/lWGXftRS5h.md (5.00, middle band) — DiT inductive biases study; different focus
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/gU58d5QeGv.md (8.00, strong band) — Würstchen architecture; stronger than current paper

**Round 2 (narrowing):**
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/r2uhY4pXrb.md (5.50, ViCo) — personalized generation with visual conditioning; comparable quality profile (real contributions + evaluation gaps)
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/T1MTmAlF7x.md (5.00, EDM2+) — architecture exploration without novel technical contribution; current paper has more novelty
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/gKui6QvvfK.md (5.25) — compositional VQ sampling; different topic
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/uJqKf24HGN.md (7.00, UniCon) — unidirectional control adapter; stronger evaluation than current paper
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/lTrrnNdkOX.md (6.40, Qihoo-T2X) — proxy-tokenized DiT; slightly stronger due to fewer evaluation gaps

**Round 1 bracket:** Between 3.5 and 7.0, plausibly in the 5.0-6.0 range.

**Round 2 narrowing:** Compared to ViCo (5.5), the current paper has similar strengths in technical contribution but more significant evaluation issues (baseline training ambiguity + F1 degradation). Compared to EDM2+ (5.0), the current paper has stronger technical novelty. The paper is weaker than Qihoo-T2X (6.4) and LinFusion (6.25) due to these evaluation issues. **Final score: 5.0**, reflecting a paper with genuine contributions and impressive efficiency results, but evaluation gaps that prevent the claims from being fully substantiated.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>