- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have a thorough understanding of the paper and can cross-check all reviewer claims against the actual text. Let me synthesize the final review.

---

## Summary

This paper proposes CVXQ, a weight quantization framework for LLMs that formulates the bit allocation problem as a constrained nonlinear least-squares problem, uses rate–distortion theory to approximate gradients, and solves the resulting allocation via dual ascent (water-filling). The method adds companded quantization matched to Laplace-distributed weights, bias correction for non-zero mean errors, and a matrix-partitioning scheme with theoretical analysis via Jensen's inequality. Experiments are conducted on OPT (125M–66B) and LLaMA-2 (7B–70B) models at 3–4 bits, comparing to RTN, GPTQ, AWQ, OWQ, and QuIP.

## Strengths

- **Principled optimization formulation for mixed-precision quantization**: The paper formulates LLM weight quantization as a constrained least-squares problem (Equation 3), derives optimality conditions via Lagrangian duality (Equation 4), and solves it with a dual-ascent procedure. This provides a cleaner theoretical framing than the purely heuristic or fine-tuning-based approaches in GPTQ and AWQ, and it explicitly addresses the combinatorial challenge of per-channel bit allocation.

- **Computationally efficient algorithm**: By leveraging a closed-form gradient approximation from rate–distortion theory (Equation 5), the method avoids backpropagating through the non-differentiable quantization step. The dual-ascent update (Equation 6) converges in tens of iterations, making post-training quantization practical — the paper reports minutes for billion-parameter models. A speed benchmark on a single OPT-175B weight matrix shows 3.8× speedup over FP16.

- **Companded quantization tailored to LLM weight distributions**: The sigmoid-based companding transform (Equation 8) derived from the Laplace CDF reduces quantization error at low bit depths compared to uniform RTN (Figure 2), and the paper treats scale/mean as efficiently tunable hyperparameters.

- **Theoretical analysis of matrix partitioning (Equation 9)**: Using Jensen's inequality, the paper proves that per-column or per-row quantization yields non-negative bit-rate savings, providing a formal justification for the grouping strategies used in AWQ and GPTQ. This moves beyond purely empirical grouping.

- **Robustness to hyperparameter choices**: Table 2a–b shows model accuracy is largely insensitive to minibatch size (over a 4× range) and token count (over a ~6× range), and Figure 5 demonstrates monotonic convergence within ~20 iterations. This is practically useful.

## Weaknesses

### Major

- **The central evidence for practical value on large models is very weak, and the paper's primary defense is not clearly supported.** The paper reports perplexity gains of only 0.00–0.01 for 3-bit OPT-66B and LLaMA-2-70B over baselines (line 150). This is a straightforward, honestly reported result. However, the paper's argument that small perplexity gains still matter because RTN degrades downstream accuracy (line 294) is **not verifiably supported by the parsed evidence**. The paper asserts "RTN-quantized models lead to severely reduced accuracy on downstream tasks such as GSM8K" but the table reference (Table 4(a)) describes pruning percentages, not downstream scores. Table 4c (common-sense QA) is present but appears to report only CVXQ scores — baseline comparisons (RTN, GPTQ, AWQ) are not visible in the parsed text. For the models that practitioners care about most (66B+), the paper does not provide a clean, end-to-end downstream comparison that demonstrates CVXQ's advantage over simpler methods. This is the paper's most significant gap.

### Minor

- **The "convex optimization" framing is somewhat overstated for what the algorithm actually does.** The objective (3) is not convex in the discrete bit depths; the paper relaxes this to continuous variables. The critical gradient approximation (Equation 5) is imported from rate–distortion theory under a "sufficiently high bit depth" assumption (line 82) that is explicitly violated at 3–4 bits. The resulting primal update (6) reduces to a standard water-filling formula (well-known in compression since Orchard & Bouman, 1992; Shoham & Gersho, 1988). While these observations do not invalidate the method's practical utility, the paper's theoretical novelty is less than the "convex optimization" framing suggests.

- **Scalability results don't match the abstract's claim.** The abstract states CVXQ "scales to models containing hundreds of billions of weight parameters." However, full-model perplexity/accuracy results are only shown for models up to 70B parameters. The only evidence for >70B is a speed benchmark on a single weight matrix from OPT-175B (line 296). A full-model perplexity or accuracy result for a model in the 100B+ range would substantiate this claim.

- **Several algorithmic details are underspecified for reproduction.** The PCA projection dimensionality $E'$, subsampling factor $L'$, and learning rate $\beta$ for gradient variance accumulation (Equation 7) are not reported. The companding parameters in Equation 8 are described as tunable on "coarse 1D grids" but the grid ranges and procedure are not given. These details are needed for reproducibility.

- **The equal-variance assumption across layers ($H_1 = \cdots = H_N$) is stated but not verified** (line 88). The paper argues that these constants cancel out under this assumption, but does not check whether actual weight distributions across layers are similar enough for this to hold.

### Trivial

- The paper contains a reference inconsistency: line 294 claims RTN degrades GSM8K accuracy and points to "Table 4(a)," but Table 4(a) is described as reporting pruning percentages, not downstream task scores. This appears to be a cross-reference error or a parser artifact.

## Nice-to-Haves

- An ablation that isolates the dual-ascent bit allocation by comparing it against a simpler heuristic (e.g., uniform allocation or variance-based allocation) while keeping companding and clustering fixed. Table 2d currently compares RTN → RTN+mixed precision → RTN+mixed precision+companding, which does not directly test the allocation algorithm itself.
- Perplexity and downstream results with total bit rate (weight bits + overhead) explicitly equalized across methods, to remove any ambiguity about the comparison.

## Removed Points

These points from the reviewers were flagged for removal. Treat them with caution:

- **"Unfair comparison because effective bit rates are not matched"** (Harsh Critic point 2): The paper explicitly notes (line 150) that AWQ uses 2–4× more overhead bits and OWQ operates at 0.01–0.05 higher bit depths than CVXQ. The asymmetry thus **favors the baselines** (they receive higher total bit budgets), not the proposed method. This criticism misunderstands the direction of the asymmetry and is removed per the rule that asymmetries favoring baselines do not constitute unfair comparisons.

- **"No experiment on models above 70B"** partial removal: The Harsh Critic claims the abstract's scalability claim is completely unsupported, but the paper does present a speed benchmark on an OPT-175B weight matrix (3.8× speedup, line 296) and discusses scaling the method. The criticism that full-model perplexity results don't go beyond 70B is retained as a minor weakness, but the stronger claim of "no evidence whatsoever" is removed.

- **"Companding function presented without derivation"**: The paper does provide a derivation — it states the function is the normalized cubic root of the Laplace CDF (line 119–122). The reviewer missed this explanation.

- **Formatting/parser artifact complaints** (OCR issues like "Xis"): These are parser errors, not author errors, and are removed per the hard rules.

- **Generic scope-creep criticisms** requesting additional models/tasks beyond what is standard: These are weakened to nice-to-haves where applicable.

## Novel Insights

None beyond the paper's own contributions. The reviewers raised useful criticisms and clarifications but did not surface a novel perspective that the paper itself does not contain.

## Suggestions

1. **Provide a clean downstream comparison table** that includes RTN, GPTQ, and AWQ baselines alongside CVXQ on GSM8K, ARC, HellaSwag, etc. for at least one large model (70B). This is the single most important addition — it would either substantiate or refute the paper's central argument that small perplexity gains still yield important downstream benefits.

2. **Report results with explicit total bit rate** (weight bits + overhead bits) for all methods in the main table, so readers can verify that comparisons are at matched total budgets.

3. **Add an ablation isolating the bit allocation algorithm**: replace the dual-ascent water-filling with a simpler heuristic (e.g., uniform allocation or log-variance allocation) while keeping companding and clustering fixed, to demonstrate the incremental value of the convex optimization machinery.

4. **Specify the missing hyperparameters** (PCA dimension $E'$, subsampling ratio $L'$, variance accumulation learning rate $\beta$) in a revised version or supplement.

5. **Verify or relax the equal-$H_n$ assumption** across layers by plotting the empirical weight distribution per layer for a representative model.
