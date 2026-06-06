---

## Summary

AMADEUS is a training-free RAG framework for role-playing agents (RPAs) that addresses out-of-knowledge persona consistency through three components: Adaptive Context-aware Text Splitter (ACTS), Guided Selection (GS), and Attribute Extractor (AE). The paper also introduces CharacterRAG, a purpose-built dataset of 15 fictional characters with 976K written characters and 450 QA pairs. The central claim is that AMADEUS maintains persona consistency even when user queries fall outside the character's explicit knowledge, evaluated via MBTI/BFI personality assessments and CharacterRAG QA.

---

## Strengths

- **AMADEUS shows a large improvement on personality-type prediction.** Table 1 shows MBTI accuracy of 85.00% vs. 65.00% (Naive RAG) and BFI accuracy of 81.33% vs. 72.00% — a substantial margin, not a marginal one. The Σ|d| drops from 21 (Naive RAG) to 9 (AMADEUS) for MBTI, indicating qualitatively more correct character-level predictions.

- **ACTS chunking is properly ablated at the chunking level with three embedding models.** Table 2 demonstrates that ACTS achieves the highest Σμ and lowest Σσ² across BGE-M3, Qwen3-0.6B, and mE-large-instruct embeddings compared to RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter, SemanticChunker, and the intermediate ATS (ACTS without hierarchical context). The ATS vs. ACTS comparison directly isolates the contribution of hierarchical context.

- **Human evaluation of GS+AE is methodologically credible.** Table 3 reports Cronbach's α of 0.825 (BFI) and 0.810 (MBTI) among 14 evaluators, both above the 0.8 high-consistency threshold, with mean Likert scores near 4/5. This provides direct third-party validation of the attribute extraction quality.

- **CharacterRAG fills a genuine benchmark gap.** Table 4 shows that all three tested LLMs fail badly without RAG (ACC: GPT-4.1 49.56%, Gemma3-27B 27.56%, Qwen3-32B 18.89%), validating that the dataset tests real long-document retrieval and cannot be answered from parametric knowledge alone. No prior benchmark targeted RAG-based RPA evaluation.

- **Graph- and web-search-based RAG paradigms are shown to be inappropriate for role-playing.** LightRAG achieves only 34.67% BFI accuracy vs. 81.33% for AMADEUS, and CRAG shows sharp performance degradation under Qwen3 (ACC: 28.67%). These findings deliver actionable guidance to the community.

---

## Weaknesses

### Fatal
None.

### Major

- **GS and AE always use GPT-4.1 regardless of the generation backbone, making the multi-LLM comparison methodologically misleading.** Section 5.1 explicitly states: *"We implement Guided Selection (GS) and Attribute Extractor (AE) using GPT-4.1 ('gpt-4.1-2025-04-14')."* This means "AMADEUS (Gemma3-27B)" in Table 4 is actually GPT-4.1 for chunk selection and attribute extraction + Gemma3-27B for final generation, while "Naive RAG (Gemma3-27B)" uses Gemma3 throughout. The headline claim that AMADEUS works well "across all three LLMs" is therefore misleading: the Gemma3 and Qwen3 configurations benefit from an undisclosed GPT-4.1 component that the baselines lack. The paper should either test GS/AE with each backbone, or clearly frame AMADEUS as a pipeline where GS/AE is a fixed strong module — not as a method that generalizes across model families.

- **No end-to-end component ablation in the downstream task metrics (Table 4).** The paper validates ACTS via Table 2 (chunking similarity) and GS+AE via Table 3 (human evaluation), but never presents an experiment of the form ACTS-only vs. ACTS+GS vs. ACTS+AE vs. ACTS+GS+AE on CharacterRAG ACC/HS. Given that the CharacterRAG improvement over Naive RAG is small (e.g., ACC: 91.33% → 92.67% for GPT-4.1), it is impossible to determine how much each component contributes to the final result. The three-part contribution claim cannot be individually substantiated without this table.

### Minor

- **MBTI as a proxy metric for out-of-knowledge persona consistency has known limitations.** The paper uses crowd-sourced personality-database.com votes as ground truth for MBTI, which it acknowledges. MBTI has well-documented psychometric reliability issues (test-retest instability, binary forced categorization). While this methodology follows prior work (Wang et al., 2024b), the paper could strengthen the claim by cross-checking with the psychometrically more robust BFI results (also included in Table 1) and noting the BFI results explicitly corroborate the MBTI findings.

- **Small margins in Table 4 for in-knowledge QA are not accompanied by significance tests.** GPT-4.1 ACC improves by 1.34pp (91.33% → 92.67%), ACC_L by 0.03 points, and HS by 0.24 points over 450 total questions (30 per character). These margins could plausibly arise from variance in LLM-based scoring without reaching statistical significance. No confidence intervals or significance tests are reported.

- **Potential self-evaluation bias.** The evaluation metrics ACC, ACC_L, and HS are all LLM-based (Section 5.2). Since GPT-4.1 is used for GS and AE, if the same model is also the evaluator, AMADEUS results in the GPT-4.1 column could be inflated by self-consistency. The paper does not specify which LLM is used as the evaluator, which should be clarified.

- **GS fallback rate is not reported.** Algorithm 1 shows that if the slot S is empty after N iterations, GS reverts to returning top-K+1 chunks by similarity — degenerating to standard RAG. The frequency of this fallback across the 60 MBTI + 120 BFI questions is never disclosed, which makes it unclear how often GS actually adds value vs. degrades to a baseline.

### Trivial

- **The dataset covers only anime/manga characters from Namuwiki (Korean-language).** All 15 characters (Tanjiro, Son Goku, Saitama, Frieren, etc.) are from Japanese animation. While the paper is transparent about this, generalizability claims should be appropriately scoped.

---

## Nice-to-Haves

- An experiment testing GS and AE driven by the same backbone LLM as the generator (Gemma3 or Qwen3) would show whether the method's value persists without GPT-4.1 in the loop, substantially strengthening the multi-model claims.
- Reporting the wall-clock or token cost of AMADEUS relative to Naive RAG (GS makes up to 30 LLM calls per query; AE makes at least one) would help practitioners assess feasibility.
- A sensitivity analysis over slot size M (currently fixed at 2) and max iterations N (30) would justify these as hyperparameter choices rather than unexplored knobs.
- Extending human evaluation from GS+AE chunk/attribute pairs (Table 3) to full system responses would directly validate the out-of-knowledge persona consistency claim with more direct evidence.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"MBTI is used as the primary metric; BFI is ignored"** — The harsh critic frames this as a single-metric concern, but Table 1 includes both MBTI and BFI results. AMADEUS leads on both (81.33% BFI accuracy). This part of the critique is partially inaccurate.

- **"Overlap coefficient α=2 is not meaningfully superior per Figure 4"** — The reported values (5.920 vs. 5.916) are numerically tiny, and the harsh critic correctly identifies that this is a weak empirical support. However, the practical effect is also practically trivial — the paper's justification for this heuristic is reasonable, and the ATS vs. ACTS difference in Table 2 provides a more important validation of the design direction. This is demoted to a trivial-level observation not worth keeping as a standalone weakness.

- **"N=30 may leave large portions of Tanjiro's 145K-character persona uninspected"** — Valid as a concern, but there is no evidence that the coverage gap is causing measurable harm in the results. Without a quantitative coverage analysis showing missing relevant chunks, this is speculative.

- **Criticism of CharacterRAG as a narrow domain** — The paper is fully transparent that the dataset uses anime/manga characters sourced from Namuwiki and does not overclaim generalization. This is scope description, not a flaw.

- **Strength: "CharacterRAG addresses an important problem"** — Too generic, removed per filtering rules. Kept the specific evidence about 0-RAG baseline collapse instead.

---

## Novel Insights

The most valuable insight emerging from this work — beyond the paper's stated contributions — is the diagnostic showing that **LightRAG (graph-based) and CRAG (web-search-based) are not merely less optimal for RPA but actively harmful**, with BFI accuracy collapsing to 34.67% for LightRAG. This is a non-obvious negative result that carries strong practical guidance for the RAG-for-role-playing community and would justify the work even without AMADEUS's positive results. The finding that thinking mode (Qwen3-32B) provides no benefit for role-playing is similarly counter-intuitive and informative.

---

## Suggestions

1. **Fix the multi-LLM comparison**: Either run GS/AE with each backbone model or explicitly frame AMADEUS as a pipeline where GS/AE is a fixed strong module (GPT-4.1). Report the GPT-4.1-only configuration as the primary result.
2. **Add an end-to-end ablation table**: ACTS-only, ACTS+GS, ACTS+AE, ACTS+GS+AE on CharacterRAG ACC/ACC_L/HS using the same backbone for all components.
3. **Specify the evaluation LLM** in Section 5.2 to allow readers to assess self-evaluation bias.
4. **Report the GS fallback rate** (how often slot S remains empty) broken down by query type to clarify the operational scope of the method.
5. **Add significance tests or confidence intervals** for Table 4, especially for the small margins in the GPT-4.1 column.

---

## Evaluation by Axis

- **Originality**: Moderate. ACTS, GS, and AE are sensible engineering contributions, not conceptually novel. CharacterRAG dataset is a more original contribution for the subfield.
- **Importance of research question**: High. RAG-based role-playing under out-of-knowledge queries is a real and underexplored problem with practical applications.
- **Claims well-supported**: Partially. ACTS is well-supported (Table 2). GS+AE attribute extraction is supported (Table 3 human eval). The full-system AMADEUS vs. baselines comparison is confounded by the GPT-4.1 component injection in multi-LLM experiments, and lacks component-level ablation on downstream metrics.
- **Soundness of experiments**: Moderate. The MBTI/BFI evaluation follows prior work and the human evaluation is rigorous. The multi-LLM comparison methodology is flawed as described.
- **Clarity of writing**: Good. The method is clearly described and Algorithm 1 is precise.
- **Value to research community**: High (CharacterRAG dataset) and moderate (AMADEUS pipeline). The dataset alone is a durable contribution.

---

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>