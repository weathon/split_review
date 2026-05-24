Now I have a thorough understanding of both the paper and the calibration landscape. Let me synthesize the final review.

## Summary

This paper identifies three fundamental limitations of static Supervised Causal Learning (SCL): fragility to distribution shifts, failure in compositional generalization, and a performance gap between synthetic and real-world data. To address these, the authors propose Test-Time Training for SCL (TTT-SCL), a framework that dynamically generates training data aligned with each test instance. They instantiate this as TACTIC, which uses a stochastic search over graph space guided by an Alignment of Distribution (AD) metric and a sparsity constraint, then trains an SCL model on the generated data. Experiments show TACTIC outperforms both traditional causal discovery methods and existing SCL on synthetic, pseudo-real (Syntren), and real-world (Sachs) data.

## Strengths

1. **Identifies compositional generalization failure as a fundamentally new limitation of static SCL.** While prior work (Montagna et al., 2024) attributed SCL failures to unseen individual components, this paper demonstrates (Fig. 2, Component-mixed setting) that models fail on *novel combinations* of seen components — even when all individual components appear in training. The "Component-mixed" condition consistently underperforms the i.i.d. baseline across six synthetic settings, with drops of 4–7 AUROC points. This is a clear, well-demonstrated finding.

2. **Proposes a principled framework (TTT-SCL) with a concrete instantiation (TACTIC) that achieves state-of-the-art on real-world data.** TACTIC (Notears) achieves 78.9 AUROC on Sachs (vs. best baseline PC at 67.1) and 80.1 on Syntren (vs. best baseline AVICI at 65.4). This directly addresses the real-world transfer gap documented in Table 1 (AVICI drops from 97.8 on RFF_G to 62.3 on Sachs). The ablation in Table 3 shows both the AD metric and sparsity constraint are necessary — removing sparsity drops Sachs performance from 78.9 to 63.5 AUROC.

3. **Stage-wise analysis (Table 4) demonstrates that the SCL training phase adds value beyond the score-based search.** On every domain tested, the final SCL prediction improves over the highest-scoring graph from the search (e.g., Sachs: 66.6 → 78.9; RFF_G: 88.9 → 91.8 AUROC). This is a genuinely non-trivial finding — a trained model on generated data systematically outperforms the best graph found by the search, which is the paper's most important piece of evidence for the two-stage design.

## Weaknesses

### Fatal
None.

### Major

1. **The Metropolis-Hastings acceptance probability in Figure 3 is technically problematic.** The paper presents `α = min[1, score(G')/score(G)]` where `score(G) = AD(G, D_test) - λ·Sparsity(G)`. AD is a log-likelihood (negative), and sparsity is an L0 norm (positive), so scores are generally negative. The ratio of two negative numbers is positive, but the direction is wrong: a better (less negative) score divided by a worse (more negative) score produces a fraction < 1, while a worse score divided by a better score produces a value > 1 (clamped to 1). This means the better graph is accepted with low probability and the worse graph is always accepted — the opposite of the intended behavior. A standard Metropolis acceptance would use `exp(score(G') - score(G))` when score is in log-space. This calls into question whether the stochastic refinement procedure operates as described. The paper does not acknowledge or address this mismatch.

2. **The AD metric regression model is underspecified.** The paper computes `log p(X_i | f_i^k)` where `f_i^k` is the fitting function of X_i given its parents under the candidate graph, estimated from D_test. No information is provided about the function class used for these regressions: are they linear models, neural networks, kernel methods, Gaussian processes, or nonparametric regressors? This choice determines the quality of density estimation, the computational cost, and the validity of the likelihood comparison across candidate graphs with different parent sets. Without this detail, the method is not reproducible, and it is unclear whether the AD scores are statistically well-founded.

3. **Hyperparameter λ is not specified and its sensitivity is not discussed.** The sparsity weight λ in Eq. 5 is central to balancing AD vs. sparsity. The paper mentions λ only in the ablation (λ = 0 for the "no sparsity" variant) but never states the value used in the main experiments, how it was chosen, or how sensitive results are to this choice. Given that the ablation shows removing sparsity causes a dramatic performance collapse (Sachs: 78.9 → 63.5), the sensitivity to λ is critical.

### Minor

1. **The real-world evaluation in the main text is limited to a single dataset (Sachs, 11 variables).** The paper mentions additional bnlearn benchmarks (Asia, Cancer, Earthquake, Survey) in Appendix G, but the parser has stripped the appendix. As judged from the main text alone, the claim of "real-world applicability" rests on one biological dataset of modest dimensionality. The Syntren dataset is pseudo-real (simulated from biologically plausible models, not actual experimental data), so it does not count as a second real-world benchmark. Stronger real-world evidence in the main paper would substantially strengthen the claims.

2. **No explicit comparison isolating the contribution of the search score from the SCL training.** The paper compares TACTIC (Notears) against standard causal discovery methods (PC, GES, NOTEARS, etc.) in Table 2, but NOTEARS is used only as a seed initializer. The highest-scoring graph from the TACTIC search already achieves 66.6 on Sachs (Table 4), which is higher than NOTEARS (61.8) and GES (61.8). This suggests the AD + sparsity score may be a stronger score function than what GES or NOTEARS optimize. A cleaner evidential baseline would compare this search-only graph against score-based methods *using the same evaluation protocol* to partition how much of the final gain comes from the stronger score vs. the SCL training.

3. **Stochastic refinement details are missing.** The paper states that the search "iteratively proposes local modifications" but does not specify: the number of iterations, the proposal distribution over edge additions/deletions/reversals, how the DAG constraint is maintained during proposals, or how the set of K candidate graphs is selected from the search trajectory. These details affect both reproducibility and the reader's ability to assess computational cost.

### Trivial
None beyond the formatting artifacts attributable to the PDF parser.

## Nice-to-Haves

- A theoretical or intuitive justification for why training an SCL model on data generated from candidate graphs improves over the best candidate graph itself. The paper notes that this is a "fundamental distinction" from score-based methods, but does not explain the mechanism (e.g., ensembling, denoising, implicit regularization from the SCL model).
- Runtime comparisons (wall-clock time per test instance) for the search + SCL training vs. baselines would help assess practical viability, especially given the method trains a model from scratch for each test instance.
- Adding results from the bnlearn datasets (Asia, Cancer, Earthquake, Survey) to the main paper, along with at least one additional real-world dataset beyond Sachs, would significantly strengthen the real-world evidence.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Circularity / transductive overfitting concern"** from the harsh critic. While the paper could provide more theoretical justification for the two-stage procedure, the criticism that the method "could overfit" and this "is not addressed" is speculative. The paper provides empirical evidence (Table 4) that the SCL model improves over the search output, not that it degrades. The stage-wise analysis directly addresses whether the procedure is beneficial. The critic's framing of "circular inference" is a conceptual concern, not an error identified from the paper as written. Demoted to a nice-to-have.

- **"Overclaiming and limited real-world evidence"** partially retained in Minor weakness 1 above, but the claim that TACTIC "sidesteps the OOD problem entirely" and is an "avoidance strategy" is a characterization dispute, not a technical flaw. The paper is explicit that TTT-SCL is a paradigm shift from static pre-training to dynamic adaptation, which is a legitimate approach to OOD — not an evasion.

- **"Missing baselines: TACTIC search only should be compared against GES/NOTEARS using the same score"** partially retained in Minor weakness 2 above. The harsh critic's framing that "the improvement could be entirely from the search procedure" is overly skeptical given Table 4 shows clear improvement from SCL training on top of the search. The retained weakness is a fair suggestion for cleaner ablation, not evidence that the core claim is unsupported.

- **Criticism that "the paper would also do Y" (demanding the paper solve problems outside its stated scope)** such as comparing against BIC/AIC or discussing alternative complexity penalties — these are nice-to-haves, not weaknesses.

- **Strength Finder claims about "paradigm shift"** — kept in spirit but reframed. The claim that TACTIC is a "paradigm shift" is the paper's own framing; the evidence supports it being a novel and effective approach, which is sufficient.

## Novel Insights

The most interesting observation that emerges from the reviews is the parallel between this paper's "concentration" strategy and test-time training in other ML domains (protein prediction, image classification). What distinguishes this work is that TTT in the causal setting requires *generating* the training data (graphs + synthetic observations) rather than just adapting model parameters. The two-stage improvement (search → SCL training) shown in Table 4 suggests that the SCL model acts as a denoiser or regularizer of the search output, implicitly ensembling multiple candidate graphs weighted by how well their induced data distributions match the test data. This is a genuinely different use of TTT from the standard fine-tuning paradigm and deserves explicit theoretical study. However, the paper does not develop this insight itself — it presents the empirical fact without explaining the mechanism.

## Suggestions

1. **Fix the acceptance probability formula.** Replace `score(G')/score(G)` with `exp(score(G') - score(G))` (if the score is a log-target), or define the score as a positive quantity to be maximized and clarify the acceptance rule. State clearly what quantity is being used.

2. **Specify the regression method** used to estimate `f_i^k` (the conditional densities for the AD metric). State the function class, estimation procedure, and why it is appropriate for the likelihood comparison.

3. **Report the value of λ** used in all main experiments, how it was selected (cross-validation? heuristic?), and include a sensitivity analysis (e.g., AUROC across a range of λ values for one or two datasets).

4. **Add details of the stochastic search:** number of iterations, edge proposal distribution, DAG constraint handling, and how the K=200 training graphs are selected from the trajectory.

5. **Consider moving the bnlearn results (Asia, Cancer, etc.) from the appendix to the main text** to strengthen the real-world evidence, or add at least one more real-world benchmark.

## Score and Decision

**Round 1 bracket:** The paper is clearly above weak anchors at 3.0–3.4 (papers with major novelty or validity problems) and below strong anchors at 7.0–8.0 (papers with strong theoretical grounding or comprehensive evaluation). Initial bracket: 4.5–7.0.

**Round 2 narrowing:** Compared to accepted poster papers at 6.0 (e.g., "A Meta-Learning Approach to Bayesian Causal Discovery," "Adversarial Causal Bayesian Optimization"), this paper has a clearer novel contribution (identifying compositional failure, proposing TTT-SCL) and stronger real-world empirical results. However, it has more significant underspecification issues and a technical problem with the acceptance formula that the 6.0-level anchors generally do not exhibit. Compared to the 5.8 rejected paper (OOCDM), this paper has stronger evidence for its core claims but similar levels of methodological incompleteness.

**Final score:** 5.5. The paper identifies a genuine limitation and proposes a novel, empirically effective framework. But the underspecified method details and the problematic acceptance formula are significant issues that prevent acceptance in the current form. The gap between the paper's contributions and its presentation/technical completeness is too wide for the acceptance threshold. With careful revision addressing the major weaknesses, the paper could plausibly reach acceptance level.

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Causal Structure Learning Supervised by LLM | JzFLBOFMZ2 | 3.20 | 1 | Weaker: paper has unclear contribution and flawed method; this paper is substantially stronger in both problem identification and empirical validation |
| Causal Disentangled Representation Learning | etnG659OB9 | 3.00 | 1 | Weaker: limited novelty and experiments; this paper has clearer framing and more extensive evaluation |
| Learning Latent Structural Causal Models | 0sO2euxhUQ | 4.00 | 1 | Weaker: insufficient experiments (5 variables only), no comparisons; this paper has stronger baselines and real-world validation |
| Training on test proteins (TTT for proteins) | qT0IWGqo1j | 4.25 | 1 | Comparable quality but different domain: this paper's causal discovery framing is more novel but the TTT-for-proteins paper has more extensive evaluation across 3 tasks |
| Meta-Learning Bayesian Causal Discovery | eeJz7eDWKO | 6.00 | 2 | Stronger on clarity/completeness; this paper has stronger novelty in problem framing but weaker on method specification |
| Adversarial Causal Bayesian Optimization | YcW8i9VCf5 | 6.00 | 2 | Stronger on theoretical grounding (regret bounds); this paper has stronger empirical results on real data |
| Learning Causal Dynamics Models in OO Env | 7VVGO0kuuY | 5.80 | 2 | Comparable: both have interesting ideas but significant presentation/methodological gaps; this paper has clearer contribution identification |
| Deriving Causal Order from Single-Variable Interventions | u63OVngeSp | 7.00 | 1 | Stronger: thorough theoretical guarantees and clean empirical evaluation; this paper lacks theoretical analysis |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>