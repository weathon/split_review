- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper studies training dynamics of contrastive learning across three settings (a linear network, physics-inspired toy datasets, and ImageNet with a supervised contrastive loss), arguing that training proceeds through discrete "phase transitions" between qualitatively different representation topologies. The core empirical finding — a sudden, sharp transition from a "Twisted Disk" to a "Bowl" representation on the Kepler physics dataset, whose timing is controlled by augmentation robustness and which occurs without any drop in training loss — is genuinely compelling. The linear analysis shows that non-monotonic dynamics can arise even in simple settings, while the ImageNet experiments provide suggestive but less conclusive evidence.

## Strengths

- **Sudden topological phase transition cleanly demonstrated on the Kepler physics dataset (Section 3.4, Figures 4–7):** The model switches abruptly from a "Twisted Disk" to a "Bowl" representation at a critical training time. This transition is visible as a sharp jump in R², occurs without any drop in training loss, and the paper explicitly states (and shows) that the change involves a topological reconfiguration (the center of the disk has no analogue in the bowl). This is a novel and well-documented finding.

- **Augmentation robustness systematically controls transition timing (Figure 6):** The paper shows that the number of epochs until the phase transition on the Kepler dataset increases monotonically as the augmentation fraction α decreases (16 trials per setting, with confidence intervals). A similar delay is observed for the ARI jump on ImageNet (Figure 8). This provides causal evidence that augmentations accelerate phase transitions.

- **Non-monotonic dynamics are proved possible even in a linear network (Section 2, Theorem, Figure 2):** The paper derives a closed-form expression for the cosine metric showing that it is a ratio of sums of exponentials, proving that non-monotonic training dynamics arise naturally in contrastive learning but not in supervised learning (Proposition 3). This is a clean theoretical result.

- **Use of complementary metrics beyond loss (R², ARI, AMI, direct visualization):** The paper does not rely on a single metric. The R² on the physics dataset, the clustering metrics (ARI/AMI) on ImageNet, and direct 3D visualizations (Figures 5, 9) all point in the same direction, strengthening the claim that the observed changes are not artifacts of one measure.

## Weaknesses

### Fatal

None.

### Major

- **The paper's title and abstract claim phase transitions in "contrastive learning" broadly, but the ImageNet experiments use a supervised contrastive loss with non-destructive augmentations, which differs substantially from standard self-supervised SimCLR/BYOL training.** The paper says (lines 212–214) it uses "supervised contrastive losses" for the vision experiments, and explicitly forgoes "typical such as cropping, color jittering, flipping, etc." The ImageNet training setting (supervised label-dictated positives, α-quantile selection of closest positives dynamically) is far from standard SSL. The conclusion acknowledges this limitation ("extension... to more self-supervised learning methods... would be valuable"), but the title, abstract, and framing (e.g., "How do self-supervised models actually train?" and "the role of augmentations in self-supervised learning is to speed up these discrete phase transitions") present the results as applying to self-supervised contrastive learning broadly. This mismatch between the generality of the claims and the specificity of the evidence is a structural weakness.

- **The ARI/AMI discrepancy on ImageNet is not adequately explained.** The paper reports (line 240) that "the AMI does not show any sudden jumps," offering only the speculative explanation that "It may be measuring phase transitions that occur both early and late in training." No evidence is provided for this hypothesis, and the two metrics disagree on the very phenomenon (a discrete jump) that the paper claims to detect. The paper's ImageNet conclusions therefore rest entirely on one metric (ARI), whose DBSCAN hyperparameter sweep does not resolve the conceptual discrepancy with AMI. This weakens the ImageNet evidence considerably.

### Minor

- **The linear setting is described in the abstract as showing "phase transitions" (line 4), but the paper itself states "no topological phase transitions occur" in that setting (line 119) and uses the term "phase-like behavior" and "loosely."** This inconsistency in framing: the abstract overclaims for the linear setting, while the text is appropriately cautious. The linear section is valuable as a warm-up showing non-monotonic dynamics, but calling its behavior "phase transitions" in the abstract is misleading.

- **The explanation of why the Twisted Disk → Bowl transition is "topological" (not simply a nonlinear embedding learned late) rests on visual inspection and the statement that "the central point in the disk has no analogue in the bowl."** This is intuitive and probably correct, but the paper does not provide a quantitative characterization (e.g., intrinsic dimensionality, persistent homology, or a change-point detection method on the representation geometry itself) that would rule out a continuous deformation. This does not undermine the core finding (the transition is clearly sudden and important), but it limits the rigor of the topologically-distinct-phases claim.

- **The ImageNet experiments do not show the training loss curve alongside ARI, so the reader cannot directly verify the claim that the representation change occurs without a loss drop.** The paper states (as a general property) that loss decreases smoothly while representations undergo discrete transitions (Figure 1), but the ImageNet section does not present the loss trajectory. This is a presentation gap that would be easy to fill.

### Trivial

None.

## Nice-to-Haves

- Show the training loss curve alongside ARI for the ImageNet experiments.
- For the physics dataset, provide a quantitative measure of topological difference between the Twisted Disk and Bowl (e.g., comparing singular value spectra, intrinsic dimensionality, or CKA between the two representations) rather than relying solely on visual inspection.
- For the physics dataset, show that intermediate representations (during the transition window) are not simply interpolations between the two fixed points (e.g., bimodality analysis or CKA distance to each phase).

## Removed Points

These points were flagged for removal; treat them with caution.

- **"The number of conserved quantities is only 3—not obvious this scales":** This is a generic concern about toy datasets that applies to almost all scientific toy experiments. The paper explicitly uses a low-dimensional system for visualization and analytical tractability. The question of scaling to higher-dimensional latent spaces is legitimate but belongs in future work, not as a current weakness.
- **"Baseline: what happens with standard SimCLR augmentations on CIFAR-10":** The paper explicitly states its choice to use non-destructive augmentations across all settings (Section 3.2, Section 4.1). Asking for standard SSL augmentations is scope creep given the paper's stated design choice.
- **"The linear section should be dropped entirely":** This is a subjective editorial opinion, not a weakness. The linear analysis provides theoretical grounding for non-monotonic dynamics (Theorem, Proposition 3) that the paper's claims build on.
- **"Statistical rigor: show alignment across runs using Procrustes/CKA":** The paper already shows 16 independent runs with confidence intervals on transition timing (Figure 6) and R² trajectories (Figure 7). The additional request is reasonable but beyond what is standard for this type of analysis; it is a nice-to-have rather than a missing requirement.
- **"Training details (batch size 4096, LR 4.8, LARS) are atypical and could be artifacts":** Large-batch training with LARS is standard for ResNet-50 on ImageNet. The critic provides no specific reason to believe the results are artifacts of these choices. Speculative.
- **"Excluding DBSCAN outliers could artifactually inflate ARI":** Speculative without evidence. The paper conducts a hyperparameter search over ε to mitigate sensitivity.
- **"Missing related works on grokking/loss landscape geometry":** As per instructions, missing related works should not be mentioned.
- **"The paper could use persistent homology":** This is a suggestion for a different methodology, not a weakness of the current approach.

## Novel Insights

The two input reviews mostly recapitulate the paper's own observations rather than generating genuinely novel insights beyond the paper's contributions. The most useful meta-insight is this: the physics dataset experiment is strong enough to stand on its own as a compelling demonstration of phase transitions in representation learning for dynamical systems. The paper would be substantially stronger if it narrowed its scope to match its best evidence, rather than stretching its claims to cover standard self-supervised vision learning where the evidence is weaker. The ARI/AMI discrepancy on ImageNet is a genuine puzzle that the paper papered over, and resolving it would be a real contribution in itself.

## Suggestions

1. **Narrow the scope of the title and abstract** to match what is actually shown. The paper's strongest contribution is the physics dataset; consider a title like "Phase Transitions in Contrastive Representation Learning on Dynamical Systems" or explicitly qualify that the ImageNet setting uses a supervised contrastive variant.

2. **Address the ARI/AMI discrepancy directly.** Either explain why AMI does not jump (with evidence), replace it with a metric that does capture the jump, or acknowledge the ambiguity. If using ARI alone, justify why ARI is the right metric and AMI is not for this setting.

3. **Show the ImageNet training loss curve** alongside ARI in Figure 8 to directly support the claim that the representation change is not accompanied by a loss drop.

4. **Provide a quantitative characterization of the topological difference** between the Twisted Disk and Bowl (e.g., comparing the intrinsic dimensionality, or measuring distances between the two learned representations via CKA), to move beyond visual inspection.
