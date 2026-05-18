Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

---

## Summary

This paper proposes LSlotFormer, a language-guided object-centric world model that extends SlotFormer by conditioning slot predictions on T5 language embeddings. The model operates in a compact latent slot space rather than pixel space, predicting future object-centric states autoregressively under language instruction. These predictions are fed to an action decoder for visuo-linguo-motor control. Evaluated on the language-table benchmark, the method consistently outperforms diffusion-based world models (Seer, Susie) in task success rate while being substantially faster to train and run (up to 85% training speedup, 74% inference speedup). The paper also provides ablations on action decoder design and generalization experiments.

## Strengths

- **Consistent and sizable improvement in control success rate over strong diffusion-based baselines.** Table 1 shows the proposed method outperforms all Seer and Susie variants across three success thresholds. At the strictest threshold (0.05), the method achieves 34.5% vs. Seer-F+SAVi's 21.0% and Susie+SAVi's 4.5%. The advantage holds even when baselines use the same SAVi encoder and action decoder architecture, isolating the benefit to the world model itself.

- **Substantial computational efficiency gains.** Table 2 reports training at 0.06 s/it and inference at 0.19 s/it, compared to Seer-F (0.40 and 0.72 s/it) and Susie (0.18 and 0.47 s/it). This is a genuine architectural advantage of operating in compact latent space rather than generating full video frames.

- **Thoughtful ablation studies on action decoder design.** Section 4.6 systematically tests architecture choices (MLP vs. transformer, grouping by timestep vs. by slot), the number of future steps (Table 4), whether past slots help, and whether adding instructions to the decoder is beneficial. These experiments provide practical guidance for using object-centric representations in control — an under-explored topic.

- **Qualitative evidence that language guidance is effectively injected.** Figure 3 shows that only the proposed method correctly predicts the robot arm moving toward the target object for the instruction "Move the cube towards the moon," while Seer variants fail to reflect the instruction in their generated frames.

- **Honest reporting of generalization limitations.** The paper evaluates unseen blocks and unseen tasks (Table 1), showing expected performance degradation, and discusses these limitations in Section 5. This transparency is valuable to the community.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No confidence intervals or error bars on main success rate results (Table 1).** Success rates are reported as point estimates from 200 episodes. With 200 episodes, the 95% binomial CI around a 50% success rate is roughly ±7 percentage points. While the main comparisons (e.g., 34.5% vs. 21.0%) exceed this margin, adding confidence intervals or multiple-seed statistics would substantially strengthen the credibility of the claims. This is the most significant missing piece for an empirical paper.

- **Unseen-task generalization analysis is shallow.** The paper reports low success rates on unseen tasks (e.g., 16.5% for T1) and notes that instructions include unseen words, but does not diagnose *why* performance drops. Is the bottleneck in slot encoding (failing to bind the new target), language understanding (T5 not having seen the word), world model dynamics, or action decoding? Without this analysis, the generalization claim is weak and the limitations section remains high-level.

- **The DDIM sampler for baselines is set to 10 steps via "trial and error," but the paper does not check whether more DDIM steps would close the performance gap.** If more steps (e.g., 30 or 50) improved Seer's predictions enough to raise its success rate, the advantage of the proposed method would shrink — even if the speed gap widened. A sensitivity analysis over DDIM steps for Seer would clarify whether the performance gap is robust or sensitive to this hyperparameter.

- **Seer-F domain mismatch partially confounds the comparison.** Seer-F is pre-trained on Something-Something V2 (human actions with everyday objects), not robotic manipulation data. Its underperformance relative to the proposed method may partly reflect this domain mismatch rather than a fundamentally inferior world model paradigm. The paper partially addresses this by also testing Seer-S (trained from scratch), which also underperforms the proposed method, so the concern is bounded — but the framing of Seer-F as a "pre-trained" strong baseline should acknowledge this domain difference.

### Trivial

- The "first" claim ("to the best of our knowledge, we are the first to propose object-centric world models guided by language instruction") is adequately qualified and properly scoped against prior work that requires goal images at test time. However, the phrasing in Section 2.2 ("We introduce the first object-centric world model guided by natural language") is slightly stronger. This is a minor presentational issue.

## Nice-to-Haves

- **Sample-efficiency scaling curve:** Vary the amount of training data (e.g., 25%, 50%, 75%) and plot success rate vs. number of training trajectories, comparing the proposed method to Seer-S. The claim of sample efficiency (Table 1 shows the method trained on 7k trajectories beats Seer trained on 7k + Something-Something) is plausible but a scaling curve would make it definitive.

- **Failure mode analysis for unseen tasks:** Show qualitative failure cases and diagnose whether the issue is slot binding, language understanding, world model dynamics, or action decoding.

- **Ablation of action decoder training signal:** If the authors trained the action decoder on ground-truth slots instead of predicted slots, would the performance differ? This would quantify how much the action decoder learns to compensate for world model inaccuracies and would strengthen the claim that the world model's predictions are accurate enough.

## Removed Points

- **"Ambiguity in action-decoder training procedure" (Critical Issue 1 from harsh critic):** The paper is unambiguous on this point. Figure 2 caption states: "The action decoder is trained by inputting the current state slots and future state slots obtained from the trained world model." Section 3.2 (line 85) states: "With current slots s_T, predicted future slots S_prd from the world model..." The action decoder is clearly trained on predicted slots from the frozen world model. This is standard practice in model-based RL — training the policy on the inputs it will actually receive at test time. The critic's concern that this "could mask poor world-model quality" misunderstands the framework. *Removed because it misreads the paper.*

- **"The 'first' claim is overstated" (Critic's Critical Issue 3):** The paper uses "to the best of our knowledge" qualifiers (lines 25, 37) and properly distinguishes from Zadaianchuk et al. (2020, 2023) and Haramati et al. (2024) which require goal images at test time. The claim is appropriately scoped. *Removed because the paper adequately addresses this.*

- **"The number of future steps used in the world model during evaluation is not reported":** This is incorrect. Table 4 explicitly reports success rates for 0, 1, 5, 10, and 20 future steps, and the ablation concludes 10 is optimal. *Removed because factually wrong.*

- **"FVD evaluation on 130 samples is small":** The paper acknowledges this implicitly and does not overclaim FVD results. This level of reporting is appropriate for the paper's scope. *Removed as a nitpick.*

- **"Seer results in Figure 3 use 30 DDIM steps while Table 2 uses 10 steps":** The paper transparently reports these as different evaluation contexts (Figure 3 for visualization quality, Table 2 for speed comparison). No inconsistency. *Removed as a non-issue.*

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs did not surface an insight that the paper itself does not already articulate.

## Suggestions

1. **Add confidence intervals or bootstrap estimates to Table 1.** With 200 episodes and a few random seeds (or even bootstrap resampling of the single run), the paper can report ±CIs for the main results. This is the single change that most strengthens the paper's credibility.

2. **Diagnose the unseen-task generalization bottleneck.** Add a simple analysis (or a few qualitative figures) showing whether failures in unseen tasks stem from slot binding, language understanding, world model prediction, or action decoding. Even a coarse categorization would turn an acknowledged limitation into an actionable finding.

3. **Perform a sensitivity analysis on Seer's DDIM steps.** Test whether using more DDIM steps (e.g., 30, 50) changes Seer's success rate enough to affect the conclusions. This is straightforward to run and would make the comparison more robust.

4. **Clarify in the ablation section (Table 4) that all future-state inputs to the action decoder are predicted slots from the trained world model, not ground-truth slots from the SAVi encoder.** A single sentence would eliminate any remaining ambiguity.

## Score and Decision

The paper proposes a well-motivated and technically sound approach. The core claim — that a compact latent object-centric world model outperforms diffusion-based generative world models in both efficiency and control performance for language-guided robotic manipulation — is supported by consistent experimental evidence across multiple metrics. The ablations are thorough and informative. The main weakness is the absence of statistical uncertainty estimates on the central results, but this is addressable and does not invalidate the paper's conclusions. The paper makes a solid contribution to the intersection of object-centric representation learning, world models, and language-conditioned control.

**MY FINAL SCORE: <pineapple>7.0</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**