Now I have a thorough understanding of both the paper and the calibration anchors. Let me write the consolidated review.

## Summary

This paper studies data contamination in LLM training through controlled experiments (training models from scratch with deliberately inserted benchmark data) and a theoretical analysis of forgetting via AdamW weight decay. The key empirical finding is that when models are trained well beyond Chinchilla-optimal token counts (≥5× Chinchilla), even high-repetition contamination (up to 144×) can be completely forgotten. A theoretical bound (Proposition 1) links forgetting to cumulative weight decay, and the paper shows empirical forgetting is faster than this bound. The analysis is then extrapolated via theory to suggest that large models like OLMo-7B and Llama 3 405B have forgotten early-training data.

## Strengths

1. **Systematic three-dimensional scaling experiments.** Section 4.1 and Figure 2 cleanly separate the effects of model size (up to 1.6B), training tokens (up to 15× Chinchilla), and repetition count (4×–144×). The finding that 12× repeated contamination becomes indistinguishable from holdout at 15× Chinchilla (Figure 2b) is a concrete, well-supported result with direct practical implications.

2. **Demonstration that complete forgetting is possible with novel data.** Section 4.2 (Figures 3a–3c) shows that after 7 Chinchilla of continued training on novel data, even 144× repeated contamination is fully forgotten (accuracy gap within confidence intervals of zero). The controlled comparison in Figure 3d (repeated same 100M tokens) isolates that *novel data*, not just time, drives forgetting — a refinement over the stabilization result of Tirumala et al. (2022).

3. **Weight-decay-based forgetting bound with practical calibration.** Proposition 1 and equation (3) give an explicit bound on how many AdamW steps are needed to decay a past gradient contribution below ε. The comparison in Figures 6c–d shows empirical forgetting is *faster* than this bound, establishing it as a safe overestimate that practitioners can use conservatively.

4. **Near-duplicate filtering across benchmarks.** Section 3.3 documents and removes cross-benchmark near-duplicates (e.g., ARC-Easy/MMLU) using Levenshtein-distance filtering, addressing a confound that prior contamination work often overlooks.

## Weaknesses

### Fatal
None.

### Major

1. **Abstract and introduction overclaim about large models based on theory alone.** The abstract states that "many LLMs, including Llama 3, have forgotten the data seen at the beginning of training." The largest model trained from scratch is 1.6B parameters; the OLMo-1B experiment tracks only ~0.3% of the remaining pretraining (2000/370,000+ steps). The analysis for OLMo-7B and Llama 3 405B (Section 5.1, Figure 5) is purely theoretical — it computes cumulative weight decay from assumed hyperparameters. As the paper itself acknowledges (lines 261–262), weight decay shrinking the gradient vector is a *necessary* condition for forgetting, not a sufficient one: later gradient updates could align with early ones and preserve the learned information. The paper presents this limitation in Section 5.1 but then states the strong claim without this caveat in the abstract and introduction. This is a gap between the headline claim and the evidence.

2. **The definition of "forgotten" is inconsistent across sections.** In the scaling/forgetting experiments (Section 4.2, Figure 3c), "forgotten" means the accuracy gap is within the confidence interval of zero. In the theoretical section (Proposition 1), it means the gradient contribution is decayed below some ε. These are different criteria — accuracy recovery and gradient decay are related but not identical. The paper moves between them without commenting on the disconnect.

### Minor

1. **OLMo-1B forgetting is only tracked over ~1% of remaining training.** The OLMo-1B experiment (Section 4.3) shows a 96% reduction in the accuracy gap over 2000 steps but does not track whether accuracy fully returns to baseline. The claim that this trajectory extrapolates to "less than 1% of the total forgetting" (line 213) is an extrapolation; the actual end-of-training values are not measured. A follow-up checkpoint further along training would have substantiated the claim.

2. **The gap between empirical forgetting and the weight-decay bound is acknowledged but not explained.** The paper shows (Figures 6c–d) that empirical forgetting is faster than the theoretical bound, and Section 4.2 demonstrates that novel data drives this. However, what fraction of the gap is due to gradient cancellation versus representation drift versus other factors is not analyzed. The theory (Proposition 1, equation 3) isolates weight decay as the sole mechanism, so any additional forgetting from gradient interference is outside the model — making it unclear when the bound is tight and when it is loose for new architectures or data distributions.

3. **No experiment tracks full recovery to baseline for any model.** In the 124M forgetting experiment (Section 4.2), accuracy gaps are shown to be within confidence intervals of zero after 7 Chinchilla of additional training. But the paper does not check whether the cross-entropy loss gap also fully closes, or whether the weight-decay bound is consistent with the observed trajectory. A simple check of whether the observed trajectory is on track to meet the bound would strengthen the connection between theory and experiment.

### Trivial

- Figure 5 caption uses "decline" instead of "decile" (line 248).
- Section 3.2's footnote on contamination levels is referenced before the footnote is introduced.

## Nice-to-Haves

- A systematic exploration of how different learning rate schedules (cosine vs. constant vs. cosine with warmup) affect the forgetting bound in Figures 5 and 6 would make the theory more broadly applicable.
- An empirical check on an existing OLMo-7B checkpoint (contaminating and tracking for even a small fraction of remaining training) would directly support the 7B-scale claims that currently rest on theory alone.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Proposition 1 is not a novel mathematical result"** — This is an opinion about the nature of the theoretical contribution, not a verifiable weakness. The paper presents it as a conceptual bridge and derives it from the AdamW equations; novelty judgments vary across reviewers.
- **"The text should say 'suggests' rather than 'means'"** (regarding OLMo-1B extrapolation) — A stylistic word-choice preference that falls below the threshold for a substantive weakness.
- **"1.6B model plateau could be noted more"** (Section 4.1) — A minor presentational suggestion, acknowledged in the paper already as a non-monotonic pattern.
- **"The paper could benefit from a discussion of catastrophic forgetting"** — The paper explicitly distinguishes catastrophic forgetting from the natural forgetting it studies (Section 2, lines 38–43). The distinction is already drawn.
- **Strength Finder: generic strengths about "an important problem"** — Dropped per filtering rules. Only concrete, evidence-backed strengths are retained.
- **Strength Finder: strengths that conflict with verified weaknesses** — No such conflicts detected.

## Novel Insights

The reviewers' primary novel observation beyond the paper's own claims is that the disconnect between the abstract's strong assertion about Llama 3 and the actual empirical evidence constitutes a pattern of overclaiming that masks the paper's genuine contributions. The empirical scaling experiments and the weight-decay bound are solid; they would be better served by presenting the large-model extrapolation as a hypothesis or approximate bound rather than a concluded finding. This is a presentation/claim-calibration issue rather than a methodological flaw.

## Suggestions

1. **Tone down the abstract and introduction claims about Llama 3 and OLMo-7B.** Rephrase "have forgotten" to "our theoretical analysis suggests they may have forgotten" or "the weight-decay bound indicates they likely have forgotten." This preserves the insight while matching the evidence.

2. **Add an explicit check of the weight-decay bound against the observed trajectory** in the 124M forgetting experiment (Section 4.2). This would validate whether the empirical trajectory is on track to meet the bound, supporting the claim that the bound is a safe overestimate.

3. **Harmonize the definition of "forgotten"** across the experimental and theoretical sections, or at minimum add a sentence acknowledging the different criteria and why they are both meaningful.

4. **Track at least one OLMo-1B checkpoint later in training** to verify that the accuracy gap continues to close toward baseline.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak band (avg < 3.5): "Language Models for Textual Data Valuation" (avg 2.00, Withdrawn) — substantially weaker in scope and evidence. The current paper is clearly stronger.
- Middle band (3.5–7.5): "Time Travel in LLMs: Tracing Data Contamination" (avg 7.00, Accept spotlight) — similar contamination topic, strong method paper with clean claims. Current paper is slightly weaker due to overclaiming. "To the Cutoff... and Beyond?" (avg 6.75, Accept poster) — clean natural experiment, no overclaiming. Comparable scope but cleaner claims. "Elephants Never Forget" (avg 4.75, Reject) — weaker methodology; current paper is clearly stronger.
- Strong band (avg > 7.5): "Cheating Automatic LLM Benchmarks" (avg 7.75, Oral) — higher-impact paper with tight claims; current paper is not at this level.

**Round 2 (Narrowing, bracket 5–7.5):**
- "Spectral Dynamics of Weights" (avg 6.25, Reject) — interesting analysis but lacked concrete insights; current paper has clearer contributions and better experiments, so slightly stronger.
- "Rethinking LLM Unlearning" (avg 6.0, Accept poster) — mixed reviews (scores 6,5,8,3,6,8); current paper's experiments are more systematic and comprehensive.
- "Mitigating Memorization in Language Models" (avg 7.33, Accept spotlight) — well-executed comprehensive study; cleaner claims than current paper.

**Initial bracket:** 5.0–7.5 after round 1.
**Narrowing:** The paper sits between the weaker anchors (~5) and the stronger contamination papers (~6.75). It is clearly stronger than "Elephants Never Forget" (4.75) and "Spectral Dynamics" (6.25), slightly weaker than "Time Travel" (7.00) and "To the Cutoff" (6.75) due to the overclaiming issue, and comparable to "Rethinking LLM Unlearning" (6.0) but with more systematic experiments.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>