I now have all the evidence I need. Let me construct the final consolidated review.

---

## Summary

This paper reframes the problem of missing modalities in multimodal egocentric video recognition as a test-time adaptation (TTA) challenge, and introduces MiDl (Mutual information with self-Distillation minimization), a self-supervised method that adapts a pretrained multimodal model on-the-fly without retraining. MiDl minimizes mutual information between the model's predictions and the modality type present (encouraging modality-invariant predictions) while using KL-divergence-based self-distillation to preserve performance on complete-modality inputs. Experiments across Epic-Kitchens and Epic-Sounds, three architectures (MBT, vanilla self-attention, Omnivore), multiple missing rates, and several adaptation scenarios show consistent and often substantial accuracy gains (e.g., +7% on Epic-Kitchens at 75% missing rate) over the non-adapted baseline and existing TTA methods.

## Strengths

1. **Novel and well-motivated problem formulation.** The paper is the first to frame missing modality as a test-time adaptation problem, which is a realistic and practical departure from prior work that requires expensive retraining. The formulation is clean and general.

2. **Significant and consistent performance gains.** MiDl delivers clear improvements across multiple datasets, missing rates, and architectures. Table 1 shows a 7% gain on Epic-Kitchens at 75% missing rate (51.7% → 58.7%) and a 3.7% gain on Epic-Sounds at 50% missing rate (47.8% → 51.5%), often exceeding unimodal performance. These gains come without retraining.

3. **Agnostic to architecture, modality type, and pretraining strategy.** The method generalizes across MBT (Table 1), vanilla self-attention (Table 3), and Omnivore backbones (Table 5); across dominant and non-dominant missing modalities (Tables 1, 4); and across different pretraining strategies (masked autoencoder vs. Omnivore). This breadth is demonstrated through dedicated experiments, not just claimed.

4. **Clean ablation validates the design choices.** Table 6 shows that KL alone yields no adaptation, MI alone degrades performance at low missing rates, and the combination (MiDl) provides consistent gains across all missing rates. This confirms that both terms are necessary and that their interaction is well-understood by the authors.

5. **Evaluation under three realistic scenarios.** The paper tests MiDl in standard online TTA (Section 5.2), long-term adaptation on training-domain data (Section 5.3), and warm-up on out-of-domain Ego4D data (Section 5.4). The out-of-domain warm-up provides the cleanest evidence of pure test-time transfer.

## Weaknesses

### Fatal
None.

### Major
None. The paper's contributions are genuine and well-supported. The concerns below are substantive but do not undermine the core claims.

### Minor

1. **The LTA experiments (Section 5.3) deviate from pure test-time adaptation.** S_in is explicitly described as "a subset of training data" (line 120). Using training-domain data for adaptation means the model benefits from data drawn from the same distribution as the original training set (and for which labels exist in the pretraining phase). This is closer to few-shot fine-tuning than strict test-time adaptation. The paper partially addresses this concern with the out-of-domain warm-up experiment on Ego4D (Section 5.4), which provides stronger evidence of pure test-time transfer — but the paper's main LTA gains (+11.9% at 100% missing rate on Epic-Kitchens) rely on training-domain data. The authors should be more explicit about this distinction and avoid conflating the two scenarios.

2. **The method's scope is narrower than the title and framing might suggest.** MiDl relies entirely on complete-modality (AV) samples in the test stream for adaptation (Section 4: "we refrain from adaptation when S reveals x_t with incomplete modality"). When the test stream has no complete-modality samples (p_AV = 0), no adaptation occurs. The paper acknowledges this (lines 77–78: "we assume that p_AV ≠ 0"), but this limiting condition could be stated more prominently — perhaps in the abstract or introduction — rather than deferred to Section 4. Readers could misinterpret the approach as working in all missing-modality scenarios.

3. **The mutual information objective uses uniform weighting over modality types without justification.** The MI term in Equation 2 averages predictions and entropies uniformly over m ∈ {A, V, AV} (line 71). This implicitly treats all three modality configurations as equally important. While this is a reasonable default, the paper does not discuss whether this uniform weighting could lead to suboptimal solutions when the stream distribution p_m is highly skewed (e.g., mostly audio-only samples with few complete-modality samples), nor whether importance weighting by stream probabilities would be beneficial.

4. **No sensitivity analysis for key hyperparameters.** The paper uses a fixed learning rate γ and a single gradient step per complete-modality sample, but does not analyze sensitivity to these choices. A single step may be insufficient (or too many) depending on the adaptation budget, and the learning rate could significantly affect the stability of the KL regularizer. This is a standard expectation for TTA papers that is absent here.

5. **Computational cost estimate is optimistic.** The paper states MiDl is "only 2× slower since all additional 4 forward passes can be performed in parallel" (line 197). This assumes ideal batch-processing conditions that may not hold in all deployment settings, especially on memory-constrained hardware typical of egocentric/wearable devices. A measured runtime (ms per sample) on the actual hardware would be more informative.

### Trivial
None.

## Nice-to-Haves

- A simple online baseline that imputes missing features using a running estimate from complete-modality samples seen so far (e.g., running mean of missing modality features) would help isolate whether MiDl's benefit comes from the MI+KL objective or from any feature-level adaptation. The current baselines (Shot, ETA) are designed for covariate shift, not missing modality.
- An analysis of how MiDl's gain scales with the number of adaptation steps / complete-modality samples seen would strengthen the practical guidance for practitioners.
- A failure-case discussion: under what conditions might MiDl degrade performance (e.g., very few complete-modality samples leading to noisy MI estimates, or out-of-distribution domains where the KL regularizer anchors to a poor initial state)?

## Removed Points

- **Criticism that p_AV=0 results in Table 1 come from LTA.** This is factually incorrect. Table 1 is in Section 5.2 (standard online TTA), while LTA is a separate setup in Section 5.3 with its own table (Table 2). The paper reports p_AV=0 in Table 1 explicitly to show MiDl does not degrade performance when no adaptation is possible (Section 4: "we also report results with p_AV=0"). There is no conflation. This point is removed as factually wrong.
- **Demand for comparison to "online fusion baseline (running average of unimodal predictions)."** This is a reasonable suggestion but falls short of a genuine weakness — the paper already compares to unimodal models and existing TTA methods, and the requested baseline would test a different hypothesis (late fusion vs. model adaptation). Moved to Nice-to-Haves.

## Novel Insights

Beyond the paper's own contributions, the most interesting takeaway from the ablation (Table 6) is the asymmetric interaction between the MI and KL components: MI alone *hurts* performance at low missing rates but can help at high missing rates, while KL alone is inert. The combination succeeds because MI pushes toward modality invariance (helpful when missing rates are high) while KL prevents catastrophic forgetting of the complete-modality behavior (critical when complete-modality samples are frequent). This tension between forgetting and invariance is a recurring theme in TTA, and the paper provides a clean instantiation of a two-term loss that manages it well.

## Suggestions

1. Restructure the narrative to state the key limitation (requires complete-modality samples) early, e.g., in the abstract or introduction, rather than burying it in Section 4.
2. Clearly differentiate the LTA experiments using training-domain S_in from pure test-time adaptation, and consider reporting LTA results on out-of-domain data (as in Section 5.4) as the primary evidence for long-term test-time transfer.
3. Add a brief discussion of the uniform weighting assumption in the MI term, acknowledging that stream distributions may be non-uniform and discussing whether re-weighting could help.
4. Include a sensitivity analysis for the learning rate and number of gradient steps, even if brief (e.g., a small table or paragraph in the appendix). This is standard for TTA papers.
5. Provide measured wall-clock latency on a representative GPU rather than relative factor estimates that assume ideal parallelism.

## Score and Decision

The paper makes a genuinely novel contribution by reframing missing modality as a TTA problem and introducing a principled, well-validated method. The experiments are thorough, the ablation is clean, and the method generalizes across architectures, datasets, and missing rates. The main weaknesses (training-domain data used in LTA, scope limitation requiring complete-modality samples) are real but acknowledged or mitigated by other experiments. The paper should be accepted with minor revisions to clarify scope and add standard sensitivity analysis.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>