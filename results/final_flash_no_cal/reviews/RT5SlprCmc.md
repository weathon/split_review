Now I have a comprehensive understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes MadDist and TDMadDist, two self-supervised algorithms for learning the Minimum Action Distance (MAD) from state-only trajectories using quasimetrics (asymmetric distance functions). It introduces a simple quasimetric (d_simple), a scale-invariant loss, and a benchmark suite of environments with known ground-truth MAD. The core contribution is demonstrating that an asymmetric distance function trained with trajectory-derived upper-bound constraints can achieve high correlation with the true MAD and translate to effective downstream planning.

## Strengths

- **First asymmetric MAD learning methods.** The paper explicitly and correctly identifies that prior MAD learning approaches rely on symmetric distance metrics (Euclidean distance) which cannot capture the inherent asymmetry of the MAD in environments with irreversible dynamics (e.g., CliffWalking, KeyDoorGridWorld). Sections 5 and 6 define and implement quasimetric distance functions for MAD learning, and Section 2 contrasts this against prior symmetric approaches. This is a well-motivated and genuine novelty.

- **Comprehensive benchmark suite with known ground-truth MAD.** The paper evaluates on NoisyGridWorld, KeyDoorGridWorld, CliffWalking, PointMaze (UMaze, MediumMaze), and OGBench PointMaze (six variants), all with computable ground-truth MAD. This enables precise quantitative assessment of learned distances rather than relying on proxy metrics. Section 7 enumerates these environments and explains how ground truth is computed (e.g., Floyd-Warshall over the maze graph). This systematic evaluation goes beyond prior work.

- **Strong and consistent empirical performance.** MadDist achieves the highest Spearman/Pearson correlations (typically >0.9) and lowest CV ratios across all environments (Figure 3), and attains near-perfect or perfect (1.00 ± 0.00) success rates on all six OGBench PointMaze planning tasks (Table 1), decisively outperforming QRL and Hilbert baselines. The results hold across deterministic/stochastic dynamics, discrete/continuous states, and noisy observations.

- **Scale-invariant loss objective.** Equation 5 uses a normalized loss ((d_θ/(j-i) − 1)²) that prevents long-trajectory pairs from dominating the gradient, addressing a known limitation of the squared-error formulation in prior work (Eq. 2). This is a practical and well-motivated improvement.

- **Downstream task validation.** Table 1 shows that high MAD approximation accuracy translates to effective goal-conditioned planning, demonstrating practical relevance beyond distance estimation quality.

## Weaknesses

### Major

- **Missing direct predecessor baseline in experiments.** The paper extensively discusses Steccanella & Jonsson (2022) in Sections 2, 4, and 6.1 as the most closely related prior work — it formulates MAD learning with the same basic approach (Eq. 2), and MadDist is described as "similar to prior work (Steccanella & Jonsson, 2022), but differs in the use of a quasimetric distance function and a scale-invariant loss." Yet this predecessor is completely absent from the experimental comparison (Section 7). Without this baseline, the reader cannot attribute MadDist's improvements to the asymmetric formulation, the scale-invariant loss, the contrastive term, or the simple quasimetric vs. general engineering improvements. The paper claims to "outperform state-of-the-art algorithms for learning the MAD" (Conclusion), but the most relevant state-of-the-art is not compared. This is a significant omission that weakens the paper's central comparative claims.

- **TDMadDist underperforms without analysis despite being a main contribution.** TDMadDist is presented in Section 6.2 and the abstract as one of "two novel algorithms," yet the paper explicitly reports that it "underperforms the MadDist and QRL algorithm" (Section 7 Discussion). No diagnostic analysis is provided to explain why the bootstrapping mechanism fails, in what regime it might offer advantages, or whether the issue is target network instability, compounding errors, or the specific environment structure. Negative results can be informative, but presenting an underperforming method as a main contribution without analysis limits scientific value. The paper should either analyze the failure or relegate it with a proper discussion.

- **Incomplete theoretical analysis of what quantity MadDist actually learns.** The loss function L_o (Eq. 5) directly minimizes the relative error between the learned distance d_θ and the observed trajectory length j−i. The paper correctly acknowledges that j−i is an upper bound on the MAD (Section 4). However, it does not provide a theoretical account of why minimizing error to an upper bound recovers the lower bound (the true MAD), beyond appealing to the combination of the upper-bound constraint loss L_c and the triangle inequality of the quasimetric. The paper would benefit from a formal argument or at least intuitive reasoning about how the interaction of L_o, L_c, L_r, and the triangle inequality leads to recovery of the MAD rather than the expected trajectory distance under the behavior policy. The TDMadDist result (which uses bootstrapping to explicitly target the minimum over paths, yet underperforms) makes this analysis particularly important. As currently written, there is a gap between the optimization objective and the claimed recovered quantity.

- **Seed count inconsistency.** The empirical setup (Section 7) states: "All reported results are means over five independent runs (random seeds) to ensure statistical robustness." However, the Figure 3 caption states: "Shaded regions indicate minimum and maximum values across three random seeds." The paper does not clarify whether different evaluations use different numbers of seeds, and if so, why. This inconsistency undermines the presentation of statistical rigor.

### Minor

- **Perfect success rates need explanation.** Table 1 reports MadDist achieving 1.00 ± 0.00 on four of six OGBench planning tasks. While this is not inherently implausible, a standard deviation of exactly zero across five random seeds on a downstream planning task is unusual and warrants discussion. Is the planning evaluation sufficiently challenging? Does the metric saturate? A brief comment would preempt concern.

- **NoisyGridWorld results are deferred to appendix.** This environment is introduced in the Environments section as a key challenge (stochastic transitions, observation noise), but its results do not appear in any main figure or table. The paper states they are in Appendix F, which is stripped. Including these results in the main text would strengthen the evaluation.

- **Lack of analysis on the MadDist/TDMadDist performance gap.** The paper notes that TDMadDist underperforms MadDist but does not investigate why. Given that TDMadDist uses bootstrapping to explicitly minimize over paths, understanding why this fails would provide scientific insight into the nature of the learned distance and the difficulty of TD learning for MAD.

### Trivial

- None.

## Nice-to-Haves

- An ablation isolating the contributions of the quasimetric, the scale-invariant loss, and the contrastive term (e.g., MadDist with a symmetric metric vs. d_simple, or with/without L_r) would strengthen the understanding of which components drive performance. If these exist in the (stripped) appendix, the authors should consider moving key results to the main text.
- A controlled experiment on an environment where random-walk distance and shortest-path distance decouple (e.g., a "dumbbell" MDP or a graph with a narrow bridge) would help demonstrate what quantity MadDist actually learns and distinguish between recovering the MAD vs. the trajectory distance.

## Removed Points

These points were flagged for removal but are provided for reference; treat them with caution.

- *"The paper's central claim is that MadDist learns the Minimum Action Distance (MAD). However, the loss function directly optimizes the learned distance toward the observed trajectory distance j−i... Minimizing the error to an upper bound does not recover the lower bound."* — **Removed as too strong.** The paper's empirical results (high correlation with ground-truth MAD) contradict the claim that MadDist simply learns the trajectory distance. The critique distills to a reasonable request for clearer theoretical justification, which I have preserved in the Major weaknesses. The framing as a "fundamental misalignment" or "fatal flaw" is not supported given the empirical evidence and the extensive use of similar formulations in published prior work (Steccanella & Jonsson, 2022).

- *"TDMadDist *does* include a mechanism to extract a minimum over paths via bootstrapping... If learning the MAD were the source of success, TDMadDist should outperform MadDist."* — **Demoted to context in the existing Major weaknesses.** This inference assumes bootstrapping works correctly — it could fail due to target network instability, variance of one-step targets, or other practical issues. The lack of analysis is the real problem, which I have already captured.

- *"Implausibly perfect results... A standard deviation of exactly zero across five random seeds is highly suspicious and demands explanation."* — **Demoted to Minor.** The results are not inherently implausible; the planning task could be easy enough that any reasonable distance yields success. The lack of explanation is a valid but minor concern.

- *"The NoisyGridWorld results are missing from the main text despite being introduced as a key challenge."* — **Preserved as Minor weakness.**

- *"Does the evaluation protocol allow perfect performance regardless of distance quality?"* — **Speculative with no evidence; removed.**

- *"The ablation is relegated to the appendix, which is stripped from the submission."* — **Removed per instructions: parser-stripped appendix content should not be penalized.** However, the point about moving key ablations to the main text is preserved as a nice-to-have.

- *"The paper does not test on any environment where this correlation breaks (e.g., a graph with a long corridor or a critical bottleneck)."* — **Removed as speculative.** While valid as a suggestion for future work, it is not an identified flaw in the existing evaluation. Preserved as a nice-to-have.

- *"Missing parts: The missing baseline (Steccanella & Jonsson 2022) must be added."* — **Preserved as Major weakness.** (Not a "missing related work" — it's about experimental comparison, which is valid.)

- Strength Finder points about "addressing an important problem" and generic framing — **Removed as generic/superficial.** The specific strengths (asymmetric MAD, benchmark suite, empirical performance, scale-invariant loss, downstream validation) are preserved.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the MadDist/TDMadDist performance gap raises a non-trivial question about what is actually being learned. If a method that explicitly bootstraps toward the minimum over paths (TDMadDist) performs worse than a method that simply regresses to trajectory lengths with upper-bound constraints (MadDist), this suggests either (a) the TD bootstrap introduces instability that negates the benefit of targeting the true MAD, or (b) the environments tested have properties where trajectory-length regression already recovers the MAD, making the bootstrap unnecessary. The paper does not resolve this, but it points to a potentially interesting finding about the interaction between learning objective, data distribution, and environment structure in distance learning.

## Suggestions

1. Add Steccanella & Jonsson (2022) as an experimental baseline. This is the most direct predecessor and is essential for attributing improvements to specific contributions.
2. Provide a theoretical analysis or intuitive argument for why minimizing error to the upper bound j−i (with upper-bound constraints and triangle inequality) recovers the MAD, not the expected trajectory distance. Alternatively, explicitly characterize the gap.
3. Analyze why TDMadDist underperforms — is it bootstrapping instability, target network issues, variance, or something more fundamental? This would turn a weak contribution into a valuable scientific result.
4. Resolve the seed-count inconsistency (3 vs. 5 seeds) and clarify which results use which number.
5. Add a brief discussion of the 1.00 ± 0.00 results — explain whether the planning evaluation saturates.
6. Move NoisyGridWorld results and a key ablation (e.g., symmetric vs. quasimetric distance) from the appendix to the main text.

## Score and Decision

**Originality:** The paper is the first to apply quasimetrics to MAD learning, which is a genuine but incremental advance over Steccanella & Jonsson (2022) and symmetric approaches. The simple quasimetric and scale-invariant loss are practical contributions.

**Importance of research question:** Learning state representations that capture the minimum action distance is well-motivated for goal-conditioned RL, reward shaping, and transfer learning. The question is significant.

**Are claims well supported?** Partially. The empirical results are strong, but the central claim that MadDist learns the MAD (rather than a trajectory-distance proxy) lacks a clear theoretical justification, and the missing predecessor baseline weakens comparative claims. The TDMadDist failure is not analyzed.

**Soundness of experiments:** The experimental design is generally sound (multiple environments, multiple metrics, ground-truth MAD comparison, downstream task). However, the missing baseline and seed-count inconsistency are concerns.

**Clarity of writing:** The paper is clearly written and well-structured. The method description is accessible.

**Value to the research community:** Moderate. The benchmark suite and the finding that quasimetric MAD learning works well empirically are useful. The unanswered questions about what is learned and why TDMadDist fails limit the immediate impact.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>