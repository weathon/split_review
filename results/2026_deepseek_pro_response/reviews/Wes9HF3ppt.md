Now I have strong calibration. Let me compile the final review.

**Round 1 bracket:** 5.5 – 7.0

**Round 2 comparisons:**
- "Beyond Autoregression: Discrete Diffusion for Complex Reasoning" (6.25, Accept): Similar structure — non-AR method for planning tasks with strong synthetic results. My paper has more method novelty (new insertion paradigm vs loss reweighting) and broader scope (text + infilling), but weaker evaluation rigor on the text side. Comparable quality.
- "Planned Denoising" (5.75, Accept): Planner+denoiser decomposition for discrete diffusion. My paper is clearly stronger — more fundamental method change, more diagnostic experiments, broader evaluation.
- "Scaling MDMs" (6.50, Accept): Much larger scale (1.1B params) and scaling laws, but modest novelty. My paper has more novelty but less scale and weaker text evaluation.

**Final score: 6.0** — The paper's synthetic experiments and novel insertion paradigm are genuine contributions that the community would benefit from. But the text evaluation problems (pathological MDM baseline, overstated claims, unanalyzed biased objective) are real and significant enough to pull it below a clear accept. A strong rebuttal addressing these could move it to 6.5+.

---

## Summary
This paper introduces Insertion Language Models (ILMs), which generate sequences by iteratively inserting tokens at arbitrary positions — jointly selecting both position and token — rather than generating left-to-right (ARMs) or denoising fixed-length masked sequences (MDMs). The key technical contributions are a biased denoising training objective that avoids high-variance trajectory marginalization, and a single-transformer parameterization with a dedicated stop classifier. On synthetic planning tasks (star graphs, zebra puzzles), ILMs dramatically outperform ARMs and MDMs. On text generation and infilling (LM1B, TinyStories), the results are mixed — ILMs outperform MDMs but trail ARMs, and several evaluation issues complicate interpretation.

## Strengths
- **Star graph experiments cleanly isolate the architectural advantage**: The three-tier difficulty design (easy/medium/hard) systematically varies arm-length variability while holding other properties constant. On Star_easy (fixed-length arms), all models achieve near 100%. On Star_hard (variable arm lengths), MDM accuracy collapses to 21% and ARM to 23% while ILM maintains 99.1% (Table 1). This provides compelling direct evidence for the claimed advantage of iterative insertion with relative positions over MDMs and ARMs.

- **Stopping classifier is a demonstrable improvement over prior insertion-based generation**: The comparison with a re-implemented Insertion Transformer (Stern et al., 2019) on star graphs — IT achieves only 35.2/22.1/17.5 vs ILM's 100/100/99.1 (Table 1) — validates that the dedicated binary stopping classifier is a meaningful architectural contribution. The paper notes IT consistently under- or overshoots target lengths.

- **Zebra puzzle results demonstrate generalization to realistic constraint satisfaction**: ILM achieves 90.0% sequence accuracy, outperforming both ARM (81.2%) and MDM (82.6%), and approaching the oracle-order ARM baseline (ARMO, 91.2%). This extends the out-of-order advantage beyond synthetic graphs to structured reasoning tasks.

- **Infilling evaluation shows practical capability where ARMs cannot compete**: Without specialized training, ARMs cannot perform infilling at all, and MDMs are constrained by fixed-mask-count architecture. ILM achieves better ΔNLL across all three infilling settings (Table 3), with notable gains on multi-segment infilling (ΔNLL_inp = −7.93 for ILM vs. −6.02 for MDM).

- **Clean method and parameterization**: The training objective (Equation 2) and transformer-based architecture (Equations 3–4) are simple and well-motivated. The joint parameterization over insertion position and token using a single backbone with a `<stp>` token for the stop decision is elegant.

## Weaknesses

### Fatal
None.

### Major
- **MDM text-generation baseline appears pathological, undermining the ILM > MDM text claim**: In Table 2, the MDM generates sequences averaging 985 tokens on Stories (dataset mean: 205) and 85 tokens on LM1B (dataset mean: 28). Since sequences are padded to 1024 for Stories, this indicates the MDM is unmasking nearly every possible position — its stop mechanism is not functioning properly. The paper notes the length anomaly in passing ("the MDM produces longer sequences," line 215) but does not investigate, diagnose, or acknowledge that this is a baseline failure rather than a model property. When the baseline produces outputs 4–5× the expected length, the claim that ILM outperforms MDM on text quality carries limited information. The ILM's advantages on planning tasks do not depend on this comparison, but the text-generation case for ILM is weakened.

- **"On par with ARMs" claim in the abstract is overstated**: The abstract claims ILMs "perform on par with ARMs." On LM1B, ARM achieves NLL 3.94 vs. ILM's 4.67 — an 18.5% relative gap that is not "on par." The body text is more measured ("slightly worse than ARMs," line 251; "competitive with ARMs," line 20), but the abstract inflates the claim beyond what the evidence supports. The gap on Stories is small (2.11 vs. 2.14), but ILM generates sequences 40% shorter than ARM (119 vs. 201 tokens), introducing a length confound: shorter sequences may be easier to make coherent, so the Prometheus judge results (Figure 5) cannot be interpreted cleanly as a quality win.

- **Biased training objective is never analyzed**: Section 3 explicitly states the training objective is biased ("we use a biased training objective that makes direct use of all the dropped tokens"). The justification is that the unbiased estimator has high variance (deferred to Appendix D, which is stripped). Yet the paper provides no characterization of what kind of bias is introduced, whether the objective corresponds to a consistent estimator of any well-defined target distribution, or under what conditions the bias might be problematic. For a method paper whose core training procedure departs from an unbiased estimator, this is a significant gap. At minimum, a discussion of the bias-variance tradeoff (or a small-scale empirical comparison against the unbiased estimator) is needed for others to confidently adopt the method.

### Minor
- **RoPE vs. "absolute position" explanation is imprecise**: The paper states MDMs use the DDiT architecture with RoPE (line 133), which encodes relative positions. Yet the explanation for MDM's star-graph failure says MDMs "work with absolute token positions" (line 147). The real issue is more subtle: even with RoPE, MDMs predict tokens at fixed position slots, so when arm lengths vary the same position index maps to different semantic content. The explanation needs clarification.

- **α_Duo is undefined in the body text**: Table 3 labels the ILM variant as "ILM α_Duo" but α_Duo is never introduced or explained anywhere in the body of the paper. The reader cannot interpret what variant of ILM inference is being evaluated for infilling.

- **ΔNLL obscures absolute quality in infilling evaluation**: Table 3 reports only percentage changes, making it impossible to assess whether the absolute quality of infilled text is reasonable. A 20% increase over a very low baseline differs from a 20% increase over a high baseline.

- **Evaluation sample counts not reported for unconditional generation**: The infilling evaluation specifies sample counts (3500 for LM1B, 3300 for TinyStories) but unconditional generation does not.

### Trivial
- **Figure 6 color-label mismatch**: The inline text (line 215) refers to "ILM (blue)" but the figure's apparent coloring (per the parser-extracted alt text) shows ILM as green and ARM as blue. This suggests the figure was revised without updating inline text references.

## Nice-to-Haves
- Include error bars or at minimum report the number of evaluation samples used for unconditional generation.
- Add a controlled small-scale comparison of the biased vs. unbiased training objective (e.g., on the star graph task) to characterize the bias empirically.
- Report absolute NLL alongside ΔNLL in the infilling evaluation.
- Control for sequence length in text quality evaluation by reporting metrics stratified by generated length.
- Compare against the Insertion Transformer on text tasks, not just synthetic.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"empirical valuation" typo**: Formatting artifact / minor typo, not a substantive weakness.
- **Missing comparison with XLNet-style order-agnostic models**: Cannot verify whether this is relevant without external sources; removed per policy.
- **No variance estimates / error bars flagged as major**: For language modeling benchmarks at this scale, single-run evaluation is standard. Moved to Nice-to-Haves.
- **"Missing Parts" about appendix**: The parser strips appendices; these exist in the original submission.
- **"Missing related works"**: Cannot verify existence of specific related works from external sources; removed per policy.

## Novel Insights
The star graph experiments provide a crisp diagnostic that isolates a specific structural limitation of MDMs — reliance on fixed-position slots — that is distinct from the better-known simultaneous-unmasking problem. The three-tier design shows that MDMs fail specifically when position-to-content mapping becomes variable (different arm lengths shift which position indices correspond to the junction/target nodes), even with RoPE-based architectures. This is a clean empirical demonstration that complements the paper's theoretical motivation and offers a reusable evaluation framework for future non-autoregressive generation methods.

## Suggestions
- Diagnose and fix the MDM text-generation baseline, or explicitly acknowledge that the MDM's length-control failure at this scale prevents a fair text-quality comparison, and reframe the text-generation story accordingly.
- Tone down the abstract's "on par with ARMs" claim to match the more measured language in the body ("competitive with" or "slightly worse than").
- Add a paragraph discussing the nature of the bias in the training objective — what distribution the model is actually learning to approximate — and ideally provide one small-scale empirical comparison against the unbiased estimator.
- Define α_Duo and explain the infilling inference procedure clearly in Section 5.3.2.
- Reconcile the RoPE usage with the "absolute token positions" explanation for MDM failure on star graphs.

## Anchor Comparisons
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Reparameterized Discrete Diffusion for Text (1pTlvxIfuV) | 5.50 | R1 | My paper has stronger synthetic results, broader scope, and more fundamental novelty |
| Think while You Generate: DDPD (MJNywBdSDy) | 5.75 | R2 | My paper is clearly stronger — more fundamental method change, more diagnostic experiments |
| Beyond Autoregression: Discrete Diffusion for Planning (NRYgUzSPZz) | 6.25 | R2 | Closest match. Both have strong planning results. My paper has more method novelty and broader scope, but weaker text evaluation rigor |
| Scaling up MDMs on Text (WNvvwK0tut) | 6.50 | R1 | That paper has larger scale and scaling laws. My paper has more novelty but weaker evaluation |
| SEDD (71mqtQdKB9) | 6.60 | R1 | SEDD has stronger text results and a principled loss. My paper has more novelty in generation paradigm but weaker text evaluation |
| Interpolating AR and Diffusion LLMs (tyEyYT267x) | 8.00 | R1 | Clearly stronger — SOTA results, principled framework, comprehensive evaluation. My paper is not in this tier |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>