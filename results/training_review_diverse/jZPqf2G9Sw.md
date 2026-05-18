Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces a method for conditioning protein backbone diffusion models on dynamical properties — specifically the lowest non-trivial normal mode from Normal Mode Analysis (NMA). The key innovation is replacing a learned classifier with an analytical loss (NMA-loss) for guidance, making the approach practical without requiring eigenvector prediction networks. The authors demonstrate dynamics-only conditioning on a custom GVP-based model and joint dynamics+structure conditioning on the pretrained Genie model, using hinge targets from lysozyme, adenylate kinase, and hemoglobin. The work addresses a genuinely underexplored direction in protein design.

## Strengths

- **First approach to condition protein generative models on dynamical properties**: The paper tackles a clear gap — existing protein diffusion models condition on structure but not dynamics. The abstract states this directly ("conditioning on dynamical properties remains elusive") and the conclusion reinforces it ("For the first time, we condition the protein diffusion model on dynamics"). This novelty is genuine and well-motivated.

- **Analytical conditioning term replaces a learned model**: Instead of training a neural network to approximate \(p(y|x_t)\) (which would require predicting eigenvectors of arbitrary matrices — an unsolved problem), the paper equates this term to a simple analytical function (NMA-loss). This is stated at line 101: "We escape the need to train a neural network and equate \(p(y|x_0)\) to a simple analytical function." This design choice makes the approach computationally tractable and transferable.

- **Joint conditioning framework with theoretical grounding**: The paper extends dynamics conditioning to joint dynamics+structure conditioning (Equation 17), providing SDE-based justification. This is important because, as the paper notes (line 160), "dynamics and structure are correlated" but not identical — many structures can share similar low-frequency modes without functional packing.

- **Plug-and-play transfer to Genie without retraining**: The method is demonstrated on the pretrained Genie model by modifying only the sampling loop (consistent with standard guidance approaches). This universality is a practical strength for adoption.

- **Invariant loss function design**: The NMA-loss is constructed to be invariant to rotation and translation by comparing relative pairwise angles and relative magnitudes of displacement vectors (Section 3.2). This is a thoughtful design choice given that eigenvectors are orientation-independent and have only relative amplitude meaning.

## Weaknesses

### Fatal
None.

### Major

- **Missing designability comparison for the hinge experiments**: For the joint conditioning hinge targets, the paper reports scTM proportions for joint-conditional samples (0.48, 0.78, 0.41) and for dynamics-only samples (0.93, 1.0, 0), but does **not** report the scTM of the 27 unconditional samples (or, more crucially, structure-conditioning-only samples). Without a comparison between joint conditioning (dynamics+structure) and structure-conditioning-only, it is impossible to assess whether adding dynamics guidance degrades designability or whether the observed scTM values reflect baseline difficulty of the hinge targets. This gap undermines the claim that "conditioning does not compromise designability."

- **Computational cost and stability of NMA during sampling are not addressed**: The method requires computing the lowest normal mode of the denoised prediction at every diffusion step. The paper provides no analysis of: (a) wall-clock time per sample, (b) whether the NMA eigenvectors computed on noisy early-step predictions are stable or physically meaningful, or (c) whether guidance should be restricted to later sampling steps. While the paper mentions using a coarse-grained Cα representation (line 88), which partially addresses implementation specifics, the broader practical concerns remain unaddressed. If the method requires O(N³) diagonalization per step on unreliable intermediate structures, its practical utility is questionable.

- **Small sample sizes for the flagship hinge demonstration**: The hinge results rest on only 27 joint-conditional samples across three targets (≈9 per target) after filtering. The scTM proportions vary widely across targets (0.41–0.78), and with 9 samples per target the confidence intervals are large. The paper should either increase the sample size or explicitly frame the hinge results as preliminary/exploratory.

### Minor

- **Guidance scale selection unexplained**: The guidance scales are reported as "in the order of 2000–3000" (line 211), which is several orders of magnitude larger than typical classifier guidance scales. The paper does not explain why such large scales are needed, how they were chosen for each target, or whether the results are sensitive to this choice. This is a practical reproducibility concern.

- **No ablation of NMA-loss components**: The NMA-loss combines an angle term and an amplitude term (with the amplitude term weighted by 2). The paper does not ablate these components or test whether the angle term alone is sufficient. Given that eigenvector magnitudes are only meaningful up to a mode-wide scaling, it would be informative to know whether the amplitude term contributes meaningfully or whether it is redundant.

- **Presentation of the theoretical derivation could be cleaner**: The derivation from Equation 7 to Equation 14 follows the standard reconstruction guidance framework (Chung et al., 2022a) but re-derives it in a way that may cause confusion. Specifically, the introduction and subsequent cancellation of \(p(\mathbb{E}[x_0|x_t])\) in the fraction (Equation 14) is formally correct but the text does not clearly acknowledge the approximation being made or directly connect to the existing reconstruction guidance literature. This is a presentation issue, not a correctness issue.

### Trivial
None.

## Nice-to-Haves

- **Dynamics-only conditioning on Genie without structure conditioning**: Showing NMA-loss distributions for Genie conditional samples (analogous to Figure 2 but for Genie) would strengthen the transferability claim beyond just the three hinge targets.
- **Ablation of guidance start step**: Testing whether dynamics guidance applied only in the last ~50 steps produces similar NMA-loss would address the practical concern about noisy early predictions.
- **Wider range of hinge targets or increased sample size per target** would improve statistical reliability.

## Removed Points

- The critic's claim that the paper "does not mention whether the NMA is performed on the full backbone or a coarse-grained representation" is inaccurate — line 88 explicitly states: "We use a coarse-grained protein representation, where each residue is represented with the Cα carbon only." This detail is removed from the computational-cost weakness, though the broader concern about cost/stability remains justified.

- The critic's note that the method is "not plug-and-play in the sense of requiring no modifications to the sampling loop" is technically true but standard for all guidance-based methods and does not constitute a meaningful weakness. It is removed.

- The critic's suggestion that "results from the two models are not directly comparable" is a feature of the experimental design, not a flaw — the GVP model is used for large-scale dynamics validation (300 targets) and Genie for the hinge demonstration, which is a reasonable two-pronged strategy. Removed.

## Novel Insights

The most insightful observation across the reviews is that the paper's core technical innovation — using an analytical NMA-loss in place of a learned classifier for guidance — simultaneously solves two problems: (1) it avoids training an eigenvector prediction network, which the paper correctly notes is an unsolved problem for variable-size matrices, and (2) it makes the conditioning plug-and-play for pretrained models since no additional training data or labels are needed. This is a genuinely elegant design choice that future work on dynamics-aware protein design will likely build on. The trade-off is that this choice places the entire computational burden of NMA (Hessian construction + diagonalization) on the sampling loop, and the paper's evaluation does not adequately characterize whether this trade-off is acceptable. The hinge demonstration is compelling as a proof-of-concept but the evidence base is too thin (27 samples, 3 targets, missing baselines) to support strong claims about designability preservation.

## Suggestions

1. **Provide the missing designability baseline**: Report scTM for Genie samples conditioned on structure only (no dynamics guidance) for the same hinge targets, and compare to the joint-conditioning scTM. This is the single most important experiment to add.

2. **Add computational profiling**: Report average wall-clock time per sample for the Genie experiments and describe the NMA implementation (elastic network model parameters, number of neighbors, whether eigenvalue decomposition is done at every step or can be amortized).

3. **Analyze NMA stability across the diffusion trajectory**: Show how the NMA-loss and eigenvectors of the denoised prediction evolve with sampling step t (e.g., early vs. late steps) to demonstrate that guidance on noisy structures is stable and meaningful.

4. **Ablate and discuss guidance scale**: Provide a sensitivity analysis for the guidance scale (1–2 orders of magnitude) and explain why values of 2000–3000 are required.

5. **Increase hinge sample size or reframe claims**: Either generate more samples per target to enable reliable statistics, or explicitly caveat the hinge results as preliminary proof-of-concept.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>