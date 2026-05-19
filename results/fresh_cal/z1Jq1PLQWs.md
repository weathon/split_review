I have all the content needed from the initial file read. Let me now compose the final review.

---

## Summary

This paper introduces the first efficient online mirror-descent algorithm (Double-Scrible) for adversarial linear bandits with preference (pairwise comparison) feedback. The main algorithm achieves \(\widetilde{O}(d\sqrt{T})\) regret with a matching \(\Omega(d\sqrt{T})\) lower bound for the logistic dueling bandit (Logit-DB) problem — matching the information-theoretic limit. Extensions to batched (B-wise) feedback and top-m ranking feedback are presented with improved rates, along with matching lower bounds for each. Synthetic experiments demonstrate computational scalability.

---

## Strengths

1. **First efficient gradient-descent algorithm for adversarial preference bandits with optimal regret.** Prior work (UCB, Thompson sampling) was computationally intractable for all but the smallest instances. Double-Scrible uses a one-point gradient estimation trick adapted to preference feedback (Lemma 11, Remark 5(1)), avoids the derivative lower-bound assumption required by prior GLM-bandit methods, and runs in \(O(dT)\) time (Remark 5(2)). This is a genuine algorithmic contribution that opens the door to practical preference-based learning at scale.

2. **Matching lower bounds confirm near-optimality.** Theorem 3 provides an \(\Omega(d\sqrt{T})\) lower bound for Logit-DB, establishing that Double-Scrible is optimal up to logarithmic factors. Similarly, Theorem 6 (batched) and Theorem 9 (ranking) give matching lower bounds for the extensions. These are derived from information-theoretic first principles.

3. **Computational efficiency demonstrated with runtime tables.** Section 6.2 reports wall-clock runtimes for \(T\) up to 80,000 and dimensions up to \(d=50\), confirming the \(O(dT)\) theoretical complexity translates to practical scalability.

4. **Batched extension is natural and well-posed.** The BaBle-Scrible algorithm (Section 4) generalizes Double-Scrible to B-wise batch queries with a clean regret analysis (Theorem 4) and a matching lower bound (Theorem 6). The presentation of this extension is clear and self-contained.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unsubstantiated reduction of ranking feedback to batched feedback.** The paper claims (line 229) that MNL-Scrible "extracts \(m\) independent pairwise preference feedback from \(\sigma_{m,t}\)" and then states the regret bound of Theorem 7 "follows immediately from Thm. 4." However, the \(m\) pairwise comparisons are all derived from the **same** top-\(m\) ranking drawn under the Plackett-Luce model. They are **not independent**: the events at different ranks are coupled through the sequential sampling-without-replacement structure of the PL model. The batched analysis in Section 4 explicitly relies on independence of the \(B\) queries to reduce the variance of the gradient estimate by a factor of \(B\). The paper provides **no analysis** of how correlations among the \(m\) extracted comparisons affect the variance of the average gradient estimator, nor any justification that the variance reduction factor \(1/m\) still holds under correlation. This is a genuine gap in the proof — Theorem 7's guarantee is not properly supported by the argument given.

   *Why this matters*: The ranking-feedback setting is presented as a main contribution (both in the abstract and the contributions list). Until the independence claim is either properly justified (perhaps via a martingale argument or a more careful variance analysis) or the proof is revised to handle correlations, the ranking result should be considered unproven. This does **not** affect the dueling or batched contributions, which stand on their own.

### Minor

1. **Technical inaccuracy in Remark 1.** The paper states (line 65) that for any \(x\in\mathcal{D}\),
   \[
   \frac{\theta_t^{*\top}(x^*-x)}{4} \le P_t(x^*,x) - 1/2 \le \theta_t^{*\top}(x^*-x).
   \]
   The lower bound \(\sigma(z)-1/2 \ge z/4\) fails for values of \(z\) where the logistic function saturates (e.g., \(z=2\) gives \(\sigma(2)-1/2 \approx 0.381\) while \(z/4=0.5\)). The paper only uses the upper bound to relate the actual regret to the linearized regret (line 71: "noting \(\mathrm{Reg}_T \le \widehat{\mathrm{Reg}}_T\) from Rem. 1"), so the error in the lower bound does **not** affect the main regret analysis. However, the statement as given is false, and the lack of qualification (e.g., "for small enough differences") suggests less care in the technical exposition than would be desirable.

2. **Minimal experimental validation.** The experiments (Section 6) report only the cumulative regret curves of the proposed methods without any baselines for comparison. No log-log plots or curve fitting are provided to confirm the \(\widetilde{O}(\sqrt{T})\) scaling rate. The Inst-2 environment description appears truncated. While experiments are not mandatory for a theory paper, the claim that "Empirical evaluations validate our theoretical findings" (abstract, line 4) is overstated relative to what is actually shown. The runtime tables are useful, but they demonstrate scalability, not regret-optimality.

### Trivial

- The text around line 65 (Remark 1) contains garbled/run-together words due to PDF extraction — this should be cleaned up.
- The Inst-1 and Inst-2 environment descriptions (lines 246–247) are incomplete.

---

## Nice-to-Haves

- **Pseudocode in the main text.** The algorithms are described only in prose; compact pseudocode (even for Double-Scrible alone) in the main body would improve readability and reproducibility.
- **Comparative baseline in experiments.** Even a small-scale comparison on synthetic data with a simple tractable baseline (e.g., a random policy or a crude approximation of UCB) would strengthen the empirical case.
- **Proof sketch for Theorem 1 in the main paper.** The paper defers the complete proof to the appendix, which is typical, but a 2–3 sentence sketch showing how the gradient estimator works and why the Hessian eigenvalue assumption (\(H_{\mathcal{D},\psi}^2\)) is needed would help the reader gauge the proof's soundness without diving into the appendix.

---

## Removed Points

*These points were flagged in the reviews but are removed from the main weaknesses list with justification:*

- **"Missing related works"** — Removed. The paper provides a discussion of prior work in Section 1; as per policy, missing related works are not flagged without external verification.
- **"Computational intractability not demonstrated" / "cannot be independently verified"** — Removed per hard rules: cited references are assumed to exist as of the review date.
- **"No pseudocode in main text"** — Moved to Nice-to-Haves; it is a presentation choice common in page-limited theory papers, not a weakness.
- **"Does not address RLHF with policy optimization"** — Removed as scope creep. The paper explicitly scopes itself to adversarial linear optimization with preference feedback (Section 1.1), not full RLHF policy optimization.
- **"Lower bound proofs deferred to appendix"** — Removed as standard practice for theory papers.
- **Strength: "Empirical validation of theoretical scaling"** — Removed because it conflicts with the verified weakness about minimal experiments (no baseline comparisons, no rate validation). The experiments show plausibility, not rigorous validation.
- **"Inst-2 not described" / general criticism of experiment design lacking baselines** — Retained as Minor weakness #2 (merged from the various related comments).

---

## Novel Insights

None beyond the paper's own contributions. The key observation — that one-point gradient estimation can be adapted from value-feedback to preference-feedback by playing symmetrically opposite points around the current iterate — is the paper's main technical insight and is well articulated.

---

## Suggestions

1. **Fix the ranking-feedback proof.** Either (a) provide a rigorous analysis of the variance of the gradient estimate under the correlations induced by the PL-model ranking, showing that the \(1/m\) variance reduction still holds (perhaps using a martingale argument or a careful covariance bound), or (b) revise the claim to reflect a weaker but provable rate, or (c) explicitly note that the argument as presented is incomplete and the ranking result should be considered conjectural. This is the single most important revision.
2. **Correct Remark 1** by qualifying the lower bound to hold only for \(|\theta_t^{*\top}(x^*-x)|\) bounded by an appropriate constant (e.g., \(\le 2\)), or replace it with a correct inequality known from the logistic function literature.
3. **Strengthen the experiments** by adding at least one baseline comparison (e.g., a naive greedy policy) and providing a log-log plot of regret vs. \(T\) to visually confirm the \(\sqrt{T}\) scaling.
4. **Complete the Inst-1/Inst-2 descriptions** in the experiments section so others can reproduce the adversarial environments.

---

## Score and Decision

The paper makes a genuinely novel contribution — the first efficient gradient-descent algorithm for adversarial preference bandits with optimal regret and matching lower bounds — which alone merits acceptance at a competitive venue. The batched extension is clean and well-supported. The ranking-feedback extension has a proof gap that needs to be addressed, but this does not undermine the core dueling contribution. The experiments are minimal but acceptable for a theory paper with the suggested improvements.

**Originality:** High — first gradient-based approach for this setting.  
**Importance of question:** High — RLHF and preference feedback are practically relevant.  
**Claims support:** Mixed — dueling/batched claims are well-supported; ranking claim is not.  
**Soundness of experiments:** Below standard — lacks baselines and rate validation.  
**Clarity:** Adequate — dense but readable.  
**Value to community:** High — provides a computationally tractable framework for a problem previously dominated by intractable methods.

MY FINAL SCORE: <score>7.0</score>  
MY FINAL DECISION: <decision>Accept</decision>