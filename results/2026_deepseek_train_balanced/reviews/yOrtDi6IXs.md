## Summary

This paper studies safe linear bandits with instantaneous hard constraints in non-convex and discrete feature spaces. It proposes NCS-LUCB, which replaces the global star-convexity assumption of prior work (Pacchiano et al., 2024) with weaker local assumptions around the origin and the optimal point. The paper provides an upper bound of $\tilde{O}(d(1+1/(\epsilon\iota))\sqrt{T})$, a matching-style lower bound $\Omega(\max\{d\sqrt{T}, 1/(\epsilon\iota^2)\})$, and a small numerical illustration.

## Strengths

1. **Clear articulation of "non-convexity bias" with a concrete toy example (Section 5.2)**: The paper provides a fully specified 4-action example ($a_0=[0,0], a_1=[1/3,0], a_2=[0,2/3], a_3=[1,0]$, $\tau=0.95$) demonstrating how applying the star-convex bonus design (Pacchiano et al., 2024) to a non-convex action set biases the agent toward suboptimal directions and causes linear regret. This makes the core failure mode concrete and directly motivates the new bonus design.

2. **Novel bonus term $g_t^\nu(a)$ with formal optimism and regret guarantees**: The paper introduces $g_t^\nu(a) = \nu \times (1 - \frac{\tau}{\tau+2\beta_2 L \|\overline{\phi(a)}\|_{\Lambda_t^{-1}}})$ (Eq. 4). Lemma 2 proves this restores the optimism property (the optimal action's value is optimistically estimated) in non-convex spaces, and Lemma 4 bounds $\sum_t g_t^\nu(a_t) \leq \frac{2\beta_2 L\nu}{\iota\epsilon\tau}\sum_t \|\phi(a_t)\|_{\Lambda_t^{-1}}$, establishing that the bonus converges at a rate yielding sublinear regret. This two-part proof is the paper's central technical contribution.

3. **Weaker local assumptions compared to prior global assumptions**: Assumption 3 requires only that small neighborhoods around the origin (radius $\epsilon$) and around the optimal point (radius $\iota$) are contained in the feature space, strictly relaxing the global star-convexity of Pacchiano et al. (2024). Figures 3a/3b visually contrast the two assumptions, and the textual discussion (lines 80-84) clarifies this relaxation.

4. **Information-theoretic lower bound (Theorem 2)**: Proves $\Omega(\max\{d\sqrt{T}, \frac{1}{\epsilon\iota^2}\})$ for $T \geq \frac{32e}{\epsilon\iota^2}$, showing that the $\epsilon$ and $\iota$ dependence in the upper bound is inherent to the problem, not an artifact of the analysis. Remark 3 notes only a $\frac{1}{\sqrt{\epsilon}}$ gap between upper and lower bounds.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Inconsistent regret bound expressions across the paper**: The abstract states $\tilde{\mathcal{O}}(d(1+\frac{\tau}{\epsilon\iota})\sqrt{T})$, Contribution 1 states $\tilde{\mathcal{O}}(d(1+\frac{1}{\tau\epsilon\iota})\sqrt{T})$, and Theorem 1 gives $(2\beta_1 + \frac{2\beta_2 L(\tau+\iota)}{\epsilon\iota\tau})\sqrt{2T d\log(\dots)}$. While all are equivalent through $\tilde{\mathcal{O}}$ notation (constants suppressed), the specific placement of $\tau$ differs (numerator, denominator, canceled) without explanation, creating an unnecessary inconsistency in a theory paper where precision matters.

2. **Very minimal experimental validation**: The single experiment uses 5 discrete actions in $\mathbb{R}^2$ with identity mapping ($\phi(a)=a$), only one baseline (LC-LUCB), and no error bars or confidence intervals despite reporting "average regret over 10 trials." There is no use of a non-linear feature map, no higher-dimensional setting, and no continuous action space. For a theory paper a small experiment is acceptable, but this does not demonstrate effectiveness in genuinely non-convex feature spaces — the "non-convexity" here amounts to the action set being discrete rather than star-convex.

3. **Computational tractability of the maximization step left unresolved**: The paper acknowledges (Section 7, line 231) that "the maximization step in non-convex scenarios often becomes intractable in non-convex continuous cases" and defers this to future work. Since the algorithm requires solving $\arg\max_{a\in\mathcal{A}_t} \langle\phi(a),\theta_t\rangle + b_t(a)$ over a potentially non-convex set at each round, this creates a gap between the algorithm description and its practical implementability for continuous non-convex action spaces.

### Trivial

- Line 152 contains a typo: "coeffecicient" → "coefficient."
- Theorem 1 uses superscript $I$ and lowercase $l$ interchangeably to refer to "Algorithm 1" (formatting artifact).

## Nice-to-Haves

- Provide a concrete numeric calculation showing how $g_t^\nu(a_1)$ approximates the desired bonus $2/3$ in the toy example of Section 5.2, bridging the intuition and the algorithm.
- Include proof sketches for Lemma 2 and Lemma 4 in the main text to aid verification.
- Discuss how the approach handles the setting where $\iota$ is unknown more concretely (currently mentioned as Bandits-over-Bandits future work).

## Removed Points

These points were flagged by reviewers but are removed after verification:

- **"Assumption 3 is incomplete, invalidating the theoretical contribution"**: The text after "either of the following conditions holds" is missing in the extracted file — this is a PDF parser extraction failure (the original submission would contain the conditions). Per instruction, formatting artifacts from parsing are not author errors.
- **"$\iota$ is never formally defined"**: Likely the same parser artifact; the $\iota$-neighborhood condition would appear in the dropped portion of Assumption 3.
- **"Only one baseline compared, and its failure is expected"**: LC-LUCB is the most directly relevant baseline (same problem setting under star-convexity). Showing it fails in non-convex settings directly demonstrates the paper's claimed phenomenon — this is informative, not a weakness.
- **"Toy example assumes known $\theta^*$"**: This is explicitly a pedagogical illustration. The paper states Lemma 2 handles the general case. Not a weakness of the algorithm.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Reconcile the three regret bound expressions so the abstract, contribution list, and Theorem 1 state the same simplified form (e.g., consistently $\tilde{\mathcal{O}}(\frac{d}{\epsilon\iota}\sqrt{T})$ with the same $\tau$ dependence).
2. Expand the experiment to include at least one non-linear feature map or a higher-dimensional setting to demonstrate the method operates beyond a 2D discrete problem with 5 actions. Add error bars.
3. Provide a proof sketch or reference for Lemma 2 and Lemma 4 in the main text so readers can follow the argument without the appendix.
4. Either address the computational tractability of the $\arg\max$ step or more explicitly scope the paper to discrete/finite action spaces where it is tractable.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>