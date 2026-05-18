Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper introduces FlightBench, the first open-source benchmark that provides head-to-head comparisons between learning-based and optimization-based methods for ego-vision-based quadrotor navigation. It includes two learning-based methods (Agile, LPA), three optimization-based methods (Fast-Planner, EGO-Planner, TGK-Planner), and two privileged upper-bound baselines (SBMT, LMT). The benchmark contributes three novel task difficulty metrics — Traversability Obstruction (TO), View Occlusion (VO), and Angle Over Length (AOL) — and evaluates methods across six performance metrics in eight test cases spanning Forest, Maze, and Multi-Waypoint scenarios.

## Strengths

1. **First unified benchmark bridging learning-based and optimization-based ego-vision quadrotor navigation.** As shown in Table 1, FlightBench is the only open-source benchmark that simultaneously covers 3D scenarios, classical methods, learning methods, and vision-based sensory input — whereas existing benchmarks (MRBP, Bench-MR, PathBench, Gibson Bench, OMPLBench, RLNav, Plannie) each miss at least one of these dimensions. This fills a clear gap in the community.

2. **Novel, quantifiable task difficulty metrics (TO, VO, AOL) with formal definitions.** The paper proposes three grounded metrics that capture distinct challenges: limited traversable space (TO), field-of-view occlusion (VO), and path sharpness (AOL). These are defined in Equations 1-3 and enable constructing test cases with graded difficulty (Table 2). The correlation analysis (Figure 4) shows that AOL correlates with motion quality metrics above 0.9 for privileged methods, and VO/AOL correlate strongly with success rate for ego-vision methods — supporting that these metrics capture real performance bottlenecks.

3. **Detailed experimental analysis exposing specific strengths and weaknesses of each paradigm.** The evaluation reveals nuanced findings: learning-based methods achieve high success in the Forest scenario but drop sharply in Maze/MW (e.g., LPA success 0.30 in Maze); optimization-based methods maintain much lower acceleration and jerk even in challenging scenarios (Fast-Planner avg. jerk 0.19 in Forest vs. LPA's 1.14×10⁴). The multi-platform computation time analysis (Table 4) shows learning methods can achieve faster inference (LPA: 1.395ms total on desktop) while EGO-Planner's local replanning yields competitive planning time (0.510ms). The latency randomization experiment (Table 5) revealing that training with 25-50ms simulated delay improves success rate from 0.3→0.9 for LMT is a practically valuable finding.

4. **Inclusion of privileged baselines (SBMT, LMT) as upper bounds.** These methods with global obstacle information set clear performance ceilings (SBMT 15.25 m/s in Forest, LMT 0.9 success in Maze), providing a concrete reference for how much room ego-vision methods have for improvement — a design absent from most navigation benchmarks.

## Weaknesses

### Major

- **Uncontrolled flight speed confounds main comparative results (Table 3).** The paper states "we standardize the expected maximum speed at 3 m/s for a fair comparison" but exempts SBMT, LMT, and LPA "whose flight speeds cannot be manually controlled." In Table 3, LPA achieves 8.96 m/s in Forest while optimization methods are capped at ~2.5 m/s. Since LPA is one of the two learning-based methods being directly compared against optimization baselines, the central claim that "learning-based methods excel in high-speed flight" is at least partly tautological — LPA simply isn't speed-constrained. The separate speed analysis (Section 4.2.2 and Figure 2) partially mitigates this by studying success rate at varying speeds, but the main evaluation table remains confounded for the LPA-vs-optimization comparison. The privileged methods (SBMT, LMT) being unrestrained is less problematic since they serve as upper-bound references rather than direct comparables, but LPA's exemption is a genuine fairness issue.

### Minor

- **Correlation analysis relies on only 8 test cases without uncertainty quantification.** The correlation coefficients (Figure 4) between difficulty metrics and performance metrics are computed across 8 data points (3 Forest + 3 Maze + 2 MW). While the strongest reported correlations (e.g., AOL vs. curvature > 0.9) would be statistically significant even with n=8, the broader claims that the difficulty metrics "effectively capture challenges" would be substantially stronger with more test configurations. No confidence intervals or p-values are reported. The heatmaps also average across methods, conflating between-method and within-method variance. This analysis is the primary validation of the proposed difficulty criteria.

- **Average curvature definition contains a mathematical error in exposition.** The formula in Section 3.3 defines $\bar{\kappa} = \frac{1}{L} \int_0^T \kappa(t) \mathbf{v}(t) \, \mathrm{d}t$, where $\kappa(t)$ is a scalar and $\mathbf{v}(t)$ is a vector, yielding a vector quantity — inconsistent with the scalar values reported in Table 3 (e.g., 0.06 m⁻¹). The intended quantity is almost certainly a scalar arc-length weighted average (e.g., $\bar{\kappa} = \frac{1}{L} \int_0^T \kappa(t) \, ||\mathbf{v}(t)|| \, \mathrm{d}t$). This appears to be a typo in the paper's exposition (the implementation likely computes a scalar), but should be corrected.

- **No error bars or variance measures.** Each metric is averaged over ten independent runs (Section 4.1), but no standard deviations or confidence intervals are reported for any of the numerical results in Tables 3-5. Given the stochasticity of RL policies and the variability of optimization solvers, this omission makes it impossible to assess whether observed differences between methods are meaningful.

- **Latency experiment limited to one test case and two methods.** The latency randomization finding (Section 4.4) is demonstrated on a single test case (MW test 2) and only for RL-based methods (LMT, LPA). The imitation-learning method Agile is not tested. While the finding is suggestive, the claim that "integrating latency randomization is essential" would be more convincing across multiple scenarios and method types.

- **Limited method coverage.** The benchmark includes only two learning-based methods and three optimization-based methods from a single research lineage. Notable omissions include Champion (Kaufmann et al. 2023), which is cited but not implemented. This is acknowledged as a limitation, but for a "comprehensive benchmark," broader coverage would strengthen the contribution.

### Trivial

- **Mapping time for learning methods conflates trivial preprocessing with heavy mapping.** In Table 4, the mapping time for learning methods includes "converting images to tensors and pre-processing quadrotor states," which is not directly comparable to the occupancy grid/ESDF mapping of optimization-based methods. The paper notes this, but the column labeling could be clearer.

## Nice-to-Haves

- The difficulty metrics (VO, AOL) are validated only through correlation analysis. A stronger validation would test whether methods that explicitly reason about occlusion or sharp turns perform better at high-VO or high-AOL tests, providing causal rather than correlational evidence.
- Generating a larger set of random test configurations (e.g., by randomizing obstacle placements) to obtain more stable correlation estimates would substantially strengthen the validation.
- The computation time comparison could benefit from noting that the Jetson measurements do not account for power or thermal constraints that could affect real-time performance.

## Removed Points

- **Reproducibility concerns about missing appendix / code links.** The reviewer noted that implementation details and code links appear only in the appendix. Per the hard rules, the appendix exists in the original submission but was stripped during parsing. The paper's reference to \Cref{appx:implementation} is standard practice.

- **Criticism that the paper's "comprehensive benchmark" claim is undermined by the number of methods.** Per hard rules, I am instructed to REMOVE criticisms that evaluate the paper against the wrong class of expectations. This is a benchmark paper; the method set is defensible as an initial comprehensive comparison, and expanding methods is a natural direction for future work, not a fatal flaw. (The specific mention of missing Champion is kept as a Minor weakness above, but the broader "not comprehensive enough" framing is removed as scope-creep.)

- **Criticism that the correlation "is not statistically significant" at 0.7.** The reviewer's hypothetical about 0.7 is a strawman — the paper's actual strongest claims are about correlations above 0.9, which ARE significant even with n=8. The valid concern is about sample size and confidence intervals, not about significance of the reported values.

- **Criticism about power/thermal constraints on Jetson.** This is a minor ask that would not change the accept/reject judgment.

## Novel Insights

The most interesting finding that emerges across the reviews is the asymmetry in where the two paradigms succeed: learning-based methods dominate in high-speed regimes specifically because their end-to-end architecture bypasses the latency bottlenecks of hierarchical planning (mapping → planning → control). The latency experiment (Table 5) quantitatively links this architectural advantage to a concrete vulnerability — when realistic ROS communication delays are introduced, the performance gap narrows dramatically unless the learning policy is trained with randomized latency. This suggests that the "speed advantage" of learning-based methods may be as much a systems/engineering finding as an algorithmic one, and that optimization-based methods with carefully optimized local replanning (EGO-Planner's 0.510ms planning time on desktop) can match or exceed learning-based inference speed when well-designed. The paper's own data thus paints a more nuanced picture than the headline "learning excels at high speed."

## Suggestions

1. **Resolve the speed confound.** The simplest fix is to report two versions of the main comparison table: one with all methods at their natural speeds (current version), and a second where LPA's velocity is actively clipped during deployment to match the 3 m/s ceiling of optimization methods. If clipping degrades LPA's performance, that itself is an informative result about the robustness of end-to-end policies to speed constraints.

2. **Expand the test set for correlation analysis.** Generate 20-30 random obstacle configurations spanning the difficulty space (varying obstacle density, corridor width, turn angle). Even evaluating a subset of methods on these would produce much more reliable correlation estimates. If this is infeasible, add bootstrap confidence intervals and clearly caveat the analysis as exploratory.

3. **Report standard deviations for all numerical results.** At minimum, provide std. dev. for success rate (based on the 10 independent runs already conducted) and for computation times. This is standard practice for a benchmarking paper.

4. **Fix the curvature metric formula.** Correct to a scalar arc-length weighted average: $\bar{\kappa} = \frac{1}{L} \int_0^T \kappa(t) \, ||\mathbf{v}(t)|| \, \mathrm{d}t$ (or the equivalent arc-length parameterization).

5. **Expand the latency experiment** to include at least one additional scenario and the Agile method, or temper the claim from "is essential" to "is highly beneficial."

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>