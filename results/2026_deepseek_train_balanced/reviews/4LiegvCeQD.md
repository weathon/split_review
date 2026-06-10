Now let me write the final review.

## Summary

The paper proposes IEL (Intra-Model Ensemble Learning), a test-time adaptation method that dynamically selects a "teacher" model per sample — the model whose softmax has the highest probability for the majority-voted class — and minimizes cross-entropy from all models toward it. The method operates at batch size 1 with frozen batch normalization, targeting the single-sample TTA setting where batch-statistic-dependent methods struggle. Evaluated on CIFAR-10C, CIFAR-100C, and ImageNet-C, the paper shows accuracy improvements over static (unadapted) baselines.

## Strengths

1. **Dynamic per-sample teacher selection is a genuinely novel mechanism.** The teacher model (Equation 1, line 85-87) is determined per-sample by majority voting followed by selecting the model with the highest probability for the voted class. This teacher can change from sample to sample, and the design inherently protects the strongest model (its loss term reduces to its own low entropy) while pulling weaker models toward the consensus. This differs from static knowledge distillation and from standard ensembles that never modify member models.

2. **Operates under a genuinely restrictive TTA regime.** The paper freezes all batch normalization layers and uses batch size 1 (lines 105, 117, 121), ensuring that all adaptation comes from the IEL loss rather than from updating batch statistics. This isolates the contribution of the method and targets a setting (single-sample batches) where methods like TENT are known to struggle.

3. **Evidence of generalization beyond tuning data.** On some corruption types (e.g., ResNet152 on zoom blur and fog in Table 3, line 203), accuracy improvements on the held-out evaluation set exceed those on the tuning set, indicating that IEL does not merely memorize adaptation samples.

4. **Asymmetric model adaptation confirms non-trivial dynamics.** On corruption types where some models degrade while others improve (e.g., Impulse Noise in Table 1, lines 205-206), the empirical behavior demonstrates that not all models collapse to the same output — there is genuine dynamic interaction among ensemble members.

## Weaknesses

### Major

1. **No comparisons to any existing TTA method.** The paper positions IEL as a test-time adaptation method and discusses TENT, EATA, COTTA, ROID, and SHOT in the related work (lines 14, 65-66), but the experiments compare only against "static model accuracies when left unchanged" (line 127). Without benchmarking against even a single existing TTA method — especially EATA, which also targets the single-sample setting — the paper cannot substantiate its claim of being a competitive TTA approach. Showing improvement over "doing nothing" is a much lower bar than showing improvement over the state of the art, and this omission is the single most serious weakness in the paper.

2. **Reporting "highest accuracy improvements over all epochs" instead of final accuracy.** The paper explicitly states that Tables 1–3 report "highest accuracy improvements (%) over all epochs" (lines 129, 131). Reporting the peak performance across epochs (rather than final or average) is cherry-picking and does not reflect the reliability of the method. If accuracy fluctuates significantly across epochs — and the fact that the paper selects the highest value rather than the final one suggests it may — the reader cannot assess whether the method converges to a stable improvement or simply spikes temporarily.

3. **No specification of which models form the CIFAR ensembles.** For ImageNet, the paper states models come from the PyTorch Vision library (line 117). For CIFAR-10C and CIFAR-100C, no architectures or identities of the ensemble members are specified — the paper only mentions "ResNet50" and "ResNet152" in figure captions, without stating how many models, which specific architectures, or whether they have distinct architectures as claimed (line 81). This is a reproducibility gap for the CIFAR experiments.

### Minor

4. **The regularization constant α = 10e⁻¹¹ is effectively zero and its role is unclear.** The paper mentions α once (line 127) with the confusing statement that it "effectively makes our learning rate even smaller." The loss function (Equation 1) does not include α, so it is unclear what is being regularized and whether this hyperparameter has any measurable effect. No ablation is provided.

5. **Tension in the "diversity as optimization signal" framing.** The first contribution bullet (line 40) claims "diversity as a new optimization signal for classification," but the method minimizes cross-entropy between models, which explicitly reduces diversity (as the paper itself acknowledges at lines 36-38). The paper is transparent about this trade-off, but calling diversity reduction "using diversity as a signal" is terminologically confusing and mischaracterizes the contribution.

6. **No analysis of calibration or confidence reliability.** Since IEL explicitly reduces prediction entropy (line 21, Figure 1) and entropy minimization is known to degrade calibration, the paper should report calibration metrics (ECE or reliability diagrams). The absence is notable given the paper's own acknowledgment that calibration may be sacrificed (line 99).

### Trivial

7. **The paper states "using only one sample per batch was empirically found to produce identical performance gains as using multiple samples per batch" (line 121) but provides no data supporting this claim.**

## Nice-to-Haves

- Test on mixed-corruption streams rather than resetting per corruption type (line 121). The current protocol (reset weights, then adapt to isolated corruption types) sidesteps continual and mixed-corruption scenarios.
- Ablate the dynamic teacher selection: compare against fixed-teacher baselines (always the largest model) or against the average softmax as target.
- Report hyperparameter sensitivity (learning rate, number of models M, number of epochs).
- Report inference cost: backpropagating through all M models per sample is expensive; comparing FLOPs/sample to TENT or EATA would contextualize the cost.

## Removed Points

These points are flagged for removal; treat them with caution.

- *"Evaluation protocol undermines single-sample claim (structural)."* The paper's "single sample" refers to batch size = 1, not "each sample seen exactly once." Running multiple epochs on a stationary corruption type is standard in TTA evaluation (the corruption type defines a fixed distribution; multiple passes improve estimation). The paper is clear about resetting between corruption types. This criticism overinterprets "single sample" and is inconsistent with standard TTA evaluation practices. → **Removed** (misunderstanding of the setting).

- *"Method actively destroys ensemble diversity, which is the core mechanism that makes ensembles work."* The paper explicitly acknowledges this trade-off multiple times (lines 21, 36-38, 66, 97, 213). It presents the "perfect model" counter-example (lines 60-62). The empirical results show the method works on 12/15 (CIFAR-10C), 11/15 (CIFAR-100C), and 15/15 (ImageNet-C) corruption types. The critic's claim that this "may invalidate the approach" is unsupported by the evidence the paper provides. The catastrophic forgetting the critic flags is exactly what the paper's Limitations section (line 207, 213) honestly reports. → **Demoted** from "structural/fatal" to minor observation. The paper's own framing is adequate.

- *"The selected model is still affected by backprop."* The paper says "least affected" and "small contributions" (line 97), not "unaffected." The critic mischaracterizes the claim. → **Removed** (strawman; paper never claims the selected model is unaffected).

- *Section-by-section nitpicks about the human collaboration analogy, "upward spiral," and similar.* These are stylistic observations without concrete evidence of a flaw. → **Removed** (non-substantive).

- *Criticism about "the paper claims TENT becomes ineffective without evidence or citation."* The paper says "methods like TENT... become ineffective with access to only a single sample per batch" (line 14). This is a well-known limitation of TENT (its reliance on batch statistics), widely documented in the TTA literature. It does not require a specific citation for this specific sentence. → **Removed** (factually correct, common knowledge in the field).

- *Strengths that are generic/superficial from the Strength Finder.* Some strengths from the finder ("The paper addressed an important problem") are too generic. I have retained only concrete, evidenced strengths. Generic framing was dropped. → **Removed** (generic).

## Novel Insights

None beyond the paper's own contributions. The reviews surface a key disconnect: the paper makes a genuinely novel methodological contribution (dynamic per-sample teacher selection from an ensemble) but evaluates it against a baseline that is too weak ("doing nothing") for a top-venue TTA paper. The strengths and weaknesses do not cancel each other out — the method is clever, but the evaluation does not meet the standard required to demonstrate that it is competitive. The missing comparison to EATA (which also targets single-sample TTA) is the most consequential gap.

## Suggestions

1. Compare IEL against at least EATA, TENT (with batch size >1), and ROID on the standard CIFAR-10C / CIFAR-100C / ImageNet-C benchmarks. Report both the ensemble accuracy and the best single-model accuracy.
2. Report final accuracy (or accuracy curves across epochs) rather than "highest over all epochs."
3. Fully specify the ensemble composition for the CIFAR experiments (architectures, number of models, training details).
4. Add calibration metrics (ECE) to the evaluation given that IEL minimizes entropy.
5. Clarify what the α=10e⁻¹¹ regularization term applies to, or remove it if it is vestigial.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>