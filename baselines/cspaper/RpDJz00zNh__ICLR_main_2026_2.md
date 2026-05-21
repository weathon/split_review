---
job_id: 41b0060d-4c57-47df-8db3-5fc4a3055ed6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: RpDJz00zNh.pdf
paper: ConciSeHint: Boosting Efficient Reasoning via Continuous Concise Hints during Generation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on efficient reasoning in large language models, test-time intervention during generation, and empirical evaluation on standard reasoning benchmarks.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including Abstract, Introduction, Related Work, Method, Experiments, quantitative results, ablations, and Conclusion. While I have substantial concerns about novelty, experimental rigor, and some methodological claims, these do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, concealed instructions targeting automated reviewers, or other obvious manipulation attempts in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes **ConciseHint**, a test-time framework for reducing reasoning verbosity in large reasoning models by repeatedly injecting a concise hint during generation. The method uses a hand-written or learned hint, adapts the injection interval based on the current generated length via Equation (1), and adjusts the injection position within each chunk via Equation (3). The paper evaluates the approach on Qwen and DeepSeek models across GSM8K, AIME24, and GPQA-Diamond, and also studies a trained variant, **ConciseHint-T**, based on learned hint embeddings.

## Strengths
The paper targets a timely and practically relevant problem, namely reducing the token and latency overhead of long chain-of-thought style reasoning in current LRMs. The framing of "in-reasoning intervention" is easy to grasp and differs in style from the more common prompt-only or fine-tuning-only approaches discussed in Section 2.

I found the high-level presentation intuitive. **Figure 1** is effective at communicating the paper’s central contrast, namely pre-reasoning control versus intervention during reasoning. **Figure 2** also helps the reader understand the generate-inject-repeat loop and the distinction between manual hints and learned hint embeddings. Even though I have concerns about the underlying rigor, the core mechanism is easy to visualize, which is a real strength for a systems-style test-time method.

The empirical results do show that the method often reduces output length substantially. In **Table 1**, the token savings relative to the unmodified original reasoning are frequently large, sometimes roughly halving token usage or more, and the plug-in nature of the method is supported by the “Ours (baseline)” rows. This compatibility angle is one of the more convincing aspects of the paper. The ablation in **Table 3** is also useful: it supports the claim that strong fixed intervention can damage performance on harder tasks, while adaptive scheduling is less brittle.

The learned-hint extension, ConciseHint-T, is reasonably motivated. **Table 2** and **Figure 3** suggest a controllable tradeoff between token usage and accuracy through the interpolation parameter $\gamma$. Even though I am not fully convinced by the generalization claims, the controllability story is at least supported by the monotonic trend in token reduction shown in the plots.

The paper also deserves credit for going beyond accuracy-only reporting. The discussion around latency and prefilling cost, especially the visualization in **Figure 5** and the empirical latency analysis in the appendix figures, indicates that the authors are thinking about actual deployment cost rather than just token count.

## Weaknesses
1. **The method is simple to the point that the paper overstates its conceptual contribution, and the novelty relative to existing test-time control methods is not convincingly established.**  
   The core algorithm in **Algorithm 1** is: generate $\tau_k$ tokens, splice in a short “be concise” style hint, append the modified text back into the context, and repeat. The adaptive part is then a linear heuristic for interval growth in **Equation (1)** and a hand-crafted position rule in **Equation (3)**. This is easy to understand, but the paper presents it as filling a largely unexplored gap, and that claim feels stronger than what is substantiated in the paper itself. The distinction from prompt-based control is true in a literal sense, but mechanically this is still repeated prompting at test time, just injected into the evolving context rather than only prepended once.  
   Why this matters: for an ICLR main-track paper, the bar is not just “works to some extent” but whether the method advances understanding or capability in a nontrivial way. Here, the contribution currently reads as a useful heuristic rather than a sufficiently deep new method, and the paper does not do enough to convince the reader otherwise.

2. **The central adaptivity claim is weakly justified because query complexity is never actually estimated; it is replaced by current generated length, which is endogenous to the intervention itself.**  
   In **Page 4, Equation (1)**, the injection interval is defined as
   $$
   \tau_k = \alpha + \beta l_k,\quad \alpha>0,\beta>0.
   $$
   The paper interprets $l_k$ as a complexity indicator. But $l_k$ is just the current generated length, and generated length is not an exogenous property of the query. It is affected by the model, the sampling configuration, and by the very intervention being applied. Once hints shorten or redirect the reasoning, the “complexity estimate” is no longer a stable estimate of task difficulty, it is a moving byproduct of the policy. This creates a circularity: the controller uses generation length to infer complexity, while generation length is itself changed by the controller.  
   The paper acknowledges a “prior” that length correlates with complexity, but that is much weaker than validating that this surrogate is appropriate here. **Table 3** only shows that fixed intervals can be worse on harder benchmarks; it does not validate that within a benchmark, the adaptive schedule actually tracks per-instance difficulty.  
   Why this matters: the paper repeatedly markets the method as complexity-adaptive, but the evidence supports at best a length-adaptive heuristic. That is a materially weaker claim.

3. **Several mathematical formulations are underspecified or inconsistent with the actual implementation described.**  
   There are multiple issues here:
   - In **Equation (2)** on Page 5,
     $$
     T' = T[0:p] + T_{\text{hint}} + T[p:\tau_k-1],\;\; p\in[0,\tau_k-1],
     $$
     the notation mixes token indexing and substring slicing loosely, and it assumes $T$ has length exactly $\tau_k$. But **Algorithm 1, line 4** uses `max_token_len = \tau_k`, which is an upper bound, not a guarantee that exactly $\tau_k$ tokens are produced. If generation stops early, then indexing to $\tau_k-1$ is not correct. The paper later checks `finish_reason`, which implies early stopping is possible.
   - In **Algorithm 1**, the update
     $$
     l_k = l_k + \tau_k
     $$
     on line 8 is also questionable for the same reason. If the model generates fewer than $\tau_k$ tokens in the final chunk, the update is inaccurate. Strictly speaking, it should depend on the actual generated length, say $|T|$, not the requested cap $\tau_k$.
   - In **Equation (3)**,
     $$
     p=\tau_k * \min((\tau_k-\alpha)/1024,\;0.8),
     $$
     $p$ is treated as a position index, but the formula yields a real value. The paper never specifies the rounding convention, floor/ceil behavior, or how non-integer positions are handled in token-level slicing.  
   These are not cosmetic complaints. The method itself is defined through token-level edits and scheduling, so ambiguity in token counts and indices directly affects reproducibility and even the meaning of the algorithm.

4. **The learned-hint training procedure, ConciseHint-T, is insufficiently specified and scientifically weakly validated.**  
   The description on **Page 5-6** says the authors inject trainable hint embeddings into responses at a fixed interval, initialize them from the manual hint embeddings, and optimize them with next-token prediction on concise reasoning data. But several key details are missing:
   - What exactly is the length of the trainable hint, in tokens or embedding slots?
   - Are all model parameters frozen, as in standard prompt tuning, or is any layer norm / embedding block updated?
   - At training time, are hints inserted into gold concise traces, model-generated traces, or some hybrid?
   - How is the training interval chosen, and is it the same as test time?
   - If the concise dataset is built from GSM8K-style reasoning, why should the learned embeddings encode a domain-general “conciseness pattern” rather than benchmark-specific stylistic artifacts?
   
   The evidence in **Table 2** is also less persuasive than the text suggests. Training on MixChain-Z-GSM8K and then evaluating on AIME24 and GPQA-Diamond gives mixed results. For example, at $\gamma=1.0$, token usage drops further, but accuracy declines nontrivially, especially on GPQA-Diamond. The paper frames this as evidence that the embeddings have “effectively captured concise patterns” and “generalize well to out-of-domain data,” but those are stronger claims than the numbers justify.  
   Why this matters: ConciseHint-T is one of the headline additions over the training-free method, yet the training protocol and generalization story are not fleshed out enough to support strong conclusions.

5. **The empirical evaluation is incomplete for the paper’s core claims, particularly regarding fairness of comparisons and robustness.**  
   The baselines in **Section 4.1** are representative, but not comprehensive enough for the paper’s positioning. The paper’s story is about efficiency-accuracy tradeoffs in reasoning models, especially adaptive control. Yet the main tables do not compare against a broader set of adaptive reasoning-budget methods or stronger recent training-based compression methods in the main paper. Appendix comparisons are not enough to rescue this, because the main paper should carry the burden of demonstrating the method’s standing.  
   There is also a fairness issue in how the paper compares train-free and training-based methods. ConciseHint-T is trained, but the main comparison table is dominated by training-free baselines. Then the learned variant is only shown on **Qwen3-1.7B** in **Table 2**, on one concise-training source. This makes it hard to understand whether the gains come from the intervention mechanism or from access to additional supervision.  
   Why this matters: without stronger apples-to-apples comparisons, it is difficult to place the true contribution of the method relative to the literature the paper is trying to join.

6. **The results tables reveal a more fragile accuracy story than the narrative admits.**  
   The paper repeatedly says it maintains performance well, but **Table 1** is more mixed than that. A few examples:
   - On **Qwen3-8B / GPQA-Diamond**, `Prompt` has 57.58 accuracy and `Ours (Prompt)` drops to 55.56 while reducing tokens from 6285 to 3880. That is not negligible, especially on a 198-question benchmark where a couple of percentage points are meaningful.
   - On **DeepSeek-R1-14B / AIME24**, `Ori.` is 63.00 while `Ours (Ori)` drops to 61.00 with token savings. That tradeoff may still be acceptable, but again it weakens the blanket claim of preserving performance “well.”
   - On **Qwen3-4B / GPQA-Diamond**, `BeConcise` actually has higher accuracy than `Ours (Ori)` despite higher token count.
   
   The problem is not that tradeoffs exist. The problem is that the text selectively highlights friendly examples and tends to blur the cost side of the tradeoff. The paper would be stronger if it explicitly characterized when the method is safe and when it is not.  
   Relatedly, the paper reports averages over multiple runs, but there are no standard deviations, confidence intervals, or statistical tests in **Table 1-5**. For AIME24 especially, with only 30 problems, small score changes are noisy.  
   Why this matters: the scientific conclusion should be calibrated to the evidence. Right now the prose is a bit too triumphant relative to the observed variability.

7. **The ablation on injection position is not fully convincing and contains internal tension with the claimed compute-accuracy tradeoff.**  
   In **Table 4**, injecting “At the head” on GPQA-Diamond gives **higher accuracy** (58.95) than the dynamic strategy (55.56), and even slightly **lower token usage** (3798 vs 3880). The paper argues that head injection increases computing a lot due to prefilling, which may be true for latency, but the main paper table here reports token usage, not latency. In token terms, the dynamic strategy is not clearly preferable.  
   The paper’s defense is shifted to appendix latency analysis, but in the main paper the reader is shown a table where the proposed dynamic rule does not appear superior on the reported metrics. This weakens the claim that the specific hand-crafted formula in **Equation (3)** is “essential.” At best, it looks like one reasonable heuristic among several.  
   Why this matters: Equation (3) is one of the paper’s core methodological ingredients, but the evidence presented in the main paper does not strongly justify that exact design.

8. **The paper does not adequately disentangle token savings caused by direct text insertion from genuine changes in model reasoning behavior.**  
   In **Figure 5** and the appendix latency discussion, the authors note that injected hint tokens appear immediately rather than being decoded token-by-token. More broadly, the method edits the visible context that the model conditions on. This raises a simple but important question: how much of the measured token reduction comes from steering the reasoning policy toward conciseness, and how much comes from changing the transcript format, suppressing continuations, or truncating reflective loops?  
   **Table 5** shows fewer transition words such as “wait” and “alternatively,” which the paper interprets as removing redundant self-reflection. That may be true, but it may also mean suppressing potentially useful correction steps. The paper does not provide a deeper error analysis to distinguish “less redundancy” from “less recovery from mistakes.”  
   Why this matters: the claimed mechanism is not just “shorter output,” but more efficient reasoning. The current evidence does not fully separate these interpretations.

9. **The exposition has noticeable sloppiness in terminology, notation, and claims.**  
   A few examples:
   - The paper sometimes says “complexity-adaptive,” sometimes effectively means “length-adaptive.”
   - **Algorithm 1** uses API-like pseudocode that is not mathematically tight and includes spelling issues such as “inverval.”
   - The paper says “The detailed theoretical and empirical analysis for injection costs can be found at Section A.2,” but the so-called theoretical analysis is largely an engineering latency decomposition rather than theory in the usual ML sense.
   - Claims like “we find it always works well for various models and benchmarks” on **Page 4** are too sweeping given the limited benchmark/model grid and visible tradeoffs.
   
   None of these alone would sink the paper, but together they make the work feel less mature than it should for ICLR.

10. **The main-paper evidence for real-world efficiency is thinner than the headline suggests.**  
   The paper motivates the work heavily in terms of compute and latency, but the main body reports mostly token counts. The actual end-to-end latency evidence is deferred to the appendix. Because the method modifies context repeatedly, latency is not trivially proportional to output tokens, especially given the prefilling/recomputation discussed around **Figure 5**.  
   If real efficiency is a main claim, the main paper should present latency and perhaps cost curves alongside token counts, not only in supplementary material. This matters especially because **Table 4** already hints that the compute tradeoff cannot be inferred from tokens alone.

## Questions
1. The main conceptual claim is that the method is **complexity-adaptive**, but **Equation (1)** uses current generated length $l_k$ as the sole complexity signal. Can the authors provide evidence, in the rebuttal, that per-instance $l_k$ correlates with true task difficulty in a way that is not merely induced by the intervention itself? For example, correlation with an external difficulty proxy, or a comparison to a classifier-based difficulty estimate, would materially increase my confidence.

2. Please clarify the exact token-level semantics of **Equation (2)** and **Algorithm 1**. If the model stops before producing $\tau_k$ tokens, should the update be
   $$
   l_{k+1} = l_k + |T|
   $$
   rather than $l_k + \tau_k$? Also, how is the real-valued position from **Equation (3)** converted into an integer token index?

3. For **ConciseHint-T**, please specify the training protocol in enough detail to be reproducible: hint length, frozen versus trainable parameters, insertion interval at training time, optimizer, number of steps, and whether training traces are gold concise traces or model outputs. This is currently too underspecified.

4. Can the authors provide stronger evidence that the learned hints capture a domain-general conciseness behavior rather than benchmark-specific style from MixChain-Z-GSM8K? For example, evaluating learned hints trained on one domain and tested across several others, or comparing to random/untuned soft prompts of the same length, would help.

5. The claims around preserving accuracy would be more convincing with uncertainty estimates. Can the authors report standard deviations or confidence intervals for **Table 1-4**, especially on AIME24 and GPQA-Diamond, where benchmark sizes are small?

6. The dynamic position rule in **Equation (3)** is presented as essential, but in **Table 4** injecting at the head gives better accuracy and slightly fewer output tokens than the dynamic rule. Could the authors clarify whether the real advantage is solely latency, and if so, provide those latency numbers in the main paper rather than only appendix discussion?

7. A stronger error analysis would help. Among the cases where ConciseHint hurts accuracy, are failures primarily due to premature stopping, suppressed self-correction, wrong final extraction, or repetition artifacts after injection? The case studies in **Figure 8** hint at these modes, but a systematic breakdown would make the contribution more scientifically informative.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the main paper. The work studies efficiency interventions for language-model reasoning and does not introduce an obviously sensitive dataset, human-subject protocol, or high-risk deployment claim in the main text.

## Soundness Rating
2: fair. The core empirical effect, token reduction, is demonstrated, but several methodological claims are stronger than what the evidence supports, and key parts of the algorithm and trained variant are underspecified.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures help, but there are important ambiguities in notation, indexing, and claim calibration that weaken clarity.

## Contribution Rating
2: fair. The paper explores a practically relevant direction and may be useful as a heuristic, but the conceptual advance over repeated test-time prompting/control is modest, and the evidence does not yet support the stronger framing.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has an interesting and practically useful idea, and the token savings are real, but the current submission overclaims adaptivity, lacks sufficient rigor in the algorithmic formulation and experimental validation, and does not yet make a strong enough scientific case for ICLR main track.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and carefully checked the main methodological and empirical claims, though some uncertainty remains because several implementation details of the trained variant are not fully specified.