Now I have a thorough understanding of both the paper and the calibration anchors. Let me write the consolidated final review.

---

## Summary

This paper addresses output length volatility in LLM long-form generation through a three-stage approach: (1) VOLTBench, a new benchmark designed to quantify length volatility across heterogeneous tasks (structured/unstructured, multiple languages, up to 500 chapters / 100k words); (2) an attention-trace analysis identifying internal failure patterns ("Attention Collapse" and "Attention Instability") that correlate with premature termination and section skipping; and (3) SELB, a training-free decoding-stage method that enforces structural adherence via logits boosting and proactive failure token suppression, yielding substantial improvements in length stability on the benchmark.

## Strengths

- **Genuinely overlooked problem.** The paper correctly identifies that existing long-form generation evaluation focuses on single-generation quality and systematically ignores output volatility — the inconsistency in length and content across multiple runs. This is a real and costly issue for reliable deployment, and the paper provides the first large-scale quantification of it.

- **Comprehensive multi-dimensional benchmark.** VOLTBench is carefully constructed across four dimensions (task type, language, instruction complexity, output format), covering both unstructured text and structured data (code, math), with length scales up to 100k words. Table 1 demonstrates convincingly that no prior benchmark combines multiple sampling with stability evaluation across this breadth.

- **Simple, training-free mitigation that works.** SELB requires no additional training, no auxiliary models, and no iterative prompting. It achieves dramatic improvements on its target tasks: on a 100-section task, it lifts output from 445 words (base Qwen2.5-7B) to 15,651 words while reducing length volatility (LVC) by 69% and maintaining structured content accuracy at 100%.

- **Generalization to free-form generation.** Section 6.4 demonstrates that an adapted SELB-Hybrid strategy extends to unstructured 20k-word novel writing, achieving 97% MLA and 12.1% LVC, where baselines collapse to under 600 words. This partially addresses concerns about the method's reliance on chapter-based prompts.

- **Practical identification of failure modes.** The documentation of incomplete generation and section skipping as the two dominant failure patterns, with empirical evidence across multiple models, is a useful contribution for practitioners.

## Weaknesses

### Major

- **Misleading headline quantitative claim.** The abstract, introduction, and conclusion repeatedly state that SELB "improves the mean output length of the base model by 148%." However, the base model (Qwen2.5-7B) produces 445 words while SELB produces 15,651 words — an increase of approximately 3,400%, not 148%. The 148% figure actually corresponds to the improvement over LongWriter-8B (6,320 → 15,651 words), which is not the base model. This is either a significant error or a misleading formulation, and it appears in the paper's most prominent claims. Whether careless or intentional, it erodes trust in the reported results and should be corrected.

- **Tight coupling between benchmark structure and method evaluation.** VOLTBench's chapter-based format and SELB's structural enforcement are intimately linked: the benchmark defines success largely as chapter-count adherence, and the method hard-codes chapter-title injection and EOS suppression. This makes the primary evaluation partially circular — the method is being assessed on precisely the dimensions it was hard-coded to satisfy. The paper partially mitigates this concern through the free-form generalization (Section 6.4), which is a genuine validation that the approach can work without explicit chapter markers. However, that experiment is described only briefly in the main paper with full details deferred to the now-stripped Appendix I, and it remains a single experiment rather than systematic evaluation across diverse free-form tasks.

### Minor

- **Attention probing is observational, not causal.** Section 5 identifies "Attention Collapse" and "Attention Instability" from two hand-selected traces (Qwen2.5-7B and Qwen2.5-3B on one task). No statistical prevalence is reported across models or runs, and no intervention experiment demonstrates that fixing these attention patterns causally improves output. The link from attention findings to SELB is post-hoc: SELB does not manipulate attention — it bypasses the need for the model to self-regulate attention by forcibly injecting structure. The probing section reads more as a plausibility argument than a rigorous mechanistic investigation.

- **Quality evaluation depth.** While SCA (execution-based verification for code) is a strong, objective quality metric for structured tasks, UCA for unstructured tasks relies on LLM-as-a-Judge checking three fine-grained constraints (character, keyword, theme). These are reasonable proxies, but they don't directly measure fluency, coherence, or factual consistency at extreme lengths. The paper mentions lexical diversity analysis (Appendix G) and representational stability analysis (Appendix H), which would address this, but they are inaccessible in this stripped version. Human evaluation would substantially strengthen the quality claims but is absent.

- **The paper's main results are on a single base model for the mitigation method.** Table 2 evaluates many models, but SELB results are primarily demonstrated with Qwen2.5-7B as the base. While Figure 5 shows SELB applied to Qwen3-8B and Llama-3.1-8B for length curves, the full quality metrics (SCA, UCA) are not reported for those models with SELB.

### Trivial

- The abstract's footnote about code release ("upon acceptance") is standard but worth noting.

## Nice-to-Haves

- A component ablation of SELB would clarify whether the structural enforcement alone suffices or whether the banned-phrase list and EOS suppression contribute meaningfully beyond simple title injection.
- Side-by-side qualitative examples of baseline vs. SELB output at extreme lengths would help readers judge whether forced continuation produces coherent text or hollow filler.
- Comparison with dedicated length-control decoding methods (e.g., FUDGE-style logit manipulation) beyond the four general decoding baselines included.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"The benchmark's reliance on chapter markers makes evaluation tautological"* — softened and retained as a Major weakness with the important caveat that Section 6.4 and the free-form experiments partially address this concern. The original harsh-critic framing as entirely invalid was too strong.

- *"SCA/UCA are insufficient quality metrics"* — softened and retained as a Minor weakness. For structured tasks, SCA (execution-based verification) is actually a rigorous metric. For unstructured tasks, the paper does provide supplementary analyses (lexical diversity, representational stability) in appendices. The concern is valid but not as severe as originally framed.

- *"No human evaluation at all"* — retained as part of the Minor quality evaluation concern but not as a standalone fatal weakness, since LLM-as-a-Judge is standard practice and the paper has supplementary quality analyses.

- *"Attention analysis is entirely post-hoc and meaningless"* — softened. The analysis is observational rather than causal, but it does provide useful characterization of failure modes. Retained as Minor.

- *"Only two model instances shown"* — retained within the Minor attention probing weakness.

- *Strength Finder's generic strengths* — removed. Examples: "The paper is well written" and general claims about importance without specific evidence tied to the paper's actual contributions.

- *Strength Finder's claim about "causal link"* — removed. The paper does not establish causal mechanisms between attention patterns and output failures; the link is correlational.

## Novel Insights

The paper's key insight — that length volatility is a systematic and measurable property of LLMs that can be diagnosed through attention traces and mitigated through lightweight decoding interventions — is a useful reframing of the long-form generation problem. Prior work focused on whether models *can* generate long text at all; this paper shifts attention to whether they can do so *reliably*. The finding that structured tasks exhibit lower volatility (likely because format constraints provide stronger generation guidance) is an actionable insight that could inform prompt design in practice.

## Suggestions

- Correct the 148% figure throughout the paper. If the comparison is against LongWriter-8B, state this explicitly. If the comparison is against the base model, use the actual ~3,400% figure. The current formulation is misleading and must be fixed before publication.
- Expand the free-form generation evaluation (Section 6.4) into the main paper with full metrics rather than a single paragraph. This is the strongest evidence against the tautology concern and deserves more prominence.
- Add summary statistics for the attention patterns across multiple runs and models. Even a simple table reporting how often "attention collapse" precedes early termination across 10+ runs would substantially strengthen the probing section.
- Provide at least one human evaluation or qualitative case study comparing baseline vs. SELB outputs at extreme lengths to complement the automated quality metrics.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| LongWriter-Zero (JWx4DI2N8k) | 6.00 (Oral) | Stronger: RL-based training paradigm, SOTA results, cleaner evaluation. Our paper's training-free approach is less ambitious and has the misleading figure issue. |
| ExpertLongBench (nJvgBolRcR) | 5.50 (Poster) | Stronger: cleaner benchmark construction with expert validation, no misleading claims. Our paper adds a method but has evaluation concerns. |
| Predicting LLM Output Length (3loQDtveWI) | 5.33 (Poster) | Slightly stronger: cleaner experiments, no misleading figures, clear baseline comparisons. |
| Embedding Trust (ROTJZgRp7Q) | 5.00 (Reject) | Comparable: both have real contributions with some validation gaps. Our paper is broader (benchmark + probing + mitigation) but has the headline figure issue. |
| MGAL (RdLSJ5CJsr) | 4.00 (Withdrawn) | Weaker: benchmark-only paper. Our paper adds method and probing. |
| SagaScale (bYpSLBk8H8) | 3.50 (Reject) | Weaker: benchmark with significant quality/motivation concerns. Our paper is more comprehensive and better motivated. |
| UPHELD (wCV1efgkyV) | 3.00 (Reject) | Much weaker: small dataset with severe limitations. Our paper is substantially stronger. |

The paper's strengths — identifying a real and overlooked problem, building a comprehensive benchmark, and proposing a simple effective mitigation — are genuine and would typically support a score in the 5.0–5.5 range. However, the misleading 148% headline figure and the somewhat tautological primary evaluation (even though partially mitigated by free-form experiments) pull the score down. The attention probing, while interesting, does not add as much as claimed since the connection to the mitigation is post-hoc. Relative to the anchors, this paper is clearly stronger than the low-band papers (3.0–4.0) but falls short of the clear accept papers (5.33–6.0). It lands in the borderline range where the misleading figure tips it below acceptance.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>