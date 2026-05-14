Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper proposes a simplified spectral algorithm for community detection in the two-community stochastic block model, eliminating the degree-based row/column deletion preprocessing step and the correction step from Chin et al. (2015). The authors claim that spectral partition alone achieves inverse-log error rates matching information-theoretic limits, and they support this with a heuristic Chernoff-bound analysis of the second eigenvector's entry distribution, Monte Carlo simulations, and experiments on synthetic graphs.

## Strengths

- **Valid algorithmic simplification (Theorem 2.2):** The paper correctly identifies that the degree-based row/column deletion step from Chin et al. (2015) can be eliminated while preserving the spectral norm bound on the noise matrix \(M = A - \mathbb{E}[A]\). The appendix provides a proof sketch using results from Füredi & Komlós (1981) and Krivelevich & Vu (2000). This is a genuine, albeit minor, contribution.

- **Sharpness characterization of the original bound (Section 3.2):** The optimization formulation demonstrating that \(\gamma = \sin^2\theta\) is tight in the worst case is correct and well-reasoned. The construction with \(x_1 = \cdots = x_{n-k} = 1/\sqrt{2(n-k)}\) and middle entries set to zero cleanly achieves equality up to constants, confirming that Theorem 3.2 of Chin et al. is sharp without exploiting eigenvector structure.

- **Insight about perfect recovery with imperfect alignment:** Both the Chernoff analysis and Monte Carlo simulations reveal that \(\gamma = 0\) (perfect recovery) can be achieved even when \(\sin\theta > 0\). This correctly highlights that eigenvector alignment is not the sole determinant of recovery quality — the distributional shape of the entries matters. This observation is conceptually interesting and could motivate future work.

## Weaknesses

### Fatal

None that completely invalidate every contribution. The paper has genuine elements (Theorem 2.2, the optimization sharpness result in Section 3.2), but the central claim is substantially undermined by the issues below.

### Major

- **Regime confusion between theoretical framing and experimental validation.** The paper's abstract says "under constant edge density assumptions" (dense regime), but the introduction and theoretical discussion are framed entirely in terms of sparse SBM results: Theorems 1.2 and 1.3 from the literature are sparse-regime theorems, and the paper positions itself as improving upon Chin et al. (2015) which operates in the sparse regime (constant \(a, b\), edge probabilities \(a/n, b/n\)). However, every experiment uses \(a = 0.06n, b = 0.04n\), making edge probabilities constant at 0.06 and 0.04 — the dense regime. In this regime, \((a-b)^2/(a+b) = 0.004n\) grows linearly with \(n\), so the condition in Theorem 1.3 is trivially satisfied for any fixed \(\gamma\) at large \(n\), and community recovery becomes asymptotically easy. The empirical observation that \(\gamma\) decreases with \(n\) is therefore expected, not surprising. The paper's headline claim — that the correction step is unnecessary — is tested only in a regime where the correction step was never the bottleneck. This mismatch between the theoretical context (sparse SBM) and experimental regime (dense SBM) means the central empirical claim is not adequately supported. *The paper must either rescope its contribution to the dense regime and drop comparisons to sparse-regime results, or run experiments with constant \(a, b\) to properly test the claim.*

- **Heuristic "theory" presented as rigorous analysis (Sections 3.3–3.5).** The Chernoff-bound derivation that produces the optimization constraints (Equation 11) contains a critical gap. The analysis treats the entries of \(A\mathbf{u}_2\) as if they were i.i.d. samples from the difference-of-binomials distribution. Step A.2.3 in the appendix sets \(i/(2n+1) \leq C \cdot e^{-t^* x_i}\) by arguing that "the probability that a random entry exceeds \(x_i\) should be approximately \(i/(2n+1)\)," which is an order-statistic argument that requires exchangeability or independence. The entries of \(A\mathbf{u}_2\) are not independent — different rows share edges (though the dependence is weak, \(O(1/n)\) per pair). The paper never addresses this. Additionally, the claim in Section 2.1 that removing degree deletion "preserves the independent distribution of matrix entries and can subsequently maintain independence in the entries of eigenvector \(\mathbf{w}_2\)" is simply incorrect: eigenvector entries are never independent regardless of preprocessing, since they are coupled through the eigenvalue equation. The Chernoff analysis and normal approximation are reasonable heuristics — and the paper sometimes calls them "predictions" — but they are repeatedly described as "theoretical analysis," "theoretical predictions," and are used to claim "improved bounds." This is a gap between what is claimed and what is actually established. A rigorous analysis would need to account for the joint distribution of the eigenvector entries or at minimum quantify the error from the independence approximation.

### Minor

- **Overclaim about bridging to Theorem 1.3 (Section 4).** The empirical fit \(\sin\theta = C/(\log(2/\gamma))^{1/4}\) is obtained by OLS regression on dense-regime data and is presented as directly yielding the final result of Theorem 1.3. Curve-fitting experimental data does not constitute a proof, and the connection to the theorem is asserted rather than derived. The paper should clearly distinguish between empirical observations and proven theorems.

- **The convergence analysis (Section 4.1) proves little.** The observation that the gap between algorithm performance and Monte Carlo predictions shrinks as \(O(1/\sqrt{n})\) matches the known \(\ell_\infty\) error bound from Abbe et al. (2019) and is expected behavior. It does not independently validate the paper's novel claims.

### Trivial

- The paper occasionally blurs the line between rigorous proof and heuristic derivation — e.g., using language like "our theoretical analysis identifies" for what is essentially a Chernoff heuristic. The writing would benefit from clearer signposting of which claims are proven, which are heuristic predictions, and which are empirical observations.

## Nice-to-Haves

- Experiments with constant \(a, b\) (sparse regime) to assess whether the simplified algorithm actually achieves inverse-log scaling in the setting where Chin et al.'s correction step was designed and matters.
- A direct comparison of the empirical error rate against the information-theoretic lower bound from Zhang & Zhou (2015) (Equation 2), rather than only fitting a curve between \(\sin\theta\) and \(\gamma\).
- A more careful discussion of the entrywise dependence structure of \(A\mathbf{u}_2\) and its implications for the Chernoff analysis, even if only to acknowledge the approximation being made.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic claim that entries are "strongly correlated":** Removed — the dependence between different entries of \(A\mathbf{u}_2\) is through at most one shared edge per pair, giving \(O(1/n)\) covariance. The dependence is weak, not "strong," though the independence assumption remains technically unjustified. The core weakness (lack of rigorous justification for the i.i.d. treatment) is preserved above in softened form.

- **Strength Finder claim that "tighter error bounds through eigenvector distribution analysis" is a core strength:** Removed — this conflicts with the verified major weakness that the Chernoff analysis is heuristic rather than rigorous. The idea is interesting but the execution lacks rigor.

- **Strength Finder claim that "simplified algorithm empirically achieves inverse-log error scaling without correction" as a strong core strength:** Demoted — the empirical observation exists but is obtained in the dense regime where the result is not surprising. Included as a minor strength with appropriate caveat above.

- **Strength Finder claim that "convergence analysis validates the distributional approximation":** Demoted — the \(O(1/\sqrt{n})\) convergence merely reproduces the known entrywise error bound from Abbe et al. and does not independently validate the paper's novel claims.

- **Harsh critic's formatting/style nitpicks and concerns about missing appendix/proofs:** Removed per hard rules — the appendix exists in the original submission and formatting artifacts are parser issues.

- **Harsh critic's demand for experiments comparing against the Zhang & Zhou information-theoretic lower bound:** Moved to Nice-to-Haves — this would strengthen the paper but its absence does not invalidate the current contribution.

- **Harsh critic's point about "the suggestion that algorithmic complexity does not improve performance is unsupported":** Removed — this is a concluding remark, not a core claim being evaluated. The paper's main claims are about the spectral algorithm, not a general principle about complexity.

## Novel Insights

The optimization formulation in Section 3.2, which shows that \(\gamma = \sin^2\theta\) is sharp by constructing a worst-case vector that concentrates all mass in the correctly-classified entries and sets misclassified-region entries to zero, is genuinely instructive. This cleanly separates the geometric constraint (how misaligned the eigenvector is) from the algorithmic question (whether the spectral algorithm actually produces vectors with this worst-case structure). The recognition that the spectral algorithm's eigenvector has a specific distributional shape — roughly a difference-of-binomials — that prevents it from hitting the worst case is the right conceptual insight. The paper's execution of this insight into rigorous bounds falls short, but the framing is valuable.

## Suggestions

- **Clarify the asymptotic regime immediately and consistently.** If the paper is about the dense SBM (constant edge probabilities), state this in the introduction and explain why comparisons to sparse-regime results like Chin et al. are still meaningful. If the paper claims results for the sparse regime, the experiments must use constant \(a, b\).

- **Reposition the Chernoff analysis as a heuristic prediction, not a theoretical bound.** The current language ("our theoretical analysis identifies," "improved bounds") overstates the rigor. Call it a "distributional heuristic" or "approximate analysis" and clearly state the independence assumption being made.

- **Remove or correct the claim about eigenvector entry independence (Section 2.1, line 262–263).** The eigenvector entries are not independent; the benefit of removing the degree-deletion step is the simpler algorithm and the preservation of matrix-entry independence, which is useful for other reasons (e.g., easier bootstrap/resampling).

- **Run at least one experiment in the sparse regime** (e.g., \(a = 30, b = 20\), edge probabilities \(30/n, 20/n\)) to show whether the spectral-partition-only algorithm gets close to inverse-log rates when edge density is low. Without this, the paper's central claim remains unvalidated in the regime that matters.

## Score and Decision

### Anchor comparison:

- **`A0YvRCa5jM` (avg 3.0, Reject):** GNN community detection paper with theoretical-experimental mismatch and unclear assumptions. Similar level of gap between claims and evidence as the current paper, though the current paper has more genuine nuggets (Theorem 2.2, the optimization sharpness result).
- **`zWL3AwI4kq` (avg 4.5, Reject):** Streaming community detection with solid theory but readability issues. Stronger theoretical foundation than the current paper, whose "theory" is largely heuristic. The current paper's central claim has weaker support.
- **`pliEmukDsv` (avg 5.0, Reject):** Column thresholding with solid theory under a restrictive condition. Has genuine theoretical contributions that the current paper lacks.
- **`0GpolO2auw` (avg 6.0, Accept Poster):** Sublinear spectral clustering oracle with substantial non-trivial theory. Well above the current paper in rigor and contribution.
- **`nCsF3Bsn2n` (avg 8.0, Accept Oral):** Strong theory + experiments, clear contribution. Far above the current paper.
- **`euLwjbiza4` (avg 3.0, Reject):** Sparsification algorithm improvements, limited significance. The current paper has more ambition but similar issues with claims exceeding evidence.
- **`FQ2dMjf88y` (avg 4.0, Reject):** Dynamic coreset spectral clustering, mix of theory and experiments. Comparable in the gap between theoretical ambition and delivered results.

**Calibration:** The current paper shares with the 3.0 anchor (A0YvRCa5jM) a significant gap between theoretical claims and experimental validation. Its genuine contributions (Theorem 2.2, the optimization sharpness result) are real but incremental. The regime confusion and heuristic-theory-presented-as-rigor are serious issues that prevent acceptance. The paper is below the 4.5–5.0 band where papers have solid (if limited) theoretical contributions. I judge it at **3.5** — reject, with the caveat that if the authors rescope to the dense regime and recharacterize the Chernoff analysis as heuristic, a future version could be publishable at a workshop.

**Evaluation axes:** The research question (whether the correction step is necessary) is interesting and well-motivated (moderate originality). However, the claims are not well supported due to the regime mismatch and heuristic analysis (poor soundness). The writing is generally clear despite the theoretical content. The value to the community is limited in current form due to the unresolved issues.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>