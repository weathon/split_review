## Summary

This paper proposes Vision Filter (ViF), a generic hierarchical backbone for computer vision built on a new Fourier Neural Filter (FNF) operator. FNF extends the standard Fourier Neural Operator (FNO) by introducing an input-dependent (adaptive) integral kernel via selective activation (SA) and adaptive modulation (AM), aiming to overcome FNO's known bandwidth bottleneck and over-smoothing limitations. Extensive evaluations on ImageNet-1K, COCO, and ADE20K show that ViF achieves strong performance relative to CNN, Transformer, and Mamba-based backbones.

---

## Strengths

- **Favorable throughput-accuracy trade-off on ImageNet-1K:** Table 2 and Figure 1 show that ViF-T achieves 83.8% Top-1 at ~1600 Img/Sec, outperforming VMamba-T (82.6%) at a comparable throughput, and ViF-B achieves 85.2%, the best among all compared backbones. These are meaningful and concrete gains.

- **Ablation confirms importance of SA and AM:** Table 5 shows that removing selective activation causes the largest single accuracy drop (83.1% vs. 83.8%), and removing adaptive modulation also degrades accuracy (83.5% vs. 83.8%), providing direct evidence that both proposed components contribute to the performance.

- **Local convolutional components are justified empirically:** The ablation (Table 5) shows that removing LC-1 drops accuracy to 83.6% and removing LC-2 to 83.4%, confirming that both contribute and are not redundant.

- **Consistent state-of-the-art results across three tasks:** ViF outperforms all listed Transformer (Swin, NAT, DeiT) and most Mamba (VMamba, LocalVMamba) baselines on all three mainstream tasks in their respective scales, establishing it as a broadly competitive backbone.

---

## Weaknesses

### Fatal
None.

### Major

- **No empirical validation of the core frequency-domain mechanism.** The paper's entire motivation rests on the claim that FNF overcomes the bandwidth bottleneck and over-smoothing by "enhancing informative mid/high-frequency components while suppressing redundant low-frequency ones" (Remark 3). However, there is no frequency-response analysis, no visualization of learned filter spectra, and no comparison of effective bandwidth between FNF and baseline FNO or GFNet at matched capacity. The ablation (Table 5) confirms that SA matters for accuracy, but says nothing about *why* — it does not validate the frequency-domain narrative. This is a significant gap: the mechanism motivates the method, and without direct evidence the mechanism operates as described, the theoretical framing is unsupported by the experiments.

### Minor

- **Factual error in §5.3 regarding ViF-S vs. VMamba-S on single-scale segmentation.** The text states: "ViF-S shows superior performance with 50.5 single-scale mIoU…outperforming VMamba-S." However, Table 4 clearly shows VMamba-S achieves 50.6 SS mIoU vs. ViF-S's 50.5 — ViF-S does *not* outperform VMamba-S in single-scale mIoU. ViF-S does lead in multi-scale (51.3 vs. 51.2) and has lower parameter count (76M vs. 82M), so the efficiency argument has merit, but the specific SS claim is inverted and should be corrected.

- **Inconsistency between abstract framing and the paper's own limitations.** The abstract states ViF "consistently outperforms prominent variants of both Transformer- and Mamba-based backbones across diverse visual tasks," but the Limitations section (§6) explicitly acknowledges "marginal performance gains compared to other ViM models on downstream tasks." This is internally contradictory. On COCO (3× schedule), ViF-T vs. VMamba-T is 48.9 vs. 48.8 (+0.1); on ADE20K SS, ViF-B vs. VMamba-B is 51.3 vs. 51.0 (+0.3). These results support ViF as a competitive Fourier-based backbone, but not as a clear dominator over Mamba models on all tasks. The abstract should be scoped to match the actual findings.

- **Theoretical propositions are shallow.** Proposition 1 (bandwidth bottleneck) and Proposition 2 (over-smoothing) are essentially restatements of well-known spectral truncation and multiplicative contraction facts. More critically, neither Remark 3 nor Remark 5 provides a formal argument showing FNF actually resolves these issues — the case is made through natural-language assertions. The theoretical section sets up a problem it does not formally solve on its own terms.

### Trivial

- **Ablation text inconsistency:** The ablation text says "removing selective activation (SA) has the largest impact, with accuracy dropping to 83.3%," but Table 5 reports the w/o SA accuracy as 83.1%. This discrepancy (83.3% in prose vs. 83.1% in table) should be corrected.

- **Adaptive Modulation is borrowed from Liu & Tang (2025):** Definition 7 and the associated formulation ℳ(z) = z ⊙ [β · ‖z‖^α] is attributed to Liu & Tang (2025). While incorporating components from other works is entirely normal, contribution (1) in §1 presents FNF as wholly original ("we propose FNF, the first unified backbone…"). The novelty claim should be scoped to clarify which components are novel to this paper versus adapted from prior work.

---

## Nice-to-Haves

- A frequency-domain analysis comparing the effective bandwidth or spectral energy distribution of ViF vs. GFNet and FNO (e.g., visualizing frequency-bin activation magnitudes before/after SA) would directly substantiate the paper's central theoretical narrative and make the ablation results interpretable in terms of the proposed mechanism.
- An ablation sweeping the learnable α and β hyperparameters in adaptive modulation would clarify how sensitive the frequency-balancing effect is and whether it behaves as described in Remark 5.
- The full ViF block contains local convolutions (LC-1, LC-2) and an FFN alongside the O(N log N) global convolution. Reporting the actual end-to-end complexity of a full ViF block (vs. claiming O(N log N)) would make the complexity analysis more precise and honest.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "missing AFNO baseline."** AFNO (Guibas et al., 2022) is referenced in Related Work and the paper's block-diagonal structure borrows from it. The lack of a direct AFNO row in the comparison tables is a genuine gap, but falls under missing related work baseline which the hard rules preclude per the instructions around baseline fairness.

- **Harsh Critic: Throughput values are approximate read-offs without confidence intervals.** This is a minor presentation concern that is standard practice in backbone papers and does not affect the core comparison.

- **Harsh Critic: High-resolution throughput not reported.** Requesting high-resolution scaling results is outside the paper's stated scope and is a nice-to-have, not a weakness.

- **Harsh Critic: Relation between Eq.(4) and Eq.(5-6) is asserted rather than derived.** While there is a derivation gap, this level of formality is consistent with the paper's presentation style and is not unusual in empirical architecture papers.

- **Strength Finder: "The paper addressed an important problem" / general sycophantic framing.** These generic framing claims have been absorbed into the specific evidence-backed strengths listed above.

---

## Novel Insights

The core insight — using an input-dependent, gated global convolution in the frequency domain (G(v) ⊙ P(v)) to simultaneously address both the bandwidth bottleneck and over-smoothing of FNO in a unified operator — is a concrete and actionable design principle. The practical result that selective activation contributes more to accuracy than either local convolution branch in isolation (Table 5) is a non-obvious empirical finding about the relative importance of time-frequency gating vs. local priors. If paired with frequency-response analysis, this could be a genuine advance in understanding how to design Fourier-based vision operators. As the paper stands, the insight is present but not fully substantiated.

---

## Suggestions

1. Add a frequency-domain diagnostic figure (e.g., per-frequency-bin energy plots of intermediate feature maps for FNO, GFNet, and ViF) to directly validate that SA widens effective bandwidth; this alone would substantially strengthen the paper's core claim.
2. Correct the text in §5.3 to accurately reflect the SS mIoU comparison (ViF-S 50.5 < VMamba-S 50.6) and replace the superiority claim with an efficiency-adjusted comparison.
3. Revise the abstract to accurately reflect that downstream margins over ViM models are modest, consistent with §6's own honest assessment.
4. Clarify in §1 which components of FNF are original to this paper and which are adapted from Liu & Tang (2025) and Guibas et al. (2022).
5. Correct the ablation text (83.3% → 83.1% for w/o SA) to match Table 5.

---

## Score and Decision

**Axis evaluation:**
- *Originality:* Moderate — FNF as a unified time-frequency gated backbone is a concrete novel combination, though its components draw on prior work (AFNO block structure, borrowed adaptive modulation).
- *Importance of research question:* Moderate — designing efficient, spatial-structure-preserving vision backbones is genuinely important; the Fourier approach is a credible alternative to Mamba.
- *Claims well-supported:* Partially — ImageNet results are solid; the core frequency-domain mechanism claim is not directly validated; one factual error in the text.
- *Soundness of experiments:* Good — three-task evaluation follows established protocols, competitive baselines, ablation is meaningful though limited to classification.
- *Clarity of writing:* Good overall, with minor inconsistencies between text and tables.
- *Value to research community:* Moderate-high — introduces a competitive Fourier-based backbone that researchers can use and build on.

The paper makes a real contribution as a competitive Fourier-based visual backbone with solid ImageNet numbers. The main gap — the absence of any empirical validation that the proposed mechanism actually operates on frequency content as claimed — prevents the paper from fully delivering on its theoretical framing. The factual error and abstract/limitations mismatch are correctable. Overall, this is a publishable, borderline-accept-level contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>