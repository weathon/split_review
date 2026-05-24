Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper empirically investigates neural scaling laws for time series foundation models (TSFMs) across both in-distribution (ID) and out-of-distribution (OOD) settings, examining three scaling axes (model size, compute, data) and comparing encoder-only vs. decoder-only Transformer architectures including two advanced TSFMs (Moirai, Chronos). The study finds that NLL follows an approximate power law in both ID and OOD settings, encoder-only and decoder-only models exhibit similar OOD scalability, and architectural enhancements in Moirai/Chronos primarily improve ID performance but reduce OOD scalability. Based on the fitted exponents, the paper derives practical design principles for scaling TSFMs.

## Strengths

- **First systematic characterization of OOD scaling for TSFMs across three axes.** Prior work (Edwards et al., 2024; Shi et al., 2024a) studied ID scaling only. This paper demonstrates that NLL follows an approximate power law on OOD data as well, with exponents comparable to ID settings (Figures 2–4). This extends the understanding of scaling behavior to the practically relevant OOD regime.

- **Comparative analysis of scaling behavior across architectures under identical training conditions.** The paper trains encoder-only, decoder-only, Moirai, and Chronos variants on the same corpus with the same setup (Figures 5–7), providing the first controlled comparison of how architectural choices affect scaling exponents. The finding that encoder-only models have a slight ID scalability advantage while both architectures exhibit similar OOD scalability is a concrete, reproducible result.

- **Carefully curated pre-training corpus with balancing and quality filtering.** The dataset construction from LOTSA (39 datasets, 7 domains, ~17B time points) with balanced sampling, SNR filtering (>20 dB), and controlled data subsets (10M/100M/1B time points) supports the reliability of the scaling measurements.

- **Actionable design principles grounded in the fitted exponents.** Section 4 derives guidelines such as $D \propto N^{0.8}$ (doubling model size requires ~1.7× more data) and the finding that model size scaling yields greater OOD improvements than ID improvements. These principles are directly traceable to the fitted power laws, providing concrete guidance even if the exponents are small.

## Weaknesses

### Fatal
None.

### Major

- **Inconsistency in training to convergence across experiments.** Parameter scaling results (Section 3.1, Figure 2) report models "trained on the full pre-training corpus to convergence" with "minimum NLL and MAPE." However, compute scaling (Figure 3) and data scaling (Figure 4) report "averaged evaluation results during training" rather than converged final performance. The paper states on line 147 for data scaling: "report the averaged evaluation results during training." This conflates early-training dynamics with asymptotic scaling behavior. For compute scaling in particular, "the optimal results for each compute budget are achieved by different model sizes N, but the lowest loss decreases according to an approximate power law" — the envelope (not individual curves) is fit. This methodological inconsistency means that the compute and data scaling exponents may reflect training speed rather than ultimate convergence behavior, and they should not be treated as equivalent to the parameter scaling exponents.

- **No uncertainty estimates on the central quantitative contribution.** The power-law exponents (Table in Figure 5, equations in Figures 6–7) are the paper's core quantitative output. No error bars, confidence intervals, or bootstrap estimates are provided for any exponent value. The paper acknowledges "significant noise in NLL and MAPE during training" (line 145) and reports differences between architectures as small as 0.001 (encoder 0.027 vs. decoder 0.026 for ID parameter scaling) without any indication of whether these differences are statistically meaningful. Without uncertainty quantification, readers cannot assess whether the claimed ID/OOD or cross-architecture differences in exponents are genuine or within measurement noise.

### Minor

- **Moirai and Chronos retrained from scratch rather than using official pre-trained checkpoints.** The paper states (line 203) that "these models are trained on the dataset we built with the same training setup." Moirai and Chronos involve complex architectural designs (any-variate attention, multi-scale patching, discrete tokenization) that were optimized for large-scale pre-training on specific data distributions. Retraining them from scratch on a differently balanced, potentially smaller corpus may not reflect their inherent scalability. The very small exponents observed for Moirai (ID NLL exponent 0.003 vs. encoder-only's 0.029) and Chronos (0.009 vs. decoder-only's 0.019) could partly reflect suboptimal training conditions rather than fundamental architectural limitations. The paper's conclusion that these models "reduce OOD scalability" should be tempered.

- **"Emergent abilities" claim is weakly supported.** Figure 8 shows three datasets (us births, nm5 daily, australian electricity) where MAPE peaks at intermediate model sizes then drops sharply. The paper labels this as "emergent phenomena" (Section 6.1, Figure 8 caption). With only three examples, no error bars, and no systematic investigation of how many OOD datasets exhibit this pattern vs. follow a smooth power law, this is a suggestive observation at best. The paper's framing as "emergent abilities" overstates the evidentiary basis, though the paper does appropriately describe these as "examples" and "case studies."

- **The scaling exponents are very small, with limited discussion of practical significance.** The NLL power-law exponents for parameter scaling are 0.027–0.032 (compared to ~0.07–0.1 for language models in Kaplan et al., 2020). For data scaling with NLL, the ID exponent is 0.008. These mean that increasing model size 1000× reduces NLL by only ~5–7%, and increasing data 1000× reduces ID NLL by ~1.8%. While the paper reports these findings honestly, it does not discuss what such weak scaling implies for the practical utility of the power-law framework for TSFMs — whether these trends are operationally meaningful or close to the noise floor. This context is important for readers assessing whether the reported "scaling laws" warrant the investment they imply.

### Trivial
None.

## Nice-to-Haves
- Reporting uncertainty (e.g., bootstrap confidence intervals) on the power-law exponents would substantially strengthen the paper's quantitative claims.
- Adding a clearly stated explicit guarantee that the Wu et al. (2023) and Monash OOD test sets are entirely disjoint from the LOTSA-based pre-training corpus (or, if overlap exists, reframing the analysis accordingly).
- Including a limitations section discussing the very small exponents, the convergence inconsistency, and the retraining issue with advanced TSFMs would improve scientific rigor.
- A more systematic investigation of the "emergent" behavior (e.g., how many of the 39 datasets show it, under what conditions) would be needed to substantiate that claim.

## Removed Points
- **OOD test set overlap concern.** The harsh critic claimed the OOD test sets (Wu et al., 2023 benchmark, Monash) may not be truly out-of-distribution because LOTSA might include these datasets. This is a speculative concern — the paper states the OOD tests use "a subset... to test the model's out-of-distribution forecasting capabilities" (line 63) and refers to Appendix A Table 3 for dataset composition details (removed by the parser). The original submission likely contains this information. A criticism that depends on information that the appendix (stripped by the parser) would clarify should not be treated as a verifiable weakness. *Reason for removal: speculative — depends on unverifiable overlap claim about parser-stripped appendix content.*
- **Weak ETS baseline.** The paper uses ETS as a classical reference point to show a threshold effect (~3M parameters needed to outperform it on OOD). This is appropriate framing; ETS is not positioned as a state-of-the-art competitor. *Reason for removal: not a substantive criticism of the paper's claims.*
- **Missing error bars on Figures.** Already covered under the "no uncertainty estimates" Major weakness; this is the same concern, not a separate issue. *Reason for removal: duplicate.*
- **Design principles are standard.** The claim that "model size is the most critical factor" is standard scaling-law advice, but the paper derives it from its own empirical fits rather than asserting it without evidence. This is a valid approach. *Reason for removal: not a weakness — the paper grounds the advice in its own data.*
- **Parameter count formula accuracy for small models.** The harsh critic speculates that the formula may not match empirical parameter counts for models down to 1K parameters. No evidence of discrepancy is provided. *Reason for removal: speculative, not substantiated.*

## Novel Insights

Beyond the paper's own contributions, the reviews surface a notable observation: the reported exponents for TSFM scaling (0.022–0.032 for NLL parameter scaling) are substantially smaller than typical LLM exponents (0.07–0.1), meaning performance gains from scaling are much more marginal. This raises an important question neither the paper nor the reviews fully resolve: whether the "scaling law" framing is appropriate when the effect sizes are so small that a 1000× increase in model size yields a ~5% NLL reduction. The paper's most interesting result may be that TSFMs scale much worse than language models, not that they scale similarly — but this is not the story the paper tells.

## Suggestions

1. **Train all experiments to convergence** or at minimum report the convergence status of each experiment type transparently. The inconsistency between converged parameter scaling and non-converged compute/data scaling is the single largest methodological concern.
2. **Provide bootstrap or seed-based uncertainty estimates** on all reported power-law exponents. Without these, the claimed differences between ID/OOD and between architectures are uninterpretable.
3. **Use official Moirai/Chronos checkpoints** for comparison, or clearly frame the current results as measuring scalability under a *specific training configuration* rather than as a general statement about those architectures.
4. **Either present the emergent abilities observation as preliminary/speculative** (which the paper partially does) or conduct a systematic analysis across all OOD datasets with multiple seeds to establish the phenomenon.
5. **Add a discussion section addressing limitations** — the small exponents, the convergence inconsistency, and the potential implications for whether the scaling-law framework is practically useful for TSFMs at realistic scales.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `/home/wg25r/review_agent/human_reviews/XhdckVyXKg.md` (Wearable Sensing TSFM) | 3.00 | 1 (weak) | Weaker paper — proposed a TSFM without systematic scaling analysis |
| `/home/wg25r/review_agent/human_reviews/2wwPG1wpsu.md` (LST-Bench) | 2.50 | 1 (weak) | Weaker — benchmark paper without scaling analysis |
| `/home/wg25r/review_agent/human_reviews/py3RTHNT6J.md` (Scaling Law Remote Sensing) | 2.20 | 1 (weak) | Weaker — narrower domain, less comprehensive |
| `/home/wg25r/review_agent/human_reviews/UldnqRQWKS.md` (Mixed Quantization Scaling) | 3.00 | 1 (weak) | Weaker — narrower topic (quantization) |
| `/home/wg25r/review_agent/human_reviews/ZkEsEFFUyo.md` (CloudOps Pre-training) | 4.33 | 2 (middle) | Somewhat weaker — focused on dataset contribution with thinner analysis, similar concerns about OOD validity |
| `/home/wg25r/review_agent/human_reviews/nTlzEM1x3B.md` (Frequency-Driven Zero-Shot) | 4.50 | 2 (middle) | Comparable strength — both empirical studies with notable limitations |
| `/home/wg25r/review_agent/human_reviews/YhIpTdrUDY.md` (Adaptive TSFM) | 4.00 | 2 (middle) | Somewhat weaker — narrower scope |
| `/home/wg25r/review_agent/human_reviews/IRL9wUiwab.md` (TSFM Representations) | 6.00 | 2 (middle) | Stronger — cleaner experimental design, but still rejected; reviewed more favorably despite being a "technical report" |
| `/home/wg25r/review_agent/human_reviews/79ZkWgY2FI.md` (Small-to-Large Generalization) | 5.25 | 2 (middle) | Somewhat stronger — clearer message, accepted at a venue with poster |
| `/home/wg25r/review_agent/human_reviews/4Qz9BT4mpM.md` (Agreement-on-the-line) | 5.75 | 2 (middle) | Stronger — cleaner methodology |
| `/home/wg25r/review_agent/human_reviews/LYS3RhIYCq.md` (Scaling Laws IL Games) | 6.20 | 2 (middle) | Stronger — more thorough experiments, clean implementation |
| `/home/wg25r/review_agent/human_reviews/pISLZG7ktL.md` (Data Scaling Robotics) | 8.00 | 1 (strong) | Much stronger — rigorous real-world experiments, clear claims |
| `/home/wg25r/review_agent/human_reviews/Tzh6xAJSll.md` (Associative Memories Scaling) | 7.60 | 1 (strong) | Much stronger — theoretical+empirical contributions |

**Round 1 bracket**: The paper sits between the weak anchors (2–3) and strong anchors (8), within the middle band. Initial bracket: 3.5–6.5.

**Round 2 narrowing**: Compared to middle-band anchors, the paper is stronger than the CloudOps paper (4.33, which primarily contributed datasets) and the adaptive TSFM paper (4.0), comparable to the frequency-driven zero-shot paper (4.5), but weaker than the TSFM representations paper (6.0) and the Small-to-Large generalization paper (5.25) in terms of experimental rigor. The paper's contribution is original and timely, but the methodological inconsistencies (convergence, no uncertainty estimates) and the very small exponents limit its impact.

The paper makes a real contribution — it is the first to systematically study OOD scaling for TSFMs — but the evidence is weakened by the convergence inconsistency in the compute and data scaling experiments, the absence of uncertainty quantification on the central quantitative claims, and the weak effect sizes that are not adequately discussed. These issues are correctable but, as presented, reduce confidence in the findings.

**Final score: 4.5. Decision: Reject.**

A revised version that addresses the convergence consistency, provides uncertainty estimates on exponents, and adds a candid discussion of the small effect sizes could potentially reach 5.5–6.0.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>