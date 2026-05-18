Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes TA-STVG, a Transformer-based approach for spatio-temporal video grounding (STVG) that generates target-aware object queries from the video-text pair rather than using zero-initialized queries. Two modules are introduced: Text-Guided Temporal Sampling (TTS) selects target-relevant frames using holistic text information, and Attribute-Aware Spatial Activation (ASA) mines fine-grained visual attribute features from those frames to initialize queries. Experiments on HCSTVG-v1/v2 and VidSTG report state-of-the-art results across all metrics, and generality experiments show the modules improve other architectures (TubeDETR, STCAT).

## Strengths

- **Clear motivation validated by oracle experiment (Figure 2):** Replacing zero-initialized queries with ground-truth-generated queries yields +18.0% m_IoU and +13.5% m_vIoU, directly demonstrating that target-specific query information has large potential. This provides a principled rationale for the paper's direction.

- **State-of-the-art results across multiple benchmarks with consistent improvements:** TA-STVG achieves new SOTA on all four metrics on HCSTVG-v1 (Table 1), all four on HCSTVG-v2 (Table 2), and all eight on VidSTG (Table 3) for both declarative and interrogative sentences. Improvements over the baseline are consistent across settings (e.g., +3.1% m_tIoU on HCSTVG-v1, +2.1%/2.0% m_vIoU on VidSTG).

- **Systematic ablations isolate component contributions:** Table 4 shows TTS alone (+2.3% m_tIoU), ASA alone (+1.5%), and together (+3.1%). Tables 5 and 6 further dissect the contribution of appearance vs. motion branches and attributes. The ablations are thorough and allow the reader to understand what each part contributes.

- **Generality demonstrated by plugging into existing methods:** Table 10 shows TTS+ASA improves TubeDETR by +2.3% m_tIoU and STCAT by +1.7% m_tIoU, confirming the modules are not architecture-specific and can enhance other frameworks.

## Weaknesses

### Fatal
None.

### Major

- **The claim that ASA captures "fine-grained visual attribute information" is not convincingly supported.** The key ablation (Table 7) shows that replacing attribute-specific activation with instance-level activation (supervised by ground-truth box masks) yields nearly identical results: the reported gains are only ~0.4% m_vIoU and ~0.3% m_tIoU. These differences are within typical random variation for this task. The paper provides no direct evidence (e.g., disentangled attention maps per attribute, per-attribute classification accuracy, or analysis on subsets where attribute cues are critical) that the model actually uses fine-grained attributes as claimed. Since attribute-awareness is presented as a core novelty (contribution ♣), this weakens the paper's main narrative. The overall ASA module still adds ~1.5% m_tIoU over baseline, but the *attribute-specific* component adds little beyond what a simpler mask-based instance activation would achieve.

### Minor

- **The oracle experiment gap is large and unanalyzed.** The oracle achieves 68.9% m_IoU, while TA-STVG achieves 53.0% — closing only ~16% of the gap. The paper does not discuss this gap, analyze why TTS+ASA falls short, or identify the main bottlenecks (e.g., noisy frame selection, insufficient attribute modeling). While the oracle motivates the direction, its usefulness as evidence for the specific method is weakened without addressing why the gap remains large.

- **SOTA improvements over prior work are very small and lack statistical significance.** On HCSTVG-v1, the gain over CGSTVG is +0.5% m_tIoU (53.0% vs. 52.5%); on VidSTG Declarative, +0.7% m_tIoU (56.1% vs. 55.4%); on vIoU@0.5, +0.2%. No confidence intervals or multiple-run statistics are reported. While the consistency across many metrics is encouraging, the individual margins are thin enough that claims of "state-of-the-art" are meaningful only if the improvements are robust.

- **The attribute label construction is deferred entirely to the supplementary material without even a brief summary in the main text.** The paper mentions "weak attribute labels generated from the textual expression" and "Due to space limitation, we refer readers to our supplementary material" — but provides no concise description (e.g., "we extract noun-adjective pairs for appearance and verbs for motion using a dependency parser"). This leaves the reader unable to assess the reliability or coverage of the attribute supervision while reading the main paper.

- **No discussion of why instance-level activation performs nearly as well as attribute-specific activation.** The paper acknowledges the alternative (instance-level activation from ground-truth box masks) in a brief "Discussion" paragraph but offers no analysis of *why* the two are so close or what factors limit the benefit of attribute-specific supervision. This is a missed opportunity to refine the paper's claims.

### Trivial

- The paper does not report how many frames are typically selected by the hard threshold (θ=0.7) in TTS, or whether this varies significantly across videos or datasets. An ablation on θ is provided, but the output characteristic is not described.

## Nice-to-Haves

- An oracle experiment within the *full* TA-STVG pipeline (replacing TTS+ASA-generated queries with ground-truth-box queries in the same decoder setup) would show the upper bound of the proposed architecture and help readers assess how much room for improvement remains.
- Statistical significance tests (e.g., multiple random seeds) for the key SOTA comparisons would strengthen the empirical claims, especially given the small margins.
- Analysis of attention maps per attribute (e.g., comparing attribute-supervised vs. instance-level attention on frames where specific color/action cues are present) would directly test whether attribute supervision changes model behavior in the claimed way.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"The paper does not test with the full motion-aware version on methods that already have motion features (e.g., CGSTVG)."* — Scope creep. The paper already demonstrates generality on two methods (TubeDETR, STCAT) with reasonable consistency. Demanding integration with every existing method is impractical and goes beyond the paper's scope.
- *"The oracle experiment functions only as an existence proof that 'queries containing perfect location information help' — which is trivially true."* — Overly dismissive. The oracle experiment is standard practice for motivating a research direction and is used as such here. Its value is not diminished by the fact that TTS+ASA doesn't close the entire gap, though the gap itself is a legitimate concern (addressed in Minor weaknesses above).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Strengthen the attribute-awareness claim** with direct evidence: report per-attribute classification accuracy, compare attribute-supervised vs. instance-level attention maps on frames where specific attributes are critical, or evaluate on subsets where attribute cues are unambiguous vs. ambiguous. If the attribute-specific supervision adds little, consider reframing ASA's contribution around its overall spatial activation function rather than fine-grained attribute learning.

2. **Discuss the oracle gap** explicitly. Even a short analysis of why the gap remains large (e.g., "TTS selects noisy frames in challenging cases" or "the attribute classification signal is weak") would make the paper more intellectually honest and help guide future work.

3. **Provide a concise one-sentence summary** of the attribute label construction in the main text (e.g., "We parse the subject phrase to extract noun-adjective pairs for appearance attributes and action verbs for motion attributes, forming a multi-label classification target").

4. **Report the average number of frames selected by TTS** and its variance across datasets to help assess the robustness of the hard threshold design.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>