- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6
Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

This paper studies two-player zero-sum imperfect-information extensive-form games (IIEFGs) with linear function approximation, formulated as partially observable Markov games (POMGs) with linearly realizable rewards. The authors propose two algorithms: LSOMD (Least-Squares Online Mirror Descent) and LSFTRL (Least-Squares Follow-the-Regularized-Leader), both built on a novel least-squares loss estimator that uses composite features of infoset-action pairs to handle partial observability. The paper provides sublinear regret bounds for both algorithms that eliminate dependence on the action-space size \(A\), and also contributes the first regret lower bound \(\Omega(\sqrt{d\min(d,H)T})\) for the linear POMG setting. This constitutes the first theoretical treatment of learning IIEFGs with linear function approximation.

## Strengths

- **First provably efficient algorithms for IIEFGs with linear function approximation.** The paper substantiates this claim with two concrete algorithms (LSOMD, LSFTRL) and their regret guarantees (Theorems 3.3, 4.2, 4.4), addressing an open problem noted in the introduction (Section 1). This is a genuine theoretical advance over prior tabular-only results.

- **Novel least-squares loss estimator using composite features.** Section 3.1 introduces a composite feature vector \(\phi^{\nu^t}(x_h,a_h)\) (Eq. (4)) that makes estimation possible despite the partial observability of state-level features. Lemma 3.1 proves unbiasedness. This is the key technical innovation that enables function approximation in the POMG setting, where standard approaches (regressing rewards against unknown state features) fail.

- **Regret bounds that eliminate dependence on the action-space size \(A\).** Table 1 and Theorems 3.3, 4.2, and 4.4 show that all proposed bounds have no dependence on \(A\), compared to prior tabular results (e.g., Fiegel et al. 2023's \(\widetilde{O}(\sqrt{XAT})\)). The LSFTRL bounds (\(\widetilde{O}(\sqrt{H^2 d\lambda T})\) and \(\widetilde{O}(\sqrt{H X d T})\)) also eliminate the \(X\) dependence in the first bound.

- **Regret lower bound for linear POMGs.** Theorem 4.6 provides the first lower bound \(\Omega(\sqrt{d\min(d,H)T})\) for the linear setting, helping calibrate the upper bounds and identify gaps for future improvement.

- **Technical novelty in the stability analysis of LSOMD.** Section 3.3 explains how the stability term is bounded via the log-partition function \(\log Z_1^t\), circumventing the sparsity-based arguments used in tabular OMD (Kozuno et al., 2021). This is a non-trivial adaptation because the linear loss estimator is dense, unlike tabular importance-weighted estimates.

## Weaknesses

### Fatal

None. The paper's core claims are supported and the methodology is coherent, though some assumptions are strong.

### Major

- **The offline learning setting is non-standard and requires stronger justification.** Section 2 states the max-player "has access to the feature vectors of state-action weighted by min-player's policy \(\nu^t\) ... as well as transitions before the \(t\)-th episode starts." The composite features \(\phi^{\nu^t}(x_h,a_h)\) (Eq. (4)) are defined using both the environment transitions \(p_{1:h}\) and the opponent's sequence-form policy \(\nu^t\). The paper emphasizes that it "neither require[s] the policy \(\nu^t\) to be accessible to the max-player," but the composite features are computed *from* \(\nu^t\) and provided to the max-player exogenously (described as "revealed" in Section 3.1). The paper does not specify how these features are obtained without knowledge of \(\nu^t\) or a central controller, nor does it discuss real-world scenarios where such pre-computed features would be available. This is not a contradiction—the setting is consistently defined—but it is a significant departure from standard game-theoretic learning (where the opponent is unknown and adversarial) and the paper would benefit from an explicit discussion of what the setting entails and why it is a meaningful starting point. The significance of the results is partly contingent on the plausibility of this assumption.

- **The LSOMD bound scales with \(X^2\), which may be worse than tabular results in many regimes.** Theorem 3.3 gives \(\widetilde{O}(\sqrt{(d+1/\rho) H T X^2})\). When \(X^2 \gg XA\) (which is often the case since \(X\) is typically much larger than \(A\) in large games), this bound is weaker than the minimax optimal tabular bound \(\widetilde{O}(\sqrt{X A T})\) of Fiegel et al. (2023). The paper acknowledges this gap (Remark 3.4), but the \(X^2\) term is so large that it undermines the practical motivation of function approximation overcoming the curse of dimensionality. The LSOMD result is more of a proof-of-concept that learning is possible than a practically meaningful improvement.

- **The LSFTRL bound depends on \(\lambda\), a quantity that can be as large as \(X\) and may not be verifiable a priori.** Assumption 4.1 requires \(p_{1:h}^{\nu^t}(x_1)/p_{1:h}^\star(x_2) \leq \lambda\) for all infosets. The paper notes that \(\lambda\) can be as large as \(X\), in which case the \(\widetilde{O}(\sqrt{H^2 d \lambda T})\) bound becomes vacuous compared to tabular results. The alternative bound \(\widetilde{O}(\sqrt{H X d T})\) from Theorem 4.4 addresses this but still has a \(\sqrt{X}\) dependence. The paper does not provide sufficient characterization of when \(\lambda\) is small enough for the first bound to be meaningful.

### Minor

- **All regret guarantees hold only in expectation, not with high probability.** The paper explicitly acknowledges this (Remark 3.4) and sketches a potential path to high-probability results. However, for the stated goal of finding an \(\varepsilon\)-Nash equilibrium, expectation guarantees are typically insufficient without further conversion. This is a known limitation that the authors candidly discuss, but it does weaken the practical relevance of the results.

- **Lack of discussion of computational tractability.** Algorithms 1 (LSOMD) computes the covariance matrix \(Q_{\mu^t,h}\) as a sum over all \((x_h, a_h) \in \mathcal{X}_h \times \mathcal{A}\), which requires \(O(XA)\) operations per episode. Similarly, the composite features \(\phi^{\nu^t}\) must be computed over all infoset-action pairs. The paper does not address whether these operations are tractable or whether sparsity assumptions could reduce the cost. While theoretical sample-complexity papers often abstract away computation, the large \(X\) and \(A\) that motivated function approximation in the first place would make these steps impractical.

- **The "balanced transition" \(p^\star\) in LSFTRL (Eq. (9)) is defined abstractly without a concrete construction.** The maximin solution over valid transitions is introduced as a key algorithmic ingredient, but no example or efficient algorithm for computing it is given. A concrete illustration (e.g., a small game tree) would improve clarity and help assess feasibility.

- **Inconsistency in describing whether transitions are known.** The abstract says "known transition," the introduction (Section 1, line 18) says "unknown transition and unknown rewards," and the conclusion (Section 5) says "unknown transitions." Section 2 clarifies that the offline setting provides access to transitions, so the description in the introduction is somewhat misleading. This is a presentational inconsistency that should be harmonized.

### Trivial

None.

## Nice-to-Haves

- A dedicated Limitations section acknowledging the strong informational assumptions (exogenous composite features, known transitions in the offline setting) and the gap to the lower bound would strengthen the paper's framing.
- A concrete example of how \(p^\star\) could be computed in a small game would help illustrate the LSFTRL algorithm.
- A simple corollary or numerical example showing a regime where the new bounds improve over tabular results (e.g., when \(d \ll X\) and \(A\) is large) would make the contribution more tangible.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The setting is contradictory"** (Harsh Critic): The critic claims the paper's description is contradictory because the max-player "has access" to features weighted by \(\nu^t\) but the policy \(\nu^t\) is "not accessible." **Removed** — there is no contradiction. The paper states that composite features (which depend on \(\nu^t\) and transitions) are *revealed* to the max-player pre-computed. The max-player does not need to extract \(\nu^t\) from them. The setting is unusual but internally consistent. The criticism is downgraded to a Major weakness about strength of assumptions, not a logical contradiction.

- **"Assumption 3.2 is non-trivial and may not hold"** (Harsh Critic): The critic questions whether the uniform policy \(\pi\) can guarantee \(\lambda_{\min}(Q_{\pi,h}) \geq \rho > 0\). **Removed** — this is a carefully stated technical assumption, standard in linear bandits and RL. Every theoretical paper in this area makes exploration assumptions. Questioning it without evidence of infeasibility is not a valid weakness.

- **"The LSOMD computation defeats the purpose of function approximation"** (Harsh Critic, framed as a fatal flaw): The critic states that computing \(Q_{\mu^t,h}\) over all \((x_h,a_h)\) requires \(O(XA)\) complexity, "which defeats the purpose of function approximation." **Downgraded to Minor.** The criticism is factually correct about the \(O(XA)\) computation, but the paper is a theoretical sample-complexity work, and many foundational papers in linear RL similarly assume access to full feature matrices. The point is kept in Minor but as a discussion point, not a fatal flaw.

- **"The paper should include a sketch of how expectation regret could be converted to high-probability"** (Harsh Critic): The paper already discusses this in Remark 3.4, citing a possible extension using self-concordant barriers (Lee et al., 2020). This is a standard deferred-future-work statement. **Removed** from weaknesses; moved to Nice-to-Haves.

- **"Missing related works"** (Harsh Critic, implied): **Removed per hard rules** — I do not have external sources to confirm missing related works.

- **Strength Finder: generic strengths** ("this paper addressed an important problem" type): The Strength Finder's output was already concrete and specific. All listed strengths are grounded in specific sections of the paper. No removals needed from strengths.

## Novel Insights

The most valuable insight from the cross-review is that the paper's main limitation is **not** a technical flaw in the algorithms or proofs, but rather a conceptual ambiguity about the learning protocol. The harsh critic correctly identifies that the "offline setting" with revealed composite features is a strong modeling assumption that changes the nature of the problem — but incorrectly frames this as a contradiction. The resolution is that the paper presents a *feasibility result* (the problem is learnable with function approximation under certain informational assumptions) rather than a practical algorithm for standard online gameplay. The important gap between the setting studied here and the standard game-theoretic learning setting (where opponents are unknown and policies are not externally provided) is worth explicit discussion. A genuinely novel observation that emerges from the review process is that the paper's two algorithms (LSOMD and LSFTRL) face different tradeoffs between assumptions and bound quality: LSOMD avoids the \(\lambda\) dependence and the balanced transition machinery but suffers from \(X^2\) scaling, while LSFTRL can achieve better scaling (\(X\)-free in one bound) at the cost of a more opaque parameter \(\lambda\) and a non-trivial algorithmic object \(p^\star\). This tension suggests that the "right" algorithm for linear POMGs may require further innovations.

## Suggestions

1. **Clarify the learning setting explicitly.** The paper should clearly state: "The max-player receives, before each episode \(t\), the precomputed composite features \(\{\phi^{\nu^t}(x_h,a_h)\}\) for all infoset-action pairs. These features are defined using the opponent's policy \(\nu^t\) and the environment transitions, but are provided externally; the max-player does not directly observe \(\nu^t\)." Then discuss what real-world scenarios (if any) could provide such features, or explicitly frame the work as a theoretical first step in a stylized model.

2. **Harmonize the description of transitions.** Resolve the inconsistency between abstract ("known transition"), introduction ("unknown transition"), and conclusion ("unknown transitions"). The offline setting clearly assumes transitions are available; this should be stated uniformly.

3. **Add a brief discussion of computational complexity.** At minimum, state whether computing \(Q_{\mu^t,h}\) over all \(\mathcal{X}_h \times \mathcal{A}\) is intended as a conceptual step or whether there are sparse structure assumptions that make it tractable.

4. **Provide a concrete example for the balanced transition \(p^\star\).** A small game tree (2-3 infosets) showing how Eq. (9) is solved and what values of \(\lambda\) arise would significantly improve the exposition of LSFTRL.

5. **Add a limitations paragraph.** A short section or paragraph in the conclusion acknowledging the strong informational assumptions, the gap to the lower bound, and the expectation-only nature of the guarantees would make the paper more self-aware and harder to misinterpret.
