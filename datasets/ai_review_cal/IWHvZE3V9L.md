- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have all the information needed. Let me write the consolidated review.

## Summary

ProPicker introduces a promptable 3D segmentation model for particle picking in cryo-ET. The method uses a frozen TomoTwin encoder to extract a 32-dimensional feature vector from a user-provided sub-tomogram prompt, then conditions a 3D U-Net on this vector to segment only the desired particle type. The key contributions are: (1) a favorable speed-performance trade-off (5–10× faster than TomoTwin with comparable F1 scores), (2) generalization to unseen particles from a single prompt, and (3) data-efficient fine-tuning for new particles.

## Strengths

- **Large speed advantage with maintained accuracy.** Figure 2 shows ProPicker-C (stride 32) matches TomoTwin (stride 4) in F1 across 100 particles while being >5× faster; ProPicker-TM (stride 56) achieves a 10× speedup with minimal performance loss. This is the paper's strongest empirical result.

- **Generalization to unseen particles on par with TomoTwin.** Table 1 reports best-case F1 scores for 8 held-out particles. ProPicker-C (s=32) performs on par with TomoTwin (s=2) across all particles, supporting the universality claim.

- **Data-efficient fine-tuning outperforms specialist pickers.** Figure 5 shows that fine-tuning ProPicker-C on a single tomogram (~150 instances) yields higher F1 scores than DeepFinder trained from scratch on the same data, in both single-class and multi-class settings.

- **Real-world tomogram generalization without domain-specific training.** On EMPIAR 10988 (crowded cellular ribosomes), ProPicker-C achieves an F1 of 0.61, matching TomoTwin's 0.60, despite training exclusively on synthetic data.

## Weaknesses

### Fatal
None.

### Major

- **Conditioning mechanism is never specified.** The paper's core architectural contribution is a "promptable segmentation architecture that uses a conditioning mechanism to control the type of particle to be segmented" (Section 1), and later states "only fine-tune the segmentation model and the prompt conditioning mechanism" (Section 4.2). Yet the paper never describes *how* the 32-dimensional prompt feature vector $\mathbf{z}_p$ is injected into the 3D U-Net. Standard options (concatenation with bottleneck features, FiLM modulation, cross-attention) have very different implications for expressiveness, training dynamics, and parameter count. This omission prevents full reproducibility and leaves the reader unable to evaluate the central technical design choice. The description "$y = S(x; z_p)$" (Section 3.1) is merely a notational convention, not a mechanism specification.

### Minor

- **Real-world validation is thin.** The claim that ProPicker "can generalize to unseen real-world tomograms" (Contribution 3) rests on one quantitative F1 score (0.61 on EMPIAR 10988) and qualitative examples on EMPIAR 10045. Although the paper acknowledges limitations (Section 5), the gap between the strength of the claim and the evidence is noticeable. A small quantitative breakdown across multiple real tomograms would significantly strengthen the case.

- **Unseen-particle experiments share the simulation distribution.** The 8 unseen particles in Section 4.1.2 are generated with the same simulator as the training data. While this tests generalization to new *particle identities*, it does not probe distribution shift in acquisition conditions (noise model, resolution, artifacts). The scope is reasonable for a first step, but the paper could be more explicit about this limitation.

- **CryoSAM comparison is evaluated on different data.** CryoSAM is tested on clean ground-truth tomograms because it "is unable to handle noisy tomograms" (Section 4.1.2), while ProPicker and TomoTwin are evaluated on noisy tomograms. The authors are transparent about this choice in the text, but Table 1 presents all scores side-by-side without a visual indicator of this asymmetry. This could mislead a casual reader into overestimating the performance gap.

- **No variance or confidence intervals in key figures.** Figures 2 and 5 report medians/means across particles but do not show variance. Given that performance varies substantially across particle types (evident from the spread in Figure 2), reporting variability would strengthen interpretation of the aggregate claims.

### Trivial
None.

## Nice-to-Haves
- An ablation study comparing frozen vs. fine-tuned prompt encoder would clarify whether the prompt encoder is a bottleneck for generalization.
- An ablation quantifying sensitivity to Gaussian denoising strength (used for real-world tomograms) would help practitioners apply the method correctly.
- The relationship between the "up to 10× faster" figure in the abstract and the specific configuration (ProPicker-TM at stride 56, not default ProPicker-C) could be stated more precisely to avoid overgeneralization.

## Removed Points

These points were considered and removed; treat with caution:

1. **Prompt encoder details insufficient** (Harsh Critic): The critic objects that the TomoTwin encoder architecture is not fully described. The paper cites Rice et al. (2023) for the encoder, which is standard practice for a frozen off-the-shelf component. Readers can consult the cited paper for architecture specifics. **Removed:** standard citation practice.

2. **Learning rate 0.01 seems unusually high** (Harsh Critic): The critic acknowledges "this is not necessarily a flaw." This is a non-critical observation without evidence that it harms results. **Removed:** speculation without demonstrated impact.

3. **Figure 2 y-axis missing units** (Harsh Critic): The text explicitly states throughput in "tomograms per hour" (Section 4.1.1). Any figure rendering issues are parser artifacts. **Removed:** parser artifact / not a paper problem.

4. **Prompt extraction in practice** (Harsh Critic): Suggests an automated prompt extraction heuristic for fully automated workflows. This is outside the paper's stated scope (manual prompt extraction per Section 3.2, Step 1). **Removed:** scope creep.

5. **Additional baseline for fine-tuning** (Harsh Critic): Suggests fine-tuning TomoTwin itself. The paper already notes "it is not straightforward how to fine-tune TomoTwin" (Section 4.2). The critic's suggestion to "acknowledge more clearly" is already adequately addressed. **Removed:** already acknowledged.

6. **Strength: "Hybrid ProPicker-TM preserves accuracy while speeding up template matching"** (Strength Finder): Redundant with the main speed-strength and adds no new evidence beyond what is already captured in Strength #1. **Removed:** duplicative.

7. **Strength: "Real-world tomogram generalization without domain-specific training"** (Strength Finder - rephrased as supporting strength): This was kept as a core strength above (Strength #4). **Kept in main review.**

## Novel Insights

The most interesting observation spanning both reviews is that the conditioning mechanism—the core of the promptable architecture—is entirely undisclosed, yet the empirical pipeline (TomoTwin encoder → 3D U-Net → clustering/TM) still produces coherent, reproducible-looking results. This suggests that either the conditioning mechanism design space is wide enough that many choices work, or the prompt vector's role is simpler than implied (e.g., concatenation at the bottleneck). This tension between the claimed architectural novelty and the absence of its description is the review's most salient signal. Beyond this, no genuinely novel insight emerges beyond the paper's own contributions.

## Suggestions

1. **Specify the conditioning mechanism in full.** Provide the exact architectural details of how $\mathbf{z}_p$ (dimension 32) is injected into the 3D U-Net (concatenation layer, FiLM parameters, cross-attention, etc.). If this is a simple operation, state it plainly; the omission currently reads as an oversight rather than intentional concealment.

2. **Expand real-world evaluation.** Add quantitative F1 scores for EMPIAR 10045 (if annotations exist or can be approximated), or for additional EMPIAR entries where ground truth is available. Even a small table with per-dataset F1 scores would substantially strengthen Contribution 3.

3. **Clearly flag the CryoSAM asymmetry in Table 1.** Add a footnote or separate column indicating that CryoSAM's scores are on clean (noise-free) data while all others are on noisy data, to prevent misinterpretation.

4. **Add error bars or per-particle variance** to Figures 2 and 5 to help readers calibrate the reliability of the reported aggregate metrics.
