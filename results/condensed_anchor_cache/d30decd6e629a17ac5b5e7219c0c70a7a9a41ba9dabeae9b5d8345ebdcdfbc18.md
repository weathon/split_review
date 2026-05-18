- Decision: Accept
- Scores: 6, 6, 6, 6

## Merged Review

### Summary
All reviewers rate the paper 6, with confidence ranging from 2 to 4. The paper introduces Noise‑conditioned Energy‑based Annealed Rewards (NEAR), a framework for imitation learning from observation that replaces adversarial training with energy‑based modeling using denoising score matching. Learned energy functions serve as reward signals for RL policies. NEAR is evaluated on complex humanoid tasks (locomotion, martial arts) and compared to Adversarial Motion Priors (AMP). Reviewers find the problem motivation strong, the algorithm clearly explained, and the ablation and failure analyses useful. However, they note several weaknesses: missing comparisons with alternative baselines (including non‑adversarial methods and other diffusion‑based IRL works), incomplete justification of improvement over AMP, lack of computational cost analysis, limited task scope, statistical rigor concerns (only 5 seeds, 20 test episodes), and clarity issues in figures and intuition. Several reviewer questions overlap directly with these criticisms (e.g., requests for comparisons with DiffAIL, SMILING, L2 distance reward, and learning curves/wall‑time comparisons).

### Strengths
- The research problem (imitation learning from observation) is relevant and important. (R1)
- The algorithm details are clearly presented; the use of denoising score matching to learn energy functions as reward signals is novel. (R1, R4)
- Ablation studies on key components (e.g., annealing) are informative, and the failure analysis provides useful insight. (R1)
- NEAR performs well on a range of complex humanoid tasks, including stylized walking, running, and martial arts, achieving imitation accuracy and smoothness competitive with AMP. (R2, R3)
- The method avoids the instability and non‑smooth reward landscapes of adversarial training, yielding stable reward signals. (R4)
- The paper is well‑written, with detailed explanation of NEAR and clear positioning within the motion imitation literature. (R3)
- The evaluation includes quantitative metrics such as spectral arc length and imitation accuracy. (R3)

### Weaknesses
- **Limited baseline comparison.** NEAR is only compared against AMP. Other non‑adversarial imitation learning methods (e.g., a simple L2 distance reward) are omitted without justification. (R1, R2, R3) Several reviewers request direct comparisons with other diffusion‑based IRL works, specifically [1] DiffAIL and [2] SMILING, to support the claim that NEAR is the first to apply diffusion models for reward learning. (R4)
- **No clear improvement over AMP.** NEAR does not consistently outperform AMP; its performance often shows higher variance and motions are generally closer to ground truth for AMP. Reviewers ask for motivation why NEAR is a good alternative (e.g., lower hyperparameter sensitivity, faster learning, better sample efficiency). (R2, R3) The learning curves and wall‑time comparisons between NEAR and AMP are missing. (R3)
- **Limited task scope.** The framework is only evaluated on continuous, physics‑driven humanoid tasks. Applicability to discrete actions, sparse rewards, non‑smooth expert demonstrations, or highly stochastic / multi‑modal environments is not explored. (R2)
- **Computational cost not analyzed.** Training a noise‑conditioned energy model can be computationally intensive, but the paper does not compare GPU hours or training time with AMP, nor does it provide a breakdown of training the energy model vs. the RL policy. Scaling with state dimensionality and number of demonstrations is unclear. (R2)
- **Statistical rigor concerns.** Only 5 random seeds are used for training; confidence intervals are reported but wide and overlapping. 20 test episodes is low for variance estimation. Reviewers suggest 20–30 seeds or more episodes would improve reliability. (R1)
- **Clarity of figures and intuition.** Figure 1 and Figure 3 are difficult to interpret; the paper lacks intuitive explanation of how the energy function provides a good reward signal (e.g., why the policy follows a trajectory rather than reaching a high‑probability state). (R1, R3) The description of the energy function and adversarial reward in Figure 1 (different scales, values) needs more detail. (R3)
- **Explicit contribution statement.** The novelty is not explicitly stated; the contribution could be more clearly separated from related work. The paper should directly compare its method with existing approaches rather than only describing them. (R1) Additionally, the claim of being the first to use energy‑based diffusion models for IRL requires clarification, given existing works like [1] and [2]. (R4)
- **Data scarcity.** NEAR appears more affected by limited data than AMP; this is a notable weakness that should be analyzed further. (R1, R3) One reviewer notes that AMP should also suffer from data scarcity (discriminator memorization). (R3)
- **Missing future work.** The conclusion lacks a future work section; extending the annealing strategy is suggested. (R1)

*Questions that overlap with weaknesses / missing experiments:*
- Why is only one baseline (AMP) compared? (R1)
- Can the authors provide a comparison of NEAR’s computational requirements (training time, GPU hours) relative to AMP? (R2)
- What is the variability across episodes (not just seeds)? (R3)
- Why does NEAR not always outperform AMP despite added complexity? (R3, R2)
- How does NEAR compare with DiffAIL [1] and SMILING [2] in terms of data efficiency and performance? (R4)