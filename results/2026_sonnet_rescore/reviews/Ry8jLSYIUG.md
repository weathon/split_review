Now I have read the full paper. Let me synthesize the final review by verifying each reviewer claim against the text.

---

## Summary

This paper investigates the fundamental capacity limits of invisible image watermarking. It develops geometric upper bounds under PSNR and linear robustness constraints (Sections 2.2–2.5), runs carefully controlled diagnostic experiments showing that Video Seal fails to utilize available capacity even in minimal settings (Section 3), and demonstrates via Chunky Seal — a scaled-up Video Seal variant — that 1024-bit capacity with comparable robustness is practically achievable (Section 4). The central conclusion is that current deep-learning watermarking models are far from theoretical limits due to architectural and training deficiencies, not because the limits themselves are tight.

---

## Strengths

- **Principled geometric framework (Sections 2.2–2.4):** The treatment of PSNR as an ℓ₂-ball constraint and derivation of capacity across the cube-in-ball, ball-in-cube, and partial-overlap regimes is rigorous and reproducible. The worst-case corner analysis (Section 2.4) shows the penalty is at most 1 bpp, a clean and tight result.

- **Controlled diagnostic experiment ruling out hypotheses A, B, C (Section 3.1, Figure 5 left):** Training Video Seal on a single gray image with only MSE loss and no augmentation eliminates dataset complexity, robustness, and perceptual constraints as explanations. The failure to embed 1024 bits in this stripped-down setting is compelling evidence of architectural bottleneck, not real-world complexity.

- **Linear and handcrafted models prove achievability (Section 3.2, Table 1):** A single linear layer achieves 100% accuracy at 2048 bits and PSNR > 40 dB (Table 1), and the hypercube-in-ball construction reaches 456,509 bits at 42 dB, nearly matching the theoretical bound. These concrete demonstrations refute hypothesis D (bounds unachievable) without ambiguity.

- **Tiling experiment (Section 3.2):** Tiling a 32×32px Video Seal achieves 32,768 bits while maintaining 41.7 dB PSNR, confirming that Video Seal's 256×256px result is equivalent to its 32×32px result and that the architecture simply fails to exploit spatial resolution.

- **VQ-VAE/VQGAN data-distribution analysis (Section 2.6):** Using neural compression codebooks to upper-bound the number of perceptually distinct images is a novel approach. The conclusion — that collisions reduce capacity by at most ~0.05 bpp — is quantitatively grounded and dispatches hypothesis C cleanly.

- **Chunky Seal proof-of-concept (Section 4, Table 3):** Delivers 4× capacity increase (1024 vs. 256 bits) with PSNR 45.3 dB vs. 44.4 dB, SSIM 0.995 vs. 0.996, and competitive bit accuracy across all transformation categories, establishing that practical capacity improvements are achievable without sacrificing structural robustness.

---

## Weaknesses

### Fatal
None.

### Major

- **LPIPS mischaracterization in Section 4:** Table 3 reports LPIPS of 0.0085 ± 0.0067 (Chunky Seal) vs. 0.0019 ± 0.0011 (Video Seal) — a 4.5× difference. The text in Section 4 calls this "only slightly higher LPIPS," which is not an accurate characterization. LPIPS is widely regarded as the most perceptually calibrated of the reported image quality metrics. A 4.5× increase in LPIPS is a meaningful perceptual quality regression that the authors should quantify honestly rather than downplay. The paper's broader claim — "achieving 4× the capacity per pixel with comparable robustness and quality through simple scaling" — depends on "comparable quality" being accurate, and the LPIPS data weakens this. The paper can still make its core point (larger capacity is achievable), but accurately acknowledging this regression would strengthen rather than undermine the argument.

### Minor

- **Figure 1 shows only heuristic bounds:** Sections 2.5 explicitly notes that Bounds 10–12 "can both over-approximate and under-approximate" the true capacity. Figure 1's visual impression — that all robustness-constrained bounds sit orders of magnitude above practice — is accurate for most augmentation settings (Table 2: rotation 30°, LinJPEG q=10, Horizontal Flip all leave thousands of bits under the conservative Bound 13). However, for the most aggressive crop (75%), the conservative Bound 13 yields only 904 bits at 256×256px, while current SOTA is ~655 bits (0.001 bpp × 65,536 pixels), only ~1.4× above SOTA rather than orders of magnitude. This special case is not visible in Figure 1, and a reader taking the figure at face value would overestimate the gap. Including Bound 13 lines in Figure 1, or citing Table 2's numbers in the caption, would address this without undermining the main claim.

- **Handcrafted model lacks perceptual quality evaluation:** The handcrafted hypercube scheme is the primary empirical anchor for the claim "bounds are achievable, so hypothesis D is false" (Section 3.2). However, this scheme embeds a maximally structured high-frequency perturbation — essentially coarse pixel quantization. No LPIPS, SSIM, or MS-SSIM is reported for the handcrafted model. The theoretical argument (these are valid PSNR ≥ 42 dB embeddings) holds regardless of perceptual appearance, but the claim that "our bounds are not that far off" implicitly treats the handcrafted model as a legitimate watermarking approach. Reporting at least LPIPS for the handcrafted scheme, or explicitly acknowledging that it is a mathematical construction that satisfies the PSNR constraint rather than a perceptually acceptable watermark, would sharpen the argument.

### Trivial

None that don't fall under formatting / parser noise.

---

## Nice-to-Haves

- **Efficiency profile for Chunky Seal:** Section 4 notes the embedder is 90× larger than Video Seal, but no inference latency or throughput numbers are given. Practitioners evaluating deployment feasibility cannot compare tradeoffs without approximate timing. A single sentence with rough estimates would suffice; the discussion already correctly cautions against naive scaling as a path forward.

- **Include additional baselines (e.g., MiRRE, WAM, TrustMark) in Table 3:** These methods appear in Figure 1 but are absent from Table 3. Readers cannot determine whether Chunky Seal's 1024-bit regime is unique or whether some existing high-capacity methods already approach it. Even reporting their capacity and LPIPS values in a supplementary column would contextualize the contribution.

- **Clarify framing of linear model comparison:** Section 3.2 notes that "a linear model outperforms Video Seal." In context it is clear this is in the gray-image/PSNR-only diagnostic setup, but the framing could be sharpened with a reminder that the linear model degenerates to a fixed perturbation mask under this trivially simple task — making the diagnostic point (Video Seal should be able to overfit this but cannot) all the sharper.

---

## Removed Points

*These points were flagged for removal; treat with caution.*

- **Harsh Critic — "conservative Bound 13 tells a more nuanced story and Figure 1 is misleading as a whole":** Partially retained (kept as Minor), but the "orders of magnitude" headline is accurate for most augmentations; the concern is specific to the 75% crop case, which is addressed in Table 2. The paper is honest about the heuristic nature throughout Section 2.5.

- **Harsh Critic — "Chunky Seal results might change with tuning":** This is a speculative concern. The paper explicitly acknowledges VideoSeal was "extensively optimized," and this is framed as making Chunky Seal's results conservative. Speculative performance changes are not a concrete verifiable weakness.

- **Strength Finder — "Even the most aggressive 75% crop leaves 904 bits for 256×256px images, showing robustness requirements cannot account for the observed gap":** This strength is overstated given that current SOTA embeds ~655 bits at 256×256px, meaning the 75% crop conservative bound of 904 bits is barely above practice. The broader claim is valid for all other augmentations, but this specific framing overstates the evidence. The strength is retained for the overall dataset of augmentations, not this cherry-picked argument.

- **Harsh Critic — section on "missing parts," requesting comparisons to MiRRE, WAM, TrustMark in Table 3:** Moved to Nice-to-Haves rather than a weakness since the paper's core claims do not depend on this comparison.

- **Any criticism about missing appendix proofs, missing supplementary material, or absent references:** Removed per hard rules (parser strips appendix sections).

---

## Novel Insights

The most genuinely novel analytical observation is the *resolution non-utilization finding* in Section 3.1: Video Seal trained at 256×256px achieves essentially the same capacity as at 32×32px despite having 64× more pixels. This is not just an empirical data point but a diagnostic that cleanly eliminates spatial under-utilization as an explanation — because the model simply doesn't use the pixels. Combined with the linear model succeeding at 2048 bits in the same setup, this points squarely to the architecture's inductive biases as the bottleneck, not the optimization landscape or the bound's tightness. The proposed sanity checks in Section 5 (capacity scales linearly with image size, decreases with higher PSNR, outperforms linear baselines) operationalize this insight into a concrete benchmark for future architectures.

---

## Suggestions

1. Replace the phrase "only slightly higher LPIPS" in Section 4 with accurate language acknowledging the 4.5× LPIPS increase, and discuss whether this reflects a genuine quality regression or variance sensitivity in the metric.
2. Add Bound 13 as a shaded region or dashed line to Figure 1 to show the range of theoretical uncertainty, particularly for aggressive crop settings, while retaining the heuristic bounds as the main curves.
3. Include a brief perceptual-quality note for the handcrafted model — even just stating that it satisfies the PSNR constraint but is a mathematical construction that would not pass perceptual screening — to distinguish "achievable under PSNR" from "achievable perceptually."
4. Add approximate inference latency numbers (milliseconds per image) for Chunky Seal vs. Video Seal to the Table 3 caption or the limitations paragraph.

---

## Evaluation on Key Axes

- **Originality:** The geometric capacity framework and the controlled diagnostic decomposition (ruling out hypotheses A–D through progressive simplification) are both novel contributions not replicated by prior information-theoretic watermarking capacity work. **High.**
- **Importance:** The fundamental question of whether current models are near their limits is practically significant for AI provenance, and the paper provides tools for measuring this gap. **High.**
- **Claims well-supported:** Core claims (large gap exists, VideoSeal has architectural limitations, gap is not due to robustness or data distribution, Chunky Seal closes some gap) are all well-evidenced. The "orders of magnitude" headline is accurate for most but not all settings; the LPIPS claim is inaccurate. **Mostly supported with notable exceptions.**
- **Soundness of experiments:** The diagnostic design is clean and well-controlled. The sweep over learning rates and λᵢ is appropriate. Conservative vs. heuristic distinction is maintained. **Good.**
- **Clarity:** Generally clear and well-organized; the progression from theory → diagnostics → proof-of-concept is logical. The mischaracterization of LPIPS and Figure 1's single-curve presentation are the main clarity issues. **Good with minor issues.**
- **Community value:** Theoretical bounds framework, sanity checks for future methods, and Chunky Seal code/checkpoint release all provide direct reusable resources. **High.**

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>