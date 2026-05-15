Now I have all the information needed to write the consolidated review. Let me compose it.

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

Let me write the final review now.

---

Actually, let me also check one more thing about the paper's introduction framing to verify whether the harsh critic's point about oracle model mixing is valid.

The paper's Table 1 compares:
- Classical results with first-order oracle
- Their quantum results with zeroth-order oracle

The critic says "comparison with classical algorithms mixes oracle models (quantum zeroth-order vs classical first-order) without explicit discussion of whether this is a fair comparison."

The paper's techniques section says: "the proposed algorithm uses QuantumGradientEstimation to efficiently estimate the gradient through quantum zeroth-order oracle." So the paper does note that it uses zeroth-order oracle to get gradient information. This is standard in the field - quantum zeroth-order is considered the quantum analog of classical first-order because Jordan's method extracts gradient from function queries.

I'll remove this criticism.

Let me now write the final review.Here is my final consolidated review.

## Summary

This paper gives a quantum algorithm for minimizing the maximum of \(N\) convex, Lipschitz functions, achieving complexity \(\tilde{O}(\sqrt{N}\epsilon^{-5/3}+\epsilon^{-8/3})\) — a quadratic improvement in \(N\) over the classical state of the art — and proves a lower bound of \(\tilde{\Omega}(\sqrt{N}\epsilon^{-2/3})\), establishing near-optimality in the dependence on \(N\). The speedup arises from a quantum subroutine that replaces the classical \(\Omega(N)\)-cost softmax sampling with \(\tilde{O}(\sqrt{NK})\) queries using quantum maximum-finding and state preparation. The lower bound argument introduces a multi-round unstructured search problem to control sub-exponential success probabilities in the progress-control framework.

## Strengths

- **Near-optimal quantum speedup in \(N\).** The main theorem (Theorem 1) states an upper bound \(\tilde{O}(\sqrt{N}\epsilon^{-5/3}+\epsilon^{-8/3})\) against a lower bound \(\tilde{\Omega}(\sqrt{N}\epsilon^{-2/3})\). Compared to the classical \(\tilde{O}(N\epsilon^{-2/3}+\epsilon^{-8/3})\) from Carmon et al. (2021), the quadratic improvement in \(N\) is clear, and the lower bound shows it is optimal in \(N\) up to polylog factors. Table 1 presents the comparison cleanly.

- **Novel integration of quantum Gibbs-like sampling into the BROO framework.** The paper identifies that the bottleneck in Carmon et al.'s classical ball-regularized optimization oracle is the softmax sampling step, which costs \(\Omega(N)\) classically. Algorithm 2 and Lemma 1 show how to produce \(K\) copies of the softmax state using \(O(\sqrt{NK}\log(1/\delta))\) quantum queries — a genuine quadratic speedup — and then feed them into Epoch-SGD-Proj. This is a clever and non-trivial combination of existing quantum primitives.

- **Lower bound via multi-round unstructured search.** The lower bound argument (Section 4) adapts the classical zero-chain hard instance and introduces a multi-round variant of unstructured search to handle the issue that a single round has only polynomially small failure probability. The idea that each step of progress along the chain requires solving an unstructured search problem, and that multiple rounds must be solved adaptively, is technically novel and may be of independent interest for future quantum lower bounds.

- **First quantum algorithm for this problem via trust-region methods.** The paper explicitly notes that quantum speedups for trust-region/ball-optimization frameworks were previously open, and this work provides the first such result (Techniques paragraph).

## Weaknesses

### Fatal
None.

### Major

1. **Mismatch between Algorithm 3's description and Lemma 1's claim about the sampling distribution.** Algorithm 3 (Quantum sampling of the softmax distribution) explicitly replaces the true tail probabilities \(\exp(f_i(\bar{x})/\epsilon')\) for indices outside the detected top-\(K\) set with the constant \(\exp(h/\epsilon')\) (where \(h\) is the \(K\)-th largest value), producing the *approximate* distribution \(w'\). Yet Lemma 1 claims the algorithm produces \(K\) samples from the *true* distribution \(p_i = \exp(f_i(\bar{x})/\epsilon') / \sum_j \exp(f_j(\bar{x})/\epsilon')\). The main text says only "More explanation is given in Appendix" and "We present the proof of this lemma in Appendix." Without seeing the appendix, it is unclear whether the amplitude amplification step somehow corrects this approximation, or whether Lemma 1 is stated imprecisely. This is not a trivial gap: if the bias from the tail approximation is not properly controlled, the stochastic gradient estimator in Algorithm 2 becomes biased, and the convergence guarantee from Epoch-SGD-Proj (which assumes unbiased gradients) may fail. The main text provides no analysis of the total variation distance between the true and approximate distributions, nor any calculation showing how large \(K\) must be to render the bias negligible. Given that the entire query complexity speedup depends on \(K\) being much smaller than \(N\), this needs to be resolved in the main body or at least sketched there.

2. **Unstated assumption about differentiability for Jordan's gradient estimation.** Proposition 4 states that QuantumGradientEstimation outputs \(\nabla f_i(x)\) using one query. Jordan's original algorithm assumes the function is differentiable with bounded partial derivatives. The paper only assumes each \(f_i\) is convex and \(L\)-Lipschitz — these functions are differentiable almost everywhere but need not be differentiable at the specific query point the algorithm chooses. The stochastic gradient in Algorithm 2 (line 6) uses \(\nabla f_i(x)\) directly at whatever point \(x\) the algorithm visits. The paper provides no justification that Jordan's method returns a correct gradient (or a valid subgradient) at nondifferentiable points. While this is standard practice in the quantum optimization literature (e.g., Chakrabarti et al. 2020, Sidford & Zhang 2023), and the issue is mitigated by the fact that convex Lipschitz functions are differentiable at almost every point and subgradient methods are robust, a rigorous theoretical paper should either explicitly assume differentiability or provide a brief justification. As written, this is a gap in the formal assumptions.

### Minor

1. **The \(\epsilon\)-gap between upper and lower bounds is non-trivial.** The quantum upper bound has leading term \(\tilde{O}(\sqrt{N}\epsilon^{-5/3})\) while the lower bound is \(\tilde{\Omega}(\sqrt{N}\epsilon^{-2/3})\) — a gap of \(\epsilon^{-1}\). The paper acknowledges this as an open question, which is commendable, but the gap is large enough that the algorithm is provably non-optimal in \(\epsilon\). This does not undermine the headline contribution (optimality in \(N\)), but it limits the practical relevance unless \(\epsilon\) is relatively large.

2. **Key derivations entirely deferred to the appendix.** The proof of Lemma 1 (quantum sampling), the proof of Proposition 5 (progress control), and the full lower bound proof are all delegated to the appendix. While this structure is standard for theoretical papers, it means a reviewer cannot verify the correctness of the algorithm's central subroutine without the appendix. In particular, the bias analysis for the approximate softmax distribution (raised above) is entirely absent from the main text.

### Trivial

- The complexity expression in Theorem 4 contains a division by \(\log N\) in its explicit form. While this is absorbed into the \(\tilde{O}\) notation and is technically correct (it yields \(\operatorname{poly}(\log N)\) factors), the explicit formula looks unusual and may indicate that the polylog factors from different sources were not combined in the cleanest way.

## Nice-to-Haves

- A brief calculation in the main text showing the total variation distance between the approximate sampling distribution \(w'\) and the true distribution \(p\), with a sketch of how large \(K\) must be (as a function of \(N\) and \(\epsilon'\)) to keep the stochastic gradient bias within the tolerance of the Epoch-SGD-Proj analysis. This would greatly increase confidence in the main claim without needing to consult the appendix.

- A short remark in the preliminaries addressing the differentiability assumption for Jordan's method — e.g., noting that convex Lipschitz functions are differentiable almost everywhere and that at nondifferentiable points the algorithm can be viewed as returning an approximate subgradient, which is sufficient for the SGD analysis.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Unfair comparison mixing oracle models (quantum zeroth-order vs classical first-order)."** This is standard practice in quantum optimization: the quantum zeroth-order oracle is the natural quantum analog of the classical first-order oracle because Jordan's method extracts gradient information from function-value queries. The paper explicitly notes this connection in the Techniques section. Removed per Hard Rules (factually standard practice; the paper already addresses it).

- **"Parameter choices \((\eta_1, D_1, T_1)\) not justified in the main text."** These are standard parameters inherited from the classical Epoch-SGD-Proj analysis. It is normal for theoretical papers to state parameters without deriving them in the main text. Removed per Hard Rules (reproducibility nitpick about standard implementation details).

- **"The paper's gap between upper and lower bounds in \(\epsilon\) limits practical relevance."** The paper already candidly acknowledges this as an open question. Framing it as a weakness the paper failed to address misrepresents the paper's own transparency. Weakened to Minor weakness #1 above rather than treated as a separate flaw.

- **"Comparison of results in Table 1 should note that quantum zeroth-order is as powerful as classical first-order through Jordan's trick."** The paper's Techniques section already explains this. Removed as the paper already addresses it.

- **"Division by \(\log N\) in Theorem 4 indicates a sloppy derivation."** This is a presentation nitpick about an explicit formula that is correct up to polylog factors and absorbed into \(\tilde{O}\). Moved to Trivial.

- **Strength Finder's claimed strength "Clean use of standard quantum primitives in a novel combination."** This is generic; any good quantum algorithm paper combines standard primitives. Moved here.

## Novel Insights

The multi-round unstructured search problem introduced for the lower bound (Section 4) is a genuinely interesting technical innovation. Standard progress-control arguments for quantum lower bounds fail when the success probability per step is polynomially small rather than super-polynomially small (because polynomially small success probabilities allow accumulation over multiple steps). The paper's solution — chaining unstructured search problems so that each round's solution unlocks the next — forces algorithms to solve them adaptively, preventing parallel accumulation of small success probabilities. This technique could be useful for other quantum lower bounds where the hard instance's per-step progress has only polynomial hardness.

## Suggestions

1. **Clarify the sampling distribution issue.** Either modify the description of Algorithm 3 to match Lemma 1 (if the amplitude amplification step indeed corrects the approximation), or modify Lemma 1 to state that the algorithm produces samples from an approximate distribution whose bias is bounded, and include a brief bias bound in the main text.

2. **Add a sentence addressing differentiability.** In the preliminaries or when introducing Proposition 4, note that convex Lipschitz functions are differentiable almost everywhere (Rademacher's theorem) and that Jordan's method can be applied; at nondifferentiable points one can work with subgradients obtained via limiting finite differences, and the SGD analysis is robust to this.

3. **Add a brief sketch of the bias analysis from the sampling subroutine** in Section 3 (even 3–4 lines showing the total variation bound and how \(K\) scales). This would make the main argument self-contained and allow the reader to verify the soundness of the algorithm without reading the appendix.

## Score and Decision

This is a solid theoretical paper with an interesting core result: a quantum algorithm that provably achieves a quadratic speedup in \(N\) for a well-motivated optimization problem, together with a matching lower bound showing near-optimality. The strengths — the quantum speedup for the softmax sampling bottleneck, the clean integration into the BROO framework, and the novel multi-round search lower bound — are genuine and well-articulated.

The major concerns are (1) the mismatch between Algorithm 3's description (approximate distribution) and Lemma 1's claim (exact distribution), which creates uncertainty about the correctness of the central subroutine, and (2) the unstated differentiability assumption for Jordan's gradient estimation. Both are likely addressable (the appendix presumably contains the missing analysis), but as presented in the main text, they leave gaps that prevent full confidence in the results.

The paper has clear contributions and the main direction is convincing. However, given that the central algorithmic claim depends on resolving these gaps, I recommend a borderline assessment.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>