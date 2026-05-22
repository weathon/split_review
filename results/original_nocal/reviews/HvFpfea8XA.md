Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes AMADEUS, a training-free framework for retrieval-augmented role-playing agents (RPAs) composed of three components: Adaptive Context-aware Text Splitter (ACTS), Guided Selection (GS), and Attribute Extractor (AE). To support this, the authors manually construct CharacterRAG, a dataset of 15 fictional characters with 976K written characters of persona documents and 450 QA pairs. The key claim is that AMADEUS maintains persona consistency even when answering questions that lie beyond a character's explicit knowledge, evaluated via MBTI/BFI personality type prediction and QA accuracy on the new dataset.

## Strengths

- **Meaningful empirical improvement on MBTI/BFI out-of-knowledge evaluation**: Table 1 shows AMADEUS achieves 85.00% MBTI accuracy with Σ|d|=9 vs. Naive RAG at 65.00%/21 and 81.33% BFI accuracy with Σ|d|=14 vs. Naive RAG at 72.00%/21. These are substantial gaps (20pp and 9pp respectively) that go well beyond prior RAG baselines, directly supporting the claim that the framework handles out-of-knowledge queries.

- **ACTS demonstrably improves chunk quality**: Table 2 shows ACTS achieves the highest sum of mean similarity scores (6.8575 with BGE-M3, 8.6226 with Qwen3-0.6B, 12.3240 with mE5) and the lowest sum of variance across all three embedding models, compared to RCTS, MHTS, SemanticChunker, and ATS. The consistent improvement across models makes this more than a one-off finding.

- **Human evaluation validates the GS+AE pipeline**: Table 3 reports mean Likert scores µ=3.97 (BFI) and 3.90 (MBTI) with Cronbach's alpha 0.825 and 0.810 (both exceeding the 0.8 threshold), based on 14 evaluators scoring 60 random samples. This provides direct evidence that the inferred attributes are reasonable from a human perspective.

- **Manual construction of a dedicated RAG-based RPA dataset (CharacterRAG)**: The dataset fills a genuine gap — no prior dataset was designed for RAG-based role-playing evaluation. The manual removal of external/out-of-character information and preservation of hierarchical subsection structure (§2.1–2.2) are thoughtful design decisions that make the dataset usable for future work.

- **Systematic evaluation across model families**: Results are reported on GPT-4.1, Gemma3-27B, and Qwen3-32B with three embedding models (BGE-M3, Qwen3-0.6B, mE5-large-instruct), comparing against Naive RAG, CRAG, and LightRAG (§5.1, Table 4). This establishes that the improvements are not model-specific.

## Weaknesses

### Fatal
None.

### Major

- **No ablation study isolating the three components**: The method has three distinct sub-stages (ACTS, GS, AE), yet every experiment compares the full AMADEUS against external baselines. Without ablations that remove ACTS, GS, or AE individually, it is impossible to attribute the observed gains to any specific component or synergy between them. For example, Table 1's large improvements (85% vs. 65% on MBTI) could stem primarily from ACTS, GS, or AE, or their combination — the reader cannot tell. Table 4's small margins on CharacterRAG (e.g., 92.67% vs. 91.33% for GPT-4.1) are precisely the kind of result where an ablation would reveal whether the expensive GS+AE steps are actually necessary.

- **No uncertainty quantification or statistical significance**: None of the results in Tables 1, 4, or Figure 5 report standard deviations, confidence intervals, or significance tests. Many reported differences are small (e.g., 1.34% ACC gap on CharacterRAG with GPT-4.1; 0.45% with Qwen3-32B). Without multiple runs or statistical testing, the reader cannot determine whether these differences reflect genuine improvement or measurement noise. This is especially concerning because the primary LLM-based metrics (ACC, ACC_L, HS) are used without any human correlation or calibration study.

- **The MBTI/BFI evaluation is a well-established but indirect proxy, and its limitations should be more clearly acknowledged**: The paper follows prior work (Wang et al., 2024b; Park et al., 2025) in using personality-type prediction accuracy as a proxy for persona consistency. The ground-truth labels are crowdsourced from personality-database.com (thousands of user votes per character), and the metric measures whether the aggregate of 60/120 forced-choice responses maps to a static label rather than evaluating turn-by-turn conversational consistency. While this is a field-standard approach and not a fatal flaw, the paper would benefit from explicitly discussing these limitations and supplementing with a more direct consistency measure (e.g., human judgments of dialogue coherence).

- **The HS results in Figure 5 show CRAG outperforming AMADEUS on 2/6 settings without comment**: For Qwen3-32B, CRAG achieves lower (better) HS than AMADEUS on both MBTI (1.80 vs. 2.04) and BFI (1.96 vs. 2.03). This is not addressed in the text. While the paper correctly bolds the best values in the table, the lack of discussion is a gap — readers expect an explanation for why the proposed method underperforms on hallucination scores for this particular LLM.

### Minor

- **Limited dataset diversity and scale**: CharacterRAG contains 15 fictional characters from a single Korean wiki source (Namuwiki), all from anime/manga, with 450 QA pairs total (30 per character). The small scale and single-genre/single-source origin limit claims of generality. The paper acknowledges the source but does not discuss how this affects generalizability to other media, Western characters, or non-anime genres.

- **No inter-annotator agreement reported for dataset construction**: The dataset construction is described at a high level (§2.1) — "manually removed" external information, "reconstructed from the perspective of each character" — but no quality metrics (agreement rates, kappa) are reported. Since the dataset is a central contribution, this is a notable omission.

- **GS introduces substantial LLM cost with no efficiency comparison**: GS iterates over chunks sorted by similarity (up to N=30 LLM calls per query, §4.2, Algorithm 1) to decide if a chunk supports attribute inference. The paper does not compare against cheaper alternatives (e.g., top-K similarity retrieval, simple prompting) to justify this cost.

- **Human evaluation (Table 3) assesses only the attribute extraction step, not the final response quality**: While the human evaluation shows that GS+AE produces reasonable attributes, it does not validate that using these attributes actually improves the final generated response. The final responses are evaluated only via unvalidated LLM metrics.

- **SemanticChunker failure with mE5 not discussed**: In Table 2, SemanticChunker has missing entries ("-") for mE5-large-instruct, but the paper provides no explanation for this failure.

- **"Chunk duplication frequency" (Figure 1) is not formally defined**: The caption mentions the metric and reports average chunk usage rates, but the text never formally defines what is being measured or how it relates to persona consistency.

### Trivial
- The Figure 1 caption repeats thrice due to PDF extraction artifacts (not an author error).
- Some notation (e.g., "SCOA1", "SLUEI" in Table 1 BFI types) could benefit from a legend.

## Nice-to-Haves
- A qualitative comparison table showing Naive RAG vs. AMADEUS outputs for the same out-of-knowledge queries would help readers judge the real-world improvement.
- Sensitivity analysis of key hyperparameters: the overlap coefficient α in ACTS (currently justified only via similarity distributions in Figure 4, not end-to-end performance) and slot size M in GS (currently M=2 without justification).
- Comparative positioning against fine-tuned role-playing agents would contextualize the training-free approach.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The metric does not measure persona consistency in any direct sense" / "ground-truth labels are unreliable" (from Harsh Critic Critical Issue #1)**: The paper explicitly follows an established evaluation protocol from prior published work (Wang et al., 2024b; Park et al., 2025) that uses crowdsourced personality labels and interview-based assessments. Demoting this criticism from "fatal" to "major indirectness" — it is a known limitation of the methodology, not a fatal flaw unique to this paper. The limitation is real but the paper inherits it from the field; calling it "fatal" or claiming the "central claim collapses" is not supported given the field-standard methodology.

- **"Figure 5 discrepancy — text states AMADEUS is best"**: The text states "our framework achieves the best performance across all three LLMs" immediately following a discussion of Table 4 (CharacterRAG QA results), not Figure 5. In Table 4, AMADEUS is indeed best across all three LLMs. In Figure 5, the paper correctly bolds CRAG where CRAG outperforms. The text does not claim AMADEUS is best on Figure 5 across all settings. The failure to discuss CRAG's stronger HS on Qwen3-32B is retained as a minor weakness above.

- **"The paper lacks standard deviations or significance tests"**: Retained as a major weakness (not removed).

- **"Related work missing" / "no existing benchmark" claims**: Removed per rule — I cannot verify existence of missing related work from external sources.

- **Formatting/style nitpicks**: Removed per rule (PDF extraction artifacts, capitalization issues, etc.).

- **Strength "Problem motivation is timely"**: This is generic and lacks a specific anchor to the paper's concrete content. Removed.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Add ablation experiments**: Run AMADEUS w/o ACTS (replace with RCTS), w/o GS (use top-K similarity), and w/o AE (skip attribute extraction). This is essential for attributing improvements and would significantly strengthen the paper.

2. **Report uncertainty**: Re-run experiments with at least 3 random seeds (where applicable) or use bootstrapping to report confidence intervals for all main tables (1, 4, and Figure 5). This is critical given the small margins on CharacterRAG QA.

3. **Validate LLM-as-judge metrics**: Provide correlation with human judgments for a subset of responses, or calibrate the HS/ACC/ACC_L scores against expert annotations.

4. **CharacterRAG quality documentation**: Report inter-annotator agreement rates for the dataset construction process and provide detailed guidelines given to annotators.

5. **Explain the Qwen3-32B HS discrepancy**: Discuss why CRAG achieves lower hallucination scores on the MBTI/BFI setting for Qwen3-32B but not for GPT-4.1 or Gemma3.

6. **Formalize "chunk duplication frequency"** with a clear equation or definition in the main text.

## Score and Decision

Based on the paper's originality (thoughtful modular framework for a timely problem), importance of the research question (RAG-based role-playing with consistency under out-of-knowledge queries), claims supported by meaningful improvements on the MBTI/BFI evaluation but weakened by missing ablations and lack of statistical rigor, soundness of experiments (good breadth, shallow depth), clarity (well-structured but some definitions missing), and community value (dataset is a practical contribution):

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>