Now I have thoroughly verified the paper content against all reviewer claims. Let me produce the final consolidated review.

## Summary

The paper introduces AMADEUS, a training-free RAG-based framework for role-playing agents that aims to maintain persona consistency even on out-of-knowledge questions. The framework has three components: Adaptive Context-aware Text Splitter (ACTS) for hierarchical chunking, Guided Selection (GS) for LLM-based chunk filtering, and Attribute Extractor (AE) for extracting personality attributes from selected chunks. The authors also introduce CharacterRAG, a manually constructed dataset of 15 fictional characters (976K characters, 450 QA pairs). Experiments evaluate on both in-knowledge (CharacterRAG) and out-of-knowledge (MBTI/BFI personality estimation) settings across three LLMs and three embedding models.

## Strengths

1. **Clear improvements on the out-of-knowledge task, which is the paper's main claimed contribution.** On MBTI personality estimation, AMADEUS achieves 85.00% accuracy and 0.8394 Avg F1 vs. Naive RAG (65.00%, 0.6146) and CRAG (68.33%, 0.6448). On BFI, it achieves 81.33% vs. Naive RAG's 72.00% and CRAG's 76.00%. These are substantial gaps (17–20 percentage points on MBTI) that convincingly show the framework maintains better consistency on questions beyond explicit character knowledge.

2. **CharacterRAG fills a genuine gap as a dataset designed specifically for RAG-based role-playing.** The paper correctly identifies that existing role-playing datasets are designed for dialogue generation or fine-tuning, not for the RAG setting. The manual construction (removing external information, rewriting from character perspective) is well-motivated and the dataset enables reproducible benchmarking.

3. **Multi-model, multi-embedding evaluation across several LLMs and retrievers.** Experiments span GPT-4.1, Gemma3-27B, Qwen3-32B (with thinking mode), plus BGE-M3, Qwen3-0.6B, and mE5-large-instruct embeddings. The consistent improvement across this range suggests the benefit is not tied to a single model configuration.

4. **Human evaluation of GS and AE intermediate outputs shows reasonable reliability.** Cronbach's alpha of 0.825 (BFI) and 0.810 (MBTI) on the intermediate attribute extraction task exceeds standard thresholds, lending credibility to the pipeline's intermediate stages.

## Weaknesses

### Major

1. **No component-level ablation on final response quality.** The paper compares full AMADEUS against Naive RAG, CRAG, and LightRAG, but never isolates the effect of ACTS, GS, or AE individually on the end-task metrics. Table 2 evaluates ACTS only on similarity scores (not role-playing metrics). Table 3 evaluates GS+AE on intermediate outputs. Consequently, the reader cannot attribute the overall improvement to any particular component. This is the most significant evaluation gap — the paper claims a three-component contribution but provides no evidence that each component is necessary.

2. **Missing comparison against the simplest training-free baseline: feeding the full persona as context to a long-context LLM.** Since AMADEUS is described as "training-free," the natural baseline is to give the entire persona document to a long-context model and let it respond directly. This baseline would directly test whether the RAG pipeline (chunking, retrieval, selection, extraction) is net beneficial over simply using the raw persona. Its absence weakens the claimed advantage of the RAG-based approach.

### Minor

3. **Improvements on the in-knowledge CharacterRAG task are small and unreported for significance.** On GPT-4.1: 92.67% vs. 91.33% (1.34 pp); on Gemma3-27B: 88.00% vs. 86.44% (1.56 pp); on Qwen3-32B: 78.89% vs. 78.44% (0.45 pp). No confidence intervals, variance, or significance tests are reported. While the out-of-knowledge results show large gains, the in-knowledge gains are modest enough that the lack of significance reporting is a concern.

4. **Dataset is limited to 15 characters from a single cultural source (Korean Namuwiki).** The paper acknowledges the source but does not discuss the generalizability of findings to characters from other cultural or media contexts. Since the persona structure and the challenges of role-playing may differ across cultures and narrative traditions, this scope limitation should be explicitly addressed.

5. **The GS decision criterion (Algorithm 1, line 8–9: "With an LLM, determine if chunk c contains information from which the character's attributes can be inferred") is underspecified.** The prompt used for this LLM call is not provided (the appendix is stripped from the submission, per the parsing note). Reproducing the exact behavior depends on unspecified prompting.

6. **Figure 5 shows AMADEUS has a worse Hallucination Score than CRAG on Qwen3-32B for MBTI (2.04 vs. 1.80) and BFI (2.03 vs. 1.96).** This result is not discussed in the paper, even though it contradicts the general trend and involves the model that should benefit most from the "reasoning" aspects of the framework.

### Trivial

7. Figure 1's description of 15 plots for 15 MBTI types includes some repeated type names (ISTP appears multiple times), which appears to be a typo in the figure caption (parser artifact).

## Nice-to-Haves

- Run a proper ablation: remove each component individually and measure the impact on CharacterRAG ACC and MBTI accuracy. This would substantially strengthen the contribution attribution.
- Add a long-context LLM baseline for a direct "RAG vs. no RAG" comparison.
- Report confidence intervals or bootstrapped significance for the main results.
- Report the computational cost of GS (up to 30 LLM calls per query) to contextualize the practical trade-off.
- Expand the dataset beyond a single cultural source to improve generalizability claims.

## Removed Points

- **Criticism about fan-site ground truth being a "structural flaw" that invalidates the evaluation.** The paper explicitly follows the evaluation paradigm established in prior work (Wang et al., 2024b; Park et al., 2025) and cites it. Using crowd-sourced personality labels as ground truth is the accepted methodology in this sub-area for out-of-knowledge evaluations. The relative comparison (AMADEUS vs. baselines evaluated on the same labels) remains valid. This is a known limitation of the paradigm, not a fatal flaw specific to this paper.
- **Criticism that "hallucination" is undefined.** The paper defines HS (Hallucination Score) operationally in Section 5.1: a 10-point scale measuring whether the response faithfully reflects only facts contained in chunks or the answer.
- **Claim that ACTS is "not a novel algorithmic contribution."** The novelty standard varies by venue; the paper positions ACTS as a practical engineering contribution adapted for role-playing, which is reasonable.
- **Claim that Table 1's accuracy metric is unclear.** The number in parentheses counts incorrect predictions across the 4 MBTI questions per character; Accuracy = (total − Σ|d|)/total. This is clear from the caption.
- **Claim that 14 human evaluators is insufficient.** With 60 samples × 14 evaluators = 840 evaluations and Cronbach's alpha > 0.8, the sample size is statistically adequate for demonstrating inter-rater reliability.
- **Several generic formatting/style nitpicks** from the harsh critic.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Run a component ablation study (remove ACTS, GS, AE individually) and measure impact on both CharacterRAG ACC and MBTI/BFI accuracy — this is the single most impactful addition.
2. Include a baseline that uses the full persona document as the context for a long-context LLM, to directly test whether the RAG pipeline adds value over raw context.
3. Add confidence intervals or bootstrap-based significance tests to the main result tables.
4. Include the GS decision prompt in the main text or a guaranteed appendix section to improve reproducibility.
5. Explicitly discuss the cultural scope limitation of the dataset and, if possible, add a few characters from non-Korean sources.
6. Discuss the Qwen3-32B HS anomaly (Figure 5) where CRAG outperforms AMADEUS on the out-of-knowledge HS metric.

## Score and Decision

**Round-1 bracket (initial):** After the bracketing pass (weak anchors avg < 3.5, middle 3.5–7.5, strong > 7.5), the paper clearly falls in the middle band. It is substantially stronger than simple RAG benchmarks (avg ~2.5–3.0) but not at the level of polished technical contributions scoring > 7.5.

**Round-2 narrowing (inside 4–6.5):**
- *MMRole* (6.50, Accept): Much larger dataset (85 characters, multimodal), trained a specialized agent. The current paper is notably weaker — smaller scope, no trained model, weaker evaluation framework.
- *Human Simulacra* (5.60, Accept): Comparable scope (personification benchmark, psychology-guided evaluation). The current paper has a similar level of contribution but the evaluation is less rigorous (no ablation, fewer characters). Slightly weaker overall.
- *Tell Me What You Don't Know* (5.20, Reject): Comparable scope (RPA evaluation with benchmark). That paper had deeper analysis (representation analysis) but similar evaluation gaps. The current paper is roughly comparable but has a stronger practical contribution (dataset + framework vs. analysis only).
- *BIG5-CHAT* (5.25, Reject): Personality-focused with training methods and large dataset. Similar in that both used BFI/MBTI evaluation. That paper was criticized for limited novelty and evaluation gaps — similar concerns apply here.

**Final calibration:** The paper sits between 5.0 and 5.5. It has a genuine contribution (CharacterRAG dataset, clear out-of-knowledge improvements) but the evaluation is too gapped (no ablation, missing baseline, small single-source dataset, marginal in-knowledge gains) to fully support the claimed contributions. I place it slightly below Human Simulacra (5.60) due to weaker evaluation rigor, and comparable to Tell Me What You Don't Know (5.20) and BIG5-CHAT (5.25).

**Anchors retrieved across all rounds:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| acDwoHrwZ8 | 3.00 | 1 | Weak — simple multi-agent paper, much less polished |
| a2rSx6t4EV | 2.33 | 1 | Weak — education RAG benchmark, much simpler |
| fMaEbeJGpp | 2.50 | 1 | Weak — multimodal RAG system, preliminary |
| oqRe1KvD17 | 3.00 | 1 | Weak — reward-driven RAG, similar evaluation gaps |
| TqwTzLjzGS | 5.25 | 1,2 | Comparable — BIG5 personality dataset, rejected for evaluation gaps |
| FGSgsefE0Y | 6.50 | 2 | Stronger — MMRole, much larger dataset, trained model, accepted |
| AN3VTbqM1N | 4.00 | 2 | Comparable — implicit character portrayal, smaller scope |
| oXYZJXDdo7 | 7.00 | 2 | Stronger — retrieval as generation, polished experiments |
| WbWtOYIzIK | 8.00 | 3 | Much stronger — knowledge cards, rigorous evaluation |
| Iyrtb9EJBp | 8.00 | 3 | Much stronger — RAG trustworthiness, thorough |
| 07yvxWDSla | 8.00 | 3 | Much stronger — synthetic pretraining, polished |
| 7gUrYE50Rb | 8.00 | 3 | Much stronger — embodied QA, comprehensive |
| 87DtYFaH2d | 5.20 | 2 | Comparable — RPA refusal, deeper analysis but similar gaps |
| BCP5nAHXqs | 5.60 | 2 | Slightly stronger — Human Simulacra, more rigorous evaluation |
| rKMQhP6iAv | 4.25 | 2 | Weaker — personas as truthfulness modeling, more theoretical |
| KZaEdLM4Gn | 4.67 | 2 | Weaker — multi-persona collaboration, smaller contribution |
| cxt2Auexc3 | 5.75 | 2 | Comparable — personality editing, similar evaluation concerns |
| 6e3hoDZKuO | 3.50 | 2 | Weaker — goal dialogue RL, different domain |
| WEQS3oUPs3 | 5.33 | 2 | Comparable — goal dialogue, different domain |
| JnWJbrnaUE | 3.75 | 2 | Weaker — CRAG, simpler evaluation |
| R2OzZWOkjz | 3.80 | 2 | Weaker — RAEG, simpler contribution |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>