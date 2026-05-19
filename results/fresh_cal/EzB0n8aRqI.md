Now I have all the evidence I need. Let me write the consolidated review.

---

## Summary

This paper studies open-set noise in learning with noisy labels (LNL). It introduces a complete noise transition matrix that accounts for unknown outlier classes, derives error rate inflation bounds for both fitted and overfitted training regimes, and theoretically proves (under a class-concentrated assumption) that open-set noise causes smaller degradation to classification accuracy than closed-set noise at equal noise ratios. The paper constructs CIFAR100-O and ImageNet-O datasets for empirical validation, analyzes 'easy' vs. 'hard' open-set noise modes, and examines entropy-based open-set noise detection.

## Strengths

1. **Generalized noise transition matrix (Definition 3.1).** The paper extends prior work by defining a complete noise transition matrix that handles multiple unknown outlier classes (not just a single meta-class), with a zero block reflecting that noisy labels are never assigned to unknown classes. This is a clean and useful formalization.

2. **Two-case theoretical analysis (Section 3.2).** The paper distinguishes between fitted (model fits the noisy distribution) and overfitted (model memorizes noisy labels) regimes and derives separate error rate inflation expressions for each. This is more realistic than prior work that typically assumes ideal conditions, and the distinction is carried through the experiments (PreActResNet18 for overfitted, pretrained ResNet18 for fitted).

3. **Theoretical comparison of open-set vs. closed-set noise (Theorem 3.7).** The paper formally proves that, under a class-concentrated assumption, open-set noise causes lower error rate inflation than closed-set noise at the same noise ratio. The toy example illustrating why the assumption is needed (different T matrices yielding different error rates from the same O_x, C_x) is helpful.

4. **Empirical validation on new benchmarks.** The paper constructs CIFAR100-O and ImageNet-O datasets and provides experimental results on classification accuracy (Figure 2a/b) that consistently show open-set noise causes smaller accuracy degradation than closed-set noise, across datasets, noise ratios, and both training regimes.

5. **Empirical analysis of entropy-based detection limits (Figure 3).** The paper confirms that entropy dynamics are effective for detecting 'easy' open-set noise but not 'hard' open-set noise, a finding that documents a known detection mechanism's limitations.

## Weaknesses

### Fatal
None.

### Major

- **Contradictory claims about OOD detection trends (Section 4.1, lines 182–183).** The paper states: "the presence of open-set noise degrades OOD detection performance" — then immediately gives as an example: "in the fitted case, the existence of open-set noise leads to steady improvement in OOD detection performance." These two statements directly contradict each other within the same paragraph. "Degrades" and "improves" cannot both be true as general claims about the same phenomenon. This is not a minor wording issue: the paragraph proposes OOD detection as a more discriminative evaluation framework for LNL methods, but the contradictory description of the data undermines the evidentiary basis for that proposal. The authors must clarify which trend actually holds (or whether it depends on dataset, noise ratio, or regime) and reconcile the text with the figures.

### Minor

- **Definition of 'easy' vs. 'hard' open-set noise is not provided in the main text.** The paper uses these terms throughout the experiments (Figures 2, 3) but never defines how they are operationalized — e.g., whether 'hard' means semantically similar outlier classes, or what the construction criteria are for CIFAR100-O and ImageNet-O. The main text should state which classes serve as outliers and how easy/hard is controlled, as these distinctions are central to interpreting the experimental results. (Some details may reside in the appendix, but the main text should be self-contained for this key design choice.)

- **Theorem 3.7 is stated without any proof sketch in the main text.** After a toy example showing why the class-concentrated assumption is needed, the theorem is simply declared ("we have proved") with no intuition, no sketch of why the inequality follows from the assumption, and no explanation of how the result connects to the earlier derivations (Remark 3.6). A brief proof sketch or intuitive explanation would significantly improve readability and trust in the result.

- **No discussion of the class-concentrated assumption's viability.** The paper acknowledges that the assumption is necessary for tractability and provides a helpful toy example showing why. But it never discusses whether real datasets (like WebVision) satisfy this assumption to a meaningful degree, nor how the theorem's conclusions degrade when the assumption is partially violated. A limitations paragraph would strengthen the paper.

### Trivial

- **Typo in Definition 3.3 (line 74):** The text reads "expected to be an open-set noise with probability as O_x and expected to be an open-set noise with probability O_x" — the second "open-set" should read "closed-set."

- **Panel labels in Figure 2 caption (line 178):** The caption says "(a/b)" and "(c/d)" but does not explain which panel is which. The text references these, but the caption should be self-explanatory.

## Nice-to-Haves

- Report results with variance across multiple runs (e.g., 3–5 seeds) for the key comparisons in Figures 2 and 3, to increase confidence that the observed trends are robust rather than noise artifacts.
- Add a dedicated limitations paragraph discussing the class-concentrated assumption, the simplicity of synthetic noise on CIFAR/ImageNet subsets, and the fact that real training often lies between the fitted and overfitted extremes.
- Explain why 'hard' vs. 'easy' open-set noise show opposite trends between fitted and overfitted cases (Figure 2a/b) — the paper notes this intriguing result but never connects it back to the theory.

## Removed Points

- **Vision-language model experiments not discussed in main text.** Removed per the rule that appendix-stripped content is not a valid weakness. These explorations may be fully described in the appendix.
- **Missing related works.** Removed per rule: the reviewer cannot confirm the existence of missing references from external knowledge.
- **Missing error bars / statistical significance.** Moved to Nice-to-Have; single-run evaluation is common practice in this benchmark setting and is not a flaw.
- **Formatting nitpicks and parser artifacts.** Removed per rules about formatting issues being parser errors.
- **Reproducibility concerns about undisclosed hyperparameters.** Removed per rules about trivial implementation details impractical to include in a submission.
- **Speculative "fatal" framing of OOD contradiction.** Demoted to Major (not Fatal) because the contradiction is in presentation/writing, not in the underlying methodology. The core theoretical contributions (Theorem 3.7, error rate inflation analysis) remain intact irrespective of this writing issue.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no new analytical perspectives not already present in the paper's framework.

## Suggestions

1. **Resolve the OOD detection contradiction** — the single highest-leverage fix. Clarify whether open-set noise degrades or improves OOD detection, under which conditions (dataset, noise ratio, regime), and ensure the text and figures are consistent. This is essential for the paper's credibility.

2. **Define 'easy' and 'hard' open-set noise explicitly in the main text**, including how they are operationalized in CIFAR100-O and ImageNet-O (which outlier classes, selection criteria).

3. **Add a brief proof sketch or intuition for Theorem 3.7**, explaining how the class-concentrated assumption leads to the inequality.

4. **Consider adding a limitations paragraph** acknowledging the scope conditions of the theoretical analysis and the synthetic nature of the empirical evaluation.

## Score and Decision

The paper presents a genuinely useful formalization of open-set noise in LNL with clean notation, a sensible two-case analysis, and a theoretically grounded comparison showing that open-set noise is less harmful than closed-set noise. The empirical results broadly support the theory. The main weakness is a clear writing contradiction in the OOD detection claims that undermines one of the paper's proposed contributions. This is fixable with revision and does not invalidate the core theoretical framework. The paper would benefit from slightly more main-text detail about experimental construction and proof intuition, but these are minor.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>