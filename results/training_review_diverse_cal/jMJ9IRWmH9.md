Now I have all the information I need. Let me produce the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

---

Let me write the full review now.

The paper proposes P³EFT, a protocol for privacy-preserving parameter-efficient fine-tuning (LoRA) over APIs. The key ideas are: (1) exploiting the linearity of backpropagation to decompose gradients into sums sent to different servers, preventing any single server from seeing the true gradient, and (2) training multiple LoRA adapters with secret mixing weights and adversarial regularization to hide label information from activations.

**Cross-verification of key reviewer claims:**

1. **"No formal privacy guarantee"** — The paper uses "provably obfuscate" (line 32). The proof shows the gradient decomposition recovers the true gradient (correctness), but the paper does not define what privacy property is guaranteed. This is a legitimate concern, though the paper does provide empirical attack-based privacy metrics.

2. **Jacobian invertibility** — The reviewer claims the paper "never analyzes the Jacobian inversion threat." But lines 123-124 explicitly state: "a server could, in some cases, use g_θ to recover g_h, either fully (e.g. if Jacobian is invertible), or partially." The paper acknowledges this but does not deeply analyze it. The reviewer overstates the absence.

3. **"No numerical results"** — Confirmed. Figure 4 and 5 are described but no accuracy/F1/AUC values are given in the text. This is a genuine weakness.

4. **DC comparison "circular"** — The paper tunes α so DC has "comparable privacy as our algorithm" measured via the same attack metrics. This is standard practice for comparing privacy-accuracy tradeoffs (matching on the y-axis), not circular. I'll weaken this.

5. **Nonlinear attacks on adapter activations** — The paper uses linear adversarial heads (line 165, 169). It never addresses whether a nonlinear attacker could extract labels from individual adapter activations. Valid concern.

6. **"One bit" claim** — Line 89 says "all but one bit of information" based only on a PCA visualization. For a binary task (1 bit total), this effectively claims near-perfect leakage. Overstated without information-theoretic analysis. Valid criticism.

7. **Missing hyperparameters** — n (number of adapters), m (noise components), noise variance, regularizer coefficient for main experiments are not stated. Valid.

8. **Missing cryptographic related work** — Per instructions, I must remove this as "missing related works" criticism.

Let me now produce the review.## Summary

This paper addresses the problem of label privacy when fine-tuning LLMs over APIs (e.g., OpenAI, Hugging Face). The authors propose P³EFT, a two-party split learning protocol that protects client training labels through two mechanisms: (1) a gradient obfuscation protocol that exploits the linearity of backpropagation to decompose gradients into noise-dominated vectors sent to separate servers, and (2) a multi-adapter mixing scheme with adversarial regularization that prevents label leakage from activations. The paper evaluates on DeBERTa-XXLarge and Flan-T5-Large on SST-2 and MRPC, reporting accuracy and privacy metrics against several attacks.

## Strengths

- **Novel exploitation of PEFT's small parameter count for privacy.** The core insight — that PEFT's compactness allows running multiple adapters with secret mixing weights — is creative and well-motivated. This distinguishes P³EFT from generic split learning defenses. The mixing weight construction (Equation 3-4) preserves the original model output at initialization while obfuscating individual adapter contributions.

- **Sound gradient obfuscation protocol with correctness guarantee.** The paper correctly observes that backpropagation is linear in output gradients (Equation 1) for fixed inputs and parameters, and uses this to decompose a gradient into recoverable components. The protocol in Algorithm 1 recovers the *true* parameter gradient, so "this obfuscation method does not affect the training dynamics" (line 136). This property is proven, not just claimed.

- **Timely and practical problem formulation.** The paper targets a realistic setting — API fine-tuning where the client owns labels and the server owns the model — and correctly identifies that standard PEFT leaks labels (Figure 1), motivating the need for defenses.

- **Empirical privacy evaluation against multiple attack types.** The paper evaluates against Spectral attack (ROC AUC), Norm attack (ROC AUC), and Logistic Regression accuracy — providing a multi-faceted empirical privacy assessment rather than relying on a single metric.

## Weaknesses

### Fatal
None.

### Major

- **Numerical results are absent from the text.** The paper's main experimental findings (Figures 4 and 5) are described only qualitatively ("nearly the same accuracy," "slightly better trade-offs"). No accuracy percentages, F1 scores, or privacy metric (AUC) values are reported numerically. For an empirical paper whose central claim is that P³EFT "has higher accuracy" than baselines, the reader cannot verify this claim or compare against future work. The figures may contain the data, but figures cannot be inspected with the same precision as tables.

- **The adversarial regularizer's defense against nonlinear attacks is unexamined.** The paper trains *linear* adversarial heads (logistic regression, line 169) that try to predict labels from individual adapter activations, then updates adapters adversarially. But the server sees individual adapter activations for all training examples and could train arbitrary nonlinear classifiers on them. The paper provides no argument — theoretical or empirical — that the linear adversarial regularizer prevents nonlinear attacks. This is a significant gap in the security analysis.

- **Missing hyperparameters for main experiments.** Key protocol hyperparameters are only specified for the preliminary experiment (Section 4.1: n=2, noise variance=1000). For the main fine-tuning experiments (Section 4.2), the number of adapters *n*, number of noise components *m*, noise variance schedule, and adversarial regularizer coefficient are not stated. This prevents reproducibility and makes it impossible to assess whether the reported privacy-accuracy tradeoffs are cherry-picked.

### Minor

- **The "provably obfuscate" claim overreaches.** The paper proves that the gradient decomposition recovers the *correct* gradient (due to linearity of backprop). But "provably obfuscate" implies a proof about what an adversary can learn, which is not provided. There is no formal privacy definition (differential privacy, computational indistinguishability, or even an explicit information-theoretic bound) in the paper. The privacy evaluation is entirely empirical (attack-based). Aligning the language with what is actually proved would strengthen credibility.

- **The "all but one bit" claim is unsupported.** Line 89 states: "From an information-theoretic perspective, knowing just one vector of gradients or trained activations allows the attacker to learn all but one bit of information about client's private labels." This claim is supported only by a 2D PCA visualization (Figure 1). For a binary task, "all but one bit" effectively means the attacker can determine the label with near certainty. This requires an information-theoretic estimate (e.g., mutual information), not a visualization. The claim should be removed or properly supported.

- **No computational overhead measurements.** The method requires *n* forward passes and *m* backward passes per example. The paper dismisses this as "negligible time compared to running the large pre-trained model" (line 169) without any timing measurements. For a practical API offering, the overhead factor (~n+m) is material and should be quantified.

- **The defense against parameter-inversion attacks across consecutive steps is proposed but not evaluated.** The paper correctly identifies that a server observing θ_t and θ_{t+1} could recover g_θ (lines 121-124). Two mitigations are suggested (non-colluding servers per step, or randomizing optimizer statistics), but neither is implemented, evaluated, or analyzed for its impact on convergence.

### Trivial
None.

## Nice-to-Haves

- An ablation study separating the contributions of (a) gradient obfuscation alone, (b) multi-adapter mixing without regularization, and (c) full P³EFT would help isolate which component drives the privacy-accuracy tradeoff.
- Standard deviations over multiple seeds in the experimental results would strengthen the quantitative claims.
- A discussion of when the method provably fails (e.g., all servers collude, or the attacker uses unrestricted nonlinear models on adapter activations) would help practitioners assess risk.

## Removed Points

These points from the reviewer inputs were removed with justification:

- **"Missing cryptographic approaches in related work"** — Per policy, missing related works criticisms are excluded as the reviewer cannot verify completeness.
- **"DC comparison is circular"** — The paper tunes DC's α so that it achieves "comparable privacy" on the same attack metrics. This is standard practice for comparing privacy-accuracy tradeoffs on a common axis, not circular. The concern is about the metrics' quality, not circularity.
- **"The paper never analyzes the Jacobian inversion threat"** — The paper *does* mention this at lines 123-124 ("a server could, in some cases, use g_θ to recover g_h, either fully (e.g. if Jacobian is invertible), or partially"). The analysis is shallow but not absent.
- **"Multiple independent servers / TEE is a massive engineering assumption"** — The paper discusses this as an option, not a claim of implementation. This is an acknowledged limitation, not a flaw in the claimed contribution.

## Novel Insights

The multi-adapter mixing scheme (Section 3.3) is the paper's most distinctive contribution and deserves more attention than it receives. The construction of mixing weights that preserve the original model's output at initialization while ensuring individual adapters diverge under different gradients is clever, and the idea of privacy-through-multiplicity (making the server see *more* information — many adapter outputs — rather than less, while ensuring each individual output is uninformative) is an interesting design choice that inverts the usual intuition. The paper's central tension is that its strongest idea (multi-adapter mixing) receives the weakest evaluation (no test against nonlinear attacks, no hyperparameter reporting).

## Suggestions

1. Add a table reporting numerical accuracy/F1, all three privacy metrics, and the standard LoRA upper bound for each task-configuration. Include standard deviations.
2. State all key hyperparameters (n, m, noise variance, regularizer weight) for every experiment.
3. Test against a nonlinear attack on individual adapter activations (e.g., a small MLP or XGBoost classifier) to validate the adversarial regularizer's effectiveness beyond linear adversaries.
4. Tone down the "provably obfuscate" language to reflect what is actually proved (correctness of gradient recovery) vs. what is evaluated empirically (privacy against specific attacks).
5. Either provide an information-theoretic analysis to support the "all but one bit" claim, or remove it.

## Score and Decision

This paper tackles a timely and practically important problem. The core ideas — particularly leveraging PEFT's compactness for multi-adapter mixing — are genuinely novel and well-motivated. The gradient obfuscation protocol is mathematically sound. However, the paper has significant presentation and evaluation issues: the experimental results are only reported visually with no numerical values, key hyperparameters are missing, the adversarial defense against nonlinear attackers is unexamined, and the privacy claims are phrased more strongly than the evidence supports. These gaps are addressable in revision, but in their current form they prevent the reader from verifying the paper's central claims.

**Score:** 5.0 (borderline — interesting ideas, insufficiently validated)

**Decision:** Reject

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>