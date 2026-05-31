## Summary
This paper proposes a method to impose geometric priors on the latent space of learned world models for reinforcement learning. By modeling the abstract state space as a quotient space (e.g., \(\mathbb{R}/k\mathbb{Z}\)) and using additive group actions for transitions, the method encodes known symmetries such as rotations. The framework also supports combining these structured features with unstructured ones via a sparsity-based disentanglement regularizer. Experiments on Passage, Torus, MiniGrid, and VizDoom show improved generalization in transition prediction and better downstream RL performance compared to unstructured baselines.

## Strengths
- **Clear motivation and intuitive idea.** The paper makes a compelling case for encoding known symmetric structures directly into the geometry of the latent space rather than relying on equivariant network architectures. The toy examples (Passage, Torus) clearly illustrate the benefit of such priors.
- **Demonstrated gains in generalization and RL.** The quantitative results (Table 1, Figure 4, Figure 7) show consistent improvement in Mean Reciprocal Rank and Hits@k when geometric priors are used, and the downstream RL experiments (Figure 8) indicate that these representations can be effectively leveraged for task learning.
- **Addresses a practical challenge.** The ability to handle both symmetric and non-symmetric features in the same latent space (e.g., orientation vs. position in MiniGrid, rotation vs. spatial coordinates in VizDoom) is an important step toward applying geometric priors to more realistic environments.
- **Well-structured presentation.** The paper is logically organized, the background is sufficient, and the figures (especially the torus visualizations) help convey the core ideas.

## Weaknesses
### Major
1. **Strong assumption about action-to-coordinate mapping \(\sigma\).**  
   The disentanglement loss (Eq. 11) requires a known mapping \(\sigma: \mathcal{A} \to \mathcal{I}\) that specifies which latent coordinates should *not* be affected by each action. The paper does not discuss how this mapping is obtained in practice, nor does it consider scenarios where such a mapping is unknown or ambiguous. This significantly limits applicability—the method essentially requires the modeller to pre-specify which dimensions capture symmetric vs. non-symmetric features.

2. **Potentially unfair baseline comparison.**  
   The unstructured baseline (AWM without priors) uses the same latent dimensionality as the structured model (e.g., 3 dimensions for VizDoom). Because the structured model is explicitly tailored to the environment’s symmetries, this comparison conflates the effect of the prior with the effect of having a latent space whose geometry is insufficient for the unstructured model to represent the dynamics. The claim that the method “outperforms [baselines] with greater representation power” is not supported by any experiment—no results with larger latent dimensions for the unstructured baseline are shown.

3. **Lack of ablation on key components.**  
   The framework includes a disentanglement loss (Eq. 11), a volume regularizer (Eq. 7), and a contrastive loss. The paper does not ablate these components to understand their individual contributions. For example, is the disentanglement loss necessary, or does the prior alone (choice of latent space) suffice? How sensitive are results to the threshold \(w\) in the volume loss?

4. **Incomplete specification of the VizDoom experiment.**  
   The paper states that a “variation of the InfoNCE loss” is used for VizDoom, but the details are omitted (the appendix is not available). This makes the experiment difficult to reproduce or fully evaluate.

### Minor
- **Equation 11 is ambiguous.**  \(|\Delta(z,a)^{\sigma(a)}|\)  likely denotes the L1 norm of the subvector indexed by \(\sigma(a)\), but the notation is not clarified.  
- **The overall loss in Eq. 8 does not include the disentanglement loss.** It is unclear whether \(\mathcal{L}_{\text{disentanglement}}\) is used in all experiments or only some.  
- **The volume hinge loss (Eq. 7) is introduced but its role is not discussed in the experimental analysis.**  
- **The paper claims “no alteration of training objectives or network architectures”**, yet the latent space itself is changed (e.g., modular arithmetic vs. Euclidean space) and the transition model uses \(\oplus\) that depends on the geometry. This claim is misleading.

## Nice-to-Haves
- An experiment where \(\sigma\) is learned or where the mapping is mis-specified would strengthen the paper.  
- A comparison against an unstructured baseline with a larger latent dimension (e.g., 10–20) would clarify whether the gains come from the prior or from the compactness.  
- Testing on environments with approximate or partial symmetries (e.g., noisy rotations) would provide insight into robustness.

## Novel Insights
None beyond the paper’s own contributions.

## Suggestions
- Clarify the role of \(\sigma\): is it given a priori or can it be derived from the environment? Provide guidelines for practitioners.  
- Add an ablation study: measure performance without the disentanglement loss, and vary the latent dimension for the unstructured baseline.  
- Include the VizDoom loss formulation in the main text or ensure the appendix is accessible.

## Score and Decision
The paper addresses an important problem and shows promising results, but the reliance on a known action-to-coordinate mapping and the incomplete baseline comparison are significant weaknesses that limit the impact. The contribution is incremental over prior work (e.g., Quessard et al., Park et al.) and the experiments are not sufficiently convincing to recommend strong acceptance.

MY FINAL SCORE: <score>5</score>  
MY FINAL DECISION: <decision>Reject</decision>