---
job_id: 4f9428b8-7872-452a-961f-4bffb8fa922a
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: zqA7Q9Q21L.pdf
paper: R2PS: Worst-Case Robust Real-Time Pursuit Strategies Under Partial Observability
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, at the intersection of reinforcement learning, learning on graphs, multi-agent games, and applications to robotics/security-style planning.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including abstract, introduction, methodology, experiments, quantitative results, and conclusion; it also presents nontrivial technical claims with empirical support, even though several claims and experimental choices need sharper justification.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to reviewers, or other obvious manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies graph-based pursuit-evasion games with two practical complications, partial observability for the pursuers and asynchronous moves where the evader can react after observing or predicting the pursuers’ move. The paper first argues that a dynamic programming distance table computed for Markov PEGs can still induce optimal strategies for the asynchronous evader setting, then introduces a belief-preservation mechanism to extend pursuit policies to partial observability, and finally plugs this mechanism into the EPG cross-graph RL framework to train a GNN-based real-time pursuer policy. Experiments on synthetic and map-derived graphs show improved zero-shot performance over a PSRO baseline and better performance with belief-based updates than with a simpler position-set extension.

## Strengths
1. The paper targets a practically relevant setting that is underexplored in prior PEG work, namely combining graph-structure generalization, worst-case adversarial behavior, and partial observability. This is a meaningful extension beyond the perfect-information setting emphasized in prior EPG-style work.

2. The main technical idea of reusing the DP distance table \(D\) beyond the original synchronous, perfect-information setting is interesting. In particular, the asynchronous evader policy in **Equation (3)** is a natural and clean reformulation of the evader’s decision rule after observing the pursuers’ move, and the link to the minimax structure exposed in **Lemma 1** is one of the more convincing parts of the paper.

3. The partial-observability construction is operationally simple and easy to implement. The position-set update in **Equation (4)** and the belief update in **Equation (7)** give a concrete approximation to full history dependence without blowing up the state space. Even if the approximation is not theoretically optimal under continual partial observability, it is at least clearly specified at a high level and computationally light.

4. The integration with RL is sensible. The policy-guidance loss in **Equation (8)**, which adds a KL-style imitation term toward the DP reference action, is a reasonable way to stabilize adversarial cross-graph training. The training pipeline shown in **Figure 1** helps clarify the interaction among the sampled graph, reference policy, opponent policy, and learned policy; this figure is one of the clearer parts of the paper and supports the claimed training setup better than the surrounding prose alone.

5. The empirical section contains multiple kinds of evaluation rather than a single benchmark number. In particular:
   - **Table 1** is useful because it does more than report wins, it also exposes graph statistics such as node count, average degree, and diameter, which helps contextualize the difficulty variation across maps.
   - **Table 2** is a strong table in terms of breadth. It compares against multiple evader policies, including stay, synchronous DP, asynchronous DP, and a trained best-response asynchronous evader, which is much better than evaluating only against one weak opponent.
   - **Table 4** provides a targeted ablation showing that more frequent belief updates help, and that access to the actual opponent model improves performance. This is one of the more persuasive pieces of evidence that the belief mechanism matters.

6. The learning-curve visualization in **Figure 4** is helpful. It shows that adding DP-based policy guidance \((\beta=0.1)\) improves training over pure RL \((\beta=0)\) on both the synthetic and larger training sets. This directly supports a central design choice in the method.

7. The paper does make a genuine effort to discuss computational practicality. The contrast between RL inference and DP recomputation, supported by **Table 3**, is relevant to the stated “real-time” claim, and the asymptotic comparison in Section 4.2 is aligned with that objective.

## Weaknesses
1. The theoretical contribution is narrower than the framing suggests, and several claims are overstated relative to what is actually established in the main paper. The abstract and introduction repeatedly speak about “worst-case robust real-time pursuit strategies under partial observability,” but the actual strict optimality results, namely **Theorem 2**, **Corollary 1**, and **Theorem 3** in Section 3.1, are for the asynchronous-move perfect-information setting induced by \(D\), not for the partially observable setting. In Section 3.2, the paper explicitly shifts to heuristic extensions based on \(\mathrm{Pos}\) and belief, and the only formal guarantee is **Proposition 1**, which merely says the policies reduce back to the perfect-information policy when \(\mathrm{Pos}\) is a singleton. That is much weaker than any kind of optimality or robustness guarantee under partial observability. This matters because the title and several central claims encourage the reader to expect stronger guarantees than the paper really provides.

2. The mathematical treatment of the belief update is underspecified and in places inconsistent. In **Equation (7)**, the update is written as
   \[
   \text{belief}_{\text{new}}(s_e) \leftarrow \sum_{\text{neighbor }n_e\text{ of } s_e}\nu(n_e,s_e)\text{belief}_{\text{old}}(n_e),
   \]
   but the notation \(\nu(n_e,s_e)\) is never properly defined in the main paper as a transition probability from \(n_e\) to \(s_e\). Earlier, \(\nu\) denotes a policy over actions, and in the asynchronous setting \(\nu^*(s_p,s_e,n_p)\) is an action choice, not a Markov kernel between nodes. Then on **Page 6**, the text says “\(\nu(n_e)\) is set to be a uniform distribution over \(\mathrm{Neighbor}(n_e)\),” which changes the argument structure again. This is not a cosmetic issue, because belief propagation depends exactly on whether \(\nu\) is a policy over actions, a stochastic transition matrix over positions, or something conditioned on pursuer action. The update should be written cleanly, for example as
   \[
   b_{t+1}(s'_e)\propto \mathbf{1}[s'_e\in \mathrm{Pos}_{t+1}] \sum_{s_e} P_\nu(s'_e\mid s_e, s_p, a_t)\, b_t(s_e),
   \]
   together with an explicit definition of \(P_\nu\) and normalization. As written, the belief mechanism is conceptually important but mathematically blurry.

3. The proof presentation in the main paper is too thin for some of the stronger claims. A lot of the heavy lifting is deferred to the appendix, which is acceptable to some extent, but even in the main text the logical assumptions are not fully transparent. For example, **Theorem 1** is conditional on the existence of a pure-strategy Nash equilibrium, which is a significant caveat. Yet the practical algorithmic narrative in Sections 3 and 4 reads as if the DP construction broadly solves the game. Similarly, in Appendix A.1 the Bellman equation presentation is awkward, with formatting and case distinctions that are hard to parse, and the reward/termination handling is not stated as carefully as it should be for an infinite-horizon discounted game with absorbing termination. I am not claiming the theorem is false, but the exposition is not at the standard where a reader can confidently verify the argument from the main paper alone.

4. The empirical evaluation is missing stronger baseline comparisons for partial observability. The main comparative claim in Section 5.2 is against PSRO, but PSRO is a general game-RL framework rather than a specifically strong partially observable graph-policy baseline. The paper also mentions EPG, Grasper, and other prior PEG approaches, yet the experiments do not include a direct adaptation or ablation showing what happens if one uses the same GNN/RL backbone without the proposed belief-preservation mechanism, or with a recurrent history encoder instead of the handcrafted \((\mathrm{Pos}, \text{belief})\) input. Without such comparisons, it is hard to isolate whether the gains come from the new partial-observability design, from pretraining across more graphs, or simply from a stronger training recipe.

5. Relatedly, the ablation story is still incomplete despite **Table 4**. That table is helpful, but it only probes update frequency and access to the true opponent. It does not answer several key questions: what happens if belief is removed entirely and only \(\mathrm{Pos}\) is used in RL; what happens if both \(\mathrm{Pos}\) and belief are removed and the policy sees only current local observations; how sensitive performance is to the choice of uniform default \(\nu\); whether the gains persist under different observation ranges during training, not just test-time; and whether the benefit in **Figure 4** comes mainly from guidance \(\beta>0\) or from the belief-state augmentation. These are core questions for understanding the method rather than minor extras.

6. The “worst-case robustness” claim is stronger than the evidence. **Table 2** shows that the method does well against the asynchronous DP evader and still retains nontrivial performance against a trained best-response asynchronous evader, which is good. But the results are far from uniformly strong on the harder maps. Against \(\mathrm{BR}_{\mathrm{async}}\), success rates drop to \(0.10\), \(0.20\), \(0.23\), and \(0.27\) on several graphs in **Table 2**. This does not invalidate the approach, but it does weaken the repeated phrasing suggesting robust worst-case performance. The more precise claim would be that the policy is more robust than the compared baseline and remains real-time, not that it has established strong worst-case robustness in the partial-observability regime.

7. The use of a globally informed optimal asynchronous evader against partially observable pursuers is defensible as a stress test, but it creates a somewhat lopsided setting that is not fully discussed. The paper motivates this as a worst-case security scenario, which is fair, yet this assumption is doing a lot of work. It would be useful to know whether the method remains superior under more symmetric information structures, or whether some of the observed benefit is specific to training against this particular DP adversary. As written, the paper makes a strong practical case but only under one rather adversarial information asymmetry.

8. The “real-time” scalability evidence is useful but still limited. **Table 3** reports RL inference times under larger graphs, and the speed gap versus DP is indeed large. However, the practical graphs are still in the low-thousands of nodes, and the architecture described in Appendix C.2 relies on \(O(n^2 m)\) attention-style computations. For a paper making a strong real-time and dynamic-graph deployment pitch, I would have liked a clearer analysis of memory/runtime bottlenecks, especially since the GNN encoder uses dense attention rather than a sparse message-passing architecture. The current evidence supports “faster than recomputing DP on these tested graphs,” which is weaker than the broader real-time narrative.

9. Some presentation choices reduce clarity. **Algorithm 1** on **Page 4** is difficult to read in the provided format, and the nested conditions in the loops are especially hard to parse. The notation also drifts between policies over actions, positional transitions, and next-node selections. This matters because the paper’s main contributions are not just empirical, they rely on readers trusting the exact minimax semantics of the DP and belief updates. The prose occasionally slides from theorem-backed statements to intuition-heavy claims without clearly marking the boundary.

10. The figures illustrating belief preservation are visually intuitive, but their scientific role is limited. **Figure 2** and **Figure 3** help the reader form an intuition for how belief spreads and collapses after observing the evader, and I appreciate that. However, they stop short of explaining why the particular belief dynamics in **Equation (7)** are the right abstraction or how they relate quantitatively to improved capture rates. In other words, the figures are useful illustrations, but they do not compensate for the missing analytical justification of the belief update.

## Questions
1. Please clarify the exact semantics of **Equation (7)**. Is \(\nu(n_e,s_e)\) meant to denote a transition probability \(P(s_e \mid n_e)\), an action-conditioned policy-induced kernel, or something else? How is this reconciled with the earlier notation where \(\nu\) is a policy over actions, especially in the asynchronous setting where \(\nu^*(s_p,s_e,n_p)\) depends on the pursuers’ move?

2. Can you provide a sharper statement of what is and is not theoretically guaranteed under partial observability? Right now, the main text seems to move from strict optimality in Section 3.1 to a much weaker heuristic in Section 3.2, but the framing does not always reflect that shift. A more precise claim would increase confidence.

3. What would happen experimentally if the RL policy used only \(\mathrm{Pos}\), only belief, neither of them, or a learned recurrent history encoder instead? A clean ablation here would help isolate whether the gains truly come from belief preservation rather than from general cross-graph training.

4. In **Table 2**, how sensitive are the reported zero-shot results to the number and diversity of training graphs? The paper trains on 300 graphs total. It would be useful to know whether the same qualitative advantage over PSRO holds with substantially fewer training graphs, or whether performance depends critically on training-set scale.

5. The comparison to PSRO is interesting, but can you include or discuss a stronger partially observable baseline that uses the same backbone architecture and training budget without the proposed guidance/belief mechanism? That would make the empirical attribution much cleaner.

6. For the scalability claim, can you provide memory consumption or throughput details in addition to wall-clock time, especially given the \(O(n^2 m)\) attention computation in Section 4.2? This would make the real-time claim more convincing.

7. The paper motivates the globally informed evader as a worst-case adversary. Could you report at least one experiment where the evader is also observation-limited, or where the pursuers do not train specifically against the asynchronous DP evader? This would help assess how specialized the learned policy is to the chosen adversary model.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
N/A.

## Soundness Rating
3: good. The core technical direction is plausible and several claims are supported, but the partial-observability component is more heuristic than the framing suggests, and some key notation around the belief update is insufficiently precise.

## Presentation Rating
2: fair. The paper is readable overall and the high-level story is understandable, but notation drift, awkward algorithm presentation, and some overstatement of guarantees reduce clarity.

## Contribution Rating
3: good. The paper addresses an important and underexplored setting and combines DP-based adversaries, belief preservation, and cross-graph RL in a useful way, although the empirical attribution and theoretical scope are not as strong as the headline framing suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper tackles a meaningful problem and has enough technical and empirical substance to merit serious consideration, especially the asynchronous-DP extension and the cross-graph RL integration. That said, the partial-observability guarantees are much weaker than the title suggests, the belief update is underspecified mathematically, and the ablations are not yet strong enough to fully validate the core mechanism.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main technical and experimental claims carefully, though some proof details rely on appendix material and the notation around belief propagation leaves room for interpretation.