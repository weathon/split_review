Now let me perform the calibration search to appropriately score this paper.**Round 1 bracket: 5.5 – 7.5**

The paper is more analytically rigorous than typical watermarking papers (which score ~5–5.5), but less of a pure methodology breakthrough. Let me narrow the bracket with round 2.Now I have sufficient material to write the final review.Now I have sufficient context to write the comprehensive final review. Let me synthesize everything.

---

## Summary

This paper asks whether current deep learning-based image watermarking methods have saturated their fundamental capacity limits. The authors present a geometric framework that derives theoretical capacity bounds under PSNR and linear robustness constraints, demonstrating that current SOTA methods operate orders-of-magnitude below what theory predicts. Through carefully designed diagnostic experiments—retraining Video Seal on a single gray image with no augmentation—they isolate architectural limitations as the primary bottleneck and rule out data distribution, robustness requirements, and perceptual constraints as explanations. As proof that substantially higher capacity is achievable, they train Chunky Seal, a scaled-up variant of Video Seal delivering 1024 bits (4× Video Seal's 256 bits) with comparable robustness.

---

## Strengths

- **Novel geometric capacity framework (Sections 2.2–2.5):** The paper establishes watermarking capacity bounds from first principles using a three-regime analysis (cube-in-ball, ball-in-cube, non-trivial intersection) for a gray image under a PSNR constraint, and extends to arbitrary cover images (penalty at most 1 bpp). This geometric approach is analytically novel relative to prior information-theoretic literature that assumed Gaussian noise or small perturbations. At 45 dB, the framework yields roughly 2000 bits for a 16×16 image — "orders of magnitude more than the 0.001 bpp we see in practice" (Section 2.3.3).

- **Elegant diagnostic that definitively rules out explanations A/B/C (Section 3.1):** By retraining Video Seal on a single fixed gray image with only MSE loss and no augmentations, the authors reduce the task to its simplest form. The model reaches 100% accuracy at 512 bits but fails at 1024 bits despite theoretical capacity of ~600,000 bits at 40 dB. Furthermore, the 256×256 and 32×32 models show essentially identical performance (Figure 5, Table 1), demonstrating that architecture — not robustness, perceptual constraints, or dataset complexity — is the primary bottleneck.

- **Linear baseline provides a decisive achievability argument (Section 3.2):** A single linear embedder/extractor achieves 100% accuracy at 1024 and 2048 bits within 50 epochs on the same gray image, directly falsifying hypothesis D (bounds are unachievable). This is the most important piece of evidence: if a linear layer trained in 50 epochs can do what Video Seal cannot do in 600 epochs, the bottleneck is clearly architectural.

- **Handcrafted model approaches the theoretical bound (Section 3.2, Table 1):** The hypercube-in-sphere construction achieves 456,509 bits at 42 dB PSNR — roughly 14× the tiling result and close to the analytical bound. This further confirms that the gap cannot be ascribed to the bounds being unrealistic.

- **Conservative lower bounds under robustness (Table 2):** Bound 13 provides a worst-case lower bound that remains meaningful: 904 bits under 75% crop, 14,676 bits under 30° rotation, and 26,757 bits under LinJPEG q=10 — all at 256×256px, 42 dB. Even in the most aggressive settings, the bound is well above SOTA capacity (~256 bits).

- **Data distribution effect bounded to ~0.05 bpp (Section 2.6):** The VQ-VAE/VQGAN argument showing that even an upper bound on the number of perceptually distinct images reduces capacity by only ~0.05 bpp is elegant and uses neural compression codebooks as a proxy in a novel way.

- **Concrete sanity checks proposed (Section 5):** The four proposed sanity checks (capacity linear in image size, capacity decreasing with PSNR, outperforming linear/handcrafted baselines, predictable drops under augmentation) are a practical and reproducible contribution to help steer future model evaluation.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **LPIPS difference significantly understated.** Table 3 reports LPIPS of 0.0085 (Chunky Seal) vs. 0.0019 (Video Seal), a 4.5× difference. The paper's text (Section 4) calls this "only slightly higher LPIPS," which is not an accurate characterization. LPIPS is widely regarded as the most perceptually calibrated of the reported metrics. The claim that Chunky Seal preserves "image quality" while having 4.5× higher LPIPS needs more careful qualification. It is worth noting that PSNR (45.32 vs. 44.42) and SSIM/MS-SSIM are nearly identical, but LPIPS captures structured perceptual artifacts that PSNR misses. The paper's broader argument is not invalidated, but calling a 4.5× LPIPS gap "slight" misrepresents Table 3.

- **Figure 1 presents only heuristic bounds, while the headline "orders of magnitude" claim has varying accuracy depending on setting.** Table 2 (conservative Bound 13 at 42 dB) shows that for aggressive 75% crop, the conservative lower bound is only ~0.005 bpp for 256×256px — approximately 5× above SOTA (≈0.001 bpp), not "orders of magnitude." For rotation 30° the conservative bound is 0.075 bpp (~75× above SOTA), which does support the framing. The paper's body text distinguishes heuristic from conservative bounds clearly (Section 2.5), and Bound 13 is honestly labeled as "extremely conservative." However, Figure 1 — the central visual argument and first impression — plots only the heuristic bounds without indicating this range. Including both, or referencing Table 2 in the caption, would make the visual match the nuance of the main text.

- **Handcrafted model's perceptual quality unreported.** The handcrafted hypercube construction (Equation 2) embeds 456,509 bits at 42 dB by quantizing each pixel to a coarse grid, producing a maximally structured, high-frequency perturbation pattern. While PSNR > 40 dB is confirmed in Table 1, no perceptual metrics (SSIM, LPIPS) are reported for this construction. The handcrafted model is used as the primary evidence that the theoretical bounds are not merely mathematical artifacts ("Bound D is unlikely"). This argument would be strengthened by clarifying whether the bound is only achievable under a PSNR criterion or also under perceptual metrics. The paper acknowledges in Section 5 that "perceptual constraints" are out of scope, but this acknowledgment comes after the handcrafted model has already been used as an empirical anchor.

### Trivial

- **Linear model comparison framing is occasionally loose (Section 3.2):** The paper says the linear model "outperforms Video Seal" without consistently noting this comparison holds only on a fixed gray image with no augmentation — a setting where the linear model degenerates to learning a fixed additive perturbation mask. This framing is appropriate as a *diagnostic* (Video Seal should also be able to overfit this trivial problem), but presenting it as a general comparison could mislead readers about the linear model's generality.

---

## Nice-to-Haves

- **Include Bound 13 (conservative) in Figure 1** alongside the heuristic bounds, with brief explanation in the caption. The paper's argument survives this for most augmentations and for aggressive crop is only slightly weakened. Showing both would make the central visual more honest and harder to dismiss.

- **Report LPIPS (or at minimum SSIM) for the handcrafted model** to clarify whether near-optimal capacity under PSNR alone implies perceptually acceptable watermarking.

- **Add at least one additional high-capacity method to Table 3.** Several methods (MiRRE, WAM, TrustMark) appear in Figure 1 but are absent from Table 3. Readers cannot determine from Figure 1 whether Chunky Seal's 1024-bit capacity with robustness is unique or whether other methods approach it.

- **Report Chunky Seal inference/training time.** With embedder 90× larger and extractor 23× larger than Video Seal, practical deployment requires knowledge of latency overhead. A single-sentence acknowledgment with approximate numbers would suffice, especially since Section 5 mentions the "need for future architectures that deliver both higher capacities and efficiency."

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic concern: "conservative Bound 13 tells a more nuanced story" as a structural flaw.** This is retained as a minor (not major) concern because the paper clearly distinguishes heuristic and conservative bounds in Section 2.5 and Table 2; the issue is that Figure 1 does not show this nuance, which is a presentation issue, not a methodological error.

- **Harsh critic concern: "Video Seal comparison is only valid on a fixed gray image."** This was noted but the paper's framing is actually the correct diagnostic logic — if Video Seal cannot even overfit a trivial fixed problem, the limitation is architectural, not task-specific. The comparison is not presented as a general benchmark; it is presented as a diagnostic. Moved to Trivial.

- **Harsh critic claim about PSNR-only assumptions in handcrafted model.** Partially retained as a minor concern (perceptual quality unreported), but the claim that this "invalidates" the bound is incorrect — the bounds are mathematical and the handcrafted model is a mathematical construction. Downgraded to Minor.

- **Missing related work criticisms.** Removed per hard rule.

- **Reproducibility nitpicks about hyperparameter search.** Removed per hard rule.

---

## Novel Insights

The most genuinely novel observation in this paper is the use of a single-gray-image experiment as a diagnostic tool: by stripping all real-world complexity from Video Seal — fixed image, no augmentations, only MSE loss — the authors have essentially designed a "watermarking IQ test" that any correctly functioning model should pass trivially, and yet Video Seal fails it. The further observation that a 32×32 Video Seal trained on this setup achieves essentially the same capacity as a 256×256 Video Seal — despite having 64× fewer pixels available — is particularly striking. This confirms not just that the model underperforms, but that the architecture fails to exploit spatial dimensionality even under ideal conditions. The VQ-VAE argument bounding the data-distribution effect to ~0.05 bpp is also a clever use of neural compression codebooks as a proxy for image complexity.

---

## Suggestions

1. Replace "only slightly higher LPIPS" with an accurate characterization (e.g., "notably higher LPIPS despite comparable PSNR, SSIM, and MS-SSIM") and add a sentence acknowledging this as a regression the paper does not explain.
2. Add Bound 13 as a second line in Figure 1 (or a shaded band spanning heuristic to conservative), with a legend noting "heuristic bound" vs. "conservative lower bound."
3. Report at least one perceptual quality metric (SSIM or LPIPS) for the handcrafted model in Table 1, even if only a note acknowledging the PSNR-perceptual quality gap.
4. Include inference latency for Chunky Seal in Table 3 or a dedicated table.

---

## Calibration and Score

**Round 1 anchors (bracketing):**
| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| GNN as Noisy Channels | S3zKrEQpRr.md | 3.00 | 1 | Weak analog; unrelated domain; clearly below this paper |
| AI Image Compression adversarial | f47c05mcOj.md | 3.00 | 1 | Narrow scope; clearly below |
| SAT-LDM watermarking | ETFfXGM3e4.md | 5.50 | 1 | Methods paper with limited novelty; somewhat below this paper |
| Watermark Detection Attribution | O08nfMzc93.md | 4.50 | 1 | Less rigorous theoretical analysis; below this paper |
| Recipe for Watermarking | HexshmBu0P.md | 5.33 | 1 | Engineering survey; below this paper |
| SuperMark | T0ebbDO60R.md | 3.75 | 1 | Limited scope; below |
| Lightweight Watermarking | j7b4mm7Ec9.md | 7.60 | 1 | Practical SOTA advances; above or comparable |

**Round 1 bracket: 5.5 – 7.5**

**Round 2 anchors (narrowing):**
| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Undetectable Watermark | jlhBFm7T2J.md | 6.50 | 2 | Novel cryptographic framework; comparable scope; this paper matches or slightly exceeds in analytical rigor |
| Watermarking Theory to Practice | LdIlnsePNt.md | 6.00 | 2 | Theory+practice combo with proof gaps; this paper is clearly stronger (cleaner theory, no proof errors) |
| Theory–Practice Disconnect in NNs | GqI4fTVUXC.md | 6.00 | 2 | Closest structural analog (diagnostic analysis of theory–practice gap); this paper is better structured |
| Scaling Laws for Associative Memories | Tzh6xAJSll.md | 7.60 | 1 | Strong theoretical paper; this paper is comparable in rigor but narrower in scope |

The paper under review is clearly stronger than LdIlnsePNt (6.0) and GqI4fTVUXC (6.0): the theoretical bounds are rigorous, the diagnostic experiments are conclusive, and there are no proof errors. It is comparable to jlhBFm7T2J (6.5, accepted): both combine novel theoretical contribution with empirical validation in the watermarking space, and both have real but minor weaknesses. The paper falls below the lightweight watermarking paper (7.6) because that paper advances practical SOTA more directly, while Chunky Seal is deliberately a proof-of-concept rather than a practical contribution.

**Positioning:** Between jlhBFm7T2J (6.5) and j7b4mm7Ec9 (7.6), but closer to 6.5-7.0. The diagnostic elegance and clean theoretical framework tip this above 6.5. The only verified weaknesses are Minor (LPIPS mischaracterization, Figure 1 heuristic-only bounds, missing handcrafted model perceptual metrics). No major or fatal issues.

**Final score: 7.0, Accept.**

The paper makes a concrete and well-supported case for an important claim: current watermarking models have not saturated capacity, the gap is architectural not fundamental, and 4× capacity increases are achievable. The theoretical framework is original, the experiments are well-designed, and the proposed sanity checks are a lasting practical contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>