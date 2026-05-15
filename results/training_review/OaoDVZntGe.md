## Summary

This paper introduces Inverse Attention Agents (Inverse-Att), a MARL method that combines self-attention mechanisms with Theory-of-Mind-style reasoning. The agent first learns to assign attention weights to goals via a self-attention policy (Phase 1), then trains an inverse network to infer other agents' attention weights from their observations/actions (Phase 2), and finally integrates those inferences to update its own attention (Phase 3). Experiments across five MPE environments show Inverse-Att outperforming MAPPO, IPPO, MAA2C, ToM2C*, and a self-attention-only baseline (Self-Att) in mix-and-match evaluations, with additional human experiments showing benefits in 4 out of 5 roles.

## Strengths

- **Consistent empirical superiority across diverse tasks**: Inverse-Att achieves the highest average reward across all five MPE tasks in Table 1 (e.g., Spread: 404.14 vs next-best 283.89 for Self-Att; Navigation: 497.96 vs 328.24). This pattern holds across cooperative, competitive, and mixed settings, demonstrating broad applicability.

- **Human experiments support real-world coordination benefits**: Inverse-Att achieves higher rewards than baselines when paired with human players in 4 out of 5 evaluated roles (Table 2), e.g., Spread 332.3 vs Self-Att 272.0, Adversary Wolf 286.9 vs 197.4. While small-scale, this is a genuine positive signal for human-agent ad-hoc coordination.

- **Inverse attention network accurately infers attentional states**: Figure 3 shows the inverse network correctly predicts the top-1 attended goal with near-100% accuracy across all roles, confirming that the core inference mechanism works as designed for agents with the same attention architecture.

- **Clean three-phase training pipeline**: The algorithm (Alg. 1) and architectures (Figures 1, 2) are clearly structured, with the phase separation (self-attention → inverse network training → integrated policy) making the method easy to understand and reproduce. The initialization strategy for the UW network (identity for self-weights, zero for inferred weights) is a nice practical touch.

- **Robustness across population scales**: Inverse-Att outperforms Self-Att and MAPPO at scales 2, 3, and 4 in Spread, Adversary, and Grassland (Tables t:spread_result, t:adv_result, t:grass_result), supporting generalization claims beyond a single fixed population size.

## Weaknesses

### Fatal
None.

### Major

- **Mix-and-match evaluation does not isolate ad-hoc coordination from in-group benefit**: The mix-and-match pool (Section 6.2) includes three seeds per method, and Inverse-Att's inverse network is designed to infer attention of same-role agents. Since Inverse-Att agents naturally produce interpretable attention patterns while MAPPO/IPPO/MAA2C agents do not, Inverse-Att may disproportionately benefit when paired with other attention-based agents (Self-Att or Inverse-Att) rather than genuinely adapting to *any* unseen policy. The paper reports only aggregate rewards across all pairings, making it impossible to verify whether gains reflect ad-hoc coordination or within-group compatibility. This is the most significant gap in the evaluation.

- **Baseline performance is suspiciously low, suggesting possible implementation/tuning issues**: MAPPO achieves only 31.82 in Spread, IPPO gets 0.55, and MAA2C achieves 48.46 — compared to Self-Att's 283.89. These scores are far below reasonable expectations for well-tuned implementations of these algorithms on simple MPE tasks. While the paper states that "all baseline methods are trained for the same amount of accumulative episodes" (40M steps), performance this low raises concerns about whether the baselines were properly tuned, whether the GF observation space disadvantages MLP-based methods, or whether there is a mismatch in how observations are provided to different methods. Without training curves or hyperparameter details, it is difficult to assess whether the reported advantage over these baselines is meaningful.

### Minor

- **Unclear whether baselines receive the same observations (GF) or raw coordinates**: Section 6.1 states that "the key distinction lies in our application of the GF function atop raw observations," which appears to describe the environment for all agents. However, Section 6.2 says baselines "follow the same method as" their original papers (which use raw state). The paper never explicitly confirms that MAPPO/IPPO/MAA2C baselines receive GF representations. If baselines receive raw coordinates while attention-based methods receive learned GF representations, the comparison is fundamentally unfair. If all methods use GF, this non-standard input may disadvantage MLP-based methods, making the advantage of attention mechanisms at least partially an artifact of the representation choice.

- **Inverse network's applicability to non-attention agents is unexamined**: The inverse network is trained exclusively on Self-Att agent data from Phase 1. In Phase 3, it is applied to all same-role agents regardless of policy architecture (MAPPO, MAA2C, etc.), which do not use attention mechanisms. The network will still output weights, but their correspondence to any actual internal state of those agents is unknown and unvalidated. The paper acknowledges inference is limited to "same type" agents (meaning same role), but does not discuss the more critical assumption that teammates must share a compatible architecture for the inferred weights to be meaningful.

- **The ToM component's contribution over the self-attention baseline is not cleanly isolated**: Self-Att already dramatically outperforms all non-attention baselines (e.g., 283.89 vs MAPPO's 31.82 in Spread). The incremental improvement from Inverse-Att over Self-Att, while present in most settings, is sometimes modest (e.g., Adversary Wolf: 107.93→110.15; Grassland Wolf: 93.68→101.21) and reverses in the human Grassland Wolf condition (Self-Att 197.9 vs Inverse-Att 185.7). The paper lacks an ablation that removes the inverse inference (e.g., concatenating random weights instead of inferred ones) to demonstrate that the ToM inference itself, rather than the increased model capacity or multi-agent training dynamics, drives the improvement.

- **Human experiments are underpowered**: With only 5 participants and 5 episodes per condition, the human study provides suggestive rather than conclusive evidence. Standard deviations are large and confidence intervals overlap in several conditions (e.g., Grassland Wolf: Self-Att 197.9±12.76, Inverse-Att 185.7±30.45). The claim of "superior cooperation with humans" is not statistically justified.

- **Inverse network accuracy metric is coarse**: The evaluation uses rank-alignment accuracy (e.g., does the predicted top-1 weight match the ground-truth top-1?). This metric can be high even when predictions are near-uniform and far from the true distribution. Reporting mean absolute error, cosine similarity, or correlation would provide a more informative picture of inference quality.

- **GF representation acquisition is underspecified**: The paper references "offline datasets D_N" used to train the score network, but does not describe what these datasets contain, how many samples are used, how they are collected, or whether they are environment-specific. This component is central to the observation space used by all methods.

### Trivial

- The `\text{attention}()` function used in Eqs. (1) and (6) is never defined (scaled dot-product? additive?). The reference to Vaswani et al. provides context, but the specific mechanism should be stated.
- The paper references `\autoref{app:}` multiple times for additional details that are not present (stripped by the parser from the original submission).

## Nice-to-Haves

- **Conditional performance by teammate type**: Report Inverse-Att's reward separately when paired with MAPPO, Self-Att, and Inverse-Att teammates. This would directly address the most significant evaluation gap.
- **Ablation replacing inferred weights with random/zero weights**: An experiment where UW concatenates non-informative weights instead of inferred ones would isolate the benefit of the ToM component.
- **Inverse network tested on non-attention agent observations**: Analyze what the inverse network outputs when given MAPPO agent observations and whether using those predictions helps or hurts performance.
- **Study with more human participants** to establish statistical significance.
- **Training curves for baselines** to verify proper convergence.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about "missing related works"**: Per guidelines, I cannot confirm the existence or absence of related works without external sources.
- **Criticism about "no justification for freezing inverse network"**: Freezing a pre-trained component during downstream training is standard practice and requires no special justification.
- **Formatting/style nitpicks and typo claims**: These are parser artifacts, not author errors.
- **Criticism about "GF gives unfair observation advantage" stated as fact**: The paper describes GF as part of the environment for all agents, not just attention-based methods. The concern about GF disadvantaging MLP methods is retained as a Minor weakness, but the specific claim that baselines receive different observations is removed as unsupported.
- **Generic strengths from Strength Finder** that lack specific evidence or concrete content (e.g., "addressed an important problem," "targeted an interesting question").

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the paper's framing around "same type" inference is ambiguous between role-identity and policy-architecture, and this ambiguity creates a significant gap between the method's design and its evaluation. The inverse network is trained on one architecture (Self-Att) and deployed on others (MAPPO, etc.) without any validation of whether the outputs remain meaningful. This is a subtle but important methodological limitation that future work in neural ToM for MARL must address — namely, that "inferring mental states" of agents with fundamentally different architectures may require the inference network to be architecture-agnostic or to be validated across architectures.

## Suggestions

1. **Break down mix-and-match results by teammate policy type**. This single addition would most directly resolve whether the method genuinely enables ad-hoc coordination or benefits from in-group effects.
2. **Add an ablation** where the UW network receives non-informative weights (zeros or random) controlling for model capacity, to isolate the value of the ToM inference itself.
3. **Clarify the observation space** used by each baseline method — explicitly state whether MAPPO/IPPO/MAA2C receive GF representations or raw coordinates.
4. **Validate the inverse network on non-attention agents** (e.g., MAPPO) by checking whether the inferred weights correlate with any measurable behavior (e.g., goal occupancy, movement direction) even in the absence of ground-truth attention.
5. **Report training curves for baselines** to verify that MAPPO/IPPO/MAA2C were properly trained to convergence.
6. **Increase human participant count** and perform formal statistical tests (e.g., paired t-tests with Bonferroni correction) to support the human cooperation claims.

## Score and Decision

The paper presents a conceptually clean method and shows consistent empirical improvements. However, the evaluation has two structurally limiting weaknesses: (1) the mix-and-match results are not disaggregated by teammate type, making it impossible to verify the core claim about ad-hoc coordination with unseen *arbitrary* agents; (2) the baseline performance is anomalously low, raising unresolved questions about experimental fairness. These gaps are addressable with additional analysis/experiments but prevent the current version from being a fully convincing contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>