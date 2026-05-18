Now I have a thorough understanding of the paper and the reviews. Let me construct the final consolidated review, carefully filtering each criticism against the rules and verifying against the paper text.

---

## Summary

This paper introduces a novel paradigm of implicit communication through actions in MDPs, treating the environment as a finite-state channel (FSC) where the agent's actions serve as channel inputs and the states observed by a receiver serve as channel outputs. The paper makes two main contributions: (1) an information-theoretic characterization of the fundamental capacity-reward trade-off, deriving a single-letter capacity expression (Theorem 1) and formulating the trade-off as a convex optimization (Theorem 2, Lemma 1); (2) Act2Comm, a transformer-based learning framework that jointly optimizes control and communication for non-differentiable FSCs in the finite block-length regime. Experiments on two MDP environments demonstrate Act2Comm's ability to trade off communication rate against control reward.

## Strengths

- **Novel problem framing with practical motivation.** Conceptualizing the MDP environment itself as a communication channel—where actions are the input and states the output—is original and well-motivated by real-world scenarios (e.g., medical nano-robots, deep-space/subterranean operations) where dedicated communication channels are unavailable or impractical. The paper clearly distinguishes this setting from prior work on emergent communications (which assumes explicit dedicated channels) and from Sokota et al. (2022) (where the receiver observes both actions and states).

- **Single-letter capacity expression for the action-state channel (Theorem 1).** Given that "exact single-letter expressions for FSC capacity are generally unknown" (the paper notes this explicitly), deriving \(C = \max_{\pi} I(X;S^{+}|S)\) for the action-state channel (a POST channel) and showing capacity is achievable by a stationary randomized policy is a non-trivial and theoretically significant result. This provides a clean upper bound that grounds the rest of the paper's analysis.

- **Convex optimization characterization of the capacity–reward trade-off (Theorem 2, Lemma 1).** Framing the capacity-with-reward-constraint problem as a convex optimization over occupation measures is elegant and yields a tractable numerical method (gradient ascent using the closed-form gradient from Lemma 2). Lemma 1's claim that \(C(V)\) is concave implies the achievable rate-reward region is convex, a useful theoretical property.

- **Act2Comm is a practical design addressing a genuinely hard engineering challenge.** The EAS channel and quantizer are non-differentiable, preventing end-to-end gradient-based training. Act2Comm's iterative training strategy—alternating between a critic network (which learns to estimate gradients through the non-differentiable channel), encoder updates, and decoder updates—is a principled approach to this problem. The block-attention feedback coding mechanism is also thoughtfully designed.

- **Experimental demonstration of the core trade-off.** The experiments show that Act2Comm can achieve meaningful communication while incurring only modest reward degradation (e.g., in "Catch the Ball" with \(p=0\), reducing reward from 1.66 to 1.5 enables error-free communication at rate 0.2). The results across the two environments confirm the expected qualitative behavior: higher rates or lower BERs come at the cost of reward.

## Weaknesses

### Fatal
None.

### Major

- **The experimental evaluation lacks baseline comparisons, making it impossible to assess whether Act2Comm is genuinely effective.** The experiments plot achievable regions for Act2Comm alone but do not compare against even trivial alternatives such as: (a) a "split-resource" scheme that reserves some fraction of time steps for explicit communication (sending a fixed symbol) and follows the target policy otherwise; (b) a repetition code using a fixed deterministic deviation from the target policy; or (c) a random coding baseline that selects actions according to the target policy's marginal distribution independent of the message. Without any such baselines, the central practical claim—that Act2Comm "effectively balances the dual objectives of control and communication"—is unsubstantiated. The plots in Figures 3–5 could represent good performance or could represent poor performance that is still better than nothing; the reader has no reference point. Since Act2Comm is presented as the paper's practical contribution (Contribution 3), this is a decisive gap. This weakness is not addressed by the appendix.

### Minor

- **Practical implementation details are underspecified.** The paper introduces a temperature parameter \(\gamma\) for the sigmoid-based approximation of action frequencies (estimating the control loss) but does not discuss how \(\gamma\) is chosen, how sensitive the training is to this choice, or how the approximation affects gradient quality. The iterative training strategy (alternating encoder, critic, decoder) is described at a high level, but convergence behavior, the number of inner steps needed, and sensitivity to \(\sigma_w\) (noise in neighbor sampling) are not discussed. For a method whose contribution is partly practical, these details matter for reproducibility and adoption.

- **Slight overclaim about multi-agent potential.** The conclusion states "our study demonstrates the potential of communication through actions in multi-agent systems," but all experiments are single-agent (controller + external receiver). While the paper acknowledges this is "a reasonable first step," the framing inflates the contribution beyond what was actually validated. The single-agent setting is defensible as a first step, but the multi-agent claim should be tempered.

### Trivial
None.

## Nice-to-Haves
- Baseline comparisons with the simple schemes described above (split-resource, repetition coding, random coding).
- A discussion of scalability: the two MDPs have 3 and 27 states with 2–3 actions. A note on whether the transformer-based scheme can scale to larger state/action spaces would be helpful.
- Sensitivity analysis for \(\gamma\), \(\sigma_w\), and inner-step count.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that Theorem 1's claim about stationary policies achieving capacity is unsubstantiated / lacks proof.** The critic questions whether the action-state channel's capacity can be achieved by a stationary randomized policy without history dependence. While this is a strong claim, the paper references the POST channel literature (Permuter et al., 2014) and the proof is standardly deferred to the appendix (which was stripped by the parser). Per the meta-review rules, weaknesses about missing appendix proofs are removed.

- **Criticism that the concavity of \(I(w,T)\) is unsubstantiated, undermining Theorem 2.** The critic notes that the paper does not show that the tangent line \(l(w,w_n,T)\) is a global upper bound (which would prove concavity) and argues concavity of mutual information in the occupation measure is non-obvious. The paper states concavity as a claim and provides Lemma 2 (tangent line). Formal proof of concavity and the tangent line's bounding property would appear in the appendix (stripped by the parser). Per the meta-review rules, weaknesses about missing appendix proofs are removed.

- **Criticism about garbled notation in Equation (4) (conditional mutual information).** The critic notes the formula appears non-standard. This is a parser/rendering artifact, not an author error. Per the meta-review rules, formatting artifacts are removed.

- **Criticism that the paper should also cover multi-agent experiments.** This is scope creep: the paper explicitly scopes itself to single-agent with an external receiver, which is a necessary first step. The demand for full multi-agent experiments falls outside the paper's stated scope. (The minor weakness retained above about overclaiming multi-agent potential is the appropriate version.)

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that the paper itself does not already state. The harsh critic's main insights (need for baselines, underspecified implementation details) are constructive criticisms rather than novel analytical observations.

## Suggestions

1. **Add at least two baselines to the experiments.** A split-resource baseline (reserve \(x\%\) of time steps for pure communication using a predetermined signaling scheme) and a repetition-code baseline (repeat each message bit via a fixed action deviation) would provide meaningful lower bounds on performance and allow readers to evaluate whether Act2Comm's complexity is justified. Even a "no coding" baseline (always follow the target policy, decode randomly) would help anchor the plots.

2. **Provide a sketch of the proof of Theorem 1 in the main text.** A short coding-scheme description and converse argument would help readers understand *why* the action-state channel's structure permits stationary policies to achieve capacity, even if the full proof remains in the appendix. This would also address concerns about the claim's plausibility.

3. **Document the key hyperparameters** (\(\gamma\), \(\sigma_w\), inner-step count) and their sensitivity. Report the values used in experiments and, if possible, a brief ablation showing how performance varies with \(\gamma\) or \(\sigma_w\).

4. **Temper the multi-agent claims** in the conclusion, or add a single sentence clarifying that multi-agent validation is future work.

## Score and Decision

**Originality:** High — the framing of implicit communication through actions in MDPs is genuinely novel and well-distinguished from prior work on emergent communications and source-coding-based approaches.

**Importance:** Medium-High — the problem is motivated by real scenarios where explicit communication is infeasible (medical nanobots, subterranean robotics, adversarial environments). The theoretical characterization provides a fundamental limit, and the practical framework addresses a challenging non-differentiable coding problem.

**Claims supported:** Partially — the theoretical contributions appear internally consistent (final judgment depends on the appended proofs), but the practical contribution is weakened by the absence of baselines. Act2Comm's behavior is characterized but not compared against alternatives.

**Soundness:** Medium — the theoretical development is well-structured but cannot be fully verified from the main text alone. The experimental methodology is sound in what it measures but incomplete in what it compares against.

**Clarity:** Good — the paper is well-organized and the core ideas are communicated clearly. The notation is mostly consistent, and the system model is carefully laid out.

**Value:** Medium — the theoretical characterization is valuable for understanding fundamental limits; the practical framework has potential utility but needs stronger empirical validation to establish its effectiveness relative to simpler designs.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>