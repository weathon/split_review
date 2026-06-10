## Summary

This paper introduces Distributed Hebbian Temporal Memory (DHTM), an episodic memory model for online sequence learning in partially observable environments. DHTM combines factor graph belief propagation with a multi-compartment neuron model inspired by HTM, using local Hebbian learning rules and sparse transition matrices to form Successor Features without backpropagation. The method is evaluated in Gridworld and AnimalAI navigation tasks against LSTM, CSCG, and a tabular Episodic Control (EC) agent, with additional comparison to Dreamer V3.

## Strengths

- **Demonstrates online adaptation to non-stationary environments without oracle resets.** In the Gridworld experiment (Section 4.1, Figure 2A), after the environment changes at episode 300, DHTM quickly recovers and finds a new trajectory. This directly supports the paper's claim of fully online operation, and contrasts with CSCG which cannot adapt without being retrained from scratch and LSTM which performs poorly even with an oracle reset signal.

- **Provides evidence that cross-variable temporal dependencies matter for distributed representations.** The factor-size ablation in AnimalAI (Figure 3B) shows that DHTM with factor size > 1 (which captures dependencies across multiple previous time-step hidden variables) converges to a near-optimal path, while factor size = 1 (equivalent to independent parallel HMMs) fails to converge. This is the cleanest experiment in the paper, demonstrating that the model's ability to account for statistical dependencies between features is not just architectural overhead but yields measurable benefit.

- **Local Hebbian learning rules avoid global gradient signals.** Equations (15) and (17) define Monte-Carlo updates for transition weights and synapse efficacies using only pre- and post-synaptic coincidences, with no backpropagation through time or full-sequence buffers. This design choice enables truly online operation and is a principled departure from dominant gradient-based approaches.

## Weaknesses

### Major

- **The Dreamer V3 comparison is not controlled and the "order of magnitude" claim overstates the evidence.** The paper's headline efficiency claim (Abstract, line 21) compares DHTM (~3k steps) against Dreamer V3 (~35k steps), but DHTM benefits from substantial prior knowledge that Dreamer V3 does not receive: (a) a pre-trained encoder trained offline on 2000 episodes of uniform-strategy data (line 304); (b) a hand-decomposed reward function over feature states (Eq. 11, line 186); and (c) planning under a fixed uniform policy rather than learning a policy (line 222). These differences mean the two systems solve fundamentally different problems with different amounts of baked-in knowledge. The pre-training data alone (2000 episodes) likely exceeds or rivals the total interaction budget being compared. A controlled comparison — e.g., giving Dreamer V3 the same decomposed reward and pre-trained encoder — would be needed to support the claimed efficiency advantage. As presented, the comparison is misleading and should be removed or substantially recontextualized.

- **No comparison against neural episodic memory methods that already handle distributed representations.** The paper's core claimed advantage over tabular EC is support for distributed representations (line 27, line 317). However, there exists a substantial literature on neural episodic memory for RL — Neural Episodic Control (Pritzel et al., 2017, cited by the paper), MERLIN (Wayne et al., 2018), and differentiable neural dictionaries — that already combines episodic memory with distributed representations. Without comparisons against these methods, it is impossible to assess whether DHTM offers a genuine advance or is simply a different implementation of the same idea. This gap undermines the paper's ability to establish novelty.

### Minor

- **The advantage over simple tabular EC is modest, and the distributed representation case rests on a single ablation.** In Gridworld (Figure 2), the paper acknowledges EC "performs on par with DHTM" (line 287). In AnimalAI (Figure 3A), DHTM with factor size 4 converges to a "slightly shorter path on average" with overlapping error bars. The factor-size ablation (Figure 3B) is the only experiment showing a clear advantage, and it is a single ablation on a single task with a modest effect size. The paper's contribution would be substantially strengthened by demonstrating a task where tabular EC simply cannot scale (e.g., a larger state space) while DHTM succeeds.

- **The LSTM and CSCG baselines are evaluated in a setup that systematically disadvantages them.** These models are plugged into a custom planning architecture (successor feature computation under uniform policy, hand-crafted action selection) that is not designed to exploit their strengths. LSTMs are designed for end-to-end training via BPTT, not for serving as a predictive module in a bespoke planning loop. The LSTM "doesn't show any learning on this time-step scale" (line 306); this likely reflects an architecture mismatch rather than a fundamental limitation of recurrent models for this domain. The comparison would be more informative if it included approaches designed for online adaptation (e.g., online Bayesian HMM variants, streaming recurrent architectures).

- **Only 5 random seeds are used for each experiment (line 269).** For RL experiments with the level of stochasticity present in these environments, 5 seeds is marginal for establishing statistical significance, especially when error bars overlap (as they appear to in parts of Figure 3A).

- **Key methodological components are heuristic and their effects are unanalyzed.** The segment log-likelihood interpolation (Eq. 6) and the max-approximation replacing marginalization (Eq. 8) are motivated by intuition and neurophysiological analogy, respectively, but the paper provides no analysis of what information is lost, under what conditions these approximations are reasonable, or whether they preserve any consistency guarantees of the sum-product algorithm. While heuristic components are common in bio-inspired methods, the paper's claims of fast, reliable online learning would benefit from at least empirical characterization of how these choices affect behavior.

- **The claimed computational efficiency from sparsity is not empirically supported.** The paper states that complexity depends linearly on the number of non-zero components (line 132), but provides no measurements of actual sparsity levels, parameter counts, runtime, or memory usage. For a method whose practical utility is partly motivated by efficiency, the absence of any computational profiling is a gap.

### Trivial

- The tabular EC baseline assumes "infinite cells per column" (line 260), giving it effectively unlimited representational capacity. This is a significant advantage that helps explain its strong performance but is not discussed as a factor favoring the baseline.

## Nice-to-Haves

- Convergence or stability analysis of the Hebbian learning rules, especially in non-stationary environments where old memories should decay appropriately.
- A task where tabular EC cannot scale (e.g., due to state-space size) to clearly demonstrate DHTM's distributed representation advantage.
- Runtime and memory measurements to substantiate the claimed efficiency from sparsity.
- An analysis of when DHTM's lack of hidden-state generalization (each trajectory gets a unique encoding) causes it to fail — e.g., tasks requiring generalization across similar trajectories.

## Removed Points

- **"Little research on TM models that can be used in fully online adaptive systems" (harsh critic)**: Removed per hard rules — arguing the paper overlooks related work (online Bayesian HMMs, streaming LSTMs) is effectively a "missing related works" criticism that cannot be verified with the tools available.
- **"No convergence analysis of learning rules" (harsh critic)**: Demoted to minor/removed — the request for convergence proofs is not standard for an empirical systems/methods paper at this venue; the paper is adequately transparent about the update rules.
- **"Failure analysis / when DHTM does not work" (harsh critic)**: Removed — this is a constructive suggestion for future work, not a weakness of the current paper. The paper already acknowledges the generalization tradeoff (line 19).
- **"Computational cost — no runtime measurements" (harsh critic)**: Moved to nice-to-have — reporting runtime is valuable but not a standard expectation for a methods paper; the absence does not threaten the core claims.
- **Strength Finder's Strength 3 (Dreamer V3 efficiency)**: Removed per rules — it conflicts with the verified weakness about the uncontrolled Dreamer V3 comparison; when a strength and verified weakness disagree, the weakness wins.
- **Strength Finder's Supporting Strength 2 ("principled log-likelihood approximation")**: Removed as overclaimed — the paper itself describes this as an interpolation "between two extreme cases" (line 151), making it a heuristic, not a principled derivation. The label "principled" is inaccurate.
- **Strength Finder's generic strengths about "addressing an important problem"**: The strength finder did not produce such generic strengths in this case, so no removal needed.

## Novel Insights

The contrasting perspectives between the harsh critic and strength finder reveal a fundamental tension in the paper: the method is genuinely novel in its architecture (factor graph + dendritic segments + Hebbian learning), but the experimental strategy consistently undersells this novelty. The harsh critic correctly identifies that the strongest baselines (tabula EC) match DHTM's performance, and the Dreamer V3 comparison is uncontrolled — yet the strength finder correctly identifies that the factor-size ablation (the single experiment where DHTM clearly outperforms alternatives) is the most informative result in the paper. The synthesis reveals that the paper's evidentiary bottleneck is not a flaw in the method but in the evaluation design: a single ablation (factor size 1 vs. 4) carries nearly the entire weight of the distributed-representation claim. If the authors had added just one more experimental condition — a task where tabular EC provably fails while DHTM succeeds — the paper's central thesis would be convincingly supported. The current submission has all the right pieces but lacks the decisive experiment that would connect its architectural innovation to a clear empirical victory.

## Suggestions

1. **Recontextualize or remove the Dreamer V3 comparison.** Either control for the pre-trained encoder, decomposed reward, and uniform policy, or remove the comparison and simply report DHTM's absolute performance. The headline claim in its current form is misleading.

2. **Add a comparison against at least one neural episodic memory method** (e.g., Neural Episodic Control or a differentiable neural dictionary baseline). This is the natural competitor for the paper's claimed advantage.

3. **Design an experiment where tabular EC cannot scale** — e.g., a larger state space, higher-dimensional features, or a task requiring generalization — and show DHTM succeeds. This single addition would convert the factor-size ablation from a suggestive result into a conclusive one.

4. **Increase the number of seeds** to at least 10–20 for the main RL results to improve statistical reliability.

5. **Provide empirical sparsity measurements** (e.g., fraction of non-zero factors over time, memory usage) to substantiate the efficiency claims.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>