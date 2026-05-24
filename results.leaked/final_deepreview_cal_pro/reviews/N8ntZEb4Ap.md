Now I have a solid calibration anchor set. Let me synthesize everything into the final review.

**Round-1 bracket**: Based on anchors at ~3.0 (weak), ~4.5-5.25 (middle), and ~8.0 (strong on different topics), the paper plausibly sits in **5.0–6.5**.

**Round-2 anchors** read in full:
- RelChaNet (5.25): similar domain (neural FS), 9 datasets, rejected — AutoNFS is stronger in experiment breadth and clarity
- difFOCI (6.00): differentiable FS, accepted — comparable but with better theoretical grounding; AutoNFS has more extensive experiments but weaker baselines
- NAMformer (5.25): tabular interpretability, rejected — AutoNFS is more polished but has analogous evidential gaps

AutoNFS is clearly above RelChaNet (5.25) and comparable to or slightly below difFOCI (6.00). The missing neural baselines and under-supported complexity claim keep it from reaching 6.0+. Final score: **5.5**.

---

## Summary

AutoNFS proposes a neural feature selection method that uses Gumbel-Sigmoid relaxation with a sparsity penalty to learn a feature mask end-to-end with a predictive task network. Its key practical innovation is automatically determining both *which* features to select and *how many*, eliminating the need for a user-specified feature budget. The method is evaluated on 11 OpenML benchmarks under three corruption scenarios and 24 real-world metagenomic datasets, where it generally maintains or improves predictive performance while substantially reducing dimensionality.

## Strengths

- **Automatic feature budget determination is a genuine and well-demonstrated contribution.** The selection penalty (Eq. 3) allows the model to learn the feature count during training rather than requiring manual specification. Tables 1 and 2 show substantial dimension reduction (e.g., from 128 to 65 for aloi, from an average of 535 to 41 features across metagenomic datasets) while maintaining or improving downstream accuracy. This is the paper's clearest advance over methods that require a pre-specified k.

- **Extensive empirical evaluation across diverse settings.** The paper evaluates on 11 OpenML datasets under three controlled corruption scenarios (random, corrupted, second-order), plus 24 real-world metagenomic datasets — a substantially broader evaluation than most FS papers in this space. The benchmark follows a well-established protocol from Cherepanova et al. (2023), and results are reported with both classification and regression tasks.

- **Insightful feature selection quality analysis.** The misselection error analysis (Figure 3a) and feature importance ablation (Figure 3b) go beyond simple accuracy comparisons to characterize *what* the method selects and whether selected features are genuinely important. Zero misselection errors on random/corrupted features and the 0.313 average performance drop per removed feature are informative.

- **Clear, well-structured method description.** The architecture, training algorithm (Algorithm 1), temperature annealing schedule, and inference procedure are all clearly laid out. The paper is well-written and easy to follow.

## Weaknesses

### Major

- **Missing direct neural feature selection baselines.** The paper's related work section discusses STG (Yamada et al., 2020b), Concrete Autoencoders (Balin et al., 2019), and INVASE (Yoon et al., 2018) — all differentiable neural feature selectors that use continuous relaxations similar to AutoNFS. Yet none of these appear in the experimental comparison. The benchmark includes classical methods (Univariate, Lasso, RF, XGBoost) and a few neural methods (LassoNet, Deep Lasso), but the most directly comparable differentiable selectors are absent. Without them, the paper cannot substantiate its claim of advancing the state of the art in neural feature selection. This is the single most important experiment to add.

- **Benchmark comparison confounded by unequal feature budgets.** The paper states: "all baseline methods select the same number of features as were in the initial representation (before corruption), whereas our method automatically chooses a much smaller subset" (Section 4.1). This means baselines are forced to include noisy/corrupted features while AutoNFS is not. The paper's ranking advantage (Figure 2) may therefore reflect AutoNFS's ability to drop noisy features rather than superior selection of informative ones. The paper does not evaluate any baseline at the reduced budget that AutoNFS discovers, which would be necessary to isolate selection quality from budget determination.

### Minor

- **Complexity analysis lacks necessary experimental detail.** Section 4.3 presents a scaling analysis with α≈0.08 as a key contribution, but critical details are missing: what exactly "Feature Time" measures (training? inference? end-to-end or masking network only?), how the number of features was synthetically varied across the 10²–10⁵ range, and on what hardware. The result that AutoNFS is nearly constant-time is difficult to reconcile with the architecture — the task network processes D-dimensional inputs and the masking network's output layer grows with D. If the constant overhead of the embedding processing dominates for the tested D range, the paper should explain this. As presented, the evidence does not adequately support the "nearly constant computational overhead" claim prominently advertised in the abstract and introduction.

- **No feature selection baselines on metagenomic data.** The metagenomic evaluation (Section 4.2, Table 2) compares only "full data" vs. "AutoNFS-reduced" representations for MLP and RF. Without any feature selection baseline (even a simple filter or random subset), the dimension reduction benefit cannot be specifically attributed to AutoNFS — a random subset or mutual-information filter might achieve similar compression.

- **"Minimal set" claim is overstated.** The abstract and introduction claim AutoNFS "automatically determines the minimal set of features." The method uses a hard threshold of 0.5 on sigmoid outputs after training, which is arbitrary and not justified. No formal minimality is established; the method finds a *small* set through the sparsity penalty, but "minimal" implies optimality that is not verified.

- **Masking network design is unmotivated.** The masking network takes a learned seed embedding as input and outputs a mask vector. A single learnable parameter vector would be simpler and computationally cheaper. The paper does not explain why the embedding-plus-subnetwork design is necessary or whether it provides any benefit over a simpler parameterization.

### Trivial

- **Algorithm-text inconsistency.** Equation 3 defines \(\mathcal{L}_{select} = \frac{1}{D}\sum_j m_j\), but Algorithm 1 line 14 computes it as \(\frac{1}{B}\sum_j m_j\). The normalizing constant should be consistent.

- **Naming inconsistency.** Figures use "GFS-NetWork" (Figure 2) and "GFSNetwork" (Figure 4b) while the text uses "AutoNFS." These should be unified.

- **Undefined term in figures.** "Delete2Vec" appears in Figures 4a and 4b but is never described in the text.

## Nice-to-Haves

- A hyperparameter sensitivity analysis for λ and temperature schedule summarized in the main text (the paper references Appendix F, which is stripped in the review version — but including key findings in the main body would strengthen the automatic-selection claim).
- Discussion of sensitivity to the hard threshold (σ(w_i) > 0.5); the selected set may change substantially with small threshold variations.
- Evaluation of whether a simple learnable mask vector performs comparably to the full masking network, which would justify or simplify the architecture.

## Removed Points

These points were flagged by reviewers but removed from the final review after verification against the paper:

- *"STG/Concrete Autoencoders/INVASE may not be released / cannot be independently verified"* — REMOVED. The paper cites them, they exist as published works. The issue is their absence from experiments, not their existence.

- *"The complexity exponent of 0.08 is implausible because both the masking and task network scale at least linearly with D"* — PARTIALLY REMOVED as a factual claim. The masking network's hidden layers process a fixed-size embedding (constant w.r.t. D), and only the output layer grows with D. The task network's first layer does scale linearly with D, but the claim that α≈0.08 is "implausible" is speculative. The substantive issue (insufficient experimental detail) is retained as a Minor weakness, but the claim of impossibility is removed.

- *"The paper does not specify whether hyperparameters were tuned separately for each method or kept fixed"* — REMOVED. The paper references a well-established benchmark protocol (Cherepanova et al., 2023) and describes the setup in Appendix C. This is a reasonable level of detail for the main text.

- *"No statistical significance reported for metagenomic accuracy differences"* — DEMOTED from weakness. The small differences (0.588→0.596, 0.685→0.697) are presented as maintaining performance while reducing dimensionality, not as improvements. The paper does not claim these differences are statistically significant.

- *"The method is a straightforward combination of Gumbel-Sigmoid with a sparsity penalty; novelty relative to STG or Concrete Autoencoders is not clearly delineated"* — REMOVED as a standalone weakness. This is largely subsumed by the missing-baselines weakness. The automatic feature count determination *is* a distinguishing feature that STG and Concrete Autoencoders do not provide without modification.

- *"Confidence intervals in Figure 4b are unclear about what sources of variance they represent"* — REMOVED. The figure caption states "over 5 runs," which is a sufficient explanation.

- *"Figure 2 hides absolute accuracy/NMSE values"* — REMOVED. Detailed per-dataset metrics are provided in Tables 3–5 (Appendix C), which the paper references. Rank summaries are standard for multi-dataset benchmarks.

## Novel Insights

The automatic feature budget determination through a simple cardinality penalty combined with temperature annealing is a clean and practically useful idea. The paper demonstrates that this approach works across a wide range of datasets without per-dataset tuning of λ, which is a non-trivial empirical finding. The feature importance ablation (Figure 3b) — showing that removing any single AutoNFS-selected feature causes a 0.313 average performance drop — is a compelling way to demonstrate that the method is not just selecting few features but selecting *essential* ones. However, the missing comparison against other differentiable selectors means the community cannot yet assess whether this specific combination (Gumbel-Sigmoid + cardinality penalty + annealing) is superior to alternatives like STG with an L0 penalty or Concrete Autoencoders with a reconstruction objective.

## Suggestions

1. **Add STG, Concrete Autoencoders, and at least one of INVASE/LSPIN as baselines.** This is the most important action to make the paper a credible contribution. Since these methods are cited in the related work section, the authors are already familiar with them. Run them on the same benchmark with the same evaluation protocol.

2. **Evaluate baselines at the feature budget AutoNFS discovers.** For each dataset, take the number of features AutoNFS selected and run the baseline methods restricted to that k. This would disentangle selection quality from budget determination and strengthen the claim that AutoNFS selects *better* features, not just *fewer*.

3. **Document the complexity measurement protocol.** Specify what is timed (end-to-end training? single forward pass?), how feature counts were varied (synthetic padding? different datasets?), and on what hardware. If the near-constant result arises because constant overheads dominate for the tested range, state this explicitly and qualify the claim accordingly.

4. **Add at least one FS baseline (e.g., mutual information filter, L1 logistic regression) to the metagenomic evaluation** to contextualize the dimension reduction benefit.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| lt6xKGGWov (Neural MI FS) | 2.33 | R1 | AutoNFS is substantially stronger — better method, far more experiments |
| 3qDhqj6qfu (TabKANet) | 3.00 | R1 | Different domain (tabular modeling), AutoNFS has clearer contribution |
| Ai4L058yoO (Dynamic FS revisit) | 4.50 | R1 | AutoNFS has better experiments, clearer method, real-world evaluation |
| zbpzJmRNiZ (NAMformer) | 5.25 | R1,R2 | Comparable quality; AutoNFS has broader evaluation but analogous evidential gaps |
| 3M3jtMDjUb (RelChaNet) | 5.25 | R2 | AutoNFS is clearer and has more extensive experiments; RelChaNet was rejected |
| KiN7g8mf9N (difFOCI) | 6.00 | R2 | difFOCI has stronger theoretical grounding; AutoNFS has broader experiments. difFOCI accepted — AutoNFS is slightly weaker due to missing baselines and overclaimed complexity |
| Oju2Qu9jvn (Dynamic FS with CMI) | 7.33 | R2 | Clearly stronger paper; AutoNFS is not in this tier |

**Round-1 bracket**: 5.0–6.5. **Round-2 narrowing**: AutoNFS sits between RelChaNet (5.25) and difFOCI (6.00). The missing neural baselines and under-supported complexity claim place it closer to 5.5 than 6.0. The paper has genuine strengths (automatic budget, extensive evaluation, clear method) but the experimental gaps prevent a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>