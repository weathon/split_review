- Decision: Reject
- Avg Score: 4.75
- Scores: 8, 3, 3, 5
Now I have a thorough understanding of the paper and the reviewer inputs. Let me compose the consolidated review.

## Summary

This paper introduces Privacy-Aware Sparsity Tuning (PAST), a defense against membership inference attacks (MIAs) that applies adaptive ℓ1 regularization to model parameters based on their "privacy sensitivity" — measured as the gradient of the loss gap between member and non-member data. The key empirical finding motivating PAST is that only a small fraction of parameters substantially affect privacy risk (the top 20% account for 89.27% of total sensitivity). PAST promotes sparsity in privacy-sensitive parameters while sparing insensitive ones, and can be applied as a post-training tuning step on top of existing defenses. Experiments across five datasets and eight baselines show consistent improvements in the privacy-utility trade-off.

## Strengths

- **Empirical discovery that privacy risk is concentrated in few parameters.** Figure 1b quantifies that the top 20% of parameters account for 89.27% of total privacy sensitivity and 97% of parameters have sensitivity below 0.1. This provides a principled motivation for non-uniform regularization and is a novel finding in the MIA defense literature.

- **Consistent privacy-utility improvements across diverse datasets.** Table 1 reports P1 score gains on Texas100 (0.572 vs. 0.557), Purchase100 (0.812 vs. 0.792), CIFAR-10 (0.784 vs. 0.638), CIFAR-100 (0.575 vs. 0.360), and ImageNet (0.438 vs. 0.350). The improvement is particularly large on CIFAR-100 (+0.215) and ImageNet (+0.088), showing the method generalizes beyond simple benchmarks.

- **Ablation isolating the benefit of adaptive weights.** Figure 5a compares L1, L2, L1+Ours, and L2+Ours on CIFAR-100. PAST's curve lies strictly below the uniform-regularization curves in the privacy-utility plane, proving that the adaptive weighting — not merely the sparsity penalty — is responsible for the improved trade-off.

- **Orthogonal compatibility with existing defenses.** Table 2 shows that applying PAST on top of five pretrained defenses (AdvReg, CCL, LabelSmoothing, MixupMMD, RelaxLoss) raises the P1 score in every case (e.g., MixupMMD from 0.755 to 0.825), establishing PAST as a plug-in extension.

- **Efficiency validated by wall-clock time.** Figure 6c reports PAST takes 1374s on CIFAR-100 with DenseNet121 — only 10.4% more than standard training (1245s) and less than six of the eight compared defenses.

- **Validation of loss gap as a privacy proxy.** Figure 1a provides empirical evidence that attack advantage and loss gap increase synchronously during standard training, supporting the use of loss gap gradients as the privacy-sensitivity signal.

## Weaknesses

### Fatal

None.

### Major

- **No variance or confidence estimates reported for any result.** The paper reports all P1 scores, attack advantages, and test accuracies as point estimates without standard deviations, error bars, or confidence intervals. This applies to Table 1 (P1 scores across five datasets), Table 2 (compatibility results), and all privacy-utility curves. It is impossible to assess whether the reported improvements are statistically significant or within the noise of a single run. While single-run evaluation for large-scale experiments (e.g., ImageNet) may be acceptable, smaller datasets like CIFAR-10/100 should include results over multiple seeds.

### Minor

- **The module-size factor |ℳ(θᵢ)| in the adaptive weight formula (Eq. 4) is included without justification or ablation.** The formula γᵢ = |ℳ(θᵢ)| · ∇_{θᵢ} G̃_θ / Σ_{j∈ℳ(θᵢ)} ∇_{θⱼ} G̃_θ multiplies by the parameter count of the containing module. The paper neither explains the rationale for this factor nor ablates its effect (e.g., by comparing with per-layer normalization without the module-size term). Since the overall adaptive weighting is validated empirically, this is a design-detail concern rather than a structural flaw.

- **Reliance on a held-out non-member set (the "inference set") is not discussed as a limitation.** The method requires labeled non-member data from the same distribution as the training set to compute the loss gap and its gradients. While this setup is shared with baseline methods (MixupMMD, AdvReg) and is standard for evaluation, it is a practical constraint in real deployments (e.g., hospital patient data) that goes unacknowledged in the Limitations section, which only mentions black-box and white-box attack settings.

- **Fixed α = 2.5 in Table 1 may not be optimal across all datasets.** The paper fixes α = 2.5 for all five datasets when reporting P1 scores in Table 1, but the ablation on α (Figure 6a) demonstrates that different α values yield different privacy-utility trade-offs. Without per-dataset tuning, the reported P1 scores may under-represent PAST's best possible performance on some datasets. (The privacy-utility curves in Figures 3 and 4 do explore varying α, partially mitigating this concern.)

- **The limitations section is sparse.** It only mentions that black-box settings are studied and that the privacy-utility trade-off cannot be fully broken. Missing are any discussion of the non-member data requirement, potential sensitivity to the composition of the inference set, or the fact that only three attack classes are evaluated.

### Trivial

- The notation in Eq. 4 omits absolute-value signs around the gradients; the formula uses ∇_{θᵢ} G̃_θ rather than |∇_{θᵢ} G̃_θ|, though the context makes clear that magnitudes are intended.

## Nice-to-Have

- An ablation comparing the proposed γᵢ normalization with simpler alternatives (e.g., normalization without the |ℳ(θᵢ)| factor, or per-layer scaling) would improve confidence in the specific design choice.
- Reporting inference set sizes used during training for all datasets (not just CIFAR-10 in the motivation) would aid reproducibility.
- A plot showing P1 score as a function of inference set size (e.g., 100 to 10,000) would clarify the method's data requirements.
- A comparison with structured or magnitude-based pruning would help position PAST relative to complexity-reduction defenses, since PAST also induces sparsity.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Criticism about notation clarity (detached gradient):** The critic questioned the computational graph detachment of G̃_θ. The paper explicitly states on line 158: "Note that the γ_i does not require a gradient in backpropagation, so it is detached from the computational graph." The concern is addressed in the paper. → **Removed (addressed by paper).**

2. **Criticism about individual attack advantages not reported:** The critic claimed individual attack advantages are not reported. However, Figures 3 and 4 show privacy-utility curves per attack method. The P1 score aggregates the highest advantage, but the per-attack data is present in the figures. → **Removed (addressed by paper).**

3. **Criticism about baseline tuning thoroughness:** The critic questioned whether baselines were tuned equally. The ablation in Figure 5a explicitly compares PAST against tuned L1/L2 baselines and shows PAST outperforms them, partially addressing this concern. Moreover, the asymmetry concern favors baselines (not the author's method). → **Removed (partially addressed by paper, and asymmetry favors baselines).**

4. **Criticism about missing related-work comparison with pruning-based defenses:** This is a suggestion, not a weakness. Related work section already discusses pruning defenses. → **Moved to Nice-to-Have.**

5. **Criticism that Figure 1a is from a single run on CIFAR-10:** This is a motivation figure illustrating an empirical observation, not a main experimental result. While replication across seeds would strengthen it, this does not rise to the level of a weakness in the paper's contributions. → **Removed (motivation figure, not a core claim).**

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely surface the same core observations — the paper's key empirical finding about parameter sensitivity concentration, its adaptive regularization strategy, and the scope of its evaluation. No cross-reviewer synthesis reveals an insight that the paper itself does not already articulate.

## Suggestions

1. **Add variance estimates for all main results.** Report P1 scores in Tables 1 and 2 as mean ± std over at least 3 random seeds for small-to-medium datasets (Texas, Purchase, CIFAR-10/100). Add error bars or shaded regions to privacy-utility curves (Figures 3, 4, 5a).
2. **Discuss the non-member data requirement explicitly in the Limitations section**, noting scenarios where such data may be unavailable.
3. **Provide a brief justification or ablation of the module-size factor |ℳ(θᵢ)|** in the adaptive weight formula. If it is included for normalization purposes, clarify this; if it approximately cancels out, remove it.
4. **Report inference set sizes** used during PAST tuning for all datasets, not only CIFAR-10.
