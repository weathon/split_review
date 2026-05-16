Now I have all the information I need. Let me write the consolidated final review.

## Summary

This paper proposes LSlotFormer, the first language-guided object-centric world model. It extends SlotFormer by integrating language instructions into the transformer-based autoregressive slot prediction, enabling future state prediction conditioned on natural language. On the language-table simulated manipulation benchmark, the method achieves substantially higher task success rates than diffusion-based world models (Seer, Susie) while being 4–7× faster in training and inference. The paper also provides ablations on action decoding strategies and evaluates generalization to unseen blocks and tasks.

## Strengths

- **First language-guided object-centric world model.** The paper introduces LSlotFormer, the first approach to incorporate natural language instructions into an object-centric slot-based world model for future state prediction. This is a clearly claimed and defensible contribution (Section 3.1, contributions list).

- **Consistently superior control performance over diffusion-based world models.** On seen tasks with the strictest success threshold (0.05 distance), the method achieves 50.0% success vs. 32.0% for the best diffusion baseline (Susie+VAE) and 6.0% for Seer-F+SAVi, with consistent margins across all thresholds (Table 1). This demonstrates a meaningful practical advantage.

- **Substantial computational efficiency.** The method requires 0.06 s/it for training vs. 0.40 (Seer) and 0.18 (Susie), and 0.19 s/it for inference vs. 0.72 (Seer) and 0.47 (Susie) (Table 2). This 4–7× speedup is a genuine practical contribution for real-time or resource-constrained settings.

- **Systematic ablation studies on action decoding.** The paper explores MLP vs. transformer decoders, slot grouping strategies (by timestep vs. by slot), the effect of language instruction in the action decoder, and the optimal number of future steps (Tables 3, 4; Section 4.6). These ablations generate useful insights for the community, e.g., that providing future state slots (even one step) transforms task success from near 0% to >30%, and that transformers grouping by timestep outperform grouping by slot.

- **Sample efficiency demonstrated.** Despite training on only 7,000 trajectories, the method surpasses Seer-F (fine-tuned on a large pre-training dataset from Something-Something V2) in task success, and achieves competitive FVD (346.59 vs. 205.94 for Seer-F) despite using much less data, supporting the sample-efficiency benefit of operating in compact slot space.

## Weaknesses

### Fatal
None.

### Major

- **LSlotFormer conditioning mechanism is underspecified, harming reproducibility.** The paper states only that the language instruction embedding is "integrated as context of transformer decoder" (Section 3.1, line 72). No detail is given about *how* this integration works — whether via cross-attention, prefix-token concatenation, additive conditioning, or another mechanism, at which layer(s), or with what dimension alignment. Since the entire contribution of language-guided prediction rests on this architectural choice, this is a significant reproducibility gap. The paper also omits standard architectural details (number of transformer layers, attention heads, dimension of feed-forward layers, position encoding scheme) that would be needed to re-implement the method. This is not a fatal issue (the overall approach is clear) but it is the single largest weakness of the current manuscript.

- **The claimed benefits of object-centric representation are not isolated from the latent-predictive approach.** The paper's motivation emphasizes object-centric representation as a key advantage (Section 1, line 21), and claims to "outperform non-object-centric methods" (Section 2.2, line 49). However, the experiments compare only against *diffusion-based* world models (Seer, Susie). No comparison is made with a non-object-centric *latent predictive* world model (e.g., Dreamer-style RSSM with a single global latent vector). Without this control, it is impossible to determine whether the observed improvements stem from object-centricity specifically, or from the latent-predictive paradigm more generally. The +SAVi baselines control for the slot encoder but not for the world model paradigm itself. Adding such a baseline (or at minimum clearly scoping the claim) would substantially strengthen the paper.

### Minor

- **No confidence intervals or variance reported for primary results.** Success rates in Table 1 are based on 200 episodes but lack confidence intervals, standard errors, or hypothesis tests. While the differences are large enough that significance is plausible, the absence of variance reporting makes it impossible for the reader to assess reliability. Bootstrapped 95% confidence intervals would be a straightforward fix.

- **Generalization analysis is shallow.** Unseen task performance is at most 17.4% (Table 1), and the only analysis offered is that "instructions include words that our world model had not previously encountered during training" (Section 4.5). There is no diagnostic breakdown of whether failures stem from poor world model predictions, slot extraction issues for novel objects/positions, or action decoder brittleness. Since the paper lists generalization as a contribution, deeper analysis (e.g., inspecting failure modes qualitatively or ablating components) is expected.

- **No quantitative evaluation of world model prediction accuracy.** The paper relies entirely on downstream task success as a proxy for world model quality. Reporting slot prediction MSE over the prediction horizon would help diagnose where failures originate and would support the qualitative claims made from Figures 3 and 4.

- **Computational speed comparison lacks model size information.** Table 2 reports training/inference time but does not report parameter counts for the compared models. Without knowing the number of parameters, it is unclear whether the speed advantage stems from architectural efficiency or simply from having fewer parameters. Reporting parameter counts would make the efficiency claim more informative and actionable.

- **Mild overclaim regarding "non-object-centric methods."** The claim at line 49 that the method "outperforms non-object-centric methods" is supported only indirectly — the VAE variants of Seer/Susie use non-object-centric VAE latents, but these are still components of diffusion models rather than standalone non-object-centric latent predictive models. The scope of this claim should be tightened to match what is actually compared.

### Trivial

- The characterization of the FVD gap (346.59 vs. 205.94) as "only a small difference" is imprecise — a 140-point gap on FVD is not self-evidently small and should either be quantified more neutrally or supported with context from the literature.

## Nice-to-Haves

- A non-object-centric latent predictive baseline (e.g., Dreamer-style) would cleanly isolate the benefit of object-centric representation.
- Confidence intervals for all success rates would improve statistical rigor.
- A failure-mode analysis for unseen tasks (with qualitative examples) would strengthen the generalization claims.
- Parameter counts for all compared models would make the efficiency comparison more complete.
- Slot prediction MSE over the rollout horizon would provide a direct measure of world model quality.

## Removed Points

These points are flagged to be removed, treat them with caution:
- *"Action decoder training order ambiguous"* — The paper clearly states "As a result of this experiments, we use transformer layers..." (Section 3.2, line 101). The description is clear; the ablations in Section 4.6 explain the reasoning. This is a presentation choice, not a flaw.
- *"Susie is not a full world model"* — The paper already acknowledges this in Section 4.4 (line 139: "a temporally coarse world model... struggles to accurately predict long low-level action trajectories"). This is an acknowledged design choice, not a missed flaw.
- *"The paper does not specify the number of trajectories after filtering"* — This is a superset of poor detail, but the paper states "trajectories filtered with a minimum length of 50 are utilized" (Section 4.1). The exact count after filtering is a trivial implementation detail many papers omit.
- Pure formatting/style nitpicks and phrasing critiques that do not affect the core contribution.

## Novel Insights

The reviews collectively surface an important tension in this paper: the work presents a well-motivated and empirically effective method (language-guided slot-based world models outperform diffusion-based alternatives on this task), but the narrative framing — particularly around "why object-centric representation matters" — is not fully supported by the experimental design. The two reviewer perspectives (harsh critic's methodological rigor vs. strength finder's focus on demonstrated results) highlight that the paper's strongest evidence supports the *method-level* claim ("our architecture works better"), while the *representation-level* claim ("object-centric representations drive this improvement") requires additional controls. This distinction matters because the paper's most interesting insight for the community — the specific design choices for action decoding from slots (Tables 3, 4) — is actually independent of the comparison to diffusion models. The ablations on time-step grouping, future-step horizon, and instruction conditioning are the paper's most novel and transferable contribution, yet they receive less emphasis than the comparison to Seer/Susie.

## Suggestions

1. **Specify the LSlotFormer conditioning mechanism in detail.** Provide a precise description of how the language instruction embedding interfaces with the transformer decoder (e.g., "the T5 embedding is appended as a prefix token to the slot sequence with causal masking" or "a cross-attention layer over the instruction token is added after each self-attention block"). Include number of layers, attention heads, hidden dimensions, and positional encoding choices.

2. **Add a non-object-centric latent predictive baseline or reframe the claims.** Either implement a variant using a global latent vector instead of slots (controlling for the latent-predictive paradigm) or tighten the paper's language so that the comparison is scoped to "diffusion-based generative world models" rather than implying the advantage is specifically due to object-centricity.

3. **Add confidence intervals to all success rate tables.** With 200 episodes per condition, bootstrapped 95% confidence intervals are simple to compute and would significantly improve rigor.

4. **Diagnose generalization failures.** Sample a few failure episodes for unseen tasks and inspect whether the world model predictions were reasonable or not. This would turn a weak number into useful analysis.

5. **Report parameter counts alongside computation times** in Table 2.

## Score and Decision

The paper proposes a novel and well-motivated method (first language-guided object-centric world model), supports its primary comparative claim (outperforms diffusion-based world models) with clear empirical evidence, and provides useful ablation insights. The main weaknesses — underspecified architecture details and an incomplete isolation of the object-centricity benefit — are real but addressable. The core contribution stands and is of value to the community.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>