Now I have thoroughly read the paper and can verify the reviewer claims against it. Let me synthesize the final review.

## Summary

This paper proposes a complementary memory system for open-vocabulary continual classification, combining a frozen CLIP zero-shot model (slow/consolidated system) with an exemplar-based fast system. Two main contributions are: (1) **Tree Probe**, a hierarchical clustering-based approach that trains linear classifiers per leaf node, achieving near-constant training time with accuracy close to batch-trained linear probes; and (2) **Adaptive Instance Marginalization (AIM)**, which uses CLIP's summed probability over exemplar labels to adaptively weight predictions from the exemplar and zero-shot models. The system is evaluated across data-incremental, class-incremental, and task-incremental settings plus three flexible inference scenarios, demonstrating speedups of 6x–25x over linear probe while maintaining competitive accuracy and preserving zero-shot capability.

## Strengths

- **Tree Probe offers a practical and well-demonstrated efficiency–accuracy trade-off.** The method achieves near-constant amortized training time (𝒪(log n)) while matching or slightly surpassing linear probe accuracy at sufficient node capacities. Fig. 3(c) and Table 1 show TreeProbe(100k) matching linear probe accuracy with 6× speedup, and TreeProbe(50k) achieving 25× speedup with ~1% accuracy drop. The node capacity ψ provides a principled knob for practitioners to tune this trade-off.

- **AIM effectively balances target-task improvement with zero-shot preservation.** The adaptive weighting mechanism (using CLIP's own summed probability over exemplar labels as the gating weight) is simple, computationally cheap, and validated by results. In class-incremental learning (Fig. 2b), CLIP+LinProbe (AIM-Emb) achieves the best overall accuracy by maintaining reasonable unseen-class accuracy while excelling on seen classes. In flexible inference scenarios (Fig. 2d), AIM-Emb significantly outperforms Avg-Emb across all three evaluation modes.

- **Comprehensive evaluation across diverse scenarios.** The paper tests data-incremental, class-incremental, and task-incremental learning, plus three flexible inference scenarios (Zero-shot, Union+Zero-shot, Mix+Zero-shot). This provides a more thorough assessment than typical continual learning benchmarks. The method is also compared against ZSCL using its exact evaluation protocol (same seed, backbone, prompt ensemble), outperforming it on all metrics (Table 2).

- **Superior to the most related prior work (ZSCL) while being more efficient.** Table 2 shows TreeProbe(50k)+AIM achieves +5.0 points on Target accuracy and +3.8 points on Average vs. ZSCL, while being dramatically more efficient (no GPU needed for exemplar model training beyond embedding extraction).

- **Scales to larger zero-shot models with consistent improvement.** Table 3 shows that with CLIP ViT-L/14, TreeProbe improves target accuracy by +9.2 points over CLIP zero-shot with only 0.1 points zero-shot drop, demonstrating generalization across model sizes.

## Weaknesses

### Fatal
None.

### Major

- **No empirical comparison to any prompt-based continual learning method.** While the paper discusses prompt-based methods (L2P, DualPrompt, CODA-Prompt) in the introduction (line 24) and related work (lines 61–63), arguing they "tend to overfit... losing generalization capability" and cannot meet efficiency goals due to "relatively large computation" (line 101), these arguments remain unsupported by any experimental evidence. Given that prompt-based methods on frozen ViTs are a dominant paradigm in continual learning for visual backbones, and several claim to retain open-vocabulary ability, the absence of an empirical comparison is a significant gap. The paper's claim that "no solution exists that meets all these goals" (line 24) is weakened without demonstrating why these methods cannot be adapted.

- **No variance or statistical significance reported for any result.** All evaluations (Fig. 2, Fig. 3, Table 1–3) are presented as single numbers with no standard deviations, confidence intervals, or multiple seeds. In continual learning, task ordering, data splits, and initialization can produce meaningful variance. While the paper uses a fixed seed for the ZSCL comparison (line 286), this does not provide an estimate of variability. This makes it impossible to assess whether reported improvements (e.g., TreeProbe "slightly surpasses" linear probe) are systematic or within the noise range.

### Minor

- **Tree Probe missing ablations of key design choices.** The paper varies node capacity (ψ), which is the primary tuning knob, but does not ablate: the tree-building algorithm (KMeans vs. alternatives), the number of neighbors (k) used for ensembling, or whether regularization of leaf-level linear models affects accuracy. Without these, it is unclear which components drive TreeProbe's performance.

- **No inference time reported.** The paper extensively reports training efficiency but omits inference time for Tree Probe, which requires finding k nearest leaf nodes and running each corresponding linear classifier, then ensembling. Since inference cost is relevant to practical deployment, this gap partially undermines the practical efficiency claim (though training efficiency is the paper's primary focus, per the stated goal of "efficient incremental learning").

- **AIM's reliance on CLIP probability calibration is not analyzed.** The gating weight α = p(y∈Y_e|I) depends on CLIP's softmax probabilities being reasonably calibrated, at least in a relative sense (distinguishing whether the label set contains exemplar-covered vs. non-exemplar-covered labels). CLIP is known to be poorly calibrated in some settings. While the strong empirical results partially validate the approach, an explicit calibration analysis or sensitivity study (varying α from 0 to 1 to show the oracle trade-off) would strengthen confidence.

- **TreeProbe's accuracy advantage over Linear Probe is marginal.** The paper honestly reports that TreeProbe "slightly surpasses" linear probe (line 275), and the main advantage is speed rather than accuracy. This is fine, but the paper's framing could more clearly emphasize that TreeProbe's contribution is primarily in the speed-accuracy Pareto frontier rather than accuracy alone.

### Trivial
- The AIM-Prob variant (Eq. 8) is presented but never evaluated experimentally — the paper uses only AIM-Emb. The probabilistic variant could be removed or explicitly justified.

## Nice-to-Haves
- **Calibration analysis for AIM:** Plot p(y∈Y_e|I) vs. actual label coverage frequency. Show how AIM behaves when CLIP's estimate is wrong.
- **Inference time comparison:** Report wall-clock inference time for all methods.
- **Sensitivity analysis of AIM:** Vary the gating weight systematically (oracle analysis) to show how close the learned α gets to the optimal trade-off.
- **Ablation of Tree Probe:** Compare KMeans vs. random splits, different k values, and with/without regularization.

## Removed Points
- **"The paper dismisses prompt-based methods in a single sentence in the introduction"** — This is exaggerated. The paper discusses prompt-based methods in three separate locations (intro line 24, related work lines 61–63, method line 101). The substantive concern about missing empirical comparison is retained as a Major weakness; the "single sentence" framing is removed.
- **"The paper does not discuss the assumption that exemplar labels are known at test time"** — The paper is explicit that Y_e (the union of exemplar labels) is known (line 194). This is standard and expected, not a limitation.
- **"The paper states that zero-shot performance of tasks is in supplemental—but without seeing it in the main paper, the reader cannot assess the starting point"** — Per the rule about missing appendix content, this is a parser artifact; the original submission has this content.
- **"How are the linear classifiers trained? Using what loss?"** — The paper states they use linear classifiers trained for 20 epochs with hyperparameters selected from a sweep (line 278). Softmax cross-entropy loss is the standard for linear probes; this level of detail is appropriate for a paper.

## Novel Insights
The reviewers surface an interesting tension: the paper's dismissal of prompt-based methods as incompatible with open-vocabulary efficiency goals (arguing they require "relatively large computation") is at odds with the fact that prompt-based methods are simultaneously the closest competitors and yet operate on fundamentally different principles. The paper's complementary memory systems paradigm (frozen CLIP + fast exemplar model) is genuinely distinct from prompt tuning, which adapts the backbone through learned tokens. This suggests a potentially productive research direction — combining prompt-based adaptation of the slow system with exemplar-based fast learning — that neither the paper nor the reviewers fully explore. Additionally, the acknowledgment that AIM underperforms on Union+Zero-shot when exemplar-covered labels dominate (~91% of candidates) because "AIM likely assigns more weights to the exemplar model" reveals a previously underappreciated failure mode of the method: when the exemplar set covers almost all candidate labels, AIM converges toward an exemplar-only model, losing the zero-shot safety net precisely when the task composition makes it least necessary. This is a nuanced finding worth deeper investigation.

## Suggestions
1. Add error bars (mean ± std over at least 3 random seeds) to all main results.
2. Add at least one prompt-based baseline — adapt a method like L2P or CODA-Prompt to the open-vocabulary setting, or provide a rigorous, evidence-backed argument for why adaptation is non-trivial or impossible.
3. Report inference time for all methods.
4. Add an ablation study for Tree Probe: vary the tree-building method, k for neighbor ensembling, and the effect of L2 regularization.
5. Include a calibration or sensitivity analysis for AIM's gating weight.

## Score and Decision

The paper makes a clear contribution: Tree Probe is a novel and practical method that meaningfully advances the efficiency-accuracy Pareto frontier for exemplar-based continual learning, and AIM provides a simple yet effective fusion strategy. The evaluation is comprehensive across diverse scenarios, and the empirical advantages over ZSCL are clearly demonstrated. The main weaknesses — missing variance reporting, no comparison with prompt-based methods, and missing inference time — are substantive but not fatal; they weaken the evidence but do not invalidate the core contribution. The paper would benefit from revisions to address these gaps before acceptance.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>