- Decision: Reject
- Avg Score: 3.00
- Scores: 5, 3, 1
Now I have all the information needed. Let me produce the consolidated review.

## Summary

Simple-TTS proposes an end-to-end latent diffusion model for text-to-speech that operates without phonemizers, forced aligners, duration predictors, or pitch predictors. It adapts the U-ViT image diffusion backbone to 1D audio (U-Audio Transformer), conditions on byte-level ByT5 representations, and modifies the diffusion noise schedule. Trained on 44.5K hours of MLS English data, it achieves a WER of 2.4% (text-only) on LibriSpeech test-clean, nearly matching the ground-truth WER of 2.2%, and outperforms open-source baselines in both objective and subjective evaluations.

## Strengths

- **First diffusion TTS system without phonemizers, aligners, or duration/pitch predictors.** Table 1 explicitly inventories the required components for NaturalSpeech2, VoiceBox, and Simple-TTS, showing that Simple-TTS eliminates all of them. This is a direct reduction in system complexity that the paper uses to define its core contribution.

- **Strong empirical results on standard benchmarks.** In the text-only setting, Simple-TTS achieves a WER of 2.4%, nearly matching the ground-truth WER of 2.2% on LibriSpeech test-clean (Table 2). In the speaker-prompted setting, it achieves a WER of 3.4% vs. Vall-E's 5.9% and a speaker similarity of 0.514 vs. YourTTS's 0.337. A human evaluation (Table 3) confirms statistically significant improvements in both quality MOS (+0.52) and similarity MOS (+1.46) over YourTTS.

- **Key design choices validated by controlled ablations.** The ablation study (Table 4) shows that replacing ByT5 with BPE-based T5 increases WER by 4.4×, and substituting the scaled cosine noise schedule with the standard cosine schedule increases WER by 2.2×. These controlled comparisons provide direct causal evidence for two of the paper's claimed innovations.

- **Practical efficiency with few sampling steps.** Simple-TTS achieves a WER of 4.0% with only 15 DDPM steps in the speaker-prompted setting, already surpassing Vall-E's reported WER (5.9%), demonstrating that the model does not require hundreds of sampling steps to be useful.

## Weaknesses

### Fatal
None.

### Major

- **Potential speaker overlap between training and evaluation sets may inflate quantitative results.** The paper trains on the English subset of Multilingual LibriSpeech (MLS, 44.5K hours from LibriVox) and evaluates on LibriSpeech test-clean (also derived from LibriVox). Both datasets draw from the same audiobook repository, and the paper provides no statement about whether speakers are disjoint between training and evaluation. If speakers overlap, the reported WER (2.4%) and speaker similarity scores could be artifactually favorable because the model has been trained on the same voices it is evaluated on. This issue weakens the headline quantitative claims, though it does *not* affect the human evaluation (Table 3, which compares directly against YourTTS in a controlled subjective setting) or comparisons to baselines trained on entirely different datasets (VITS-LJ, VITS-VCTK, YourTTS).

- **Training data scale advantage over open-source baselines confounds claims of architectural superiority.** Simple-TTS is trained on 44.5K hours of speech, while VITS-LJ (24 hours, single speaker), VITS-VCTK (~44 hours, 109 speakers), and YourTTS (VCTK-scale) are trained on orders of magnitude less data. The paper states that Simple-TTS "outperforms more complex models" without isolating whether the improvements come from the method or simply from greater data scale. The comparisons to proprietary systems (Vall-E, VoiceBox) are fairer in data scale, but those rely on reported numbers with different evaluation setups. A controlled experiment training Simple-TTS on a smaller data subset, or training baselines on a large dataset, would be needed to attribute gains to the architecture.

- **Claim about duration diversity is stated but unsupported.** The paper asserts that unlike NaturalSpeech2, Simple-TTS "is capable of synthesizing diverse speech across the distribution of natural durations" (Section 2). No experiment, visualization, or metric is provided to substantiate this claim.

### Minor

- **Incomplete ablation of the three claimed "key ingredients."** The paper identifies three key ingredients (Section 7): (1) adapting U-ViT to audio (U-AT), (2) byte-level language model (ByT5), and (3) modified noise schedule. Only ByT5 and the noise schedule are ablated (Table 4). The central architectural choice—the U-Net downsampling/upsampling design vs. a flat transformer operating on full-length sequences—is not tested, leaving a gap in the internal validation.

- **Noise schedule modification is underspecified.** The paper describes a "scaled cosine schedule with scale factor s=0.5" but does not provide the exact mathematical formula (e.g., α_t = cos(π/2·t^s) or equivalent). Only a qualitative description and a visualization (Figure 2, not available in text) are given. Given that this is claimed as a key contribution, the lack of a precise definition impairs reproducibility.

- **Confidence intervals not reported for automated metrics.** Table 2 reports single WER and speaker similarity numbers without uncertainty estimates, even though the evaluation set is a filtered subset of test-clean (likely fewer than 1000 utterances). By contrast, the human evaluation (Table 3) appropriately reports 95% confidence intervals from bootstrapping.

- **Ablation results may not reflect convergence behavior.** The ablation studies are trained for only 50k steps (25% of the full 200k), and the paper notes that the full model was still improving at 200k. The relative importance of the ablated components at convergence is unknown.

### Trivial
None.

## Nice-to-Haves

- A brief limitations / failure-case discussion (e.g., performance on long sentences, handling of punctuation, systematic phoneme errors).
- A discussion of inference cost (real-time factor or total generation time), especially since the paper highlights that 15 steps can suffice.
- Releasing the checkpoint upon acceptance (currently stated) rather than "upon acceptance" is standard practice; the existing commitment is adequate.

## Removed Points

- **"Omission of Tortoise TTS comparison."** Removed per the rule against citing missing related works as weaknesses. I cannot independently verify the relevance or availability of Tortoise TTS for comparison in this setting.
- **"Noise schedule missing from paper is fatal."** Downgraded from a fatal claim to a minor weakness. The qualitative description and scale factor (s=0.5) plus Figure 2 provide a reasonable basis for implementation, though the exact formula would improve reproducibility.
- **"Speaker overlap invalidates all quantitative results (fatal)."** Downgraded from fatal to major. The concern is real, but (a) the human evaluation is independent of this issue, (b) comparisons to baselines trained on different datasets (VITS, YourTTS) are unaffected, and (c) the core contribution (end-to-end diffusion without alignments) is not invalidated by inflated absolute numbers.
- **"Inference cost should be discussed."** Moved to Nice-to-Haves. This is useful information but not a flaw in the paper's argument.
- **Strength Finder claims about "addressing an important problem" and "targeting an interesting question."** Removed as generic/superficial. Only specific, verifiable strengths backed by concrete evidence are retained.

## Novel Insights

The reviews surface an important tension: the paper's strongest selling point (simplicity—no aligners, phonemizers, or duration models) is also where the evaluation is weakest. The potential speaker overlap and data scale confounds mean that the reader cannot cleanly attribute the strong results to the method's simplicity rather than to favorable evaluation conditions. Conversely, the human evaluation and ablation studies provide genuine evidence that the core design decisions matter, even if the absolute numbers need qualification. This suggests that the paper's contribution would be better framed around *demonstrating viability* of the end-to-end latent diffusion approach, with candid discussion of the evaluation limitations, rather than around claiming to "outperform" baselines that were trained under very different conditions.

## Suggestions

- **Address the speaker overlap issue directly.** State whether training (MLS) and evaluation (LS test-clean) speakers are disjoint. If they are not, re-evaluate on a truly unseen dataset or at minimum acknowledge the limitation and discuss its likely impact on the reported numbers.
- **Control for data scale.** Train Simple-TTS on a subset of MLS comparable in size to VCTK (~44 hours) and compare to VITS-VCTK and YourTTS trained on the same data. This would isolate the method's contribution from the confound of data volume.
- **Provide the exact noise schedule formula** (e.g., the mathematical expression for α_t as a function of t with scale factor s).
- **Add uncertainty estimates to Table 2** (confidence intervals or standard deviations across evaluation samples).
- **Support or remove the unsupported claim about duration diversity** with experimental evidence.
- **Acknowledge the data scale limitation in the paper's narrative** rather than claiming to "outperform" systems trained on far less data without qualification.
