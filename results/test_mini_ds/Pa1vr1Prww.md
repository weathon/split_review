Now I have enough calibration. Let me write the final consolidated review.

---

## Summary

This paper uses sparse autoencoders (SAEs) to deepen mechanistic understanding of in-context learning (ICL) in LLMs. It introduces the Task Vector Cleaning (TVC) algorithm to decompose task vectors into a sparse set of interpretable SAE features (as few as 4), identifies two families of causally relevant features — task-execution features (activating just before task completion) and task-detection features (activating on output tokens to signal task identity) — and adapts Sparse Feature Circuits (SFC) to trace causal connections between them in Gemma-1 2B.

## Strengths

1. **TVC produces genuinely sparse, performant decompositions of task vectors.** Figure 3 shows that the method reduces active SAE features to fewer than 4 on average (Figure 3b) while maintaining loss improvement comparable to the original task vector up to layer 14 (Figure 3a). This directly demonstrates that task vectors can be meaningfully decomposed into SAE features.

2. **Steering experiments confirm causal relevance of task-execution features.** Figure 5 shows a clear diagonal pattern: steering with a single task-execution feature improves loss on exactly one task in most cases, with the exception of related tasks (e.g., translation-to-English sharing a feature). This is the most compelling causal evidence in the paper.

3. **The SFC adaptations (token-position categorization and loss-function modification) are thoughtful engineering contributions.** Section 4.1.1 groups features by token type (prompt, input, arrow, output, newline), enabling separation of features by their role in ICL. Section 4.1.2 addresses the cloning-circuit interference problem that would otherwise prevent SFC from working on ICL.

4. **Unifies task vectors with sparse feature decompositions.** The paper bridges two previously separate lines of work (task vectors from Todd et al./Hendel et al. and SAE feature discovery), showing that task vectors can be expressed as sparse sums of interpretable SAE latents — a non-trivial finding.

5. **Discovery of task-detection features is novel and well-motivated.** Section 4.2 identifies features that activate on output tokens (Table 2) and are causally linked to task-execution features, adding a new component to the known ICL circuit.

## Weaknesses

### Fatal
None.

### Major

1. **The TVC algorithm is underspecified.** The main text provides only a high-level description: initializing from the SAE encoder output, then optimizing with a sparsity penalty and a performance loss computed on steering (lines 108–120). The exact loss function, optimization procedure (learning rate, number of steps, convergence criterion), and how the sparsity/performance objectives are balanced are absent from the paper. The algorithm is deferred to Figure 10 (an image). Without this specification, TVC cannot be independently reimplemented or assessed. This is the single most significant weakness because TVC is the method that enables the central claim.

2. **No error bars or variance reporting on any quantitative result.** Figures 3a, 5, 6, 7, and 8 all report point estimates without standard deviations, confidence intervals, or replication information. For claims about loss improvements and causal effects that could vary across tasks, data samples, or random seeds, this makes it impossible to gauge the reliability of the reported effects.

3. **The causal evidence linking detection features to execution features is thin.** The entire experimental description is one sentence (line 221): "We then ablated detection directions while fixing attention patterns and measured the decrease in execution activations." Key details are missing: what "ablating detection directions" means (zero-ablation? directional ablation?), how attention patterns are "fixed" and whether this intervention itself distorts the circuit, how many detection/execution feature pairs were tested, and whether the results are statistically significant. Figure 8 shows a heatmap with no error bars. The weak connections for "person profession" and "present simple gerund" (which the paper notes warrant further investigation) suggest the effect does not hold universally.

4. **The "greater detail than any prior mechanistic interpretability work" claim (line 248) is not supported.** The paper does not systematically compare its granularity or findings to prior ICL interpretability work (e.g., Wang et al., which is mentioned only in passing). Without a concrete comparison — what new information does the SAE-based approach reveal that attention-patching or activation-patching could not? — this claim is unverifiable.

### Minor

1. **The faithfulness evaluation excludes two tasks without fully addressing the implications.** The paper notes (lines 206–207) that "person profession" and "football player position" were excluded from Figure 6 because the small difference between fully ablated and non-ablated losses made faithfulness calculations unstable. This is acknowledged, but the fact that the metric fails for 2 out of roughly 8–10 tasks should raise the question of whether the loss function modification (Section 4.1.2) has introduced artifacts. The paper attributes the issue to the modified loss function but continues to use that same loss for all other analyses.

2. **TVC is applied to extract detection features without explaining how.** The paper says "We applied our task vector cleaning algorithm to extract task-detection features" (line 210), but TVC was designed to decompose task vectors (which are residual stream directions). Detection features are identified via SFC, not from task vectors. How the adaptation works is not explained.

3. **Activation mass results (Tables 1, 2) lack per-task breakdowns and variance.** The tables average across all tasks, which obscures potential differences. Showing per-task distributions or standard deviations would strengthen the claim that executor features consistently activate on arrow tokens and detection features on output tokens.

4. **Steering experiments (Figure 5) do not specify how the "most relevant" feature was chosen per task, nor how many features were tested.** The paper reports that "most tasks have a single feature with high effect," but describing the distribution of effects across all extracted features for a given task would be more informative.

### Trivial

None.

## Nice-to-Haves

- A comparison of faithfulness under the modified loss vs. the original SFC loss would help isolate whether the modification is necessary or introduces artifacts.
- The paper studies only one model (Gemma-1 2B). Testing on a second model (even at the same scale) would strengthen claims about generality.
- Showing absolute loss improvement values (not just relative) for the TVC comparison (Figure 3a) would help contextualize the decomposition's effect size.

## Removed Points

- **"SAE reconstruction is a straw man" and "no LASSO/basis pursuit comparison"** from the harsh critic: The paper compares against two ITO variants (L0=5, L0=20) and the original task vector, which are reasonable baselines for this setting. LASSO and basis pursuit are generic sparse coding methods that do not account for the LLM steering context. This is scope creep.
- **"The paper does not discuss that only a single model was studied"** (from limitations section critique): The limitations section explicitly states "we only interpreted Gemma-1 2B" (line 244). The critic's point is factually incorrect — the paper does discuss this.
- **"Missing code"** and **"No code was provided for review"**: Code release is promised upon acceptance, which is standard. The paper includes a reproducibility statement (Section 7).
- **"Missing SAE training details"**: The paper states it uses Gated SAEs from existing libraries and references published work for details. This is standard practice.
- **"The paper claims in the abstract that SAE features 'encode the model's knowledge of which task to execute' — conflation with causation"**: The features are validated through causal steering experiments (Figure 5), so the claim is supported by the evidence presented.
- **Several strengths from the Strength Finder** dropped as generic or sycophantic: all four "Supporting strengths" were preserved; dropped "The paper demonstrates that SAEs can deepen understanding" as it restates the paper's goal rather than providing a concrete strength.

## Novel Insights

The harsh critic's observation that TVC's design — using the steering performance signal to guide sparse decomposition — makes the resulting features "causally relevant by construction" is a useful framing that the paper does not explicitly articulate. The reviewer identifies that this is both a strength (the features inherit causal relevance from task vectors) and a limitation (the method is task-specific and cannot decompose arbitrary model behaviors). This tension between the method's power and its specificity is worth the authors addressing directly in revision.

The cross-review synthesis also surfaces a point neither reviewer made explicitly: the paper's two main methodological contributions (TVC for decomposition, SFC adaptations for circuit finding) operate at fundamentally different levels of granularity. TVC decomposes a single vector into features; SFC builds a causal graph over features. The paper could benefit from explicitly comparing what each method contributes to the overall ICL explanation.

## Suggestions

1. **Specify the TVC algorithm.** Provide the full loss function, optimization hyperparameters (learning rate, steps, convergence), and the sparsity-performance trade-off in the main text or appendix. This is essential for reproducibility.
2. **Add error bars.** Report standard deviations or confidence intervals for all quantitative results (Figures 3, 5, 6, 7, 8). This is standard practice and would significantly strengthen the paper.
3. **Clarify the detection-to-execution causal experiment.** Describe the intervention protocol precisely: what "ablating detection directions" means technically, how attention patterns are fixed and why this is valid, how many pairs were tested, and whether the results are significant across pairs.
4. **Tone down the "greater detail than any prior work" claim**, or support it with a concrete comparison table showing what specific insights the SAE-based approach reveals that prior methods could not access.
5. **Show per-task breakdowns** for the activation mass tables and steering effect distributions, not just averages.

## Score and Decision

**Calibration Report:**

*Round 1 (Bracketing: score 0–3, 4–7, 8–10):*
- Weak anchors (avg 1.67–3.00): Chess SAE (2.50), pSAE-chiatry (2.50), Sparsity beyond TopK (1.67) — clearly weaker papers
- Middle anchors (avg 4.67–7.00): Sparse Autoencoders Find Highly Interpretable Features (4.80), Compute Optimal Inference (4.67), Sparse Autoencoders Do Not Find Canonical Units (7.00), Towards Principled Evaluations (7.00) — mixed quality
- Strong anchors (avg 8.00–9.00): Sparse Feature Circuits (8.00), Scaling SAEs (8.20), Retrieval Head (8.00) — clearly stronger papers

**Bracket: 4.5–6.5**

*Round 2 (Narrowing within bracket):*
- Lower band (4.5–5.5): SAE for Unlearning (5.25), Compute Optimal Inference (4.67), Mechanistic Basis of Data Dependence (4.50) — comparable or slightly weaker
- Upper band (5.5–6.5): PatchSAE (6.50), Revisiting ICL Inference Circuit (6.50), Residual Stream Analysis with MLSAEs (6.50), Function Vectors (6.00), From Context to Concept (6.00) — somewhat stronger

**Final comparison:** The paper is more novel than "From Context to Concept" (rejected for insufficient novelty despite 6.0 score from replicating task vector findings) because it contributes new methodology (TVC) and discovers new circuit components (task-detection features). However, it is weaker than "Function Vectors" (6.0, accepted) which tested across more models with cleaner methodology. It is substantially weaker than Sparse Feature Circuits (8.0) which it builds on. The underspecified TVC and missing error bars are the primary limitations preventing a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>