Now I have all the information I need. Let me write the consolidated review.

## Summary

2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

---

Here is the final review:

---

## Summary

This paper proposes HiSo, a Hessian-informed zeroth-order federated optimization method that accelerates convergence by leveraging global diagonal Hessian approximations while strictly preserving scalar-only (dimension-free) communication. The key insight is that gradient scalars already transmitted between clients and server can be reused to learn a diagonal Hessian approximation at no extra communication cost. Empirically, HiSo achieves 1.4–5.4× speedup in communication rounds over the state-of-the-art ZO-FL baseline (DeComFL) across OPT-350M/1.3B/2.7B on SST-2, QQP, and SQuAD, with 29%–80% communication cost savings. Theoretically, the paper provides convergence analysis showing potential dimension-independent rates under a well-approximated Hessian condition.

## Strengths

1. **Hessian learning at zero additional communication cost (Section 4.2, Eq. 12).** The paper shows that the update vectors Δx_r (reconstructible from scalars and seeds) can be reused to update a global diagonal Hessian approximation via Diag(|Δx|²). Since these scalars are already transmitted for model reconstruction, the curvature information comes for free — a genuine and clever insight that directly delivers on the core claim of accelerating ZO-FL while maintaining scalar-only communication.

2. **Clean and consistent empirical speedup across LLM scales (Table 2).** HiSo achieves 1.4–5.4× speedup in communication rounds and 29%–80% communication cost savings over DeComFL across three model sizes (OPT-350M, OPT-1.3B, OPT-2.7B) and three tasks (SST-2, QQP, SQuAD). The per-round communication cost is identical between HiSo and DeComFL, making this a direct algorithmic comparison. The experiments use multiple seeds with standard deviations reported, lending credibility.

3. **Generalized scalar-only communication framework (Algorithm 1).** The paper decouples scalar-only communication from vanilla ZO-SGD, enabling a broader class of optimization algorithms within the dimension-free communication paradigm. This abstraction cleanly separates the communication mechanism from the update rule, which is a useful structural contribution beyond the specific HiSo algorithm.

4. **Theoretical analysis with multiple local updates (Corollary 3).** The analysis extends convergence guarantees to τ > 1 local steps — a setting that DeComFL could not theoretically handle under the low-effective rank assumption. Showing that HiSo's rate remains dimension-independent while DeComFL's becomes dimension-dependent again is a genuine theoretical advance, even if conditional on the well-approximated condition.

## Weaknesses

### Fatal
None.

### Major

1. **The dimension-independent convergence rate is conditional on an assumption not connected to the algorithm's update rule.** The central theoretical claim (Corollaries 1–3) depends on the well-approximated condition (Definition, Eq. 17), which assumes the learned H_r already satisfies Tr(H_r^{-1/2} Σ H_r^{-1/2}) ≤ ζ with ζ ≪ d. The paper does not analyze whether the proposed update rule (Eq. 12, based on Diag(|Δx|²)) converges to a matrix satisfying this condition. The connection between Diag(|Δx|²) and the Hessian diagonal is heuristic (analogous to Adam/RMSProp) and is never formalized. The paper is transparent about this gap (Section "Remarks about well-approximated condition"), but the consequence is that the proven dimension-independent rate applies to a hypothetical algorithm that assumes a well-approximated H_r, not to the dynamics of HiSo as implemented. The paper's own abstract and introduction could more prominently qualify this.

2. **Missing ablation isolating the effect of the learned Hessian.** The experiments compare HiSo against DeComFL, but there is no ablation against: (a) HiSo with a *fixed* diagonal preconditioner (e.g., H_r ≡ I or H_r with random diagonal entries), or (b) DeComFL with the same number of local steps / perturbation count as HiSo. Without these, it is unclear whether the observed speedup comes from the *learned* curvature information, or simply from the structural effect of the preconditioned update rule (i.e., using H_r^{-1/2}u instead of u as the search direction), which could accelerate convergence even with a random diagonal. This is the most important missing experiment for validating the core claim that *Hessian information* drives the acceleration.

### Minor

1. **Connection between Diag(|Δx|²) and Hessian diagonal is not formalized.** Section 4.2 obliquely references Adam/RMSProp, but the paper does not analyze what the fixed point of Eq. 12 is, or under what conditions Diag(|Δx|²) ≈ Diag(H^{-1}). If Δx ≈ η H^{-1} ∇f, then |Δx|² ≈ η² (H^{-1}∇f) ⊙ (H^{-1}∇f), which depends on the gradient direction, not on H^{-1} alone. This could create feedback loops between H and Δx. A formal analysis or even a heuristic justification of why this update rule works would strengthen the paper considerably.

2. **No wall-clock time comparison.** The paper reports communication rounds and KB-scale costs, but does not report wall-clock time per round for HiSo vs. DeComFL. The client must compute H_r^{-1/2}u (O(d) diagonal multiplication) for each perturbation, and the Hessian update adds overhead. While likely negligible relative to the forward pass, these costs should be reported to confirm that round savings translate to time savings.

3. **Σ definition for non-convex functions (footnote 3).** The paper defines Σ as a PSD matrix that "upper-bounds the Hessian" and the footnote mentions using absolute eigenvalues. For non-convex LLM loss landscapes with both positive and negative eigenvalues, taking absolute values changes the optimization geometry. While this is common practice in Hessian-informed ZO work, a brief discussion of the implications would improve rigor.

### Trivial

1. Notation inconsistency in Eq. 12: the displayed equation uses Δx_{r,0} while the surrounding text uses Δx_{r,τ}. This appears to be a minor notation slip (likely referring to the update at the beginning of the round) and should be harmonized.

## Nice-to-Haves

- A comparison against HiSo with a random/fixed diagonal H_r would cleanly isolate whether the learned Hessian is responsible for the speedup.
- Reporting a few ablation points on the perturbation count P to show sensitivity to this hyperparameter.
- A brief discussion in the theory section on the relationship between the H_r update (Eq. 12) and the well-approximated condition, even if informal.

## Removed Points

- **"Communication cost inconsistency between Tables 2 and 3."** The captions explain the difference: Table 2 reports cost to match DeComFL's best accuracy; Table 3 reports total cost until convergence (to HiSo's own higher accuracy). These are different stopping criteria, not an inconsistency. The per-round costs are consistent between the two tables.
- **"The well-approximated condition is fatal."** The paper transparently acknowledges this limitation in its Remarks section and Theorem 1 does not require it. This is a recognized gap, not a fatal flaw.
- **"Missing reproducibility details (τ, learning rates, etc.)."** These are standard for the appendix and the paper references Appendix E and F for details.
- **"Generalized framework is not novel / straightforward abstraction."** Even if straightforward, presenting it as a formal abstraction is a valid contribution that enables future work.
- **"First-order methods achieve higher accuracy; accuracy gap unacceptable."** The paper frames this as a communication-accuracy trade-off, which is standard in communication-efficient FL work. The contribution is explicitly in the ZO regime.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add the key ablation:** Compare HiSo against a version with a fixed diagonal preconditioner (e.g., identity or random). This would directly validate whether the learned Hessian, not just the preconditioned update structure, drives the observed speedup. This single experiment would significantly strengthen the paper's core claim.

2. **Tone down the theoretical claims or tighten them.** The abstract and introduction could more prominently state that the dimension-independent rate is a "plausible explanation" (as the Remarks section already does) rather than suggesting it is a proven property of the algorithm. Alternatively, add a discussion connecting the fixed point of Eq. 12 to the well-approximated condition.

3. **Resolve the Eq. 12 notation issue** and add a brief note on how the spectral properties of H_r are maintained (e.g., the ε term for positive definiteness).

## Score and Decision

The paper makes a genuine contribution: the insight that gradient scalars can be reused for Hessian learning at no extra communication cost is clever and practically valuable. The empirical results are clean and convincing. The main weaknesses are (1) the theoretical dimension-independent rate is conditional on an assumption not connected to the algorithm's dynamics, and (2) the missing ablation isolating the Hessian effect. Neither is fatal, and both are addressable. On balance, the paper sits above the acceptance threshold for a top venue.

**Round 1 bracket:** (4.5, 7.5). The paper is clearly stronger than rejected ZO-FL papers (avg score ~3-4) — it has more novel methodology and cleaner experiments. It is not in the top tier (8+) but is a solid middle-band paper.

**Round 2 narrowing:** Compared to the Meerkat paper (avg 5.0, accepted poster) on ZO-FL for LLMs, HiSo has a more novel algorithmic contribution (Hessian learning without extra communication) but weaker theory (conditional on unverified assumption). Compared to Cost-Aware Client Selection (avg 5.5, accepted oral), HiSo has stronger empirical validation on real LLM tasks. Compared to PF-VRZO (avg 4.5, rejected), HiSo has the FL dimension and stronger experiments. HiSo is closest to the 5.5–6.0 band.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>