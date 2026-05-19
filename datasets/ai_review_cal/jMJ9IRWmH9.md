- Decision: Reject
- Avg Score: 3.50
- Scores: 1, 5, 5, 3
Now I have all the information I need. Let me produce the consolidated review.

---

## Summary

This paper analyzes label leakage in parameter-efficient fine-tuning (PEFT) over APIs and proposes P³EFT, a two-party split-learning protocol that combines (1) a private backpropagation scheme exploiting the linearity of backprop to distribute gradient computation across multiple servers, and (2) a mixture-of-adapters approach with adversarial regularization designed to prevent label leakage from model activations. Experiments on DeBERTa-v2-XXLarge and Flan-T5-Large on SST-2 and MRPC show that P³EFT maintains competitive accuracy with a Distance Correlation baseline at similar measured privacy levels.

---

## Strengths

- **Empirically demonstrates label leakage in standard PEFT (Section 3.1, Figure 1).** The paper provides clear visual evidence that gradients communicated during LoRA fine-tuning and trained activations both cluster by label under k-means clustering, confirming that even fine-tuning <0.1% of parameters leaks private labels. This concretely motivates the problem.

- **Core insight about exploiting the linearity of backprop for gradient privacy (Section 3.2, Algorithm 1).** The observation that backprop is conditionally linear in output gradients (Equation 1) is sound, and the multi-server protocol that distributes noise-obfuscated gradient vectors allows recovery of the true gradient client-side. The XGBoost experiment (line 187) provides empirical support: a classifier trained on the per-server noisy gradients achieves only 50.4% accuracy (chance level for a balanced binary task), suggesting these do not leak label information.

- **Evaluation on large-scale modern models.** The experiments use DeBERTa-v2-XXLarge (1.5B) and Flan-T5-Large (770M) on standard GLUE tasks, which is more demanding than the smaller models/datasets common in prior split-learning work and strengthens practical relevance.

- **Competitive accuracy vs. a prior privacy-preserving method.** Figure 4 shows that P³EFT achieves higher task accuracy than the Distance Correlation (Sun et al., 2022) baseline at comparable measured privacy levels (spectral attack AUC, norm attack AUC, logistic regression accuracy). The sensitivity analysis in Figure 5 further explores the accuracy–privacy Pareto frontier.

---

## Weaknesses

### Fatal
None.

### Major

- **The obfuscation procedure in Algorithm 1 is unspecified, preventing reproducibility and formal analysis.** Algorithm 1 calls `obfuscate(g_h, m)` to produce m random vectors and scalars summing to g_h, but provides no concrete algorithm, no constraints on how the vectors are sampled, and no analysis of what (if any) privacy guarantees the decomposition provides. A naive construction could trivially leak information; a proper secret-sharing scheme needs specification and analysis. This gap means the core privacy mechanism of the paper cannot be faithfully replicated or formally evaluated, and the claimed "provably obfuscate" (contribution list, line 32) is unsupported by any proof.

- **The adversarial regularization component is critically underspecified.** Section 3.3 describes training n linear "heads" to predict labels from individual adapter outputs and then performing an "adversarial update" of the adapters, but the paper does not specify: the exact loss function for the adversarial term (e.g., cross-entropy maximization? gradient reversal layer? alternating optimization?), the regularization coefficient balancing task accuracy and privacy, or the training loop details. The claim that this "ensures that it is impossible to predict labels from individual adapters" (line 163) is an extremely strong assertion that is unsubstantiated — adversarial debiasing reduces, but does not provably eliminate, predictive information. This component is central to the protocol's privacy guarantees, and the lack of precision is a structural issue for reproducibility and soundness.

- **Experimental evaluation is too narrow to support the advertised claims.** The method is compared against only one privacy-preserving baseline (Distance Correlation from Sun et al., 2022) plus two non-private controls (no-LoRA and unregularized LoRA). Only two datasets (SST-2, MRPC) and two model architectures are used. Privacy is evaluated via only three attack types (spectral, norm, logistic regression); stronger and more recent attacks (e.g., combined gradient-activation attacks, iterative recovery across steps, model inversion) are not considered. No variance or error bars are reported for any results, making it impossible to assess the reliability or significance of the reported accuracy and privacy numbers. A single run per configuration is insufficient, especially since adversarial training can have high variance across seeds.

### Minor

- **Practical applicability is limited by the multi-server assumption.** The private backprop protocol requires multiple independent, non-colluding servers. In the most common API scenario (a single provider such as OpenAI or Hugging Face), the server can trivially sum requests to recover g_h. The paper acknowledges this and suggests mitigations (TEEs, decentralized systems), but these are not evaluated, and no protocol variant for the single-server case is provided. This is a structural limitation that should be clearly scoped.

- **No formal privacy analysis.** Despite describing the protocol as "provably obfuscating" gradients, no information-theoretic or cryptographic privacy guarantee is provided. The privacy evaluation is entirely empirical (attack-based). While empirical attack evaluation is valuable in itself, the paper would benefit from either formal guarantees or more measured language about what is being claimed.

- **"Provably obfuscate" overclaim.** The contribution list (line 32) uses the term "provably obfuscate the gradients," but the paper provides no proof — only empirical evidence and the linearity argument (which shows correctness of gradient recovery, not privacy). The language should be calibrated to what is actually demonstrated.

### Trivial
None.

---

## Nice-to-Haves

- Comparison to DP-SGD with low noise and large batch size as a simple baseline for understanding the privacy–accuracy trade-off.
- Evaluation on additional tasks (e.g., MNLI, QQP) to strengthen generality claims.
- Specification of all hyperparameters used in P³EFT (n, m, noise variance schedule, adversarial regularization coefficient, batch size, learning rate, optimizer settings).

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The paper does not offer any workaround for this case"* (from the harsh critic's multi-server critique). The paper does mention TEEs and decentralized systems as workarounds, though they are not evaluated. Removed for factual inaccuracy.

- *"The algorithmic appendix was stripped by the parser"* remark. The parser strips appendix content from all papers; this is not a valid criticism of the submission.

- *"Training w/o LoRA adapters is not a realistic privacy baseline"* characterization. The paper presents this as a lower-bound baseline, not a privacy-preserving method, which is reasonable.

- Various generic formatting/presentation nitpicks from the harsh critic's section notes (e.g., "the gradient visualization in Figure 3 is illustrative but does not quantify privacy" — the paper does quantify via XGBoost accuracy).

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between a promising high-level approach and significant underspecification of key components, but do not identify any novel cross-paper patterns or unexpected implications beyond what the authors themselves discuss.

---

## Suggestions

- **Fully specify the obfuscate function.** Provide a concrete secret-sharing scheme (e.g., pick m-1 random vectors i.i.d. from a Gaussian, compute the last vector deterministically to satisfy the sum constraint) and analyze what information each per-server message reveals about g_h (e.g., information-theoretic indistinguishability or computational hiding). This is critical for reproducibility and privacy analysis.

- **Provide full implementation details for the adversarial regularizer:** specify whether gradient reversal or alternating minimax optimization is used, the value of any regularization coefficient λ_adversarial, the training schedule, and how the n linear heads and adapters are updated relative to each other. Show an ablation study isolating the contribution of the regularizer to privacy.

- **Add error bars and statistical significance.** Report at least 3 independent runs with standard deviation for all accuracy and privacy metrics.

- **Calibrate language.** Remove or justify the term "provably" in the contribution list, and soften the claim that the regularizer "ensures it is impossible" to predict labels to something like "reduces the ability to predict labels."

- **Address the single-server scenario directly.** Either provide a method that works with one server (e.g., sequential queries with temporal decomposition analyzed under a bounded-storage model) or clearly scope the contribution to multi-server decentralized APIs and discuss the limitation upfront.

---
