Now I have all the information needed. Let me compile the final authoritative review.

---

## Summary

This paper studies the deterministic NTK for infinitely wide, fully-connected ReLU networks as depth \(L\) grows. It claims two main contributions: (i) the normalized kernel converges entrywise to 1 (Theorem 2), and (ii) the closed-form predictor expression \(\Theta_\infty^{(L)}(x^\top X)^\top (\Theta_\infty^{(L)}(XX^\top))^{-1}\) converges despite the kernel becoming singular (Theorem 3), proved via rough differential equations.

## Strengths

1. **Proposition 4 provides a clean closed-form recurrence for the normalized NTK.** The expression \(\bar{\Theta}_\infty^{(L+1)}(x,x') = \frac{L}{L+1} h'(\rho^{(L)})\bar{\Theta}_\infty^{(L)} + \frac{1}{L+1} h(\rho^{(L)})\) allows explicit analysis of how depth drives the normalized kernel. This is a useful formulation not present in prior work in this exact form.

2. **Theorem 2 (convergence to the all-ones matrix) follows cleanly from Proposition 4 and Lemma 1.** The paper correctly characterizes the limiting behavior of the normalized kernel for ReLU networks on the sphere, and the derivation is mathematically sound assuming the supporting lemmas hold.

3. **The paper clearly scopes its setting (\(L \in o(\min n_i)\), deterministic limit).** This is contrasted with Hanin & Nica (2020) where depth grows faster than width, providing clarity on the regime of applicability.

## Weaknesses

### Fatal

1. **Proposition 5, property (4) is mathematically incorrect, and the proof of Theorem 3 collapses as a result.** The claim that \(\lim_{d\to0^+} \frac{d^k}{dz^k}\psi_d(z)=0\) for all \(k\) is false. For \(\psi_d(z) = 1/(1+\exp(-2z/(d(1-z^2))))\):
   - For \(k=0\): \(\lim_{d\to0^+} \psi_d(z) = 1\) for \(z>0\) and \(0\) for \(z<0\) (a step function), not 0.
   - For \(k=1\) at \(z=0\): direct computation gives \(\psi'_d(0) = -1/(2d) \to -\infty\) as \(d\to0^+\), not 0.
   
   The entire RDE argument relies on the derivatives of \(\psi_d\) vanishing as \(d = \det(\tilde\Theta^{(L+1)})\det(\tilde\Theta^{(L)}) \to 0\) to conclude that the driver terms \(v_{ij}^{(L)}\) converge to 0 in 1-variation. Since the derivatives diverge at the transition point \(t=1/2\) and the function converges to a step function (not a constant function), the claimed convergence is unjustified. The proof additionally uses an inequality bounding \(\det(A_n^{(L+1)}(t))\) from below by a product of powers of determinants — this inequality is not justified for positive definite matrices and does not follow from standard determinant identities. **The core proof of the paper's central claimed contribution (Theorem 3) is invalid.**

2. **Superscript mismatch between Theorem 3's statement and its proof.** The theorem states \(u_i^{(L)}(1) = \tilde\Theta_\infty^{(L)}(x^\top X)^\top(\tilde\Theta_\infty^{(L)}(XX^\top))^{-1}\) (using depth \(L\)), but the proof constructs \(A_n^{(L+1)}(t)\) interpolating between \(\tilde\Theta_\infty^{(L)}\) and \(\tilde\Theta_\infty^{(L+1)}\), with \(b_n^{(L+1)}(t) = \tilde\Theta_\infty^{(L+1)}(x^\top X^\top)\). At \(t=1\) the construction gives \((\tilde\Theta_\infty^{(L+1)}(XX^\top))^{-1}\tilde\Theta_\infty^{(L+1)}(x^\top X^\top)^\top\). The paper never explains how the index shift from \(L+1\) back to \(L\) is resolved.

3. **Theorem 3 does not characterize the claimed limit — it only asserts existence and boundedness.** The abstract and introduction promise that "the closed-form solution approaches a fixed limit on the sphere," but the theorem provides no formula, no description of the limit, and no rate. A result that only guarantees boundedness with an \(\mathcal{O}(n)\) bound that could depend on \(L\) falls far short of what the paper's narrative advertises. The summary paragraph after the proof states the limit is "non-trivial" and that at training points the limit is \(e_i\), but these claims are not derived from the proof.

### Major

4. **The claimed novelty of Lemma 1 and Theorem 2 relative to existing literature is overstated.** The convergence of the correlation \(\rho^{(L)}\) to 1 (Lemma 1) is a standard result in mean-field theory of deep ReLU networks, appearing in Poole et al. (2016), Schoenholz et al. (2017), and as the "ordered phase" in Xiao et al. (2020). Theorem 2 (normalized kernel → 1) then follows straightforwardly from this known behavior plus Proposition 4. The paper does not clearly differentiate its own results from this prior work, and the discussion of related work in Section 2 does not cite the relevant mean-field papers where ρ→1 was first established.

5. **Experiments do not validate Theorem 3.** The third column of Figure 1 shows \(\bar\kappa^{(l)}(x^\top X^\top)(\bar\kappa^{(l)}(XX^\top))^{-1}\) stabilizing with depth, but: (a) the individual curves are not labeled, so the reader cannot tell what each trace represents; (b) the caption states each curve corresponds to "a different pair of inputs" but this expression is a vector, not a pairwise quantity, so this description is inconsistent with the column label; (c) the experiments only demonstrate numerical stabilization up to \(L=30\), which does not confirm the existence of a theoretical limit. The MNIST experiments are deferred to an appendix that is unavailable in the submission.

6. **The convergence rate discussion in Section 7 contradicts itself.** The text reads: "*while convergence for the limiting kernel is sublinear, the convergence for the limiting kernel is experimentally fast*" — the two clauses refer to the same object yet contradict. The surrounding text suggests the second clause was intended to refer to the convergence of \(\kappa_x^\top\kappa^{-1}\), but the writing is garbled. Combined with the conclusion's statement that "we raise the hypothesis that there might exist a 'pointwise' limit to the NTK when \(L\to\infty\)" — using the word "hypothesis" rather than "theorem" — even the authors appear uncertain about the core claim.

### Minor

7. **The proof sketch for Proposition 1 is uninformative.** It says "\(\mu=0\) implies \(x^\top x' \ge 0\) with probability \(1/2\)" which does not obviously lead to the stated closed-form expression. Since this proposition is for a special case (perfectly correlated inputs), the sketch could mislead readers about the derivation.

8. **The ODE/Cramer's rule derivation in the proof of Theorem 3 is unclear.** Equation (5) writes \(u'(t)_i\) as a ratio of determinants using Cramer's rule, but the solution of \(A(t)u(t)=b(t)\) with constant \(b\) would give \(u'(t) = -A(t)^{-1}A'(t)u(t)\), which does not naturally decompose into the form shown. The connection between the Cramer's rule expression and the subsequent bound is not explained.

### Trivial

9. Various typos and unclear figure descriptions (noted above).

## Nice-to-Haves

- If the authors can provide a correct proof of the existence of a limit for the predictor expression, the result would be interesting. A direct analysis of the limit of \(\kappa_x^\top\kappa^{-1}\) using the known closed-form NTK expressions (without rough path theory) might be more tractable.
- A formula or qualitative description of the limiting predictor would substantially strengthen the contribution.

## Removed Points

- **"False novelty claim about Lemma 1/Theorem 2"** (from harsh critic): The criticism that these are "well-known" is partially valid (ρ→1 is known), but the paper does not present Lemma 1 as a novelty — it is presented as a lemma supporting Theorem 2. Proposition 4's specific recurrence formula is not found in prior work in this exact form. However, the failure to adequately cite the relevant mean-field literature remains a weakness. → **Demoted to Major weakness 4.**

- **"Empirical evaluation does not validate Theorem 3"** (from harsh critic): The claim that "the y-axis for the third column shows several curves; the paper does not explain what these curves represent" — I verified that the caption says "Each curve in the plots corresponds to a different pair of inputs." While this is a valid criticism about clarity, the core issue that experiments don't confirm the theory is real. → **Kept as Major weakness 5.**

- **"Missing related works"**: The harsh critic mentions missing citations (Poole et al., Schoenholz et al., Hayou et al.) but references are in the removed appendix section — I cannot verify if they are cited. → **REMOVED per instructions: Do not mention missing related works as I cannot confirm their absence.**

- **"The proof sketch of Proposition 1 is uninformative"**: This is accurate — the sketch is indeed too brief. → **Kept as Minor weakness 7.**

- **"Proof of Theorem 2 is not given; the appendix is missing"** (from harsh critic): The proofs are in Appendix C, which is removed from the submission. The instruction says to assume appendices exist in the original. → **REMOVED.**

- **"Formatting nitpicks"** (e.g., typo in conclusion): → **REMOVED per instructions about formatting artifacts.**

## Novel Insights

The harsh critic's identification of the mathematical error in Proposition 5 property (4) is a genuine insight: the function \(\psi_d\) approximates a step function as \(d\to0\), so its derivatives diverge (not vanish) at the origin. This means the entire rough-path construction cannot achieve the claimed convergence, and the paper's central theorem is unsupported. Beyond this, no novel insight emerges from the reviews that the paper itself does not already attempt to claim.

## Suggestions

1. **Fix or remove Theorem 3.** The current proof is unsalvageable as written. If the result is true, it requires a fundamentally different proof that does not rely on the false property (4). A direct analysis of the limit of \(\kappa_x^\top\kappa^{-1}\) using the explicit NTK formulas (Propositions 2 and 4) without rough path theory would be a more promising direction.

2. **Acknowledge prior work on ρ→1.** The paper should cite the mean-field literature (Poole et al. 2016, Schoenholz et al. 2017) and clearly state what is new in Proposition 4/Theorem 2 versus what is known.

3. **Improve Figure 1** by labeling curves, explaining what each trace represents in the third column, and providing error bars or multiple random seeds.

---

## Score and Decision

**Round 1 bracket:** Based on the topic-anchored calibration search, low-band NTK papers (score < 3.5) averaged 2.33–3.00, mid-band (3.5–7.5) averaged 4.25–6.00. The weakness-anchored queries returned papers with flawed proofs scoring 2.33–3.00. My initial bracket: **2.5–3.5**.

**Round 2 narrowing:** I compared the paper against several anchors in the 3–6 range. The "NTK with Derivative Labels" paper (fUz6Qefe5z, avg 3.00) shares the same failure mode: a central theoretical claim whose proof is not rigorous, with experiments that don't compensate. The "Weak Correlations" paper (2NwHLAffZZ, avg 2.33) had even worse presentation issues. The current paper is better written than the 2.33 anchor but shares the fatal proof flaw of the 3.00 anchor. The "Positive Definiteness of NTK" paper (YN4uWzcbtt, avg 4.25) had incremental but *sound* mathematics — the current paper is worse because the proof is flawed, not just incremental.

**What the low-band anchors failed at:** The 3.00-rated "NTK with Derivative Labels" paper had a handwavy mathematical proof that left reviewers unconvinced, with insufficient experimental support. The current paper shares *exactly* this failure — the RDE proof of Theorem 3 is not just handwavy but mathematically incorrect (property (4) of ψ_d), and the experiments provide no validation of the central claim.

**Final score:** 3.0. The paper has some valid content (Proposition 4, Theorem 2 as a corollary) and is reasonably well-organized, but its central claimed contribution (Theorem 3) is not validly proved, constituting a fatal flaw. The paper cannot be accepted in its current form.

### Anchors consulted

| Path | Avg Score | Round | Query Bucket | Comparison |
|------|-----------|-------|-------------|------------|
| fUz6Qefe5z | 3.00 | R1 | topic-low | Shares fatal flaw: central proof not rigorous, experiments insufficient |
| NbbsRnPBoS | 2.33 | R1 | topic-low | Less relevant (depth in linear networks) |
| 2NwHLAffZZ | 2.33 | R1 | topic-low, weakness | Worse presentation, shares unsupported proof claims |
| YN4uWzcbtt | 4.25 | R1 | topic-mid | Incremental but *sound* — current paper is worse |
| WH9NhxOeu9 | 5.00 | R1 | topic-mid | Sound generalization bounds — not comparable |
| VEJzjAvaIy | 5.75 | R1 | topic-mid | Sound NTK divergence proof — current paper is worse |
| 5EtSvYUU0v | 6.00 | R1 | topic-mid | Ambitious theoretical framework, mixed reviews |
| 3LLkES6nNs | 4.25 | R2 | weakness (RDE) | Incremental but sound — current paper is worse |
| V6JRkfj9dU | 4.67 | R2 | topic-mid | Sound generalization bounds |
| bWz8aOPwsJ | 3.75 | R2 | weakness (proof error) | Empirical NTK trace paper, different methodology |

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>