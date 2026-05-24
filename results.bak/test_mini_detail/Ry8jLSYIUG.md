Now let me write the consolidated review.

## Summary

This paper presents a geometric analysis of image watermarking capacity, deriving theoretical upper bounds under PSNR constraints (and heuristic/conservative bounds for robustness to linear transformations). It then demonstrates empirically that current neural watermarking models operate far below these bounds — even in the simplest possible setting (single gray image, no augmentations) where models like Video Seal fail to embed 1024 bits while a handcrafted scheme achieves 456,509 bits. As a practical demonstration, the authors train Chunky Seal, a scaled-up Video Seal, achieving 4× capacity (1024 bits) with comparable quality and robustness. The paper argues convincingly that architectural limitations, not fundamental capacity ceilings, are the bottleneck.

## Strengths

1. **Novel theoretical bounds on watermarking capacity under PSNR constraints.** Sections 2.2–2.4 derive clean, rigorous bounds (Bounds 1–9) on the number of embeddable bits under an ℓ₂ (PSNR) constraint, using a geometric box-ball counting approach. The analysis for centered gray images, arbitrary covers, and the demonstration that the penalty from non-centered covers is at most 1 bpp is genuinely original and fills a gap in the literature. For a 256×256 image at 45 dB, these bounds predict ~600,000 bits — orders of magnitude above what any current model delivers.

2. **Clean isolation of architectural underperformance as the root cause.** Section 3.1 trains Video Seal on a single gray image with only an MSE loss and no augmentations — stripping away all real-world complexity. Despite this extreme simplification, Video Seal fails to embed 1024 bits (89.63% bit accuracy at 40.1 dB), whereas a linear layer achieves 100% accuracy at 2048 bits and a handcrafted scheme (Eq. 2) embeds 456,509 bits at 42 dB (Table 1). This experiment cleanly eliminates explanations A–C (robustness/perceptual/data complexity) and isolates the problem to model architecture.

3. **Honest treatment of limitations.** The paper transparently flags that the robustness bounds (Bounds 10–12) are "heuristic" and not guaranteed to be valid lower or upper bounds (Section 2.5), provides a rigorous but very conservative lower bound (Bound 13), and acknowledges that Chunky Seal is too large for practical deployment. This intellectual honesty strengthens the paper's credibility.

4. **Chunky Seal demonstrates that scaling capacity is feasible.** Despite its limitations, Chunky Seal shows that a 4× capacity increase (256 → 1024 bits) is achievable under realistic robustness constraints with comparable image quality (Table 3: PSNR 45.32 vs 44.42 dB, SSIM 0.995 vs 0.996, overall bit accuracy 99.15% vs 99.31%). This provides an existence proof that current capacity levels are not fundamental ceilings.

## Weaknesses

### Major

1. **The headline "orders of magnitude" gap under robustness constraints rests on heuristic, unvalidated bounds.** The paper's most eye-catching claim—that current methods operate orders of magnitude below capacity even under realistic robustness (Figure 1, Figure 4, Abstract)—depends on Bounds 10–12, which are explicitly heuristic. The rigorous lower bound (Bound 13) tells a more modest story: for 75% crop at 42 dB, it gives 904 bits for a 256×256 image (Table 2), only ~3.5× Video Seal's 256 bits. Chunky Seal achieves 1024 bits under a broader set of augmentations, which is above Bound 13 but well below the heuristic predictions (~0.5 bpp, or ~100,000 bits). The paper acknowledges that Bound 13 "is extremely conservative and unrealistic," but the heuristic bounds are never validated as realistic either — they are simply asserted to be "much closer to the true capacity" without evidence. The reader is left uncertain about the true size of the robustness-constrained gap.

2. **Chunky Seal's setup is never compared to a theoretical bound for its specific constraints.** The paper trains Chunky Seal with a combined augmentation set (rotation ≤10°, crop 77–95%, JPEG Q 50–80, brightness/contrast ±50%, etc.) and achieves ~45 dB PSNR. But no theoretical bound is computed for this exact setup. The heuristic bounds in Figure 4 consider individual transformations in isolation (e.g., 30° rotation alone, 75% crop alone), and the conservative bounds in Table 2 are for single transformations at 42 dB. Since Chunky Seal uses a combination of mild augmentations, the relevant bound would be lower than any single-transform bound but is never computed. This leaves a gap in the argument: we cannot say how close Chunky Seal is to the theoretical limit for its own setup.

### Minor

3. **The paper's claims about "orders of magnitude" would benefit from tighter framing.** The abstract states "theoretical capacities are orders of magnitude larger than what current models achieve." This is solidly established for the PSNR-only bound (~2,000× gap for a 256×256 image at 45 dB) but is leveraged into the robustness discussion where the evidence is weaker. The paper would be stronger if it explicitly separated these two regimes in the main claims.

4. **Limited discussion of how the heuristic bounds could overestimate capacity in practice.** Section 2.5 mentions that the heuristic bounds can both under- and over-approximate true capacity (citing Appendix Figures 8 and 9), but the main text and Figure 1 present them as though they are the expected capacity. A quantitative discussion of how much the heuristic bounds might plausibly overestimate — even a rough calibration via the conservative bound — would help readers calibrate their trust.

5. **Missing details that would strengthen reproducibility.** The training augmentations for Chunky Seal are described qualitatively (Table 3 caption mentions "Rotate (≤10°)," "Crop (77–95%)," "JPEG (Q 50–80)," etc.), but the exact augmentation pipeline and sampling distributions are not specified. The number of test images from SA-1B is also not stated. These are minor omissions that should be addressed.

### Trivial

- Table 2 uses "bpp" but the column header could be clearer about whether it refers to the 16×16 or 256×256 image.
- The paper uses "Chunky Seal" in the abstract (line 35) but introduces the name only in Section 4; consider defining it earlier.

## Nice-to-Haves

- Compute a theoretical capacity estimate (heuristic or conservative) for Chunky Seal's specific robustness schedule and PSNR, so readers can judge how close the practical demonstration is to the theory.
- Present the conservative bound (Bound 13) alongside the heuristic bound in the main Figure 1, or at least discuss the range between them explicitly in the main text rather than only in Table 2 in the appendix.
- Apply the proposed sanity checks (Section 5) to Chunky Seal — e.g., verify that capacity scales linearly with image size — to strengthen the argument that these checks are actionable.

## Removed Points

- **Criticism that the paper conflates simplified and realistic settings (merged from Harsh Critic #3):** The paper carefully separates these — Section 3 explicitly tests whether "real-world complexity" explains the gap (ruling out hypotheses A–C), and Section 4 separately demonstrates improvement under realistic constraints. The leap from simplified to realistic settings is not conflated; the paper uses the simplified experiments to isolate the cause, not to prove the size of the realistic gap. This is a careful experimental design, not a conflation.

- **Complaint about missing related work / lack of comparison to specific methods (general filtering):** Not included per protocol — I cannot verify existence of specific related works without external sources.

- **Complaint about reproducibility (hyperparameters not disclosed):** The paper provides learning rate sweeps, λᵢ sweeps, batch sizes, optimizer, epochs, and architecture details. The missing augmentation pipeline details for Chunky Seal are retained as Minor #5 since they are verifiable omissions from the paper.

- **Complaint about statistical significance (number of test images):** Retained as Minor #5 — the paper reports mean and std but should specify N. This is a minor omission, not a fatal flaw.

- **Complaint from Strength Finder about "models likely significantly underperforming" (generic):** Removed as it's a reasonable conclusion from the evidence, not a weakness.

- **Strength Finder claims that are generic ("addressed an important problem"):** Removed — the retained strengths are specific and evidence-grounded.

## Novel Insights

The most striking finding is not simply that current models fall short of theoretical bounds — it is that they fall short *in a setting stripped of every practical complication*. Training Video Seal on a single gray image with only an MSE loss (no augmentations, no perceptual losses, no dataset diversity) still fails at 1024 bits, while a linear layer or a handcrafted scheme succeeds by orders of magnitude. This isolates the failure to the architecture's inability to learn an identity-like mapping, a problem noted in the residual learning literature (the paper cites He et al. 2016 and Hardt & Ma 2017) but newly demonstrated here in the watermarking context. The implication is that better architectural inductive biases — not just scaling — may be needed, which is a more specific and actionable diagnosis than simply observing that "models underperform."

## Suggestions

1. In the revision, explicitly separate the PSNR-only and robustness-constrained claims. The PSNR-only evidence is rigorous and compelling; the robustness-constrained evidence is suggestive but heuristic. Consider rewriting the abstract to say something like "For PSNR-only constraints, theoretical capacities exceed current practice by orders of magnitude. For robustness-constrained settings, heuristic bounds suggest large gaps, but rigorous lower bounds leave the picture less settled."
2. Compute and report a theoretical capacity estimate (at least the heuristic bound, ideally the conservative bound too) for Chunky Seal's exact robustness and quality configuration.
3. Include the conservative Bound 13 in the main Figure 1 alongside the heuristic robustness bounds, or add a separate main-figure panel showing the range between them.

## Score and Decision

**Round 1 bracket:** After reading the paper and comparing against calibration anchors, I initially bracketed the paper between 4 and 7. The weak-band anchors (avg 2.6–3.0, all clearly weaker papers) and strong-band anchors (avg 7.6–8.0, breakthrough-level analysis papers) confirm this.

**Round 2 narrowing:** I compared the paper against:
- **LdIlnsePNt (avg 6.00, Reject):** Theoretical text watermarking paper with statistical bounds and a practical algorithm. That paper was rejected due to weak theory-practice connection, unfair comparisons, and incomplete proofs. The current paper is *stronger*: its theory-experiment connection is cleaner, its limitations are transparently stated, and it does not overclaim.
- **JYu5Flqm9D (avg 5.75, Accept Poster):** Multi-bit LLM watermarking with theoretical formulation. The current paper has stronger theoretical originality and cleaner experiments.
- **UchRjcf4z7 (avg 6.50, Accept Poster):** Transfer attack on image watermarks with solid experiments. The current paper has deeper theoretical contribution but more speculative robustness claims.
- **HexshmBu0P (avg 5.33, Reject):** Recipe paper, clearly weaker in theoretical contribution.

**Final score:** 6.0. The paper has genuine theoretical originality and clean empirical isolation of architectural limitations — a solid contribution. However, the headline claims under robustness constraints rest on heuristic bounds whose quality is acknowledged but not independently validated, and the practical demonstration (Chunky Seal) is never compared to a theoretical bound for its own setup. These issues are addressable in revision but prevent the paper from reaching the 7+ band occupied by more complete analyses. Score 6.0 reflects "marginally above acceptance threshold" — the core contribution is worth publishing with revisions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>