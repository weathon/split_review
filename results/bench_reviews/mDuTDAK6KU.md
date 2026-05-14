Now I have enough information. Let me write the final consolidated review.

---

## Summary

KOALA proposes a lightweight adversarial detector that flags inputs as attacks when class predictions from two complementary similarity metrics—KL divergence and an L0-based score—disagree. The core idea is that dense vs. sparse perturbations stress these metrics differently, forcing disagreement that enables detection. The paper includes a theoretical proof that, under certain prototype-separation conditions, no bounded perturbation can simultaneously fool both metrics, and evaluates the method on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet.

## Strengths

- **Novel detection principle grounded in metric complementarity**: The idea of using disagreement between KL divergence (sensitive to dense, low-amplitude shifts) and an L0-based metric (sensitive to sparse, high-impact changes) is fresh and geometrically well-motivated. The ablation study (§4.3, Table 2) shows that the KL+L0 combination consistently outperforms alternative metric pairs (L0+Cosine, KL+Cosine) on ResNet/CIFAR-10, providing empirical support for the claimed complementarity.

- **Ambitious theoretical framework**: The paper attempts to provide a formal correctness guarantee (Theorem 1), which distinguishes it from the majority of empirical adversarial detection work. The proof structure—showing that KL-flip and L0-flip conditions are mutually exclusive under bounded perturbations—is conceptually clear and offers useful geometric intuition about why the detector should work.

- **Practical, lightweight design**: The method requires only clean-image fine-tuning with no adversarial training or architectural changes. This plug-and-play property is demonstrated across two different architectures (ResNet-18, CLIP ViT-B/32), showing some generality.

## Weaknesses

### Fatal

None.

### Major

- **Non-standard detection metrics make results uninterpretable for comparison**: The confusion matrix definitions in §4.2 are highly non-standard for adversarial detection. TP counts adversarial examples that are *not flagged* but happen to be correctly classified as true positives. FN only covers undetected attacks that are *also misclassified* — adversarial examples that evade detection but are classified correctly by both metrics escape the FN count entirely. This conflates classification correctness with detection correctness, inflating recall and making the reported precision/recall numbers (e.g., 0.94/0.81 on ResNet/CIFAR-10) impossible to compare with any standard detection benchmark. The paper's detection claims cannot be evaluated against prior work using these metrics.

- **No comparison to any existing adversarial detector**: Despite surveying Feature Squeezing, LID, Mahalanobis, MagNet, NIC, and others in §2, the paper compares KOALA only against itself (different metric combinations). Without even a single baseline detector on the same models and attacks, there is no evidence KOALA advances the state of the art in adversarial detection.

- **Theorem applies to only 10% of Tiny-ImageNet test samples**: Table 1 shows that Theorem 1's conditions are satisfied on only 510/5,000 (10%) of Tiny-ImageNet test samples and 3,345/5,000 (67%) of CIFAR-10. On the non-compliant majority of Tiny-ImageNet samples, precision drops to 0.62–0.63. A detection guarantee that covers 10% of the data distribution in one setting is a severe practical limitation that the paper does not adequately address.

- **No adaptive attack evaluation**: An attacker aware of KOALA's detection mechanism (disagreement between KL and L0 predictions) can explicitly optimize to cause agreement between the two heads. The paper does not evaluate any such adaptive attack, which is a standard requirement for adversarial detection research. The paper mentions adaptive adversaries in §2 but never tests against them. While Theorem 1 purports to guarantee detection under certain conditions, for the substantial fraction of inputs where conditions are not met (33–90% depending on dataset), adaptive attack vulnerability is entirely unexplored.

### Minor

- **Attack generation details are underspecified**: §4.1 lists the attack methods (PGD, CW, AutoAttack) but does not specify whether they were generated against the baseline classifier and then evaluated on KOALA (a transfer setting) or generated white-box against the full KOALA model. This affects the interpretation of all detection results.

- **Proofs rely on KKT conditions applied to a cardinality-constrained set without justification**: Claim B.1 involves a feasible set defined by a minimum-cardinality constraint (`|δ_i| ≥ min_i` for at least Δ_L0(p*) coordinates), which is non-convex and disconnected. The proof applies KKT conditions (necessary only for local optima of smooth constrained problems) to this set without addressing the combinatorial selection of which coordinates to activate. The greedy selection heuristic is not proven optimal, which weakens the claim that the constructed δ' achieves the maximum inner product.

- **Assumption A3 lacks empirical justification**: The coordinate-wise bound `|δ_i| ≤ (3/2)|p*_i|` is described as "mild and practical" (§3.2) but no evidence is provided that real adversarial perturbations satisfy this bound. Since the bound is defined relative to the clean embedding (which varies per input), its practical restrictiveness is unclear.

- **No hyperparameter sensitivity analysis**: The L0 threshold τ, surrogate smoothness φ, and loss weights ω_L0=0.9, ω_KL=0.1 are set without any ablation or sensitivity study. The claim that "L0 is harder to optimize" as justification for the loss weights is not supported by evidence.

### Trivial

- The L0 metric's threshold in Eq. 2 depends on μ(c,p), the average absolute difference between the prototype and embedding. This means the effective threshold varies per prototype-embedding pair, creating a coupling between the metric and the specific comparison. This is not discussed but has no apparent impact on the empirical results.

## Nice-to-Haves

- Embedding-space visualizations (t-SNE/UMAP) showing where KL and L0 metrics agree/disagree for clean vs. adversarial examples would substantiate the geometric intuition in Figure 1.
- A characterization of what architectural or training choices could increase the fraction of Theorem 1-compliant samples, particularly for the CLIP/Tiny-ImageNet setting where compliance is only 10%.
- Analysis of the gap between the differentiable L0 surrogate used in training and the discrete L0 metric used at inference, and whether this gap affects detection quality.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim about the theorem being "vacuous/tautological"**: The theorem's condition involves the adversarial class ĉ, but this does not make it tautological. The theorem states that *if* the prototype of the target adversarial class is sufficiently separated from the true class prototype, *then* detection is guaranteed. This is a meaningful conditional guarantee: it tells us what structure in the embedding space enables detection. The limitation is not that the theorem is vacuous but that the condition is satisfied on only a subset of inputs.

- **Harsh Critic claim that the KL+L0+Cosine artifact is "damning"**: The paper acknowledges this finding in §4.3 and correctly interprets it as an instance where high detection rate comes at the cost of broken classification rather than genuine robustness. The paper uses this to argue *against* the three-metric combination, which is a reasonable analysis, not a self-contradiction.

- **Strength Finder claim about "Rigorous evaluation across models and attacks"**: This overstates the evaluation, which lacks baseline comparisons, adaptive attacks, and uses non-standard metrics. Weakened and moved to Strengths with caveats.

- **Harsh Critic claims about missing related works, typos, formatting, unreleased models, undisclosed hyperparameters, missing appendix**: These are all excluded per the hard rules. The paper cites what it cites, formatting artifacts are parser issues, and hyperparameter/implementation details are not required beyond what is provided.

## Novel Insights

The most interesting insight emerging from this paper—independent of whether the specific execution succeeds—is the observation that complementary distance metrics define distinct prediction-stability regions whose *mutual exclusivity* can be formally characterized. The proof strategy of showing that the conditions for fooling two metrics are incompatible (via energy budget trade-off between alignment direction and coordinate-wise magnitude) is a conceptual contribution that could be applied to other metric pairs beyond KL and L0. Even with the proof's technical gaps, this geometric framing of detection as "no single perturbation can lie in two stability bands simultaneously" is a useful way to think about designing certifiably detectable classifiers.

## Suggestions

1. **Fix the detection metrics**: Use standard detection definitions: TP = adversarial AND flagged; FP = clean AND flagged; TN = clean AND not flagged; FN = adversarial AND not flagged. Report the standard metrics and also report clean/adversarial accuracy separately for the accepted (non-flagged) predictions. This would make results comparable to prior work.

2. **Add baseline comparisons**: At minimum, evaluate Feature Squeezing and LID on the same ResNet/CIFAR-10 and CLIP/Tiny-ImageNet setups. This is essential for the paper to claim improvement over the state of the art.

3. **Evaluate adaptive attacks**: Design an attack that explicitly minimizes disagreement between the KL and L0 heads (e.g., a loss that penalizes both KL(c_target, p+δ) and L0(c_target, p+δ) being small simultaneously). Evaluate KOALA against this adaptive adversary and report how detection performance degrades.

4. **Address the proof gap**: Either prove that the greedy selection in Claim B.1 is optimal (e.g., by showing the objective is submodular or by using a different optimization framework) or reformulate the proof to provide an upper bound without requiring optimality of the constructed δ'.

This paper has a genuinely interesting idea and an ambitious theoretical framework. However, the evaluation is currently not up to the standard needed to support its claims: the detection metrics are non-standard, no baselines are compared, and no adaptive attacks are evaluated. The theorem, while conceptually valuable, applies to a small fraction of inputs in one of the two settings tested. With substantial revision addressing these issues, this could become a strong contribution.

---

On originality: the KL+L0 disagreement idea is novel in the adversarial detection space. On importance: adversarial detection is a significant problem. On claim support: the claims are partially supported — the theorem provides useful intuition but applies to a limited subset, and the empirical results are difficult to interpret due to non-standard metrics. On soundness: the experiments have significant gaps (no baselines, no adaptive attacks, non-standard metrics). On clarity: the writing is generally clear, though the confusion matrix definitions are confusing. On community value: the geometric framing is valuable, but the paper in its current form does not provide actionable evidence that KOALA works as a practical detector.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>