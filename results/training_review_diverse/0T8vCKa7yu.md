Now I have sufficient evidence from the paper to verify all claims. Let me write the consolidated review.

## Summary

This paper (Part 1 of a three-part series) presents CVXQ, a weight quantization method for LLMs that formulates mixed-precision bit allocation as a constrained optimization problem (minimizing output distortion subject to a bit budget), solves it via dual ascent using closed-form derivative approximations from rate–distortion theory, and adds companded quantization, bias correction, and matrix partitioning. The approach is evaluated on OPT and Llama-2 models up to 70B parameters, reporting perplexity on WikiText2 and C4.

## Strengths

1. **Principled convex optimization formulation for bit allocation.** The paper reframes weight quantization as a constrained least-squares problem (Eq. 3) with a Lagrangian dual solution (Eq. 4–6), providing a theoretically grounded alternative to heuristic or Hessian-based allocation methods. The dual ascent update (Eq. 6) with the closed-form derivative approximation from rate–distortion theory (Eq. 5) yields an algorithm with clear optimality conditions (Section 3.1, Algorithm 1).

2. **Strong empirical results on small to medium LLMs.** On WikiText2, CVXQ achieves a perplexity reduction of up to 4.55 over the next best method for 3-bit OPT-125M (28.14 vs. 32.69 for GPTQ) and consistently matches or outperforms GPTQ, AWQ, OWQ, and QuIP across OPT-1.3B to OPT-13B at both 3 and 4 bits (Table 1).

3. **Comprehensive ablation and sensitivity analysis.** The paper systematically ablates minibatch size, token count, cluster size, and individual components (mixed precision, companding, bias correction), showing that the method is largely insensitive to optimization hyperparameters (Table 2a–b) and that each component contributes to accuracy (Table 2d, Figure 5).

4. **Matrix partitioning with a provable savings guarantee.** The paper derives a closed-form expression for bit savings from column/row partitioning (Eq. 9) and proves non-negativity via Jensen's inequality, providing a principled basis for fine-grained mixed-precision allocation.

5. **Companded quantization for LLM weight distributions.** The use of a Laplace-CDF-based companding function (Eq. 8) with efficient lookup-table dequantization is well-motivated by the heavy-tailed nature of LLM weights (Figure 2) and shown to improve accuracy in ablations (Table 2d).

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled effective bit rate in baseline comparisons.** The paper acknowledges (line 150) that "AWQ uses a group size of 128, incurring 2–4 times as many overhead bits as the proposed method, and OWQ by its nature operates at average per-weight bit depths that are 0.01–0.05 bits higher than proposed." However, it never reports the actual achieved average bit depth (including overhead) for any method, nor does it control for this in the comparison. Since perplexity improves with more bits, the claimed gains of 0.00–0.01 for large models (OPT-66B, Llama-2 70B) could be fully explained by the bit-rate discrepancy. The paper's central claim of superiority cannot be properly evaluated without controlling for effective bit rate. This is the most consequential weakness.

2. **Missing downstream task comparisons against baselines.** The paper criticizes RTN on GSM8K (line 294: "RTN-quantized models lead to severely reduced accuracy on downstream tasks such as GSM8K") and lists downstream tasks in the experimental setup (GSM8K, ARC, HellaSwag, PIQA, Winogrande, line 148). Yet Table 4(c) shows only CVXQ's results on these tasks with no comparison to GPTQ, AWQ, OWQ, or QuIP. Without baseline comparisons, this evidence neither supports CVXQ's advantage nor substantiates the criticism of RTN.

3. **Missing runtime and memory measurements.** The paper claims "in minutes for billion-parameter models and in a few hours for 10–100-billion-parameter models" (line 18) but provides no wall-clock timing data for the quantization process. The single kernel speedup number (3.8× for OPT-175B's largest matrix, line 296) is not a substitute. Given that the method requires backpropagation through the full model (line 7–10 of Algorithm 1), a direct runtime comparison with calibration-only methods (GPTQ, AWQ) is essential to support the practicality claim and the stated motivation of suitability for activation quantization.

### Minor

1. **The surrogate distortion model (Eq. 5) is not directly validated.** The derivation replaces the true distortion derivatives with a closed-form rate–distortion approximation (Eq. 5) based on three assumptions: high enough bit rate that the half-error-per-bit law holds, similarly distributed weights across layers, and a linearization of the network. The paper never tests whether this approximation matches the true distortion for any model or layer. While the perplexity results provide indirect empirical validation, the "optimum" claim in the abstract would be significantly strengthened by a direct comparison of the surrogate's predictions against actual measured distortion.

2. **Reference error.** The paper states "RTN-quantized models lead to severely reduced accuracy on downstream tasks such as GSM8K (Table 4 (a))" (line 294). However, Table 4(a) reports pruning percentages of zero-quantized weights, not downstream accuracy. The downstream results appear elsewhere (Table 4c). This cross-reference is incorrect.

3. **Notation inconsistency.** The symbol α is used for both the running-mean EMA update rate in the gradient variance accumulation (h line 51 — $"&#92;alpha"$ in $"G_n^2 &#92;gets (1-&#92;alpha) G_n^2 + (&#92;alpha/P_n)..."$) and for the dual ascent step size (line 96: "step size α=2"). These are distinct quantities, and reusing the same symbol is confusing.

4. **No variance or statistical significance reported.** All perplexity results are reported as single numbers without standard deviations or confidence intervals. While single-run evaluation is common in LLM quantization, some indication of stability across calibration samples would improve credibility.

5. **The theoretical connection between the Lagrangian optimality conditions (Eq. 4) and the actual algorithm update (Eq. 6) is underspecified.** The paper correctly notes that the quantization function is non-differentiable (line 82) and then substitutes a surrogate derivative (Eq. 5). However, the gap between the formal Lagrangian approach on the true objective and the surrogate-driven update actually used is acknowledged but not bridged. A discussion of when this approximation is expected to break down (e.g., at very low bit depths) would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- A direct validation experiment comparing the surrogate distortion model $G_n^2 S_n^2 2^{-2B_n}$ against the true measured output distortion for a small model would significantly strengthen the theoretical claims.
- Reporting the actual average bit depth (including overhead for signaling cluster indices and scale/mean parameters) for all methods in Table 1 would resolve the bit-rate control concern.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Introduction misrepresents GPTQ/AWQ as fine-tuning weights"**: GPTQ (Frantar et al., 2022) does update unquantized weights during quantization via Hessian-based compensation, so the characterization is defensible. AWQ is not cited in the specific sentence being criticized; the critic conflated citations. Removed: Critic factually misread the paper.
- **"Bias correction missing citation to Nagel et al., 2020"**: Per policy, missing related-work citations are not verifiable with available information. Removed: violates rule on missing related works.
- **"Table 3 appears only as a fragment"**, **"Table captions not present"**: These are parser artifacts from PDF extraction, not issues in the original submission. Removed: parser artifacts.
- **"Missing reference implementation URL from abstract"**: The URL was truncated by PDF extraction (line 4 ends with "obtained from."). Removed: parser artifact.
- **"No discussion of memory overhead for per-cluster scales and means"**: The paper explicitly discusses overhead in Table 4(b) and the surrounding text (lines 226). Removed: paper already addresses this.
- **"Unacceptable delays claim not supported by citation"**: The claim about activation quantization delays is a forward-looking motivation for Part 2, not a central claim of this paper. Removed: scope creep complaint.
- **Several strength-finder strengths that are generic**: e.g., "demonstrated downstream task relevance" — the paper only shows CVXQ's own downstream results without baselines, so this is misleading as stated. Removed: conflicts with verified weakness about missing downstream baselines.

## Novel Insights

The most interesting observation from the reviews is that the paper's two strongest results are in tension with its weakest ones. The method delivers genuinely large gains on small models (OPT-125M: 4.55 perplexity reduction) but essentially ties with baselines on large models (0.00–0.01 on OPT-66B, Llama-2 70B). The paper attributes this to larger models being "more compressible in general" — but this explanation is undercut by the uncontrolled bit-rate comparison issue (AWQ/OWQ operate at higher effective bit rates). If the large-model results are truly near-identical once bit rate is controlled, then CVXQ's advantage is confined to small models, which the paper itself acknowledges are "too limited for practical use." This substantially narrows the scope of the claimed contribution beyond what the abstract suggests.

## Suggestions

1. **Report actual achieved bit rates for all methods.** Compute the true average bit rate per weight (including overhead for group indices, scales, means) for CVXQ and every baseline. Then either match bit rates across methods or show a perplexity-vs-bit-rate curve.

2. **Add downstream task comparisons against baselines.** Run GPTQ, AWQ, OWQ, and QuIP on at least 2–3 downstream tasks (ARC, HellaSwag, GSM8K) and compare with CVXQ in a single table.

3. **Report wall-clock runtime for the quantization process** on at least one model per scale (e.g., OPT-1.3B, OPT-13B, OPT-66B) to substantiate the practicality claim.

4. **Fix the cross-reference error** for GSM8K / Table 4(a).

5. **Add a brief limitations section** addressing the surrogate model's assumptions (high-bit-rate regime, identically distributed weights) and the scope of the method (weights only in Part 1, with activation quantization deferred).

## Score and Decision

**Originality**: Good — the convex optimization framing for mixed-precision bit allocation is novel, though individual components (dual ascent, rate-distortion theory, companded quantization) are adapted from prior work.

**Importance of research question**: High — LLM quantization is practically important.

**Whether claims are well supported**: Partially — the strong small-model results are well supported, but the large-model comparisons are undermined by the uncontrolled bit-rate issue, and the "optimum" claim is not fully validated.

**Soundness of experiments**: Moderate — adequate for small models, but the bit-rate control issue, missing downstream baselines, and absent runtime data weaken the overall picture.

**Clarity of writing**: Good — the paper is generally well-structured despite some notation issues.

**Value to the research community**: Moderate — the convex optimization perspective and matrix partitioning analysis are contributions, but the empirical gaps limit immediate impact.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>