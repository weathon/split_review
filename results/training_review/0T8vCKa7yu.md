Now I have a thorough understanding of the paper and can verify each claim. Let me produce the consolidated review.

## Summary

This paper proposes CVXQ, a post-training weight quantization method for LLMs that frames mixed-precision bit allocation as a constrained rate–distortion optimization problem. The key ideas are: (1) a Lagrangian relaxation of the bit-depth allocation problem using a rate–distortion approximation \(d_n(B_n)=G_n^2 S_n^2 2^{-2B_n}\), (2) a dual-ascent algorithm that alternates between updating bit depths via a water-filling formula and recomputing per-layer gradient variances, (3) companding scalar quantization for non-uniform weight distributions, and (4) bias correction for systematic quantization error. The method is evaluated on OPT (125M–66B) and Llama-2 (7B–70B) at 3–4 bits, reporting perplexity on WikiText-2 and C4 and accuracy on commonsense QA tasks.

## Strengths

- **Principled optimization formulation for mixed-precision quantization.** The paper formalizes bit allocation as a constrained least-squares problem (Eq. 3), derives optimality conditions from the Lagrangian (Eq. 4), and solves via dual ascent. This provides a cleaner theoretical framing than the heuristic sensitivity metrics used in many prior methods. (Section 3, Algorithm 1)

- **Fast convergence and scalability.** The dual-ascent procedure converges within ~20–30 iterations (Figure 5), enabling quantization of billion-parameter models in minutes and 10–100B models in hours. This is a genuine practical advantage. (Section 3, Figure 5)

- **Theoretical analysis of matrix partitioning benefits.** The paper derives the exact bit savings from column/row partitioning via Jensen’s inequality (Eq. 9, Figure 3), providing a principled justification for fine-granularity mixed-precision allocation. (Section 3.3)

- **Companding quantization adapted to LLM weight distributions.** The sigmoid-based companding (Eq. 8, derived from the Laplace CDF) reduces quantization error for the light-tailed weight distributions common in LLMs; the ablation (Table 2d) attributes ~0.5 perplexity reduction to this component. (Section 3.2)

- **Bias correction mechanism.** CVXQ updates layer biases using the running mean of inputs multiplied by weight quantization error, mitigating the systematic bias that can degrade accuracy. (Section 3.2, Algorithm 1)

- **Broad evaluation scale.** Experiments span 8 model sizes (OPT 125M–66B, Llama-2 7B–70B) at multiple bit depths (3–4 bits), with comparisons against RTN, GPTQ, QuIP#, OWQ, and AWQ, plus ablations and downstream QA results. (Tables 1, 3, 4c)

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled bit-rate comparisons undermine quantitative claims.** The paper acknowledges that AWQ uses 2–4× more overhead bits (group size 128 vs. CVXQ’s 512/256) and that OWQ operates at 0.01–0.05 higher per-weight bit depths, yet still presents perplexity numbers as head-to-head comparisons. Because these overhead differences directly affect effective bit rate, the claimed superiority of CVXQ is not conclusively established—no experiment matches average bit rate (including overhead) across methods. (Lines 150–151)

2. **Negligible gains on practically relevant model scales.** For 3-bit OPT-66B and Llama-2 70B, CVXQ’s perplexity improvements over the best baseline are 0.00–0.01. For 4-bit Llama-2 7B, CVXQ (5.35) is *worse* than QuIP (5.32). The only substantial gain (4.55 perplexity reduction) is on OPT-125M, which the paper itself calls “too limited for practical use.” The core claim of “optimum quantization outcomes” is not well-supported at the scales that matter most. (Table 1, lines 150, 294)

3. **Missing relevant baselines.** While the paper compares against QuIP# (Chee et al., 2024), it omits AQLM (Egiazarian et al., 2024) and SpQR (Dettmers et al., 2023) from the experimental comparison, despite citing both in the text. These are standard SOTA methods for LLM quantization at 3–4 bits, and their absence leaves the comparison set incomplete. (Lines 27–29, 58)

### Minor

4. **Rate–distortion approximation is unvalidated.** The core optimality condition relies on the approximation \(d_n(B_n) = G_n^2 S_n^2 2^{-2B_n}\), which assumes optimal scalar quantization of i.i.d. sources (Gersho & Gray). The paper does not empirically verify whether this approximation holds for actual LLM weight matrices or their output sensitivity, so it is unclear how far the “optimal” allocation is from the true optimum. (Eq. 5, lines 82–88)

5. **Downstream evaluation is incomplete.** The paper claims RTN-quantized models fail on GSM8K but does not show CVXQ’s own GSM8K results. Downstream accuracy is reported only for 3-bit Llama-2 on a set of commonsense QA tasks (Table 4c), with no results for OPT models or 4-bit settings. This makes it hard to assess whether CVXQ preserves accuracy on challenging reasoning tasks. (Lines 233, 294)

6. **Ablation study is underspecified.** Table 2(d) describes ablations as “starting with RTN and adding different components (Jeon et al., 2023)” without naming the components, making it impossible to determine which individual techniques contribute how much to the final performance. (Line 218)

7. **“Convex optimization” framing is slightly overstated.** The original problem (3) is non-convex due to discrete \(B_n\). Convexity only holds after the discrete relaxation and the rate–distortion approximation are applied. The paper acknowledges the relaxation but the title and framing could mislead readers about the nature of the theoretical guarantees. (Lines 63–74)

### Trivial

8. Variable naming inconsistency between Algorithm 1 and the main text: the dual update step size is called \(\alpha\) in the text (line 96) but \(\beta\) in Algorithm 1 (line 56, step 13).

## Nice-to-Haves

- Fair bit-rate comparison controlling for overhead structure across methods.
- Validation of the rate–distortion approximation by comparing predicted vs. measured per-layer distortion.
- GSM8K results for CVXQ and all baselines to support the claim about downstream accuracy.
- End-to-end latency measurements on actual LLM inference (the paper reports only a single matrix–vector kernel speedup).
- Comparison with AQLM and SpQR.
- Evaluation on more recent architectures (Llama-3, Mistral).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *“Missing key baseline: QuIP#”* — The paper’s experiments **do** include QuIP (Chee et al., 2024), which is QuIP#. This criticism is factually wrong. REMOVED.
- *“No derivation/comparison for compander”* — The companding function is explicitly derived as the normalized cubic root of the Laplace CDF. Requesting a multi-compander comparison is scope creep. REMOVED.
- *“No standard errors or multiple runs”* — Single-run evaluation is standard for large-scale LLM quantization benchmarks. Not a flaw in this field. REMOVED.
- *“GPTQ fine-tuning characterization is misleading”* — The paper’s characterization of GPTQ as involving weight updates during calibration is defensible and standard in the literature. REMOVED.
- *“No end-to-end latency”* — The paper clearly specifies it measures a single mat-vec kernel. The criticism asks for something outside the paper’s stated scope. REMOVED.
- *“Pruning/generalization claim lacks evidence”* — The paper cites Hassibi & Stork (1992) for this connection. It is a reasonable citation, not an unsubstantiated claim. WEAKENED and moved to minor.
- *“No evidence for 1024 calibration examples claim”* — This is reported as an experimental observation, not a central claim. MINOR at most, and already absorbed into other points.

## Novel Insights

The most interesting observation emerging from these reviews is the tension between the paper’s *principled optimization framing* and its *modest empirical gains at scale*. The paper argues convincingly that mixed-precision allocation should follow from a rate–distortion optimality condition, and it provides a clean theoretical derivation. Yet at the large model scales where quantization matters most (≥7B parameters), the method offers essentially the same perplexity as RTN and GPTQ. This suggests either that the rate–distortion approximation breaks down for large models (sensitivity becomes nearly uniform across layers), or that the optimization landscape is sufficiently flat that any reasonable allocation scheme yields similar results. The paper’s strong results on OPT-125M but negligible gains on larger models hint that the relationship between bit allocation granularity and model size is non-trivial—a point worth investigating further but not developed here.

## Suggestions

1. **Re-run experiments with matched effective bit rates.** Either match AWQ’s group size (128) or adjust target bit rates to account for overhead differences. Without this, the quantitative comparisons are not interpretable.

2. **Include AQLM and SpQR as baselines** to benchmark against the current SOTA for 3–4 bit LLM quantization.

3. **Provide GSM8K results** for CVXQ and all baselines to substantiate the downstream accuracy claims.

4. **Validate the rate–distortion approximation** by plotting predicted vs. measured per-layer distortion for at least one medium-sized model (e.g., OPT-13B).

5. **Name the ablation components in Table 2(d)** so readers can assess the contribution of each technique independently.

6. **Tone down the “convex optimization” framing** or explicitly acknowledge that convexity applies only to the relaxed, approximated problem.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>