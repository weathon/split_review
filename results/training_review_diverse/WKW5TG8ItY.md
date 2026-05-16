Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper studies the interaction between Lipschitz continuity and adversarial example transferability in ensembles. The authors identify an important trade-off: clipping layer-wise spectral norms (which improves individual model robustness) simultaneously increases the transferability rate between ensemble members, diluting ensemble-level gains. To address this, they propose LOTOS (Layer-wise Orthogonalization for Training rObust enSembles), which promotes orthogonality between the top-k singular subspaces of corresponding affine layers across ensemble members. The method is supported by a theoretical result (Theorem 4.1) showing that for convolutional layers, even k=1 provides effective orthogonalization, keeping overhead negligible. Experiments on CIFAR-10/100 with ResNet-18 and DLA models show that LOTOS improves black-box robust accuracy over clipped baselines and combines favorably with prior state-of-the-art (TRS).

## Strengths

1. **Identifies a genuine and non-obvious trade-off.** The paper shows empirically (Figure 1) that decreasing the spectral-norm clipping value increases individual model robustness but simultaneously raises transferability rates between ensemble members. This contradicts the naive expectation that Lipschitz continuity uniformly benefits ensemble robustness and provides clear motivation for a dedicated ensemble-training method. This finding alone is a useful contribution to the community's understanding.

2. **LOTOS is a well-motivated, novel method grounded in an architectural insight.** The orthogonalization loss targets the top singular subspaces of corresponding affine layers, which govern the most sensitive input directions. Theorem 4.1 provides a theoretically grounded efficiency result for convolutional layers: even k=1 effectively bounds the response to the other model's remaining singular vectors. The empirical verification (Figure 3, Left) confirms negligible improvement from k>1, making the method computationally practical.

3. **Consistent empirical gains across multiple dimensions.** In Table 1, LOTOS improves black-box robust accuracy over C=1 clipping alone (e.g., 29.3% vs. 23.6% for ResNet-18 on CIFAR-10). Table 2 shows LOTOS scales well with ensemble size (29.3% → 49.5% from 3→9 models, versus marginal gains for baselines). Table 3 shows LOTOS combines with TRS to further boost robust accuracy (up to 33.2% from 22.5% for ResNet-18 on CIFAR-10). The method also works on heterogeneous architectures (Figure 4), where prior methods may not apply.

## Weaknesses

### Fatal
None.

### Major

- **White-box attack parameters are not specified.** The paper repeatedly refers to "white-box attack" when computing transferability rates (Figure 2, Section 5.2 discussions) but never names the attack algorithm, number of steps, step size, perturbation budget ε, or whether it is targeted or untargeted (Definition 3.2 defines both, but experiments report only one aggregate). Without this information, the core transferability results are not reproducible. *Evidence*: The "Attacks" paragraph in Section 5 (line 138) describes the evaluation protocol in words but omits all attack hyperparameters. This is the single most important missing piece for reproducibility.

- **Ensemble robust accuracy is not defined in the main text.** Under black-box attacks, the paper reports "robust accuracy" for ensembles (Tables 1–3) but never states whether this is the fraction of examples where *all* models are correct, a majority vote, or some other aggregation rule. Without this, the reported numbers are ambiguous and the results cannot be reproduced or compared against future work. *Evidence*: The "Attacks" paragraph (line 138) and the table captions describe the surrogate model setup but not the ensemble decision rule.

### Minor

- **The "mal" margin parameter (Equation 3) is used experimentally but never formally defined.** The notation `\mathfrak{m a}\mathtt{1}` appears in the definition of S_k as a subtraction term inside ReLU, and the paper states "increasing the value of mal (from 0 to 0.8)" (line 154), but no text explains what this parameter controls. One can infer it is a slack/margin threshold below which the output norm is treated as negligible, but the paper never states this explicitly. *Evidence*: Equation (3), line 98, and line 154.

- **The connection between Proposition 3.3 and transferability rate is acknowledged as a proxy but remains loose.** Proposition 3.3 bounds the difference in *population loss* between two models on adversarial examples, whereas transferability rate (Definition 3.2) measures the probability that a *classification decision* transfers. The paper calls this a "proxy" (line 82) and uses hedged language ("might be," "might imply"), which is appropriate, but the theoretical motivation section would benefit from acknowledging this gap more explicitly rather than presenting the proposition as direct grounding.

- **LOTOS models are less individually robust than C=1 models, and the ensemble gain is not decomposed.** The paper acknowledges (line 154) that LOTOS models have lower individual robust accuracy than C=1 models. As the "mal" parameter increases, LOTOS models approach C=1 behavior. This means the ensemble gain could partly come from increased individual robustness (as mal grows) and partly from diversity. The paper does not disentangle these two factors, which would clarify the mechanism.

- **Training degradation at k≥20 is reported without supporting evidence.** The paper notes "for k≥20, we noticed a degradation in the training of the models" (line 187) and attributes it to over-constraining, but provides no training loss curves, accuracy trends, or other diagnostic evidence to substantiate this claim.

### Trivial
None.

## Nice-to-Haves

- A direct plot of ensemble robust accuracy (not just individual robust accuracy and transferability) vs. clipping value, analogous to Figure 1 but for the ensemble, would make the central trade-off immediately visible.
- The runtime/efficiency claim ("negligible" overhead, Section 4.1) would benefit from a concrete per-epoch wall-clock time comparison in the main text for one representative setting (Orig vs. C=1 vs. LOTOS).
- A brief note clarifying which experiments use batch normalization and which do not, placed early in Section 5, would help readability.
- Explicit standard deviation reporting for all entries in Tables 1–3 (some entries appear to lack error bars in the extracted text) would improve statistical rigor.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Abstract claims imply generality"** — The abstract states "increases the robust accuracy of ensembles of ResNet-18 models by 6 p.p." This is qualified to a specific architecture and dataset; it does not imply general claims beyond what is reported.
- **"Proposition 3.3 assumes both models share the same Lipschitz constant L"** — In the experiments, all models are clipped to the same C value, making this assumption reasonable. Not a weakness.
- **"FastClip singular vector availability"** — Whether FastClip returns all or top-k singular vectors is an implementation detail of a cited method; the paper uses k=1, which any power-iteration method can compute cheaply.
- **"Figure 1 does not show ensemble robust accuracy"** — The figure's purpose is to show the trade-off between individual robust accuracy and transferability, which it does. Ensemble robust accuracy is evaluated separately in Table 1.
- **"Heterogeneous ensemble gain is modest"** — The paper reports the results as they are. The critic's suggestion that more commentary is needed is a matter of taste, not a factual weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a dedicated experimental setup paragraph that specifies: (a) the white-box attack algorithm, steps, step size, and ε used for transferability measurement; (b) the black-box attack parameters; and (c) the exact aggregation rule for ensemble robust accuracy (e.g., majority vote or all-correct). This is essential for reproducibility.
2. Define the "mal" parameter explicitly in Section 4 when introducing Equation (3): state that it is a slack/margin threshold — the orthogonalization loss only penalizes the output norm when it exceeds this value.
3. Add a simple training loss curve or accuracy trend to support the claim that "over-constraining" causes the observed degradation at k≥20.
4. Consider adding a brief decomposition or discussion of how much of LOTOS's ensemble gain comes from improved individual robustness vs. increased diversity.

## Score and Decision

This paper makes a legitimate contribution: it identifies a real and underappreciated tension between Lipschitz continuity and ensemble transferability, proposes a novel and well-motivated method (LOTOS) to address it, provides theoretical grounding for its efficiency on convolutional layers, and demonstrates consistent empirical gains across architectures, datasets, and ensemble sizes. The weaknesses are presentation-level (missing attack specifications, undefined parameters) rather than structural or evidential. These are fixable with revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>