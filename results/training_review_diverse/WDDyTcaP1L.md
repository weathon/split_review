Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes PAST (Privacy-Aware Sparsity Tuning), an adaptive ℓ₁ regularization method for defending against membership inference attacks (MIAs). The core idea is to assign per-parameter weights to the ℓ₁ penalty based on each parameter's "privacy sensitivity"—defined as the gradient of the loss gap between members and non-members with respect to that parameter. PAST is applied as a post-convergence tuning stage and is designed to focus regularization on the small fraction of parameters that most affect privacy leakage. Experiments on five datasets (Texas100, Purchase100, CIFAR-10/100, ImageNet) against multiple attack types show improved privacy-utility trade-offs compared to eight non-DP defense baselines.

## Strengths

1. **Novel and well-motivated proxy for privacy sensitivity.** The gradient of the loss gap between members and non-members is a conceptually clean way to measure each parameter's contribution to privacy leakage. The paper validates this proxy by showing (Figure 1a) that the loss gap and attack advantage rise synchronously during standard training.

2. **Computational efficiency and simplicity.** PAST adds only one extra gradient backpropagation per tuning epoch, increasing training time by 10.4% relative to standard training (Figure 5c). This makes it practical for deployment.

3. **Compatibility with existing defense methods.** Because PAST operates as a post-convergence tuning phase, it can be stacked on top of pre-existing defenses. Table 2 shows that applying PAST to five different pretrained defenses (AdvReg, CCL, LabelSmoothing, MixupMMD, RelaxLoss) consistently improves the P₁ score (e.g., from 0.720 to 0.784 for AdvReg), demonstrating plug-and-play integration.

4. **Thorough ablation studies on hyperparameters.** The paper systematically analyzes the effect of the focusing parameter α (Figure 5a), the base regularization strength λ (Figure 5b), and the number of tuning epochs (Figure 5c), providing practical guidance for selecting hyperparameters.

5. **Consistent empirical improvements across diverse settings.** PAST shows gains over eight non-DP baselines across five datasets, multiple attack types (NN-based, metric-based, augmentation-based), and multiple architectures (ResNet, DenseNet, MLP), under the strongest black-box adaptive attack setting.

## Weaknesses

### Fatal
None.

### Major

1. **Missing DP baselines combined with unsupported "state-of-the-art" claim.** The paper claims "state-of-the-art balance in the privacy-utility trade-off" (Abstract, Conclusion) but does not compare against any differential privacy (DP) training method (e.g., DP-SGD). DP methods are the standard rigorous defense against MIAs, operate under the same black-box threat model, and are directly comparable. The related work section also omits DP entirely. The paper's results are credibly superior to the non-DP baselines tested, but the "state-of-the-art" claim is unsubstantiated without engaging with the dominant paradigm for provable MIA defense. The authors should either (a) add DP-SGD baselines at comparable utility levels, or (b) temper the SOTA claim to reflect the scope of comparison (e.g., "among empirical, non-DP regularization-based defenses").

### Minor

1. **Core motivational claim rests on a single observation.** The paper's entire motivation—that "only a small fraction of parameters substantially impact the privacy risk" (Section 3.1)—is supported by a single figure (Figure 1b) from one dataset (CIFAR-10) and one architecture (ResNet-18). No evidence is provided for different datasets, model sizes, or training stages. While the method itself is validated across diverse settings, the generality of the driving observation remains unclear. Showing this distribution for at least one more dataset or architecture would significantly strengthen the motivation.

2. **No reported variance or statistical significance.** All experimental results (trade-off curves, tables) appear to come from single runs. There are no error bars, confidence intervals, or statements about multiple seeds. Privacy-utility trade-offs can vary across runs due to stochasticity in training, attack simulation, and data splits, making it impossible to assess whether the observed improvements (e.g., Table 1: 0.572 vs. 0.557 on Texas100) are statistically meaningful. This is a standard expectation for empirical papers in this field.

3. **Reliance on non-member data insufficiently discussed.** PAST requires an inference set of non-member examples to compute the loss gap and its gradient (Section 3.2). In many real-world deployments, obtaining a representative set of non-members from a sensitive distribution is impractical. While the paper notes that other methods (Mixup+MMD, AdvReg) share this requirement, it does not address how a practitioner might obtain such data (e.g., public proxy data, held-out data, synthetic data) or analyze sensitivity to the composition of the non-member set. The limitations section (Conclusion) only discusses label-only and white-box attacks, missing this practical constraint.

4. **Lack of comparison between tuning and training from scratch.** PAST is applied as a post-convergence tuning stage. The paper claims this is beneficial because "the loss gap can more accurately reflect member information in a roughly converged model," but provides no empirical comparison against applying PAST from the beginning of training. This comparison would clarify whether the tuning stage design is necessary or merely convenient.

5. **Normalization within modules not justified.** The privacy sensitivity weights are normalized within each associated module (e.g., linear layer) rather than globally (Equation in Section 3.2). The choice of within-module normalization is not explained or ablated. This could have implications for layers with very few parameters or for the relative emphasis across layers.

6. **P₁ score construction not justified.** The P₁ score (Table 1) is computed using the *highest* attack advantage across all attack methods. This conservative/worst-case choice is stated but not justified, and it contrasts with the trade-off curves which appear to use per-attack advantage. A brief justification would improve clarity.

### Trivial
None.

## Nice-to-Haves

- **DP-SGD baseline** (as discussed above) would either validate or bound the method's SOTA claim.
- **Broader validation of the sparsity claim** across at least one additional dataset/architecture.
- **Variance reporting** with 3–5 random seeds.
- **Sensitivity analysis** of PAST's weights to different samples of the inference set (e.g., bootstrap resampling).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"The trade-off curves (Figs. 2, 3) are dense and hard to parse"* — This is a figure-formatting/readability nitpick. Removed per hard rules on formatting/style nitpicks.

2. *"The absence of DP is especially notable because the paper's own related work section discusses overparameterization and MIA defenses but omits DP entirely"* — While the overall DP-baseline criticism is kept as Major, this specific sub-point about the related work section is too close to a "missing related work" complaint. The core criticism (missing DP baseline for SOTA claim) stands independently.

3. *"Broader impacts: The paper focuses on a positive application... but does not discuss potential negative uses"* — This is a generic expectation that exceeds standard practice for a methods paper. Nice-to-have at most, not a weakness.

4. *"The loss gap itself is a proxy; the paper shows correlation in Fig. 1a but does not discuss whether this gradient is stable or noisy"* — The paper provides a reasonable validation (synchronous rise of loss gap and attack advantage) for using the loss gap as a proxy. Demanding a stability/noise analysis of the gradient is a methodological stretch beyond what is typical for a paper of this type.

5. *"Statistical significance tests" and "Ablation on training from scratch vs. tuning" and "Sensitivity of weight assignment to inference set composition"* — Some of these appear in the "Strengthening the Paper on Its Own Terms" section. The significant ones (tuning vs. from-scratch) are already in the Minor weaknesses. The others are Nice-to-Haves that don't affect the core validity.

## Novel Insights

None beyond the paper's own contributions. The reviews identify standard methodological gaps (missing DP baselines, no variance reporting, limited generality of the motivational claim) rather than offering novel technical insights about the method or problem. The most useful observation is the meta-level point that the paper's strongest claim ("state-of-the-art") overreaches relative to the scope of baselines tested, which is a framing issue the authors should resolve.

## Suggestions

1. **Add DP-SGD as a baseline** at several privacy budgets that yield comparable utility levels, and plot the privacy-utility trade-off curves. This is the single most impactful change: it either validates the SOTA claim or honestly contextualizes PAST's performance.

2. **If DP baselines cannot be added**, revise all instances of "state-of-the-art" to accurately reflect the comparison scope (e.g., "state-of-the-art among non-DP regularization defenses" or "superior privacy-utility trade-offs compared to existing empirical defenses").

3. **Report all key results with variance** (mean ± std over 3–5 random seeds), including error bars on trade-off curves and confidence intervals on P₁ scores in Table 1.

4. **Strengthen the motivational claim**: show privacy sensitivity distributions for at least one more dataset (e.g., CIFAR-100 or Purchase100) to demonstrate the sparsity phenomenon is not an artifact of a single setting.

5. **Acknowledge and discuss the non-member data requirement** more directly in the limitations section, and if possible, analyze sensitivity to the choice and size of the non-member set.

## Score and Decision

The paper presents an interesting and intuitive method with clear empirical support across a wide range of settings. The core idea (adaptive ℓ₁ regularization based on privacy sensitivity) is novel, computationally lightweight, and compatible with other defenses. However, the paper overclaims by asserting "state-of-the-art" without engaging with DP methods, and it lacks basic variance reporting that is standard for empirical work. These are fixable issues that do not invalidate the core contribution but do reduce confidence in the current presentation. The paper would be competitive after addressing the major weakness (DP comparison or claim tempering) and the variance issue.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>