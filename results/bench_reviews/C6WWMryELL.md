Now I have a thorough understanding of the paper and my calibration anchors. Let me compile the final review.

---

## Summary

This paper investigates length volatility in long-form LLM generation through a three-stage approach: (1) VOLTBench, a multi-dimensional benchmark introducing multi-sample stability metrics (LSD, LVC, FAD); (2) an attention-trace analysis identifying internal failure patterns (Attention Collapse, Attention Instability); and (3) SELB, a training-free decoding strategy that enforces structural adherence via logit boosting and suppresses failure-mode tokens. The benchmark and large-scale empirical evaluation provide useful descriptive data on how current LLMs degrade at long output lengths.

## Strengths

- **Novel benchmark for generation volatility**: VOLTBench is the first benchmark to systematically quantify output length volatility through multi-sample metrics across multiple runs. The experiments on 10+ models (Table 2) expose severe instability — e.g., LongWriter-8B generates 6,320 words on average for a 100-section task but with an LVC of 45.4%, and most models fail entirely beyond 50 sections. Moving beyond single-generation evaluation is a genuine contribution.

- **Multi-dimensional benchmark design**: VOLTBench integrates unstructured and structured tasks across multiple languages (English/Chinese), instruction complexities, and length scales up to 500 chapters (Section 3.1). This enables fine-grained analyses showing, for instance, that structured tasks yield longer and less volatile outputs (Figure 3), offering actionable insights.

- **Attention-trace analysis provides useful diagnostics**: The attention trace methodology (Section 5) identifies two distinct failure signatures — Attention Collapse (premature termination) and Attention Instability (section skipping) — that correlate with observed generation failures. Figure 4 clearly communicates these patterns. While correlational, this analysis moves beyond pure output inspection.

- **SELB-Hybrid demonstrates generalization to free-form tasks**: The adaptation in Appendix I extends beyond section-enforced scenarios. On a 20,000-word novel task, SELB-Hybrid achieves MLA of 97% and LVC of 12.1%, outperforming baselines that suffer from severe length collapse (e.g., GPT-4o-mini generating <600 words). This partially addresses concerns about the method's reliance on explicit section anchors.

## Weaknesses

### Fatal

None.

### Major

- **Privileged structural oracle in SELB creates unfair comparisons**: SELB relies on explicit knowledge of the required section count, section titles, and target section length — information provided by the benchmark's task format. Baseline methods (repetition penalty, entropy stopping, length constraint, LongWriter-8B) receive the same input prompts but do not exploit this structural information at the decoding level. Consequently, SCA (100%) and MLA (78.25%) are partially artifacts of enforced structure rather than evidence of improved generation capability. A fair baseline that receives the same section-count and title information without strict logit boosting (e.g., constrained decoding or structured prompting) would be needed to interpret the performance claims. The SELB-Hybrid results partially mitigate this concern for unstructured tasks, but the main structured-task comparisons remain confounded.

- **The CKA representational stability analysis is confounded**: Appendix H claims that SELB prevents representational drift by showing higher cosine similarity between hidden states at late time steps and an early anchor. However, forced section titles reset the semantic context by reintroducing similar tokens, which mechanically increases cosine similarity regardless of whether the model's internal narrative state is preserved. The analysis as presented cannot distinguish genuine stability from this trivial confound.

### Minor

- **Attention analysis is correlational, not causal**: Section 5 identifies patterns that correlate with failures but does not establish causation. The paper's language is appropriately qualified (patterns "precede" failures), but the framing in the introduction ("identify the root causes") overstates what the analysis demonstrates. A perturbation study (e.g., manipulating attention to test whether collapse causes deviation) would strengthen the mechanistic claim but is absent.

- **Methodological simplicity limits contribution breadth**: SELB's core mechanism — boosting logits for predetermined section titles when a length threshold is reached, blocking EOS tokens, and suppressing conversational filler — is a collection of well-motivated but straightforward heuristics. The method works for its intended purpose but does not offer a generalizable principle for long-form generation control. This limits its significance as a methodological contribution, though it remains practically useful.

- **SELB-Hybrid details deferred to appendix**: The free-form generalization results (Section 6.4) are compelling but the full mechanism, evaluation setup, and comprehensive results appear only in Appendix I. The main paper would benefit from more detail on this adaptation.

### Trivial

- The attention trace methodology averages over all layers and heads, which may obscure layer-specific dynamics that could differentiate the two failure patterns more precisely.

## Nice-to-Haves

- A fair baseline that receives structural information (section count, titles) without strict logit boosting — e.g., adding section titles to the prompt prefix or using constrained decoding — would substantially strengthen the experimental comparisons.
- Human evaluation or qualitative examples of SELB-generated text to verify that forced section breaks produce coherent continuations rather than disjointed concatenations.
- Ablation showing SELB performance degrades when section titles are not perfectly known, to test robustness.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"SELB is not a valid research contribution — it is a hand-crafted, rule-based decoding hack"**: This overstates the case. While SELB is indeed simple and heuristic-based, a method's simplicity does not disqualify it as a contribution. SELB addresses a clearly identified problem and produces measurable improvements. The legitimate concern about the structural oracle and comparison fairness is captured in the Major Weaknesses section above. The claim that SELB is "equivalent to writing a post-processor" ignores that it operates during decoding (single-pass) and influences the generation trajectory rather than post-hoc padding.

- **"Attention trace analysis provides no actionable insight beyond what a practitioner could infer from generation logs"**: The attention traces DO reveal *when* failures begin internally (attention collapse precedes output degradation), which is not directly visible from output inspection alone. This has diagnostic value, even if the methodological contribution is modest.

- **"The attention-trace methodology is under-specified"**: The paper provides a full mathematical definition of α^(t) in Section 5, including the layer-and-head averaging procedure. While averaging may lose resolution, the methodology is clearly specified.

- **"Forced section titles will reset semantic context leading to higher cosine similarity"** (from Strength Finder): The strength finder claimed SELB "prevents representational drift" as a strength. This is moved to Removed Points because the CKA analysis is confounded (see Major Weaknesses).

- **"SELB achieves 148% increase in mean output length and 69% reduction in volatility"** (from Strength Finder, presented as standalone evidence): These numbers conflate enforced structure with improved generation. Moved because, while numerically correct, they cannot be interpreted as evidence of improved model capability without the structural-oracle caveat.

- **Generic strengths from Strength Finder about "addressing an important problem"**: These are removed as they are generic/superficial and do not constitute concrete evidence.

- **"The paper identifies internal attention patterns driving instability"** (causal framing): Changed to correlational framing — the paper identifies patterns that *correlate with* instability, not patterns that *cause* it.

## Novel Insights

None beyond the paper's own contributions. The observation that multi-sample length volatility is a distinct and severe failure mode in long-form generation is itself the paper's novel insight, and the benchmark provides systematic evidence for it.

## Suggestions

- Add a baseline that uses the same structural information as SELB but via prompt engineering (e.g., appending "You are now starting Chapter 3" at appropriate points) rather than logit manipulation. This would isolate the contribution of the decoding-level intervention.
- Include at least one full SELB-generated text example in the main paper or a prominent appendix so readers can qualitatively assess whether forced sections produce natural continuations.
- Either reframe the CKA analysis with appropriate caveats about the confound from forced section titles, or replace it with a more rigorous analysis of internal stability (e.g., measuring drift within a single section before the forced title boost).
- Consider a perturbation experiment for the attention analysis — e.g., artificially suppressing attention to constraint tokens and measuring the effect on output volatility — to strengthen the mechanistic claims.

## Score and Decision

### Anchor comparison:

- **ExpertLongBench** (`/home/wg25r/review_agent/human_reviews_2026/nJvgBolRcR.md`, avg 5.50, Accept Poster): Stronger paper — expert-designed benchmark with rigorous CLEAR evaluation framework, thorough experiments on 13 LLMs. The current paper's benchmark (VOLTBench) is solid but less rigorously validated, and the SELB method is simpler than CLEAR. VOLTBench + SELB is below ExpertLongBench.

- **Deco-G** (`/home/wg25r/review_agent/human_reviews_2026/XMb9poL2Mo.md`, avg 4.00, Withdrawn): A decoding framework using HMM training for format compliance. More technically sophisticated method than SELB, but reviewers found issues with baselines and evaluation scope. The current paper is comparable in overall quality — SELB is simpler but the benchmark contribution adds value. Roughly at the same level.

- **Frankentext** (`/home/wg25r/review_agent/human_reviews_2026/wfmEwfaRxN.md`, avg 4.00, Withdrawn): Creative idea with thorough experiments but mixed reviews on coherence and focus. The current paper has a clearer three-stage structure but weaker method novelty. Comparable quality level.

- **Oolong** (`/home/wg25r/review_agent/human_reviews_2026/lrDr6dmXOX.md`, avg 3.00, Reject): Benchmark paper criticized for limited novelty and missing baselines. The current paper is stronger — VOLTBench introduces multi-sample stability as a novel evaluation dimension, and the paper includes both analysis and a mitigation method.

- **MGAL** (`/home/wg25r/review_agent/human_reviews_2026/RdLSJ5CJsr.md`, avg 4.00, Withdrawn): Multilingual long-context benchmark. Similar benchmark-contribution profile. The current paper's additional method and analysis components put it slightly above.

- **SagaScale** (`/home/wg25r/review_agent/human_reviews_2026/bYpSLBk8H8.md`, avg 3.50, Reject): Novel-based long-context benchmark with automation pipeline. The current paper has a more comprehensive evaluation dimension (volatility) and a method contribution, making it stronger.

The current paper sits between the 3.00–4.00 benchmarks (Oolong, SagaScale) and the 5.50 benchmark (ExpertLongBench). It is comparable to the 4.00 papers (Deco-G, Frankentext, MGAL) but adds a method component they lack, while having method weaknesses that prevent it from reaching the ExpertLongBench tier. Score: **4.0**.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>