Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper studies safe linear bandits with instantaneous hard constraints in non-convex and discrete feature spaces. It proposes NCS-LUCB, an algorithm with a novel reward-shaping bonus term designed to overcome the "non-convexity bias" that causes prior star-convex methods to incur linear regret. Under a Local Point Assumption (Assumption 3), the paper proves a high-probability regret upper bound of $\tilde{\mathcal{O}}(d(1+\frac{\tau}{\epsilon\iota})\sqrt{T})$, provides an information-theoretic lower bound of $\Omega(\max\{d\sqrt{T}, \frac{1}{\epsilon\iota^2}\})$, and validates the method empirically on a discrete non-convex action set where the prior LC-LUCB algorithm fails.

## Strengths

- **First algorithm for safe linear bandits under non-convex/discrete feature spaces.** The paper addresses an open challenge identified by the authors — prior work (Amani et al., 2019; Pacchiano et al., 2024) assumed convexity or star-convexity. NCS-LUCB is the first method that provably achieves sublinear regret under only local assumptions (Assumption 3), which is genuinely weaker than global star-convexity.

- **Novel bonus that provably overcomes non-convexity bias.** The bonus $g_t^\nu(a)$ (Eq. 4) is designed to be sufficiently optimistic to restore the optimism property in non-convex spaces (Lemma 2) while still decaying fast enough to avoid linear regret (Lemma 4). The toy example (Section 5.2) concretely illustrates why the star-convex bonus fails and how the proposed correction works.

- **Near-matching upper and lower bounds.** Theorem 1 gives $\tilde{\mathcal{O}}(d(1+\frac{\tau}{\epsilon\iota})\sqrt{T})$ regret, and Theorem 2 gives $\Omega(\max\{d\sqrt{T}, \frac{1}{\epsilon\iota^2}\})$. Remark 3 shows only a $1/\sqrt{\epsilon}$ gap between the two at $T = \lceil 1/(\epsilon\iota^2)\rceil$, demonstrating that the dependence on the local parameters $\epsilon$ and $\iota$ is largely unavoidable.

- **Empirical validation.** The numerical experiment (Section 6) on a discrete action set confirms that NCS-LUCB achieves sublinear regret while LC-LUCB (Pacchiano et al., 2024) incurs linear regret, consistent with the theoretical claims.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The lower bound's $\epsilon/\iota$ term is constant in $T$, weakening the claimed necessity argument.** Theorem 2 gives $\Omega(\max\{d\sqrt{T},\ \frac{1-2\epsilon}{\epsilon}(\frac{1-\iota}{\iota})^2\})$. The second term does not scale with $T$ — it is a fixed penalty. The paper argues this "highlights the necessity of $\epsilon$ and $\iota$ in the upper bound," and the lower bound does indeed depend on $\epsilon$ and $\iota$. However, because the term is constant while the upper bound's dependence on $\epsilon$ and $\iota$ is multiplied by $\sqrt{T}$ (sublinear), the lower bound does not force the sublinear regret to involve $\epsilon$ or $\iota$ in the way the upper bound predicts. The comparison at a single ad-hoc point $T = \lceil 1/(\epsilon\iota^2)\rceil$ in Remark 3 does not substitute for a lower bound whose $\epsilon/\iota$ penalty scales with $T$. This weakens the paper's claim that the lower bound "verifies the role of $\iota$ and $\epsilon$ in the upper bound," though the claim of necessity (these parameters fundamentally affect problem difficulty) is still valid.

- **Limited discussion of when discrete action sets satisfy Assumption 3.** The paper claims that the method "handles discrete action spaces while maintaining a comparable regret bound" and provides a working discrete experiment (Section 6). However, Assumption 3 requires that for every feature vector $x \in \mathcal{F}$, there exists a point $\alpha x/\|x\| \in \mathcal{F}$ with $\alpha \in [\epsilon, \tau/\sqrt{d}]$. For a general finite discrete set, this is a restrictive condition — most discrete sets will not have points on every ray at the required norms. The paper does not characterize which discrete sets satisfy the assumption, nor does it discuss constructions or transformations that would broaden applicability. The claim about handling discrete spaces is supported by one specific example but not by a general argument.

- **The parameter $\iota$ is effectively assumed known.** Theorem 1 sets $\nu = (\tau+\iota)/\iota$, which depends on $\iota$. The paper mentions the Bandits-over-Bandits approach for adapting to unknown $\iota$ but leaves it to future work. This limits the practical applicability of the current analysis to settings where a meaningful lower bound on $\iota$ is available.

- **The $\epsilon$-part of Assumption 3 is described as "local" but quantifies globally over all $x \in \mathcal{F}$.** The condition requires, for every $x \in \mathcal{F}$, a scaled point $\alpha x/\|x\|$ near the origin. While the *points required* are local (near the origin), the *quantification* is over all feature vectors. This does not invalidate the assumption or its usefulness — and the condition is indeed much weaker than star-convexity — but the repeated description as "local assumptions around the starting point" slightly oversimplifies the condition's scope. The paper would benefit from clarifying that the $\epsilon$-condition is an angular-coverage condition at the origin applying to all directions present in $\mathcal{F}$.

### Trivial
None.

## Nice-to-Haves

- A more intuitive explanation of why the modified bonus $g_t^\nu$ prevents the agent from getting stuck on suboptimal rays in general non-convex sets (beyond the specific toy example). Lemma 4 bounds the bonus's contribution, but a high-level narrative (e.g., "the bonus decays as the agent gathers information along each direction, and the $\iota$-condition ensures the optimal direction is eventually explored") would aid readability.
- A brief sketch of the lower bound construction in the main text, explaining how the constant penalty $\frac{1}{\epsilon\iota^2}$ arises.
- Discussion of the regime where $\tau$ is very small. The paper's Assumption 3 requires $\epsilon < \tau/\sqrt{d}$, bounding $\tau$ away from $0$ relative to $\epsilon$, but a comment on this interplay would be helpful.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Incomplete statement of Assumption 3 (ι-condition missing)"** — The parsed text cuts off after "either of the following conditions holds." This is a parser artifact; the original PDF contained the complete assumption, as evidenced by the paper's consistent use of $\iota$ in all subsequent theorems, lemmas, and discussion. Per the rules, formatting artifacts from parsing are not author errors.
- **"Toy example does not prove the general case"** — The toy example is explicitly presented as an *illustration* of non-convexity bias, not as a proof. The general case is proven in Lemmas 2 and 4. This criticism misunderstands the role of the example.
- **"The ε-part of Assumption 3 is actually a global condition"** — The condition requires points near the origin (bounded radius $[\epsilon, \tau/\sqrt{d}]$) for each direction present in $\mathcal{F}$. This constrains only a neighborhood of the origin, which is reasonably described as "local." The quantification over all $x \in \mathcal{F}$ makes it angularly global but spatially local; the paper's description as "local assumptions around the starting point" is substantively correct and much weaker than star-convexity.
- **"τ in the denominator could be problematic when τ is small"** — The paper's Assumption 3 already requires $\epsilon < \tau/\sqrt{d}$, so $\tau$ is bounded away from $0$ relative to $\epsilon$. The reviewer acknowledges this is consistent.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Clarify in Section 5.1 that the lower bound's constant $\epsilon$/$\iota$ term shows these parameters are *necessary* for problem hardness (any algorithm must incur a fixed penalty depending on them), even though the constant does not force the sublinear-regret dependence to involve them in the same way the upper bound predicts.
2. Add a brief discussion (or an explicit remark) characterizing when discrete action sets satisfy Assumption 3 — e.g., any discrete set that contains at least one point per direction at norm $\le \tau/\sqrt{d}$. Alternatively, relax the claim from "handles discrete action spaces" to "handles discrete action spaces that satisfy Assumption 3" to avoid overclaiming.
3. Clarify that the $\epsilon$-part of Assumption 3 is an angular-coverage condition around the origin applying to all directions in $\mathcal{F}$, and distinguish this from the $\iota$-condition which is a genuinely local neighborhood around $x^*$.
4. A brief intuitive paragraph in Section 4 explaining why a more optimistic bonus does not cause linear regret (connecting Lemma 4's bound to the idea that exploration along each direction eventually resolves uncertainty).

## Score and Decision

**Originality:** The paper tackles a genuinely new problem setting (non-convex/discrete feature spaces for safe linear bandits) with a novel bonus design. **Importance:** The problem is well-motivated by real-world applications where feature maps produce non-convex or discrete action sets. **Claims support:** The main theoretical claims are supported by proofs (Lemmas 2, 4, Theorem 1, Theorem 2), though the lower bound's interpretation could be clearer. **Soundness:** The proofs appear structurally sound. The experiments validate the core claim (sublinear vs. linear regret). **Clarity:** The paper is generally well-written, with clear problem setup, algorithms, and proof outline. The toy example is helpful. Some presentation details (the $\epsilon$-condition scope, discrete-set justification) could be sharpened. **Value:** The paper fills a clear gap in the safe bandit literature and provides the first near-optimal results under non-convexity.

The weaknesses are addressable and do not undermine the core contributions. I recommend acceptance with revisions to address the minor points above.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>