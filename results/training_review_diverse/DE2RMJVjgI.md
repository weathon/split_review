## Summary

This paper proposes FS-PTAL, a point-supervised temporal action localization framework with four components (label extension, pseudo label mining, score contrast, and feature separation) designed to address action-background confusion. The method achieves 56.74% Avg(0.1:0.5) mAP on THUMOS14, outperforming prior point-supervised methods by ~4%. The ablation study validates each module's contribution, and the paper identifies a genuine flaw in prior OIC calculations.

## Strengths

- **Strong empirical results**: FS-PTAL achieves a clear SOTA on THUMOS14 under point-level supervision, outperforming the previous best method LACP by nearly 4% on Avg(0.1:0.5) and showing notable gains at high IoU thresholds (Table 1), which directly supports the claim of improved action-background separation.

- **Ablation study quantifies individual module contributions**: Table 2 shows that removing the pseudo label mining, score contrast, or feature separation modules drops performance by 7.4%, 4.2%, and 5.1% respectively, providing causal evidence that each component is essential. The label extension module contributes 2.1% on its own.

- **Novel identification of a flaw in prior outer-inner contrastive loss**: Section 3.4 and Figure 3 identify that prior OIC calculations (used in LACP, etc.) can incorrectly include short actions in the outer region of a long action, leading to erroneous contrast scores. The paper proposes a corrected formulation (Equation 8) that respects distances to neighboring labels.

- **Error analysis motivates the problem directly**: Figure 1 uses the Alwassel et al. diagnostic to show that existing methods (BackTAL, ASM) suffer heavily from Localization Err. and Background Err., empirically grounding the action-background confusion problem that the paper targets.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Formula (8) for the outer-inner contrast score is incompletely specified in the main text**: The formula as presented shows only two edge cases (n=1, n=N_sl^c) for the left/right boundary of the outer scope, but does not clearly specify the general case for interior segments. The cases environment appears to define `left` for only the first segment and `right` for only the last segment, leaving the computation for non-boundary segments ambiguous. While additional detail may exist in the appendix (which was stripped), a reader should be able to understand the core computation from the main text.

- **No controlled comparison isolating proposed modules against their direct prior equivalents**: The paper claims that the score contrast module improves over OIC (Shou et al., 2018; Lee & Byun, 2021), and that the feature separation module differs from prior work (Min & Corso, 2020; Lee & Byun, 2021). However, no experiment directly replaces, e.g., the OIC loss in LACP with the proposed score contrast to show a clean improvement, or swaps the feature separation module of a prior method with the proposed one. The ablation study shows each module's contribution to the full FS-PTAL framework, but does not isolate whether the advantage comes from the specific proposed modifications versus overall framework differences.

- **The relationship between the extended feature length T and the original length T_ori is not explained**: Section 3.1 states that T time steps are sampled via inverse CDF but does not clarify whether T equals T_ori, is larger, or is determined by some rule. This affects understanding of the label extension module's impact on feature dimensionality.

### Trivial
- Some hyperparameter values (τ₁, τ₂ mentioned in Section 3.1) are not stated in the main text.

## Nice-to-Haves

- Include a controlled experiment that replaces the OIC loss in LACP with the proposed score contrast module to directly measure the improvement attributable to the corrected OIC formulation.
- Present the error diagnosis (Alwassel et al.) for FS-PTAL alongside Figure 1 in the main text, rather than deferring to the appendix, to directly demonstrate that the proposed model reduces Localization Err. and Background Err.
- Clarify whether the extended feature length T equals T_ori or is increased.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Internal inconsistency between Table 1 and Table 2"** — The Harsh Critic claimed that computing Avg(0.1:0.7) from Table 1's numbers gives ~43.2%, contradicting Table 2's 50.7%. This is mathematically wrong: the two averages reported in Table 1 (Avg(0.1:0.5)=56.74% and Avg(0.3:0.7)=44.69%) are fully consistent with an Avg(0.1:0.7) of 50.7%. Simple algebra shows the implied middle IoU values (0.3–0.5 average ~50.75%) are perfectly reasonable. No inconsistency exists.

- **"Table 1 appears incomplete or misaligned with ablation baseline"** — The critic faults Table 1 for not including a "no-module" baseline. This is standard practice: SOTA comparison tables (Table 1) benchmark against other published methods, while ablation tables (Table 2) compare the paper's own variants. The baseline (none of A,B,C,D = 36.6%) is correctly placed in Table 2.

- **"Method description is too vague / defers to appendix"** — Several criticisms about missing details (τ₁, τ₂ values, γ_act, γ_bkg, architecture specifics, complete algorithms) were tied to their absence from the main text despite being in the appendix. Per the review guidelines, content deferred to the appendix should not be penalized as the appendix is part of the submission. The one substantive formula issue (Formula 8 being incomplete in the main text) is retained as a Minor weakness above.

- **"Error analysis in Figure 1 does not include FS-PTAL"** — The diagnostic for FS-PTAL is presented in the appendix (Sec. E). Per the review guidelines, the existence of appendix content should not be penalized. The issue of whether it belongs in the main text is moved to Nice-to-Haves.

- **"Writing quality (mthod, tlao bgeel, aupper)"** — These are parser artifacts from PDF extraction, not author errors.

- **"Results on ActivityNet v1.3, BEOID, GTEA not in main text"** — These results are in the appendix, which is standard practice.

- **Numerous generic/formulaic criticisms** about missing hyperparameters, training procedure details, ablation IoU breakdowns, and related works — these either reflect standard conference paper conventions (details in appendix) or are scope-creep demands.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily validate or challenge the paper's stated claims rather than adding a new analytic lens.

## Suggestions

1. Complete Formula (8) to show the general case for non-boundary segments, or provide a clear textual description of how the outer scope is computed for every segment.
2. Add one controlled experiment that isolates a proposed module against its direct prior counterpart (e.g., swapping OIC in LACP with the proposed score contrast) to strengthen the novelty case.
3. Include the error diagnosis for FS-PTAL in the main text, or at minimum state the key takeaway (e.g., "FS-PTAL reduces Localization Err. by X% and Background Err. by Y% relative to BackTAL/ASM").
4. Clarify whether the extended feature length T after the label extension module differs from T_ori, and if so, by how much.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>