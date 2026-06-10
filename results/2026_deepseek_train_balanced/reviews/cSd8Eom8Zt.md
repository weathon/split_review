## Summary

This paper proposes DeepKDE, an autoencoder-based post-processing method that reshapes a pretrained model's feature space to match a target distribution (Normal or Gaussian Mixture Model). The key technical innovation is a differentiable loss that approximates the Jensen-Shannon divergence via kernel density estimation, combined with a supervised clustering loss and a reconstruction loss. Experiments on CIFAR-10 and Fashion MNIST using ResNet-18 and ViT backbones show accuracy improvements over the original models, and the structured latent space enables interpretability analysis of misclassifications.

## Strengths

1. **Novel differentiable KDE-based density matching loss (Eq. 7, Section 2.1).** The idea of minimizing JS divergence between the latent distribution and a target by plugging KDE estimates into a differentiable loss function is genuinely new. This avoids adversarial training or complex generative models, making it architecturally simple. The paper also pragmatically acknowledges the tension between KDE's high-dimensional weakness and the need for density estimation, arguing that choosing an easy target distribution makes early suboptimal estimates sufficient for convergence (line 84).

2. **Demonstrated accuracy improvements (Section 3.2, Figure 3).** DeepKDE achieves higher classification accuracy than the original ResNet-18 and ViT models on both CIFAR-10 and Fashion MNIST. This is non-trivial: imposing a strong distributional constraint on the latent space (GMM or Normal) could degrade performance, yet the results show improvement. The comparison uses the original models' standard classification accuracy as the baseline.

3. **Qualitative interpretability via structured latent space (Figure 5, Section 3.2).** The known GMM structure allows the authors to explain specific misclassifications — e.g., a car with a trailer falling in the truck cluster or a truck resembling a car falling in the car cluster. This demonstrates a concrete benefit of having a known probability distribution in the latent space for post-hoc analysis.

## Weaknesses

### Major

1. **Ablation analysis contains contradictory descriptions that prevent interpretation (Section 3.1, Figures 2(d)–2(f)).** The paper reports weight triplets described as corresponding to {L_pdf, L_cl, L_rec} but the descriptions do not match the weights:

   - **Figure 2(d):** weights {0, 0.9, 1}, described as "emphasizing the role of L_pdf." But L_pdf has weight 0, so this shows the latent space *without* L_pdf, not its role.
   - **Figure 2(e):** weights {0.9, 0, 0.1}, described as "emphasizing the role of L_cl." But L_cl has weight 0.
   - **Figure 2(f):** weights {0.8, 0.2, 0}, described as "emphasizing the role of L_rec." But L_rec has weight 0.

   Additionally, the set {0, 0.9, 1} does not satisfy the stated total loss formula L_tot = α·L_pdf + β·L_cl + (1−α−β)·L_rec, since 1−0−0.9 = 0.1, not 1. The paper does not explain this discrepancy. As a result, the ablation analysis — which should provide insight into each loss component's contribution — cannot be reliably interpreted.

2. **The contribution of the novel L_pdf component is not isolated from the supervised clustering loss.** The paper's primary technical claim is that the KDE-based distribution matching (L_pdf) is the novel and useful component. Yet the experiments never compare DeepKDE with all three losses against a version with L_pdf removed (α=0, keeping β and L_rec fixed). The ablation in Section 3.1 shows that removing L_cl causes mode collapse, establishing that L_cl is necessary. But the converse — whether L_pdf provides any benefit beyond L_cl + L_rec — is not tested. Without this ablation, the accuracy improvements on CIFAR-10 and Fashion MNIST could be attributable entirely to the supervised clustering loss, which is a standard technique. The paper's central contribution is thus conflated with a known approach.

3. **Critical experimental details are missing, compromising reproducibility.**
   - **Feature extraction layer unspecified (line 150).** The paper states features are extracted from "a meaningful layer" of the primary model but never specifies which layer of ResNet-18 or ViT. Since this entirely determines what information DeepKDE receives, the experiments cannot be reproduced or properly compared against.
   - **No numerical accuracy table.** The main quantitative result (accuracy comparison) is only referenced as Figure 3. No actual accuracy values, baseline accuracies of the original models, or standard deviations are given anywhere in the text.
   - **No variance or number of runs reported.** No indication that experiments were repeated or that the reported improvements are statistically significant.
   - **Cluster center specification unclear (Eq. 9).** The loss L_cl uses cluster centers c_j, but it is not stated whether these are learned parameters or fixed to the target GMM centers. This is essential for understanding how labels are used.

### Minor

1. **KDE reliability in 10-dimensional space is asserted but not validated.** The paper acknowledges that "KDE is known to be a poor estimator for multidimensional densities" (line 84) and argues that choosing an easy target mitigates this. However, no analysis or empirical evidence is provided that the KDE estimates are accurate enough for gradient-based optimization in d=10. A bandwidth sensitivity study or diagnostic of KDE accuracy during training would substantiate this claim.

2. **Large batch size is not justified.** The batch size of 10,000 (20% of CIFAR-10's 50K training samples) is far larger than typical. This is presumably necessary for meaningful KDE estimates but is not discussed or analyzed. This also limits the method's applicability to larger datasets where such batch sizes may not fit in memory.

3. **The accuracy comparison does not control for supervised post-processing.** DeepKDE uses labels via L_cl during its post-processing training, while the original model is evaluated directly without any post-processing. A comparison against a simple supervised baseline (e.g., a linear classifier or MLP trained on the same extracted features) would help isolate whether the distribution-matching component provides any benefit beyond standard supervised post-processing.

### Trivial

- None of substance beyond the issues already identified above.

## Nice-to-Haves

- A bandwidth sensitivity study for the KDE estimator would strengthen the method's empirical grounding.
- Extending evaluation to the downstream tasks mentioned in the conclusion (anomaly detection, clustering) would demonstrate the claimed benefits of having a known latent distribution.
- Specifying how the cluster centers c_j in Eq. 9 are determined (learned or fixed) would clarify the method.

## Removed Points

- **Critic's claim that the accuracy comparison is "structurally invalid" because DeepKDE uses labels while the original model doesn't.** This overstates the issue: the original model was also trained with labels for classification. The comparison tests whether additional post-processing (with labels) can improve on the original model — a standard paradigm in transfer learning. The real problem is that the novel L_pdf component's contribution is not isolated, which is addressed above as Major weakness #2.
- **Critic's claim about "missing related works" and "should cite standard transfer learning baselines."** Rules prohibit flagging missing citations as a weakness.
- **Critic's dismissal of the qualitative analysis as "not evidence."** While the analysis is post-hoc, it is a legitimate demonstration of interpretability enabled by the structured latent space.
- **Strength Finder's claim of "systematic ablation isolating each loss component's role."** This strength is undermined by the verified descriptive errors in the ablation figures; it is therefore dropped.
- **Strength Finder's claim of "accuracy improvement is non-trivial."** While the improvement is reported, the attribution problem (Major #2) weakens this as a strength. Kept in modified form with caveat.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Correct the ablation descriptions to accurately reflect which loss component is present in each configuration, or clarify the weight notation if it differs from {α, β, 1−α−β}.
2. Add an ablation comparing DeepKDE with all three losses against a version with L_pdf removed (α=0, same β) on the benchmark datasets.
3. Specify the exact feature extraction layer for each primary model and provide a numerical accuracy table with mean and standard deviation over multiple runs.
4. Include a comparison against a simple supervised baseline (e.g., linear classifier or 2-layer MLP trained on the same features) to disentangle the effect of L_pdf from L_cl.

## Score and Decision

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>