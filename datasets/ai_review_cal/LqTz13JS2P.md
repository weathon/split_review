- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 5, 8, 8
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper provides a unified theoretical framework for repeated generalized principal-agent problems (including Bayesian persuasion, Stackelberg games, and contract design) where the agent learns via no-regret or no-swap-regret algorithms and the principal lacks commitment power. The key contributions are: (1) a reduction showing that a learning agent corresponds to an approximately-best-responding agent, with the approximation quality governed by the agent's regret; (2) tight asymptotic bounds on the principal's achievable utility — at least \(U^* - \Theta(\sqrt{\mathrm{Reg}(T)/T})\) against no-regret agents, and at most \(U^* + O(\mathrm{SReg}(T)/T)\) against no-swap-regret agents; (3) a demonstration that this asymmetry is intrinsic; and (4) applications to Bayesian persuasion, Stackelberg games, and contract design that refine and generalize prior work.

## Strengths

- **Unified framework with explicit rates.** The paper subsumes and generalizes prior results on playing against learning agents in Stackelberg games (Deng et al. 2019) and contract design (Guruganesh et al. 2024) into a single framework applicable to all generalized principal-agent problems where the agent lacks private information. The bounds are quantitative (\(O(\sqrt{\mathrm{Reg}(T)/T})\) and \(O(\mathrm{SReg}(T)/T)\)) rather than qualitative (\(o(1)\)), providing concrete rates. (Theorems 3.1, 3.2; Corollaries in Section 5.)

- **Novel proof technique for the swap-regret upper bound.** The proof of Theorem 3.2 constructs a hypothetical principal strategy over the product space \(S \times A\) by averaging over the realized distributions of signals and actions, relating the agent's contextual swap-regret to approximate best response. This construction is technically inventive and likely reusable beyond this paper. (Proof of Theorem 3.2, equations (3.1)–(3.3).)

- **Clean reduction from learning to approximate best response.** Lemma 3.1 shows that, when the principal uses a fixed strategy, the agent's time-averaged behavior is a \(\delta\)-best response with \(\delta = \mathrm{Reg}(T)/T\). This reduction is simple yet powerful — it decouples the learning dynamics from the principal-agent optimization and enables the entire analysis to proceed via the well-structured approximate-best-response problem.

- **Tightness and intrinsic asymmetry.** The paper not only provides upper and lower bounds but also demonstrates (Example 4.2, Theorem 3.3) that the \(\sqrt{\delta}\) dependence in the lower bound is unavoidable, confirming that the asymmetry between the linear upper bound and the square-root lower bound is not an artifact of the analysis. (Example 4.2, Theorem 3.3.)

- **New results for Bayesian persuasion.** As a byproduct of the general framework, the paper obtains the first quantitative bounds for Bayesian persuasion with a learning receiver, including the non-trivial result that a no-swap-regret learner caps the sender's utility at \(U^* + o(1)\) even though the sender has informational advantage and chooses signaling schemes after seeing the receiver's strategy. (Corollary 5.1.)

## Weaknesses

### Fatal
None.

### Major
None that threatens the paper's core claims. The issues below are addressable and do not undermine the main results.

### Minor

- **The mean-based example (Theorem 4/5.4) analysis is informal.** The proof sketch for the mean-based construction uses approximations (e.g., "\(\approx\)", "with high probability", heuristic counting) rather than rigorous concentration bounds. Crucially, the critic's objection that the example assumes deterministic behavior is *incorrect* — the paper's definition of \(\gamma\)-mean-based (Definition 5.3) is explicitly probabilistic (\(\Pr[a^t = a \mid s^t = s] < \gamma\)), and the footnote about deterministic algorithms appears elsewhere and refers to general no-regret learning, not to this definition. The analysis does use probabilistic reasoning. However, the analysis remains an informal sketch: it does not rigorously propagate the \(\gamma\) probability bound through the multi-phase construction, does not formalize the "with high probability" statements, and the asymmetric \(O(\sqrt{\gamma})\) vs \(O(\gamma)\) gap in the sender's utility is claimed but not tightly derived. The construction and intuition are clear, but a theorem stated in a theory paper deserves a more precise analysis. (Pages 20–21, proof of Theorem 5.4.)

- **The construction of contextual no-swap-regret algorithms is stated without a specific citation.** Proposition 3.1 claims such algorithms exist with regret \(O(|A|\sqrt{|S| T})\) under the assumed feedback, constructed by "running an ordinary no-(swap-)regret multi-armed bandit algorithm for each context independently." This is a standard construction and the claim is correct, but the paper does not cite a specific algorithm that achieves no-swap-regret under bandit feedback for a single context (the only non-trivial ingredient). A reference (e.g., the Blum & Mansour 2007 reduction from swap to external regret combined with a bandit expert algorithm) would strengthen this foundation. (Proposition 3.1, lines 175–180.)

- **Theorem 3.3 (tightness lower bound for swap-regret) has its proof deferred entirely to the appendix.** While this is standard practice for a conference paper of this length, the claim is central to the paper's tightness story. A brief proof sketch or outline of the construction in the main text would help the reader evaluate the claim without consulting the appendix. (Theorem 3.3, lines 334–336.)

### Trivial

- The paper uses forward references (e.g., from the mean-based example to Theorem 5.3, noted by the authors with a comment). These should be resolved in a camera-ready version.

## Nice-to-Haves

- The paper could note that the principal's computational problem (computing near-optimal fixed strategies) is a convex optimization problem, adding practical relevance.
- The non-matching constants in the final range \([U^* - \Theta(\sqrt{\mathrm{SReg}/T}), U^* + O(\mathrm{SReg}/T)]\) could be discussed further — the gap between the lower-order terms is noted but not explored in depth.
- The paper could explicitly note that the perturbation argument for the constrained case respects the Bayes plausibility constraint via Assumption 2 (distance from boundary), which is a well-executed technical maneuver worth highlighting.

## Removed Points

- **Criticism about algorithm existence being a "structural gap" (Harsh Critic Point 1):** Removed because the paper *does* address this: it states that such algorithms exist under bandit feedback (line 175), provides a construction (line 179), and gives explicit regret bounds (Proposition 3.1). The construction of running independent per-context no-(swap-)regret bandit algorithms is standard. The critic's claim that "obtaining no-swap-regret [under bandit feedback] is non-trivial" and that "standard reductions assume full-information feedback" is inaccurate — known constructions exist (e.g., Blum & Mansour 2007's reduction from swap to external regret combined with a bandit expert algorithm). Lack of an explicit citation is a minor presentation issue, not a structural gap.
- **Criticism about the swap-regret definition using \(S \times A \to A\) deviations being insufficiently justified:** Removed because the paper explicitly defines this as *contextual* no-swap-regret and uses it in the proof. This is a natural extension, not an oversight.
- **Criticism about the order of moves (agent moves before principal):** The paper explains this design choice (line 156), and it is central to the model. Not a weakness.
- **Generic "strengths" from the Strength Finder stating this paper "addresses an important problem" —** removed for being generic/superficial. Only concrete, evidenced strengths are retained.
- **Critic's statement that the mean-based example assumes deterministic behavior and that the analysis must handle randomness:** This misunderstands the paper — the \(\gamma\)-mean-based definition is already probabilistic, and the analysis uses probabilistic reasoning. Kept only the valid core: informality of the analysis.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's significance and on the nature of its minor weaknesses; no reviewer uncovered a hidden flaw or unrecognized strength that the paper itself does not already articulate.

## Suggestions

1. Strengthen the mean-based example proof: replace heuristic approximations with explicit probabilistic bounds derived from the \(\gamma\)-mean-based definition. Even a brief concentration argument would suffice to turn the intuitive sketch into a rigorous proof.
2. Add a citation for a no-swap-regret bandit algorithm (e.g., Blum & Mansour 2007, or a reduction from swap to external regret) to support Proposition 3.1.
3. Include a 2–3 sentence proof sketch for Theorem 3.3 in the main text, briefly describing how the "simulated" agent is constructed to be no-swap-regret by design.
4. Resolve the forward reference from the mean-based example to Theorem 5.3.
