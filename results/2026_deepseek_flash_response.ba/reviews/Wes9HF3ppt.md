## Summary

This paper introduces Insertion Language Models (ILMs), which generate sequences by inserting one token at a time at arbitrary positions. Unlike Masked Diffusion Models (MDMs) that use fixed-length mask tokens, ILMs drop tokens entirely during noising and learn to predict both the token content and insertion position. The key technical innovation is a training objective that avoids high-variance Monte Carlo estimation by using aggregate token-count targets computed from the full sequence. The paper evaluates ILMs on planning tasks (star graphs, zebra puzzles) where they substantially outperform both ARMs and MDMs, and on text generation/infilling where they are competitive with ARMs and better than MDMs.

## Strengths

1. **Clean empirical demonstration of MDM limitations on variable-length tasks.** The star graph experiments (Table 1) are well-designed and produce striking results: on Star\_hard, ILM achieves 99.1% exact match while MDM collapses to 21.0% and left-to-right ARM reaches only 23.0%. The paper provides a crisp explanation — MDMs operate on absolute token positions, so when arm lengths vary, predicting junction node positions is "equivalent to solving the puzzle itself in a single pass." This controlled experiment cleanly isolates the failure mode that ILM overcomes. The zebra puzzle results (90.0%) further corroborate that ILM's out-of-order generation helps on constraint satisfaction.

2. **Novel insertion-based formulation that addresses a genuine gap.** By dropping rather than masking tokens, ILMs naturally handle variable-length infilling without placeholder tokens. This is a qualitatively different capability from both ARMs (fixed left-to-right) and MDMs (fixed-length masks). The paper correctly identifies this as an important limitation of prior work and proposes a principled alternative.

3. **Ablation validates the stopping classifier design.** The Insertion Transformer (IT) baseline, which differs primarily by using an EOS token instead of a dedicated stopping classifier, performs poorly (17.5–35.2% vs ILM's ~100% on star graphs). This provides evidence that the stopping classifier is a meaningful design choice, not an incidental detail.

4. **Multi-metric evaluation beyond perplexity.** The paper uses Prometheus 2 7B as an LLM judge (Figure 5) to rate generated text on coherence, consistency, fluency, grammaticality, and non-redundancy, providing a quality assessment beyond NLL alone.

## Weaknesses

### Fatal
None.

### Major

1. **The abstract overclaims text generation results.** The abstract states ILMs "perform on par with ARMs ... in unconditional text generation." However, Table 2 shows a 0.73 nats/token gap on LM1B (ARM 3.94 vs ILM 4.67, an 18.5% relative difference). The body uses more measured language ("competitive with ARMs," "still perform slightly worse"), but the abstract's stronger claim is misleading for the LM1B result. Given the growing scrutiny of LoMLM (Language Model for Language Model) papers at top venues, such framing discrepancies are increasingly flagged by reviewers.

2. **The training objective/inference mismatch is acknowledged but unanalyzed.** The training objective (Eq. 2) trains the model to predict aggregate count distributions over *all* dropped tokens simultaneously (normalized per-gap counts of every missing token), while inference inserts *one token at a time* (Algorithm 2). The paper acknowledges this is biased (line 79: "To avoid this issue, we use a biased training objective") but provides no analysis — theoretical or empirical — of what this bias entails. Under what conditions does minimizing the aggregate-count objective produce a model that correctly performs sequential insertion? When does it fail? The paper cites Appendix D for details, but the appendix is not included in the submission. This is not a fatal flaw — the empirical results on planning tasks suggest the bias is manageable in practice — but it is a significant gap in the methodological contribution.

3. **No variance reporting for any experiment.** None of the tables (1, 2, 3) include standard deviations, confidence intervals, or number of seeds. For star graphs where ILM achieves 99–100%, this matters little. But for text experiments where differences are modest (Stories NLL: ARM 2.11 vs ILM 2.14, a 1.4% gap), the reader cannot assess whether these differences are meaningful. This is particularly important when the paper claims ILM is "on par" with ARM.

### Minor

1. **Missing inference details.** The top-k value for position sampling during inference is not specified (line 209 mentions "top-k sampling k ∼ p\_θ^ilm(k | x[b])" without giving k). The MDM's number of sampling steps in the infilling evaluation (Table 3) is not reported. These are small gaps but make reproducibility harder.

2. **Prometheus evaluation lacks protocol details.** Figure 5 shows ILM outperforming ARM and MDM on linguistic metrics, but the evaluation lacks sample sizes, error bars, and any description of the evaluation protocol (prompt template, temperature, etc.). Without these, the reader cannot assess statistical reliability.

3. **Star\_easy result is not fully explained.** ARM gets only 32.3% on Star\_easy (degree 3, symmetric) compared to 75.0% on Star\_medium (degree 2, asymmetric). The paper attributes the ARM's difficulty to "implicit lookahead" but doesn't explain why the supposedly easier setting is harder for ARM. This is a minor exposition gap.

4. **Ad-hoc explanation for infilling results on TinyStories.** Table 3 shows both MDM and ILM produce *worse* NLL than the input text after infilling (positive ΔNLL\_inp). The paper attributes this to stories being "fairly simple" (line 245) — this feels post-hoc and is not supported by any analysis.

### Trivial
None.

## Nice-to-Haves
- A small-scale empirical study comparing the biased aggregate-count objective against a Monte Carlo approximation on a simplified domain would substantially strengthen the methodological claims.
- Analysis of how the uniform sampling of n (number of dropped tokens) affects learning — does the model mostly train on highly corrupted sequences, and does this impact fine-grained insertion decisions?
- Reporting the number of NFEs (neural function evaluations) for MDM in all experiments would make comparisons more apples-to-apples.

## Removed Points
The following points from the reviewers were filtered as unsubstantiated or misreadings:
- "Fatal structural flaw" (harsh critic's point 1): Demoted from the critic's "critical" framing to Major. The paper acknowledges the bias (line 79) and the empirical results on planning tasks strongly suggest the bias is manageable. The reviewer's framing as fatal overstates the case — many generative models (e.g., BERT for generation) have similar training/inference discrepancies that are managed in practice. The concern is legitimate but not fatal.
- "ILM's lower entropy suggests under-generation": The paper directly acknowledges this (line 215: "the ILM is on the lower side... but still fairly close to the dataset entropy") and contextualizes it. This is addressed, not hidden.
- "MDM generates much longer sequences, making comparison less straightforward": The paper discusses this explicitly (lines 215–216) as a known characteristic of MDMs.
- "Missing IT explanation": The paper does explain why IT performs poorly (line 147: "consistently undershoots or overshoots the target sequence" due to EOS vs. stopping classifier).
- "Unfair MDM comparison for infilling": The infilling task is evaluating general capability; the paper's framing is appropriate for its stated goals.
- Generic "missing related works" criticisms that cannot be verified without external lookup.

## Novel Insights
The harsh critic's observation about the training/inference mismatch is the most useful insight — it correctly identifies that the paper's core technical contribution (the biased aggregate-count objective) has an unanalyzed gap that weakens the overall contribution. However, the critic overstates this as fatal; the more precise concern is that the paper would be substantially strengthened by even a minimal analysis of this bias.

## Suggestions
1. Calibrate the abstract's language — replace "perform on par with ARMs" with the more accurate phrasing used in the body (e.g., "are competitive with ARMs while outperforming MDMs").
2. Add variance/confidence intervals to all main results, especially Table 2.
3. Add a small diagnostic study analyzing the bias from the aggregate-count training objective — even a synthetic setting where the exact objective is tractable would suffice.
4. Specify the top-k value for position sampling and the MDM sampling steps used in all experiments.
5. Report the sample size, prompt template, and evaluation protocol for the Prometheus evaluation.

## Score and Decision

I calibrated this paper against the following anchors from the human-review corpus:

| Path | Score | Round | Comparison |
|------|-------|-------|-----------|
| FiLM (UbOzNf6hGq) | 4.25 | Brkt | ILM is clearly stronger — more novel method, better experiments, but shares a training/inference discrepancy concern |
| COrAL (0JjsZC0w8x) | 5.75 | Brkt+narrow | Comparable. COrAL has a similar "order-agnostic generation" framing; ILM has cleaner planning experiments, COrAL has slightly more thorough evaluation |
| SequenceMatch (FJWT0692hw) | 6.00 | Brkt+narrow | ILM is slightly weaker. SequenceMatch has solid execution with all 6/6 scores; ILM has more experimental breadth but a bigger methodological gap |
| Interpolating AR/Diffusion (tyEyYT267x) | 8.00 | Brkt | ILM is substantially weaker — that paper provides theoretical analysis (gradient variance), achieves SOTA, and is universally praised |
| RADD (sMyXP8Tanm) | 6.20 | Narrow | ILM is slightly weaker. RADD provides theoretical insights about absorbing diffusion and cleaner analysis |

**Round 1 bracket:** 4.5–6.5  
**Round 2 narrowing:** Compared against SequenceMatch (6.0, solid method paper with all 6s) and COrAL (5.75, Reject with similar profile), ILM sits between them — better experiments than COrAL, but a more significant unanalyzed gap than SequenceMatch. The training/inference mismatch and overclaimed abstract prevent a higher score.  
**Final score:** 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>