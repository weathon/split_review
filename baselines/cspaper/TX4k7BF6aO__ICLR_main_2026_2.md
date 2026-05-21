---
job_id: efaafa11-fc31-4e38-9205-40961ab3f3e3
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: TX4k7BF6aO.pdf
paper: Agentic Reinforced Policy Optimization
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This submission is clearly within ICLR scope, it studies reinforcement learning for LLM-based agents, uncertainty via token entropy, and policy optimization for multi-turn tool use.

## Minimum Quality
Pass ✅ The paper includes the expected scientific structure, namely abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion. While I have substantial concerns about some mathematical claims and parts of the empirical methodology, these are review-level issues rather than desk-reject-level failures.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find hidden prompts, instructions targeting automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes Agentic Reinforced Policy Optimization (ARPO), an RL algorithm for multi-turn tool-using LLM agents. The main idea is to use token entropy after tool calls as a signal for adaptive branching during rollout, then train with a step-aware advantage attribution scheme built on top of GRPO-style updates. The paper evaluates ARPO on 13 benchmarks spanning mathematical reasoning, knowledge-intensive QA, and deep search, and reports consistent gains over trajectory-level RL baselines with improved tool-call efficiency.

## Strengths
The paper tackles a timely and relevant problem. Most RLVR-style work for LLMs still treats rollouts at the trajectory level, while actual tool-using agents make a sequence of branching decisions conditioned on environment feedback. The paper identifies this mismatch clearly and proposes a method that is at least directionally aligned with the structure of the problem.

The empirical motivation around entropy is interesting and reasonably well communicated. In **Figure 1** and **Figure 2**, the authors show that token entropy tends to spike immediately after tool feedback, especially for search-based interactions. Even though the causal interpretation is not fully nailed down, these figures do support the practical intuition that tool feedback creates local uncertainty regions where extra exploration may be useful. I also appreciated that **Figure 4(a)** makes the proposed adaptive branching mechanism easy to understand at a glance.

The experimental suite is broad for this line of work. **Table 1** covers 10 reasoning benchmarks across two backbone families, and **Table 2** extends the study to harder deep-search settings with both 8B and 14B Qwen3 models. This is more comprehensive than many agentic RL papers that report results on only one narrow benchmark family. The gains are also fairly consistent: in **Table 1**, ARPO improves over GRPO/DAPO/REINFORCE++ on the average score for both Llama3.1-8B and Qwen2.5-7B; in **Table 2**, ARPO beats GRPO across the main averages for GAIA, WebWalkerQA, and HLE.

The efficiency angle is practically valuable. The right panel of **Figure 1** and **Figure 7(a)** both argue that ARPO reaches better accuracy with fewer tool calls during training. For agentic RL, where tool usage can dominate cost, this is not a cosmetic metric.

The method is presented with enough algorithmic structure that one can understand what is being changed relative to standard GRPO-style training. The rollout mechanism in Section 3.1 and the workflow in Algorithm 1 make the implementation path fairly concrete.

## Weaknesses
1. **The core mathematical definitions around entropy change and branching are underspecified and partly inconsistent, which matters because they directly determine when ARPO explores.**  
   In Section 3.1 on **Page 4-5**, the paper defines \(H_{\mathrm{initial}} \in \mathbb{R}^{1 \times k}\), then \(H_t \in \mathbb{R}^{1 \times k}\), and then \(\Delta H_t = \mathrm{Normalize}(H_t - H_{\mathrm{initial}})\). But the text immediately after says that normalization means “summing all the values of \(\Delta H\) and dividing by the vocab size \(V\).” This is odd for several reasons. First, if \(H_t - H_{\mathrm{initial}}\) is a length-\(k\) vector over token positions, dividing its sum by vocabulary size \(V\) is dimensionally unmotivated, because entropy itself is already a scalar per token obtained after summing over the vocabulary in **Equation (1)**. Second, once the vector is collapsed by summation, \(\Delta H_t\) is no longer a matrix or vector, despite the notation suggesting otherwise. Third, **Equation (2)** then uses \(P_t = \alpha + \beta \cdot \Delta H_t\), which assumes a scalar. This is the core control signal of the method, yet its exact computation is not cleanly specified. That is not a minor notation quibble, it affects reproducibility and the interpretation of the whole branching rule.

2. **The probabilistic branching rule in Equation (2) is not well defined as a probability, and the parameter semantics are confused.**  
   In **Equation (2)** on **Page 5**, \(P_t = \alpha + \beta \Delta H_t\) is called the “partial sampling probability,” but there is no guarantee that this quantity lies in \([0,1]\). There is no clipping, sigmoid, normalization, or any other probabilistic transform. Then branching is triggered if \(P_t > \tau\). This makes \(P_t\) more of a score than a probability. Also, the text says \(\beta\) represents the “stability entropy,” which is not defined anywhere. If branching is central to the claimed gains, the paper needs a precise operational definition: is \(P_t\) a Bernoulli parameter, a heuristic score, or a deterministic thresholded statistic? Right now it is somewhere in between.

3. **The theoretical section substantially overclaims what is actually shown.**  
   Section 3.3 claims a “Generalized Policy Gradient (GPG) Theorem” and further states that “ARPO, as an advanced implementation of the GPG Theorem, provides a robust theoretical foundation” (**Page 6-7**). But the derivation in **Equation (6)** and in Appendix F.3 is largely a re-grouping of token-level autoregressive probabilities into macro-actions. For an autoregressive model, writing
   \[
   \prod_{t=1}^{H}\pi_\theta(a_t \mid s_t) = \prod_{T=1}^{K}\pi_\theta(MA_T \mid MS_T)
   \]
   is basically a segmentation identity, not a substantive new policy-gradient result. More importantly, the theorem does not analyze the actual ARPO mechanism, namely entropy-triggered branching with shared-prefix trajectories and advantage attribution. There is no theorem about when entropy-based branching improves sample efficiency, reduces variance, preserves unbiasedness, or stabilizes optimization. So the theory does not support the main algorithmic novelty as strongly as the text suggests.

4. **The discussion of soft advantage estimation is not mathematically convincing, and the notation becomes shaky in a way that blocks verification.**  
   Section 3.2 and Appendix F.2 try to justify why the “soft” setting approximates the hard shared-token attribution. However, several details are problematic. In **Equation (3)** the GRPO objective is standard, but **Equation (4)** only notes that if two trajectories share the same prefix then their importance ratios are equal for the shared token positions. That observation alone does not imply that the resulting optimization “closely approximates” the hard shared-token estimator. The later derivation in Appendix F.2 introduces mixed notations \(o_i\), \(o_i'\), \(o_l^i\), \(o_{l:i}\), \(y_i\), \(p\), \(q\), and even uses reference-model ratios in **Equations (12)-(13)** whereas **Equation (3)** defined ratios against \(\pi_{\mathrm{old}}\), not \(\pi_{\mathrm{ref}}\). That is a substantive inconsistency, not just typography. Since the paper claims a theoretical interpretation of the soft estimator, the mismatch between
   \[
   r_{i,t}(\theta)=\frac{\pi_\theta(\cdot)}{\pi_{\mathrm{old}}(\cdot)}
   \]
   in the main text and
   \[
   r^{<l}_{i,t}(\theta), r^{>l}_{i,t}(\theta) = \frac{\pi_\theta(\cdot)}{\pi_{\mathrm{ref}}(\cdot)}
   \]
   in the appendix undermines the derivation. At present, I do not think the paper has actually established the claimed equivalence or regularization view.

5. **The reward formulation in Equation (5) is poorly specified and arguably malformed in the main text.**  
   On **Page 6**, the piecewise definition of \(R\) is difficult to parse and appears incomplete. The formatting suggests
   \[
   R = \max(\mathrm{Acc.}+r_M, \mathrm{Acc.})
   \]
   if format is good and \(\mathrm{Acc.}>0\), then \(0\) if format is good and \(\mathrm{Acc.}=0\), and a nested definition of \(r_M\). But the condition for bad format is not stated explicitly, and the notation “\(\exists (<\text{search}> \& <\text{python}>)\)” is not precise. It is also not obvious why a reward bonus for jointly using search and python is appropriate across all tasks in the benchmark suite. This matters because the method is partly presented as an algorithmic contribution, but the observed gains may depend materially on this particular reward shaping.

6. **The empirical comparisons are broad, but some key controls are missing for isolating what actually drives the gains.**  
   The paper compares ARPO mainly against trajectory-level RL baselines such as GRPO, DAPO, and REINFORCE++. However, ARPO combines at least two changes: adaptive branching in rollout and a modified treatment of shared versus branched token advantages. The main paper does not provide a clean ablation table separating: (i) branching only, (ii) advantage attribution only, (iii) entropy trigger versus random trigger, and (iv) entropy trigger versus fixed branching after every tool call. **Figure 5** only compares hard versus soft advantage estimation, and even there the y-axis is reward during training rather than downstream benchmark performance. Without these controls, it is difficult to know whether the main gain comes from entropy-awareness specifically, from simply spending rollout budget on partial branches, or from some interaction with reward design.

7. **The efficiency claim is promising, but the accounting is not fully apples-to-apples.**  
   The paper repeatedly claims that ARPO uses “only half the tool-use budget” of existing methods, highlighted in **Figure 1** and **Figure 7(a)**. But ARPO also computes extra token entropies after tool calls and may branch from intermediate states, which changes the shape of compute rather than only the number of tool invocations. Tool calls are indeed expensive, but they are not the only cost in agentic RL. If the paper wants to make a broader efficiency claim, it should report at least one of wall-clock time, total generated tokens, or training FLOPs. Otherwise, the result is better interpreted as “tool-call efficiency,” not overall training efficiency.

8. **The evaluation setup raises reliability questions because many deep-search results rely on LLM-as-judge, and the paper gives little calibration for this choice in the main text.**  
   In Section 4 on **Page 7**, the paper states that for tasks beyond four QA datasets, results are “judged by Qwen2.5-72B-instruct under the LLM-as-Judge setup.” This is common in the area, but here it covers a substantial portion of the evaluation, including **Table 2**. The paper does not provide, in the main text, agreement statistics with human annotation or exact judging prompts. For tasks like GAIA/HLE/WebWalkerQA, small formatting differences or partial correctness can materially affect scores. The issue is not fatal, but it lowers confidence in the precision of the reported margins.

9. **The presentation has a number of local clarity issues that make the paper look less mature than the empirical scope would suggest.**  
   There are several examples: “pioneeringly” in the contribution list is marketing language rather than scientific positioning; “real-time feedback in real-time” on **Page 2** is redundant; Section 3 says the method is illustrated in “Figures 3 and 4” but **Figure 3** is more of a high-level schematic and **Figure 4** is the actual mechanism diagram; **Algorithm 1** on **Page 33** contains suspicious details such as “for iteration \(=1,\dots,1\)” and line 30 updating \(r_\phi\) via replay, even though the rest of the paper describes rule-based rewards rather than a learned reward model. These issues do not invalidate the empirical findings, but they do make it harder to tell which parts are essential and which are generic boilerplate.

10. **The paper’s positioning against closely related step-level or segment-level RL work is somewhat incomplete in spirit, even if the citation list is fairly extensive.**  
   The authors cite several relevant recent papers, including segment-level RL and step-level tool-use work. Still, the paper does not sharply distinguish ARPO from the closest neighboring ideas, especially methods that already advocate finer-grained credit assignment or trajectory decomposition for LLM RL. The burden here is not just adding citations, it is clearly stating what is fundamentally new: is it entropy as the trigger, adaptive partial rollout as the mechanism, shared-prefix advantage handling, or the particular combination of all three? Right now that boundary is blurrier than it should be.

## Questions
1. Please define the exact computation of \(\Delta H_t\) used in experiments. Is it a scalar or a \(k\)-dimensional vector before normalization? Why is the normalization divided by vocabulary size \(V\), given that token entropy in **Equation (1)** has already summed over the vocabulary? A precise formula here would materially increase my confidence.

2. In **Equation (2)**, is \(P_t\) actually a probability or just a branching score? If it is a probability, how do you ensure \(P_t \in [0,1]\)? If it is a score, please rename it and explain why thresholding the affine form \(\alpha+\beta\Delta H_t\) is the right design.

3. Can you provide an ablation that isolates the contribution of entropy-triggered branching from the contribution of simply doing partial rollout? Concretely, I would like to see at least:  
   - fixed branching after every tool call,  
   - random branching with matched branching rate,  
   - entropy-triggered branching without special advantage attribution,  
   - advantage attribution without entropy-triggered branching.  
   This would clarify whether entropy is truly the key signal.

4. The main theory currently reads more like a reparameterization of token-level autoregressive generation into macro-actions than a justification of ARPO itself. Can you clarify which formal claim you actually want the theory to support? For example, are you claiming unbiasedness of the estimator under branching, variance reduction, or only conceptual compatibility with policy gradients?

5. Please clarify the inconsistency between the importance ratio in **Equation (3)**, which uses \(\pi_{\mathrm{old}}\), and the ratios in Appendix F.2 (**Equations (12)-(13)**), which use \(\pi_{\mathrm{ref}}\). Is this a typo, or does the appendix analyze a different objective?

6. For the efficiency claim in **Figure 7(a)**, can you report matched-compute comparisons beyond tool calls, such as generated tokens per update, wall-clock time, or end-to-end training cost? This would strengthen the practical argument substantially.

7. For **Table 2**, can you provide more detail on the LLM-as-judge setup in the main paper, including prompt design, tie handling, and any calibration against exact-match or human evaluation on a subset? This would help assess how meaningful the observed margins are.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard concerns associated with training and evaluating web-search-capable LLM agents. The paper does not raise a distinct ethics issue that would require separate ethics review based on the information in the main text.

## Soundness Rating
2: fair. The empirical results are reasonably extensive and suggest the method is useful, but several core technical definitions and theoretical claims are not stated with enough precision for me to rate soundness higher.

## Presentation Rating
2: fair. The paper is readable overall and the figures are helpful, but there are multiple notation inconsistencies, under-specified equations, and some confusing algorithmic details.

## Contribution Rating
3: good. Despite my concerns, the paper addresses an important problem in agentic RL, proposes a plausible and practically relevant method, and shows broad empirical gains.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The empirical story is fairly strong and the problem is important, but the paper needs a much tighter treatment of the branching rule, advantage attribution, and theoretical claims.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with RL for LLMs and checked the main mathematical and experimental claims carefully, but some implementation details remain ambiguous in the paper.