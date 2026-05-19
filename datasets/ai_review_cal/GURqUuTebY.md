- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6
Now I have a clear picture of the paper and can verify the reviewer claims. Let me compose the final consolidated review.

## Summary

This paper presents DreamFlow, a text-to-3D generation method that replaces the standard score distillation objective (SDS/VSD) with an approximation of the probability flow ODE (APFO) using a predetermined, decreasing noise schedule rather than random timesteps. The authors frame text-to-3D optimization as a multi-view Schrödinger Bridge problem and derive an update rule that differs from VSD primarily in its gradient scaling and deterministic schedule. The method operates in three coarse-to-fine stages (NeRF, mesh fine-tuning, high-resolution refinement) and claims a 5× speedup over ProlificDreamer with competitive or better photorealism.

## Strengths

- **Novel and well-motivated core idea.** Replacing random timesteps in score distillation with a deterministic noise schedule is a sensible approach to reducing gradient variance — a known limitation of SDS/VSD. The motivation is clearly articulated and the connection to the diffusion generative (sampling) process rather than the training objective is a conceptually clean framing.

- **Smooth optimization trajectory is empirically demonstrated.** Figure 6 (referenced as fig_landscape) shows that the loss and gradient norm decrease monotonically for DreamFlow while fluctuating for VSD, providing visual evidence for the reduced-variance claim. This is a concrete, method-specific advantage that goes beyond just reporting final metrics.

- **High-resolution generation (1024×1024) with explicit speed numbers.** The paper reports concrete wall-clock timings (50 min NeRF + 40 min mesh + 20 min refinement ≈ 2 hours on a single A100), which gives the reader a clear picture of computational cost. Achieving 1024×1024 output with SDXL refinement is a genuine engineering contribution.

- **Schrödinger Bridge theoretical framing provides a principled derivation path.** While the practical update rule ends up structurally similar to VSD, the derivation from SB → probability flow ODE → amortized sampling is mathematically sound and offers a different lens for thinking about text-to-3D optimization.

## Weaknesses

### Fatal
None.

### Major

- **The speed comparison against ProlificDreamer is not properly controlled, undermining the headline 5× claim.** The paper states DreamFlow uses a single A100 for all stages, but does not specify what hardware or resolution ProlificDreamer was run on for the reported timings (5h NeRF + 7h mesh). For DreamFusion and Magic3D, hardware and resolution are given; for ProlificDreamer — the primary baseline — they are not. Additionally, DreamFlow's NeRF stage operates at 256×256 while the ProlificDreamer baseline may use 64×64 (the resolution used in the original paper). When baselines run at different resolutions and on unspecified hardware, a raw wall-clock comparison conflates too many factors to be interpretable as a clean "5× speedup."

- **The user preference study is critically under-described.** The description states "three binary comparison tasks (total 60 comparison)" without clarifying whether this is 60 total comparisons (20 per baseline) or 60 per baseline. The number of participants, their instructions, viewing conditions, and inter-rater agreement are all absent. Without these details, the reader cannot assess whether the reported preferences are statistically reliable. The quantitative evaluation also relies solely on CLIP R-precision, with no confidence intervals, standard deviations, or significance tests reported. CLIP R-precision is a narrow measure (text-image alignment, not geometry, multi-view consistency, or photorealism) and is known to be gameable, making it insufficient as the sole quantitative metric for claims of "state-of-the-art quality."

- **The technical contribution is structurally close to VSD, but the paper's framing inflates the departure.** The derived update in Eq. 8–9 is VSD's gradient subtraction (D_φ − D_p) with a different coefficient ((σ(t_{i+1})−σ(t_i))/σ(t_i) instead of λ(t)) and a deterministic schedule replacing random timesteps. The paper itself acknowledges this similarity in passing ("the difference occurs in its scaling of gradient flow," Sec. 3.2). The Schrödinger Bridge derivation provides a different theoretical lens, but the practical algorithm is not a fundamentally new paradigm. The framing should more directly state what is novel (the deterministic schedule and its effect on variance) and what follows prior work.

### Minor

- **No direct ablation isolating the deterministic schedule.** The paper does not compare APFO with the same update rule but random timesteps (i.e., the only difference being the schedule). Such an ablation would be the cleanest test of the paper's central claim that the deterministic schedule is the source of improvement. Without it, other differences in the optimization pipeline could contribute to the observed speed/quality gains.

- **The optimization analysis (Figure 6) is only qualitative.** Loss values and gradient norms are plotted, but no quantitative measures (variance across runs, convergence rate to a quality threshold) are provided. Moreover, since VSD's random timesteps produce inherently varying gradient magnitudes, the fluctuation is expected — the relevant question is whether the average gradient direction is equally effective, which is not addressed.

- **Limitations section is too brief.** It mentions only potential biases from the diffusion model. The paper does not discuss failure modes specific to its own approach (e.g., geometry artifacts from the lack of 3D awareness in the 2D diffusion prior, whether the ODE approximation breaks down at coarse timesteps, or cases where the predetermined schedule fails relative to adaptive approaches).

### Trivial
None.

## Nice-to-Haves

- Adding standard deviations or confidence intervals to the CLIP R-precision results over multiple seeds would substantially strengthen the quantitative claims.
- A controlled speed comparison at matched resolution (e.g., DreamFlow at 64×64 vs. ProlificDreamer at 64×64) would clarify whether the speedup is due to the method itself or the higher-resolution shortcut.
- Specifying the noise schedule shape (linear/quadratic in t or log-σ) and spacing (uniform in time or in noise level) more explicitly would aid reproducibility.
- Reporting a failure case or two would give a more balanced picture of the method's strengths and limitations.

## Removed Points

**"The user study text is internally contradictory (says 'consistently wins on photorealism' but then 'DreamFusion remains better')."** — This criticism is based on a misreading. The paper states DreamFlow wins on photorealism (one axis) while DreamFusion remains better on 3D consistency and prompt fidelity (a different axis). These are distinct evaluation criteria and not contradictory. The description is under-specified (kept as Major), but the claimed contradiction is not present.

**"Missing related works."** — Per the review guidelines, this cannot be verified without external sources and is not included.

**"Reproducibility details missing from main text (LoRA rank, learning rate, schedule shape)."** — These details are standard for an appendix and the parser strips supplementary material. Per the review guidelines, criticisms about missing appendix content are removed.

**"CLIP R-precision is a weak proxy that does not capture geometry."** — The weakness about missing uncertainty quantification is kept; the generic claim that CLIP is "gameable" and "widely acknowledged" as weak is removed as it is an area-of-concern sweep rather than a specific identified problem with the paper's usage.

**"The Schrödinger Bridge introduction is tangential."** — This is a subjective presentation preference, not a substantive weakness.

## Novel Insights

The reviews do not surface genuinely novel observations beyond the paper's own contributions. One observation worth noting: the harsh critic correctly identifies that the practical update rule in Eq. 8–9 is structurally very close to VSD, differing primarily in the coefficient and the deterministic schedule. This, combined with the paper's own admission of similarity, suggests that the main practical novelty is indeed the predetermined schedule and its effect on variance — a point the paper would benefit from foregrounding more directly rather than emphasizing the Schrödinger Bridge framing.

## Suggestions

1. **Fix the ProlificDreamer speed comparison.** Either (a) run DreamFlow and ProlificDreamer on the same hardware and at matched resolutions and report the wall-clock times, or (b) provide the hardware/resolution assumptions for the ProlificDreamer numbers and clearly state any asymmetries. Without this, the 5× claim is not verifiable.

2. **Report full user study methodology.** Include the number of participants, instructions, number of comparisons per pair, and preferably a measure of inter-rater agreement (e.g., Fleiss' κ). Clarify whether "60 comparisons" is total or per baseline.

3. **Add uncertainty quantification to CLIP R-precision.** Report scores from at least 3 independent runs with means and standard deviations.

4. **Include an ablation comparing APFO with random timesteps vs. the deterministic schedule** (same update rule, only the schedule changes). This directly tests the core claim.

5. **Replace or supplement the CLIP R-precision with a metric that better captures 3D quality** (e.g., multi-view consistency score, or a properly conducted user study on overall quality rather than just photorealism).

6. **Tone down the claims of novelty.** Acknowledge directly that the update rule is structurally similar to VSD, and position the deterministic schedule and the resulting variance reduction as the primary technical contribution.
