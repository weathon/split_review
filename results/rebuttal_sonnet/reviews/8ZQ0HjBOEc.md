## Summary

This paper studies the behavior of the Neural Tangent Kernel (NTK) for infinitely wide, fully-connected ReLU networks as depth $L \to \infty$. The main contributions are: (1) Theorem 2 showing the normalized NTK $\bar{\Theta}_\infty^{(L)}$ converges to the all-ones matrix, and (2) Theorem 3 proving via a rough differential equation framework that despite this degeneracy, the kernel predictor ratio $\tilde{\Theta}_\infty^{(L)}(x^\top X^\top)(\tilde{\Theta}_\infty^{(L)}(XX^\top))^{-1}$ has a well-defined, bounded limit. Section 6 distills generalization criteria for other kernel families.

---

## Rebuttal Assessment

### Weakness: Abstract claims "closed-form solution approaches a fixed limit" — Theorem 3 proves only existence/boundedness

**Author's response:** Partially address

**Assessment:** Partially convincing. The author argues that "closed-form solution" in the abstract refers to the Jacot et al. (2018a) predictor expression itself (Proposition 3), which is genuinely closed-form, and that "approaches a fixed limit" means the predictor ratio converges — not that its limit has a closed form. This interpretation is defensible on a careful reading of the abstract (lines 9): the sentence structure is: [closed-form solution for the NTK predictor exists] → [that solution approaches a fixed limit]. However, the ambiguity is real and non-trivial: the abstract doesn't distinguish the full predictor from the kernel ratio term, and Theorem 3 only covers the ratio component $\kappa_x^\top\kappa^{-1}$, not the full predictor $f_\infty(x) = f_0(x) + \kappa_x^\top\kappa^{-1}(y^*-y_0)$. The promised revision to the abstract exists only in the rebuttal, not the paper.

**Score impact:** Weakness downgraded (from misrepresentation to ambiguity) but not removed.

---

### Weakness: Full predictor's $f_0(x)$ term as $L \to \infty$ is unanalyzed

**Author's response:** Acknowledge

**Assessment:** Unconvincing as a defense — honest but the gap remains. The author confirms Section 5 explicitly restricts attention to the kernel ratio term ("we describe how the term $\kappa_x$ from Proposition 3 approaches a fixed limit" — verified at line 129 of the paper). The paper consciously narrows its stated claim, which partially mitigates the strength of the original criticism (the paper is somewhat honest about scope). However, the Introduction motivates the work by characterizing "the output of the neural network" (line 15: "2) the limiting solution to the output of a fully-connected ReLU network"), which implies a full predictor result. The promised discussion paragraph does not exist in the current paper.

**Score impact:** Weakness unchanged — acknowledged limitation confirmed by paper, not remediated.

---

### Weakness: Notation inconsistency between $\bar{\Theta}_\infty^{(L)}$ and $\tilde{\Theta}_\infty^{(L)}$

**Author's response:** Partially address

**Assessment:** Partially convincing. The author claims both symbols denote the same normalized kernel of Definition 4. Verifying this against the paper: Definition 4 (line 137–139) defines $\bar{\Theta}_\infty^{(L)}$ with normalization $\frac{n_0 2^{L-1}}{L}$, and Section 3 lists $\bar{\Theta}_\infty^{(L)}$ as the normalized kernel. Theorem 3 and its proof (lines 173–225) use $\tilde{\Theta}_\infty^{(L)}$ without any definition or cross-reference. The proof's use of $\det(\tilde{\Theta}_\infty^{(L)}(XX^\top)) \to 0$ is indeed consistent with $\tilde{\Theta}$ being the normalized kernel, confirming the author's claim that these are the same object. This means the proof is mathematically consistent — the notation ambiguity is editorial, not a mathematical gap. However, the equating statement the author promises ("we will add an explicit equating statement before Theorem 3") does not appear in the current paper.

**Score impact:** Weakness downgraded — confirmed as editorial lapse without mathematical consequence, but still unfixed in the paper.

---

### Weakness: Rough-path machinery for $p=1$ is pedagogically counterproductive

**Author's response:** Partially address

**Assessment:** Partially convincing. The author gives three justifications: (1) $\psi_\mathcal{D} \in C^\infty$ makes $p=1$ the natural setting; (2) the rough-path framework generalizes structurally to $p>1$ for extension to other kernels; (3) uniformity on $S^{n_0-1}$ follows cleanly from Itô-Lyons map continuity and compactness. These are legitimate reasons, though (1) and (3) could be replicated with standard ODE theory. The reviewer's core point — that the Lyons Universal Limit Theorem reduces to Gronwall at $p=1$ and the rough-path formalism obscures rather than illuminates — remains valid. The author's best argument is (2), but Section 6 does not actually use $p>1$ variation; the other kernels just need to satisfy the same three criteria, for which $p=1$ suffices.

**Score impact:** Weakness unchanged — justifications are partially convincing but do not eliminate the pedagogical concern.

---

### Weakness: Internally inconsistent sentence in Conclusion

**Author's response:** Acknowledge

**Assessment:** Unconvincing as a defense — correctly diagnosed as a typographical error but the fix is only promised. The sentence "while convergence for the limiting kernel is sublinear, the convergence for the limiting kernel is experimentally fast" (line 262, verified) repeats "the limiting kernel" for both clauses. The author's intended contrast (slow convergence of $\tilde{\Theta}(XX^\top)$ vs. fast convergence of the predictor ratio) is clear and supported by Figure 1 and the surrounding text. The fix is not in the current paper.

**Score impact:** Weakness unchanged (trivial, but unfixed).

---

## Strengths

1. **Non-trivial limit despite kernel degeneracy**: Theorem 3 proves the predictor ratio converges to a bounded limit even as the kernel matrix degenerates. The $\psi_\mathcal{D}$ smoothing construction — scaled by the product of consecutive determinants — cleverly converts matrix singularity into an ODE perturbation problem (lines 195–225).

2. **Analysis without spectral assumptions**: Unlike Nguyen et al. (2021) and Murray et al. (2023), the derivation uses only convergence of $\rho^{(L)} \to 1$ (Lemma 1) and the rough-ODE framework — no Hermite/Mercer spectral assumptions (confirmed in Introduction, line 15–16).

3. **Solid secondary results**: Lemma 1 ($\rho^{(L)} \to 1$), Proposition 4 (recursive normalized kernel), and Theorem 2 ($\bar{\Theta}_\infty^{(L)} \to \mathbf{1}_n\mathbf{1}_n^\top$) are well-stated and form a solid theoretical foundation.

4. **Generalization criteria**: Section 6 identifies three checkable conditions (positivity, eventual positive-definiteness, vanishing normalized determinant) allowing extension beyond ReLU NTK, with the $\eta^{(L)}$ kernel as a concrete example (lines 239–243).

5. **Interpretable special case**: The result that $x = x_i \in X$ implies the limit is $e_i$ (the $i$-th standard basis vector) — stated in prose after the proof (line 227) — provides the most interpretable consequence, confirming interpolation behavior.

---

## Weaknesses

### Fatal
None.

### Major

- **Full predictor $f_\infty(x)$ is only half-analyzed**: Theorem 3 covers $\kappa_x^\top\kappa^{-1}$ but not $f_0(x)$ as $L \to \infty$. The Introduction claims to characterize "the limiting solution to the output of a fully-connected ReLU network" (line 15), but no analysis of $f_0(x)$ exists and no future-work caveat appears in the current paper. This gap between stated motivation and delivered result is substantive and acknowledged by the authors.

- **No characterization of the limit for $x \notin X$**: Theorem 3 proves existence and boundedness of $\lim_{L\to\infty} \kappa_x^\top\kappa^{-1}$ but gives no characterization of its form for test points outside the training set. For $x = x_i \in X$ the limit is $e_i$ (interpretable), but for general $x$ the limit remains unknown. The paper's abstract claim that the predictor "approaches a fixed limit" is technically correct but the limit's nature is uncharacterized.

### Minor

- **$\tilde{\Theta}$ undefined in main text**: Despite the author's rebuttal confirming $\tilde{\Theta} = \bar{\Theta}$, the paper never states this explicitly. A reader encountering Theorem 3 cannot verify the relationship without reconstructing it from the proof. This is an editorial failure at the junction of the paper's two main results.

- **Rough-path framing at $p=1$**: Using the Lyons Universal Limit Theorem for bounded-variation ($p=1$) paths is mathematically valid but pedagogically heavy, reducing to Gronwall-type classical ODE arguments. The generalization-to-other-kernels justification (the author's best argument) is only partially valid since Section 6's generalization still operates at $p=1$.

- **Conclusion typo** ("convergence for the limiting kernel" repeated in both clauses of a contrast) — confirmed, unfixed in current paper.

### Trivial
None beyond those noted.

---

## Nice-to-Haves

- Add a named corollary formalizing the $x = x_i \in X \Rightarrow \lim_{L\to\infty} \kappa_x^\top\kappa^{-1} = e_i$ case.
- Provide at minimum a qualitative conjecture about the form of the limit for general $x \notin X$.
- Add a short remark about $p=1$ simplification alongside the rough-path invocation, as the authors promised.
- Add a paragraph explicitly discussing $f_0(x)$ as a future-work item.

---

## Novel Insights

The paper's most conceptually original move is to bypass the matrix singularity of $\kappa(XX^\top)$ by treating the predictor ratio $\kappa_x\kappa^{-1}$ as the terminal value of an ODE solution, rather than computing it as a ratio of a degenerate numerator and denominator. The $\psi_\mathcal{D}$ function — scaled by the product of consecutive determinants — is cleverly designed so that as $\det(\tilde{\Theta}) \to 0$, the driving terms of the ODE system also vanish, converting a problem of matrix singularity into a problem of ODE perturbation with a well-controlled limit. The technique is potentially exportable to other settings where ratios of sequences of matrices degenerate.

---

## Suggestions

1. Unify the $\bar{\Theta}$ vs. $\tilde{\Theta}$ notation with an explicit equating statement before Theorem 3.
2. Add a formal corollary for the $x = x_i$ case.
3. Add a paragraph discussing $f_0(x)$ explicitly as future work, noting the current paper's scope restriction.
4. Revise the abstract to make clear that Theorem 3 establishes convergence of the ratio term, not the full predictor.
5. Add a remark noting that at $p=1$, the rough-path argument simplifies to classical ODE stability.

---

## Score and Decision

**Calibration against original review:** The original score was 4.5 (Reject). The rebuttal's impact:

- *Abstract claim*: Downgraded from "misrepresentation" to "ambiguity" — minor upward pressure.
- *$f_0(x)$ gap*: Confirmed and acknowledged; no new information changes the assessment.
- *Notation*: Confirmed as editorial only (not a mathematical gap) — minor upward pressure; the proof is sound.
- *Rough-path pedagogy*: Partially justified but not eliminated; neutral.
- *Conclusion typo*: Acknowledged, unfixed; neutral.

The rebuttal's most meaningful contribution is confirming that $\tilde{\Theta} = \bar{\Theta}$, which means Theorem 3's proof is mathematically consistent (the seam between Theorem 2 and Theorem 3 is intact). This removes one source of uncertainty from the original review. However, the two major weaknesses — incomplete coverage of $f_0(x)$ and no characterization of the limit for $x \notin X$ — remain fully in place, and the promised revisions do not exist in the current paper. The paper's fundamental contribution (Theorem 3's proof technique) is genuinely novel and the mathematics appears sound, but the presentation remains incomplete.

Adjusting from 4.5 to 5.0 to reflect: (1) the notation concern being resolved as editorial rather than mathematical, (2) the abstract reading being defensible (not technically false), while maintaining Reject because the major weaknesses remain unfixed in the submitted paper and the limit itself (the paper's central object) is uncharacterized for general test points.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>