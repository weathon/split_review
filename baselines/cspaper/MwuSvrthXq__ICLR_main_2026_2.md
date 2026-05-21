---
job_id: 9c94c7b8-3c65-422e-9ffd-adea6146d22f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: MwuSvrthXq.pdf
paper: Reinforcement Learning for Heterogeneous DAG Scheduling with Weighted Cross-Attention
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining reinforcement learning, graph-based representation learning, and combinatorial optimization for heterogeneous DAG scheduling.

## Minimum Quality
Pass ✅. The submission contains the necessary scientific components, including abstract, introduction with related-work discussion, methodology, experiments, quantitative results, and conclusion. While there are substantial concerns about rigor, clarity, and support for some claims, these do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions to reviewers, or suspicious embedded text aimed at influencing automated review.

# Expected Review Outcome:
## Summary
This paper studies heterogeneous DAG scheduling with task-pool compatibility constraints and proposes WeCAN, a single-pass reinforcement learning framework that combines weighted cross-attention between tasks and resource pools with an LDD-based graph encoder for DAG dependencies. The paper also argues that list-scheduling-style generation maps have an inherent optimality gap, introduces a skip-action mechanism intended to close this gap in a single-pass setting, and evaluates the approach on modified TPC-H and computation-graph benchmarks.

## Strengths
The paper addresses a relevant and practically meaningful scheduling setting. Unlike many prior neural DAG schedulers that assume simpler homogeneous settings or fixed environment structure, this work explicitly targets heterogeneous pools with compatibility coefficients, which is a nontrivial and useful extension.

The architectural idea is reasonable and fairly well motivated. In particular, the weighted cross-attention layer in Section 3.1 is designed to let task embeddings depend on the available pool set and compatibility structure, rather than forcing compatibility into a fixed one-hot or averaged summary. This is a sensible inductive bias for the stated goal of adaptability across changing numbers of pools and task types.

The empirical results are broad in scope. The paper evaluates on both a real-world-inspired benchmark family and synthetic computation graphs. In **Table 1** and **Table 2**, WeCAN consistently outperforms the listed heuristic and neural baselines in makespan, often by a visible margin, while keeping runtime in the same ballpark as fast heuristics in greedy mode. Those tables support the claim that the method is competitive in the quality-speed tradeoff, at least on the reported setups.

The ablation study is useful and more informative than the usual checkbox ablation. **Table 3** suggests that both proposed ingredients matter: replacing the proposed WeCA variant with the inside version hurts performance, and replacing LDDGNN with forward or bidirectional GAT also degrades results. This gives some evidence that the gains are not coming from a generic larger model alone.

The figures are helpful in communicating the intended intuition. **Figure 1** gives a reasonably clear high-level picture of the split between one-time neural processing and the generation map. **Figure 2** is also useful because it directly targets the paper’s stated adaptability claim, showing behavior under changes in pool number, pool type, task number, and task type. Even if I have concerns about the evaluation protocol, the figure does at least try to test the right thing rather than only reporting in-distribution benchmark wins.

The discussion of the optimality gap of list scheduling is interesting. The counterexample intuition illustrated in **Figure 5** is easy to follow, and the attempt to connect this to the need for skip actions is conceptually valuable. I appreciated that the paper tries to analyze not just how to train a scheduler, but also what schedules are even representable under the chosen generation map.

## Weaknesses
1. **Several core mathematical expressions are either inconsistent with standard attention formulations or ambiguously specified, which makes the method hard to verify.**  
   The WeCA equation on **Page 4** is particularly problematic:
   \[
   \boldsymbol{g}_v = \boldsymbol{f}_v + \frac{\operatorname{softmax}(\boldsymbol{q}_v^T \boldsymbol{K}^c)}{\sqrt d}\operatorname{diag}(K_{acc}(v,c(1)),\dots,K_{acc}(v,c(n_c)))\boldsymbol{V}^c.
   \]
   This divides the *post-softmax* weights by \(\sqrt d\), whereas in standard scaled dot-product attention the scaling is applied to the logits before the softmax, not after it. The paper later says the “outside” placement of compatibility is intentional, but that does not explain the nonstandard placement of \(1/\sqrt d\). If this is merely shorthand, it should be written correctly. If it is really the implemented form, the attention weights are not normalized in the usual sense, and the interpretation in the text becomes shaky.  
   There is a similar issue in the main-text LDDGNN equation on **Page 5**, where attention appears as
   \[
   \sum_{w\in V}[(\bm q_v^{l,j})^T\bm k_w^{l,j}\cdot b_{d_e(v,w)}\cdot M_{v,w}^j]\bm v_w^{l,j},
   \]
   with no softmax at all, and with multiplicative use of both bias and mask. Later material gives a different formula with additive logits and softmax. Since the main paper is what reviewers evaluate, this discrepancy matters. Right now, the main text presents one mechanism and the later detailed formula presents another.

2. **The probabilistic policy definition is underspecified and internally inconsistent across steps.**  
   In Section 2.2, the paper defines a stepwise policy \(p_\theta(\pi_t\mid s_t,\pi_{<t})\), but on **Page 5**, Equation (1) writes
   \[
   p_\theta(\pi)=\frac{\exp u_\pi}{\sum_\pi \exp u_\pi},
   \]
   reusing \(p_\theta(\pi)\) for what is actually a per-step action probability over currently unmasked actions. This clashes with the earlier definition where \(p_\theta(\pi)\) is the full schedule probability, given as a product over timesteps. That notation is not just cosmetically sloppy, it makes the REINFORCE objective in Section 3.3 harder to parse, because the object being differentiated changes meaning across the paper.  
   Also, the denominator in Equation (1) is written as \(\sum_\pi \exp u_\pi\) without specifying whether the sum is over all task-pool actions, only currently unmasked actions, or also includes skip when available. The text says masks set invalid scores to \(-\infty\), but this should be explicit in the formal definition.

3. **The theoretical claims are stronger than what the main paper convincingly establishes.**  
   The paper makes bold statements such as Theorem 1(ii), claiming Algorithm 1 assigns positive probability to at least one optimal solution and all feasible orders, and Theorem 1(iv), claiming that for each problem there exist scores enabling an optimal solution via greedy selection. These are existence-type representability statements, not performance guarantees, but the prose around them sometimes reads as if the practical gap is therefore “fixed.” That is too strong. Showing that some parameter setting can represent an optimal schedule is not the same as showing the learned model can discover or reliably approximate it.  
   The jump from representability to empirical benefit is particularly aggressive in Section 4.2 on **Pages 6-7**, where the authors state that the single-pass skip design “theoretically closes this gap while retaining computational efficiency.” What is actually shown is closer to a surjectivity or coverage argument over an expanded action space. That is an interesting structural statement, but it does not by itself establish that the training problem is well behaved or that optimal schedules become likely under learned parameters.

4. **The main experimental evidence for the skip-action contribution is too narrow relative to how central it is in the paper.**  
   The abstract, introduction, and Section 4 heavily emphasize skip as a key contribution. However, in the main paper the empirical support is essentially concentrated in **Figure 3**, where only a modified heavy-task setting is shown. That figure does suggest a benefit, but it is a rather narrow slice of the problem family and the setup is not deeply characterized in the main text.  
   More importantly, the central claim is not merely that skip helps on one stress test, but that it closes an important representational gap of list-style generation. For such a central claim, I expected a broader analysis in the main paper: how often skip is used, what fraction of instances materially benefit, whether improvements correlate with measurable structural statistics, and whether the benefit persists outside specially constructed heavy-task cases. As presented, the argument is conceptually interesting but empirically underdeveloped.

5. **The comparison to baselines is not entirely fair or sufficiently controlled.**  
   The baseline selection is decent, but some implementation choices appear favorable to the proposed method and underexplained. For the list heuristics, the paper reports the best of three pool-selection rules, which is fine, but for neural baselines the adaptation choices are more consequential. The description on **Page 7** says One-Shot is used as a single-pass neural baseline, but the paper’s own architecture and environment encoding are substantially tailored to heterogeneous compatibility, whereas the adapted One-Shot baseline appears simplified. The text also notes that Topoformer code was unavailable and a replacement encoder was used, which further muddies the comparison.  
   This matters when interpreting **Table 1** and **Table 2**. The improvements are nontrivial, but because the heterogeneous setting is one of the paper’s main selling points, the burden is on the authors to show that the baselines were adapted as strongly and fairly as possible. Right now, it is still plausible that some of the gain is from better problem encoding rather than from the specific proposed components or training formulation.

6. **The generalization claims are overstated relative to the evidence shown in the main paper.**  
   The paper repeatedly claims adaptability and robust generalization to varying heterogeneous environments. **Figure 2** is the main evidence in the paper, and it is directionally encouraging, but it is not enough to fully support the breadth of the claim. The figure reports percent improvement over best heuristics under a few environment fluctuations, but does not show absolute makespan, variance, or failure cases.  
   Also, the fluctuations seem relatively local around a fixed training setup. The main text then states that this “validates” robust performance under pool-number, pool-type, task-number, and task-type changes. That is too strong. At best, **Figure 2** provides initial evidence of some transfer robustness under selected perturbations. “Validates robust performance” is a much bigger statement than what the figure can sustain.

7. **The training section is too thin for a reinforcement-learning paper making strong empirical claims.**  
   Section 3.3 on **Page 5** gives a very bare REINFORCE description, but omits several choices that materially affect learning stability and reproducibility: sampling scheme per instance, entropy regularization or lack thereof, reward normalization, rollout strategy, gradient estimator details, training budget sensitivity, and how the baseline \(b(X)\) is computed in practice over batched heterogeneous instances. The paper later says the baseline is average rewards, but the main paper itself is sparse.  
   For a method whose contribution depends not only on architecture but also on learning a combinatorial policy, these details are not peripheral. The concern is not just reproducibility; missing optimization details make it harder to assess whether the gains are robust or whether alternative training choices might erase them.

8. **There are notable exposition issues and notation mistakes throughout the paper, and they materially hurt readability.**  
   A few examples: on **Page 3**, the text says “Here, \(F(t,v)\) is the set of tasks on \(c\) at time \(t\),” clearly meaning \(F(t,c)\). On **Page 4**, pool features are introduced as \(\rho(c)\), while the problem definition earlier uses \(\lambda(c)\) for capacities. On **Page 5**, the skip action is denoted \(u_{\pi_{ckip}}\), presumably a typo for \(u_{\pi_{skip}}\). On **Page 34**, Equation (6)-style definitions contain index inconsistencies such as \(\bm V^2\) drawing from \([\bm h_{v(1)}^c,\dots,\bm h_{c(n_c)}^c]\), which mixes task and pool indexing.  
   Any one typo is minor. The issue is cumulative. Because the paper leans heavily on formal arguments, inconsistent notation undercuts confidence that the math and implementation are fully aligned.

9. **Some claimed advantages are not cleanly separated from problem-specific engineering choices.**  
   The paper presents WeCA as a generally adaptable mechanism for compatibility-aware heterogeneous scheduling. But the experiments all use exactly three pools in the main benchmark tables, and the environments rely on manually designed compatibility coefficients by task and pool types. This does not invalidate the work, but it means the results are still somewhat entangled with the specific benchmark construction.  
   For example, in **Table 1**, WeCAN-Greedy is faster than PPO-BiHyb and clearly better in makespan, which is good. But the paper attributes much of this to single-pass efficiency, while the same table also shows that sample-based WeCAN is already substantially slower than greedy, and the gains over the strongest neural baseline are a few thousand makespan units without much structural diagnosis. I would have liked clearer evidence that the proposed representation, not just more tailored benchmark alignment, is driving the win.

10. **The paper’s framing around “closing the optimality gap” is rhetorically stronger than the actual scope of the results.**  
   The counterexample in **Figure 5** is valid as a cautionary example, and I agree that list scheduling can exclude optimal schedules. But the paper often phrases the contribution as if introducing skip resolves the issue in a practical sense. In reality, what is shown is that the action space can represent schedules requiring waiting, and that this helps on some hard cases. That is an important but narrower contribution.  
   I would encourage the authors to tone this down: they are not solving optimal DAG scheduling, and they are not even showing systematic approximation-quality improvements across all regimes due to skip. They are improving representational coverage of the generation map. That is still worthwhile, but the paper would be more credible if it stated the claim in that more precise way.

## Questions
1. In the main-text WeCA equation on **Page 4**, why is the factor \(1/\sqrt d\) applied after the softmax rather than to the logits? If this is notational shorthand, please rewrite it precisely. If it is intentional, please explain how this affects normalization and why it is preferable.

2. The main-text LDDGNN update on **Page 5** appears inconsistent with the later detailed attention formula. Which expression is the actual implemented one? Please provide the exact attention computation used in experiments, preferably in the main rebuttal without requiring readers to reconstruct it from multiple places.

3. For Equation (1) on **Page 5**, what exactly is the normalization domain at each step? Is the sum over all task-pool pairs plus skip, or only over currently unmasked actions? Please state this formally and reconcile the notation with the earlier use of \(p_\theta(\pi)\) for the probability of a full schedule.

4. The paper claims strong adaptability to changing environment structure. Can the authors provide more direct evidence that the learned representation truly handles variable pool/task types, rather than just benefiting from nearby test perturbations? For example, what is the degradation trend as the number of unseen pool types or task types grows further?

5. Regarding **Figure 3**, how sensitive are the skip-action gains to the definition of “heavy tasks”? In particular, do the gains remain when varying only duration, only resource demand, or both? A more disentangled analysis would strengthen the central narrative.

6. Can the authors clarify how fair the neural baseline adaptations are, especially for One-Shot in the heterogeneous setting? What exact architectural and feature changes were made, and how much tuning effort was spent to optimize those baselines?

7. Theorems 1 and 2 are representability statements. Can the authors explicitly discuss the gap between “the optimal schedule has positive probability under some parameterization” and “the learned policy reliably discovers such schedules”? This distinction is currently blurred in Sections 4.1-4.2.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns requiring escalation are evident from the main paper. The work studies scheduling algorithms and reports benchmark results; while deployment could affect efficiency and resource allocation fairness in practice, the submission does not raise a concrete ethics issue that requires formal ethics review at this stage.

## Soundness Rating
2: fair. The paper has a plausible core idea and decent experiments, but important mathematical definitions, theoretical claims, and empirical support for some central assertions are not sufficiently clean or convincing.

## Presentation Rating
2: fair. The paper is understandable at a high level, and some figures help, but the notation, equations, and several parts of the exposition are inconsistent enough to hinder careful verification.

## Contribution Rating
2: fair. The compatibility-aware single-pass scheduling setup is relevant and the empirical results are promising, but the contribution is weakened by overstated claims, limited support for the skip-action narrative, and uncertainty about the exact technical formulation.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a meaningful target problem, some good empirical results, and a potentially useful architectural idea, but the current version is too loose mathematically and too strong in its claims for me to support acceptance with confidence.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I carefully checked the main technical claims and experiments, but some ambiguity in the paper’s notation makes full verification difficult.