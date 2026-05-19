Now I have all the information needed. Let me compile the final consolidated review.

---

## Summary

This paper proposes CRAFT, a framework for jointly modeling audio spectrograms and raw waveforms in transformers. It introduces three components: a multi-scale audio embedding (MSAE) for waveform tokenization, a contrastive learning loss (SWaCL) to align spectrogram and waveform representations during pretraining, and bottleneck fusion tokens (SWaB, adapted from MBT) during finetuning. On AudioSet balanced set, CRAFT achieves 33.4% mAP, a 2.0% improvement over the batch-size-controlled spectrogram-only baseline (180-SSAST-AST at 31.4%), demonstrating that cross-representation modeling can improve audio classification.

## Strengths

- **CRAFT yields a real, measurable improvement over a properly controlled baseline.** Table 4 and the ablation text show that CRAFT (180-PSWaCL-SWaB) at 33.4% mAP outperforms the batch-size-matched spectrogram-only model (180-SSAST-AST at 31.4%) by 2.0% on AudioSet-bal. The 2.0% gain is modest but genuine, and it is achieved without ImageNet pretraining.

- **Naive joint training fails, motivating the proposed design.** The paper shows that naively adding waveforms during pretraining and finetuning (SWaPT-SWAST) underperforms the spectrogram-only SSAST baseline (Table 1). This negative result provides empirical justification that cross-representation modeling requires deliberate alignment, not just concatenation.

- **Figure 2 shows that adding contrastive learning does not degrade pretraining metrics while enabling downstream gains.** The masked-patch accuracy and MSE for PSWaCL are close to those of SSAST throughout pretraining, yet finetuning mAP rises. This demonstrates that the contrastive objective enriches representations without harming the primary pretraining task.

- **MSAE fills a gap for waveform tokenization in transformer-based audio models.** Prior transformer audio models (AST, HTS-AT, SSAST) operate exclusively on spectrograms. The multi-scale 1D convolution design with kernel sizes 11, 51, and 101 provides a principled waveform embedding that integrates with existing patch-based architectures.

## Weaknesses

### Fatal

None.

The core experimental result — that CRAFT improves over a batch-size-controlled spectrogram-only baseline — is intact. The weaknesses below concern framing, overclaiming, and missing details, not invalidation of the central finding.

### Major

- **The headline 4.4% improvement conflates method gain with batch-size scaling.** The abstract and introduction claim "4.4% higher mAP on AudioSet balanced set compared with the spectrogram-based counterpart" (SSAST at batch size 24: 29.0% → CRAFT: 33.4%). However, the paper's own ablation shows that simply scaling SSAST to batch size 180 yields 31.4% mAP (Table 4). The incremental gain of CRAFT over this fair, batch-controlled baseline is **2.0%** (31.4% → 33.4%), not 4.4%. While the paper discloses the batch-size breakdown in Section 4.4, the abstract and intro present the inflated figure without qualification, which misrepresents the contribution's magnitude.

- **SWaCL (contrastive learning) provides zero independent benefit.** Table 5a and the ablation text state: 180-SSAST-AST = 31.4%; 180-PSWaCL-AST = 31.4%. Adding the contrastive loss alone yields no improvement. The paper acknowledges this numerically but continues to frame SWaCL as a key innovation in the abstract and introduction ("innovative cross-representation contrastive learning approach"), without prominently noting that it is ineffective on its own. SWaCL's role is enabling SWaB to work — it is a necessary enabler, not an independent contributor — and this should be explicitly communicated rather than left for readers to infer from the ablations.

- **The paper inaccurately claims SWaB-only "matches SSAST."** The ablation text states "either PSWaCL-only approach or SWaB-only approach can only match the performances of SSAST." Table 3 shows SSAST-SWaB at 30.4% mAP. Using the paper's own default batch-size baseline (180-SSAST-AST = 31.4%), this is **1.0% worse**, not a match. This is a factual error in the paper's characterization of its own results.

- **"SOTA comparable" claims on ESC-50 are overstated.** The paper reports 90.1% accuracy on ESC-50 and claims "SOTA comparable performances." However, HTS-AT (Chen et al., 2022), which the paper itself cites, achieves 97.0% on ESC-50 — a 6.9% gap. The correct claim is that CRAFT improves over SSAST; calling 90.1% "SOTA comparable" is misleading.

### Minor

- **Key architectural hyperparameters are unreported.** The number of bottleneck tokens (B), which layer(s) the bottleneck fusion is applied at, and the projection head dimension for the contrastive loss are not specified anywhere in the paper. These are important for reproducibility and for understanding the method's overhead.

- **Computational cost is not discussed.** CRAFT uses separate encoder passes for spectrogram and waveform during finetuning, plus bottleneck computations. The paper does not report the increase in FLOPs, parameters, or inference time relative to the SSAST baseline. Since the gain over the controlled baseline is 2.0%, readers cannot assess whether the added compute is justified.

- **The claim about ESC-50 yields two different comparison baselines depending on which SSAST variant is referenced.** The 5.4% gain (84.7% → 90.1%) is over SSAST without ImageNet pretraining. However, SSAST with ImageNet pretraining achieves 88.7% on ESC-50, against which CRAFT's gain is only 1.4%. Since CRAFT does not use ImageNet pretraining, the paper should explicitly address this distinction.

### Trivial

- MSAE kernel sizes [11, 51, 101] are used without ablation or justification for these specific values.
- The phrase "Patchfy function... are the same as SSAST as a convolution operation" (Section 3.1, line 58) has a minor grammatical error ("are" → "is") but the meaning is clear.

## Nice-to-Haves

- An experiment testing **180-SSAST-SWaB** (SSAST pretrained at batch 180, then finetuned with bottleneck fusion) would cleanly separate whether SWaB needs SWaCL pretraining specifically or merely any good pretrained representation.
- A comparison against simple late fusion (concatenating logits of independently trained spectrogram and waveform models) would calibrate the value of joint modeling.
- Analysis of the bottleneck tokens' attention patterns could provide direct evidence for the claimed "temporal misalignment" mitigation.
- Generalization to other within-modality representation pairs (e.g., MFCC + logmel) would strengthen the claim that the approach is broadly applicable.

## Removed Points

These points were identified by reviewers but are either unsupported by the paper's content, incorrect, or outside the evaluation scope:

- **"The method borrows heavily from existing work without sufficient differentiation"** — The harsh critic correctly notes that SWaB is adapted from MBT and contrastive learning from SimCLR. However, the paper shows empirically that naive fusion fails (SWaPT-SWAST underperforms), and the specific combination of contrastive learning between spectrogram/waveform views with bottleneck fusion is not present in prior work. The empirical evidence of the difficulty (SWaPT-SWAST degrading performance) is itself a differentiator. This criticism is generic and ignores the paper's own evidence.

- **"No justification for MSAE kernel sizes [11, 51, 101]"** — The paper provides a justification: "smaller kernel sizes capture fine-grained temporal-frequency responses, while those with larger kernels extract long-term temporal-frequency characteristics." An ablation would strengthen this but the rationale is stated.

- **"The Patchfy operation is stated to be the same as SSAST, but SSAST uses a linear projection of flattened patches, not a convolution"** — The paper explicitly says "our Patchfy function on both spectrograms and waveforms are the same as SSAST as a convolution operation." Whether SSAST uses a convolution or linear projection is debatable depending on implementation, but the paper's claim is self-consistent. This is a technical tangent that does not affect the paper's core contribution.

- **"SWaPT-SWAST performance is not analyzed (no visualization)"** — This is a request for additional analysis, not a weakness. The negative result is clearly reported in Table 1.

- **"Figure 1 suggests bottlenecks at every layer but the text says one layer"** — Without access to the figure, this cannot be verified. The text says "If we opt to apply fusion bottlenecks at **one** transformer encoder layer" (emphasis added), which is unambiguous. If the figure differs, it would be clarified in a camera-ready version.

- **"Missing limitations section"** — A brief limitations discussion appears in the conclusion ("Future works involve the incorporation of masked autoencoder based methods and the optimization of computation consumptions"). This could be expanded but its absence is not a weakness that undermines the paper.

- **"Statistical significance not reported"** — Single-run evaluation with point estimates is standard practice for AudioSet and ESC-50 benchmarks in audio ML. Demanding confidence intervals for a system paper using established metrics exceeds community norms.

## Novel Insights

None beyond the paper's own contributions.

The reviews surface no genuinely novel observation about the paper that the paper does not already articulate. The interdependence between SWaCL and SWaB — where contrastive pretraining provides zero benefit on its own yet is necessary for the bottleneck fusion to work — is the paper's most interesting finding, and it is present (though somewhat buried) in the ablation discussion. The key takeaway is that cross-representation alignment in audio requires both semantic-level (contrastive) and token-level (bottleneck) mechanisms, and neither works without the other.

## Suggestions

1. **Reframe the central claim.** Lead with the 2.0% improvement over the batch-controlled baseline (180-SSAST-AST → CRAFT), and clearly separate the batch-size scaling effect from the method's contribution. Move the 4.4% figure to a footnote or explicit decomposition.

2. **Correct the factual error.** Revise "either PSWaCL-only approach or SWaB-only approach can only match the performances of SSAST" to accurately reflect that SWaB-only (SSAST-SWaB at 30.4%) underperforms the batch-size-matched baseline (31.4%).

3. **Qualify the ESC-50 "SOTA" claim.** Acknowledge that 90.1% is 7% below methods like HTS-AT (97.0%) and frame the result as "improvement over SSAST" rather than "SOTA comparable."

4. **Disclose architectural details.** Report bottleneck token count B, the specific layer(s) where bottlenecks are applied, the contrastive projection head dimension, and total parameter count / FLOPs for CRAFT versus SSAST.

5. **Add the controlled baseline experiment.** Run and report **180-SSAST-SWaB** to directly test whether SWaB requires SWaCL-specific pretraining or works with any strong pretrained representation.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>