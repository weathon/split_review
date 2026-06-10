## Summary

This paper proposes PAST (Privacy-Aware Sparsity Tuning), which replaces uniform ℓ₁ regularization with an adaptive weighting scheme for defending against membership inference attacks (MIAs). The adaptive weight for each parameter is derived from the gradient of the member/non-member loss gap w.r.t. that parameter. The method follows a two-phase procedure: train to convergence, then tune with adaptive-ℓ₁ regularization. Experiments on five datasets against eight baselines and multiple attack types show improved privacy-utility trade-offs, and a key result shows PAST can be applied on top of other defenses to further improve their privacy metrics.

## Strengths

1. **Strong motivating empirical finding.** The paper shows (Section 3.1, Figure 1) that 97% of parameters in a ResNet-18 on CIFAR-10 have privacy sensitivity < 0.1, and the top 20% of parameters account for 89.27% of total cumulative sensitivity. This directly challenges the implicit assumption behind uniform ℓ₁/ℓ₂ regularization that all parameters contribute equally to privacy leakage, and provides a principled, data-driven motivation for adaptive regularization.

2. **Ablation cleanly isolates the contribution of adaptive weights.** The ablation in Section 4.2 (Figure 3a) compares L1 vs. L1+Ours and L2 vs. L2+Ours under identical tuning conditions. PAST (L1+Ours) strictly dominates both uniform L1 and uniform L2 across the entire privacy-utility frontier. Since the only difference is the adaptive weighting, this directly attributes the improvement to the core novelty, not to the tuning schedule or sparsity mechanism alone — this is the cleanest evidence for the paper's central claim.

3. **Complementarity with existing defenses is convincingly demonstrated.** Table 2 shows that applying PAST on top of five existing defense methods (AdvReg, CCL, LabelSmoothing, MixupMMD, RelaxLoss) improves the P1 score in every case — e.g., MixupMMD from 0.755→0.825 (+0.07), AdvReg from 0.720→0.784 (+0.06). This shows PAST is not merely an alternative to prior methods but can be used as a post-hoc privacy-enhancing fine-tuning step, which is practically valuable.

4. **Minimal computational overhead with concrete measurement.** Section 4.2 (Figure 4c) reports PAST takes 1,374s vs. 1,245s for standard training on DenseNet121/CIFAR-100 — only 10.4% overhead — since the adaptive weights are detached from the computational graph (line 158). This is substantially more practical than computationally expensive defenses like adversarial regularization.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Ambiguity in the core γᵢ formula hinders reproducibility.** Equation (line 150) introduces a tilde notation (G̃_θ) that is never defined; the surrounding text simply says "normalized privacy sensitivity" without specifying what normalization is applied. Additionally, the formula does not address whether gradients are taken in absolute value — gradients of the loss gap (which involves an absolute value at the outermost level) can be negative, which could make γᵢ negative (or the denominator near zero) and γᵢ^α undefined for non-integer α (α=2.5 is used). The |ℳ(θᵢ)| (module cardinality) factor is included without justification or ablation. These issues must be resolved for the method to be independently reproducible.

2. **Table 1 compares PAST only against undefended baselines for P1 scores across datasets.** The only cross-dataset quantitative table reports P1 scores for PAST and "w/o" (undefended) on five datasets, but does not include the other seven defense methods. The cross-dataset comparison against baselines therefore lacks tabular precision — readers must rely entirely on the visual trade-off curves (Figures 2, 3). Adding a tabular summary of the strongest competing methods on the same P1 metric would substantially strengthen the SOTA claim.

3. **Actual sparsity is not reported despite "Sparsity" in the title.** The paper provides weight distribution plots and Gini index, but does not report the fraction of parameters driven to exactly zero. Since the mechanism is ℓ₁-based sparsification targeting sensitive parameters, the achieved sparsity level is a natural quantity to report and is currently missing.

4. **The motivating observation (97% of parameters have sensitivity < 0.1) is shown for only one setup** (ResNet-18 on CIFAR-10). The paper's core motivation would be substantially strengthened by showing this concentration holds across architectures (e.g., DenseNet, MLP) and datasets (e.g., Texas100, Purchase100). As it stands, the reader cannot assess whether this is a general property or incidental to one configuration.

5. **Shadow model training for the adaptive black-box attack is underspecified.** The paper states that the strongest adaptive black-box attack is used, but does not specify whether the shadow models replicate the two-phase PAST tuning procedure using the same inference set splits and hyperparameters. This information is needed to assess whether the attack modeling is truly adaptive.

### Trivial
None.

## Nice-to-Haves

- Report results with variance estimates (error bars / standard deviations) across multiple random seeds. While single-run evaluation is common in the MIA defense literature, adding variance information would increase confidence in the results.
- Add a control experiment that gives ℓ₁ regularization access to the same inference set (e.g., via validation-based early stopping on the loss gap) to separate the benefit of non-member data access from the benefit of the adaptive weighting scheme.
- Compare against a simpler baseline that directly takes gradient steps on the loss gap without ℓ₁ regularization, using the same two-phase tuning setup, to clarify whether the sparsity mechanism provides value beyond gradient-informed optimization.

## Removed Points

- **"Circularity between proxy and objective" (Harsh Critic, Critical Issue 1):** *Removed* — This mischaracterizes the method. Using gradients of a well-established proxy (loss gap) to inform regularization weights is standard gradient-informed optimization, not circular reasoning. The evaluation tests MIA success across multiple attack types beyond the loss gap itself (NN-based, augmentation-based, metric-based), so there is no self-validation problem. The critic's own acknowledgment that the ℓ₁ mechanism "is a genuine difference" undermines the claimed severity.

- **"Data requirement creates unfair asymmetry" (Harsh Critic, Critical Issue 2, fairness framing):** *Downgraded to Nice-to-Have* — The paper explicitly notes that Mixup+MMD and AdvReg also use the inference set (line 199). PAST outperforms these same-data baselines. The concern about disentangling data advantage from the weighting mechanism is a reasonable ablation suggestion but not a fairness flaw in the existing comparison.

- **Several section-by-section observations:** (a) "Tuning phase may leak non-member privacy" — speculative, not supported by evidence; (b) "Ablation on α is expected" — saying a result is predictable is not a weakness; (c) "A fairer comparison would also allow baselines to benefit from the two-phase tuning" — the ablation (Figure 3a) already compares L1 vs. L1+Ours under identical two-phase tuning, so this is already addressed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Clarify the γᵢ formula: define G̃_θ (specify the normalization), state whether absolute values are applied to gradients in numerator/denominator, and justify or ablate the |ℳ(θᵢ)| factor.
2. Add actual sparsity measurements (fraction of parameters exactly zero before/after PAST tuning).
3. Include tabular P1 comparison against the strongest baselines to complement the visual trade-off curves.
4. Report the motivating sensitivity distribution for at least one additional architecture/dataset to establish generality.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>