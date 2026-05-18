Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me construct the final review.

## Summary

NeRM proposes a two-stage generative model for human motion synthesis: first learning variational implicit neural representations (INRs) that map temporal coordinates to poses via an auto-decoded latent per sequence with a clip-sampling strategy to handle varied framerates, then training a diffusion model on the learned latents for conditional generation. The core claim is that the INR-based representation enables training on raw motion data with mixed framerates and generates high-framerate motions without the memory or sampling overhead of pose-sequence approaches.

## Strengths

1. **Continuous motion field enables training on native varied-framerates without downsampling.** Section 3.1 describes how NeRM represents motions as continuous functions over temporal coordinates with a clip-sampling strategy, allowing the model to train directly on datasets like HumanML3D where framerates range from 20 to 250 fps, instead of discarding high-framerate details via preprocessing. The paper shows that native-framerate training outperforms its own fixed-framerate variant, isolating the benefit of this design.

2. **Competitive results across multiple generation tasks and datasets.** NeRM is evaluated on text-to-motion (HumanML3D, KIT), action-to-motion (UESTC, HumanAct12), and unconditional generation (AMASS), achieving state-of-the-art or competitive results across all settings (Tables 1, 3, Figure 5). This demonstrates that the framework generalizes beyond a single task or dataset.

3. **High-framerate motion synthesis with quantitative and qualitative evidence.** NeRM generates motions at arbitrary framerates (e.g., 100 fps) and Table 2 shows favorable clip-FID scores compared to interpolation-based upsampling of baseline outputs. Figure 4b visualizes that NeRM avoids foot-sliding artifacts that plague interpolation-based approaches.

4. **Variational INR + latent diffusion pipeline decouples representation from generation.** The two-stage design is technically sensible: variational INRs handle frame-rate variability while the latent diffusion model models the distribution of motion codes, enabling efficient sampling without processing dense frame sequences directly.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation studies for any key design component.** The paper includes multiple architectural choices — the variational formulation (vs. deterministic latent), the codebook-coordinate attention (vs. Fourier features alone), progressive training (vs. multi-framerate from scratch), and the KL weight λ_KL — yet **none are ablated**. The paper claims "we empirically find that such [Fourier] embedding is insufficient" (line 84) but provides no results comparing with and without the codebook. Without ablations, it is impossible to determine which components drive the reported performance gains, and the reader cannot assess whether the method is well-grounded or overfit to the experimental setup. This is a significant gap for any methods paper claiming architectural novelty.

2. **Missing architecture details that prevent reproduction.** The paper does not specify: the MLP depth/width of decoder *f_θ*, the dimension of latent *z*, the number of transformer layers or heads in denoiser *ϵ_φ*, the number of codes *N* or code dimension *d* in the codebook, or the value of λ_KL. While the notation *N*, *d*, λ_KL is introduced, their concrete values are never given. This makes the paper functionally non-reproducible. The critic's characterization that "architecture details are almost entirely absent" is accurate for the specific numerical values needed.

3. **The paper's central narrative about multi-framerate training is weakened by its own fixed-framerate results.** The paper claims "this advantage [over baselines] exactly stems from our capability of handling varied-framerate data" (line 147–148). However, the Fairness Discussion (line 151) reveals that even NeRM trained on fixed-framerate (downsampled) data — i.e., without multi-framerate training — outperforms or matches several baselines. While the paper attributes this to "our powerful latent diffusion framework and codebook-enhanced representation," this means the *architectural contributions* (INR + diffusion + codebook) — not the multi-framerate data utilization — may largely explain the gains over prior work. The comparison between native and fixed-framerate NeRM (which would isolate the value of multi-framerate training) is mentioned but the delta is not prominently analyzed or discussed as the central evidence. The paper needs a direct, controlled internal comparison (same architecture, same pipeline, same evaluation) between native-framerate and fixed-framerate training to substantiate the claim.

4. **Efficiency claims are asserted without quantitative support.** The abstract and introduction state NeRM is "memory-friendly" and "highly efficient even when generating high-framerate motions," but no GPU memory usage, parameter count, or sampling time measurements are provided. Given that memory overhead and slow sampling of high-framerate motion are the paper's primary motivations (Section 1), the lack of any quantitative efficiency data is a significant omission.

### Minor

1. **High-framerate evaluation uses a weak baseline comparison.** Table 2 compares NeRM's high-framerate outputs against low-framerate baselines upsampled via spherical linear interpolation. The paper acknowledges this (line 153) and the constraint is real (baselines cannot natively generate high-framerate motion), but interpolation is a deterministic, non-generative baseline that any plausible generative model would be expected to beat on detail-sensitive metrics. This experiment shows NeRM can generate plausible high-framerate poses, but does not demonstrate that it is better than *generative* alternatives for high-framerate motion.

2. **clip-FID is introduced without validation.** The new metric (Section 4.1) is defined as FID over randomly extracted motion clips. While the motivation (sensitivity to local details like foot sliding) is reasonable, the paper provides no analysis showing clip-FID correlates with human judgment or with established metrics. The hyperparameters (random center *v*, clip size *m*) are not ablated. This is a useful addition but currently stands as an unvalidated metric that systematically favors the proposed method.

3. **KL weight λ_KL is not reported.** The loss function (line 91) includes λ_KL, which controls the strength of regularization and critically affects latent space quality and downstream diffusion modeling. Its value is never given, leaving an important hyperparameter unspecified.

4. **No evaluation of the progressive training strategy.** The paper describes a two-phase training (first fixed-framerate, then multi-framerate) but provides no comparison against training only on multi-framerate data from the start. The effect of this design choice on final performance is unknown.

### Trivial

- The qualitative results in Figure 4 show only 3 cherry-picked examples. A larger random set or user study would strengthen the visual quality claims.

## Nice-to-Haves

- A controlled internal ablation comparing NeRM trained on native framerates vs. the same data downsampled to 20 fps, holding all other architectural choices fixed, would directly isolate the value proposition of multi-framerate training.
- Ablation of the codebook: performance with vs. without CCA, and with different codebook sizes.
- Reporting GPU memory usage and sampling time for NeRM vs. baselines at different target framerates (e.g., 20, 60, 100 fps).

## Removed Points

- **Missing related works (e.g., MMoS, Fu et al. 2024):** Removed per instructions — I cannot externally verify the existence or relevance of these works. The critic also noted this was "not a fatal omission."
- **MoFusion FID of 6.009 being implausible:** Removed — the Table 1 is rendered as an image in the extracted text, so I cannot verify the specific numerical entry. The critic's claim about published MoFusion FID (~0.2–0.3) cannot be cross-checked against the paper.
- **Criticism about the second stage treating variational latents as point estimates being a "serious design flaw":** Downgraded from critic's framing. Using one sample per sequence from the posterior to train a diffusion model is standard practice in two-stage generative models (e.g., Stable Diffusion, MLD), not a design flaw. The valid sub-point about λ_KL being unreported is preserved in Minor weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension between the paper's architectural contributions and its claimed "multi-framerate training" advantage, but this is an evaluation-narrative issue rather than a novel insight about the method itself.

## Suggestions

1. **Add ablation studies** for: (a) native vs. fixed-framerate training within the same NeRM pipeline, (b) with vs. without codebook-coordinate attention, (c) with vs. without variational formulation, and (d) progressive vs. direct multi-framerate training. This is the single most impactful addition.
2. **Report all key architectural hyperparameters** in the main text or supplement: latent dimension, MLP layers of *f_θ*, transformer layers/heads of *ϵ_φ*, codebook size *N* and *d*, λ_KL value, and training iteration counts.
3. **Provide GPU memory and sampling time measurements** to substantiate the efficiency claims that appear in the abstract and introduction.
4. **Validate clip-FID** by reporting it at standard framerates (20 fps) alongside conventional FID, or by correlating it with human judgment on foot-sliding artifacts.

## Score and Decision

The paper proposes a genuinely interesting direction — using variational INRs to handle varied-framerate motion data — and demonstrates competitive results across multiple benchmarks. However, the experimental validation has significant gaps: the absence of any ablation studies means the relative contributions of the multi-framerate training, codebook, variational formulation, and progressive training are all unknown. The missing architecture details impair reproducibility. The efficiency claims central to the paper's motivation are unsubstantiated. And the central narrative about multi-framerate training being the source of improvement is weakened by the paper's own fixed-framerate results, which are not directly compared in a controlled ablation. These issues are addressable in a major revision, but the paper in its current form does not provide sufficient evidence to separate architectural contributions from the claimed data-utilization benefit.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>