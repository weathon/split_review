Now I have verified all the reviewer claims against the paper. Let me produce the consolidated review.

---

## Summary

This paper identifies a counterintuitive phenomenon: removing certain "difficult-to-learn" examples (those near class boundaries) can improve unsupervised contrastive learning performance. The authors formalize this through a similarity graph model with three similarity parameters (α for same-class, β for easy inter-class, γ for hard inter-class), derive linear probing error bounds proving that difficult examples hurt generalization, and theoretically show that removal, margin tuning, and temperature scaling each tighten these bounds. Empirically, they propose a simple cosine-similarity percentile-based selection mechanism and demonstrate consistent accuracy improvements across CIFAR-10/100, STL-10, and TinyImagenet, with gains up to 15.0% on TinyImagenet via the combined method.

## Strengths

1. **Novel theoretical framework that formally models difficult-to-learn examples in contrastive learning.** The paper introduces a similarity graph with explicit parameters (α, β, γ) to capture the higher similarity of different-class pairs that contain boundary-near examples (Section 3.2). It then derives linear probing error bounds (Theorems 3.1, 3.2) that rigorously prove the presence of these examples worsens generalization (the bound in Theorem 3.2 is strictly larger than that in Theorem 3.1). This is a genuine conceptual contribution to a topic that prior theory largely ignored.

2. **Theoretical characterization of three practical strategies for mitigating the negative impact.** The paper proves that removing difficult examples (Corollary 4.1), applying margin tuning (Theorems 4.2, 4.3), and temperature scaling (Theorems 4.4, 4.5) each tighten the error bound, and provides explicit conditions under which the bounds approach the ideal no-difficult-example case. Connecting theory to concrete hyperparameter strategies is non-trivial.

3. **Consistent empirical validation of the core phenomenon across multiple datasets and large gains on TinyImagenet.** The controlled mixing experiment (Figure 2) isolates the causal effect of adding/removing difficult examples. On TinyImagenet, margin tuning yields +13.7%, temperature scaling yields +12.8%, and the combined method yields +15.0% over baseline SimCLR (Tables 2–4). These are substantial improvements, not marginal.

4. **Simple, efficient selection mechanism with sensitivity analysis.** The proposed mechanism uses cosine similarity percentiles from the current batch (no pretrained model required). Figures 4(a,b) show the method is not sensitive to exact percentile choices, and Figure 4(c) validates that the selected interval contains mostly different-class pairs. The mechanism is computationally cheap and straightforward to implement.

## Weaknesses

### Fatal
None.

### Major

1. **No standard deviations or error bars reported despite multiple runs.** All tables report "Results are averaged over three runs" but never provide standard deviations, confidence intervals, or per-run values. Given that improvements on CIFAR-10 are 0.6%–1.6% (Tables 1–4), these could fall within run-to-run noise. Without variance information, the reader cannot assess whether the observed gains on smaller datasets are statistically meaningful. This is the most consequential experimental shortcoming.

2. **The theoretical framework's core model (uniform α, β, γ) is neither validated nor relaxed in ways that connect to practice.** The entire theoretical edifice rests on the assumption that all same-class pairs have identical similarity α, all easy inter-class pairs have β, and all difficult inter-class pairs have γ. The paper mentions a relaxation in Section B.3 but does not give its content in the visible portion, and all core theorems are derived from the idealized parameters. There is no empirical measurement of α, β, γ on real datasets, no synthetic experiment where the ordering is violated to test robustness, and no argument that this uniform model captures the essential heterogeneity of real augmentation graphs. This gap weakens the claim of a "unified theoretical framework."

3. **The theoretical predictions are not directly tested.** The paper derives specific conditions: Corollary 4.1 gives a condition under which removal improves the bound, Theorem 4.5 gives conditions under which temperature scaling helps, and Theorem 4.3 specifies a margin value involving unknown parameters (γ, β, etc.). Yet none of these conditions are empirically verified — e.g., by varying the fraction of removed samples and checking whether performance tracks the predicted bound ordering, or by sweeping ρ and checking whether the optimal value matches the theoretical expression. The experiments apply a fixed procedure and report accuracy, which does not confirm the causal mechanism claimed.

4. **Missing comparisons to relevant hard-negative handling baselines.** The paper cites Robinson et al. (2020) and Kalantidis et al. (2020) in the references but does not compare against their methods experimentally. While Figure 1 does compare against the SAS baseline (Joshi & Mirzasoleiman, 2023) — contrary to the reviewer's claim that it does not — the absence of comparisons to Robinson et al. (hard negative sampling) and Kalantidis et al. (hard negative mixing) means the practical benefit of the proposed approach is uncalibrated against established techniques in the same problem space.

### Minor

1. **Percentage of data removed is not reported for the removal experiment (Table 1).** Without knowing what fraction of the dataset was discarded, the trade-off between sample size reduction and the beneficial effect of removing difficult examples cannot be evaluated. This is an easily fixable omission.

2. **The mixing experiment (Section 2) uses pixel-level linear interpolation to create difficult examples, which may produce unnatural artifacts** (blended labels, linear combinations that do not resemble natural boundary examples). The paper does not discuss whether such samples are a good proxy for the γ-type pairs in the theoretical model or whether the conclusions hold for naturally-occurring difficult examples.

3. **The optimal hyperparameters σ (margin) and ρ (temperature scaling factor) are not reported in the main text.** The main text introduces σ and ρ but gives no indication of their values, how they were chosen, or whether performance is sensitive to their settings. The paper defers to the appendix (Section A.4), but the main text should at minimum state the range used or mention that they were tuned on a validation set. Without this, the results are not reproducible from the main text alone.

4. **The "failed to notice" characterization of Joshi & Mirzasoleiman (line 11) is rhetorically ungenerous.** It is a minor presentational issue, but the paper would benefit from a more measured tone when describing prior work.

### Trivial

None beyond the above.

## Nice-to-Haves

- **Estimate α, β, γ on real datasets** (e.g., using trained representations) to ground the theoretical model empirically and verify that the assumed ordering 0 ≤ β < γ < α < 1 holds in practice.
- **Directly test a theoretical prediction:** vary the fraction of removed samples and check whether performance follows the trend predicted by Corollary 4.1, or vary ρ and check whether the optimal ρ matches the expression in Theorem 4.5.
- **Include ImageNet-1K results in the main text** rather than only in the appendix (the paper mentions they exist in Section A.5).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper never compares to SAS (Joshi & Mirzasoleiman) in the main tables."** — Factually incorrect. Figure 1 compares against SAS core subsets across all four datasets. The criticism is removed.
- **"No comparison to existing methods for handling hard negatives (Joshi & Mirzasoleiman 2023)"** in the context of SAS — Partially removed (the SAS comparison exists in Figure 1). The criticism about Robinson et al. and Kalantidis et al. is retained in Major #4 above since those methods are indeed not compared.
- **"The framing that a 'universal phenomenon' is demonstrated by Figure 1 is overstated — Figure 1 shows only four datasets"** — The paper justifies this as "multiple datasets" and shows consistent results across four commonly-used benchmarks. Calling it "overstated" is a judgment that is not strictly a weakness of the paper. Removed.
- **"The selection mechanism... still depends on the current representations"** — The paper claims it "does not rely on pre-trained models" which is technically true; using online features is standard practice and does not constitute a weakness.
- **"The condition in Theorem 4.3 that the margin must be set to a specific expression involving unknown parameters makes it practically irrelevant"** — Many theoretical results provide structural insight (e.g., "more challenging examples need larger margins") without being directly deployable as formulas. This is standard in theoretical ML papers and is not a weakness.
- Any formatting, grammar, or style nitpicks — These are parser artifacts, not author errors.

## Novel Insights

The most interesting synthesis emerging from these reviews is how the two perspectives converge on the same core tension: the paper has a genuine theoretical contribution (the similarity-graph modeling of difficult examples and the unified treatment of three mitigation strategies) that is intellectually coherent under its stated assumptions, but it fails to bridge the gap between those assumptions and empirical practice. The harsh critic correctly identifies that the simplified uniform model is never validated, the theoretical conditions are never tested directly, and the experimental rigor (error bars, missing baselines) is insufficient for the claims. Meanwhile, the strength finder correctly identifies that the theoretical derivations are non-trivial, the phenomenon is real, and the empirical gains on TinyImagenet are substantial. The paper's central weakness is not that its theory is wrong, but that it does not do the work to connect theory to practice — no empirical measurement of α/β/γ, no direct bound tests, no robustness checks against model misspecification. The paper reads as a solid first draft of a theory that needs a much tighter empirical loop to be convincing.

## Suggestions

1. **Report standard deviations for every table.** Since the authors already ran three seeds, this requires zero additional computation. It is the single most impactful fix.
2. **Add at least one direct test of a theoretical prediction.** For example, vary the fraction of removed samples and plot accuracy alongside the bound behavior predicted by Corollary 4.1. Alternatively, sweep ρ in temperature scaling and show that performance peaks near the theoretically motivated value.
3. **Report the percentage of data removed in Table 1** so readers can evaluate the removal trade-off.
4. **Add comparisons to Robinson et al. (hard negative sampling) and/or Kalantidis et al. (hard negative mixing)** in at least one experiment to calibrate the proposed approach.
5. **Provide an empirical estimate of α, β, γ** on one dataset (e.g., using the trained SimCLR representations on CIFAR-10) to show that the assumed ordering holds and to quantify the gap γ−β. This would substantially strengthen the credibility of the theoretical model.
6. **Report the values of σ and ρ used** and describe how they were selected (grid search? rule of thumb?).
7. **Soften the "failed to notice" wording** about prior work — it adds nothing and may alienate readers.

## Score and Decision

The paper makes a genuine theoretical contribution to an underexplored problem and shows consistent empirical support. However, the experimental validation has several significant gaps (no error bars, no direct test of theoretical predictions, missing comparisons) that prevent the claims from being fully supported. The theoretical model, while internally sound, is disconnected from empirical practice. With the above fixes, especially error bars and direct bound tests, the paper could be substantially strengthened. In its current form, the weaknesses outweigh the contributions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>