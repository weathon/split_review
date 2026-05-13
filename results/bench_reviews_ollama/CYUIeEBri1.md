No human calibration reviews are available. I have now read the full paper and the two AI-generated reviews. Let me synthesize the final review.

Let me carefully verify the key claims in the harsh critic's review against the paper:

**Claim 1: Unfair baseline comparison (no noise-augmented audio-only baselines)**
The paper compares AV-SDS against audio-only baselines (Wav2Lip, GeneFace, CodeTalker, Tri-Modal) under noise. These baselines were not designed/trained for noisy conditions, while AV-SDS uses AV-HuBERT (pre-trained with noise augmentation). This is a valid concern — the noise robustness might largely come from AV-HuBERT rather than the proposed framework. However, the paper does compare against the cascade AV-S2UM+U2S+S2X which also uses AV-HuBERT, showing the direct pipeline is better. Also, the paper argues the point is about using AV speech (with visual) vs. audio-only — this is inherently the contribution. The question is: is this truly unfair? The baselines are standard models for their tasks, evaluated under noise to show they degrade. The fairer question would be whether noise-augmented audio-only baselines could match. This is a valid concern but not necessarily fatal — the paper's claim is that AV speech provides robustness, which is demonstrated. Still, attributing that robustness specifically to the discrete-unit framework vs. just AV-HuBERT is less well-supported.

**Claim 2: Missing ablation for discrete-unit bridge (continuous AV-HuBERT features vs. discrete units)**
The paper states in Section 3.2: "While it's possible to use the AV-HuBERT representation directly to obtain discrete units, we opt for the Speech SSL model, trained specifically on speech data, to ensure unified speech discrete units across different modalities." This directly addresses why they don't use AV-HuBERT continuous features — they want unified discrete units that can bridge across modalities. However, this doesn't fully address the ablation question. The paper argues for units as a bridge, but doesn't empirically verify that continuous features would be worse (or equivalent). This is a valid concern but not necessarily fatal — the paper provides a reasoned argument for why units are needed (lack of paired data, unified representation across modalities).

**Claim 3: AV-SDS underperforms audio-only at low/no noise**
Looking at Table 2d data mentioned: at SNR=15, AV-SDS achieves FGD=4.434 vs. Tri-Modal's 4.322. This is a valid observation. The paper does discuss this implicitly by focusing on degradation slopes rather than absolute performance. However, the paper does not explicitly acknowledge this trade-off, which is a legitimate concern. The gap is small (0.112 in FGD) and may be an acceptable cost for the noise robustness. This is a valid minor-to-moderate concern about completeness of discussion, not a fatal flaw.

**Re: The ReVISE comparison for novelty**
The paper cites ReVISE (Hsu et al., 2023) in Section 2.2 and uses it as a comparison. The claim that AV-SDS is conceptually similar to ReVISE has some merit — ReVISE also uses AV→units. But AV-SDS applies this to body language synthesis across multiple modalities, which is a genuine extension. This is about novelty framing, not a fatal flaw.

**Re: Unit2X is just "substituting one input embedding for another"**
This is true but somewhat reductive. The contribution of showing that discrete units can serve as a universal intermediate representation across 4 different modalities is non-trivial and experimentally validated.

Let me now write the final consolidated review.</think>Now I have the full paper content. Let me carefully verify the harsh critic's claims against the actual paper text, then write the consolidated review.

## Summary

The paper proposes AV-SDS, a two-stage framework for noise-robust audio-visual speech-driven body language synthesis that uses discrete speech units as an intermediary bridge between audio-visual speech input and multiple body language output modalities (talking heads, landmarks, 3D mesh, co-speech gestures). The first stage (AV-S2UM) maps audio-visual speech to discrete units via AV-HuBERT, and the second stage (Unit2X) synthesizes body language from these units, replacing the audio encoder in existing models with a unit-based encoder.

## Strengths

- **Effective discrete-unit bridge for the paired data gap**: The paper correctly identifies the lack of paired visual-speech/body-language data as a key bottleneck. The two-stage framework elegantly sidesteps this by routing through discrete units that can be extracted from audio-only paired data. Table 1 provides direct evidence: Unit2X matches or exceeds S2X across all four modalities (e.g., FGD 3.976 vs. 4.133 for mesh), and substantially outperforms the cascade U2S+S2X (LSE-C 7.34 vs. 5.74 for landmarks), confirming that direct unit-to-body-language is a viable and superior intermediary.

- **Demonstrated noise robustness across four modalities**: Table 2 shows that under increasing noise (SNR 15→−15), AV-SDS degrades far less than audio-only baselines. For co-speech gestures (Table 2d), AV-SDS degrades by only 0.409 FGD (4.434→4.843) versus 1.588 (4.322→5.910) for the Tri-Modal baseline. Similar trends hold for talking heads, landmarks, and mesh.

- **Principled semantic vs. acoustic unit design**: The paper assigns semantic units (HuBERT-derived) to semantically-driven modalities and acoustic units (RVQ-derived) to rhythm-driven modalities. Table 3 validates this: AV-S2UM(U^a) achieves the best LSE-C/LSE-D (audio-visual sync), while AV-S2UM(U^s) achieves the best WER (semantic fidelity), confirming each unit type preserves its targeted information category.

- **Zero-shot generalization to gestures**: Section 4.4 notes that AV-S2UM is trained only on LRS3, making the co-speech gesture experiments (Table 2d) zero-shot for that module, which demonstrates genuine generalization beyond the training domain.

## Weaknesses

### Fatal
None.

### Major

- **Conflation of noise robustness from AV-HuBERT vs. the proposed framework**: The central noise-robustness claim is that AV-SDS provides robust synthesis, but the audio-only baselines (Wav2Lip, GeneFace, CodeTalker, Tri-Modal) were not designed for noisy conditions, while AV-SDS relies on AV-HuBERT pre-trained with noise augmentation on large-scale AV data. The demonstrated robustness may largely reflect AV-HuBERT's inherent noise robustness rather than a contribution of the discrete-unit framework. The paper would be substantially strengthened by including (a) an audio-only baseline with noise-augmented training or speech-enhancement preprocessing, and/or (b) an ablation using continuous AV-HuBERT features directly for synthesis (bypassing the discrete-unit stage). Without such comparisons, it is difficult to attribute the noise robustness specifically to the two-stage discrete-unit architecture rather than to the pre-trained encoder. That said, this does not invalidate the practical finding that the complete AV-SDS pipeline is more noise-robust than standard audio-only approaches—the attribution of *which component* drives the robustness is simply unclear.

- **AV-SDS underperforms audio-only baselines under mild/no noise conditions, unacknowledged**: At SNR=15 (Table 2d), AV-SDS achieves FGD=4.434 vs. Tri-Modal's 4.322 for co-speech gestures—a worse result under mild noise. Similar trends may exist in other tables (the paper focuses on degradation slopes rather than absolute performance). This quantization cost is a real trade-off: noise robustness comes at the expense of some clean-condition performance. The paper does not discuss this trade-off, which matters for practical deployment where most operating conditions are not extreme noise. This is not fatal but is an incomplete analysis of a real cost.

### Minor

- **The discrete-unit bridge is architecturally simple**: Section 3.3 describes Unit2X as substituting the audio encoder with a unit-based encoder (LUT for semantic units, RVQ for acoustic units). While the paper frames this as a module, the synthesis step itself involves no architectural innovation—the contribution is the systematic demonstration that this substitution works across four modalities. This is fine as a contribution (showing feasibility effectively), but the novelty claim should be appropriately scoped.

- **AV-GES test set details are sparse**: The paper curates a new AV-GES test set for co-speech gesture evaluation (565 utterances), described in Section 4.4 but with no discussion of quality controls, gesture alignment procedures, or release plans. As the sole modality with paired AV-gesture evaluation data, more information would increase confidence.

### Trivial
None.

## Nice-to-Haves

- Unit prediction accuracy under noise (comparing predicted units from noisy AV vs. clean audio) would directly validate AV-S2UM's information preservation, rather than relying solely on downstream WER as a proxy.
- Analysis of what clean-condition performance gap would be acceptable for different deployment scenarios, making the quantization cost discussion more concrete.
- Attention visualizations showing which visual features AV-S2UM attends to at different noise levels, to illuminate the information flow.

## Removed Points

- **Claim that ReVISE makes the novelty "incremental"**: The paper cites ReVISE (Hsu et al., 2023) and uses it as a comparison in Table 3. While ReVISE uses AV→semantic units for speech enhancement, AV-SDS applies the unit-based bridge to four distinct body language synthesis tasks (not speech enhancement), with both semantic and acoustic units—an extension in scope and applicability. Calling this "incremental" overstates the overlap; the contribution is in demonstrating and validating the bridging strategy for generation tasks.

- **"Unit2X is just substituting one embedding for another, no architectural innovation"**: This is accurate but presented as a weakness rather than a design choice. The paper's contribution is precisely showing this simple substitution works universally across modalities—a finding that needs empirical validation, which the paper provides. Removed as an overstatement of a minor observation.

- **Missing ablation for audio-only S2UM with noise augmentation**: While useful, this is a specific experimental addition rather than a fundamental flaw. The paper's claim is that audio-visual speech provides robustness—the comparison with audio-only without noise augmentation is a valid way to show the advantage of incorporating visual information, even if it doesn't isolate every factor perfectly.

- **Reproducibility concern about vocabulary sizes and transposed convolution design**: These are minor implementation details. The number of transposed convolution layers (n=1 for semantic, n=3 for acoustic) and architecture details are provided; vocabulary sizes are determined by standard SSL models (HuBERT, HiFi-Codec). This is nitpicking.

- **Video-driven comparison (DPE) is a "straw man"**: The comparison in Section 4.6 explicitly acknowledges the different objectives (speech-driven content preservation vs. video-driven transfer) and serves to clarify the distinction, not to claim superiority over a fundamentally different approach.

- **Criticisms about AV-GES dataset release or curation details**: The paper provides sufficient information (565 utterances, sourced from TED-GESTURE via the Afouras et al. methodology). More details would help but this doesn't undermine the results.

- **Strength Finder claims about "first direct AV speech-driven multi-modal synthesis framework" being a strength**: This is a framing claim rather than a substantive strength. The "first" claim is about scope definition. Removed as generic.

## Novel Insights

The paper reveals an interesting trade-off space: using pre-trained self-supervised representations as discrete unit bridges provides noise robustness but introduces quantization loss that can hurt performance under clean conditions. The semantic vs. acoustic unit distinction is well-motivated and empirically validated, showing that different body language modalities benefit from different speech information granularities—a finding that could inform future multi-modal synthesis architectures.

## Suggestions

- Add at least one fair comparison for noise robustness: either re-train an audio-only baseline with noise augmentation, or add a speech enhancement front-end + existing model pipeline. This would clarify whether the robustness comes from AV information, the discrete-unit framework, or AV-HuBERT specifically.
- Explicitly discuss the clean-condition performance gap and the quantization cost, so readers can make informed decisions about when to deploy the method.
- If possible, add an ablation using continuous AV-HuBERT features (without discrete units) directly for body language synthesis, to validate that the discrete-unit stage is necessary rather than just using a noise-robust encoder directly.

## Assessment

The paper makes a solid, well-validated contribution: it demonstrates that discrete speech units can effectively serve as a universal bridge between audio-visual speech and body language synthesis across four modalities, achieving meaningful noise robustness. The experiments are thorough across four tasks, the semantic/acoustic unit distinction is well-motivated and validated, and the zero-shot generalization to gestures is a genuine strength. The key limitation is that the noise-robustness results conflate the contribution of AV-HuBERT (a pre-trained, noise-augmented encoder) with that of the proposed two-stage framework, and the paper doesn't disentangle these factors. The unacknowledged clean-condition performance gap, while small, should be discussed. These are addressable concerns that weaken attribution but don't invalidate the practical utility of the complete system.

**Originality**: Moderate. The discrete-unit bridging idea builds on prior work (ReVISE, speech-to-speech translation) but extends it meaningfully to multi-modal body language synthesis with both semantic and acoustic units.

**Importance**: Good. Noise-robust speech-driven synthesis is a practical and under-explored problem.

**Claims support**: Partially supported. The system works, but the specific contribution attribution (discrete units vs. AV-HuBERT) is unclear.

**Experiments**: Comprehensive across four modalities but with fairness gaps in baseline comparisons.

**Clarity**: Good. The paper is well-structured with clear motivation and methodology description.

**Community value**: High. The framework is general and can be integrated with future synthesis models.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>