Now I have all the information needed. Let me write the consolidated review.

## Summary

MEMO proposes a diffusion-based talking video generation method with two core innovations: (1) a memory-guided temporal module that stores motion information from all previously generated frames via linear attention with causal decay, addressing long-term identity consistency; and (2) an emotion-aware audio module that replaces cross-attention with multi-modal attention and uses detected audio emotions to condition facial expressions via Emotion AdaNorm. The method also contributes a data processing pipeline yielding ~660 hours of high-quality talking head data and demonstrates strong generalization without facial inductive biases.

## Strengths

- **Novel memory-guided temporal module with principled motivation**: The paper identifies a real limitation of existing diffusion-based talking head methods — error accumulation from conditioning on only 2–4 past frames — and proposes a clean solution: linear attention with a causal memory decay mechanism that stores information from all past frames in constant GPU memory. This is supported by ablation (Figure 10) showing longer memory improves temporal coherence, and by human evaluation where MEMO achieves 93.8% best/2nd-best for identity consistency and 91.4% for motion smoothness.

- **Emotion-aware audio conditioning via multi-modal attention and Emotion AdaNorm**: Replacing static cross-attention with multi-modal attention that jointly processes audio and video, combined with dynamic emotion detection from audio to guide expression via adaptive layer norm, is a well-motivated architectural improvement. The ablation (Figure 11) confirms multi-modal attention outperforms cross-attention. Human evaluation shows 92.4% best/2nd-best for expression-audio alignment and 93.3% for overall quality.

- **Strong generalization demonstrated across diverse and out-of-distribution scenarios**: MEMO does not rely on face landmarks, bounding boxes, or other facial inductive biases, enabling it to handle singing, rapping, multiple languages, virtual avatars, and artistic-style reference images. Table 1 shows consistent improvements on an OOD dataset across FVD, FID, and Sync-C, and Figure 8 provides qualitative evidence of this generalization.

- **Large-scale data processing pipeline**: The five-step pipeline (scene detection, face detection, quality assessment, SyncNet filtering, manual inspection) reducing >2,200 hours of raw video to ~660 hours of high-quality data is a practical contribution, particularly given the sensitivity of diffusion training to data quality.

- **Decomposed three-stage training strategy**: The progressive training protocol (face domain adaptation → robust scale-up with loss-based filtering → dynamic past-frame training up to 48 frames) is a well-thought-out approach to bridging the gap between training and inference conditions.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison with the most relevant concurrent work (Loopy)**. The paper explicitly identifies Loopy (Jiang et al., 2024) as "the most related concurrent work to our memory module" and describes it as using "a temporal segment module to model cross-clip relationships" (Section 2). However, Loopy is entirely absent from all experiments (Section 5.1 lists only VExpress, EchoMimic, and Hallo as baselines). Since Loopy's temporal segment module is the natural competitor for MEMO's memory module, omitting it means the paper's central claim — that the memory module provides superior temporal modeling — is unanchored against the closest alternative. Without this comparison, the claim that MEMO "consistently outperforms state-of-the-art" is not fully supported.

2. **Training–inference gap for the memory module remains unvalidated**. The memory module is motivated as leveraging "all previously generated frames," yet during training the model sees at most 48 past frames (Stage 3, Section 4.3). The paper asserts that "48 past frames are sufficient to generalize memory updates over longer sequences" due to the decay scheme, but provides no evidence for this claim. No experiment tests video quality (FVD, identity consistency, Sync-C) as a function of sequence length, especially for 100+ frames. Since the decay mechanism means older frames have exponentially diminishing influence, the effective memory horizon may be limited. Without validation that the module actually mitigates error accumulation over long sequences, the core contribution's effectiveness is unverified.

3. **Emotion detection module is critically underspecified**. The emotion-aware audio module is presented as a key contribution, yet the "newly trained emotion detection model" (Section 4.2) receives no description whatsoever: its architecture, training data, label taxonomy, output dimension, or accuracy are not reported. The Emotion AdaNorm mechanism is described only as "projected into emotion embeddings, which are incorporated into each layer via adaptive layer norm" — no details on projection, per-layer application, or interaction with other conditioning signals. This makes the module impossible to reproduce or ablate independently. Furthermore, no quantitative metric for emotion alignment (e.g., pre-trained emotion classifier accuracy on generated frames) is reported; the only evidence is qualitative (Figure 9) and a human evaluation category that itself lacks rigor (see Minor point 1). For a claimed contribution, this is an unacceptable level of specification.

### Minor

1. **Human evaluation lacks standard methodological transparency**. The paper reports strikingly high top-2 choice percentages (86.6%–93.8%) but provides none of the following: number of evaluators, their expertise/recruitment method, whether they were blinded to method identity, how top-2 choice is defined and whether tied preferences were allowed, the full distribution of preferences across all four methods, or any inter-rater agreement measure. The high percentages may be partially explained by the top-2 design (random chance = 50% per method with 4 methods), but without basic methodological details, the human evaluation — used as key evidence for multiple claims — is insufficiently rigorous.

2. **Multi-modal attention mechanism is not mechanically specified**. Section 4.2 distinguishes multi-modal attention from cross-attention only through loss function notation (conditioning on v|a vs. joint v,a). No architectural details are given: does multi-modal attention involve concatenating audio and video features before self-attention, using separate attention pathways, or a different mechanism? The paper says "jointly processes both video and audio inputs" but does not specify how. Combined with the missing emotion model details, this module cannot be independently implemented.

3. **Decay factor γ in the memory module is not explained**. The memory update formula (Eq. 3) depends critically on γ (a decay factor, 0<γ<1), but the paper does not state whether γ is a learned parameter or a fixed hyperparameter, nor what its value is or how it was chosen. No ablation studies explore different decay schedules. Since γ controls how quickly past information is discounted — and therefore the effective memory horizon — this is a significant missing detail for a module that is the paper's central novelty.

4. **Technical concern: SD 1.5 initialization with rectified flow loss**. The paper initializes with SD 1.5 weights (trained with DDPM loss and a specific noise schedule) but adopts the rectified flow loss from SD3 (Eq. 1). The paper does not address whether the architecture was modified to support the flow formulation, whether the different noise schedules are compatible, or how initialization interacts with the new loss. While this may be a straightforward engineering choice, it requires justification.

5. **Data processing pipeline is claimed as a contribution but not ablated**. The paper presents the pipeline as Contribution 3 (Section 4.4), but no experiment shows its impact (e.g., training without pipeline vs. with it, or measuring Sync-C changes when pipeline filtering is omitted). The 660-hour figure is presented without evidence that the scale or quality of data drives the reported results rather than the architectural innovations.

6. **OOD dataset is too briefly described**. The OOD dataset is described only as "300 video clips across a more diverse set of audios, backgrounds, ages, genders, languages, etc." (Section 5.1) — no further characterization, no comparison of distribution shift relative to the training data. This makes the generalization claim hard to evaluate.

7. **No confidence intervals or standard deviations in Table 1**. While single-run evaluation is common in this space, the absence of any variance measure makes it difficult to assess whether the reported improvements (especially on metrics where differences appear small) are meaningful.

### Trivial

- Figure 1 uses a single anecdotal example of error accumulation in Hallo to motivate the memory module; the paper does not subsequently quantify this effect. This weakens the motivation but does not affect the validity of the proposed method.
- The description of Loopy's approach ("only considers the representative motion frames in other temporal segments") is somewhat reductive; a more charitable engagement would strengthen the related work.

## Nice-to-Haves
- An ablation of the decay factor γ (e.g., γ ∈ {0.5, 0.7, 0.9, 0.99}) to show sensitivity and justify the chosen value.
- Computational cost analysis (GPU memory, runtime per frame) comparing the memory module to standard temporal self-attention with varying context lengths.
- A limitations section discussing known failure cases, computational overhead of memory retrieval, or robustness to emotional ambiguity.
- Validation of the data pipeline's impact by comparing training with and without pipeline filtering, or with different pipeline stages removed.

## Removed Points

These points are flagged to be removed per policy; treat them with caution:

- **"No released artifacts"**: The critic notes that pipeline code and dataset are not released. Per policy, criticisms about release status/availability of artifacts described in the paper are removed.
- **Missing methods (AnimateAnyone, SadTalker-v2, etc.)**: The critic mentions these as missing baselines. Per policy, missing related works are not included as weaknesses since they cannot be independently verified as relevant to the paper's scope.
- **"No runtime or memory comparison"**: Moved to Nice-to-Haves — it is a reasonable suggestion but not a weakness that undermines the paper's claims.

## Novel Insights

The harsh critic makes an insightful observation beyond the paper's own framing: the training–inference gap in the memory module (max 48 frames during training vs. potentially unlimited frames at inference) is not merely a missing ablation but a structural tension in the paper's core claim. The paper asserts that the decay scheme makes 48 frames sufficient, but this is an assertion without evidence — and it implicitly admits that the effective memory horizon is bounded by the decay rate, which would limit the "long-term" benefit the module claims. Additionally, the critic correctly notes that the claim of "first to leverage motion information from all past frames" is in tension with Loopy's concurrent temporal segment approach, making the missing comparison a significant omission. These observations collectively point to a paper whose ideas are promising but whose evaluation design does not match the strength of its claims.

## Suggestions

1. **Add Loopy to all quantitative and qualitative comparisons.** This is the single most important improvement. Without it, the paper's primary claim of state-of-the-art temporal modeling is unsubstantiated against the closest alternative.

2. **Validate the memory module's behavior on long sequences.** Generate videos of varying lengths (e.g., 50, 100, 200, 500 frames) and report FVD, identity consistency (e.g., face feature similarity to reference), and Sync-C as functions of sequence length. Compare to a baseline without the memory module to isolate the effect.

3. **Fully specify the emotion detection model.** Provide architecture, training data, label set, accuracy metrics, and the projection mechanism. Ideally, release the emotion detector to enable reproduction.

4. **Add an automated emotion alignment metric.** Evaluate generated videos using a pre-trained emotion classifier to measure how well detected emotions in generated faces match the emotions in the audio.

5. **Report standard human evaluation methodology.** Include: number of evaluators, recruitment details, whether the evaluation was blinded, the full preference distribution across all methods (not just top-2 aggregated), and inter-rater agreement.

6. **Specify γ and include its ablation.** State whether γ is learned or fixed, its value (or learned range), and show an ablation of decay schedules.

7. **Describe multi-modal attention architecturally.** Clarify whether it uses concatenation before self-attention, dual cross-attention, or another mechanism.

8. **Justify the SD 1.5 + rectified flow loss combination.** Explain whether architectural modifications were made to accommodate the flow formulation and initial experiments validating this choice.

9. **Ablate the data pipeline.** Show the effect of the pipeline on training stability and final metrics by training with and without pipeline filtering.

## Score and Decision

The paper presents well-motivated and interesting architectural ideas (memory-guided temporal modeling, emotion-aware multi-modal attention) that address genuine limitations in existing talking video generation. The qualitative results are compelling, and the strong human evaluation scores (even accounting for top-2 design) suggest real improvements. However, three structural issues prevent acceptance in the current form: (1) the most relevant concurrent work (Loopy) is discussed but not compared experimentally, leaving the core claim unanchored; (2) the memory module's long-sequence behavior is unvalidated, creating a gap between the stated motivation and the experimental evidence; and (3) the emotion detection module — a claimed key contribution — is critically underspecified. These are fixable with additional experiments and clarifications, but in the current submission, the evaluation does not convincingly support the paper's claims of consistent state-of-the-art performance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>