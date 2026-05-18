Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

## Summary

This paper identifies a previously overlooked trade-off: while Lipschitz continuity (via spectral norm clipping) improves the robustness of individual models, it *increases* the transferability rate of adversarial examples across ensemble members, undermining ensemble robustness. To address this, the authors propose LOTOS (Layer-wise Orthogonalization for Training rObust enSembles), a method that orthogonalizes the top-\(k\) subspaces of corresponding affine layers across ensemble members during training. LOTOS reduces transferability while preserving the benefits of Lipschitzness, achieving a 6 p.p. improvement in robust accuracy on CIFAR-10 for ResNet-18 ensembles and a 10.7 p.p. improvement when combined with the prior state-of-the-art TRS method.

## Strengths

1. **Identifies and empirically validates a previously unrecognized trade-off.** The paper is the first to show that decreasing the Lipschitz constant (via spectral norm clipping) *increases* the transferability rate among ensemble members, creating a tension between individual model robustness and ensemble robustness. This is convincingly demonstrated in Figure 1, which plots accuracy, robust accuracy, and transferability across varying clipping values, and supported by Proposition 3.3 as motivating intuition.

2. **Proposes LOTOS, a novel, lightweight, and well-motivated method.** LOTOS orthogonalizes the top-\(k\) subspaces of corresponding affine layers across models. The method is grounded in a clear intuition: since top singular vectors dominate a layer's transformation, orthogonalizing them forces models to respond differently to input perturbations. Theorem 4.1 shows that \(k=1\) suffices for convolutional layers under reasonable assumptions, and Figure 3 (left) empirically validates this — transferability changes by less than 1 p.p. as \(k\) varies from 1 to 15.

3. **Strong empirical results across multiple settings.** LOTOS improves robust accuracy by 6 p.p. over the Lipschitz-clipped baseline on CIFAR-10 (Table 1), scales well with ensemble size (Table 2: 9-model LOTOS ensembles substantially outperform 3-model), works on heterogeneous architectures where most prior methods are not applicable (Figure 4), and combines synergistically with TRS for an additional 10.7 p.p. gain (Table 3).

4. **Thorough ablation studies validate design choices.** The paper systematically ablates \(k\) (dimension of orthogonalized subspace), ensemble size, which layers to orthogonalize (Figure 3 right shows first-layer-only is nearly as effective as all layers), and the effect of batch normalization. These ablations give confidence that the design choices are well-founded.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported by evidence, and no identified weakness invalidates the central contribution.

### Minor

1. **Ensemble aggregation rule is not specified.** The paper reports "robust accuracy" for ensembles in Tables 1, 2, and 3 but never states how the ensemble combines individual model predictions into a single decision (e.g., averaging logits, averaging softmax probabilities, majority vote). While averaging softmax/logits is standard practice in the ensemble robustness literature, the omission makes the reported numbers less precisely interpretable, especially given that the paper's theoretical framework (Definition 3.2, Proposition 3.3) centers on the probability that *all* models are fooled simultaneously — the relationship between this condition and the ensemble's final prediction depends on the aggregation rule. The authors should specify the aggregation rule and, ideally, discuss how the transferability rate connects to ensemble robustness under that rule.

2. **Proposition 3.3 provides intuition, not a formal proof of monotonicity.** The proposition states an upper bound on the difference between two models' losses on adversarial examples. The paper correctly frames this as a "conjecture" (Section 3.2) and uses hedging language ("might be an indicator"), but the narrative around the bound could still be read as implying a monotonic relationship between Lipschitz constant and transferability. The bound only says that a smaller \(L\) *permits* greater similarity — it does not guarantee it. This is a common and acceptable use of a motivating inequality, but the paper would benefit from a sentence explicitly noting that the bound is permissive, not causal: i.e., a small \(L\) is consistent with high transferability but does not force it. The real evidence for the trade-off is the empirical data in Figure 1, which is convincing on its own.

3. **Theorem 4.1 is stated under restrictive assumptions without formal justification for the general case.** The theorem assumes a single input/output channel and circular padding. The paper claims (line 127) that it "extends" to multi-channel layers and other padding modes, but provides no formal argument for this extension. The empirical results (Figure 3 left, showing \(k=1\) suffices in practice) corroborate the practical conclusion, so this does not undermine the paper's claims. However, the theoretical section would be strengthened by either proving the multi-channel case or stating the empirical justification more prominently alongside the theorem.

4. **The paper's main results for black-box attacks rely on appendix-deferred attack specifications.** The attack algorithm, number of steps, perturbation budget \(\epsilon\), and other parameters are referenced to appendix sections (lines 138–139). While putting implementation details in the appendix is standard, the paper should at minimum state the perturbation budget \(\epsilon\) and the attack algorithm used (e.g., PGD with \(x\) steps) directly in the main text, since these are essential for interpreting the magnitude of the reported robust accuracy numbers.

### Trivial

1. **The weights \(w_i\) in Equation (3) are introduced but never discussed.** Since \(k=1\) is used throughout with \(w_1=1\) implicitly, this is a harmless inconsistency, but it should be clarified.

2. **The margin parameter "mal" in Equation (3) appears to be an important hyperparameter but its role is explained only in an appendix reference.** A brief definition in the main text would improve readability.

## Nice-to-Haves

- **Direct comparison with standalone TRS and DVERGE in the same main-text table.** Currently, Table 3 shows TRS+LOTOS and TRS alone, but a table with standalone LOTOS, standalone DVERGE, and standalone TRS under the same Lipschitz-clipped budget would make the incremental contribution clearer without requiring the reader to cross-reference the appendix.

- **Discussion of whether the trade-off is specific to spectral-norm clipping.** The paper uses FastClip for Lipschitz control, which is the SOTA and a reasonable choice. However, a brief discussion of whether the transferability-increasing effect generalizes to other Lipschitz regularization methods (gradient penalties, orthogonal layers) would strengthen the narrative.

- **Moving the heterogeneous ensemble results (currently Section S.4) or the adversarial training combination (Section S.8) more prominently into the main text.** These results answer important questions that the paper itself raises in Section 5.

## Removed Points

- **"The k ablation nuance discussion is missing"**: The paper *does* discuss this on lines 187–188, noting that \(k \ge 20\) leads to training degradation. This is not a missing analysis.
- **"Proposition 3.3 over-claims theoretical support"**: The paper explicitly calls this a "conjecture" and uses hedging language throughout ("might be an indicator," "might imply"). The criticism is technically valid but the paper is already appropriately cautious; retained as Minor #2 above with softened framing.
- **"The paper should compare to more methods"**: Scope is not a weakness when the comparison set is defensible and includes the SOTA (TRS, DVERGE in appendix).
- **Any formatting/style nitpicks**: These are PDF parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The key insight — that Lipschitz continuity trades off individual robustness against ensemble transferability — is the paper's own discovery, and the reviews do not surface any additional novel perspective beyond what the authors already articulate.

## Suggestions

1. **Specify the ensemble aggregation rule** (e.g., "we average logits across models and take the argmax") directly in Section 5, before the first robustness results table. Also clarify how the transferability rate definition (Definition 3.2) relates to ensemble robustness under this rule.

2. **Add a note to Proposition 3.3** clarifying that the bound is permissive, not causal: a small Lipschitz constant is consistent with high transferability but does not force it. This would preempt any over-interpretation of the theoretical motivation.

3. **State the attack parameters** (\(\epsilon\), attack algorithm, number of steps) for the black-box attacks directly in the main text rather than only in the appendix.

4. **Recommend \(k=1\) and \(M=1\) explicitly** in the Method section, with a forward reference to the ablation results that justify this choice.

5. **Clarify the role of the margin parameter "mal"** in Equation (3) with a brief sentence in the main text.

## Score and Decision

This is a strong paper with a clear contribution: it identifies a real and previously overlooked trade-off, proposes a novel method (LOTOS) that is both principled and practical, and supports its claims with thorough empirical evaluation. The theoretical components (Proposition 3.3 and Theorem 4.1) provide useful framing and motivation but are not the paper's main strength — the empirical results are. The method is validated across architectures, datasets, ensemble sizes, and in combination with prior SOTA methods. The weaknesses are primarily about omitted specifications and framing precision that can be addressed in a revision.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>