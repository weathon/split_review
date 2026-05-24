Now I have thoroughly read the paper and verified the claims. Let me construct the consolidated review.

---

## Summary

This paper tackles scaling inverse reinforcement learning (IRL) to planetary-scale route recommendation with hundreds of millions of states and demonstration trajectories, using Google Maps as the testbed. The authors contribute (i) **MaxEnt++**, an improved initialization for MaxEnt IRL inspired by eigenvector iteration yielding a 16% speedup; (ii) **Receding Horizon Inverse Planning (RHIP)**, a novel algorithm that interpolates between deterministic and stochastic policies via a planning horizon parameter; (iii) **spatial parallelization** via a geography-based sparse mixture-of-experts; and (iv) **graph compression** strategies that yield a 2.7× training speedup. The final policy achieves a 15.9% and 24.1% improvement in route accuracy over the ETA+penalties baseline for driving and two-wheelers respectively, representing the largest published real-world deployment of IRL.

---

## Strengths

- **MaxEnt++ initialization (16% speedup, no accuracy loss):** The eigenvector-inspired initialization is principled and the empirical result (16% faster training with identical accuracy) is clearly documented in Section "Empirical Study" and Figure 3. This directly supports the scalability claim.

- **RHIP's practical trade-off control:** Algorithm 1 and Equation (2) present a clean parameterization where the horizon \(H\) controls the blend of stochastic and deterministic planning. Table 1 shows that RHIP with \(H=10\) achieves the highest accuracy (0.5030 driving, 0.5564 two-wheelers) while training 70% faster than MaxEnt, placing MaxEnt off the Pareto front. This is concrete evidence of a genuine algorithmic insight with measurable impact.

- **Spatial MoE with verified regional specialization:** The cross-metro experiment (Fig. 4, left) cleanly shows that off-diagonal performance drops sharply, confirming that each expert learns region-specific routing preferences. This enables the 360M-parameter global model trained on 110M trajectories.

- **Graph compression with quantified impact:** Table 2 reports a controlled experiment showing 2.7× training speedup with no accuracy loss and minimal NLL increase (0.018), across 124k-node metros. The lossless (split) and lossy (merge) strategies are clearly distinguished.

- **Documented negative results:** The paper honestly reports that Arnoldi iteration (ARPACK) fails due to lack of log-space implementation, and that closed-form matrix geometric series (UMFPACK) only helps below 10k nodes. This saves practitioners from pursuing these dead ends.

- **Sparse reward models reveal data quality issues:** Figure 2 shows a concrete example where the 360M-parameter SparseLin model identifies and corrects a data error (an incorrectly marked private gate), demonstrating an unexpected practical benefit of large sparse reward models.

---

## Weaknesses

### Fatal

None.

### Major

1. **Statistical significance claim is inadequately supported.** The table caption reports a p-value threshold of .122, which is unconventional in ML (standard is 0.05). The paper does not explain in the main text what statistical test was used, how it is computed from a single training run (since the global model was trained once), or why .122 was chosen as the threshold. The claimed improvements over other IRL methods are small (0.4% for driving, 0.2% for two-wheelers), so proper error quantification is essential to establish that these margins are not noise. Without a clear methodology for the significance test, the claim of "state-of-the-art results" is only weakly supported. *(The appendix is referenced for details, but the unusual threshold itself and the lack of main-text explanation are issues visible on the page.)*

2. **Unexplained discrepancy between global and metro results.** In Table 1, the global RHIP model (DNN+SparseLin) achieves accuracy 0.4958, while its metro counterpart achieves 0.5030 — the global model underperforms the metro model. This inversion deserves explanation (e.g., the global evaluation set is larger and more diverse, or the MoE averages across many regions). Additionally, the trade-off plot (Fig. 3) shows accuracy values around 0.452 for what appears to be a single metro, while Table 1 shows ~0.50 for similar models on the 9-metro set. This discrepancy (likely due to different evaluation conditions or a different reward model class) is not clarified, making it hard to interpret the trade-off plot's absolute values.

### Minor

1. **Equation (3) contains a semantic error: should be \(\max\) not \(\min\).** The text describes the initialization as the "highest reward to the destination," which corresponds to \(\max_{\tau} e^{r(\tau)}\) (since \(r \leq 0\) and \(e^x\) is increasing). However, Equation (3) writes \(\min_{\tau} e^{r(\tau)}\). The inequality chain happens to hold numerically for both operators at the destination (where only one path exists), but the semantics are inconsistent — \(\min\) picks the *lowest* (most negative) reward path, contradicting the textual explanation. This is almost certainly a typo given the empirical success of the method, but it undermines technical rigor as written.

2. **RHIP's reductions to classic algorithms are asserted without sufficient justification in the main text.** The paper states that RHIP reduces to MaxEnt++ (\(H=\infty\)), BIRL (\(H=1\)), and MMP (\(H=0\)). For BIRL in particular, the reduction to a single-step Boltzmann policy absorbs several assumptions (MAP approximation, specific regularizers) that are not discussed. For MMP (\(H=0\)), the statement "margin terms absorbed into \(r_\theta\)" glosses over structural differences between a margin-based loss and a deterministic planner's cost. The claims may hold under specific conditions (deferred to the appendix), but as stated in the main text they overstate the theoretical unity. The paper would be stronger with more precise characterizations (e.g., "under the MAP approximation, RHIP with \(H=1\) recovers a form similar to MAP-BIRL").

3. **Training time speedup from spatial MoE is not separately quantified.** The paper reports overall training time ("1.4 GPU-years") but does not provide a breakdown of how much speedup comes from the MoE parallelization vs. graph compression vs. MaxEnt++/RHIP. A simple table showing training throughput (steps/second) for sequential vs. parallelized versions on a representative metro would strengthen the scalability claim.

### Trivial

None.

---

## Nice-to-Haves

- A small-scale comparison to behavior cloning (or GAIL/IQ-Learn) on a fixed set of origin-destination pairs in the metro set, to empirically confirm their expected underperformance due to the goal-conditioning issue, would strengthen the motivation for using IRL.
- A discussion of why the global model's accuracy (0.4958) differs from the metro model's (0.5030) would help readers understand generalization.

---

## Removed Points

- **Criticism about missing appendix details (statistical test methodology, hyperparameters):** Per policy, appendix content is stripped by the parser and its absence cannot be attributed to the authors. The retained weakness focuses on what *is* present in the main text (the .122 threshold).
- **Criticism about lack of BC/comparison to policy-based methods:** The paper explicitly scopes this out on goal-conditioning grounds (Section 2), and the criticism is a scope-expansion request, not a flaw in what the paper sets out to do.
- **Criticism about merging of single-outgoing-edge nodes not being discussed as lossless:** The paper *does* state "Feature vectors of the merged nodes are summed, which is lossless for linear \(r_\theta\) but introduces approximation error in the nonlinear setting" (Section 4, graph compression paragraph). The critic misread this.
- **Criticism about reproducibility (hyperparameters, hardware):** These are standard implementation details typically deferred to appendices; the paper cites the appendix for this information.
- **Strength Finder's generic claims about "importance of the problem":** These are excluded as they are problem-motivation boilerplate, not specific to the paper's evidence.

---

## Novel Insights

The reviews surface one observation that goes beyond the paper's own framing: the fact that **the global RHIP model (0.4958) underperforms the metro model (0.5030)** is not discussed by the paper, yet it raises an interesting question about whether the geographic MoE sacrifices global coherence. The cross-metro experiment shows regional specialization (good), but the global accuracy dip hints at a possible cost to that specialization that is not explored. This tension — between local specialization and global generalization — is worth examining in future work. Separately, the discrepancy between the trade-off plot's accuracy scale (~0.452) and Table 1's (~0.50) for what appear to be related experimental conditions is an unaddressed presentational inconsistency.

---

## Suggestions

1. **Correct Equation (3):** Change \(\min_{\tau} e^{r(\tau)}\) to \(\max_{\tau} e^{r(\tau)}\) to match the textual description of the "highest reward" initialization. Verify the inequality chain and proof in the appendix are consistent.

2. **Strengthen the statistical evaluation:** Either (a) report bootstrapped confidence intervals over the evaluation set for accuracy and NLL, or (b) clearly describe the significance test used and justify the .122 threshold. If the threshold was determined by a multiple-comparison correction, state this explicitly.

3. **Temper the RHIP reduction claims:** Replace "reduces to" with more precise language (e.g., "under specific conditions recovers a form analogous to").

4. **Explain the global vs. metro accuracy gap** and the trade-off plot vs. Table 1 accuracy discrepancy in the main text or a footnote.

5. **Add a brief table of per-component speedups** (e.g., baseline sequential training → +MoE → +graph compression → +MaxEnt++/RHIP) to quantify the contribution of each scaling technique.

---

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>