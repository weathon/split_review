## Summary

This paper proposes a spectral algorithm that combines Predictive State Representations (PSRs) with tensor decomposition methods to recover explicit POMDP transition and observation parameters from action-observation sequences collected under random exploration. The key theoretical contribution (Theorem 1) guarantees recovery up to a *full-rank observability partition*—states that share identical observation distributions across all full-rank actions are grouped, and transitions are learned between these groups. This relaxes the per-action unique-observation assumption of prior tensor methods (Azizzadenesheli et al., 2016; Guo et al., 2016). Experiments across four domains demonstrate parameter convergence, planning parity with PSRs, and a downstream state-based reward specification capability that black-box PSRs cannot provide.

## Strengths

- **Provable recovery up to a state partition (Theorem 1).** The paper formally characterizes the class of POMDPs learnable by the method and proves that observation/transition models can be recovered up to the full-rank observability partition. This is a genuine theoretical advance over prior tensor methods that required unique per-action observation distributions for every state. The proof is referenced to Appendix A.

- **Relaxes per-action full-rank constraints via joint diagonalization (Lemma 1).** The algorithm simultaneously leverages all full-rank actions via a random-weighted sum (Eq. 18), whereas earlier work required per-action full-rank *and* unique observation distributions. Lemma 1 guarantees that random weights yield distinct eigenvalues for states with different observation distributions almost surely. This broader applicability is critical for domains like Sense-Float-Reset, where the *reset* action is singular.

- **Empirical convergence to ground-truth parameters.** Figure 3 shows that observation-matrix error and partition-level transition error decrease steadily with data volume and are substantially lower than the EM baseline, which converges to poor local minima. On Tiger and 3‑state Sense‑Float‑Reset, near-zero error is achieved after 10⁶ interactions, confirming the spectral estimation procedure recovers the intended parameters.

- **State-based reward specification is convincingly demonstrated.** Figure 4 on the noisy-hallway domain shows a concrete use case where state-based reward specification (Ours_state) eventually outperforms observation-only reward, and neither PSR nor EM can achieve this because they lack interpretable state parameters. This directly validates the paper's core motivation: explicit models enable downstream manipulation that black-box predictors cannot.

## Weaknesses

### Major

1. **Section 4.3 (partition-level recovery) is substantially under-explained in the main text.**  
   The paper's most important algorithmic step—converting the ambiguous similarity transform \(P'\) (from joint diagonalization) into the partition-correct transform \(\tilde{P}\)—is described in roughly 4–5 sentences (lines 187–228). The text invokes a "random block-diagonal rotation matrix \(R\), whose blocks correspond to the full-rank observability partition" and states that \(\tilde{P} = \text{diag}(RP'^{-1}m_\infty)RP'^{-1}\) is the desired transform, with correctness deferred to Appendix A.5.  

   **The main text does not explain:**
   - How the blocks of \(R\) are identified from finite-sample eigenvalue estimates when the partition is not known in advance.
   - Why the block-diagonal structure of \(Q = P^{-1}P'\) (proved in Appendix A.4) is guaranteed and how it is exploited.
   - Any intuition for why normalizing by \(\text{diag}(RP'^{-1}m_\infty)\) forces the final vector to \(\mathbf{1}\) and recovers the state-sum-to-likelihood property.

   This is the algorithmic center of the paper that differentiates the method from standard PSRs, yet a reader cannot evaluate its correctness from the main text alone. The exposition should be expanded with at least one paragraph of intuition and a step or two of pseudocode.

### Minor

2. **No direct evaluation of partition quality.**  
   The core theoretical output of the method is a partition of states (the full-rank observability partition). The experiments report overall observation and transition \(L_1\) errors (Figure 3), which serve as indirect evidence. However, there is no direct metric—such as normalized mutual information (NMI), adjusted Rand index (ARI), or purity—measuring whether the estimated partition matches the ground-truth partition. Since the value of the method over prior tensor approaches is *precisely* the ability to aggregate states with shared observation distributions, a direct partition-evaluation metric would substantially strengthen the experimental validation.

3. **Planning comparison uses different rollout strategies across models, which complicates interpretation.**  
   The paper acknowledges (line 223 and Appendix C.3) that "different sampling strategies" are used for rollouts with the learned POMDP versus the ground-truth model. In the 3‑state Sense‑Float‑Reset domain, the "Ours" curve appears to match or exceed GT in total reward. While the paper appropriately references the appendix for details, this discrepancy should be discussed more explicitly in the main text: if the rollout strategy difference can cause a coarser learned model to appear to outperform the true model, the reader needs a clear explanation of why this does not undermine the planning-parity claim.

4. **Missing spectral-initialized EM baseline.**  
   The EM baseline is initialized from scratch with the correct number of states and predictably converges to poor local minima. In the spectral learning literature, a standard and stronger baseline is EM initialized from the spectral estimates. Including this would demonstrate whether the spectral estimates provide a meaningful warm-start that EM alone cannot achieve, and would better isolate the contribution of the tensor-based similarity transform recovery.

### Trivial

- The caption for Figure 3 labels the x-axis as "exploration interactions" without specifying that it is on a log scale (the description later clarifies this).
- The paper uses \(P'\) and \(\tilde{P}\) for two different transforms; the notation is slightly overloaded and could be clarified with a table.

## Nice-to-Haves

- **Computational complexity analysis:** The method performs SVD, matrix inversions, eigendecompositions, and joint diagonalization. A brief discussion of practical scaling (e.g., to 50+ states) would help readers assess applicability.
- **Sensitivity analysis on rank detection:** The method relies on truncating the SVD of the Hankel matrix and thresholding singular values of \(M^a\) to detect full-rank actions. An ablation showing sensitivity to these thresholds would be valuable.
- **Partition visualization for the hallway domains:** The Sense‑Float‑Reset example has a nice illustration of the partition (Figure 1). The hallway domains used in the reward-specification experiments do not; a similar diagram would help readers connect theory to the experimental design.

## Removed Points

*These points were raised in the input reviews but are removed here following the filtering rules. They are retained for reference but should not factor into the assessment.*

- **Criticism that Section 4.3 is "nearly impossible to verify without the appendix."** The hard rule on missing-appendix criticisms applies: the appendix exists in the original submission. However, the criticism of *insufficient main-text exposition* is retained as a Major weakness (point 1 above) because the main text should provide enough intuition to evaluate the method without requiring the appendix.
- **Criticism about the SFR-3 outperforming GT being "fatal" or "structural."** The paper acknowledges different rollout strategies and defers to Appendix C.3. This is a framing issue, not a fatal flaw; it is retained as a Minor weakness (point 3) but downgraded from the harsh critic's severity.
- **Request for confidence intervals / user studies / theoretical proofs for empirical claims.** These demands reflect different community standards; the paper's single-run-per-seed evaluation with 100 seeds is standard for this type of large-scale empirical work.
- **Generic requests about missing related work.** Per the hard rules, missing-related-work criticisms are removed.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a genuinely novel perspective that the paper itself does not articulate.

## Suggestions

1. **Expand Section 4.3 in the main text** by one paragraph of intuition and a short algorithmic sketch. Explain how the blocks of the rotation matrix \(R\) are determined from the eigendecomposition of the random-weighted sum, and why the \({\rm diag}(\cdot)\) normalization forces partition-wise probabilities to sum correctly.
2. **Add a direct partition-quality metric** (e.g., ARI or NMI) to the experimental results. This would transform the indirect claim ("total error goes down, so the partition must be right") into a direct validation of the paper's core theoretical output.
3. **Discuss the rollout-strategy discrepancy in the main text** rather than deferring entirely to the appendix. Explain whether the strategy differences could create artifacts, and if so, why the overall conclusion of planning parity remains valid.
4. **Include a spectral-initialized EM baseline** to show whether the spectral estimates provide a warm-start benefit over EM from scratch.

## Score and Decision

### Calibration

**Round 1 (bracketing):** Three queries returned anchors grouped as weak (avg 3.0–3.2, on unrelated topics), middle (avg 4.5–6.0, on POMDP learning), and strong (avg 7.6–8.0, on unrelated topics). Initial bracket: **4.5–7.0**.

**Round 2 (narrowing inside the bracket):** Two queries on spectral POMDP learning and parameter estimation returned anchors in the 4.5–6.5 range. The paper was compared against:
- *Wasserstein Believer* (4.50): requires access to true state during training—a much stronger assumption than the paper under review. The paper under review is clearly stronger.
- *Provable Representation* (5.33): heavy reliance on prior work, limited novelty. The paper under review has clearer novelty (connecting PSRs to tensor methods) and more thorough experiments.
- *Robustifying SSMs* (6.50): very different topic (SSM robustness), strong theory, moderate presentation issues. Comparable-level contribution in its own domain.
- *Ex-BMDP* (6.25): strong theory but very restrictive assumptions (deterministic latent dynamics). The paper under review has comparable theoretical depth with less restrictive assumptions.

The paper under review is stronger than the 4.5–5.3 anchors and comparable to the 6.0–6.5 range. Its novel contribution and solid experiments place it near the upper end of the bracket, but the significant exposition gap in Section 4.3 and the missing direct partition evaluation prevent it from exceeding 6.5.

**Final score: 6.0**

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>