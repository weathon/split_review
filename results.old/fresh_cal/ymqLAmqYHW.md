Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper proposes Key-Locks (K&L), a backdoor attack that embeds "locks" into model parameters during training and generates per-sample "keys" via gradient descent at inference time. The key idea is that by avoiding a fixed trigger, the attack can evade defenses designed to remove static backdoor patterns. The paper evaluates K&L against eight defenses across four datasets and reports that K&L is the only method that maintains high attack success rates under all defenses, while also showing improved attribution-based stealth.

## Strengths

- **Consistent defense penetration across all evaluated scenarios (Table 1)**: K&L achieves successful attack rates (bold entries) under all eight defenses (ANP, BNP, FP, FT, I-BAU, NAD, CLP, RNP) on CIFAR-10, CIFAR-100, GTSRB, and Tiny ImageNet, while every baseline method (BadNet, Blended, Input-Aware, SSBA, WaNet, BppAttack) fails under at least one defense. This is the paper's primary empirical evidence and presents a striking result if the evaluation protocol is sound.

- **Quantified attribution stealth far exceeding baselines (Table 2)**: The cosine similarity between attribution maps of backdoor and clean samples is 0.6995 for K&L vs. the next best at 0.0690 (Blended) and 0.0026 for BadNet. This ~10x improvement over the closest baseline is a concrete, measured achievement that directly supports the claim of imperceptible triggers.

- **Trigger generation without additional trainable parameters**: Unlike input-dependent attacks (Input-Aware, SSBA) that require training a generator network—itself tightly coupled to the model parameters and defensible—K&L's key generation uses gradient descent directly. This is a genuine technical distinction from prior methods.

- **STRIP evasion demonstrated across four datasets (Figure 4)**: The entropy distributions of K&L-backdoored samples and clean samples overlap substantially across all datasets, providing a clean empirical demonstration that the attack circumvents entropy-based detection.

## Weaknesses

### Fatal
None.

### Major

- **Critically underspecified defense evaluation protocol**: The paper never clarifies whether the K&L "key" (trigger) is generated on the **original backdoored model** or the **defended model**. This is essential because K&L's key-generation process is gradient-based and model-dependent: if keys are generated on the defended model, the attack is effectively a targeted adversarial perturbation on the defense-weakened model, which is a categorically different threat model from the static-trigger baselines. The paper's central claim—that K&L "penetrates defenses" better than baselines—cannot be properly evaluated without this detail. This is the single most important clarification needed.

- **AAC metric is introduced but never formally defined**: The paper states "We also introduce a new metric: the Accuracy-ASR Curve (AAC)" and reports numeric values AAC1 (0.9415), AAC3 (0.9111), AAC5 (0.8772). However, the metric is never defined: what are the axes? What do the suffixes 1, 3, 5 represent? Is it an area-under-curve metric? How is it computed? Without a definition, the AAC results (Table 3, Figure 3) cannot be interpreted or reproduced. (This is not a parser artifact—the metric is named and values reported but never defined in any visible portion of the extracted paper.)

### Minor

- **"Decoupling" claim is overstated relative to the mechanism**: The paper claims the algorithm "decouples the attack algorithm from model parameters" (contribution list). However, the key generation uses gradient descent computed with respect to the model parameters \(W'\) (Eqs. 5–6), so the attack is still coupled to the model—just through gradients rather than through a fixed trigger pattern. The paper partially acknowledges this ("converting samples to Backdoor samples utilizes gradient descent, which employs model parameters," Section 3.3.2 Property (b)), but the contribution framing is stronger than the mechanism supports. The method would be better described as having *looser* coupling via gradient-based trigger generation, not full decoupling.

- **Lock embedding procedure is not described in the extracted text**: Section 3.3 (the "Embedding Locks" process) is absent—the paper jumps from "3.2 Research Problem" to "3.3.1 Use the Key to Open the Door." The terms "locks loss" and "maintain loss" are referenced repeatedly but never defined or formalized. If this is a parser artifact, the paper is still incomplete as presented; if not, the method is not reproducible. The training objective and lock-embedding algorithm need to be stated.

- **No variance or statistical significance reported**: Table 1 reports single ASR/BA values per defense-dataset combination with no standard deviations, confidence intervals, or indication of multiple trials. This makes it impossible to assess whether reported advantages are statistically meaningful.

### Trivial

- The paper uses "the the" (double article, line 18).
- "Unlikely" is used where "Unlike" is intended (line 166).

## Nice-to-Haves

- **Adaptive baselines**: Since K&L generates per-sample triggers at test time, the evaluation would be strengthened by including adaptive baselines that give competing methods similar test-time adaptability (e.g., generating a targeted PGD perturbation from a backdoored model). This would isolate whether K&L's "lock" embedding provides benefit beyond standard adversarial perturbations.

- **Threat model clarification**: The paper would benefit from explicitly discussing the threat model: K&L requires test-time access to the model (or its gradients) to generate keys per sample. This is a stronger assumption than classical backdoor attacks where the trigger is fixed at training time. Acknowledge and justify this assumption.

- **Inference-time cost discussion**: Gradient descent per sample at inference is expensive. The paper mentions computational cost in the conclusion but does not quantify it (iterations, time per sample, scalability).

## Removed Points

These points were raised by reviewers but are removed with justification:

1. **"Three requirements are trivial / not a contribution"** (Harsh Critic Point 4): Removed. The paper cites prior work for these requirements and claims only to "systematically delineate" them. They are observations about all backdoor attacks, not presented as novel discoveries. The paper's main contribution is the K&L algorithm, not these requirements.

2. **"Decoupling via lock loss" as a strength** (from Strength Finder): This strength conflicts with the verified weakness that the decoupling claim is overstated. The "no additional trainable parameters" aspect is valid and retained as a separate strength; the "decoupling" framing is dropped.

3. **"Missing ablation figures (Figures 5–7)"**: Likely a parser artifact (figures stripped from extracted text). The ablation description itself is present (Section 4.3).

4. **Speculative claims about evaluation unfairness** (from Harsh Critic Point 1): The critic's assertion that results are "likely an artifact of an asymmetric setup" is speculative. The underspecified protocol is a verified weakness (retained as Major), but the stronger claim of actual unfairness cannot be confirmed from the paper as written and is removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface one useful observation: if the evaluation protocol allows key generation on the defended model, K&L blurs the line between backdoor attacks and targeted adversarial attacks—a conceptual connection the paper could productively explore rather than distance itself from (Section 3.4's attempt to differentiate from adversarial attacks is unconvincing, as the test-time behavior is functionally identical to a targeted PGD attack on a model made deliberately vulnerable during training).

## Suggestions

1. **Clarify the defense evaluation protocol explicitly**: State whether the key for a defended model is generated on the original \(W'\) or on the post-defense \(W''\). If the latter, provide defense-specific justification and include adaptive baselines.

2. **Formally define the AAC metric**: Specify what the metric computes, what the x- and y-axes represent, how AAC1/3/5 are derived from the curve, and the formula.

3. **Provide the lock embedding loss functions** (Section 3.3) in full: define \(\mathcal{L}_{\text{locks}}\) and \(\mathcal{L}_{\text{maintain}}\) mathematically. This is essential for reproducibility even if the section was stripped by the parser.

4. **Rephrase the "decoupling" claim** to accurately reflect that the attack remains coupled through gradients but with looser binding than fixed-trigger methods.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>