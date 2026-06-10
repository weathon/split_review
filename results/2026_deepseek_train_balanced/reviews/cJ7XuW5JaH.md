Now I'll produce the final consolidated review.

## Summary
This paper proposes a label recovery attack in Federated Learning that estimates posterior probabilities from an auxiliary dataset to recover batch labels from shared gradients. The authors derive the gradient-label relationship ∇z = p - y from the exponential family perspective, show it generalizes to focal loss, and empirically demonstrate that positive/negative samples of a class have approximately equal probability distributions, enabling posterior estimation. The attack achieves high accuracy on both untrained and trained models across diverse settings.

## Strengths
1. **Exponential family derivation of label leakage.** Section 4.2 (Equations 5–9) provides a principled explanation of why ∇z = p − y emerges: for exponential-family distributions, ∇_η ℓ(θ; x) = T(x) − θ, and for multi-class classification with cross-entropy + Softmax, the sufficient statistic T(x) is the label y and the parameter θ is the posterior probability p. This reframes the gradient-label relationship as an inherent consequence of the exponential-family structure of the categorical distribution, which prior analytical attacks (iDLG, LLG, iLRG) did not offer.

2. **Attack works on trained models (>90% InsAcc) across varying batch sizes and class imbalance.** Figure 4 demonstrates that after 1 epoch of training, the attack maintains >90% InsAcc for batch sizes from 64 to 1024 and class imbalance ratios from 10% to 90%. This is a practical advance because realistic FL deployments involve partially trained models, while prior analytical attacks (LLG, iLRG) are designed primarily for untrained models.

3. **Empirical discovery of approximate probability distributions for positive/negative samples.** Section 5.1 documents via ridgeline plots (Figure 2) and box plots (Figure 3) that positive (and negative) samples of a class have tightly clustered posterior probabilities. This observation enables posterior estimation from an auxiliary dataset without access to the actual training data.

4. **Thorough evaluation across diverse architectures and activations.** Table 2 covers MNIST/LeNet-5, CIFAR10/VGG-16, and CIFAR100/ResNet-50 with five activation functions (ReLU, Tanh, ELU, Sigmoid, SELU), demonstrating the attack's universality.

## Weaknesses

### Fatal
None.

### Major
1. **Theorem 1 derivation appears inconsistent with the standard cross-entropy result.** The paper's focal loss definition uses a non-standard per-class redefinition of p_t (p_t = p_i if i=t and p_t = 1-p_i if i≠t). When γ=0 and α_t=1, the paper claims equivalence to cross-entropy, but Theorem 1 gives ∇z_j = Σ_t (p_j − δ_{tj}) = K·p_j − 1, which does **not** match the known cross-entropy result ∇z_j = p_j − y_j. The paper's statement that focal loss with γ=0, α_t=1 is "equivalent to the cross-entropy loss" (line 69) is mathematically questionable under the given definition, because the loss sums over all K classes with redefined p_t rather than using the standard one-hot-weighted sum. This error undermines the paper's claim of "first root cause investigation" and the claimed generality of Theorem 1. Since Table 1 (an image) is inaccessible, the discrepancy cannot be fully resolved from the text alone, but as presented the derivation needs correction.

2. **The auxiliary dataset assumption creates an unacknowledged informational asymmetry in baseline comparisons.** The proposed attack requires a labeled auxiliary dataset from the *same distribution* as the victim client's private data. The baselines (LLG, iLRG) receive no such auxiliary data. The paper states the comparison is "fair" because all methods use untrained models (Section 6.1), but the fairness issue is about *informational advantage*, not training status. The proposed method gets 100 labeled samples per class (1,000 for CIFAR10, 10,000 for CIFAR100) from the validation set — a massive additional information channel that the baselines cannot exploit. That the proposed method outperforms baselines under this asymmetry is expected and not informative about its relative merit. A fair comparison would require either (a) giving the same auxiliary data to baselines, or (b) evaluating whether the proposed method's posterior estimation technique offers any advantage over simpler alternatives that also use the same auxiliary data (e.g., gradient matching initialized with auxiliary samples).

### Minor
3. **Overclaimed novelty.** The paper states "for the first time, we investigate the root cause of label leakage from gradients." However, iDLG (Zhao et al., 2020) already derived and exploited ∇z_j = σ(z_j) − δ_{jc}, which is the same relationship. The exponential-family framing is genuinely new, but the core gradient-label relationship was known. The novelty lies in the theoretical *explanation* (the "why"), not the discovery of a previously unknown vulnerability.

4. **No variance or error bars reported despite 20 runs.** The paper states "we run each experiment 20 times and report the average results" (Section 6.2) but reports only point estimates. Given that many results are exactly 100%, knowing whether all 20 trials achieved 100% or whether the average is 100% with some variance is essential. Without variance, the perfect results look suspicious — they could indicate the test conditions are trivially solvable rather than the method being robust.

5. **Only FedSGD is evaluated; no FedAvg results.** The paper assumes FedSGD (the client sends the gradient of the full batch). Most practical FL deployments use FedAvg, where clients perform multiple local SGD steps and send updated weights. The attack's clean exploitation of the bias gradient's algebraic structure is likely obscured under FedAvg, and the paper provides no evaluation of this more realistic scenario.

6. **Temperature parameter claimed in the abstract but not experimentally evaluated.** The abstract states the attack achieves >90% InsAcc on different "temperature parameters," yet τ only appears once in the formula (φ̂_j = (1/τ)Φ(...), line 169) with no dedicated experiment varying τ.

7. **No evaluation of distribution mismatch between auxiliary and target data.** The paper assumes the auxiliary dataset has the *same* distribution as the victim's data — an optimistic assumption. In practice, a server's auxiliary data would likely come from a related but not identical distribution. The paper does not quantify how performance degrades under distribution shift.

8. **Confusing notation in the focal loss definition (Section 4.1).** The per-class redefinition of p_t (p_t = p_i if i=t and p_t = 1-p_i if i≠t) is non-standard and unclear about what i refers to. This makes the derivation of Theorem 1 difficult to follow and may have led to the mathematical issue noted in Weakness 1.

### Trivial
None.

## Nice-to-Haves
- Evaluate baselines (LLG, iLRG) with the same auxiliary data to enable an apples-to-apples comparison.
- Add a simple gradient-matching baseline that also uses the auxiliary dataset to assess whether the proposed posterior estimation technique offers advantages over straightforward alternatives.
- Include a limitations/failure-cases discussion.
- Report per-trial statistics (min, max, std) for the 20-run experiments.
- Evaluate under FedAvg with varying numbers of local steps to assess practical relevance.
- Clarify the focal loss definition and notation; verify the correctness of Theorem 1's cross-entropy special case.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Suspiciously perfect results" (from harsh critic)** — The critic argues that 100% results across settings "suggest the setting is too easy." This is speculative. The paper's attack is designed to be a near-deterministic algebraic method under its assumptions (well-estimated posterior probabilities + known bias gradient). Perfect results are consistent with a method that has the right formula and sufficient data. Without variance information (Weakness 4), this concern cannot be confirmed or refuted, but the framing as "suspicious" is not a verified flaw.

- **"Key observation is a basic consequence of classifier training" (from harsh critic)** — The critic claims the observation that positive/negative samples have similar probabilities is "not a surprising empirical discovery." While not surprising in retrospect, it is a non-trivial empirical validation that the paper documents with figures, and it directly enables the attack. Dismissing a documented empirical finding as "not surprising" is a matter of opinion, not a weakness.

- **"Root cause analysis is a post-hoc reframing" (from harsh critic, partially)** — The exponential family derivation is genuinely novel and goes beyond iDLG. The overclaiming about "first time" is addressed in Weakness 3. The critic's stronger claim that the analysis has "no new discovery" is too harsh — the exponential family framing IS new, even if the underlying gradient relationship was known.

- **Strength Finder: "Robust across diverse classification variants"** — This is a restatement of results rather than a structural strength. The evidence (Table 3) supports it, but it belongs as evidence under the trained-model strength rather than a standalone strength.

- **Strength Finder: "Consistent 100% ClsAcc and InsAcc across most dataset/model/activation combinations"** — This is evidence of performance, not a conceptual strength. Folded into Strength 4.

## Novel Insights
The most interesting insight from the cross-review is not in either evaluation alone: it is that the paper's two main contributions (the exponential-family derivation and the attack with auxiliary data) have a tension that neither reviewer fully articulated. The exponential-family analysis (Section 4.2) elegantly shows that ∇z = p − y is a *fundamental* property of using cross-entropy + Softmax — a structural inevitability given the categorical distribution's exponential-family form. If this is truly the "root cause," then *any* classifier using this combination is inherently vulnerable regardless of loss function details. However, the proposed attack still needs auxiliary data to estimate p (the posterior probabilities). This means the theoretical contribution identifies a universal vulnerability, but the practical attack is limited by the auxiliary data requirement. The strongest defense of the paper would be: the exponential-family analysis proves that the vulnerability is inescapable for standard classifiers, and the auxiliary-data-based attack is one practical instantiation — but the paper does not make this argument, weakening the connection between its theoretical and practical contributions.

## Suggestions
1. **Fix Theorem 1.** Re-derive the focal loss gradient using standard multi-class focal loss notation (Lin et al., 2017), verify that the cross-entropy special case (γ=0, α_t=1) correctly reduces to ∇z_j = p_j − y_j, and clarify the p_t notation. If the current derivation is correct under the paper's non-standard definition, explain the definition clearly and show how it relates to standard focal loss.
2. **Re-balance the baseline comparison.** Either give the baselines access to the same auxiliary dataset, or alternatively compare the proposed method against a simpler baseline that also uses auxiliary data (e.g., using auxiliary samples to estimate label proportions via gradient matching).
3. **Report variance.** Add standard deviations, min/max, or box plots for the 20 runs.
4. **Add a FedAvg experiment.** Even a simple evaluation with 1–5 local steps would significantly improve practical relevance.
5. **Add a robustness experiment with distribution shift.** Sample the auxiliary dataset from a different but related distribution (e.g., a held-out split with different class proportions or a different domain) to show how the attack degrades.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>