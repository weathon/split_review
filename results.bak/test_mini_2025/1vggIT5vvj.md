Now I have all the data I need. Let me synthesize the final review.

**Summary of calibration comparison:**

**Round 1 bracket:** The paper sits between weak anchors (avg ~3.0) and very strong anchors (avg ~8.0). The plausible range from bracketing is **5.5-8.0**.

**Round 2 narrowing:** Directly comparable papers in the same space score 6.0-6.5 (poster level). The current paper is notably stronger than "Interpretable Diffusion via Information Decomposition" (6.0) and "Precise Parameter Localization" (6.2), and comparable or slightly stronger than "Localizing and Editing Knowledge in T2I Models" (6.5). It is slightly weaker than the oral-level "On the Role of Attention Heads in LLM Safety" (7.0) from the LLM domain, which is a fair ceiling since that paper's findings were more surprising and impactful.

The paper's strengths — novel methodology (HRVs), clean validation paradigm, strong downstream results, clear presentation — push it above the 6.0-6.5 poster anchor range. Score: **7.0**.

---

## Summary

This paper introduces Head Relevance Vectors (HRVs) for cross-attention heads in text-to-image diffusion models. HRVs are constructed by generating random images and using argmax over concept-strength scores from cross-attention maps to identify which heads are most relevant to each of 34 human-specified visual concepts. The paper validates HRVs via an ordered weakening analysis (MoRHF vs. LeRHF) and demonstrates three applications: reducing polysemous word misinterpretation (63.0% → 15.9% error rate), enhancing Prompt-to-Prompt image editing (Pareto-optimal CLIP/BG-DINO scores), and improving multi-concept generation over Attend-and-Excite (2-6% relative gains). Generalization to SDXL is also confirmed.

## Strengths

- **Ordered weakening analysis convincingly validates that HRVs capture concept-interpretable features.** The comparison between MoRHF (most-relevant-first) and LeRHF (least-relevant-first) weakening in Figure 3 shows clear qualitative and quantitative differences: target visual concepts degrade significantly faster with MoRHF. This provides direct causal evidence that each element of an HRV reflects the corresponding head's specific relevance to the concept, not just a generic importance signal.

- **Large, practically meaningful reduction in polysemous word misinterpretation.** In a human evaluation across 10 cases × 10 seeds (Section 5.1), SD-HRV reduces the misinterpretation rate from 63.0% to 15.9% — a nearly 4× reduction. This is a concrete, task-level improvement addressing a known failure mode of T2I models, and the effect size is large enough to be credible on its own.

- **HRV-enhanced image editing achieves Pareto-optimal or best-in-class results across five challenging attributes.** For object attributes (Color, Material, Geometric Patterns), P2P-HRV simultaneously achieves the highest CLIP and BG-DINO scores among six baselines (Figure 7). For image attributes (Image Style, Weather Conditions), P2P-HRV obtains the best CLIP scores (0.3424 vs. next-best 0.3286; 0.3348 vs. next-best 0.3046) and receives >2× the human preference votes of the second-best method (Table 1). The experimental setup (500 edited images per target, multiple baselines) is thorough.

- **Generalization to SDXL (1300 CA heads) is confirmed,** showing the method is not architecture-specific. The t-SNE analysis (Figure 10) further demonstrates that HRVs are concept-specific and timestep-invariant, a useful sanity check. The method requires no model modification or fine-tuning, making it practical and reusable.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Multi-concept generation improvements are modest (2-6% relative).** While positive and consistent, the gains over Attend-and-Excite in Section 5.3 are relatively small (Table 2: Full Prompt +4.5%/+2.3%, Min. Object +3.0%/+5.1%, BLIP-score +6.3%/+3.2%). The paper frames this as "mitigating catastrophic neglect," which could give a stronger impression than the empirical magnitude warrants. This does not undermine the paper's core contribution — the multi-concept application is one of three and not the primary selling point — but the framing could be more measured.

- **Missing ablation of key design choices in HRV construction.** The paper uses argmax over concept strengths (rather than softmax or raw CA values) and a weakening factor of -2 without sensitivity analysis. While the argmax is justified for handling cross-head scale differences (Appendix B.2), and the overall results are robust, ablations comparing these choices would clarify the methodology's robustness and design rationale. These are gaps the paper can address without changing its conclusions.

- **Human evaluation details are deferred to the appendix.** The main text reports a misinterpretation rate drop from 63.0% to 15.9% and human preference scores for image editing, but the number of participants, inter-rater reliability, and exact pairwise comparison design are only referenced as being in the appendix. While the effect sizes are large enough that this is unlikely to overturn conclusions, including a brief summary of these details in the main paper would improve self-containedness.

### Trivial

- The exact spatial pooling operation is described as "averaged across spatial dimension (i.e., H²)" which is clear, but the notation uses H for both the number of heads and the spatial dimension, which could cause momentary confusion.

## Nice-to-Haves

- An analysis of whether HRV quality is sensitive to the specific concept-words chosen (e.g., varying the GPT-4o-generated word list and measuring HRV consistency).
- A brief discussion of computational cost (GPU-hours for constructing HRVs from 2,100 images), since practitioners may want to estimate resource requirements.
- A failure-type decomposition for image editing (e.g., does P2P-HRV primarily fix cases where P2P partially succeeds, or does it rescue complete failures?).

## Removed Points

These points were raised by reviewers or synthesizer but are removed per the filtering rules:

- **"Cross-concept scaling concern about argmax":** The critic argued that CA map scales may not be comparable across concepts. However, within a single head, all concept-strength values are computed using the same query Q^(h), so the scales are inherently comparable. The paper also handles multi-token words by averaging across token dimension. This concern reflects a misunderstanding of the method. **Removed (factually incorrect).**

- **"Pooling operation unspecified (average vs. sum)":** The paper explicitly states "averaged across spatial dimension." This is a misreading. **Removed (nitpick).**

- **"Missing human evaluation details (participants, inter-rater agreement)":** The paper states these details are in Appendix D.2, which is stripped by the parser. Per rules, criticisms about missing appendix content are removed. **Removed (parser artifact).**

- **Strength about GPT-4o generating concept-words:** While true, this is a practical implementation choice rather than a scientific strength. The strength of the paper lies in HRV construction and validation, not in the use of an off-the-shelf LLM for word-list generation. **Removed (generic/superficial).**

- **"Missing comparison to newer methods" (from strength finder / generic):** Not raised as a specific weakness but a generic area-of-concern sweep would be removed if present. No such claim was actually made by the reviewers. **Not present in inputs — no action needed.**

## Novel Insights

The reviews add little beyond the paper's own contributions. The ordered weakening analysis design (MoRHF vs. LeRHF) is identified by both the harsh critic and the strength finder as the core validation paradigm, and it is indeed the paper's strongest piece of evidence for HRVs as interpretable features. No reviewer identified a missing connection or reinterpretation of the results that the authors themselves did not already discuss.

## Suggestions

1. Add a brief ablation comparing argmax vs. softmax (or raw values) for HRV construction, and test the weakening factor at one or two alternative values (e.g., -1, -3). This would address the main methodological robustness question.
2. Tone down the framing of the multi-concept results to match their modest magnitude (2-6% relative), or add a discussion of where HRV-based improvements come from in this setting.
3. Include a one-sentence summary of human evaluation design (number of participants, question format) in the main paper rather than deferring entirely to the appendix.

## Score and Decision

**Calibration anchors used:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Interpretable Diffusion via Info. Decomposition | 6.0 (poster) | 1,2 | Weaker: the current paper is better written, has clearer applications, and stronger validation |
| Precise Parameter Localization for Textual Gen. | 6.2 (poster) | 2 | Weaker: similar domain, but current paper has more novel methodology and stronger validation paradigm |
| Localizing and Editing Knowledge in T2I Models | 6.5 (poster) | 1,2 | Similar/comparable: both have mixed reviews on methodology, but current paper's HRV construction is more novel than adapted CMA |
| On the Role of Attention Heads in LLM Safety | 7.0 (oral) | 1,2 | Slightly stronger (oral-level): more surprising findings, but different domain; current paper is comparably rigorous |

**Final score rationale:** The paper is stronger than the 6.0-6.5 poster anchors in the same domain (better presentation, more novel methodology, cleaner validation) but slightly below the oral-level attention-head analysis paper (whose findings were more surprising and had broader implications). Score 7.0 reflects a paper that makes a genuine, well-validated contribution with minor, addressable weaknesses.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>