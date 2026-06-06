## Summary

This paper introduces *random set stability* (Assumption 3.1), a novel stability notion designed for data-dependent random sets produced by stochastic optimization algorithms. The key contribution is Lemma 3.4, which bounds the expected worst-case generalization error by a Rademacher complexity term plus a stability parameter $\beta_n$, entirely eliminating the intractable mutual-information (IT) terms present in all prior bounds of this form. Applying this framework, Theorems 4.3 and 4.4 yield the first fully computable fractal- and topological-complexity generalization bounds for practically used optimization algorithms. Experiments on ViT and GraphSAGE demonstrate non-vacuous bounds and empirically validate the predicted interplay between topological complexity and stability.

---

## Strengths

- **Novel random set stability framework closing the IT-term gap.** The paper introduces Assumption 3.1, which extends Foster et al. (2019)'s hypothesis set stability to properly account for algorithmic randomness $U$ — an explicitly identified gap in prior work. Lemma 3.2 and Corollary 3.3 show this assumption is satisfied by practical optimizers (projected SGD), giving an explicit $\beta_n = O(T^2/n)$ theoretical bound in the convex Lipschitz-smooth setting.

- **First fully computable topological generalization bounds.** Theorems 4.3 and 4.4 provide IT-free versions of the bounds from Birdal et al. (2021) and Andreeva et al. (2024), expressed in terms of box-counting dimension, $\alpha$-weighted lifetime sums, and positive magnitude — all numerically estimable quantities. This directly resolves the main obstacle that rendered previous trajectory-level bounds impractical.

- **Theoretically principled interpolation between classical bounds.** Corollaries 3.5 and 3.6 recover algorithmic stability bounds ($J=1$) and classical Rademacher complexity bounds ($J=n$, $\beta_n=0$) as special cases of Lemma 3.4, confirming the framework is consistent with and subsumes established theory.

- **Non-vacuous empirical bound evaluation.** Table 1 reports end-to-end estimated bounds for ViT and GraphSAGE; for most configurations the bounds remain below 100% error and scale predictably with $\beta_n$. This is a concrete first demonstration that trajectory-level generalization bounds can be fully evaluated numerically.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The Adam gap in theoretical grounding.** All experiments use the Adam optimizer, while the theoretical stability guarantee (Corollary 3.3) applies only to projected SGD. The paper correctly observes that empirically measured $\beta_n$ decreases with $n$ (Figure 1, Right), but the text does not clearly distinguish between: (a) Corollary 3.3 providing a theoretical bound on $\beta_n$ for projected SGD, and (b) the empirical estimation procedure in Section 5 being what actually grounds the Adam experiments. A reader applying Theorem 4.4 to Adam-trained networks must rely entirely on the empirical estimation procedure, not on any theoretical guarantee from Section 3. The paper should be explicit about this distinction.

- **Functional-form inconsistency in the correlation analysis.** Theorem 4.4 predicts $\log \mathbf{E}^1(\mathcal{W}_{S,U}) \sim \beta_n^{-1/3} G_S(\mathcal{W}_{S,U}) \approx n^{1/3} G_S(\mathcal{W}_{S,U})$, yet Figures 2 and 3 plot $\mathbf{E}^1$ (not $\log \mathbf{E}^1$) against $G_S$ and fit a linear regression line. The claim in Section 5.1 that the observed increase in slope with $n$ "strongly supports Theorem 4.4" is overstated: the experiment tests a linear relationship while the theory predicts an exponential one. The correlation is visually striking but does not cleanly validate the specific functional form the theorem asserts.

- **GraphSage correlation decay at large $n$.** Pearson correlations drop to $r = 0.37$ and $r = 0.28$ at $n = 5000$ and $n = 10000$ (Figure 3). The authors attribute this to harder convergence at large $n$, citing Birdal et al. (2021) and Andreeva et al. (2024). However, this explanation is directionally inconsistent with the theoretical prediction of Theorem 4.4 — that the coupling between topological complexity and generalization should become *tighter* as $n$ grows. This discrepancy for GraphSage deserves more systematic discussion rather than a brief speculative remark.

- **Gap between theoretical and empirical $\beta_n$ unacknowledged.** Corollary 3.3 gives $\beta_n = O(T^2/n)$ for projected SGD. Under the experimental setting ($T = 500$, $n$ in hundreds), this yields $\beta_n \sim O(10^3)$ or larger — many orders of magnitude above the empirically measured values of $\beta_n \sim 10^{-4}$ in Table 1. This enormous gap (well-known from the looseness of Hardt et al.'s bounds for neural networks) is not explicitly noted. Acknowledging it would actually strengthen the paper's case for empirical estimation: it explains *why* the empirical procedure is necessary and appropriate.

### Trivial

- The "without loss of generality, assume $\beta_n^{-2/3}$ is an integer divisor of $n$" clause in Theorems 4.3 and 4.4 is technically non-standard; WLOG is conventionally used for symmetry arguments, not integrality constraints. This should be phrased as "assuming WLOG by rounding, as detailed in Appendix B.4."

---

## Nice-to-Haves

- On the theory side: provide at least one setting (e.g., a simple convex quadratic) where both the IT-based bound from Dupuis et al. (2024) and the new bound are numerically computable simultaneously, and compare their numerical values directly. This would convert the "IT terms can be infinite, justifying our slower rate" argument from an intuitive claim into a demonstrated fact.
- On the empirical side: re-run the correlation analysis in Figures 2–3 with $(\eta, b)$ fixed and $n$ varied across seeds, so that variation is across data draws rather than hyperparameter settings. This would separate the theoretically predicted topological–generalization coupling from the well-known effect that larger learning rates increase both generalization gap and trajectory complexity.
- Include a brief sensitivity analysis: if the true $\beta_n$ is 2–5× the empirically estimated value, how do the bounds in Table 1 change? This would quantify the robustness of the "non-vacuous" claims to estimation error.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Rate comparison framing in the introduction** (Harsh Critic, "Introduction" section): The critic suggests the introduction should front-load the $n^{-1/3}$ vs. $n^{-1/2}$ rate cost. The paper does explicitly acknowledge this trade-off ("a deliberate trade-off to maintain boundedness") in Section 4, and the introduction cannot present all technical costs up front without losing accessibility. Removed as a scope-creep/presentation preference.

- **Assumption 4.1 uniformity in $z$** (Harsh Critic, Section 4): The paper already explicitly states "Note however that this local Lipschitz continuity of $\ell(\cdot,z)$ is still required to be uniform in $z \in \mathcal{Z}$." The critic calls this "underdiscussed," but it is disclosed. Removed as a strawman.

- **Table 1 "apples-to-apples" comparison caveat** (Harsh Critic, Table 1): The critic notes that prior bounds are point-at-convergence while this paper bounds trajectory worst-case, so comparisons to prior discrepancy reports are imprecise. This is true but minor and does not affect the paper's claims; removed as a nitpick.

---

## Novel Insights

The paper's most intellectually sharp contribution is not merely removing IT terms (useful but technically incremental) but the parameter $J$ in Lemma 3.4, which continuously interpolates between the single-iterate stability regime ($J=1$) and the data-independent uniform-complexity regime ($J=n$). This interpolation reveals that the classical stability–complexity trade-off is not binary but parametric, and the optimal $J = \beta_n^{-2/3}$ encodes the "right" granularity at which to apply Rademacher complexity arguments to a given trajectory. The resulting $\beta_n^{1/3}$ rate is an artifact of this optimization over $J$, not an ad hoc design choice — a connection the paper makes somewhat implicitly that deserves more prominent discussion.

---

## Suggestions

1. Add a brief paragraph at the end of Section 3.2 explicitly noting that Corollary 3.3 (projected SGD) does not directly provide a theoretical $\beta_n$ for Adam, and that for Adam the empirical estimation procedure in Section 5 is the operational basis for the bounds.
2. Replace the linear fit of $\mathbf{E}^1$ vs. $G_S$ in Figures 2–3 with a fit of $\log \mathbf{E}^1$ vs. $G_S$, which directly tests the functional form asserted by Theorem 4.4. Report both fits if desired.
3. Add explicit commentary (a single sentence in Section 5.1 or the limitations paragraph) that the Corollary 3.3 theoretical bound on $\beta_n$ is orders-of-magnitude loose compared to empirical estimates, motivating the empirical estimation approach.
4. Discuss the GraphSage large-$n$ correlation decay (Figure 3) more thoroughly, possibly investigating whether a convergence diagnostic (e.g., training loss level) predicts when the coupling breaks down.

---

## Score and Decision

**Axis evaluation:**

- **Originality:** High — random set stability is a genuinely new concept that cleanly bridges algorithmic stability and random set theory; the $J$-interpolation idea is novel.
- **Importance of research question:** High — removing intractable IT terms from trajectory-level bounds is a long-standing open problem in generalization theory.
- **Claims well-supported:** Moderate-to-high — theoretical claims are fully proved; empirical support is consistent with theory but the correlation analysis has a functional-form inconsistency that prevents it from being a clean test.
- **Soundness of experiments:** Moderate — non-vacuous bounds in Table 1 are meaningful; correlation analysis methodology has the noted inconsistency and the Adam gap concern.
- **Clarity of writing:** High — the paper is well-organized, assumptions are clearly stated, and limitations are honestly discussed.
- **Value to research community:** High — the first fully computable topological bounds for deep network training trajectories is a concrete deliverable useful to researchers studying generalization.

The theoretical contribution is sound, technically novel, and cleanly executed. The weaknesses (Adam gap in theory, correlation analysis methodology, GraphSage decay) are real but bounded and do not undermine the core claims. The paper advances the state of the art in trajectory-level generalization bounds in a meaningful way.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>