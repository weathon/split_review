- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 5, 6, 8
Now I have all the information needed to verify each claim against the actual paper text. Let me produce the consolidated review.

## Summary

This paper studies implicit communication through actions in an MDP: a controller embeds messages into its action sequence while pursuing an MDP reward, and a receiver decodes the messages by observing the resulting state trajectory. The environment is modeled as a finite-state channel (POST channel). The paper derives the capacity-reward trade-off as a convex optimization over occupation measures (Theorem 2) and proposes Act2Comm, a transformer-based learning scheme that jointly optimizes control and communication performance for finite blocklengths. Experiments on two small MDPs demonstrate achievable rate–reward–BER trade-offs.

## Strengths

1. **Novel problem formulation with practical relevance.** Framing the MDP environment as a communication channel through which actions carry messages — where the receiver sees states but not actions — is a well-motivated and underexplored setting. The paper clearly distinguishes this from prior work (Sokota et al., 2022, where actions are also observed; Karabag et al., 2019). The introduction provides compelling motivation from biology and robotics.

2. **Theorem 2 — capacity-reward trade-off as convex optimization.** The reduction of the rate-reward trade-off problem to maximizing a concave function \(I(w,T)\) over the polytope of occupation measures \(\mathcal{W}\) with a linear reward constraint is the paper's central theoretical contribution. The closed-form gradient (Lemma 2) makes the optimization solvable. This provides a principled fundamental limit connecting information theory and MDP control.

3. **Act2Comm is a genuinely engineered practical scheme.** The extended action-state (EAS) channel transform, block-attention feedback coding, critic-based gradient estimation through a non-differentiable channel, and the iterative encoder/decoder training together form a non-trivial solution to a difficult joint optimization problem. The design addresses real challenges (non-differentiable quantizer and environment, alternating optimization) that arise in this setting.

4. **Demonstration of controllable trade-offs.** The experimental figures (3–5) show that Act2Comm can achieve different operating points along the rate–reward–BER frontier by varying a single hyperparameter \(\lambda\). This confirms that the framework can practically navigate the trade-off, not merely characterize it theoretically.

## Weaknesses

### Fatal
None.

### Major

1. **No experimental baselines.** The paper presents trade-off curves for Act2Comm alone with no comparison against any alternative communication strategy. Without baselines — e.g., a simple repetition code, a random code that respects action-frequency constraints, a naive scheme ignoring the message (BER=0.5), or the information-theoretic upper bound from Theorem 2 — the reader cannot judge whether Act2Comm is genuinely effective or merely producing the trade-off that any scheme would exhibit. The paper states that Act2Comm "effectively balances" control and communication, but this claim is unsubstantiated without a reference point. This is the most significant gap in the paper.

2. **Theorem 1 attribution is ambiguous.** The paper states (line 79) that the action-state channel "is also referred to as a POST channel in the literature (Permuter et al., 2014)" and simultaneously claims as a contribution (line 20, line 34) that it "derive[s] a single-letter expression for its capacity" (Theorem 1: \(C = \max_\pi I(X;S^+|S)\)). The paper does not clearly state whether Theorem 1 is a known result from POST channel theory or a new derivation. This ambiguity dilutes the paper's novelty claims. Since the main theoretical contribution is Theorem 2 (the capacity-reward trade-off), the authors should explicitly clarify the status of Theorem 1 and refocus the novelty claim on what is genuinely new.

3. **No statistical uncertainty reported.** The experimental results (rate–reward–BER curves) are presented as single trajectories with no error bars, confidence intervals, or multi-seed statistics. Given that Act2Comm involves stochastic training and sampling, the reliability and variance of the reported trade-off curves cannot be assessed. Multiple independent runs with standard summary statistics are needed.

### Minor

1. **Limited scope of empirical validation.** The evaluation is confined to two MDPs: a 3-state/2-action "Lucky Wheel" and a 27-state/3-action "Catch the Ball." While suitable as proof-of-concept, these do not establish how Act2Comm scales to larger state/action spaces or more complex transition structures. The encoder output dimension scales as \(|\mathcal{S}| \times (k/R)\), and the paper does not discuss scaling limits or computational feasibility for larger MDPs.

2. **Conclusion modestly overclaims.** The final paragraph states that Act2Comm "can be used as a plug-in component in various MDP and RL applications" and "may potentially improve overall control performance... when applied to multi-agent systems." These claims go beyond what the paper's experiments (single-agent MDPs with no multi-agent coordination task) demonstrate. The second claim is appropriately qualified ("may potentially," "future research") but the first overreaches.

### Trivial
None.

## Nice-to-Haves

- Comparing Act2Comm's achieved rate-reward pairs against the theoretical frontier \(C(V)\) from Theorem 2 would be highly informative for quantifying how close the practical scheme operates to the fundamental limit.
- A comparison between the block-attention feedback coding and a simpler alternative (e.g., feedforward coding without feedback) would isolate the value of the feedback mechanism.
- Adding a discussion of when the approach might fail (e.g., when the target policy is nearly deterministic, communication rate will be near zero) would strengthen the paper's intellectual honesty.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic's reproducibility concerns about architecture sizes, hyperparameters, training details** — The paper almost certainly includes these in the appendix (stripped by the parser). Per policy, parser-stripped content is assumed to exist. **Removed.**

- **Harsh Critic's complaint about Lemma 1 not being proven** — A proof would reside in the appendix (stripped). **Removed.**

- **Harsh Critic's complaint about environments being described only by reference to appendix figures** — The parser strips figure captions and appendix content; these descriptions exist in the original submission. **Removed.**

- **Harsh Critic's criticism about the encoder definition in Section 3 being "later contradicted" by Theorem 1 (stationary policies suffice asymptotically)** — The paper explicitly addresses this: "Theorem 1 reveals a surprising fact: the capacity... can be achieved by... a stationary randomized policy... without relying on historical information." This is not a contradiction but a key insight. **Removed as factually incorrect about the paper.**

- **Harsh Critic's claim that Theorem 1 being known "reduces" the paper's contribution to "a straightforward convex reformulation"** — This dismisses Theorem 2 unfairly. Theorem 2 (capacity-reward trade-off as convex optimization) is not a trivial corollary; it is a novel result that bridges information theory and control via occupation measures. **Removed.**

- **Strength Finder's generic strengths about the problem being "important" or "well-motivated"** — These are generic and not specific evidence about the paper's execution. **Removed.**

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard tension between a novel problem formulation/theory paper and a practical coding scheme: the theoretical component (Theorem 2) is clean and principled but guarantees only asymptotic optimality, while the practical component (Act2Comm) addresses finite blocklengths but lacks the baselines needed to establish its effectiveness relative to simpler alternatives.

## Suggestions

1. **Add at least one baseline** — a simple repetition code, a random code matching the target action frequencies, or a trivial scheme that ignores the message (BER=0.5). Compare Act2Comm's rate-reward-BER trade-off curves against these. Even a single baseline would substantially strengthen the empirical claims.

2. **Clarify the status of Theorem 1 explicitly.** A single sentence — e.g., "The capacity expression in Theorem 1 follows from known results for POST channels (Permuter et al., 2014); our contribution is the capacity-reward trade-off in Theorem 2" — would resolve the ambiguity.

3. **Run experiments with multiple seeds** (at least 5) and report the mean and variance or shaded confidence bands for the trade-off curves.

4. **Add a brief discussion of scaling and limitations** — comment on how the method's complexity scales with \(|\mathcal{S}|\) and \(|\mathcal{X}|\), and when the communication rate is fundamentally bounded by the structure of the target policy.

5. **Tone down the conclusion** to match what was actually demonstrated: Act2Comm can achieve controllable trade-offs on small MDPs; extending to multi-agent settings and larger-scale problems remains future work.
