Now I have a thorough understanding of all the evidence. Let me synthesize the final review.

## Summary

This paper introduces rRCM (Robust Representation Consistency Model), a certified robustness method that reformulates denoising along diffusion PF ODE trajectories as a discriminative task in latent space. Through a two-stage training process (contrastive pre-training along temporal trajectories + supervised fine-tuning with consistency regularization), the method enables one-step denoising-then-classification — dramatically reducing inference costs compared to prior diffusion-based smoothing methods while matching or improving certified accuracy. On ImageNet, rRCM achieves a 5.3% average certified accuracy improvement over DDS with an 85× reduction in inference latency (53 seconds vs. 52 minutes for DensePure at comparable accuracy).

## Strengths

1. **Major improvement in the efficiency–robustness trade-off.** On ImageNet, rRCM-B-Deep achieves 67.3% certified accuracy at radius 0.5 with 53 seconds inference latency, while DensePure requires 52+ minutes for comparable accuracy (Table 1). This is a qualitative leap that directly addresses a known limitation of diffusion-based smoothing. The 85× average inference cost reduction is well-documented with latency numbers.

2. **Novel reformulation of denoising as discriminative representation learning.** The paper's core idea — viewing PF ODE trajectories as providing structured connections between clean and noisy samples, then using instance discrimination to align temporally adjacent points in latent space (Eq. 7) — is genuinely novel. Unlike prior work that uses diffusion models as a separate purification module, rRCM integrates denoising and classification into a single model for one-step prediction (Figure 2b).

3. **Strong scalability with model size and training budget.** The paper demonstrates consistent certified accuracy gains scaling from rRCM-S → rRCM-B → rRCM-B-Deep, and with larger batch sizes (Figures 3, 4). Performance has not yet plateaued, indicating further gains are likely with more resources.

4. **Competitive or state-of-the-art certified accuracy on both ImageNet and CIFAR-10.** On ImageNet, rRCM-B-Deep surpasses all classical and diffusion-based baselines at every reported radius. On CIFAR-10, rRCM-B improves over DDS by up to 6.4% at r=0.5 and is competitive with ensemble methods (Boosting with 10 classifiers) using a single model.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Clean (unperturbed) accuracy of rRCM models is not reported.** The paper reports that the baseline ViT classifier used for DDS/DensePure achieves 81.35% validation accuracy on ImageNet, but never reports rRCM's own clean accuracy. Without this, the reader cannot fully disentangle whether some of the certified accuracy gains come from having a stronger underlying classifier versus from the robustness-specific training. While the main results (certified accuracy vs. radius) remain valid comparisons, this information would help contextualize the contributions.

2. **The paper mentions a MoCov3 comparison but does not show the quantitative results.** Section 3.3 states "we conduct further experiments and compare the effectiveness of our method with MoCov3" in reference to Figure 5, but the text only presents a conceptual diagram — no quantitative comparison (e.g., certified accuracy of an MoCo-v3 pre-trained model fine-tuned with the same objective) appears in the main text. Given that the paper argues its pre-training differs from standard contrastive learning, showing these results would significantly strengthen that claim.

3. **Training compute is not reported or controlled for.** The pre-training uses 600k steps at batch size 4096 on ImageNet — substantial compute that is not accounted for when comparing with classical methods trained with far fewer iterations. While the paper's primary selling point is inference efficiency (which is well-supported), the "state-of-the-art" claim is somewhat asymmetrical when baselines have not received comparable training budgets. Reporting total GPU-hours for pre-training and fine-tuning separately would enable proper context.

4. **No ablation of the individual loss terms in the pre-training objective.** The pre-training loss (Eq. 7) combines a consistency loss and a contrastive loss, computed on different network outputs (encoder vs. projector). The paper explains the design rationale (training instabilities with the alternative) but provides no quantitative ablation showing the contribution of each term, the effect of the projector head, or the choice of where to compute each loss.

### Trivial

- The specific discretization step count `N` for the PF ODE is not stated (only `T=80` is given, which is the maximum diffusion time). While the paper follows the EDM/consistency model schedule where this is specified, stating `N` explicitly in the main text would improve clarity.

## Nice-to-Haves

- **PF ODE approximation quality analysis.** The paper uses a crude approximation for constructing temporal pairs during pre-training (x_{t_{n-1}} ≈ x_{t_n} + (t_{n-1} - t_n)ϵ) and honestly acknowledges this limitation. An analysis of how this approximation affects representation quality (e.g., comparing against pairs from a pre-trained score model on a small validation set) would strengthen the methodology section but is not necessary for the core claims.

- **Hyperparameter sensitivity.** Reporting results for at least one alternative value of τ, η₁, η₂ or the number of time steps N would help assess robustness of the method.

- **t-SNE visualization of representations.** A qualitative visualization comparing encoder outputs of clean/noisy/perturbed samples from rRCM vs. a standard classifier would make the "consistent representations" claim more vivid.

## Removed Points

- **"No variance or confidence intervals for certified accuracy"**: This criticism reflects a misunderstanding of standard practice in the randomized smoothing literature. Cohen et al. (2019), Carlini et al. (2022), and essentially all RS papers report point estimates on a 500-image test subset. The certification procedure itself provides statistical guarantees (99.9% confidence) for each individual sample's radius. Requesting bootstrap CIs or subset variance goes beyond what is standard or expected in this line of work.

- **"PF ODE approximation is crude / not analyzed"**: The paper explicitly acknowledges the approximation (Section 3.3: "We adopt this method (Song et al., 2023) in our work, leaving further exploration of pre-trained score models to future research") and justifies it by avoiding reliance on a separate pre-trained score model. This is an honest design choice, not a hidden flaw.

- **"Training a ViT from scratch with fine-tuning objective proves challenging — this is speculation"**: The paper reports this as an empirical observation from early experiments. It is a valid qualitative observation supporting the need for pre-training, not a speculative claim.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one interesting observation: the paper's two-stage approach (contrastive pre-training along PF ODE trajectories + supervised fine-tuning with consistency) can be seen as a way to *factorize* the learning problem — representations learned through temporal alignment in step 1, then class-boundary refinement in step 2. This factorization explains why the method scales well (the pre-training objective is class-agnostic and can benefit from more data/compute) and why it avoids the training difficulties of learning from scratch with the combined objective. The reviews also highlight that the paper's central conceptual contribution (using PF ODE structure for robust representation learning) is separable from the specific implementation choices, suggesting that future work could improve the approximation used for temporal pairs or integrate stronger pre-trained score models.

## Suggestions

1. **Add clean accuracy to the main tables.** Report each rRCM model's top-1 accuracy on clean ImageNet/CIFAR-10 validation sets alongside the baseline classifier's accuracy. This allows readers to properly contextualize the certified accuracy gains.

2. **Include the MoCov3 comparison results.** The text already mentions this comparison was performed — report the actual certified accuracy numbers. This is the cleanest ablation for isolating the effect of the consistency-tracking pre-training versus standard contrastive pre-training.

3. **Report total training GPU-hours** for pre-training and fine-tuning separately. This enables fair comparison of the overall cost of the method versus alternatives.

4. **Add a brief ablation table** showing (a) pre-training + fine-tuning (full method), (b) fine-tuning only from scratch, (c) MoCo-v3 pre-training + same fine-tuning, to directly demonstrate the value of each component.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>