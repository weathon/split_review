Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes AMADEUS, a training‑free RAG framework for role‑playing agents (RPAs), comprising three components: Adaptive Context‑aware Text Splitter (ACTS), Guided Selection (GS), and Attribute Extractor (AE). To support RAG‑based role‑playing, the authors also contribute CharacterRAG, a manually constructed dataset of 15 fictional characters (976K characters, 450 QA pairs). The framework is evaluated on in‑knowledge QA (CharacterRAG) and on out‑of‑knowledge consistency via MBTI/BFI personality questionnaires. Results show consistent improvements over Naive RAG, CRAG, and LightRAG, with particularly large gains on the MBTI/BFI tasks.

## Strengths

- **Large and consistent gains on out‑of‑knowledge questions.** On the MBTI type‑prediction task, AMADEUS raises accuracy from 65.00% (Naive RAG) to 85.00%, and on BFI from 72.00% to 81.33% (Table 1). These improvements are substantial and hold across 15 distinct characters, directly supporting the paper’s central claim about maintaining persona consistency beyond explicit knowledge.

- **CharacterRAG is a valuable new resource for RAG‑based role‑playing.** The dataset is manually constructed with care to remove editor‑speculated information and reconstructed from each character’s perspective. It provides 15 diverse personas (976K characters) and 450 manually annotated QA pairs across six attribute types. The dataset fills a clear gap — no existing benchmark targets RAG‑based role‑playing — and the experiments demonstrate that it can expose meaningful performance differences among methods (e.g., LightRAG 48.00% vs. AMADEUS 92.67% on GPT‑4.1, Table 4).

- **ACTS demonstrably improves retrieval quality.** Across three embedding models (BGE‑M3, Qwen3‑0.6B, mE5‑large‑instruct), ACTS achieves the highest sum of mean similarity scores and lowest variance compared to RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter, and SemanticChunker (Table 2). The benefit of adaptive chunking with hierarchical context is clearly supported.

- **Human evaluation confirms the reliability of GS and AE outputs.** Fourteen evaluators rated the chunks selected by GS and attributes extracted by AE, yielding mean Likert scores of 3.97 (BFI) and 3.90 (MBTI) with Cronbach’s α > 0.8 (Table 3). This provides independent validation that the intermediate pipeline outputs align with human judgment.

- **The framework is training‑free and consistently effective across three LLMs** (GPT‑4.1, Gemma3‑27B, Qwen3‑32B) and multiple embedding models, suggesting robustness of the approach.

## Weaknesses

### Fatal
None.

### Major

- **The MBTI/BFI evaluation pipeline is critically underspecified.** The paper does not describe how the RPA’s free‑form responses to 60 MBTI and 120 BFI questions are converted into four‑letter MBTI types or SLOAN types. Without this detail the experiment is not reproducible, and it is unclear whether the evaluation measures persona consistency or simply the evaluator’s ability to extract traits from coherent text. The ground truth (fan‑voted labels from personality‑database.com) also has known limitations that are not discussed. Since the MBTI/BFI experiments are the primary evidence for the paper’s central out‑of‑knowledge claim, this omission is significant.

- **No ablation study isolates the contribution of each component.** AMADEUS introduces three novel components (ACTS, GS, AE), yet the experiments only compare the full system against off‑the‑shelf RAG baselines. Without ablations (e.g., ACTS‑only, ACTS+GS without AE, full system), it is impossible to attribute improvements to specific mechanisms. This is especially problematic because the gains on CharacterRAG are modest (≈1% ACC on GPT‑4.1, Table 4) and could plausibly be driven by a single component or by confounded factors such as prompt design.

- **The language of the persona documents is not clarified.** The dataset is “based on Korean data” (Namuwiki, footnote 2) and the Ethics Statement refers to “the Korean‑language dataset,” yet all examples in the paper are in English and the MBTI/BFI questions are in English. The paper does not state whether the persona documents were translated to English or used in their original Korean. If they are in Korean, the retrieval is cross‑lingual, introducing an uncontrolled source of variation that could differentially affect methods. If they were translated, that process and its quality should be reported.

### Minor

- **No statistical significance testing for main results.** On the 450‑question CharacterRAG evaluation, the improvements over Naive RAG range from ≈0.5% to ≈1.6% across LLMs. No confidence intervals, significance tests, or multiple‑run statistics are reported. Without these, it is unclear whether the observed gains are reliable or within sampling variation.

- **The evaluator model for LLM‑based metrics is not specified.** The paper states that ACC, ACC_L, and HS are “LLM‑based metrics” but never identifies which LLM computes them. GS and AE use GPT‑4.1; if the same model also evaluates the outputs, this creates a potential evaluator‑bias confound. (The human evaluation in Table 3 only assesses the intermediate GS+AE outputs, not the final responses.)

- **No verification that the MBTI/BFI questions are truly outside the persona documents.** The paper states that these questions are “not included in the knowledge” but reports no manual or automatic check. If even a fraction of the questions have direct or nearly‑direct answers in the persona, the “out‑of‑knowledge” framing is weakened.

- **The numerical value of K (top‑k retrieval count) is not reported.** K is defined in Equation 3 and used in Algorithm 1’s fallback (“Top‑(K+1)”), but its experimental value is never stated. Similarly, the “+1” in the fallback is not explained.

- **Slot size M is fixed at 2 without justification or sensitivity analysis.** The paper does not explore alternative values or discuss how this choice affects performance.

- **Several table entries are unexplained.** In Table 4, LightRAG and w/o RAG show “‑” for Hallucination Score without any explanation for why this metric is omitted for those methods.

### Trivial

- Table 2’s aggregation (sum of μ, sum of σ²) is unusual; average values across the 15 characters would be more interpretable.
- Figure 1’s caption is confusing: the text describes each subplot by MBTI type rather than by character, which appears to be a description artifact.
- The paper states that the overlap coefficient α=2 is optimal based on Figure 4, but the differences among α=2,5,10,15 are visually very small and the supporting evidence is weak.

## Nice-to-Haves

- Ground‑truth verification that the MBTI/BFI questions have no answerable content in the persona documents (e.g., by checking if an LLM can answer them from the persona alone).
- End‑to‑end human evaluation of final responses (the current human eval in Table 3 only covers the intermediate GS+AE outputs).
- Sensitivity analysis for α (overlap coefficient), M (slot size), and N (max search iterations).

## Removed Points

The following points from the inputs were removed because they are factually wrong, reflect misunderstanding, or violate the hard rules:

- **“Chunk size in ACTS is not stated explicitly.”** The paper clearly states that chunk size = l_max (maximum paragraph length in the persona), defined in Equation 4. The critic appears to have overlooked this.
- **“Parameter K is never defined.”** K is defined in Equation 3 as the number of top‑k chunks. The numerical value is unspecified (a minor concern retained above), but the parameter itself is defined.
- **“Exact prompts for GS and AE are not provided.”** Per hard rules, criticisms about content that likely resides in the appendix (which is stripped by the parser) are removed. The prompts may be in the appendix; if not, this is a minor reproducibility concern already covered by the missing‑details items.
- **Several formatting/style nitpicks and speculative criticisms** (e.g., “caption claims each plot corresponds to an MBTI personality type but the experiment varies characters”, “could the metric be measuring a proxy”) were removed as they are either parser artifacts or speculation unsupported by the paper.
- **Criticisms about missing inter‑annotator agreement for dataset construction** are retained in spirit under “Minor” as the paper does not report this, but the critic’s framing as a major issue is softened — the dataset construction process is otherwise described in reasonable detail.

## Novel Insights

None beyond the paper’s own contributions. The key insight — that adaptive chunking with hierarchical context plus guided selection of inferable chunks can improve RAG‑based role‑playing on out‑of‑knowledge questions — is clearly articulated by the authors.

## Suggestions

1. Describe the MBTI/BFI evaluation pipeline in full: how are free‑form responses converted to personality types? What LLM or rubric is used? This is essential for reproducibility and for trusting the central claim.
2. Run a complete ablation study: compare (a) standard chunking + Naive RAG, (b) ACTS alone + Naive RAG, (c) ACTS + GS (without AE), (d) full AMADEUS on at least the MBTI/BFI tasks and CharacterRAG.
3. Report confidence intervals (bootstrap) or significance tests for all main metrics.
4. Specify which LLM is used as the evaluator for ACC, ACC_L, and HS. If it is GPT‑4.1 (the same model used for GS and AE), consider using a different model for evaluation or adding human evaluation of final responses.
5. Clarify the language of the persona documents — are they in Korean or English? If cross‑lingual, discuss the potential impact and why it does not differentially affect baselines.
6. State the numerical value of K used in experiments and provide a brief rationale for the “+1” in the GS fallback.
7. Add a brief failure analysis: several characters (e.g., Mikoto Misaka, Megumin) show poor performance across methods; discussing why would strengthen the empirical contribution.

## Score and Decision

The paper makes a genuine contribution: CharacterRAG is the first dataset designed for RAG‑based role‑playing, and the AMADEUS framework is well‑motivated, training‑free, and shows substantial improvements on the out‑of‑knowledge MBTI/BFI evaluations (20% and 9% absolute gains). However, the evaluation has significant gaps that weaken support for the core claims: the MBTI/BFI evaluation pipeline is underspecified, there is no ablation isolating the contribution of each component, statistical significance is unreported, and the language of the persona documents is ambiguous. These issues are addressable but in the current form make the paper borderline. I recommend a borderline score.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>