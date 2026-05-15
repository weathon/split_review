Now I have a thorough understanding of the paper and can verify each claim. Let me construct the final consolidated review.

## Summary

The paper proposes ReViWo, a framework that decomposes visual observations into view-invariant (VIR) and view-dependent (VDR) representations via a two-encoder autoencoder trained on multi-view data. The VIR is then used as the state representation for world model training and offline RL policy learning. Experiments in Meta-world and PandaGym simulations show substantial robustness gains over VAE-based baselines under camera installation shifts and camera shaking, with a preliminary real-world evaluation on ALOHA. The core technical idea — cross-reconstruction that forces the VIE to encode only state information while the VDE encodes viewpoint — is clean and well-motivated.

## Strengths

- **Explicit architectural decomposition of visual observations into view-invariant and view-dependent representations.** The two-encoder design with cross-reconstruction (combining VIE output from one image with VDE output from a different image to reconstruct a target image at a novel viewpoint) provides a clear, principle-driven training signal for disentanglement. This is a concrete architectural advance over prior methods like MVWM, which use a single encoder.

- **Consistent and large-margin superiority over baselines across multiple simulation environments and two distinct viewpoint disturbance types.** On Meta-world tasks, ReViWo retains >80% success under CIP where COMBO drops to 0% (Door Open, Drawer Open); on Window Close under CIP, ReViWo achieves >80% vs COMBO's 22.8%. Under camera shaking, ReViWo similarly maintains performance while baselines collapse. These results are presented with error bars over 3-4 seeds, providing reasonable confidence in the trends.

- **Decoder cross-reconstruction (Fig. 7) provides interpretable, non-quantitative confirmation that the decomposition works.** The decoder generates images combining the task state from one input with the viewpoint from another, and the results match ground truth well. This goes beyond typical latent-space evaluations and directly visualizes what each encoder has captured.

- **Analysis of data requirements (Fig. 5) gives practical deployment guidance.** Training with only 10 viewpoints over a 90° azimuth range achieves comparable performance to 20 viewpoints over 180° for offsets ≤10°, suggesting the method is data-efficient.

- **Ablation showing VIR is beneficial even without the world model (Tab. 3).** ReViWo w/o WM (CQL + VIR) still outperforms COMBO (model-based + VAE), isolating the benefit of the representation itself.

## Weaknesses

### Fatal
None.

### Major

- **The contrastive loss term L_Contrastive in Eq. (3) is described textually but never given a mathematical formulation.** The paper states it "encourages z_s to remain consistent across identical states and varies across different states" and analogously for z_v, but no explicit loss function, sampling procedure, or hyperparameter value (λ₂) is provided. Because this term is claimed to be part of the training objective that enforces representation separation, the method as described is not fully reproducible. While the cross-reconstruction loss alone likely drives most of the disentanglement, readers cannot verify whether or how this auxiliary term contributes.

### Minor

- **Handling of unlabeled Open X-Embodiment data is underspecified.** The paper states "we introduce a weighting factor in the loss calculation for these unlabeled data" (line 83) but never specifies what this factor is, how it is chosen, or how training differs for labeled vs. unlabeled examples. Given that the core training signal depends on view labels for cross-reconstruction, the treatment of label-free data is important for reproducibility.

- **The real-world evaluation (Tab. 1) is preliminary and does not test the full ReViWo pipeline.** It uses only a behavior-cloning variant (ReViWo-BC), a single task (bottle to plate), 10 trajectories per condition, a modest viewpoint shift (±15°), and compares to ACT (an end-to-end imitation learning method, not a representation-learning baseline). The paper appropriately calls this "preliminary evidence," but the real-world results do not directly support the paper's core claim about world-model-based RL under viewpoint disturbance.

- **Missing controlled comparison: CQL+VAE vs. CQL+VIR (ReViWo w/o WM).** In Tab. 3, ReViWo w/o WM (CQL + VIR) is compared to COMBO (model-based + VAE). This confounds the representation change (VIR vs. VAE) with the RL algorithm change (CQL vs. COMBO). While the comparison is reasonable and the conclusion likely holds, a cleaner ablation would hold the RL algorithm fixed.

- **The t-SNE analysis (Fig. 6) is qualitative.** No quantitative cluster compactness metric (e.g., silhouette score, intra-class / inter-class distance ratio) is reported. The visual clustering is compelling but a numeric comparison would strengthen the claim.

- **Camera configuration details for simulation data collection are partially unspecified.** The paper mentions "20 cameras from different viewpoints" but does not fully specify the exact azimuth/pitch ranges or whether viewpoints are absolute positions or relative offsets. A reference to "1 for the detailed setup" suggests these details may have been in a stripped appendix.

### Trivial
- The claim that "ReViWo achieves the highest performance on the training viewpoint for certain tasks" with the hypothesis that "VIR masks unrelated information" is not experimentally tested — but it is clearly presented as a hypothesis ("we hypothesize"), not a conclusion.
- The typo "Contrasive" for "Contrastive" in Eq. (3) — but this is a parser artifact.

## Nice-to-Haves
- Quantitative cluster compactness metric for the VIR t-SNE analysis.
- Evaluation of VDR quality (e.g., train a viewpoint classifier on VDR and measure accuracy).
- Statistical significance tests (e.g., bootstrap tests) for the main comparisons in Fig. 4 where error bars overlap.
- Analysis of which image patches the VIE attends to (attention maps) to support the claim that it ignores viewpoint-specific content.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"positional embeddings … computed using the function (1−timestep) appears to be a parsing artifact"** — REMOVED per hard rules (formatting/parser artifact).
- **"does not compare to MVWM in any controlled ablation that isolates the encoder architecture"** — REMOVED; the paper compares to MVWM as a full method, which is the relevant evaluation. Demanding an encoder-only ablation is scope creep beyond what the paper aims to show.
- **Claim that COMBO comparison is "not a multi-view or representation-learning method"** — REMOVED; ACT is indeed a different class of method (end-to-end BC), but the real-world experiment is presented as preliminary evidence, not a comprehensive benchmark. The reviewer misinterprets the scope of this experiment.
- **The criticism about lack of statistical significance tests for Fig. 4** — REMOVED; error bars over 3-4 seeds are standard practice in this field.
- **"the paper does not clearly describe how these labels were obtained"** — PARTIALLY REMOVED; the paper states labels come from fixed-position cameras. The specific camera positions are referenced as "1 for the detailed setup," suggesting appendix content was stripped. The remaining concern about camera configuration specificity is kept as a minor weakness.
- **The claim that the paper should "Release the code and hyperparameters"** — REMOVED; demanding complete code release is outside standard review expectations for a conference paper.
- **Strength Finder Point about "consistent and large-margin superiority" being supported by "real-world settings"** — WEAKENED; the real-world evaluation uses ReViWo-BC, not the full pipeline, so I moved this to note the distinction.
- **"Policy rollout visualizations under camera shaking"** — REMOVED; demand for additional supplementary visualizations is a nice-to-have, not a weakness.

## Novel Insights
The reviews reveal an interesting tension: the paper's core strength (the cross-reconstruction training objective) is also the source of its main weakness (the contrastive loss is underspecified). The reviewers converge on the fact that the cross-reconstruction loss itself likely does most of the disentanglement work, making the undefined contrastive term less critical than it might appear. A potentially productive direction not discussed in the paper is whether the contrastive loss is even necessary — an ablation removing it entirely would both strengthen the method and resolve the specification gap. Additionally, the consistent pattern across experiments (VIR helps, world model helps further) suggests the representation quality is the primary driver of robustness, with the world model providing secondary gains through imaginary rollouts.

## Suggestions
1. **Specify the contrastive loss formulation** — provide the exact equation, sampling procedure, and λ₂ value. Alternatively, remove it entirely and show that the cross-reconstruction + VQ losses are sufficient.
2. **Specify the weighting factor and procedure for unlabeled Open X-Embodiment data** — this is critical for reproducibility.
3. **Add the controlled comparison: CQL (or COMBO) with VAE vs. with VIR** to fully isolate the effect of the representation from the RL algorithm.
4. **Run the full ReViWo pipeline (world model + RL) on the real-world ALOHA setup**, even if with limited trajectories, to directly support the paper's central claim about world-model-based RL.
5. **Add a quantitative cluster metric** (e.g., silhouette score) to the t-SNE analysis.

## Score and Decision

**Originality:** Good. The decomposition into two encoders with cross-reconstruction is a principled advance over prior single-encoder approaches.  
**Importance of research question:** High. Viewpoint robustness is a practical bottleneck for deploying learned policies on real robots.  
**Claims support:** Partially. The simulation results strongly support the core claims. The real-world results are preliminary. The contrastive loss being undefined partially undermines the method description.  
**Soundness of experiments:** Reasonably sound in simulation. Missing one controlled comparison (same RL algorithm, different representation). Analysis is qualitative but compelling.  
**Clarity of writing:** Good overall, but underspecified in two places (contrastive loss, unlabeled data weighting).  
**Value to community:** Potentially high. The approach is practical and the simulation results are strong. Once the specification issues are resolved, this would be a useful method.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>