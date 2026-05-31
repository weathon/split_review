## Summary

This paper proposes to incorporate geometric priors (symmetry groups) into the latent space of abstract world models for reinforcement learning. The authors model the latent space as a quotient space (e.g., \(\mathbb{R}/k\mathbb{Z}\) for cyclic symmetries) and use an additive group action for transitions, combined with a disentanglement regularization to separate symmetric and non-symmetric features. Experiments on toy MDPs, MiniGrid, and VizDoom show improved generalization and downstream RL performance compared to unstructured baselines.

## Strengths

- **Addresses an important problem**: Improving sample efficiency in RL via structured representations is a timely and relevant research direction.
- **Clean integration of geometric priors**: The method encodes known symmetries directly into the latent space topology without requiring equivariant network architectures, which can be computationally expensive.
- **Empirical improvements across multiple environments**: The approach consistently outperforms baselines (AWM without priors, PRAE, Rotation Matrix) on generalization metrics (H@k, MRR) and downstream RL tasks, including the high-dimensional VizDoom environment.
- **Disentanglement of symmetric and non-symmetric features**: The proposed regularization to separate structured and unstructured latent dimensions is a useful addition that enables scaling to more complex environments.

## Weaknesses

### Fatal
None.

### Major

1. **Strong reliance on prior knowledge**: The method requires knowing the type of symmetry (e.g., cyclic, torus) and which latent dimensions correspond to symmetric vs. non-symmetric features (via the mapping \(\sigma\)). This limits applicability to environments where such structure is known a priori. The paper does not discuss how to discover or approximate these structures automatically.

2. **Insufficient evaluation of disentanglement**: The paper claims that the learned representations are "simpler and more disentangled" but only provides qualitative visualizations. No quantitative disentanglement metrics (e.g., DCI, MIG, or intervention-based measures) are reported. The disentanglement loss (Eq. 11) is also not clearly explained—the notation \(|\Delta(z,a;\theta_{\text{trans}})^{\sigma(a)}|\) is ambiguous.

3. **Lack of ablation studies**: Key components (volume regularization, disentanglement loss, choice of latent dimension, effect of different group structures) are not ablated. This makes it difficult to attribute the observed improvements specifically to the geometric prior versus other regularization terms.

4. **Comparison to baselines may be unfair**: The baseline "AWM (same latent dimensionality)" uses a plain Euclidean latent space, while the proposed method uses a product of quotient spaces and Euclidean spaces. The geometric prior changes both the topology and the effective degrees of freedom. A fairer comparison would control for total latent dimension and regularization strength without the group structure.

5. **Limited scope of environments**: The experiments are on relatively simple MDPs (toy cycles, torus, MiniGrid) and a custom VizDoom scenario. Scalability to more complex tasks (e.g., continuous control, Atari, or environments with approximate symmetries) is unclear. The VizDoom experiment uses a static dataset and a small action set.

### Minor

- The description of the disentanglement loss (Eq. 11) is unclear: "\(\Delta(z,a;\theta_{\text{trans}})^{\sigma(a)}\)" is not formally defined. It appears to mean the L1 norm of the components of \(\Delta\) indexed by \(\sigma(a)\), but this should be stated explicitly.
- The downstream RL experiments freeze the world model; it would be informative to see whether fine-tuning the model during RL improves performance further.
- The paper does not discuss failure cases or limitations, e.g., when the assumed symmetry is only approximate or when multiple symmetries interact in complex ways.

### Trivial

- Some figure captions are repeated verbatim in the text (e.g., Figures 3, 4, 5, 6), which is a formatting artifact rather than a content issue.

## Nice-to-Haves

- Ablation studies on the disentanglement loss and volume regularization to isolate their contributions.
- Quantitative disentanglement metrics (e.g., DCI, MIG) on the learned latent spaces.
- Experiments on more challenging environments (e.g., Atari, DM Control) to test scalability.
- Comparison to other model-based RL methods (e.g., Dreamer, MuZero) with similar geometric priors.

## Novel Insights

The paper's core insight is that by choosing a latent space whose topology matches the symmetry group of the environment (e.g., a circle for rotations), the transition model can learn simpler, more generalizable dynamics. The combination of this topological prior with a sparsity-based disentanglement loss to separate symmetric and non-symmetric features is a practical contribution. However, the idea of using quotient spaces for cyclic symmetries is not entirely new (cf. Quessard et al., 2020), and the novelty lies primarily in the integration with contrastive world models and the explicit handling of mixed symmetric/unstructured features.

## Suggestions

- Clarify the formulation of the disentanglement loss (Eq. 11) and provide a precise definition.
- Add ablation studies to evaluate the contribution of each loss term (volume, disentanglement) and the effect of different latent dimensions.
- Report quantitative disentanglement metrics to support the claim of "simpler and more disentangled representations."
- Discuss limitations: when is the geometric prior beneficial, and when might it hurt performance (e.g., approximate or misspecified symmetries)?

## Score and Decision

The paper presents a clean method for incorporating geometric priors into abstract world models and shows empirical improvements on several environments. However, the strong reliance on prior knowledge, lack of ablation studies, and insufficient evaluation of disentanglement are significant weaknesses that limit the paper's impact and generalizability. The contribution is moderate and the paper is borderline, but the current evidence is not strong enough to warrant acceptance.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>