Here is the finalized consolidated review.

---

## Summary

This paper studies whether batch-normalized networks can simultaneously maintain good forward signal propagation (avoiding rank collapse) and avoid gradient explosion. The authors construct an MLP with orthogonal random weight matrices and batch normalization, proving two non-asymptotic results for linear activations under the condition that batch size equals width (n=d): (1) the isometry gap decays exponentially with depth (Theorem 1), implying representations become perfectly orthogonal; (2) the expected log-gradient norm is bounded by a constant independent of depth (Theorem 2), directly contradicting prior mean-field results (Yang et al., 2019) that predicted unavoidable explosion. An empirical activation-shaping scheme is proposed for non-linear activations (tanh, sin) that shows promising but heuristic results.

---

## Strengths

1. **First non-asymptotic gradient bound for BN networks with finite width.** Theorem 2 proves that the expected log-gradient norm is bounded by \(O(d^5)\) with no depth dependence, using Weingarten calculus rather than asymptotic mean-field limits. This formally contradicts the previously held view (Yang et al., 2019, Theorem 3.9) that gradient explosion is unavoidable in batch-normalized networks. The paper explicitly contrasts with prior work (Section 3.3, proof sketch) and validates the qualitative prediction experimentally in Figure 2.

2. **Exponential orthogonalization with a precise rate.** Theorem 1 proves the isometry gap decays as \(e^{-\ell/k}\) (where \(k\) depends on width and initial isometry gap), showing representations become perfectly orthogonal in the infinite depth limit. This improves over Daneshmand et al. (2021), who only proved convergence to within an \(O(\text{width}^{-1/2})\)-ball of orthogonality. The exponential decay is validated empirically in Figure 1.

3. **Rigorous non-asymptotic theory via Weingarten calculus.** The analysis (Theorem 3, Corollary 1) uses integration over the orthogonal group to obtain precise finite-width rates, avoiding the asymptotic approximations common in mean-field studies. This is a genuine methodological contribution (Section 2).

4. **Necessary condition for explosion is precisely characterized.** The paper proves gradient explosion occurs only for degenerate (linearly dependent) inputs and empirically verifies that random batches from CIFAR10/100, MNIST, and FashionMNIST are full-rank in practice (Section 3.1). Figure 3 confirms that degenerate inputs cause explosions while non-degenerate inputs keep gradients bounded.

---

## Weaknesses

### Fatal

None.

### Major

1. **The core theory requires \(n=d\) (batch size equals width) and is structurally tied to square matrices.** The isometry gap definition (Eq. 4) uses \(\det(X^\top X)\), the Weingarten calculus analysis assumes square representation matrices, and the entire framework collapses when \(n \neq d\). The paper explicitly states this requirement (line 71: "we need two main modifications to avoid gradient explosion: (i) \(n=d\)") but does not relax it or analyze how the behavior degrades when \(n \neq d\). Since batch size is an independent hyperparameter from width in practice, this restriction severely limits the theory's direct applicability. While the paper is honest about this assumption, the practical scenarios where \(n=d\) holds are a measure-zero subset of realistic training setups.

2. **The theory is rigorously proven only for linear activations; the extension to non-linear activations is entirely heuristic.** The paper clearly states (line 37) that the limitation of the theory is that it holds for linear activations, and the activation-shaping scheme (Section 5) is presented as an empirical method. However, the scheme lacks a concrete, reproducible algorithm: the rate \(R(\ell, \alpha_\ell)\) is defined but only as "the slope of the log norm of the gradients," and the strategy is described as "ensuring faster decay than a harmonic series" without specifying the actual gain schedule \(\alpha_\ell\) as a function of layer index. The experiments only show depths up to 300 (Figure 4), while the text claims "arbitrary depths." Given that practical networks rely on non-linear activations, this gap means the paper's main theoretical contribution does not apply to the settings where deep learning is most impactful. The paper's title and framing ("Towards Training Without Depth Limits") risk overstating the scope.

### Minor

1. **The \(d^5\) bound on \(\mathbb{E}[\log\|\nabla\|]\) is numerically vacuous.** For \(d=100\) (used in the experiments), \(d^5 = 10^{10}\), so the bound allows \(\|\nabla\|\) to be as large as \(\exp(10^{10})\). While the structural claim (depth-independence) is meaningful and the experimental results show much smaller gradients, the theoretical guarantee itself provides no practically meaningful numerical constraint. This is common in theoretical work but worth noting since the paper emphasizes the bound as a formal guarantee.

2. **Limited experimental validation for the core claims.** The training experiments (Figure 5) use only CIFAR10, moderate depths (25–150), and report training accuracy without test accuracy. No comparison is made to other techniques designed to stabilize deep networks (e.g., Fixup initialization, SkipInit, or alternative normalization-free methods). The claim of "depth-independent convergence" is visually supported but not quantified. The paper is primarily theoretical, so this is not fatal, but the experiments fall short of fully establishing practical significance.

3. **The isometry gap analysis omits mean reduction from BN.** The BN operator used in the theory (Eq. 3) omits the mean reduction step present in standard batch normalization. The paper acknowledges this and claims (line 69) that it does not influence the results, citing Figure 5 (mean_reduction). While this is a reasonable simplification common in theoretical work on BN, the lack of a formal argument or accessible figure in the main text makes it hard for readers to assess whether the theory transfers to the standard BN operator.

### Trivial

- The intuitive argument in Section 3.2 connecting degenerate inputs to gradient explosion (lines 153–165) is described as "not rigorous" by the authors themselves ("While this is only an intuitive argument"), which is fine for a conceptual discussion, but the phrasing "Remarkably, we cannot empirically verify that for *all* degenerate inputs the gradient norm remains bounded" (line 165) is confusing — it seems to state the opposite of what is intended.

---

## Nice-to-Haves

- A systematic study of the \(n \neq d\) regime (e.g., measuring gradient norms and isometry gap for varying ratios of batch size to width) would help clarify how gracefully the theory degrades when this condition is violated.
- A concrete, reproducible gain schedule \(\{\alpha_\ell\}_{\ell=1}^L\) for the activation shaping scheme (e.g., a table or explicit formula) would make the empirical extension practically useful.
- Reporting test accuracy alongside training accuracy for the CIFAR10 experiments would strengthen the practical claims.

---

## Removed Points

These points were flagged by reviewers but are removed per policy:

- **"No comparison to training with Gaussian weights + BN"** — The paper *does* compare orthogonal weights to Gaussian weights with BN in Figure 2 (linear_contrast_grad). This criticism is factually wrong.
- **"The rate \(R(\ell, \alpha_\ell)\) is never formally defined"** — The paper defines it (line 243): "the slope of the log norm of the gradients \(R(\ell, \alpha_\ell)\)." Additional details are in the appendix (which the parser strips).
- **Criticisms about missing appendix content (Lemma 1 Lipschitz proof, activation shaping details, Figure 5 mean_reduction)** — The parser strips appendix sections from all papers; they exist in the original submission.
- **"The Lipschitz assumption on cross-entropy is questionable without verifying Lemma 1"** — The claim is stated and the proof is referenced in the (stripped) appendix. Standard practice for conference papers.
- **"Demanding comparison to Fixup/SkipInit"** — These are architectural solutions for different settings (networks without BN). Scope creep.
- **"The paper never addresses the n=d restriction"** — The paper explicitly addresses it on line 71. The paper doesn't *relax* it, but it does address it.

---

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation that the paper does not fully develop: the implicit orthogonality bias observed during SGD training (Figure 6) suggests that orthogonal initialization may have lasting effects on the optimization trajectory even after many steps. This observation could motivate future theoretical work on how gradient dynamics preserve or converge to orthogonality in BN networks — a mechanism that the paper observes but does not explain. This is distinct from prior work that *enforces* orthogonality constraints during training (e.g., Lezcano-Casado, 2019) and is worth flagging.

---

## Suggestions

- Add a paragraph or table discussing the \(n=d\) restriction: under what conditions might the theory partially apply when \(n \neq d\)? Even a heuristic discussion or a small experiment showing graceful degradation would substantially strengthen the paper.
- Provide the activation shaping gain schedule explicitly (e.g., \(\alpha_\ell = 1/\ell\) or similar) so that the method can be reproduced without reverse-engineering from figures.
- Tone down the "arbitrary depths" claim in the context of non-linear activations, or add experiments at depths \(\geq 500\) with shaped activations to support it.
- Add test accuracy and standard deviations for the CIFAR10 training experiments to enable quantitative comparison with future work.

---

**Originality**: High — the use of orthogonal weights to provably avoid gradient explosion in BN networks is novel and counters established mean-field results.  
**Importance of research question**: High — understanding whether and how gradient explosion can be avoided in BN networks is a fundamental question.  
**Claims support**: The theoretical claims are well-supported under stated assumptions; the practical claims for non-linear activations are heuristic and less supported.  
**Soundness of experiments**: Adequate for a theory paper, but limited in scope and lacking comparisons.  
**Clarity of writing**: Good — the paper is well-structured, and the limitations are honestly stated.  
**Value to community**: Moderate-high — the theoretical results open a new direction, but the practical gap limits immediate applicability.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>