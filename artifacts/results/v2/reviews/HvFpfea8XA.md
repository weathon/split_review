## Summary

This paper introduces AMADEUS, a training-free retrieval-augmented generation (RAG) framework for role-playing agents (RPAs), composed of three components: Adaptive Context-aware Text Splitter (ACTS), Guided Selection (GS), and Attribute Extractor (AE). ACTS adaptively chunks persona documents with hierarchical context, GS selects chunks that can inform attribute inference, and AE extracts personality attributes (beliefs/values, psychological traits) from those chunks. The authors also contribute CharacterRAG, a manually constructed dataset of 15 fictional characters with 976K characters of persona text and 450 QA pairs. Experiments compare AMADEUS against Naive RAG, CRAG, and LightRAG on both within-knowledge QA (CharacterRAG) and out-of-knowledge personality inference (MBTI/BFI questionnaires).

## Strengths

- **CharacterRAG is the first dataset specifically designed for RAG-based role-playing agents.** It fills a gap left by prior role-playing datasets, which neither support RAG pipelines nor strip external editorial content that could contaminate persona consistency. The 15-character, 976K-character persona collection with 450 QA pairs across six attribute types is a useful resource for the community.

- **ACTS convincingly outperforms existing chunking methods on embedding-based metrics.** Table 2 shows that ACTS achieves the highest sum of mean similarity scores (∑μ) and lowest sum of variances (∑σ²) across three embedding models (BGE-M3, Qwen3-0.6B, mE5_large-instruct) when compared to RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter, SemanticChunker, and a non-contextual adaptive splitter. The improvement is consistent and the hierarchical context augmentation is a well-motivated design.

- **Human evaluation of GS and AE outputs shows high inter-rater reliability.** Table 3 reports Cronbach's alpha of 0.825 (BFI) and 0.810 (MBTI) from 14 evaluators on a 5-point Likert scale, exceeding the standard 0.7 threshold. This provides evidence that the attribute extraction process is reasonable from a human perspective.

- **AMADEUS demonstrates consistent improvements across three LLMs and three metrics.** Table 4 shows that AMADEUS achieves the best ACC, ACC_L, and HS on the CharacterRAG QA task for GPT-4.1, Gemma3-27B, and Qwen3-32B, with the pattern holding across all three models.

- **The paper identifies substantive limitations of graph-based and web-search-based RAG for role-playing.** The experiments show LightRAG achieving only 34.67% BFI accuracy (Table 1) and struggling with entity ambiguity, while CRAG shows inconsistent performance due to web search noise. These findings are informative for future RAG-based RPA research.

## Weaknesses

### Major

- **The central out-of-knowledge evaluation (MBTI/BFI) relies on ground-truth labels from a fan-voting site (personality-database.com) with no demonstrated reliability, and the prediction protocol is completely unspecified.** Table 1 is the primary evidence for the paper's core claim—that AMADEUS maintains persona consistency beyond explicit knowledge—but the ground-truth MBTI/BFI types come from "thousands of actual participants' votes" on a public fan site whose labeling methodology, consistency, and relevance to the canonical character descriptions are never established. More critically, the paper does not describe *how* the character's responses to 60 MBTI and 120 BFI questions are converted into a predicted four-letter MBTI type or SLOAN type. This is a black-box step in the evaluation pipeline; without it, the reported accuracies (85.00% MBTI, 81.33% BFI) and F1 scores cannot be verified or interpreted. The paper also does not report whether an LLM is used as the predictor (which would introduce circularity concerns since the generator and judge may share the same biases). Since the within-knowledge improvement is marginal (see below), the central claim almost entirely depends on this unverified evaluation.

- **No ablation study isolates the contributions of ACTS, GS, and AE on the downstream task.** The paper introduces three sub-components but never measures their individual impact on the quality of generated responses. Table 2 evaluates ACTS on similarity scores (a proxy metric). Table 4 compares the full AMADEUS against baselines but does not ablate AE or GS. It is impossible to attribute observed improvements to hierarchical chunking, guided selection, attribute extraction, or simply the increased prompt length. An ablation—e.g., Naive RAG → +ACTS → +GS → +AE on the CharacterRAG QA task—is necessary to demonstrate that each component is functional and justified.

### Minor

- **The within-knowledge improvement over Naive RAG is marginal and lacks significance testing.** On the CharacterRAG QA set with GPT-4.1, AMADEUS achieves 92.67% ACC vs. Naive RAG's 91.33%—a difference of 1.34 percentage points. No confidence intervals, significance tests, or multiple-trial statistics are reported, so it is unclear whether this gap is meaningful or within noise. The hallucination score improvement (2.89 vs. 3.13) is similarly small.

- **The MBTI/BFI prediction methodology is entirely unspecified.** Beyond the ground-truth concern, the paper does not explain how 60 (or 120) individual responses are aggregated into a single predicted personality type per character. This encompasses: (a) whether each response is independently classified and then voted, (b) whether standard MBTI/BFI scoring rubrics are applied to the character's answers, or (c) whether an LLM judge is prompted to produce a single type from all responses. This omission makes Table 1 uninterpretable.

- **The dataset construction lacks key details.** CharacterRAG is described as manually constructed by "human annotators," but the paper provides no information about the number of annotators, their qualifications, inter-annotator agreement, or the criteria for selecting the 15 characters. The dataset is in Korean (sourced from Namuwiki), but the paper does not discuss potential language bias or how English-language models handle translated persona prompts.

- **GS and AE rely on GPT-4.1 for every decision without error or cost analysis.** The paper does not report the token/API cost per query, the accuracy of the LLM judge in GS (e.g., human agreement on whether a chunk contains inferrable attributes), or any systematic analysis of failure cases where GS or AE produce incorrect outputs.

- **The claim that graph-based RAG is "unsuitable for role-playing" is based on a single instance (LightRAG).** While the evidence against LightRAG is clear, generalizing to all graph-based RAG methods from one configuration is too strong, especially since the paper acknowledges not directly testing GraphRAG.

- **The human evaluation (Table 3) assesses the reasonableness of attribute extraction, not whether using those attributes leads to better final responses.** The high inter-rater reliability shows the extraction is well-grounded, but it does not demonstrate that AE improves downstream role-playing quality over, e.g., naively including more retrieved chunks.

### Trivial

- The description of Table 1 is confusing as written. The paper says the parenthetical numbers "indicate the number of times the ground-truth type of each character was not correctly identified," but it is unclear whether this counts incorrect responses out of multiple trials or captures deviations at the dimension level (e.g., getting E/I wrong).
- M=2 (slot size) and N=30 (max iterations) are presented without any sensitivity analysis or justification.

## Nice-to-Haves

- Replace or complement the MBTI/BFI ground truth with verifiable attribute-based inference (e.g., situation questions whose answers are logically entailed by the persona), providing a direct test of out-of-knowledge consistency.
- Conduct a human evaluation of *final generated responses* for persona consistency on both within-knowledge and out-of-knowledge queries, rather than only evaluating the intermediate attribute extraction step.
- Provide the exact prompts used for GS and AE (likely in the appendix).
- Report confidence intervals or bootstrap estimates for all main results, especially the closely matched within-knowledge scores.

## Removed Points

*These points were flagged for removal and should be treated with caution.*

- **Missing prompts for GS and AE:** The harsh critic states that prompts are not provided. The paper includes an appendix (removed by the parser) and states supplementary materials will be released, so this concern may be addressed in the original submission. The deeper issue—lack of analysis of LLM-judge accuracy—is retained as a minor weakness.
- **Formatting, style, and grammatical nitpicks:** None of the reviews raised plausible formatting concerns that survive filtering.
- **Questioning the existence/release of CharacterRAG:** The paper clearly describes the dataset construction. Per the hard rules, any criticism that questions the existence of a cited resource is removed.
- **Suggestions to add more characters or enlarge the dataset:** This would be a generic request for more data when the current size (15 characters, 976K characters) is sufficient for demonstrating the framework's behavior.

## Novel Insights

None beyond the paper's own contributions—the main novel observation (graph-based RAG's unsuitability for role-playing) is already reported by the authors. The reviews do not surface a perspective that the paper itself misses.

## Suggestions

1. **Replace or transparently document the MBTI/BFI evaluation.** Either adopt a verifiable ground truth (e.g., attribute-based entailment questions) or provide a complete, step-by-step description of the prediction protocol, including how responses are mapped to predicted types, and a human validation study of the ground-truth labels.
2. **Run a component-level ablation** on the CharacterRAG QA task (and on any validated out-of-knowledge set) with each component added incrementally, reporting standard errors or confidence intervals.
3. **Provide a worked example** showing the full pipeline from a sample out-of-knowledge query through GS/AE to the final response, so readers can qualitatively assess the benefit.
4. **Report the token/API cost** of the GS and AE stages and include an analysis of LLM-judge accuracy (e.g., human agreement on a sample of GS decisions).

## Score and Decision

**Round 1 bracket:** Based on the calibration search, papers with similar topics and weakness profiles cluster between 3.0 and 5.5. The three topic-band queries placed the paper's plausible competitors at 2.33–3.00 (low band, weak evaluation RAG papers), 4.00–5.20 (middle band, role-playing/RAG papers with some issues), and 8.00 (high band, strong RAG papers with thorough evaluation). The weakness-anchored queries returned 3.50–5.75 for papers with personality evaluation concerns, and 3.50–5.00 for papers with missing ablation/component analysis. Initial bracket: **3.5–5.5**.

**Round 2 narrowing:** Inside the bracket, the most comparable anchor is *Tell Me What You Don't Know* (5.20, RPA paper with sounder central evaluation but accepting some methodology trade-offs). Papers around 4.0–4.5 (*PersonaEval* at 4.00, *CtrlA* at 4.50, *No Free Lunch* at 4.50) either had narrower scope or sounder evaluations for their specific claims. The current paper's central evaluation weakness (unverifiable MBTI/BFI ground truth and black-box prediction protocol) is more severe than what the 4.5+ anchors exhibit, and the missing ablation is a gap those papers did not share. However, the CharacterRAG dataset contribution and ACTS evaluation are stronger than the <3.75 anchors. Final bracket: **3.5–4.5**.

**Final anchor comparisons:**

| Anchor | Avg Score | Round/Query | Comparison |
|--------|-----------|-------------|------------|
| Reward-RAG (oqRe1KvD17) | 3.00 | R1-topic-low | Weak RAG paper with evaluation issues; current paper has stronger dataset and method contributions |
| PersonaEval (wZbkQStAXj) | 4.00 | R1-topic-mid | Role-playing evaluation benchmark; current paper has similar evaluation concerns but more substantive method contributions |
| Tell Me What You Don't Know (87DtYFaH2d) | 5.20 | R1-topic-mid | RPA paper with sounder central evaluation; current paper's out-of-knowledge evaluation is weaker |
| CtrlA (QYvtX2XA8p) | 4.50 | R1-topic-mid | Adaptive RAG with solid evaluation; current paper has weaker evaluation of its core claim |
| BIG5-CHAT (TqwTzLjzGS) | 5.25 | R2 | Personality-focused paper with stronger evaluation; current paper's personality evaluation is weaker |
| Corrective RAG (JnWJbrnaUE) | 3.75 | R2 | RAG paper with method unclear; current paper is clearer but evaluation is weaker |
| Agent-G (g2C947jjjQ) | 3.50 | R2 | Incremental graph RAG; current paper has more contribution but central evaluation is weaker |
| Quantifying AI Psychology (31UkFGMy8t) | 5.25 | R1-weakness | Personality evaluation paper with some validity concerns; current paper's personality evaluation is less rigorous |
| RAGGED (KDXj60FpJr) | 5.00 | R1-weakness | RAG analysis framework with solid methodology; current paper has weaker methodology |

**What did the low-band anchors fail at?** The <3.75 papers (Reward-RAG, Corrective RAG, Agent-G) all had evaluation designs that did not convincingly support their central claims—either missing critical baselines, using circular metrics, or failing to ablate components. The paper under review shares two of these failure modes: its central claim rests on an evaluation with questionable ground truth, and it lacks component-level ablation. However, the paper has a stronger artifact contribution (CharacterRAG dataset) and more extensive experiments across multiple LLMs, which differentiate it from the lowest band.

**Score: 4.0** — The paper has genuine contributions (the dataset, the ACTS design, the cross-LLM evaluation) but the evidence for its core claim (out-of-knowledge consistency) is significantly weakened by the unverifiable MBTI/BFI ground truth and opaque prediction protocol. The missing ablation further limits the ability to attribute improvements to specific components. These issues are addressable but prevent acceptance in the current form.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>