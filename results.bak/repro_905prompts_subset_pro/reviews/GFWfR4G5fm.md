Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper identifies three critical out-of-distribution generalization failures in supervised causal learning (SCL) — fragility to distribution shifts, failure in compositional generalization, and a synthetic-to-real performance gap — and proposes Test-Time Training for SCL (TTT-SCL), a framework that shifts from static pretraining to dynamically generating training data aligned with each test instance. The core operationalization is the Alignment of Distribution (AD) metric, which scores candidate graphs by how well structure-induced mechanisms fit the test data, combined with a sparsity penalty. The TACTIC instantiation uses stochastic graph refinement to search for high-scoring graphs and trains an SCL model on the resulting data. Experiments show strong performance on OOD synthetic settings and notably on real-world data (Sachs AUROC 78.9 vs. AVICI's 62.3).

## Strengths

- **Thorough and convincing experimental diagnosis of SCL generalization failures:** The paper systematically documents fragility to distribution shifts across graph structure, mechanism, and noise dimensions (Figure 2), failure of compositional generalization ("Component-mixed" results), and a dramatic synthetic-to-real gap (Table 1: AVICI drops from 97.8 on RFF_G to 62.3 on Sachs). This multi-faceted evidence, spanning multiple mechanism families and graph types, provides strong motivation for the paradigm shift to test-time training.

- **Novel TTT-SCL framework with a principled alignment metric:** The framework shifts from static diversity-seeking pretraining to per-instance test-time concentration. The AD metric (Eq. 3) operationalizes distributional alignment through likelihood under structure-induced mechanisms, and the sparsity penalty (Eq. 4) prevents degenerate dense solutions — together forming a tractable optimization target (Eq. 5). This is a genuinely new perspective on the SCL generalization problem.

- **Strong empirical results on out-of-distribution and real-world data:** TACTIC (Notears) achieves best AUROC on Linear_U (86.3), Chebyshev_G (83.0), Sachs (78.9), and Syntren (80.1), significantly outperforming the static AVICI baseline on all but the in-distribution RFF_G setting (Table 2). The consistent improvement from seed graph → highest-score graph → final SCL prediction (Table 4) cleanly demonstrates that both the AD-guided search and the supervised learning phase contribute value beyond a pure score-based search.

- **Rigorous ablation validating sparsity and the learning stage:** Removing the sparsity penalty (Table 3) causes consistent AUROC drops across all settings. The stage-wise analysis (Table 4) isolates the gains from search refinement and from the SCL model trained on generated data, confirming that each component of TACTIC is necessary.

- **Clear conceptual framing:** Figure 1 and the structured motivation (Section 3) make the paradigm shift from causal discovery → static SCL → TTT-SCL immediately accessible and well-justified.

## Weaknesses

### Fatal

None. The paper's core claims are well-supported by the evidence presented.

### Major

None.

### Minor

- **Forward sampling assumes Gaussian noise regardless of test data distribution.** The paper states (Section 4.2, Stage 3) that forward-sampled training data uses standard Gaussian noise by default, even when the test data uses different noise families (e.g., Uniform noise for Linear_U). This introduces a distributional mismatch between generated training data and test data that partially contradicts the claimed alignment. While the empirical results suggest the method is robust to this mismatch, the paper provides no analysis or justification for why a Gaussian assumption is adequate across all noise families. An ablation varying the forward-sampling noise or a discussion of sensitivity would strengthen the contribution.

- **No comparison with a simpler test-time training baseline.** TACTIC's pipeline includes stochastic graph refinement, AD scoring, and SCL model training. A baseline that generates training data directly from a NOTEARS seed graph (without the AD-guided MCMC search) and trains the same SCL model would isolate the value of the AD-guided refinement. Without this, it is unclear whether the AD metric and stochastic search are doing essential work beyond what simpler test-time data augmentation could achieve.

- **λ hyperparameter selection is not discussed.** The sparsity penalty weight λ is a critical hyperparameter balancing AD against graph sparsity, yet the paper does not state how it was chosen for experiments or provide a sensitivity analysis. While the λ = 0 ablation (Table 3) shows sparsity matters, the robustness of results to different λ values remains unknown.

- **Computational cost is not characterized in the main text.** Per-instance test-time training involves fitting regressions for each candidate graph during MCMC, forward-sampling datasets, and training an SCL model from scratch. The complexity analysis is deferred to Appendix F (stripped). Given that test-time cost is the primary trade-off for TACTIC's improved performance, the main text should at minimum provide order-of-magnitude estimates to help readers assess practical feasibility.

### Trivial

- The paper occasionally refers to "Synthren" and "Syntren" interchangeably (compare Table 1 header vs. Table 2 header), which is a minor inconsistency.

## Nice-to-Haves

- An experiment varying the regression model class used in AD computation (e.g., linear vs. non-linear) would demonstrate that TACTIC's gains are not tightly coupled to a specific inductive bias in the AD metric.
- Analysis of how TACTIC behaves when the test dataset is small (low n), where mechanism regression for AD may overfit and degrade the quality of generated training data.
- Sensitivity analysis for noise model assumptions in AD (e.g., using a Gaussian likelihood when true noise is heavy-tailed).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **AD metric insufficiently specified:** The harsh critic claimed the AD metric specification is a "structural gap" that threatens reproducibility. However, the paper explicitly states that implementation details are in Appendix A ("While there are many ways to implement AD as discussed in Appendix A, in the main text we use the implementation based on likelihood"). The appendix is stripped by the parser; this is a missing-appendix issue, not an author omission. Per review guidelines, criticisms rooted in missing appendix content are removed. The main text does provide the mathematical form of AD (Eq. 3) and the conceptual rationale.

- **"Section 3 restricted to small graphs and limited mechanism families":** The harsh critic noted that the diagnosis experiments use only 10-variable graphs. While the diagnosis is conducted at this scale, the full evaluation includes real-world data (Sachs, 11 nodes; Syntren, 20 nodes) and Appendix G (referenced in the main text) extends to bnlearn benchmarks. The criticism as stated overstates the limitation.

- **"The comparison with AVICI is not balanced because TACTIC uses test-time computation":** The harsh critic suggested this as a fairness concern. However, the paper explicitly compares against both traditional causal discovery methods (PC, GES, NOTEARS, RESIT, SCORE, NoGAM) and the strongest static SCL model (AVICI). The point of TTT-SCL is precisely to leverage test-time computation — this is the contribution, not an unfair advantage. The paper also includes the seed graph as a baseline within Table 4, showing improvement from the same starting point. This criticism is removed as a misunderstanding of the paradigm being proposed.

- **Strength Finder — generic strengths removed:** "This paper addressed an important problem" and similar framing-level strengths were removed as they lack concrete grounding in specific paper content.

## Novel Insights

A genuinely novel observation emerging from this work is that compositional generalization failure (Issue 2) — where SCL models fail on novel combinations of seen components — is a distinct and more fundamental limitation than simple distribution shift. This implies that merely scaling up diversity in pretraining is intractable and motivates test-time concentration as the correct response. This diagnosis goes beyond prior SCL critiques (e.g., Montagna et al., 2024) that attributed failures only to unseen individual components and proposed more diversity as the solution.

## Suggestions

- Include a simpler test-time baseline (e.g., generate training data from NOTEARS seed without AD-guided MCMC, train same SCL model) to isolate the value of AD-guided search.
- Add a sentence or brief paragraph in the main text characterizing the computational cost of TACTIC in orders of magnitude (even if full analysis is in Appendix F).
- Discuss the Gaussian noise assumption in forward sampling and its potential interaction with non-Gaussian test distributions.
- Report how λ was set for each experiment, even if just as a footnote or table note.

## Score and Decision

**Calibration anchors retrieved:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| ZXs3pkmrRG (TICL) | 5.50 | R1 | Our paper is clearly stronger: better motivation, more principled method, stronger real-world results |
| rW3NVhKtQ2 (TT-GREB) | 4.50 | R1 | Significantly weaker; marginal improvements, unclear theoretical foundation |
| xByvdb3DCm (Selection+Intervention) | 8.00 | R1 | Clearly stronger; formal proofs, rigorous theory. Our paper is more empirical |
| pOoKI3ouv1 (Robust agents) | 5.75 | R2 | Different area; high variance in reviews (8,1,6,8) |
| x3F8oPxKV2 (Zero-shot SCM) | 6.25 | R2 | Our paper stronger empirically; x3F8oPxKV2 had limited evaluation and scalability concerns |
| zwMfg9PfPs (OOV Generalization) | 6.75 | R2 | Comparable quality; zwMfg9PfPs has stronger theory but synthetic-only; our paper has real-world results |
| bMvqccRmKD (Causality RL) | 7.00 | R2 | Different area; strong theory + experiments |

**Round 1 bracket:** Between 5.5 and 7.5, based on TICL (5.50) below and xByvdb3DCm (8.00) above.

**Round 2 narrowing:** The paper is clearly stronger than x3F8oPxKV2 (6.25) and comparable to zwMfg9PfPs (6.75). It lacks the theoretical depth of the 7.0–8.0 tier but has stronger empirical validation than the 5.5–6.25 tier. The AD specification gap (deferred to stripped appendix) prevents a higher score, as does the absence of a simpler test-time baseline and noise-model sensitivity analysis.

**Final placement:** 6.5 — a solid contribution with clear motivation, a principled framework, and strong empirical results including real-world data. The paper would benefit from a more self-contained description of the core AD mechanism and additional ablations to isolate the value of AD-guided search, but these are addressable concerns that do not undermine the fundamental contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>