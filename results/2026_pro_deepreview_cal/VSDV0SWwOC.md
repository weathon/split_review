Now I have enough calibration data. Let me synthesize the final review.

**Calibration summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Few-shot Style-Conditioned VAE (kVcEiWtld9) | 4.25 | R1 | LS-Merge is clearly stronger — more comprehensive experiments, principled OT alignment, broader scope |
| Foldable SuperNets (LJGY2GVcit) | 5.50 | R1 | Similar ambition but LS-Merge's VAE approach is more novel; LS-Merge has better ablation depth |
| WIDEN (2pvMZKGYDR) | 5.67 | R1 | LS-Merge has broader scope (cross-architecture), more diverse experiments |
| Realistic Evaluation of Merging (Bq3fEAGXUL) | 5.33 | R2 | Different type (evaluation paper), LS-Merge makes a stronger methodological contribution |
| What Matters for Merging at Scale (fvUVe2gJh0) | 5.33 | R2 | Different type (evaluation), LS-Merge is more method-focused |
| Submodule Linearity (irPcM6X5FV) | 6.00 | R2 | LS-Merge has more novel approach, broader experiments, but Submodule Linearity has cleaner story |
| Parameters Fusing (vqbd2OQnGp) | 6.50 | R2 | Most comparable — both have novel ideas with solid but imperfect validation; LS-Merge has more thorough experiments |
| MAP (1v7SRWsYve) | 6.33 | R2 | LS-Merge is comparable in quality, more ambitious in scope |
| LLM Augmented LLMs (jjA4O1vJRz) | 6.50 | R2 | LS-Merge is comparable, different approach to composition |

**Bracket: 5.5–7.0 → narrowed to 6.0–6.5.** LS-Merge is most comparable to Parameters Fusing (6.50) and Submodule Linearity (6.00), sitting between them. I'll score it **6.5**, as its experimental thoroughness and methodological novelty slightly exceed the 6.00 anchor, while matching the ambition level of the 6.50 anchor.

Now let me write the review carefully, filtering the harsh critic's points.## Summary

LS-Merge proposes encoding LLM weights into a learned latent space via a transformer-based VAE, performing model merging (interpolation, soup-style operations) in that latent space, and decoding back to weights. The framework supports both homogeneous merging and, via proportional dimensionality matching and optimal-transport alignment, heterogeneous merging across architectures. The paper also demonstrates self-merging (sampling and combining multiple latents from a single model) and evaluates on Gemma and LLaMA families across multiple benchmarks.

## Strengths

- **Compelling PCA vs. VAE ablation that justifies the entire approach.** Table 8 shows that PCA-reconstructed models collapse to near-random accuracy on MMLU (~25.5%) even at mild compression (r=1.6×), while the Transformer-VAE preserves ~96% of original accuracy even at r=4×. This is strong evidence that pretrained weights lie on a non-linear manifold, making linear subspace methods insufficient and directly validating the core design choice.

- **Latent-space expert merging consistently outperforms weight-space baselines.** Table 3 shows LS-Merge (both linear interpolation and soup variants) beating Uniform Soup, SLERP, Greedy Soup, Dare-Ties, and data-level merging across eight diverse benchmarks (MMLU, MMLU-pro, HellaSwag, GSM8k, TruthfulQA, NLQGraph, Knowledge Crosswords, AbstainQA). Gains are non-trivial — e.g., LS-Merge(soup) achieves 56.0 MMLU vs. 50.8 for the best weight-space baseline (Greedy Soup).

- **Weight-statistics analysis provides genuine empirical grounding for encoder design.** Table 1 documents extreme kurtosis (up to ~15) in self-attention layers with near-zero means and low variance, characterizing LLM weights as leptokurtic with heavy tails. This is a concrete finding that informs the choice of a VAE over Gaussian-assuming alternatives and the need for tail-aware training.

- **Layer-type ablation reveals complementary functional knowledge.** Table 6 shows merging MLP layers alone gives modest gains, merging attention alone degrades performance, but merging both jointly achieves the best results, indicating that the method preserves cross-layer co-adaptations rather than disrupting them.

- **Successful heterogeneous merging enabled by OT alignment.** Figure 4 and Table 5 show that OT-aligned latent interpolation (LLaMA→Gemma cross-family, and Gemma 4B→1B intra-family) produces improvements over the target base model, while unaligned mixing degrades performance. The finding that matching dimensionality alone is insufficient — distributional alignment is necessary — is an insight with practical value.

## Weaknesses

### Fatal
None.

### Major

- **Layer-index pairing for heterogeneous merging is under-justified.** Algorithm 1 pairs layers by index position (line 1: `N ← min(|L_src|, |L_tgt|)` and defines pairs `(l_src^(j), l_tgt^(j))`), which assumes a functional correspondence between, say, layer 5 of LLaMA and layer 5 of Gemma. For cross-family merging (LLaMA ↔ Gemma), this assumption is almost certainly wrong — the architectures have different attention mechanisms, different numbers of layers, and different layer roles. The paper drops all layers beyond the minimum depth, truncating the deeper model's later layers entirely. Without a principled mapping or evidence that index-based pairing preserves meaningful functional correspondences, the claim of "heterogeneous merging" is weakened. The proportional mapping in Section 3.3 handles width/depth ratio adjustment but does not address the semantic mismatch of layer indices.

- **Cross-architecture evidence is thin for the strength of the claim.** The conclusion states LS-Merge "enables robust cross-scale and cross-family model merging for the first time," but the evidence is limited to three benchmarks (WinoGrande, ARC-C, HellaSwag) with modest absolute gains (e.g., HellaSwag 49.07→50.10, ARC-C 42.78→43.34 in Table 5). No error bars or statistical significance are reported for these specific experiments. The experiments use only small models (1B–4B parameters). While the OT+interpolation does consistently beat the base model and the no-OT variant, the improvements are in the 1–2 point range, which makes the "robust" descriptor an overstatement given the limited evaluation scope.

### Minor

- **Self-merging gains may conflate latent exploration with ensemble effects.** Table 2 shows LS-Merge self-merging improves over both the base model and VAE reconstruction. However, the method samples multiple latent codes and merges them, which is analogous to an ensemble. No control (e.g., encoding/decoding multiple times and averaging the resulting *weights*, rather than latents) is provided to disentangle whether the benefit comes from latent-manifold exploration or from a simple averaging regularization effect.

- **Scalability claims are asserted without evidence.** The abstract and conclusion describe LS-Merge as "scalable," but the largest model in cross-architecture experiments is 4B parameters, and no computational cost, memory, or training-time analysis is provided. The heaviest homogeneous experiment uses Llama-2-13B, but only in a same-architecture comparison (Table 4), not testing cross-architecture at that scale. The VAE training is done on 1B–4B checkpoints.

- **Gaussian OT assumption is not validated against the data.** The OT alignment (Equation 2) is solved under a closed-form Gaussian approximation using empirical mean and covariance per layer's latent distribution. However, Section 3.1 shows the weight distributions are heavy-tailed and non-Gaussian. The paper does not test whether the latent distributions (after VAE encoding) are actually well-approximated by Gaussians, nor does it ablate the Gaussian OT against non-parametric OT. If the latent distributions are also heavy-tailed, the Gaussian OT map may be suboptimal.

### Trivial

- The paper uses "scalable" in the abstract without the analysis to support it — this is an overclaim in phrasing rather than a technical flaw.

## Nice-to-Haves

- An ablation comparing the two-stage curriculum (deterministic pretraining → KL fine-tuning) against a standard β-VAE trained end-to-end would strengthen the claim that the curriculum specifically helps with heavy-tailed weight distributions.
- A computational cost table (VAE training time, encoding/decoding latency, memory) for the models used would ground the scalability discussion.
- More benchmarks for the cross-architecture experiments would increase confidence in the generalizability of the heterogeneous merging results.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic: "The 'proportional mapping' step (line 4) is never explained—no equation, no architectural detail, and no training procedure are given."** — REMOVED. The proportional mapping IS explained in Section 3.3: the equation `r = n_t N / (n_s M)` and the statement "This proportional alignment across depth and width standardizes each architecture to a common per-layer latent dimensionality." The harsh critic was factually incorrect.

- **Harsh critic: "no training procedure are given"** — REMOVED. Section 3.2 describes the two-stage curriculum (deterministic autoencoder → KL fine-tuning), the β-VAE objective (Equation 1), and the optimizer (AdamW with lr=1e-4, weight decay=1e-5, cosine-to-zero schedule).

- **Harsh critic: "The algorithm discards all layers beyond min(|L_src|, |L_tgt|)"** — KEPT but recharacterized. This is a real concern about layer-index pairing (see Major weakness 1), but the harsh critic's framing as making the method "irreproducible" is overblown — the algorithm is clear even if the assumption is questionable.

- **Harsh critic: "There is no ablation showing that the transformer-based encoder or the curriculum actually improves tail preservation compared to a simpler VAE"** — MOVED to Nice-to-Haves. This is a reasonable ablation request but does not undermine the core contribution; the PCA vs VAE ablation already demonstrates that non-linear encoding is necessary.

- **Harsh critic: "The experiment does not rule out that the method is merely adding a small structured perturbation"** — REMOVED as speculative. The paper does compare OT+interpolation against OT-only and no-OT baselines, and the consistent improvement pattern (Figure 4, Table 5) argues against pure noise.

- **Harsh critic: "no experiment disentangles whether the benefit comes from exploring the latent manifold or from a regularization effect of averaging multiple decoded weights"** — KEPT as Minor weakness. This is a valid control that is missing.

- **Harsh critic: "A fairer comparison would be to ensemble weight-space checkpoints in a similar fashion"** — KEPT within the Minor weakness about self-merging ensemble effects, but the expert-merging setting is different (each expert is distinct, not multiple samples of the same model), so this criticism applies less there.

- **Strength Finder: "Rigorous weight-statistics analysis that informs encoder design"** — KEPT as a strength. The analysis is genuine and well-documented.

- **Strength Finder: "Two-stage curriculum stabilizes VAE training on heavy-tailed weights"** — WEAKENED. The paper describes this but does not ablate it against alternatives. Included as a Nice-to-Have rather than a standalone strength.

- **Strength Finder: "Zero-shot generalization to unseen architectures"** — KEPT as a supporting observation but noted that performance degrades at higher compression ratios (Table 7), which the paper itself acknowledges.

## Novel Insights

The paper's finding that matching latent dimensionality is insufficient for heterogeneous merging — distributional alignment via OT is necessary — is a genuinely useful insight for future work in weight-space learning. The PCA vs VAE comparison (Table 8) also provides a clear, actionable lesson: linear subspace methods fundamentally cannot capture the functional weight manifold of pretrained LLMs, even at mild compression. This justifies the computational cost of non-linear encoders in a concrete, measurable way.

## Suggestions

- Provide a more principled layer-correspondence method for cross-architecture merging. Even a simple functional similarity metric (e.g., CKA between layer outputs on a small calibration set) would be a significant improvement over index-based pairing.
- Add error bars or confidence intervals to the cross-architecture results (Table 5, Figure 4) to allow readers to assess the reliability of the modest observed gains.
- Include a weight-space ensemble baseline for self-merging (e.g., encode/decode N times and average the decoded weights) to isolate the contribution of latent-space exploration.

## Score and Decision

**Originality:** High. The idea of moving model merging into a learned latent space, particularly with OT alignment for heterogeneous architectures, is genuinely novel in the LLM merging literature.

**Importance:** The problem is well-motivated — architectural homogeneity is a real bottleneck for model merging. The framework opens a new direction.

**Claims supported:** The core claims about latent-space merging outperforming weight-space baselines for homogeneous expert fusion are well-supported. The cross-architecture claims are partially supported but overclaimed given the modest evidence and limited benchmarks.

**Soundness:** The methodology is generally sound, with the PCA vs VAE ablation being particularly convincing. The main concern is the layer-index pairing in heterogeneous merging and the Gaussian OT assumption.

**Clarity:** The paper is well-structured and the framework is clearly explained, though some technical details (e.g., the exact chunking and token-downsampling mechanics) could be more precise.

**Value to community:** High. LS-Merge opens a new paradigm for model merging that could be extended by future work. The weight-statistics analysis and PCA comparison provide useful reference points.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>