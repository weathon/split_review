- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 5, 5, 5
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper proposes UniVoxel, a unified voxelization framework for inverse rendering that jointly learns geometry (SDF), materials (albedo, roughness), and illumination (local Spherical Gaussians) from multi-view images. The key design is encoding a scene into two explicit voxel grids (SDF field and semantic field), from which all scene properties are decoded by lightweight 3-layer MLPs, avoiding the deep implicit networks and multi-bounce ray tracing used by prior methods. This reduces per-scene training from hours/days to ~18 minutes while maintaining or exceeding reconstruction quality.

## Strengths

- **Dramatic and well-evidenced speedup:** The paper reports per-scene training of 18 minutes (0.3 hours) vs. MII at 12 hours (40× faster) and Nvdiffrec-mc at 4 hours (12× faster), with all baselines timed on the same RTX 3090. This efficiency claim is the paper's central contribution and is convincingly supported.

- **Novel illumination modeling via local Spherical Gaussians:** Rather than using environment maps (which require expensive multi-bounce ray tracing for visibility), the paper learns per-point SG parameters from the voxelized semantic field via a lightweight MLP. The ablation study (Table 2) validates that this approach achieves better or comparable quality to environment-map baselines while being ~6.7× faster than the best envmap variant (18 min vs. 2 hours).

- **Competitive reconstruction quality despite massive speedup:** On the MII synthetic benchmark, UniVoxel outperforms all baselines (NeRFactor, MII, Nvdiffrec-mc, TensoIR) on most metrics for albedo, roughness, novel-view synthesis, and relighting. For example, novel-view PSNR reaches 25.5 dB vs. 23.4 (TensoIR), 23.6 (MII), and 18.9 (Nvdiffrec-mc). This demonstrates that the speed gain does not come at a quality cost.

- **Principled design choice enables lightweight decoders:** The explicit voxel grids (SDF field at 1 channel, semantic field at 6 channels at 160³ resolution) feed into 3-layer MLPs with 192 channels each. This contrasts sharply with implicit methods requiring deep MLPs for each property, and the efficiency gain is directly attributable to this architectural choice.

- **Comprehensive ablation studies isolating each component:** Ablations compare different illumination models (SG, SH, envmap, NeILF) within the same framework and ablate each loss term. These controlled experiments provide clear evidence for the effectiveness of the proposed design.

- **Elegant extension to varying illumination:** The method naturally handles per-view lighting changes by adding view embeddings to the SG predictor network (Eq. 12), validated on challenging NeRD real-world scenes.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Quantitative evaluation is incomplete for varying-illumination real-world scenes.** For the 3 NeRD scenes captured under changing illumination, the paper provides only qualitative visualizations of normals, albedo, roughness, and relighting (Figure 4). No quantitative NVS metrics (PSNR/SSIM/LPIPS) are reported for these scenes, even though they represent the most challenging and practically relevant scenario. While the lack of ground-truth relighting targets is understandable, held-out-view metrics would substantially strengthen the evidence for real-world generalization.

- **No ablation on the number of SG lobes (k=16).** The number of Spherical Gaussian lobes is set to 16 with no sensitivity analysis. Since the representation's capacity and computational cost both scale with k, a sweep (e.g., k=4,8,16,32) would clarify the quality-efficiency trade-off.

- **The white-light regularization (Eq. 11) assumes predominantly white direct lighting, which could bias results on scenes with strongly colored illumination.** The paper mentions this assumption in passing ("Since the incident light is primarily composed of direct lighting, which is mostly white lighting") but does not discuss it as a limitation or evaluate its impact on scenes with colored lighting.

- **No quantitative geometry evaluation.** The method uses volumetric SDF as its geometry representation, yet no quantitative geometry metric (e.g., Chamfer distance, F-score) is reported, even for synthetic scenes where ground-truth meshes are available. The Shiny Blender experiment is mentioned but its results are deferred to a section not present in the extracted text.

- **No explicit limitation discussion.** The paper lacks a limitations paragraph discussing scenarios where the local SG representation may struggle (e.g., strong specular inter-reflections, strongly colored indirect light, or scenes requiring very high-frequency lighting).

### Trivial
None.

## Nice-to-Haves
- A sensitivity analysis on the loss weights (seven λ values) would help gauge the method's robustness to hyperparameter tuning.
- Brief discussion of how the coarse-to-fine resolution schedule (96³ → 160³) was chosen would be helpful.

## Removed Points

These points were flagged by the reviewers but are removed with justification:

1. **"Missing TensoIR training time in the main table"** — Removed because the table is included via `\input{tables/mii}` in the original submission; its absence is a parser artifact, not a paper issue. The strength finder confirms that TensoIR timing (1 hour) is reported in the actual paper.

2. **"Without multi-bounce ray tracing claim is misleading"** — Removed because this is technically accurate and clearly qualified. The paper's claim refers to avoiding *multi-bounce* ray tracing during training, which is correct. During relighting, the paper transparently states that single-bounce visibility is computed (Section 3.4, line 230). The harsh critic acknowledges the claim is "technically accurate."

3. **"UniVoxel(Hash) hyperparameter details not provided"** — Removed because hyperparameters for this variant are deferred to an appendix section that is stripped by the parser; the rule states to remove criticisms about missing appendix content.

4. **"Missing related works"** — Removed per instructions (cannot verify existence of missing references).

## Novel Insights

The reviews surface an interesting tension: the paper's strongest evidence (synthetic benchmarks with full metrics) and its weakest (qualitative-only real-world varying-illumination results) pull in opposite directions. The harsh critic correctly identifies this gap, but it is worth noting that the varying-illumination NeRD scenes are fundamentally difficult to evaluate quantitatively because per-view illumination changes mean there is no single ground-truth lighting environment to compare against. The paper could partially address this by reporting NVS metrics on held-out views under the *same* varying illumination (comparing predicted vs. ground-truth pixel colors for those views), which would at least verify that the model correctly captures the per-view appearance. This gap is real but moderate — the synthetic results already validate the core claims.

## Suggestions

1. **Add quantitative NVS metrics for the 3 varying-illumination NeRD scenes.** Even though relighting targets are absent, rendering the reconstructed model under each training view's specific lighting and comparing against held-out test views (where available) would add rigor directly in the main paper.

2. **Add an ablation on the number of SG lobes (k) and the number of Fibonacci incident-light samples.** A simple sweep would strengthen the practical utility claim.

3. **Add a limitations paragraph** explicitly discussing scenarios where local SGs and the white-light prior may be insufficient.

4. **Include quantitative geometry metrics** (e.g., Chamfer distance) for synthetic datasets where ground-truth meshes exist, even if only in the appendix.
