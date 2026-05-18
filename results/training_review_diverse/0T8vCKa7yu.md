Now I have a thorough understanding of the paper and all review claims. Let me produce the consolidated final review.

## Summary

This paper proposes CVXQ, a post-training mixed-precision weight quantization framework for LLMs. It formulates bit-depth allocation as a constrained nonlinear least-squares problem, uses a rate–distortion approximation to obtain closed-form marginal distortion estimates, and solves the allocation via dual ascent. Additional components include PCA/subsampling for efficient gradient-variance accumulation, companding based on a Laplace CDF, bias correction, and matrix partitioning with a Jensen's inequality guarantee on bit savings. The method is evaluated on OPT and Llama-2 families (125M–70B) at 3–4 bits.

## Strengths

1. **Principled optimization formulation.** The paper formalizes bit allocation as a resource-allocation problem (Eq. 3) with optimality conditions (Eq. 4) that lead naturally to a dual-ascent algorithm (Algorithm 1, Eq. 6). This avoids combinatorial search or per-layer Hessian inverses and provides a clear optimization lens on mixed-precision quantization. Evidence: Sections 3, Equations 3–6.

2. **Efficient gradient-variance accumulation.** To scale backpropagation through the full model, CVXQ uses PCA on the output embeddings along the embedding dimension and subsampling along the token dimension (Eq. 7), then accumulates gradient variances online across minibatches. This makes iterative optimization feasible for billion-parameter models. Evidence: Section 3, Equation 7, Algorithm 1 (lines 7–10).

3. **Theory-grounded companding and matrix partitioning.** The compander derived from the Laplace CDF (Eq. 8) is a principled alternative to uniform RTN quantization for light-tailed weight distributions. The matrix partitioning analysis (Eq. 10, Jensen's inequality guarantee that bit savings are non-negative) is clean and supported by empirical measurements in Figure 3. Evidence: Sections 3.2–3.3, Figure 3, Table 2(d).

4. **Thorough ablation study.** The paper systematically examines sensitivity to batch size, token count, cluster size (Table 2 a–c), and provides component ablations showing the marginal contribution of mixed precision and companding (Table 2d). The optimization is shown to be robust across a wide range of hyperparameter values. Evidence: Table 2, Figure 5.

5. **Empirical results across model scales.** CVXQ achieves competitive perplexity on WikiText2 for OPT and Llama-2 models at 3–4 bits, with the largest gains on smaller models (up to 4.55 perplexity reduction for OPT-125M at 3 bits) and performance matching or slightly exceeding baselines on larger models. Downstream QA results are also reported. Evidence: Table 1, Table 4(c).

## Weaknesses

### Fatal
None.

### Major

1. **Rate–distortion approximation unvalidated at the operating regime (3–4 bits).** The core gradient approximation (Eq. 5) is derived from rate–distortion theory, which the paper itself notes holds "at a sufficiently high bit depth" (line 82). The method is then applied at 3–4 bits per weight on average, a regime where this assumption is known to break down. No empirical check is provided to verify that the closed-form expression \(G_n^2 S_n^2 2^{-2B_n}\) actually tracks the true marginal distortion reduction at these bit depths; nor is the approximation error bounded or discussed. Because the entire dual-ascent update (Eq. 6) depends on this functional form, the theoretical grounding for the bit allocation is weaker than claimed. The strong empirical results partially mitigate this concern, but the paper's "optimality" framing is not supported without validation of the underlying approximation.

2. **Experimental comparisons do not fully control for effective bit budget.** The paper acknowledges (line 150) that AWQ uses a group size of 128 (vs. CVXQ's 512–768), incurring 2–4× more overhead bits, and that OWQ effectively operates at 0.01–0.05 higher bits per weight. However, the perplexity comparisons in Table 1 are reported without adjusting for these differences or reporting the *effective* per-weight bit rate (including all overhead bits for scales, cluster indices, etc.) for each method. The paper has Table 4b discussing overhead internally but does not use this information to produce controlled comparisons. The reported perplexity advantages—especially the large gap for OPT-125M—could be partly explained by differences in actual bit expenditure rather than superior allocation. Without controlled comparisons, the numerical claims should be interpreted with caution.

### Minor

1. **No runtime characterization for the optimization phase.** The paper claims CVXQ runs "in minutes for billion-parameter models and in a few hours for 10–100-billion-parameter models" (line 18) but provides no actual wall-clock times, GPU hours, or comparison to GPTQ (which is also fast). Algorithm 1 involves repeated forward/backward passes plus an inner loop of 10 primal–dual updates per outer iteration. The only concrete runtime number reported (line 296: 3.8× speedup) is for an inference kernel, not the optimization itself. This makes the scalability claim unverifiable.

2. **No discussion of limitations or failure modes.** The paper presents no limitations section and does not discuss when CVXQ might underperform—e.g., for layers with small \(P_n\) where gradient variance estimates are noisy, when the calibration set poorly represents the inference distribution, or when the Laplace-distribution assumption underlying the compander is violated. This omission weakens the paper's scholarly completeness.

3. **Companding function not quantitatively compared to alternatives.** The paper qualitatively argues that the Laplace-CDF-based compander (Eq. 8) reduces MSE for light-tailed distributions but provides no quantitative MSE comparison against alternatives such as optimal Lloyd–Max quantization or the per-channel min–max scaling used in GPTQ/AWQ.

4. **Hyperparameter choices not justified.** Key hyperparameters (dual step size \(\alpha=2\), max_iter=64, \(\beta\) values for the momentum in gradient accumulation) are reported but no sensitivity analysis or justification for these specific values is given. While Table 2 shows robustness to data hyperparameters, the algorithm's own parameters are not similarly ablated.

5. **Convergence shown only for a single setting.** Figure 5 plots perplexity across iterations for one configuration (C4 calibration, batch size 16, cluster size 512). Convergence behavior for larger models, different calibration sets, or different random seeds is not examined.

6. **No discussion of why gradient variance is preferred over Hessian trace-based sensitivity.** Related work on Hessian-based mixed precision (Chen et al., 2021, which the paper cites) allocates bits using Hessian trace as a sensitivity proxy. The paper does not discuss the advantages of gradient variance over Hessian trace for the LLM setting, leaving a scientific connection unexplored.

### Trivial

- The paper calls itself a "convex optimization perspective" (title, abstract) but the original problem (3) is nonlinear (acknowledged line 63), the quantizer is a step function, and the relaxation involves a heuristic approximation. This framing slightly overstates the theoretical rigor, though the Lagrangian/dual-ascent machinery used is standard in convex optimization.

## Nice-to-Haves

- **Validate Eq. 5 empirically:** For at least one representative layer, compute the true marginal distortion reduction by enumerating bit depths and compare to \(G_n^2 S_n^2 2^{-2B_n}\) to bound the approximation error at 3–4 bits.
- **Controlled-bit-budget comparisons:** Report the effective bits per weight (including all overhead) for CVXQ and every baseline, and compare perplexity at matched effective bit rates.
- **Report wall-clock optimization times** for at least one model per size category and compare to a single-iteration method like GPTQ.
- **Add a limitations paragraph** discussing when CVXQ's assumptions may fail.
- **Ablate the iterative loop:** Compare bit depths from the first dual-ascent pass (frozen) vs. the full iterative result to measure the benefit of recomputing \(G_n^2\) after bit-depth updates.

## Removed Points

The following criticisms from the reviewers were evaluated against the paper and removed per the filtering guidelines:

- **Garbled tables / PDF extraction artifacts** (Harsh Critic, "Other Observations" final bullet). This is a parser issue, not an author error. Per hard rules: remove.
- **"The paper should present the key downstream results in the main text clearly"** — the images in the extracted text are garbled but exist in the original. Parser artifact. Remove.
- **"Missing comparison to Hessian-based mixed precision (HAWQ)"** — Per hard rules, do not mention missing related works. The paper does cite Chen et al. (2021) which covers Hessian-based approaches. The reviewer's asked-for discussion of *why gradient variance vs. Hessian trace* is kept as a Minor weakness (item 6) since that's about depth of discussion, not about a missing citation.
- **"The problem is non-convex because the quantizer (2) is a step function"** — The paper explicitly acknowledges this (line 82: "the quantization function (2) is constant almost everywhere, a naive computation of the partial derivatives...does not provide a useful direction for descent"). The paper never claims the original problem is convex; it claims a "convex optimization perspective" through Lagrangian relaxation and dual ascent. This criticism misreads the paper's framing. Downgraded from the original characterization to Trivial.
- **Several generic strengths from the Strength Finder** (e.g., "the paper addressed an important problem") — dropped per instructions to remove generic/superficial strengths.

## Novel Insights

The key insight emerging from the reviews is that CVXQ's main value may be more in its **principled framework** than in dramatic accuracy improvements on large models. The paper honestly reports that for OPT-66B and Llama-2 70B, CVXQ achieves "minor perplexity gains (0.00–0.01)" over baselines (line 150), and the largest gains are on the small OPT-125M model. This pattern—principled optimization matters most when models are small/less compressible, while large models are so compressible that simple RTN nearly matches sophisticated methods—is an interesting empirical observation that the paper could develop further. Additionally, the Jensen's-inequality-based guarantee for matrix partitioning (Eq. 10) is a clean theoretical result that stands independently of the approximation concerns.

## Suggestions

1. **Validate the rate–distortion approximation** at the bit depths used (3–4 bits) for at least one representative layer by enumerating bit depths and measuring actual vs. predicted marginal distortion. This would either confirm or bound the error in the central approximation.
2. **Report effective bit rates** (including all overhead) for CVXQ and every baseline, and present at least one set of perplexity comparisons at controlled effective bit budgets.
3. **Add wall-clock optimization times** for representative models to substantiate the scalability claim.
4. **Include a limitations paragraph** discussing assumptions (high-rate approximation, Laplace-distributed weights, calibration set representativeness, thin-layer sensitivity) and scenarios where CVXQ may not outperform simpler methods.
5. **Ablate the iterative loop** by comparing a single-pass dual ascent (frozen \(G_n^2\)) against the full iterative procedure to quantify the marginal benefit of recomputing gradient variances.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>