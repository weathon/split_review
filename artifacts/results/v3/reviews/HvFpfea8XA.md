Now I'll produce the final consolidated review.

## Calibration Anchor Report

**Round 1 — Bracketing**

| Anchor | Avg Score | Round/Query Bucket | Comparison |
|--------|-----------|-------------------|------------|
| `oqRe1KvD17` (Reward-RAG) | 3.00 | round1-topic-low (<3.5) | Weaker paper — less thorough evaluation, fewer models tested. Our paper is somewhat stronger. |
| `fMaEbeJGpp` (Multimodal RAG QA) | 2.50 | round1-topic-low (<3.5) | Much weaker — poor writing, no novelty, limited experiments. Our paper is clearly stronger. |
| `RfYD6v829Y` (TrojanRAG) | 3.40 | round1-topic-low (<3.5) | Different domain (security), but similar score tier. Comparable in having partial contributions with methodological gaps. |
| `wZbkQStAXj` (PersonaEval) | 4.00 | round1-topic-mid (3.5–7.5) | Comparable — both have a benchmark contribution and methodology concerns. PersonaEval's human evaluation is more comprehensive. |
| `87DtYFaH2d` (Tell Me What You Don't Know) | 5.20 | round1-topic-mid (3.5–7.5) | Stronger — more rigorous evaluation, deeper analysis, clearer contribution. Our paper has more significant evaluation gaps. |
| `QYvtX2XA8p` (CtrlA) | 4.50 | round1-topic-mid (3.5–7.5) | Stronger — cleaner evaluation on standard RAG benchmarks. Our paper addresses a more niche domain. |
| `rKMQhP6iAv` (Personas as a way to Model Truthfulness) | 4.25 | round1-topic-mid (3.5–7.5) | Comparable — hypothesis-driven with evaluation concerns. Both have partial evidence but methodology gaps. |
| `TqwTzLjzGS` (BIG5-CHAT) | 5.25 | round1-weakness (personality prediction) | Stronger — larger dataset (100K dialogues), uses BFI evaluation with more rigorous protocol. |
| `JnWJbrnaUE` (CRAG) | 3.75 | round1-weakness (missing ablation) | Comparable — both propose RAG variants and have evaluation gaps. |
| `KDXj60FpJr` (RAGGED) | 5.00 | round1-weakness (missing ablation) | Stronger — systematic ablation framework, clearer contribution despite mixed reviews. |

**Round 2 — Narrowing within bracket (3.5–5.5)**

| Anchor | Avg Score | Round/Query Bucket | Comparison |
|--------|-----------|-------------------|------------|
| `cphaRg46jD` (No Free Lunch: RAG Fairness) | 4.50 | round2 (missing human eval) | Stronger — more rigorous experimental design, clearer hypotheses. Our paper has weaker evaluation methodology. |
| `8WpRt9pjeh` (Synthesizing Bonds) | 4.33 | round2 (personality prediction, no ablation) | Comparable — both use crowdsourced/synthetic ground truth with limited human evaluation. |
| `zEm5nXxiXU` (AIDBench) | 3.67 | round2 (benchmark, no ablation) | Comparable — benchmark contribution with limited analysis. Our paper proposes both method and dataset. |

**Round-1 bracket:** 3.5–5.5 (clearly above the 2.5–3.0 weak papers but below the 5+ strong papers due to significant evaluation gaps).

**Round 2 narrowing:** The round-2 anchors confirm that papers with comparable evaluation gaps (missing ablation, no human eval of final outputs, questionable ground truth) sit around 3.5–4.5. Our paper is on the lower end this range.

**What the low-band anchors failed at:** Weak evaluation rigor, missing ablations, limited human evaluation, overclaimed results from questionable metrics. The paper under review shares these failures — the MBTI/BFI evidence for the core out-of-knowledge claim is not properly validated (derivation procedure not described, crowdsourced ground truth without reliability analysis), and no human evaluation of final generated responses is conducted. These failures are not redeemed by the modest CharacterRAG gains (+0.45–1.56 pp).

**Final score:** 3.5 — indicates a paper with genuine contributions (the dataset, the ACTS analysis) but whose central claim is not adequately supported by the current evaluation.

---

## Summary

This paper proposes AMADEUS, a training-free RAG-based framework for role-playing agents, consisting of (i) Adaptive Context-aware Text Splitter (ACTS), (ii) Guided Selection (GS), and (iii) Attribute Extractor (AE). It also introduces CharacterRAG, a manually constructed dataset of 15 fictional characters with 976K characters of persona documents and 450 QA pairs. The goal is to improve persona consistency for queries both within and beyond a character's explicit knowledge. Experiments compare AMADEUS against Naive RAG, CRAG, and LightRAG across multiple LLMs and embedding models.

## Strengths

- **Effective adaptive chunking with empirical validation.** Table 2 shows ACTS consistently outperforms RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter, and SemanticChunker on mean similarity scores with lower variance across three embedding models (BGE-M3, Qwen3-0.6B, mE5large-instruct). This directly validates the contribution of adaptive chunk length, overlap, and hierarchical context for role-playing.

- **First dedicated RAG-based role-playing dataset.** CharacterRAG is a manually constructed resource with 15 characters, 976K written characters, and 450 QA pairs spanning six persona attributes (Activity, Belief/Value, Demographic Information, Psychological Traits, Skill/Expertise, Social Relationships). The dataset fills a genuine gap and will support future research.

- **Reliable attribute extraction validated by human judges.** Table 3 reports a human evaluation (14 judges, 60 items) of the GS+AE attribute extraction outputs achieving µ≈4/5 on a Likert scale with Cronbach's α > 0.8, demonstrating that the extracted attributes are perceived as reasonable.

- **Evaluation across diverse LLM and embedding families.** AMADEUS is tested with GPT-4.1, Gemma3-27B, and Qwen3-32B (including thinking mode) as readers, and three embedding models, showing consistent (if modest) improvements — demonstrating the framework is not tied to a single model.

- **Negative findings about graph-based and web-search RAG for role-playing.** LightRAG (48–69.56% ACC, Table 4) and CRAG (28.67–70% ACC) perform substantially worse than Naive RAG, surfacing meaningful caveats for practitioners building role-playing systems.

## Weaknesses

### Major

- **The central claim about out-of-knowledge persona consistency is not properly validated.** The paper's main evidence for out-of-knowledge improvement is the MBTI/BFI evaluation (Table 1: 85% MBTI accuracy vs. 65–68.33% for baselines). However, (a) the procedure for deriving predicted MBTI/BFI types from the LLM's free-text responses to 60/120 questions is not described — the paper only says "compare the results to psychological test outcomes" — making it impossible to assess whether the evaluation is fair across methods; (b) the ground-truth labels come from a crowdsourced voting website (personality-database.com) without any reliability or inter-annotator agreement analysis, yet these labels are treated as hard ground truth to compute accuracy metrics. When the central empirical claim of the paper relies on this evaluation, the missing details are a significant gap. (See Section 5.2, footnote 4, Table 1.)

- **No human evaluation of the actual generated responses.** The human evaluation (Table 3) only assesses whether the *attribute extraction* outputs (GS+AE) are reasonable — it does not evaluate the quality, consistency, or character-faithfulness of the *final generated responses*. For a paper whose core contribution is improving persona consistency in generated dialogue, this is a critical absence. All response-level metrics (ACC, ACC_L, HS) are computed by an unidentified LLM judge with undisclosed prompts, which introduces unknown biases and limits reproducibility. (See Section 5.2 "Metrics" and Table 3.)

- **No ablation studies isolating component contributions.** AMADEUS has three components (ACTS, GS, AE). Table 2 validates ACTS on a proxy metric (similarity scores) but no end-task ablation removes ACTS, GS, or AE individually on either CharacterRAG or MBTI/BFI. Without this, it is impossible to attribute improvements to any specific component, and the modest CharacterRAG gains (+1.34 pp for GPT-4.1, +0.45 pp for Qwen3-32B) could arise from any part of the pipeline. (See Table 4.)

### Minor

- **The LLM used for computing ACC, ACC_L, and HS is not identified**, and the prompts for these metrics, as well as for GS and AE, are not provided. This is a serious reproducibility concern for a systems paper.

- **No statistical significance testing or confidence intervals** are reported for any metric. Given that some differences are very small (e.g., +0.45 pp on Qwen3 ACC), the claimed improvements may not be meaningful.

- **Naive RAG chunking parameters are not specified** (chunk size, overlap strategy), making it unclear whether the comparison is to a reasonable baseline.

- **The dataset is relatively small** (15 characters, 450 QA pairs), which limits the generalizability of findings. Most characters come from a single cultural source (Korean Namuwiki).

### Trivial

- Figure 4's caption mentions "α=5, α=10, α=15" with identical log-sim values (5.916), which appears to be a plotting artifact that should be clarified.
- Table 4 reports HS for CRAG/LightRAG with some values missing ("—") without explanation.

## Nice-to-Haves

- Report average inference time and LLM API cost per query for AMADEUS (which calls an LLM up to 30 times per query in GS) versus baselines.
- Include a "Naive RAG + ACTS" baseline to isolate the contribution of ACTS alone on end-task performance.
- Test on English-sourced characters to demonstrate the framework is not dataset-specific.

## Removed Points

These points were flagged by reviewers but are removed with justification:

1. **"Large gains in out-of-knowledge persona consistency" (Strength Finder).** This strength depends on the MBTI/BFI evaluation being valid. Given that a verified weakness (above) questions the validity of this evaluation, per the filtering rules this strength is removed from the main listing. The empirical numbers are as reported but their interpretation as evidence for persona consistency is uncertain.

2. **"The comparison to baselines is not adequately controlled" — claim that gains in Table 4 are "very modest" as a weakness per se.** The modesty of gains is a factual observation, not a methodological flaw. The real flaw is the lack of ablation studies and missing Naive RAG chunking details (retained above as Minor weaknesses).

3. **"CRAG shows large variance across MBTI vs BFI."** The paper acknowledges this and offers a plausible explanation (noise from web search). This is not a weakness — it is correctly discussed.

4. **Criticism about missing related work.** Per instructions, I cannot verify the completeness of related work coverage.

5. **"LightRAG performs poorly... paper attributes to graph construction issues" — this is not a weakness, it is a finding.** Retained as a positive strength (negative finding with practical value).

6. **"The paper is not particularly novel... incremental pipeline of existing techniques."** Novelty assessment is a judgment call. The pipeline-level contribution combined with the dataset is sufficient for this venue tier. Not retained as a weakness.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a tension that is instructive for the field: the MBTI/BFI-based evaluation borrowed from prior role-playing work (Wang et al., 2024b; Park et al., 2025) appears to be treated as a standard protocol, but it inherits unresolved questions about ground-truth reliability and type derivation methodology. This suggests the community needs a more rigorous evaluation framework for out-of-knowledge persona consistency than existing personality-test-based approaches. The paper's negative findings about LightRAG and CRAG for role-playing are also noteworthy — they suggest that RAG architectures designed for factual QA may need fundamental rethinking for persona-conditional generation, rather than simple adaptation.

## Suggestions

1. **Describe the MBTI/BFI type derivation procedure in full.** How are free-text responses mapped to MBTI/BFI types? If using an LLM to classify, provide the prompt, temperature settings, and validation against human annotation.
2. **Conduct a human evaluation of final generated responses** — ideally comparing AMADEUS vs. Naive RAG on a held-out set of out-of-knowledge and in-knowledge questions, with annotators rating character-appropriateness and consistency.
3. **Add end-task ablation experiments** removing each component (ACTS, GS, AE) individually on both CharacterRAG and MBTI/BFI.
4. **Identify the judge LLM and provide all prompts** used for ACC, ACC_L, HS, GS, and AE.
5. **Report confidence intervals** (e.g., bootstrap over the 450 QA pairs) and statistical significance for the main comparative results.
6. **Specify Naive RAG chunking parameters** (chunk size, overlap) and ideally include a "Naive RAG + ACTS" baseline.

## Score and Decision

**Calibration Summary:**

*Round-1 bracket:* 3.5–5.5. The paper is clearly above weak papers scoring 2.5–3.0 (which lacked any substantive contribution or had major writing flaws), but below stronger papers at 5+ (which had rigorous evaluation, human studies, or comprehensive ablation).

*Round-2 narrowing:* Anchors with comparable evaluation gaps — missing human eval of outputs (cphaRg46jD, 4.50), questionable ground truth for personality prediction (TqwTzLjzGS, 5.25), missing ablation (JnWJbrnaUE, 3.75) — cluster at 3.75–5.25. However, unlike those papers, the paper under review's central claim *depends* on the questionable evaluation, making it more vulnerable.

*Final comparison:* The paper shares the failure modes of low-band anchors (25th–40th percentile in the review corpus): evaluation of the core claim is not properly validated, and no human evaluation of actual system outputs exists. These failures collectively undermine the central claim about out-of-knowledge persona consistency improvement, triggering the rule that 2+ Major weaknesses undermining the core claim cap the score at ≤3.5.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>