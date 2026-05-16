Now I have all the verification I need. Let me construct the final consolidated review.

---

## Summary

This paper introduces GPS (Gumbel Prior Similarity), a differentiable set-to-set similarity measure that models the distribution of K-nearest-neighbor distances between two sets using Gumbel distributions. The log-likelihood of the fitted Gumbel serves as the similarity score, and its negative can be used as a loss function for training. The method is evaluated on few-shot image classification (miniImageNet, tieredImageNet, CIFAR-FS, etc.) and 3D point cloud completion (ShapeNet, PCN, KITTI) across multiple backbone networks, showing consistent improvements over CD, EMD, and recent CD variants while maintaining linear computational complexity comparable to Chamfer Distance.

## Strengths

1. **Novel use of Gumbel distributions to model KNN distance distributions for set matching.** The idea of modeling the extreme-value statistics of distances between sets — rather than directly comparing individual point pairs — is a genuinely new angle. The empirical fit shown in Figure 2 demonstrates that Gumbel distributions can approximate the distribution of (negative-log) KNN distances, providing a concrete motivation that goes beyond heuristic intuition.

2. **Consistent empirical improvements across diverse tasks and backbones.** The improvements are not concentrated in one setting. In few-shot classification, GPS outperforms DeepEMD and other CD variants on all tested datasets (e.g., 66.52% vs. 65.91% 1-shot on miniImageNet, Table 5; 72.98% vs. 72.56% on CIFAR-FS, Table 6). In point cloud completion, GPS improves every backbone it is tested on (FoldingNet, PMP-Net, PoinTr, SnowflakeNet, CP-Net, PointAttN, SeedFormer) across multiple metrics and datasets (Tables 8–12). The pattern is broad and consistent.

3. **Linear computational complexity matching CD.** Figure 5(b) shows GPS running time is nearly identical to CD and orders of magnitude faster than DeepEMD. This is a practically important property — GPS obtains better accuracy than CD without sacrificing efficiency, which is rare among CD alternatives.

4. **Ablation and hyperparameter analysis.** The paper systematically explores the effect of α, β, K (number of NNs), and M (number of Gumbel mixtures) in Tables 1–3 on CIFAR-FS. The finding that mixtures add robustness and that different hyperparameter choices converge to similar performance is practically useful guidance.

## Weaknesses

### Fatal

None.

### Major

1. **The probabilistic derivation is incomplete and the method's theoretical status is unclear.** The paper claims a probabilistic framework (graphical model in Figure 3, Equation 3) but the transition to the final formula (Equation 4) is not justified step-by-step. The derivation treats \(p(q)\) and \(p(\mathcal{P}_1=\mathcal{P}_2|q)\) as constants without discussion of whether this is reasonable, and the sum over "Gumbel distributions" \(q\) becomes an unweighted sum over mixture components \(m\) and NN ranks \(k\) with no clear probabilistic interpretation. The paper itself acknowledges the i.i.d. assumption required by extreme value theory "is hardly valid" (Section 3.3). The final GPS score is a sum of Gumbel PDF values — not a probability, not a log-likelihood ratio, and not the output of a coherent generative model. The method may well be a useful loss function (many successful losses in the literature are heuristics), but the paper presents it as more theoretically grounded than it actually is. This disconnect between framing and content is the paper's most significant weakness, as it makes it difficult to understand *why* GPS should work and leaves readers uncertain about what class of contributions the paper belongs to.

2. **Key implementation details are underspecified to the point of compromising reproducibility.** (a) The paper defines the Gumbel PDF in terms of standard parameters \(\mu,\sigma\) (Definition 1), but the method uses parameters \(\alpha,\beta\) with no explicit mapping between them. (b) The mixture formulation is mentioned ("a mixture of \(M\) independent Gumbel distributions") but mixture weights are never specified — are they uniform? Learned? Data-dependent? (c) The distance shifting \(\delta = (\alpha_{k,m})^{-1/\beta_{k,m}}\) is given but its derivation from "mode = 0" is not shown. These gaps mean a reader cannot reimplement GPS from the current description alone.

### Minor

1. **No confidence intervals or standard deviations are reported for any experiment.** In few-shot classification, improvements are often <1 percentage point (e.g., 66.52% vs. 65.91% on miniImageNet 1-shot). Without variance estimates, it is impossible to assess whether these differences are statistically significant. This is a standard expectation for empirical papers, and its absence weakens the paper's central claim of "significant improvements."

2. **Overstated novelty claim.** The paper states "We are the first to leverage statistical information from KNNs for set-to-set matching." This is not accurate — DCD (density-aware CD, Wu et al. 2021) already uses KNN-based density estimation, and both DCD and InfoCD operate on statistical properties of distances. The genuine novelty is in *modeling KNN distance distributions with Gumbel distributions*, not in using KNN statistics per se. The claim should be narrowed.

3. **Point cloud comparison protocol is less explicit than for few-shot.** For few-shot classification, the paper clearly states all baselines were retrained in-house from scratch under identical conditions. For point cloud completion, the paper says "by replacing the CD loss with our GPS wherever it occurs" but does not explicitly state whether the CD baselines were retrained in-house or compared against published numbers. For some tables (e.g., Tables 8, 9, 11), the text says "our approach consistently improves the performance of baseline models" without clarifying how those baseline numbers were obtained. This ambiguity undermines the reliability of the comparison.

4. **Proposition 1 is mathematically trivial and does not connect meaningfully to the method.** The proposition states that \(f(x)=xe^{-x}\) has a unique maximum at \(x=1\) and is concave/convex in certain intervals. While the subsequent gradient discussion is intuitive, the formal proposition adds little analytical depth — the gradient properties described (decay near the mode) follow directly from the Gumbel PDF shape itself.

### Trivial

- The notation \(\bar{\mathcal{P}_2}\) in \(p(\mathcal{P}_1=\bar{\mathcal{P}_2}|\mathcal{X}_1,\mathcal{X}_2)\) (line 41) is potentially a typo (should be \(\mathcal{P}_2\)?) and is confusing since \(\mathcal{P}_2\) is the distribution generating \(\mathcal{X}_2\).

## Nice-to-Haves

- A control experiment that replaces the Gumbel with another distribution (e.g., Gaussian on log distances) to demonstrate that the Gumbel choice specifically — not just the KNN structure — drives improvements. The paper argues Gumbel is appropriate via extreme value theory but then acknowledges the i.i.d. assumption is violated; an empirical ablation would clarify.
- A discussion of when GPS might underperform CD or other losses, and whether there are identifiable failure modes.
- Sensitivity analysis of the \(\delta=0\) choice for few-shot classification: does the \(\log(d_{\min})\) transformation ever cause numerical issues when learned distances become very small?
- More analysis of why the simplest configuration (1 NN, 1 Gumbel, no mixture) already works well, given that the method is motivated by using multiple NNs and mixtures.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"ℓ is not defined"** (Harsh Critic): The paper defines ℓ in context (line 127: "ℓ for a loss parametrized by ω") and mentions cross-entropy in Section 3.3. The training objective in Equation 5 follows DeepEMD's framework, which uses cross-entropy. The criticism is incorrect.
- **"No comparison to optimal transport losses"** (Harsh Critic): The paper already compares against EMD and DeepEMD, which are optimal transport-based. Comparing against additional OT variants (sinkhorn, sliced Wasserstein) would be scope creep beyond the paper's chosen baseline set.
- **"No analysis of K and M in main experiments"** (Harsh Critic): Tables 1–3 systematically ablate K (1st/2nd NN) and M (mixtures) on CIFAR-FS. The reviewer missed this.
- **"No discussion of failure cases"** (Harsh Critic): This is a common generic request that applies to nearly every paper. The paper does include a Limitations paragraph (Section 5) acknowledging hyperparameter tuning challenges. The absence of specific failure cases is a nice-to-have, not a weakness.
- **"Section-by-section note about \bar{P_2} typo treated as a major complaint"** (Harsh Critic): This is a trivial notation issue, already moved to Trivial above.

## Novel Insights

The reviews surface a genuine tension in the paper: the Gumbel modeling idea is empirically productive and the efficiency/accuracy trade-off is genuinely impressive, but the paper's own theoretical framing undermines itself. The harsh critic correctly identifies that the probabilistic derivation is not a derivation in the standard sense — it is more of a design rationale. Yet the strength finder correctly observes that the empirical fit (Figure 2), gradient behavior (adaptive weighting of poor predictions), and consistent results across two very different tasks (classification and generation) suggest the idea captures something real about distance distributions. The most interesting unresolved question is whether the Gumbel shape specifically matters, or whether any unimodal distribution on log-distances would yield similar results. Answering this would either strengthen or simplify the paper's contribution significantly.

## Suggestions

1. **Reframe the method honestly.** Drop the pretense of a full probabilistic derivation and present GPS as a *biologically/statistically motivated loss function*: using the Gumbel PDF evaluated at transformed distances as a similarity score, justified by empirical fits (Figure 2), desirable gradient properties (adaptive weighting), and empirical success. This would eliminate the disconnect between framing and content.

2. **Specify the mapping from α,β to μ,σ, clarify the mixture formulation (weights), and provide a pseudocode algorithm.** Without these, the method is not reproducible.

3. **Add standard deviations or confidence intervals** for at least the main few-shot and point cloud results. Even for single-run evaluation, reporting the variance across test episodes (few-shot) or multiple seeds would substantially strengthen the reliability of the claims.

4. **Clarify the point cloud baseline protocol.** State explicitly for each table whether the CD baseline was retrained in-house or taken from published numbers, and ensure the comparison is fair.

5. **Tone down the "first to leverage KNN statistics" claim** to "first to model KNN distance distributions using Gumbel/EVT distributions for set matching," which is both accurate and distinctive.

## Score and Decision

The paper proposes a genuinely novel and practically useful set-similarity measure with a strong efficiency-accuracy profile and consistent empirical results across two distinct tasks. However, the theoretical framing overpromises relative to what is actually delivered, and the missing implementation details and lack of confidence intervals compromise verifiability. These are significant problems but not fatal — the contribution stands on its empirical merits and can be strengthened with clearer exposition rather than new experiments. I view this as a borderline accept that requires major improvement in presentation and completeness.

**Score: 5.5**

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>