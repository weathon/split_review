Now I have a comprehensive picture. Let me finalize the calibration analysis.

**Round 1 bracket:** [5.5, 7.5]

**Round 2 narrowing:** 
- DeComFL (6.25): Direct predecessor. HiSo clearly improves on it.
- AdaFisher (6.25): Also uses preconditioning for optimization acceleration. HiSo is at least comparable.
- LoZO (7.00): Most similar — ZO for LLMs, well-received. HiSo is comparable in quality though in FL setting vs single-node.
- PAdaMFed (7.60): Stronger — cleaner theory, no conditional assumptions.

HiSo sits between DeComFL (6.25) and LoZO (7.00), closer to LoZO in contribution quality but with a theoretical gap that LoZO doesn't have. **Final score: 6.5.**

---

Now let me write the final review.

## Summary
This paper proposes HiSo, a Hessian-informed zeroth-order federated optimization method that accelerates convergence by learning a global diagonal Hessian approximation as a preconditioner, while strictly preserving scalar-only (dimension-free) communication. The key insight is that the diagonal Hessian preconditioner can be built from already-communicated ZO update scalars without any extra communication. The paper also introduces a generalized scalar-only FL framework that decouples dimension-free communication from vanilla ZO-SGD, enabling broader optimizer design within this paradigm. Empirically, HiSo achieves 1.4–5.4× convergence speedup over DeComFL across LLM fine-tuning benchmarks while maintaining identical per-round communication cost.

## Strengths
- **Generalized scalar-only FL framework (Algorithm 1):** The paper identifies that dimension-free communication is not intrinsically tied to ZO-SGD — any optimizer whose updates can be represented via scalars and reconstructible state fits the paradigm. This cleanly decouples the communication mechanism from the optimizer choice, which is a genuine conceptual advance over prior work.
- **Zero-extra-cost Hessian preconditioning (Section 4.2):** The diagonal Hessian approximation is built from the already-communicated per-client Δx updates (via squared magnitudes + EMA), which both server and clients can independently reconstruct from the scalars and seeds they already possess. This entirely avoids transmitting any second-order information.
- **Consistent 1.4–5.4× empirical speedup over DeComFL (Table 2):** Across OPT-350M, OPT-1.3B, and OPT-2.7B on SST-2, QQP, and SQuAD, HiSo requires substantially fewer communication rounds to match or exceed DeComFL's best accuracy, with identical per-round communication cost.
- **Higher accuracy than all ZO baselines at the lowest communication cost (Table 3):** HiSo outperforms DeComFL and FedZO in test accuracy on every (model, task) pair while incurring the lowest total communication cost among ZO methods.
- **Theoretical analysis extends DeComFL to τ > 1 local steps (Corollary 3):** The analysis provides convergence guarantees for multi-local-step ZO-FL, resolving an open question from the DeComFL paper, and subsumes DeComFL as a special case (H_r ≡ I).
- **Honest discussion of theoretical limitations:** The paper explicitly acknowledges that "it is hard to determine if this approximation holds in the context of LLMs" (Section 5.2) and notes that at worst, HiSo degenerates to DeComFL performance.

## Weaknesses

### Fatal
None.

### Major
- **Unverified link between the H-learning rule and the well-approximated condition:** The paper's strongest theoretical claim — dimension-and-L-independent convergence — rests entirely on the "well-approximated Hessian condition" (Eq. 17). However, the relationship between the RMSProp-style update rule (Eq. 12) and this condition is entirely uncharacterized analytically. The paper provides no proof, bound, or even heuristic argument for when or whether Eq. (12) produces an H_r that satisfies Eq. (17). The paper honestly acknowledges this gap, but it substantially weakens the theoretical contribution: the clean convergence rates in Corollaries 1–3 are conditional on an assumption whose satisfaction by the algorithm is unverified. This is a significant gap between the algorithm's mechanism and its claimed theoretical guarantees.

### Minor
- **Communication savings framing could be more precise:** The "up to 90 million times communication savings" headline (Introduction, Table 3) compares the total communication cost of first-order methods trained to their final (higher) accuracy against HiSo trained to its final (lower) accuracy. While the orders-of-magnitude gap is real, a more controlled comparison (e.g., how much communication first-order methods need to reach HiSo's accuracy level) would give a clearer picture of the accuracy-communication trade-off.
- **Corollary 3's rate retains κ dependence:** The client-drift term in Corollary 3 is O(√(τκ/mR)), preserving dependence on the effective rank κ of the original Hessian. While the rate is indeed independent of d and L as claimed, the κ dependence is worth explicit discussion — particularly since κ may itself scale with problem properties.
- **One anomalous communication-cost datapoint:** On OPT-1.3B + QQP (Table 3), HiSo's total communication cost (96.67 KB) exceeds DeComFL's (43.95 KB) because HiSo converges to higher accuracy and runs more total rounds. The paper acknowledges this obliquely but doesn't fully explain the total-rounds vs. speedup-rounds distinction across Tables 2 and 3.
- **Limited federated scale:** Experiments use 6 total clients with 2 sampled per round, which is a small federated setup.

### Trivial
- The introduction (line 27) claims convergence "independent of model dimension and function smoothness" without the "well-approximated condition" qualifier, while the abstract (line 9) does include "under some Hessian approximation assumptions." This slight inconsistency should be corrected.

## Nice-to-Haves
- An ablation with a static diagonal preconditioner (e.g., diagonal Fisher from the pretrained model) would help disentangle whether gains come from learned curvature adaptation or simply from any non-identity preconditioner.
- A direct empirical validation of Hessian approximation quality on a small model (where the true Hessian diagonal can be computed) would strengthen the paper's central claim.
- A communication-vs-accuracy frontier plot comparing HiSo, DeComFL, and a compressed first-order baseline would help readers assess the practical trade-off.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that "the Hessian approximation is built from a heuristic that does not estimate the Hessian" (structural):** The paper is upfront that the method "resembles RMSProp" (footnote 2, line 142) and uses the term "Hessian-informed" to mean the update approximates the Hessian preconditioning direction (footnote 1, line 36), not that it estimates the Hessian matrix itself. The paper explicitly acknowledges it's learning a preconditioner in the spirit of Adam/RMSProp. The connection between squared gradients and diagonal preconditioning is well-established in optimization literature. This criticism overstates the gap.

- **Harsh Critic claim about server computation of Eq. (12) being infeasible:** The harsh critic argues the server cannot compute Eq. (12) because it "only sees aggregated scalars." This is incorrect. The server receives per-client gradient scalars g_{r,k}^{(i)} (as shown in Algorithm 1, line 14: "scalar representations of {Δx_{r,k}^{(i)}}"), and can reconstruct each per-client Δx_{r,k}^{(i)} from g_{r,k}^{(i)} and the shared seeds to compute the diagonal squares. No extra communication is needed.

- **Harsh Critic claim that the well-approximated condition is "structurally circular":** The paper's theoretical approach — prove a rate under an assumption, then propose an algorithm aimed at satisfying it — is standard practice in optimization theory. The paper explicitly notes Theorem 1 does not require the condition and that the corollaries are conditional. The paper further acknowledges the difficulty of verifying the condition for LLMs. The "circularity" framing is a mischaracterization.

- **Harsh Critic's "missing related work" on RMSProp/Adam Hessian connection:** Per review policy, missing related work mentions are removed.

- **Strength Finder claim about "empirical validation of the low-effective-rank assumption" (Figure 5):** The learned H values showing a long-tail distribution is consistent with the low-effective-rank narrative but does not independently validate it — the H values are not actual Hessian eigenvalues. This supporting strength is removed as it overclaims what Figure 5 demonstrates.

## Novel Insights
The paper's decoupling of scalar-only communication from ZO-SGD into a generalized framework (Algorithm 1) is a genuinely novel conceptual contribution that may enable future work beyond the specific HiSo algorithm. The observation that per-client Δx updates already contain curvature information that can be aggregated into a global preconditioner without extra communication is also a useful design pattern for communication-efficient FL.

## Suggestions
- Reframe the Hessian approximation as a learned preconditioner (consistent with RMSProp/Adam terminology) rather than claiming Hessian approximation, and adjust the theoretical framing accordingly. This would close the gap between the algorithm's mechanism and its theoretical assumptions.
- Add an ablation with a fixed diagonal preconditioner to isolate the benefit of *learned* curvature adaptation.
- In the introduction, include the "well-approximated condition" qualifier when stating the dimension-independent convergence claim, consistent with the abstract.

---

**Calibration summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| omrLHFzC37 (DeComFL) | 6.25 | R1 | Direct predecessor; HiSo demonstrably improves on it |
| ZAMoxm86KV (FZooS) | 3.67 | R1 | Much weaker; HiSo is substantially stronger |
| DJRd4IQHGQ (FeedSign) | 5.25 | R1 | Weaker; less principled approach, less rigorous theory |
| puTxuiK2qO (AdaFisher) | 6.25 | R2 | Comparable preconditioning contribution; HiSo in more challenging FL setting |
| 9BiVepgmWW (LoZO) | 7.00 | R2 | Most comparable ZO-for-LLMs paper; HiSo has FL angle but theoretical gap LoZO lacks |
| ZuazHmXTns (PAdaMFed) | 7.60 | R1 | Clearly stronger; cleaner theory without conditional assumptions |

HiSo is a clear improvement over DeComFL (6.25) and comparable to LoZO (7.00) in contribution quality, though LoZO has a cleaner theoretical story. The theoretical gap (unverified link between H-update rule and the well-approximated condition) is significant enough to place HiSo somewhat below LoZO. **Final score: 6.5, Accept.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>