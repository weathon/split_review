---
job_id: 0fea60af-9694-498c-bc02-26e0ec62c8ed
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ZZFNyU3ZSo.pdf
paper: UniMoD: Efficient Unified Multimodal Transformers with Mixture-of-Depths
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on efficient training of unified multimodal transformers via token pruning and conditional computation for representation learning and generative modeling.

## Minimum Quality
Pass ✅. The submission includes the expected scientific components, namely abstract, introduction, related work, methodology, experiments with quantitative results, and conclusion; despite several methodological and clarity issues, it clears the minimum bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, instructions targeting automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies token redundancy in unified multimodal transformers and argues that a single Mixture-of-Depths router is not well suited when generation and understanding tasks have different redundancy patterns. Based on empirical analyses of attention weights, ARank across layers/tasks, and a task-competition setup, the authors propose UniMoD, a task-aware MoD variant with separate routers and task-specific pruning on selected layers. Experiments on Show-o and Emu3 report reduced training FLOPs, roughly 15% on Show-o and 40% on Emu3, while largely maintaining benchmark performance on multimodal understanding and text-to-image generation.

## Strengths
The paper tackles a practically relevant problem. Unified multimodal models are expensive to train, and efficiency methods specifically tailored to them are still limited. Applying token-level conditional computation in a task-aware way is a reasonable direction, and the paper focuses on training-time efficiency rather than only inference tricks.

The empirical motivation is more substantial than in many efficiency papers. The authors do not simply insert MoD blocks and report speedups, they first attempt to characterize differences across tasks and layers. In particular, **Figure 2** is useful in illustrating that token attention behavior differs across tasks for several unified models, especially Show-o, JanusFlow, and Emu3. Even though the interpretation can be sharpened, the figure does support the broader claim that “one pruning policy for everything” is likely too crude.

The method itself is easy to understand at a high level. **Figure 5** gives a reasonably clear picture of the three block types, T2I-MoD, MMU-MoD, and Shared-MoD, and how the layer switch module injects them into a standard unified transformer. For an efficiency paper, this kind of architectural transparency matters.

The main results are promising. In **Table 3**, UniMoD is much stronger than the two simple efficiency baselines on Show-o. For example, compared with Interleaved Layer and EarlyExit, UniMoD preserves generation quality far better, especially on GenEval and DSG, while still reducing TFLOPs from 51.1 to 43.3. On Emu3, the reduction from 89.0 to 53.5 TFLOPs is substantial, and the generation metrics even improve slightly. This is the strongest empirical point in the paper.

The ablation in **Table 5** is also helpful. It suggests that naively inserting MoD is not enough, and that both the layer selection and task-aware routing contribute. In particular, the huge gap in GenEval between Basic MoD (0.15) and UniMoD (0.61) indicates that the pruning placement and task separation matter a lot for generation stability.

The paper is relevant to the ICLR audience because it sits at the intersection of multimodal representation learning, sparse computation, and scalable training of foundation models.

## Weaknesses
1. **The core novelty is somewhat narrow, and the paper does not position that limitation sharply enough.**  
   At a method level, UniMoD is essentially MoD plus task-specific routers plus a heuristic layer-selection scheme based on ARank. That can still be publishable if the empirical case is strong, but the manuscript sometimes overstates the conceptual leap, especially in the contribution bullets on **Pages 2-3**. The method is a targeted adaptation of existing token-pruning ideas rather than a clearly new pruning principle. This matters because for ICLR, incremental systems work typically needs either stronger evidence of broad generality or much cleaner methodological insight than what is currently provided.

2. **The empirical analysis is interesting but not yet convincing enough as the causal basis for the method design.**  
   The paper presents five “observations” in Sections **3.2-3.4**, but the chain from those observations to the final design still feels looser than the narrative suggests. For example, **Figure 2** shows average attention received by text/image tokens, but it does not directly demonstrate that separate routers are necessary, only that attention statistics differ. Likewise, **Figure 3** shows ARank differences across tasks and layers, but the jump from “ARank differs” to “use per-task routers and these specific MoD placements” is heuristic rather than tightly validated. The paper would be stronger if it showed that alternative explanations, such as per-layer capacity tuning without per-task routing, fail systematically. Right now, the evidence is suggestive, not decisive.

3. **The mathematical presentation around the objectives and routers is sloppy in ways that make the method harder to trust than it should be.**  
   There are multiple notation issues in **Equations (2)-(4)**. In **Equation (4)** on **Page 7**, the text says “\(D_t(x_i)\) is the task-specific router function” and also says “\(D_t(\cdot)\) is the corresponding routing function and \(R_t(x_i)\) is the task-specific weight,” which conflicts with the notation in **Equation (2)** where \(D^l\) is clearly the transformer block and \(R^l\) is the router. This is not a cosmetic issue, because the exact semantics of the routing score, threshold, and residual update define the method. Similarly, the thresholded form in **Equations (2)** and **(4)** suggests hard routing, while the actual implementation later says the router “retains the Top-K tokens with the highest scores” in Section **4.1**. Thresholding and top-\(K\) routing are not equivalent unless \(\delta_t^l\) is defined implicitly by the \(K\)-th score. The paper should write the actual optimization and forwarding rule explicitly, for example with a selected index set \(S_t^l = \operatorname{TopK}(R_t^l(x^l), K_t^l)\), then define the layer update only on \(i \in S_t^l\). As written, the core mechanism is underspecified.

4. **ARank is used as a central design signal, but its definition and interpretation are not sufficiently justified.**  
   In **Equation (3)** on **Page 5**, ARank is defined as the mean rank of \(A_h = (x^lW_{Qh})(x^lW_{Kh})^\top\), before the softmax normalization usually associated with attention maps. That is already a nonstandard proxy for redundancy, and the paper does not explain why the rank of this pre-softmax bilinear score matrix is a reliable estimator of token informativeness in unified multimodal settings. More importantly, the text says “Higher ARank values indicate lower sequence redundancy” in **Figure 3**, and later “a low ARank means that most of its tokens are less informative,” but the connection between matrix rank and token-level pruneability is asserted rather than validated. Since ARank drives both layer selection and pruning ratio estimation in Section **4.1**, this gap matters materially.

5. **The pruning-ratio estimation is very heuristic and not well specified enough for reproducibility.**  
   In Section **4.1** on **Page 7**, the authors say they “approximate each layer's pruning ratio by normalizing its ARank score by the sequence length.” That leaves several missing details: what exact normalization formula is used, how ratios are clipped, whether task-specific ratios are smoothed across layers, how this is adapted when sequence lengths differ between tasks, and whether image/text token counts are handled jointly or separately. This is one of the main algorithmic ingredients, yet it is described in one sentence. A paper about compute-performance tradeoffs needs this part to be nailed down, not hand-waved.

6. **The baselines are too weak for the central empirical claim.**  
   The main comparison in **Table 3** is against Full Computation, EarlyExit, and Interleaved Layer. These are simple baselines, but they are not the most relevant alternatives once the paper is framed as a token-pruning / MoD paper. The ablation in **Table 5** includes “Basic MoD” and “w/o task-aware router,” which is useful, but this is not the same as a careful head-to-head against a strong generic MoD adaptation with tuned capacities and tuned layer placement. In other words, the strongest baseline is relegated to an ablation rather than promoted to the main table. Given that the core claim is “task-aware routing matters,” the main results table should include the best non-task-aware MoD competitor with equal tuning effort.

7. **The gains on Show-o are modest and the metric tradeoff is less clean than the prose suggests.**  
   On **Table 3**, UniMoD reduces Show-o TFLOPs from 51.1 to 43.3, which is useful but not dramatic. At the same time, some understanding metrics drop, such as GQA from 56.3 to 54.5 and VQAv2 from 68.3 to 66.2. The paper emphasizes “maintaining or improving performance,” but for Show-o the result is closer to “preserving some metrics while sacrificing others modestly for a moderate compute reduction.” That is still acceptable, but the current wording oversells the consistency of the improvement.

8. **The Emu3 evaluation is hard to interpret because the training setup differs materially from the original model, and the paper relies on this model for one of its strongest efficiency claims.**  
   Section **5.1** states that official MMU training resources are unavailable, so the authors use LLaVA-v1.5-mix-665K and add MMU-specific code. Section **5.2** further notes that full Emu3 results differ from the original paper because of alternative training datasets. This is understandable, but it weakens the evidential value of the Emu3 result. If the dataset mixture and training code are materially different, it becomes harder to know whether the 40% FLOP reduction would hold under the original unified training recipe. This is a generalization concern, not a fatal flaw, but it lowers confidence in the breadth of the conclusion.

9. **The analysis of layer importance is too narrow to support the design rule used later.**  
   Observation 2 in Section **3.3** is based on skipping odd-numbered layers in Show-o and inspecting GQA performance in **Table 1**. First, this is only one task and one benchmark. Second, some values are odd enough to raise questions, for example layer 3 gives GQA = 0.0, while neighboring layers are not catastrophic. That may be correct, but such an extreme outlier demands explanation. Third, the method later uses ARank-based layer selection, not the skip-one-layer importance test. So the role of **Table 1** in the argument is unclear. It reads more like anecdotal evidence than a principled basis for the final design.

10. **The task-competition experiment is intriguing but underdeveloped.**  
    **Figure 4** shows that generation tokens tend to receive weight 1 more often than understanding tokens in the competitive setup. But this experiment introduces a bespoke router capacity of 0.5 plus a Gumbel-Softmax formulation described only in the appendix. It is not obvious that this competition setup faithfully reflects the actual UniMoD routing regime. In other words, the figure may reveal something about one artificial bottleneck experiment rather than about the behavior of the deployed method. Since Observation 5 is used to motivate task-specific pruning, the paper needs to clarify why this competition result should be taken as more than an illustrative curiosity.

11. **The clarity and consistency of exposition need work.**  
    There are many small but cumulative issues: “Mixture of Depths” is written as both singular and plural; “Show-o” and “Show-o*” are used without immediate clarification in **Table 2**; “UniMod” and “UniMoD” both appear in **Table 4**; some sections use “sequence redundancy” and others “token redundancy” interchangeably without defining the distinction; and there are several grammatical problems that obscure meaning. None of these alone is fatal, but together they reduce confidence, especially in a paper that depends on subtle routing details.

12. **The evidence for scalability beyond two tasks is too weak in the main paper.**  
    The paper claims in Section **5.2** that the method “naturally extends beyond two tasks,” but the actual support is deferred outside the main body. Since task-awareness is the headline idea, the lack of main-paper evidence for more than two tasks limits the generality of the contribution. The same applies to adaptation to pure diffusion models, which is potentially interesting but outside the main paper’s core evidence.

13. **Some claims about memory and speed are plausible but under-analyzed.**  
    **Table 4** reports fairly small iteration-time reductions for Show-o, 1.30s to 1.25-1.27s, despite nontrivial TFLOP reductions. That is believable because wall-clock speed does not scale linearly with FLOPs, but the paper’s discussion is too brief. Since the title emphasizes efficiency, a clearer decomposition of where the practical savings do and do not materialize would improve the paper’s utility.

## Questions
1. Please provide the exact routing rule used in training and inference. Is routing implemented by a hard threshold \(R_t^l(x_i^l) \ge \delta_t^l\), by top-\(K\) selection, or by a soft relaxation during training followed by top-\(K\) at evaluation? Right now **Equations (2)** and **(4)** do not match the prose in Section **4.1**.

2. Please specify the exact formula that maps ARank to the per-layer keep ratio \(K_t^l\) or pruning ratio. A concrete expression would materially improve reproducibility and would let readers judge whether the gains come from ARank itself or simply from hand-tuned sparsity schedules.

3. Can you add a stronger non-task-aware MoD baseline to the main results, not only in the ablation table, with equal tuning budget and optimized layer placement/capacity? This would directly test whether task-aware routing is truly the key ingredient.

4. For **Table 1**, why does skipping layer 3 produce GQA = 0.0 while adjacent layers are far less destructive? Is that a typo, a benchmark failure, or a real model pathology? This number is so extreme that it needs explanation.

5. How sensitive are the results to the sample count used to compute ARank, namely 50 MMU samples and 20 T2I prompts according to **Page 17**? If the selected layers change substantially with a different sample subset, the layer switch module may be less robust than implied.

6. Can you clarify whether the separate routers require explicit task labels at training and inference time? If so, how would UniMoD handle mixed or compositional prompts where task boundaries are ambiguous?

7. For Show-o in **Table 3**, the method improves MME and POPE but drops GQA and VQAv2. What is the authors’ best explanation for this uneven effect across MMU benchmarks? A more granular error analysis could change my confidence.

8. The Emu3 setup differs from the original due to unavailable training resources. Can you clarify how much of the reported advantage might depend on the substitute MMU data mixture rather than on the routing mechanism?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work is an efficiency method for multimodal model training and does not introduce a new dataset release, human subjects component, or an obviously high-risk application beyond the usual concerns associated with large multimodal generative models.

## Soundness Rating
2: fair. The paper is technically plausible and supported by several experiments, but the central methodological details around routing and ARank-based ratio selection are underspecified, and some core claims rely on heuristic analyses rather than tightly controlled evidence.

## Presentation Rating
2: fair. The overall story is understandable and the figures are helpful, especially **Figures 2** and **5**, but the notation, equation-to-text consistency, and several important algorithmic details need substantial clarification.

## Contribution Rating
2: fair. The paper addresses an important practical problem and reports useful efficiency gains, but the conceptual advance over existing MoD-style pruning is moderate, and the empirical case is not yet broad or rigorous enough for a stronger score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and practically relevant, and the Show-o/Emu3 results suggest the idea has merit. However, the current version leaves too many important details heuristic or underspecified, relies on relatively weak baselines for its strongest claims, and does not yet make a sufficiently tight scientific case that the task-aware design, rather than careful tuning of standard MoD, is the true source of the gains.

## Reviewer Confidence
4: confident. I am familiar with multimodal transformers, token pruning, and sparse conditional computation, and I checked the main equations, figures, and tables carefully.