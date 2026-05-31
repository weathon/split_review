Now let me perform calibration searches for scoring.Now I have enough information to write the complete review. Let me compile my analysis.---

## Summary

The paper introduces **Test-Time Training for Supervised Causal Learning (TTT-SCL)**, a framework that addresses the out-of-distribution failures of static pre-trained SCL models by dynamically generating test-aligned synthetic training data at inference time. Section 3 provides a systematic diagnosis of three failure modes — distribution shift fragility, compositional generalization failure, and synthetic-to-real performance divergence — supported by structured experiments across six synthetic settings plus real-world data. The concrete instantiation, **TACTIC**, uses a Metropolis-Hastings-style stochastic search over DAG space guided by an Alignment of Distribution (AD) metric combined with a sparsity penalty, then trains an SCL model (AVICI) on the K=200 collected graph-data pairs. Empirical results show TACTIC achieves state-of-the-art on four of five tested distributions, with especially large gains on real-world (Sachs) and pseudo-real (Syntren) data.

---

## Strengths

- **Systematic, well-executed diagnostic section.** Figure 2 and Table 1 provide concrete, quantified evidence for all three claimed failure modes — for instance, Mechanism shift reduces Chebyshev_G AUROC from 100 to 57 for the AVICI scm-v0 model, and the AVICI scm-v0 model drops from 97.8 on in-distribution RFF_G to 62.3 on Sachs. The Component-mixed baseline tests compositional generalization specifically: it includes all individual components but withholds their combinations. This is a cleaner experimental design than most prior work on SCL generalization.

- **AD + sparsity ablation is well-structured and convincing.** Table 3 demonstrates that removing the sparsity term (λ = 0) consistently degrades performance, with Chebyshev_G dropping from 83.0 to 69.7 AUROC. The explanation — dense graphs achieve high AD by spurious edges with negligible mechanisms — is mechanistically sound and supported by Appendix E data on AD/sparsity/score tradeoffs.

- **Three-stage decomposition in Table 4 is methodologically sound.** The seed graph → highest-score graph → final SCL output trajectory is the right structure for attributing gains. The "Search Improvement" (52.2 → 75.8 on Chebyshev_G) and "Learning Improvement" (75.8 → 83.0) are cleanly separated and provide direct evidence for each stage's contribution.

- **Strong cross-distribution generalization.** TACTIC (Notears) achieves best AUROC on Linear_U (86.3), Chebyshev_G (83.0), Sachs (78.9), and Syntren (80.1) — all shifted or real-world settings — while AVICI (scm-v0) at 97.8 on RFF_G only wins on its own training distribution. This directly validates the TTT-SCL paradigm.

- **Flexible initialization demonstrates robustness.** Table 2 shows TACTIC (Notears) consistently outperforms TACTIC (random) across all settings (e.g., Sachs 78.9 vs 58.6), confirming that a warm-start seed adds value without being essential to the framework.

---

## Weaknesses

### Fatal
*None.*

### Major

- **Missing Bayesian model averaging baseline undermines the core "Learning Improvement" claim.** Table 4 is the most important ablation in the paper, but it compares the highest-scoring single graph (e.g., 66.6 AUROC on Sachs) to the final SCL output (78.9). The natural and obvious alternative to training an SCL model on K=200 chain samples is simply threshold-averaging the K adjacency matrices from the MCMC chain — i.e., Bayesian model averaging. The paper's central claim in Section 4.4 is that "this two-stage process constitutes the fundamental distinction between TACTIC and classical score-based causal discovery," but this claim cannot be evaluated without knowing whether the 12.3 AUROC gain on Sachs comes from the SCL model's generalization capacity or from ensemble smoothing that any averaging over K graphs would produce. This is an evidential gap that directly concerns the main contribution of Stage 3. The comparison is inexpensive (just average the collected adjacency matrices) and should be added.

- **Regression model used in Structure-Induced Mechanism (SIM) is never specified in the main text.** Section 4.1 defines SIM as "given a candidate graph G_train^k, we regress the corresponding mechanisms from the observed D_test," but never names the regression method. This is consequential: the choice of regressor (linear, kernel, GP, neural) determines what the AD metric actually measures, whether it is well-specified for a given mechanism class (linear vs. RFF vs. Chebyshev), and whether the method can generalize to unknown real-world mechanisms. The paper lists six mechanism types in Section 3.1 and claims good performance on all of them — but without knowing which regressor is used, this cannot be assessed or reproduced. This is not a trivial detail.

### Minor

- **AD metric's relationship to established decomposable structure scores is not discussed.** Equation 3, AD(G, D_test) = (1/d) Σ_i log p(X_i | f_i^k), is a sum of conditional log-likelihoods given parent sets — the same decomposable form as BIC, BDe, and other standard structure scores from the score-based causal discovery literature. The paper presents AD as a novel contribution ("our proposed AD metric") without noting this connection. The genuinely novel use is applying this score to guide MCMC that generates SCL *training data* rather than selecting a single output graph; but the score itself is familiar. Clarifying which aspects of AD are novel versus established would sharpen the contribution.

- **K=200 and λ are fixed design choices with no justification or sensitivity analysis.** The number of MCMC samples K=200 and the sparsity weight λ (Eq. 5) are stated but never justified, varied, or analyzed for sensitivity. K directly controls training set size and MCMC convergence; λ controls the sparsity-alignment tradeoff. For a test-time method where both parameters affect every prediction, the choice of K and λ should be at least partially justified — e.g., a performance curve over K showing diminishing returns at 200.

- **6 AUROC gap on RFF_G is understated.** TACTIC (Notears) achieves 91.8 vs AVICI (scm-v0) at 97.8 on RFF_G (Table 2). The paper describes this as "slightly lower," but 6 AUROC points on a dataset that is specifically AVICI's training distribution is a meaningful gap, especially for a method that customizes itself to *every* test instance at test time. A method with test-time concentration should at least approach in-distribution performance; that it doesn't is worth investigating. This could be explained by K=200 being insufficient, by the regression model being misspecified, or by the fixed Gaussian noise assumption — but the paper does not explore any of these.

### Trivial

- The stochastic refinement in Section 4.2 is described purely procedurally without naming the acceptance probability α = min[1, score(G_{k+1})/score(G_k)] as Metropolis-Hastings. Naming the algorithm would make the method description more precise and easier to relate to adjacent work.

---

## Nice-to-Haves

- **K-vs-AUROC performance curve.** Showing how performance changes with K (e.g., 20, 50, 100, 200, 500) would both justify the K=200 choice and characterize whether the MCMC chain has converged.
- **Mechanism regressor ablation.** Testing whether using the correct regressor class (e.g., linear regression for Linear_U, kernel regression for Chebyshev_G) vs. a universal misspecified regressor changes the performance profile would illuminate the sensitivity to SIM specification.
- **λ sensitivity analysis.** Even a small sweep on one dataset would help practitioners choose λ for new domains.
- **Scaling experiment.** Results are reported for 10–20 variables. A brief discussion of how TACTIC behaves at 50+ variables (or Appendix F's runtime curve alongside AUROC) would clarify practical applicability.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

1. **"TACTIC is essentially Bayesian structure learning" (Harsh Critic, framed as Fatal/Major).** Partly valid as observation (the acceptance probability is MH-style, the score is decomposable), but framed too strongly as a fatal novelty-killing flaw. The genuinely novel contribution — using the MCMC chain as SCL training data rather than outputting the best/averaged graph — is unambiguously distinct from standard Bayesian DAG MCMC. Kept only as Minor (missing baseline comparison) and Minor (AD metric novelty needs clarification). The "fatally similar to prior art" framing is removed.

2. **Missing Bayesian structure learning citations (Harsh Critic).** The hard rule prohibits citing absent related works. Removed.

3. **"Training on K=200 is potentially ill-conditioned" (Harsh Critic).** The critic argues the model may not converge, but training details are almost certainly in the stripped appendix. Per rules, not penalizing for missing appendix content. Demoted to Minor (under the broader missing-spec concern) but not the full characterization.

4. **Sachs non-Gaussian noise mismatch (Harsh Critic).** The concern that Sachs protein expression data violates the N(0,1) noise assumption is speculative without knowledge of the actual data distribution; more importantly, TACTIC achieves 78.9 AUROC on Sachs (strong result), making this a speculative concern that the data contradicts. Removed.

5. **"Component-mixed combinations not listed explicitly" (Harsh Critic).** Details are in Appendix B. Per rules, not penalizing for missing appendix content.

6. **Strength: "Important problem" (Strength Finder).** Generic; removed per filtering rules. All retained strengths are concrete.

---

## Novel Insights

The most genuinely novel element in the paper — more novel than it is given credit for in the harsh review — is the two-stage functional separation between *search quality* (AD + sparsity MCMC) and *inference quality* (SCL training). By using MCMC to generate a *curriculum of near-ground-truth (G, D) pairs* rather than selecting a single best graph, the paper effectively turns a classic structure-search problem into a data-augmentation problem for a neural learner. This reframing means the SCL model can potentially learn from the diversity in the K-sample set (different DAGs that all fit the test distribution) rather than committing to one answer. Whether this diversity is what drives the "Learning Improvement" in Table 4 — or whether simple model averaging would achieve the same — is precisely the question the missing baseline must answer.

---

## Evaluation on Key Axes

- **Originality**: *Moderate-high.* The TTT-SCL paradigm and the specific two-stage architecture (MCMC-generated training set + SCL training) are genuinely novel. The AD metric is functionally familiar but contextually new.
- **Importance**: *High.* OOD fragility of SCL is a real bottleneck for real-world causal discovery, and the diagnostic Section 3 makes the problem concrete with clear evidence.
- **Claim support**: *Moderate.* Most claims are well-supported; the key missing piece is the model-averaging baseline for the "Learning Improvement" claim.
- **Experimental soundness**: *Moderate-high.* Five datasets (synthetic + pseudo-real + real), multiple baselines, three evaluation metrics, ablation structure in Table 3 and Table 4 are all solid. Main gap is the missing comparison noted above.
- **Clarity**: *Good.* Significantly cleaner than comparable submissions in this space; method description is largely self-contained, notation is consistent.
- **Community value**: *High.* Both the diagnostic framing and the TTT-SCL framework are likely to influence how the community thinks about SCL generalization.

---

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Human Score | Round | Comparison to Paper Under Review |
|------|----------------|-------|----------------------------------|
| ZXs3pkmrRG (TICL - TTT for interventional SCL) | 5.50 | R1/R2 | Most similar paper; rejected; TACTIC has better presentation and experiments but same missing baseline gap |
| lQYi2zeDyh (Demystifying amortized CD) | 5.00 | R2 | Analysis paper only, no proposed solution; TACTIC is more substantial |
| x3F8oPxKV2 (Zero-shot causal models) | 6.25 | R1/R2 | More conceptually ambitious; rejected for fundamental assumptions; comparable scope |
| bMvqccRmKD (Causal RL generalization) | 7.00 | R1 | Accept; stronger theoretical grounding; TACTIC lacks this rigor |
| pOoKI3ouv1 (Robust agents learn causal models) | 5.75 | R1 | Theoretical paper; mixed scores; different methodology |
| EpgoFFUM2q (AdaRC - TTA for GNNs) | 6.00 | R2 | Accepted; clean method for test-time adaptation; TACTIC is more novel but has more gaps |
| 22ywev7zMt (OOD generalization of SSL) | 5.67 | R2 | Rejected; analysis + method paper; TACTIC is more domain-specific but better evaluated |
| Xk9Q0CrJQc (Distribution shifts for MLFFs) | 6.25 | R2 | Rejected; similar structure (diagnostic + solution); TACTIC is more novel |
| 7iuFxx9Ccx (Resource-efficient TTT) | 6.00 | R2 | Rejected; clean TTT paper but incremental; TACTIC is more novel |

**Round 1 bracket:** 5.0–7.0, with 5.5–6.5 as the plausible range.

**Round 2 narrowing:** The most directly comparable paper (TICL, avg 5.50) was rejected for similar gaps (missing natural comparison baseline, unclear contribution framing). TACTIC is better on presentation and has stronger experiments. AdaRC (6.00, Accept) is a simpler method with cleaner ablations. Zero-shot Causal Models (6.25, Reject) is more ambitious but falls on strong assumptions. TACTIC's core weakness — the missing Bayesian model averaging baseline that would validate Stage 3's "Learning Improvement" claim — is comparable in severity to the gaps in the 5.5–6.0 range anchors.

The paper sits between the rejected TICL (5.5) and the accepted AdaRC (6.0): better than TICL in execution and experimental rigor, slightly below AdaRC's clean rigor due to the missing key baseline. I score it at **6.0** — right on the line between reject and borderline accept. Given the missing Bayesian model averaging baseline directly undermines the paper's central novelty claim about Stage 3, a revision requiring that comparison (and the specification of the SIM regression model) is warranted before acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>