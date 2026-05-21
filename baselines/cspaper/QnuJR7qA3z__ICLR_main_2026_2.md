---
job_id: a847980e-2d66-4727-be91-90ca39b35d74
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: QnuJR7qA3z.pdf
paper: HARA: A Unified Framework for Hardware-Efficient Non-Linearity in Transformers
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope through ML systems and hardware-aware deployment of Transformer models, with a method for approximating core nonlinear operators in modern architectures.

## Minimum Quality
Pass ✅. The submission contains the required scientific components, including abstract, introduction, related work, methodology, experiments, quantitative results, and discussion/conclusion; despite several technical and empirical weaknesses, it clears the minimum bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to reviewers, or other manipulation attempts in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes HARA, a framework that replaces multiple Transformer nonlinearities, including activation functions, Softmax, LayerNorm, and RMSNorm, with a unified arithmetic-plus-shallow-ReLU architecture. The main technical idea is a three-stage initialization pipeline, centered on dynamic programming for piecewise-linear breakpoint selection and an analytical mapping from piecewise-linear functions to a one-hidden-layer ReLU network. The paper evaluates approximation error, projected hardware area/power savings, and end-to-end impact on BERT, Swin, LLaMA, and Stable Diffusion style models, reporting very small accuracy degradation together with substantial synthesized hardware savings relative to separate specialized nonlinear units.

## Strengths
1. The paper attacks a practically meaningful problem. The motivation, replacing heterogeneous nonlinear hardware blocks with a shared approximation engine, is well aligned with real deployment constraints for Transformer inference, especially on edge devices.

2. The unification angle is the strongest part of the paper. Instead of treating GELU, Softmax, and normalization as separate approximation problems, the paper tries to cast them into a common arithmetic-ReLU template. This is a sensible systems-level objective and is broader than a one-function approximation paper.

3. The DP-based initialization idea is potentially useful. The ablation in **Table 4** suggests that the proposed initialization, followed by fine-tuning, is much stronger than naive direct training. The improvement is not marginal: for example, GELU drops from \(1.38\times 10^{-3}\) to \(1.89\times 10^{-7}\), and Softplus from \(5.44\times 10^{-2}\) to \(4.77\times 10^{-6}\). Even if some methodological details are still underspecified, this table does support the claim that initialization is a major factor.

4. The operator-level approximation results in **Table 3** are strong on their face. HARA consistently achieves lower MSE than NN-LUT and RI-LUT across the three displayed operators and across multiple hidden dimensions. The LayerNorm numbers are especially striking, where HARA is several orders of magnitude lower than the baselines.

5. The end-to-end results are surprisingly stable. **Table 6** reports almost unchanged metrics after replacing all nonlinearities with HARA approximations under the stated configuration. This is further supported by **Tables 10-13**, which show that once the hidden dimension reaches 8 or 16, the all-operator setting tracks the baseline closely for BERT, Swin, and LLaMA, and mostly for DiT as well. That pattern is useful because it shows a monotonic quality-complexity tradeoff rather than one cherry-picked point.

6. The figures do help communicate the paper’s intended story. **Figure 1** gives a readable high-level pipeline, from target operators to decomposition and approximation, and makes the “single canonical architecture” claim easier to follow. **Figure 3** is also useful: it visually illustrates the paper’s argument that conventional finite-interval fitting can misbehave outside the training interval, whereas the proposed constrained construction behaves better in the tails. That is one of the few places where the motivation for the asymptotic constraint becomes intuitive rather than purely verbal.

7. The hardware angle is at least concretely instantiated rather than hand-waved. **Figure 2** and **Table 5** provide a specific URN-based architecture and estimated area/power accounting. Even though I have reservations about the fairness and completeness of the comparison, the paper does make a genuine effort to tie the approximation method to an architectural design rather than stopping at software-only MSE.

## Weaknesses
1. The central “unified framework” claim is only partially substantiated because the method does not truly approximate all operators in one common functional form; rather, some operators are first decomposed into auxiliary primitives whose own implementation assumptions are nontrivial. This matters most in **Section 3.3.2** and **Equations (2)-(3)**. For Softmax and LayerNorm, the paper moves the complexity into \(\mathrm{Pow2}\) and \(\log_2\), plus max/sum/sign/shift/arithmetic, and then claims elimination of specialized hardware for \(exp\), \(sqrt\), and \(div\). That is directionally plausible, but “unified” here is weaker than advertised because the resulting hardware still requires a fairly rich support structure, including max blocks, sum generators, local buffers, controllers, and auxiliary functions as shown in **Figure 2**. In other words, the paper unifies certain nonlinear primitives, but not the whole nonlinear-processing stack. The claim should be narrowed accordingly.

2. The mathematical exposition around the PWL-to-ReLU conversion is not rigorous enough in the main paper, and some notation is confusing or inconsistent. This is not a cosmetic issue because the initialization pipeline is the main claimed algorithmic contribution. In **Algorithm 1** on **Page 5**, the stated output is “\(n,m,B\)” while **Section 3.2** describes the required network parameters as \((W_1,b_1,W_2,b_2)\). The mapping between these symbols is only partially implied. Also, line 12 defines \(n_j \gets k_j-k_{j-1}\), line 13 sets \(m_j \gets \text{sign}(n_j)\), and line 15 computes \(B_j \gets (m_B)_j/m_j\), but there is no discussion of the case \(n_j=0\), for which \(m_j=0\) and line 15 divides by zero. Since adjacent PWL slopes can absolutely coincide, this is not an edge case one can ignore. The algorithm as written is therefore underspecified.

3. Relatedly, the derivation in **Appendix A.1**, which the main text relies on, contains notation that is hard to verify and at points appears dimensionally or logically muddled. In **Equation (5)**, the expression for \(k[i]\) and \(B[i]\) mixes terms such as \(W_2[j]\cdot(W_1^+[j], b_1^+[j])\), which is not a scalar formula as written. In **Equations (7)-(9)**, the reconstruction argument for the slopes is sketched, but the paper does not fully prove that the proposed constrained parameterization recovers an arbitrary desired PWL function under the stated ordering of breakpoints and signs. The paper says the inverse problem becomes “well-posed” once \(W_1>0\) and \(k[0]=0\), but that leap is asserted more than demonstrated. Because the claimed advantage over direct training hinges on this analytical conversion, the paper needs a cleaner, explicit mapping such as \(W_1[j]=1\), \(b_1[j]=-p_j\), \(W_2[j]=k_j-k_{j-1}\), with the corresponding intercept construction shown carefully. As written, the math is not robust enough for a main-track methodological claim.

4. The experimental validation of approximation quality is narrow relative to the paper’s headline. The paper repeatedly frames HARA as a replacement for “the full spectrum” of Transformer nonlinear operators, but **Table 3** only compares against baselines for GELU, Softmax, and LayerNorm. There is no direct baseline comparison for Sigmoid, Tanh, SiLU, Softplus, or RMSNorm in the main paper. Likewise, **Table 4** includes more functions, but that is only an internal ablation, not a comparative study. If the contribution is operator unification, the empirical comparison should reflect that broader scope.

5. The fairness of the hardware comparison is questionable. **Table 5** compares a baseline made of three separate specialized units against one HARA URN at HD=8, but the accounting basis is not fully comparable. The baseline uses LUT-based specialized implementations for Softmax, LayerNorm, and GELU, yet it is not clear whether shared control, buffering, reduction logic, and memory infrastructure are consistently counted on both sides. Meanwhile, the HARA side includes a “single and basic core block of unified HARA implementation (URN)” in the text, but **Figure 2** and **Table 9** suggest the actual deployed architecture involves 16 URNs plus SG/MB/LB/controller. This makes it difficult to interpret the “over 60% area saving” as an apples-to-apples system comparison. At minimum, the paper should clearly separate cost of a single function unit, cost of the full supporting datapath, and cost at matched throughput.

6. The hardware evidence is only synthesis estimation, and several practically important metrics are missing. The paper acknowledges this in **Section 5**, but it still weakens the overall contribution. There is no measured FPGA/ASIC prototype, no post-layout timing or energy, no end-to-end latency on a Transformer workload, and no throughput-normalized comparison. **Table 9** gives latency in a symbolic form such as “SL/8+15” cycles for Softmax and LayerNorm, but sequence length is not instantiated, and there is no comparison to the baseline latency. Since the paper’s main value proposition is hardware efficiency, this omission is material.

7. The end-to-end evaluation is too thin to establish robustness. In **Section 4.1** and **Table 6**, the paper gives one number per model and configuration, without variance, repeated trials, confidence intervals, or details on whether these are validation or test metrics in each case. For tasks with some stochasticity, especially image generation with HPSv2, reporting a single scalar without uncertainty is not enough to support “negligible impact” claims. The results may well be stable, but the paper does not demonstrate that statistically.

8. The quantization story is muddled. The abstract and main claims emphasize compatibility with 8-bit quantization, but **Table 6** conflates HARA replacement and “standard 8-bit post-training quantization” into one summary number, making it hard to isolate the effect of the approximation itself from the effect of quantization. Then in the appendix, **Tables 14-16** show mixed behavior depending on operator and bitwidth, with some noticeable degradation for LayerNorm-related settings under \([8,8]\) and especially under lower precision. The paper should disentangle three cases explicitly: baseline FP, HARA FP, and HARA quantized. Right now the presentation makes the quantization robustness claim sound cleaner than the evidence actually shown.

9. The paper’s positioning against prior work is incomplete for the exact claim being made. The related work mentions NN-LUT and RI-LUT, and some operator-specific Softmax approximations, but the paper does not adequately engage with alternative hardware-sharing or unified nonlinearity designs. This matters because the claimed novelty is not merely “approximating GELU with ReLU,” it is “one unified hardware-efficient framework for multiple Transformer nonlinearities.” For that claim, the paper needs stronger differentiation from prior hardware co-design approaches that also share resources across nonlinear operators.

10. There is an inconsistency between the paper’s broad rhetorical claims and what the evidence actually supports. For example, **Page 2** claims “fully compatible with 8-bit quantization” and the conclusion says HARA provides a “practical and extensible paradigm,” but the current evidence is limited to software replacement plus synthesis estimates. Likewise, **Figure 4** in the appendix presents an accuracy-area tradeoff only for GELU, not for the more architecturally consequential Softmax/normalization path. The work is interesting, but several claims are one notch stronger than the presented data justify.

11. Some parts of the presentation read as polished but scientifically under-specified. **Figure 2** is a good schematic, yet it does not state operand bitwidths, parameter storage size, or whether CLUT contents are per-operator, per-layer, or global. Those details matter because the whole pitch is hardware simplification. Similarly, **Figure 3** is visually persuasive, but it reports MSE values for “ReLU Net” and “HARA” without defining whether those are trained with equal parameter budgets, equal hidden dimensions, identical training data/ranges, and comparable regularization. The figure supports the intuition, but not a rigorous apples-to-apples comparison by itself.

## Questions
1. Please give a precise, self-contained mapping from the DP output to the actual network parameters used at inference. Concretely, how do \(n\), \(m\), and \(B\) in **Algorithm 1** map to \((W_1,b_1,W_2,b_2)\) in **Equation (1)**? Also, how is the case \(n_j=0\) handled so that line 15 of **Algorithm 1** is well-defined?

2. Can the authors provide the exact DP objective and constraints? The text says the algorithm “globally minimize[s] the MSE,” but the recurrence, state definition, discretization strategy, and computational complexity are omitted in the main paper. What is the time complexity in the number of sampled points and segments, and how expensive is this initialization in practice for each operator?

3. For **Equations (2) and (3)**, please clarify the actual inference data path and the domains over which Pow2 and Log2 are approximated. For Softmax, what range of \(\hat{x}\) is assumed after max subtraction? For LayerNorm/RMSNorm, how are numerical corner cases handled when \(|\bar{x}|\) is very small or the variance approaches zero? Is an \(\epsilon\) term included anywhere, as in practical LayerNorm implementations?

4. The hardware comparison would be much more convincing if the accounting were fully normalized. Can the authors provide an apples-to-apples comparison at matched throughput and matched precision, including all required support logic and parameter storage, for both the baseline specialized design and HARA? Right now **Table 5** and **Table 9** leave too much room for interpretation.

5. Please report latency and energy, not only area/power estimates. Even post-synthesis or FPGA-based numbers would help. Since HARA may trade off simpler nonlinear primitives against extra control and chaining, latency could move in either direction.

6. Can the authors provide end-to-end results with uncertainty estimates, or at least repeated runs where appropriate? This is especially relevant for the generative setting and for the claim that performance changes are consistently below \(0.1\%\).

7. A more complete baseline study would help. Why are comparative results in **Table 3** limited to GELU, Softmax, and LayerNorm when the paper also targets Sigmoid, Tanh, SiLU, Softplus, and RMSNorm? If baselines for these operators are unavailable, that should be stated explicitly.

8. The quantization claim needs cleaner decomposition. Please provide three separate settings per model: baseline floating-point, HARA floating-point, and HARA+\([8,8]\) quantization, ideally in one table in the main paper. That would make the “quantization compatibility” claim much easier to evaluate.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper itself. The work is about efficient ML deployment and does not introduce a clear new risk category beyond standard downstream-use considerations for the underlying models.

## Soundness Rating
2: fair. The core idea is plausible and supported by promising empirical trends, but the main algorithmic component is underspecified in important mathematical details, and the hardware claims rely on incomplete and not fully apples-to-apples evidence.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures are helpful, but the notation, derivations, and experimental accounting are not clear enough for a paper whose main contribution is a technical approximation pipeline plus hardware co-design claim.

## Contribution Rating
2: fair. There is a meaningful systems motivation and the unification objective is interesting, but the current evidence does not yet support the broader contribution claims at the level expected for ICLR main track.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a worthwhile problem formulation, some strong empirical signals, and an interesting initialization idea, but too many pieces of the core technical and hardware story remain under-specified or insufficiently validated for me to recommend acceptance in its current form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. It is unlikely, but not impossible, that I misunderstood some implementation details hidden by the current exposition.