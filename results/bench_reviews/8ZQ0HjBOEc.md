Now I have all the information needed to synthesize the final review.

## Summary

This paper studies how the NTK of infinitely-wide ReLU networks behaves as depth goes to infinity. It proves that the normalized kernel entries converge monotonically to 1 (Theorem 2) and claims that the NTK regression expression $\kappa_x^\top \kappa^{-1}$ converges to a well-defined limit even though the kernel approaches a singular all-ones matrix (Theorem 3, via rough differential equations). It also distills general criteria under which such convergence holds.

## Strengths

- **Clean characterization of normalized kernel collapse (Theorem 2, Proposition 4):** The paper rigorously proves that $\bar{\Theta}_\infty^{(L)}(x,x')$ strictly increases to 1 as $L\to\infty$ for all pairs on the sphere, with a concrete recursive formula via $h(\rho^{(L)})$. This is a crisp, self-contained result that cleanly formalizes the well-known ordered-phase collapse for ReLU NTKs.

- **Generalizable convergence criteria distilled from the proof:** The paper explicitly lists three properties (diagonal dominance, eventual positive definiteness, determinant → 0) that suffice for the limiting expression to converge, and validates a second kernel ($\eta^{(L)}$) satisfying them. This abstraction makes the theory portable beyond the specific NTK case.

- **Identifying the conceptual obstacle:** The paper correctly identifies that the standard closed-form NTK solution (Proposition 3, from Jacot et al.) requires kernel invertibility, while Theorem 2 shows the kernel becomes singular as $L\to\infty$. Highlighting that $\kappa_x^\top\kappa^{-1}$ may remain well-defined even when $\kappa$ approaches a singular matrix is an interesting and non-trivial observation.

## Weaknesses

### Major

- **Theorem 3's proof is insufficient to establish the claimed result:** Even accounting for material deferred to the appendix (which is stripped from the parser), the proof sketch in the main text (lines 197–229) has critical gaps: (i) the determinant inequality involving $\psi_{\mathcal{D}}$ is asserted without derivation; (ii) the convergence of $v_{(i,j)}$ to 0 in 1-variation is stated without verification; (iii) the application of Lyons' Universal Limit Theorem is invoked without checking its preconditions (convergence of the rough path lift in the appropriate $p$-variation topology); and (iv) the connection between the RDE solution and the claimed bound $\| (\tilde{\Theta}_\infty^{(L)}(XX^\top))^{-1} \tilde{\Theta}_\infty^{(L)}(x^\top X) \|_2 \in \mathcal{O}(n)$ is not clearly established. These gaps undermine the paper's main theoretical contribution. The proof requires a major overhaul before Theorem 3 can be accepted as proven.

- **No connection between the theoretical limit and actual neural network outputs in the singular regime:** Proposition 3 (Jacot et al.) gives the closed-form output *only* when the limiting kernel is invertible. Theorem 2 shows the kernel approaches a rank-1 singular matrix. Theorem 3 bounds the mathematical expression $\tilde{\Theta}_\infty^{(L)}(x^\top X^\top)(\tilde{\Theta}_\infty^{(L)}(XX^\top))^{-1}$ but never verifies that this limit equals, or even approximates, the actual neural network output when the kernel is non-invertible. The paper's repeated claim to "not require any non-invertibility assumption" is misleading — the analysis is of the algebraic expression, not of the learned function in the singular regime. Without this link, the practical relevance of the claimed limit is unclear.

- **Experiments do not validate the core theoretical claims:** The experiments (Figure 1, Figure 3) show convergence of kernel entries ($\bar{\Theta}_\infty^{(L)}$, $\rho^{(L)}$, $\eta^{(L)}$) to 1, which Theorem 2 already proves. They do not evaluate the central object — the limiting expression $\tilde{\Theta}_\infty^{(L)}(x^\top X^\top)(\tilde{\Theta}_\infty^{(L)}(XX^\top))^{-1}$ — on actual datasets, with finite-width networks, or against any quantitative performance metric. There are no error bars, no comparisons to baselines, and no evidence that the claimed limit is meaningful for prediction. The experiments therefore provide no support for the paper's headline conclusions.

### Minor

- **The regime condition $L \in o(\min_i n_i)$ is stated but never used in any proof.** The theoretical results all analyze the deterministic infinite-width kernel $\Theta_\infty^{(L)}$ (width already sent to infinity) as $L\to\infty$. The joint scaling condition is mentioned to distinguish from Hanin & Nica (2020) but is never invoked mathematically. This disconnect between the stated setting and the actual analysis misleads about what is being proven.

- **The RDE machinery feels disproportionate to the result.** The constructed differential equation converges to $u'_\infty(t)=0$ (trivially constant). The paper does not explain why rough path theory is needed when the driving signal has bounded variation, nor why simpler matrix perturbation arguments would not suffice. This makes the proof feel over-engineered relative to the content it delivers.

### Trivial

- Theorem 3's statement has a dimensional inconsistency: $v_{ij}^{(L)} : [0,1] \to \mathbb{R}^n$ is a path in $\mathbb{R}^n$, but its rough path lift is said to be $\mathbf{v}^{(L)} : \Delta_{0,1} \to \mathbb{R}^{n \times n+1}$. The dimensions $\mathbb{R}^{n \times n+1}$ do not correspond to the standard rough path lift of an $\mathbb{R}^n$-valued path.

- The conclusion contains a confusing sentence: "the convergence for the limiting kernel is experimentally fast" — context suggests "limiting solution" is meant, not "limiting kernel."

## Nice-to-Haves

- The authors could prove much of Theorem 3 with simpler linear algebra arguments (e.g., analyzing the SVD of the perturbed kernel matrix) rather than invoking rough differential equations, which would make the paper more accessible.
- The paper could connect the result to practical recommendations: at what depth does the classifier become effectively constant, and can this be predicted from the condition number of $\Theta_\infty^{(L)}(XX^\top)$?

## Removed Points

These points were flagged by reviewers but removed per instructions:

- Criticisms that the abstract's claim about "arbitrary data with support on the sphere" contradicts the non-colinearity condition — these are about different regimes (data preprocessing vs. data support) and the paper is clear about this.
- The claim that cases (a–c) "contradict" Theorem 2's singularity result — these are about fixed $L$ vs. $L\to\infty$, no contradiction exists.
- Complaints about Proposition 1's proof sketch being incomplete — the proposition is a well-known computation (Cho & Saul 2009) and the sketch is adequate.
- Missing related works — cannot be verified without external sources.
- Formatting nitpicks and missing appendix references — parser artifacts.
- "Strength" about empirical validation — experiments are too weak to qualify as a genuine strength given verified weaknesses.
- "Strength" about "elegant resolution" via RDEs — conflicts with the verified weakness that the proof is insufficient; moved here for caution.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any meta-insight not already present in the paper.

## Suggestions

1. **Fix Theorem 3's proof.** Either provide a fully rigorous RDE argument that checks all preconditions (explicit definition of driving paths, verification of convergence in $p$-variation, verification of Lipschitz continuity for the Itô-Lyons map), or replace the RDE machinery with a simpler matrix analysis that establishes the same result. The current sketch is not publication-ready.
2. **Clarify what exactly is being proven.** The paper should explicitly state whether Theorem 3 establishes the limit of $\kappa_x^\top \kappa^{-1}$ (a mathematical expression) or the limit of the neural network output. If the former, the claim to "not require any non-invertibility assumption" should be scoped carefully — Proposition 3 still requires invertibility to connect to the learned function.
3. **Strengthen the experiments.** The main theoretical claim is about the behavior of $\tilde{\Theta}_\infty^{(L)}(x^\top X^\top)(\tilde{\Theta}_\infty^{(L)}(XX^\top))^{-1}$ — evaluate this expression explicitly, compare it to finite-width neural network outputs, and include quantitative metrics (e.g., prediction accuracy, regression error) with error bars across multiple seeds.
4. **Either use or remove the $L\in o(\min_i n_i)$ condition.** If it is needed, explain where and how; if it is only a scope-setting remark, say so clearly and do not present it as part of the analysis.
5. **Fix the dimensional inconsistency** in Theorem 3's statement and the typo in the conclusion.

## Score and Decision

**Calibration anchors (retrieved from human review corpus):**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `IKy24F8tGn.md` (ResNet depth) | 2.00 | Weaker: core theorem fundamentally flawed; this paper's Theorem 2 is solid. |
| `HksswvbYIp.md` (Empirical NTK) | 3.50 | Similar quality: both have limited experiments and incomplete theoretical connections; this paper has more theory but less empirical validation. |
| `wGc6aWvRLa.md` (ReLU convergence) | 4.50 | Stronger: more rigorous theory with clear proof of convergence; this paper's main theorem is less substantiated. |
| `U6SnDgI3gG.md` (NTK vs CNTK spectra) | 6.00 | Significantly stronger: clean theory with proper experiments and validation at an accepted venue. |
| `0elvad3gEu.md` (NTK width determination) | 5.50 | Stronger: well-connected theory and experiments; this paper's main theorem lacks comparable support. |
| `vokk8t1gnp.md` (Weak correlations) | 5.33 | Stronger: novel theoretical framework with proper proof and empirical validation. |
| `nCsF3Bsn2n.md` (Probabilistic kernel) | 8.00 | Much stronger: rigorous theory with extensive experiments and practical impact. |

The paper presents an interesting conceptual direction (analyzing the NTK regression expression when the kernel becomes singular) and has some genuinely solid results (Theorem 2, Proposition 4, the general criteria). However, the main theoretical contribution (Theorem 3) has significant proof gaps, the connection to actual neural network outputs is not established, and the experiments do not validate the core claims. Relative to the calibration anchors, the paper falls below accepted standards at ICLR.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>