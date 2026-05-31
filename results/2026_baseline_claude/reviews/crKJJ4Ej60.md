## Summary

This paper proposes **Copy-Paste**, a generation paradigm for mitigating faithfulness hallucinations in RAG systems by maximizing direct lexical copying from retrieved context. The key empirical motivation is an observed inverse correlation between copying degree and hallucination density across six models on RAGTruth. The contribution is realized as a two-stage pipeline: (1) Copy-Paste-Prompting (three variants: CP-Order, CP-Link, CP-Refine) generates high-copying candidate responses, and (2) CopyPasteLLM applies DPO using these responses as preference data. The authors also introduce Context-Parameter Copying Capturing (CPCC), an interpretability tool that traces contextual vs. parametric knowledge usage at every token position during Chain-of-Thought generation.

---

## Strengths

- **Data efficiency with strong empirical gains.** CopyPasteLLM achieves 12.2–24.5% accuracy improvements on the FaithEval counterfactual subset over the strongest fine-tuning baseline (Context-DPO), using only 365 training samples—50× fewer than the 18,000 required by Context-DPO. This extreme data efficiency is consistently demonstrated across three model families (Mistral-7B-v0.2, Llama-3-8B, Llama-3.1-8B), making the claim robust.

- **Well-motivated empirical observation.** The motivating analysis of copying degree versus hallucination density in Figure 1—computed via kernel density estimation across six diverse models on RAGTruth—provides a concrete, multi-model empirical foundation. The pattern is consistent, not a single model artifact.

- **Non-trivial mechanistic insight via CPCC.** The CPCC analysis reveals that CopyPasteLLM's effectiveness stems from *suppressing parametric knowledge confidence* (4th column of Figure 4: parametric hidden states shift substantially) rather than enhancing contextual representations (3rd column: contextual hidden states co-distribute with the base model). This is a nuanced and testable insight that goes beyond a simple "model copies more → does better" explanation.

- **Comprehensive evaluation.** The paper tests across four datasets (RAGTruth, FaithEval, ConFiQA-QA/MR/MC, PubMedQA), two settings (counterfactual and non-counterfactual), three prompting methods, and multiple faithfulness/hallucination metrics (MiniCheck, AlignScore, ELO-ranked Twist/Causal hallucinations). Non-counterfactual performance in Table 3 confirms the method does not degrade baseline contextual grounding ability.

- **End-to-end automated pipeline.** The fully automated process—from high-copying response generation through multi-criteria filtering, ELO tournament, answer stamping, to DPO training—requires no manual annotation, which is practically important.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **Evaluation protocol ambiguity for FaithEval.** The paper notes 241 samples from FaithEval were used for training CopyPasteLLM, and the remaining samples are used for testing. However, it is not clearly stated whether the baselines in Table 1 are *also evaluated on this same remaining subset*, or on the full FaithEval dataset. If baselines are evaluated on the full dataset while CopyPasteLLM is tested on a non-overlapping subset, the comparison is not apples-to-apples. More importantly, if the 241 training samples happen to be the harder items (or the "typical" counterfactual cases), the remaining 759 test items might be systematically easier, inflating CopyPasteLLM's performance gains. This needs explicit clarification with a shared test set.

2. **Correlation vs. causation in the core motivation.** The motivating observation that higher copying degree correlates with lower hallucination (Figure 1) may reflect a confounder: models that tend to follow instructions better naturally produce higher-copying responses and also hallucinate less. The paper hypothesizes that copying *causes* lower hallucination, but the RAGTruth analysis only demonstrates correlation. The copy-paste training pipeline subsequently operationalizes this hypothesis without a clean causal experiment (e.g., a controlled study fixing model capability while varying copying constraint).

3. **Robustness to noisy contexts not quantified.** Copy-heavy responses will faithfully reproduce errors in the provided context. The paper acknowledges this risk in the ethics statement, but there is no experiment measuring degradation when context quality is systematically poor. This is a practical concern for real-world RAG deployments, and its absence is a gap in the empirical coverage.

### Minor

1. **Interpreting ELO hallucination scores in Table 2.** The paper uses ELO scores for the Twist and Causal hallucination columns, but never explicitly states whether higher ELO = fewer hallucinations (winner = less hallucination) or higher = more. Readers must infer from context that higher is better. The direction should be stated explicitly.

2. **"Stamping" strategy lacks in-text justification.** Appending gold/wrong answers to chosen/rejected CP candidates before DPO (the "Stamping" step) is an unusual procedure. The ablation is deferred to Appendix G, but the intuition for why this disentangles reasoning from decisions would benefit from in-text explanation—especially since it's a differentiating design choice.

3. **FaithEval vs. GPT-4o comparison.** The claim that CopyPasteLLM (8B) surpasses GPT-4o's reported 47.5% by ~45 percentage points is extraordinary. This likely reflects that the Copy-Paste paradigm is specifically tailored to counterfactual tasks where direct context copying trivially provides the correct answer—an important caveat worth stating explicitly rather than leaving to the reader.

### Trivial
- Figure 1 caption appears three times in succession (parser artifact, not a paper flaw).

---

## Nice-to-Haves

- An experiment varying context quality (clean vs. partially incorrect contexts) would quantify the reliability-faithfulness tradeoff that is central to the method's limitations.
- Scaling CopyPasteLLM to a 70B backbone or testing the prompting methods on a frontier model (e.g., GPT-4o) as the base for Stage 1 would strengthen generalizability claims.
- A brief discussion of how CPCC could be used at inference time (e.g., as a detection signal for faithfulness failures) would increase practical impact.

---

## Novel Insights

The most genuinely novel insight is the asymmetric mechanism uncovered by CPCC: CopyPasteLLM achieves contextual faithfulness not by amplifying contextual knowledge representations (which remain nearly identical to the base model's) but by *selectively suppressing parametric knowledge confidence*. This "parametric recalibration" interpretation is non-obvious and advances the mechanistic understanding of knowledge conflict resolution in LLMs. It suggests that overcoming context-parametric conflicts is fundamentally a suppression problem (reducing competing internal signals) rather than an enhancement problem (increasing external signal strength), with implications for how preference-based training interacts with a model's internal belief state.

---

## Suggestions

- Provide explicit confirmation that all methods in Table 1 are evaluated on the exact same test split of FaithEval (the 759 samples after removing 241 training samples).
- Include even a small experiment (e.g., 50-100 samples) with intentionally noisy or partially wrong context to bound the method's failure mode.
- Clarify the ELO tournament direction in Table 2 and consider converting ELO scores to win-rates against a fixed reference to improve interpretability.
- State explicitly in the main text why the stamping strategy is expected to help DPO training, even if the full ablation is in the appendix.

---

## Score and Decision

The paper introduces a creative, well-motivated, and empirically strong approach to RAG faithfulness. The 50× data efficiency over the strongest baseline is a genuine and reproducible contribution. The CPCC interpretability analysis provides real mechanistic insight—not just post-hoc rationalization. The primary concerns (evaluation protocol clarity for FaithEval, causation vs. correlation, noisy-context robustness) are meaningful but do not invalidate the core claims; they are resolvable through clarification and additional experiments. The method works consistently across three model families and multiple benchmarks.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>