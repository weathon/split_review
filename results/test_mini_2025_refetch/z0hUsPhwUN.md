Now I have sufficient calibration context. Let me finalize the review.

## Summary

This paper proposes **Control-GIC**, a VQGAN-based generative image compression framework that supports controllable bitrate via multi-granularity coding. The core idea is to assign image patches to fine/medium/coarse granularities based on local entropy, encode only the chosen patches as VQ indices, and use a conditional decoder to reconstruct. The method operates as a single unified model covering a range of bitrates. Experiments compare against generative, variable-rate, and classical compression methods on Kodak, DIV2K, and CLIC2020.

## Strengths

1. **Fine-grained bitrate control with a single model** – Figure 7 convincingly demonstrates that Control-GIC can adjust the bitrate within a range as narrow as 0.001 bpp (from 0.4171 to 0.4172) by varying only the medium-grained ratio, while maintaining nearly constant LPIPS. This directly supports the claim of highly flexible bitrate adaptation using a single unified model.

2. **Competitive rate-distortion-perception performance** – On Kodak (Figure 3) and DIV2K (Figure 4), Control-GIC achieves competitive or superior LPIPS, DISTS, FID, KID, and NIQE against both generative compression methods (HiFiC, MRIC, MS-ILLM, CDC) and variable-rate methods (SCR, CTC), despite these baselines training separate models for each rate point.

3. **Single-model efficiency with fastest inference** – Figure 5 shows Control-GIC requires only 0.6M training steps (single training session) and achieves the lowest encoding/decoding times among all compared methods (7× faster encoding than MS-ILLM, 4× faster than MRIC). This is a genuine practical advantage.

4. **Well-validated decoder design** – Figure 8 provides clean ablation evidence that both medium-grained and fine-grained conditioning in the decoder progressively lower LPIPS, DISTS, and VID, confirming the value of the multi-granularity decoder design.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison with the most directly related prior work** – The introduction mentions that "several methods introduce scalable (Iwai et al., 2024) or variable-rate (Guo et al., 2023) designs into generative models" but these are not included in the experiments. This weakens the novelty claim of being "the first capable of fine-grained bitrate adaptation" in generative compression. The paper compares against fixed-rate generative methods (HiFiC, MRIC, MS-ILLM, CDC) and non-generative variable-rate methods (SCR, CTC), but not against the specific class of variable-rate *generative* methods that are closest to its own approach. The authors should either add these comparisons or clearly explain why they are not feasible (e.g., code not available, different evaluation protocols).

### Minor

1. **Entropy coding comparison uses an asymmetric baseline** – The paper's bitrate calculation relies on a static Huffman table built from training-set frequency statistics, while many generative baselines (HiFiC, MRIC, MS-ILLM) use learned, image-adaptive entropy models. The ablation in Table 1 compares against *uniform-frequency* Huffman (saving up to 5%), but not against a learned entropy model on the same VQ indices (e.g., a small context model or hyperprior). This means the bpp axis may not be perfectly commensurate across methods. Notably, this asymmetry likely *disadvantages* Control-GIC (a more efficient entropy coder would lower its bpp further), so it does not invalidate the results — but it means the reported bitrate values are a conservative upper bound rather than an optimized one. An ablation comparing against a learned entropy model would strengthen confidence in the R-D curves.

2. **The "first" claim is too strong** – The paper states "to our knowledge, this is the first that allows highly flexible and controllable bitrate adaptation" in generative compression. Given the existence of prior variable-rate generative methods (Guo et al., 2023; Iwai et al., 2024), this claim should be qualified more precisely (e.g., "first to achieve sub-0.01 bpp granularity" or "first with this specific granularity-allocation mechanism").

3. **"Probabilistic conditional decoder" is not probabilistic** – The decoder formulation in Eq. (3) uses $\sim p(\cdot)$ notation suggesting a sampling distribution, but the actual computation in Eq. (4) is fully deterministic (a mask-and-replace operation with skip connections). This is a naming/nomenclature issue rather than a technical flaw, but it is misleading.

### Trivial
- The decoder's "nearly minimal-loss reconstruction except quantization" claim (Section 3.2, line 111) is somewhat vague — the masking process itself discards information at unselected granularities, so "minimal-loss" should be scoped to the selected feature locations.

## Nice-to-Haves
- An ablation studying the impact of different training-ratio settings (currently fixed at 50% fine, 40% medium, 10% coarse) on generalization across bitrates would strengthen the method section.
- Reporting variance/error bars on the R-D curves would help assess the robustness of the reported advantages.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Entropy computation underspecified (harsh critic's point #3):** The critic claims the patch size, stride, and entropy formula are missing. The paper explicitly references Appendix A.2 for these details ("See Appendix A.2 for proof of correlation"). Since the parser strips appendices from all papers, this criticism cannot be verified from the available text and is removed per instructions.
- **Missing related works citation (harsh critic):** The critic demands citations for missing related works. Per instructions, missing related works should not be included as I cannot independently verify their relevance.
- **"Fatal/Structural" entropy coding framing:** The harsh critic called the entropy coding issue "structural" and "fatal." As analyzed above, the asymmetry likely disadvantages the proposed method rather than inflating its performance, so this is not fatal. It has been demoted to Minor above.
- **Reproducibility nitpicks (harsh critic):** Criticisms about undisclosed hyperparameters, mask generation details, and thresholding procedures that may be in the appendix are removed per instructions about missing appendix content.
- **Strength Finder generic strengths:** Some strength-finder claims about "superior effectiveness" were generic. The concrete, verified strengths are retained; generic praise about the problem being "important" is removed.
- **Statistical significance / error bars:** The request for confidence intervals on R-D curves is a nice-to-have but not standard for this type of comparison.

## Novel Insights

None beyond the paper's own contributions — the reviews primarily surface verification or qualification of the paper's stated claims rather than uncovering unexpected findings.

## Suggestions

1. **Add a learned entropy model ablation** — Replace the static Huffman coder with a lightweight learned context model (e.g., a PixelCNN or small transformer over VQ indices) and re-measure bpp at a few key rate points. This would either validate or bound the bpp-axis fairness concern.
2. **Compare against or clearly justify omission of variable-rate generative methods** (Guo et al., 2023; Iwai et al., 2024). If code is unavailable, state this explicitly and explain why conceptual comparison still supports the paper's novelty.
3. **Tone down the "first" claim** to precisely describe what aspect of fine-grained control is novel.
4. **Rename or rephrase the "probabilistic conditional decoder"** to reflect its deterministic nature (e.g., "conditional feature-injection decoder").

---

**Evaluation axes:**
- **Originality:** Moderate. Multi-granularity allocation for bitrate control in VQGAN is a novel combination, though the individual components (VQGAN, entropy-based masking, conditional skip connections) are known.
- **Importance:** Moderate-high. Flexible rate adaptation in generative compression is practically valuable.
- **Claims supported:** Mostly yes, with the entropy coding caveat and missing baseline noted above.
- **Soundness:** Reasonable. Experiments are thorough, ablations are meaningful, but the entropy coding confound and missing baselines weaken full confidence.
- **Clarity:** Good. The paper is well-structured and generally clear.
- **Value:** Positive. The single-model efficiency and fine-grained control are useful contributions.

**Round 1 bracket:** After comparing against weak anchors (avg 2.33–3.40 — rejected papers with fundamental flaws), middle anchors (avg 4.25–7.50), and strong anchors (avg 8.00 — oral/spotlight papers with paradigm-shifting contributions), the paper clearly sits in the middle band, between approximately 4 and 7.

**Round 2 narrowing:** Compared against PerCo (ktdETU9JBg.md, avg 6.00, Accept poster) — similar experimental thoroughness, but PerCo had stronger novelty (diffusion decoder for compression) and no entropy coding confound. Compared against DiffPC (RL7PycCtAO.md, avg 5.75, Accept poster) — similar level of contribution and missing-baseline criticism. Control-GIC has an edge in reporting efficiency numbers (Figure 5). Compared against the idempotence paper (Cy5v64DqEF.md, avg 7.50, Accept spotlight) — significantly stronger theoretical contribution. Control-GIC is somewhat below the 7.50 level. Compared against the zero-shot diffusion paper (qi7udwV66M.md, avg 4.25, Withdrawn/Reject) — Control-GIC is clearly stronger.

**Anchor papers retrieved (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| vK8C37eHXM.md | 3.20 | R1 | Weaker — diffusion+autoencoder paper rejected for unclear contribution |
| gIrVoQEDQv.md | 3.40 | R1 | Weaker — NCA compression with limited baselines |
| BJ4WgPgFqJ.md | 2.33 | R1 | Weaker — progressive quantization VAE, withdrawn |
| ktdETU9JBg.md | 6.00 | R1/R2 | Similar — PerCo, accepted poster, more novel but no efficiency analysis |
| 42lcaojZug.md | 6.75 | R1 | Stronger — video rate control with solid practical contribution |
| D5mJSNtUtv.md | 6.00 | R1 | Stronger — FSAR entropy coding with clear practical advantage |
| qi7udwV66M.md | 4.25 | R1/R2 | Weaker — zero-shot diffusion, withdrawn/rejected |
| CxXGvKRDnL.md | 8.00 | R1 | Much stronger — progressive diffusion with universal quantization, oral |
| gzqrANCF4g.md | 8.00 | R1 | Much stronger — tokenizer for visual generation, strong theory |
| RL7PycCtAO.md | 5.75 | R2 | Similar — DiffPC, accepted poster, similar missing-baseline issue |
| Cy5v64DqEF.md | 7.50 | R2 | Stronger — idempotence theory, spotlight accept |
| mb2ryuZ3wz.md | 5.75 | R2 | Similar — adaptive token length, accepted poster |
| ulIW7Frjpn.md | 4.75 | R2 | Weaker — LLM entropy model for transform coding, rejected |
| Z7aq3djHZw.md | 6.25 | R2 | Stronger — JPEG-LM, more original approach, though rejected |

The paper is most comparable to the poster-level papers scoring 5.75–6.00. Control-GIC has some strengths (efficiency reporting, fine-grained control demo) and some weaknesses (entropy coding confound, missing baselines) that place it slightly below the cleanest poster-level papers.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>