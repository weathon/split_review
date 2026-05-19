- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3, 5
Now I have verified the key claims against the paper. Let me produce the final review.

## Summary
The paper proposes MGSI (DualLLM), a method for extending the effective context window of LLMs without long-context pretraining. It uses two short-context LLMs (lower compressor and upper decoder) initialized from the same checkpoint, connected via cross-attention at shallow layers. A binary tree structure stores multi-grained compressed representations of past context, and a query-aware search retrieves relevant information at appropriate granularity. The method achieves competitive results on language modeling and long-context benchmarks while offering speed and memory advantages.

## Strengths
- **Shallow-layer self-injection eliminates hidden-space alignment overhead.** The lower and upper models are initialized from the same checkpoint (Sec. 3.1, 3.2), avoiding the extra pretraining and warmup stages required by heterogeneous encoder-decoder approaches like CEPE (which needs a RoBERTa encoder adaptation, Sec. 4.2). This makes the training pipeline simpler and more direct.

- **Query-aware coarse-to-fine compression via the context tree is a principled design.** The tree structure with depth-first search and cosine-similarity policy (Sec. 3.2, Fig. 2) encodes relevant text segments at finer granularity and less relevant ones more coarsely. The ablation study (Table 5) shows that removing query-aware retrieval causes the largest performance drop on MD-QA, confirming this component's importance.

- **Demonstrated efficiency gains on a single GPU.** The method achieves 2× speedup over streaming architectures (Activation Beacon) and 3× over encoder-decoder models (CEPE), with all experiments exceeding 200K tokens running on a single A800 80GB GPU (Sec. 4.3, Fig. 3). This concretely supports the paper's central claim of balancing performance with computational cost.

- **Extrapolation to 128K tokens after training on 8K sequences.** Language modeling perplexity does not degrade catastrophically at long contexts despite the model only seeing 8K-token sequences during training (Sec. 4.2, Tables 1-2). This demonstrates a genuine capability of the compression-based approach.

## Weaknesses

### Fatal
None.

### Major
- **Several implementation details are under-specified, harming reproducibility.**
  (a) The chunk-level position indices (Eq. 2, \(P_Q, P_\mathcal{K}\)) are assigned to queries and keys in cross-attention, but the paper never explains how these interact with LLaMA's RoPE — whether they replace the RoPE positions, are added as an absolute bias, or use some other mechanism. (b) The noise hyperparameter \(\sigma\) for random splitting (Eq. 1, \(\epsilon\sim\mathcal{N}(0,\sigma^2)\)) is not given. (c) The similarity computation for query-aware retrieval uses "a short forward pass through one self-attention layer" (Sec. 3.2) but does not specify which layer is used. (d) The trainable/frozen parameter split is ambiguous: the paper states cross-attention layers are "fully tunable" and the upper model's top \(N-M\) self-attention layers are trained (line 204), but does not state whether the lower model's weights (or the upper model's bottom \(M\) self-attention layers) are frozen or fine-tuned. These gaps mean a reader cannot reproduce the method without substantial guesswork.

- **Comparison against baselines is not controlled for training conditions.** The paper compares against published results of baselines (Activation Beacon, CEPE, LongAlpaca, etc.) that were trained on different data mixtures. The paper acknowledges that omitting books3 hurts performance (lines 221-222), but does not retrain baselines under the same data conditions. For language modeling, Table 2 reports "3-10%" improvement over baselines trained on a "mixed dataset" — but it is unclear whether those baselines were retrained on the same data or whether published numbers from different mixtures are being compared. The same concern applies to instruction-following benchmarks: baselines like LongChat and LongAlpaca were fine-tuned on different (sometimes proprietary or larger) datasets (Sec. 4.2). Without a controlled comparison (same data, same base model, same compute), the magnitude of improvement may be partly an artifact of data differences rather than the method itself.

### Minor
- **The tree structure's necessity is not fully ablated.** Query-aware retrieval is ablated only on MD-QA (Table 5, bottom rows), not on language modeling where the policy is fixed to "always-right" (line 133), causing the tree to degenerate to a linear chain. For language modeling, it is unclear whether the multi-resolution compression itself (without a binary tree structure) would suffice. A control experiment — e.g., compressing each chunk at multiple fixed granularities without any tree — would clarify whether the tree is load-bearing or merely an incidental implementation detail.

- **Limited evidence for extrapolation in instruction-following tasks.** The SFT training data is filtered to 1200–8192 tokens (line 200), and the paper does not report downstream task performance broken down by input length. The claim of "extrapolation to arbitrary length" is supported primarily by language modeling perplexity where only 10 examples are tested at 128K (line 217); for instruction-following, no evaluation is conducted at lengths exceeding the training horizon.

- **No error bars or variance estimates.** All results are reported as single points. For language modeling, 100 examples are used at most lengths and only 10 at 128K, meaning variance could be substantial. This is common practice in this subfield but limits confidence in the exact magnitude of improvements.

### Trivial
- The noise standard deviation \(\sigma\) for node splitting (Eq. 1) is said to be a "predefined hyperparameter" but is never given numerically.
- The paper notes Activation Beacon's incompatibility with FlashAttention (line 250) but does not explicitly state whether DualLLM's cross-attention is compatible.

## Nice-to-Haves
- Retrain a subset of baselines (e.g., Activation Beacon, CEPE) under the same data conditions as DualLLM to resolve the comparison fairness concern.
- Report perplexity as a function of length for all tested lengths in a single clear table/plot with confidence intervals.
- Provide pseudocode or a precise algorithmic specification of the tree construction and search procedure.
- Ablate the chunk size and noise parameter \(\sigma\) to show sensitivity.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Comparison against YaRN is not informative"** — Removed. The paper uses YaRN as a representative of full-attention methods to illustrate the \(O(L^2)\) memory scaling issue, which is a valid and informative comparison point for the efficiency evaluation. The critic's claim that this comparison is unfair misunderstands the purpose of including a non-compression baseline in an efficiency analysis.

- **"Tables missing from parsed text"** — Removed. The tables are included via `\input` commands and exist in the original submission. This is a parser artifact, not an author error.

- **"Missing related works"** — Removed per guidelines: I cannot verify the existence of such works without external sources.

- **"Cross-attention and position-id mechanism should be specified with enough detail"** (from Strengthening section) — Merged into Major weakness (1) above rather than listed separately.

- **Strength Finder's generic claims** (e.g., "this paper addressed an important problem") — Removed as generic/superficial. Only concrete, paper-specific strengths are retained.

- **Critic's claim about "statistical significance and variance" being a critical issue** — Demoted from major to minor, as single-run evaluation is standard practice for large-scale LLM benchmarks in this subfield, and the paper uses 100-example averages.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the expected trade-offs (novelty vs. reproducibility, efficiency claims vs. controlled comparison) but do not identify a new angle on the work that the paper itself misses.

## Suggestions
1. **Specify all missing implementation details:** provide the value of \(\sigma\), state which layers are used for the similarity forward pass, explain how chunk-level position ids interact with RoPE, and explicitly declare which parameters are frozen versus trained.
2. **Control the comparison:** retrain at least the most directly comparable baselines (Activation Beacon, CEPE) on the same data mixture as DualLLM, and report results with variance.
3. **Ablate the tree structure itself** for language modeling: compare against a simpler multi-resolution compression without the binary tree to isolate its contribution.
4. **Report instruction-following performance broken down by input length** to substantiate the extrapolation claim for downstream tasks.
