Now I have a thorough understanding of the paper. Let me write the consolidated final review.

---

## Summary

This paper analyzes the behavior of the Neural Tangent Kernel (NTK) of infinitely wide, fully-connected ReLU networks as depth $L \to \infty$, in the regime $L \in o(\min n_l)$ (depth much slower than width). The two central results are: (1) the normalized NTK $\bar{\Theta}_\infty^{(L)}(XX^\top)$ converges to the all-ones matrix (Theorem 2), making it singular in the limit, and (2) despite this singularity, the NTK predictor ratio $\tilde{\Theta}_\infty^{(L)}(x^\top X^\top)(\tilde{\Theta}_\infty^{(L)}(XX^\top))^{-1}$ converges to a bounded, well-defined limit (Theorem 3), proved via a rough differential equations (RDE) framework. The results are empirically illustrated on synthetic and MNIST data.

---

## Strengths

- **Non-trivial limit despite kernel degeneracy (Theorem 3):** The paper's core insight is that while $\tilde{\Theta}_\infty^{(L)}(XX^\top)$ degenerates to a singular constant matrix, the ratio $\kappa_x \kappa^{-1}$ — the quantity that actually appears in the kernel predictor from Proposition 3 — remains well-defined and bounded. This is achieved by interpolating between successive depths using the smooth function $\psi_\mathcal{D}$, differentiating the linear system $Au = b$, and applying the Lyons Universal Limit Theorem. The approach correctly avoids the assumption made in Xiao et al. (2020) that the limiting kernel can be split into a constant part and an invertible data-dependent part.

- **Analysis without spectral assumptions:** As explicitly stated in the Introduction and demonstrated in Section 5, the derivation relies only on the convergence of the layer-wise correlation $\rho^{(L)} \to 1$ (Lemma 1) and the RDE machinery. Unlike Nguyen et al. (2021) and Murray et al. (2023), no assumptions on the Hermite expansion spectrum or Mercer decomposition are required, making the results applicable to a broader class of kernels.

- **Generality of proof technique (Section 6):** The paper distills three concrete, checkable criteria (diagonal dominance, eventual positive definiteness, vanishing determinant of the normalized kernel) that characterize the class of kernel sequences for which the RDE argument applies. This is verified for both the NTK and the example kernel $\eta^{(L)}$, providing a reusable blueprint.

- **Empirical verification (Figure 1):** The 3×3 grid of plots in Figure 1 cleanly illustrates that $\bar{\kappa}^{(l)}(XX^\top)$ converges slowly (sublinearly) to 1 while $\bar{\kappa}^{(l)}(x^\top X^\top)(\bar{\kappa}^{(l)}(XX^\top))^{-1}$ stabilizes rapidly — directly supporting the theoretical claims.

---

## Weaknesses

### Fatal
None.

### Major

- **Undefined notation $\tilde{\Theta}$ at the seam of the two main results:** Definition 4 and all of Section 5 up to (and including) Theorem 2 use $\bar{\Theta}_\infty^{(L)}$ for the normalized kernel. Then, Theorem 3 and its entire proof switch to $\tilde{\Theta}_\infty^{(L)}$, a symbol that appears nowhere in Section 3 (Notation) and is not assigned a definition in the visible main text. The Notation section explicitly states: "The limiting deterministic kernels are represented using $\Theta_\infty^{(L)}$, and $\bar{\Theta}_\infty^{(L)}$ for their normalized version." Figure 1, meanwhile, labels the ratio using $\bar{\kappa}$. Whether $\tilde{\Theta}$ carries a different normalization than $\bar{\Theta}$ is never stated. If they differ, Theorem 3 cannot be straightforwardly applied as the sequel to Theorem 2; if they are the same, the inconsistency should be corrected. This ambiguity occurs precisely at the boundary between the paper's two central results and undermines the clarity of the contribution.

- **The limit for $x \notin X$ is not characterized, only shown to exist:** Theorem 3 establishes that the ratio $\tilde{\Theta}_\infty^{(L)}(x^\top X^\top)(\tilde{\Theta}_\infty^{(L)}(XX^\top))^{-1}$ converges to a bounded limit satisfying $\|\cdot\|_2 \in \mathcal{O}(n)$, and that this limit equals $e_i$ when $x = x_i \in X$. For a general test point $x \notin X$, no explicit characterization is given. The abstract claims the "closed-form solution approaches a fixed limit on the sphere" — but the word "fixed" implies a characterizable limit, and the paper delivers only existence and an upper bound $C(x)\mathbf{1}_n^\top$. The single most interpretively relevant case (what does the learned function predict for new inputs as depth grows?) is left open. Stating the $e_i$ result formally as a corollary and providing at least a qualitative description of the general limit would substantially strengthen the contribution.

### Minor

- **The use of rough path machinery for $p = 1$ paths appears over-engineered:** The proof of Theorem 3 explicitly asserts that the driving paths $v_{(i,j)}$ are of bounded total variation with $p = 1$, citing Definition 11 with $p = 1$ in the appendix. For $p = 1$ (bounded variation paths), the Lyons Universal Limit Theorem degenerates to classical stability theory for ODEs with smooth, bounded-variation coefficients — a result recoverable from, e.g., the Gronwall inequality, without any rough path formalism. If $p = 1$ is correct, the rough differential equation framework is far more machinery than the proof requires. If the paths actually have $p > 1$-variation (which would justify the rough path approach), the paper should state this and verify the roughness conditions against the concrete form of $A_n^{(L+1)}(t)$ and $\psi_\mathcal{D}$. Either way, this tension should be resolved in the proof.

- **The $e_i$ special case is stated only as informal prose:** The sentence "Moreover, when evaluated at $x_i \in X$, $i \in \{1, \ldots, n\}$, the limit is $e_i$, the $i^{\text{th}}$ standard basis vector" appears after the proof of Theorem 3 without proof or formal statement. This is the most interpretively concrete special case of the theorem (the learned function interpolates the training labels in the depth limit) and deserves to be formalized as a Corollary with at least a proof sketch.

### Trivial

- **Confusing repeated phrase in conclusion:** Line in Section 7 reads: "we demonstrate empirically that, while convergence for the limiting kernel is sublinear, the convergence for the limiting kernel is experimentally fast." The phrase "limiting kernel" is used twice with distinct referents (once for $\kappa^{(L)}$ itself converging to all-ones, once for the ratio $\kappa_x \kappa^{-1}$ converging to its limit). The sentence should be rewritten for clarity.

---

## Nice-to-Haves

- **Analyze $f_0(x)$ as depth grows:** The full predictor (Proposition 3) is $f_\infty(x) = f_0(x) + \kappa_x^\top \kappa^{-1}(y^* - y_0)$. Theorem 3 characterizes only the second term. Since $f_0(x)$ is the random initialization output and also grows with $L$, a complementary analysis or brief discussion of this term's behavior in the depth limit would give a complete picture of the predictor.

- **More explicit comparison with Seleznova & Kutyniok (2022):** Both that work and Theorem 2 here show the NTK of deep ReLU networks converges to a singular matrix. The relationship between the two results (whether Theorem 2 reproves, generalizes, or is complementary to Seleznova & Kutyniok) is mentioned but not sharply delineated.

- **Quantitative convergence rate for the ratio:** Section 6 argues that convergence of $\kappa_x \kappa^{-1}$ is "fast" because $v_{(i,j)}$ vanishes faster than the determinant. Even an informal bound (e.g., exponential-in-$L$) would strengthen the practical claim.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **[Harsh Critic] Invertibility of $A_n^{(L+1)}(t)$ along the path is unverified:** The paper defines $A_n^{(L+1)}(t) = (1 - \psi_\mathcal{D}(2t-1))\tilde{\Theta}_\infty^{(L)}(XX^\top) + \psi_\mathcal{D}(2t-1)\tilde{\Theta}_\infty^{(L+1)}(XX^\top)$. This is a convex combination of two positive definite matrices (both are PD for finite $L$, as required by the paper's assumptions), and convex combinations of PD matrices are PD. Hence invertibility along the entire interpolating path follows from a well-known fact in linear algebra; the proof gap is not real. **Removed.**

- **[Harsh Critic] Abstract overclaims "closed-form limit":** The abstract says "the corresponding closed-form solution approaches a fixed limit on the sphere." The "closed-form solution" refers to Proposition 3's predictor $f_0(x) + \kappa_x^\top\kappa^{-1}(y^* - y_0)$, not the limit itself. The abstract is accurately describing that the predictor converges to a fixed limit, which is what Theorem 3 shows. This is not overclaiming. The valid concern (limit not explicitly characterized for $x \notin X$) is retained separately above. **Removed.**

- **[Harsh Critic] Case (c) confusing text about stereographic projection mapping all pairs to $x_i^\top x_j = 1$:** The text states case (c) results in $x_i^\top x_j = 1$ for all $i, j$, which would be singular. This is almost certainly a PDF parser artifact (garbled math or conditional rendering), per the instructions to treat such issues as parser errors. **Removed.**

- **[Harsh Critic] Comparison with Murray et al. (2023) and Nguyen et al. (2021) is off-target:** The critic notes these papers have different goals (generalization bounds, not depth limits) so the comparison is slightly off-target. However, the paper's comparison is limited to the claim that its results "do not require assumptions on the Hermite/Mercer spectrum" — a property that is accurate and distinguishes the technique, even if the papers' primary goals differ. This is not a weakness. **Removed.**

- **[Strength Finder, generic]:** The strength "this paper addressed an important problem" is generic and dropped per filtering rules.

---

## Novel Insights

The paper's most genuinely novel contribution is the observation that the NTK predictor ratio $\kappa_x \kappa^{-1}$ can be viewed as the solution to a smoothly-interpolated linear system, differentiated to yield an ODE/RDE, and that the convergence of the driving signal to zero implies convergence of the solution — entirely sidestepping the need to invert the degenerate limiting kernel directly. The resulting "rough path" lens for studying depth-limit behavior of kernel predictors is transferable: Section 6's three-condition criterion (positivity, eventual PD, vanishing normalized determinant) identifies a broad class of kernel sequences for which the technique applies. The specific finding that at training points the predictor ratio converges to the standard basis vector $e_i$ — i.e., the network perfectly interpolates training data in the depth limit — is a clean and interpretable consequence worth formalizing.

---

## Suggestions

1. **Unify notation:** Define $\tilde{\Theta}$ explicitly in Section 3 or Section 5, or replace all occurrences with $\bar{\Theta}$. If they carry different normalizations, state the relationship clearly before Theorem 3.
2. **State the $e_i$ result as a formal Corollary** with a brief proof sketch immediately after Theorem 3.
3. **Clarify the rough path invocation:** If $p = 1$, explain why the Lyons ULT is invoked rather than a classical ODE stability argument; if $p > 1$, verify the roughness conditions from the concrete definition of $v_{(i,j)}$.
4. **Strengthen Theorem 3's conclusion for $x \notin X$:** Provide at least a qualitative or asymptotic characterization of the limit as a function of the geometry of $x$ relative to the training set.

---

## Score and Decision

**Originality:** The RDE approach to characterizing depth-limit behavior of the NTK predictor ratio is novel. The use of $\psi_\mathcal{D}$ to construct a smooth interpolation between successive depth kernels is an interesting device. Score: 3/5.

**Importance of research question:** The role of depth in overparameterized networks is a central open question; understanding the depth limit of the NTK predictor is a meaningful and useful step. Score: 4/5.

**Claims supported by evidence:** Theorem 2 and Lemma 1 are solid. Theorem 3's proof has the rough path vs. $p=1$ tension and the undefined $\tilde{\Theta}$ notation that reduce confidence. The limit for $x \notin X$ is only existence, not explicit. Score: 2/5.

**Soundness of experiments:** The experiments in Figure 1 clearly support the stated convergence claims. Limited in scale but adequate for illustration. Score: 3/5.

**Clarity of writing:** Notation inconsistency between $\bar{\Theta}$ and $\tilde{\Theta}$ at a critical juncture, the informal prose for the $e_i$ result, and the internally inconsistent conclusion sentence are real clarity problems. Score: 2/5.

**Value to the research community:** The criterion list in Section 6 and the proof technique are genuinely transferable. Score: 3/5.

**Overall:** The paper asks a sharp question and the core idea (studying $\kappa_x\kappa^{-1}$ via smooth interpolation and RDE) is clever. However, the central theorem's proof has unresolved tension around the rough path formalism for $p=1$ paths, and the notation inconsistency at the paper's most critical juncture weakens confidence in the result's rigor. The limit for test points is characterized only existentially. These are issues a revision should address, but they do not fundamentally invalidate the contribution. This sits at borderline reject — the ideas merit further development, but the current presentation of the central theorem is below the rigor expected of a theory contribution at ICLR.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>2</clarity>
<community_value>3</community_value>
</subscores>