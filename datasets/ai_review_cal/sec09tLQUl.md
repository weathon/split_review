- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper studies the connection between memorization and poor minority-group generalization in spurious-correlation settings. The authors use a neuron-level memorization detection method (from Maini et al., 2023) to show that minority-group examples require fewer neurons to flip their predictions, and that dropping those neurons improves worst-group accuracy. They then propose FairDropout, an example-tied dropout technique: a fixed subset of neurons are designated as "memorizing" and each training example is assigned a random subset of these; at inference the memorizing neurons are dropped. The method is evaluated on vision (CelebA, Waterbirds, MetaShift), language (MultiNLI), and medical (MIMIC-CXR) benchmarks without using group annotations.

## Strengths

1. **Novel empirical analysis linking minority-group overfitting to neuron-level memorization.** Figures 2 and 3 provide direct evidence, under the methodology of Maini et al. (2023), that (a) minority-group examples require far fewer neurons to flip their prediction than majority-group examples, and (b) dropping these neurons improves test worst-group accuracy in ~75% of cases. This is a concrete, novel diagnostic contribution to the spurious-correlation literature regardless of the downstream method.

2. **Scales example-tied dropout to large architectures and realistic spurious-correlation benchmarks.** The paper extends a technique previously demonstrated on ResNet-9 / MNIST / CIFAR-10 (for label noise) to ResNet-50 and BERT, with a practical placement strategy (after residual blocks for ResNet-50; via a new linear layer before the classifier for BERT). This scaling is non-trivial and validated on datasets spanning vision, language, and medical imaging.

3. **Achieves competitive worst-group accuracy without group annotations on several benchmarks.** On MultiNLI (70.3±2.4) and MIMIC-CXR (70.6±0.6), FairDropout achieves the best results among all group-annotation-free baselines reported in Table 1. On CelebA and MetaShift, it is competitive with methods like Resample and ReWeightCRT despite using only standard cross-entropy loss.

4. **Method is simple and composable.** FairDropout adds no learnable parameters and uses standard cross-entropy loss, making it a light-weight module that the paper explicitly notes can be combined with existing imbalanced-learning or classifier-retraining methods for further gains.

## Weaknesses

### Fatal

None.

### Major

1. **Method-mechanism disconnect between the motivating analysis and the algorithm.** The analysis in Section 3.2 identifies *which specific neurons are causally important* for each minority-group example (via sequential neuron removal). The natural algorithmic consequence would be to identify and suppress precisely those neurons. Instead, FairDropout randomly pre-allocates a set of "memorizing" neurons per sample with no feedback loop that encourages the model to concentrate memorization into those specific neurons. The paper acknowledges this in Section 5 as an untested assumption ("we hypothesize that generalizing neurons are less likely to memorize examples since memorization is more easily achieved in the memorizing neurons"). However, this means the method does not implement what the motivation promises: there is no evidence that the randomly allocated neurons actually become specialized for their assigned examples, nor that the mechanism works via the claimed memorization-redirection path. The method could work for entirely different reasons (e.g., aggressive feature suppression at test time), which the paper does not investigate.

2. **Missing critical baseline: standard (input-independent) dropout at an equivalent rate.** FairDropout drops all \((1-p_\text{gen})H\) memorizing neurons at inference. With \(p_\text{gen}=0.2\) (used in the CelebA warm-up), 80% of neurons in the affected layer are dropped. The paper does not compare against standard (Srivastava et al.) dropout applied to the same layer at the same rate, either during training, at test time, or both. Without this baseline, the claimed benefit of *example-tied* allocation over simple regularization is unsubstantiated. The improvements on MultiNLI and MIMIC-CXR could stem entirely from aggressive feature suppression, not from the example-specific assignment. This is the single most important evidential gap for the paper's central contribution.

### Minor

1. **Allocation mechanism is underspecified and internally contradictory.** Section 3.3 states that "each sample is allocated a memorizing neuron uniformly with probability \(p_\text{mem}\)" but also that "every example allocates the same fixed number of memorizing neurons" and "in this case, each image allocates only one memorizing neuron." If allocation is probabilistic with parameter \(p_\text{mem}<1\), some examples receive zero memorizing neurons — contradicting the "fair" claim and the "one per image" statement. If every example gets exactly one, then \(p_\text{mem}\) is not used as described. The relationship between \(p_\text{gen}\) and the effective number of memorizing neurons per sample is also unclear. This makes the method irreproducible from the text as written.

2. **Figure 3 methodology does not match what FairDropout does at test time.** The experiment in Figure 3 drops neurons *per-example* — a custom subset of neurons is removed for each individual example to flip its prediction. FairDropout, by contrast, drops *all* memorizing neurons globally at test time for every example (i.e., the same fixed set of \((1-p_\text{gen})H\) neurons are removed for all inputs). The direct causal link between the Figure 3 result (per-example dropping helps) and the FairDropout algorithm (global dropping of a pre-allocated set) is therefore tenuous.

3. **Converted baselines lack explicit validation caveat.** The paper compares against group-dependent methods (GroupDRO, CVaRDRO, DFR) converted to class-based variants via Yang et al. (2023). The paper states this clearly, but the gap between the original group-annotated performance and the converted version can be large — e.g., original GroupDRO achieves ~90% worst-group accuracy on CelebA while the class-converted version scores 68.5%. The current presentation claims FairDropout "outperforms" these methods without noting that the comparison is against weakened variants of the original algorithms. This does not invalidate the results (since the setting is genuinely no-group-info), but the framing would benefit from explicit acknowledgment.

4. **Per-dataset hyperparameters are not fully reported.** Only the CelebA warm-up configuration (\(p_\text{mem}=p_\text{gen}=0.2\), after the 3rd residual block) is disclosed. The tuned hyperparameters for each dataset (the chosen \(p_\text{gen}, p_\text{mem}\), and layer position) are not reported, which hinders reproducibility and makes it difficult to assess how sensitive results are to these choices.

### Trivial

None.

## Nice-to-Haves

- Add a standard-dropout ablation at the equivalent rate to isolate the effect of example-tied allocation.
- Demonstrate that allocated memorizing neurons actually specialize — e.g., show per-neuron activation differences or ablation analyses comparing allocated neurons against random neurons.
- Report per-dataset chosen hyperparameters.
- Add a brief analysis of training dynamics (do the same neurons consistently absorb memorization for the same examples across epochs?).

## Removed Points

These points were considered and removed:
- **"Alternative explanations for memorization analysis not ruled out"** (Harsh Critic point 3): The paper follows the established methodology of Maini et al. (2023) and, crucially, provides causal evidence in Figure 3 (dropping the identified neurons improves accuracy). The alternative explanation (soft decision boundaries) is speculative and not better supported. This does not undermine the paper's analysis.
- **"Waterbirds underperformance weakens narrative"**: The paper acknowledges and attempts to explain this. A method not performing well on one dataset is a data point, not a weakness per se.
- **"Section 5 limitations reduce confidence"**: Acknowledging limitations is proper scholarship, not a weakness.
- **"No discussion of computational cost / training dynamics"**: These are non-standard expectations and are better placed as nice-to-haves.
- **"Missing related works"**: Cannot be verified without external sources.
- **Formatting, typographical, and presentation nitpicks**: Likely parser artifacts, not author errors.

## Novel Insights

The harsh reviewer independently notices that the paper's central gap is the lack of a feedback loop connecting the memorization-localization analysis to the FairDropout allocation mechanism — a structural observation that goes beyond the paper's own limitations section. The Strength Finder correctly identifies that the paper's strongest evidence is the combination of Figures 2 and 3 (the diagnostic analysis), which is actually separable from the FairDropout method itself. An interesting synthesis: the diagnostic contribution (identifying that minority-group failures are linked to a small set of localized neurons) may be more valuable and better-supported than the algorithmic contribution (FairDropout). If the method works but for reasons unrelated to its claimed mechanism (e.g., it simply acts as aggressive structured dropout), the paper's narrative would need substantial revision.

## Suggestions

1. **Add a standard dropout baseline.** Compare FairDropout against standard (per-example independent, no fixed per-example masks) dropout applied to the same layer at the same effective rate — both during training and at test time. If the gap is negligible, reframe the contribution.
2. **Verify the mechanism directly.** Show that allocated memorizing neurons are more important for their assigned examples than random unassigned neurons (via neuron ablation or activation analysis). Without this, the method's stated motivation is unvalidated.
3. **Clarify the allocation mechanism.** Resolve the contradiction between "with probability \(p_\text{mem}\)" and "same fixed number per example." State clearly: how many memorizing neurons does each example actually get?
4. **Report per-dataset hyperparameters** in a table, including the chosen \(p_\text{gen}\), \(p_\text{mem}\), and layer position for each dataset.
5. **Strengthen the baseline caveat.** Explicitly note that converted group-dependent baselines are weakened variants and state the original (group-annotated) performance for context, even though the paper's setting does not use group labels.
