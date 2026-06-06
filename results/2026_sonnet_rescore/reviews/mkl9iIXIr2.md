## Summary

This paper studies Online Inventory Optimization (OIO), a variant of Online Convex Optimization (OCO) with carryover stock constraints. The authors propose a two-stage projection algorithm that connects OIO to Smoothed OCO (SOCO): a base learner proposes a decision, which is then projected onto the feasible region constrained by carryover stock. This reduction, formalized in Lemma 1, shows that carryover constraints translate into a switching cost proportional to the cycle length $L_{\max}$. The paper achieves: (1) the first dynamic regret bound for OIO of $\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})$, (2) an improved static regret bound of $\tilde{\mathcal{O}}(\sqrt{L_{\max}T})$ (a $\sqrt{L_{\max}}$ improvement over prior work), and (3) a matching lower bound $\Omega(\sqrt{L_{\max}T})$, resolving an open question from Hihat et al. (2023).

---

## Strengths

- **First dynamic regret guarantee for OIO.** Table 1 confirms no prior work provided a dynamic regret bound in the OIO setting. Theorem 4 (via Algorithm 5/SOGD) achieves $\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})$ without knowing $P_T$ or $L_{\max}$ a priori, which is a meaningful theoretical advance.

- **Novel OIO–SOCO reduction via Lemma 1.** The key insight—that the carryover constraint translates, under the two-stage projection, into a switching cost $2G(\max_i L_t^i)\|\hat{y}_t - \hat{y}_{t+1}\|_1$ (Eq. 7–8)—is elegant and circumvents the fundamental difficulty that prevented naive application of meta-algorithms to OIO. Remark 4 clearly articulates this connection.

- **Improved static regret with matching lower bound.** The static regret improves from $\mathcal{O}(L_{\max}\sqrt{T})$ (all prior work in Table 1 except [4]) to $\mathcal{O}(\sqrt{L_{\max}T})$, a factor of $\sqrt{L_{\max}}$. Theorem 5 proves $\Omega(GD\sqrt{L_{\max}T})$ as a lower bound, making this bound tight and resolving the open question of Hihat et al. (2023).

- **Parameter-free doubling trick.** Theorem 2 formalizes that the doubling trick for unknown $L_{\max}$ incurs only $\mathcal{O}(L_{\max}\log L_{\max})$ overhead, which is dominated by the leading term for any broad regime of $T$. The analysis is careful and self-contained.

---

## Weaknesses

### Fatal
None.

### Major

- **Dynamic near-optimality is informal, not a formal result.** The paper calls the dynamic regret $\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})$ "near-optimal," but Theorem 5 proves only a *static* lower bound: $\Omega(GD\sqrt{L_{\max}T})$ (i.e., for $P_T = 0$, fixed comparator $u$). The $P_T$-dependent factor is accounted for by citing Zhang et al. (2018b)'s $\Omega(\sqrt{(1+P_T)T})$ bound for standard OCO—a different problem without carryover constraints. A unified lower bound $\Omega(\sqrt{L_{\max}(1+P_T)T})$ for OIO *dynamic* regret is never proven as a formal theorem. Section 5 states: "In OCO, Zhang et al. (2018b) have established the $\Omega(\sqrt{(1+P_T)T})$ lower bound. Our regret upper bound matches this lower bound up to a logarithmic factor. On the other hand, we also have a $\sqrt{L_{\max}}$ factor in our bound. The following theorem ensures this optimality." But "the following theorem" (Theorem 5) is strictly static; the two bounds are combined informally. The claim of near-optimal *dynamic* regret for OIO is thus an inference, not a proof, and should be presented as such.

### Minor

- **Static regret improvement is not uniform over all prior work.** The abstract and Section 1.1 assert an improvement of "$\sqrt{L_{\max}}$ over existing works." However, reference [4] (Agrawal & Jia, 2022) achieves $\tilde{\mathcal{O}}(\sqrt{T} + L_{\max})$ (Table 1, row 4), which is strictly better than $\mathcal{O}(\sqrt{L_{\max}T})$ when $L_{\max} = o(\sqrt{T})$. (For example, with $L_{\max} = T^{1/3}$, [4] gives $\approx \sqrt{T}$ while this work gives $T^{2/3}$.) The settings differ (lead time, single-item vs. multi-item, linear vs. interval capacity), and no explicit claim of dominance over [4] is made in the table, but the sweeping language of "improvement over existing works" should be qualified to exclude [4].

- **Restriction to linear capacity constraints limits direct comparison with Hihat et al. (2023).** The paper's baseline Hihat et al. (2023) handles general convex capacity constraints $\mathcal{C}$, while this work restricts to the linear-sum constraint (Eq. 3). The conclusions acknowledge: "This assumption is critical to the proof of Lemmas 5 and 6." As a result, the improved static regret bound $\tilde{\mathcal{O}}(\sqrt{L_{\max}T})$ is not demonstrated to hold for the more general convex setting that [7] operates in. The abstract's framing could mislead readers into thinking this subsumes [7]'s setting.

### Trivial
None.

---

## Nice-to-Haves

- **A proof sketch of Lemma 1 in the main text.** Lemma 1 is the technical heart of the paper: the bound in Eq. (7) that converts projection error into switching cost is load-bearing for every subsequent result. Currently the proof is fully deferred to the appendix. A few lines explaining *why* the projection cost is bounded by cycle-length × switching cost would help readers appreciate and trust the core insight without reading the appendix.

- **Clarification of the dynamic regret lower bound gap.** The "Strengthening" observation from the harsh critic is apt: proving a formal $\Omega(\sqrt{L_{\max}(1+P_T)T})$ lower bound for OIO dynamic regret—possibly by extending the Theorem 5 construction to the path-length-parameterized regime—would make the near-optimality claim unconditional. The paper could explicitly acknowledge this as an open problem.

- **Brief numerical illustration.** A simple experiment (e.g., regret vs. $T$ on a non-stationary demand sequence) would make the $\sqrt{L_{\max}}$ improvement tangible without requiring a full empirical study, especially for an ICLR audience.

- **Statement of probabilistic $L_{\max}$ result in the main text.** Remark 3 mentions the probabilistic extension (covering i.i.d. demand, a standard benchmark) but defers all content to the appendix. Given that i.i.d. demand is the standard inventory management baseline, even a one-sentence quantitative statement in the main text would improve accessibility.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The proof of Lemma 1 cannot be verified from the main text alone" (Harsh Critic):** Removed per hard rule — criticisms about absent appendix content are inadmissible since the parser strips all appendices from every paper. The appendix exists.

- **"Missing related works" (Harsh Critic, implicitly):** No related-work gaps were specifically flagged, but any such criticism would be removed per hard rule since external sources cannot be confirmed.

- **"No empirical content makes it unsuitable for ICLR" (Harsh Critic):** Demoted to Nice-to-Have rather than a weakness. The paper is a clean theory paper and is evaluated on those terms. Lack of experiments is a stylistic choice that fits the theory tradition; it does not invalidate any claim. The argument that "ICLR papers without empirical validation typically face harder scrutiny" is venue-meta-reasoning, not a scientific flaw.

- **"Computational complexity discussion for multi-item projection is missing" (Harsh Critic):** The paper mentions $\mathcal{O}(KT) = \mathcal{O}(T\log T)$ cost in Section 4.3 and addresses projection implicitly. The omission of the specific $O(N\log N)$ projection complexity is a trivial implementation detail, not a scientific flaw; removed per hard-rule on nitpicks.

- **Corollary 1 directional argument concern (Harsh Critic):** After careful re-reading, the logic in Corollary 1 is sound as stated: since OIO can be reduced to SOCO (upper bound), any improvement in SOCO would translate to an OIO improvement, contradicting Theorem 5. This is a valid contrapositive. The concern is not a genuine flaw and is removed.

---

## Novel Insights

The most genuinely novel technical observation is the cycle-based analysis in Lemma 1, which reveals that carryover constraints in OIO are structurally equivalent to a time-varying switching cost for the base learner: $2G(\max_i L_t^i)\|\hat{y}_t - \hat{y}_{t+1}\|_1$. This is not merely a reformulation—it eliminates the fundamental obstruction to applying two-layer meta-algorithms to OIO, since the carryover constraint on $y_t$ becomes invisible to the base learner's trajectory $\hat{y}_t$. The resulting bidirectional connection between OIO and SOCO (Remark 4, Corollary 1) is an elegant structural result: OIO regret bounds imply SOCO lower bounds and vice versa, yielding the $\Omega(\sqrt{LT})$ SOCO lower bound as a byproduct of an inventory optimization argument.

---

## Suggestions

1. **Prove or formally conjecture the combined OIO dynamic regret lower bound $\Omega(\sqrt{L_{\max}(1+P_T)T})$**, or explicitly downgrade the claim from "near-optimal dynamic regret" to "near-optimal up to the $P_T$ factor, under OCO lower bounds" in the abstract and conclusions.
2. **Qualify Table 1's implicit ordering** by noting that Agrawal & Jia (2022) achieves a better bound when $L_{\max} = o(\sqrt{T})$, and restrict the "uniform improvement" claim to the $\mathcal{O}(L_{\max}\sqrt{T})$ prior art.
3. **Add a brief proof sketch of Lemma 1** in the main text—even 3-4 lines—since this is the central technical lemma and is currently a black box.
4. **Discuss whether the linear constraint restriction affects the static regret comparison with [7]** more explicitly, so readers understand the precise scope of improvement over Hihat et al. (2023).

---

## Assessment

**Originality:** High — the OIO–SOCO reduction and the cycle-based projection analysis are technically novel; the dynamic regret guarantee for OIO is the first such result.

**Importance:** Medium-high — inventory management is practically relevant and dynamic regret is the right theoretical notion; the $\sqrt{L_{\max}}$ lower bound resolves an open question.

**Claims supported:** Mostly — the static lower/upper bound matching is rigorous; the dynamic near-optimality claim is partially informal (combining two separate lower bounds from different settings).

**Soundness:** High for what is proven; the techniques are clean and the proofs appear correct on their face.

**Clarity:** Good — the problem is well-motivated, Table 1 is informative, and the two-stage projection strategy is clearly described; the informal dynamic lower bound claim is the main presentation gap.

**Community value:** Solid for the theory/OCO community and operations research; somewhat specialized for a general ML audience.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>