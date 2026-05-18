Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper investigates the relationship between neuronal polysemanticity (entanglement) and weight sparsity in large language models. It proposes using the Wasserstein distance of a neuron's output distribution to a Gaussian as a metric for entanglement, identifies "Wasserstein neurons" with highly non-Gaussian output distributions, and shows these neurons are disproportionately important under sparsification. It introduces Sparse Expansion, an experimental framework that clusters inputs and applies SparseGPT per cluster, to study how disentanglement can recover performance under sparsity.

## Strengths

1. **Novel quantitative lens on entanglement.** The paper connects superposition theory to practical model compression by proposing Wasserstein distance to a Gaussian as a tractable measure of neuronal entanglement. The correlation with the proposed mapping difficulty (MD) metric (Figure 2e) gives convergent evidence that non-Gaussian output distributions are associated with neurons that must differentiate similar inputs into different outputs — a clean operationalization of the polysemanticity intuition.

2. **Demonstration that Wasserstein neurons are disproportionately critical under sparsity.** The paper shows across Llama 3 8B that sparsifying the top 3% of neurons by Wasserstein distance degrades perplexity and task performance far more than sparsifying neurons selected by mean output, variance, weight magnitude, or at random (Figure 3). The capability breakdowns (Figures 3b-d) showing collapse in reasoning tasks when Wasserstein neurons are ablated at high sparsity are compelling evidence that entanglement affects sparsity robustness.

3. **Sparse Expansion as an analytical tool reveals disentanglement effects.** The framework shows that when inputs are clustered and SparseGPT is applied per cluster, Wasserstein neurons improve substantially more than random neurons (Figure 5a), and their weighted Wasserstein distance decreases for 98% of such neurons with a median 42% reduction (Figure 5b). This provides a mechanistic link: separating inputs reduces the effective entanglement, which in turn improves sparse reconstruction.

4. **Empirical bounds on sparse computation under entanglement.** The paper provides real-model evidence connecting clustering-induced reduction in effective features (PCA components to 90% variance) to linear bounds on minimum error and maximum improvement (Figures 8b-c), grounding recent theoretical predictions (Hänni et al. 2024, Adler & Shavit 2024) in empirical data.

## Weaknesses

### Fatal
None.

### Major

1. **The central sparsification experiment (Section 2.3) lacks a precise description of its procedure, making the core empirical claim difficult to interpret.** The paper states that "3% of all neurons...are sparsified via SparseGPT in every FFN." But SparseGPT is a layer-level unstructured weight pruning algorithm; it operates on the entire weight matrix using the full Hessian, not on a per-neuron basis. The text does not clarify whether (a) only the selected neurons' weights are pruned while other neurons' weights remain dense, (b) SparseGPT is run on the full layer and then only the selected neurons' rows are examined, or (c) the selected neurons' rows are zeroed (ablated) rather than weight-pruned. These are fundamentally different operations with different interpretations. The caption of Figure 3 further muddies the matter by referring to "neuron sparsity" alongside "sparsified via SparseGPT," and then mentioning "ablating Wasserstein neurons" at ≥95% sparsity — conflating weight pruning and neuron ablation. Since this experiment is the primary evidence for the paper's central claim that Wasserstein neurons are "severely limited in their ability to be compressed," the ambiguity is a significant methodological gap that must be resolved for the claim to be properly evaluated.

2. **Sparse Expansion's performance comparisons (Section 3.6) do not control for total parameter count.** Sparse Expansion stores 16 sets of sparse weights per layer plus a PCA+K-means router, a massive increase in effective parameters. The paper acknowledges the method is "not practically implementable" but still presents perplexity comparisons against SparseGPT without holding the total nonzero weight count constant. The reported gains could partly or entirely reflect the fact that Sparse Expansion allocates more total weight bits to each layer. A controlled comparison (e.g., against a single denser sparse matrix with the same total nonzero count, or a mixture with randomly assigned experts) is needed to attribute gains to the disentanglement mechanism rather than to the increased parameter budget.

### Minor

1. **The Wasserstein distance metric's validation is correlational and limited.** The paper validates WD against mapping difficulty (MD), but MD itself is an unvalidated metric proposed in the same paper. No toy-model demonstration is provided where ground-truth entanglement (e.g., from a known superposition setting like Elhage et al. 2022) is shown to correlate with WD. Without such grounding, it is unclear whether WD captures entanglement specifically or merely some other property of non-Gaussian distributions (e.g., a step-function neuron in a binary classification network would also have non-Gaussian outputs but may not be "entangled" in the superposition sense). The argument is not circular (as one reviewer claimed — the paper correctly treats MD and WD as independent operationalizations), but it is weaker than it could be.

2. **The R² ≈ 0.24 for WD predicting improvement under Sparse Expansion (Figure 7) is presented as WD "best explaining improvement," but the comparison is against metrics with R² ≈ 0 or < 0.001.** The paper's claim is technically correct as a comparative statement, but it would be more informative to report the full distribution of improvements (including the many high-WD neurons that show little improvement) and to discuss why 76% of the variance remains unexplained. The framing could be misinterpreted as claiming WD is a strong predictor rather than merely the least-bad among near-zero alternatives.

3. **The link to superposition theory (Section 3.5) is empirically thin.** The empirical bounds in Figure 8 are derived from a single model (Pythia 1.4B) at a single sparsity level (80%). The "linear front" is a heuristic observation on log-log axes. The paper appropriately characterizes this as preliminary evidence, but the claim that Sparse Expansion tests "theoretical bounds of computation under entanglement" is overstated relative to the evidence shown.

### Trivial
- The asymmetric normalization in the mapping difficulty metric (median for outputs, max for inputs, Equation 2) is not justified and could produce spurious correlations — pairs with very small input differences that happen to have non-negligible output differences could dominate the ratio.
- The paper uses "sparsified" to refer to both weight-level pruning (within a neuron's row) and neuron-level ablation, sometimes within the same figure caption (Figure 3), creating avoidable confusion.

## Nice-to-Haves
- A synthetic toy experiment (e.g., in a controlled superposition setting from Elhage et al. 2022) showing that WD correlates with known ground-truth entanglement would substantially strengthen the metric's validity.
- Testing whether the set of top-3% Wasserstein neurons changes with different calibration datasets (the metric is computed over Wikitext-2 outputs) would clarify the robustness of the phenomenon.
- Reporting variance in WD and improvement across multiple runs of Sparse Expansion (different random seeds for K-means clustering) would assess metric stability.

## Removed Points
These points were raised in the reviews but are removed or downgraded per the rules:
- **"Circular definition" criticism (Harsh Critic Issue 2's stronger framing)**: The reviewer claimed the metric is "circularly defined" because MD and WD correlate. This is incorrect — the paper proposes two distinct operationalizations of entanglement (MD: input-output mapping behavior; WD: distribution shape) and shows they converge. Convergent validity between two independent metrics is the opposite of circularity. The underlying concern (lack of external ground-truth validation) is kept as a Minor weakness above.
- **"Sparse Expansion's contribution to understanding entanglement is overstated" (Issue 4's framing as structural flaw)**: The reviewer claims the method only shows that multiple weight sets better approximate a complex function — but the paper's value is in using this to study specific neuron types. The method is self-described as an experimental framework, not a practical compression tool. The more reasonable concern about parameter-count confounding is preserved in Major weakness 2.
- **Generic strength claims from Strength Finder**: No strengths were generic or lacked specific content; all were grounded and evidence-backed, so none were removed.
- **Formatting/style nitpicks**: None present in the reviews.
- **Missing related work / appendix / references**: Not raised in a way that requires action.

## Novel Insights
Beyond the paper's own contributions, the most notable observation across the reviews is that the WD-to-Gaussian metric's "success" compared to other metrics (mean, variance, GMM components) may be a low bar — the others all have R² near zero. This suggests the real open question is not "why does WD work?" but "what is the actual factor that makes certain neurons hard to sparsify, and why do standard distributional metrics (mean, variance) fail entirely to capture it?" The paper identifies the phenomenon but does not provide a mechanistic explanation for why shape irregularity matters more than scale or spread for weight pruning. An interesting follow-up would be to investigate whether the same neurons flagged as Wasserstein are also those that participate in multiple distinct circuits (identifiable via mechanistic interpretability), which would directly connect the WD metric to circuit-level polysemanticity.

## Suggestions
1. **Clarify the Section 2.3 experiment.** State explicitly: (i) whether neurons are ablated (row zeroing) or weight-pruned; (ii) if pruned, the exact procedure for applying SparseGPT to a subset of rows; (iii) whether the rest of the model remains dense; (iv) the distinction between "neuron sparsity" and "weight sparsity" in the x-axis of Figure 3. This is the single most important revision.
2. **Add a controlled parameter-count baseline** for Sparse Expansion comparisons, e.g., a single denser sparse matrix with the same total nonzero weights, or a mixture with randomly assigned experts.
3. **Include a toy-model validation** of the WD metric in a setting with known ground-truth superposition (following Elhage et al. 2022).
4. **Temper the R² framing** from "best explains improvement" to something like "is most correlated among the tested metrics (R² ≈ 0.24), while alternatives show negligible correlation," and discuss the substantial unexplained variance.
5. **Remove the conflation of "sparsified" and "ablated"** by using distinct terminology for weight pruning vs. neuron removal throughout the paper.

## Score and Decision

**Originality**: The paper addresses a genuinely novel connection — between neuronal entanglement (from superposition theory) and weight sparsity (from model compression). The WD-to-Gaussian metric, while not a complex technical innovation, is a novel application of existing tools to a new problem. **3/5**

**Importance of research question**: Understanding which neurons are hard to prune and why is directly relevant to improving model compression and to mechanistic interpretability. The question is timely and well-motivated. **4/5**

**Claims supported**: The core claim that Wasserstein neurons are disproportionately important under sparsity is supported but hamstrung by the ambiguous description of the central experiment. The claim that WD predicts improvement under Sparse Expansion is supported (as a comparative claim) but the correlation is weak. The claims about disentanglement via Sparse Expansion are supported at a correlational level. **2.5/5**

**Soundness of experiments**: The experiments are broad (multiple models, sparsities, tasks) but the central experimental procedure is underspecified, the parameter-count confound in Sparse Expansion comparisons is not addressed, and the metric validation lacks ground-truth anchoring. **2.5/5**

**Clarity of writing**: Generally clear in motivation and interpretation. The key ambiguity in Section 2.3 undermines what would otherwise be the clearest part of the paper. The conflation of pruning and ablation terminology is a distracting inconsistency. **3/5**

**Value to community**: If the experimental ambiguity is resolved and the metric is further validated, the paper could provide a useful diagnostic tool (WD to Gaussian) for identifying entanglement-vulnerable neurons and inspire entanglement-aware pruning algorithms. The Sparse Expansion framework is unlikely to be used directly but may influence future methods. **3/5**

**Weighted overall**: The paper identifies a real and potentially important phenomenon, but the ambiguous central experiment and unaddressed confound in the performance comparisons prevent the contribution from being fully convincing in its current form. The work is interesting and worth pursuing, but the presentation needs substantial revision before the core claims can be accepted as established.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>