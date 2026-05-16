Here is the consolidated final review:

---

## Summary

This paper identifies, characterizes, and demonstrates the consequences of *likelihood displacement* in direct preference learning (DPO and variants) — the counter-intuitive phenomenon where the log-probability of the preferred response *decreases* even as the preference gap widens. The authors show this can be *catastrophic* (probability mass shifting to opposite-meaning tokens) even in maximally simplified settings (single token, single sample). They provide a theoretical analysis via the unconstrained features model, deriving the Centered Hidden Embedding Similarity (CHES) score, which measures how much a preference sample drives displacement. Experiments on three model families (OLMo-1B, Gemma-2B, Llama-3-8B) validate CHES as a strong predictor of displacement. Finally, they demonstrate that likelihood displacement can cause *unintentional unalignment* in safety alignment (refusal rates dropping from 74% to 33%), and that filtering high-CHES samples mitigates this.

---

## Strengths

1. **Demonstrates catastrophic likelihood displacement even in maximally simplified settings.** Table 1 reports that single-token, single-prompt DPO (e.g., preferring `No` over `Never`) can reduce the preferred token's probability by up to 0.96 (Llama-3-8B, from 0.99 to 0.03), and the tokens that increase most are often opposite in meaning to the preferred token (e.g., `Yes`). This directly challenges prior attributions to model capacity, multi-token responses, or SFT phase.

2. **Theoretical analysis pinpoints the role of embedding geometry.** Theorems 1 and 2 (informal versions in Section 4) derive that the instantaneous change in log-probability of the preferred token is governed by (i) the unembedding inner product between preferred and dispreferred tokens, and (ii) the alignment of other token unembeddings with the difference direction. This formally grounds why similar preferences cause displacement and explains shifts to opposite-meaning tokens.

3. **The CHES score accurately identifies training samples that cause likelihood displacement.** Figure 3 (Section 5) shows that for the UltraFeedback dataset, the CHES score ranking perfectly matches the degree of displacement across all three models: higher CHES percentiles produce strictly larger decreases in preferred response log-probability. Edit distance and last-hidden-embedding inner product are not predictive. This validation is done on 512-sample subsets at multiple percentiles with error bars from three runs, and replicated on AlpacaFarm and with IPO.

4. **Exposes that likelihood displacement can cause unintentional unalignment in safety training.** Section 6 reports that training Llama-3-8B-Instruct via DPO on SORRY-Bench (where >70% of samples have two refusal responses) causes the refusal rate to drop from 74.4% to 33.4%. Gemma-2B-IT shows a similar drop (80.5% to 54.8%). This is a concrete, measurable harm where well-intentioned preference learning reduces safety compliance.

5. **Data filtering via length-normalized CHES mitigates unintentional unalignment more effectively than adding an SFT term.** Figure 5 shows that filtering to the 5% of samples with lowest length-normalized CHES scores prevents the refusal rate drop and even boosts refusal rates beyond the starting baseline. Adding an SFT term to the DPO loss also prevents the drop but yields lower final refusal rates. This provides a practically useful, theoretically motivated mitigation strategy.

6. **Consistency across model families and scales.** Core experiments are replicated on OLMo-1B, Gemma-2B, and Llama-3-8B, covering different architectures. The unintentional unalignment is demonstrated on both Gemma-2B-IT and Llama-3-8B-Instruct. The CHES-based findings hold across all settings.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The CHES derivation assumes coefficients are positive without theoretical guarantee.** The CHES score is obtained from Theorem 4 by setting all α coefficients to 1, based on the empirical observation that they are "mostly positive" across three models and two datasets (Section 4.2.2). The paper provides no theoretical reason these coefficients should be non-negative. If some were negative (especially for particular model configurations or data distributions), the CHES–displacement relationship could weaken or reverse for specific samples. This is not fatal because the paper independently validates CHES empirically, but the theoretical grounding of the CHES score is weaker than the rest of the analysis. The authors should either provide a theoretical argument for non-negativity, or report the distribution of coefficient signs more extensively across models, datasets, and training stages.

2. **CHES-based filtering is not compared against a simpler "response-type" filter.** In the SORRY-Bench unalignment experiment (Figure 6), the length-normalized CHES ranking largely separates samples by whether the two responses are of the same type (two refusals or two non-refusals) vs. opposite types. The 5% threshold used for filtering corresponds almost exactly to opposite-type samples. The paper does not ablate whether a simple rule — "keep only samples where one response is a refusal and the other is not" — achieves comparable mitigation. CHES presumably captures additional nuance (e.g., gradations within same-type samples), but this is not demonstrated. Adding this baseline would clarify whether CHES provides value beyond an intuitive heuristic.

3. **The theoretical analysis is validated only through the CHES score's predictive power, not through direct verification of the assumed dynamics.** The paper uses the unconstrained features model to derive CHES, then validates CHES empirically. However, this does not directly verify that the *dynamics* assumed in the theory (gradient flow under the unconstrained model) correctly model the actual training process — only that the resulting similarity measure correlates with displacement. The paper should be more explicit about this inferential gap.

4. **Limited exploration of data efficiency trade-off for CHES filtering.** In the unalignment experiment, filtering keeps only 5% of preference samples. While this works for a safety-specific narrow task, the paper does not discuss how this trade-off would play out in broader alignment scenarios where retaining more data diversity matters. The limitations section touches on this, but the practical feasibility concern deserves more prominence.

### Trivial

1. **Only 5 CHES percentile subsets (0, 25, 50, 75, 100) are evaluated in Figure 3.** Showing additional percentiles or a continuous scatter plot would strengthen the evidence of monotonicity. The current design is still convincing, but finer-grained resolution would be better.

2. **Model sizes only span 1B–8B.** The paper would be strengthened by including a larger model (e.g., 13B+). This does not invalidate the results — the consistency across three diverse model families is already good — but generalizability to very large models is unverified.

3. **Computational cost of CHES is not discussed.** Computing CHES requires a forward pass of the entire dataset through the model. This is not prohibitive, but the paper does not mention whether CHES scores change during training (and whether they need recomputing).

---

## Nice-to-Haves

- A direct ablation comparing CHES-based filtering to a simple "opposite-response-type" filter in the SORRY-Bench experiment would cleanly separate what CHES adds beyond an intuitive rule.
- Extending the model size range (e.g., 13B+) and the number of CHES percentile buckets (e.g., 10 instead of 5) would strengthen the empirical claims.
- A brief experiment showing that in standard instruction-following alignment (where displacement is benign), CHES scores are typically low would help contextualize the results.

---

## Removed Points

- **"The paper does not discuss whether likelihood displacement can be benign most of the time."** — The paper DOES discuss this. Line 422 states "likelihood displacement may often be benign in such settings, and so does not require mitigation." The limitations section (lines 568–570) explicitly says "we do not claim that this occurs universally" and cites successful applications. This criticism is factually wrong.
- **"Missing error bars on some figures" / "error bars denote minimal and maximal values"** — The paper is transparent about its error bar method. The reviewer's own text calls this "acceptable." Not a weakness.
- **"Appendix A is referenced extensively but not available for review"** — The reviewer explicitly says "missing appendix content is not a flaw." Not a weakness.
- **Formatting nitpick about probability vs. log-probability reporting** — The reviewer says "This is not a flaw — both are informative." Not a weakness.

---

## Novel Insights

The reviews together surface a genuinely novel insight beyond the paper's own contributions: that the CHES score may be most valuable not as a black-box filter (since in safety settings it largely recovers the intuitive opposite-response-type rule) but as a *continuous measure* of preference distinctness that could enable more nuanced data curation — e.g., setting adaptive thresholds, weighting samples during training, or guiding response generation toward sufficiently distinct pairs. The paper's current binary filter (keep/discard 5%) under-exploits this possibility. Additionally, the sign-of-coefficients issue points to an interesting open question: can the α coefficients be proven non-negative from properties of the softmax and gradient flow, or do they sometimes flip sign in ways that would suggest the CHES score needs correction terms?

---

## Suggestions

1. **Address the coefficient sign question head-on:** Either provide a theoretical argument (possibly based on the log-softmax derivative structure) that α coefficients are non-negative under gradient flow, or report the empirical distribution of their signs across a wider range of models, datasets, and training checkpoints. Show the robustness of the CHES–displacement correlation when the assumption is violated.
2. **Add a response-type baseline to Section 6:** Compare CHES filtering against a simple rule that keeps only samples with one refusal and one non-refusal. If CHES outperforms this baseline on some metric (e.g., it identifies harmful same-type pairs that the simple rule misses), show this explicitly. If it does not, acknowledge the equivalence and clarify CHES's value in settings where response type is not known or hard to define.
3. **Add more granularity to the CHES validation:** Present a continuous scatter plot of CHES score vs. log-prob change, or use more than 5 percentile buckets, to strengthen the monotonicity claim.
4. **Discuss the data efficiency trade-off of CHES filtering** more prominently — if only 5% of data can be used, what are the implications for general alignment beyond safety?

---

## Score and Decision

**Originality:** High. The paper identifies and theoretically characterizes likelihood displacement in a novel way, separating it from prior attributions.  
**Importance:** High. DPO is widely used, and this explains a known but poorly understood failure mode with practical safety implications.  
**Claims supported:** Mostly. The central claims are well-supported, except the CHES derivation's sign assumption relies on empirical observation rather than proof.  
**Soundness:** Good. Experiments are well-designed, clean, and replicated across models. The few gaps (no response-type baseline, limited coefficient sign analysis) are addressable.  
**Clarity:** Good. The paper is well-structured with effective takeaway boxes, though some sections could be more explicit about inferential gaps.  
**Value to community:** High. Provides both theoretical understanding and practical guidance for data curation.

The paper makes a genuine contribution. Its weaknesses are bounded and addressable; none threaten the core claims. With the clarifications suggested above, this would be a strong paper.

**Score:** 7.5

**Decision:** Accept

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>