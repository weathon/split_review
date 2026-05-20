Now let me write the consolidated review.

## Summary

This paper identifies and formalizes a "Jensen gap" that arises when optimizing group max-min fairness (MMF) objectives in recommender systems under mini-batch training. The key insight is that MMF constraints violate sample independence, making the loss function non-linear and thus creating a gap between the mini-batch convergence point and the true optimum. The authors propose FairDual, a dual optimization algorithm that reformulates the MMF-constrained objective as a group-weighted loss and uses mirror gradient descent to minimize the gap. Experiments on three datasets with six backbone models show improvements in both accuracy and fairness metrics over baselines.

---

## Strengths

1. **Theoretical identification of the Jensen gap for MMF-constrained objectives**: The paper formally proves (Theorem 2, Section 4.1) that mini-batch sampling on a non-linear additive MMF loss introduces a Jensen gap \(J(B)\neq0\), and shows theoretically and empirically that the gap widens as batch size shrinks and group size grows. This formal analysis fills a gap in prior fairness-aware recommendation work that uses heuristic re-weighting without analyzing the bias introduced by mini-batch training.

2. **Reformulation of MMF as a group-weighted objective with dual interpretation**: Theorem 3 (Section 5.1) demonstrates that the MMF-constrained problem can be exactly rewritten as a group-weighted cross-entropy loss where weights are determined by dual variables with an economic interpretation as "shadow prices." This provides a principled alternative to ad-hoc weighting schemes.

3. **Consistent experimental improvement across multiple backbones and datasets**: Tables 1 and 2 report that FairDual outperforms six baselines (UNI, DRO, S-DRO, Prop, IFairLRs, Maxmin Sample) on MIND, Amazon-Book, and Amazon-Electronic across both accuracy (NDCG, MRR) and fairness (MMF) metrics, with statistical significance (\(p<0.05\)). The improvements are observed across backbones including BigRec, RecFormer, and NRMS.

4. **Empirical validation of Jensen gap reduction**: Figure 3(a) shows in simulation that FairDual maintains a lower Jensen gap than baselines DRO, S-DRO, Prop, and IFairLRs across varying batch sizes and group sizes, with the gap remaining nearly flat as batch size changes — consistent with the method's theoretical motivation.

---

## Weaknesses

### Major

1. **The theoretical bound on the Jensen gap (Theorem 4) has a scaling error that contradicts the paper's claims.** The bound is given as:
   \[
   J(B) \le \frac{H}{\eta} + \frac{|U|L|\mathcal{G}|^2}{B(1-\alpha)\sigma}\eta + \frac{L|\mathcal{G}|^2}{2(1-\alpha)^2\sigma\eta}.
   \]
   The paper then claims "When setting learning rate \(\eta = O(B^{-1/2})\), the bound of Jensen gap is comparable with \(O(B^{-1/2})\)." However, substituting \(\eta = O(B^{-1/2})\) gives:
   - Term 1: \(H/\eta = O(B^{1/2})\) — grows with \(B\)
   - Term 2: \(O(B^{-3/2})\) — decays
   - Term 3: \(O(B^{1/2})\) — grows with \(B\)
   
   The dominant terms are \(O(B^{1/2})\), meaning the **bound grows with batch size**. This is the opposite of what the paper claims and contradicts the empirical finding that larger batch sizes reduce the gap. Either the derivation contains an error, or the claimed \(\eta = O(B^{-1/2})\) scaling does not apply as stated. This undermines the central theoretical contribution of a "sub-linear convergence rate" guarantee. The issue is verifiable directly from Equation (10) as printed in the paper.

2. **The MMF fairness metric is not formally defined, making absolute improvements difficult to interpret.** The paper defines MMF@K as "the aggregated ranking score of the 20% worst-off groups" (Section 6.1) with a formula referenced to prior work, but does not give the precise mathematical expression. The reported absolute MMF values are very small (e.g., 0.12%–2.82% on MIND). While the relative improvements are statistically significant, the reader cannot assess whether a change from, say, 0.12% to 1.07% reflects a practically meaningful fairness improvement without a precise definition of what the metric measures.

3. **Missing comparison with a straightforward Lagrangian SGD baseline.** The paper argues that prior dual methods "cannot be applied to large-scale industrial RS" but does not include a simple Lagrangian SGD baseline that updates \(\mu\) using the subgradient without mirror projection or frozen item embeddings. Such a baseline would isolate the benefit of FairDual's specific design choices (mirror gradient descent, frozen feature extractor) from the general dual optimization framework. Without it, the paper's claims about the necessity of these components are not empirically supported.

### Minor

1. **Limited scale for the most advanced backbone (BigRec).** The paper states that BigRec "only utilizes 1024 samples to train due to large computational cost" (Section 6.1). While this is transparently acknowledged, the primary results in Table 1 are based on this small training subset, raising questions about generalizability to full-scale training. The NRMS and RecFormer results in Table 2 use the full MIND dataset but show much smaller absolute MMF values.

2. **Theorem 3's projection constraint and computational tractability are inadequately justified.** The constraint set \(\mathcal{M}\) is defined over all subsets of \(\mathcal{G}\) (the power set), which could be exponential in \(|\mathcal{G}|\). The paper states the projection is "efficiently solvable since \(\mathcal{D}\) is coordinate-wisely symmetric" (Section 5.2.2), citing Balseiro et al. (2021). This justification is too brief for a key algorithmic step and does not explain how the power-set constraint is reduced to a tractable form.

3. **Direct Jensen gap measurement only shown on synthetic data.** Figure 3(a) measures the Jensen gap in simulation with a simple matrix factorization model, not on the actual recommender architectures (BigRec, RecFormer, NRMS) used in the main experiments. While the synthetic results are consistent with the theory, a direct measurement on real architectures would strengthen the connection between the theoretical analysis and empirical results.

### Trivial

None.

---

## Nice-to-Haves

- A controlled experiment where the true optimum is approximated (e.g., via full-batch training) to directly measure FairDual's Jensen gap reduction on real models.
- Training time and memory usage comparisons given the paper's emphasis on scalability.

---

## Removed Points

The following points raised by the reviewers were removed with justification:

- **"The evaluation does not convincingly demonstrate FairDual reduces Jensen gap in realistic large-scale settings"** — This criticism is too vague and speculative. The paper *does* show Jensen gap reduction in simulation (Figure 3a) and improved real-world metrics (Tables 1-2). A stronger version of this point is retained in Minor weakness 3.
- **"Missing error bars / variance in tables"** — The paper reports statistical significance via t-tests with \(p<0.05\), which is standard practice for this type of benchmark evaluation.
- **"The bound is incorrect rather than misstated"** — While we agree the scaling is wrong, calling the bound "incorrect" is too strong; the bound *as an inequality* may be correct, but the claimed rate is wrong. This is adequately captured in Major weakness 1.
- **"Fairness metric definition is unclear from main text"** — Addressed in Major weakness 2 but softened from the critic's framing.
- **"The paper does not discuss limitations"** — The critic lists three limitations the paper "does not discuss" (group membership handling, projection cost, frozen feature staleness). While these are valid points, the paper scopes them as future work, and this is more of a nice-to-have.
- **Strength Finder claim about "sub-linear convergence guarantee" being "stronger than existing debiasing SGD methods"** — This overclaims given the Theorem 4 issue; removed.
- **Strength Finder claim about "consistent and statistically significant improvements"** — This is partially true but the MMF absolute values are very small; retained in edited form.
- **Generic strength claims** about the problem being "important" — removed as generic.

---

## Novel Insights

The harsh critic's analysis of the Theorem 4 bound scaling reveals an inconsistency that the Strength Finder overlooked entirely. The bound as written has \(O(B^{1/2})\) dominant terms when \(\eta = O(B^{-1/2})\), not the claimed \(O(B^{-1/2})\). This is a concrete, mathematically verifiable error in the paper's centerpiece theoretical result. Meanwhile, the Strength Finder correctly identifies that the paper's core conceptual contribution — identifying and formalizing the Jensen gap for MMF-constrained objectives — is genuinely novel and well-motivated. The tension between a flawed bound and a genuinely interesting problem-algorithm contribution is the central challenge for evaluating this paper. The FairDual algorithm itself may be effective (the empirical results are reasonably convincing), but the theoretical guarantee as presented is unreliable.

---

## Suggestions

1. **Fix the bound in Theorem 4.** Re-derive the scaling carefully. If the bound genuinely grows with \(B\), clarify this explicitly and discuss what it means for the theory. If the bound can be tightened with a different learning rate schedule (e.g., \(\eta = O(1/\sqrt[4]{B})\) or similar that balances the three terms), state this clearly. Alternatively, if the constants \(H\) or \(L\) have hidden dependencies on \(B\) that change the scaling, make those dependencies explicit.

2. **Define MMF@K precisely** with a formal equation in the main text, and include a discussion of what the absolute MMF values mean in practical terms (e.g., what does an MMF of 1% represent in terms of group-level exposure).

3. **Add a simple Lagrangian SGD baseline** without mirror projection or frozen embeddings to isolate the benefit of FairDual's specific design choices.

4. **Measure the Jensen gap directly** on at least one real backbone model (e.g., NRMS on MIND) by approximating the true optimum via either full-batch training or a very large-batch reference run.

5. **Provide training time and memory overhead** comparisons to support the scalability claims.

---

## Score and Decision

### Calibration Anchor Summary

**Round 1 (Bracketing — all on "fairness in recommender systems optimization theory"):**

| Anchor path | Avg score | Band | Comparison |
|---|---|---|---|
| `/home/.../ArW410lq8C.md` (One to All) | 3.00 | Weak | Lower quality — less theory, no analysis of training bias |
| `/home/.../kc3QtI6NBF.md` (Actionable Inverse Class.) | 3.00 | Weak | Different topic (actionable recourses), less relevant |
| `/home/.../u4CQHLTfg5.md` (Individual Fairness as Extension) | 3.00 | Weak | Primarily conceptual, no algorithmic contribution |
| `/home/.../TJU9J8iQXL.md` (Is Fairness Metric Fair?) | 2.33 | Weak | Narrow focus on metric evaluation only |
| `/home/.../DqU4AB4wRy.md` (GUFR) | 5.00 | Middle | Similar domain (RS fairness), has theory+experiments but weaker problem motivation and baseline comparisons. Current paper is somewhat stronger |
| `/home/.../KJHUYWviZ6.md` (Socially Fair Regression) | 4.50 | Middle | Different setting (regression); less applied |
| `/home/.../SBj2Qdhgew.md` (Demystifying Fairness in FL) | 7.33 | Middle | Stronger theory (information-theoretic), accepted as poster. Current paper less theoretically rigorous |
| `/home/.../VoI4d6uhdr.md` (Effective Theory of Bias) | 7.00 | Middle | More rigorous theory in different domain |
| `/home/.../A3YUPeJTNR.md` (Hidden Cost of Waiting) | 8.00 | Strong | Oral — much stronger overall |
| `/home/.../TTrzgEZt9s.md` (DRO with Bias/Variance Reduction) | 8.00 | Strong | Spotlight — broader scope, cleaner theory |

**Round 2 (Narrowing):**

| Anchor path | Avg score | Decision | Comparison |
|---|---|---|---|
| `/home/.../DqU4AB4wRy.md` (GUFR) | 5.00 | Withdrawn/Reject | Same domain (RS fairness). Current paper has better problem identification but GUFR had cleaner theory. Current paper is slightly stronger |
| `/home/.../2E2q9t1MFp.md` (Impact of Data Distribution) | 4.67 | Withdrawn/Reject | Theory-heavy but limited experiments. Current paper has stronger empirical validation |
| `/home/.../QibJggOAnB.md` (Fair Clustering via Alignment) | 6.00 | Reject | Cleaner theory but less applied relevance. Current paper is comparable in quality |
| `/home/.../fDaLmkdSKU.md` (Near-Optimal Solutions) | 5.80 | Accept (poster) | Most similar approach (dual methods for constrained learning). Cleaner theory but less applied. Current paper is slightly weaker due to the Theorem 4 issue |
| `/home/.../cNaHOdvh9J.md` (Adversarial Latent Feature Aug.) | 6.50 | Accept (poster) | Different approach but similar venue. Cleaner execution. Current paper is weaker |
| `/home/.../yqST7JwsCt.md` (Entropy-Based Aggregation FL) | 6.00 | Reject | Similar tier |
| `/home/.../VhQUwxIHER.md` (Small Variance Big Fairness) | 5.00 | Reject | Similar tier, weaker experiments |
| `/home/.../E1NxN5QMOE.md` (Oblique Decision Forests) | 7.00 | Accept (spotlight) | Stronger execution |

**Round 1 bracket:** The paper clearly falls between weak (≤3.5) and strong (≥7.5) anchors, placing it in the **4.5–6.5 range**.

**Round 2 narrowing:** Comparing against the most relevant anchors:
- The paper is stronger than GUFR (5.0) — better problem motivation and more comprehensive experiments, though GUFR had cleaner theory.
- The paper is comparable to Near-Optimal Solutions of Constrained Learning (5.8, accepted poster), which also uses dual methods for constrained learning. However, the Near-Optimal paper did not have a scaling error in its central bound.
- The paper is weaker than Adversarial Latent Feature Augmentation (6.5, accepted poster) and Oblique Decision Forests (7.0, accepted spotlight).
- The paper is comparable to Fair Clustering via Alignment (6.0, rejected) and Entropy-Based Aggregation (6.0, rejected) — these papers had interesting contributions but specific flaws that prevented acceptance.

Considering the Theorem 4 scaling error (which is a significant but not fatal flaw — the algorithm and empirical results remain valid), the paper sits around the **5.0–5.5** level. It is not as strong as papers accepted at ICLR poster level in this specific area, but it is above the clearly weak papers (3.0).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

## Score and Decision

**Score: 5.0** — Marginally below the acceptance threshold. The paper has a genuine conceptual contribution (identifying and formalizing the Jensen gap for MMF optimization) and a reasonably effective algorithm (FairDual). However, the central theoretical bound (Theorem 4) contains a verifiable scaling error — the bound grows as \(O(B^{1/2})\) rather than the claimed \(O(B^{-1/2})\) — which undermines the paper's primary theoretical selling point. Combined with an under-specified fairness metric, the absence of a key baseline (simple Lagrangian SGD), and limited-scale evaluation for the most advanced backbone, the paper falls short of the threshold for acceptance. The issues are fixable, and a corrected version with a proper bound derivation and additional baselines could be competitive.

**Decision: Reject**