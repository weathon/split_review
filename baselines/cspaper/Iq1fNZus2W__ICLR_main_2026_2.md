---
job_id: 8aecc80a-0d1a-47d6-8aa1-b015befb90c3
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Iq1fNZus2W.pdf
paper: Patch-Wise and Keyword-Aware: Efficient Multi-Condition Control of Diffusion Transformers via Position-Aligned and Keyword-Scope Attention
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies efficient conditioning mechanisms for diffusion transformers, which is a generative modeling and representation learning problem with methodological contributions and empirical evaluation on image generation.

## Minimum Quality
Pass ✅. The submission contains the core sections expected for a research paper, including Abstract, Introduction, Related Work, Method, Experiments, quantitative and qualitative results, and Conclusion. While I have significant concerns about empirical breadth, mathematical specificity, and positioning, these are review-level weaknesses rather than desk-reject-level omissions or fatal procedural flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies the inefficiency of the standard “concatenate-and-attend” strategy for multi-condition Diffusion Transformers and argues that much of the resulting cross-token attention is redundant. To address this, the authors propose Patch-Wise and Keyword-Aware Attention (PKA), which combines Position-Aligned Attention (PAA) for spatially aligned conditions and Keyword-Scoped Attention (KSA) for subject-driven conditions, together with an early-timestep sampling strategy for fine-tuning. Experiments on FLUX-based multi-condition generation report substantial runtime and VRAM savings, along with competitive or improved image quality and controllability relative to OminiControl2 and UniCombine.

## Strengths
1. The paper tackles a real bottleneck in DiT-based controllable generation. The motivating problem is important and timely, especially as multi-condition control becomes more common and transformer-based denoisers are increasingly used in place of UNets.

2. The central intuition is reasonable and, at a high level, well matched to the two condition types the paper studies. The distinction between spatial-aligned conditions and subject-driven conditions is helpful, and the proposed decomposition into PAA and KSA is easy to understand conceptually.

3. The paper includes useful visual motivation. In particular, **Figure 2** supports the claim that attention for spatial-aligned conditions is concentrated near aligned positions, and **Figure 3** gives an intuitive example that subject-related activations are localized rather than global. These figures do not fully prove the method is broadly valid, but they do make the proposed sparsification story more concrete.

4. The system-level design shown in **Figure 4** is one of the clearer parts of the paper. The decomposition into cached condition KV tensors, full text interaction, PAA for spatial conditions, and KSA for subject conditions is communicated effectively. Even though some implementation details remain underspecified, the architecture diagram helps the reader understand what is actually replaced relative to full attention.

5. The efficiency gains are meaningful. **Figures 7 and 8** show a clear and practically relevant reduction in latency and attention-module VRAM as the number of conditions grows. Assuming the measurement protocol is fair, this is the most convincing part of the experimental story.

6. The quantitative results in **Table 1** are reasonably strong on the selected tasks. The method improves FID and SSIM across all three tasks over both baselines, and it also improves the subject-consistency metrics where applicable. Even though the benchmark scope is limited, the improvements in the table are not merely cosmetic.

7. The paper also attempts to justify its training modification rather than presenting it as a heuristic with no motivation. **Figure 5** gives at least some empirical support for the claim that visual conditions matter more at earlier denoising stages, which provides a rationale for the proposed shifted timestep sampling.

## Weaknesses
1. **The empirical scope is too narrow for the paper’s breadth of claims.**  
   The paper repeatedly frames PKA as a general framework for “multi-condition control” in DiTs, but the actual evaluation in Section 4 is limited to three task combinations: Subject-Canny-to-Image, Subject-Depth-to-Image, and Canny-Depth-to-Image (**Page 6 to Page 8, Table 1**). These cover only two broad condition families used by the paper itself, spatial conditions via canny/depth and subject conditions via reference subject images. There is no evidence on other common control types such as segmentation/layout masks, pose, scribbles, style references, or more semantically entangled spatial constraints. This matters because the whole premise of the method is that different condition classes admit different structured sparsity patterns. If the tested condition set is narrow, it is hard to know whether the proposed decomposition is a generally useful design principle or just a good fit for the specific modalities selected here.

2. **The comparison against baselines is underpowered for a paper whose main selling point is efficient multi-condition DiT control.**  
   Section 4.1 compares only to OminiControl2 and UniCombine. These are relevant baselines, but the paper’s claims would be more convincing if it also included stronger or more diverse efficient-control baselines, particularly methods that use masking, pruning, condition injection, or KV/cache-based acceleration in related settings. As written, the paper mostly compares its structured sparsification against two end-to-end systems rather than isolating whether the proposed attention restriction itself is superior to simpler efficient alternatives. The ablations partly address this for PAA via sliding-window attention, but the overall baseline set is still too small for the scope of the claims.

3. **The mathematical specification of PAA is oversimplified to the point of ambiguity.**  
   In **Equation (2)** on **Page 4**,  
   \[
   PAA([X;SP])[i]=\mathrm{Softmax}\left(\frac{Q_{X_i}K_{SP_i}^{\top}}{\sqrt{d}}\right)V_{SP_i},
   \]
   the “one-to-one attention” formulation is not very coherent as written. If \(Q_{X_i}\) and \(K_{SP_i}\) correspond to a single aligned token pair, then \(Q_{X_i}K_{SP_i}^{\top}\) is effectively a scalar per head, so the softmax is either trivial or ill-defined unless there is an additional local neighborhood, channelwise set, or multi-token grouped structure that is not specified. The text says PAA computes attention only “between corresponding spatial positions,” which sounds more like gated cross-token modulation than attention over a nontrivial support. If the actual implementation attends over a local neighborhood or over multiple condition tokens per position, the equation should say so explicitly. This is not a cosmetic issue, because the claimed complexity reduction from \(\mathcal{O}(N^2)\) to \(\mathcal{O}(N)\) depends on the exact support size of the attention operator.

4. **KSA is also underspecified in key places, and the masking formulation is not precise enough for reproducibility.**  
   In **Equation (3)** on **Page 5**,  
   \[
   M^t=\mathrm{Norm}\left(\sum_{i\in\mathbb K}(Q_X^tK_i^{t\top})\right)\ge \epsilon,
   \]
   several details are missing. What exactly is \(\mathrm{Norm}(\cdot)\), min-max normalization, softmax over tokens, \(L_2\) normalization, or something else? Is \(M^t\) binary per token, per head, or per spatial position after head aggregation? How are multiword subjects mapped to the keyword set \(\mathbb K\)? Is \(\mathbb K\) manually selected, extracted from captions by heuristic rules, or inferred automatically? Since the method name explicitly includes “keyword-aware,” this selection mechanism is central, not peripheral. Without specifying keyword extraction and normalization, the KSA pipeline is not reproducible and may be brittle in ways the current experiments do not reveal.

5. **The temporal reuse assumption behind KSA is plausible but insufficiently validated.**  
   The method reuses the mask \(M^t\) at timestep \(t+1\), justified by “temporal consistency” on **Page 5**. However, no quantitative analysis is provided showing how stable these masks actually are across steps, nor how performance degrades when the subject region moves, expands, contracts, or is initially ambiguous under high noise. This matters because mask drift can create a feedback loop: if the mask misses the subject early, subsequent steps may permanently exclude relevant subject-conditioned attention. **Figure 10** only studies threshold \(\epsilon\), not the stability of the mask itself, and the examples shown are visually simple enough that this failure mode may not be triggered.

6. **The early-timestep sampling proposal is not disentangled sufficiently from the main method.**  
   Section 3.3 introduces a shifted logit-normal timestep sampling strategy with \(t\sim \text{Logit-}\mathcal N(\mu,\delta)\), motivated by **Figure 5**. But the evidence in the main paper is almost entirely qualitative, and the exact settings used in the final model are not integrated into the quantitative tables. **Figure 11** on **Page 9** is again visual. There is no table showing convergence speed, final metrics, or sensitivity to \((\mu,\delta)\) under the same protocol used in **Table 1**. As a result, it is difficult to tell whether early-timestep sampling is a substantive contributor to the final reported gains, a minor training trick, or a source of hidden tuning advantage over the baselines.

7. **The efficiency evaluation is incomplete and may overstate practical gains.**  
   The abstract and Section 4.2.1 emphasize up to \(10\times\) speedup and \(5.12\times\) VRAM reduction, but **Figure 8** is explicitly “VRAM consumption of attention mechanism” rather than end-to-end model memory. Similarly, latency measurements in **Figure 7** are helpful, yet the paper does not clearly state whether they include all denoising-step overheads, caching setup cost, mask generation cost, data movement, and kernel-launch effects. This distinction matters because the proposed method introduces extra control logic, cache handling, and masking operations. If the measured gain is primarily on the isolated attention submodule rather than the full generation pipeline, the headline savings may not transfer directly to deployment settings.

8. **The quantitative story in Table 1 is less clean than the text suggests.**  
   The paper says its controllability is “highly competitive” with only a minor exception, but in **Table 1** the **Subject Canny** task shows a nontrivial drop in edge F1 from **0.551** for UniCombine to **0.414** for the proposed method, while the gains are mostly in FID/SSIM and subject consistency. That is not a tiny difference. If the method deliberately trades off spatial controllability for better image realism or subject preservation, that is fine, but the paper should say so clearly and analyze it. Right now the prose on **Page 8** somewhat smooths over an actual tradeoff that deserves discussion.

9. **The paper’s qualitative evidence is suggestive but not strong enough to support some of the stronger claims.**  
   **Figure 6** is used to argue superior visual quality over OminiControl2 and UniCombine, and the examples do look favorable to the proposed method. However, the visual comparisons are cherry-pickable by nature, and the paper does not include failure cases, prompt conflicts, or examples where conditions disagree. The method should be stress-tested on deliberately conflicting subject and spatial conditions, because the proposed hard restrictions in PAA and KSA are precisely the kind of design that may behave poorly when constraints are inconsistent or when the correct region is not obvious.

10. **The literature positioning is somewhat incomplete for the specific technical angle taken here.**  
    The related work covers controllable diffusion and efficient DiTs broadly, but it is thinner on methods that use masked attention, position-aware condition injection, or alternative efficient control designs in DiTs and closely adjacent architectures. Since the paper’s contribution is not just “efficiency” in general but a condition-structured restriction of attention, the discussion should more carefully differentiate what is new relative to prior masked-attention or condition-routing approaches. As written, the positioning is somewhat broad-brush.

11. **Training and evaluation details are too sparse for a method paper centered on efficiency and control fidelity.**  
    On **Page 6**, the training setup states 20,000 LoRA fine-tuning iterations with batch size 1 and accumulation 4, but essential details are omitted or unclear: image resolution, number of denoising steps at inference, exact FLUX variant, LoRA target modules, number of seeds used for reported metrics, whether all methods were tuned comparably, and how keyword-containing captions were selected when curating the Subject200K subset. These are not secondary details. Since the proposed method depends directly on token structure, timestep behavior, and caption keywords, reproducibility hinges on this information.

12. **Some claims are stronger than what the evidence currently supports.**  
    The abstract says PKA provides a “practical path towards complex, fine-grained, and resource-friendly AI generation,” and the conclusion suggests it is a promising foundation for even more complex generative tasks. That may be directionally true, but the evidence in the main paper supports a narrower claim: the method appears effective on a limited set of two-condition combinations under one FLUX-based fine-tuning setup. The paper would be stronger if it calibrated its claims to that scope instead of selling a more general story than the experiments justify.

## Questions
1. For **Equation (2)**, what is the exact support over which the softmax is computed? If PAA truly uses only one aligned token pair \((X_i, SP_i)\), the attention distribution is degenerate. Please clarify whether the actual implementation uses a local neighborhood, multiple heads with nontrivial support, or another formulation. A corrected equation and complexity derivation would substantially increase my confidence.

2. For **Equation (3)**, please define \(\mathrm{Norm}(\cdot)\) precisely and explain how the keyword set \(\mathbb K\) is obtained. Is keyword extraction manual, rule-based, parser-based, or learned? How robust is KSA when the subject phrase spans multiple tokens or when the caption contains multiple candidate entities?

3. Can the authors provide a quantitative ablation table, not only visual comparisons, separating the contributions of PAA, KSA, KV caching, and early-timestep sampling? Right now, the paper mixes several ideas, and it is hard to tell which component is responsible for which gains.

4. Can the authors report end-to-end memory and latency, not only attention-module VRAM, under a fixed image resolution and fixed number of denoising steps? This would make the practical significance of **Figures 7 and 8** much clearer.

5. On **Table 1**, how should readers interpret the sizable drop in F1 on the Subject-Canny task relative to UniCombine? Is this a systematic tradeoff between subject fidelity and edge adherence? A short analysis of when PKA hurts controllability would improve the paper.

6. How does the method behave under conflicting or weakly aligned conditions, for example when the subject reference suggests one pose or scale while the spatial condition suggests another? This seems especially important for PAA, since forcing one-to-one position alignment may be brittle under imperfect correspondence.

7. The paper argues generality over increasing numbers of conditions, but the main quantitative tasks appear limited to pairs of conditions. Can the authors provide quantitative, not only supplementary qualitative, evaluation with three or four simultaneous conditions?

8. What are the exact hyperparameters used for the shifted timestep sampling in the final model, and were these tuned on a validation set shared fairly across methods? A compact sensitivity study over \(\mu\) and \(\delta\) with quantitative metrics would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics-specific concerns are apparent from the main paper. The work is a methodological efficiency paper for controllable image generation, and the submission does not describe human-subject experiments, sensitive private data collection, or a new dataset release requiring special review.

## Soundness Rating
2: fair. The core intuition is plausible and some empirical evidence is convincing, especially on efficiency, but important mathematical details are underspecified and the experimental validation is not broad enough to fully support the generality of the claims.

## Presentation Rating
3: good. The paper is generally readable and the figures are useful, especially **Figures 2, 3, 4, 7, and 8**, but several equations and implementation details are too vague for a method paper, and some claims are stated more strongly than the evidence warrants.

## Contribution Rating
2: fair. The paper addresses an important problem and proposes a sensible structured-attention idea, but the current evidence suggests a promising but still somewhat narrow contribution rather than a fully established advance for general multi-condition DiTs.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The efficiency angle is meaningful and the paper has a decent core idea, but the current version does not quite clear the bar for ICLR because the method specification is too loose in key equations, the empirical coverage is too limited for the scope of the claims, and some important tradeoffs are insufficiently analyzed.

## Reviewer Confidence
4: confident. I am familiar with diffusion-transformer conditioning methods and efficient attention design, and I checked the main equations, tables, and figures carefully. My main uncertainty is not about the general direction, but about whether the omitted implementation details would resolve some of the technical ambiguities.