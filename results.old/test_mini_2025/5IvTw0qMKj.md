Now I have a thorough understanding of the paper and the calibration anchors. Let me produce the final consolidated review.

## Summary

This paper proposes C²INet, a continual learning framework for multi-agent trajectory prediction that combines causal intervention (via backdoor adjustment on confounder C) with a memory-queue-based prior update mechanism. The goal is twofold: remove environmental confounding biases in trajectory representations, and prevent catastrophic forgetting when learning new environment tasks sequentially. Experiments on ETH-UCY, synthetic, and SDD datasets with multiple backbones (STGAT, STGCNN, PECNet, YNet) show consistent improvements over standard continual learning baselines.

## Strengths

1. **Novel combination of causal intervention and continual learning for trajectory prediction.** The paper is the first to integrate backdoor adjustment with a continual-learning prior queue for trajectory forecasting. This is a timely and well-motivated problem since real-world deployment requires both debiasing and incremental adaptation.

2. **Extensive experimental evaluation across three datasets with multiple backbones.** Results are reported on ETH-UCY (5 environments), a synthetic circling dataset (8 settings), and SDD (8 scene regions), using STGAT, STGCNN, PECNet, and YNet backbones. The plug-and-play design is demonstrated empirically (Sec. 5.3, Table 1). C²INet variants are consistently top-2 across nearly all task sequences, often outperforming standard continual learning methods (EWC, MoG, Coresets).

3. **Both online and offline update modes.** The paper addresses practical deployment constraints by proposing an offline mode (clustering-based pseudo-feature selection when all data is available) and an online mode (streaming pseudo-feature addition). This reflects realistic deployment scenarios such as autonomous driving in new regions.

4. **Posterior visualization confirms task-specific separation.** Figure 3 shows that C²INet (online and offline) produces distinct, well-separated Gaussian mixtures for different tasks, while GCRL collapses into a single aggregate — providing visual evidence that the continual memory mechanism preserves task discriminability.

## Weaknesses

### Major

1. **The combination of P(Z|X) and Q(C|X) into P(Z|X,C) via product of Gaussians (Eq. 3) is mathematically unjustified as presented.** The paper defines P(Z|X) ∼ N(μ₁, ω₁) (over trajectory latent Z) and Q(C|X) ∼ N(μ₂, ω₂) (over confounder encoding C), then states "These distributions are combined to derive the optimal mixed distribution P(Z|X,C) ∼ N(μ*, ω*)" using standard product-of-Gaussians formulas. However, Z and C are different latent variables living in potentially different spaces. Multiplying their densities as if they are beliefs about the same variable is not valid without establishing that Z and C share the same dimensionality and that the product operation is meaningful for the conditional distribution P(Z|X,C). The paper does not provide any justification for this step, and it is the central mechanism of the causal intervention module. This is a significant gap in the method specification.

2. **Causal graph inconsistency undermines the claimed effect of the *do*-operator.** Section 2.2 establishes the path "X → Z ← C" (line 108), meaning the confounder C directly influences the latent representation Z. Section 2.3 then claims that intervening on X via do(X) "renders Z independent of the confounding disturbance from C" (line 118). In causal theory, do(X) blocks only the path C → X; if a direct C → Z edge exists (as the graph indicates), do(X) does NOT make Z independent of C. The paper appears to conflate blocking C → X with removing all confounding influence on Z. The backdoor adjustment formula in Eq. 1-2 uses P(C) as the adjustment set, which would address confounding of X→Y through C, but the claim about Z remains unsupported.

3. **The continual learning derivation (Eqs. 4–9) is opaque and contains unsubstantiated approximations.** The transition from Eq. 5 to Eq. 6 invokes "the calculation formula of limit" and drops an underbrace term as o(α_{K-1}) without stating the limiting operation, the convergence conditions, or justifying why α_{K-1} (a trainable parameter not guaranteed to be small) justifies the big-O claim. The derivation references Appendix A.2.2, but as presented in the main text it is too fragmented to follow as a self-contained argument. Since the resulting Eq. 8 is the core optimization objective for prior updates, this opacity is a significant concern.

4. **A non-continual-learning baseline outperforms the proposed method on the primary aggregated metric in the most challenging setting.** On the final ETH-UCY column (average across all 5 tasks), COUNTERFACTUAL achieves 0.83/1.75 ADE/FDE while C²INet-offline achieves 0.86/1.81 and C²INet-online achieves 0.86/1.82 (Table 1). COUNTERFACTUAL is a causal intervention method that does not explicitly address catastrophic forgetting, yet it achieves a better overall average. While C²INet dominates on the first four tasks individually, the paper's central claim of "effectively mitigating catastrophic forgetting" is weakened by the fact that the method underperforms a non-CL baseline on the final aggregated metric. The paper acknowledges this in passing but does not adequately discuss the implications.

### Minor

5. **No standard deviations or confidence intervals reported despite averaging over 5 seeds.** The paper states that results are averaged over five random seeds (Sec. 5) but reports only point estimates. Without variance information, the significance of improvements (often <3% in ADE/FDE) cannot be assessed. This is standard practice for trajectory prediction benchmarks and should be included.

6. **No ablation of the causal intervention module.** The paper never compares C²INet with vs. without the *do*-operator (i.e., a standard VAE without causal intervention), making it impossible to isolate the contribution of the causal component from the continual memory component. An ablation would substantially strengthen the empirical support.

7. **No ablation of the pruning strategy.** The pruning mechanism (Eqs. 11–12) and the threshold γ are introduced but their effect on performance and memory is never empirically evaluated. Given that pruning is presented as a practical necessity, its impact should be quantified.

8. **Posterior visualization lacks quantitative separation metrics.** Figure 3 is compelling qualitatively, but claims about "distinct" vs. "indistinguishable" distributions could be supported with quantitative measures (e.g., silhouette score, inter/intra-class variance, or KL divergence between task-specific posteriors).

### Trivial

9. The figure caption for Table 1 says "Color blocks indicate the ranking of different backbones for comparison" but this mechanism is not clearly legible in the printed table.
10. Eq. 9 appears to have a formatting issue with the KL divergence parentheses.

## Nice-to-Haves

- Reporting results under alternative task orders on ETH-UCY would address known sensitivity of continual learning to task sequencing. The current order (univ→eth→zara1→zara2→hotel) follows prior work but a sensitivity study would strengthen claims of robustness.
- Per-task breakdown of final performance in the main text (currently referenced to appendix) would help readers assess whether the method sacrifices some tasks for others.

## Removed Points

- **Criticism about Eq. 2 ELBO derivation being unreliable due to dropped KL term**: The paper correctly uses standard variational inference, including the "≥" inequality (line 135) to form a proper ELBO. Dropping the intractable KL(Q||P(C|X,Y,Z)) and obtaining a lower bound is standard practice. REMOVED (factually incorrect criticism).
- **Criticism about symmetric KL term (Eq. 10) being "ad hoc"**: The paper explicitly cites Egorov et al. (2021) for this regularization. It is adopted from prior work, not invented ad hoc. REMOVED (factually incorrect criticism).
- **Criticism about min-max optimization convergence not being verified**: Min-max training is standard for VAE-style objectives and does not require convergence guarantees in an empirical systems paper. REMOVED (non-standard demand).
- **Criticism about "missing related works"**: Notverifiable without external sources. REMOVED per policy.
- **Criticism about COUNTERFACTUAL's 0.83 vs C²INet's 0.86 being "often-small differences" combined with "no standard deviations"**: The COUNTERFACTUAL comparison is kept as Major Weakness #4. The no-std issue is kept as Minor #5. The "small differences" characterization is a value judgment that is already covered by those weaknesses.
- **Strength about "Pruning strategy for memory efficiency"**: While genuine, this is a supporting detail rather than a core strength. Retained implicitly in the review body but not listed as a standalone top strength.
- **Claim that the paper "should not be accepted in its current form" from the harsh critic's conclusion**: This is a decision, not a weakness. The review will reach its own conclusion.

## Novel Insights

The most interesting observation that emerges from combining the reviews is the tension between the paper's two core claims. The causal intervention and continual memory modules are presented as complementary, but the evidence for disentangling their individual contributions is absent — no ablation removes one module while keeping the other. The COUNTERFACTUAL result sharpens this concern: a non-CL causal method obtains better final averages, suggesting that either (a) the continual memory mechanism imposes a regularization penalty that hurts final-task performance, or (b) the causal intervention is doing most of the work and the continual learning component adds limited value. Neither possibility is resolved by the current experimental design, and both point to ablations as the single highest-impact addition.

## Suggestions

1. **Fix Eq. 3 by clarifying the shared latent space assumption.** If Z and C are assumed to be in the same d-dimensional space, state this explicitly and justify why the product of Gaussian densities is appropriate for computing P(Z|X,C). Alternatively, switch to a standard conditional VAE formulation where the trajectory encoding and confounder encoding are concatenated or summed in a principled manner.

2. **Resolve the causal graph inconsistency.** Clarify whether C → Z is a direct edge or whether C influences Z only through X (C → X → Z). If the latter, correct the causal graph and text accordingly. If the former, explain how do(X) blocks C's influence on Z, or adjust the claimed effect of the intervention.

3. **Add standard ablations:** (a) C²INet without the causal intervention module (standard VAE), (b) C²INet without the continual memory module, (c) sensitivity to pruning threshold γ. These are necessary to isolate the contribution of each component.

4. **Report standard deviations** for all main-table metrics.

5. **Discuss the COUNTERFACTUAL comparison honestly.** Either provide evidence that C²INet's continual memory provides superior stability on earlier tasks that compensates for the small deficit on the final aggregate, or acknowledge the trade-off explicitly.

## Score and Decision

**Bracket determination (Round 1):** Three calibration queries on "continual learning trajectory prediction causal intervention" produced weak anchors (avg ≤3.25: poorly-scoped papers with coherence issues), middle anchors (3.5–7.5: mixed, mostly rejected/withdrawn at 4–5, accepted at 6–7), and strong anchors (≥8: ICLR oral/poster papers with rigorous theory or clear execution). C²INet's strengths (extensive experiments, novel problem combination) place it above the weak band, while its methodological gaps (Eq. 3, causal graph, opaque derivation) keep it below the strong band. **Initial bracket: 3.5–6.0.**

**Narrowing (Round 2):** Targeted queries within (3.5, 6.0) returned several causally-oriented papers. The closest match is the CTP paper (avg 4.50, Withdrawn/Reject), which similarly combines causal methods with trajectory prediction and was criticized for "complex modeling steps not well-motivated" and insufficient theoretical justification — problems C²INet shares. Other anchors at 4.0–4.33 (causal RL for STPP, causal cross-domain prediction) were rejected for similar methodological-opacity concerns. C²INet has more extensive experiments than these papers, but its core mathematical issues (Eq. 3, causal graph) are more central to its contribution and therefore more damaging.

**Final score:** 4.5. The paper's problem framing and experimental breadth are genuine strengths, but the method is not coherently specified at the mathematical level in ways that affect core claims (not peripheral presentation issues). The causal intervention mechanism relies on an unjustified distribution-combination step, the causal graph contains an inconsistency with the claimed effect of do(X), and the continual learning derivation is too opaque to evaluate. These are structural issues that cannot be resolved without reworking or substantially clarifying the method's foundations.

<score>4.5</score>
<decision>Reject</decision>