Now I have the complete paper. Let me produce the updated meta-review.

---

## Summary

WithAnyone is a three-contribution paper introducing: (1) **MultiID-2M**, a ~500k group-photo dataset with per-identity reference images across ~25k identities; (2) **MultiID-Bench**, a benchmark with the novel copy-paste metric M_CP that separates Sim(GT) from Sim(Ref) to penalize trivial reference duplication; and (3) **WithAnyone**, a FLUX-based identity-customization model using GT-aligned ID loss, InfoNCE with 4096 extended negatives, and a paired tuning phase. The paper's core insight — that Sim(Ref) rewards copying while Sim(GT) provides a fairer target — is formally grounded and empirically validated.

---

## Rebuttal Assessment

**Weakness: Co-design of training objective and primary evaluation metric**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly points to two mitigations already in the paper. Section 4 explicitly states benchmark identities are "rare, long-tail identities with no overlap to training data" (confirmed in the paper). OmniContext cross-validation (Table 1b, confirmed in paper) shows WithAnyone achieves the best score among face-customization models (6.52 vs. PuLID 5.78). However, the author honestly concedes that OmniContext doesn't provide M_CP-specific independent validation (Section 6.1 explicitly notes "VLMs exhibit limited ability to distinguish individual identities"), and the paper defers the overlap verification to Appendix C (stripped). The structural concern is real: the held-out identities share the same *conceptual condition* as training (reference ≠ target), even if they are distinct identities. The mitigations are genuine but do not fully remove the concern.
- **Score impact:** Weakness downgraded (from Major to a mitigated Major — held-out identities and OmniContext cross-validation are real, both confirmed in paper)

**Weakness: Sim(GT) improvement is largely driven by CP reduction, not identity preservation**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly cites the ablation numbers: removing Phase 3 changes Sim(GT) from 0.405 (full) to 0.406 (w/o Phase 3), a negligible −0.001 change, while CP jumps from 0.161 to 0.239 (+0.078). These numbers are confirmed in Table 3. The author also correctly cites Section 6.3 ("reduces copy-paste artifacts without diminishing similarity to the ground truth"). However, the abstract's claim to "improve controllability over pose and expression" and the conclusion's phrasing "maintaining—and in many cases improving—identity similarity" still contains the framing ambiguity the original reviewer flagged. The author promises revision but the current paper retains this language. The weakness is structurally acknowledged but unfixed.
- **Score impact:** Weakness unchanged (paper not revised; abstract/conclusion framing issue persists)

**Weakness: Multi-ID results are less decisive than single-ID**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly contextualizes DreamID's CP = 0.116 vs. WithAnyone's 0.171 in Table 2b: DreamID achieves this at Sim(GT) = 0.311 vs. WithAnyone's 0.414. Position relative to the trade-off curve (Figure 5b) is the right comparison. The argument is methodologically sound. However, the author also acknowledges the "breaking the trade-off" claim is less conclusive for multi-ID and promises hedging in revision — which means the current paper's claim is still overstated.
- **Score impact:** Weakness downgraded (from Minor — the reviewer correctly identified the issue, and the author's trade-off-curve framing is a legitimate reframe, but the current paper is still unrevised)

**Weakness: User study sample size (n=10)**
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as a rebuttal — The author acknowledges the weakness directly ("a study of this scale is underpowered for strong statistical claims") and promises to add inter-rater agreement statistics to the main text. No statistical measure appears in the current paper. The acknowledgment is honest but does nothing to address the evidential gap.
- **Score impact:** Weakness unchanged (acknowledged but not fixed)

**Weakness: M_CP metric stability near degenerate cases**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly describes the existing mitigation: Sim(GT) > 0.40 filter for single-ID ranking (Table 1 footnote, confirmed) and Sim(GT) > 0.35 for multi-ID (Table 2 footnote, confirmed). The author also honestly acknowledges there is no sensitivity analysis and promises to add one. The current paper lacks this, and the concern that WithAnyone might systematically benefit from high-θ_tr cases (where paired training specifically helps) remains unaddressed empirically.
- **Score impact:** Weakness unchanged (promise to add sensitivity analysis not fulfilled in current paper)

**Weakness: BU metric not defined in main text**
- **Author's response:** Acknowledge
- **Assessment:** Convincing acknowledgment — Section 4 confirmed: "We additionally report identity blending, prompt fidelity (CLIP IT), and aesthetics; formal definitions and further details are provided in Appendix D." No inline definition in main text. The author promises to add one sentence.
- **Score impact:** Weakness unchanged (trivial, acknowledged, not fixed)

---

## Strengths

- **Formally grounded M_CP metric** (Eq. 2): Angular-normalized metric with clear mathematical motivation. Figure 5 demonstrates the diagnostic value: all 14+ baselines lie on a clear trade-off curve; WithAnyone uniquely deviates above it.
- **Large-scale paired dataset** (Section 3): ~500k identified group photos with ~25k identities, supporting training paradigms unavailable elsewhere; 1.5M additional unpaired images for reconstruction.
- **GT-aligned ID loss** (Eq. 4): Avoids noisy predicted landmarks by aligning with GT landmarks, enabling ID supervision across all noise levels (Figure 7 confirms lower and more informative gradients than prediction-aligned).
- **Contrastive loss with 4096 extended negatives** (Eq. 5, Table 3): Removing extended negatives drops Sim(GT) from 0.405 to 0.368 and eliminates most of the CP benefit.
- **Strong single-ID quantitative results** (Table 1a): Sim(GT) = 0.460 (second only to InstantID's 0.464), CP = 0.144 (second lowest among all methods with Sim(GT) > 0.40); clear breakout from the trade-off regression visible in Figure 5a.
- **Comprehensive ablation** (Table 3): All four components ablated with interpretable contributions.
- **Open-source release**: Dataset, benchmark, and model released for community use.

---

## Weaknesses

### Fatal
None.

### Major

- **Co-design of training objective and evaluation metric (mitigated but not removed)**: Phase 3 paired tuning trains on the exact condition (ref ≠ target, same identity) that M_CP is designed to measure. Mitigations exist: test identities are held out (Section 4, confirmed), and OmniContext provides independent cross-validation (Table 1b). However, OmniContext explicitly does not measure M_CP, and the paper itself acknowledges VLMs cannot distinguish identities well on that benchmark. The held-out identities share the conceptual structure of the training condition. Truly independent validation of the copy-paste claim remains absent.

### Minor

- **Abstract and conclusion framing**: The abstract claims WithAnyone "improves controllability over pose and expression" and the conclusion says "maintaining—and in many cases improving—identity similarity." Table 3 shows that Phase 3's contribution to Sim(GT) is −0.001 (0.406 → 0.405), meaning Phase 3 primarily reduces CP, not improves Sim(GT). The broader Sim(GT) gain comes from GT-aligned ID loss and extended negatives. The paper overattributes the Sim(GT) improvement to the paired tuning phase. Author acknowledges this but has not revised the text.

- **Multi-ID trade-off claim is overstated**: DreamID achieves lower CP (0.116 vs. 0.171) in the 3–4-person subset; the trade-off curve advantage is less clear than in single-ID. The trade-off-curve framing is a fairer comparison, but the paper does not caveat this distinction adequately in the current text.

- **User study underpowered**: n=10 participants across 230 image groups; no inter-rater agreement or significance measure reported in main text. Paper defers all statistical details to Appendix H (stripped). Author acknowledges this limitation.

- **M_CP threshold sensitivity absent**: The Sim(GT) > 0.40 filter for CP ranking is ad hoc; no sensitivity analysis at ±0.05 is provided. Author acknowledges and promises addition.

### Trivial

- **BU metric undefined in main text**: One-sentence informal definition should appear in Section 4. Author acknowledges.

---

## Nice-to-Haves

- Sensitivity analysis of the CP-ranking Sim(GT) threshold (even just 0.35 and 0.45 for the single-ID table) to establish robustness of the key ranking claim.
- Decomposition of Sim(GT) results by whether the GT prompt specifies pose/expression changes, to disentangle "better prompt-following" from "better identity preservation."
- Brief discussion of the general-VLM performance gap on OmniContext (GPT-4o: 8.12, OmniGen2: 8.34 vs. WithAnyone: 6.52) and what it implies for the trajectory of face-specific customization.

---

## Novel Insights

The paper's most durable contribution is the formal separation of Sim(Ref) from Sim(GT) as evaluation targets, operationalized through the angular-normalized M_CP metric. The rebuttal confirms (and the paper demonstrates) that paired tuning primarily reduces copy-paste (ΔCP = 0.078) while Sim(GT) is essentially unchanged (ΔSim(GT) = −0.001). This itself is a meaningful finding: suppressing copy-paste and improving identity fidelity are partially orthogonal objectives. The GT-aligned ID loss and extended-negative contrastive training are the components that actually lift Sim(GT), while Phase 3 cleans up the copy-paste residual. Future work designing identity-consistency metrics would benefit from this decomposition.

---

## Suggestions

1. Revise the abstract and conclusion to precisely attribute Phase 3's contribution (CP reduction, not Sim(GT) improvement) and overall system improvement (GT-aligned ID loss + extended negatives for identity fidelity; Phase 3 for CP reduction).
2. Add a one-sentence informal definition of BU in Section 4.
3. Report Kendall's W or inter-rater agreement in the main text alongside n=10.
4. Add a brief sensitivity check for the Sim(GT) threshold in Table 1 and 2 footnotes.
5. Hedge the multi-ID "breaking the trade-off" claim more carefully, noting it is most clearly demonstrated in the single-ID setting.

---

## Score and Decision

**Changes since original review:**
- The co-design weakness is **partially mitigated**: held-out identities and OmniContext cross-validation are confirmed in the paper, and these are real mitigations. Downgraded from a clean Major to a mitigated Major.
- The multi-ID weakness is **partially contextualized** by the trade-off-curve framing, which is methodologically fair.
- All other weaknesses are acknowledged but **not fixed in the current paper** (no revision submitted). The rebuttal's promises (sensitivity analysis, inter-rater agreement, abstract revision, BU definition) are not evidence — only the paper counts.
- No new problems were revealed by the rebuttal. The author's responses are honest and do not overclaim.

The rebuttal produces a net small upward adjustment: the co-design weakness is demonstrably mitigated (not removed) by evidence already in the paper, and the multi-ID critique is fairly reframed. The three-contribution structure remains strong and the core M_CP insight is durable. The score moves very slightly upward from 6.5, but the unfixed framing issues and underpowered user study prevent a full step to 7.0.

**Final score: 6.5** (unchanged — the partial mitigations of the major weakness and the multi-ID contextualization are offset by the unfixed abstract/conclusion framing and the absence of the sensitivity analysis, statistical measures, and BU definition in the actual paper.)

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>