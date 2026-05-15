Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me construct the final consolidated review.

## Summary

The paper reframes the missing-modality problem in egocentric video as a test-time adaptation (TTA) challenge and proposes MiDl (Mutual information with self-Distillation), which adapts a pretrained multimodal model at test time without retraining. MiDl minimizes an approximation to the mutual information between model predictions and modality type (to encourage invariance to which modality is available) while using KL-divergence with the original model's predictions on complete-modality inputs (to prevent catastrophic forgetting). Experiments on Epic-Kitchens and Epic-Sounds with MBT and other backbones show consistent gains of 3–7% in the basic TTA setting and larger gains in a long-term adaptation setup that uses training data for pre-adaptation.

## Strengths

- **Novel problem framing.** The paper is the first to explicitly reframe missing modalities as a test-time adaptation problem (Section 3), connecting two previously separate literatures. It validates the need for a tailored approach by showing that off-the-shelf TTA methods (Shot, ETA) fail under this distribution shift (Table 1).
- **Consistent gains without retraining.** MiDl improves accuracy over the non-adapted baseline across multiple missing rates on two datasets (e.g., Epic-Kitchens 75% missing: 48.4% → 55.4% in Table 1). These gains require no access to training data or labels, distinguishing MiDl from prior missing-modality methods that require retraining.
- **Controlled ablation validates design.** Table 6 cleanly shows that removing the KL term causes degradation under low missing rates (full-modality accuracy drops from 63.7% to 46.8% on Epic-Kitchens), while removing the MI term yields no adaptation at all. This supports the claim that both components are needed.
- **Evidence of cross-architecture and cross-modality applicability.** The method is evaluated on MBT and vanilla self-attention architectures (Section 6.1), when different modalities are missing (Section 6.2), and with Omnivore pretraining (Section 6.3), providing breadth of evidence.

## Weaknesses

### Fatal
None.

### Major

- **Gap between the theoretical MI objective and the practical loss.** The paper motivates MiDl by minimizing $\mathbf{MI}(f_\theta(x;m), m)$ over the stream distribution (Equation 1). However, the practical update (Equation 2) operates on a single sample $x_t$ by creating three artificial modality variants $(A,V,AV)$ with a uniform weighting, not by sampling $m$ from the true stream distribution $\mathbb{P}_S(M=m)$. The paper acknowledges the approximation (lines 52–53), but the theoretical framing in Section 4 presents the ideal objective as the method's foundation, creating a disconnect. The approach is better described as encouraging modality invariance via a per-sample entropy-based regularizer, and the paper would benefit from reframing or tightening the connection.

- **Method does nothing when $p_{AV}=0$.** When no complete-modality samples appear in the stream (100% missing rate), $\mathcal{L}_{\mathrm{MI}}=0$ by construction and the method skips all adaptation steps. Table 1 shows essentially 0% gain over baseline in this setting. The paper explicitly acknowledges this limitation (line 77), but it is a fundamental constraint: the method is most needed precisely when it cannot adapt. The "long-term adaptation" (Section 5.3) and "warm-up" (Section 5.4) settings partially circumvent this by pre-adapting on external data, but that shifts the setting away from pure test-time adaptation.

### Minor

- **Headline numbers conflate different experimental settings.** The abstract and introduction report "a 6% gain on Epic-Sounds and an 11% gain on Epic-Kitchens" without specifying the setting. The 11% figure comes from the Long-Term Adaptation setting (Table 2, Epic-Kitchens 100% missing: 31.8→43.7), which uses training data for pre-adaptation — not a pure test-time setup. The basic TTA results (Table 1) show gains of 5–7%. While LTA is a valid experiment, the abstract should distinguish the settings to avoid misleading readers about the magnitude of improvement achievable in the pure test-time scenario.

- **Gains in the basic TTA setting are modest relative to the full-modality baseline.** On Epic-Kitchens with 75% missing, MiDl recovers from 48.4% to 55.4%, still far below the full-modality performance of 63.7%. The practical significance of 3–7% gains in this setting is unclear without an error analysis or comparison to training-based missing-modality methods (even as an upper bound).

- **Computational cost is significant for wearable deployment.** MiDl requires 5× the inference cost per adaptation step (3 forward passes for modality variants + 1 for the original model + 1 backward pass), with 2× latency (line 197). The paper mentions parallelism but provides no real-time feasibility analysis for wearable devices, which is the motivating application.

- **Missing optimization hyperparameters.** The learning rate $\gamma$, batch size, and number of adaptation steps per sample are not reported in the main text (line 69 only mentions $\gamma>0$). These details may be in the appendix (stripped by the parser), but their absence from the main paper's setup section hampers quick reproducibility assessment.

### Trivial
- The unimodal performance numbers in Table 1 are described as "unimodal models" without explicitly stating whether these are separately trained models or the same multimodal model with a single modality input. The text (line 97: "unimodal models that rely solely on the available modality") strongly implies separate training, but a clarifying sentence would help.

## Nice-to-Haves
- Comparison against training-based missing-modality methods (Ramazanova et al. 2024, Lee et al. 2023) as an upper bound, even if the settings differ, would help contextualize MiDl's practical value.
- Evaluating MiDl on partial missing patterns (corrupted audio, missing frames) beyond binary modality dropout would strengthen the claim of real-world applicability.
- A diagnostic showing whether the adapted model becomes *correctly* invariant (all modality variants predict the right class) vs. trivially invariant (all predict a constant) would address a natural concern about the MI objective.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **The critic's claim that the Omnivore experiment conflates different concepts (Section 6.3).** The paper explicitly states it uses Omnivore "to initialize each one of our backbones" (line 176) and notes its nature. The experiment is about pretraining strategy generalization, not about Omnivore being a multimodal model. This criticism misunderstands the experiment.
- **Criticism about missing related work on domain generalization/invariant representations.** Per guidelines, I cannot evaluate missing related work claims.
- **The claim that baselines are "weak" because the paper doesn't compare against retraining-based missing-modality methods.** The paper's frame is test-time, no-retraining adaptation. Comparing against training-based methods is not a fair head-to-head, though such comparisons would be informative as an upper bound (moved to nice-to-haves).
- **The claim that the method's improvement is "not practically significant."** Gains of 3–7% on standard benchmarks without retraining are practically meaningful; this is a subjective dismissal without evidence.
- **Criticisms about missing appendix content (standard deviations, hyperparameters).** Appendix sections were stripped by the parser; they exist in the original submission.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Reframe the theoretical motivation.** Explicitly describe the practical loss (Equation 2) as an *approximation* to MI minimization or as a "modality-invariance regularizer" rather than presenting the stream-level MI objective (Equation 1) as the direct foundation. This would close the theory-practice gap.
2. **Disambiguate the headline numbers.** In the abstract and introduction, clearly attribute the 11% gain to the LTA setting and the ~5–7% gains to the basic TTA setting.
3. **Add a mechanism for adapting on incomplete-modality samples.** For example, when only one modality is available, the MI term could operate on the available predictions from consecutive frames or use a buffer, rather than skipping adaptation entirely. This would address the $p_{AV}=0$ limitation.
4. **Report optimization details in the main text.** Include learning rate, batch size, and number of adaptation steps to improve reproducibility.

## Score and Decision

This paper tackles a practical and underexplored problem with a clean, simple method that works across architectures and datasets. The core idea — minimizing modality-prediction dependence as a self-supervised TTA objective — is novel and the controlled ablation validates the design. However, the paper is weakened by a disconnect between its theoretical MI framing and the practical loss, and by the method's inability to adapt when complete-modality samples are entirely absent. The headline results blend numbers from different experimental settings in a slightly misleading way. These are real but not fatal issues. The paper makes a useful contribution and is worth publishing with revisions to tighten the framing and clarify the results.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>