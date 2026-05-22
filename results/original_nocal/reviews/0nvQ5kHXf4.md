Now I have a comprehensive understanding of the paper and can verify the reviewer claims directly. Let me compose the final consolidated review.

---

## Summary

This paper introduces Weight-Activation Subspace Iteration (WASI), a method for jointly compressing both weights and activation maps into low-rank subspaces during transformer fine-tuning. The key insight is that the essential subspaces of both model parameters and activations remain stable across training iterations, enabling the reuse of subspace iteration in place of costly full SVD recomputation. WASI is evaluated on ViT, SwinT, and TinyLlama across multiple datasets, reporting up to 62× memory reduction at matching accuracy and a 1.4× wall-clock speedup on a Raspberry Pi 5.

---

## Strengths

1. **Joint weight-activation compression framework is novel and well-motivated.** Prior work compressed either weights (SVD-LLM) or activations (ASI) but not both. WASI is the first method to unify both into a single training framework, and the paper provides a clear motivation for why this is needed (memory bottlenecks from both sources during backpropagation).

2. **62× memory reduction with matching accuracy on SwinT is a concrete, measured improvement.** In Sec. 4.3 (Fig. 6), WASI at ε=0.9 matches vanilla accuracy across five datasets while cutting memory by up to 62× and FLOPs by 1.5× on SwinT. The experiment covers multiple datasets (CIFAR-10/100, CUB, Flowers, Pets) with consistent results, demonstrating robustness.

3. **Real hardware speedup of 1.4× on a Raspberry Pi 5 (Sec. 4.4, Fig. 8).** This is a genuine deployment-oriented evaluation showing wall-clock savings on actual edge hardware, not just simulated metrics. The improvement is consistent across all compression levels.

4. **Weight subspace stability is validated and exploited to avoid repeated SVD.** Sec. 4.2 (Fig. 3a) shows singular values remain nearly constant across 40 epochs. Fig. 3b then demonstrates that WSI (using subspace iteration) requires 1.36× fewer FLOPs than recomputing full SVD per iteration at matched accuracy, and at matched FLOPs achieves ~35% higher accuracy. This directly supports the paper's core hypothesis.

5. **Generality demonstrated across architectures (ViT, SwinT, TinyLlama).** The method extends beyond vision transformers to a decoder-only LLM, with orders-of-magnitude savings on TinyLlama (953× activation memory, 30× weight memory) without accuracy loss, showing the approach is not narrowly tailored to one architecture.

6. **Avoids LoRA adapter overhead unlike SVD-LLM.** As shown in Fig. 5, WASI achieves up to 100× better memory efficiency than SVD-LLM at matched accuracy because it does not require storing frozen weights plus adapters in memory simultaneously.

---

## Weaknesses

### Fatal

None.

### Major

1. **Ambiguous gradient update formulation in the main text (Eq. 11).** The weight update is written as `L_i R_i = L_i R_i + η · ∂L/∂W_i`. This notation does not clarify how gradients flow to the individual factors L_i and R_i. Standard backpropagation through a factorization requires computing `∂L/∂L_i` and `∂L/∂R_i` via the chain rule; the paper defers this to `f_LR` (defined in Appendix A.1), which was stripped by the parser. While the experimental results (convergence, good accuracy) strongly imply the implementation is correct, the main text as written is insufficient for a reader to verify the update rule or reproduce the method without the appendix. The authors should either state the update for L_i and R_i explicitly or clarify the notation as shorthand for a specific factor-update procedure.

2. **Headline resource-reduction claims are unqualified in the abstract.** The abstract claims "reducing memory usage by up to 62×" without noting that these savings are measured *only over compressed linear layers within MLP blocks*. Sec. 4.1 transparently states this scope ("focusing on linear layers within multi-perceptron blocks for fair comparison with previous methods") and references full-model results in Appendix B.3. The abstract does not carry this caveat, which could mislead readers about the practical savings when deploying WASI on a full transformer model where attention layers, embeddings, and normalization also consume memory. The 953× claim for TinyLlama is also explicitly scoped to "only the layers that are fine-tuned" (last 5 layers). These are *accounted for*, but the abstract's phrasing is over-broad.

### Minor

3. **Subspace stability validation is indirect.** The paper validates rank stability (Fig. 3a) and shows that WSI (which reuses subspace information) works well (Fig. 3b). However, the core claim is that the *subspace itself* (i.e., the span of the leading singular vectors) remains stable. No direct measurement of subspace similarity (e.g., principal angles between subspaces at consecutive iterations) is provided. The WSI vs. SVD comparison provides indirect evidence, but a direct metric would strengthen the theoretical motivation.

4. **On-device latency experiment lacks comparison to ASI.** The Raspberry Pi 5 experiment (Sec. 4.4) only compares WASI vs. vanilla training. ASI, which the paper identifies as the most directly comparable activation-compression baseline and which has itself been tested on a Raspberry Pi 5 (albeit on a compact convolutional model), is not included. Including ASI would isolate whether the added weight compression (WSI) provides additional real-world speedup beyond what activation compression alone achieves. Numerical per-iteration times and accuracy values for the Pi experiment are deferred to the appendix.

5. **TinyLlama experiment is limited in scope.** The experiment fine-tunes only the last 5 layers of TinyLlama, uses ε=0.1 (extremely aggressive compression), and BoolQ accuracy hovers around 64-66% (near random for a 2-class task with a 50% baseline, though the paper correctly shows WASI matching or slightly exceeding vanilla). These constraints limit how strongly the results support the generality claim for large language models.

### Trivial

None of substance — the paper is clearly written overall.

---

## Nice-to-Haves

- Include a direct measurement of subspace similarity (principal angles) between consecutive training iterations for a representative layer, to directly validate the subspace stability assumption.
- Add ASI to the Raspberry Pi latency comparison to isolate the benefit of weight compression in a deployment setting.
- Provide full-model resource accounting (including attention, embeddings, normalization) alongside the linear-layer-only numbers, to contextualize the headline savings.
- Include numerical tables for the main figures rather than relying solely on line plots (the plots are dense and numerical values would aid verification).

---

## Removed Points

The following points from the reviews were evaluated and removed:

1. **"The SVD-LLM comparison in Fig. 6 is unfair"** — Factually incorrect. Fig. 6 (SwinT) compares *only WASI vs. vanilla training*, not SVD-LLM. SVD-LLM appears only in Fig. 5 (ViT on CIFAR-10). ViT has 3D activation maps, and the paper notes SVD-LLM is inapplicable *only* to models with "four or more dimensions." The ViT comparison is valid and the critique misreads the paper.

2. **"The gradient update is mathematically incorrect / fatal"** — Overstatement. The notation in Eq. 11 is ambiguous but the method demonstrably converges and matches/beats vanilla accuracy across multiple experiments, confirming the implementation is correct. Details are deferred to Appendix A.1 (stripped by parser). This is a presentation clarity issue, not a fatal methodological error.

3. **"Missing related works"** — Removed per policy (cannot be verified without external sources).

4. **"Formatting/style nitpicks"** and **"typos/grammar complaints"** — Removed per policy; these are parser artifacts, not author errors.

5. **"Reproducibility concerns about missing appendix / proofs"** — Removed per policy; the appendix was stripped by the parser and exists in the original submission.

6. **"The comparison is apples-to-oranges" (SVD-LLM on ViT)** — Removed as discussed above; ViT has 3D activations and SVD-LLM is applicable.

7. **Strength finder's generic strengths** about "problem importance" — Removed as generic; only concrete, evidence-backed strengths are retained.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation about the method or results that the paper itself does not articulate.

---

## Suggestions

1. **Rewrite Eq. 11 with explicit factor updates.** State the update rules for L_i and R_i directly (or clarify the notation, e.g., "the product L_i R_i is treated as a single variable and updated, after which factors can be recovered via SVD or re-factorization"). This resolves the ambiguity without requiring the (stripped) appendix.

2. **Qualify the abstract's memory claims.** Add a brief scope caveat (e.g., "for compressed linear layers under an explained-variance threshold") to the 62× claim.

3. **Add a numerical table** for the main resource-accuracy results (Figs. 5, 6) so readers can verify the exact memory/accuracy trade-offs without estimating from line plots.

4. **Include ASI in the Raspberry Pi experiment** to demonstrate that the weight component of WASI provides additive real-world benefit beyond activation compression alone.

---

## Score and Decision

The paper proposes a technically sound and practically motivated method for joint weight-activation compression during transformer fine-tuning. The experiments are reasonably extensive (three architectures, five datasets, real hardware deployment) and the results are consistently positive. The main weaknesses are presentation clarity (the ambiguous Eq. 11 in the main text) and some overclaiming in the abstract, neither of which undermines the core contribution. The SVD-LLM comparison concerns raised by the harsh critic are largely based on misreading the paper.

**Overall assessment:** This is a solid contribution with clear empirical support, suitable for acceptance.

**MY FINAL SCORE:** <score>7.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>