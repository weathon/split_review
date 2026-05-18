Now I have thoroughly examined the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes two loss terms for improving generalization in regression tasks: (1) a relational contrastive loss \(L_{std}\) that minimizes the standard deviation of the feature-label distance ratio \(d_r(f_i,f_j) = d(f_i,f_j)/d(y_i,y_j)\) across batch pairs, and (2) a spectral norm alignment loss \(L_{svd}\) that aligns the largest singular values of feature matrices from real and C-Mixup-synthesized domains. The paper evaluates on eight benchmark datasets covering in-distribution and out-of-distribution settings, reporting competitive results.

## Strengths

- **Novel combination of two complementary losses for regression generalization**: The paper identifies two distinct challenges — stabilizing the feature-label distance ratio and aligning feature representations across domains — and proposes a loss for each. This two-pronged approach is a sensible decomposition of the problem, and the MPI3D results (Tables 3–4) provide direct evidence that spectral norm alignment outperforms alignment with Frobenius or nuclear norms, confirming that the choice of norm matters empirically.

- **Consistent empirical gains across a diverse set of benchmarks**: On eight datasets spanning tabular, time-series, image, and drug-discovery domains, the proposed method achieves best or second-best performance in the majority of cases under both ID and OOD settings. The evaluation includes both average and worst-domain OOD metrics, which is a meaningful robustness indicator.

- **The t-SNE visualization provides qualitative support for the L_std loss**: Figure 1 shows that the feature embedding trained with \(L_{std}\) produces more discriminative patterns with less variance compared to baselines (MSE-only, RML, RankSim), making the method's behavior interpretable.

- **Sensitivity analysis for hyperparameters**: Figure 2 explores \(\alpha\) and \(\beta\) across a wide range (\(10^{-9}\) to \(10^{4}\)) on two datasets, providing practical guidance for tuning the combined objective.

## Weaknesses

### Major

**1. Theorem 1 requires an invertibility condition that does not generally hold for regression layers.**  
The proof of Theorem 1 writes \(\|f_i-f_j\|_p = \|W_p^{*-1}(y_i-y_j)\|_p\), which assumes the optimal weight matrix \(W_p^*\) is square and invertible. In standard regression settings, \(W_p^*\) is an \(M \times D\) matrix (output dimension \(M\), feature dimension \(D\)). For scalar regression (\(M=1\)) or multi-output regression with \(M \ll D\), the matrix is not square and its inverse does not exist. The paper provides no discussion of this issue or any workaround (e.g., using the pseudoinverse, which would not yield the claimed inequality in general). This undermines the theoretical motivation for \(L_{std}\) as presented. While the loss itself remains empirically defined and may still be useful, the theoretical justification is flawed and needs substantial revision.

**2. The fine-tuning protocol creates a confounding factor that is not adequately controlled.**  
The paper adopts a specific fine-tuning (FT) strategy on top of a C-Mixup pretrained network for all experiments except MPI3D. However, the baselines reported in Tables 1 and 2 (C-Mixup, ERM, etc.) are taken from the original papers or reproduced without this FT protocol. The only baseline run with FT is "FT + RML" (Table 1). This means the improvement of "FT + L_std + L_svd" over C-Mixup and other baselines could be partially or entirely attributable to the FT strategy rather than the proposed losses. The MPI3D results (Tables 3–4), which explicitly do NOT use FT, partially mitigate this concern — but this is only one dataset. Without ablating the FT contribution on at least one additional dataset (e.g., RCF-MNIST or DTI), the claim that the proposed losses are responsible for the gains is not convincingly supported.

**3. The theoretical connection between spectral norm alignment and distribution discrepancy is heuristic rather than rigorous.**  
Theorem 2 relates distribution discrepancy to the difference in output Frobenius norms. The paper then argues that the output Frobenius norm is bounded by an expression involving the spectral norm of the feature matrix (via the weight matrix), and concludes that aligning feature spectral norms can reduce discrepancy. However, several gaps remain: (i) the bound depends on learned weight matrices \(W\) and biases \(b\), which are not controlled; (ii) the bound is an upper bound, so aligning spectral norms does not necessarily tighten it; (iii) the chain from Theorem 2 (output norms) to the proposed loss \(L_{svd}\) (feature matrix singular values) is not formally established. The MPI3D empirical comparison showing spectral > Frobenius > nuclear norm is valuable, but the paper's theoretical framing oversells what is actually a heuristic alignment strategy.

### Minor

**4. The \(L_{std}\) formula is missing the squared term inside the sum.**  
Equation (line 132) writes \(L_{std} = \sqrt{\frac{1}{N_b^2-1} \sum_i \sum_j (d_r(f_i,f_j) - \bar{d}_r)}\). A standard deviation requires \((d_r - \bar{d}_r)^2\) inside the sum. This appears to be a typo — the surrounding text describes minimizing "standard deviation" — but the error should be corrected. Additionally, the paper does not discuss numerical stability: when \(d(y_i,y_j)\) is very small (common in regression with dense, continuous labels), \(d_r\) can become arbitrarily large, potentially causing instability. Some discussion of regularization (e.g., adding a small constant to the denominator) would strengthen the paper.

**5. Hyperparameter values for \(\alpha\) and \(\beta\) are not reported for the main experiments.**  
The sensitivity analysis (Figure 2) explores a wide range, but the actual values used in Tables 1–4 are never stated. The paper says "we analyze the trend" and "we follow Cha et al. (2021) for hyper-parameter seed selection" on MPI3D, but does not specify the chosen \(\alpha, \beta\) values for any dataset. This is a reproducibility concern, especially since the sensitivity analysis shows strong dependence on these parameters.

### Trivial

- The phrasing "freeze the top of the C-mixup pretrained network (excluding the last block and the linear layers)" followed by "only fine-tune the bottom layer" is ambiguous — "top" and "bottom" are used in conflicting ways. The intended meaning (freeze everything except the last block and linear layers) becomes clear from context but should be stated directly.
- Standard deviations for results averaged over three seeds are not reported in the tables, making it difficult to assess the significance of improvements.

## Nice-to-Haves

- An ablation on at least one non-MPI3D dataset that removes the FT strategy entirely, to isolate the effect of \(L_{std}\) and \(L_{svd}\) from the fine-tuning protocol.
- A diagnostic plot showing how the distribution of \(d_r\) changes with \(L_{std}\) (e.g., does the variance actually decrease without collapsing all structure?), which would help reconcile the claimed "proportion is a mapping function" framing with the variance-minimization objective.
- Direct comparison of \(L_{std}\) alone vs. \(L_{svd}\) alone on all OOD datasets (currently only partially reported via MPI3D).

## Removed Points

These points were flagged by reviewers but removed or downgraded after verification against the paper:

- **"L_std is self-contradictory because it minimizes variance while claiming proportion varies"** — This is a strawman. The paper claims the proportion is not CONSTANT (unlike RML's hard assumption), and applies a soft variance penalty. There is no contradiction between "this quantity can vary" and "we regularize its variation." The concern about potentially suppressing meaningful structure is valid but belongs in Nice-to-Haves, not as a structural flaw.

- **"Freezing top vs bottom phrasing" framing as a serious ambiguity** — After careful reading, the intended meaning (freeze everything except the last block and linear layers) is recoverable. This is a trivial clarity issue at most.

- **"O(N²) pairwise cost is costly"** — Batch sizes in regression are typically small enough that this is not a practical concern for the reported experiments.

- **Various pure formatting/style nitpicks and concerns about missing appendix sections** — These are parser artifacts, not author errors.

- **The claim that Proof of Theorem 2's \(\mathcal{L}(h',h) = \mathcal{L}(h-h',0)\) is not justified** — The paper states that \(L\) is MSE loss, for which this identity holds (since \(\|h(x)-h'(x)\|^2 = \|(h-h')(x)-0\|^2\)). The remark is correct but could be more explicit.

## Novel Insights

The most interesting finding to emerge from the intersection of the reviewer critiques is the tension between the paper's two main theoretical claims: Theorem 1 requires an invertible weight matrix to bound \(d_r\), and Theorem 2's bound involves output norms that are then connected to feature spectral norms through a different set of uncontrolled weights. Neither theoretical pillar is fully self-contained, and together they reveal that the paper's contributions are fundamentally empirical — the losses work on benchmarks, but the claimed theoretical grounding is substantially weaker than presented. A stronger version of this paper would either simplify the theoretical claims to match the heuristic nature of the arguments, or rework them to avoid the invertibility issue and tighten the spectral norm connection.

## Suggestions

1. **Fix Theorem 1**: Explicitly state the invertibility assumption and discuss when it approximately holds (e.g., when \(M = D\) and the weight matrix is full rank), or replace the inverse bound with a more general inequality that works for non-square matrices. Alternatively, reframe the theoretical contribution as a heuristic motivation rather than a formal theorem.
2. **Control for the FT confound**: Re-run at least the main baseline (C-Mixup) with the same FT protocol on one additional dataset (e.g., RCF-MNIST or DTI) to demonstrate that the gains come from the losses, not the FT strategy. If FT is essential, acknowledge it as part of the method package and justify it.
3. **Report hyperparameter values**: State the specific \(\alpha, \beta\) values used for each dataset and the selection procedure (e.g., held-out validation split).
4. **Fix the \(L_{std}\) formula**: Add the missing square and discuss numerical stability (e.g., adding a small epsilon to the denominator).
5. **Tone down the theoretical claims**: Acknowledge that the connection between \(L_{svd}\) and distribution discrepancy is heuristic; the MPI3D empirical results provide sufficient justification on their own.

## Score and Decision

The paper tackles an important underexplored problem (generalization in regression) and proposes two plausible loss terms with consistent empirical support across multiple benchmarks. However, the theoretical justification contains a non-trivial mathematical error (invertibility assumption in Theorem 1), the experimental setup has a confounding factor that is not properly controlled (FT protocol), and several reproducibility details are missing (\(\alpha, \beta\) values, standard deviations). These are substantial issues that require correction. With revisions addressing these concerns, this work could be a solid contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>