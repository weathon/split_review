Now I have a thorough understanding of both the paper and the reviewer claims. Let me compose the final consolidated review.

## Summary

This paper proposes SUMMER, a framework for multimodal emotion recognition in conversations (MERC). The method includes three main contributions: (1) Sparse Dynamic Mixture of Experts (SDMoE) for adaptive token-wise interaction, (2) Hierarchical Cross-Modal Fusion (HCMF) with a Global MoE for cross-modal context modeling, and (3) a "retrograde distillation" strategy where a unimodal (text-only) teacher model guides a multimodal student model via Interactive Knowledge Distillation (IKD). Experiments on IEMOCAP and MELD datasets show competitive results, outperforming prior baselines.

## Strengths

- **State-of-the-art empirical results.** SUMMER achieves clear improvements over prior methods on both IEMOCAP (e.g., +2.61% w-ACC) and MELD, with particularly strong gains on minority and semantically similar emotion categories (e.g., +15.5% on "Fear" over CORECT). These results are the paper's strongest evidence.

- **Systematic ablation study isolating each component.** Table 4 independently ablates SDMoE→MoE, HCMF→self-attention, IKD removal, and the smooth label term, with each causing a measurable performance drop. This provides empirical decomposition of the design decisions.

- **Novel combination of dynamic MoE routing with distillation.** The idea of using a unimodal (text-only) teacher with SDMoE to guide multimodal fusion is a conceptually interesting departure from standard multimodal-teacher distillation or self-distillation, and the strong teacher performance (outperforming prior multimodal baselines) supports the intuition that text carries discriminative signal worth distilling.

## Weaknesses

### Fatal

None.

### Major

1. **Missing critical baseline: standard (non-retrograde) distillation.** The paper claims "retrograde distillation" (unimodal teacher → multimodal student) as a core contribution, but never compares it against a standard knowledge distillation baseline (e.g., KL divergence from a *multimodal* teacher, or self-distillation as in SDT). The ablation in Table 4 removes IKD entirely, which only shows that *some* form of distillation helps — not that the *retrograde unimodal* nature is what drives the improvement. Without this comparison, the central distillation claim is unsubstantiated. The paper would need to show that a unimodal teacher outperforms a multimodal teacher under the same distillation framework.

2. **The "retrograde distillation" claim about reducing gradient conflicts is asserted without evidence.** The paper repeatedly states that IKD "mitigates gradient conflicts" and "addresses fusion disorientation," but it provides no measurement (e.g., cosine similarity between gradients, loss landscape analysis, or gradient norm comparisons) to support this mechanistic claim. This makes the conceptual selling point untestable.

3. **The case study baseline (Table 3) for justifying text as the teacher modality uses a different architecture than the actual teacher.** Table 3 compares modality combinations using the "original attention mechanism" (vanilla model), while the actual teacher uses SDMoE. The paper states: "Therefore, we designed and pre-trained a unimodal teacher model using the SDMoE module" (Section 3.5). The 4–7 point gap between the Table 3 text baseline and the teacher in Tables 1–2 is therefore partly attributable to SDMoE, not purely to modality choice. The paper should either run Table 3 with SDMoE on all modalities or explicitly acknowledge this confound.

### Minor

- **No confidence intervals, standard deviations, or statistical significance tests.** Results are reported as raw point differences without error bars. Given the small size of some emotion classes, variance may be high. While single-run reporting is common in this field, the lack of uncertainty quantification weakens the precision of the claimed improvements.

- **The standard MoE ablation baseline is underspecified.** Table 4 replaces SDMoE with "MoE" but does not specify the routing strategy (Top-K? Which K? How many experts?). Without this detail, the ablation cannot be assessed as a controlled experiment.

- **Equation (2) and its relationship to the Gumbel-Softmax (Eq. 3) is unclear.** Equation (2) defines a threshold-based hard selection, while Equation (3) applies Gumbel-Softmax over *all* experts. It is ambiguous whether these are alternative formulations or a pipeline (mask then reparameterize). The paper should clarify how the hard selection in (2) is reconciled with the differentiable relaxation in (3).

- **The HCMF mask threshold (0.5) is given without justification.** The condition |s_tr - s_st| > 0.5 for binary masking (Eq. 4–5) is never motivated or ablated. A sensitivity analysis over this threshold would strengthen confidence that the value is not cherry-picked.

- **Hyperparameter details are incomplete.** The number of experts (n), the value of κ weights in the KD loss, Gumbel temperature range, and the dynamic adjustment factor φ are not specified. Some of these may appear in the appendix (A.2).

### Trivial

- The term "retrograde distillation" is defined only by context rather than explicitly contrasted with related terms, though its meaning (unimodal teacher → multimodal student, opposite of standard large-teacher-to-small-student) is inferable from the text. A brief formal definition would improve clarity.

- The error analysis paragraph (Section 4.5) lists plausible reasons for underperformance but provides no quantitative diagnosis. It is too brief to be actionable.

## Nice-to-Haves

- An analysis of computational cost (parameter count, FLOPs, training time) relative to baselines would clarify the practical trade-offs.
- Reporting the standard train/validation/test split conventions used (standard splits for IEMOCAP/MELD are assumed but not explicitly stated).
- A comparison against a standard multimodal-teacher KD baseline to isolate the retrograde aspect specifically (this is already listed as a Major weakness, but a full experimental study would be a significant addition beyond the scope of a rebuttal).
- Pre-training details for the teacher model (epochs, data, optimizer) would aid reproducibility but may be in the appendix.

## Removed Points

- **Criticism that the teacher "is not simply a unimodal text encoder" because it uses SDMoE:** Removed because the paper explicitly states "we designed and pre-trained a unimodal teacher model using the SDMoE module" (Section 3.5). The teacher is unimodal in the sense that it only processes text input — "unimodal" refers to input modality, not architectural simplicity. The paper is transparent about this. The valid sub-concern (Table 3 architecture mismatch) is retained as a Major weakness.
- **Criticism that "retrograde distillation" is never defined or contrasted with related terms:** Removed as overly pedantic. The paper defines it in context (abstract: "utilizes a pre-trained unimodal teacher model to guide the learning of multimodal student model") and contrasts with standard KD implicitly in the Related Work section.
- **Criticism about missing appendix details / missing references:** Removed per meta-reviewer instructions — the appendix was stripped by the parser and exists in the original submission.
- **Criticism about stale baselines (SOTA claim unverifiable):** Removed because we do not know the submission date, and the paper cannot be faulted for failing to cite work that may not have existed at the time of submission. The comparison set (up to 2023) is reasonable for a paper in this timeline.
- **Stylistic/nitpicky criticisms about the equation notation being "technically incorrect":** The dynamic routing equation (Eq. 2) uses standard notation conventions seen in MoE literature; the underlying threshold-then-softmax operation is clear from the surrounding description ("Weights in W_g are selectively deactivated if they fall outside the range"). The ambiguity about Softmax scope is a presentation minor, not a technical error.
- **Criticism about binary mask being "abruptly discontinuous":** Hard attention masking is a standard design choice in sparse attention literature. This is a matter of design preference, not a technical flaw.

## Novel Insights

The most interesting observation across the reviews is the unresolved confound in the paper's central framing: the paper simultaneously claims that (a) text is the strongest single modality (justified by Table 3 using a vanilla architecture) and (b) the teacher's strength comes from SDMoE (Section 3.5). These two claims are never cleanly separated. A more rigorous design would either show that text+SDMoE > audio+SDMoE > video+SDMoE (apples-to-apples with the same architecture), or explicitly acknowledge that the teacher's advantage comes from SDMoE applied to text, not from text alone. This confound ripples into the distillation claim: if SDMoE is doing most of the work, the "retrograde unimodal" framing may be less important than the fact that the teacher has effectively learned high-quality text representations via dynamic routing. None of the submitted reviews identified this specific architectural confound, which is more precise than the generic "teacher inconsistency" critique.

## Suggestions

1. **Add a standard KD baseline.** Compare IKD (unimodal teacher → multimodal student) against IKD with a multimodal teacher → multimodal student, and against standard self-distillation. This single experiment would validate (or refute) the core distillation claim.
2. **Re-run Table 3 with SDMoE on all modalities** to provide an apples-to-apples justification for text modality selection. If this is computationally expensive, at minimum note the architecture confound explicitly.
3. **Provide uncertainty estimates** (3–5 run means and std. dev.) for the main results and key ablations.
4. **Clarify the relationship between Eqs. (2) and (3):** state explicitly whether these are alternatives or whether (3) is a differentiable relaxation of (2) used during training.
5. **Specify the "MoE" baseline** in Table 4: routing strategy, number of experts, and K value.
6. **Add a sensitivity analysis or justification for the 0.5 threshold** in the HCMF mask, or replace the hard binary mask with a soft weighting.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>