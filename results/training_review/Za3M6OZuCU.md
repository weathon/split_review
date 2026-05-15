## Summary

This paper introduces a novel framework for implicit communication through actions within an MDP: the agent (encoder/controller) embeds messages into its action sequence, and a receiver decodes them from the observed state sequence, treating the MDP environment as a finite-state channel (action-state channel). The paper makes two main contributions: (1) a theoretical characterization of the fundamental trade-off between communication capacity and MDP reward, showing the capacity is a single-letter conditional mutual information and the capacity-reward frontier is a convex optimization; (2) Act2Comm, a transformer-based practical coding scheme that jointly optimizes control and communication over the non-differentiable action-state channel via iterative training with a critic network. Experiments on two small MDPs demonstrate that Act2Comm can achieve reliable communication while maintaining specified reward levels.

## Strengths

- **Novel problem formulation.** The paper is the first to frame the MDP environment itself as a communication channel (action-state channel) where actions serve as channel inputs and states as outputs. This cleanly separates from prior emergent-communication work that assumes dedicated parallel channels, and from Sokota et al. (2022) where the receiver observes both states and actions (source coding), whereas here the receiver observes only states (channel coding). The motivation (nano-robots, deep-space robots, adversarial settings) is well-articulated. (Section 1, Figure 1)

- **Single-letter capacity expression for a special FSC.** Theorem 1 gives a closed-form capacity \(C = \max_{\pi} I(X;S^+|S)\) for the action-state channel, achieved by a stationary randomized policy. For general FSCs, capacity characterizations are typically multi-letter; obtaining a single-letter expression by exploiting the POST-channel structure is a genuine theoretical contribution. (Section 4, Theorem 1)

- **Convex characterization of the capacity-reward trade-off.** Theorem 2 reduces the capacity-reward trade-off to a convex optimization over occupation measures \(w\), with a concave objective \(I(w,T)\) and a closed-form gradient (Lemma 2). This makes the fundamental limits numerically computable and provides a principled way to select target policies. (Section 4, Theorems 1–2, Lemma 2)

- **Act2Comm — a practical scheme for non-differentiable FSC coding.** The paper proposes a complete pipeline (channel transform to EAS channel, block-attention feedback coding, transformer encoder/decoder, critic network for gradient estimation, and iterative training) to address the joint control/coding problem. This is a non-trivial engineering contribution for a problem class (non-differentiable FSCs with input-output constraints) with limited prior practical solutions. (Section 5, Figure 2)

## Weaknesses

### Fatal
None.

### Major
- **Experiments lack baselines.** All experimental results (Figures 3–5) show only Act2Comm's own trade-off curves. Without comparison to even simple alternatives — such as a repetition code over the target policy, random block codes, or the theoretical capacity-reward bound from Theorem 2 — it is impossible to assess whether Act2Comm's performance is genuinely good or merely achieves trivial trade-offs. The paper claims Act2Comm "performs excellently" (Section 6), but this claim is unsubstantiated without a reference point. For a new practical scheme, establishing that it improves over straw-man baselines is essential to demonstrate its value. (Section 6, Figures 3–5)

- **Limited experimental scope.** The evaluation is confined to two very small MDPs (3 states/2 actions and 27 states/3 actions). While reasonable as a proof-of-concept, the paper presents Act2Comm as a "general framework" and claims it "can be used as a plug-in component in various MDP and RL applications" (Section 7). The current evidence does not support claims of generality or scalability. Testing on at least one larger or more complex MDP is necessary to substantiate these claims. (Section 6)

### Minor
- **No ablation studies.** Act2Comm incorporates multiple design components (transformer encoder/decoder, block-attention feedback, critic network, temperature-parameterized control loss, iterative training). The paper does not ablate any of these to isolate their contributions. For example, the critic network is motivated as essential for handling non-differentiability, but its benefit over simpler alternatives (e.g., straight-through estimation, REINFORCE) is never validated. Ablations would significantly strengthen confidence in the design choices. (Section 5)

- **Unspecified environment properties.** The "Lucky Wheel" environment is described only as having 3 states and 2 actions, with no mention of whether it is deterministic or stochastic. If it is deterministic, the action-state channel is trivial (noise-free), which limits the informativeness of results on that environment. This detail should be stated explicitly. (Section 6, Experiment 1)

- **Temperature parameter \(\gamma\) not analyzed.** The control loss approximation uses a temperature parameter \(\gamma\) (Section 5) that is said to make the sigmoid approximation sharp when "sufficiently large." No analysis or ablation of \(\gamma\)'s effect on the trade-off is provided, leaving a free parameter without guidance. (Section 5, part 4)

### Trivial
- **Figure references are garbled** (e.g., "the details of the environment and experimental setting is provided in Fig." — cuts off; "Fig. In particular" — incomplete). These are parser artifacts affecting readability.

## Nice-to-Haves
- Comparison against the theoretical capacity-reward bound from Theorem 2 would directly quantify the finite-blocklength gap and help validate the theory.
- A study of how performance scales with blocklength (finite-blocklength behavior) would be informative for practical deployment.
- An analysis of learned codewords (sequences of decision rules) would help interpret how Act2Comm embeds information.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"Unproven foundation of the capacity-reward trade-off"** (Harsh Critic point 2): The critic asserts that Theorems 1–2 and Lemmas 1–2 lack proof. Conference papers routinely defer proofs to appendices; the parser strips appendix content. Per the meta-reviewer guidelines, criticisms about missing proofs in the appendix must be removed. The specific technical concerns about concavity of \(I(w,T)\) and sufficiency of stationary policies are substantive but likely addressed in the stripped appendix material.

- **"Blocklength not specified"** (part of Harsh Critic point 3): The paper defines the code rate and blocklength symbolically (\(n = k/R\)) and the figures show rate on the axes. The specific numerical values of \(k\) and blocklength are implementation details likely in the appendix/experimental settings section (which was stripped). Per guidelines, nitpicks about such implementation details are removed.

- **Missing related work discussion** (Harsh Critic Section-by-Section Notes): The critic says the paper "does not discuss existing machine-learning approaches for coding over non-differentiable channels." The paper actually does discuss this in Section 2 (lines 36–37): "Machine learning has recently advanced traditional channel coding schemes... However, these are designed for Gaussian channels... Our channel, in contrast, is non-differentiable." The paper correctly notes that existing learned coding schemes target differentiable channels and that FSC coding results are limited. The critic's statement is factually incorrect.

- **"Theorem 1 is stated without proof"** (Harsh Critic notes): Same as above — proofs go in the appendix.

- **Formatting/style nitpicks** (e.g., "the paper should at least give key parameters"): Per guidelines, these are removed.

## Novel Insights
None beyond the paper's own contributions. The key insight that emerges from the reviews is that the paper pairs an elegant theoretical characterization (single-letter capacity for a POST channel, convex trade-off) with a fairly complex practical scheme, but the evaluation falls short of convincingly demonstrating the scheme's practical value due to the absence of any comparative baselines. This asymmetry between the clean theory and the opaque empirics is the main tension the authors should address.

## Suggestions
1. **Add at least one baseline** to the experiments. The most natural is the theoretical capacity-reward curve from Theorem 2 (even though it is asymptotic, it provides a meaningful reference). A simple repetition code over the target policy (repeating actions to create codewords) would also be straightforward and informative.
2. **Run at least one ablation** — especially removing either the block-attention feedback or the critic network (replacing it with straight-through estimation) — to demonstrate that the design choices are principled.
3. **State clearly whether each environment is deterministic or stochastic.** If "Lucky Wheel" is deterministic, acknowledge that and focus the narrative on "Catch the Ball" where noise matters.
4. **Temper the generality claims** in the conclusion ("plug-in component in various MDP and RL applications") given the limited evaluation, or add a larger-scale experiment to support them.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>