- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3
Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes H-KD, a knowledge-distillation framework that transfers intermediate decoder features from a pre-trained ANN teacher (Restormer/PromptIR/AdaIR) to an SNN student (SpikerIR) for image restoration. The method is evaluated on five degradation types (denoising, deraining, deblurring, dehazing, defocus deblurring) and claims extreme parameter efficiency (1/300 of the teacher) and energy savings (1/50 of the teacher). The core idea—using ANN decoder features to guide SNN training—is well-motivated, and the denoising results show the student can match or surpass the teacher on some noise levels with dramatically lower energy.

## Strengths

1. **Novel and well-motivated distillation approach**: The idea of aligning ANN decoder features with SNN decoder features (rather than encoder features or logits) is a sensible design choice for image restoration, where decoder features carry critical reconstruction information. The ablation in Table 6 confirms that removing distillation degrades PSNR (from ~32.83 dB to 32.31 dB on BSD68 denoising), directly validating the approach.

2. **Strong denoising results demonstrating feasibility**: On BSD68 with noise σ=25, SpikerIR (30.65 dB) matches or slightly surpasses the Restormer teacher (30.63 dB, Table 1), while using orders of magnitude fewer parameters. This is the paper's strongest evidence that ANN-to-SNN distillation can work for dense prediction.

3. **Concrete energy measurement on neuromorphic hardware**: Table 7 reports actual energy measurements on a Lynxi HP300 platform (1.53 mJ per image for SpikerIR vs 76.41 mJ for the equivalent ANN), providing quantitative evidence of the energy efficiency advantage — roughly a 50× reduction for the same architectural capacity.

4. **Honest treatment of limitations**: Section 7 explicitly discusses slower inference on non-neuromorphic hardware (Figure 10b) and increasing training time per epoch (Figure 10a), which adds credibility and helps guide future work.

## Weaknesses

### Fatal
None.

### Major

1. **Spiking neuron model and core architectural components are unspecified.** The paper introduces "Spiking Block," "Spike Convolution Unit," and "Multi-dimensional Attention" in the caption of Figure 2, but never defines any of them in the text. The spiking neuron model (IF, LIF, parametric LIF, etc.), its firing threshold, reset mechanism, membrane-potential dynamics, and the surrogate gradient function are all absent. Section 5.1 describes the architecture as "a convolutional layer and a ReLU layer" — ReLU is not a spiking neuron; an SNN paper must specify how spike-based computation is achieved. For a paper whose central claim is proposing an SNN architecture and training framework, this is a critical reproducibility gap.

2. **Parameter count inconsistency undermines quantitative claims.** The paper states SpikerIR has "only 0.07M parameters" (Contribution 1) and "1/300 the number of parameters of the teacher network" (abstract). However, the described architecture (4 encoder-decoder levels, channels {48, 96, 192, 384}, 2 SpikerIR blocks per level) would imply substantially more than 70K parameters — a single 3×3 convolution at the 384-channel level alone would account for ~1.3M parameters. Whether the 0.07M figure is a counting error, a different variant, or refers to a different level of analysis is unclear. The reader cannot reconcile the architectural description with the claimed parameter budget, making the central efficiency claim unverifiable.

3. **No comparison against existing SNN restoration baselines.** The paper cites Song et al. (IJCAI 2024) as an SNN-based deraining method and states "we tried to use it to achieve other image restoration tasks with unsatisfactory results" but provides no quantitative comparison on the deraining task where Song et al. is applicable. All comparisons in the experiments are against ANN-only methods. Without an SNN baseline, the reader cannot determine whether the gains come from the H-KD distillation scheme, the SpikerIR architecture, or simply from having more capacity/epochs — the SNN-specific contribution is uncalibrated.

### Minor

4. **Energy claim in the abstract does not match the experiments.** The abstract states "1/50 the energy consumption of the teacher network," but Table 7 (the only energy table) compares SpikerIR against an "equivalent ANN" with the same architecture, not against the actual teacher network (e.g., Restormer with 26.1M parameters). The teacher's energy is never reported. The 1/50 saving against a same-architecture ANN is a different and weaker claim than "1/50 of the teacher network" stated in the abstract.

5. **Deraining results significantly lag the teacher with no analysis.** On deraining (Table 2), SpikerIR shows a large performance gap (~5 dB lower than Restormer according to the reviewer). The paper acknowledges lower scores but does not investigate why distillation fails on this task while succeeding on others (e.g., motion deblurring where SpikerIR is competitive). This limits support for the claim of being a "general" image restoration framework.

6. **Sensitivity analysis missing for key hyperparameters.** Time steps (T=4), distillation weight (γ=0.12), and FFT loss weight (λ=0.1) are set empirically without any ablation or sensitivity study. The energy formula scales linearly with T, making this a particularly important parameter to explore.

7. **FFT loss contribution is not isolated.** The loss function (L₁ + λ·FFT loss) is introduced but never ablated. A simple with/without comparison would clarify whether the frequency-domain loss is a meaningful component of the method.

### Trivial
None.

## Nice-to-Haves
- A comparison or discussion of ANN-to-SNN conversion methods as alternative baselines, which are the most common approach for obtaining accurate SNNs. The paper focuses on direct training + distillation, so this is not a required comparison, but it would contextualize the contribution.
- A time-step ablation (varying T) to show the energy/performance trade-off, which is practically important for deployment decisions.

## Removed Points

These points are flagged to be removed; treat them with caution if reading derived from the reviews.

- **Reproducibility nitpicks about undisclosed hyperparameters**: The paper does state T=4, γ=0.12, λ=0.1, the optimizer (AdamW), learning rate schedule, and epochs. The remaining hyperparameters are standard for this community and do not constitute a missing-critical-detail issue.
- **Criticism about missing appendix content**: The PDF parser strips appendices; missing proofs or ablation details in "the appendix" are an artifact of the extraction process, not a flaw in the original submission.
- **Criticism that the paper does not engage with ANN-to-SNN conversion literature**: Section 2 (Related Work) explicitly mentions ANN-SNN conversion as one of two main training strategies. The paper is focused on direct training + distillation, which is a distinct line of work. Calling this "missing engagement" is inaccurate.
- **Claims about the paper making unfair comparisons that favor the proposed method**: The comparisons are against significantly larger teacher models (26–35M parameters), which creates an asymmetry that disadvantages the teacher, not the student. This is not an unfair comparison.
- **Formatting nitpicks and "garbled text" complaints**: Parser artifacts are not author errors.

## Novel Insights

None beyond the paper's own contributions. The two reviewers largely catalog known issues (missing architectural details, insufficient baselines, overclaimed scope) and known strengths (novel distillation direction, concrete energy numbers) without synthesizing a new observation that transcends what the paper itself states.

## Suggestions

1. **Specify the spiking neuron model explicitly**: State the neuron type (IF/LIF/parametric), its threshold, reset mechanism (reset-to-zero vs reset-by-subtraction), membrane time constant, and the exact surrogate gradient function used. Define what "Spiking Block," "Spike Convolution Unit," and "Multi-dimensional Attention" are — these are currently only named, never described.

2. **Reconcile the parameter count**: Provide a detailed parameter breakdown (by component or block) to clarify whether 0.07M is the full model or a smaller variant, and ensure all tables use consistent numbers. If different experiments use different architectures, state this explicitly.

3. **Add the existing SNN baseline (Song et al. 2024) on deraining**: Even a single comparison on the deraining task would calibrate the SNN-specific contribution and help readers understand whether H-KD improves over state-of-the-art SNN restoration.

4. **Report teacher energy consumption directly**: Show the actual energy of Restormer/PromptIR/AdaIR under the same formula or measurement setup to substantiate the 1/50 claim against the teacher (rather than against a same-architecture ANN).

5. **Add ablations for time steps T and the FFT loss**: These are cheap experiments that would substantially strengthen the paper by showing the method is not brittle.
