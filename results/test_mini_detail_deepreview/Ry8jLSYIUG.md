Now I have a solid calibration. Let me write the final review.

**Round 1 bracket:** I initially bracketed this paper between 5.5 and 7.5 based on the calibration anchors.

**Round 2 narrowing:** After reading anchors in the 6.0–7.5 range, the paper is clearly stronger than ll2nz6qwRG (5.83, Accept — two-stage watermarking, weaker theoretical grounding), 1IwoEFyErz (6.0, Reject — Shallow Diffuse, similar method paper), and comparable to jlhBFm7T2J (6.5, Accept — undetectable watermark, strong theoretical claim but weaker experiments), 16O8GCm8Wn (6.4, Accept — VINE benchmark+method), and UchRjcf4z7 (6.5, Accept — transfer attack). The paper under review has a more fundamental theoretical contribution than these anchors and cleaner diagnostic experiments. The final score of 7.0 positions it above the mid-6 anchor papers.

---

## Summary

This paper investigates whether current deep-learning image watermarking models have saturated the fundamental capacity limits of images. The authors derive geometric bounds on watermarking capacity under PSNR constraints (and, more speculatively, under linear robustness constraints), showing that theoretical capacities are orders of magnitude above what current models achieve. Controlled experiments isolate the bottleneck: Video Seal fails to embed 1024 bits into a single gray image with only a PSNR constraint, while a simple linear model and a handcrafted embedder succeed (the handcrafted model achieves 456,509 bits at 42 dB). The paper then trains Chunky Seal, a scaled-up Video Seal, demonstrating 4× capacity (1024 bits) with comparable quality and robustness. The core contribution is diagnosing that architectural limitations—not fundamental constraints—are the primary cause of the gap.

## Strengths

1. **First rigorous geometric bounds on watermarking capacity under PSNR constraints.** Section 2.3 derives upper bounds (Bounds 3–6) showing that even a 16×16 px image at 45 dB has ~2000 bits of capacity. The bounds are derived from first principles (grid counting, volume approximations, exact lattice point enumeration) and validated against a handcrafted model that nearly matches them. This is a genuinely novel theoretical contribution to the watermarking literature.

2. **Controlled experiments cleanly isolate architecture as the bottleneck.** Section 3.1 shows that Video Seal, retrained on a single gray image with no augmentations, cannot embed 1024 bits at acceptable PSNR (Figure 5, left). A linear model succeeds at 2048 bits (Figure 5, right). The 32×32 tiling experiment (Section 3.2) demonstrates that Video Seal's failure is resolution-independent: the model achieves the same capacity at 32×32 px as at 256×256 px, proving it does not exploit available resolution. These experiments are carefully designed, well-controlled, and directly support the paper's central claim.

3. **Handcrafted embedder nearly matches the theoretical bounds (Section 3.2, Equation 2).** The model achieves 456,509 bits at 42 dB on a 256×256 px gray image (Table 1), ruling out the hypothesis that the bounds themselves are unattainable. This is the strongest piece of evidence that the gap is due to architectural limitations of learned models.

4. **Chunky Seal demonstrates that higher capacity is achievable under realistic constraints.** Table 3 shows 1024-bit capacity with PSNR 45.32 dB, SSIM 0.995, and 99.15% overall bit accuracy across transformations—matching or exceeding Video Seal's quality and robustness. The paper is transparent that this required 90× larger embedder and was achieved without hyperparameter tuning, correctly framing it as a feasibility proof rather than a practical solution.

5. **Honest treatment of limitations.** The paper explicitly acknowledges that the robustness bounds (Bounds 10–12) are heuristic, that Bound 13 is "extremely conservative and unrealistic," and that "our robustness bounds are heuristic rather than formal" (Section 5). This transparency is a strength.

## Weaknesses

### Fatal
None.

### Major

1. **Claims about the robust watermarking gap are overstated relative to the evidence.** The abstract and introduction state that theoretical capacities are "orders of magnitude larger than what current models achieve" without distinguishing between the PSNR-only setting (where the evidence is conclusive) and the robust setting (where the bounds are heuristic). The only validated lower bound (Bound 13) gives 904 bits for Crop&Rescale 75% at 42 dB (Table 2)—Chunky Seal's 1024 bits already exceeds this. For the heuristic bounds (Bounds 10–12), the paper provides no evidence they are attainable; indeed, Chunky Seal's 4× capacity gain with 90× larger model size suggests the heuristic bounds may be far too optimistic. The paper should present the PSNR-only analysis as the primary result and frame the robust claims more cautiously.

2. **Chunky Seal's scaling efficiency is poor, undermining the "headroom" narrative for the robust setting.** The embedder grows 90× (11.0M → 1022.7M parameters) while capacity increases only 4× (256 → 1024 bits). The paper acknowledges this is "not a practical path forward" (Section 5), but the modest improvement relative to the massive scaling weakens the claim that "substantially higher capacities are within reach" under robustness. If the heuristic bounds (~32,768 bits) were realistic, one would expect larger gains from such scaling. The paper's strongest evidence for unused capacity remains in the PSNR-only setting.

### Minor

3. **Only one baseline comparison for Chunky Seal.** Table 3 compares only to Video Seal. Including at least one other SOTA method (e.g., TrustMark, WAM) at their native capacity would strengthen the claim that the capacity gap is not specific to Video Seal.

4. **LPIPS difference (0.0085 vs. 0.0019) is mentioned but not analyzed.** The paper says "only slightly higher LPIPS" (Section 4), but a 4.5× increase warrants discussion of whether this reflects a meaningful quality difference or is negligible in practice.

### Trivial

None.

## Nice-to-Haves

- Compare Chunky Seal with a tiled Video Seal at 1024 bits to show whether a monolithic model is necessary.
- Provide per-attack aggregate metrics (e.g., average over all augmentations) rather than reporting individual rows.
- Include a small experiment showing the capacity–robustness Pareto frontier for Chunky Seal at varying capacities.

## Removed Points

The following points from the reviews were removed:

- **"Bound 13 is relegated to the appendix and not given enough weight"** (Harsh Critic) — **FALSE.** Bound 13 is described in the main text (Section 2.5) and the conservative capacity values are reported in Table 2, which is in the main body.
- **"LPIPS difference is not discussed"** (Harsh Critic) — **FALSE.** The paper states "only slightly higher LPIPS" (Section 4). The discussion is brief but present.
- **"No model has come close to those heuristic values"** (Harsh Critic) — This is a restatement of the paper's own observation, not a weakness. The paper explicitly acknowledges the heuristic bounds may overestimate capacity.
- **"Missing related work"** — Removed per instructions (no external sources to verify).
- **Generic formatting/style nitpicks** — Removed per instructions.
- **Strength Finder strengths that are generic** (e.g., "this paper addressed an important problem") — Removed. Only concrete, evidence-backed strengths retained.
- **"The paper does not address the problem of..." for topics outside the paper's stated scope** — Removed (scope creep).

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses largely confirm the paper's own framing: the PSNR-only analysis is rigorous and convincing, while the robustness analysis is more speculative. The paper's diagnostic methodology (training models in simplified settings to isolate architectural failure) is a methodological contribution that could be applied more broadly.

## Suggestions

1. **Sharpen the claims about robust capacity.** Restructure the paper to present the PSNR-only analysis as the main result ("orders of magnitude gap"). Frame the robust analysis as a more speculative extension, using language like "substantial" rather than "orders of magnitude." Present the conservative Bound 13 results more prominently alongside the heuristic bounds.

2. **Add a direct comparison with at least one other SOTA method in Table 3.** This would strengthen the generalizability of the Chunky Seal results.

3. **Discuss the LPIPS difference** and provide a simple visual comparison or analysis to clarify whether it matters in practice.

4. **Consider adding one more controlled experiment** to diagnose why Video Seal fails: e.g., visualizing the learned residuals, analyzing gradient flow through the U-Net, or testing a shallower architecture. This would make the architectural diagnosis more concrete.

## Score and Decision

**Score: 7.0** — This is a well-motivated paper with a novel theoretical contribution (capacity bounds) and clean, convincing controlled experiments. The core finding—that current models operate far below achievable capacity due to architectural limitations—is significant for the watermarking community. The main weakness is overclaiming on the robust side, where the evidence is weaker. This is correctable in revision. The paper is stronger than mid-6 watermarking method papers (e.g., the undetectable watermark at 6.5, VINE at 6.4) because the theoretical contribution is more fundamental and the diagnostic experiments are more rigorous.

**Decision: Accept**

### Calibration Anchors

**Round 1:**
- S3zKrEQpRr (3.00, Reject) — GNN communication channel metaphor. Much weaker: loose theoretical framing, no direct applicability.
- jbfDg4DgAk (3.00, Reject) — LLM sparse watermarking. Different domain, lower quality.
- Z1E0EahS5w (3.33, Reject) — Reservoir computing bounds. Theoretically grounded but not watermarking.
- Hh0Cg4epYY (2.33, Reject) — Bayes error bounds. Weak theory-practice connection.
- O08nfMzc93 (4.50, Reject) — Watermark detection/attribution. Narrower contribution, weaker experiments.
- ETFfXGM3e4 (5.50, Reject) — SAT-LDM watermarking. Novelty concerns, flawed experiments. This paper is clearly stronger.
- 16O8GCm8Wn (6.40, Accept) — VINE watermarking benchmark+method. Comparable quality, but VINE's contribution is mostly empirical. This paper has stronger theoretical grounding.
- UchRjcf4z7 (6.50, Accept) — Transfer attack on watermarks. Similar quality but different contribution type.
- j7b4mm7Ec9 (7.60, Reject) — Lightweight watermarking. High scores but rejected — likely due to scope/novelty. This paper is more novel.
- EUSkm2sVJ6 (7.60, Accept) — Data usage inference. Not watermarking, not comparable.
- SctfBCLmWo (8.00, Accept) — Dataset bias. Not watermarking, not comparable.
- P7KIGdgW8S (8.00, Accept) — Graph neural network stability. Not watermarking, not comparable.

**Round 2:**
- jlhBFm7T2J (6.50, Accept) — Undetectable watermark. Strong theoretical claim (undetectability) but reviewers flagged robustness issues. This paper has stronger experimental validation of its core claims.
- ll2nz6qwRG (5.83, Accept) — Two-stage robust watermarking. Weaker: no theoretical capacity analysis, straightforward method paper.
- 1IwoEFyErz (6.00, Reject) — Shallow Diffuse. Similar watermarking method paper. This paper is stronger: theoretical contribution + clean diagnostics.
- mDKxlfraAn (6.40, Accept) — Watermark removal. Strong empirical method but no theoretical contribution comparable to this paper.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>