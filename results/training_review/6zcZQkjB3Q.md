Now I have all the information needed. Let me compose the final consolidated review.

## Summary

iReVa proposes a traceable model editing method that inserts per-edit key-value adaptors into the MLP layers of Transformer LMs. Each edit is stored as a separate (key, value) neuron, enabling explicit localization and withdrawal of individual edits by removing the corresponding column. Experiments on GPT2-XL, GPT-Neo-2.7B, and GPT-J-6B show competitive edit success and specificity, along with a first-of-its-kind knowledge withdrawal test.

## Strengths

- **First demonstrated knowledge withdrawal in model editing (Section 6.2, Table 2):** The paper designs and evaluates Retrieve Success and Consistency metrics for withdrawal, showing near-perfect scores. No prior method has demonstrated this capability, and the paper explicitly acknowledges the unique challenges (forgetting in streaming methods like GRACE).
- **Strong empirical performance with robust ablation (Table 1, Table 3):** iReVa achieves the best average score across six baselines on zsRE-10K and PARAREL-10K on GPT2-XL. The ablation study systematically isolates each design component (activation function, max-pooling, ℒ_rec, ℒ_irr) and shows measurable degradation when any is removed, confirming each module's contribution.
- **Generalization across model scales and layers (Table 4, Figure 2):** iReVa maintains strong results on GPT2-Large, GPT-Neo-2.7B, and GPT-J-6B, and across layers 17–47 of GPT2-XL, unlike ROME/MEMIT which peak only in middle layers.
- **Reasonable parameter overhead (Section 6.3):** 0.08B parameters for 10K edits on a 1.5B model (~5.3%) with training time competitive to ROME and MEMIT, making the traceability feature practically usable.

## Weaknesses

### Fatal

- **Sign error in the irrelevance loss (Eq. 10, Section 4.2):** The loss is written as `ℒ_irr = −1/|D_out| Σ max(k̂ᵀ x_i − θ, 0)`. With `b > 0` in the total loss `ℒ = ℒ_edit + aℒ_rec + bℒ_irr`, minimizing ℒ would *encourage* activation on out-of-scope inputs (the gradient pushes k̂ toward x_i for activated out-of-scope inputs). The stated goal and the ablation results (Table 3: removing ℒ_irr *reduces* NS) both indicate the term is supposed to *discourage* out-of-scope activation. The implementation almost certainly uses the correct (positive) sign, but the equation as published would mislead any reader trying to reproduce the method from the paper alone. The authors must issue an unambiguous correction: was `−` a typo, and if so, state the correct form explicitly.

### Major

- **"Traceability" is demonstrated only through its most trivial consequence.** The paper's main novelty claim is "traceable model editing," but the only experiment on traceability is the withdrawal test (Table 2), which is a direct architectural consequence of storing per-edit columns — any slot-based method (e.g., an array of LoRA adaptors) would have this property. The paper does not show whether traceability enables any non-trivial capability: selective correction of a single edit among many, debugging of edit interference, interpretability of which edits conflict, or hierarchical composition. Without such evidence, the claim that iReVa offers "better interpretability and a stronger capacity for carrying traceable edits" remains an assertion rather than a demonstrated contribution.

- **Missing analysis of edit-order sensitivity.** Edits are applied sequentially while freezing prior adaptors. Distribution shift from earlier edits could affect the quality of later ones. The paper reports results for a single (unspecified) order but provides no analysis of variance across different edit orderings or whether early edits degrade late-edited performance. This is especially relevant for the 10K-edit setting where interference is likely to accumulate.

### Minor

- **Overstated claim about existing work (Section 2.2).** The paper says "none of [the existing methods] focuses on traceable model editing," but GRACE (Hartvigsen et al., 2023) explicitly stores per-edit parameters and supports removal. The paper later (Section 6.2) acknowledges GRACE but dismisses it on forgetting grounds. The initial claim should be qualified.
- **The reconstruction loss ℒ_rec (Eq. 9) penalizes the projection of the key difference onto the input i, not the difference itself.** If i is near-zero or orthogonal to (k̂⁰ − k̂), the loss is trivially satisfied without preserving the key distribution. The paper does not justify this design choice or ablate it against a direct difference penalty.
- **Hyperparameter reporting is incomplete.** The paper gives values for θ, α, a, b (Section 5.4) but does not describe how they were selected (e.g., held-out validation, grid search). The learning rate differs by model (5e−2 for GPT2-XL, 5e−3 for GPT-J-6B), and "gradient-free method" for GPT-Neo-2.7B is mentioned but not described, hurting reproducibility.
- **The value initialization (Section 4.1) is not ablated.** Initializing v̂ from the unembedding column of the target token is a heuristic; the paper provides no comparison to random or zero initialization, making it unclear how critical this choice is.
- **Parameter overhead for scalability.** 0.08B parameters for 10K edits is 5.3% of the 1.5B model (Section 6.3). The paper frames this as efficient but does not discuss how this overhead scales to 100K+ edits or whether it becomes a memory bottleneck.

### Trivial

- *None.* The paper is adequately structured and the presentation is generally clear.

## Nice-to-Haves

- Reporting variance (e.g., standard deviation across 3+ runs) for the main results in Table 1 would help gauge stability, though single-run evaluation is common practice in this literature.
- The "gradient-free" method for GPT-Neo-2.7B could be briefly explained even if deferred to an appendix.

## Removed Points

*(These points were flagged by reviewers but are excluded from the main evaluation for the reasons stated below.)*

- **Criticism about numerical tables missing from extracted text:** The tables are embedded as images — this is a PDF-parser artifact, not an author error. Remove per hard rule.
- **Criticism about missing Algorithm 1 / missing appendix content:** The parser strips appendices; these likely exist in the original submission. Remove per hard rule.
- **Criticism about confidence intervals not reported:** Single-run benchmarking is standard practice for large-model editing papers; demanding otherwise would be a scope mismatch. Weaken to nice-to-have.
- **"Section 6.1 claim about 'close to 100% ES without detriment to NS' is misleading":** The ablation shows the activation function trades off ES/PS for NS, but the paper's claim is about the end-to-end result of *iReVa as a whole*, not about the activation function being free. The reviewer conflates "the method's overall result" with "a component's cost." Remove.
- **Complexity-analysis complaint about "averaged length of target tokens":** The paper decomposes multi-token targets into multiple data pairs (Section 5.4); l as the average token count per target is consistent with this design. The reviewer's alternative interpretation is not more correct. Remove.

## Novel Insights

The reviews surface a tension the paper does not fully engage with: traceability (the ability to locate and withdraw edits) is a direct architectural property of any method that stores per-edit parameters in disjoint slots. The key question is not whether the method *can* withdraw — every slot-based method can — but whether this granularity enables something that shared-parameter methods *cannot* do at all. The paper's only answer is "withdrawal itself," which is a new evaluation capability but not a new *capability* in terms of what can be achieved with the edited model. This leaves the claimed "interpretability" undifferentiated from a simple hash-table-like mechanism. Future work should focus on demonstrating applications of traceability that go beyond withdrawal, such as compositional edits, selective rollback of individual edits without affecting others, or using the per-edit key structure for diagnosing knowledge conflicts.

## Suggestions

1. **Fix the sign in Eq. 10** and issue a clear statement about the correct formulation. This is the single most actionable fix — the equation as written cannot produce the reported results.
2. **Report edit-order variance.** Run the 10K-edit sequence with 3–5 random permutations and report mean ± std for ES/PS/NS. If the method is robust, this strengthens the paper; if not, it surfaces a meaningful limitation.
3. **Add at least one non-trivial traceability demonstration.** For example: (a) after 100 edits, withdraw a specific single edit and show that only its retrieved answer reverts while the other 99 remain corrected; (b) visualize the matching scores (K̂ᵀ i) for in-scope vs. out-of-scope inputs for a few edits to give the "interpretability" claim concrete grounding.
4. **Ablate the value initialization** (random vs. token-embedding vs. zero) and the reconstruction loss form (projection penalty vs. direct difference penalty) in a small-scale experiment (e.g., zsRE-1K) to justify the design choices quantitatively.
5. **Describe the "gradient-free" method** used for GPT-Neo-2.7B, even briefly, to ensure reproducibility.

## Score and Decision

The paper presents a clean architecture for traceable model editing with strong empirical results across multiple models. The fatal sign error in Eq. 10 is the most serious issue — it must be a typo given the ablation results, but as published it renders the formal description of the core objective incorrect. The major gap is that the traceability claim lacks non-trivial demonstration. These are remediable issues; the paper has genuine contributions (first withdrawal test, strong batch performance, clean design). However, in its current form, the sign error alone would prevent reliable reproduction, and the traceability claim is undersupported.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>