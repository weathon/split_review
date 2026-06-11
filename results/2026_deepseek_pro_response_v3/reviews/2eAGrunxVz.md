Now let me finalize my analysis. Let me compare systematically:

- **PRC Watermark (6.50):** This paper is the direct predecessor — our paper explicitly improves on it. PRC was accepted but had significant weaknesses: robustness inferior to Gaussian Shading under heavy perturbations, marginal metric improvements, concerns about image content changes. Our paper directly addresses these: 4 orders of magnitude faster extraction, better robustness at high capacities, cleaner theoretical foundation (spherical 3-design vs. cryptographic PRC), encryption-free design, and more comprehensive evaluation including WEvade adversarial attacks and solver/timestep ablations.

- **TabWak (7.20):** First watermark for tabular diffusion models. Solid theoretical guarantees and thorough evaluation. However, reviewers noted it underperforms Gaussian Shading on most datasets. Our paper matches or outperforms all baselines across the board and has a cleaner theoretical chain (3-wise independence → spherical 3-design → approximate Gaussian).

Spherical Watermark is clearly stronger than PRC Watermark (6.50) and comparable to or slightly better than TabWak (7.20) — it enters a more competitive domain but with stronger results and a more elegant construction. I place the final score at **7.5**.

Now let me write the final review.

---

## Summary
The paper proposes Spherical Watermark, a lossless watermarking framework for diffusion models that embeds binary watermarks into the Gaussian latent noise without per-image key storage. The core insight is a three-stage reversible mapping: (1) binary embedding that mixes repeated watermark bits with random padding via an invertible matrix to produce a 3-wise independent bitstream, (2) projection onto the unit sphere followed by orthogonal rotation to create a spherical 3-design, and (3) chi-squared scaling to match the Gaussian prior up to third-order moments. Experiments on Stable Diffusion v1.5/v2.1 show near-identical FID, classifier-based undetectability at chance level, extraction ~4 orders of magnitude faster than PRC Watermark, and superior robustness under adversarial attacks.

## Strengths
- **Novel, theoretically grounded construction**: The chain of lemmas (Theorem 3.1 → Theorem 3.2 → Lemma 3.3 → Lemma 3.4) building from 3-wise independent bits to spherical 3-design to approximate Gaussian recovery is elegant and distinguishes the method from prior heuristic or purely cryptographic approaches (Section 3.3).
- **Encryption-free design with zero per-image key storage**: The Signature (T, C) is fixed and secret at runtime; random padding bits r provide per-image variability. This directly addresses the key-management bottleneck of Gaussian Shading (Section 3.2).
- **Near-identical FID and classifier-based undetectability**: Table 1 shows FID scores essentially indistinguishable from unwatermarked generation across SD v1.5 and v2.1 on both COCO and SDP (e.g., 48.1224 vs. 48.1256 on SD v1.5/COCO). Figure 2 confirms latent-level and image-level classifiers achieve near-chance (~50%) accuracy, while Tree-Ring and Gaussian Shading are detected at 97–100%.
- **Extraction speed roughly four orders of magnitude faster than PRC Watermark**: Figure 4 shows PRC extraction at ~10¹ seconds vs. ~10⁻³·⁵ seconds for Spherical Watermark, eliminating the belief-propagation decoding bottleneck (Section 4.2).
- **Superior adversarial robustness over competing lossless methods**: Table 2 shows 98.12% ACC and 99.83% TPR under WEvade attacks, outperforming Gaussian Shading (88.06% ACC) and PRC Watermark (97.69% ACC, 95.38% TPR) (Section 4.2).
- **Comprehensive ablation studies**: Module ablation (Figure 6b-c) confirms both binary embedding and spherical mapping are essential; parameter ablation (Table 3) quantifies the s–N trade-off; solver and timestep ablations (Tables 4–5) show robustness across DDIM, PNDM, and DPM-Solver++ and timestep counts from 10–50 (Section 4.3).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Theoretical framing drifts between precise and overstated language**: The abstract is carefully calibrated — "prove…up to third-order moments" and "empirically demonstrate…statistically indistinguishable." But the introduction (lines 26, 28) claims the paper "prove[s] that the final noise is statistically indistinguishable from standard Gaussian noise." Since what is proved is moment-matching to degree 3 (spherical 3-design), not statistical indistinguishability in the cryptographic sense of Equation (2), this overstatement should be corrected. The Discussion (line 332) correctly notes that "higher-order moments may deviate from the true prior." The remedy is simple: harmonize the introduction language to match the abstract's precision.
- **The l_c ≠ l_x case is gestured at but never resolved**: The paper introduces C as l_c × l_c (line 113), then sets l_c = l_x "for notational convenience," and a footnote says "in practice, l_c is chosen as a factor of l_x (e.g., l_c = floor(sqrt(l_x))) to balance rotational expressiveness with computational and storage efficiency" (line 121). If l_c = 128 when l_x = 16384, how does C operate on the full 16384-dimensional vector z^(2)? The theoretical analysis assumes l_c = l_x throughout. This gap makes the practical deployment procedure unclear and should be resolved.
- **Gaussian Shading baseline results need clearer framing**: The paper notes that "with fixed keys, Gaussian Shading no longer achieves true losslessness" (line 193), but the undetectability results (Figure 2, 100%/97% detection) could be misinterpreted as Gaussian Shading being an inherently worse method. The comparison actually tests a specific architectural property — whether a scheme remains undetectable without per-image randomness — which is exactly the paper's claimed contribution. The paper should state explicitly whether the nonce is also fixed or omitted, and frame the result as demonstrating this architectural advantage.
- **The gap between Lemma 3.4 and the actual construction could confuse readers**: Lemma 3.4 states an exact equivalence requiring u to be uniformly distributed on the sphere, but z^(3) is a spherical 3-design, not uniform. The text uses "≈" (line 177) to acknowledge this, but presenting Lemma 3.4 as an exact statement whose hypotheses are not fully met could mislead. A brief remark in the text clarifying the gap between the 3-design and full uniformity would help.
- **Computational efficiency numbers are approximate**: The extraction time comparison reports "roughly four orders of magnitude" from a log-scale bar chart (Figure 4), with approximate values of ~10¹ s (PRC) and ~10⁻³·⁵ s (Spherical Watermark). A table with precise means, standard deviations, and hardware details would make the claim independently evaluable.

### Trivial
- The Discussion section (line 332) acknowledges the higher-order moment deviation but does not connect back to the theoretical analysis or discuss what practical consequences, if any, this could have for undetectability.
- Section 4.1 places 32-bit traditional methods and 512-bit latent methods in the same Table 2; a note clarifying the capacity asymmetry would prevent potential misinterpretation of cross-group accuracy comparisons.

## Nice-to-Haves
- Harmonize the theoretical narrative: use "provably matches the Gaussian prior up to third-order moments" in the introduction, reserving "statistically indistinguishable" for the empirical demonstration with classifiers.
- Resolve the l_c ≠ l_x case in the main text or commit to l_c = l_x throughout and remove the distracting footnote.
- Tabulate exact timing numbers (mean, std dev, hardware) for embedding and extraction.
- Brief discussion of security under key leakage (what if T or C is exposed?).
- More formal error-propagation model for parameter s beyond the empirical analysis in Table 3.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **HC: "The proof for Theorem 3.1 must handle shared padding bits"** — Speculative; the proof is in the stripped Appendix C. Without access to it, we cannot assert a flaw. Removed.
- **HC: "PRC error floor connection to watermarking is not explained in Related Works"** — This is foreshadowing in Related Works; the experiments do demonstrate PRC failure modes. Not a substantive weakness. Removed.
- **HC: "WEvade adaptation details are missing"** — The paper references Appendix F.4, which was stripped by the parser. Not a paper flaw. Removed.
- **HC: "~10 seconds for PRC belief-propagation seems suspiciously high"** and **"~0.0003 seconds for matrix operations seems optimistic"** — Speculative hardware/implementation claims. Removed.
- **HC: "The abstract says 'recover exact multivariate Gaussian noise' which overpromises"** — The abstract actually says "recover exact multivariate Gaussian noise" in the context of the method description, not as a theoretical claim. The theoretical claim is separately stated as "up to third-order moments." The abstract is precise. Removed.
- **HC: "The critique of PRC in the introduction (lines 17–24) is asserted without qualification"** — The experiments bear out the claim; the introduction previews empirical findings, which is standard practice. Removed.
- **SF: Generic strengths** (e.g., "the paper addressed an important problem") — Filtered; only concrete, evidence-backed strengths retained.

## Novel Insights
The paper's decomposition of Gaussian sampling into (1) a discrete mixing step producing 3-wise independent bits, (2) projection to a spherical 3-design, (3) rotation, and (4) chi-squared scaling is a genuinely novel approach to the lossless watermarking problem. The insight that a spherical 3-design — rather than full uniformity — suffices for practical undetectability (as demonstrated by classifier-indistinguishability) is valuable and could inform future work on distribution-preserving embeddings beyond watermarking.

## Suggestions
- Harmonize the theoretical claims: use "provably matches the Gaussian prior up to third-order moments" in the introduction, reserving "statistically indistinguishable" for the empirical demonstration with classifiers.
- Either resolve the l_c ≠ l_x case in the main text or commit to l_c = l_x throughout all descriptions and experiments, and remove the distracting footnote.
- Add a short paragraph in the Discussion connecting the higher-order moment deviation back to the spherical 3-design definition and explaining why this gap does not harm undetectability in practice.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
| Path | Avg Score | Band | Comparison |
|------|-----------|------|------------|
| `jlhBFm7T2J` (PRC Watermark) | 6.50 | 6.0–7.5 | Direct predecessor; our paper improves on nearly every dimension (speed, robustness, simplicity) |
| `ll2nz6qwRG` (Hidden in the Noise/WIND) | 5.83 | 4.5–6.1 | Related latent-noise watermarking; our evaluation is more comprehensive and our method has stronger theory |
| `T0ebbDO60R` (SuperMark) | 3.75 | 2.5–4.5 | Training-free watermarking via super-resolution; different approach, weaker results |
| `9XEBFywIW7` (Spread them Apart) | 4.40 | 2.5–4.5 | Inference-time watermarking with robustness guarantees; less comprehensive evaluation |

**Round 2 (Narrowing):**
| Path | Avg Score | Band | Comparison |
|------|-----------|------|------------|
| `71pur4y8gs` (TabWak) | 7.20 | 6.5–8.5 | Similar approach for tabular data; our paper has stronger relative performance vs. baselines and cleaner theory |
| `j7b4mm7Ec9` (Lightweight Deep Watermarking) | 7.60 | 7.0–8.5 | Different paradigm (encoder-decoder); not directly comparable |
| `ujpAYpFDEA` (Watermarked LLMs) | 7.50 | 7.0–8.5 | LLM watermarking; different domain |

**Round 1 Bracket:** 6.5–8.0

**Final Score Rationale:** This paper is clearly stronger than PRC Watermark (6.50), which it directly improves upon. It is comparable to TabWak (7.20) — both have strong theoretical foundations and thorough evaluation in their respective domains — but Spherical Watermark outperforms its baselines more consistently and has a cleaner theoretical chain. The weaknesses are limited to framing/clarity issues that are straightforward to fix. The paper does not reach the 8.0+ tier (where papers tend to have no significant weaknesses and paradigm-shifting contributions), but it is a solid, well-executed contribution. Score: **7.5**.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>