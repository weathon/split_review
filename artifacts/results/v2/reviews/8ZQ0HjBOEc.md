Now I have sufficient calibration context. Let me write the consolidated review.

## Summary

This paper studies the behavior of the deterministic NTK of infinitely wide ReLU networks as depth grows. Theorem 2 proves that the normalized kernel $\bar\Theta_\infty^{(L)}$ converges to the all-ones matrix. Theorem 3, the main result, claims that despite this singularity, the predictor expression $\tilde\Theta_\infty^{(L)}(x^\top X)^\top(\tilde\Theta_\infty^{(L)}(XX^\top))^{-1}$ converges to a well-defined bounded limit. Experiments in Section 6 show empirical convergence of several kernel quantities.

---

## Strengths

1. **Theorem 2 (convergence of normalized kernel to 1) is a clear, well-stated result.** The paper proves that $\bar\Theta_\infty^{(L)}(x,x')$ strictly increases to 1 as $L\to\infty$ for data on the sphere, and Proposition 4 provides an explicit recurrence that makes the mechanism transparent. This is a concrete contribution to understanding depth in the NTK regime.

2. **Experiments visualize the convergence of the predictor expression.** Figure 1 directly plots $\bar{\kappa}^{(l)}(x^\top X^\top)(\bar{\kappa}^{(l)}(XX^\top))^{-1}$ (the quantity Theorem 3 analyzes) for three different kernel choices ($\Theta_\infty$, $\rho$, $\eta$) and shows stabilization within $L\approx10$–$30$. The experiments also extend to MNIST (Appendix F). This provides empirical evidence that the limiting behavior described in Theorem 3 occurs at accessible depths.

3. **Identification of generalizable sufficient conditions.** Section 6 lists three abstract properties (diagonal dominance, eventual positive definiteness, determinant → 0) that a kernel sequence must satisfy for the same limiting analysis to apply. This abstraction allows the results to be transferred to other architectures or activation functions.

---

## Weaknesses

### Major

1. **The proof of Theorem 3 (the paper's central claim) is insufficient and relies on an unverified technical claim.**  
   The proof sketch in the main text (~20 lines) attempts to show convergence of the predictor via rough-path theory. The argument depends critically on **Proposition 5(4)**, which asserts that for the sigmoidal interpolation function  
   \[
   \psi_d(z)=\frac{1}{1+\exp\!\bigl(\frac{-2z}{d(1-z^2)}\bigr)},
   \]  
   all derivatives vanish as $d\to0^+$:  
   \[
   \lim_{d\to0^+}\frac{d^k}{dz^k}\psi_d(z)=0\quad\forall k.
   \]  
   This is **false at $z=0$** for $k\ge1$: a direct calculation gives $\psi_d'(0)=1/(2d)$, which diverges as $d\to0^+$ rather than going to zero. Since the proof uses this property to conclude that the driving terms $v_{i,j}^{(L)}$ converge to zero, the argument cannot be accepted as written.  

   Beyond this, the chain of determinant inequalities bounding the Cramér's rule expression is opaque; the dependence of $\mathcal{D}$ on both $L$ and $t$ is not resolved; and the application of the Lyons Universal Limit Theorem is asserted without checking the required technical conditions (e.g., convergence in $p$-variation, properties of the rough path lift).  

   Because Theorem 3 is the paper's core claimed contribution, an unsubstantiated proof is a structural weakness. The paper does not meet the standard for a theoretical result at this venue.

2. **The notation $\tilde\Theta_\infty^{(L)}$ is never defined.**  
   The paper carefully defines $\Theta_\infty^{(L)}$ (the original kernel) and $\bar\Theta_\infty^{(L)}$ (its normalized version, Definition 4). Theorem 3 and its proof then introduce $\tilde\Theta_\infty^{(L)}$ without any definition or explanation of how it relates to the other two. The discussion after the theorem and the experiment section (Figure 1) use $\bar\kappa$ in analogous expressions, but it is never clarified whether $\tilde\Theta=\bar\Theta$ or whether a different normalization is intended. This ambiguity makes the main result impossible to parse precisely.

### Minor

3. **No connection to actual network training.**  
   The experiments show that the kernel expression $\bar\kappa^{(l)}(x^\top X^\top)(\bar\kappa^{(l)}(XX^\top))^{-1}$ stabilizes with depth, but the paper never compares this limiting value to the output of a finite-width network trained with gradient descent, nor to the predictions of the standard (finite-depth) NTK formula of Proposition 3. Without this connection, it is unclear whether the proved limit governs the behavior of actual neural networks or is only an algebraic property of the kernel recursion.

4. **Convergence metric for Theorem 3 is unspecified.**  
   The theorem states that the predictor converges, but does not specify the norm or topology (pointwise? Euclidean? uniform in $x$?). This makes the claim difficult to evaluate quantitatively.

5. **Heavy RDE machinery is under-explained in the main text.**  
   The proof invokes Lyons' Universal Limit Theorem, rough path lifts, $p$-variation metrics, and the Itô–Lyons map, but none of these are defined or motivated in the main text (the appendix containing the background is stripped). For a paper whose central result depends on this machinery, the main text should give the reader enough to assess whether the argument is structurally sound.

### Trivial

6. Minor inconsistencies: the notation $\leftarrow_{i,j}$ in the proof is used where only $\leftrightarrow_{i,j}$ was defined; the variable $j$ in Proposition 5(4) appears in the quantifier but not in the expression (likely a typo).

---

## Nice-to-Haves

- **Characterize the limit more explicitly.** Currently Theorem 3 only proves boundedness and continuity of the limit. An implicit characterization (e.g., as solution of an integral equation) would substantially strengthen the contribution.
- **For the $\psi_d$ function, consider an alternative interpolation** (e.g., linear interpolation with a subsequent limit) that avoids the derivative blow-up at $z=0$, or provide a rigorous analysis of the product $\psi_D'\times(\tilde\Theta^{(L+1)}-\tilde\Theta^{(L)})$ as $L\to\infty$.
- **Clarify whether $\tilde\Theta=\bar\Theta$** and adjust notation throughout to be consistent.
- **Verify empirically that the claimed limiting predictor matches the output of a wide-but-finite network** trained with gradient descent on a small synthetic dataset, which would directly validate the practical relevance of Theorem 3.

---

## Removed Points

These points were raised by reviewers but are removed from the main weakness list with justification:

- **"They never compute $\tilde\Theta_\infty^{(L)}(x^\top X)^\top(\tilde\Theta_\infty^{(L)}(XX^\top))^{-1}$ and plot its value."** – This is factually incorrect. Figure 1, third column, plots exactly this expression for three different kernels. REMOVED.
- **"Proposition 4 uses $h'$ but $h'$ is not explicit."** – $h(z)=\frac{z\arcsin z}{\pi}+\frac{\sqrt{1-z^2}}{\pi}+\frac{z}{2}$ is a standard function from the NTK literature; its derivative $h'(z)=\frac{\arcsin z}{\pi}+\frac12$ is a standard computation. A minor presentation issue at most. REMOVED from main weaknesses.
- **"Figure 1 axes labels are garbled."** – This is a PDF-parser artifact, not an author issue. REMOVED per hard rules.
- **"Proof of Lemma 1 not in main text."** – References to the appendix for proofs are standard practice. REMOVED.
- **Missing appendix proofs, missing related works.** – The parser strips appendices; the existence of references is not to be doubted. REMOVED per hard rules.
- **Typos ("colinear"), formatting issues.** – REMOVED per hard rules (typos/formatting artifacts).
- Strengths about "explicit closed-form recursion for ReLU NTK" and "clean handling of data on the sphere" – These are standard results and preprocessing steps from the existing literature, not novel strengths of this paper. REMOVED.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear tension: the paper asks a timely and interesting question, but the attempted mathematical argument for its central result contains a concrete flaw (the $\psi_d$ derivative claim) and the overall proof is too sketchy to be accepted as a rigorous contribution. The experimental illustration of the predictor's convergence is suggestive but disconnected from actual trained-network outputs, leaving the practical significance unverified.

---

## Suggestions

1. **Fix or replace the proof of Theorem 3.** The $\psi_d$ interpolation approach has a clear issue at $z=0$. Either provide a rigorous analysis showing that the product $\psi_D' \times (\tilde\Theta^{(L+1)}-\tilde\Theta^{(L)})$ still vanishes despite the derivative blow-up (e.g., using that the kernel difference has a zero at the relevant point), or adopt a different interpolation strategy (e.g., linear interpolation with a separate limit argument). The determinant inequality chain must be made precise.
2. **Define $\tilde\Theta_\infty^{(L)}$ explicitly** (or replace it with $\bar\Theta_\infty^{(L)}$ throughout if that is what is intended) and ensure notational consistency between Theorem 3, the proof, and the experiments.
3. **Add a small-scale experiment** comparing the limiting theoretical predictor to the actual output of a finite-width ReLU network trained with gradient descent, to demonstrate that the limit is not just an algebraic artifact of the kernel recurrence.
4. **Specify the convergence topology** in Theorem 3.
5. **Provide a standalone explanation** of why the RDE machinery is necessary and what it achieves that a more elementary interpolation argument cannot.

---

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Source | Comparison |
|------|-----------|--------|------------|
| `fUz6Qefe5z` – NTK derivative labels | 3.00 | r1-topic-low | Similar: handwavy math, core result not convincingly proved. Our paper has somewhat better presentation and partial experiments, but same structural flaw. |
| `2NwHLAffZZ` – Weak correlations linearization | 2.33 | r1-topic-low | Weaker paper; our paper has more concrete results. |
| `kkVTeMvC9D` – Training Jacobian | 3.40 | r1-topic-low | Comparable: empirical focus with limited theory. Our paper is more theoretical but less rigorous. |
| `bWz8aOPwsJ` – NTK trace evolution | 3.75 | r1-weakness | Mixed reviews (6,3,3,3); rejected for weak insights and notation issues. Our paper has a more serious flaw (proof gap). Comparable or slightly weaker. |
| `kOtFuzoA93` – Novel kernel models | 4.00 | r1-topic-mid | Dense theory, no experiments, rejected. Our paper has experiments but less rigorous theory. Comparable. |
| `YN4uWzcbtt` – Positive definiteness of NTK | 4.25 | r2 | Clear incremental result, presented well. Our paper is significantly less rigorous. Weaker. |
| `3LLkES6nNs` – Infinitely deep ResNets | 4.25 | r2 | Some novelty concerns but technically sound. Our paper has a verifiable proof gap. Weaker. |
| `VEJzjAvaIy` – NTK divergence in classification | 5.75 | r1-topic-mid | Clear well-proven result, accepted. Our paper is substantially weaker in rigor. |
| `AoraWUmpLU` – Activation functions in Neural ODEs | 8.00 | r1-topic-high | Strong paper with rigorous analysis. Our paper is far below this level. |

**Round-1 bracket:** 3.0–4.5 (topic band), narrowed to ~3.0–3.75 from weakness queries.

**Round-2 narrowing:** Compared against anchors in the 2.5–4.5 range. The NTK trace evolution paper (3.75) was rejected for weak insights and notation; our paper adds a verifiable proof gap on top of similar issues, placing it below 3.75. The positive definiteness paper (4.25) is better-rigorized. The NTK derivative labels paper (3.00) shares the same "proof not convincing" problem and is the closest comparator.

**What the low-band anchors failed at:** Papers scoring ≤3.0–3.5 in this space typically (a) have an unsubstantiated core claim, (b) use handwavy mathematics where rigorous proof is required, and (c) do not adequately connect theory to experiments. The paper under review exhibits all three failure modes: Theorem 3's proof is insufficient, the $\psi_d$ property is incorrect as stated, and there is no experimental connection to actual trained networks.

**Score:** **3.0** — The paper raises an interesting question and has partial results (Theorem 2, experimental convergence plots), but the central contribution (Theorem 3) is not convincingly established. The proof contains a concrete mathematical error and the overall argument is too sketchy to be accepted. A score of 3.0 reflects a paper with some merit that falls well short of the acceptance threshold due to an unsubstantiated main claim.

**MY FINAL SCORE:** <score>3.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>