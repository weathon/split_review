Here is my final consolidated review.

---

## Summary

This paper proposes Causal Relation Networks (CausalRNs), an all-MLP architecture for autoregressive sequence modeling. Its core theoretical contribution is the discovery that Relation Networks with $\exp(x)$ activation can be exactly linearized from $O(N^2)$ to $O(N)$ time via the property $\sum_i \exp(\mathbf{p}_i + \mathbf{q}_j) = \exp(\mathbf{q}_j) \circ \sum_i \exp(\mathbf{p}_i)$, enabling parallel training and $O(1)$ streaming inference. The paper also introduces pre-activation normalization to recover a matrix-valued memory state and draws conceptual connections to exponential gating, state expansion, and existing architectures.

## Strengths

- **Exact, approximation-free linearization of exponentially-activated Relation Networks**: Proposition 3.2 (Eq. 9) proves that using $\exp(x)$ as the activation reduces pairwise summation from $O(N^2)$ to $O(N)$ via a simple factoring identity. The derivation is clean, correct, and proceeds step-by-step from the MLP definition. This is the paper's strongest contribution.

- **Empirical validation that pre-activation normalization recovers matrix-valued memory**: Figure 6 (Section 4.4) compares convergence on the copying task across string sizes $2^4$ to $2^8$. Pre-activation-normalized (quadratic) CausalRNs converge faster than Transformers, while linearized (vector-memory) variants fail at lengths $\ge 2^7$. This directly supports the paper's central hypothesis about matrix-valued states enabling in-context retrieval.

- **Systematic ablation study isolating each design choice**: Figure 3 tests four components independently (post-reduction normalization, pre-activation normalization, $\exp(x)$ activation, state expansion) with clear baseline comparisons. The ablations link each component to known design patterns (exponential gating, state expansion, matrix-valued states), providing genuine insight beyond just reporting performance.

- **Interpretability analysis shows learned relational structure without explicit attention**: Figure 7 demonstrates that a trained Linear BiRN can focus on foreground objects (frog, plane) while suppressing background, despite having no explicit attention mechanism — only MLPs and summation.

- **The paper honestly scopes itself as a scientific investigation**: Section 5 lists three clear limitations (no multi-head scheme, not I/O-aware, doesn't use tensor cores), and the introduction states "We do not position the CausalRN as a replacement for Transformers or State Space Models" (line 33). This framing, when read in the body, correctly sets expectations for a theoretical/exploratory contribution.

## Weaknesses

### Fatal
None.

### Major

- **The abstract makes empirical claims that are contradicted or unsubstantiated by the paper's own experiments**: The abstract claims CausalRNs are "comparable to Linear Transformers" (line 9) and that "perfect retrieval on the copying task...was previously only possible with Transformers" (line 10). However: (a) No Linear Transformer baseline appears in any experiment — the claim of comparability is entirely unsubstantiated; (b) The body text itself says Linear BiRN results are "not competitive" (line 204); (c) The copying-task exclusivity claim is asserted without showing that any other linear-time architecture (Mamba, RWKV, Hyena, Linear Attention) fails at this task. These are not minor framing issues — they create a direct contradiction between the abstract's promises and the evidence provided. The paper would be stronger (and more consistent with its own scientific-investigation framing) if the abstract were rewritten to match the modesty of the body.

- **No controlled comparison on model size, parameter count, or compute budget**: Tables 1 and 2 compare CausalRNs against Transformers and Mamba on perplexity and accuracy, but nowhere does the paper report how many parameters each model has, what the model sizes are, or whether comparisons are at matched budgets. Without this information, the quantitative results are uninterpretable — a smaller CausalRN getting higher perplexity than a larger Transformer tells the reader nothing about the architecture. This is a basic experimental design gap.

- **The copying-task exclusivity claim is unsubstantiated**: The abstract's assertion that perfect retrieval on the copying task "was previously only possible with Transformers" is not supported by any experiment or citation showing that other architectures (Mamba, RWKV, Hyena, etc.) fail under comparable conditions. This claim appears as a headline result but lacks the evidence needed to back it up.

### Minor

- **Approximation error of split pre-activation normalization is not analyzed**: Section 3.4 introduces an approximation $\exp(\mu(x) + \mu(y))$ to preserve linearizability while using pre-activation normalization, but never quantifies how much this approximation costs in terms of memory quality or retrieval fidelity. This is a natural experiment that would deepen the paper's own theoretical narrative.

- **Ablation study conducted only at a single string length**: The careful ablation in Figure 3 (Section 4.2) is performed solely on the copying task with string length 128. The conclusions drawn about "the importance for sequence modeling architectures to maintain matrix-valued memory states" would be strengthened by testing at additional lengths.

- **Framing tension between the abstract and the body**: While the body is appropriately modest, the abstract's framing ("comparable to Linear Transformers," "perfect retrieval...previously only possible with Transformers") sets up expectations the paper cannot meet and that its own authors disclaim later. This inconsistency harms the paper's credibility.

### Trivial
None.

## Nice-to-Haves
- Adding a Linear Transformer baseline (even on a small-scale controlled experiment) would substantiate the abstract's "comparable to" claim.
- Reporting parameter counts for all models in Tables 1 and 2 would make the comparisons interpretable.
- A brief analysis of how performance changes with depth (number of stacked CausalRN blocks) would address a standard architectural concern.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **Tables are embedded images**: This is a PDF-extraction artifact, not an author error. The tables exist in the original submission.
- **"First all-MLP" definitional debate**: The paper's claim that CausalRNs are the "first all-MLP architecture that supports autoregressive sequence modeling" is specific and defensible. Mamba uses selective SSM layers (not pure MLPs), and RWKV uses a mix of mechanisms. The critic's objection is based on a loose definition of "all-MLP" that the paper does not adopt.
- **No runtime/efficiency measurements**: The paper claims mathematical properties (linear time, $O(1)$ streaming, parallelizability), not wall-clock benchmarks. Requesting runtime measurements is scope creep for a theoretical probe paper.
- **Multi-layer stacking not analyzed**: The paper does discuss stacking in Section 3.1 (equivariance enables stacking). A deeper analysis would strengthen the paper but its absence is not a weakness.
- **"One epoch is unusual"**: The paper explains (lines 196-197, 204) that the dataset sizes (522M tokens for WikiText-103, 5M images for CIFAR-5M) allow convergence within a single epoch, making this a deliberate design choice rather than an oversight.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a genuine tension between the abstract's competitive framing and the body's scientific-investigation framing, and highlight missing experimental controls, but these are standard review critiques rather than novel observations.

## Suggestions
- Rewrite the abstract to match the body's modesty: remove "comparable to Linear Transformers" (unsubstantiated) and qualify or remove the "previously only possible with Transformers" exclusivity claim.
- Add parameter counts to all experimental comparisons, even if at small scale with matched model sizes.
- Either substantiate the copying-task exclusivity claim with evidence that other linear-time architectures fail, or replace it with a more precise statement (e.g., "CausalRNs achieve perfect retrieval on the copying task, comparable to Transformers").
- Analyze the approximation error of the split pre-activation normalization (how much does $\exp(\mu(x)+\mu(y))$ differ from the exact quadratic form?).

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>