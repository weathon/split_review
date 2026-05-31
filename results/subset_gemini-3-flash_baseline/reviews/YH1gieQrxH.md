## Summary
The paper proposes a framework for incorporating geometric priors into abstract world models by structuring the latent space as a product of quotient spaces (e.g., $\mathbb{R}/k\mathbb{Z}$) and Euclidean spaces. By modeling transitions as additive group actions within these structured manifolds and employing a sparsity-based disentanglement loss, the method allows agents to learn representations that separate symmetric features (like rotation) from non-symmetric features (like spatial position). The authors demonstrate that this approach improves transition prediction accuracy, generalization to unseen state-action pairs, and downstream reinforcement learning performance in environments ranging from simple grid-worlds to first-person 3D views in VizDoom.

## Strengths
- **Principled Integration of Priors:** The method provides a clean way to incorporate known symmetries (cyclic/rotational) without requiring the heavy computational machinery of equivariant neural networks. Using quotient spaces as the latent manifold is a mathematically sound approach to modeling periodic dynamics.
- **Handling Mixed Dynamics:** A significant strength is the ability to combine structured (symmetric) and unstructured (non-symmetric) features. Most prior work in equivariant RL assumes the entire state follows a specific group action; this paper successfully addresses the more realistic scenario where only parts of the state are symmetric.
- **Empirical Breadth:** The experiments cover a good spectrum, from toy MDPs (Passage, Torus) to complex high-dimensional visual inputs (VizDoom). The visualization of the learned latent spaces (Figures 5 and 6) provides strong evidence that the model actually recovers the intended geometric structure.
- **Generalization Benefits:** The paper convincingly shows that geometric priors act as a powerful regularizer, preventing the "latent collapse" or overfitting common in unstructured world models when data is sparse (Table 1 and Figure 7).

## Weaknesses
### Fatal
None.

### Major
- **Action-Latent Mapping ($\sigma$):** The disentanglement mechanism relies on a mapping $\sigma$ that specifies which latent coordinates are affected by which actions. In the current formulation, this appears to be a piece of prior knowledge provided to the model. While the paper argues this is a "prior," in complex environments, knowing exactly which dimensions of a learned latent space should be invariant to which actions is a strong assumption that limits the "autonomy" of the representation learning.
- **Scalability of Manifold Choice:** The user must manually specify the structure of $\mathcal{Z}$ (e.g., how many cyclic components vs. Euclidean components). While the paper shows this works for $E(2)$ and $E(3)$ symmetries, it is unclear how the method would perform if the prior was slightly misspecified (e.g., assuming a torus when the environment is a bounded grid).

### Minor
- **Baselines:** While the comparison to PRAE and Quessard et al. (2020) is valuable, the paper would benefit from comparing against more recent "standard" world models like DreamerV3, even if those models use much higher dimensionality, to contextualize the "minimalist" representation benefit.
- **Hyperparameter Sensitivity:** The volume regularization threshold $w$ and the disentanglement loss weight are likely crucial for the "interpretability" shown in the figures, but there is little discussion on how sensitive the results are to these values.

## Nice-to-Haves
- An ablation study on the disentanglement loss ($\mathcal{L}_{\text{disentanglement}}$) to see if the group-structured latent space alone is sufficient to encourage separation, or if the explicit sparsity constraint is the primary driver.
- Discussion on whether the value of $k$ in $\mathbb{R}/k\mathbb{Z}$ needs to be tuned or if the encoder simply scales its outputs to match whatever $k$ is provided.

## Novel Insights
The primary novel insight is the demonstration that complex, high-dimensional first-person 3D dynamics (VizDoom) can be decomposed into a very low-dimensional (3D) latent space by explicitly partitioning the manifold into a quotient space for rotation and a Euclidean space for translation. Unlike previous work that uses rotation matrices or complex equivariant layers, this paper shows that simply defining the latent space's topology and using a standard additive transition model is sufficient to capture these symmetries, provided a disentanglement loss is used to steer the features.

## Suggestions
- Clarify in the methodology section how much "manual" intervention is required to define $\sigma(a)$. Is it hardcoded based on the environment's known physics, or is there a heuristic used?
- Provide a brief analysis of the failure modes when the geometric prior does not perfectly match the environment (e.g., applying a cyclic prior to a non-periodic "Passage" environment).

## Score and Decision
The paper is a solid contribution to the field of structured representation learning in RL. It addresses a practical gap (mixing symmetric and non-symmetric features) with a technically sound and empirically validated approach.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>