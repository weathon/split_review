Now I have a thorough understanding of the paper. Let me construct the consolidated review.

---

## Summary

This paper proposes DAM (Dynamic Adapter Merging), a rehearsal-free method for domain-incremental video question-answering (VidQA) learning. DAM trains domain-specific adapters sequentially on a frozen video-language backbone, then at inference uses a non-parametric router to compute instance-level adapter relevance scores, and dynamically merges the top-*k* adapters via weighted averaging to produce the final prediction. Experiments across six VidQA datasets show a 9.1% improvement over S-Prompts with 1.9% less forgetting, and the method extends to image VQA using BLIP-2. The core insight—that merging compensates for inaccurate router predictions—is supported by targeted analysis.

## Strengths

1. **9.1% accuracy improvement with 1.9% less forgetting (Table 1).** DAM outperforms the best prior prompt-based method (S-Prompts) across six sequentially trained VidQA datasets. This is the paper's central empirical claim and is directly supported by the reported results.

2. **Dynamic merging demonstrably compensates for router inaccuracy (Table 3, Figure 4).** When router accuracy is low (e.g., 51.0% on MSVD), adapter merging yields a 4.9% downstream accuracy gain; Figure 4 shows a 30% relative improvement when router accuracy drops to 0%. This provides concrete evidence that the method's core mechanism works as claimed and gives practical insight into *when* merging helps.

3. **Non-parametric router is simpler yet more effective than learned alternatives (Table 2).** The proposed centroid-based router achieves the best downstream VidQA accuracy despite being simpler than the trainable routers in L2P, CODA-Prompt, and S-Prompts, which are shown to cause optimization stability issues in this setting.

4. **Scalable across varying numbers of domains (Figure 3).** DAM consistently outperforms S-Prompts when the number of trained domains is varied from 2 to 6, with in-domain gains of 1.7%–4.8% and out-of-domain gains of 2.9%–7.1%, showing robustness in realistic multi-domain scenarios.

5. **Extends to image VQA with a 4.1B-parameter model (Table 4).** DAM applied to BLIP-2 for continual VQA outperforms S-Prompts, demonstrating generalization beyond video-level tasks.

6. **Parameter-efficient design (Section 3.1).** Adapters contain less than 5% of total backbone parameters, enabling integration with billion-parameter models like FrozenBiLM (1.2B) and BLIP-2 (4.1B) with minimal overhead.

## Weaknesses

### Fatal
None.

### Major

1. **Adaptation of prompt-based baselines is underspecified, leaving potential fairness concerns.** The paper states that prompts are "prepended to their existing tokens as was done in (Wang et al., 2022b)." However, the FrozenBiLM backbone has both a CLIP ViT visual encoder and a DeBERTa language encoder. It is unclear whether prompt tokens are inserted into the visual stream, the text stream, or both. Prompt placement significantly affects expressivity in vision-language models, and since the paper's headline 9.1% improvement depends on this comparison, the current description is insufficient. This is not evidence of an unfair comparison, but the omission prevents readers from verifying the fairness of the reimplementation.

2. **OOD evaluation mechanism is not explained.** Section 4.2 and Figure 3 evaluate DAM on domains never seen during training, reporting that DAM outperforms S-Prompts by 2.9%–7.1% on these OOD domains. The paper does not clarify what mechanism enables the frozen backbone plus seen-domain adapters to produce meaningful answers for questions about unseen domains. The frozen backbone (FrozenBiLM) presumably has some zero-shot VidQA capability from pretraining, but this is never quantified or acknowledged. Without this grounding, it is unclear whether the OOD results reflect genuine cross-domain knowledge transfer or simply backbone-level zero-shot performance. The OOD analysis can remain valuable if the paper explains the underlying mechanism and reports the backbone's standalone zero-shot accuracy as a reference baseline. (The comparison against S-Prompts remains valid since both use the same backbone—the concern is about interpretability of the absolute results, not about unfairness.)

3. **Missing adapter architecture and centroid computation details undermine reproducibility.** Several specifics are absent: (a) The number of adapters *N* per domain is introduced symbolically but never numerically specified—are there two adapters per transformer layer (after self-attention and after FFN, as implied by Section 3.1) or more? (b) The adapter bottleneck dimension is not reported. (c) The centroid computation (Section 3.2) averages features from the training data of each domain, but since this is a rehearsal-free setting, it is unclear how these centroids are computed without storing raw data (e.g., incremental averaging during training). These are architectural and algorithmic design choices, not trivial hyperparameters, and they must be specified for the method to be reproducible.

### Minor

1. **Inconsistency in reported VQA extension results.** Table 4's caption states that DAM outperforms S-Prompts by **4.8%** top-1 accuracy, while the body text (Section 4.5, line 156) reports **4.4%**. This discrepancy must be resolved.

2. **Temperature hyperparameter is not ablated.** The router uses τ = 0.01, producing a highly peaked softmax. No sensitivity analysis is provided to justify this choice or show how performance varies with τ.

3. **Forgetting metric not explicitly defined.** The paper cites (Wang et al., 2022c;b) for the evaluation metrics, but the specific definition of "forgetting" used in Tables 1 and 4 should be stated explicitly rather than left to be inferred from citations, especially since the paper introduces multiple comparisons.

4. **"Cannot calculate" entry for CODA-Prompt router accuracy (Table 2) is unexplained.** The paper states that CODA-Prompt's router accuracy cannot be calculated "as it does not explicitly predict the domain identity," but does not explain how CODA-Prompt was adapted for VidQA if it lacks domain identification. A brief description of the adaptation would clarify this.

### Trivial

None beyond the formatting artifacts that are parser-related.

## Nice-to-Haves

- **Ablate the continual initialization scheme**: Compare adapters initialized via the continual scheme vs. randomly initialized per domain to validate the claim that weight inheritance smooths the parameter space and aids merging.
- **Report standard deviations**: Results are averaged over 5 runs, but no error bars are shown in Tables 1–4. Given variability in continual learning, this would strengthen the evaluation.
- **Quantify the gap to full-model fine-tuning**: The upper bound (Ind-FT) uses individually fine-tuned adapters, not full-model fine-tuning. Reporting the gap to full-model fine-tuning would contextualize the parameter-efficiency trade-off.
- **Report training/inference overhead**: The method is described as efficient, but wall-clock time or FLOPs for the router and merging are not reported.

## Removed Points

*These points were flagged by reviewers but removed from the main review with brief justification:*

- **"Barbie movie example is dated"**: A presentational observation about the example year being 2023 while the review is in 2026. This is a formatting/presentation nitpick that has no bearing on technical merit. **Removed per Hard Rule 5 (formatting/style nitpicks).**
- **"Paper does not situate method within adapter-based CL literature (Houlsby et al., 2019)"**: The paper's related work section covers prompt-based DIL methods, model merging, and rehearsal-based VQA-CL approaches. Adapter-based continual learning is a broad area; the paper's contribution is specifically about *dynamic merging* of adapters for VidQA, not about proposing a new adapter architecture. The omission of a general adapter-CL survey does not weaken the paper's positioning. **Removed as scope creep.**
- **"Missing related works" (general)**: Per Hard Rule 4, missing related works cannot be flagged as weaknesses. **Removed.**
- **"First to explore domain-incremental VidQA learning is slightly overstated because VQACL and CLCrossVQA exist"**: The paper explicitly states these are *rehearsal-based* methods for *image* VQA (Section 2). The claim is "first to explore domain-incremental *VidQA* learning" which is distinct. **Removed as factually incorrect reading of the paper.**

## Novel Insights

None beyond the paper's own contributions. The harsh critic's concern about the OOD evaluation mechanism is well-taken, and the strength finder's identification of the merging-vs-router-accuracy relationship (Table 3, Figure 4) as the paper's most insightful finding is accurate. These are contributions the paper itself makes, not insights that emerge from the reviews.

## Suggestions

1. Clarify where prompt tokens are inserted (visual stream, text stream, or both) in the FrozenBiLM backbone and justify why this adaptation is faithful to the original methods.
2. Explain the mechanism behind OOD performance: quantify the frozen backbone's zero-shot VidQA accuracy as a reference, or explicitly state that OOD results measure cross-domain transfer from similar seen domains.
3. Specify the adapter architecture: define *N* numerically, state the bottleneck dimension, and explain how centroids are computed without data storage (or note that centroids are computed once during training by accumulating feature means).
4. Resolve the 4.4% vs. 4.8% discrepancy in the VQA extension.
5. Add a sensitivity analysis or justification for the temperature τ = 0.01.

## Score and Decision

Originality: Good — first systematic exploration of domain-incremental VidQA learning with a novel merging mechanism.  
Importance of research question: High — continual learning for large video-language models is practically relevant.  
Claims well-supported: Mostly yes, but the fairness of the 9.1% comparison needs clarification.  
Soundness of experiments: Solid ID evaluation; OOD evaluation needs explanation.  
Clarity of writing: Generally clear; missing details on architecture and adaptation hurt reproducibility.  
Value to community: Potentially high, especially the router-vs-merging analysis.

MY FINAL SCORE: <score>7.5</score>  
MY FINAL DECISION: <decision>Accept</decision>