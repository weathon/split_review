## Summary
The paper proposes MH-f-POVI, a method that replaces full deep ensembles (each member a separate network) with a single multi-headed network sharing a base feature extractor, where each head acts as a particle in function-space particle-based variational inference. This reduces the parameter overhead from 5× (for a 5-member ensemble) to just ~2% additional parameters. The method is evaluated on OOD detection, calibration under covariate shift (CIFAR10C/100C), and aleatoric/epistemic uncertainty disentanglement, achieving competitive or superior results versus deep ensembles and DDU on several metrics.

## Strengths
- **Quantified parameter efficiency (2% vs 5×)**: The paper provides concrete parameter counts showing the multi-headed architecture adds only ~2% parameters over a single network, versus 5× for a 5-member deep ensemble (line 132, Table 1). This is the paper's central practical claim and is well-supported by numbers.
- **Ablation proves repulsion loss is necessary**: Figure 3 cleanly demonstrates that MH-f-POVI (with function-space repulsion) separates ambiguous MNIST (high aleatoric) from Fashion-MNIST OOD (high epistemic), while MH-POVI (without repulsion) collapses both into aleatoric uncertainty. This directly validates that the repulsion term, not just the multi-head architecture, drives the desired behavior.
- **Competitive OOD detection on CIFAR100**: On the challenging 100-class setting, MH-f-POVI with shuffled-patch context points achieves the best SVHN detection AUROC, "even outperforming full deep ensembles" (Section 5.2, line 151), despite using far fewer parameters.
- **Retrospective uncertainty for pre-trained networks**: The method can retrofit calibrated uncertainty onto an already-trained base network by only training the repulsive heads on a frozen feature extractor (Section 3, lines 77-78). This separation is a genuine practical innovation over prior function-space methods that required joint training of full ensembles.
- **Robust calibration under shift where DDU fails**: On CIFAR10C/100C, MH-f-POVI achieves competitive AUROC for detecting incorrect predictions under covariate shift, while DDU yields "the worst AUROC values" (Section 5.3, lines 161-162, Figure 4), directly addressing a known limitation of density-based DUMs (Postels et al., 2021).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Computational cost claim rests only on parameter counts**: The paper frames "significantly reduced compute" (abstract, conclusion) as a core advantage, but provides no training/inference wall-clock time, FLOPs, or GPU-hour measurements. Parameter count supports storage efficiency, but the O(n²B) repulsion computation during training and the need to evaluate 20 heads per input during inference are unmeasured. The claim is plausible (shared base + small heads is architecturally cheaper than 5 full networks) but the evidence is incomplete. (Table 1, line 132; line 168)
- **Active learning results are asserted without supporting evidence**: The abstract and contributions list active learning as a demonstrated capability, but the experiment is dispatched in a single sentence (line 134) with no figure, table, or numeric results. This is a stated empirical claim that is not substantiated in the paper.
- **Context point selection is a practical vulnerability**: Performance varies substantially across context point choices (KMNIST vs. PATCHES vs. NOISE on DirtyMNIST; CIFAR100 vs. patches on CIFAR10/100; random patches work best for CIFAR100). The paper acknowledges this variation but offers no principled guidance for selecting context points on a novel task. A practitioner faces an open design question. (Section 3, lines 80-81; Tables 1-2)
- **No ablation on number of heads**: All experiments use 20 heads without testing performance with 5, 10, or 30 heads. This directly relates to the claimed efficiency-diversity trade-off and would strengthen practical recommendations.
- **Missing DUM baselines**: The paper compares against only DDU as a DUM representative but does not evaluate orthonormal certificates (Tagasovska & Lopez-Paz, 2019) or SNGP (Liu et al., 2020), which the related work identifies as "close to our approach" (line 93). Comparisons against these would more directly test whether the function-space repulsion mechanism adds value over other non-ensemble architectures.

### Trivial
- **Bi-Lipschitz framing is slightly imprecise**: The abstract states the "multi-headed neural network" is regularized to preserve bi-Lipschitz conditions (line 4), but the bi-Lipschitz regularization (spectral normalization) is applied only to the base network, not to the heads (lines 78-79). The statement is technically correct (the base network is part of the multi-headed network), but could be read as implying the heads are also bi-Lipschitz constrained.

## Nice-to-Haves
- Evaluate retrospective uncertainties on a base network trained without spectral normalization to test generality.
- Include a comparison against function-space SVGD with deep ensembles (Wang et al., 2019), the direct predecessor of this work.
- Report sensitivity to the repulsion kernel choice (Laplacian vs. RBF vs. MMD).
- Provide code to support reproducibility, especially given the practical nature of the contribution.

## Removed Points
These points were flagged by the reviewers but removed after cross-checking against the paper:
- **"Evaluation against DUMs is strategically narrow because DDU is known to fail"**: The paper explicitly acknowledges this limitation (line 161, citing Postels et al.) and uses DDU as a representative baseline to show its method does not share this weakness. This is a valid experimental design, not a flaw. The narrower suggestion (add more DUM baselines) is retained as a minor weakness above.
- **"Synthetic data comparison against unregularized deep ensembles, not SVGD-based"**: The synthetic experiments (Figure 1) are illustrative; the main empirical evaluation uses proper baselines including deep ensembles and DDU. This is a scope choice, not a flaw.
- **"No theoretical rationale for negative data augmentation"**: The paper provides a practical motivation (random patch shuffling creates off-manifold context points). A full theoretical treatment is not standard for this type of empirical contribution.
- **General concerns about proxy metrics, speculative fatal claims, formatting/style nitpicks, reproducibility about code/large artifacts**: These lack specific anchors in the paper or reflect parser artifacts, not author errors.

## Novel Insights
None beyond the paper's own contributions. The key insight — that function-space particles only need diversity in function space, not in parameter space, enabling a shared base network with multiple heads — is clearly articulated and empirically validated. The paper correctly identifies and addresses the limitation of prior work (D'Angelo & Fortuin, 2021) that used training data as context points, and the negative data augmentation strategy for generating context points is a practically useful innovation.

## Suggestions
1. Provide training/inference time comparisons (wall-clock, FLOPs) to substantiate the computational efficiency claim.
2. Either add quantitative active learning results or remove active learning from the contributions list.
3. Ablate the number of heads (5, 10, 20, 30) to guide practitioner choices.
4. Include at least one additional DUM baseline (orthonormal certificates or SNGP) to broaden the comparison.
5. Propose heuristic guidelines for context point selection on new tasks.

## Score and Decision
MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>