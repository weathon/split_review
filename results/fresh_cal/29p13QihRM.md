Now I have all the evidence I need. Let me produce the consolidated review.

## Summary

This paper proposes LSlotFormer, the first language-guided object-centric world model for visuo-linguo-motor control. It extracts object-centric slot representations from video using SAVi, then autoregressively predicts future slots conditioned on a language instruction (via T5 encoding) using a transformer-based architecture. The predicted future slots are fed to a learned action decoder for control. On the language-table benchmark, the method outperforms diffusion-based world models (Seer, Susie) in control task success rate while requiring substantially less computation (85% less training time, 74% less inference time). The paper includes thorough ablations on action decoder design and the necessity of future-state prediction.

## Strengths

1. **Superior control task success rate** — Table 1 shows the proposed method achieves 55.5% success at the strictest threshold (0.05), substantially outperforming the best diffusion-based baseline Seer-F (38.5%) and Susie (15.5%). This directly supports the central claim that the object-centric latent world model surpasses generative alternatives in control performance.

2. **Substantially lower computational cost** — Table 2 reports training at 0.06 s/it and inference at 0.19 s/it, an 85% and 74% reduction respectively compared to Seer (0.40/0.72), while also being faster than Susie (0.18/0.47). This computational advantage is a core contribution that holds regardless of baseline tuning details.

3. **Sample efficiency** — Trained from scratch on only 7,000 trajectories, the method beats Seer-S (same data, 14.5%) and closely approaches Seer-F (pretrained on large-scale Something-Something V2, 38.5%) at the 0.05 threshold, while also having competitive FVD (346.59 vs 641.84 vs 205.94). This demonstrates the benefit of operating in a compact object-centric latent space.

4. **Systematic exploration of action decoder designs** — Section 4.6 and Table 3 compare MLP, transformer-by-slot, and transformer-by-timestep architectures, finding that the transformer-by-timestep achieves the best performance (38.0% at 0.05 vs 25.5% for MLP). The ablations on "how far to look" (Table 4) and the "is a world model necessary" experiment cleanly demonstrate that future state information is critical for control.

## Weaknesses

### Fatal

None.

### Major

1. **No uncertainty quantification for the main success-rate results.** Table 1 reports success rates from 200 episodes but provides no variance, confidence intervals, or information about random seeds. The paper does not mention whether results are averaged over multiple training runs or over multiple environment seeds. While some gaps are large (e.g., 55.5% vs 14.5% at the 0.05 threshold), others are smaller (42.0% vs 33.0% at 0.075 threshold for unseen blocks). The central claim — that the object-centric world model *surpasses* diffusion-based alternatives — rests on these numbers, and the reader cannot judge statistical reliability without error bars. Reporting standard deviations or bootstrapped intervals over at least 3 training seeds is standard practice for control evaluations and is needed here.

2. **Potential unfairness in baseline DDIM step configuration.** The DDIM sampler for Seer and Susie is set to 10 steps for control evaluation (line 126), described as "determined through trial and error to achieve high-quality generation." However, the qualitative visualization in Figure 3 uses 30 DDIM steps for Seer ("Seer results are generated using 30 DDIM sampler steps"), creating a tension: if 30 steps are needed for the qualitative results shown, why are control evaluations conducted at 10? The paper argues that increasing steps would widen the computational gap, but this does not address whether control performance for Seer/Susie would improve with more sampling steps. The paper should either demonstrate that 10 steps saturates control performance (e.g., evaluating at 10, 30, 50 steps on a subset) or report the best-case baseline performance to ensure a fair comparison.

### Minor

3. **Slot loss permutation invariance is not addressed.** The world model is trained with a simple MSE loss on slot embeddings with a fixed ordering (Equation 1): $\mathcal{L}_{\mathrm{slot}} = \frac{1}{L_{\mathrm{prd}}}\frac{1}{K}\sum_{t}\sum_{k}||\hat{s}_{tk} - s_{tk}||^2$. Slot-based models typically use Hungarian matching or a permutation-invariant loss to handle the fact that slot indices are not semantically aligned across timesteps. Without such a mechanism, the loss could penalize correct predictions that happen to be assigned to different slot indices, potentially degrading the world model's predictions. The paper should clarify whether any matching is applied and, if not, discuss the implications.

4. **Missing implementation details for reproducibility.** The paper does not report specific values for the number of slots *K*, slot dimension *D*, SAVi training details (number of frames, reconstruction loss), LSlotFormer hyperparameters (number of transformer layers, attention heads, learning rate, batch size, optimizer), or the specific T5 model variant beyond "T5-base." These details are needed for reproducibility and are standard to include.

5. **Narrow generalization evaluation.** The "unseen blocks" evaluation (Section 4.5) swaps shapes between existing color-shape combinations (e.g., green pentagon instead of green star), which tests only combinatorial generalization of known attributes. This is a very limited test — novel colors or object types entirely absent from training would be a stronger assessment. The generalization results are low across all methods (5–12%), and the paper's claims about generalization should be tempered accordingly.

6. **Minor inconsistency in DDIM steps between text and figure.** The evaluation setup (line 126) states 10 DDIM steps for baselines, but Figure 3's caption reports "Seer results are generated using 30 DDIM sampler steps" for the qualitative visualization. This discrepancy should be resolved — either clarify that the visualization uses a different configuration, or explain why the control evaluation uses fewer steps.

### Trivial

- None beyond the issues already noted above.

## Nice-to-Haves

- An ablation where the action decoder is trained with varying numbers of future steps (1, 5, 10, 20) should explicitly confirm that the decoder was retrained for each setting (implied but not stated).
- The paper could include a version of the method where SAVi is frozen from a general dataset (e.g., CLEVR) without finetuning on language-table, to isolate whether performance stems from the world model architecture or from domain-specific encoder specialization. This is a natural extension but not a required fix, as the Seer+SAVi baseline already controls for the encoder.

## Removed Points

These points were raised by one or more reviewers but are removed after verification against the paper:

- **SAVi domain pretraining not controlled for** (Removed: partially inaccurate). The paper *does* control for this via the Seer+SAVi baseline, which uses "the same SAVi model employed in our approach" (line 119). The SAVi encoder is identical between the proposed method and Seer+SAVi; the difference is that SAVi operates on real frames vs. generated frames. The concern about SAVi+real > SAVi+generated frames is a different issue and is already addressed by the paper's overall comparison design.

- **Action decoder train-test mismatch** (Removed: factually incorrect). Figure 2's caption clearly states: "The action decoder is trained by inputting the current state slots and future state slots obtained from the trained world model." Both training and inference use world-model-predicted slots, so there is no mismatch.

- **FVD gap should be discussed more** (Removed: already discussed). The paper states: "Seer-F scores the best at 205.94, followed by our approach at 346.59... this further highlights the sample efficiency of our method" (lines 174-175). The argument that control performance (not video quality) is the relevant metric is a defensible position that the paper explicitly takes.

- **Seer-F pretraining advantage** (Removed: already acknowledged by the paper). The paper notes that Seer-F has a data advantage from pretraining on Something-Something V2 and uses this as context to highlight sample efficiency.

- **Missing related works** (Removed: you do not have external sources to confirm existence).

- **Formatting/style nitpicks, typos, garbled text** (Removed: these are parser artifacts, not author errors).

- **Slot dimension/number of slots not specified** — This is merged into Weakness #4 (missing implementation details) rather than treated as a separate point.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' analyses did not surface a perspective on the work that the paper itself does not already articulate.

## Suggestions

1. **Add confidence intervals or standard deviations** for all success-rate tables by evaluating over at least 3 random seeds of model training. This single addition would substantially elevate the credibility of the main claims.

2. **Conduct a controlled experiment on DDIM steps** — evaluate Seer at 10, 30, and 50 DDIM steps on a subset (e.g., 50 episodes) to show whether control performance saturates at 10 steps. If it does not, report the best-case baseline and discuss whether the computational trade-off still favors the proposed method.

3. **Clarify the slot loss permutation invariance** — specify whether Hungarian matching or any other permutation-handling mechanism is used for the MSE loss, or discuss why fixed ordering is sufficient for this particular setting.

4. **Add a reproducibility appendix** with specific values for K (number of slots), D (slot dimension), SAVi training details, LSlotFormer hyperparameters, and training configuration.

5. **Resolve the DDIM step discrepancy** between the evaluation setup (10 steps) and Figure 3's caption (30 steps for Seer).

6. **Temper generalization claims** — the current evaluation of unseen blocks only swaps shapes between existing color-shape combinations, which is a narrow test. Acknowledge this limitation more explicitly.

## Score and Decision

**Originality**: Good — first language-guided object-centric world model. The paper clearly builds on SlotFormer and SAVi but the integration with language conditioning for control is novel.

**Importance of research question**: High — efficient world models for language-conditioned control are practically important and computationally relevant.

**Claims well supported**: Partially — the core claims are supported by the data, but the lack of statistical uncertainty quantification and the DDIM step concern reduce full confidence.

**Soundness of experiments**: Good experimental design with thoughtful ablations and controlled comparisons (Seer+SAVi baseline is well-motivated). The two major concerns above are fixable.

**Clarity of writing**: Clear and well-structured. The figures and ablations are informative.

**Value to the research community**: Positive — demonstrates that latent object-centric prediction can outperform pixel-level generation for control while being substantially more efficient.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>