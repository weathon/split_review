Now let me synthesize my final review. I have a good understanding of the paper, its strengths and weaknesses, and how it compares to calibrated anchors.

---

## Summary
This paper identifies three fundamental limitations of static supervised causal learning (SCL): fragility to distribution shifts, failure in compositional generalization, and a synthetic-to-real performance gap. To address these, it proposes Test-Time Training for SCL (TTT-SCL), a framework that dynamically generates test-aligned training data using a proposed Alignment of Distribution (AD) metric combined with an L0 sparsity constraint. The TACTIC method instantiates this via stochastic graph refinement, showing strong results on synthetic, pseudo-real (SynTREn), and real-world (Sachs) benchmarks.

## Strengths
- **Clear and convincing diagnosis of static SCL failures (Section 3).** The paper presents controlled experiments demonstrating performance degradation under graph, mechanism, and noise shifts (Figure 2), compositional generalization failure, and a striking synthetic-to-real gap (Table 1: AVICI drops from 97.8 on RFF_G to 62.3 on Sachs). This motivates the proposed framework effectively and is a contribution in its own right.

- **Principled integration of distribution alignment with causal minimality.** The AD metric (Equation 3) based on log-likelihood under structure-induced mechanisms, combined with an L0 sparsity penalty (Equation 4), forms a unified score (Equation 5) that jointly optimizes for distributional fit and causal parsimony. The sparsity ablation (Table 3) confirms that removing the penalty consistently degrades performance (e.g., Sachs drops from 78.9 to 63.5 AUROC), validating that both components are necessary.

- **Convincing stage-wise evidence that supervised re-training adds value over pure score optimization.** Table 4 shows that the highest-scoring graph from TACTIC's search improves upon the seed graph, and the final SCL model trained on the aligned data further boosts performance (e.g., RFF_G: 80.5 → 88.9 → 91.8). This directly supports the paper's central claim that using SCL on aligned instances yields better causal graphs than score-based search alone.

- **Strong performance on distribution-shifted and real-world settings.** TACTIC (Notears) achieves 78.9 AUROC on Sachs (vs. AVICI's 62.3) and 80.1 on SynTREn (vs. 65.4), and outperforms baselines on Linear_U and Chebyshev_G where static SCL fails (Table 2). These results validate that test-time alignment effectively bridges the generalization gap.

## Weaknesses

### Fatal
None.

### Major
- **Missing baseline that isolates the AD-guided search from SCL re-training.** The stage-wise analysis (Table 4) compares seed graph → highest-score graph → final SCL output, but does not report the performance of an SCL model trained directly on data generated from the seed graph alone (without any graph search). This baseline would separate the contribution of the expensive AD-guided search from the contribution of simply re-training an SCL model on any test-aligned data. Without it, one cannot tell whether the AD optimization is doing genuine work or whether the gains stem largely from the SCL re-training step itself. This is a significant evaluation gap for a paper whose central mechanism is the AD-guided search.

### Minor
- **The claim of "theoretical results" is unsupported in the main text.** The conclusion states "Our theoretical and empirical results underscore the effectiveness of AD and necessity of sparsity," but no theorems, proofs, or formal analysis appear in the main text. The paper's contributions are entirely empirical; this language should be removed.

- **AD computational implementation is described only at a conceptual level in the main text.** The paper defines AD via Equation 3 but defers the concrete regression procedure (function class, model capacity, fitting method for \(f_i^k\) via SIM) to Appendix A. The main text would benefit from at least a brief specification of the regression approach used in experiments, as this choice directly affects the AD score's behavior.

- **No computational cost discussion in the main text.** TACTIC performs iterative graph search with repeated mechanism regression, plus training an SCL model on 200 generated instances — all per test instance. Complexity analysis is deferred to Appendix F, and no wall-clock comparison against baselines appears. Readers cannot assess the practical trade-off between accuracy gains and computational expenditure from the main text alone.

- **Hyperparameter values (\(\lambda\), \(K=200\)) are stated but not justified or analyzed for sensitivity.** The paper uses these values across all domains without discussing how they were chosen, whether they transfer across settings, or how sensitive results are to their variation. A brief sensitivity note would strengthen reproducibility.

### Trivial
- The forward-sampling step uses standard Gaussian noise by default (line 178) regardless of the test data's true noise distribution. The paper acknowledges this choice explicitly but does not discuss its impact on alignment quality. This is a minor limitation worth flagging.

## Nice-to-Haves
- A scatter plot or correlation analysis linking AD scores to downstream AUROC would make the AD metric's guiding role more directly interpretable. This evidence is referenced as being in Appendix E but would strengthen the main text.
- A discussion of how the method might scale to graphs with more than 20 nodes (the SynTREn setting uses 20; Sachs uses 11) would help readers assess broader applicability.
- Clarify how the transition probability \(\alpha = \min[1, \text{score}(G^{k+1})/\text{score}(G^k)]\) behaves when scores are negative (they are, since AD is log-likelihood). While the ratio of two negative numbers is positive and thus valid, an explicit note would preempt confusion.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh critic: "The transition rule is an invalid acceptance probability."** REMOVED because it is factually incorrect. AD is a log-likelihood (always ≤ 0 for continuous densities), and subtracting λ·sparsity makes scores strictly negative. The ratio of two negative numbers is positive, so \(\alpha \in (0, \infty)\) and \(\min[1, \alpha] \in (0,1]\), which is a valid acceptance probability. No temperature parameter is required for validity.

- **Harsh critic: "Key hyperparameters are absent or implausible."** PARTIALLY REMOVED. The paper states \(\lambda\) is a hyperparameter and \(K=200\) explicitly (line 198: "we set the number of dynamically generated training graphs to \(K = 200\)"). These are present, just not justified — kept as minor.

- **Harsh critic: "The paper overclaims by referring to 'theoretical results' that are nowhere present."** Kept as a minor weakness, but the harsh critic's framing as a "fatal" or "structural" flaw is excessive — this is a sentence-level overstatement in the conclusion, not a methodological defect.

- **Harsh critic: "The AD metric is under-specified, making the method unreproducible and its core mechanism opaque — a structural flaw."** DEMOTED from fatal to minor. The main text defines AD conceptually (Equation 3, with explanation of SIM), which is standard practice for papers that defer implementation specifics to appendices. The claim that this is a "structural flaw" is overblown. The missing details (regression model class) are a presentation issue, not a validity problem.

- **Harsh critic: "The paper omits any discussion of computational cost."** DEMOTED to minor. The paper explicitly references Appendix F for complexity analysis. While the main text would benefit from a summary, this is not an omission — it is standard structuring.

- **Strength Finder: "Principled integration of a tractable distribution-alignment metric."** KEPT but note that "principled" overstates the case — AD is a reasonable heuristic, not derived from first principles.

- **Strength Finder: "Strong and consistent performance on distribution-shifted benchmarks."** KEPT as a genuine strength backed by Table 2.

## Novel Insights
The paper's diagnosis that static SCL fails not just under individual distribution shifts but also under *compositional generalization* (trained on all components separately but failing on their novel combination) is genuinely insightful. This goes beyond standard OOD analysis and reveals that current SCL models memorize training configurations rather than learning modular causal representations. This observation, while empirical, has implications for how the community should think about training data design for causal learning beyond simply scaling up diversity.

## Suggestions
- Add the missing baseline (SCL trained on data generated from the seed graph without AD-guided search) and report it in Table 4. This is the single most important addition for validating the paper's central mechanism.
- Include a one-sentence specification of the regression model used for SIM in the main text (e.g., "We use linear regression for the AD computation in all experiments").
- Remove or qualify the "theoretical results" language in the conclusion, since the paper contains no formal theorems.
- Add a brief note on approximate runtime (e.g., "TACTIC takes approximately X minutes per test instance on a d=10 graph") to give readers a practical sense of the cost.

## Score and Decision

**Round 1 bracketing:** The most similar anchor is ZXs3pkmrRG (TICL, avg 5.50), another test-time training method for SCL. Weaker anchors (3.00–3.25) have fundamental flaws our paper lacks. Stronger anchors (7.33–8.00) either have significant theoretical contributions or large-scale benchmarking value. Initial bracket: **5.0–7.0**.

**Round 2 narrowing:** Compared against ZXs3pkmrRG (5.50, TICL), our paper has clearer presentation, better-motivated experiments, and stronger results on real-world data — placing it above 5.50. Compared against x3F8oPxKV2 (6.25, zero-shot SCM), our paper has more practical focus with better empirical validation but similar issues with overclaiming and some missing detail. TACTIC is comparable to this level. Compared against iad1yyyGme (6.75, CausalTime), our paper is a methods contribution rather than a benchmarking resource with broad community value.

**Anchor comparison summary:**
- ZXs3pkmrRG (TICL, 5.50): most similar paper; TACTIC is better executed and better motivated
- lQYi2zeDyh (5.00): analysis paper limited to bivariate; TACTIC has broader scope
- Lxst78Rrwj (5.00): invariance-based causal discovery; similar empirical quality but weaker motivation
- x3F8oPxKV2 (6.25): zero-shot SCM learning; comparable quality; TACTIC's real-world validation is stronger
- iad1yyyGme (6.75): benchmark contribution; TACTIC is slightly below in community-value terms
- wmV4cIbgl6 (7.33): large-scale benchmark; TACTIC doesn't reach this level of contribution

The paper sits between 5.50 and 6.75, closer to 6.25. Accounting for the missing baseline (a genuine evaluation gap) and the "theoretical results" overclaim, I place it at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>