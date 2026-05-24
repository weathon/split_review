Now I have all the information I need. Let me compose the final review.

## Review of "Dynamic Context Adaptation for Consistent Role-Playing Agents with Retrieval-Augmented Generations"

### Summary

This paper proposes AMADEUS, a training-free RAG framework for role-playing agents, comprising three components: Adaptive Context-aware Text Splitter (ACTS) for persona-aware chunking with hierarchical context, Guided Selection (GS) for LLM-based chunk reranking, and Attribute Extractor (AE) for summarizing character attributes from retrieved chunks. The paper also introduces CharacterRAG, a manually constructed dataset of 15 anime characters with 976K characters of persona text and 450 QA pairs, designed specifically for RAG-based role-playing evaluation. Experiments across multiple LLMs and embedding models show improvements over Naive RAG, CRAG, and LightRAG on personality inference (MBTI/BFI) and knowledge-grounded QA tasks.

### Strengths

1. **CharacterRAG dataset fills a gap.** The paper constructs the first dataset specifically designed for RAG-based role-playing agents, with manually cleaned persona documents (stripped of meta-information), hierarchical structure, and 450 QA pairs across six attribute types. This is a concrete resource contribution that the community can build on.

2. **Clear motivation and coherent pipeline design.** The paper identifies a genuine problem — RAG-based RPAs hallucinate or produce uninformative responses when queries fall outside a character's explicit knowledge — and proposes a three-stage pipeline (ACTS→GS→AE) with each stage targeting a specific aspect of the problem. The training-free design is practical.

3. **Solid chunking analysis (ACTS).** Table 2 provides clean evidence that adaptive persona-length chunking with hierarchical context (ACTS) outperforms standard chunking methods (RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter, SemanticChunker) across three different embedding models, both in mean similarity and variance. This evaluation is well-controlled.

4. **Human evaluation of GS and AE.** Table 3 reports a mean Likert score near 4/5 with Cronbach's alpha > 0.8 across 14 evaluators, supporting the claim that the GS+AE pipeline produces reasonable attribute inferences from a human perspective.

5. **Comprehensive LLM and embedding coverage.** Experiments span three LLMs (GPT-4.1, Gemma3-27B, Qwen3-32B) and three embedding models (BGE-M3, Qwen3-0.6B, mE5-large-instruct), providing robustness checks that the trends are not model-specific.

### Weaknesses

#### Major

1. **Asymmetric baseline comparison confounds the source of improvement.** AMADEUS uses GPT-4.1 for Guided Selection (LLM-based chunk reranking) and Attribute Extraction, while none of the baselines (Naive RAG, CRAG, LightRAG) receive any LLM-in-the-loop augmentation during retrieval. The large gains on MBTI/BFI (85% vs. 65% for MBTI accuracy) could be substantially driven by the additional reasoning capacity of GPT-4.1 during retrieval/selection rather than by the specific algorithmic design of ACTS, GS, or AE. The paper lacks a control experiment — e.g., augmenting Naive RAG with a GPT-4.1-based reranker, or replacing GS with pure embedding-based selection while keeping AE. Without this, the reader cannot attribute the observed gains to the proposed technical contributions.

2. **No ablation of the three components on downstream tasks.** The paper never isolates the contributions of ACTS, GS, and AE on the final generation metrics (ACC, ACC_L, HS). Table 2 evaluates ACTS only on similarity scores (not downstream accuracy). Table 3 evaluates GS+AE reasonableness in isolation. But there is no experiment like "AMADEUS w/o AE" or "AMADEUS w/o GS" on the CharacterRAG or MBTI/BFI tasks. This makes it impossible to determine which component drives the improvements, or whether a simpler pipeline (e.g., ACTS + top-K retrieval + a generic "use the persona" prompt) would achieve comparable results.

#### Minor

3. **Personality evaluation ground truth is unvalidated.** The MBTI and BFI ground-truth labels come from personality-database.com, a fan-voted website with no expert validation. While this follows established practice in prior work (Wang et al., 2024b), the paper does not discuss this limitation, and the reported accuracy numbers rest on labels whose reliability is unknown. The "accuracy" metric (dimension-level match rate) is consistent with the reported ∑|d| values (the critic's numerical discrepancy claim is incorrect — see Removed Points) but the table caption does not explain how accuracy is computed, which invites confusion.

4. **No confidence intervals or significance tests.** Given the modest test sizes (60 MBTI questions, 120 BFI, 450 CharacterRAG questions), the reported improvements may fall within noise. The paper should report per-character variance or bootstrap-based intervals, especially for the personality inference results where some per-character predictions vary substantially.

5. **Overstated claim about graph-based RAG unsuitability.** The paper asserts that "graph-based RAG methods are not well suited for RPA applications" based on testing only LightRAG (with a passing reference to GraphRAG). This overgeneralizes from a single implementation and does not consider the possibility that different graph construction strategies or hyperparameter tuning could yield different results.

6. **Experimental details are underspecified.** The number of retrieved chunks K is never explicitly stated for the baselines or for the AMADEUS fallback case. The data translation process (Korean Namuwiki source to English examples) is not described. These details matter for reproducibility, though the prompts and other implementation specifics are presumably in the appendix (which was stripped by the PDF parser).

#### Trivial

7. **Figure 1 caption garbled.** The caption lists MBTI types (e.g., ISTP appears six times) in a way that does not correspond to the actual character types from Table 1, suggesting a copy-paste or formatting error in the figure caption.

### Nice-to-Haves

- Add a baseline where Naive RAG is augmented with a GPT-4.1 reranker to control for LLM usage during retrieval.
- Add ablation experiments on CharacterRAG: (i) AMADEUS w/o GS (top-K embedding selection instead), (ii) AMADEUS w/o AE (no attribute context in prompt), (iii) ACTS only.
- Report wall-clock time and number of LLM calls per query to quantify the computational cost of GS and AE.
- Provide an error analysis showing which characters or attribute types are hardest for AMADEUS.

### Removed Points

The following points raised by the harsh critic are removed with justification:

- **MBTI accuracy numerical discrepancy:** The critic claimed ∑|d|=9 is inconsistent with 85% accuracy. However, accuracy is dimension-level: (60 total dimensions − 9 errors) / 60 = 85%. This is internally consistent. The accuracy definition is unsurprising given that ∑|d| is a dimension-level sum, but the table caption could be clearer. **Reason:** Factually wrong.

- **Missing prompts / appendix content:** The critic faults the paper for not providing GS/AE prompts. The PDF parser strips the appendix; these details exist in the original submission. **Reason:** Parser artifact per hard rules.

- **Duplicate MBTI types in Figure 1 caption as a significant issue:** While the caption contains garbled type listings, this is a minor formatting error in the figure caption, not a research flaw. **Reason:** Trivial presentation issue, downgraded from the critic's framing.

- **Question about Korean data with English examples:** The paper states annotators "directly reconstructed" the persona from Namuwiki (Korean wiki). It is implicit that the annotators produced English text; the lack of explicit mention is a minor clarity gap but not a substantive weakness. **Reason:** Weakened per soft rules; data construction process is described.

### Novel Insights

None beyond the paper's own contributions. The key insight — that adaptive chunking with hierarchical context plus LLM-guided selection and attribute extraction can improve RAG-based role-playing — is clearly presented in the paper itself.

### Suggestions

1. **Add a controlled baseline.** Run Naive RAG with an LLM-based reranker (same GPT-4.1) over the chunks retrieved by embedding similarity. If AMADEUS still outperforms this baseline, the gains are clearly attributable to the specific GS and AE designs rather than to LLM reasoning alone.

2. **Provide a full ablation study on CharacterRAG.** Remove or replace each component one at a time (ACTS→fixed chunking, GS→top-K, AE→no-attribute prompt) and report ACC, ACC_L, and HS. This is the single most impactful addition for the paper's credibility.

3. **Clarify the accuracy metric definition** in Table 1's caption and/or the main text.

4. **Tone down the claim about graph-based RAG unsuitability**, or support it with experiments on more than one graph-based method.

### Score and Decision

**Round 1 bracketing:** The paper sits between weak anchors (avg 2.3–3.4, clearly flawed papers) and strong anchors (avg 7.75–8.0, rigorous full contributions). The relevant comparison band is the middle band (3.5–7.5).

**Round 2 narrowing within the bracket:** The most comparable anchors in the 4.0–6.5 range are:
- "Tell Me What You Don't Know" (5.20, **Reject**) — RPAs with representation analysis. AMADEUS has comparable experimental breadth but weaker evaluation control (no ablation, asymmetric baselines). Slightly weaker.
- "CtrlA: Adaptive RAG" (4.50, **Reject**) — RAG method with multiple components. AMADEUS has a more coherent pipeline and contributes a dataset. Slightly stronger.
- "BIG5-CHAT" (5.25, **Reject**) — LLM personality through training. Similar domain but different methodology. Comparable quality.
- "RAG-DDR" (6.00, **Accept**) — RAG training method with extensive experiments. AMADEUS has clearer evaluation gaps. Weaker.

The paper's contributions (dataset, pipeline design, chunking analysis) are genuine, but the two major weaknesses — asymmetric baseline comparison and missing ablation — prevent the empirical results from convincingly supporting the claimed advantages. This places the paper below the acceptance threshold.

**Final score: 5.0** — Marginally below the acceptance threshold. The paper tackles a worthwhile problem and makes concrete contributions, but the evaluation has structural gaps that must be addressed before the empirical claims are fully supported.

**Decision: Reject**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>