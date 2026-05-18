Here is my final consolidated review.

## Summary

This paper introduces the paradigm of communicating through actions in a Markov decision process (MDP), where the controller's actions serve as channel inputs and the resulting states serve as channel outputs observable by a receiver. The paper makes two main contributions: (1) a theoretical characterization of the action-state channel capacity (Theorem 1) and the capacity–reward trade-off as a convex optimization (Theorem 2); and (2) Act2Comm, a transformer-based coding scheme that learns to embed messages into actions while approximately preserving a target policy's reward. Experiments on two small MDPs demonstrate the feasibility of this approach.

## Strengths

- **Single-letter capacity expression for a non-trivial FSC (Theorem 1).** Deriving a closed-form capacity formula that depends only on the stationary randomized policy and MDP transition kernel is a genuine theoretical contribution. The result that capacity can be achieved without history-dependent encoding—despite the general necessity of multi-letter expressions for FSCs—is a clean and non-obvious insight enabled by the action-state channel's special structure.

- **Capacity–reward trade-off as a convex optimization with a computable gradient (Theorem 2, Lemma 2).** Mapping the trade-off to a convex program over occupation measures allows efficient numerical computation of the information-theoretic upper bound. The closed-form gradient enables gradient-based solvers. This provides a principled benchmark for any practical coding scheme.

- **Act2Comm addresses a genuinely hard problem.** The scheme tackles the non-differentiability of the action-state channel (due to discrete actions and stochastic transitions) via a critic-based gradient approximation and sigmoid-based differentiable surrogate for policy frequency. The block-attention feedback mechanism is a sensible design for the finite-blocklength regime.

- **Clear differentiation from prior work.** The paper explicitly distinguishes its setting from Sokota et al. (2022) (where the receiver observes both actions and states, making it a source coding problem) and from standard emergent communication with dedicated channels. This motivates why the problem is fundamentally different and harder.

- **Concrete experimental demonstration.** The paper reports specific quantitative results: in "Catch the Ball" (p=0), Act2Comm achieves zero-error communication at rate 0.2 while reducing reward from 1.66 to 1.5 (roughly 10% sacrifice). This demonstrates feasibility of the proposed approach.

## Weaknesses

### Fatal
None.

### Major

- **No baselines or comparison to the theoretical capacity–reward bound.** The experiments show Act2Comm's own trade-off curves but provide no reference point for interpretation. There is no comparison to even simple alternatives (e.g., a repetition code mapped through actions, a block code using random decision rules, or a naive scheme that separates control and signaling actions). More critically, the paper derives C(V) from Theorem 2—the information-theoretic upper bound—but never plots Act2Comm's achieved rate–reward points against this curve. Without knowing how far the scheme is from the bound, the reader cannot judge whether Act2Comm's performance is good, mediocre, or poor. This omission substantially weakens the empirical contribution, which is the paper's third stated contribution.

- **The critic-based gradient estimation mechanism is underspecified.** The paper states that a critic network is trained on noisy neighbors of the belief map Z and that this "helps update the encoder" via "the learned gradient estimation." However, the precise mechanism connecting the critic's predictions to gradient updates of the encoder parameters is never made concrete. The iterative training procedure (alternating between encoder and decoder updates) is described at a high level, but the update rules are not given. Key hyperparameters (learning rates, temperature γ schedule, number of inner steps s_in, network architecture sizes) are absent, which makes reproducibility difficult.

### Minor

- **Overclaimed generality.** The conclusion states that Act2Comm "can be used as a plug-in component in various MDP and RL applications," but experiments are limited to two small environments (3 states/2 actions and 27 states/3 actions). This claim should be tempered or supported with more diverse evaluation.

- **Environment descriptions are too brief in the main text.** Both test environments are introduced in 1–2 sentences with references to figures that are not legible in the extracted text. While the basic parameters are given, the reader cannot fully assess the suitability or complexity of these testbeds without visual aids.

### Trivial

- The temperature parameter γ for the sigmoid-based frequency estimator is mentioned but its effect on training stability, bias, and the choice of "sufficiently large" is not discussed.
- The communication loss L_com is defined as cross-entropy "between the predictions from a critic network and their corresponding ground-truth," but it is unclear whether the critic's predictions or the decoder's logits are ultimately used for decoding at test time.

## Nice-to-Haves

- Comparing Act2Comm's achieved rate–reward pairs against the theoretical C(V) curve from Theorem 2. This single addition would greatly strengthen the paper.
- Adding simple baselines (repetition coding, random decision-rule code, a naive separation scheme) to contextualize Act2Comm's performance.
- Ablation study: replacing the transformer encoder with a simpler architecture (e.g., MLP) to justify the design choices.
- Error probability vs. blocklength curves for various rates, since the finite-blocklength regime is central to P3.

## Removed Points

- **"Notation is overloaded"** — The reviewer claimed X (Section 3) conflicts with x_t and U. This is standard notation: X is a random variable, x_t is an instance, and U is the decision-rule space for the EAS channel. All are clearly distinguished in the text. *(Removed: factually incorrect criticism.)*
- **"B^(τ), C^(τ) not fully defined"** — Both are explicitly defined in the main text: B^(τ) ≜ [2b_1−1; ... ; 2b_τ−1] and C^(τ) ≜ [C_1; ... ; C_τ]. *(Removed: factually incorrect.)*
- **"Combinatorial explosion of decision-rule space U = X^{|S|}"** — The reviewer claimed the encoder would need to handle 3^27 ≈ 7.6×10^12 possibilities. This misunderstands the method: the encoder outputs a continuous belief map Z ∈ R^{|S| × k/R}, then quantizes it element-wise to U. The output dimension per time step is |S| (manageable), and U is never enumerated. *(Removed: misunderstanding of the method.)*
- **Missing appendix/proofs** — Referenced. These exist in the original submission; the parser strips appendix sections. *(Removed: per hard rule.)*
- **Missing figure details** — "Detailed architecture is provided in Fig." — The figures exist in the original submission but were stripped by the parser. The paper provides textual descriptions alongside them. *(Removed: parser artifact.)*
- **Strength: "Experimental validation with concrete numbers" from Strength Finder** — Kept, as the numbers are concrete and relevant. However, note the caveat about missing baselines.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Plot Act2Comm's achieved rate–reward points against the theoretical C(V) curve from Theorem 2 for the same environments. This is the single most impactful improvement: it quantitatively connects the two main contributions and lets the reader assess how much gap remains.
2. Add at least one simple baseline (e.g., a repetition code mapping binary messages onto repeated decision rules, or a random code) to ground the performance numbers.
3. Provide a pseudocode description of the iterative training procedure, including the specific update steps for the encoder via the critic network.
4. Temper the generality claim in the conclusion, or add experiments on larger/more diverse environments.
5. Report key hyperparameters (learning rates, γ schedule, s_in, architecture sizes) for reproducibility.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>