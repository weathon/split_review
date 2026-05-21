---
job_id: 2ac34f4a-6e3c-404c-a5d3-9ea01cc0f179
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 36CzrZYEch.pdf
paper: IRIS: Intrinsic Reward Image Synthesis
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining reinforcement learning, intrinsic rewards, uncertainty-related signals, and autoregressive text-to-image generation.

## Minimum Quality
Pass ✅. The submission contains the necessary components, including abstract, introduction, related work, method, experiments, quantitative results, and conclusion, and it presents a nontrivial empirical study rather than a trivial repackaging.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies reinforcement learning for autoregressive text-to-image generation without external reward models, using an intrinsic reward based on the model’s own token-level uncertainty. The main proposal, IRIS, applies GRPO to maximize negative self-certainty, defined from the forward KL between a uniform distribution and the model output distribution, over both text and image tokens. Empirically, the paper reports that, for Janus-Pro models, decreasing self-certainty improves image generation quality relative to the base model and can approach the performance of RL training with external rewards on GenEval, T2I-CompBench, and WISE.

## Strengths
- The paper asks a meaningful question: whether autoregressive T2I models can be post-trained with RL using only intrinsic signals, avoiding the cost and domain dependence of external reward models. That is a worthwhile direction for the community.

- The core empirical observation is interesting and somewhat counterintuitive relative to the recent LLM literature on self-certainty. In particular, **Figure 2** is useful because it juxtaposes the trend for language reasoning and T2I: self-certainty increases for the text model under external-reward RL, while it decreases for Janus-Pro under image-generation RL. Even though the analysis is still mostly empirical, this figure does communicate the paper’s main intuition clearly.

- The method is simple to state and easy to implement on top of standard RL fine-tuning. Using a token-level intrinsic reward instead of a learned reward model is practically appealing.

- The ablation section is better than what many papers in this area provide. **Figures 6, 7, and 8** directly test key design choices, namely whether to maximize or minimize self-certainty on image tokens, whether to do the same on text tokens, and whether forward KL is preferable to entropy-based backward KL. This is the right kind of empirical decomposition for a paper making a reward-design claim.

- There are real gains over the base model. In **Table 1(a-c)**, IRIS improves substantially over vanilla Janus-Pro-1B on all three benchmarks, for example from 0.66 to 0.72 on GenEval, from 0.3338 to 0.3793 on T2I-CompBench, and from 0.28 to 0.37 on WISE. So the method is not a null result.

- I also appreciate the authors’ note in **Page 6, Section 4.1** about the Janus vs. Janus-Pro chat-template mismatch in prior implementation. That kind of implementation hygiene matters for a fair comparison.

## Weaknesses
- **The paper overstates its comparative results against external-reward RL.** The abstract says IRIS is “competitive with or superior to external rewards,” and the introduction/main-results framing strongly suggests parity or better. But the main quantitative evidence in **Table 1** does not really support the “superior” part, and even “competitive” is mixed. For both 1B and 7B models, IRIS is below T2I-R1 in overall score on all three benchmarks shown in the main paper:  
  - **GenEval**: 1B, 0.72 vs 0.75; 7B, 0.77 vs 0.78  
  - **T2I-CompBench**: 1B, 0.3793 vs 0.3820; 7B, 0.3916 vs 0.3992  
  - **WISE**: 1B, 0.37 vs 0.38; 7B, 0.48 vs 0.50  
  This is not a trivial wording issue. The difference between “improves the base model substantially” and “matches or beats external rewards” is exactly the difference between an interesting empirical observation and a stronger alignment claim. Right now the results support the former more than the latter.

- **There is an experimental selection problem that materially weakens the validity of the reported headline numbers.** On **Page 6**, the paper states that **Table 1** reports “the best result of different methods among the checkpoints from 100 step to 800 step on the three benchmarks,” and on **Page 7** the caption states “We report the scores of the best checkpoint (measured by the average performance) of the T2I-R1 and IRIS.” This appears to mean the paper selects checkpoints using the test benchmarks themselves. That is effectively test-set model selection. Without a separate validation protocol, the reported best-checkpoint numbers are optimistic and not strictly comparable as unbiased test estimates. This is a serious issue, not bookkeeping. It affects the central claims because the claimed competitiveness of IRIS depends on these selected best numbers.

- **The mathematical formulation of the reward is sloppy in a way that obscures what is actually optimized.** In **Equation (2)**, the paper defines
  \[
  \mathrm{SC}(o_t \mid q,o_{<t}) := \mathrm{KL}\!\left(U \,\|\, \pi_\theta(o_t \mid q,o_{<t})\right),
  \]
  but \(\pi_\theta(o_t \mid q,o_{<t})\) is written like the probability of the sampled token \(o_t\), while KL requires a full distribution over the vocabulary. The intended object is presumably
  \[
  \mathrm{KL}\!\left(U \,\|\, \pi_\theta(\cdot \mid q,o_{<t})\right)
  = \sum_{v \in \mathcal V} U(v)\log\frac{U(v)}{\pi_\theta(v \mid q,o_{<t})}.
  \]
  This distinction matters. As written, the reward is not mathematically well-typed. The same ambiguity recurs in the GRPO objective, where token-level rewards are summed over sampled trajectories, but the reward itself depends on the whole predictive distribution at each prefix, not on the chosen token in the standard bandit sense. If the authors want to claim a token-level intrinsic reward, they need to write the reward as a function of the distribution explicitly and explain the credit assignment carefully.

- **Equation (1) is also malformed / underspecified.** The paper writes
  \[
  \max_{\pi_\theta}\mathbb{E}_{o\sim\pi_\theta(\cdot|q)}\left[r(o|q)-\beta\mathrm{KL}(\pi_{\theta}(o|q))\|\pi_{\mathrm{ref}}(o|q)\right],
  \]
  which is not a valid KL expression. It seems the intended term is either \(\mathrm{KL}(\pi_\theta(\cdot|q)\|\pi_{\rm ref}(\cdot|q))\) at the sequence level, or the usual tokenwise KL regularizer. This may look cosmetic, but in an RL paper the exact regularized objective matters.

- **The theoretical/motivational explanation for forward KL vs. entropy is hand-wavy and not convincingly tied to the actual T2I setting.** On **Page 4**, the paper states that forward KL to uniform “encourages mode-covering behavior,” while backward KL / entropy is “mode-seeking,” and from this concludes that forward KL is a better measure of self-certainty. That is too loose. Entropy maximization is not “mode-seeking” in the ordinary sense, and the comparison between \(\mathrm{KL}(U\|\pi)\) and \(\mathrm{KL}(\pi\|U)\) needs a more careful argument in the finite vocabulary autoregressive setting. Since this distinction is central to IRIS, the current explanation is not sufficient. **Figure 8** shows that forward KL works better empirically in their setup, but the text overreaches on the theoretical interpretation.

- **The evidence for the paper’s broader claims about “reasoning” and “general” capability enhancement is thinner than advertised.** The paper repeatedly claims that IRIS “enhances the reasoning capabilities of T2I models” and that intrinsic rewards incentivize “general T2I abilities” (**Pages 3, 6, and 8**). But the evidence in the main paper is still limited to one model family, one architecture class, one RL algorithm, and three benchmark suites. The semantic-CoT analysis in **Figure 4** is anecdotal, showing one qualitative example, and does not establish that the improvement truly comes from better reasoning rather than from a generic diversity effect or a prompt-formatting artifact. If the reasoning claim is important, the paper should separate “better exploration / diversity” from “better reasoning / planning” much more carefully.

- **The ablation evaluation protocol is not as clean as the paper suggests.** In **Section 4.3**, all ablations are evaluated by averaging four external reward models, namely HPSv2, DINO, GIT, and ORM. The paper argues these are “simple and unbiased metrics” because they are not used in IRIS training. But that is only half true. These metrics are exactly the reward models used to train the external-reward baseline in **Section 4.1**, so they are not neutral with respect to the broader comparative story. This matters especially because the paper uses those curves in **Figures 5-9** to justify design choices and then generalizes from them to claims about image quality and alignment. External-reward metrics are acceptable as proxies, but calling them “unbiased” is too strong.

- **Some qualitative evidence is suggestive but not fully convincing.** **Figure 1** is visually appealing and does support the paper’s intuition that self-certainty can produce overly plain images. Still, it is a cherry-picked figure with three prompts and one image per condition. It does not rule out the possibility that the negative self-certainty setting is simply increasing diversity at the cost of consistency. Likewise, **Figure 4** claims that semantic CoTs improve image generation, but the evidence is one bicycle example, and the figure does not quantify whether the textual intermediate actually becomes more faithful, more informative, or merely longer. In a paper making strong causal claims about intrinsic reward and reasoning, the qualitative analysis should be less anecdotal.

## Questions
1. The main-results table appears to use benchmark performance to choose the “best checkpoint.” Can the authors clarify whether any held-out validation set or validation prompts were used for model selection? If not, could they report fixed-step comparisons, or selection based only on training-time signals, to avoid test-set tuning?

2. Please rewrite **Equation (2)** using the full predictive distribution, e.g.
   \[
   \mathrm{SC}_t(q,o_{<t})=\mathrm{KL}(U\|\pi_\theta(\cdot\mid q,o_{<t})).
   \]
   As written, the notation conflates a sampled token with a distribution. Also, how exactly is this tokenwise reward attached to sampled actions in GRPO, given that the reward depends on the full distribution at each prefix?

3. For **Equation (1)** and the GRPO objective on **Pages 4-5**, can the authors specify the exact KL regularization used in implementation, sequence-level or token-level? The current notation is not mathematically correct enough to reproduce.

4. Since **Table 1** shows IRIS below T2I-R1 on all three overall benchmark scores, can the authors moderate the claims in the abstract and introduction, or provide stronger evidence for “competitive with or superior to external rewards”? For example, a pre-registered human preference evaluation in the main paper would help.

5. The paper attributes gains partly to improved semantic CoT reasoning. Can the authors provide a more direct analysis of this mechanism, such as measuring CoT length, diversity, object coverage, relation coverage, or agreement between CoT content and final image quality? Right now **Figure 4** is too anecdotal to support a strong mechanism claim.

6. Can the authors report robustness across seeds and prompt subsets for the main comparisons? The standard deviations in **Table 1** are small for some metrics, but the checkpoint-selection issue makes it hard to know how stable the conclusions really are.

7. A useful clarification would be whether IRIS is mainly increasing exploration/diversity or actually improving alignment. If the authors can report diversity metrics, prompt faithfulness metrics, and human preference side by side, that would make the paper’s central claim much sharper.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper improves text-to-image generation systems and explicitly discusses RL post-training for these models. Even though the paper is methodological and does not involve human subjects, stronger image-generation capability can obviously be misused for deceptive or harmful content, including misleading synthetic imagery. The ethics statement on **Pages 10-11** acknowledges deepfake-style misuse in general terms, which is good, but the work still falls into the category of potentially harmful generative-model capability advancement.

## Soundness Rating
2: fair. The empirical signal is interesting and the experiments are nontrivial, but the paper has a serious model-selection problem, and the mathematical description of the reward/objective is not precise enough.

## Presentation Rating
2: fair. The paper is readable overall, and the figures help, but the notation around the objective and reward is sloppy, some claims are overstated relative to the results, and several core points need sharper exposition.

## Contribution Rating
2: fair. The idea of intrinsic-reward RL for autoregressive T2I is interesting and relevant, but the evidence does not yet support the strongest claims, and the current execution falls short of what I would want for ICLR main track.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has an interesting empirical finding and a promising direction, but the current version overclaims, uses test benchmarks for checkpoint selection, and does not present the reward/objective with enough mathematical precision for me to recommend acceptance.

## Reviewer Confidence
4: confident. I am familiar with RL post-training and multimodal generation, and I checked the main technical and experimental claims carefully, though I did not independently verify implementation details.