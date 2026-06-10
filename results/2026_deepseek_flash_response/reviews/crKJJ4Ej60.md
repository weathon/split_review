Now let me write the final review.

## Summary

This paper proposes **Copy-Paste**, a generation paradigm for RAG that maximizes direct lexical copying from provided context as a path to contextual faithfulness. It is instantiated through (1) three prompting methods (CP-Order, CP-Link, CP-Refine) that generate high-copying responses via hard and soft constraints, and (2) **CopyPasteLLM**, a DPO-trained model using only 365 automatically constructed preference samples — 50× less data than Context-DPO. The paper also introduces **Context-Parameter Copying Capturing**, a token-level analysis tool that reveals CopyPasteLLM works by suppressing parametric knowledge confidence rather than enhancing contextual representations.

## Strengths

- **Novel and provocative paradigm.** The idea that verbatim copying from context should be embraced (rather than avoided) as a route to faithfulness is a genuine departure from the standard RAG approach of abstractive generation conditioned on retrieved context. This reframing is well-motivated by the practical observation that attribution is inherently satisfied when the answer is a direct quote.

- **Impressive data efficiency with strong empirical results.** CopyPasteLLM achieves 92.8% accuracy on FaithEval (Llama-3-8B) — a 12.6-point gain over Context-DPO — while using only 365 training samples versus Context-DPO's 18,000. This efficiency is obtained through a well-designed automated preference construction pipeline (multi-criteria filtering, Elo tournament, answer stamping) that generates roughly five preference pairs per sample.

- **Insightful mechanistic analysis.** The Context-Parameter Copying Capturing algorithm (Section 3.3) and the UMAP visualizations (Figure 4) reveal a non-obvious finding: CopyPasteLLM's contextual representations remain nearly co-distributed with the base model's, while its parametric knowledge representations shift substantially. This suggests the mechanism is selective suppression of parametric confidence rather than enhancement of contextual processing — a genuinely novel insight that goes beyond prior work.

- **Comprehensive evaluation across model scales.** Results span models from 7B to 671B parameters (Mistral-7B, Llama-3.1-8B, Qwen2.5-72B, DeepSeek-V3-0324), showing the prompting methods (especially CP-Refine and CP-Order) consistently outperform Attributed and Citations baselines on faithfulness and hallucination metrics across all scales.

- **Generalization to non-counterfactual settings.** The approach also improves accuracy in contexts where context aligns with parametric knowledge (Table 3, average gain from 90.26% to 95.73%), demonstrating that learned contextual trust is broadly beneficial, not just a counterfactual trick.

## Weaknesses

### Major

- **Divergence between Accuracy and Hit Rate on FaithEval raises questions about what is being measured.** On FaithEval (Table 1, Llama-3-8B), CopyPasteLLM's Accuracy jumps 12.6 points over Context-DPO (80.2→92.8) while its Hit Rate moves only 0.5 points (36.7→37.2). Since FaithEval is a counterfactual benchmark where gold answers are consistent with modified contexts, Accuracy on this benchmark may be substantially influenced by lexical overlap — which is exactly what CopyPasteLLM is trained to maximize. The paper frames its contribution as improving *contextual faithfulness*, but the evaluation may partially be measuring *willingness to copy context verbatim*, which is a weaker and more obvious claim. The paper does not explain this divergence or discuss what Accuracy specifically measures on these benchmarks (the metric is never defined in the main text). Given that the headline 92.8% vs. GPT-4o's 47.5% claim rests on this metric, the lack of clarity is a significant gap. The paper would be substantially stronger if it included a metric that controls for copying (e.g., requiring paraphrasing, combining multiple context sentences, or evaluating on answers where the correct response is *not* a direct copy).

- **Base model performance is omitted from counterfactual settings.** Table 1 (counterfactual scenarios) does not include a "Base" row for any model, making it impossible to isolate how much of the gain comes from DPO training versus how much copying tendency already exists in the base model. Table 3 provides base model numbers for non-counterfactual settings, but their absence from the counterfactual table — where the paper's most dramatic claims live — is a notable omission.

### Minor

- **The RAGTruth correlation is thin evidence for the core premise.** The paper's entire motivation for equating copying with faithfulness rests on a single correlation analysis on RAGTruth (839 questions, 6 models, Section 2.2). While the paper appropriately frames this as a "motivating observation," the leap from this correlation to the full Copy-Paste paradigm is large. The analysis does not examine counterexamples (e.g., cases where high copying coexists with unfaithfulness, such as copying a wrong sentence from a long context). The paper would benefit from a more thorough analysis of when copying is *not* the right strategy.

- **No ablation of the preference construction pipeline.** The pipeline (Section 3.2) involves six candidate types, multi-criteria filtering with four metrics, an Elo tournament, and answer stamping. It is impossible to know which components drive the results without ablations. The paper references Appendix G for ablations, but these are not visible in the main text.

- **No variance or confidence intervals reported.** All tables report point estimates without standard deviations, despite the small training set (365 samples) and the use of LLM-as-Judge evaluation for some metrics, where variance could be meaningful.

- **The 365-sample efficiency claim needs nuance.** While the training set size is genuinely small, constructing those 365 samples requires generating six candidate types per sample, running multiple automated evaluations, and an Elo tournament. The total compute cost per sample is substantially higher than simply collecting existing data. The paper should acknowledge this or provide a cost comparison.

### Trivial

- The paper refers to Appendix G (ablations), Appendix A (theoretical interpretation), and Appendix K (limitations), but these sections are not visible in the provided manuscript. The main text should briefly summarize key ablation findings.

## Nice-to-Haves

- **Comparison against a trivial "just copy" baseline.** A prompt like "Answer by copying the most relevant sentence from the context verbatim" would establish whether the complex pipeline adds value over the obvious baseline.
- **Experiments with noisy or irrelevant context.** Since CopyPasteLLM is trained to trust context, evaluating on deliberately noisy, outdated, or misleading context would reveal failure modes important for deployment.
- **Reporting both Accuracy and Hit Rate in the same table and discussing their relationship** would help readers interpret the FaithEval results.
- **Ablations showing the marginal contribution of the Elo tournament, answer stamping, and multi-criteria filtering** would strengthen the paper.

## Removed Points

- **"The evaluation metric is tautological with the training objective"** — Removed as speculative; the paper does not define Accuracy, but FaithEval is a standard benchmark whose accuracy metric measures correctness against counterfactual gold answers, not lexical overlap per se. The reviewer provides no evidence from the paper that Accuracy = lexical overlap.
- **"Comparison against baselines is systematically unfair"** — Removed; the baselines (Context-DPO, Canoe, ParamMute, CoCoLex) are the standard SOTA for contextual faithfulness. Comparing against them is appropriate. The claim that the comparison is "unfair because they don't optimize for copying" misinterprets the paper's contribution: the paper argues copying *is* the path to faithfulness, making these baselines directly relevant.
- **"Correlation is not causation" as a major weakness** — Removed as overstated; the paper frames the RAGTruth analysis as a "motivating observation" and "hypothesis," not as proof of causation.
- **Various formatting/style nitpicks and missing appendix content** — Removed per instructions (parser artifacts, not author errors).

## Novel Insights

The most interesting synthesis from the reviews is the tension between the paper's two strongest claims. On one hand, the mechanistic analysis (Figure 4) genuinely reveals something interesting — that DPO-trained high-copying preference selectively suppresses parametric knowledge representations while leaving contextual representations unchanged. This is a non-obvious finding and suggests the method is doing something more nuanced than just "train the model to copy." On the other hand, the headline empirical claim (92.8% on FaithEval) is undermined by the Acc/Hit Rate divergence, which suggests that a substantial portion of the gain may come from lexical overlap rather than genuine improved reasoning. The paper would be much stronger if the mechanistic analysis were used to *explain* this divergence — e.g., are the tokens where CopyPasteLLM succeeds but Context-DPO fails precisely those where parametric suppression is most active? This connection between the two contributions is the missing link.

## Suggestions

1. **Disentangle copying from faithfulness in the evaluation.** Evaluate on a benchmark where the correct answer requires paraphrasing (not verbatim copying) of the context, or where context contains multiple relevant sentences that must be *combined*. If CopyPasteLLM still outperforms baselines there, the claim is substantially stronger.

2. **Add base model results to Table 1** and discuss the Acc/Hit Rate divergence explicitly.

3. **Include a simple "copy-only" baseline** (e.g., a prompt instructing verbatim copying) to calibrate the value added by the DPO training and pipeline.

4. **Report variance estimates** or at minimum conduct multiple runs for the key results in Table 1.

5. **Provide the ablation results** (referenced as Appendix G) in the main text or a summarized form.

## Score and Decision

**Calibration anchors used:**
- *Round 1 (bracketing)*: Low band (<3.5): RuY1r1PDdQ.md (3.00, RAG evaluation benchmark), a2rSx6t4EV.md (2.33, education RAG benchmark), oqRe1KvD17.md (3.00, Reward-RAG), fMaEbeJGpp.md (2.50, multimodal RAG QA). Middle band (3.5-7.5): asGQQc7gNo.md (6.67, Factuality/Context-Faithfulness trade-off — ACCEPT), JnWJbrnaUE.md (3.75, Corrective RAG — REJECT), 1OyE9IK0kx.md (5.00, Faithful CoT — REJECT), hPk92D2GJV.md (5.25, BALCONI context/internal knowledge — REJECT). High band (>7.5): Bo62NeU6VF.md (8.00, Backtracking safety), Iyrtb9EJBp.md (8.00, RAG Trustworthiness — ACCEPT), SPS6HzVzyt.md (8.00, Context-Parametric Inversion — ACCEPT), EytBpUGB1Z.md (8.00, Retrieval Head — ACCEPT).

- *Round 2 (narrowing)*: WPZ2yPag4K.md (5.75, Fine-Tuning for Factuality — ACCEPT), d2H1oTNITn.md (6.40, Mask-DPO — ACCEPT), 9Hxdixed7p.md (6.25, 3D-Properties of DPO — ACCEPT), Igm9bbkzHC.md (6.75, Controllable Context Sensitivity — ACCEPT), Tigr1kMDZy.md (7.33, Overthinking the Truth — ACCEPT), KRnsX5Em3W.md (6.50, LLMs Know More Than They Show — ACCEPT).

**Round 1 bracket:** 5.0 – 7.0.

**Narrowing to final score:** The paper is substantially stronger than the rejected middle-band anchors (BALCONI at 5.25, Corrective RAG at 3.75). It is comparable to Mask-DPO (6.40) in terms of novelty and rigor, though weaker than Controllable Context Sensitivity (6.75). The Acc/Hit Rate divergence is a genuine concern that prevents the paper from reaching the top band (7.5+), where papers like Context-Parametric Inversion (8.0) have cleaner evaluations and stronger mechanistic analysis. The paper is stronger than Fine-Tuning for Factuality (5.75) due to greater novelty and more comprehensive evaluation. Final score: **6.0**.

**Overall:** The paper makes a genuine contribution by proposing and validating a novel paradigm for RAG faithfulness. The mechanistic analysis is insightful and the data efficiency is impressive. However, the core empirical claim is partly undermined by a lack of clarity about what the evaluation metric measures, and the paper would benefit from addressing the Acc/Hit Rate divergence and adding base model comparisons. These concerns are addressable and do not invalidate the paper's contributions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>