Now let me finalize the review.

## Summary

This paper proposes Copy-Paste, a generation paradigm that directly embeds contextual fragments into LLM responses to mitigate faithfulness hallucinations in RAG systems. The authors observe an inverse correlation between copying degree and hallucination density on RAGTruth, then instantiate this through a two-stage pipeline: (1) Copy-Paste-Prompting methods (CP-Order, CP-Link, CP-Refine) that generate high-copying responses, and (2) CopyPasteLLM, trained via DPO on preference data constructed from these high-copying responses. On FaithEval, ConFiQA, and PubMedQA, CopyPasteLLM shows strong performance using only 365 training samples. A Context-Parameter Copying Capturing analysis reveals that the method's effectiveness stems from recalibrating parametric knowledge confidence rather than enhancing contextual representations.

## Strengths

- **Inverse correlation is empirically validated across six models (Fig 1, lower panel):** On RAGTruth, the paper shows that higher copy coverage (κ) and density (δ) correspond to lower hallucination density across multiple model families (Mistral, Llama-2, GPT-3.5, GPT-4), establishing the foundational motivating observation for the entire approach.

- **Data efficiency with strong cross-distribution results:** On ConFiQA — where CopyPasteLLM was *not* trained on any ConFiQA data — it achieves competitive or superior performance against baselines like Context-DPO that were trained on ConFiQA data (Table 1). For instance, on Mistral-7B-v0.2 ConFiQA-MR (most challenging subset), CopyPasteLLM achieves 80.8% acc vs Context-DPO's 81.3% (trained on ConFiQA), and outperforms Context-DPO on ConFiQA-MC (82.5% vs 80.4%). This cross-distribution generalization is compelling evidence that the method works beyond within-distribution fine-tuning.

- **Mechanistic analysis provides novel insight via Context-Parameter Copying Capturing:** The UMAP visualization (Fig 4) reveals that CopyPasteLLM's contextual knowledge representations remain nearly co-distributed with the base model (column 3), while its parametric knowledge distributions shift substantially (column 4). This supports the claim that effectiveness stems from recalibrating parametric confidence rather than enhancing context processing — a non-obvious finding.

- **Comprehensive evaluation design across multiple dimensions:** Experiments cover both counterfactual and non-counterfactual settings, four model families (Mistral, Llama-3, Llama-3.1, with additional Qwen and DeepSeek in Stage 1), multiple datasets (FaithEval, ConFiQA with three subsets, PubMedQA, RAGTruth), and three prompting variants. The non-counterfactual results (Table 3) show CopyPasteLLM does not sacrifice normal performance for counterfactual robustness.

## Weaknesses

### Fatal
None.

### Major

1. **FaithEval evaluation confounded by within-distribution fine-tuning.** Table 1 reports that 241 FaithEval samples were used for training CopyPasteLLM ("We removed 241 samples used for training CopyPasteLLM from FaithEval, with the remaining samples used for testing"), while none of the baselines (Context-DPO, Canoe, ParamMute, Attributed, CoCoLex) are trained on any FaithEval data. This means the headline FaithEval results (12.2–24.5% improvement) partly reflect the advantage of being fine-tuned on the same distribution as the test set. The paper is transparent about this but does not address it experimentally. The ConFiQA results (where CopyPasteLLM was *not* trained on ConFiQA) provide cleaner evidence of generalization, but the paper leads with the FaithEval numbers as its primary claim. The authors should either (a) fine-tune baselines on the same FaithEval subset, or (b) at minimum, clearly separate cross-distribution claims from within-distribution ones and weight the former more heavily.

2. **No control isolating the copy-paste preference from standard fine-tuning.** The paper never shows that the *copy-paste preference construction* drives improvement, rather than simply having 365 well-chosen training samples with gold answers. A proper control — training standard DPO on the same 365 pairs using gold answers as chosen responses (without copy-paste preferences) and comparing to CopyPasteLLM — would attribute the gain to high-copying preferences vs. data quality or quantity. This is essential to validate the paper's core causal claim that "high copying degree" is the mechanism producing gains.

### Minor

3. **Hallucination metrics (Twist, Causal) in Table 2 are not interpretable from the main text.** The paper mentions "two major hallucination modes—Twist and Causal" (Section 3.2) as part of the Elo tournament design, but the numerical scores in Table 2 (e.g., 1506.9, 1494.5) are never explained — readers cannot tell whether higher or lower is better, what the scale is, or how to interpret these values. This requires deferring to the appendix, which is not available in the main text.

4. **Non-counterfactual evaluation (Table 3) only compares against the base model, not other fine-tuned methods.** While the primary contribution is counterfactual robustness, including other fine-tuned approaches (e.g., Context-DPO) in the non-counterfactual setting would strengthen the claim that CopyPasteLLM doesn't sacrifice normal performance.

5. **Training data composition of the 365 samples is underspecified.** The paper states 241 samples come from FaithEval but does not disclose the source of the remaining 124 samples. While the paper notes ConFiQA and PubMedQA are not used for training (mitigating leakage concerns for those evaluations), the composition should still be reported for reproducibility.

### Trivial

- "Logits Power" in Figure 3 is described operationally but lacks a precise definition or formula in the main text.

## Nice-to-Haves

- Reporting statistical significance or variance across runs for main results (Table 1, 3).
- Reporting latency/cost of the CP-Refine writer-reviewer loop (which uses an LLM judge for iterative refinement).
- An ablation quantifying the contribution of each pipeline component (multi-criteria filtering, Elo tournament, stamping answers).

## Removed Points

These points were flagged for removal; treat them with caution:

- **"Section 3.1: CP-Refine's writer-reviewer loop depends on an LLM judge — potentially expensive/brittle component"** — This is a reasonable observation but more of a nice-to-have implementation detail; the paper's scope is about the overall method and this doesn't threaten any core claim.
- **"Table 2 should compare with CoCoLex/Contrastive Decoding for Stage 1"** — This misunderstands the experimental design: Stage 1 is about generating preference data for Stage 2 training, and Table 2's baselines (Attributed, Citations) are the exact ones used as rejected candidates in the DPO pipeline. CoCoLex is compared in Table 1 after DPO training.
- **"Filtering samples where CopyPasteLLM responses exceeded base response lengths introduces bias"** — The paper states this filtering was done "to ensure fair comparison by providing base with longer token generation opportunities," which is a reasonable methodological choice, not a bias.
- **"Correlation does not imply causation"** — This is generic; the paper does not claim causation from the correlation alone, only that it motivates the DPO intervention.
- **"The data efficiency claim is not apples-to-apples"** — While fair in isolation, the paper's ConFiQA results (where CopyPasteLLM wasn't trained on ConFiQA) partially address this concern by showing cross-distribution data efficiency.
- **"Weak baselines in Stage 1"** / Strengths about generic "important problem" — Generic points removed per filtering rules.
- **Strength about "large accuracy improvements"** — This is a strength but merged into the data efficiency strength above since the ConFiQA generalization evidence is the more persuasive framing.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no perspective on the paper that the authors do not already articulate themselves.

## Suggestions

1. **Run the key control experiment**: Train standard DPO on the same 365 samples using gold answers as chosen responses (without the copy-paste preference construction). This isolates the effect of the high-copying preference from the effect of fine-tuning on well-chosen data.

2. **Address the FaithEval confound**: Either (a) fine-tune the strongest baseline (e.g., Context-DPO) on the same 241 FaithEval training samples and re-evaluate, or (b) restructure the paper to treat the ConFiQA results (cross-distribution generalization) as the primary evidence for the method, and present FaithEval results as a secondary within-distribution result with explicit caveats.

3. **Define all metrics in the main text**: Add brief definitions of Twist, Causal (the hallucination metrics), and Logits Power in the main body so readers can interpret Tables 2 and Figure 3 without deferring to the appendix.

4. **Disclose the exact composition of the 365 training samples** — how many from each source dataset.

## Calibration

**Round 1 bracket:** After inspecting weak (< 3.5), middle (3.5–7.5), and strong (> 7.5) anchor bands on topics related to RAG faithfulness, DPO hallucination mitigation, and mechanistic analysis, the plausible score range was between ~4.5 and ~6.5. The paper is clearly above weak papers (e.g., TrojanRAG at 3.40, EDU-RAG at 2.33) but below top-tier papers (e.g., Retrieval Head at 8.0, Context-Parametric Inversion at 8.0).

**Round 2 anchors (read in full):**

| Paper | Avg Score | Comparison |
|---|---|---|
| Fine-Tuning LMs for Factuality (WPZ2yPag4K) | 5.75 | Similar scope (DPO for factuality). That paper has cleaner evaluation but simpler method. Current paper has richer analysis and larger-scale evaluation but a significant confound in the FaithEval setup. Slightly weaker overall. |
| Mask-DPO (d2H1oTNITn) | 6.40 | Cleaner evaluation, more thorough baselines, out-of-domain generalization test. Current paper is weaker — the FaithEval confound is a more significant issue than any weakness in Mask-DPO. |
| Is Factuality Enhancement a Free Lunch? (asGQQc7gNo) | 6.67 | Stronger analysis with a nuanced finding about faithfulness/factuality trade-offs. Current paper is weaker. |
| Enhancing Situated Faithfulness (K2jOacHUlO) | 7.25 | Stronger in every dimension — more comprehensive, cleaner evaluation. Current paper is well below this. |
| MODPO (2BfZMh9td4) | 4.25 | Scored low for being a straightforward extension. Current paper has more novelty, evidence density, and analysis. Clearly above this. |

**Final score:** 5.5. The paper sits near the Fine-Tuning LMs for Factuality anchor (5.75) but is slightly lower due to the evaluation confound that weakens the headline claims. It is clearly above straightforward extension papers (MODPO at 4.25) and well below top-tier papers (7.25+). The core idea is sound and well-motivated, the mechanistic analysis is genuinely interesting, and the ConFiQA cross-distribution results are strong evidence. But the missing control experiment and the FaithEval confound are significant enough to lower the score relative to the strongest comparable papers. The contribution is real and the paper deserves acceptance, but it needs to address these issues for its results to be fully credible.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>