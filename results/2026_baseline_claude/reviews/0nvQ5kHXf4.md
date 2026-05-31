## Summary

WASI (Weight-Activation Subspace Iteration) is a method for efficient on-device fine-tuning of transformer models that simultaneously compresses weight matrices and activation maps into stable low-rank subspaces. Building on the observation that a model's essential parameter information lies in a fixed low-dimensional subspace throughout fine-tuning, WASI applies SVD once at initialization and then uses subspace iteration at subsequent steps to cheaply maintain approximate low-rank representations of both weights and activations. Experiments on ViT, SwinT, and TinyLlama claim up to 62× training memory reduction and ∼1.4× wall-clock speedup on a Raspberry Pi 5, with accuracy competitive to vanilla training.

---

## Strengths

- **Practically meaningful problem with hardware grounding.** The paper targets on-device fine-tuning of transformers—a genuinely under-explored but increasingly important setting. Validating on a Raspberry Pi 5 with real wall-clock measurements (Fig. 8) adds credibility beyond simulation experiments and is more rigorous than most memory/FLOPs-only analyses in comparable work.

- **Principled unification of weight and activation compression.** Prior closely related work (ASI, Nguyen et al. 2025) compresses only activations; weight compression was left to a separate family of methods (SVD-LLM) that cannot be applied to vision transformers with 3D activations. WASI is the first to combine both under a single coherent subspace-stability hypothesis, and the empirical gains from combining the two (Fig. 5: WASI Pareto-dominates ASI in FLOPs at equivalent accuracy) validate this design choice.

- **Subspace stability is empirically confirmed, not assumed.** Fig. 3a shows singular-value heatmaps across all epochs, demonstrating the rank K_i is essentially constant after the first epoch. This directly supports the design choice to compute SVD once and rely on cheap subspace iteration thereafter, and WSI is shown to need 1.36× fewer FLOPs than repeated full-SVD for the same accuracy (Fig. 3b).

- **Coverage across architectures and datasets.** SwinT results span five downstream datasets (CIFAR-10/100, CUB, Flowers, Pets); a TinyLlama / BoolQ experiment shows the method generalises from vision to decoder-only LLMs; extended results in appendices cover ViT on additional datasets and attention layers.

---

## Weaknesses

### Fatal
None.

### Major

1. **Weight update rule is technically underdefined.** Equation (11) states the update is applied directly to the product $L_i R_i$, not to the individual factors. A gradient $\partial\mathcal{L}/\partial\mathcal{W}_i$ that has rank $K_i$ added to $L_i R_i$ yields a matrix of rank up to $2K_i$, breaking the low-rank structure. The paper does not explain how the low-rank factorization is re-enforced after each gradient step—whether the product is re-projected, or whether only $R_i$ is updated while $L_i$ is kept fixed (as suggested by Algorithm 1 line 6, where $R_{i(t)}^T = \mathcal{W}_{i(t)}^T \cdot L_{i(t-1)}$). This ambiguity makes the algorithm not fully reproducible from the main text and raises a correctness concern that should be resolved.

2. **TinyLlama experiment is too restricted to support the claimed generality.** Only the last 5 layers are fine-tuned, the compression parameter $\varepsilon$ is set to the extremely aggressive value of 0.1, and the accuracy window spans a mere 2 percentage points (64–66%). The claim "WASI outperforms vanilla without accuracy loss" at activation memory reductions of 953.86× is difficult to interpret when the baseline accuracy is essentially unchanged across that narrow window. A larger fine-tuning scope and sweep over $\varepsilon$ values comparable to the ViT/SwinT experiments would be necessary to substantiate LLM generality.

3. **Memory numbers are reported only for MLP blocks.** Section 4.1 explicitly states that comparisons focus on "linear layers within multi-perceptron blocks for fair comparison with previous methods." Attention layers (query/key/value projections and their activations) often dominate memory in practice. The appendix contains extended results, but the main paper's headline numbers (e.g., 62× reduction) therefore represent partial model compression, which is not made sufficiently prominent in the abstract or conclusion.

### Minor

1. Results are primarily presented as Pareto curves (accuracy vs. memory/FLOPs) rather than tables, making it difficult to extract precise numbers at matched compression ratios. The 62× memory reduction is mentioned in the text, but the corresponding accuracy at that operating point is not stated explicitly; the reader must infer it from a figure.

2. The dynamic-programming rank-selection scheme (contribution listed in Sec. 3.3) is deferred entirely to the appendix with no sketch in the main body, making it hard to assess its novelty and correctness.

### Trivial
- The sentence "as shown in Eq. 3, truncating…" appears to reference a backpropagation formula rather than an approximation error bound; the logical link is valid but the phrasing is slightly loose.

---

## Nice-to-Haves

- A clear end-to-end memory profile including attention layers would quantify the realistic on-device footprint reduction for a complete transformer.
- An ablation isolating WSI vs. ASI contributions per dataset/architecture would strengthen the claim that the weight-compression component provides additive benefit beyond ASI alone.
- A broader LLM experiment (more layers, multiple $\varepsilon$ values, comparison vs. LoRA as a PEFT baseline) would better justify the LLM generality claim.

---

## Novel Insights

The most genuinely novel insight is the joint exploitation of subspace stability in *both* weights and activations simultaneously, enabling a unified framework in which the model is smaller both to train (activation memory and weight gradient memory) and to deploy (inference FLOPs reduced via the compressed weight matrices). Prior work had treated these as separate optimization targets. The empirical confirmation (Fig. 3a) that layer ranks are nearly constant throughout fine-tuning—enabling subspace iteration to substitute for repeated full SVD—strengthens the theoretical grounding. The extension of Tucker/ASI-style decomposition to 3D activation tensors arising in transformer attention blocks is a non-trivial engineering contribution that unlocks this family of methods for the transformer regime.

---

## Suggestions

- Clearly state in the main text (Sec. 3.3 or after Eq. 11) how $L_i$ and $R_i$ are individually updated and how the low-rank structure is maintained across gradient steps, referencing Algorithm 1 for the subspace-iteration step.
- Add a compact table reporting accuracy ± std, training memory (MB), and inference FLOPs at three representative $\varepsilon$ values for each model/dataset combination, to complement the Pareto curves.
- Report end-to-end (full model) memory figures alongside the MLP-only figures so practitioners can assess real deployment feasibility.
- Scale the TinyLlama experiment to fine-tune more layers and use a range of $\varepsilon$ values consistent with the vision experiments.

---

## Score and Decision

The paper addresses a practically relevant problem, provides strong empirical results on real hardware across multiple architectures and datasets, and unifies weight and activation compression in a principled way. The main technical concern is the underspecified weight update rule, which could mask a subtle correctness issue or simply require clarification. The TinyLlama results are insufficiently developed to support broad LLM claims. These are significant but not fatal issues; the core contributions for vision transformers are solid and the hardware results are genuine.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Borderline Accept</decision>