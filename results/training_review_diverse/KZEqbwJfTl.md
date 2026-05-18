Now I have thoroughly verified all claims against the paper. Let me produce the consolidated review.

## Summary

This paper studies agnostic conditional (selective) classification — selecting a subset of data via a halfspace selector and then minimizing classification error on that subset — under Gaussian marginals. It presents three main contributions: (1) a polynomial-time algorithm achieving \(\tilde{O}(\sqrt{\text{opt}})\) conditional error for homogeneous halfspace selectors with finite classifier classes, (2) a claimed extension to sparse linear classifiers via list learning, and (3) hardness results showing that, under cryptographic assumptions, the problem becomes intractable for general (non-homogeneous) halfspaces, and that conditional classification is at least as hard as standard agnostic classification.

## Strengths

1. **First algorithmic result for agnostic conditional classification with a provable approximation guarantee**: For the restricted but theoretically meaningful setting of finite classifier classes and homogeneous halfspace selectors under Gaussian marginals, Theorem 3.1 claims a polynomial-time \(\tilde{O}(\sqrt{\text{opt}})\)-approximation algorithm. This is the first such result in the agnostic setting, going beyond prior work that handled only the realizable case or lacked approximation guarantees relative to the optimal solution.

2. **Computational hardness result under cryptographic assumptions**: Theorem 4.3 shows that, under the sub-exponential continuous LWE assumption, no polynomial-time algorithm can achieve an additive error of \(\epsilon \le 1/\log^\gamma d\) (for \(\gamma > 1/2\)) for general halfspace selectors, even with Gaussian marginals. This cleanly delineates the boundary between tractable (homogeneous) and intractable (general) halfspace selectors.

3. **Reduction establishing that conditional classification is at least as hard as agnostic classification**: Proposition 4.5 and Claim 4.7 provide rigorous reductions showing that additive-error (resp. multiplicative) algorithms for conditional classification imply additive-error (resp. multiplicative) algorithms for standard agnostic classification with essentially the same parameters. The formal connection via Lemma 4.4 (error decomposition) is clean and useful.

4. **Novel surrogate analysis using the ReLU one-sided loss**: Proposition 3.2 exploits Gaussian antisymmetry and a geometric decomposition to relate the norm of the projected expected gradient to the one-sided conditional error. This analysis directly addresses the class-imbalance difficulty that prevents standard agnostic techniques from transferring to the conditional setting.

## Weaknesses

### Major

1. **Convergence analysis of Algorithm 2 (Projected SGD) is insufficiently justified in the main text.** The update rule uses \(g_{\mathbf{w}} = y \cdot \mathbf{x}_{\mathbf{w}^\perp} \cdot \mathbb{1}\{\mathbf{x} \in h(\mathbf{w})\}\), which is the projection of the subgradient of the surrogate loss \(\mathcal{L}_{\mathcal{D}}\) onto the subspace orthogonal to \(\mathbf{w}\). The paper explicitly states (line 65) that the goal is to minimize \(\|\mathbb{E}[g_{\mathbf{w}}]\|_2\), not \(\mathcal{L}_{\mathcal{D}}\) itself. However, the proof sketch for Proposition 3.3 (which claims convergence of \(\|\mathbb{E}[g_{\mathbf{w}}]\|_2\)) discusses boundedness of \(\mathcal{L}_{\mathcal{D}}\) and almost-Lipschitz continuity of \(\nabla\mathcal{L}_{\mathcal{D}}\) — properties of \(\nabla\mathcal{L}_{\mathcal{D}}\), not of the vector field being used for updates. Standard SGD convergence theory for smooth functions gives \(\|\nabla f(w)\| \to 0\); here the updates use projected gradients and the quantity of interest is the norm of the *projected* expected gradient. The sketch does not establish how the properties of \(\nabla\mathcal{L}_{\mathcal{D}}\) translate to convergence of \(\|\mathbb{E}[g_{\mathbf{w}}]\|_2\) under the specific update rule. The paper acknowledges (line 67) that the convergence analysis from Diakonikolas et al. (2020b) "does not obviously hold" and that the update is "similar to that of Shen (2021)" but with a "quite different gradient descent policy." This disconnect is left unresolved in the main text, and the claim that Lemma 3.4 follows from Propositions 3.2 and 3.3 rests on this gap. **Why it matters**: The convergence of Algorithm 2 is the algorithmic core of the paper's positive result (Theorem 3.1). If the convergence guarantee cannot be substantiated, the paper's headline positive contribution is unsupported.

2. **The claimed extension to sparse linear classifiers via list learning (Theorem 3.5) relies on an unaddressed assumption about the data distribution.** Robust list learning (Definition 1.3) assumes a mixture model \(\mathcal{D} = \alpha\mathcal{D}^* + (1-\alpha)\tilde{\mathcal{D}}\) where the inlier component \(\mathcal{D}^*\) has *exactly* clean labels under some target classifier \(c^*\). The conditional classification setting (Problem 1.2) makes no such assumption — \(\mathcal{D}\) is an arbitrary distribution (agnostic labels) with standard normal \(\mathbf{x}\)-marginal, and there is no guarantee of a "clean" component with exact labels anywhere. The paper does not explain how the mixture model assumption is satisfied (or circumvented) in the conditional setting. The main text states "our strategy is to use a robust list-learning algorithm to generate a finite list \(\mathcal{C}\)" (line 49) but does not address this incompatibility. Theorem A.1 (in the appendix, stripped) may address this, but the main text presents the extension as straightforward without acknowledging the gap. **Why it matters**: This extension is one of the paper's advertised contributions ("we also generalized our approach to work with any sparse linear classifiers"). If the gap cannot be closed, the scope of the positive result is limited to finite \(\mathcal{C}\), which is still a contribution but significantly narrower than claimed.

### Minor

3. **The interval-sweep in Proposition 4.5 is described without clarifying how the conditional algorithm handles arbitrary mass intervals.** The reduction sweeps over intervals of width \(O(\epsilon)\) to guess \(\Pr\{\mathbf{x} \in S^*\}\) for the optimal unconditional classifier, requiring \(O(1/\epsilon)\) calls to the conditional algorithm. This is standard and the overall \(\mathrm{poly}(d, 1/\epsilon, 1/\delta)\) runtime claim is plausible, but the presentation does not address whether the conditional algorithm's runtime depends on the interval width \(b-a\) or whether parameters need to be re-tuned per interval. This is a presentation-level gap rather than a structural flaw.

4. **The positive result is limited to homogeneous halfspaces (selecting exactly half the data), which is the regime where the advantage of conditional over standard classification is least pronounced.** The paper acknowledges this limitation honestly in Section 5. This does not invalidate the contribution but tempers its practical significance.

### Trivial

- None beyond presentation issues inherent to the PDF-extraction process.

## Nice-to-Haves

- Clarify how SPARSELIST (Algorithm 4) works without the mixture model assumption, or explicitly state the additional condition required, and delineate the scope of the positive result accordingly.
- Provide a self-contained convergence proof sketch for Algorithm 2 (or at minimum clarify how the properties of \(\nabla\mathcal{L}_{\mathcal{D}}\) imply convergence of \(\|\mathbb{E}[g_{\mathbf{w}}]\|_2\)).
- Add a brief discussion of the number of intervals needed in Proposition 4.5 and how the error propagates through the sweep.

## Removed Points

- *Critic's point about the interval sweep potentially degrading runtime to "non-polynomial"* — The paper claims poly runtime and \(O(1/\epsilon)\) calls preserves poly runtime. This is standard. The critic's concern about the conditional algorithm's runtime depending on interval width is speculative and not a structural gap in the reduction; the reduction assumes a black-box conditional algorithm with stated guarantees.
- *Critic's observation that "the paper should be evaluated against its actual scope (finite C and homogeneous halfspaces)"* — This is a restatement of the paper's own acknowledgment of limitations (Section 5), not a new insight.
- *Critic's claim that the convergence issue is "potentially fatal"* — Downgraded from Fatal to Major because (a) the paper is transparent about the algorithm not minimizing \(\mathcal{L}_{\mathcal{D}}\), (b) the full proof may reside in the appendix (stripped), and (c) the critic's argument confuses "insufficient sketch" with "fatal flaw." The gap is real but the paper's own acknowledgment and references to prior techniques suggest it may be addressable.
- *Strength Finder's strength about "generalization to infinite classifier classes via list learning"* — Moved here because this strength is contingent on the unaddressed mixture-model gap and conflicts with the verified weakness above.

## Novel Insights

The key structural insight — distinguishing homogeneous halfspaces (tractable, positive result) from general halfspaces (intractable, hardness via reduction from agnostic classification) — is the paper's own main contribution and is clearly presented. The reviews do not surface any genuinely novel observation beyond what the paper itself contributes.

## Suggestions

- Provide a complete proof of Proposition 3.3 (in the main text or a clearly referenced appendix) that explicitly connects the projected gradient updates to convergence of \(\|\mathbb{E}[g_{\mathbf{w}}]\|_2\), rather than relying on properties of \(\nabla\mathcal{L}_{\mathcal{D}}\) without establishing the link.
- Either justify the application of list learning under Problem 1.2's assumptions (explaining how the mixture model is satisfied or circumvented) or remove Theorem 3.5 and scale back to the finite-\(\mathcal{C}\) result, which remains a nontrivial contribution.
- Clarify in Proposition 4.5: enumerate the intervals explicitly, confirm the error propagation, and verify the conditional algorithm can be run with any interval \([a,b]\) without runtime dependence on \(1/(b-a)\).

## Score and Decision

The paper tackles a well-motivated problem and presents a clean conceptual separation between the tractable (homogeneous halfspaces) and intractable (general halfspaces) regimes. The negative result (Theorem 4.3, Proposition 4.5) appears on solid ground. However, the positive algorithmic result — the paper's headline contribution — has two significant weaknesses that together undermine its credibility in the current manuscript: (1) the convergence analysis of the core optimization routine (Algorithm 2) is insufficiently justified in the main text, leaving a gap between the claimed guarantee and the argument provided; and (2) the extension to sparse linear classifiers via list learning rests on an unaddressed incompatibility between the mixture model required by list learning and the agnostic conditional classification setting. These issues may be fixable in revision, but as presented, the positive contribution is not adequately supported. The paper should not be accepted in its current form.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>