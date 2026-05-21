---
job_id: c07456c7-23af-492b-a6ba-9df49fc2eb22
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ey7CXUBn1g.pdf
paper: AdaSVD: Adaptive Singular Value Decomposition for Large Language Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on post-training compression of large language models via low-rank factorization, with methodological contributions in optimization and representation-efficient deployment.

## Minimum Quality
Pass ✅. The submission includes the expected core components, namely Abstract, Introduction, Related Work, Method, Experiments with quantitative and qualitative results, and Conclusion. While there are notable clarity and methodological issues, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious text targeting automated review systems in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes AdaSVD, a post-training SVD-based compression method for LLMs/VLMs with two main components: adaComp, which alternates updates of the low-rank factors after truncation to reduce output reconstruction error on calibration data, and adaCR, which assigns layer-specific compression ratios based on a simple importance score derived from input-output similarity. The paper evaluates the approach on several 7B-scale language models and one vision-language model setting, comparing mainly against SVD, FWSVD, ASVD, and SVD-LLM.

## Strengths
The paper tackles a relevant practical problem. Post-training compression of LLMs remains important, and improving the accuracy-memory tradeoff of SVD-based methods is a reasonable direction, especially because these methods are hardware-friendly relative to some sparse or custom-kernel approaches.

The empirical gains over the strongest baseline, SVD-LLM, are often non-trivial at higher compression ratios. In **Table 1** on LLaMA2-7B, the improvements at 60% compression are substantial on perplexity, for example WikiText-2 improves from 89.90 to 50.33 and C4 from 561.00 to 239.18. Even if some downstream accuracy gains are modest, this does support the paper’s core claim that the method is particularly useful in harder compression regimes.

The cross-model comparison in **Table 2** is useful. It shows the method on OPT-6.7B, LLaMA2-7B, Mistral-7B, and Vicuna-7B under the same 60% compression setting, and AdaSVD consistently improves over SVD-LLM. This at least suggests the method is not overfit to one architecture family.

The ablations in **Table 3** are directionally helpful. In particular, **Table 3(a)** and **Table 3(b)** separate the effect of adaComp and adaCR, and the gains from adaComp appear to be the larger contributor. That decomposition is important, since otherwise the paper would read like a bundle of tricks without evidence about which part matters.

I also appreciated that the paper includes some qualitative illustrations rather than relying only on numbers. **Figure 3(c)**, although informal, attempts to visualize how the output distribution of the compressed model moves closer to that of the original model after alternating updates. **Figure 5** gives qualitative VLM examples where AdaSVD captions are clearly more coherent than vanilla SVD and often better than SVD-LLM, which helps the reader understand what the compression degradation looks like in practice.

The high-level presentation of the pipeline in **Figure 2** is effective. It makes the decomposition into truncation, stack-of-batch calibration, adaptive rank assignment, and alternating compensation much easier to parse than the text alone.

## Weaknesses
I have substantial concerns. The paper is interesting, but in its current form it falls short of ICLR standard on technical precision, methodological justification, and positioning.

1. **The mathematical formulation around the alternating updates is not fully consistent, and some equations appear underspecified or dimensionally questionable.**  
   The most serious issue is the transition from the objective in **Equation (5)**,
   \[
   \min_{U_k^\sigma, V_k^{\sigma\top}} \|U_k^\sigma V_k^{\sigma\top}X - WX\|_F^2,
   \]
   to the stated update for \(V_k^{\sigma\top}\) in **Equation (7)** and again in **Equation (13)**. If the objective depends on \(X\), then the normal equations for optimizing \(V_k^{\sigma\top}\) should generally also involve \(X\), for example through terms like \(XX^\top\), unless the problem is reformulated in a different variable. Yet **Equation (7)** gives
   \[
   V_k^{\sigma\top} = \left((U_k^\sigma)^\top U_k^\sigma\right)^{-1}(U_k^\sigma)^\top W,
   \]
   which corresponds more naturally to minimizing \(\|U_k^\sigma V_k^{\sigma\top} - W\|_F^2\), not \(\|U_k^\sigma V_k^{\sigma\top}X - WX\|_F^2\). The same issue carries into **Equation (13)**. This matters because these equations define the core optimization step of adaComp. If the update being implemented is not actually the minimizer of the stated objective, then the main methodological claim is weaker than presented.

2. **The paper repeatedly suggests convergence or stable optimization, but does not provide an actual convergence argument for the alternating scheme.**  
   In **Section 3.1**, the authors state that the factors “can be alternatively applied until convergence,” and **Figure 3(a)** is used to claim “smooth” and “stable” error reduction. But no theorem, monotonic decrease proof, or even a clear statement of what quantity is guaranteed to decrease is given in the main paper. In fact, **Table 3(c)** suggests the opposite of a simple convergence story: increasing from 1 to 3 or 15 iterations often worsens WikiText-2 and sometimes C4, especially at 40% and 50% compression. So the evidence points more toward a fragile heuristic than a principled alternating minimization method. If overfitting to calibration data is the real explanation, then the paper should say so much earlier and much more explicitly, because as written the method sounds more stable than the results support.

3. **The claimed “adaptive compression ratio” mechanism is quite heuristic, and the paper does not establish that it satisfies the stated global target retention ratio in a principled way.**  
   The rule in **Equation (19)**,
   \[
   CR(W)=mrr + I_n(W)\cdot (trr-mrr),
   \]
   is simple, but it is not obvious that averaging these per-layer ratios will produce the desired global target retention ratio once layers have different parameter counts. This is not a nitpick. In transformers, projection matrices across layers can differ in size or count across module types, so a naive layer-average does not necessarily respect a parameter-budget constraint. **Equation (20)** defines layerwise retention as a ratio of factor parameters to original parameters, but the paper does not show how the set of per-layer \(CR(W_i)\) values is adjusted to meet an overall model-level target exactly. The method may work in practice, but the formulation is incomplete as presented.

4. **The layer importance metric is under-motivated and arguably mismatched to the compression objective.**  
   In **Equation (17)**, importance is defined as the cosine similarity between input \(X\) and output \(Y=WX\). This is a rather odd choice. High cosine similarity between \(X\) and \(WX\) does not obviously imply that the layer is more sensitive to rank truncation, nor that retaining more parameters there is optimal under a global budget. A layer could drastically reshape activations while still being important, and cosine similarity between input and output could even be low precisely because the transformation is meaningful. The plots in **Figure 4** are visually interesting, and the observation that early layers often receive higher importance is plausible, but the paper never validates that this metric is a better predictor of compressibility than more direct alternatives, such as reconstruction error increase per rank removed, Hessian-based saliency, singular value decay, or whitening-informed sensitivity. Without that comparison, adaCR feels ad hoc.

5. **The experimental section is too narrow relative to the breadth of the claims.**  
   The abstract claims “Extensive experiments across multiple LLM/VLM families,” but the main paper’s strongest quantitative evidence is concentrated on LLaMA2-7B and 60% WikiText-2 comparisons on a few related 7B models. For VLMs, **Figure 5** shows only a handful of qualitative captioning examples. There is no captioning metric, no VQA result, no OCR-style benchmark, and no quantitative comparison on the VLM side in the main paper. If the paper wants to argue that the method broadly extends from LLMs to VLMs, the current evidence is too anecdotal.

6. **The baseline set is not fully convincing for the specific adaptive-rank claim.**  
   The paper compares mainly against SVD, FWSVD, ASVD, and SVD-LLM, which are relevant. However, for the adaCR contribution specifically, the natural question is whether simple non-uniform rank allocation heuristics, or other adaptive-rank allocation methods, would perform similarly. The paper only compares “constant” vs “adapt” within its own method in **Table 3(b)**, which is not enough to establish that the proposed importance metric is the right one. The evidence shows that non-uniform allocation helps, not that this particular non-uniform allocation is especially well justified.

7. **Some of the algorithmic description is incomplete or sloppy enough to hurt reproducibility.**  
   **Algorithm 1** is not sufficiently precise. For example, line 13 uses \(\text{TRUNC\_UV}(\mathcal{U}, \mathcal{V}, \Sigma')\), but the arguments do not match the current layer notation consistently, and line 14 calls \(\text{ADA\_UPDATE}(\mathcal{M}, \mathcal{X}', \text{SET}_{\mathcal{SVD}}, k)\) without clearly specifying what has been stored in \(\mathcal{SVD}\), how modules are grouped, or whether updates are layerwise or joint. Several pieces are deferred to the supplementary material, but the main paper already contains enough notation inconsistency that it is hard to reconstruct the exact training-free update procedure with confidence.

8. **The empirical story around iterations is actually a warning sign rather than a clean strength.**  
   In **Table 3(c)**, one iteration is usually best. At 60% compression, going from 1 to 3 iterations worsens WikiText-2 from 50.33 to 64.12, and 15 iterations is still worse than 1. At 40% compression, 1 iteration is again best. This means the “alternating updates until convergence” framing in **Equation (16)** is misleading in the main paper. The practical takeaway seems to be that one carefully regularized compensation step works, whereas repeated alternation can overfit or destabilize. That is still a valid engineering result, but it is a different claim.

9. **The presentation has multiple signs of insufficient polishing, including notation and wording errors in core sections.**  
   Examples include inconsistent use of \(\mathcal{V}^\top\) vs \(\nu^\top\) in the introduction on **Page 2**, grammatical issues such as “the first layer always weight most importance” in the caption of **Figure 4**, and awkward statements like “while the region bounded by corresponding to one iteration of alternative update” after **Equation (16)** on **Page 6**. These are not merely cosmetic. Because the method relies on matrix identities and alternating updates, notation consistency matters a lot here.

10. **The qualitative figures are suggestive but also somewhat cherry-picked and weakly analyzed.**  
    **Figure 5** contains examples where AdaSVD outputs are more semantically aligned than SVD-LLM, but there is no systematic error analysis. One example still contains awkward phrasing (“which is an automobile that is used for transportation”), so the figure supports “less broken than baselines” more than it supports strong preservation of generation quality. Similarly, **Figure 3(c)** overlays distributions before and after adaComp, but the axis labels and setup are too thinly explained for this to count as strong evidence. These figures help the narrative, but they are not robust validation.

11. **The paper’s claims about efficiency are incomplete because runtime and actual deployment speed are barely quantified.**  
    The motivation is deployment on resource-constrained devices, yet the main results report mostly perplexity and accuracy. There is no direct table with wall-clock decoding speed, end-to-end latency, or memory footprint before and after factorization in the main paper. Since low-rank factorization can reduce parameter count but may interact non-trivially with kernels and batching, the practical significance is hard to assess from the presented evidence.

12. **The comparison with quantization in Table 4 raises questions that are not discussed.**  
    **Table 4** shows AdaSVD + GPTQ outperforming SVD-LLM + GPTQ, which is good, but quantization consistently hurts compared with the unquantized AdaSVD counterpart, sometimes substantially. For example, at 50% compression on WikiText-2, AdaSVD degrades from 25.58 to 37.34 with GPTQ-INT4. That is fine if the goal is orthogonality, but the paper does not analyze whether the low-rank factors are especially sensitive to post-factorization quantization, whether quantizing \(U\) and \(V\) separately causes issues, or whether a different quantization order would be preferable. As written, the “orthogonal to other compression methods” claim is only partially substantiated.

## Questions
1. Please clarify the derivation of **Equations (7)** and **(13)** from the objective in **Equation (5)**. If \(X\) is part of the objective, why do the updates for \(V_k^{\sigma\top}\) not involve \(X\) or \(XX^\top\)? A dimension-by-dimension derivation in the rebuttal would materially increase my confidence.

2. Does adaCR guarantee the exact global target retention ratio at the whole-model level, or only approximately? Please provide the precise budget-allocation procedure, including how differing layer parameter counts are handled after computing **Equation (19)**.

3. For the importance score in **Equation (17)**, did you compare cosine similarity against other layer sensitivity metrics, such as singular value spectrum decay, output reconstruction error increase under trial truncation, Hessian/Fisher proxies, or activation variance? Even a small ablation would help justify why this metric is the right one rather than merely a convenient one.

4. The iteration ablation in **Table 3(c)** seems to contradict the “until convergence” wording. Is the practical recommendation always one iteration? If so, I would suggest reframing adaComp less as an iterative alternating optimization procedure and more as a one-step compensation update with optional extra steps under high compression.

5. Can you provide actual memory savings, throughput, or latency measurements in the main setting? Since the paper strongly motivates deployment, quantitative systems-side results would substantially improve the paper.

6. For the VLM claim, can you provide at least one quantitative metric in rebuttal, for example COCO captioning scores, instead of only the qualitative examples in **Figure 5**?

7. In **Table 3(a)**, AdaSVD without adaComp is sometimes worse than SVD-LLM, especially at 50% compression on both WikiText-2 and C4. What exactly differs in that setting besides turning off adaComp? This table currently makes it hard to isolate what the “base” method is.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are evident from the paper. The work studies model compression and does not introduce a dataset, human subject protocol, or deployment claim that raises an immediate ethics flag beyond the standard considerations already present in LLM deployment generally.

## Soundness Rating
2: fair. The empirical results are promising and mostly support the narrow claim that the proposed recipe can outperform prior SVD baselines, especially at high compression. However, the core mathematical updates are not presented with enough rigor, and the optimization/accounting details behind adaComp and adaCR are not fully convincing as written.

## Presentation Rating
2: fair. The high-level story and figures, especially **Figure 2**, are readable, but the paper has enough notation inconsistency, ambiguous derivations, and underexplained algorithmic details that clarity becomes a real issue.

## Contribution Rating
2: fair. There is a useful empirical improvement over existing SVD baselines, particularly in high-compression regimes, but the conceptual advance is more incremental than the paper suggests, and the adaptive rank-allocation part is insufficiently justified.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper addresses an important problem and shows meaningful empirical gains, especially in **Table 1**, **Table 2**, and parts of **Table 3**. Still, the current version has too many substantive issues in the core derivation, method specification, and justification of the adaptive rank allocation to warrant a positive recommendation at ICLR without a stronger rebuttal.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main equations, tables, and figures carefully, though a full implementation-level verification is not possible from the paper alone.