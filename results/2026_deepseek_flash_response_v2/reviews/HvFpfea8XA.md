Now I have enough calibration data. Let me finalize the review.

## Summary

The paper proposes AMADEUS, a training-free RAG framework for role-playing agents (RPAs), consisting of three components: Adaptive Context-aware Text Splitter (ACTS) for optimal chunking with hierarchical context, Guided Selection (GS) for finding attribute-informative chunks, and Attribute Extractor (AE) for surfacing character attributes. The authors also manually construct CharacterRAG, a Korean-language dataset of 15 fictional characters with 976K characters of persona text and 450 QA pairs. Experiments evaluate both within-knowledge QA and out-of-knowledge personality inference (MBTI/BFI).

## Strengths

1. **Strong results on out-of-knowledge personality inference (Table 1).** AMADEUS achieves 85.00% MBTI accuracy and 81.33% BFI accuracy across 15 characters, substantially outperforming the next-best baseline (CRAG at 68.33% MBTI, 76.00% BFI). The sum of absolute deviations drops from 21/19 to 9 (MBTI) and from 21/18 to 14 (BFI). This directly supports the paper's central claim about handling queries beyond explicit persona knowledge.

2. **ACTS consistently improves chunk quality across embedding models (Table 2).** ACTS achieves the highest sum of mean similarity scores and the lowest sum of variances for all three embedding models (BGE-M3, Qwen3-0.6B, mE5large-instruct), providing clear quantitative evidence that adaptive chunk sizing plus hierarchical context improves retrieval quality over fixed-size chunkers.

3. **First dedicated RAG-based role-playing dataset.** CharacterRAG is constructed by human annotators who manually remove editor-level information and reconstruct persona from the character's perspective. No prior benchmark explicitly targeted RAG-based role-playing, making this a foundational resource for a previously unaddressed evaluation gap.

4. **Human evaluation confirms GS+AE output reasonableness (Table 3).** Cronbach's alpha values of 0.825 (BFI) and 0.810 (MBTI) exceed the 0.8 threshold for high internal consistency, with mean Likert scores near 4.0 on a 5-point scale.

5. **Consistent gains across diverse LLMs (Table 4).** AMADEUS achieves best ACC, ACC_L, and HS across GPT-4.1, Gemma3-27B, and Qwen3-32B, demonstrating the framework's benefits are not backbone-specific.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation isolating the contribution of GS and AE on actual QA performance.** The two components that most distinguish AMADEUS from standard RAG — GS (up to 30 expensive LLM calls per query) and AE — are never ablated on the CharacterRAG QA task. Table 2 ablates ACTS vs ATS only on similarity-score distributions, not on QA accuracy. The human evaluation in Table 3 validates GS+AE outputs as reasonable, but does not tell us whether they improve downstream response quality. A controlled comparison (Naive RAG → +ACTS → +ACTS+GS → +ACTS+GS+AE) is needed to determine which components earn their keep, especially given the substantial computational overhead.

2. **Improvement on the within-knowledge task is marginal and lacks statistical grounding (Table 4).** AMADEUS improves over Naive RAG by only 1.34% on GPT-4.1 (91.33% → 92.67%), 1.56% on Gemma3-27B, and 0.45% on Qwen3-32B. No confidence intervals or significance tests are reported. While the paper's core claim concerns out-of-knowledge questions, the within-knowledge results serve as supporting evidence, and the marginal gains with no statistical grounding weaken this support. The paper would benefit from reporting whether these differences are reliable.

### Minor

1. **MBTI/BFI type inference methodology is not explained.** The paper follows interview-based assessment protocols from prior work (Wang et al., 2024b; Park et al., 2025) and states that it "conducts interview-based assessments... and compares the results to psychological test outcomes" (Section 5.2). However, it does not describe how a set of 60/120 question-responses is converted into a predicted four-letter MBTI type or SLOAN label. While referencing established evaluation protocols is standard practice, the paper's headline results (Table 1) rest on this procedure, and a brief description within the paper would improve verifiability.

2. **Ground-truth personality labels are crowd-sourced from a fan-voting site.** The paper uses personality-database.com as ground truth for fictional characters' personality types without acknowledging that this reflects popular fan interpretation rather than canonical or validated ground truth.

3. **GS cost and behavior are not analyzed.** The paper specifies up to 30 LLM calls per query for GS but does not report average iterations used, actual cost, latency, or what fraction of queries fall back to the Top-K+1 default (Algorithm 1, lines 14-16). This makes it difficult to assess the practical overhead of the framework.

4. **Derivation of l_max is underspecified.** ACTS determines l_max via a "length-calculating function φ" but does not specify whether length is measured in characters, tokens, or words, affecting reproducibility.

5. **CharacterRAG's scope is limited.** The dataset contains 15 characters from a narrow cultural domain (Japanese anime/Korean media) in a single language (Korean). This is mentioned in the ethics statement but not discussed as a limitation.

6. **No limitations section.** The paper presents only positive results; a limitations section would strengthen credibility.

### Trivial
None.

## Nice-to-Haves
- Adding GS and AE ablations on the CharacterRAG QA task (this would substantially strengthen the paper).
- A brief description of how MBTI/BFI predicted types are derived from model responses, even if following prior work.
- Reporting average LLM calls per query and total cost for GS.
- Statistical significance or confidence intervals for main results.

## Removed Points
These points from the harsh critic were removed or downgraded:
- **"Hallucination Score is under-specified"** — The paper defines HS (Section 5.2) as an LLM-based score from 1-10 and describes what it measures. Prompt details would typically be in the appendix (which was stripped by the parser). The level of detail is comparable to how other papers define LLM-based evaluation metrics.
- **"AE only extracts two attributes"** — The paper justifies this design choice in footnote 3. Reasonable scholars may disagree, but it is an explicit, motivated design decision, not an oversight.
- **"No comparison with fine-tuning-based or prompting-only methods"** — The paper explicitly scopes its comparison to RAG methods. Demanding non-Rag baselines is scope creep.
- **"O(N) runtime stated without derivation"** — This is a trivial runtime claim for a recursive traversal; no derivation is needed.
- **"No details about number of annotators or inter-annotator agreement for dataset"** — These details would typically be in the supplementary material, which was stripped by the parser.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Ablation study:** Compare Naive RAG → Naive RAG+ACTS → Naive RAG+ACTS+GS → Naive RAG+ACTS+GS+AE on the CharacterRAG QA task to isolate each component's contribution.
2. **Clarify MBTI/BFI inference:** Add a brief description of how predicted personality types are derived from model responses.
3. **Statistical grounding:** Report confidence intervals or bootstrap estimates for Tables 1 and 4.
4. **Limitations section:** Acknowledge dataset scope (15 characters, Korean-only, single cultural domain) and the crowd-sourced ground-truth limitation.

## Score and Decision

Let me explicitly lay out the calibration.

**Round 1 — Bracketing results:**
- Low band (<3.5): Papers scoring 2.33–3.00 (RAG benchmarks, multi-agent papers). The current paper is clearly stronger than these.
- Middle band (3.5–7.5): Papers scoring 4.00–6.50, including PersonaEval (4.00, Reject), RPA Refusal (5.20, Reject), MMRole (6.50, Accept), Human Simulacra (5.60, Accept).
- High band (>7.5): Papers at 8.00 — these are clearly stronger than the current paper.

Initial bracket: 4.5–6.5.

**Round 2 — Narrowing results:**
Anchors examined in full:
- MMRole (6.50, Accept): Larger multimodal dataset, trained model, but shallower methodology. Current paper has more novel methodological components but weaker experimental evidence. → Slightly weaker than MMRole.
- Human Simulacra (5.60, Accept): Comparable structure (dataset + method + personality evaluation). Similar experimental gaps (no ablations, marginal gains). Current paper has cleaner methodology. → Comparable or slightly stronger.
- RPA Refusal (5.20, Reject): Representation analysis + editing. Current paper is clearly stronger in methodological contribution and evidence. → Clearly stronger.
- Speculative RAG (5.50, Accept): Clean RAG method paper. Current paper is comparable in quality.

The current paper sits between the reject-level papers (~4-5) and the strong accept papers (6.5+). Based on the anchors, the most appropriate comparison is to Human Simulacra (5.60, Accept) and Speculative RAG (5.50, Accept) — papers with genuine contributions but notable experimental gaps. The current paper's missing ablation of GS and AE is a significant weakness that prevents a higher score, but the clear methodological contribution and strong out-of-knowledge results justify a borderline accept score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>