Now I have all the information needed to verify the reviewer claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes Tree Cross Attention (TCA), a variant of Cross Attention that retrieves information from only \(\mathcal{O}(\log N)\) tokens during inference by organizing context tokens into a tree and using a learned RL policy to navigate it. Building on TCA, the authors introduce ReTreever, a general-purpose architecture for token-efficient inference. Experiments on copy tasks, GP regression, image completion, and human activity classification show that TCA achieves performance close to full Cross Attention while using dramatically fewer tokens, and outperforms Perceiver IO under the same token budget.

## Strengths

1. **Novel and well-motivated idea with strong empirical validation.** TCA's core contribution—tree-based retrieval for cross attention learned via RL—is clearly novel. The Copy Task results (100% accuracy at N=1024 using only 2% of tokens, identical to Cross Attention's 100%) directly validate that the approach can solve perfect retrieval with massive token savings. The Copy Task also starkly demonstrates a structural limitation of Perceiver IO (15.2% → 11.6% accuracy as N grows), which TCA/ReTreever overcomes.

2. **Consistent outperformance of Perceiver IO across diverse tasks.** ReTreever beats Perceiver IO under the same token budget on GP Regression (+0.19 log-likelihood on RBF, +0.23 on Matern 5/2), Image Completion (+0.32 on CelebA, +0.05 on EMNIST), and Human Activity (+1.3% accuracy). These consistent margins across both classification and uncertainty estimation tasks make the central architectural claim credible.

3. **Full receptive field is a genuine advantage over prior tree-attention work.** As correctly argued in Section 3.3 and the Related Work, the set of selected nodes \(\mathbb{S}\) covers all tokens (each token is either in \(\mathbb{S}\) or a descendant of a node in \(\mathbb{S}\)). This contrasts with Treeformer's partial receptive field and worst-case linear complexity. This is a theoretically clean and practically meaningful distinction.

4. **Weight-sharing between the policy and cross-attention module is a principled design choice.** Parameterizing the policy as an attention module (action probabilities = attention weights over child nodes given the query) elegantly ties the two desiderata—good node representations and good retrieval—into a shared parameter set, and is a practical strength worth highlighting.

5. **Empirical demonstration that non-differentiable objectives can be optimized via RL reward.** Table 5 shows that using accuracy as the RL reward substantially outperforms using negative cross-entropy (99.6% vs. 80.3% at N=1024), validating the claim that the RL formulation allows optimization of metrics that gradient descent cannot directly handle.

6. **Memory usage grows logarithmically.** Figure 3 (left) empirically validates the \(\mathcal{O}(\log N)\) memory scaling, contrasting with Cross Attention's linear growth. While runtime measurements would complement this, the memory plot is a meaningful and clear contribution.

## Weaknesses

### Fatal
None.

### Major
1. **RL training stability and convergence are under-explored.** The sensitivity analysis (Figure 3, right) shows that \(\lambda_{RL}=0.0, 0.1, 10.0\) all cause complete failure, while \(\lambda_{RL}=1.0\) succeeds—indicating a narrow window of effective RL weighting. The paper does not report the number of training episodes, the variance across random seeds for the RL component, or convergence diagnostics (e.g., reward curves during training). Since the REINFORCE objective with a single terminal reward is known for high variance, the absence of any baseline subtraction or advantage normalization is notable. These omissions make it difficult to assess whether the RL training is reliably reproducible or requires careful per-task tuning. The paper acknowledges that "the weight of the RL loss term is crucial" (line 350), which is honest, but does not provide the analysis needed to gauge the severity of this sensitivity.

2. **Efficiency claims rely almost entirely on token counts rather than measured runtime or FLOPs.** The paper defines efficiency as "number of tokens attended to" and provides memory usage, which is valuable. However, the tree traversal incurs overhead from running the policy network at each of the \(\mathcal{O}(\log N)\) levels, and Perceiver IO's fixed latents can be optimized for hardware parallelism. Without wall-clock time, FLOPs, or throughput measurements, a practitioner cannot assess whether TCA's token savings translate into actual speed gains, especially since the paper's motivation explicitly mentions low-memory/compute domains like IoT devices. This is the single most impactful missing piece of evidence.

### Minor
1. **"Comparable to Cross Attention" is slightly inflated on the Image Completion and GP Regression tasks.** On CelebA, TCA achieves 3.52 vs. Cross Attention's 3.88 (a ~9% relative drop), and on EMNIST, 1.30 vs. 1.41 (~8% drop). On GP Regression (RBF), 1.25 vs. 1.35 (~7% drop). These are modest gaps given the ~21× token savings, so "competitive" rather than "comparable" would be more accurate. The Human Activity results (88.9 vs. 89.1) and Copy Task (exact parity) genuinely support "comparable," but the overall claim in the abstract would benefit from softening.

2. **The ablation experiments (Table 5) show high variance for the Neg. CE reward condition.** At N=1024, the standard deviation is ±14.8% accuracy, which is extremely high. This suggests the Neg. CE reward training is unstable, but the paper does not discuss how many seeds produce this variance or whether the reported mean is representative. Reporting results across more seeds for this condition would be more informative.

3. **The inference-time behavior of the policy is not specified.** Algorithm 1 uses sampling (\(v' \sim \pi\)), but at inference time a deterministic selection (argmax) is standard. The paper should clarify this.

### Trivial
- The GP Regression task uses log-likelihood as a metric, but the paper does not state whether the model outputs full predictive distributions (e.g., Gaussian with mean and variance) or point predictions with fixed variance. Clarify the output representation.
- The tree construction details for each dataset are described for sequences and images (lines 107–110) but not explicitly for the Human Activity data, though the time-axis split is natural given the 50 time-point structure.

## Nice-to-Haves
- Adding wall-clock time or FLOPs measurements to complement token-count and memory comparisons.
- Providing RL convergence diagnostics (reward curves, seed variance, number of episodes) to address the training stability concern.
- Analyzing the retrieval paths selected by the learned policy (e.g., visualizing selected nodes for Image Completion to show the policy learns meaningful spatial selection).
- Adding a brief Limitations section to acknowledge the reliance on spatial/temporal structure, the sensitivity of \(\lambda_{RL}\), and that performance on high-dimensional heterogeneous tasks remains untested.

## Removed Points

The following points from the reviewers were removed or weakened with justification:

- **Tree construction heuristic not analyzed / "paper does not specify how the k-d tree is applied to each dataset"** — The paper *does* specify this for sequences (split by time-axis) and images (split by x/y coordinates) at lines 107–110. For Human Activity, the natural time-axis split follows from the sequence description. The critic's concern about alternative grouping strategies is a valid suggestion but not a core weakness; moved to Nice-to-Haves.
- **"The absence of any variance reduction technique"** — The paper does use an entropy bonus (footnote, line 193), which is a standard technique for exploration and can indirectly aid stability. The critic is correct that baseline subtraction is absent, which is a real concern, but the categorical claim of "no" variance reduction is slightly overstated. This is folded into the Major weakness (#1) with appropriate nuance.
- **"Perceiver IO comparison conflates token-count with computational efficiency" sub-points (b) and (c)** — The point about hardware parallelism and tree construction overhead being ignored are fair but belong under the broader runtime-measurement weakness. The \(\mathcal{O}(N)\) tree construction cost is acknowledged by the paper as a one-time cost (line 80: "this phase only needs to be performed once"), so it is not ignored. Kept as part of weakness #2 (Major).
- **Strength Finder strength #1 ("TCA matches Cross Attention performance...")** — Partially retained but qualified, since the Copy Task shows exact parity but Image Completion shows a ~7–9% gap. The weakness about the inflated claim wins here, but the Copy Task parity is genuine; the strength is kept with appropriate context.
- **All formatting/style nitpicks** — None present in the original reviews to remove.

## Novel Insights

None beyond the paper's own contributions. The key insight—that logarithmic-complexity cross attention can be achieved by organizing tokens into a tree and learning a retrieval policy via RL with weight-sharing—is the paper's own novel contribution, and the reviews do not surface an additional synthetic insight not already in the paper.

## Suggestions

1. **Add runtime/throughput measurements** on a representative GPU and CPU for Cross Attention, ReTreever/TCA, and Perceiver IO across varying N. This directly addresses the practical claim and is the highest-leverage addition.
2. **Report RL training diagnostics** — reward curves during training, number of episodes, seed variance, and whether any baseline normalization was used — to establish that the RL training converges reliably.
3. **Softening the "comparable" language** in the abstract to "competitive" or "close to" would more accurately reflect the modest but real gaps on Image Completion and GP Regression.
4. **Specify inference-time policy behavior** (Algorithm 1 currently uses sampling; clarify that argmax is used at inference).
5. **Clarify the output representation** for GP Regression (whether predictive distributions or point predictions).

## Score and Decision

This paper presents a genuinely novel idea with clear motivation, strong empirical validation across diverse tasks, and a theoretically sound design. The weaknesses are real but addressable: the RL training stability concern and the absence of runtime measurements are the most significant gaps, but they do not undermine the core correctness of the proposed approach. The Copy Task results alone—perfect retrieval using 2–6% of tokens where Perceiver IO fundamentally fails—demonstrate a clear and important capability. With the addition of runtime measurements and RL training details, this paper would be solid. As is, it is a worthy contribution that will be of interest to the community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>