Now I have a thorough understanding of the paper. Let me produce the final review.

## Summary

ZeroTS proposes a framework for zero-shot time series forecasting that combines Retrieval-Augmented Generation (TS-RAG) with a frozen LLM (GPT-2) and a lightweight learnable adapter (ReinLLM). The data side retrieves similar series from an auxiliary database using a hybrid similarity metric and HSNSW indexing; the model side uses a policy network to select kernel sizes and fusion coefficients, with the negative MAE between LLM output and ground truth serving as a reward signal for end-to-end optimization. The paper claims best or second-best results across 8 zero-shot and 8 long-term forecasting settings with 1/4 memory and 1/7 inference speed versus parallel models.

## Strengths

1. **First integration of RAG with time series for zero-shot forecasting.** The paper explicitly identifies the gap (Section 1) and designs a complete pipeline: structural key-value database construction, compressed representation learning, hybrid similarity (cosine + Euclidean), and HSNSW-based retrieval (Section 4.1). This is a genuinely novel technical direction in the LLM4TS space.

2. **Clear problem formulation with well-identified limitations of prior work.** Section 1 diagnoses two specific issues in existing LLM4TS methods — insufficient scalability/flexibility and lack of data-model interactions — and the proposed components (TS-RAG for retrieval, ReinLLM for error feedback) are directly motivated by these gaps. The narrative coherence is a strength.

3. **Competitive reported results with efficiency gains.** The paper reports best/second-best on all 8 zero-shot settings and 8 long-term datasets, with 1/4 memory and 1/7 speed improvements claimed against parallel models. The efficiency claims are explicit and would be impactful if supported by the full tables.

4. **Hyperparameter study and qualitative case study.** Figure 4 examines the effect of retrieval count K and representation dimensions. Figure 5 provides a visual comparison with/without RAG showing that retrieved auxiliary series suppress hallucination by producing smoother forecasts.

## Weaknesses

### Fatal
None.

### Major

1. **The "reinforcement learning" component is mischaracterized and lacks a proper RL formulation.** The paper repeatedly calls ReinLLM a "reinforcement learning framework" (abstract, contributions, Section 4.2) but never provides an RL objective function, policy gradient update, or any standard RL training loop. What is actually described is an end-to-end differentiable pipeline where a policy network outputs actions (kernel sizes, fusion coefficients) and the negative MAE backpropagates through all parameters. The value network "estimates the value with learnable parameters" (line 150) but no target (returns, TD targets) or regression objective is specified. The update "αᵢ = αᵢ − η" (line 118) looks like standard gradient descent, not policy gradient. This is a significant overclaim — the mechanism is essentially supervised end-to-end training with a learned reward, not reinforcement learning. The paper must either (a) properly instantiate an RL algorithm (states, actions, rewards, policy gradient with a clear loss) or (b) retract the RL label and describe the actual training procedure honestly. Until this is resolved, the method cannot be fully reproduced or correctly categorized relative to existing work.

2. **Missing ablations that would validate the contribution of each component.** The paper does not ablate:
   - **RAG vs. no RAG** (quantitative, not just the qualitative case study in Figure 5)
   - **Policy network vs. random/fixed actions** (to show learned kernel/fusion selection matters)
   - **GPT-2 backbone vs. a non-LLM regression head** on the same representations (to justify the LLM's role)
   
   Without these ablations, it is unclear whether the claimed gains come from the retrieval, the learnable adapter, or the LLM itself. This is especially concerning because the architecture is complex (autoencoder compression + policy network + value network + LLM) and a simpler baseline (e.g., a small MLP on top of the fused retrieved+target representations) could potentially match performance.

3. **No error bars, standard deviations, or statistical significance for any experimental result.** The paper reports average MAE/MSE but does not provide variance estimates across runs. Given the complexity of the pipeline and the multiple components, single-run results are insufficient to establish that improvements are reliable rather than due to noise. This is standard practice for time-series forecasting papers in this venue and should be addressed.

### Minor

1. **The prompt construction for the LLM is underspecified.** Section 4.2 mentions a "triple unit including domain category, trend pattern, text description, as well as series representation" (line 110), and states that meta information is "tokenized and concatenated." But it is never clarified whether the LLM receives tokenized text descriptions, embedded numerical values, or a combination — a concrete example (e.g., "the input to GPT-2 is the string 'domain: electricity, trend: [0.02, -0.01, ...], values: [...]'") would greatly aid reproducibility.

2. **No runtime breakdown for the retrieval step.** The paper claims 1/7 inference speed vs. parallel models but does not decompose inference time across the three stages (HSNSW retrieval, policy/value network inference, LLM forward pass). The retrieval cost from a large database (Monash alone has >100K series) could dominate the total and should be reported separately.

3. **The HSNSW retrieval is compared against no alternative.** The paper uses HSNSW with hybrid similarity but does not compare against simpler alternatives (e.g., brute-force k-NN, k-means clustering) in terms of retrieval quality or speed. The paper's efficiency claims would be stronger with such a comparison.

### Trivial
- The paper uses "database" and "dataset" somewhat interchangeably (e.g., "auxiliary database (dataset)"), which could confuse readers about whether the retrieval corpus is fixed or dynamically updated. The claim of dynamic updating is never demonstrated.

## Nice-to-Haves

- A concrete example of the prompt format fed into GPT-2 would significantly improve reproducibility.
- Ablations varying the number of retrieved series K beyond the one setting shown in Figure 4.
- Comparison against a non-LLM model (e.g., linear regression or small MLP) that uses the same retrieval and representation pipeline, to isolate the LLM's contribution.
- Computational cost breakdown (retrieval vs. policy network vs. LLM forward pass).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Experimental results are garbled/unreadable"** — The table formatting artifacts are parser errors (broken characters, garbled numbers), not author errors. The original submission contains properly formatted tables.
- **"Figures 1-3 are described but not provided"** — The figures exist in the original submission as embedded images; the text extraction pipeline stripped them.
- **"Theoretical guarantee claimed but no proofs provided"** — The paper states theoretical details are in Sec. A.1 (appendix), which was stripped by the parser. Per instructions, missing appendix content is not a valid criticism.
- **"The paper should also cover Y / domain Z / additional tasks"** — Scope-creep demands that would turn the paper into a broader project rather than a stronger version of the current one.
- **Generic complaints about LLM not being time-series-specific** — GPT-2 as a frozen backbone is a defensible design choice common in the LLM4TS literature; demanding a different backbone is a matter of taste.
- **"The retrieval method is mentioned but never compared to simpler alternatives"** — Kept as a minor weakness above (retaining the core concern), but the harsh critic's framing as a fatal issue is downgraded.
- **"No discussion of computational cost of retrieval"** — Moved to minor weakness above (retained the valid concern, downgraded from "missing" to "would strengthen").

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear gap between the paper's claimed "reinforcement learning" innovation and what is actually implemented (end-to-end differentiable optimization), and the lack of ablations makes it difficult to attribute performance to any specific component. These are important but standard criticisms; no novel synthesis emerges beyond the papers' own framing.

## Suggestions

1. **Fix the RL claim.** Either properly instantiate a standard RL algorithm (define states, actions, transition dynamics, policy gradient objective with a clear loss function and training loop) or drop the "reinforcement" label entirely and describe the method as end-to-end differentiable optimization with error feedback. The latter is more accurate and does not diminish the contribution.

2. **Add three core ablations:** (a) with RAG vs. without RAG, (b) learned policy actions vs. random/fixed actions, (c) GPT-2 backbone vs. a simple MLP/linear head on the same representations. Report with standard deviations across multiple seeds.

3. **Provide a concrete example** of the prompt fed into GPT-2, showing exactly what tokenized/text format the LLM receives.

## Score and Decision

**Originality:** 7/10 — First RAG integration for time series forecasting is a genuinely novel direction. The ReinLLM adapter (error-feedback-based optimization) is a reasonable idea despite the mislabeling.

**Importance of research question:** 8/10 — Zero-shot time series forecasting is practically important and currently underexplored. The problem of leveraging external retrieval for LLM-based forecasting is well-motivated.

**Claims supported?** 4/10 — The central claims (effectiveness of RAG, RL, and LLM components) are not adequately supported due to missing ablations, no error bars, and the mischaracterized RL component whose objective is unspecified.

**Soundness of experiments:** 4/10 — Reasonable baselines and datasets, but the lack of ablations, error bars, and statistical testing significantly weakens the evidence.

**Clarity of writing:** 6/10 — The motivation and framework overview are clear, but the RL training procedure is vague, and the prompt construction is underspecified. The "theoretical guarantee" reference to a missing appendix is unhelpful.

**Value to the community:** 6/10 — The RAG-for-time-series direction is promising and could inspire follow-up work. However, the paper's current methodological gaps limit its immediate utility as a reproducible recipe.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>