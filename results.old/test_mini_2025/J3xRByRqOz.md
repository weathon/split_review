Now I have all the information needed. Let me construct the final consolidated review, carefully verifying each claim against the paper text.

## Summary

This paper introduces RA-RAG, a two-stage framework for multi-source retrieval-augmented generation that estimates per-source reliability without ground-truth labels (via iterative EM-style estimation) and then performs efficient inference by selecting a small subset of reliable *and* relevant sources (κ-RRSS) before aggregating via weighted majority voting. The paper also contributes a benchmark that simulates heterogeneous source reliability using beta and spammer-hammer priors across three QA datasets.

## Strengths

1. **Iterative reliability estimation closely tracks the oracle (Figure 2).** Across three LLMs (Llama3-8B, Phi3-mini, GPT-4o-mini) and two datasets, WMV using estimated reliabilities achieves EM scores nearly identical to Oracle WMV, which knows the true source reliabilities. This is the paper's strongest empirical result and directly demonstrates that the unlabeled iterative estimation recovers meaningful reliability values.

2. **κ-RRSS achieves near-full-source performance at substantially lower cost (Figures 5 and 6).** With κ=4 on up to 9 sources, RA-RAG matches or exceeds MV and closely approaches WMV (which queries all sources), while reducing inference cost by roughly 2×. This provides concrete evidence for the claimed scalability benefit.

3. **Misalignment filtration is shown to be critical for accurate reliability estimation (Table 2, Table 1).** Without filtering, estimated weights become distorted and RA-RAG (EM 0.465) performs worse than MV (0.449); with filtering, it recovers to 0.543, near the Oracle 0.549. Table 1 further shows filtering reduces hallucinated correct answers from irrelevant documents from 25.55% to 4.30%.

4. **Clean and reproducible benchmark design (Section 4).** The benchmark decouples source relevance (r_i) from source reliability (p_i) and uses two prior families (beta, spammer-hammer) to create heterogeneous reliability scenarios. This is a more realistic testbed than prior work that directly injects misinformation into retrieved documents without source-level modeling.

5. **Demonstration that relevance matters in addition to reliability (Figure 7).** κ-RSS (reliability-only selection) degrades EM by ~0.04–0.06 compared to κ-RRSS, confirming a non-obvious failure mode that the paper explicitly addresses.

## Weaknesses

### Major

- **Missing direct comparison to the most closely related prior methods.** The paper motivates itself by identifying limitations in Deng et al. (2024) and Pan et al. (2024), yet neither is included in the experimental comparison. While the counting-based methods of Pan et al. (2023), Weller et al. (2024), and Xiang et al. (2024) are reasonably represented by the MV baseline, Deng et al. (2024) (which uses LLM internal knowledge to assess document reliability) and Pan et al. (2024) (which heuristically categorizes source reliability into two levels and fine-tunes an LLM) are methodologically distinct approaches to the same problem. Without comparing against them, the paper cannot fully substantiate its claim of *overcoming* the limitations of existing robust RAG approaches. The reader can only conclude that RA-RAG improves over naive retrieval and majority voting, not that it advances the state of the art for robust RAG.

### Minor

- **No variance or confidence intervals reported in main figures.** The paper states results are averaged over 10 random trials, but Figures 2, 4, 5, and 7 show only point-estimate lines without error bars, standard deviations, or any indication of variability. With 3–9 sources and stochasticity in both data generation and LLM responses, variance could be non-negligible, and the reader cannot assess whether observed improvements are statistically meaningful.

- **Reliability estimation assumes per-source consistency across topics (Section 3.3).** A single reliability value v_i is estimated per source, implicitly assuming source trustworthiness is uniform across all query types. Real-world sources may be reliable on some topics and unreliable on others. The paper does not discuss this assumption, and the benchmark (which assigns fixed p_i per source) does not test robustness to topic-dependent reliability. This limits the scope of practical applicability claims.

- **The ROUGE-1 precision threshold of 0.9 (Section 3.2) is not motivated or analyzed for sensitivity.** The paper demonstrates that filtering helps overall (Table 2) but provides no ablation on the threshold value. Different thresholds could yield different trade-offs, especially for longer or more varied answers, and the chosen value appears arbitrary.

- **The scalability demonstration is limited to at most 9 sources (Section 4).** The paper claims scalability as a key advantage of κ-RRSS (Section 2.3) and shows cost savings at this scale (Figure 6), but 9 sources is small. Testing on 20–50 sources would substantially strengthen the scalability claim. The paper acknowledges computational constraints, so this is a scope limitation rather than a flaw.

- **Negative weights from the normalization v_i = Nŵ_i − 1 (Section 3.3) are discussed but not analyzed.** The paper notes this normalization "can produce negative weights" but does not examine whether negative weights actually arise in the experiments or what their effect on WMV and κ-RRSS would be.

### Trivial

- The abstract states the benchmark "contrasts with previous works that relied on setups with artificially injected misinformation," but the proposed benchmark also uses GPT-4o-mini to generate misinformation. The meaningful distinction is source-structured vs. injection-based, not artificial vs. natural, so the phrasing is slightly misleading.

## Nice-to-Haves

- **Analysis of how many queries M are needed for stable reliability estimation.** The paper uses M=200 throughout but does not examine whether accuracy saturates earlier or whether fewer queries suffice.
- **Stage 1 computational cost reporting.** The paper reports only Stage 2 (inference) costs in Figure 6 but does not quantify the cost of Stage 1 reliability estimation (which requires querying all sources for M queries).
- **Spammer-hammer results beyond NQ in the main text.** Results for TQA and HotpotQA are relegated to Appendix C.2; including a summary in the main body would strengthen the robustness claims.

## Removed Points

- **"The paper cannot substantiate its primary motivation"** — This overstates. MV represents the counting-based prior methods (Pan et al. 2023, Weller et al. 2024, Xiang et al. 2024) discussed in the paper. The criticism is real but only applies to Deng et al. (2024) and Pan et al. (2024), not all listed prior work.
- **"The qualitative example is a single case"** — The paper notes additional examples in Appendix D, which was stripped by the parser.
- **"Spammer-hammer experiment only on NQ with one model"** — The paper explicitly states TQA and HotpotQA results are in Appendix C.2, which was stripped by the parser.
- **"Section 5.3 ablation uses extreme parameters"** — Extreme parameters are appropriate for testing the failure mode (distortion from spammers), and the paper is transparent about the setting.
- **"No comparison to spaCy post-processing"** — The paper states results are in Appendix E, which was stripped by the parser.
- **"Missing related works"** — Cannot be confirmed without external knowledge of the literature.
- **Formatting/presentation nitpicks** — Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The iterative reliability estimation adapted from crowdsourcing to multi-source RAG is the core technical novelty, and the κ-RRSS selection criterion (reliability + relevance) is a practical insight validated by the RSS vs. RRSS comparison. These are clearly presented in the paper itself.

## Suggestions

1. **Add a comparison against at least one of the omitted prior methods (Deng et al. 2024 or Pan et al. 2024).** The paper's infrastructure already supports multi-source retrieval; adapting Deng et al.'s LLM-as-judge approach or Pan et al.'s heuristic estimation would be feasible and would directly test the claimed advantages.
2. **Add error bars or confidence bands to Figures 2, 4, 5, and 7.** This is a low-cost addition that would substantially strengthen the evidentiary value of the experiments.
3. **Extend the scalability experiment to a larger number of sources (e.g., 20–50)** to make the κ-RRSS efficiency claim more credible.
4. **Add a sensitivity analysis for the ROUGE-1 threshold** or justify the 0.9 choice with empirical evidence.
5. **Discuss the topic-dependent reliability limitation** explicitly and, if possible, test on a benchmark where source reliability varies by query category.

## Score and Decision

**Calibration protocol:**

**Round 1 (bracketing):** Three queries on multi-source RAG and reliability estimation.
- Weak anchors (<3.5): avg scores 2.33–3.40. These are withdrawn/rejected papers with poor quality. RA-RAG is clearly stronger.
- Middle anchors (3.5–7.5): avg scores 3.75–6.00. Includes CalibRAG (4.25, rejected — missing baselines, clarity issues), SubgraphRAG (6.0, accepted poster — thorough but missing some baselines), self-contradiction paper (6.0, accepted poster).
- Strong anchors (>7.5): avg scores 8.00. Oral/Poster papers with outstanding contributions. RA-RAG is clearly below this level.

Initial bracket: **3.5–6.0**.

**Round 2 (narrowing):** Two queries bracketing 3.0–5.5 and 5.0–7.0.
- CalibRAG (4.25, rejected): RA-RAG has cleaner writing, more thorough experiments, and a clearer contribution. Better.
- Calibration paper (5.75, rejected): Overclaiming and theoretical issues. RA-RAG has fewer theoretical concerns but comparable missing-baseline issues. Comparable.
- Self-contradiction paper (6.0, accepted poster): Well-written, comprehensive, but addresses a different problem. RA-RAG's evaluation gap is more significant. Similar but slightly weaker.
- SubgraphRAG (6.0, accepted poster): Thorough evaluation with some missing baselines. RA-RAG has a similar profile but with a more central missing-baseline gap. Slightly weaker.

Final score: **5.0**. The paper presents a clean method and a well-constructed benchmark, but the evaluation omits comparison against the most closely related prior methods (Deng et al. 2024, Pan et al. 2024) that it claims to improve upon, weakening its central contribution claim. The method is promising and the infrastructure is strong, but the evidence is incomplete as presented. Score of 5.0 positions it between the rejected papers with significant evaluation gaps and the accepted papers with more complete evidence.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>