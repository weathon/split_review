## Summary

This paper studies how the Neural Tangent Kernel (NTK) for infinitely wide, fully-connected ReLU networks behaves as depth $L$ increases to infinity (under the constraint $L \in o(\min_l n_l)$, i.e., depth grows much slower than width). The central findings are: (1) the normalized NTK $\bar{\Theta}_\infty^{(L)}$ converges to the all-ones matrix (Theorem 2/Proposition 4); yet (2) the ratio $\tilde{\Theta}_\infty^{(L)}(x^\top X)(\tilde{\Theta}_\infty^{(L)}(XX^\top))^{-1}$ — the key term in the NTK predictor — converges to a well-defined, bounded, continuous limit on the sphere (Theorem 3). The proof of Theorem 3 is the main technical contribution, and relies on rough differential equation (RDE) machinery, specifically Lyons' Universal Limit Theorem.

---

## Strengths

- **Novel proof technique.** The application of rough path / RDE theory to analyze NTK limits appears to be new to this literature. The insight of formulating the kernel ratio as a differential equation driven by a path that vanishes in 1-variation, and then invoking the Universal Limit Theorem, is creative and may open new analytical avenues.

- **Corrects a gap in Xiao et al. (2020).** The paper correctly identifies that the proof in Xiao et al. (2020, App. D.3) requires the limiting kernel to decompose into a (possibly singular) constant matrix plus an invertible data-dependent matrix — an assumption that fails because Theorem 2 shows the entire kernel converges to the all-ones matrix. Theorem 3 handles this singular case without such a decomposition assumption.

- **Concrete interpretable limit on training data.** When evaluated at training points $x_i \in X$, the limiting weight vector is explicitly the $i$-th standard basis vector $e_i$, giving a crisp characterization of perfect interpolation in the deep limit.

- **Generalizable framework.** Section 6 distills the three properties of the kernel sequence sufficient for Theorem 3 to hold, providing a recipe for extending the results to other kernels (e.g., the $\eta^{(L)}$ example), and the proof technique is noted as adaptable to convolutional NTKs.

- **Empirical validation is consistent.** The experiments on synthetic data ($n_0 = 128$) and MNIST confirm that convergence of the kernel itself is logarithmically slow, while convergence of the ratio $\kappa_x \kappa^{-1}$ is empirically fast, supporting the practical relevance of Theorem 3.

---

## Weaknesses

### Fatal
None identified.

### Major

- **The limiting test-time predictor is not explicitly characterized.** Theorem 3 establishes existence and boundedness of the limit of $\tilde{\Theta}_\infty^{(L)}(x^\top X)(\tilde{\Theta}_\infty^{(L)}(XX^\top))^{-1}$ for arbitrary $x \in S^{n_0-1}$, but does not give a closed-form or constructive description of this limit for $x \notin X$. The abstract states that "the corresponding closed-form solution approaches a fixed limit on the sphere," but only training-point evaluation is made explicit (limit $= e_i$). The practical content of the main theorem is therefore incomplete: one knows the limit exists but not what it computes for unseen inputs.

- **Regime restriction limits breadth.** The assumption $L \in o(\min_l n_l)$ — depth vanishes relative to width — is quite restrictive. Modern practice routinely uses networks where $L$ and $n_l$ are of comparable scale. The paper contrasts this with Hanin & Nica (2020), but the gap (depth-to-width ratio $\to 0$ vs. $\to \infty$) leaves the practically important regime ($L/n_l = O(1)$) unaddressed.

### Minor

- **Key proof step needs more justification.** In the chain of inequalities following equation (5), the denominator is replaced by $\det(\tilde{\Theta}_\infty^{(L+1)})\det(\tilde{\Theta}_\infty^{(L)})$ (a product of two strictly positive quantities that approach 0). The argument invokes property (4) of $\psi_\mathcal{D}$ to bound the numerator, but the intermediate inequality — particularly why the weighted geometric mean $\det^{\psi}\det^{1-\psi}$ can be lower-bounded by the product — would benefit from a more explicit step.

- **Convergence rate of $\kappa_x \kappa^{-1}$ is empirically observed but not theoretically quantified.** Section 6 argues qualitatively that convergence is fast once the determinant is small, but no formal rate (analogous to the logarithmic rate proven for the kernel itself) is established. The claim is left as a hypothesis.

### Trivial

- Notational proliferation: three normalization conventions ($\Theta, \bar{\Theta}, \tilde{\Theta}$) are introduced; consolidating two of them would reduce cognitive load.

---

## Nice-to-Haves

- An explicit formula or integral representation for the limit of $\kappa_x \kappa^{-1}$ at test points, even for small $n$ (e.g., $n=2$), would significantly strengthen the practical message.
- A brief numerical experiment comparing predictions of the limiting predictor with those of a finite-but-deep ReLU network would connect the theory to observable network behavior.

---

## Novel Insights

The most genuinely novel observation is that the singular limit of the normalized NTK (the all-ones matrix) does not prevent the kernel-regression ratio from being well-defined: the numerator and denominator approach zero at matched rates, and the ratio is the unique constant solution to an RDE whose driving signal vanishes. This reframes the "ordered phase" degeneracy — previously treated as an obstacle — as a tractable limiting differential equation, a perspective absent from prior NTK literature. The secondary insight, that for training points the limiting weights are standard basis vectors regardless of the data distribution (perfect interpolation at infinite depth), is clean and interpretable.

---

## Suggestions

- Provide an explicit formula or bounds for the limit of $\kappa_x \kappa^{-1}$ at test points, at least for special cases (e.g., $n = 1$, or $x$ close to a training point).
- Quantify the convergence rate of the ratio $\kappa_x \kappa^{-1}$ theoretically (e.g., as a function of $\det(\bar{\kappa}^{(L)})$) to complement the empirical observation in Section 6.
- Include a brief comparison between the limiting NTK predictor and an actual trained finite network at moderate depth to assess the tightness of the approximation.
- Clarify the intermediate step in the proof of Theorem 3 where $\det(A_n^{(L+1)}(t))$ is bounded below by the geometric mean of the two endpoint determinants.

---

## Score and Decision

The paper makes a genuine theoretical contribution: applying rough path theory to prove that the NTK predictor ratio converges despite kernel singularity is novel and technically non-trivial. The result fills a real gap (the Xiao et al. (2020) ordered-phase proof breaks down in the limit they claim to analyze). However, the central theorem does not yield an explicit limiting predictor for test inputs, the applicable regime ($L \ll n_l$) is narrow, and the key proof step deserves cleaner treatment. These limitations prevent the contribution from being fully compelling. Taken together, the paper is a borderline contribution — technically sound, meaningfully novel in technique, but incomplete in its characterization of the quantity it set out to analyze.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>