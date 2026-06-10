Now let me finalize and produce the complete review.

## Summary

This paper proposes a formal, mathematically-grounded taxonomy of sample-level hardness types (Mislabeling, OoD/Outlier, Atypical, with subtypes) for data-centric AI, and introduces H-CAT, an open-source benchmarking toolkit. Using H-CAT, the authors evaluate 13 Hardness Characterization Methods (HCMs) across 8 hardness types on MNIST and CIFAR-10, providing statistical comparisons via critical difference diagrams, stability analysis via Spearman rank correlations, and practical tips for HCM selection. 

## Strengths

- **First formal, mathematically-grounded taxonomy of hardness types.** Section 2.1 defines hardness categories through perturbation functions on X/Y and distinguishes them via joint/marginal probability distributions (e.g., OoD vs. Atypical by whether \(P_X^h(S)=0\) or \(>0\) within the support of \(P_X\)). No prior work provides this level of systematic probabilistic formalism; prior definitions were ad-hoc and often overlapping.

- **Table 1 convincingly documents the evaluation gap.** Mapping which of 13 HCMs have been quantitatively/qualitatively evaluated on which of 8 hardness types reveals that ~80% of entries lack any quantitative evaluation (red/orange cells). This provides direct empirical motivation for the benchmark and is a contribution in its own right.

- **Statistical significance testing via critical difference diagrams.** Section 5B uses the Friedman test (\(p \leq 0.05\)) to establish that HCMs within the same broad class are *not statistically different* from each other despite mean rank differences — a stronger methodological standard than the simple ranking comparisons common in prior HCM evaluations.

- **Stability analysis using Spearman rank correlation across seeds.** Section 5C measures rank-order consistency across multiple runs, finding that learning-dynamics methods using output confidence are most stable. This evaluation dimension (consistency of sample ordering) is critical for practical HCM usage but was absent from nearly all prior evaluations.

## Weaknesses

### Fatal
None.

### Major

1. **No random or trivial baselines, making absolute AUPRC values difficult to interpret.** The paper reports heatmaps of absolute D-AUPRC values (Figure 2) without any calibration baseline such as random scoring, constant scoring, or a simple final-epoch loss. AUPRC has a base-rate-dependent floor: a random classifier achieves AUPRC equal to the proportion of hard samples. Without a baseline, the reader cannot tell whether a reported AUPRC of, say, 0.6 is genuinely good or merely reflecting this mechanical property. The relative comparisons and CD diagrams partially mitigate this, but the absolute performance framing — particularly Takeaway A3 ("effective general-purpose HCMs") and the numerical values emphasized in the heatmaps — is weakened by this omission. This is an easily fixable addition that would substantially strengthen the evaluation.

2. **Training hyperparameters and implementation consistency across HCMs are underspecified.** The paper states the HCM module "wraps the trainer module which is a conventional PyTorch training loop" (line 167) but provides no information about optimizer, learning rate, batch size, number of epochs, weight decay, or learning rate schedule. It is unclear whether all 13 HCMs were run under identical training conditions or whether each was tuned to its originally reported configuration. This matters because some HCMs (e.g., Data Maps, Data-IQ) depend on the full training trajectory, while others (e.g., Sample-Loss, Cleanlab) operate at a single point. A table documenting per-HCM training configurations (or confirming a single standardized protocol) is essential for fair comparison, reproducibility, and independent assessment.

### Minor

1. **Empirical scope limited to two small image datasets, while takeaways use general language.** The paper honestly flags that "we focus on image data here" (line 179) and that "10/13 HCMs have been developed for this modality" (line 211), which justifies the choice. However, takeaways such as "Learning dynamics-based methods with respect to output confidence are effective general-purpose HCMs" (A3) and "HCMs should only be used when hardness proportions are low" (A1) are stated as general insights about HCMs, despite being derived from two comparatively small, clean benchmark datasets (MNIST, CIFAR-10) with artificially injected hardness. Whether these patterns hold for text, tabular data, time series, audio, or larger-scale image domains is unknown. The claims would benefit from explicit scoping to the evaluated conditions, or from a small-scale proof-of-concept on at least one additional modality.

2. **AUROC is mentioned but results are not shown.** The evaluator module (line 203) states both D-AUPRC and D-AUROC are computed, but all main figures show only D-AUPRC. If AUROC tells a different story this constitutes selective reporting; if it confirms the same trends, showing it (even in the appendix) would strengthen the evidence. The paper should clarify why AUROC was omitted and/or include it.

### Trivial
None.

## Nice-to-Haves

- A small-scale experiment on a dataset with *natural* (not synthetic) hardness — e.g., CIFAR-10-N or a dataset with known natural label errors — would strengthen the case that the synthetic-perturbation findings transfer to real-world conditions.
- A brief analysis of *why* GraNd becomes uncompetitive at high perturbation proportions (Takeaway A4) would turn an observation into a more actionable insight.
- Compute resource / runtime information would help practitioners assess the practical cost trade-offs of different HCMs.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **"14K setups" claim is rhetorically inflated** (Harsh Critic #4): The paper explicitly defines a "setup" at line 209 ("specific combination of HCM, hardness type, perturbation proportion, dataset, model, and seed"). Counting experimental runs this way is standard in ML benchmarking. The calculation (13 × 8 × ~11 × 2 × 2 × 3 ≈ 13,728) is transparent and not misleading. The criticism conflates "number of runs" with "number of independent conditions" in a way that would disqualify most large-scale benchmarks. **Removed** as an over-interpretation.

2. **Criticism about missing related works**: Not permissible to include without external verification per instructions. **Removed**.

3. **Formatting/style nitpicks** (typos, grammar, garbled characters, whitespace, line breaks, missing symbols): Per instructions, these are parser errors not author errors. **Removed** entirely.

4. **Reproducibility criticism about code/artifact release**: The instruction prohibits questioning the existence/release status of any model, tool, benchmark, or reference cited in the paper. **Removed** per hard rule.

5. **Generic "strength" about problem importance** (from Strength Finder): "This paper addressed an important problem" is generic and applicable to any paper in this area. It lacks specific content tied to this paper's execution. **Removed**.

## Novel Insights

The most interesting observation across the two inputs is that the paper's core contributions — the taxonomy and the toolkit architecture — are largely decoupled from its empirical evaluation. The taxonomy (Section 2.1) is praised by both inputs and stands on its own as a formal contribution independent of the experiments. The toolkit's modular design is a practical contribution that also does not depend on the specific empirical findings. This decoupling means that even if the empirical evaluation has significant gaps, the primary contributions remain intact. However, it also means the paper should exercise more restraint in its empirical claims: the sweeping takeaways (A3: "general-purpose HCMs," A1: "should only be used when...") package the empirical results as settled conclusions, when they are better described as suggestive findings from a narrow (if intensive) experimental scope. The paper would be stronger if it explicitly separated what the taxonomy and toolkit contribute (modality-agnostic framework) from what the experiments show (preliminary image-based patterns).

## Suggestions

1. Add a random-scoring baseline and at least one trivial HCM (e.g., final-epoch cross-entropy loss without training dynamics) to calibrate absolute AUPRC values in the heatmaps.
2. Provide a table documenting training hyperparameters (optimizer, lr, batch size, epochs, scheduler) and clarify whether these were standardized across HCMs or individually tuned.
3. Scope the language of takeaways to the evaluated conditions (image classification on MNIST/CIFAR-10, synthetic perturbations) unless evidence is added from at least one additional modality or scale.
4. Include AUROC results (in appendix if space is constrained).

## Score and Decision

**Score:** 6.0  
**Decision:** Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>