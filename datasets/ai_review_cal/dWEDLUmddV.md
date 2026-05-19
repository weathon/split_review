- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5
Now I have a clear picture of the paper and can verify each claim. Let me produce the final consolidated review.

---

## Summary

This paper identifies a previously overlooked problem in trajectory-matching dataset distillation: matching different trajectory segments can be negatively correlated, leading to accumulated trajectory error and a form of catastrophic forgetting. The authors quantify this via Pearson correlation heatmaps (Figures 1–2), formalize the impact through accumulated error analysis (Theorem 1), and propose ConTra — a concurrent (multi-task) training strategy that matches multiple segments simultaneously rather than sequentially. Experiments on CIFAR-10/100, Tiny ImageNet, and ImageNet-1K (appendix) show consistent improvements over prior TM-based methods, with gains up to 3.1% on CIFAR-10 IPC=1. The ablation studies confirm that concurrent training works as a plug-in module for MTT and DATM.

## Strengths

1. **Empirical discovery and quantification of negative correlations between trajectory segments.** Figures 1(a) and 2 provide Pearson correlation heatmaps across IPCs, directly showing that matching later epochs negatively correlates with earlier epochs (lower-triangular dominance at small IPC). This is a concrete, measurable phenomenon that prior work did not analyze.

2. **Principled framing of trajectory matching as a continual learning problem.** Section 5 draws an explicit parallel between sequential segment matching and catastrophic forgetting in continual learning, then motivates concurrent training (MTL) as the natural upper-bound solution. This framing is conceptually clean and leads directly to the proposed method.

3. **Consistent empirical outperformance across multiple benchmarks.** Table 1 shows ConTra surpassing prior SOTA (DATM, MTT, FTD, TESLA) on CIFAR-10, CIFAR-100, and Tiny ImageNet at multiple IPCs. The gains are particularly pronounced at low IPC (e.g., +3.1% on CIFAR-10 IPC=1), where negative correlations are most severe — directly validating the thesis.

4. **Ablation evidence isolates the core mechanism.** Table 3 demonstrates that concurrent training, when plugged into MTT and DATM, improves both by 0.3%–3.6%, confirming that the benefit comes from the proposed module rather than from other design choices. Figure 3 further shows that ConTra transforms negative correlations into predominantly positive ones.

5. **Cross-architecture generalization.** Table 2 shows that synthetic datasets distilled with ConTra (using ConvNet) transfer well to AlexNet, VGG11, ResNet18, and DenseNet121, outperforming prior TM-based methods across all architectures tested.

## Weaknesses

### Fatal

None.

### Major

- **Ambiguity in baseline comparison fairness.** Section 6.1 states that the authors "use the soft label and initialization with correct samples introduced in (Guo et al., 2023)" but does not specify whether all baselines in Table 1 were re-run under these same conditions. DATM (Guo et al., 2023) inherently uses them, but MTT, FTD, TESLA, and others were originally reported without these enhancements. If baseline numbers were taken from original papers (lacking these tricks), the reported gains may partly reflect the training enhancements rather than concurrent training itself. The note "For FTD, we followed the settings from (Guo et al., 2023)" suggests some re-running was done, but the scope is unclear. This must be explicitly clarified for the reported comparisons to be interpretable. *(Verifiable: Section 6.1 states the tricks are used, but no statement confirms baselines were re-run with them.)*

### Minor

- **ImageNet-1K and NAS results are referenced but not summarized in the main text.** Section 6.6 states that ConTra scales to ImageNet-1K (via TESLA) and performs well on a NAS downstream task, but no numerical results appear in the body (they are in the appendix, which is stripped by the PDF parser). For a paper claiming scalability as a contribution, a compact summary table or headline number in the main text would substantially strengthen the presentation. *(Verifiable: Section 6.6 lines 204–210 mention these experiments qualitatively but give no numbers.)*

- **The definition of "lossless" is not explicitly stated.** The paper claims "ConTra achieve lossless condensation with a 20% ratio on CIFAR-10" (line 158) but does not state the full-dataset baseline accuracy or the threshold used to define "lossless." The term follows Guo et al. (2023)'s convention, but readers should not need to cross-reference another paper to interpret a central claim. *(Verifiable: Line 158 asserts lossless condensation but provides no baseline reference or threshold definition.)*

- **Hyper-parameters β, K, and R lack principled guidance.** The paper relies on empirical tuning (Figure 4) for β and K, and sets R = ⌊(T⁺−T⁻)/K⌋. While the rationale for spacing segments is explained, there is no systematic study or heuristic for choosing these values on a new dataset. This is not a fatal gap (ablation covers the main effects) but limits the method's portability. *(Verifiable: Section 5 describes Eq. 8 with β, K, R; Figure 4 provides empirical sweeps but no principled selection rule.)*

- **Continual-learning baselines (EWC, SI) mentioned but not quantitatively reported.** The paper states (line 135) that EWC and SI "do bring some improvements, but none are as simple and effective as directly conducting concurrent training." Reporting these numbers (even if inferior) would strengthen the continual-learning analogy and rule out alternative explanations. *(Verifiable: Line 135 mentions trying EWC/SI without reporting results.)*

### Trivial

None.

## Nice-to-Haves

- A convergence plot of test accuracy vs. wall-clock time (or vs. gradient steps on the synthetic dataset) would better demonstrate the practical efficiency gain claimed for larger K, beyond the per-iteration cost reported in Table 4.
- A dedicated limitations paragraph discussing (i) increased per-iteration cost for large K, (ii) sensitivity to β and K, and (iii) the failure to generalize to Transformers (acknowledged but not analyzed) would improve the paper's completeness.

## Removed Points

- **"The paper does not comprehensively cite prior work that touched on similar issues"** — Removed per the rule against citing a lack of citations as a weakness without external verification. The paper adequately cites relevant TM works (MTT, FTD, DATM) and discusses DATM's coarse-grained study.
- **"The theoretical discussion is largely a re-statement of Du et al. (2023)"** — Removed because the paper does not claim novel theory; it acknowledges Du et al. and uses their framework to formalize why negative correlations matter. This is a legitimate application of existing theory.
- **"Missing continual learning comparison (EWC, SI)" framed as a "Strengthening the Paper" point** — Demoted from the harsh critic's emphasis to Minor (above) because the authors tried them and report qualitative results, but the absence of numbers is a genuine minor gap.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not articulate.

## Suggestions

1. **Clarify the baseline comparison protocol.** State explicitly whether every baseline in Table 1 was re-run with soft labels and correct-sample initialization, and if so, cite the source of each number. If some numbers are from original papers, re-run those baselines under identical conditions or explicitly note which tricks each baseline uses.
2. **Add a compact summary of ImageNet-1K and NAS results to the main text** (e.g., "ConTra achieves X% on ImageNet-1K at IPC Y, compared to TESLA's Z%"). This can be a single sentence or small table.
3. **Define "lossless" explicitly** in the experiments section (e.g., "within 1% of the full-dataset baseline accuracy").
4. **Report the EWC/SI numbers** from the experiments mentioned in line 135, even if they underperform — this strengthens the paper's own framing.
