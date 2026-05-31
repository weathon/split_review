Now I have sufficient information to write the final review. Let me compile everything carefully.

---

## Summary

This paper proposes HyperINF, which combines Schulz's iterative algorithm (a hyperpower method for matrix inversion) with a generalized Fisher information matrix (GFIM) approximation to efficiently compute influence function scores for data attribution on large models. On LoRA-tuned models, GFIM reduces the Hessian from a full-rank r²d² matrix to a d×d matrix, making Schulz iteration tractable. The paper presents synthetic convergence tests, mislabeled data detection, and data selection experiments on LLMs (Llama2-7B) and VLMs. HyperINF consistently outperforms baselines (LISSA, DataInf, TracIn) across most settings, particularly on VLMs where 1-epoch training is properly controlled.

## Strengths

1. **Strong convergence guarantees validated empirically**: Figure 1 shows Schulz's method converges to low Frobenius-norm error across d=512–4096 and N=200–12800, while LISSA errors explode (~10⁵) and DataInf errors scale with d. This directly supports the paper's central claim about the benefit of rigorous convergence guarantees.

2. **Consistent downstream outperformance across tasks**: HyperINF achieves the best or second-best results on mislabeled detection (5/6 GLUE tasks, Figure 2), LLM finetuning data selection (Tables 2 and 3), and VLM pretraining data selection (Table 4). The VLM experiments are particularly clean since both selected and random subsets are trained for the same number of epochs.

3. **Practical efficiency through GFIM's low-rank structure**: By exploiting the LoRA structure, GFIM reduces the Hessian from O(r²d²) to O(d²) in memory and the per-sample Hessian-gradient product from O(r²d²) to O(rd²) in computation. For r=16, this is a 256× memory reduction and 16× per-sample compute reduction versus the exact Hessian-vector product.

4. **Theoretical grounding for the Hessian approximation**: Lemma 3.1 provides a formal connection between GFIM and the Hessian under i.i.d. column assumptions on LoRA gradient matrices, giving a principled justification for replacing the full Hessian with the lower-dimensional GFIM.

## Weaknesses

### Fatal

None.

### Major

1. **Complexity analysis in Table 1 omits the Schulz iteration cost, making efficiency claims incomplete.** The paper claims complexity of O(r d² + L r d) for HyperINF in Table 1, but this only accounts for the per-sample Hessian-gradient product and does not include the one-time cost of computing the GFIM inverse via Schulz iteration. Schulz's method requires O(T d³) matrix multiplications per layer (where T ≈ 10–20 iterations; d is the LoRA dimension, e.g., 4096 for Llama2-7B). This one-time cost — on the order of tens of TFLOPs across all layers — is not listed in the table's comparison. While this cost is amortized over all training samples and GPU-friendly (as the paper notes in Appendix D.1, referencing wall-clock times), the omission creates a misleading impression in the main paper's central complexity table. **Why it matters**: The claimed complexity is the headline efficiency argument. Readers cannot assess whether HyperINF is genuinely more efficient than alternatives like DataInf (O(d)) without seeing the full cost breakdown. The paper should either add the Schulz cost to the table or clearly separate "one-time inversion cost" from "per-sample cost."

### Minor

2. **LLM finetuning data selection experiments (Table 2) compare selected subsets (5 epochs) against full-data (1 epoch), conflating data selection with training duration.** The selected 5% subset receives 5× more gradient updates than the full-data baseline. The paper transparently reports these settings and frames the comparison as a compute-efficiency argument ("20× data samples and 4× FLOPs"), so this is not deceptive. However, the claim "outperforms the full dataset" conflates two variables. The main conclusion — that HyperINF beats Random baseline (matched on epochs) — is unaffected, but the comparison to full-data training should be accompanied by a control where full data is also trained for 5 epochs, or the language should be softened.

3. **LISSA's hyperparameter configuration is unreported, raising fairness concerns about baseline comparisons.** LISSA's poor performance (near-random on mislabeled detection, severe degradation on VLM with 5% data) could stem from suboptimal settings (number of iterations, step size / damping). The paper does not describe any tuning effort for LISSA. This is a common issue in influence-function papers, but it weakens the evidence for HyperINF's superiority.

4. **The i.i.d. column assumption in Lemma 3.1 is stated without experimental verification.** The paper assumes that each column of the LoRA gradient matrix is i.i.d. with zero mean, motivated by the model being near convergence. While this is a standard idealized assumption for connecting FIM to the Hessian, the paper provides no empirical diagnostic (e.g., measuring off-diagonal correlation or column covariances on real trained models) to assess how well the assumption holds in practice.

5. **No limitations or failure-mode discussion.** The paper lacks a section discussing when HyperINF might fail — e.g., if the i.i.d. column assumption is violated, if the model is far from convergence, or if the damping factor λ is poorly chosen. This is standard practice and would strengthen the paper's scientific completeness.

### Trivial

None.

## Nice-to-Haves

- An ablation showing how the Schulz iteration count affects downstream performance on real models — the synthetic test uses random matrices, and it would be informative to see convergence behavior on real gradient-derived GFIM matrices.
- A study of sensitivity to the damping factor λ and the LoRA rank r, which jointly affect both numerical stability and computational cost.
- Statistical significance tests (beyond confidence intervals on mislabeled detection) for the LLM and VLM results.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The theoretical grounding for dense finetuning is weak"** — Removed because the paper explicitly acknowledges this limitation at line 164: *"Although the theoretical analysis in Theorem 3.1 is inspired by LoRA finetuning context, we show that data selection by HYPERINF also significantly benefits dense finetuning."* The dense finetuning results are presented as empirical findings, not theoretical claims. The criticism misunderstands the paper's own scope disclaimer.

2. **"Missing related works"** — Removed per instruction: I cannot confirm the existence/non-existence of missing references without external sources.

3. **"Missing appendix / missing proofs in appendix"** — Removed per instruction: the parser strips appendices; they exist in the original submission.

4. **"Pure formatting/style nitpicks"** — Removed per instruction.

5. **"The synthetic convergence test is tangential"** — Removed as it mischaracterizes the paper: the test directly validates the core algorithmic claim (convergence of Schulz's method for matrix inversion) that underlies the whole method.

6. **Generic strength: "This paper addressed an important problem"** — Removed per instruction to drop generic, non-specific strengths. The remaining strengths are concrete and evidence-anchored.

## Novel Insights

The harsh critic correctly identifies that the Schulz iteration's O(d³) cost per layer is absent from Table 1. However, a more interesting observation is that the GFIM matrix G = (1/r) g g^T + λI has a specific low-rank-plus-diagonal structure (rank r plus a diagonal shift). Schulz iteration applied to such structured matrices could potentially exploit this structure for faster convergence or cheaper iterations (e.g., using a better initialization informed by the rank-r factorization). The paper treats GFIM as a generic dense d×d matrix for inversion purposes, which is suboptimal — the structure could be leveraged for even greater efficiency. This is not a weakness of the current paper but an underexplored direction.

Additionally, the paper's observation that HyperINF works on dense finetuning using only the last transformer block's gradients (Table 3) — despite the LoRA-motivated theory — suggests that the GFIM approximation has broader applicability than its formal assumptions suggest. This empirical finding is perhaps more significant than the paper's presentation emphasizes.

## Suggestions

1. **Restructure the complexity analysis**: Clearly separate (a) the one-time cost of computing the GFIM inverse via Schulz iteration [O(L · T · d³), where T is the iteration count] from (b) the per-sample cost of computing influence scores [O(L · r · d²)]. Report actual wall-clock times prominently in the main paper rather than only in the appendix.

2. **Add a controlled full-data baseline**: For the LLM finetuning experiments, include results for full-data training for 5 epochs (LoRA) and 3 epochs (dense) to separate the effect of data selection from training duration. This would strengthen the claim about selection quality.

3. **Report LISSA tuning details**: Add a brief description of how LISSA was configured (iterations, damping) or note that default settings from prior work were used. This is critical since LISSA's near-random performance raises questions about fairness.

4. **Add a limitations paragraph** discussing the i.i.d. column assumption, when the method might break, and the effect of the per-sample GFIM approximation (dropping the expectation in Equation 4).

5. **Empirically verify the i.i.d. assumption**: For a representative LoRA-tuned model, compute and report the empirical correlation between columns of the gradient matrices to assess how well the assumption holds.

## Score and Decision

**Overall assessment**: The paper makes a solid contribution by combining Schulz's iteration with GFIM for influence function estimation. The core idea is sensible, the convergence benefit is convincingly demonstrated in synthetic tests, and the downstream results are consistently positive. The main weakness is the incomplete complexity analysis in Table 1, which omits the Schulz iteration's O(d³) cost and creates a misleading efficiency picture. This is a significant presentational flaw but not fatal — it can be corrected by clarifying the cost breakdown and the fact that the inverse computation is a one-time amortized cost. The LLM epoch mismatch and LISSA tuning concerns further reduce confidence slightly but do not undermine the paper's overall contributions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>