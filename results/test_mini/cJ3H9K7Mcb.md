Now I have all the information needed to synthesize the review. Let me produce the final output.

## Summary

This paper studies how OOD generalization performance changes across different *degrees* of the same type of distribution shift (e.g., varying noise intensity, rotation angle, or resolution). Through extensive experiments on NoisyMNIST, RotatedMNIST, LowLightCIFAR10, NoisyImageNet15, and LR-ImageNet15, with CNNs, ResNets, EfficientNets, ViTs, and over 20 DG algorithms, the authors document three main findings: (1) models that perform best under a moderate shift degree can degrade sharply under a slightly higher degree; (2) training on strongly shifted data guarantees robustness to milder shifts for some tasks (Gaussian noise) but hurts for others (rotation); (3) CLIP models adapted via linear probing can be disproportionately brittle to downstream distribution shifts that are rare in the pretraining data.

## Strengths

- **Systematic documentation of a largely overlooked dimension.** The paper correctly identifies that most OOD benchmarks fix the degree of distribution shift, and it provides a thorough empirical mapping of how performance varies across degrees for multiple shift types, architectures, and algorithms. This breadth (5 datasets, 4+ architectures, 20+ DG algorithms) makes the findings unlikely to be artifacts of a single setup.

- **Non-trivial asymmetry between shift types (§4.3).** The finding that training on strong Gaussian noise *does* guarantee robustness to milder noise (NoisyMNIST), while training on strong rotations *harms* performance on mild rotations (RotatedMNIST), is the paper's most genuinely interesting result. This task-dependent asymmetry is not trivial and provides concrete evidence that conclusions about "robustness to degrees" cannot be drawn from a single shift type.

- **Quantification of abrupt performance cliffs.** Table 1 reports specific relative drops (e.g., VREx on CNN: 50.3% from D₄ to D₅, 73.1% from D₄ to D₆) that give concrete, actionable numbers to the claim that "slightly higher degrees can cause severe degradation." This is more informative than a qualitative statement.

- **GradCAM analysis (Fig. 4) provides mechanistic insight.** Showing that ERM relies on local features (easily corrupted by noise) while CAD relies on global structures gives a clear intuitive explanation for why different models behave differently across degrees. This connects the empirical patterns to a concrete learning phenomenon (spurious correlations breaking at different thresholds).

## Weaknesses

### Major

- **The "brittleness" claim is over-framed relative to the evidence.** The paper's central rhetorical framing — that robustness is "surprisingly brittle" across degrees — is weakened by the fact that many of the observed drops are actually expected given known properties of deep networks. The GradCAM analysis itself explains why: models rely on different features, and those features break at different noise thresholds. The paper acknowledges this (lines 215-218) but still frames it as a surprising brittleness finding. The key question — *how much of this is just feature-sensitivity rephrased?* — is not addressed. The paper would be stronger if it explicitly scoped its contribution as "quantifying the rate at which feature-based robustness breaks down" rather than claiming brittleness as a novel discovery.

- **The best-at-each-degree analysis (Fig. 2 left) is presented as evidence of a problem with individual models, but it primarily reflects model selection.** The paper selects the top-5 models at each test degree from a pool trained on D₀∪D₁ and shows the selected models perform poorly at other degrees. While this is not "trivially expected" (as the Harsh Critic claimed — see verification above), it is fundamentally an observation about *which models from a diverse pool get selected at each degree*, not about individual model behavior. The paper's stronger evidence — Table 1 and Fig. 2 (right) tracking individual algorithms — is presented alongside this analysis but not sufficiently separated from it. The paper should explicitly distinguish the model-selection finding from the individual-model brittleness finding.

- **The CLIP section (§5) is incomplete and over-interpreted.** The paper shows that CLIP + linear probing on clean data is brittle to Gaussian noise, which the paper itself hypothesizes is because "Gaussian noise is very rare in the training data of CLIP" (line 295). This is a known limitation of linear probing on OOD data, not a specific insight about CLIP. The paper mentions (in a comment block) that fine-tuning significantly outperforms, but these results are not presented. Without fine-tuning comparisons, the section only confirms that linear probing + pretraining distribution mismatch → poor OOD performance, which is well-documented (Kumar et al., 2022). The paper's claim that "pre-trained representations are sensitive to novel downstream distribution shifts" is too broad given CLIP does fine on rotation shifts (Fig. 5, second panel) and ImageNet-pretrained models outperform CLIP on both NoisyImageNet15 and LR-ImageNet15.

### Minor

- **No quantitative summary of ranking changes across degrees.** The paper claims that "evaluations under limited degrees can lead to wrong conclusions" about algorithm rankings, but it never quantifies this. Computing rank correlations (e.g., Kendall's τ) between algorithm rankings at D₄ vs. D₅, D₄ vs. D₁₀, etc., would make this claim concrete and actionable. Visual inspection of curves in Fig. 2 (right) is insufficient.

- **The GradCAM analysis covers only two algorithms (ERM, CAD) on one dataset (NoisyMNIST).** This limits how general the mechanistic explanation is. The paper could strengthen this with a similar analysis on RotatedMNIST or LowLightCIFAR10.

- **The asymmetry finding (§4.3) is under-analyzed.** Why does training on strong noise transfer well to milder noise while training on strong rotation does not? The paper documents the phenomenon but offers no hypothesis beyond showing GradCAM on NoisyMNIST. A simple additional experiment — e.g., measuring feature overlap between models trained on different training sets — could provide valuable insight.

### Trivial

- None of substance that survived filtering.

## Nice-to-Haves

- Including Kendall rank correlation or similar quantitative stability metric for algorithm rankings across degrees would make the ranking-instability claim concrete rather than visual.
- Full fine-tuning results for CLIP models would complete §5 and allow a proper comparison to the linear probing results.
- A simple experiment measuring representation similarity (e.g., CKA) between models trained on different training sets for noise vs. rotation could help explain why the asymmetry in §4.3 occurs.

## Removed Points

- **"Selection-bias flaw invalidates the central analysis" (Harsh Critic #1):** This criticism claimed the analysis is trivially expected. However, the models were all trained on the *same* data (D₀∪D₁), so the finding that different models from a fixed pool are best at different degrees is not trivially expected. It reveals genuine heterogeneity in how models trained on identical data generalize across degrees. The criticism is factually inaccurate about the setup. (The point about framing being over-claimed is retained in the Major weaknesses above, but the "invalid" label is removed.)

- **"§4.3 conflates distribution shift during training with evaluation brittleness" (Harsh Critic #2):** This reframes the paper's empirical observation as a known phenomenon without identifying a specific error in the paper's claims. The paper is transparent about what it does (train on different domain sets, measure performance curves) and the finding (task-dependent asymmetry) is valid regardless of how one labels it. The paper does not claim this is a "failure of generalization from high to low" in a fundamental theoretical sense — it simply documents the empirical pattern. Removed as a strawman.

- **"CLIP findings are already known" (Harsh Critic #3):** The paper quantifies a specific comparison (rate of degradation of linear-probed CLIP vs. randomly initialized models across degrees) that goes beyond the generic claim that "CLIP fails on noise." The paper also acknowledges the likely explanation (Gaussian noise rarity). The specific measurement is a contribution even if the high-level intuition is familiar. Demoted from fatal to minor/incomplete.

- **Several of the Strength Finder's generic strengths:** "Clear framing of the problem" and "Systematic collection of experiments" are retained but reframed. Generic praise removed.

## Novel Insights

The most interesting cross-cutting observation is the task-dependent asymmetry: training on strong Gaussian noise reliably improves robustness to all milder noise levels, but training on strong rotations actively *harms* performance on mild rotations compared to training on clean data alone. This reveals that "degree robustness" is not a single-axis property — it depends on whether the shift preserves or destroys hierarchical feature structure. Noise randomly corrupts pixels and is additive in feature space, so exposure to strong noise teaches robustness at all levels. Rotation, by contrast, preserves pixel-level structure but changes spatial relationships — training on extreme rotations may reallocate representational capacity to rotation-invariant features at the expense of features useful for mild rotations. This insight, while not fully developed in the paper, suggests that the field needs a taxonomy of shift types based not on their source (noise vs. rotation) but on whether increasing degree introduces new features or destroys existing ones.

## Suggestions

1. Remove or substantially reframe the best-at-each-degree analysis (Fig. 2 left), clarifying that it shows *model selection across degrees from a fixed pool* rather than individual-model brittleness. The individual-model evidence (Table 1, Fig. 2 right) is cleaner.

2. Add a quantitative ranking-stability metric (Kendall's τ or rank overlap) across degree pairs to make the "evaluation bias" claim precise.

3. Either present the CLIP fine-tuning results or reframe §5 as "a cautionary case study on linear probing when the pretraining data does not cover the downstream shift" rather than as evidence of brittleness in pre-trained representations.

4. Add a brief analysis of why noise vs. rotation behave differently in §4.3 — even a simple representational similarity (CKA) measurement would substantially strengthen the paper's most interesting finding.

5. Clarify in the abstract and conclusion that the contribution is primarily empirical and cautionary ("evaluate over multiple degrees"), not a claim of surprising brittleness as a new phenomenon.

## Score and Decision

**Calibration anchors:**

| Anchor | Avg Score | Comparison to current paper |
|--------|-----------|----------------------------|
| OOD-Chameleon (3.75, Reject) | 3.75 | Weaker contribution — method is poorly motivated and experiments are thin. Current paper is more solid empirically. |
| Expecting The Unexpected / BROAD (4.25, Reject) | 4.25 | Similar type of contribution (empirical benchmark/evaluation study). BROAD has a new dataset; current paper has more nuanced findings across degrees. Comparable quality. |
| Early Period of Training (5.00, Reject) | 5.00 | Both empirical studies, comparable in scope. Early Period paper has a proposed method (gradual unfreezing) while current paper is purely descriptive. Current paper has broader experimental coverage. |
| Feature Accompaniment (5.67, Reject) | 5.67 | Has both theory and experiments, but the theory-experiment gap is a weakness. Current paper lacks theory but has cleaner empirical narrative. |
| Deep NNs Extrapolate Predictably (7.00, Accept) | 7.00 | Much stronger — novel finding with theory + extensive experiments. Current paper is less novel and lacks theoretical grounding. |
| ImageNet-OOD (6.50, Accept) | 6.50 | Clear tangible contribution (dataset) with extensive analysis. Current paper lacks a comparable concrete deliverable. |

The paper is a solid empirical study documenting an underexplored dimension of OOD evaluation. Its findings are useful but largely confirmatory of what one would expect given known properties of deep networks (feature fragility, pretraining coverage). The asymmetry finding (noise vs. rotation) is genuinely interesting but under-analyzed. The paper would benefit from sharper framing and a quantitative summary of ranking changes. Relative to the calibration anchors, it sits between the 4-5 range — better executed than OOD-Chameleon but less novel than Feature Accompaniment or Deep NNs Extrapolate Predictably.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>