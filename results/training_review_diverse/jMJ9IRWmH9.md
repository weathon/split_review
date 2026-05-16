Now I have all the evidence I need. Let me write the final consolidated review.

## Summary

This paper proposes P³EFT, a two-party protocol for privacy-preserving fine-tuning of large language models over APIs. It targets label privacy in a split-learning setting where the server hosts the model and the client owns labeled data. The method has two components: (1) gradient obfuscation via secret sharing (exploiting the linearity of backpropagation), and (2) a mixture-of-adapters approach combined with adversarial regularization to obfuscate activations. Experiments on DeBERTa-v2-XXLarge and Flan-T5-Large on SST-2 and MRPC show accuracy comparable to non-private fine-tuning while resisting several label-leakage attacks.

## Strengths

- **Clear diagnosis of label leakage in standard PEFT fine-tuning (Section 3.1, Figure 1):** The paper provides visual evidence that both gradients and activations from LoRA fine-tuning cluster by label under PCA, establishing the concrete privacy threat the method addresses. This grounded motivation is valuable.

- **Novel gradient obfuscation via linear decomposition (Section 3.2, Algorithm 1):** Exploiting the conditional linearity of backpropagation is a clever insight. The secret-sharing construction decomposes the true gradient into noise vectors sent to separate servers, and the client recovers the exact gradient by recombining — meaning training dynamics are mathematically unchanged. The XGBoost attack achieving ~50.4% accuracy (chance-level) on the obfuscated gradients provides empirical validation.

- **Mixture-of-adapters for activation obfuscation (Section 3.3):** Using multiple adapter sets with randomized mixing weights is a principled way to prevent individual adapter outputs from leaking labels while preserving the combined model's predictive accuracy. This is a distinctive contribution tailored to PEFT's parameter efficiency.

- **Practical evaluation on large, realistic models:** Experiments on DeBERTa-v2-XXLarge (~1.5B parameters) and Flan-T5-Large on GLUE tasks demonstrate that the method scales to the types of models and tasks where this privacy concern is most relevant.

- **Accuracy-privacy trade-off analysis (Figure 5):** The sensitivity charts comparing P³EFT against the Distance Correlation baseline across varying regularizer coefficients give a more nuanced picture than a single operating point would.

## Weaknesses

### Fatal
None. The core approach is conceptually valid and the experiments, while incomplete, do not contain errors that invalidate the central claims.

### Major

1. **Adversarial regularization is critically under-specified (Section 3.3, lines 163–169).** The paper states that linear "heads" are fit to predict labels from individual adapter activations, then the adapters are updated adversarially — but provides no explicit update rule, no optimization details (number of steps, optimizer, whether this is a min-max formulation or a gradient reversal layer), and no hyperparameters. This component is essential for the activation privacy claim (one of the two identified attack vectors in Figure 1), yet the description is too vague to reproduce. The claim that this step takes "negligible time" is unsubstantiated. Without specifying or ablating this mechanism, the method's privacy guarantees for activations cannot be independently verified.

2. **"Provably obfuscate" is claimed without a formal privacy definition or proof (line 32).** The abstract and contributions assert that P³EFT can "provably obfuscate the gradients," but no formal definition of privacy (e.g., cryptographic indistinguishability, information-theoretic leakage bound, or differential privacy) is given. The security analysis is entirely empirical and attack-specific (ROC AUC against three attacks). While the secret-sharing construction has intuitive security properties, the paper does not formalize what "obfuscation" means or under what assumptions it holds, making the "provably" claim rhetorical rather than substantive.

3. **Protocol security depends on infrastructure assumptions that are neither validated nor experimentally evaluated.** The protocol requires either (a) multiple non-colluding servers or (b) trusted execution environments (TEEs) to prevent a single server from recovering the gradient by combining multiple noise vectors or inverting consecutive parameter updates (Section 3.2). The paper acknowledges these requirements but provides no experiments, overhead measurements, or evidence that either condition is practically achievable for today's fine-tuning APIs. The alternative ("add noise to parameters") is itself described as "risky" and is not evaluated.

### Minor

1. **Experimental results lack statistical rigor.** Bar charts (Figures 4, 5) are presented without error bars, confidence intervals, or standard deviations. Given training variance in deep learning, the claim that P³EFT achieves "nearly the same accuracy" as the non-private baseline cannot be properly assessed. Multi-seed runs with reported variance are needed.

2. **The `obfuscate` function in Algorithm 1 is not defined.** The paper does not specify the noise distribution, how the scalars α_j are chosen, or how the decomposition Σ α_j · ĝ_h^j = g_h is constructed for m > 2. The experiment uses noise variance 1000 (line 187), but the distribution family is not stated. Without this, the gradient obfuscation component is not fully reproducible.

3. **No ablation studies on key hyperparameters.** The paper fixes n=2 adapters, m=2 noise passes, and noise variance=1000 but provides no ablation analyzing sensitivity to these choices. How accuracy and privacy vary with the number of adapters or passes is unknown.

4. **No computational overhead analysis.** Private backprop multiplies API calls by m; multiple adapters multiply forward passes by n. The paper reports no wall-clock time, cost increase, or communication overhead — critical information for practitioners evaluating whether the method is practical.

5. **DC baseline tuning is vaguely described.** The Distance Correlation baseline is tuned "to maximize accuracy with a constraint that DC has same or comparable privacy as our algorithm" (line 199), but how "comparable privacy" is measured or enforced is not specified, making the comparison difficult to interpret.

6. **Limited attack evaluation.** The XGBoost attack achieving chance-level accuracy (Section 4.1) is encouraging, but stronger attacks are not tested — e.g., adversaries who know the noise distribution, combine multiple time steps, or exploit the mixing weights structure. The privacy evaluation remains attack-specific rather than providing worst-case bounds.

### Trivial

- Notation inconsistency: "n=2 with noise variance set to 1000" in Section 4.1 (line 187) uses n to refer to noise passes, whereas n denotes the number of adapters in Section 3.3.

## Nice-to-Haves

- Comparison with simpler baselines (e.g., adding Gaussian noise to gradients/activations without the mixing scheme) would clarify whether the secret-sharing and adapter mixing are both necessary or whether the method is over-engineered.
- A single-server scenario (TEE-based) with measured overhead would substantially strengthen the practical claims.

## Removed Points

These points were flagged by reviewers but are removed or downgraded per the instructions:

1. **"Differential privacy dismissal is too quick"** — Removed. The paper correctly distinguishes its label-privacy setting from DP's membership-privacy setting. The non-label party knows which examples participate, so DP's standard protection is not the relevant guarantee. This is a reasonable scope decision, not a flaw.
2. **"'Training w/o LoRA adapters' baseline provides little insight"** — Removed. The paper presents this as a lower-bound baseline, which is a standard and useful reference point.
3. **"Missing citation for Ganin & Lempitsky (2015)"** — Removed. The paper does cite it (line 163); any garbling is a parser artifact.
4. **"Missing appendix, missing proofs in appendix"** — Removed. The parser strips appendix sections from all papers; these exist in the original submission.
5. **"Gradients for each adapter depend on W — is it guaranteed that noise does not cancel the mixing effect?"** — Removed. The paper explains that adapters receive different gradients and diverge naturally (line 161), and the adversarial regularization prevents them from converging back to a leaky state.
6. **General formatting/typo nitpicks** — Removed per instructions (parser artifacts, not author errors).

## Novel Insights

Beyond the paper's own contributions, the reviews surfaced an important structural tension: the gradient obfuscation component (Section 3.2) is elegant and mathematically lossless, while the activation obfuscation component (Section 3.3) is heuristic and under-specified. This asymmetry risks making the paper's overall privacy claim only as strong as the weaker link. A useful insight is that the secret-sharing gradient protocol could be cleanly separated and formally proven (it is, at heart, a standard additive secret sharing scheme), potentially allowing the paper to claim a well-defined privacy guarantee for the gradient path even if the activation path remains heuristic. This hybrid approach — formal for gradients, empirical for activations — might be a more honest and still useful framing than the current monolithic "provably obfuscate" claim.

## Suggestions

1. Formally define the security guarantee for the gradient obfuscation component. Since it reduces to additive secret sharing, an information-theoretic argument (each server's view is independent of g_h) is within reach and would substantiate the "provably" claim.
2. Provide the full specification of the adversarial regularization: update rule, optimizer, number of steps per training iteration, and learning rate. Alternatively, release the code with these details.
3. Add error bars (mean ± std over at least 3 seeds) to all experimental results.
4. Include an ablation study showing privacy degradation when the adversarial regularizer is removed, to verify this component is necessary.
5. Report the number of API calls and wall-clock time overhead introduced by the protocol.

## Score and Decision

The paper identifies a real and timely problem and contributes two clever ideas — gradient secret-sharing and mixture-of-adapters activation obfuscation — that are genuinely novel and leverage PEFT's structure in a non-trivial way. The experimental setting (large models, GLUE tasks) is appropriately ambitious.

However, the paper has significant rigor gaps: the adversarial regularization (critical for activation privacy) is under-specified to the point of non-reproducibility; the "provably" claim is unsupported by any formal definition; the infrastructure assumptions are untested; and the experiments lack basic statistical rigor (no error bars, no ablations, no overhead measurements). These are not fatal — the core approach is valid — but they prevent the paper from making a convincing case in its current form. A major revision addressing the adversarial regularization specification, adding formal grounding for the gradient claim, and tightening the experimental methodology could yield a strong paper.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>