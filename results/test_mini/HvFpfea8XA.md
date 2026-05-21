## Summary

This paper proposes AMADEUS, a training-free RAG framework for role-playing agents with three components: Adaptive Context-aware Text Splitter (ACTS) for persona chunking, Guided Selection (GS) for retrieving chunks useful for inference, and Attribute Extractor (AE) for extracting personality traits from selected chunks. The authors also introduce CharacterRAG, a manually constructed dataset of 15 fictional characters (976K characters, 450 QA pairs) designed specifically for RAG-based role-playing evaluation. Experiments across three LLMs and three embedding models show that AMADEUS improves persona consistency metrics over standard RAG baselines.

---

## Strengths

1. **CharacterRAG dataset fills a gap in the literature.** The paper introduces the first dataset purpose-built for RAG-based role-playing evaluation. Prior role-playing datasets consist exclusively of dialogues; CharacterRAG provides structured persona documents with QA pairs and is explicitly designed so that external information that could cause persona inconsistency is removed (§2.1). This is a concrete, reusable resource.

2. **ACTS is validated as an effective chunking strategy.** Table 2 shows that ACTS (adaptive chunk length + hierarchical context) achieves higher sum-of-mean similarity scores and lower sum-of-variance across BGE-M3, Qwen3-0.6B, and mE5-large-instruct compared to RCTS, MHTS, SemanticChunker, and ATS (ablation without hierarchical context). The ACTS-vs-ATS comparison specifically confirms the value of adding hierarchical context.

3. **Comprehensive evaluation scope.** The paper evaluates across three LLMs (GPT-4.1, Gemma3-27B, Qwen3-32B), three embedding models, and multiple evaluation protocols (CharacterRAG QA, MBTI, BFI) with human evaluation of the attribute extraction pipeline. The MBTI/BFI protocol (Table 1) shows large absolute improvements (85% vs 65–68% for baselines).

4. **Negative result about graph-based RAG is informative.** The consistent failure of LightRAG (34.67% BFI accuracy) and the degradation of CRAG on role-playing tasks is a documented finding that the community can build on.

---

## Weaknesses

### Major

- **No ablation isolating GS and AE — the core contributions are not independently evaluated.** The paper cannot attribute its reported gains to Guided Selection or Attribute Extractor because no experiment compares (a) ACTS + Naive RAG vs. (b) ACTS + GS vs. (c) ACTS + GS + AE (full AMADEUS). Table 4 confounds chunking differences (baselines use their own chunkers, AMADEUS uses ACTS) with GS/AE differences, making it impossible to determine how much of the improvement comes from better chunking versus the novel GS/AE components. The marginal improvements in Table 4 (e.g., +1.34% ACC for GPT-4.1, +0.45% ACC for Qwen3-32B over Naive RAG) could plausibly be attributed entirely to ACTS. This is a structural gap in the experimental design.

- **No statistical significance or variance reported.** All results (Tables 1, 2, 4, Figure 5) are single-run point estimates without error bars, confidence intervals, or standard deviations. LLM outputs are stochastic; metrics like ACC and HS vary across runs. The 15-character evaluation is modest in size (450 QA pairs for Table 4), and without variance estimates, small differences (e.g., 92.67% vs 91.33%) cannot be assessed for reliability.

- **Evaluation circularity concern.** GS and AE are implemented using GPT-4.1 (§5.1, line 252). The LLM-based evaluation metrics (ACC, ACC_L, HS) are not specified (§5.2) — the evaluator model is unnamed. For the GPT-4.1-based experiments in Tables 1 and 4, this creates a closed loop: the same model family selects chunks, extracts attributes, generates responses, and (potentially) evaluates them. The human evaluation (Table 3) only validates the attribute extraction step, not the final response quality, so it does not break this circularity. Independent evaluation (e.g., a different evaluator model or human scoring of final responses) is needed to trust that reported gains are not artifacts of the evaluation protocol.

### Minor

- **Small margins on the main CharacterRAG evaluation.** In Table 4, AMADEUS improves over Naive RAG by only +1.34% ACC (GPT-4.1), +1.56% ACC (Gemma3-27B), and +0.45% ACC (Qwen3-32B). The Hallucination Score improvements are modest (0.24–0.39 on a 1–10 scale). Without ablation or variance, it is unclear whether these differences are practically significant.

- **Ground-truth reliability for MBTI/BFI evaluation.** The "ground truth" personality types are sourced from a single crowdsourced website (personality-database.com), representing fan consensus rather than objective ground truth. The paper follows prior work (§5.2) but provides no analysis of vote distribution, inter-annotator agreement, or sensitivity to label noise. Given that Table 1 provides the strongest evidence for persona consistency, the reliability of this reference standard matters.

- **Dataset scope and construction details.** CharacterRAG covers only 15 characters, all from anime/manga, sourced from a single Korean wiki. The persona excerpt in Figure 2(b) uses third-person narrative ("Tanjiro was born..."), which contradicts the claim that documents are "directly reconstructed from the perspective of each character" (§2.1). No information on annotator agreement or character selection criteria is provided.

- **Overclaim about graph-based RAG unsuitability.** The paper concludes that "graph-based RAG methods are not well suited for RPA applications" (§5.3) based on a single implementation (LightRAG) used off-the-shelf without optimization for role-playing. This is an overgeneralization.

### Trivial

- The overlap coefficient is set to α=2 (l_o = l_max/2) with limited empirical justification beyond Figure 4's ridgeline analysis, which assumes a normal distribution without testing that assumption.

---

## Nice-to-Haves

- A cost analysis showing average token usage per query for the GS loop (up to N=30 LLM calls per query).
- Reporting which LLM is used as the evaluator for ACC/ACC_L/HS.
- Adding the GS/AE prompts (if not already in the appendix) and the evaluation prompts to improve reproducibility.

---

## Removed Points

These points surfaced in the reviews but are removed from the main assessment for the reasons noted:

1. **Figure 1 CDF quality complaint** — The reviewer claimed the CDFs are "nearly indistinguishable" and the difference is "not visually supported." However, the paper provides explicit quantitative values (34.93% vs 43.84% chunk usage rates). The visual quality concern is partly a PDF-extraction artifact and partly subjective; the quantitative claim stands.

2. **Missing prompts for GS/AE** — Per the hard rule, the parser strips appendix sections from all papers. Prompts and implementation details may be present in the original submission's appendix. This criticism cannot be evaluated from the accessible text.

3. **CRAG/LightRAG baseline "unfair comparison"** — The reviewer argued that using CRAG/LightRAG off-the-shelf is unfair because they weren't designed for role-playing. Evaluating baselines as-is is standard practice, and the paper's claim is precisely that these methods are *unsuitable* — a finding supported by the data. The asymmetry favors baselines (since they should perform worse on an unfamiliar task), not the proposed method.

4. **Overgeneralization about graph-based RAG** — The paper acknowledges "While we did not perform a direct comparison" (regarding GraphRAG), and the finding is presented as empirical observation about LightRAG specifically, not as a blanket claim about all graph-based methods.

5. **Missing inter-annotator agreement for dataset** — This is a reasonable suggestion for improvement but raised only by the harsh critic's section-by-section sweep; it does not threaten the core claims.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Add an ablation study** comparing (a) ACTS + Naive RAG, (b) ACTS + GS, (c) ACTS + GS + AE. This is the single most impactful addition — it would isolate the contribution of each component and is essential for the paper to support its claims.

2. **Report statistical significance.** Repeat experiments 3–5 times with temperature > 0 and report means with standard deviations or confidence intervals.

3. **Break the evaluation circularity.** Specify the evaluator model. For a subset of responses, have a different model (e.g., using Gemma3-27B outputs evaluated by GPT-4.1, or vice versa) or human evaluators score final response quality for persona consistency.

4. **Clarify the chunking used by each baseline in Table 4.** If Naive RAG uses its default chunker (e.g., RecursiveCharacterTextSplitter), state this explicitly.

5. **Document the MBTI/BFI ground truth more thoroughly** — report vote counts per character and discuss potential label noise.

---

## Score and Decision

**Calibration procedure:**

*Round 1 (bracketing):* Queried for topically similar papers in three bands. Low band (score < 3.5) returned papers like *ConfRAG* (3.00), *MAPS* (3.33), *LLM Behavioral Coherence* (1.50). Mid band (3.5–7.5) returned *R4: Nested Reasoning-Retrieval for Reward Modeling in Role-Playing Agents* (5.50), *Interact-RAG* (5.50), *Con-RAG* (4.00), *PersonaAgent* (4.00). High band (>7.5) returned papers scoring 8.00 (e.g., *Gaia2*, *LLMs Get Lost in Multi-Turn Conversation*) with no topical overlap.

*Initial bracket:* 3.5–5.5.

*Round 2 (narrowing):* Queried within the bracket for role-playing/RAG papers. Retrieved *Enhancing Persona Following at Decoding Time* (6.50) and *ChronoPlay* (5.33) in addition to prior anchors. Read full reviews for R4 (5.50, Accept Poster), Con-RAG (4.00, Reject), ChronoPlay (5.33, Accept Poster), and Enhancing Persona Following (6.50, Accept Poster).

**Anchor comparison (all anchors across both rounds):**

| Anchor | Score | Round | Comparison to this paper |
|--------|-------|-------|------------------------|
| *R4* (sWQSbVsPEz) | 5.50 | 1,2 | More rigorous evaluation (multiple runs, stronger baselines), similar domain. This paper is weaker. |
| *Interact-RAG* (yHUjWb6eMe) | 5.50 | 1 | Stronger ablations and evaluation. This paper is weaker. |
| *Con-RAG* (4IyULUbzQO) | 4.00 | 1,2 | Clear methodological flaws (prompt leakage). This paper is stronger in contribution. |
| *PersonaAgent* (Id97yjKWMG) | 4.00 | 1 | Similar scope, withdrawn decision. Comparable. |
| *ChronoPlay* (NLFxQedK9y) | 5.33 | 2 | Similar LLM-as-Judge concerns, benchmark contribution. Comparable overall. |
| *Enhancing Persona Following* (lVE8H8QNcx) | 6.50 | 2 | Much stronger evaluation with multiple benchmarks, ablation. This paper is clearly weaker. |
| *ConfRAG* (1OLTJL1wHG) | 3.00 | 1 | Fundamental methodological issues. This paper is stronger. |
| *MAPS* (VVJeDnuo4c) | 3.33 | 1 | Weak evaluation. This paper is stronger. |
| *Adaptive Friend Agent* (wKTwm7ZzDK) | 2.40 | 1 | Thin contribution. This paper is stronger. |

The paper contributes a useful dataset and validates ACTS's chunking improvements, but the experimental evaluation cannot support the claimed contributions of GS and AE due to missing ablations, no statistical significance, and circularity concerns. Comparing against the anchors, the paper sits below the 5.33–5.50 Accept-level papers but above the 3.00–4.00 Reject-level papers.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>