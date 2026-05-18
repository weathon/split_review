Now I'll produce the final consolidated review.

## Summary

This paper identifies an underexplored dimension in OOD generalization evaluation: the *degree* (severity) of distribution shifts, not just their type. Through controlled experiments on MNIST, CIFAR-10, and ImageNet subsets with synthetic shifts (noise, rotation, brightness+shot noise, resolution reduction), the paper demonstrates three main findings: (1) models that perform best under mild shifts can suffer drastic accuracy drops under slightly stronger shifts of the same type; (2) training on strong shifts does not uniformly guarantee robustness to milder shifts — the pattern is shift-type-dependent; and (3) CLIP models adapted via linear probing can be extremely brittle to downstream distribution shifts rarely seen during pre-training. The paper's core message — that single-severity evaluations can be misleading — is a valid and important caution for the OOD generalization community.

## Strengths

1. **Novel and practically important problem framing.** The paper identifies that OOD benchmarks largely ignore the *degree* of distribution shift, evaluating only at fixed severities. Showing that rankings reverse and performance collapses across adjacent shift degrees (e.g., Table 1: VREx drops 73.1% from D₄ to D₆) is a concrete demonstration that this oversight can produce misleading conclusions. This is a genuinely underexplored dimension in the OOD literature.

2. **Clean experimental design that directly probes extrapolation.** Training models on clean + mild shift data (D₀∪D₁) and evaluating across a range of stronger shifts (D₂–D₁₀) is a well-motivated protocol that mirrors realistic deployment scenarios where strong shifts are rare. The pool of 20+ DG algorithms × multiple initializations provides a thorough search over models.

3. **Non-obvious divergent patterns across shift types.** Section 4.3's finding that training on strong shifts helps for noise (NoisyMNIST) but harms for rotation (RotatedMNIST) and has mixed effects for LowLightCIFAR10 is a nuanced and non-trivial result. It concretely demonstrates that the relationship between training-severity and test-severity is task-dependent — a valuable caution for practitioners.

4. **GradCAM visualization linking mechanistic explanation to observed brittleness.** The comparison of ERM (local features) vs. CAD (global structures) on NoisyMNIST (Figure 4 in paper) provides interpretable evidence for *why* certain models collapse at specific shift degrees, going beyond pure accuracy reporting.

## Weaknesses

### Fatal
None.

### Major

1. **Pre-trained model experiments are limited to linear probing, which weakens the general claim about CLIP sensitivity.** Section 5 adapts CLIP and ImageNet-pretrained models solely via linear probing. The paper's abstract states that "large-scale pre-trained models, such as CLIP, are sensitive to even minute distribution shifts of novel downstream tasks" without qualifying the adaptation method. Since the paper's own (commented-out) preliminary results indicate that fine-tuning significantly improves robustness on NoisyMNIST, the observed brittleness may be partly an artifact of linear probing rather than a property of the representations themselves. The core Section 4 claims about brittleness do not depend on this — but the CLIP-specific narrative (abstract, Section 5.2, conclusion) overstates what the evidence supports. The authors should either add fine-tuning experiments or explicitly re-scope the CLIP claims to "when adapted via linear probing."

2. **No limitations or caveats section.** The paper draws broad recommendations ("one should be more cautious when drawing conclusions from evaluations under a limited range of degrees") but never discusses the synthetic nature of the shifts tested, the limited number of tasks, or the linear-probing-only limitation for pretrained models. A limitations paragraph is essential for a paper making normative recommendations.

### Minor

1. **Experiments use only synthetic shifts, limiting generality of broad conclusions.** The paper tests Gaussian noise, rotation, brightness+shot noise, and resolution reduction — all synthetic. The paper's title ("Robustness May be More Brittle than We Think") and conclusion imply a general phenomenon, but whether the observed brittleness patterns hold for natural distribution shifts (e.g., domain shifts in medical imaging, spurious correlations in the wild, natural adversarial examples) remains untested. This is not a fatal flaw — the paper is a valid proof-of-concept — but the generality of the conclusions is narrower than suggested.

2. **CLIP experiments on MNIST suffer from an extreme domain gap.** CLIP is pre-trained on natural images; evaluating it on grayscale digits with Gaussian noise introduces a double mismatch (domain + corruption). The observed brittleness may partly reflect this mismatch rather than a general property of pre-trained representations. The NoisyImageNet15 experiments partially address this concern but are still synthetic. A clear acknowledgment of this confound would strengthen the paper.

3. **"Further adapting to the shift improves robustness" rests on limited evidence.** The claim at line 306 that "further adapting the pre-trained models to downstream distribution shifts can sometimes significantly improve their robustness" is supported by one comparison (IN₀ vs. IN₁ on NoisyMNIST). The word "sometimes" appropriately hedges, but the evidence is thin.

### Trivial

1. **Architecture details for the 4-layer CNN are missing** (number of filters, kernel sizes, stride, pooling). The paper reports only "roughly 0.37M parameters." While not critical for the paper's message, this hinders exact reproducibility.

2. **No discussion of how ordinal degrees map to real-world severity.** The paper uses integers to represent shift degrees (e.g., D₀–D₁₀) and reports the mapping (e.g., noise std linearly spaced 0–0.8) but does not discuss how practitioners could calibrate such degrees for real-world tasks. This limits the paper's actionable guidance.

## Nice-to-Haves

- **Mechanistic analysis of why different shift types yield different patterns.** Section 4.3 reports the contrasting behavior between noise (training on strong shifts helps) and rotation (training on strong shifts harms) but offers no deeper explanation beyond a single GradCAM example. A systematic analysis (e.g., by perturbing spatial frequencies or measuring feature invariance) would turn an observation into an insight.
- **Evaluation on a realistic multi-degree benchmark** (e.g., varying degrees of spurious correlation in Waterbirds, or natural severity levels from ImageNet-C broken out by individual severity level) would substantially strengthen claims about generality.
- **Testing whether training on multiple degrees simultaneously reduces brittleness** would be a natural extension directly aligned with the paper's message.

## Removed Points

- *Criticism that Figure 1's idealized scenario "never tests" the exact pattern shown* — The paper demonstrates ranking reversals (Table 1), which is exactly the concern illustrated by the schematic. The figure is an abstract motivation, not a testable prediction.
- *Criticism that the paper doesn't quantify how ordinals map to actual severity* — The paper provides the mapping explicitly (e.g., noise std linearly spaced 0–0.8, rotation 0–80 degrees). The ordinal convention is a design choice, not an omission.
- *Criticism about selecting top-5 models from a pool trained on D₀∪D₁ not being "fully justified"* — This is the deliberate experimental design: training on clean+mild data and testing extrapolation is the paper's central probe. The methodology is sound and clearly motivated.
- *Several formatting/style nitpicks and missing appendix claims* — These are parser artifacts or out of scope for evaluation.
- *"CLIP results may be an artifact of domain mismatch" was flagged as a major omission* — The paper explicitly acknowledges this hypothesis (line 295: "Gaussian noise is very rare in the training data of CLIP") and partially addresses it via NoisyImageNet15 experiments. Retained as Minor weakness #2 with softened language.
- *Strength Finder claimed strengths that are generic or conflict with verified weaknesses* — Some strengths were oversold and have been removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add fine-tuning experiments (or at minimum linear-probing + fine-tuning comparison on one dataset) for the pre-trained model section, and re-scope the abstract/conclusion claims to match what is tested.
2. Add a limitations paragraph explicitly discussing: (a) all shifts tested are synthetic, (b) pre-trained models are evaluated via linear probing only, (c) the small number of tasks, and (d) the ordinal degree convention.
3. Strengthen the "further adaptation improves robustness" claim by either providing evidence across more shift types or removing the general statement.
4. Include architecture details for the 4-layer CNN (filter sizes, kernel sizes, stride, pooling).

## Score and Decision

**Calibration Anchors (all from the human-review corpus):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KbetDM33YG.md` | 8.00 | **(Higher)** A well-executed GNN evaluation paper with a novel problem, thorough experiments across real-world shifts, and clear methodology. This paper is similarly novel in problem formulation but has narrower empirical scope (synthetic shifts only). |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ljwoQ3cvQh.md` | 7.00 | **(Higher)** Broad empirical study (8 datasets, multiple architectures) with theoretical grounding. This paper has a more novel question but less comprehensive evaluation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/w0jk3L3IjV.md` | 5.67 | **(Comparable)** Both identify an underexplored problem in OOD and run clean experiments. This paper has a more novel problem framing but less methodological contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oKglS1cFdb.md` | 5.67 | **(Comparable)** Both are empirical OOD papers with clear experiments but limited scope. This paper's question (shift degree) is more novel. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/qDFpNXnuYK.md` | 5.00 | **(Comparable)** Empirical OOD study with some overclaiming and limited baselines. This paper is similarly empirically grounded, slightly cleaner in execution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8efAVon0eD.md` | 3.75 | **(Lower)** Methodological concerns and limited experiments. This paper's experiments are cleaner and its claims better supported. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KK29oh8jZs.md` | 3.00 | **(Lower)** Simple synthetic datasets without clear need; this paper has a more important research question and better-designed experiments. |

The paper makes a real contribution by identifying an underexplored dimension in OOD evaluation and providing clean empirical demonstrations. Its main limitations are (1) reliance on synthetic shifts, (2) incomplete support for the CLIP-related claims due to linear-probing-only evaluation, and (3) the absence of a limitations discussion. These are addressable weaknesses, not fatal flaws. Relative to the calibration anchors, the paper sits around the upper end of the mid-range — comparable to ~5.5–6.0 papers but held back by overreach in the CLIP narrative.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>