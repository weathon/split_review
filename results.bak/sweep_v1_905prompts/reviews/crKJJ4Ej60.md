Now I have all the calibration data I need. Let me synthesize the final review.

**Bracket from Round 1**: The paper sits between the middle-band anchors (3.5–7.5) and touches the low end of the high-band anchors (7.5+). Specifically, it's clearly stronger than the 5.75–6.40 papers (Fine-Tuning for Factuality, Mask-DPO, RAG-DDR) and comparable to but slightly below the Situated Faithfulness paper (7.25). My initial bracket is 6.5–7.5.

**Round 2 narrowing**: Reading Situated Faithfulness (7.25) and RAG-DDR (6.00) in full confirms this paper is above the ~6.0 papers (novelty of the Copy-Paste idea + data efficiency + strong empirical results) but below the top-tier 8.0 papers (which have no undefined metrics, complete evaluations, and greater polish). The closest anchor is Situated Faithfulness at 7.25, and this paper is slightly below it due to clarity gaps (undefined metrics, missing fluency evaluation for the final model).

---

## Summary

This paper proposes **Copy-Paste**, a generation paradigm for RAG that directly embeds contextual fragments into responses to ensure faithfulness and mitigate hallucinations. The authors instantiate this through a two-stage pipeline: (1) **Copy-Paste-Prompting** methods (CP-Order, CP-Link, CP-Refine) generate high-copying responses via hard and soft lexical constraints, and (2) **CopyPasteLLM** internalizes this behavior via DPO on automatically constructed preference pairs from only 365 query-context samples. On FaithEval, ConFiQA, and PubMedQA, CopyPasteLLM achieves 12.2–24.5% accuracy improvements over the strongest baselines while using 50× less training data. A mechanistic analysis (Context-Parameter Copying Capturing) suggests the model recalibrates parametric knowledge confidence rather than enhancing contextual representations.

## Strengths

- **Genuinely novel and intuitive core idea.** The Copy-Paste paradigm — maximizing lexical reuse from context as a direct faithfulness mechanism — is conceptually clean and well-motivated. The motivating observation (Figure 1, inverse correlation between copying degree κ/δ and hallucination density on RAGTruth) provides a principled, data-driven foundation. This is not an incremental improvement on an existing method but a distinct approach.

- **Extreme and well-evidenced data efficiency.** CopyPasteLLM achieves 92.8% accuracy on the FaithEval counterfactual subset using only 365 training samples, outperforming Context-DPO (80.2% with 18,000 samples), Canoe (10,000), and ParamMute (32,580) (Table 1). The 50× data reduction is striking and directly supports the paper's central claim that high-copying preference learning is an efficient route to contextual trust.

- **Strong performance across both counterfactual and original settings.** The method does not merely game counterfactual evaluations: Table 3 shows substantial gains in non-counterfactual settings, with a 20.67 percentage point improvement on the challenging ConFiQA-MR subset (Mistral-7B-v0.2). This demonstrates that the learned behavior generalizes beyond adversarial setups.

- **Well-designed two-stage pipeline.** Stage 1's three prompting methods (CP-Order, CP-Link, CP-Refine) are clearly differentiated, and Stage 2's preference construction — multi-criteria filtering + Elo tournament + answer stamping — is methodologically sound. The pipeline is fully automated, which is a practical strength.

## Weaknesses

### Major

- **Twist and Causal hallucination metrics are undefined.** Table 2 reports numerical "Twist" and "Causal" scores, described only as "two major hallucination modes" diagnosed by an Elo tournament (Section 3.2). The paper never defines what these modes mean semantically, how they are operationalized as quantitative scores, what evaluator produces them, or whether higher/lower values are better. This undermines the Stage 1 evaluation claims (e.g., "CP-Refine excels in hallucination reduction"). While the paper's central Stage 2 claims rely on standard accuracy/Hit metrics (Tables 1, 3), readers cannot interpret or reproduce the Stage 1 hallucination results as presented.

### Minor

- **No fluency or query-relevance evaluation for the final model (CopyPasteLLM).** The paper's own problem formulation (Section 2.1) states that Copy-Paste must balance faithfulness, query relevance, and fluency. Stage 1 evaluation (Table 2) includes a fluency (perplexity) column and references query-relevance analysis (Appendix Figure 6). However, Stage 2 results (Tables 1, 3) report only accuracy and hit rate — no fluency or relevance metrics. The abstract claims the method works "without compromising fluency and relevance," but this is unsubstantiated for the final trained model. The filtering pipeline uses perplexity and embedding similarity during preference construction, but this does not constitute an evaluation of the final model's outputs on these axes.

- **Training data composition for the 365 samples is not fully specified.** The Table 1 caption states "We removed 241 samples used for training CopyPasteLLM from FaithEval," which implies that at least some of the 365 query-context pairs derive from FaithEval. It is never stated whether the 365 are entirely from FaithEval, a mix of datasets, or selected via a specific strategy. This is a clarity issue (the paper removes training samples from the test set, so there is no contamination), but it should be explicitly disclosed to support the data-efficiency claim.

- **Mechanistic analysis is qualitative.** Figures 3 and 4 provide a plausible story about recalibrating parametric knowledge confidence, but the evidence is based on visual inspection of UMAP plots with confidence ellipses and a filtered subsample of generation steps (with variable retention rates). This is acceptable for an interpretability tool but should be acknowledged as preliminary.

- **No error bars or variance estimates.** Single-point accuracy values are reported without confidence intervals. Given the small training set (365 samples), stability is a genuine concern. This is standard in many LLM evaluation papers but would strengthen the work.

## Nice-to-Haves

- A small-scale human evaluation of contextual faithfulness for CopyPasteLLM would strengthen the claim, given that automated faithfulness metrics (MiniCheck, AlignScore) are imperfect proxies.
- Reporting compute cost (total LLM API calls) for Stage 1 would contextualize the claimed efficiency.
- Reporting what happens when context is incomplete or internally contradictory would probe the method's boundaries — the ethics statement acknowledges this risk but the experiments do not test it.

## Removed Points

The following points from the reviewers were removed with justification:

1. **"The comparison to GPT-4o's 47.5% is uninterpretable without knowing test subset alignment"** — The GPT-4o comparison is cited as a reference point ("see Appendix Table 6"), not a controlled experimental baseline in Table 1. The paper's primary comparisons (Context-DPO, Canoe, ParamMute, CoCoLex) are clearly specified. This criticism speculates about a reference that the appendix presumably clarifies.

2. **"Undisclosed origin potentially implies contamination / overfitting to FaithEval distribution"** — The paper explicitly removes training samples from the FaithEval test set. Results on ConFiQA (three subsets) and PubMedQA (separate datasets with no overlap) show similar strong performance, ruling out dataset-specific overfitting. The concern is about a clarity issue, not an evidential threat.

3. **"Missing related work / Self-RAG, CRAG baselines"** — The critic acknowledges this is acceptable given the paper's goals. "Comprehensive comparison" is a mild overstatement, but not a substantive weakness.

4. **"Gold answer usage makes the method not fully unsupervised"** — The paper correctly states "when gold answers are available" (conditional). This is honest scoping, not a flaw.

5. **Strength Finder strengths about "important problem" and "comprehensive evaluation"** — These are generic and removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations about undefined metrics and missing fluency evaluation are genuine but do not constitute novel analytical insights beyond what the paper already surfaces.

## Suggestions

1. **Define Twist and Causal metrics explicitly.** This is the highest-priority fix. State the evaluator (LLM judge? rubric? classifier?), score range, interpretation, and how these relate to the Elo tournament ranking in Stage 2.
2. **Add fluency (perplexity) and query-relevance (embedding similarity) for CopyPasteLLM** alongside Tables 1 and 3, even as an appendix table. This closes the gap between the stated optimization objective and the reported evaluation.
3. **Explicitly state the composition of the 365 training samples** — which datasets they come from, selection strategy, and any overlap with evaluation sets (beyond the removal already stated).
4. **Add error bars** (bootstrapped confidence intervals or standard deviations across multiple runs or seeds) to the main accuracy tables, especially given the small training set.

## Score and Decision

### Calibration

**Round 1 (bracketing):**
- Low band (score < 3.5): RuY1r1PDdQ (3.00), a2rSx6t4EV (2.33), oqRe1KvD17 (3.00), fMaEbeJGpp (2.50) — all weak RAG papers with limited contributions. Our paper is clearly stronger.
- Middle band (3.5–7.5): WPZ2yPag4K (5.75), d2H1oTNITn (6.40), Q6M7bZIo9t (4.67), JnWJbrnaUE (3.75), Pnktu2PBXD (6.00), K2jOacHUlO (7.25) — our paper is above all except K2jOacHUlO (Situated Faithfulness, 7.25), which is slightly more polished.
- High band (>7.5): Iyrtb9EJBp (8.00), SPS6HzVzyt (8.00), 07yvxWDSla (8.00), GGlpykXDCa (8.00) — top-tier papers with complete evaluations and no undefined metrics.

**Bracket from Round 1:** 6.0–7.5

**Round 2 (narrowing):**
- K2jOacHUlO (Situated Faithfulness, 7.25): Very similar topic (contextual faithfulness under knowledge conflicts). The paper under review has a more novel core idea but is less polished (undefined metrics, missing fluency evaluation). Slightly below this anchor.
- d2H1oTNITn (Mask-DPO, 6.40): Incremental improvement to DPO. Current paper has stronger novelty. Above this anchor.
- Pnktu2PBXD (RAG-DDR, 6.00): Standard DPO application. Current paper is clearly stronger.
- WPZ2yPag4K (Fine-Tuning for Factuality, 5.75): Limited novelty. Current paper is clearly stronger.

**Final score:** 7.0 — The paper is above the 6.0–6.4 range due to its novel core idea and strong empirical results, but below the top-tier 7.5+ papers due to the undefined Twist/Causal metrics, missing fluency evaluation for the final model, and absence of error bars. The contribution is real and well-supported; the gaps are fixable clarity issues.

**Decision:** Accept — the paper makes a genuinely novel contribution to the RAG faithfulness problem with compelling empirical evidence, and its weaknesses are addressable in a rebuttal/revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>