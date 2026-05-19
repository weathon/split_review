- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes FI (First-order local Influence), a theoretically grounded influence measure for quantifying the stability of LLMs under local perturbations. FI is derived from information geometry (perturbation manifold with Fisher-inspired metric) and enjoys reparameterization invariance — a property not shared by the Jacobian norm or Cook's distance. The paper demonstrates FI on three fronts: (1) detecting fragile input pixels in a VLM case study, (2) identifying fragile parameters via sparsification (2–3% of high-FI parameters → 75% accuracy drop on MMLU vs. near-zero for random), and (3) practical applications in quantization and model merging where protecting high-FI channels/parameters outperforms random protection.

## Strengths

- **Reparameterization invariance (Theorem 2.3).** The paper proves that FI is invariant under any diffeomorphic reparameterization of the perturbation, and provides a concrete worked example (Equation 3) showing why the Jacobian norm fails under scaling transformations common in ReLU networks (non-negative homogeneity). This is a genuine theoretical advantage over existing measures and is correctly motivated by the non-identifiability problem (Dinh et al., 2017; Amari, 1998).

- **Strong signal in parameter sparsification (Section 3.2, Figure 3).** Sparsifying only 2–3% of parameters with the highest FI in Qwen2-7B causes a ~75% accuracy drop on MMLU, while random sparsification at the same rate leaves performance nearly intact. This large effect size provides direct empirical evidence that FI identifies parameters whose perturbation truly dominates model behavior, and it cleanly distinguishes sensitive from insensitive components.

- **Closed-form computation with low-rank handling (Theorem 2.4 and Equation 4).** The paper provides a closed-form solution for FI (∇f^T G^{-1} ∇f) and addresses the practical case where G_ω is not positive-definite via a compact SVD transformation. This makes the measure computable for large models without requiring full matrix inversion.

- **Unified treatment of external and internal perturbations.** The same FI formulation handles input-level perturbations (image pixels, Section 3.1), parameter-level perturbations (Section 3.2), and cross-modal prompt effects (Section 3.1), demonstrating conceptual versatility beyond Hessian-based approaches that focus solely on parameters.

- **Demonstrated practical utility in quantization and model merging (Section 3.3).** The FI-guided protection strategy recovers >90% of quantization-induced performance loss with only 5% of channels at FP16, and yields 15–20% improvement over random protection in model merging. These results suggest FI can be deployed in real LLM optimization pipelines.

## Weaknesses

### Fatal
None.

### Major

- **No comparison to any existing influence or saliency measure in experiments.** Every experiment compares FI-guided selection only to random selection (Section 3.2: "randomly selecting the same proportion of parameters with lower FI values"; Section 3.3: "protecting low-FI channels" / "random protection"). The paper claims theoretical advantages over the Jacobian norm (invariance) and criticizes Hessian-based approaches for computational overhead, yet never tests whether FI empirically outperforms simpler alternatives such as gradient magnitude, diagonal Fisher information, Hessian trace, or weight magnitude in any of its experimental settings. Without this comparison, the claim that FI offers *practical* advantages over existing tools is unsubstantiated — the observed effects (high-FI parameters cause performance drops when perturbed) could equally be captured by a simpler measure. The sparsification experiment shows FI works, but not that it works *better* than what already exists.

- **External perturbation analysis is a single illustrative example, not a systematic evaluation (Section 3.1).** The VLM pixel vulnerability study uses one image from ScienceQA and one model (Qwen-VL). The paper draws substantive conclusions ("This empirical finding demonstrates the usefulness of FI in detecting vulnerable inputs for VLMs"; "not all areas covering these relevant objects are equally vulnerable") from this single example. No quantitative metrics (attack success rate over multiple images, comparison to random masking or other saliency methods like Grad-CAM), no evaluation across diverse images or models, and no aggregate statistics are provided. The cross-modal prompt analysis (aggressive vs. safe prompts) is similarly qualitative. While the paper frames this as "an example" (contribution ii), the conclusions drawn from it exceed what a single anecdote can support.

### Minor

- **No error bars, confidence intervals, or multiple-trial statistics reported.** Across all experiments (sparsification curves in Figure 3, quantization in Figure 5, merging in Table 2), results are reported as single numbers or single curves with no indication of variance. While single-run evaluation is common in LLM sparsification literature, the lack of any statistical characterization makes it impossible to assess whether observed differences (e.g., between protection ratios in quantization) are significant or within noise.

- **Missing experimental details for the instruction-following experiment (Section 3.2).** The text describes computing per-token FI for sequence generation with L=5, N=10, and Equation 6 for aggregation, but does not explain how this aggregated sequence-level FI is translated into per-parameter importance for guiding sparsification. The mapping from the FI computed over generated tokens to the individual weight matrices being zeroed out is not specified.

- **Computational cost not reported.** The FI computation per parameter requires computing gradients and handling a metric tensor (potentially via SVD). For models up to 13B parameters, this is non-trivial, but the paper provides no runtime measurements or FLOP estimates. This makes it difficult to assess the practical trade-off between FI and cheaper alternatives like gradient magnitude.

- **Figure numbering inconsistency.** The quantization experiment text (line 185) references "Figure 5," but the defined figure captions in the parsed text are Figures 1–4. This appears to be a mismatch (possibly a parser artifact or an actual inconsistency).

### Trivial

- The paper's claim in the introduction that Hessian-based methods involve "unrealistic assumptions" is not explained or cited, making it vague. This is a minor overstatement that could be clarified.

## Nice-to-Haves

- **Empirical demonstration of the invariance benefit.** A controlled experiment where model parameters are rescaled (e.g., multiplying weights in one layer by k while dividing the next layer's weights by k, per the ReLU homogeneity example in Equation 3) and showing that FI ranks are stable while Jacobian norm ranks change would directly validate the claimed advantage.
- **Systematic VLM evaluation.** Running the pixel-FI analysis on a benchmark (e.g., 50–100 images from ScienceQA or MMVP) with aggregate metrics (accuracy drop under masking) and comparing to random masking and a baseline saliency method (e.g., Grad-CAM) would significantly strengthen Section 3.1.

## Removed Points

**Points from reviewers that were removed or downgraded with justification:**

1. *"Missing crucial experimental details — Table 1/Table 2 content not visible, benchmark names not listed"* — **REMOVED.** Tables and figures in the parsed text are image placeholders (the parser strips rendered content). The originals contain this information. Do not penalize the paper for parser artifacts.

2. *"Reproducibility: hyperparameters not specified, code not released"* — **REMOVED per hard rules:** hyperparameter details and code release are nitpicks that do not affect the review of the paper's scientific content.

3. *"The paper should not be accepted in its current form" (harsh critic's bottom-line conclusion)* — **Not removed as a point, but re-evaluated.** The reviewer's conclusion is a judgment, not a weakness. It feeds into the overall assessment but is not a discrete weakness to include in the list above.

4. *"Missing related works"* — **REMOVED per hard rules:** I cannot verify external knowledge about what related works exist or do not exist.

5. *"Scalability not discussed"* — **DOWNGRADED from Major to Minor and merged** with the computational cost point above. The reviewer's broader concern about scalability is fair but the paper does discuss the low-rank SVD solution for large models; what's missing is runtime numbers.

6. *Strength Finder's claimed strengths about "identification of fragile input pixels" and "practical utility"* — **KEPT but qualified.** These are genuine strengths, but the external perturbation strength is tempered by the single-example limitation, and the practical utility strength is tempered by the lack of baseline comparisons. They remain valid as stated.

## Novel Insights

The most interesting observation that emerges from synthesizing the reviews is a structural tension in the paper: the theoretical framework (FI with reparameterization invariance) is genuinely novel and well-motivated, but the experimental evaluation is designed as if to prove FI works in an absolute sense (better than random), while the paper's positioning in the introduction and the theoretical claims implicitly invite comparative evaluation (better than Jacobian norm, better than Hessian-based methods). The harsh critic correctly identifies this mismatch. The paper would be more coherent if it either (a) explicitly scoped its empirical claims to "FI identifies sensitive components" without claiming practical superiority, or (b) added comparative experiments to substantiate the implied superiority. The sparsification experiment's very large effect size (75% drop at 2–3% sparsification) is the strongest piece of evidence and suggests FI is indeed capturing something real — the question is whether simpler measures capture the same thing at lower cost.

## Suggestions

1. **Most important: add at least one baseline comparison** in the sparsification experiment (Section 3.2). Compare FI-guided sparsification to gradient-magnitude-based sparsification and/or weight-magnitude-based sparsification. This directly addresses the central weakness. If FI selects meaningfully different parameters and causes a larger accuracy drop at the same sparsity level, the case for FI is much stronger.

2. **Replace the single VLM anecdote with a small systematic study.** Run the pixel-masking experiment on 20–50 images from ScienceQA, report average accuracy drop with FI-guided masking vs. random masking and a simple baseline (e.g., gradient-based saliency). Even a small-scale quantitative evaluation would dramatically improve Section 3.1.

3. **Design an experiment that directly validates the invariance property.** Take a ReLU network, rescale consecutive layers (k, 1/k), compute FI and Jacobian norm before and after, and show that FI maintains consistent rankings while the Jacobian norm changes. This would turn a theoretical advantage into a demonstrated one.

4. **Add error bars or report results across 3–5 random seeds** for at least the sparsification and quantization experiments. Even if the trends are clear, variance information is standard scientific practice.

5. **Report computational cost.** Provide wall-clock time or FLOPs for computing FI on a 7B model vs. computing gradient magnitude or diagonal Fisher. This helps readers assess the practical trade-off.
