## Summary

This paper introduces **Accelerated GRAAL**, a first-order convex optimization method that simultaneously achieves Nesterov-style acceleration and genuine local curvature adaptation. The key technical contribution is an "additional coupling step" that resolves a circular dependency between adaptive stepsize computation and momentum parameter selection—enabling geometric stepsize growth (unlike AC-FGM or AdaNAG). The algorithm provably achieves near-optimal $\mathcal{O}(\sqrt{L\|x_0-x^*\|^2/\epsilon} + \log(1/\eta_0 L))$ complexity for $L$-smooth functions and the first adaptive near-optimal complexity for $(L_0,L_1)$-smooth functions.

---

## Strengths

- **Resolves a meaningful open problem.** The authors clearly articulate Question 1 (can GRAAL's local curvature adaptation be combined with Nesterov acceleration?) and provide a definitive positive answer. The comparison with AC-FGM and AdaNAG is technically precise and reveals a fundamental deficiency: both prior methods' sublinear stepsize growth makes them unable to handle exponentially-varying local curvature.

- **The "additional coupling step" is a genuine technical innovation.** Rather than fixing $\alpha_k \propto 2/(k+2)$ as in prior works, the paper introduces $\beta_k$ via eq. (16) to satisfy $\eta_k/(\alpha_k\beta_k) = H_k$. This cleanly decouples the circular dependency between $\eta_k$ and $\alpha_k$, allows adaptive (non-predefined) $\alpha_k$, and is implementable since $\alpha_k$ depends only on past quantities. This insight is nontrivial and likely reusable.

- **Geometric stepsize growth is shown to be structurally necessary for $(L_0,L_1)$-smoothness.** Lemma 6 shows $\lambda_{\min}$ can be exponentially small, so geometric growth is needed to avoid exponential factors in complexity. This explains—with proof—why AC-FGM/AdaNAG fail on this problem class and positions Algorithm 1 as the first adaptive algorithm achieving near-optimal complexity under $(L_0,L_1)$-smoothness (Table 1).

- **Complete and modular theoretical analysis.** The potential function $\Psi_k(x)$ in eq. (21) telescopes cleanly (Theorem 1), and the subsequent analysis for $L$-smooth and $(L_0,L_1)$-smooth cases builds carefully on top. Lemmas 3–8 are well-motivated and the index-set partition $\{\mathcal{T}_j(k)\}$ for the $(L_0,L_1)$-smooth case is a careful case analysis showing control over "bad" iterations.

---

## Weaknesses

### Fatal
None.

### Major

- **No numerical experiments.** The paper presents a purely theoretical contribution without a single experiment. Given that (a) GRAAL and AdGD are motivated partly by strong experimental performance, (b) the paper's abstract claims "adaptive capabilities," and (c) the algorithm has non-trivial internal structure with five sequences ($x_k, \tilde{x}_k, \hat{x}_k, \bar{x}_k, \eta_k$), empirical validation is necessary to show the method actually works in practice and outperforms GRAAL, AC-FGM, or AdaNAG on concrete problems. Without experiments, it is unclear whether the logarithmic overhead terms and the coupling step create practical overhead.

- **Worse additive constant in the $(L_0,L_1)$-smooth case.** Corollary 3 gives an additive term of $(L_1\mathcal{D})^3$, while Vankov et al. (2024) achieves $(L_1\mathcal{D})^{5/3}$ and Tyurin (2025) achieves $(L_1\mathcal{D})^2$. The paper acknowledges this but attributes it to the cost of adaptivity without providing a lower bound or impossibility argument. It is unclear whether this gap is fundamental or an artifact of the proof technique.

### Minor

- **Parameter existence but no explicit values.** Theorem 1 requires $\theta, \gamma, \nu > 0$ satisfying eq. (19), but the second condition in eq. (19) involves $\lambda_k$, an algorithm-dependent quantity. The paper states "it is easy to verify that such parameters exist" but does not exhibit a concrete valid triple, which makes practical implementation slightly opaque.

- **Implicit Bregman divergence notation.** The function $D_f(x;z) = f(x) - f(z) - \langle \nabla f(z), x-z\rangle$ is used throughout without an explicit definition in the main text, relying on reader familiarity.

### Trivial
None worth listing.

---

## Nice-to-Haves

- Including a simple experiment (e.g., minimizing a logistic regression or quadratic objective with varying smoothness) would substantially strengthen the paper.
- A discussion of the computational overhead of maintaining the five iterate sequences, especially for large-scale problems, would be practically useful.
- An explicit proof or discussion of why the $(L_1\mathcal{D})^3$ additive term is hard to improve in the adaptive setting would sharpen the paper's positioning.

---

## Novel Insights

The central novel insight is that the circular dependency between adaptive stepsizes and Nesterov momentum can be broken by introducing a second "coupling" parameter $\beta_k$ that absorbs the slack, allowing $\alpha_k$ to be set adaptively based on cumulative stepsize sums rather than a fixed schedule. This has the critical downstream benefit of enabling geometric stepsize growth, which the paper argues (via Lemma 6) is **necessary**—not merely sufficient—for handling $(L_0,L_1)$-smooth problems adaptively. This explanatory contribution (not just an algorithmic one) clarifies why all previous accelerated adaptive methods fail on this problem class and provides a blueprint for future adaptive accelerated methods beyond the gradient descent setting.

---

## Suggestions

- Provide explicit values or ranges for $(\theta, \gamma, \nu)$ satisfying eq. (19) in the main paper, or at minimum in pseudocode comments.
- Add at least a small-scale numerical experiment comparing against GRAAL, AC-FGM, and AdaNAG on an $(L_0,L_1)$-smooth problem instance to demonstrate the practical benefit of geometric stepsize adaptation.
- Discuss whether the $(L_1\mathcal{D})^3$ additive factor in Corollary 3 can be tightened to match Vankov et al. (2024) even at the cost of minor non-adaptivity, or whether there is a separation.

---

## Score and Decision

The paper resolves a natural open problem in adaptive acceleration with a clean and reusable technical mechanism. The theoretical results are rigorous and the comparisons are honest and precise. The most significant practical limitation is the complete absence of numerical experiments, which matters at ICLR. The $(L_1\mathcal{D})^3$ additive constant—worse than state-of-the-art non-adaptive methods—is also noteworthy. Nevertheless, the theoretical contribution is genuine and advances the field meaningfully.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>