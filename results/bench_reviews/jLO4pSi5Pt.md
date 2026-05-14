Now I have all the information needed. Here is the consolidated final review.

---

## Summary

This paper studies the underexplored problem of test-time adaptation (TTA) for vision-language models (VLMs) under long-tailed test distributions. The authors identify two VLM-specific failure modes — text-induced tail erosion and modality-bias amplification — and propose L-TTA, a three-component framework comprising Synergistic Prototypes (SyPs) to enrich tail-class representations, Rebalancing Shortcuts (RSs) with class re-allocation loss for dynamic adaptation, and Balanced Entropy Minimization (BEM) to counteract head-class bias in standard entropy minimization. Experiments on 15 datasets across three imbalance ratios and four additional backbones show consistent improvements over existing TTA methods.

## Strengths

- **First systematic study of long-tailed TTA for VLMs, with VLM-specific failure mode analysis.** The paper identifies two failure modes unique to this setting (text-induced tail erosion and modality-bias amplification) and provides quantitative evidence in Figure 1(b). This problem formulation is genuinely novel — prior TTA methods for VLMs assume balanced test distributions, and prior class-imbalanced TTA methods (SAR, DELTA, LAME) are designed for unimodal backbones. The paper makes a clear case that VLM-specific challenges require VLM-specific solutions.

- **Extensive empirical evaluation across diverse settings.** L-TTA is evaluated on 15 datasets under three imbalance ratios (10, 20, 50) across OOD, cross-domain, and corruption benchmarks. Performance holds on four additional backbones (ViT-L/14, ViT-H/14, SigLIP-L/16, MetaCLIP-BigG). The gains are consistent and often substantial — e.g., +1.47%/1.70% accuracy/macro-F1 over the best competitor on the OOD benchmark at imb=10, and +2.87%/2.64% on the corruption benchmark. This breadth of validation convincingly demonstrates the method's effectiveness and generality.

- **Coherent three-component design with theoretical grounding.** Each component (SyPs, RSs, BEM) is motivated by a specific aspect of the long-tail TTA problem. Propositions 1 and 2 provide theoretical justification for BEM's rebalancing capability (formalizing how standard EM biases head classes and how BEM reduces the optimization gap). The ablation study (Table 6) confirms each component contributes positively.

- **Favorable efficiency–performance trade-off.** L-TTA requires 1.45h and 1.89G memory on ImageNet (Table 4), substantially less than training-based methods like RLCF (18.30h) and WATT (27.70h), while achieving the highest harmonic mean on both cross-domain and corruption benchmarks. The computational savings stem from prototype updates that operate in parallel and shortcut optimization that avoids backpropagation through the backbone.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Missing comparison with unimodal class-imbalanced TTA methods adapted to VLMs.** The paper cites DELTA, SAR, and LAME in the Related Work but does not compare against them, even in adapted form. The authors argue these are unimodal methods that face distinct challenges in the VLM setting (Section 2.1), and the paper's contribution is specifically about VLM LT-TTA. However, since these methods are designed for the same core problem (non-i.i.d./imbalanced test data), adapting them to use CLIP features and reporting results would substantially strengthen the claim that L-TTA's advantages come from its VLM-specific designs rather than from general class-imbalance handling. The paper's "first attempt" claim would also be better contextualized.

- **Pseudo-label feedback loop in BEM class prior estimation is unaddressed.** The class priors π in BEM (Eq. 9) are "continually updated based on the current predicted pseudo-labels" (line 151). Early predictions on tail classes are unreliable by definition, creating a potential feedback loop where poor initial predictions → incorrect prior estimates → BEM penalizes or favors wrong classes → subsequent predictions degrade further. The paper provides no analysis of this mechanism (e.g., tracking prior estimation accuracy over time, comparing corrupted vs. clean priors, or applying safeguards like confidence thresholds or momentum). While the penalty term (1−P̃)^β partially mitigates confident-class overfitting, the robustness of BEM to noisy prior estimates remains unverified. The ADTE paper (dHj8hC081K, avg 4.50) faced a closely related criticism for its pseudo-label-based bias estimation.

- **BEM's raw performance gain is modest despite being presented as a core contribution.** Adding BEM to SyP+RS improves macro-F1 from 65.17% to 65.83% (+0.66%) on ViT-B/16 (Table 6). While positive, this delta raises the question of whether BEM's theoretical sophistication is necessary, or whether simpler alternatives (e.g., logit adjustment or temperature scaling) could achieve similar gains. Propositions 1 and 2 do add intellectual value, but the empirical benefit should be commensurate with the claimed importance.

- **The K parameter for hyper-class vectors is underspecified.** The implementation details state "K = 0.3" (line 221), but Equation 6 defines K as the number of hyper-class vectors qⱼ, which must be an integer. The ablation study (Figure 4c) varies "b" from 0.1 to 1.0, suggesting K is actually a fraction of the number of classes (e.g., K = 0.3 × C), but this is never clarified. The naming inconsistency (K vs. b) and lack of specification harm reproducibility.

- **The subsampling procedure does not guarantee the stated imbalance ratio for all classes.** The paper states: "if the calculated cardinality is less than the class cardinality itself, we simply keep that class unchanged" (line 219). This means classes whose target size (from the exponential decay curve) exceeds their original size retain their original size, so the effective imbalance ratio may differ from the nominal value for some classes. While this is a minor design choice, it weakens the controlled nature of the experiment.

- **Standard deviations are not reported.** The paper states "5 runs for each experiment" (Tables 1-3 captions) but reports only means. Variance estimates would help assess whether the reported improvements are statistically significant, especially for smaller gaps (e.g., ImageNet-A at imb=50, where L-TTA's 60.07% accuracy is below DPE's 60.21%).

### Trivial
- The efficiency table (Table 4) uses non-standard notation ("1.54<×n" for WATT's memory) that should be clarified.
- The variable naming for the hyper-class vector count is inconsistent between the text (K) and the figure (b).

## Nice-to-Haves
- Tracking class prior estimation accuracy over the test stream and comparing BEM with/without deliberately misspecified priors would directly address the feedback-loop concern.
- Adapted versions of DELTA, SAR, and LAME for the VLM setting (using CLIP visual features) would make the empirical comparison more complete.
- Visualizing nearest-neighbor images to DPs and EPs for head vs. tail classes would provide intuitive insight into what these prototypes actually capture.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **θ entropy threshold collapse.** The reviewer speculates that θ "could collapse to near-zero values." The paper uses EMA to update θ with the minimum entropy in the batch (line 119), which is a standard smoothing mechanism that prevents abrupt collapse. No evidence of actual collapse is provided, and the concern is speculative.
- **CRA loss connection to MoE is "asserted but not justified."** The paper explicitly says "Gaining inspiration from" (line 129) — this is an inspiration, not an equivalence claim. The mechanism is independently described (Eq. 7) and ablated (Figure 4b shows η=1 gives +1.19%/+1.64% over η=0). The criticism conflates inspiration with claimed equivalence.
- **BEM notation ambiguity ("ɵ").** The notation in Eq. 9 is P̃ (tilde over P), which is the prediction distribution defined in Eq. 8. The notation is clear in context; the reviewer's confusion appears to be a parser artifact.
- **Formatting/style nitpicks** (e.g., table formatting, column alignment quirks) — these are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The review corpus surfaces one recurring pattern worth noting: several TTA-for-VLM papers propose methods grounded in entropy modification (ADTE with Tsallis entropy, this paper's BEM), yet all face a common unresolved challenge — the class priors used for debiasing are themselves estimated from potentially unreliable pseudo-labels in an online streaming setting, creating a feedback loop that none of the papers rigorously analyze.

## Suggestions

1. Clarify the K parameter: state explicitly whether K is an integer count or a fraction of C, and align the naming between the implementation details and the ablation figures.
2. Add an experiment tracking class prior estimation accuracy over the test stream (compared against oracle cardinalities) to demonstrate BEM's robustness to the pseudo-label feedback loop.
3. Report standard deviations for the main experimental results (Tables 1-3) to enable statistical significance assessment.
4. Consider adding adapted versions of DELTA/SAR/LAME (using CLIP visual features as input) to the comparison tables, or at minimum provide a more detailed explanation of why adaptation is non-trivial.

## Score and Decision

**Calibration anchors** (all from the human review corpus):

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| HeGMugkCOH.md (Continuous TTA for VLMs) | 3.00 | Weaker: simpler prototype method, criticized for lacking VLM-specific analysis; this paper has VLM-specific failure modes and broader experiments |
| dHj8hC081K.md (ADTE: Adaptive Debiasing Tsallis Entropy) | 4.50 | Similar domain (VLM TTA debiasing) but narrower scope (entropy modification only); accepted as poster; this paper has a broader problem formulation and more extensive evaluation |
| amBzV6V3tQ.md (LAMP: Long-tailed Multimodal Prompt Learning) | 2.67 | Long-tailed VLMs but prompt learning (not TTA); rejected for incremental novelty; this paper has a stronger experimental scope and clearer novelty |
| OdWkyqnkiS.md (CRETTA: Contrastive Residual Energy TTA) | 4.50 | Rejected; marginal empirical gains; this paper shows clearer and more consistent improvements |
| 7kLNGaAHaw.md (PEA: Backprop-free TTA) | 5.50 | Accepted poster; strong efficiency contribution with solid experiments; comparable in rigor but different contribution type |
| rClkte0ZTp.md (Efficient Test-Time Scaling for Small VLMs) | 5.00 | Accepted poster; solid but narrower scope; this paper has broader experimental coverage |

Positioning: This paper is stronger than the rejected/withdrawn anchors (scores 2.67–4.50) and comparable to accepted posters in the 5.0–5.5 range. Its novel problem formulation, VLM-specific failure mode analysis, theoretical propositions, and extensive experimental validation (15 datasets × 3 imbalance ratios × 4 additional backbones) make it a solid contribution. The weaknesses are genuine but addressable in revision and do not invalidate the core claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>