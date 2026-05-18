Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

The paper proposes a structured initialization for Vision Transformer (ViT) attention maps, where the attention maps of each head are initialized as random impulse convolution filters. The method is motivated by a theoretical analysis of ConvMixer (Proposition 1), which shows that random spatial filters can work well when only channel-mixing weights are learned, provided a rank-deficiency condition on the input. The authors reinterpret this architectural inductive bias as an initialization bias for ViT, solving for Q/K weights via optimization that makes the softmax attention approximate an impulse convolution matrix. Experiments on CIFAR-10/100, SVHN, and ImageNet-1K demonstrate consistent improvements over Kaiming Uniform, Trunc Normal, and Mimetic initialization, with particular gains on small-scale datasets.

## Strengths

1. **Novel and well-motivated structured initialization approach.** Unlike standard generative initialization that only controls parameter distributions (Kaiming Uniform, etc.), the paper directly constrains the structure of the attention map to mimic a convolution matrix. This embeds a CNN inductive bias into ViT without any architectural modification, preserving ViT's flexibility for large-scale use. (Lines 52–57, Algorithm 1, Figure 1.)

2. **Theoretical motivation for why random filters work in ConvMixer.** Proposition 1 (Section 3) formally shows that under a rank-deficiency condition on patch embeddings, any \(f\times f\) filter can be expressed by learning only channel-mixing weights as long as \(D \ge k f^2\). This provides a principled foundation that earlier empirical observations lacked, and it directly supports the paper's core premise that filter structure matters more than exact weights.

3. **Comprehensive empirical evaluation across datasets and model configurations.** The method is tested on CIFAR-10, CIFAR-100, SVHN, and ImageNet-1K, across ViT-T (3 heads, 8 heads) and ViT-S (6 heads, 16 heads). The results show consistent improvements of 2–4% over Trunc Normal on small-scale benchmarks, and competitive performance on ImageNet-1K (Table 1, Table 2). Notably, Imp.-3 achieves 91.62% on CIFAR-10 and Imp.-5 achieves 70.46% on CIFAR-100, outperforming Mimetic initialization.

4. **Thorough ablation on pseudo inputs.** The paper exhaustively evaluates nine pseudo-input combinations (PE, Gaussian, Uniform, and mixtures) across two QK-sharing configurations and two head counts (Table 3 in paper = Table 4 per paper numbering). This establishes that positional encoding works best and that no real data is needed for initialization—a careful methodological validation.

5. **Compelling ConvMixer–ViT bridging experiments.** Table 5 shows that ViTs with impulse initialization (embedding=256, h8 achieve 90.67%) approach end-to-end trained ConvMixers (91.76%) of equal depth and embedding, while other ViT initializations lag far behind (Trunc Normal at 87.27%). This directly validates the paper's core thesis that CNN architectural bias can be instantiated as initialization bias.

6. **Attention map visualization confirms intended structure.** Figure 3 shows clear off-diagonal peaks organized in a convolutional pattern for impulse initialization, whereas Mimetic primarily strengthens the diagonal and Random shows no structure. This provides direct evidence that the optimization procedure successfully embeds the impulse filter structure.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the empirical evidence. No weakness identified invalidates or severely undermines the central contribution.

### Minor

1. **The "state-of-the-art" claim is broader than the baseline set.** The paper claims "state-of-the-art performance for data-efficient ViT learning" (abstract, contributions), but comparisons are limited to other *initialization* methods (Kaiming Uniform, Trunc Normal, Mimetic). Methods that address data-efficient ViT training through architecture changes (CvT, CoAtNet), distillation (DeiT), or different training recipes are not included. While these are fundamentally different approaches and comparing against them would shift the paper's scope, the SOTA claim as written invites expectations the experiments do not fully serve. The authors should either add a relevant non-initialization comparison or explicitly qualify the claim to "state-of-the-art among initialization methods for data-efficient ViT learning."

2. **The optimization quality of Algorithm 1 is not quantified.** The paper solves for Q/K via MSE minimization between the softmax output and the target impulse matrix (10,000 Adam iterations), but never reports the final reconstruction error (MSE or cosine similarity). The critic's concern that "it is unclear whether the method works *because* it achieves impulse attention maps or despite not achieving them" is valid. While the attention map visualization (Figure 3) provides qualitative evidence, reporting the final MSE (possibly as a function of head count and embedding dimension) would directly address this gap and also validate the claim that iterative optimization handles low-rank better than SVD.

3. **Standard deviations / error bars are not reported.** All accuracy numbers are given as point estimates without variance. Given that CIFAR-10 runs can vary by 0.5–1% across seeds, the reported 2–4% improvements over Trunc Normal are credible but would be strengthened by multiple trials or confidence intervals.

4. **The pseudo-input configuration for main results is not explicitly stated.** The ablation (Table 4) explores "same" vs. "different" Q/K per layer, along with various pseudo-input combinations. The main results (Tables 1, 2) do not specify which configuration was used. While it is reasonable to assume the default "same Q/K with PE" configuration (which the paper identifies as the best average choice), the omission makes it harder to precisely reproduce the main results.

5. **The theoretical link from Proposition 1 (ConvMixer) to ViT initialization is heuristic.** Proposition 1 is derived for ConvMixer with fixed linear spatial mixing. The paper draws an analogy to ViT's multi-head attention by noting that both have multiple spatial mixing matrices shared across channels (lines 180–184). This analogy is reasonable and the paper does not claim it as a theorem, but the transition could be more carefully delineated. The paper would benefit from explicitly stating where the ConvMixer theory ends and the ViT heuristic begins, as suggested by the critic.

### Trivial

- Minor presentation: "state-of-the-art" in the contribution list (line 65) is not hyphenated consistently with the abstract.

## Nice-to-Haves

- A sensitivity analysis of the optimization hyperparameters in Algorithm 1 (iterations, learning rate) would improve reproducibility.
- Measuring the rank \(k\) of intermediate embeddings in the models tested would allow a direct empirical check of the condition \(D \ge k f^2\) from Proposition 1.
- An ablation that initializes Q/K to approximate a *linear* (pre-softmax) version of the impulse matrix would test whether the softmax nonlinearity is essential to the method's success.

## Removed Points

- **"Proposition 1 does not apply to ViT and is presented as supporting a claim it cannot support."** — The paper clearly presents Proposition 1 in the "Preliminaries" section about ConvMixer, then draws an analogy to ViT in Section 4 ("Leveraging this insight…"). It never claims Proposition 1 directly proves anything about ViT attention. The connection is explicitly framed as a motivating analogy (lines 152–153: "this configuration can be viewed as having \(f^2\) heads…"). This criticism overstates the paper's theoretical pretense.
- **"Compare against non-initialization methods like DeiT, CvT, CoAtNet."** — The paper's contribution is specifically about *initialization*. Comparing against methods that change the architecture (CvT, CoAtNet) or training paradigm (DeiT distillation) would be evaluating the paper against a different class of contribution. The paper already compares against ConvMixer of equivalent depth/width, which is the most directly relevant cross-architecture comparison.
- **"The paper does not explore sensitivity to optimization iterations and learning rate in Algorithm 1."** — While this would be nice to have, its absence is not a meaningful weakness; the paper reports that 10,000 iterations at 1e-4 converge reliably (~5 seconds), and the method is not hyperparameter-sensitive in a way that affects the paper's conclusions.

## Novel Insights

None beyond the paper's own contributions. The reviewers raise useful suggestions but do not contribute novel theoretical or methodological insights beyond what the paper already provides.

## Suggestions

1. **Qualify the "SOTA" claim.** Either add a comparison against a representative non-initialization method for data-efficient ViT learning, or limit the claim to "among initialization methods for data-efficient ViT learning."
2. **Report the final optimization MSE** between the target impulse matrix and the softmax output after Algorithm 1, ideally as a function of head count and embedding dimension. This would close a clear gap in the empirical evaluation.
3. **Add standard deviations** for the main results (multiple seeds), or at minimum acknowledge the lack of variance estimates and justify the single-run practice.
4. **Explicitly state in the main results section** which pseudo-input and Q/K-sharing configuration is used for Tables 1 and 2.
5. **Tighten the theoretical framing in Section 4** by adding a sentence that explicitly separates the ConvMixer theorem (Proposition 1) from the ViT heuristic motivation.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>