Now I have comprehensive calibration data. Let me synthesize everything and write the final review.

**Round 1 bracket**: The paper sits clearly above the TICL paper (5.50, most directly comparable — also proposes test-time training for SCL) and the amortized CD analysis paper (5.00). It's below the strong theory papers at 8.0. Initial bracket: **5.5–7.5**.

**Round 2 narrowing**: Compared against Zero-Shot Causal Models (6.25) — both have creative ideas with methodological gaps, but our paper has stronger empirical validation (real-world Sachs results, Table 4 stage-wise analysis, systematic ablations). Our paper is somewhat stronger. Compared against CausalRivers (7.33) — a different type of contribution (benchmarking with extensive engineering). Our paper is a methodological contribution with more novel intellectual content but less comprehensive engineering. The paper lands around **6.5**.

---

## Summary
This paper diagnoses three failure modes of static Supervised Causal Learning (SCL): fragility to distribution shifts, failure in compositional generalization, and poor transfer from synthetic benchmarks to real-world data. The authors propose TTT-SCL, a framework that at test time dynamically generates training data aligned to the specific test instance by optimizing an Alignment of Distribution (AD) metric with sparsity regularization. Their instantiation TACTIC uses stochastic graph search guided by AD to construct customized training sets, then trains an SCL model on them. Results show strong performance, particularly on the Sachs dataset where TACTIC (78.9 AUROC) substantially outperforms prior SCL (62.3).

## Strengths

- **Compelling diagnosis of compositional generalization failure**: The Component-mixed experiment (Fig. 2, Section 3.2) reveals that even when SCL models are trained on all individual components (mechanisms, graphs, noise types) in isolation, they still degrade on novel *combinations* of those components. Drops of 9–11 AUROC points (e.g., RFF_G_97.8: 100→91, Chebyshev_G_97.8: 100→90) demonstrate that SCL models memorize specific configurations rather than learning modular, recombinable causal representations. This directly motivates the shift from static pre-training to test-time adaptation.

- **The two-stage improvement in Table 4 cleanly validates the TACTIC pipeline**: The stage-wise analysis shows that (a) stochastic refinement improves over the seed graph (52.2→75.8 on Chebyshev), and (b) the SCL model trained on TACTIC-generated data further improves over the best-scoring graph from the search (75.8→83.0 on Chebyshev, 66.6→78.9 on Sachs). This progression distinguishes TACTIC from pure score-based methods and provides direct evidence that the SCL learning phase extracts value beyond what the score function alone captures.

- **Strong real-world results on the Sachs dataset**: TACTIC (Notears) achieves 78.9 AUROC on Sachs (Table 2), substantially outperforming AVICI scm-v0 (62.3), NOTEARS (61.8), PC (67.1), and all other baselines. This is the single most important piece of evidence for the claim that test-time alignment bridges the synthetic-to-real generalization gap.

- **Convincing sparsity ablation**: Table 3 shows that removing the L0 sparsity penalty (λ=0) yields consistent degradation across all settings — Chebyshev drops from 83.0 to 69.7, Sachs from 78.9 to 63.5 — validating that AD alone produces degenerate dense graphs and the sparsity term is essential.

- **Systematic factorial experimental design**: The OOD diagnosis (Section 3) systematically varies mechanism (Linear, RFF, Chebyshev), graph model (ER, SF), and noise (Gaussian, Uniform) across six test settings, isolating each shift type and making degradation patterns directly attributable to specific shift sources.

## Weaknesses

### Fatal
None.

### Major

- **Core mechanism-fitting procedure is underspecified in the main text**: The AD metric (Eq. 3) depends on fitting mechanisms via Structure-Induced Mechanism (SIM): given a candidate graph, regress each variable on its parents using D_test, then compute log-likelihood. However, the main text never specifies what model class is used for this regression (linear regression? neural network? kernel regression?). This choice is decisive — a linear fit will only align well with linear data, while an overly flexible model may assign high likelihood under many wrong graphs, undermining AD's discriminative power. Without this specification, the central engine of the method cannot be fully assessed or reproduced from the main text alone. While Appendix A may contain details, the core mechanism of a method should be self-contained in the main paper.

### Minor

- **Abstract overclaims performance**: The abstract states TACTIC "significantly outperforms existing SCL and traditional causal discovery methods" without qualification. On RFF_G, AVICI (scm-v0) achieves 97.8 vs. TACTIC's 91.8 — a clear counterexample. The paper's main text appropriately acknowledges this (line 210: "The pre-trained AVICI (scm-v0) model achieves optimal performance on the RFF_G datasets"), but the abstract's unqualified claim is misleading.

- **False claim of "theoretical results"**: The conclusion (line 270) states "Our theoretical and empirical results underscore the effectiveness of AD." The paper contains no theorems, proofs, or formal derivations. This statement should be corrected.

- **Initialization sensitivity is noted but not systematically characterized**: TACTIC (random) achieves only 58.6 AUROC on Sachs — worse than PC (67.1), GES (61.8), and AVICI (62.3). The paper acknowledges that NOTEARS initialization helps (line 210), but the dramatic gap between random (58.6) and NOTEARS-initialized (78.9) on the only real dataset raises questions about robustness. A characterization of performance across a spectrum of seed qualities would strengthen the claim of robustness.

- **The "2→3" improvement mechanism is not analyzed**: Table 4 shows that the SCL model trained on search-generated data outperforms the best search-found graph (e.g., 75.8→83.0 on Chebyshev, 66.6→78.9 on Sachs). This is the paper's most interesting result, but *why* it happens — whether the SCL model averages across the graph distribution, denoises spurious edges, or learns patterns the score function misses — is left as a black-box observation rather than an analyzed phenomenon.

- **The SCL model architecture in TACTIC is not explicitly named in Section 4**: Section 3.1 states AVICI is the backbone, but Section 4.3 never restates which SCL model is trained on the generated data. While inferable from context, this leaves an avoidable ambiguity.

### Trivial

- Standard deviations are reported for synthetic datasets but absent for Sachs and Syntren in Table 2. While standard for single real-world test instances, an explicit note would clarify.
- The acceptance criterion α = min[1, score(G^{k+1})/score(G^k)] (Fig. 3) is defined without discussion of edge cases, though in practice both scores are typically negative (log-likelihood minus sparsity penalty), making the ratio well-defined.

## Nice-to-Haves

- The computational cost of test-time graph search plus SCL training should be mentioned in the main text (even a rough order-of-magnitude estimate), so readers can assess practical feasibility without consulting Appendix F.
- Error-type analysis for the 2→3 stage (e.g., whether the SCL model systematically corrects false positive edges, false negative edges, or orientation errors compared to the highest-scoring graph) would transform a compelling black-box result into a genuine insight.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that the acceptance criterion α is "ill-defined when scores cross zero"**: AD is log-likelihood (typically negative) and sparsity subtracts further, so both scores are negative in practice and their ratio is well-defined. The edge case of sign crossing is theoretically possible but practically unlikely; this concern is overblown.
- **Harsh Critic claim that diagnostic claims overstate what data supports regarding compositional generalization**: The Harsh Critic claimed the average drop is "~6 points." The actual drops are 4, 9, 3, 11, 10, and 10 — averaging ~7.8 points, with several drops over 10 points. The paper's characterization as "failure in compositional generalization" is reasonable.
- **Harsh Critic concern about bnlearn results relegated to Appendix G**: Per hard rules, Appendix content is stripped by the parser and cannot be flagged as missing.
- **Strength Finder's generic claim about "clear conceptual framing"**: Merged into the existing strengths; the diversity-concentration framing is genuinely useful but not a separate strength.

## Novel Insights

The Component-mixed experiment is a genuinely novel diagnostic contribution. Rather than simply showing that distribution shift degrades SCL (which is expected), it isolates *compositional* generalization — the model is trained on all individual components but fails on their novel combinations. This reveals that SCL models do not learn modular representations of (graph, mechanism, noise) factors but instead memorize specific configurations. This finding has implications beyond this paper: it suggests that simply scaling up the diversity of static pre-training data (as proposed by Montagna et al., 2024) is fundamentally insufficient, because the combinatorial explosion of component combinations makes exhaustive coverage impossible. The TACTIC approach of generating aligned data at test time is a principled response to this diagnosis, and the two-stage improvement in Table 4 demonstrates that the SCL phase extracts structural knowledge beyond what the search score alone captures — a phenomenon that warrants deeper investigation.

## Suggestions

- Specify the regression model class used for SIM in the main text (a single sentence would suffice) and justify the choice.
- Correct the "theoretical results" claim in the conclusion — replace with "empirical results."
- Qualify the abstract's performance claim to acknowledge the RFF_G case where AVICI outperforms TACTIC.
- Add a brief error-type analysis for the 2→3 stage — this would transform the most interesting result from a black-box observation into an insight about what the SCL model learns from the graph search trajectory.
- Characterize initialization sensitivity by testing TACTIC with seeds of varying quality (random, PC, GES, NOTEARS, empty graph) to clarify when the method works and when it requires a competent seed.

---

## Calibration Anchor Summary

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| WM5G2NWSYC (Projected Subnetworks) | 2.00 | R1 | Unrelated topic, clearly weaker |
| p1b96KC6rj (Sources of Gain) | 2.17 | R1 | Different domain (CADR), clearly weaker |
| lt6xKGGWov (Feature Selection) | 2.33 | R1 | Unrelated topic, clearly weaker |
| AvXrppAS2o (Best of Both Worlds) | 3.00 | R1 | Related causal learning, weak results/baselines, clearly weaker |
| Gp6VU0oJX3 (Causal OSDA) | 3.67 | R1 | Different causal domain, weaker |
| 7f5hNhzVAe (Causal Invariant BNN) | 4.00 | R1 | Related domain generalization, weaker |
| lQYi2zeDyh (Demystifying Amortized CD) | 5.00 | R1 | Related SCL analysis, limited to bivariate, weaker |
| Lxst78Rrwj (Distributional Invariance) | 5.00 | R1 | Different approach to CD, weaker |
| ZXs3pkmrRG (TICL) | 5.50 | R1/R2 | **Most related** — also TTT for SCL but for interventional data; our paper is stronger in motivation, experiments, and presentation |
| HBf6HFnpmH (Challenging Growth) | 5.50 | R2 | Benchmarking paper, different genre, our paper stronger |
| iaP7yHRq1l (Robustness of Diff CD) | 5.50 | R2 | Benchmarking paper, different genre |
| x3F8oPxKV2 (Zero-Shot Causal Models) | 6.25 | R2 | Comparable — creative idea with methodological gaps; our paper has stronger empirical validation |
| nmvmPIi185 (Neural Causal Graph) | 6.25 | R1 | Different approach (intervenable classification), comparable quality |
| dxI1HLatWw (Generalized TD) | 6.25 | R2 | Unrelated topic |
| zwMfg9PfPs (Out-of-Variable) | 6.75 | R2 | Different topic (OOV generalization), somewhat stronger |
| iad1yyyGme (CausalTime) | 6.75 | R1 | Benchmarking paper, different genre, somewhat stronger |
| wmV4cIbgl6 (CausalRivers) | 7.33 | R1 | Benchmarking with extensive engineering, different genre, stronger |
| xByvdb3DCm (Selection+Intervention) | 8.00 | R1 | Strong theory paper, clearly stronger |
| 3cuJwmPxXj (Identifiable Repr.) | 8.00 | R1 | Strong theory paper, clearly stronger |
| TPZRq4FALB (Multi-modal TTA) | 8.00 | R1 | Different topic, clearly stronger |

**Round 1 bracket**: 5.5–7.5. **Round 2 narrowing**: Our paper is stronger than the 5.50 anchors (especially TICL, the most directly comparable) and comparable to or slightly better than the 6.25 Zero-Shot Causal Models paper. It does not reach the 7.33 level of well-engineered benchmarking contributions. **Final score: 6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>