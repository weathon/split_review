Now I have all the information I need. Let me produce the consolidated review.

**Key observations from cross-checking the paper:**

1. The `sortranking` function is called in Algorithm 1 (line 207) but not defined in pseudocode. However, Section 7.1 (lines 176-188) describes the procedure in text: sort edges by D_ij, add greedily with acyclicity check, stop when D_ij < ϵ, take topological order. The reviewer's claim that "the algorithm calls sortranking before computing any edge matrix" is corrected by the reviewer themselves — D is computed first (lines 201-206).

2. Scale-free graph results are referenced to an appendix figure (`\cref{fig:all-plots-sf}`), which was stripped. The reviewer's criticism that these are missing is invalid.

3. The CPDAG-to-DAG conversion for PC/GIES is described only as "creating a DAG from the oriented edges" — no detail on how undirected edges are handled. This is a genuine gap.

4. No code is mentioned or provided in the paper.

Here is my consolidated review:

---

## Summary

This paper proposes a novel method for causal order discovery from single-variable intervention data. It introduces a new assumption called *ϵ*-interventional faithfulness, defines a score over permutations whose optimum provably recovers a valid causal order under this assumption, and develops Intersort, a two-step algorithm (greedy initialization + local search) that approximately optimizes this score. Experiments on simulated data spanning linear, RFF, neural network, and GRN (SERGIO) domains show Intersort outperforming PC, GIES, DCDI, and EASE across most settings.

## Strengths

1. **Novel theoretical framework with formal guarantees.** The paper rigorously defines *ϵ*-interventional faithfulness and proves that the optimum of the proposed score recovers a valid causal order when all variables are intervened (Theorem 5.3/Theorem 1). Lemma 4.2 (linear SCMs almost surely satisfy the assumption for ϵ=0) and the expected-error bounds under random intervention selection (Theorem 5.5/Theorem 2) provide a solid theoretical foundation. The relaxation to parent-based faithfulness (Section 6) extends the framework's reach and yields O(d) scaling bounds (Lemma 6.4/lemma:inf), which is valuable for large-scale applications.

2. **Addresses an understudied problem with a principled approach.** The paper correctly identifies that causal order from interventional data has received far less attention than from observational data. The approach of comparing marginal distributions via statistical distances (Wasserstein) is both intuitive and theoretically grounded, bridging benchmark observations (CausalBench) with formal methodology.

3. **Consistent empirical performance across diverse simulated domains.** Intersort shows strong and consistent results across four simulated data types (linear, RFF, NN, GRN) with varying noise distributions, graph densities, and intervention ratios. The method's robustness to data normalization (Varsortability) is a practical advantage over continuous optimization methods like DCDI. The empirical validation of near-optimum performance on small d=5 graphs (Figure 1) supports the algorithm's approximation quality.

4. **Analysis under relaxed faithfulness (Section 6).** The derivation of bounds when *ϵ*-interventional faithfulness holds only for direct parents provides theoretical robustness for settings where longer-path effects may cancel. The closed-form bound for Erdős–Rényi graphs and the O(d) scaling result add practical value.

## Weaknesses

### Fatal
None.

### Major

1. **Underspecified CPDAG-to-order conversion for PC and GIES baselines (threatens empirical claims).** The paper states it constructs causal orders from CPDAGs by "creating a DAG from the oriented edges" (Section 9), but does not specify how undirected edges in the CPDAG are oriented to obtain a DAG before computing the topological order. This is a critical methodological gap: if undirected edges are handled naively (e.g., discarded or oriented arbitrarily), the baseline D_top scores could be artificially inflated or deflated, making the claimed superiority of Intersort unreliable. A proper evaluation would specify the orientation procedure (e.g., Meek's rules) or compare using graph-level metrics (SHD) after consistent post-processing. Since this is the primary empirical evidence for the paper's central performance claim, the gap must be resolved.

2. **Algorithm specification leaves reproducibility gaps.** The `sortranking` function in Algorithm 1 is called without being defined in the pseudocode. While Section 7.1 describes the greedy edge-adding procedure in text, the algorithm box is not self-contained. Additionally, the local search stopping criterion ("once an iteration brings no improvement") is stated, but the exact mechanism for evaluating candidate permutations and tie-breaking rules are not specified. These omissions make independent reimplementation unnecessarily difficult, especially without code release.

### Minor

1. **No sensitivity analysis for key parameters (ϵ, c).** The paper uses ϵ=0.3 (linear, RFF, NN) and ϵ=0.5 (GRN) and c=0.5 throughout, but provides no analysis of how results vary with these choices. Since the score's behavior and the validity of the assumption depend on ϵ, and since c·d could dominate the distance term, this is a meaningful gap. A simple sensitivity sweep would substantially strengthen the practical claims.

2. **No statistical significance testing.** With only 10 runs per setting, some observed performance differences could be noise. The violins show distributions but formal significance tests (e.g., Wilcoxon) or confidence intervals on key comparisons would increase confidence.

3. **Wasserstein distance estimation with small interventional samples.** Only 100 interventional samples are used per intervention, and the paper does not analyze how noise in the finite-sample Wasserstein estimates affects the ordering quality. An experiment varying interventional sample size would inform practical deployment.

4. **The theory guarantees properties of the exact score optimum, but Intersort is an approximation.** The paper acknowledges this gap and provides empirical validation for d=5, but for d=30 the gap between Intersort's solutions and the theoretical optimum is not quantified. The local search (k=1) is greedy and could get stuck in poor local optima.

### Trivial
None.

## Nice-to-Haves

- **Code release** would substantially aid reproducibility, especially given the underspecified baseline conversion and algorithm details.
- **A data-driven procedure for choosing ϵ** (e.g., permutation tests, cross-validation, or analyzing the distance distribution) would make the method more practically useful.
- **Comparison to a random-order baseline** would help calibrate the difficulty of the task and contextualize the D_top scores.
- **Analysis of the bound's tightness** for the Erdős–Rényi case (Section 6) could clarify whether the theoretical guarantees are informative for realistic graph sizes.

## Removed Points

These points were flagged for removal; treat them with caution:

- **"No scale-free graph results"** — The paper explicitly references scale-free results in an appendix figure (`\cref{fig:all-plots-sf}`) which was stripped during parsing. The criticism is invalid.
- **"sortranking called before computing D matrix"** — The algorithm clearly computes D first (lines 201-206) and then calls sortranking. The reviewer corrected themself on this point.
- **"No error bars or confidence intervals"** — The paper shows violin plots (full distributions) and reports 95% confidence intervals for the d=5 experiment (Figure 1). The main experiments use violins, which are more informative than error bars for small numbers of runs.
- **Generic/superficial strength from Strength Finder about "important problem"** — Not included as it lacked specific content.
- **"The bound in Lemma 6.4... relevance to the main assumption is unclear"** — The section explicitly states it analyzes the relaxed (parent-based) setting; the bound's relevance to that setting is clearly scoped.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an important methodological observation: the gap between the theoretical guarantees (which apply to the exact score optimum under population distributions) and the practical algorithm (which approximately optimizes a finite-sample score) is a structural challenge shared by many causal discovery papers. The paper's approach of empirically validating this gap for small d is commendable, but the lack of analysis for larger d and the underspecified baseline comparison mean the practical significance of the theoretical results remains incompletely validated. The parent-based relaxation analysis (Section 6) is an interesting middle ground that could inspire future work on partial faithfulness assumptions for interventional settings.

## Suggestions

1. **Specify the CPDAG-to-order conversion in detail.** Describe exactly how undirected edges from PC/GIES are oriented (e.g., applying Meek's rules exhaustively, or using a specific consistent extension algorithm). Alternatively, compare on graph-level SHD after consistent post-processing, or use order-based baselines that don't require this conversion step.

2. **Complete the algorithm pseudocode.** Add a full specification of `sortranking` (or rename it inline), and clarify the local search's candidate evaluation and tie-breaking. Better yet, release code.

3. **Add sensitivity analysis.** Show D_top for Intersort across a range of ϵ values (e.g., 0.1, 0.3, 0.5, 0.7) and at least two values of c (e.g., 0.25, 0.5, 1.0) for one representative dataset.

4. **Report statistical significance.** Add pairwise Wilcoxon signed-rank tests or confidence intervals for the key comparisons (Intersort vs. each baseline at each intervention ratio).

5. **Study impact of interventional sample size.** Vary interventional samples (e.g., 50, 100, 200, 500) and report D_top to show robustness to finite-sample estimation noise.

## Score and Decision

The paper makes a genuinely novel contribution: it proposes the first principled method for causal order discovery from single-variable interventions, with a clean theoretical framework and formal guarantees. The core idea is compelling and the theoretical analysis is the strongest part. However, the empirical evaluation has a significant methodological gap (unspecified CPDAG-to-order conversion for baselines) that undermines the central performance claims, and the algorithm reproducibility is hampered by incomplete specification. These are addressable in revision but non-trivial. The theoretical contribution alone likely justifies the paper, but the empirical claims as presented are not fully reliable.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>