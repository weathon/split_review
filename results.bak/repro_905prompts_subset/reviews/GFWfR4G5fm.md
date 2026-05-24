Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize the final review.

**Round 1 bracket**: After the initial calibration search, I determined the paper sits between 5.0 and 6.5 — above the weak anchors (~3.0–3.25) which are reject-level papers with clear flaws or very narrow scope, and below the strong anchors (~8.0) which are well-executed papers with no significant methodological gaps.

**Round 2 narrowing**: I compared against the most relevant anchor — TICL (Test-Time Learning of Causal Structure from Interventional Data) at score 5.50, Reject — which also uses TTT for causal discovery but was criticized for limited novelty, unclear presentation, and no real-world validation. The current paper is stronger on real-world validation (Sachs, SynTReN vs. only bnlearn), has a conceptual contribution (three-limitations analysis), but shares similar methodological specification issues. Against the Zero-Shot Learning of Causal Models anchor (6.25, Reject), the current paper has stronger empirical validation but weaker theoretical development. Against Demystifying amortized causal discovery (5.00, Reject) and Causal Graph Learning via Distributional Invariance (5.00, Reject), the current paper is clearly ahead. Against Meta-Learning Bayesian CD (6.00, Accept), the papers are comparable in strength though different in contribution type.

**Final score**: 6.0 — a paper with a genuine contribution and strong empirical results, but with significant specification issues that prevent full evaluation without revision.

---

## Summary

This paper identifies three fundamental limitations of static supervised causal learning (SCL) — fragility to distribution shifts, failure in compositional generalization, and a synthetic-to-real performance gap — then proposes the TTT-SCL framework that dynamically generates causally aligned training data at test time. The framework is instantiated as TACTIC, which uses an Alignment of Distribution (AD) metric with sparsity constraints and stochastic graph refinement to construct customized training sets. TACTIC achieves strong results on synthetic benchmarks and substantially outperforms prior methods on the real-world Sachs dataset (78.9 AUROC vs. best prior 67.1) and the SynTReN dataset (80.1 vs. best prior 65.4).

## Strengths

- **Systematic identification of three specific limitations of static SCL.** Section 3 provides controlled experiments showing that AVICI (scm-v0) degrades under mechanism shifts (e.g., RFF_G from 90 to 74), fails at compositional generalization (Component-mixed always below i.i.d.), and collapses from 97.8 on RFF_G to 62.3 on Sachs. These experiments are well-designed and clearly demonstrate why static pre-training is problematic, independently motivating the shift to TTT.

- **TACTIC achieves substantial improvements on real-world and pseudo-real data.** Table 2 shows TACTIC (Notears) at 78.9 AUROC on Sachs (vs. PC at 67.1, AVICI at 62.3) and 80.1 on SynTReN (vs. AVICI at 65.4). These are large, practically meaningful gaps that directly support the paper's claim of addressing the real-world applicability problem.

- **Ablation and stage-wise analysis cleanly validate the design choices.** Table 3 shows removing the sparsity penalty degrades performance on every setting (e.g., Chebyshev_G from 83.0 to 69.7, Sachs from 78.9 to 63.5). Table 4 demonstrates that both the search (seed→highest-score) and the supervised learning stage (highest-score→final SCL) contribute meaningful improvements — e.g., on Sachs: 61.8 → 66.6 → 78.9 — proving that the SCL training adds value beyond what any single graph from score-based search provides.

## Weaknesses

### Major

- **The stochastic search acceptance rule as written is incoherent.** Figure 3 specifies α = min[1, score(G_{k+1})/score(G_k)]. Since AD is a log-likelihood (typically negative) and the sparsity penalty is subtracted, scores are negative. For two negative scores, the ratio behaves pathologically: a better (less negative) graph *decreases* the acceptance probability (e.g., -5/-10 = 0.5), while a worse graph is always accepted (ratio > 1 → α = 1). Standard Metropolis–Hastings would use exp((score(G') − score(G))/T) or a Boltzmann factor. The text says "accepted with probability proportional to its score" — which differs from the figure. The paper must clarify the actual acceptance rule used and cite a standard formulation. If the implementation differs from the figure, the figure must be corrected. This does not necessarily invalidate the empirical results (the authors may have used a different rule in code), but as presented, the method cannot be evaluated or reproduced.

- **The AD likelihood computation is underspecified.** Equation (3) defines AD(G, D) = (1/d) Σ log p(X_i | f_i^k), but the paper never states what noise/residual distribution is assumed when evaluating this likelihood. The forward-sampling step mentions "standard Gaussian noise" by default (Section 4.2), but the likelihood evaluation for AD could use a different assumption (e.g., Gaussian with estimated variance, nonparametric estimation). Different choices change the score landscape and thus the search behavior. The paper does not specify whether residuals are assumed homoscedastic, how variance is estimated, or what happens when likelihood assumptions are misspecified (e.g., Uniform noise with a Gaussian likelihood model, as in Linear_U). This must be clarified for reproducibility.

- **The key hyperparameter λ is not reported.** Equation (5) defines score(G) = AD(G, D) − λ·Sparsity(G). The ablation removes sparsity (λ=0), but the non-zero λ value used for all main results is never stated. Since Table 3 shows performance critically depends on this trade-off, the paper must report λ and ideally provide a sensitivity analysis. Without this, the reader cannot assess whether the method requires careful per-dataset tuning.

### Minor

- **Number of search iterations not specified.** The paper states K=200 training instances are collected, but not the number of refinement steps, how many edge modifications are proposed per iteration, or how the chain length is determined. These details are needed to assess algorithmic effectiveness and cost.

- **Standard deviations not reported for real datasets.** Tables 2–3 report standard deviations for synthetic benchmarks (with multiple seeds) but not for Sachs and SynTReN, which appear to be single runs. Bootstrapping over subsamples would provide variance estimates and strengthen these results.

- **AVICI (scm-v0) outperforms TACTIC on RFF_G (97.8 vs. 91.8).** The paper acknowledges this candidly, which is commendable. It should be noted that on in-distribution synthetic data where the static model was explicitly trained, TACTIC incurs a ~6-point AUROC gap. The paper's real-world improvements are the main message, but this trade-off should be discussed more directly.

### Trivial

- The term "Structure-Induced Mechanism (SIM)" is introduced informally in Section 4.1 but could benefit from a concise formal definition.
- The paper would benefit from pseudocode for the search procedure.

## Nice-to-Haves

- A sensitivity analysis for λ across multiple datasets would strengthen the practical argument significantly.
- Wall-clock time or FLOP comparisons against baselines would contextualize the performance gains, since TACTIC involves NOTEARS preprocessing + score evaluation per proposal + SCL training per test instance.
- A diagnostic comparing K=200 against smaller/larger values would help understand when performance plateaus.
- Comparing the final SCL output against training the SCL model on the single highest-score graph (rather than the set of K graphs) would isolate the benefit of using multiple graphs.

## Removed Points

These points were raised by reviewers but removed or downgraded in the final review:

- **"Component-mixed definition is vague"** — The paper's definition ("contains all individual components seen in isolation, but excludes the specific combinations present in test instances") is sufficiently clear for the purpose. Additional details can be in the appendix.
- **"SIM not formally defined"** — The paper defines SIM operationally ("regress mechanisms from D_test given a candidate graph, then forward-sample"). While not a formal mathematical definition, it is adequate for a systems paper. A brief formalization could improve clarity.
- **"Only AVICI backbone used for limitations analysis"** — The paper explicitly states results with other backbones are consistent and in Appendix C. Whether this is sufficient is a judgment call; the main claim in Section 3 is about SCL generally, and showing it with one representative backbone is acceptable for the space budget.
- **"Missing related works"** — Insufficient basis to include; the paper's related works section covers the key SCL and causal discovery literature.
- **Formatting/style nitpicks** — Removed per protocol as parser artifacts or minor presentation preferences.

## Novel Insights

None beyond the paper's own contributions. The core insight — that test-time generation of causally aligned training data can outperform static SCL pre-training — is the paper's own contribution; the reviews do not surface a new perspective beyond what the authors already articulate.

## Suggestions

1. **Fix the acceptance rule specification.** Clearly state whether α = min[1, exp((score(G') − score(G))/T)] (Boltzmann), α = min[1, score(G')/score(G)] with a constraint ensuring positivity, or something else. Align the text, figure, and (implied) implementation.

2. **Report λ for all experiments and add a sensitivity analysis.** Show performance over a range of λ values on at least 2–3 datasets to confirm the method is not brittle.

3. **Specify the likelihood computation.** State the residual distribution, variance estimation procedure, and any regularization used in computing log p(X_i | f_i^k).

4. **Add search procedure details:** number of iterations, proposal distribution, burn-in if any.

## Score and Decision

**Round 1 bracket**: 5.0–6.5 (based on comparison against anchor papers in weak [<3.5], middle [3.5–7.5], and strong [>7.5] bands).

**Round 2 narrowing anchors**:
- *TICL* (ZXs3pkmrRG, 5.50, Reject): TTT for causal discovery from interventional data. Current paper has stronger real-world validation and identifies three distinct SCL limitations, but shares underspecification issues. Slightly stronger.
- *Demystifying amortized CD* (lQYi2zeDyh, 5.00, Reject): Analytical paper, bivariate only, no new method. Current paper is clearly stronger.
- *Zero-Shot Learning of Causal Models* (x3F8oPxKV2, 6.25, Reject): Strong amortized approach but strong assumptions (known graphs, noise). Comparable but current paper has better real-world validation.
- *Meta-Learning Bayesian CD* (eeJz7eDWKO, 6.00, Accept): Solid but incremental Bayesian method. Comparable strength.
- *Causal Graph Learning via Distributional Invariance* (Lxst78Rrwj, 5.00, Reject): Clear method with theoretical gaps. Current paper is stronger.

**Final**: The paper sits between the 5.50 (TICL) and 6.25 (Zero-Shot) anchors — closer to 6.0 given the real-world validation and conceptual contributions, but held back by methodological specification issues.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>