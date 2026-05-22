Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper identifies three fundamental limitations of static supervised causal learning (SCL)—fragility to distribution shifts, failure in compositional generalization, and a significant synthetic-to-real-world performance gap—and proposes Test-Time Training for Supervised Causal Learning (TTT-SCL), a framework that dynamically generates training data aligned with each test instance. The authors instantiate this as TACTIC, which searches the graph space via stochastic refinement guided by an Alignment of Distribution (AD) metric and sparsity constraints. Experiments on synthetic benchmarks, one pseudo-real dataset (Syntren), and one real-world dataset (Sachs) show TACTIC substantially outperforms static SCL baselines (e.g., 78.9 AUROC on Sachs vs. 62.3 for AVICI scm-v0) and traditional methods like PC and NOTEARS.

## Strengths

1. **Systematic empirical diagnosis of static SCL failures.** Section 3.2 and Figure 2 provide clear AUROC evidence across six synthetic settings that static SCL degrades under mechanism shifts (e.g., RFF_G drops from 90→74), graph shifts, noise shifts, and compositional generalization failures (Component-mixed underperforms i.i.d. across all settings). Table 1 further documents a stark synthetic-to-real collapse (AVICI drops from 97.8 on RFF_G to 62.3 on Sachs), directly motivating the proposed shift to test-time adaptation.

2. **Novel TTT-SCL framework with principled optimization target.** The paper formalizes the Alignment of Distribution (AD) metric (Equation 3) via likelihood and combines it with an L₀ sparsity penalty (Equation 4) that enforces causal minimality. The joint score (Equation 5) provides a clean optimization target that prevents degenerate dense solutions. This combination is well-motivated and addresses a genuine gap in the SCL literature.

3. **Strong empirical performance on real-world data.** Table 2 shows TACTIC (Notears) achieves 78.9 AUROC on Sachs (vs. 62.3 AVICI, 67.1 PC) and 80.1 on Syntren (vs. 65.4 AVICI). These are substantial gains that directly support the paper's central claim that test-time alignment closes the synthetic-to-real generalization gap.

4. **Ablation confirms necessity of sparsity.** Table 3 shows removing the sparsity penalty (TACTIC Notears-s) degrades AUROC consistently, most dramatically on Chebyshev_G (83.0→69.7) and Sachs (78.9→63.5). This provides controlled evidence that both AD and sparsity are needed.

5. **Stage-wise analysis distinguishes TACTIC from score-based methods.** Table 4 tracks performance from seed → highest-scoring graph → final SCL output. On Sachs, AUROC progresses 61.8 → 66.6 → 78.9. The two-stage improvement (search + supervised learning) empirically validates the TTT-SCL paradigm and shows it is not merely a score-based method in disguise.

## Weaknesses

### Fatal

None.

### Major

- **Missing error bars for real-data experiments.** Table 2 reports standard deviations for the three synthetic settings but not for Sachs and Syntren. The same is true for Tables 3 and 4. Without error bars (e.g., via bootstrapping or multiple seeds), the reliability of the claimed improvements on real and pseudo-real data (e.g., 78.9 vs. 62.3 on Sachs) cannot be assessed. This is the single most actionable weakness in the paper and should be addressed before acceptance.

### Minor

- **Stochastic graph refinement procedure is under-specified for reproducibility.** Section 4.2 describes local modifications (edge additions, deletions, reversals) accepted "with probability proportional to its score," and Figure 3 shows the Metropolis rule α = min(1, score(G′) / score(G)). However, the proposal distribution (are all edge operations equally likely?), the number of refinement iterations, and whether the DAG constraint is maintained via acyc check or a parameterization are not specified in the main text. While some details may reside in the (stripped) appendix, the main text should give enough information for a reader to implement the core algorithm.

- **Hyperparameter λ selection not discussed.** The sparsity penalty weight λ in Equation 5 is central to the AD-sparsity trade-off. The paper does not state how λ is chosen (fixed across datasets? tuned per dataset? if tuned, using what validation signal?). This gap affects reproducibility.

- **No discussion of sensitivity to the Gaussian noise assumption for forward sampling.** TACTIC fixes the noise distribution to standard Gaussian 𝒩(0,1). The method performs well on Linear_U (uniform noise), which is empirically encouraging, but the paper provides no discussion of why this mismatch is benign or whether performance degrades under different noise types. A brief empirical or theoretical comment would strengthen the method's principled justification.

### Trivial

- None beyond the points above.

## Nice-to-Haves

- **A controlled experiment distinguishing adaptation from overfitting.** While the stage analysis (Table 4) provides indirect evidence that SCL training adds value beyond the search phase, an experiment on synthetic data where a *separate held-out test set* from the same ground-truth SCM is used for evaluation would more directly rule out overfitting to idiosyncrasies of D_test. This is a standard concern for any TTT method and is not a fatal flaw, but addressing it would increase confidence.
- **A sensitivity analysis for K (number of training graphs).** The paper fixes K=200; showing whether performance is monotonic or plateaus would clarify how the refinement trades diversity for quality.
- **Results on additional real-world datasets.** The paper relies primarily on Sachs (plus Syntren, which is pseudo-real). Appendix G mentions results on bnlearn benchmarks (Asia, Cancer, Earthquake, Survey) but these results are in the stripped appendix. Including at least one additional real or pseudo-real benchmark in the main text would strengthen the claim of real-world applicability.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Component-mixed construction insufficiently specified"** — The paper clearly states it "contains all individual components (mechanisms, graph types, noise distributions) seen in isolation during training, but crucially excludes the specific combinations present in the test instances," which is sufficient for replication.
- **"AD metric assumptions not stated"** — The AD implementation is referenced to Appendix A, which was stripped by the parser. The paper explicitly says "While there are many ways to implement AD as discussed in Appendix A."
- **"Comparison only uses one SCL backbone (AVICI)"** — The paper states "Results with other backbones are consistent and shown in Appendix C" (stripped by parser).
- **"Overfitting concern is fatal"** — The stage analysis (Table 4) provides clear evidence that final SCL output improves over the highest-scoring graph, demonstrating that the method is not merely overfitting. The concern is inherent to any TTT method and is partially addressed.
- **Various formatting/style/strawman nitpicks** from the harsh critic that misunderstand or overstate issues not verifiable from the paper as written.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine concern about missing error bars for real-world data and some reproducibility gaps in the refinement procedure, but these are standard incremental observations rather than novel meta-insights.

## Suggestions

1. Add error bars (standard deviations or bootstrap intervals) for Sachs and Syntren in Tables 2, 3, and 4. This is the most impactful improvement the authors can make.
2. Specify in the main text: (a) the proposal distribution for edge operations, (b) the number of refinement iterations or a convergence criterion, and (c) how the DAG constraint is enforced during edge reversals. Alternatively, provide a clear reference to a specific appendix section with pseudocode.
3. State how λ is selected (fixed value, tuned, by what criterion) and whether it varies across datasets.
4. Add a brief discussion of why the fixed Gaussian noise assumption is reasonable even when test data has non-Gaussian noise (e.g., citing empirical robustness or identifiability theory).

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZXs3pkmrRG.md` (TICL) | 5.50 | Very similar TTT+SCL approach; current paper has stronger real-world results and more thorough ODD diagnosis |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lQYi2zeDyh.md` (Demystifying amortized CD) | 5.00 | Analysis-only paper; current paper adds a new method (TACTIC) with strong empirical validation |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AvXrppAS2o.md` (Best of both worlds) | 3.00 | Weak empirical results and marginal improvements; current paper is substantially stronger |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zwMfg9PfPs.md` (Out-of-Variable Generalisation) | 6.75 | Strong theoretical contribution with limited empirical validation; current paper is more empirically rigorous on a similar tier |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/22ywev7zMt.md` (OOD SSL) | 5.67 | Tangential topic; current paper has more novel methodological contribution |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xByvdb3DCm.md` (Selection meets Intervention) | 8.00 | Stronger theoretical contribution with complete evaluation; current paper is less deep but contributes a novel paradigm |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3cuJwmPxXj.md` (Rep4Ex) | 8.00 | Rigorous theory + empirical; current paper is more applied with somewhat less theoretical depth |

The paper makes a clear, well-motivated contribution to the SCL literature with strong empirical evidence spanning synthetic data, a pseudo-real benchmark, and a real-world dataset. The weaknesses are addressable and do not threaten the core claims. The paper is positioned above mid-range papers (5.0–5.5) but below the highest-tier theoretical papers (8.0). The missing error bars and minor reproducibility gaps are the main actionable items.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>