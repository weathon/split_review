---
job_id: 8c15754d-cd5d-4bcc-81cd-23ebf82bfd00
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 0nvQ5kHXf4.pdf
paper: Efficient Resource-Constrained Training of Transformers via Subspace Optimization
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on efficient training and fine-tuning of transformer models via low-rank/subspace optimization, with relevance to representation learning, optimization, and edge/on-device ML.

## Minimum Quality
Pass ✅. The paper contains all core scientific sections, including Abstract, Introduction, Related Work, Method, Experiments, quantitative results, and Conclusion; despite several technical and empirical shortcomings, it clears the minimum bar for a full review rather than a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions targeting automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes Weight-Activation Subspace Iteration (WASI), a training framework for transformer fine-tuning under resource constraints that jointly compresses model weights and activations into low-rank subspaces. The method combines a weight-side subspace iteration scheme (WSI) with activation compression based on ASI, aiming to reduce training memory, inference memory, and FLOPs while preserving accuracy on ViT, Swin Transformer, and a small LLM setting.

## Strengths
The paper addresses a relevant and practical problem. Much of the literature on efficient adaptation either focuses only on trainable parameters, such as LoRA-style methods, or only on activations. Here the authors explicitly target both weight storage and activation storage during backpropagation, which is a meaningful systems-level objective for on-device learning.

The empirical scope in the main paper is reasonably broad. The authors evaluate on multiple transformer families, including ViT, SwinT, and TinyLlama, and report both training-time and inference-time resource metrics. That is better than papers that only show a single backbone or only report parameter counts. The on-device latency experiment on Raspberry Pi 5 in Section 4.4 is also useful, because it moves beyond abstract FLOPs into actual wall-clock behavior.

I found the visual evidence in several figures helpful. In particular, **Figure 5** makes the central tradeoff fairly concrete for ViT on CIFAR-10: WASI traces a smoother accuracy-efficiency frontier than the baselines, and the contrast with SVD-LLM is especially visible in the memory plots where SVD-LLM becomes unattractive at weaker compression settings. Likewise, **Figure 6** is a strong presentation device because it shows that the trend is not isolated to one dataset; the consistency of the curves across Pets, Flowers, CUB, CIFAR-10, and CIFAR-100 supports the claim that the method is not completely brittle across tasks.

The preliminary analysis section is a genuine plus, not just filler. **Figure 3(b)** is especially informative: the comparison between WSI and repeated full SVD under varying explained variance thresholds directly addresses the rationale for replacing repeated SVD with subspace iteration. Even though I have reservations about how strong the conclusion should be, it is still the right experiment to run. Similarly, **Figure 4** usefully illustrates the skewed explained-variance spectrum of activations across modes, which is precisely the empirical property the activation compression component relies on.

The paper also contains useful quantitative tables. **Table 2** is particularly relevant because it reveals an important practical point that does not fully come through from FLOPs alone: ASI can become slower than vanilla training at larger \(\varepsilon\), while WASI remains consistently faster. That is a concrete systems benefit. **Table 1** is also valuable because it shows the extension beyond MLP blocks to all linear layers in ViT, including attention projections, and the trend is coherent with the main claims.

Presentation is mostly decent. The high-level motivation is easy to follow, and the paper is structured in a way that makes the method, preliminary validation, and downstream experiments reasonably navigable.

## Weaknesses
My main concern is that the paper’s conceptual novelty is modest relative to the way the contribution is framed. WASI is essentially a combination of two existing directions already discussed in the paper itself: activation subspace iteration for activations, and low-rank weight factorization updated through reused subspaces for weights. The combination is practically useful, yes, but the paper sometimes overstates the leap by presenting WASI as the “first method for efficient model-activation-decomposition-aware training” on **Page 2**. That phrasing is too sweeping given how much of the machinery is inherited or adapted from ASI, SVD-based compression, and prior observations on fine-tuning subspace stability. For an ICLR main-track paper, the burden is not only to be useful, but also to be clearly differentiated beyond “do both together for transformers.”

The mathematical exposition around the weight-side update is underspecified, and this matters because it is the core algorithmic contribution. In **Equation (11)** on **Page 6**, the update is written as
\[
L_iR_i = L_iR_i + \eta \cdot \widetilde{\frac{\partial \mathcal L}{\partial \mathcal W_i}}.
\]
This is not a proper optimization rule as stated. Are \(L_i\) and \(R_i\) the actual optimized parameters, or is the product \(L_iR_i\) updated in ambient space and then refactorized? If the latter, the method is not truly optimizing in the factor space, and one needs to spell out when re-projection occurs and how gradients are assigned to \(L_i\) and \(R_i\). If the former, then the paper should provide explicit formulas for \(\partial \mathcal L/\partial L_i\) and \(\partial \mathcal L/\partial R_i\). As written, the optimization variable is ambiguous, and that ambiguity affects reproducibility and the interpretation of memory/computation claims.

Relatedly, **Algorithm 1** on **Page 4** appears incomplete or inconsistent. At iteration \(t=0\), the algorithm computes \(L_i^{(t)}, R_i^{(t)} = \mathrm{SVD}(W_i^{(t)}, \varepsilon)\). For \(t>0\), however, it computes
\[
R_{i,t}^{T} = W_{i,t}^{T} \cdot L_i^{(t-1)},
\]
then
\[
L_i^{(t)} = \mathrm{Orthogonalize}(W_i^{(t)} \cdot R_{i,t}^{T}),
\]
and returns \(L_i^{(t)}, R_i^{(t)}\). But there is no explicit step producing \(R_i^{(t)}\) after \(L_i^{(t)}\) has been orthogonalized. If the intended update is the standard one-pass subspace iteration, the algorithm should say how \(R_i^{(t)}\) is recomputed from the new \(L_i^{(t)}\). Right now, the pseudocode is incomplete at exactly the place where correctness depends on it.

There are several mathematical inconsistencies in the appendix-level derivations that make me less confident in the exact FLOP formulas and gradient implementation. For example, in **Equation (13)** on **Page 13**, \(\widetilde{\Delta \mathcal W}_{o,i}\) is defined using summations over \(b,n,o,i\), which is dimensionally odd because \(o\) and \(i\) are the output indices of the quantity already being defined, so they should not both be summed out. The same issue propagates to **Equation (14)**. In the 4D case, **Equation (24)** on **Page 14** defines \(\mathcal Z^{(3)}\) by summing over \(r_3\), but the right-hand side contains \(\mathcal Z^{(1)}_{b,h,w,o}\), even though \(b\) and \(w\) are not in the left-hand side indices, and this does not match **Equation (22)**. **Equation (25)** also has an unspecified summation symbol, and **Equation (27)** writes \(\mathcal G \times_i Q\) even though the matrix was introduced as \(B\), with mismatched symbols \(g_{p_1,\ldots,p_n}\) and \(b_{q,p_i}\). These are not cosmetic typos only, because the paper asks the reader to trust that the low-rank backpropagation operator \(f_{\mathrm{LR}}(\cdot)\) is well-defined and efficient. Right now, the derivation does not fully earn that trust.

The empirical validation of the central “stable subspace” hypothesis is weaker than the text suggests. On **Page 5**, the method relies on the claim that the intrinsic weight subspace remains relatively stable during fine-tuning. Yet in **Section 4.2**, the evidence is mostly a single-model, single-dataset study, namely ViT on Pets. **Figure 3(a)** itself is also a bit awkward: it is described as showing the “evolution of singular values of \(\mathcal W_6\) across epochs,” but the text then concludes rank stability more broadly. Showing one layer of one model on one task is not enough to justify the generality implied by the method section. If the method critically depends on warm-started subspace reuse, one would want evidence across multiple layers, datasets, and at least one architecture with 4D activations such as SwinT. Without that, the stability claim reads more like a plausible heuristic than a well-supported design principle.

The baseline selection is not fully convincing for a paper making broad practical claims about transformer fine-tuning on edge devices. In **Section 4.1** on **Page 6**, the authors compare against ASI, SVD-LLM, and vanilla training. Those are relevant, but they do not cover the strongest parameter-efficient transformer fine-tuning baselines for vision models. Since the paper repeatedly compares itself to LoRA-style thinking in the introduction and related work, it is a notable omission that a straightforward LoRA baseline on ViT/SwinT is not included in the main experiments. This matters because the practical question is not just whether WASI beats SVD-LLM, but whether the added complexity of joint low-rank weight-activation training provides a favorable tradeoff against simpler adaptation methods that are widely used.

The fairness of some comparisons is also debatable. In **Section 4.3** on **Page 8**, the paper states that for fairness the same compression ratios are applied to SVD-LLM. But SVD-LLM and WASI optimize different objects and incur different overheads; equalizing one compression measure does not guarantee a fair comparison in memory, FLOPs, or accuracy. Similarly, the ViT experiments focus in the main paper on “linear layers within multi-perceptron blocks” for fair comparison with previous methods, but then stronger applicability claims are made about transformer training in general. **Table 1** later shows all linear layers including attention blocks, and the memory/FLOP behavior remains favorable, but that result is relegated outside the main narrative. This creates a slight mismatch between the strongest claims and the fairest like-for-like evaluations.

Another issue is that the claimed computational analysis is not entirely transparent. In **Section 3.4** on **Page 6**, the authors assume “for simplicity” that the same optimal rank is applied to both \(\mathcal A_i\) and \(\mathcal W_i\). But the actual method uses a scalar \(K_i\) for weights and a vector \(\mathbf r_i\) for activations, selected by different procedures. The simplification may be acceptable for intuition, yet the resulting curves in **Figure 2** are then more schematic than predictive. The figure is clean, but it risks overstating the precision of the resource forecasts because it is driven by a symmetry that the real method does not satisfy.

Some claims about controlling information loss are too strong relative to what is actually established. The paper repeatedly says that WASI “carefully controls information loss” or works under a “controlled information-loss constraint.” For the weight side, the control is through explained variance thresholding of singular values in **Equations (5)-(7)**, which bounds reconstruction loss of the weight matrix, not downstream task loss and not even necessarily gradient error after multiple training steps. For activations, the rank selection through perplexity is more directly tied to gradient approximation, but again the connection to final optimization quality is empirical rather than theoretically controlled. I would encourage the authors to tone this down. At present, the wording occasionally suggests a stronger guarantee than the paper proves.

There are also presentation and notation problems that make the method harder to audit than it should be. Examples include: **Page 6**, where “Detailed derives” should be “Detailed derivations”; **Section 4** says “Sec. 3.3 and Sec. 3.3” when clearly one of those references should be different; **Figure 4** is referred to with singular “illustrate”; several references on **Pages 10-12** appear malformed or duplicated. Normally I would treat these as minor, but here they accumulate in a paper that leans heavily on technical derivations, and they reduce confidence that all equations and experiments have been checked carefully.

Finally, while the resource results are promising, the practical speedup is not always as dramatic as the abstract framing might lead the reader to expect. The abstract highlights up to \(62\times\) memory and \(2\times\) FLOPs reduction, but the actual wall-clock gain on Raspberry Pi 5 in **Figure 8** and **Table 2** is around \(1.4\times\) at \(\varepsilon=0.9\). That is still useful, but the paper would be stronger if it more explicitly discussed where the remaining overhead comes from, for example orthogonalization, tensor reshaping, or decomposition bookkeeping. Otherwise, there is a mild gap between asymptotic/compression messaging and real-device runtime impact.

## Questions
1. Please clarify the exact optimization procedure for the weight factors. In **Equation (11)**, are \(L_i\) and \(R_i\) optimized directly, or is the product \(L_iR_i\) updated in full space and then re-factorized? A precise algorithmic statement, ideally with explicit gradients \(\partial \mathcal L/\partial L_i\) and \(\partial \mathcal L/\partial R_i\), would materially increase my confidence.

2. Can the authors provide a corrected and fully specified version of **Algorithm 1**? In particular, how is \(R_i^{(t)}\) obtained after computing the new \(L_i^{(t)}\) for \(t>0\)? As written, the pseudocode seems incomplete.

3. Several appendix equations appear inconsistent, especially **Equations (13)-(18)** and **(22)-(26)**. Are these transcription issues, or do they reflect the actual implementation? A clean corrected derivation of \(f_{\mathrm{LR}}(\cdot)\) would help a lot, because this operator is central to the method.

4. The subspace-stability claim is currently supported mainly by ViT on Pets in **Section 4.2**. Could the authors provide, in rebuttal, evidence that the rank/subspace stability phenomenon also holds for SwinT and for more than one representative layer? Even a compact multi-layer plot or rank-variance summary would strengthen the premise.

5. Why is a direct LoRA baseline absent from the main experiments, especially for ViT where it is straightforward to run? Since the paper positions itself partly against adapter-based approaches, a head-to-head comparison in training memory, wall-clock time, and accuracy would substantially improve the empirical case.

6. For **Figure 5**, it would help to know whether all methods were tuned comparably at each operating point, or whether the same hyperparameters were reused across compression levels. If the latter, did any baseline require retuning to reach a fair accuracy-efficiency tradeoff?

7. The paper reports strong memory savings and moderate but real latency gains on Raspberry Pi in **Figure 8** and **Table 2**. Can the authors break down where the runtime goes, for example decomposition overhead versus actual low-rank linear algebra? That would make the practical story much more convincing.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns arise from the paper as presented. The work focuses on efficient training and deployment of transformer models on resource-constrained devices, with standard public datasets and no evident human-subjects, privacy, or high-risk deployment issues discussed in the main paper.

## Soundness Rating
2: fair. The central empirical claims are supported to a reasonable extent, but the mathematical presentation has several inconsistencies and the optimization details for the proposed weight-factor update are underspecified.

## Presentation Rating
3: good. The paper is mostly readable and well organized, with helpful figures and tables, but there are enough notation issues, equation problems, and reference inconsistencies to keep it from being excellent.

## Contribution Rating
3: good. The joint treatment of weight and activation compression for transformer fine-tuning on edge devices is practically valuable and likely of interest to the ICLR community, even if the conceptual step beyond prior work is more incremental than the paper sometimes suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The practical value is real, the experiments are useful, and the on-device angle is compelling, but the paper needs sharper technical specification and more careful support for its strongest claims.

## Reviewer Confidence
4: confident. I am confident in this assessment; I am familiar with low-rank adaptation, activation compression, and efficient transformer training, and I checked the equations and empirical presentation with care, though some implementation-level details remain unclear from the paper.