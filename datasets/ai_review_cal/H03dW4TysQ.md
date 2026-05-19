- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5
Now I have a thorough understanding of the paper and can cross-check all claims. Let me produce the consolidated review.

## Summary

This paper proposes MoEDM, a method that prunes parameter-heavy mid-layers from pretrained diffusion models and replaces the remaining layers with time-step-gated "expert" pathways. During inference, exactly one expert per layer is activated per time step based on the known timestep \(t\), yielding 2× speedup on the 64×64 pixel-space Guided Diffusion and on Latent Diffusion. The method is evaluated on ImageNet subsets, domain shift (ImageNet→FFHQ), and text-to-image generation.

## Strengths

- **Measured 2× sampling speedup**: The paper reports concrete runtime reductions — average time feedforward per step drops from 0.033s to 0.015s for Guided Diffusion 64×64 (Table 1) and from 0.050s to 0.024s for Latent Diffusion 256×256 (Table 3). These are clean, reproducible measurements.

- **Well-controlled domain-shift experiment with proper baselines**: Table 2 compares MoEDM against fully fine-tuned full-size, BitFit, and partial fine-tuning baselines on the FFHQ domain-shift task. MoEDM matches the fully fine-tuned model (FID 12.23 vs 12.21) while achieving 2× speed. This is the paper's strongest evidence, as it controls for the effect of fine-tuning itself.

- **Ablation experiments isolate contributions**: Table 2 includes ablations removing each component — "MoEDM w/o discarding" (FID 23.52) and "MoEDM w/o MoE" (FID 33.86) — confirming that both layer discarding and dynamic routing contribute to the final performance. These ablations directly support the design choices.

- **Training-free gating design**: The gating mechanism in Equation (2) relies on the known timestep \(t\) to select which expert to activate, requiring no learned routing. This eliminates any gating overhead during inference, which the runtime measurements validate.

- **Compatibility with existing fast samplers**: MoEDM is integrated with DPM-Solver and DDIM, and the reported runtimes reflect this stacking, demonstrating practical applicability beyond toy settings.

## Weaknesses

### Fatal
None.

### Major

- **Missing fine-tuned full-model baselines on ImageNet subsets (Tables 1 and 3)**: Tables 1 and 3 compare MoEDM (fine-tuned on the target class) against the *unfine-tuned* full-size model. Since MoEDM has been specialized via fine-tuning, the observed FID/KID improvements (e.g., 5.66 vs 9.58 in Table 1) could come from specialization rather than the MoEDM architecture. The appropriate control — a fully fine-tuned version of the base model on the same class data — is absent from these two tables. The paper states (lines 113–114) that fully fine-tuning baselines were "only present[ed] ... on the most challenging and representative Domain Shift task." This is acknowledged as a space constraint, but it leaves the paper's central claim ("maintains intact task-specific performance") without direct support for the main experimental settings. The Domain Shift experiment (Table 2) does include this control and provides partial evidence, but the gap in Tables 1 and 3 is significant enough to weaken the paper's overall argument.

- **Text-to-image evaluation lacks quantitative quality metrics**: The text-to-image experiment reports only speed and example images. The paper states (line 169) that "we propose to evaluate the quality of image generation in this task by human eyes," but no human study is conducted — no preference ratings, no CLIP scores, no FID on held-out prompts. Example images (Figures 4–5) are insufficient to demonstrate quality preservation. This is an unsubstantiated claim.

### Minor

- **Abstract overstates speedup claim**: The abstract claims MoEDM "doubles the sampling speed across various applications." However, the paper itself notes (line 142) that for Guided Diffusion at 256×256 resolution, "the improvement in sampling speed is not as significant" because the important extremity layers dominate computation. No quantitative speedup figure is reported for this setting. The 2× claim is well-supported for 64×64 pixel-space and Latent Diffusion, but the abstract's phrasing should be qualified.

- **"Uneven Expansion" section heading with no reported results**: Section 4.3.2 includes a subsection heading "Uneven Expansion" (line 177) but contains only a sentence saying the authors "provisionally try manual specify expansion ratio for different layers" without reporting any results. This appears to be an unfinished experiment.

- **Vague description of training iterations for domain-shift**: The paper states (line 144) that MoEDM uses "only a fraction of the training iterations" without specifying the exact number, making it hard to assess the training efficiency comparison against fully fine-tuned baselines.

### Trivial
None.

## Nice-to-Haves

- Report total stored parameter count (all experts combined) alongside active parameters per step, as total footprint matters for deployment memory.
- Provide confidence intervals or multiple-seed runs for FID/KID, especially on small-class ImageNet subsets where variance is high.
- A small human preference study for the text-to-image setting would convert a currently unsubstantiated claim into evidence.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Parameter scoring procedure is not actually used" (Harsh Critic point #4)**: The reviewer claimed the channel-wise scoring (Section 3.1) "does not affect the final algorithm" and "could be replaced by a sentence." However, the paper uses this scoring in Section 4.2 to empirically validate that >90% of discarded parameters come from mid-layers, establishing the foundation for layer-level discarding. The criticism misunderstands the role of the scoring — it is used as analysis/validation, not as a runtime component. The paper does not claim it as a contribution separate from this validation.

2. **"Total vs. active parameter counts / memory usage"**: The paper states these are in the supplementary material (line 104). Missing appendix content is a parsing artifact.

3. **Demands for statistical significance / multiple seeds**: Standard practice for large-scale diffusion benchmark evaluation; requesting it is reasonable as a nice-to-have but not a core weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same structural evaluation gap (missing fine-tuned baselines in the main tables) that a careful reader would identify, but offer no additional analytical insight into the method itself.

## Suggestions

1. **Add fully fine-tuned baselines on ImageNet subsets** to Tables 1 and 3. This is the single most important addition: it controls for fine-tuning effects and directly tests whether MoEDM maintains quality relative to an equivalently specialized full-size model. If MoEDM matches (or comes close to) the fine-tuned full model while being 2× faster, the core claim is cleanly supported.

2. **Provide quantitative text-to-image evaluation**: Report CLIP score or FID on a held-out prompt set, or conduct a small human preference study (50–100 comparisons). A figure with example images is not evidence.

3. **Qualify the speedup claim**: Replace "doubles the sampling speed across various applications" with a more precise statement: "achieves 2× speedup on 64×64 pixel-space Guided Diffusion and on Latent Diffusion" (and report the speedup for 256×256 pixel-space if applicable).

4. **Remove or fill the "Uneven Expansion" subsection**: Either report the results of the manual expansion ratio experiment or remove the section heading.

5. **Specify training iterations**: Give the exact number of fine-tuning steps used for MoEDM and for each baseline to enable fair assessment of training efficiency.
