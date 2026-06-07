## Summary

This paper presents a benchmark for evaluating semi-supervised learning (SSL) algorithms under "open environment" conditions where labeled and unlabeled data differ in data distribution, feature space, or label space. It contributes (1) six robustness metrics derived from a Robustness Analysis Curve (RAC), (2) a theoretical generalization bound decomposing SSL error into five components, and (3) an empirical benchmark comparing 20 SSL algorithms across 9 datasets spanning tabular, image, and text modalities under three inconsistency types.

## Strengths

- **Multi-metric robustness evaluation framework (RAC-based).** The six metrics (AUC, EA, WA, EVM, VS, RCC) capture distinct facets of robustness across a continuum of inconsistency levels, going beyond prior work that evaluates only at Acc(0) or a single perturbation point. The paper validates this framework by showing empirically that Acc(0) is inconsistent with the new metrics — algorithms with high clean accuracy can perform poorly under open-environment conditions, justifying the need for richer evaluation.

- **Large-scale, multi-modal, multi-algorithm benchmark.** The paper evaluates 20 SSL algorithms (6 statistical, 10 deep, 4 robust) across 9 datasets spanning 3 modalities under 3 inconsistency types, within a unified re-implementation toolkit (LAMDA-SSL). This is substantially more comprehensive than prior robust SSL evaluations, which typically focus on a single modality and a single inconsistency type.

- **Non-trivial finding that statistical SSL can outperform deep SSL on tabular data.** The paper reports that Assemble (ensemble-based statistical SSL) shows strong performance and robustness on tabular datasets, often exceeding deep SSL methods. This challenges the default assumption of deep SSL superiority and suggests a need for more SSL research on tabular data.

- **Finding that several dedicated robust SSL algorithms fail to deliver cross-type robustness.** The observation that MTCF and Fix-A-Step achieve lower robustness than ordinary deep SSL algorithms across scenarios is practically relevant, though the paper should more carefully caveat that these methods were designed for specific inconsistency types.

## Weaknesses

### Fatal

None.

### Major

- **Insufficient statistical power for a benchmark paper making comparative claims.** The evaluation uses only 3 random seeds (lines 102), 6 t-values (0, 0.2, 0.4, 0.6, 0.8, 1.0) with linear interpolation between them, and reports no standard deviations, confidence intervals, or measures of variance anywhere in the paper or its image tables. For a paper whose primary output is comparative findings (e.g., "UDA... significantly improving the robustness over FixMatch," "Assemble demonstrates the best performance and remarkable robustness" — line 170), the reader cannot assess whether any observed difference is meaningful or could reverse under a different random draw. This is the single most significant limitation: it substantially weakens the reliability of every comparative conclusion the paper draws.

- **Theoretical framework is disconnected from the empirical work.** Theorem 3.1 (lines 72–80) presents a complex generalization bound decomposing expected error into five components (bias, variance, Disc_D, Disc_F, Disc_L). However, the bound is never operationalized: it is not instantiated on any dataset, not used to compute a quantity, not referenced in the experimental analysis (Sections 4.2–4.5), and the three qualitative conclusions drawn from it (lines 84–85) are pre-theoretic intuitions that could be stated without the theorem. The abstract and introduction present the theory as a co-equal contribution alongside the metrics and benchmark, but it does not actually contribute to interpreting or explaining any empirical result. This inflates the paper's claimed contributions beyond what it delivers.

- **Misleading evaluation of robust SSL methods without proper caveats.** The paper evaluates UASD (designed for open-set SSL / label-space inconsistency), CAFA (designed for domain-adaptive SSL / distribution shift), and MTCF (designed for multi-class open-set scenarios) across *all* inconsistency types uniformly, then concludes they "do not consistently exhibit enhanced robustness and may not surpass ordinary deep SSL algorithms in most scenarios" (line 20). Evaluating a method specialized for label-space mismatch on feature-space mismatch (grayscale CIFAR images) and concluding it is not robust is not informative. The paper should either evaluate each method on the inconsistency type it targets and note mismatches, or explicitly reframe the finding as "robust SSL methods are not transferable across inconsistency types" — a different and weaker conclusion. The current framing is misleading.

### Minor

- **Unsupported claim about inconsistency sometimes being beneficial.** The paper states (lines 21 and 180) that "inconsistency... does not invariably result in negative effects... leveraging inconsistent unlabeled examples may improve performance in some cases." This is presented as a key finding, but no specific experiment, table row, or figure is cited to support it. The claim is unsubstantiated within the paper's own experimental scope.

- **Underspecified mapping t → θ(t).** The paper defines θ(t) as "the function describing the ratio of inconsistent examples in the unlabeled dataset to t" (line 37) but never specifies the actual mapping. Since the RAC x-axis is t and the paper samples t uniformly, the reader cannot interpret what a change from t=0.4 to t=0.6 means in terms of actual data composition. This limits the interpretability of all RAC-based metrics.

- **Grayscale construction for feature-space inconsistency lacks architectural detail.** For CIFAR-10 and CIFAR-100, feature-space inconsistency is simulated by converting images to grayscale, reducing input from 3 channels to 1 (line 132). The paper does not state whether the first convolutional layer was modified to accept 1-channel input or whether grayscale was replicated across 3 channels. These choices produce very different behaviors and the omitted detail affects both reproducibility and interpretation — the observed degradation could be an artifact of architectural incompatibility rather than a property of SSL algorithm robustness per se.

- **No limitations discussion.** A benchmark paper should transparently acknowledge that its inconsistency constructions are synthetic, that conclusions may not generalize to real-world open environments (which often have multiple simultaneous inconsistencies), that the t-sampling is coarse, and that the number of seeds is low. The conclusion (Section 5) contains no such discussion.

### Trivial

- "The subsequent details about this work will be continuously supplemented and improved" (line 187) is an unusual closing for a conference submission, implying the work is incomplete.

## Nice-to-Haves

- Reporting variance over more seeds (≥10) and densifying the t-grid (e.g., every 0.1) would substantially increase the benchmark's informativeness.
- Statistical tests (e.g., Wilcoxon signed-rank) comparing algorithms across seeds and datasets would strengthen comparative claims.
- An ablation on backbone choice would help assess whether relative rankings are robust to architectural decisions.
- Connecting the generalization bound to at least one experimental setting (even a stylized or synthetic case) would give the theoretical contribution operational meaning.

## Removed Points

These are flagged for removal; treat with caution:

- **Strength: "Empirical discovery that inconsistency is not uniformly harmful."** Moved here because this strength conflicts with the verified weakness that the claim is made without citing specific experimental evidence.
- **Criticism on Finding 1 ("generality across other datasets is unestablished"):** This is a generic scope critique applicable to virtually any empirical study; it does not identify a specific error in the paper's own evidence. The paper never claims universal generality across all possible datasets.
- **Criticism about tables being images / numbers "hidden":** This is a parser artifact from the PDF extraction, not an author error. The original submission contains proper formatted tables.
- **Criticism about "no statistical tests":** Framed as a hard weakness but properly belongs as a nice-to-have enhancement, not a flaw in the paper as written.

## Novel Insights

None beyond the paper's own contributions. The reviews largely recapitulate the paper's findings and identify standard methodological gaps rather than offering new analytical perspectives.

## Suggestions

1. Report standard deviations or confidence intervals for all metric entries, using substantially more random seeds (≥10) at critical t-values. This is the single highest-leverage improvement.
2. Separate the robust SSL evaluation into "matched-type" analysis (evaluate each method on the inconsistency type it targets) and "cross-type" analysis (exploratory), with proper caveats for the latter.
3. Either (a) connect the generalization bound to the experimental results by instantiating it on at least one case, or (b) move it to an appendix and clearly label it as a preliminary formalism whose empirical validation is future work.
4. Provide concrete evidence for the claim that inconsistency can sometimes improve performance, citing specific table rows or figures, or remove the claim.
5. Specify the mapping t → θ(t) and the architectural adaptation for the grayscale image experiments.
6. Add a limitations section discussing the synthetic nature of inconsistency constructions, scope of conclusions, and statistical power constraints.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>