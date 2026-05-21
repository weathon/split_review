---
job_id: 357a6c0a-c10f-41a8-a7c5-1e111e00ac1d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ei1bRG971A.pdf
paper: DND: Boosting Large Language Models with Dynamic Nested Depth
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it proposes an adaptive-computation method for transformer-based language models, with direct relevance to representation learning, efficient inference, and large-scale ML systems.

## Minimum Quality
Pass ✅. The paper contains the expected core sections, presents a concrete method with equations, figures, ablations, and quantitative evaluation, and while I have several concerns about novelty, clarity, and experimental conclusiveness, these are not fatal flaws warranting desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, manipulative prompts, or suspicious content targeting automated reviewers in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes Dynamic Nested Depth (DND), a post-training method for LLMs that identifies supposedly critical tokens at selected transformer layers, reprocesses only those tokens through the same layer, and fuses the nested output back into the vanilla hidden states. The method combines a token-level router, a hard threshold-based selection rule, a fusion mechanism, and two training components, namely a router-control loss and a threshold-control scheme, and is evaluated on several 1B-scale dense models and one 30B-A3B MoE model.

## Strengths
The paper has a clear central idea, namely spending additional depth only on selected tokens rather than uniformly increasing computation. This is a sensible direction for adaptive computation in autoregressive LLMs, and the post-training framing is practically attractive because it targets already-pretrained models instead of requiring a fresh pretraining run.

I appreciated that the paper is not purely conceptual, it gives an implementable design with explicit routing, packing/unpacking, and fusion equations in Section 3. In particular, **Figure 2** is useful for communicating the end-to-end mechanism: vanilla pass, token selection, nested pass with shared weights, and gated fusion. Even though I have questions about some design details, the diagram makes the operational flow understandable.

The empirical coverage is broader than many papers in this niche. **Table 1** evaluates three different dense 1B-ish backbones, and the gains are reasonably consistent across those families. That cross-model consistency is a real plus. Likewise, **Table 2** shows that the method is not restricted to small dense models, and the 30B-A3B MoE experiment makes the paper more relevant to the ICLR audience than a purely toy-scale study would.

The paper does include useful ablations rather than just headline numbers. **Table 4** is particularly helpful because it separates the effects of router control, threshold control, token-selection ratio, and layer placement. The fact that the full setup outperforms either control mechanism alone does support the claim that these components are complementary, at least empirically.

I also found the training-dynamics visualizations informative. **Figure 5** and **Figure 6a/6b** provide at least some evidence that the threshold-control scheme and router loss are doing something concrete during training, rather than being decorative add-ons. Those figures strengthen the story that DND is as much about stabilizing token selection as about adding extra depth.

The overhead story is reasonably compelling. The paper reports small parameter increase and moderate speed degradation in **Table 3**, and the FLOPs estimate is at least directionally aligned with the throughput measurements. For a post-training method, that practicality matters.

## Weaknesses
1. **The novelty is narrower than the paper suggests, and the positioning against the closest prior work is not sharp enough.**  
   The core recipe here, select tokens, give them extra computation, then merge back, is quite close in spirit to the recent line around adaptive token-level depth/routing, including the papers the authors themselves identify as closest, especially ITT and MOR in Section 2.2. The claimed distinction is mostly post-training compatibility and a different control mechanism for token selection. That can still be publishable, but the paper oversells the conceptual gap a bit. The difference from prior dynamic-depth approaches feels more like an engineering refinement plus a practical training recipe than a genuinely different modeling principle. This matters because the contribution should then be judged on very solid empirical evidence and careful comparisons, but those are not always strong enough.

2. **The empirical gains, especially on the larger model, are fairly modest, and the paper does not establish whether they are statistically reliable.**  
   On the small dense models in **Table 1**, the average gains of +1.88, +2.61, and +2.50 are respectable. On the 30B-A3B model in **Table 2**, however, the average gain is only +0.87, and many task-level improvements are tiny, for example +0.13 on BBH, +0.15 on MATH, +0.20 on MATH-500, +0.27 on DROP, +0.37 on CMMLU. For a post-training method that changes computation and routing behavior, this is exactly where I would want variance across seeds, confidence intervals, or at least repeated runs on the largest model. Without that, it is hard to tell whether some of these deltas reflect a stable effect or just normal evaluation noise. This matters because the paper’s main claim is that DND “boosts” strong LLMs broadly, and the largest-model evidence is numerically quite thin.

3. **The comparison set is weaker than it should be for isolating the source of improvement.**  
   The most obvious issue is that ITT appears in **Table 1** only for Qwen3-1.7B, not for Llama3.2-1B, Gemma3-1B, or the 30B-A3B model. That makes it difficult to assess whether DND’s advantage over prior token-recursion approaches generalizes beyond one backbone. More importantly, the paper is missing simpler but crucial controls:  
   - uniform extra-depth on all tokens for a matched compute budget,  
   - random-token reprocessing at the same ratio,  
   - entropy-based token selection without a learned router,  
   - perhaps a cheap heuristic selection baseline tied to uncertainty.  
   These are not cosmetic baselines. They are necessary to demonstrate that the gain comes from the specific learned routing and nested design, rather than just “a bit more compute on some subset of tokens” or regularization effects from the modified architecture.

4. **There are important mathematical and notational inconsistencies in the core training objective, and some of them are not minor typos because they obscure what is actually optimized.**  
   In **Equation (6)**, the summation runs from \(l=\mathbf{L}_s\) to \(\mathbf{L}_c\), whereas the architecture section defines the DND-applied layer range as \(\mathbf{L}_s\) to \(\mathbf{L}_e\). It is unclear whether \(\mathbf{L}_c\) is a typo for \(\mathbf{L}_e\) or a different endpoint. In **Equation (7)**, the indices are written as \(\sum_{l=\mathbf{L}_i}^{L_l}\), which is not consistent with the rest of the paper and is mathematically ill-defined as written. Then in **Table 4**, the router-control row refers to “\(\mathcal{L}_{ui}\) and \(\mathcal{L}_{dp}\)”, while the method section defines \(\mathcal{L}_{sd}\) and \(\mathcal{L}_{dp}\). These are not isolated typography issues, because they make it harder to know which exact objective generated the reported ablations.

   There is also a more substantive concern with **Equation (6)** itself. The score-dispersion loss normalizes the sequence-level router outputs as \(p^{\prime,i,(l)} = p^{i,(l)}/\sum_j p^{j,(l)}\) and then maximizes entropy of that normalized distribution. But maximizing entropy in this form tends to encourage a *uniform distribution over tokens*, not necessarily a distribution with strong separation around the threshold \(\tau\). That is not the same thing as making token scores more discriminative for hard selection. In fact, if the raw \(p^i\) values become more equal, the normalized entropy increases. The paper verbally claims the loss “pushes the score distribution towards diversity,” but the mathematical objective as written does not obviously match that interpretation. This deserves a much more careful explanation.

5. **The routing/training story leaves a major missing link, namely how gradients reach the router under hard thresholding and packing.**  
   The method defines a binary mask in **Equation (2)** with \(m^i = \mathbf{1}[p^i > \tau]\), and then the nested computation in **Equation (3)** depends on \(\operatorname{Pack}(\mathbf{X}_v,\mathbf{M})\). This operation is non-differentiable with respect to the router decisions. The paper says the router loss is jointly optimized with cross-entropy, but it never explains whether the language-model loss backpropagates through the discrete selection using a straight-through estimator, whether gradients to the router come only from \(\mathcal{L}_{router}\), or whether the pack/unpack path is treated as detached. Since the central claim is that the router learns to select “critical” tokens for useful extra computation, this is not a side detail. If the LM objective does not meaningfully supervise routing, then DND is closer to a hand-controlled gating mechanism than the paper implies.

6. **The treatment of positional information in the nested pass is underspecified and potentially problematic for causal LLMs.**  
   In **Equation (3)**, selected tokens are packed into a compact subsequence, given new positional embeddings \(\mathbf{E}'_{\text{pos}}\), and then reprocessed. This raises several questions the paper does not answer: are these positions reset to local packed indices, remapped from original absolute positions, or adapted for RoPE-style positional encoding? For autoregressive transformers, positional handling is not a minor implementation footnote. If packed tokens are re-indexed, the attention geometry in the nested pass changes. If original positions are preserved, then the “compact sequence” formulation needs more explanation. **Figure 2** visually suggests a clean nested pass, but it hides this exact ambiguity. Since many modern LLMs use RoPE rather than additive learned positional embeddings, the notation \(\mathbf{E}'_{\text{pos}}\) is itself suspiciously generic here.

7. **The experimental protocol does not cleanly isolate DND from the effects of full-parameter SFT.**  
   Section 4.2 states that all parameters are trainable and the method is applied during standard full-scale SFT. That means the reported improvements come from jointly changing both architecture and fine-tuning dynamics. A post-training method can certainly be evaluated this way, but then the claim that the gains are due to DND specifically becomes somewhat confounded. For example, did the baseline and DND models use the same total training FLOPs and the same number of optimization steps? Was the baseline given a matched budget with a slightly longer SFT run? If not, DND may partly benefit from extra compute during training rather than only from better inference-time allocation. This is especially relevant because the paper repeatedly emphasizes efficiency.

8. **Some of the qualitative analysis is interesting but not yet convincing as scientific evidence.**  
   **Figure 4a** shows a positive relationship between token selection count and vanilla logit entropy, and **Figure 4b** shows decreasing entropy differences for more frequently selected tokens. These plots are suggestive, but they do not establish causality, and the interpretation is a bit too eager. High entropy could correlate with many things besides “criticality,” including ambiguity, poor calibration, or tokenization artifacts. Similarly, **Figure 7b** provides a visually appealing token heatmap, but it remains anecdotal. The paper could be stronger if it quantified selection behavior across token categories, positions, or syntactic roles, instead of relying on one or two examples and verbal interpretation.

9. **Presentation quality is uneven, and a few errors reduce confidence more than they should in a method paper.**  
   There are repeated notation slips and terminology inconsistencies, for example \(\mathbf{L}_e\) versus \(\mathbf{L}_c\), \(\mathbf{L}_i\) versus \(L_l\), “lunet(%)” in **Table 4**, and the mismatch between the text and table labels for router losses. The references section also looks messy in places. Normally I would not dwell on cosmetic issues, but in a paper whose main contribution is a carefully engineered routing-and-control mechanism, notation precision matters. Right now the exposition is good enough to get the broad idea, but not polished enough to inspire full confidence in the exact implementation details.

## Questions
1. **How exactly does the LM loss supervise the router?**  
   Please clarify the gradient path through **Equations (2)-(3)**. Is there any straight-through estimator, surrogate gradient, or soft routing used during training, or does the router receive gradients only from \(\mathcal{L}_{router}\)? A precise answer here would materially increase my confidence.

2. **What positional encoding is actually used in the nested pass?**  
   In **Equation (3)**, what is \(\mathbf{E}'_{\text{pos}}\) for models that use RoPE or related positional schemes? Are original token positions preserved, compressed, or reset after packing? Please explain the exact implementation and why it does not distort causal structure.

3. **Can the authors provide variance estimates or repeated runs, especially for the 30B-A3B results in Table 2?**  
   Since many of the gains are below one point, even a small multi-seed study on a representative subset of tasks would help establish robustness.

4. **Can the authors add compute-matched control baselines?**  
   The most useful additional comparisons would be: random-token reprocessing, uncertainty/entropy-based heuristic token selection, and uniform extra depth under a similar compute budget. These would substantially clarify how much of the gain comes from the learned router versus just extra computation.

5. **Please reconcile the notation and objective mismatches.**  
   Specifically, please correct and explain the layer-index inconsistencies in **Equations (6)-(7)**, the \(\mathcal{L}_{sd}\) versus \(\mathcal{L}_{ui}\) naming discrepancy in **Table 4**, and why maximizing entropy of the normalized router scores in **Equation (6)** should be expected to improve threshold-based discriminability.

6. **How is training compute controlled relative to the baseline?**  
   If DND models are trained with more per-step FLOPs, did the baseline receive a matched training budget in any experiment? If not, the paper should be more careful in attributing all gains purely to the architectural idea.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the submission. The work is a systems/methods paper on adaptive computation in LLMs and does not introduce a new dataset involving sensitive human subjects, nor does it directly raise privacy, fairness, or safety issues beyond the standard risks associated with stronger language models.

## Soundness Rating
3: good. The method is plausible and supported by multi-model experiments and ablations, but there are important unresolved issues around the routing objective, gradient flow through hard selection, and the lack of robustness estimates for modest gains.

## Presentation Rating
2: fair. The high-level story is understandable and some figures are helpful, especially Figure 2 and the training-dynamics plots, but the paper has too many notation inconsistencies and underspecified implementation details for a cleaner score.

## Contribution Rating
2: fair. The paper offers a useful practical variant of token-adaptive extra depth for LLMs, but the conceptual novelty is incremental and the empirical margin over simpler alternatives is not yet established strongly enough.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a practical idea, decent empirical breadth, and enough positive evidence that I can see it making the cut, especially as a method paper focused on post-training compatibility. That said, the novelty is incremental, several technical details are underspecified, and the experimental story needs stronger controls and better rigor to fully justify the paper’s claims.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the adaptive-computation / transformer-routing literature, though some implementation details are underspecified enough that I cannot verify every technical aspect with complete certainty.