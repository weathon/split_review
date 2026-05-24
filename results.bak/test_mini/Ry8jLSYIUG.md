Now I have a clear picture. Let me compose the final review.

## Summary
This paper analyzes the theoretical watermarking capacity of images under PSNR and linear robustness constraints using a geometric framework (high-dimensional grid model, L2-ball counting). The key finding is that theoretical capacities are orders of magnitude larger than what current deep watermarking models achieve. Through controlled experiments training Video Seal on a single gray image with only a PSNR constraint, the authors show the architecture cannot reach 1024 bits even though simple linear models and handcrafted embedders succeed at much higher capacities. A scaled-up version (Chunky Seal) achieves 4× the capacity of Video Seal (1024 bits) with comparable quality and robustness.

## Strengths

1. **Novel and rigorous theoretical capacity bounds under PSNR constraints** (Section 2.3–2.4, Figure 3): The paper develops closed-form and numerical bounds (Bounds 1–9) using a high-dimensional integer lattice model, transitioning smoothly between volume approximations and exact lattice point counts depending on the radius/dimension regime. At 40 dB for a 256×256 image the bounds give ~2+ bpp, orders of magnitude above the ~0.001 bpp of current practice. The analysis of arbitrary cover images (Section 2.4) shows the penalty is at most 1 bpp, meaning the gap is not an artifact of using centered gray covers.

2. **Controlled experiments that cleanly rule out confounders** (Section 3.1, Figure 5, Table 1): By stripping away robustness augmentations, perceptual losses, and multi-image datasets — reducing the task to watermarking a single gray image with only an MSE loss — the paper shows that Video Seal still fails at 1024 bits. The comparison to a linear model (which succeeds at 2048 bits) and the tiling experiment (32,768 bits achieved by tiling 32×32px models) provides strong evidence that the bottleneck is architectural, not fundamental. This is the paper's most compelling empirical contribution.

3. **Handcrafted embedder nearly matching the PSNR-only bound** (Section 3.2, Equation 2, Table 1): The handcrafted scheme inscribing an L∞ cube inside the L2 PSNR ball achieves 456,509 bits at 42 dB for a 256×256 image, showing the theoretical bounds are not vacuously high. This directly falsifies the hypothesis that the bounds are unachievable.

4. **Conservative lower bounds under robustness** (Bound 13, Table 2): The paper provides a genuine lower bound on capacity under various transformations (e.g., 904 bits for 75% crop at 42 dB). Even this worst-case bound exceeds current practice, demonstrating that robustness constraints alone cannot explain the gap.

5. **Honest framing and careful discussion of limitations** (Section 5): The paper explicitly acknowledges that the heuristic robustness bounds (Bounds 10–12) are not validated, that Chunky Seal is a proof-of-concept rather than a practical method, and that the analysis is restricted to linear transformations and PSNR constraints.

## Weaknesses

### Major

- **Heuristic robustness bounds (Bounds 10–12) used to support quantitative capacity claims without validation** (Section 2.5, Figure 4): The paper claims "even under the most aggressive cropping, we should expect around 0.5 bpp or almost 100,000 bits for 256×256 px images" based on heuristic bounds that are explicitly acknowledged as potentially over- or under-estimating true capacity. The gap between these heuristic bounds (~100,000 bits) and the conservative Bound 13 (~904 bits for 75% crop) spans two orders of magnitude, so the true capacity under robustness remains highly uncertain. While the conservative bound itself still supports the overall conclusion (904 > 256 bits), the paper's strongest "robustness doesn't explain the gap" language (e.g., "0.5 bpp") relies on unsubstantiated heuristic estimates. The authors should either validate the heuristic bounds in a simplified setting or reframe the robustness argument to depend primarily on the conservative bounds.

- **No uncertainty quantification for the central experiments** (Table 1): The results for Video Seal at different bit capacities are reported from single runs (best over hyperparameter sweep). Given the critical claim that Video Seal "cannot learn 1024 bits," repeating experiments with multiple random seeds would substantially strengthen the argument that this is a structural limitation rather than an optimization or initialization artifact.

### Minor

- **The 600,000 bit reference is imprecise** (Section 3.1, line 327): The paper states "From Figure 3 we expect capacities of around 600,000 bits at 40 dB in this setup." Figure 3 is explicitly for a 16×16×3 image, and the 600,000 figure is a rough extrapolation (the Bound 3 volume approximation for a 3-channel 256×256 image at 40 dB gives ~667,000 bits, and the handcrafted method at 42 dB gives 456,509 bits). The number is not *wrong* given that the linear model and Video Seal both operate on 3-channel representations (broadcast from gray), but the phrase "From Figure 3" is misleading since Figure 3 only directly shows results for a 16×16 image. This should be clarified.

- **The linear model comparison is not perfectly controlled** (Section 3.2): The linear embedder/extractor uses λᵢ values up to 20 for the MSE weight, while Video Seal's λᵢ was swept only up to 1.0. This means the linear model was trained under stronger pressure to minimize pixel distortion relative to the watermarking loss — a different optimization landscape. An ablation that progressively simplifies Video Seal's architecture (e.g., reducing ConvNeXt depth) while keeping the loss fixed would more precisely isolate the architectural bottleneck.

- **Conservative robustness bounds are for a single known transformation, not a composition** (Bound 13, Table 2): Real-world robustness requires surviving multiple simultaneous transformations (e.g., crop + JPEG). The paper's conservative bounds are derived per-transformation individually; a composited bound would likely be lower. This does not undermine the qualitative conclusion but means the reported 904-bit minimum (75% crop) is an upper bound on the true worst-case guarantee.

### Trivial
- The figure numbering in the paper diverges from the in-text references (e.g., what the text calls Bound 3 is labelled differently in Figure 3's caption/legend). This is likely a parser artifact but worth verifying.

## Nice-to-Haves
- A demonstration of the handcrafted-style embedding generalized to a robustness constraint (e.g., crop&rescale) would significantly strengthen the claim that the heuristic bounds are achievable.
- An analysis of *why* Video Seal fails — e.g., measuring the rank or effective dimensionality of the learned residuals, or the gradient signal magnitude at higher bit counts — would provide diagnostic insight beyond what the architecture comparison alone offers.

## Removed Points
These points from the harsh critic were evaluated and found to not hold up when checked against the paper.

1. **"Factual error: 600,000 bits at 40 dB is wrong"** — The harsh critic claimed the correct value is 65,000–171,000 bits. This assumes a 1-channel representation. However, the experimental setup uses 3-channel representations (the linear embedder produces a "256×256×3 watermark residual," Video Seal's architecture takes 3-channel input, and the handcrafted results in Table 1 at 42 dB give 456,509 bits — consistent only with 3 channels). For a 3-channel 256×256 image, the Bound 3 volume approximation at 40 dB gives ~667,000 bits. The "around 600,000" figure is a reasonable order-of-magnitude estimate; the criticism stems from a channel-count misunderstanding.

2. **"Handcrafted embedder is a lower bound, not a demonstration of feasibility under robustness"** — The handcrafted method is explicitly presented in Section 3.2 within the PSNR-only setting (no robustness requirement), where it is used to falsify hypothesis *D* ("our bounds are wrong"). The paper never claims it addresses robustness. The criticism conflates the PSNR-only and robustness analyses.

3. **"Handcrafted method comparisons conflate PSNR-only and robustness settings"** — The paper's claim that "our bounds are not that far off" (line 418) refers to the PSNR-only bounds in the context of the tiling experiment (32,768 bits achieved vs the ~600,000 bit bound). The handcrafted method (line 505) is also compared to the PSNR-only bound. No conflation occurs.

4. **Formatting, typos, and parser-artifact criticisms** — Removed per hard rules.

## Novel Insights
The harsh critic's observation that the gap between the heuristic robustness bounds (~100,000 bits) and the conservative Bound 13 (~904 bits) spans two orders of magnitude is noteworthy: this uncertainty range is larger than the entire gap between current practice and theory. While the paper is transparent about this, the core argument would benefit from explicitly acknowledging that "how much capacity remains under real robustness constraints" is not yet tightly bounded — the heuristic bounds may significantly overestimate achievable capacity, and the conservative bounds may significantly underestimate it. This is a concrete open problem for future work that the paper partially identifies but could emphasize more.

## Suggestions
1. Correct the "From Figure 3" reference in Section 3.1 to be precise about the image dimensions and provide the explicit bound for the 3-channel 256×256 setting used in the experiments.
2. Add multiple-seed runs for the central Table 1 experiments to demonstrate that the failures at 1024 bits are structural, not stochastic.
3. Either validate the heuristic robustness bounds (Bounds 10–12) in a simplified constructive setting, or reframe the robustness argument to rely primarily on the conservative bound (Bound 13), which already suffices to show a meaningful gap exists.

## Score and Decision

**Calibration Report**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Catch-22 LLM Watermarking | pAeEzS4LwS | 2.67 | R1 | Much weaker — no theoretical capacity analysis, limited empirical scope |
| Adversarial Shallow Watermarking | yI79EvEm8G | 3.00 | R1 | Much weaker — flawed comparisons, reproducibility issues |
| ActiveMark | yy2FLVlaoY | 2.67 | R1 | Much weaker — unrelated topic |
| Model-agnostic Restoration | 4Lop9ReXBP | 2.50 | R1 | Much weaker — narrow scope |
| Watermark-based Attribution | syOYjXqKnS | 4.67 | R2 | Weaker — less novel theory, narrower experiments |
| LatentSeal | TVSPV6D0co | 4.67 | R2 | Weaker — combination of existing works, questionable claims |
| PQIM (Hiding in the Phase) | oTGJZtrprx | 5.00 | R2 | Slightly weaker — good theory but overclaimed results, presentation issues |
| SynthID-Text Analysis | 4AfWqR3quK | 5.50 | R2 | Comparable theory depth but in LLM domain, rejected |
| **This paper** | Ry8jLSYIUG | **6.0** | — | **Target** |
| PAI (Attack-Resistant WM) | wyucYNGPiW | 6.50 | R2 | Stronger experiments but less novel theory |
| PMark | EhDgP69DJG | 7.00 | R2 | Stronger — clean theory and experiments in LLM text domain |

**Bracketing:** Round 1 placed the paper firmly in the mid band (>3.5, <7.5). Round 2 narrowed: the paper is stronger than the 4.67–5.50 anchors (which had weaker theory, overclaimed results, or narrower scope) but not as strong as PMark (7.00) or PAI (6.50), which had cleaner experiments or more comprehensive evaluation. The paper's theoretical novelty is its strongest asset; its main weaknesses are the unvalidated heuristic robustness bounds and the lack of uncertainty quantification for the central experiments. I place it at 6.0 — a solid contribution that makes a genuine theoretical advance and provides convincing evidence for its core claim, despite some methodological looseness.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>