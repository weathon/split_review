Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces BAdd, a bias mitigation method that adds bias-capturing feature vectors (from a separately trained model) to the penultimate layer's representation during training, then fine-tunes the classification head without those features at inference time. The core insight is that injecting protected-attribute information into the model's features prevents the "loss spike" cycle that traps vanilla models, allowing the backbone to learn target-relevant representations. The method is evaluated across seven benchmarks (four single-attribute, three multi-attribute) with strong results, especially on multi-attribute scenarios where it achieves +27.5% on FB-Biased-MNIST and +5.5% on CelebA over prior state-of-the-art.

## Strengths

1. **Simple, well-motivated idea with strong results on multi-attribute benchmarks.** The core mechanism — adding bias features to the penultimate layer — is conceptually clean and easy to implement. The empirical results on FB-Biased-MNIST (95.6% vs. next-best 87.6% at q=0.9) and CelebA (92.7% vs. 87.2% on HeavyMakeup bias-conflicting) are striking and clearly demonstrate that existing methods struggle with multiple intersecting biases while BAdd handles them effectively (Tables 5, 9 in the paper's numbering; Tables 8, 12 in the actual text).

2. **Theoretical grounding through loss spike analysis.** The paper identifies a concrete failure mode of vanilla training — the oscillating loss on bias-aligned samples — and derives gradient dynamics (Eq. 4) showing how bias-aligned and bias-conflicting samples pull the model in opposing directions. This provides a principled explanation for why the method works: adding $\mathbf{b}$ keeps $\mathcal{L}_\mathcal{A}$ consistently low, breaking the cycle. This analysis is a genuine contribution beyond the algorithmic recipe.

3. **Ablations validate key design choices.** The comparison of addition vs. concatenation (Table 7/10: 98.1% vs. 91.5% at q=0.99) and the layer insertion study (Table 8/11: penultimate layer best) give empirical confidence that the specific design choices matter, not just the general idea of incorporating bias information.

4. **Thorough evaluation scope.** Testing across seven benchmarks spanning simple injected biases (Biased-MNIST), texture biases (Corrupted-CIFAR10), naturalistic spurious correlations (Waterbirds), and real-world multi-attribute biases (CelebA) provides a comprehensive picture of where the method does and does not excel.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **UrbanCars evaluation is confounded by different I.D. Acc values.** BAdd's gap metrics (BG+CoObj Gap: -3.9, CoObj Gap: -1.6) look competitive with LLE (-5.9 and -2.7), but BAdd's I.D. Acc is significantly lower (91.0% vs. 96.7%). Since "Gap" = I.D. Acc − subgroup accuracy, a lower I.D. Acc mechanically reduces the gap even if subgroup accuracy is unchanged or worse. Without raw subgroup accuracies for the four groups (urban/car × background/object combinations), the apparent improvement on CoObj and BG+CoObj gaps could be an artifact of lower overall accuracy rather than genuinely better worst-group performance. The paper should report subgroup accuracies directly so readers can interpret the gaps without this confound.

2. **Fine-tuning step is asserted but not validated.** The paper states that "fine-tuning the classification layer with only the $\mathbf{h}$ features is required" (line 130) and applies it to all models, but provides no ablation comparing performance with and without this step. If the backbone has truly learned target-relevant features (as the method's logic claims), the method should work without fine-tuning the classifier after removing $\mathbf{b}$. A simple ablation — final accuracy with vs. without the 20-epoch fine-tuning — would confirm whether the backbone features are indeed self-sufficient or whether the fine-tuning is doing the actual debiasing work.

3. **Multi-attribute handling is underspecified in implementation detail.** The paper defines a single bias-capturing model $b(\cdot)$ that predicts a tuple of protected attributes $t \in \mathcal{T}$ and produces a single representation $\mathbf{b}$ (line 61). This is conceptually clear, but the paper does not specify how $b(\cdot)$ is trained for multi-attribute cases in practice: is it a multi-label classifier? Two separate classifiers whose outputs are combined? Does the dimensionality of $\mathbf{b}$ change when more attributes are added? The footnote (line 121) describes two options (classifier vs. regressor) for obtaining $\mathbf{b}$, but does not say which is used for each multi-attribute experiment. This information is needed for reproducibility.

4. **Waterbirds claim is slightly overbroad.** The abstract and introduction state that BAdd "surpasses state-of-the-art methods on both single- and multi-attribute benchmarks," but on Waterbirds (single-attribute), BAdd ties DFR on WG accuracy (92.9%) and is behind on average accuracy (93.6% vs. 94.2%). The paper's own text accurately says "reaches the state-of-the-art WG accuracy" (line 284), which is the more precise claim — but the higher-level framing could leave readers with an inflated impression.

### Trivial

- The loss spike analysis (Fig. 1/2) is qualitative only; a quantitative measure (e.g., variance of loss on bias-aligned samples) would strengthen the theoretical argument.
- The CelebA bias-conflicting and unbiased test splits are defined by reference to prior work (\cite{sarridis2023flac,hong2021bb}) but could benefit from explicit clarification, especially for the multi-attribute case where "bias-conflicting" could mean conflicting on one attribute, both, or at least one.

## Nice-to-Haves

- Report raw subgroup accuracies for UrbanCars (four groups) alongside gap metrics.
- Add an ablation comparing final performance with and without the fine-tuning step.
- Quantitative characterization of the loss spike phenomenon (e.g., loss variance over time for bias-aligned samples).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not specify how multiple protected attributes are handled in the method" (framed as structural omission).** The paper actually does specify this — $\mathcal{T}$ is defined as a domain of tuples, and $b(\cdot)$ predicts the tuple, producing a single $\mathbf{b}$ (line 61). The method is the same for single and multiple attributes; the change is in what $b(\cdot)$ predicts. The reviewer's framing of this as a "structural omission" overstates the gap. The point is downgraded to Minor (see above) because additional implementation detail would still help reproducibility.

- **"The claim of outperforming state-of-the-art is overstated... on Waterbirds."** The paper text says "reaches the state-of-the-art WG accuracy" (line 284), which is accurate for a tie. The abstract's "surpassing" is slightly broad but the paper's detailed claim is honest. Kept as a Minor weakness (point 4 above) but not the severe issue the reviewer asserted.

- **"CelebA evaluation uses the unmodified dataset without specifying how bias-conflicting and unbiased test sets are constructed."** The paper says "as in \cite{sarridis2023flac,hong2021bb}" (line 186). This follows standard protocol from prior work. The concern is technically addressed, though marginal clarity improvement would help.

- **"Statistical comparison with baselines: standard deviations of baselines are missing."** This is a generic reproducibility nitpick common in the field; many baselines are cited from original papers that may not report std. Not a weakness specific to this paper.

- **Loss spike quantification** demand moved to Nice-to-Haves.

- **"Specification of bias-capturing network" / "architecture of the bias encoder is unstated"** — the paper provides two concrete options (classifier vs. regressor, footnote line 121). The missing detail is which option is used per experiment, which is a minor clarity issue, not a structural gap.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective that the paper itself does not articulate.

## Suggestions

1. **On UrbanCars**: Report the raw subgroup accuracies (accuracy on each of the four groups defined by background and co-occurring objects). This would allow readers to interpret the gap metrics without the confound of different I.D. Acc values, and would strengthen the paper's strongest-claim benchmark.

2. **Add the fine-tuning ablation**: Compare: (a) training with $\mathbf{b}$, then evaluating with $\mathbf{h}$ only (no fine-tuning), (b) training with $\mathbf{b}$, then fine-tuning classifier with $\mathbf{h}$ only, and (c) training with $\mathbf{b}$, then fine-tuning both backbone and classifier with $\mathbf{h}$ only. This would validate the claim that the backbone has learned target-relevant features.

3. **Specify the bias-capturing model per dataset**: Add a table or column in the experimental setup specifying for each dataset whether $\mathbf{b}$ comes from a classifier or regressor, and for multi-attribute cases, whether a single multi-label or multiple separate models are used.

4. **Quantify the loss spike phenomenon**: Report the mean/variance of loss on bias-aligned samples over training steps for vanilla vs. BAdd, rather than a qualitative figure alone.

## Score and Decision

The paper presents a clean, well-motivated method with genuine contributions: a novel mechanism for bias mitigation, theoretical analysis of why it works, and strong empirical results on multi-attribute benchmarks where prior methods struggle. The weaknesses are real but addressable — they concern interpretation on one benchmark (UrbanCaps), a missing ablation, and clarity of implementation details — none of which invalidate the core contribution or the headline results on FB-Biased-MNIST and CelebA. The paper is a solid contribution to the fairness-aware vision literature.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>