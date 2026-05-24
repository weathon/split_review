Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper argues that evaluating model robustness under a single or limited set of shift degrees can produce misleading conclusions, and that performance patterns across shift degrees are often non-monotonic and brittle. The authors conduct experiments on synthetic shifts (noise, rotation, low-light) across MNIST, CIFAR10, and ImageNet subsets, evaluating over 20 DG algorithms and two architectures. They further examine how CLIP behaves under such shifts. The core message—that the *degree* of shift matters and should be varied in evaluations—is sensible and worth making.

## Strengths

1. **Clean demonstration that robustness at high degrees does not always transfer to low degrees (Section 4.3, Figure 5).** The ROTATEDMNIST experiments show that models trained on strong rotation (D₀ & D₈) actually perform *worse* at mild rotations than models trained on clean data alone. This result uses a proper experimental design (training on fixed domain combinations, averaging over 20 random initializations, no test-set-based selection), so it provides clean evidence for a genuinely counterintuitive phenomenon.

2. **Comprehensive algorithmic coverage.** The study evaluates over 20 domain generalization algorithms (ERM, IRM, VREx, Mixup, CORAL, etc.) across two architectures on multiple shift types. This breadth gives the findings reasonable empirical weight, even if some specific quantitative claims are subject to methodological concerns.

3. **Construction of controlled-degree datasets.** NOISYMNIST, ROTATEDMNIST, and LOWLIGHTCIFAR10 are useful resources that allow systematic variation of a single shift type across many degrees. LOWLIGHTCIFAR10's combination of brightness and shot noise is a step toward more realistic synthetic shifts.

4. **GradCAM analysis provides mechanistic insight (Figure 4).** The visualization showing that ERM models rely on local features that become unreliable under noise, while CAD models use global structures, gives a plausible explanation for *why* brittleness occurs. This goes beyond merely reporting accuracy numbers.

## Weaknesses

### Fatal
None.

### Major

1. **Model selection uses test-domain performance, weakening quantitative claims in Section 4.2.** In Table 1 and Figure 3 (left), models trained on D₀ and D₁ are "selected" as top-3 or top-5 based on their accuracy on a specific test degree (e.g., D₄), and their performance drop at adjacent degrees (D₅, D₆) is then reported. This conflates two effects: (a) genuine non-extrapolability of robustness, and (b) regression to the mean—models selected for exceptional performance at one degree will naturally perform closer to the average at another degree, even under perfect correlation. The paper does not compare the D₄-selected models' D₅ performance against a baseline (e.g., all models' average D₅ performance), nor does it use proper validation-based model selection. This does *not* invalidate the paper's core message (the cross-over patterns in Figure 3 are informative), but it undermines the specific quantitative claims in Table 1 (e.g., "50.3% relative drop from D₄ to D₅" for VREx).

2. **Exclusive use of synthetic distribution shifts limits generality.** All experiments use artificially contrived shifts (Gaussian noise, rotation, low-light simulation). While useful for controlled analysis, the paper draws broad conclusions about "robustness" and "OOD generalization" without any evidence from naturally occurring shifts that can be stratified by severity (e.g., ImageNet-C per-severity analysis, medical imaging with varying quality, or WILDS subsets). LOWLIGHTCIFAR10 is still synthetic. The paper would be significantly stronger with at least one real-world continuous-severity benchmark.

3. **The CLIP findings are interesting but over-interpreted.** Section 5 shows that CLIP models drop sharply under Gaussian noise on MNIST, and the paper frames this as "pre-trained models are sensitive to even minute distribution shifts." However, the paper's own hypothesis—that Gaussian noise is rare in CLIP's training data—largely explains this, and the results on rotation (where CLIP does fine) support this explanation. Further adaptation (CLIP1, etc.) substantially recovers performance, which somewhat undermines the "brittleness" narrative. The claim that "pre-trained representations are sensitive" would benefit from a more nuanced framing.

### Minor

1. **No statistical significance testing or confidence intervals in key figures.** Error bars are omitted from Figures 3 and 6, and no significance tests are provided for comparisons (e.g., whether the D₄→D₅ drop differs significantly across algorithms). The paper states "error bars are omitted for clarity (see Appendix B.5 for more details)" for Figure 6, but this practice reduces reader confidence in the patterns.

2. **The paper lacks a limitations section.** Given the methodological choices (synthetic shifts only, test-set-based selection in Section 4.2, limited architectures), a candid discussion of limitations would help readers calibrate the claims and would strengthen the paper.

3. **Section 4.3's most interesting result (rotation vs. noise contrast) lacks mechanistic explanation.** The paper observes that noise robustness transfers to milder degrees while rotation robustness does not, but offers no explanation for *why* the behavior differs (feature isotropy? shift structure? classifier geometry?). This limits the scientific contribution of an otherwise clean experiment.

### Trivial
None.

## Nice-to-Haves

- Redoing the Section 4.2 experiments with proper validation-based model selection (using only D₀/D₁ for validation) would directly test whether the brittleness pattern holds for models chosen in a realistic way.
- Including at least one dataset with a natural severity axis (e.g., ImageNet-C per corruption severity) would substantially strengthen external validity.
- A deeper analysis of *why* rotation and noise produce qualitatively different behavior in Section 4.3, perhaps via feature visualization or analysis of learned representations.

## Removed Points

- **"The brittleness claim conflates selection artifact with model behavior" (Harsh Critic #3):** This is an overstatement. The core observation—that model rankings change across degrees—is not invalidated by the selection method, since Figure 3 (left) shows models selected at *each* degree and compares their full curves, which is a legitimate way to visualize ranking instability. The selection concern mainly affects the specific quantitative drops in Table 1, not the broader conceptual claim.

- **"Section 4.3 describes a known phenomenon" (Harsh Critic):** The paper's observation about rotation robustness not transferring to mild degrees is *not* trivial or well-known, and the comparison with noise is novel.

- **"CLIP results are explained by task mismatch" (Harsh Critic):** The paper explicitly discusses this hypothesis (line 178: "we hypothesize that the sensitiveness is largely because Gaussian noise is very rare in the training data of CLIP"). The critic's point is largely already addressed.

- **Strengths about "importance of the problem" (Strength Finder):** Generic statements about the problem being important are dropped as they lack specific evidence.

## Novel Insights

None beyond the paper's own contributions. The observation that rotation robustness does not transfer to mild rotations (while noise robustness does) is the most interesting specific finding, but the paper does not provide a mechanistic explanation for why these two shift types differ.

## Suggestions

1. Restructure the Section 4.2 experiments to use a proper train/validation split: train on D₀/D₁, select models based on validation accuracy on held-out samples from D₀/D₁ (not on D₄ test accuracy), then report performance curves across all unseen degrees. This would put the brittleness finding on much firmer ground.

2. Include at least one real-world continuous-severity benchmark, such as per-severity analysis on ImageNet-C or a medical imaging dataset with variable acquisition quality.

3. Add a discussion section that honestly addresses: (a) the synthetic nature of all shifts, (b) the selection issue in Section 4.2, (c) the narrow architecture set, and (d) the extent to which the CLIP findings are explained by pre-training distribution mismatch rather than inherent brittleness.

## Score and Decision

**Calibration Anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| CNS-Bench (1STZCCI8mn) | 6.0 | R2 | Stronger overall: better technical approach, cleaner experiments. Current paper is weaker. |
| GDL-DS (LixGd92Wri) | 5.67 | R1/R2 | Similar quality, different weaknesses. GDL-DS had causal framing issues; current paper has selection concern. |
| Frequency Domain (NeKjkOWvwd) | 5.33 | R1/R2 | Similar level: interesting ideas with experimental limitations. |
| OOD-Chameleon (8efAVon0eD) | 3.75 | R1/R2 | Weaker: insufficient experiments, unclear contribution. Current paper is stronger. |
| Robustness Measuring (64vO8qoJfb) | 3.0 | R1 | Weaker: poorly motivated, unclear contribution. |
| Pre-training failures (7LZjuA4AB2) | 3.0 | R1 | Weaker: limited experiments. |

**Round 1 bracket:** 4.0–5.5

**Round 2 narrowing:** The paper is clearly stronger than OOD-Chameleon (3.75) but weaker than CNS-Bench (6.0). It sits closest to the Frequency Domain paper (5.33) and GDL-DS (5.67) in overall quality. However, the methodological concern about test-set-based selection in Section 4.2 and the exclusive reliance on synthetic shifts pull it slightly below these anchors.

**Final score:** 4.5

The paper identifies a genuinely important evaluation gap and presents extensive experiments. However, the central quantitative evidence in Section 4.2 is weakened by the test-set-based model selection procedure, which introduces regression-to-the-mean concerns that are not addressed. Combined with the exclusive use of synthetic shifts and over-interpretation of some CLIP findings, the paper does not quite meet the standard for acceptance.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>