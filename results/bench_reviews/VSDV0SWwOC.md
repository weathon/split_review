Now I have a thorough understanding of the paper and calibration anchors. Let me write the final review.

## Summary

LS-Merge proposes a framework for merging language models in a learned latent weight space rather than in raw parameter space. The method trains a transformer-based VAE on LLM weights, encodes models into a shared latent manifold, optionally aligns heterogeneous latent distributions via closed-form optimal transport, performs merging operations in latent space, and decodes back to weights. The paper demonstrates consistent improvements over weight-space baselines on LoRA expert merging, competitive performance against representation-merging methods, and—most distinctively—enables cross-architecture (different model families) merging for the first time.

## Strengths

- **Novel paradigm for model merging.** Shifting merging from weight space to a learned latent space is a creative and well-motivated idea. The pipeline (encode → align → merge → decode) is conceptually clean and generalizes beyond architectural homogeneity—a genuine advance over prior work that uniformly requires matching architectures.

- **Principled motivation from weight statistics.** The analysis of LLM weight distributions (Table 1, Figure 2) showing heavy tails (kurtosis up to ~15) and low-rank structure provides a non-trivial empirical foundation for the VAE design choices. This analysis distinguishes the work from prior approaches that assume Gaussian weight distributions.

- **Strong LoRA expert merging results.** Table 3 shows LS-Merge substantially outperforming weight-space baselines (Uniform Soup, SLERP, Greedy Soup, DARE-TIES) across 8 benchmarks, e.g., MMLU 56.0 vs. best baseline 52.5, HellaSwag 60.1 vs. 54.6. The gains are consistent and large.

- **Convincing ablation establishing non-linear manifold necessity.** Table 8's PCA vs. VAE comparison is well-executed: PCA collapses to near-random accuracy (MMLU ~25%) even at mild compression, while the VAE preserves functional performance, demonstrating that pretrained weights reside on a genuinely non-linear manifold requiring expressive encoding.

- **Enables cross-family merging where weight-space methods cannot operate at all.** Table 5 shows OT-aligned latent interpolation (LLaMA→Gemma) improves over the target base on all three benchmarks (e.g., WinoGrande 56.83→57.75). While gains are modest, the capability itself is previously unavailable, and the OT-only ablation shows that alignment is crucial.

## Weaknesses

### Fatal

None.

### Major

- **Asymmetric comparison with weight-space baselines.** The VAE used for LS-Merge is trained on model weights that include the very LoRA experts being merged (line 515-516: "Training data consist of pretrained weight snapshots for Gemma-3-1B-it and Gemma-3-4B-it, plus LoRA experts from Feng et al. (2024b)"), while weight-space baselines are zero-shot merge operators with no auxiliary training. This means LS-Merge has an information advantage: it has effectively meta-learned the weight manifold of the models it merges. The claim that latent-space merging "consistently outperforms all weight-space baselines" (line 587) is therefore not a clean evaluation of latent-space *merging* per se, but of a system that includes manifold meta-learning. The paper would benefit from a VAE trained on a *disjoint* set of checkpoints to isolate the benefit of the latent representation from the benefit of training on the to-be-merged models. This does not invalidate the contribution—the VAE's ability to learn a useful weight manifold is itself part of the contribution—but the headline claim overstates what the experiment demonstrates.

- **Cross-architecture merging gains are modest and under-evaluated.** The cross-family experiment (Table 5, LLaMA→Gemma) reports improvements of 0.6–1.0 percentage points across only three benchmarks (WinoGrande, ARC-C, HellaSwag), with a single λ=0.1. The paper claims this "enables robust cross-scale and cross-family model merging for the first time" (line 888), but the evidence for "robust" is thin: the evaluation task set is small, no comparison against simple heterogeneous baselines (e.g., learned linear projection for dimensionality matching in weight space, adapter-based transfer) is provided, and the gains, while real, are near the noise floor for single-model evaluation. The contribution is genuine—it works where weight-space methods cannot—but the strength of the claim should be tempered to match the evidence.

### Minor

- **Self-merging protocol is underspecified.** Section 4.1 describes encoding a model, sampling multiple latent codes from its posterior, merging them, and decoding. However, the number of codes sampled, the weighting scheme for merging them (equal weights? learned?), and whether posterior sampling vs. prior sampling is used in practice are not specified. The general approach is described (line 383-387), making this a reproducibility gap rather than a conceptual flaw, but it prevents independent validation of one of the paper's stated contributions.

- **Gaussian OT assumption is unverified.** The closed-form OT alignment (Section 3.3) assumes per-layer latent distributions are approximately Gaussian. The paper provides no empirical validation of this assumption (e.g., normality tests on encoded latents, Wasserstein distances before/after alignment). Given that the weight distributions themselves are heavy-tailed and non-Gaussian (Section 3.1), and the encoder is non-linear, it is non-obvious that encoded latents become Gaussian. This is a methodological gap but does not undermine the results, since the OT alignment demonstrably works in practice.

- **Claim about transformer speed advantage is unsubstantiated.** Section 3.2 states the transformer VAE is "faster than convolutional alternatives at a comparable parameter count" without benchmarking or citation. This is a minor overstatement.

- **Limited evaluation scales.** All experiments use models ≤7B parameters, with most at 1-4B. The method's scalability to larger models (≥13B) is untested, and the compression fragility above r=1.6 (Table 7) raises questions about practical deployment at scale.

### Trivial

- Different evaluation frameworks are used across tables (Feng et al. code for Tables 2-3, lm-eval for Tables 4-5). The paper acknowledges this (lines 599, 663), but it complicates cross-table comparison.

## Nice-to-Haves

- A cost-benefit analysis quantifying VAE training cost vs. merging performance gains would help practitioners assess whether the upfront investment is worthwhile for their use case.
- Visualization of latent spaces before/after OT alignment (beyond t-SNE) would strengthen intuition about what the alignment accomplishes geometrically.
- Instance-level case studies showing where merged models succeed or fail compared to baselines would add qualitative insight beyond aggregate scores.

## Removed Points

These points from the reviewer inputs were flagged and removed after verification against the paper:

1. **"LS-Merge uses a VAE trained on the weights of the specific experts being merged... This gives LS-Merge an asymmetric advantage."** — PARTIALLY KEPT. The core concern about asymmetric comparison is valid and retained as a Major weakness, but the harsh critic's framing that this "invalidates the central empirical comparison" overstates the case. The VAE is trained for weight reconstruction, not merging optimization; the contribution is precisely that learning a weight manifold enables better merging. The comparison is asymmetric but informative—it shows what is possible when one invests in learning the weight manifold. Retained but recalibrated from "fatal" to "major."

2. **"Cross-architecture merging gains are weak... No statistical significance is reported... does not compare against simple baselines for heterogeneous merging."** — PARTIALLY KEPT. The modest gains and limited evaluation are valid minor concerns. The demand for statistical significance is appropriate for some fields but is non-standard in LLM benchmark evaluation where single-run scores are the norm—moved to nice-to-have. The demand for heterogeneous weight-space baselines is scope creep: the paper's contribution is enabling something previously impossible; comparing against hypothetical alternatives is unreasonable.

3. **"Self-merging protocol is underspecified... how many codes are sampled... omitted."** — KEPT as minor. The paper does describe the general approach (posterior sampling, linear interpolation) but lacks specific parameter counts. This is a real but addressable gap.

4. **"The VAE design does not incorporate any explicit mechanism to preserve heavy-tailed extremes."** — REMOVED. The two-stage curriculum (deterministic AE → VAE) is explicitly motivated by and designed to address the heavy-tailed training instability (line 371-376). The harsh critic demands a "tail-specific" mechanism when the curriculum is precisely that.

5. **"The theoretical discussion about manifold dimensionality... remains decorative."** — REMOVED. The Eckart-Young/manifold embedding discussion (lines 169-181) provides theoretical motivation for why compression should be possible, which directly justifies the VAE approach. Calling it "decorative" is a strawman.

6. **"The mismatch between the claimed non-linear manifold and the linear OT alignment raises a tension."** — REMOVED as a separate weakness but the unverified Gaussian assumption concern is retained. The OT alignment operates on latent distributions, not on the weight manifold directly; the encoder maps the non-linear weight manifold to a (hopefully) well-behaved latent space where linear OT is appropriate. The tension the harsh critic identifies dissolves once this distinction is recognized.

7. **"Inconsistent evaluation protocols across tables."** — KEPT as trivial. The paper is transparent about this.

8. **"The conclusion recapitulates overstated claims about enabling cross-family merging."** — KEPT as a major weakness (the claim is somewhat overstated relative to the evidence).

9. **Strength Finder: "Enables heterogeneous model merging, a previously unsolved challenge."** — KEPT as a core strength with appropriate caveats about the evidence strength.

10. **Strength Finder: "Consistent and significant performance gains across multiple merging scenarios."** — KEPT. Supported by Tables 2-4.

11. **Strength Finder: "Empirically grounded analysis of LLM weight statistics justifies the VAE design."** — KEPT. Supported by Table 1 and surrounding analysis.

12. **Harsh Critic: "The framing overstates the ability to relax the requirement for multiple source models."** — REMOVED. The paper is clear that self-merging requires training a generative model (Section 1, point (i): "A generative model can learn the latent manifold of a single LLM parameters"). This is not overclaimed; it's presented as a capability enabled by the framework.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface methodological insights that the paper itself does not already articulate.

## Suggestions

1. Train a VAE on a disjoint set of model checkpoints (e.g., train on Gemma-3-1B/4B, evaluate expert merging on Llama-based LoRA experts) to cleanly separate manifold learning benefits from in-distribution encoding quality. This would directly address the major weakness about asymmetric comparison.

2. Expand cross-architecture evaluation to more benchmarks (at least 5-6 standard tasks) and report whether the merged model outperforms *either* source model, not just the target base. Consider simple heterogeneous baselines like zero-padded weight-space interpolation as sanity checks.

3. Specify the self-merging protocol precisely: number of posterior samples, weighting scheme, and provide a control (e.g., VAE reconstruction from a single sample, or weight-noise injection baseline) to distinguish variance reduction from genuine manifold traversal.

4. Validate the Gaussian assumption for OT alignment with normality diagnostics on encoded latents, and report transport quality metrics (e.g., 2-Wasserstein distance before/after alignment).

## Score and Decision

**Anchor comparisons:**

| Anchor | Avg Score | Decision | Comparison |
|--------|-----------|----------|------------|
| `ocEoHCrezd` (Latent Merging) | 2.50 | Reject | Also proposes latent-space merging but in hidden-representation space. Had fundamental evaluation problems (no proper benchmarks, missing baselines). LS-Merge is substantially stronger: proper benchmarks, multiple merging scenarios, novel cross-architecture capability. |
| `Awf3ebMpKw` (Expert Merging) | 5.00 | Accept (Poster) | A solid model merging paper that learns coefficients for existing methods. LS-Merge is comparably strong: more novel core idea (latent weight encoding), similar experimental thoroughness, but has the asymmetric comparison issue that Expert Merging does not. |
| `vpKXTmMtBQ` (Merging Scaling Laws) | 5.50 | Reject | Strong empirical contribution with 10K+ experiments. LS-Merge has a more creative core idea but weaker empirical scale. Roughly comparable overall contribution level. |
| `HZ0YvjVzpj` (Mixup Model Merge) | 3.50 | Reject | A simple interpolation variant. LS-Merge is clearly more novel and substantial. |
| `ULxerRB2DF` (OTA Merging) | 6.00 | Reject | Curvature-aware merging, stronger theoretical grounding. LS-Merge has a more novel paradigm but less theoretical rigor. |
| `NYUxN6plEh` (Learn to Merge) | 4.50 | Reject | Meta-learning for merging coefficients. LS-Merge targets a more ambitious problem (heterogeneous merging) with a more creative solution. |
| `S0MRfeGr5d` (StatsMerging) | 4.00 | Reject | Statistics-guided merging. LS-Merge goes further in enabling heterogeneous merging and has a more novel architectural contribution. |

LS-Merge is a creative and well-motivated contribution with genuine novelty. The core idea—encoding weights into a latent space for merging—opens interesting directions. The experiments demonstrate clear benefits on homogeneous merging and establish the feasibility of cross-architecture merging. The main weaknesses are the asymmetric comparison with weight-space baselines (a real but not fatal concern, since the VAE training is the method's contribution, not a confound) and the modest cross-architecture evidence. These are addressable concerns that do not undermine the paper's core contributions.

Compared to anchors: stronger than the 2.50-4.50 range papers, comparable to Expert Merging (5.00, accepted) but with a more novel paradigm and the cross-architecture contribution, somewhat weaker empirically than the Scaling Laws paper (5.50, rejected for different reasons). A score of **5.5** is appropriate.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>