Now I have sufficient calibration data. Let me finalize my analysis and write the review.

**Round 1 bracket**: 5.5–6.5 (between Tell Me What You Don't Know at 5.20 and MMRole at 6.50)

**Round 2 narrowing**: My paper is clearly stronger than Tell Me What You Don't Know (5.20) due to human evaluation, multiple LLMs/embeddings, and a new dataset. It is weaker than MMRole (6.50) because MMRole has a much larger dataset and fewer methodological gaps. The missing ablation and underspecified classification protocol are notable weaknesses that prevent acceptance. Score: 5.5.

Here is my final consolidated review:

## Summary
This paper proposes AMADEUS, a training-free framework for RAG-based role-playing agents, consisting of three components: Adaptive Context-aware Text Splitter (ACTS), Guided Selection (GS), and Attribute Extractor (AE). It also releases CharacterRAG, a manually constructed dataset of persona documents for 15 fictional characters (976K tokens, 450 QA pairs). The key claim is that AMADEUS maintains persona consistency even for out-of-knowledge questions. The paper evaluates on MBTI/BFI interview-based tasks and the CharacterRAG QA dataset, showing improvements over Naive RAG, CRAG, and LightRAG across multiple LLMs.

## Strengths
1. **CharacterRAG dataset fills a genuine gap** — It is explicitly designed for RAG-based role-playing evaluation, with persona documents reconstructed from the character's perspective and extraneous information removed. The size (15 characters, 976K tokens, 450 QA pairs) is reasonable for a manually curated resource, and the construction methodology (manual reconstruction, exclusion of meta-information that disrupts persona) is sound.

2. **Strong evidence on out-of-knowledge persona consistency** — Table 1 shows AMADEUS achieves 85.00% MBTI accuracy and 81.33% BFI accuracy, substantially outperforming Naive RAG (65.00%/72.00%), CRAG (68.33%/76.00%), and LightRAG (65.00%/34.67%). The gap is large and consistent across 15 characters, with the sum-of-deviations metric clearly favoring AMADEUS (9 vs 19–21 on MBTI, 14 vs 18–49 on BFI). These results directly support the paper's central claim.

3. **Human evaluation confirms GS→AE pipeline reliability** — Table 3 reports Cronbach's alpha of 0.825 (BFI) and 0.810 (MBTI) from 14 human evaluators scoring 60 random samples each on a 5-point Likert scale. Both values exceed the 0.8 threshold for "high level of internal consistency," and mean scores near 4/5 indicate the extracted attributes are reasonable. This is stronger evidence than relying solely on automated metrics.

4. **Systematic validation of ACTS chunking across multiple embeddings** — Table 2 compares ACTS against four chunking methods (RCTS, MHTS, SC, ATS) using three embedding models (BGE-M3, Qwen3-0.6B, mE5-large-instruct). ACTS achieves the highest summed mean similarity and lowest summed variance consistently. Figure 4 provides empirical justification for the overlap coefficient α=2 via log-density ridgelines.

5. **Evaluation across multiple LLMs** — Experiments use GPT-4.1, Gemma3-27B, and Qwen3-32B (with thinking mode), plus three embedding models. The consistent findings across these configurations strengthen the empirical claims.

## Weaknesses

### Fatal
None.

### Major
1. **No ablation study isolating component contributions** — AMADEUS has three components (ACTS, GS, AE), but the main evaluation (Table 4) compares the full pipeline against baselines that differ on all dimensions simultaneously. There is no experiment measuring, e.g., "Naive RAG + ACTS (no GS/AE)" or "AMADEUS without AE" on the downstream CharacterRAG or MBTI/BFI tasks. While Table 2 evaluates ACTS in isolation on similarity scores (a proxy metric) and Table 3 evaluates GS→AE via human eval, the paper does not show whether all three components are necessary for the downstream performance gains. The improvement on CharacterRAG (92.67% vs 91.33% on GPT-4.1) is modest, making it unclear whether the gains are driven primarily by ACTS (better chunking) or require the full pipeline. Without this ablation, the paper's central claim that the *framework's design* enhances persona consistency is incompletely supported — the improvement could be driven entirely by ACTS, with GS and AE adding little.

2. **MBTI/BFI type classification mechanism is underspecified** — The paper states (Section 5.2) that the model's free-text responses are "compared to psychological test outcomes for the character, as determined by thousands of actual participants' votes." However, it does not explain how the model's *free-text responses* are converted into a predicted MBTI or BFI type. Is there a second classifier? An LLM-based judge? A rule-based scoring system? The validity of Table 1's headline accuracy numbers (85%, 81.33%) depends critically on this pipeline, which is not described. The paper cites prior work (Wang et al., 2024b; Park et al., 2025) for the interview-based assessment protocol, but the specific type-classification step should be detailed here for the paper to be self-contained, especially since classifying MBTI/BFI types from free text is non-trivial and method-dependent.

### Minor
1. **No statistical significance or variance reporting** — Key comparisons (Table 1, Table 4) report only point estimates. With 450 QA pairs across 15 characters, per-character variance or bootstrapped confidence intervals would help assess whether the observed differences (especially the small margins on CharacterRAG) are meaningful. For example, AMADEUS achieves 92.67% vs Naive RAG's 91.33% on GPT-4.1 — a difference of ~6 correct answers out of 450, which could easily fall within noise.

2. **Computational cost and latency not discussed** — AMADEUS makes up to N=30 LLM calls per query in GS (though early termination when slot M=2 is full reduces this), plus the AE extraction call. The paper is silent on latency and token cost relative to baselines, which matters for practical deployment of a system that claims to be "training-free."

3. **Prompt templates for GS and AE are not provided** — The LLM prompts used for the guided selection check ("does this chunk contain inferable attributes?") and attribute extraction are essential for reproducibility but not included. LLM behavior is highly sensitive to prompt wording.

4. **Language considerations not discussed** — CharacterRAG is constructed from Korean wiki data and is in Korean. The paper does not address whether the results generalize to English or other languages, especially since the tested LLMs have varying Korean proficiency.

5. **Definition of l_max is somewhat underspecified** — ACTS's core parameter is defined as "the maximum length of the paragraphs that constitute the persona" (Equation 4), with φ described only as "a length-calculating function." The paper does not specify what constitutes a "paragraph" in the persona document hierarchy. This is a minor clarity issue for reproducibility.

### Trivial
None.

## Nice-to-Haves
- An ablation isolating ACTS, GS, and AE contributions on both CharacterRAG and MBTI/BFI tasks would transform the paper's contribution from "the full system works" to "here is why each component matters."
- Specifying the MBTI/BFI type classification protocol in detail (including prompts or decision rules) would make the evaluation self-contained and address the most significant transparency gap.
- Releasing prompt templates for GS and AE would aid reproducibility.
- A brief analysis of token usage and latency across methods would help practitioners assess the practical trade-off.

## Removed Points
- **"Comparison with CRAG/LightRAG is fundamentally unfair"** — The paper is comparing different RAG methods applied to role-playing, which is a standard benchmarking approach for systems papers. This is a valid comparison; the underlying concern (lack of component isolation) is already captured in Major weakness 1.
- **"Small margins on CharacterRAG invalidate the results"** — The margins are modest on CharacterRAG but the MBTI/BFI results show large, convincing gaps. This observation is already implicit in Major weakness 1 (we don't know what drives the gains) and Minor weakness 1 (no significance testing).
- **"The central claim is unsupported"** — Overstated. Table 1 provides strong evidence that the full AMADEUS system outperforms baselines on out-of-knowledge tasks. The missing ablation limits *attribution* but does not invalidate the empirical finding.
- **Strength Finder's generic or overly broad strengths** (e.g., "addressed an important problem," "targeted an interesting question") — Removed as lacking concrete, paper-specific evidence.
- **"The evaluation is underspecified to the point where headline numbers cannot be evaluated"** — This is a legitimate concern but is more precisely scoped as a specific gap (classification mechanism not described) rather than a wholesale invalidation of the evaluation.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add an ablation study that isolates ACTS, GS, and AE on both CharacterRAG and MBTI/BFI tasks. At minimum, compare: (a) Naive RAG + ACTS (no GS, no AE), (b) Naive RAG + ACTS + GS (no AE), (c) full AMADEUS, all on the same evaluation tasks. This single addition would substantially strengthen the paper.
2. Specify the MBTI/BFI type classification protocol in detail — how are free-text responses mapped to personality types? Provide the prompts or decision rules used.
3. Report per-character variance or bootstrapped confidence intervals for the key results in Tables 1 and 4.
4. Include prompt templates for GS and AE in the appendix.
5. Add a brief discussion of computational cost (latency, token usage) relative to baselines.
6. Discuss potential language-specific effects since CharacterRAG is Korean.

## Score and Decision

**Calibration Anchors:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| MMRole (FGSgsefE0Y) | 6.50 (Accept) | 1 | Stronger dataset (85 chars, 14K dialogues vs 15 chars, 450 QA), fewer methodological gaps. Our paper is weaker. |
| Tell Me What You Don't Know (87DtYFaH2d) | 5.20 (Reject) | 1 | Weaker evaluation (no human eval, single LLM focus). Our paper is stronger. |
| PersonaEval (wZbkQStAXj) | 4.00 (Reject) | 1 | Different contribution (benchmark for evaluators, not method). Our paper has stronger technical contribution. |
| GasketRAG (TqLY7QoELU) | 6.00 (Reject) | 2 | RAG alignment method, different domain. Similar severity of weaknesses (overclaiming, novelty concerns). |
| SubgraphRAG (JvkuZZ04O7) | 6.00 (Accept) | 2 | KG-RAG method with ablation studies but missing baseline comparisons. Our paper has human evaluation it lacks. |
| LightRAG (bbVH40jy7f) | 5.25 (Reject) | 2 | Graph-based RAG method; different domain. Rejected for limited novelty. |
| Follow My Instruction (Y4aWwRh25b) | 6.75 (Accept) | 2 | RAG security study; very different topic. Not directly comparable. |

**Round 1 bracket**: 5.5–6.5. The paper is clearly stronger than Tell Me What You Don't Know (5.20) and weaker than MMRole (6.50).

**Round 2 narrowing**: The paper's contributions (new dataset, human evaluation, multi-LLM evaluation, novel application of RAG to role-playing) are solid, but the two major weaknesses — missing ablation and underspecified MBTI/BFI classification — prevent it from reaching the acceptance tier. The paper is closest to the 5.5–6.0 range.

**Final Score**: 5.5

**Decision**: Reject (needs major revision to address the two major weaknesses before acceptance)

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>