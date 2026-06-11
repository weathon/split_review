Now I have a clear picture. Let me finalize the review.

**Round 1 bracket:** 3.5–5.0 (adjusted from initial estimate per overestimation tendency)

**Round 2 narrowing:** The paper is stronger than CRAG (3.75) and PersonaEval (4.00), comparable to Knowledge Boundaries (4.33), and slightly below Late Chunking (4.75) and Tell Me What You Don't Know (5.20). 

**Final score: 4.5** — the paper has a genuine dataset contribution and a reasonable framework, but the empirical gains on the core task are marginal, component ablations are missing, and the out-of-knowledge evaluation rests on crowdsourced ground truth with no direct human evaluation of final responses.

---

## Summary
This paper proposes AMADEUS, a training-free RAG framework for role-playing agents (RPAs) that aims to maintain persona consistency even for queries beyond a character's explicit knowledge. AMADEUS consists of three components: Adaptive Context-aware Text Splitter (ACTS), which segments persona documents with adaptive chunk lengths and hierarchical context; Guided Selection (GS), which uses an LLM to identify chunks from which character attributes can be inferred; and Attribute Extractor (AE), which extracts Belief/Value and Psychological Traits from selected chunks. The paper also contributes CharacterRAG, a manually constructed dataset of 15 fictional characters with 976K written characters and 450 QA pairs.

## Strengths
- **ACTS demonstrates consistent retrieval improvement over alternative splitters.** Table 2 shows ACTS achieves the highest mean similarity and lowest variance across all three embedding models (e.g., 6.8575 vs. next-best 6.7007 with BGE-M3, variance 0.0784 vs. 0.0884). The improvement holds across BGE-M3, Qwen3, and mE_large-instruct, validating that adaptive chunk length with hierarchical context benefits retrieval for role-playing.
- **Human evaluation of attribute extraction shows good reliability.** Table 3 reports a 14-evaluator study where extracted attributes receive mean scores near 4 on a 5-point Likert scale, with Cronbach's alpha values of 0.825 (BFI) and 0.810 (MBTI), both exceeding the 0.7 threshold for acceptable reliability. This independently validates that the GS+AE pipeline produces reasonable attribute inferences.
- **Substantial improvement on out-of-knowledge personality-type prediction.** Table 1 shows AMADEUS achieves 85.00% MBTI accuracy and 81.33% BFI accuracy, substantially above baselines (65.00–68.33% and 34.67–76.00% respectively). Cumulative error drops from 19–21 to 9 (MBTI) and 18–49 to 14 (BFI). This demonstrates that the GS+AE mechanism can infer latent character traits that naive/graph/web-search RAG cannot access.
- **Comprehensive experimental coverage across RAG paradigms, LLMs, and embedding models.** The evaluation spans Naive RAG, CRAG, and LightRAG; GPT-4.1, Gemma3-27B, and Qwen3-32B; and three embedding models. The no-RAG baseline in Table 4 (e.g., GPT-4.1 drops to 49.56% without RAG) cleanly validates that LLMs lack inherent knowledge of these fictional characters.
- **CharacterRAG fills a genuine gap** as the first dataset designed for RAG-based role-playing, with 15 characters, hierarchical persona structure preserving section/subsection information, and 450 manually constructed QA pairs.

## Weaknesses

### Fatal
None.

### Major
- **Gains on the core in-knowledge task are marginal, and no component ablations exist.** Table 4 shows AMADEUS improves ACC from 91.33% to 92.67% on GPT-4.1 (+1.34pp) and from 78.44% to 78.89% on Qwen3-32B (+0.45pp). ACC_L moves from 9.23 to 9.26. These are thin margins, yet the method adds two GPT-4.1 inference calls per query (GS and AE). Without ablations isolating ACTS, GS, and AE on the CharacterRAG task, the reader cannot determine whether the full three-stage pipeline is justified or whether a simpler intervention (e.g., ACTS alone) would achieve comparable results. This weakens the evidence that the full AMADEUS framework is necessary.
- **The out-of-knowledge evaluation relies on crowdsourced ground truth, and direct response-quality assessment is missing.** Table 1 measures MBTI/BFI type prediction against ground truth from personality-database.com — a website where fans vote on fictional characters' personality types. While the paper follows prior work in using this source, the ground truth's reliability is not validated, and the metric measures personality-type classification rather than response quality. Table 3 evaluates whether extracted *attributes* are reasonable (an intermediate step), but there is no human evaluation of whether the *final generated responses* to out-of-knowledge questions are persona-consistent. Figure 5 reports LLM-based Hallucination Scores, which provides partial assessment, but the gap between measured proxies and the claimed capability remains.

### Minor
- **No limitations section.** Important unaddressed limitations include: reliance on GPT-4.1 for GS and AE, the small dataset size (15 characters, all from anime/manga with Korean source text), and the MBTI/BFI ground truth concern.
- **Computational cost of GS and AE is not quantified.** The method adds two LLM inference calls per query using GPT-4.1. Token consumption and latency relative to Naive RAG are not reported, nor is the fallback rate of GS (how often line 14 of Algorithm 1 is triggered, returning top-K similarity chunks when no chunks pass the LLM filter).
- **LLM-based evaluation metrics are not validated against human judgments.** ACC, ACC_L, and HS (Section 5.2) are used throughout but their correlation with human assessments is not discussed. If the evaluator LLM is GPT-4.1 (the same model powering GS and AE), self-assessment bias is a risk.
- **Dataset scope is narrow.** All 15 characters are from anime/manga with Korean source material. Generalizability to other character types (historical figures, Western media, original characters) is unexamined.

### Trivial
- **Algorithm 1 notation ambiguity:** Line 15 reads "Top-K + 1 chunks" — it is unclear whether this means Top-(K+1) or Top-K plus one additional chunk.
- **The claim about "thinking mode" failure** (Section 5.3, regarding Qwen3-32B) is based on a single model and merits more cautious phrasing.

## Nice-to-Haves
- Ablation experiments isolating ACTS, GS, and AE on both in-knowledge and out-of-knowledge tasks.
- Reporting computational cost (token usage, latency) for GS and AE versus Naive RAG.
- A small-scale human evaluation of final out-of-knowledge responses to directly validate the headline claim about persona consistency beyond explicit knowledge.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *"The similarity metric itself may favor larger chunks"* — Speculation not verifiable from the paper. ACTS uses max-paragraph-length chunks, but whether they are larger on average than fixed-size alternatives depends on the fixed size chosen, which the paper does not report. Cannot anchor to text.
- *"More uniform chunk usage does not necessarily mean better response quality"* — The paper uses chunk duplication uniformity as a motivating observation (Figure 1), not as an evaluative claim about response quality. Response quality is evaluated separately in Tables 1, 4, and Figure 5.
- *"The O(N) runtime claim is noted but the constant factor (LLM calls) dwarfs this"* — The O(N) claim in Section 4.1 is specifically about hierarchical context extraction, not about LLM calls. The paper is transparent that GS and AE involve additional inference.
- *"The overlap coefficient analysis normality assumption is stated without justification"* — The paper explicitly states "Normal assumption" in Figure 4's caption. A nonparametric check would be ideal but this is a methodological preference, not an error.
- *"GS's LLM-as-judge prompt is never shown"* — Per protocol, concerns about missing appendix/supplementary material are removed. The prompt may exist in the stripped appendix.
- *"Could engage more with recent work on chunking strategies"* — Per hard rules, missing related work suggestions are removed as we cannot verify their existence.

## Novel Insights
The paper's observation that graph-based RAG (LightRAG) and web-search RAG (CRAG) are fundamentally ill-suited for role-playing — due to entity ambiguity, graph construction costs, and web noise disrupting persona consistency — is a practically useful insight, substantiated by the consistent underperformance of both approaches across all LLMs (Table 4) and their near-collapse on BFI personality prediction (LightRAG at 34.67% accuracy in Table 1).

## Suggestions
- Add a limitations section acknowledging dataset size/domain, reliance on proprietary LLMs, and ground truth concerns.
- Report the fallback rate of GS (how often line 14 of Algorithm 1 is triggered) to clarify the component's actual contribution.
- Clarify Algorithm 1 line 15 notation.
- Consider a small-scale human evaluation of final out-of-knowledge responses to directly validate the headline claim.

## Score and Decision

**Anchor comparison summary (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| CRAG (JnWJbrnaUE) | 3.75 | R2 | Our paper stronger: adds dataset contribution, more comprehensive evaluation, no unfair comparison issues |
| PersonaEval (wZbkQStAXj) | 4.00 | R1/R2 | Our paper stronger: both method + dataset rather than benchmark-only, more direct application |
| Knowledge Boundaries (M1ZMwDqvSe) | 4.33 | R2 | Comparable: both have interesting ideas with execution gaps; our paper has dataset contribution |
| Late Chunking (74QmBTV0Zf) | 4.75 | R1/R2 | Slightly below: Late Chunking has better ablations; our paper has broader evaluation and dataset |
| UncertaintyRAG (SR8LFpmVun) | 4.75 | R1/R2 | Slightly below: UncertaintyRAG has stronger technical contribution |
| WinnowRAG (OnMRWwOqCs) | 5.00 | R1 | Below: WinnowRAG has more coherent framework and clearer gains |
| Tell Me What You Don't Know (87DtYFaH2d) | 5.20 | R1/R2 | Below: that paper has representation analysis adding depth |
| MMRole (FGSgsefE0Y) | 6.50 | R1 | Clearly below: larger scale, multimodal, trained model |

**Round 1 bracket:** 3.5–5.0. **Round 2 narrowing:** The paper lands between Knowledge Boundaries (4.33) and Late Chunking (4.75). It has a genuine dataset contribution and a reasonable framework, but the empirical gains are thin, ablations are missing, and the out-of-knowledge evaluation has validity concerns. Final score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>