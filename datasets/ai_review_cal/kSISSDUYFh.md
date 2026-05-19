- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 5, 8
Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper evaluates whether state-of-the-art digital twin models of mouse visual cortex — trained to predict single-neuron firing rates — can reproduce key population-level response properties: the differentiability of V1 representations (Stringer et al., 2019) and the hierarchical discriminability of objects across visual areas (Froudarakis et al., 2020). It finds that standard models fail on both fronts, then shows that regularization techniques (dropout, data augmentation) can push models toward differentiable representations, which partially improves the hierarchy of discriminability. The paper is a well-structured empirical study with systematic ablation, clear negative results, and an honest discussion of limitations.

## Strengths

- **Quantitative demonstration that digital twins fail to replicate V1 population differentiability**: The paper shows that the benchmark model's eigenspectrum for natural images has a power-law exponent α = 0.82, well below the theoretical differentiability threshold (Fig. 2A,B). This is a direct, quantitative comparison to the experimental data from Stringer et al., which reported α ≈ 1.05.

- **Identification of dropout as a mechanism to recover differentiable representations**: The paper systematically varies dropout rate and shows that rates ≥0.4 yield α = 1.06 for natural images, closely matching the experimental value of α = 1.05 (Fig. 4B,C). This provides a specific, reproducible intervention that fixes the core failure.

- **Connection between representation geometry and hierarchy of object discriminability**: Models with differentiable representations (dropout ≥0.4) qualitatively recover the experimental hierarchy LM > V1 > RL, whereas non-differentiable models reverse it (Fig. 5A,B). This links a population-level geometric property to a functional computation across visual areas.

- **Systematic ablation of alternative causes**: The paper tests training on reliable neurons, the SENSORIUM dataset, a transformer architecture (ViV1T), and a correlation-based loss, and shows that none improve differentiability (Fig. 3). This thorough negative evidence strengthens the claim that the failure is robust across standard modeling choices.

- **Quantification of a trade-off between single-neuron and population-level performance**: The paper reports that regularization improves population geometry but reduces single-neuron correlation (Supp. Fig. 9), and discusses this trade-off explicitly (Section 7). This is a concrete, measurable tension that future work must address.

## Weaknesses

### Fatal
None.

### Major

1. **Missing baseline: population geometry of the training data.** The paper compares model-predicted responses (trained on MICrONS) to experimental results from Stringer et al. (2019), which used different mice and different stimuli. The paper never checks whether the actual neural responses in the MICrONS training data themselves exhibit differentiable geometry under the training stimuli (or under comparable conditions). If the MICrONS data are non-differentiable, the model is faithfully reproducing its training distribution, and the "failure" is substantially about cross-dataset/cross-stimulus generalization rather than a fundamental limitation of the model class. The paper provides some evidence against this interpretation by showing the failure holds for models trained on SENSORIUM (an independently collected dataset) and across multiple architectures (Section 5.1), which mitigates but does not eliminate the concern. This analysis should be performed on the MICrONS training data to the extent the stimulus structure allows. Without it, the central claim is incompletely supported.

2. **The link between differentiability and hierarchy improvement is correlational, not causal.** Section 6 shows that models with differentiable representations (dropout ≥ 0.4) produce a hierarchy that more closely matches the experimental ordering than non-differentiable models do. However, dropout simultaneously changes many aspects of the model: overall discriminability drops, single-neuron accuracy declines, and the model's effective capacity decreases. The paper does not demonstrate that differentiability *per se* drives the hierarchy change. A stronger test would compare models that achieve differentiability through different mechanisms (augmentation vs. dropout vs. correlation-based loss with α near 1) and check whether they all produce the same hierarchy pattern. The paper's claim that "improving model alignment with experiments requires training strategies that enhance robustness" is plausible but the causal mechanism is not isolated.

### Minor

1. **Shared core architecture limits hierarchy reproduction, and this is underexplored as a core finding.** The model uses a single core shared across all visual areas, which cannot learn area-specific transformations (e.g., increasing receptive field sizes along the hierarchy). The paper acknowledges this limitation in Section 7 and explores alternatives (task-driven models, area-specific models) in the supplement, finding they also fail. However, this architectural constraint is noted as a secondary point rather than a primary finding. Given that it directly explains why hierarchy results are weak, it deserves more prominence. (This is essentially the paper's own expressed limitation, but it could be elevated.)

2. **No statistical test for hierarchy ordering.** The paper shows mean discriminability changes and relative discriminability (Fig. 5) but does not quantify whether the model's hierarchy (LM > V1 > RL > AL) is statistically distinguishable from the experimental hierarchy (AL > LM > V1 > RL). A permutation test or rank correlation would strengthen the comparison.

3. **Limited analysis of why AL is incorrectly placed.** AL is recorded with fewer neurons (4,734 vs. 83,222 in V1) and has lower reliability (5.03% vs. 6.77% explainable variance). The paper notes these differences could affect the loss function but does not test whether the model's misordering of AL is due to data quantity or quality. A control experiment (e.g., downsampling V1 neurons to match AL count) would clarify.

4. **No evaluation on training stimuli geometry.** The paper evaluates population geometry only on out-of-distribution stimuli from Stringer et al. Showing that the model captures population geometry for in-distribution stimuli would strengthen the claim that the failure is specific to generalization, not to the model's inability to learn any population structure.

### Trivial

None.

## Nice-to-Haves

- **Interpretation of why the correlation-loss model falls short of differentiability**: The correlation-based model achieves α = 0.93 for natural images, still below the threshold. A brief mechanistic interpretation would help.
- **Deeper mechanistic explanation of why regularization promotes differentiability**: The paper speculates about biological noise and reduced overfitting but does not test between these alternatives.

## Removed Points

**These points were identified by reviewers but are excluded from the main evaluation:**

- **"The paper has a critical structural flaw that undermines its central claim" / "fatal" characterization of the missing training-data baseline.** This criticism is downgraded to Major (not Fatal) because: (a) the paper tests multiple datasets (SENSORIUM) and architectures, showing the failure is robust and not dataset-specific; (b) evaluating on out-of-distribution stimuli from different experiments is a valid generalization test, not a logical error; (c) the critic's framing assumes that if MICrONS data were non-differentiable the entire "failure" claim collapses, but the models' inability to reproduce known experimental results with different stimuli is still a meaningful limitation of digital twins. The concern is real and important, but does not invalidate the paper's core claims.

- **Criticism about AL data quantity/quality not being tested** (kept as Minor 3 above with proper framing).

- **Strength Finder strengths that are generic or conflict with verified weaknesses** were reviewed and most are concrete and specific enough to retain. No strengths were dropped.

## Novel Insights

The harsh critic correctly identifies that the paper's main claim about digital twins "failing" is partially ambiguous because the training data itself is never characterized for its population geometry. This is a valid and important point: the paper frames its evaluation as testing whether digital twins capture population response properties, but the benchmark comparisons are to *different experimental datasets* with different stimuli, not to the training data. The critic's reframing — that this is fundamentally a study of cross-dataset generalization of population geometry — is a useful lens that the paper's own framing partially obscures. A second novel observation is that the paper's central positive result (dropout fixes differentiability and improves hierarchy) is at best correlational, since dropout changes many aspects of the model simultaneously, and the paper does not isolate differentiability as the causal mechanism.

## Suggestions

1. **Compute the eigenspectrum of the actual neural responses in the MICrONS training dataset** under the same analysis pipeline, to the extent the training stimuli allow. This would resolve the central ambiguity: if the data are differentiable and the model fails, the paper's claims are validated; if not, the paper should be reframed around cross-dataset generalization.

2. **Compare multiple regularization methods that achieve differentiability** (dropout, augmentation, correlation-loss) and check whether they all produce the same hierarchy pattern. This would address the causal interpretation gap.

3. **Add a statistical test for hierarchy ordering** (e.g., rank correlation or permutation test comparing the model's area ordering to the experimental ordering).

4. **Perform a control experiment** downsampling V1 neurons to match AL neuron count to test whether data quantity explains AL's misplacement.
