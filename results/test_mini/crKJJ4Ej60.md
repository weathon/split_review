Now let me write the consolidated review.

---

## Summary

This paper proposes **Copy-Paste**, a generation paradigm for RAG that encourages LLMs to directly copy contextual fragments into responses as a way to improve faithfulness and reduce hallucinations. The authors first establish an inverse correlation between copying degree and hallucination density on RAGTruth (Section 2.2). They then design three prompting methods (CP-Order, CP-Link, CP-Refine) that produce high-copying responses, and use these to automatically construct preference data for DPO training of **CopyPasteLLM** using only 365 query-context pairs. A mechanistic analysis via **Context-Parameter Copying Capturing** shows that CopyPasteLLM exhibits higher contextual logit power and lower parametric logit power compared to the base model. Evaluations are conducted on FaithEval, ConFiQA, and PubMedQA across Llama-3-8B, Mistral-7B-v0.2, and Llama-3.1-8B.

## Strengths

1. **Empirically grounded motivation.** The inverse correlation between copying degree and hallucination density is demonstrated on RAGTruth across six models (Section 2.2, Figure 1), providing a data-driven foundation for the Copy-Paste paradigm beyond intuition.

2. **Three well-characterized prompting methods with systematic trade-offs.** CP-Order, CP-Link, and CP-Refine are clearly described and evaluated across four model families (Table 2), with detailed reporting of copying metrics (κ, δ), faithfulness, hallucination, and fluency scores. CP-Refine's soft-constraint iterative refinement achieves a strong balance between faithfulness and fluency.

3. **Fully automated preference data construction pipeline.** The multi-stage pipeline (multi-criteria filtering → Elo-style hallucination tournament → answer stamping) converts raw query-context pairs into DPO preference data without manual annotation, a practical contribution that supports scalability.

4. **Context-Parameter Copying Capturing analysis.** The token-level probe of contextual vs. parametric knowledge usage across the full Chain-of-Thought trajectory (extending KTC) provides interpretability insights. The finding that CopyPasteLLM's contextual representations remain nearly co-distributed with the base model while parametric representations diverge (Figure 4) is interesting and goes beyond simple performance reporting.

5. **Broad evaluation across models and datasets.** The method is tested on three base models (Llama-3-8B, Mistral-7B-v0.2, Llama-3.1-8B) and four datasets (FaithEval, ConFiQA, PubMedQA, RAGTruth), with both counterfactual and non-counterfactual settings. Code is released.

## Weaknesses

### Major

1. **FaithEval evaluation confounded by training/test distribution overlap.** The headline claim of 12.2%–24.5% improvement on FaithEval is substantially weakened because 241 of the 365 training samples are drawn from FaithEval itself, and the test set is the remaining FaithEval samples. Baselines (Context-DPO, Canoe, ParamMute) were not trained on any FaithEval data, making the comparison asymmetric. No control experiment is provided (e.g., training baselines on the same 241 FaithEval samples, or training CopyPasteLLM on data from a different source). The paper discloses this in the Table 1 caption and Appendix Table 4, but it is not flagged in the abstract or main text. **Consequence:** The headline accuracy gap on FaithEval cannot be cleanly attributed to the method rather than to in-distribution training advantage.

2. **Data efficiency claim is not supported by a controlled comparison.** The claim that CopyPasteLLM is "50× more data-efficient" than Context-DPO rests on comparing training on different data sources (365 from FaithEval vs. 18K from ConFiQA). If Context-DPO were trained on the same 365 FaithEval samples, it might close or reverse the gap. The data-efficiency claim would require a matched-sample experiment where all fine-tuning methods train on the same data with equal compute, which is not provided.

3. **ConFiQA results show more limited advantage when the asymmetry is reversed.** On ConFiQA (where Context-DPO is trained in-distribution while CopyPasteLLM is not), Context-DPO generally outperforms CopyPasteLLM on Llama-3-8B (e.g., ConFiQA-QA: 88.9 vs. 83.6; ConFiQA-MR: 88.4 vs. 80.9). CopyPasteLLM is competitive on Mistral-7B-v0.2 but rarely exceeds Context-DPO. This pattern is consistent with the confound explanation for the FaithEval results and undercuts the claim of uniform superiority.

4. **Mechanistic interpretations overreach the correlational evidence.** The paper states that CopyPasteLLM "fundamentally recalibrates the model's internal confidence in parametric knowledge" and "selective parametric knowledge suppression" as a mechanism. The evidence (Figures 3–4) is correlational: higher contextual logit power and lower parametric logit power are a direct consequence of training on high-copying responses, and could equally reflect learned copying behavior rather than a deeper "recalibration of trust." No causal intervention (e.g., activation patching, knock-out analysis, or training on low-copying responses as a control) is performed. The paper would benefit from framing these findings as descriptive rather than mechanistic.

### Minor

1. **Abstract overstates uniformity of results.** The abstract claims "best performance in both counterfactual and original contexts." On the ConFiQA counterfactual subsets for Llama-3-8B, Context-DPO outperforms CopyPasteLLM on all three subsets. The claim is true on FaithEval and on most non-counterfactual settings, but the phrasing is stronger than the overall pattern supports.

2. **Non-extractive RAG settings not evaluated.** The paper's premise is that copying reduces hallucinations, but many RAG settings require abstraction or synthesis (e.g., combining information from multiple sentences). Including a dataset where verbatim copying is impossible would clarify the method's scope and limitations.

### Trivial

None.

## Nice-to-Haves

- A controlled experiment where all fine-tuning baselines are trained on the same 365-sample pool (drawn from FaithEval or another source) would cleanly resolve the comparison fairness concern.
- Adding a causal analysis (e.g., comparing against a model trained on low-copying preferences, or activation patching) would strengthen the mechanistic claims.
- Testing on a purely abstractive RAG dataset (where gold answers require synthesizing multiple context spans) would clarify the method's scope.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"FaithEval preference construction introduces confound via stamping"** (Harsh Critic, Section 3.2). The critic argues that using gold answers to construct preference pairs biases training toward copying. This describes the standard operation of supervised preference construction — gold answers are the correct signal. It is not a confound beyond the already-acknowledged distribution overlap issue.
- **"Abstract phrasing misleading: Table 3 shows marginal gains on PubMedQA"** (Harsh Critic). Table 3 shows +2.8% (Mistral) and +0.2% (Llama-3-8B) on PubMedQA. The claim "best performance in both counterfactual and original contexts" refers to the overall evaluation (Table 1 + Table 3), and CopyPasteLLM does beat the base model on all PubMedQA settings. The overstatement on ConFiQA counterfactual is more relevant and retained as a minor weakness above.
- **"Section 2.1 task definition vs. evaluation mismatch"** (Harsh Critic). The paper defines Copy-Paste as maximizing lexical reuse, then evaluates on tasks where answers are not always verbatim in context. As the critic acknowledges, this is "not a flaw per se." The evaluation measures downstream faithfulness, which is the paper's stated goal.
- **"CopyPasteLLM internalization rests on a weaker foundation"** (Harsh Critic). This is a qualitative assessment that is captured more concretely by the experimental confound and mechanistic overreach points already retained.
- **Various generic or speculative concerns** (e.g., "could the metric be measuring a proxy?", generic complaints about comparison fairness without specific evidence).
- **Strength Finder claim that "CopyPasteLLM surpasses... on all ConFiQA subsets for both models"** — factually incorrect for Llama-3-8B (Context-DPO outperforms on all three ConFiQA subsets). This strength is removed.
- **Generic strengths** (e.g., "addressed an important problem," "targeted an interesting question") — removed as they lack concrete, paper-specific content.

## Novel Insights

The harsh critic's observation about the comparison asymmetry being **bidirectional** is worth attention: on FaithEval, CopyPasteLLM has in-distribution data while baselines do not; on ConFiQA, Context-DPO has in-distribution data while CopyPasteLLM does not. The fact that CopyPasteLLM remains competitive on ConFiQA (particularly on Mistral) despite being out-of-distribution is actually a positive signal for the method — but one that is obscured by the paper's framing of uniform superiority. This pattern suggests the approach has real, if more modest, value that a properly controlled experiment could isolate.

## Suggestions

1. Disclose the FaithEval training-test overlap prominently in the abstract and main text (not only in the table caption), and add a discussion of what the FaithEval results would mean with and without the confound.
2. Add a controlled experiment where all fine-tuning methods (Context-DPO, Canoe, ParamMute) are trained on exactly the same 365-sample pool used by CopyPasteLLM, with equal compute budgets. This would directly test data efficiency claims.
3. Tone down the mechanistic interpretations from "recalibration" to "consistent with reduced parametric knowledge reliance," or add a causal intervention experiment.
4. Frame the ConFiQA results as cross-dataset generalization evidence (trained on FaithEval, tested on ConFiQA, competitive despite the distribution mismatch against in-distribution baselines) rather than claiming uniform best performance.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- Weak band (score < 3.5): Papers like "RAG Hype vs. Reality" (2.00), "Understanding Conformal Factuality" (3.00), "FAITH" (3.00). These are systematic study or position papers with limited novel methodology. The current paper has more concrete technical contributions.
- Middle band (3.5–7.5): SSFO (4.50) — self-supervised DPO for RAG faithfulness, most topically similar anchor. DeepRAG (4.67) — MDP-based adaptive retrieval. DSPO (4.00) — RL for agent search. 
- Strong band (>7.5): Top-scoring papers (8.00) on multi-turn conversation, multimodal meta-reasoning, or agent benchmarks — not comparable in scope.

**Initial bracket:** 4.5–6.0

**Round 2 — Narrowing:**
- SSFO (4.50, sim 0.77): Most directly comparable. Both use DPO for RAG faithfulness with small training data. The current paper is more comprehensive (Stage 1 prompting + Stage 2 DPO + mechanistic analysis, broader evaluation) but SSFO avoids the confound issue. The current paper is moderately stronger — **5.0 vs. 4.5**.
- DeepRAG (4.67, sim 0.72): Different approach (adaptive retrieval decisions) but same general area. Comparable empirical rigor. The current paper has clearer novelty — **comparable or slightly stronger**.
- Data Selection for Alignment (6.00): Strong theoretical contribution and clean experiments in a different sub-area. The current paper lacks comparable theoretical formalism and has an experimental confound — **weaker than 6.0**.

**Final score determination:** The paper sits between SSFO (4.5) and the 6.0-level papers. The FaithEval confound is a real weakness that prevents it from being a clear accept, but the Stage 1 findings, automated pipeline, and mechanistic framework are genuine contributions beyond SSFO's purely self-supervised approach. The paper is meaningfully stronger than SSFO but not strong enough to cross into the 6+ range without addressing the confound.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>