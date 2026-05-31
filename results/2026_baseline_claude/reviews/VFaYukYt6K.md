## Summary

The paper proposes a framework for robotics motion planning that trains a conditional trajectory autoencoder with a highly compressed, discrete, causally-ordered latent space, and then performs motion planning via greedy best-first search directly in this latent token space. The key idea is that with sufficient compression (as few as 3 tokens of dimension 3), arbitrary test-time objective functions can be optimized over a tiny discrete search space without training any additional neural networks. The framework is evaluated on the Waymo Open Motion Dataset (WOMD) for trajectory prediction, goal-conditioned planning, and multi-agent interaction modeling.

---

## Strengths

- **Elegant unification of learned priors and classical planning.** The core insight—that extreme compression shrinks the latent space enough for efficient tree search, eliminating the need to train a dedicated planner or diffusion model—is genuinely novel and cleanly motivated by parallel progress in image tokenization. The analogy to Lao Beyer et al. (2025) is well-placed and extends meaningfully to a continuous-state domain where composable objectives are arguably more impactful.

- **Adaptive soft quantization is practically novel.** Rather than using hard VQ (with its codebook collapse issues), the paper adaptively ramps noise injection to control reconstruction error. The feedback law (Eq. 2) is simple and ablated in Figure 2, where it demonstrably outperforms a fixed noise level. The theoretical connection to the capacity-achieving distribution of an amplitude-limited Gaussian channel (Smith, 1971) provides additional grounding.

- **Variable-length, causally-ordered tokens enable greedy search.** Using nested dropout + causal self-attention to produce a coarse-to-fine latent ordering is well-motivated and verified: Table 1 shows greedy search *outperforms* the learned encoder at all quantization levels for 1–2 tokens, which is a convincing proof-of-concept that the structure is indeed exploitable.

- **Flexibility across tasks from a single frozen autoencoder.** The same backbone handles motion prediction, left-turn planning, speed-profile optimization, multi-agent interaction, and scene-level language grounding (Table 4), all without retraining. The multi-agent experiment (Figure 6) is particularly compelling: optimizing a single pedestrian's goal position automatically yields consistent vehicle behavior from the joint decoder.

- **Behavior transfer demonstrates semantic token structure.** Section 3.1 shows that the *same* discrete token sequence, decoded in different environments, produces contextually consistent behaviors (e.g., a turn token is adapted to road geometry). This is a clean qualitative validation of the representation's quality.

---

## Weaknesses

### Fatal
None.

### Major

1. **No planning baselines in Table 3.** The paper's primary claimed contribution is flexible test-time planning, yet Table 3 compares only against "None (original scenario)"—essentially an all-zero baseline. There is no comparison to diffusion-based guided sampling, trajectory optimization, goal-conditioned prediction models, or any sampling-based method with similar flexibility. Without a competitive reference point, it is impossible to assess whether the 75.5% left-turn success rate and 0% edge contact are impressive or merely acceptable. A paper centered on planning flexibility must include at least one competing approach.

2. **Prediction performance is below state-of-the-art by a meaningful margin.** In Table 2, the method achieves minADE₆ = 0.6793 / minFDE₆ = 1.4291 (and 0.6416 / 1.3882 with the †-variant), which trails MTR (0.6050 / 1.2207) and DriveGPT (0.5240 / 1.0538). The paper correctly notes that prediction is not the primary goal, but the 6%–13% gap in ADE versus transformer baselines trained on the same data raises questions about the underlying model's capacity. Since the autoencoder is the foundation of all downstream tasks, its representational quality is relevant to all claims.

3. **No comparison to continuous-latent baselines for planning.** A natural question is whether a VAE with continuous tokens + gradient-based latent optimization (e.g., as in VQGAN-CLIP or loss-guided diffusion) would achieve comparable or better results with a less exotic training procedure. The soft-quantization/discrete-token design is motivated primarily by the need for discrete search, but the paper does not show this is strictly necessary versus continuous optimization for the specific planning objectives considered.

### Minor

1. **Greedy search's failure modes are not analyzed.** The causal coarse-to-fine structure enables greedy token selection, but objectives that are not monotonically refined by early tokens (e.g., "turn right only at the very end") could systematically mislead greedy selection. There is no ablation comparing greedy search to beam search or exhaustive search, so the cost of the greedy approximation remains uncharacterized.

2. **Multi-agent reconstruction results are incomplete in the main text.** Table 5 (multi-agent reconstruction numbers) is referenced in the text but not present in the extracted paper. The multi-agent planning discussion (Figure 6) is qualitative only, with no quantitative evaluation of interaction realism (e.g., collision rates, scene plausibility).

3. **Edge contact rate is a coarse safety proxy.** The planning experiments measure success rate and edge contact, but omit metrics for trajectory comfort (acceleration/jerk), agent-agent collision rates, or kinematic feasibility. These are standard in planning evaluation and would strengthen the claim of "feasible and realistic solutions."

### Trivial

- The assertion that the optimal input distribution of an amplitude-limited Gaussian channel is discrete is stated without proof or citation to the relevant theorem in information theory, which may confuse readers unfamiliar with Smith (1971).

---

## Nice-to-Haves

- Comparison with loss-guided diffusion (e.g., Bansal et al., 2023) on the same planning objectives in Table 3 would be the single highest-value addition.
- A beam-search variant or ablation on beam width to characterize greedy approximation quality.
- Quantitative multi-agent planning evaluation with scene-level feasibility metrics.

---

## Novel Insights

The central novel insight is that robotics trajectory planning is uniquely suited to the "compress-then-search" paradigm enabled by extreme autoencoder compression: unlike image generation where objectives are perceptual and hard to specify, robotics tasks come with natural, differentiable objectives (waypoint error, heading change, speed targets), meaning the gain from composable test-time objectives is directly actionable. The paper also demonstrates an underappreciated interaction between causal token ordering and the feasibility of greedy optimization—because the causal structure ensures that each successive token provides finer refinement around a structure already established by earlier tokens, a greedy strategy that might fail in an unordered latent space becomes near-optimal here (Table 1). This connection between token ordering, compression, and search tractability is the paper's most transferable conceptual contribution.

---

## Suggestions

- Add at least one planning baseline (e.g., autoregressive prediction model with importance sampling, or guided diffusion) to Table 3.
- Report beam search vs. greedy search ADE/success rate to quantify the greedy approximation gap.
- Include kinematic feasibility and agent-agent collision metrics for multi-agent experiments.
- Clarify in Section 3.3 how the six diverse samples for minADE₆ are generated (random token sampling? variance-based diversity?), as this detail is important for reproducibility.

---

## Score and Decision

The paper introduces a clean and practically motivated framework with a genuine contribution: adaptive soft quantization, causal variable-length tokenization, and greedy latent search compose into a system that demonstrably enables flexible, training-free test-time objective optimization in a realistic autonomous driving dataset. The behavior transfer and multi-agent results are compelling qualitatively. However, the absence of any planning baseline is a significant gap for a planning paper, and prediction performance lags behind competitive baselines. These issues are addressable but weigh against unconditional acceptance at this stage.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>