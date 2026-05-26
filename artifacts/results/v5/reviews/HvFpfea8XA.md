Now I have all the information needed to compile the authoritative final review.

## Summary

This paper introduces AMADEUS, a training-free RAG framework for role-playing agents that addresses persona inconsistency when queries fall outside a character's explicit knowledge. The framework comprises three components: Adaptive Context-aware Text Splitter (ACTS), Guided Selection (GS), and Attribute Extractor (AE). The authors also contribute CharacterRAG, a manually constructed dataset of persona documents for 15 fictional characters (976K characters) with 450 QA pairs, designed specifically for RAG-based role-playing evaluation. Experiments show substantial improvements on MBTI/BFI personality type prediction for out-of-knowledge questions (85.00% vs. 68.33% for the best baseline) and marginal gains on knowledge-based QA.

## Strengths

1. **Clear and substantial improvements on out-of-knowledge personality inference (Table 1).** AMADEUS achieves 85.00% MBTI accuracy and 81.33% BFI accuracy compared to the best baseline (CRAG) at 68.33% and 76.00%, respectively. The sum-of-deviations metric drops from 21/19 to 9 (MBTI) and from 21/18 to 14 (BFI). This directly supports the paper's central claim that the framework maintains persona consistency for questions beyond a character's explicit knowledge.

2. **ACTS chunking produces better retrieval quality across multiple embedding models (Table 2).** ACTS achieves the highest sum of mean similarity scores and lowest variance across BGE-M3, Qwen3-0.6B, and mE5-large-instruct when compared to RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter, and SemanticChunker. This provides quantitative evidence that the adaptive chunking with hierarchical context preservation is effective.

3. **Human evaluation confirms GS+AE outputs are reasonable (Table 3).** Fourteen human raters on a 5-point Likert scale give mean ratings of 3.970 (BFI) and 3.902 (MBTI), with Cronbach's alpha values of 0.825 and 0.810 indicating high inter-rater reliability. This validates that the intermediate attribute extraction step produces trustworthy output.

4. **CharacterRAG dataset fills a gap in RAG-based role-playing evaluation.** The dataset provides persona documents written from each character's perspective with external editorial content removed, and 450 manually constructed QA pairs covering six attribute categories. It is the first dataset designed specifically for building and evaluating RAG-based RPAs.

5. **Comprehensive evaluation coverage.** Experiments span three LLMs (GPT-4.1, Gemma3-27B, Qwen3-32B), three embedding models, and three off-the-shelf RAG baselines (Naive RAG, CRAG, LightRAG) in both knowledge-based and interview-style settings, demonstrating generalizability of the framework.

## Weaknesses

### Fatal

None.

### Major

1. **Unvalidated crowdsourced ground truth for the MBTI/BFI evaluation.** The ground-truth personality labels are taken from personality-database.com, a crowdsourced website where users vote on fictional characters' types. The paper provides no information about the number of votes per character, the variance of those votes, or any independent validation of the labels. The paper's strongest evidence for its central claim (Table 1) rests on this evaluation, and noisy or contested labels would make the absolute accuracy figures uninterpretable. The paper does not acknowledge this limitation or discuss its potential impact.

2. **No ablation of the GS and AE components.** The paper evaluates the full AMADEUS framework against baselines (Tables 1, 4) and separately validates ACTS chunking quality (Table 2), but never ablates GS and AE. Without configurations such as "Naive RAG + ACTS" or "AMADEUS - AE," it is impossible to attribute the reported gains to the novel components rather than to ACTS alone. This gap is especially consequential because the improvements on knowledge-based QA (Table 4) are small (e.g., 92.67% vs. 91.33% ACC for GPT-4.1), raising the possibility that better chunking accounts for most of the benefit.

3. **No human evaluation of final response quality for out-of-knowledge questions.** The human evaluation (Table 3) assesses only whether the intermediate attributes extracted by GS+AE are reasonable. The paper does not evaluate whether the *final generated responses* to out-of-knowledge questions are actually in-character. The central claim therefore lacks direct human judgment of the system's output quality.

### Minor

4. **Small dataset scope.** CharacterRAG contains only 15 characters and 450 QA pairs, all sourced from a single Korean wiki (Namuwiki). No inter-annotator agreement metrics are reported for the dataset construction process, and the cultural/linguistic specificity is not discussed as a limitation.

5. **Marginal improvements on knowledge-based QA.** On the CharacterRAG QA task (Table 4), AMADEUS achieves only small gains over Naive RAG (1.34 pp ACC for GPT-4.1; 0.45 pp for Qwen3-32B). The paper does not analyze why the improvement is limited or whether the additional complexity of GS and AE is justified for this setting.

6. **CRAG sometimes achieves lower hallucination scores.** In Figure 5, CRAG has lower HS than AMADEUS for Qwen3-32B on both MBTI (1.80 vs. 2.04) and BFI (1.96 vs. 2.03). The paper's explanation (that CRAG may produce "less accurate but more cautious responses") is speculative and not tested.

7. **No discussion of limitations or failure cases.** The paper does not discuss when AMADEUS might fail (e.g., short persona documents, characters without stable personality traits, cases where LLM-based attribute extraction hallucinates). Including such analysis would strengthen the paper.

8. **Exact prompts and judge model for LLM-based metrics not specified.** The paper states that ACC, ACC_L, and HS are "LLM-based metrics" but does not provide the evaluation prompts or identify the judge model, making the evaluation hard to reproduce exactly.

### Trivial

9. **Figure 1 caption lists repeated MBTI type labels (ISTP appears 5 times, ISTJ 3 times, etc.).** While this is because multiple characters share the same type, the caption could state this more clearly to avoid confusion.

## Nice-to-Haves

- Conduct an ablation study comparing Naive RAG + ACTS, Naive RAG + ACTS + GS, and full AMADEUS to isolate the contribution of each component.
- Validate the ground-truth personality labels through expert annotation, or replace the evaluation with human assessment of response-level persona consistency.
- Include a direct human evaluation of the final generated responses for out-of-knowledge questions (not just the intermediate attribute extraction).
- Add error analysis for cases where AMADEUS predicts the wrong MBTI/BFI type (e.g., Mikoto Misaka, Megumin in Table 1).
- Include a comparison with a fine-tuned role-playing model (e.g., Character-GLM or LoRA fine-tuned on role-play data) to contextualize the RAG-based approach.

## Removed Points

- "Weak baselines that stack the comparison" — The baselines (Naive RAG, CRAG, LightRAG) are standard RAG methods appropriate for comparison. All baselines use the same backbone LLMs, and the "w/o RAG" condition confirms that the LLMs cannot role-play effectively without external knowledge. The critic's claim that no baseline uses a role-playing prompt is incorrect; the comparison isolates the effect of RAG methodology fairly.
- "Figure 1 caption is garbled / contains labeling errors" — The repeated MBTI type labels (ISTP appearing 5 times, etc.) reflect the fact that multiple characters share the same MBTI type. This is not an error; the caption could be clearer but is substantively correct.
- "The central claim lacks direct evidence" — Table 1 provides direct quantitative evidence for the claim, using the same methodology as prior work (Wang et al., 2024b; Park et al., 2025). The concern about ground-truth validity is a separate issue about measurement quality, not absence of evidence.
- "Missing related works" — This cannot be verified without external knowledge; per the review guidelines, this criticism is removed.
- "Reproducibility: undisclosed hyperparameters" — The paper reports the key hyperparameters (N=30, M=2, models used) in Section 5.1. Additional details (e.g., exact prompts for LLM-as-judge) are a minor completeness concern, not a reproducibility gap.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting observation about the RAG-role-playing intersection: **graph-based and web-search RAG methods are systematically ill-suited for persona consistency.** LightRAG suffers from entity ambiguity and uninformative responses, while CRAG's reliance on web search introduces noise that undermines character fidelity. This negative result is a useful finding that the broader RAG community should consider when designing retrieval strategies for open-ended character simulation. The paper also provides evidence that **adaptive chunking with hierarchical context preservation** (ACTS) is the component that most clearly improves retrieval quality, while the value of the downstream GS and AE modules remains unquantified — a gap that the reviews consistently flagged.

## Suggestions

1. Add an ablation study (ACTS-only → ACTS+GS → full AMADEUS) on the MBTI/BFI and CharacterRAG QA tasks to quantify each component's contribution.
2. Validate the personality-database.com ground-truth labels through expert annotation or, alternatively, conduct a human evaluation where raters directly assess whether the generated responses are in-character for out-of-knowledge questions.
3. Include a "Limitations" section discussing when the method may fail (short personas, characters with ambiguous or unstable traits, cases where the LLM-based attribute extractor hallucinates).
4. Provide the judge model identity and evaluation prompts for the LLM-based metrics to improve reproducibility.
5. Add inter-annotator agreement (e.g., Fleiss' kappa) for the dataset construction to support the claim of "high-quality" annotation.

## Score and Decision

**Round 1 bracket**: Based on calibration search, this paper sits between the low band (<3.5) and mid band (3.5-7.5). Low-band anchors (Reward-RAG 3.00, Multimodal RAG 2.50, TrojanRAG 3.40) had fundamental methodological flaws that this paper avoids. Mid-band anchors (RPA Refusal 5.20, BIG5-CHAT 5.25, Human Simulacra 5.60, Bias Runs Deep 5.75, MMRole 6.50) had clearer evaluation frameworks or larger-scale contributions.

**Round 2 narrowing**: Within (3.5-7.5), the paper most closely resembles the RPA Refusal paper (5.20, rejected) in structure and the BIG5-CHAT paper (5.25, rejected) in evaluation approach (personality typing via questionnaires). The RPA Refusal paper had mixed reviews (6,6,6,3,5) with the lower reviews citing methodological concerns. Our paper shares similar structural quality but has more severe evaluation weaknesses: unvalidated crowdsourced ground truth and no ablation.

The low-band anchors and weakness-anchored hits failed at having sound evaluation frameworks or complete experimental designs. The paper under review shares those failures partially — the ground-truth validity concern is real, and the missing ablation weakens attribution — but the paper's core contributions (dataset, framework, large improvements on out-of-knowledge tasks) are genuine and exceed what the low-band anchors offered.

**Final score**: 4.5 — a paper with a clear contribution and well-motivated approach, but whose main evaluation rests on an unvalidated ground-truth source and whose component-level analysis is incomplete. These weaknesses prevent acceptance at a top venue but leave the paper as a potentially useful building block for RAG-based role-playing research.

**Decision**: Reject

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>