Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes AMADEUS, a training-free RAG framework for role-playing agents, consisting of three components: Adaptive Context-aware Text Splitter (ACTS), Guided Selection (GS), and Attribute Extractor (AE). It also introduces CharacterRAG, a manually constructed dataset of 15 fictional characters (976K characters, 450 QA pairs). The method is evaluated on in-knowledge QA (CharacterRAG) and out-of-knowledge personality inference (MBTI/BFI), reporting 85% MBTI accuracy and 81.33% BFI accuracy across 15 characters, substantially outperforming Naive RAG, CRAG, and LightRAG.

## Strengths

- **Manually constructed CharacterRAG dataset is a genuine contribution.** The paper introduces the first dataset designed specifically for building and evaluating RAG-based role-playing agents, with 15 characters, 976K persona characters, and 450 QA pairs. The dataset is constructed by human annotators who removed editor-biased information, making it suitable for RAG evaluation. This fills a clear gap — existing role-playing datasets are dialogue-based, not designed for RAG.

- **Strong and consistent results on out-of-knowledge personality inference.** Table 1 reports 85.00% MBTI accuracy and 81.33% BFI accuracy for AMADEUS vs. 65.00%/72.00% for Naive RAG on GPT-4.1, with similarly large margins across Gemma3-27B and Qwen3-32B. The improvements are large (15-20 percentage points on MBTI) and consistent across all three LLMs tested.

- **Human evaluation confirms reliability of attribute extraction.** Table 3 reports mean human ratings of 3.97 (BFI) and 3.90 (MBTI) on a 5-point Likert scale with Cronbach's alpha > 0.8, indicating that the attributes extracted by GS+AE are judged consistent by human evaluators.

- **Good empirical breadth.** The paper evaluates across 3 LLMs (GPT-4.1, Gemma3-27B, Qwen3-32B), 3 embedding models (BGE-M3, Qwen3-0.6B, mE5-large-instruct), and two evaluation paradigms (in-knowledge CharacterRAG QA and out-of-knowledge MBTI/BFI), demonstrating robustness.

## Weaknesses

### Major

- **No component-level ablation on end-task performance.** The paper claims a novel three-stage framework (ACTS, GS, AE) but cannot attribute any of the reported gains to specific components. Table 2 evaluates ACTS vs. other splitters on *similarity scores* — a proxy metric that does not measure role-playing quality. Table 3 evaluates GS+AE on attribute extraction reasonableness — again not the final response. There is no experiment where, e.g., ACTS is replaced with a fixed splitter while keeping GS/AE and measuring final MBTI accuracy, or where GS is removed and only ACTS+AE are used. Without such ablations, the reader cannot tell whether the reported improvements come from the extra LLM reasoning steps in GS and AE (which any method could add), from ACTS alone, or from the specific combination. This is a significant gap for a paper whose central contribution is a three-component framework.

- **Guided Selection (GS) prompt is not provided and the LLM call is underspecified.** Algorithm 1 relies on an LLM to determine whether a chunk "contains information from which the character's attributes can be inferred regarding u." This is a critical step — it determines which chunks are selected and thus what the AE receives — but no prompt template, threshold, or operationalization of "can be inferred" is given. Without this, the method cannot be fully reproduced.

### Minor

- **Chunk-length heuristic in ACTS is document-dependent and under-justified.** ACTS sets the chunk length to the maximum paragraph length in the persona document (l_max) and overlap to l_max/2. This depends entirely on how the source document was formatted, and the paper only studies the overlap coefficient α (Figure 4), not chunk length itself. The claim that this is "adaptive" is weakened by the fact that it simply mirrors the paragraph structure of the source document, which may vary arbitrarily across writing styles.

- **MBTI/BFI evaluation uses crowd-sourced ground truth without reliability analysis.** The ground-truth personality types for characters are taken from personality-database.com. While the paper notes "thousands of actual participants' votes," no inter-annotator agreement or analysis of voter bias is reported. The scoring procedure for deriving MBTI/BFI types from model responses is cited to prior work but not detailed, making it hard to assess whether small differences in answer patterns could flip the predicted type.

- **No variance or statistical significance reported for main results.** None of the main tables (1, 2, 4) report confidence intervals, standard deviations, or significance tests. With only 15 characters and (in some settings) small absolute differences, some reported improvements could be driven by a few outliers.

- **LightRAG performing below "w/o RAG" on GPT-4.1 (48% vs. 49.56%) warrants explanation.** The paper ascribes this to graph-based RAG being unsuitable, but such a large degradation relative to not using RAG at all is striking and could indicate configuration issues or a mismatch between LightRAG's graph construction and the persona documents.

### Trivial

- The paper states "thinking mode fails to yield any substantial positive effect" for Qwen3-32B, but provides no direct comparison of Qwen3-32B with and without thinking mode on the same task. This claim is unsupported by the presented data.

## Nice-to-Haves

- The paper does not analyze sensitivity to hyperparameters N=30 search iterations and M=2 slot size. A brief sensitivity study would strengthen the empirical grounding.
- The computational cost of GS (up to 30 LLM calls per query) is not discussed. This is a practical limitation worth acknowledging.
- Only two attributes (Belief & Value, Psychological Traits) are extracted in AE. While the paper states these "directly influence behavior," an ablation or justification for excluding the other four attributes would be helpful.

## Removed Points

The following points from the harsh critic were removed or downgraded:

- *"Comparison with LightRAG and CRAG is expected to be weak… A more informative baseline would be an improved RAG pipeline"* — This asks the paper to address questions outside its stated scope (comparing against off-the-shelf RAG variants is a reasonable design choice). Demoted to nice-to-have.

- *"Table 5 is referenced but does not appear"* — The appendix is stripped by the parser; Table 5 exists in the original submission. Removed.

- *"The paper does not discuss inference-time role-playing methods (e.g., persona-driven fine-tuning)"* — The paper is focused on RAG, which is a stated scope decision. Removed.

- *"How chunk usage rate is computed should be clarified"* — Minor clarification request; not a weakness per se.

- *"The hierarchical context construction is not described"* — The paper does provide examples ("Tanjiro Kamado's actions in the story (#4)" etc.). The description is sufficient for markdown-structured documents. Removed.

- *"The chunk-length heuristic may not generalize"* — Kept as minor, but the reviewer's framing as a "methodological gap" was overstated; the heuristic is simple but plausible.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add component-level ablation on the end-task.** Replace ACTS with a fixed splitter (recursive with matched average chunk size), test without GS (skip selection, use top-K chunks directly), and test without AE (only use knowledge chunks for response). Report MBTI accuracy and CharacterRAG ACC for each variant. This single experiment would substantially strengthen the paper.

2. **Provide the GS prompt template in full.** Show at least one example of a chunk that passes/fails the "can infer attributes" check. This is necessary for reproducibility.

3. **Report bootstrapped confidence intervals** for the main accuracy results (Table 1, Table 4). With 15 characters, 95% CIs would help the reader gauge reliability.

4. **Acknowledge the computational cost of GS** (up to 30 LLM calls per query × 2 slots) and discuss trade-offs.

## Score and Decision

**Calibration report:**

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| wKTwm7ZzDK | 2.40 | R1-low | Adaptive Friend Agent: far weaker, rejected for poor evaluation |
| VVJeDnuo4c | 3.33 | R1-low | MAPS for RAG: withdrawn, less relevant |
| TjTuObGe27 | 3.33 | R1-low | FURINA role-playing benchmark: weaker, withdrawn/rejected |
| 1OLTJL1wHG | 3.00 | R1-low | ConfRAG: weaker, withdrawn |
| lVE8H8QNcx | 6.50 | R1-mid | PDD role-playing: stronger theory & ablation; AMADEUS weaker but has dataset contribution |
| sWQSbVsPEz | 5.50 | R1-mid | R4 role-playing+RAG: comparable quality, similar methodological gaps |
| mZT0dxJvc0 | 4.00 | R1-mid | PersonaFeedback: weaker, benchmark-only work |
| LO2c9ZznJl | 4.00 | R1-mid | SCorPion GraphRAG: weaker, withdrawn |
| lW7kMpMj9K | 5.50 | R2-narrow | VeriRole role-awareness: comparable quality |
| Myti1QwL2t | 5.50 | R2-narrow | SmartChunk adaptive chunking: comparable, also has ablation gaps |
| NLFxQedK9y | 5.33 | R2-narrow | ChronoPlay game RAG: comparable quality |
| RV2aeCgxdB | 6.00 | R2-narrow | ProPerSim proactive assistants: somewhat stronger evaluation |
| JXFnCpXcnY | 6.50 | R2-narrow | Psychological profiling with LLMs: different focus, stronger analysis |

**Round 1 bracket**: The paper sits between weak anchors (~3) and strong anchors (~8), most comparable to middle-band papers (4-7). 

**Round 2 narrowing**: Compared against PDD (6.50), R4 (5.50), SmartChunk (5.50), VeriRole (5.50), ChronoPlay (5.33). The paper is most comparable to R4 and SmartChunk (both 5.50, Accept Poster). It is slightly weaker than PDD (6.50) which has stronger ablation and theoretical grounding but lacks the dataset contribution. The missing component-level ablation on the end-task is the primary factor preventing a higher score.

**Final score**: The paper has real contributions (dataset + clean framework) and strong empirical results, but the lack of component-level ablation on the final metrics and underspecified GS implementation are significant gaps that weaken the evidence for the core methodological claims. Placing it at the level of comparable papers like R4 and SmartChunk.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>