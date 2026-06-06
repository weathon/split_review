## Summary

BadDet+ introduces a log-barrier penalty-based backdoor attack framework for object detection that unifies Region Misclassification Attacks (RMA) and Object Disappearance Attacks (ODA) under a single training-time penalty. Alongside this attack, the paper provides a substantive methodological critique of prior evaluation protocols, introduces the True Detection Rate (TDR) metric to complement ASR for RMA, and validates its attack on synthetic (COCO, MTSD) and physical-world (PTSD) benchmarks across four architectures (FCOS, Faster RCNN, DINO, YOLOv5).

---

## Strengths

- **Rigorous evaluation critique and new metrics (Section 3, Tables 1–2):** The paper precisely identifies that ASR alone misses retained-label duplicates in RMA (Figure 1a) and that mAP is a confounded proxy for ODA success due to spurious phantom boxes (Figures 1b–c). The introduced TDR metric is immediately useful to the community regardless of BadDet+ itself: BadDet achieves TDR@50 of 75.94% (FCOS) and 44.74% (Faster RCNN) in Table 2, which shows that prior "successful" RMA results were largely spurious.

- **Strong, consistent ODA performance across three architectures (Table 1):** BadDet+ achieves ODA ASR@50 of 96.95% (FCOS), 98.46% (Faster RCNN), and 97.60% (DINO), far exceeding all baselines, while preserving clean mAP within ~1–2 points of baseline.

- **Compelling evidence that data poisoning alone is unreliable (Figure 3):** The poisoning-ratio sweep empirically shows that UBA and UBA Box drift toward the bottom-right (high poisoning → marginal ASR gain + mAP degradation), while BadDet+ clusters in the desirable top-left region. This motivates the training-loss manipulation threat model convincingly.

- **Physical-world validation (Tables 3–4, PTSD):** BadDet+ achieves ODA ASR@50 of up to 85.16% (DINO, fixed triggers) on PTSD, compared to 54.87% for Morph and ≤15% for UBA/UBA Box, providing more thorough real-world evidence than prior work.

- **Transparency about limitations:** The paper explicitly scopes its threat model (Section 4 Threat Model paragraph), acknowledges the YOLO failure in the results section ("λ=0 is optimal for this architecture"), and delineates defense scope in Sections 2.2 and 6.

---

## Weaknesses

### Fatal
None.

### Major

- **YOLO RMA underperformance directly undermines the unification claim.** Table 4 shows that on YOLOv5, BadDet outperforms BadDet+ on both ASR@50 (BadDet: 96.57 Fixed / 93.25 Random vs. BadDet+: 91.97 / 87.04) and TDR@50 (BadDet: 3.14 / 7.64 vs. BadDet+: 7.54 / 14.00). The paper notes "λ=0 is optimal for this architecture" and defers investigation to Appendix A.8. The abstract and introduction claim "consistent applicability across RMA and ODA" and "position- and scale-invariant behavior," yet the one architecture where BadDet+'s log-barrier penalty is optimal at λ=0 (i.e., effectively disabled) is among the most widely deployed in safety-critical settings. The paper's framing of this as a detector-specific characteristic "warranting further investigation" understates a real crack in the universality argument.

- **No ablation isolating the log-barrier contribution from the threat model advantage.** BadDet+ compares against data-poisoning-only baselines while operating under a strictly stronger threat model (training-loss manipulation). Section 4 and Section 6 are appropriately candid about this asymmetry, but there is no ablation replacing the log-barrier with a simpler training-loss penalty (e.g., a standard cross-entropy push toward the target class). Without this, the paper cannot establish whether the log-barrier form specifically is the key ingredient or whether any training-loss term would yield comparable gains. The paper's main methodological claim — that the log-barrier penalty's threshold behavior is what reliably suppresses original-class logits — is plausible but empirically unverified.

### Minor

- **Single-run main tables vs. 10-seed boxplots in defense evaluation (Figure 2 vs. Tables 1–4).** The defense evaluation explicitly uses 10 random seeds and displays the resulting spread in Figure 2, revealing non-trivial variance across runs. The main result tables report single-run values for ASR@50, TDR@50, and mAP with no variance estimates. Given the sensitivity visible in Figure 2, mean ± std or a range across 2–3 training seeds for key entries in Tables 1–4 would meaningfully change reader confidence in single-point comparisons.

- **Physical-world degradation gap not analyzed.** FCOS RMA ASR@50 drops from 96.41% (MTSD fixed) to 85.16% (PTSD fixed), a drop of ~11 points, while ODA FCOS drops from 93.77% (MTSD) to 59.59% (PTSD) — a 34-point gap. The paper accurately reports BadDet+ as showing "stronger transfer than prior work," but no analysis is offered for what drives the remaining brittleness (trigger visibility conditions, sign categories, resolution changes, etc.). A basic breakdown would strengthen the physical-world claim.

### Trivial
None.

---

## Nice-to-Haves

- **λ-sensitivity discussion in main text.** The 1000× difference in optimal λ between YOLO (λ=0.001) and all other architectures (λ=1), and the fact that Appendix A.5 studies this systematically, deserves a brief mention in the main results as a limitation on plug-and-play deployment.

- **Physical-world gap characterization.** Breaking down PTSD results by trigger visibility, sign category, or lighting condition would directly advance the paper's own claim about synthetic-to-physical generalization.

- **Principled diagnosis of the YOLO failure.** Understanding whether YOLOv5's anchor assignment or loss structure prevents the log-barrier from steering predictions effectively would deepen the contribution and could suggest a remedy. This is more valuable than adding a fifth architecture.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic: "Comparison asymmetry is not reflected in main tables."** The paper explicitly discusses the stronger threat model in Section 4's Threat Model paragraph ("our design assumes a stronger adversarial setting"), in the Section 5.3 poisoning-ratio analysis, and in Section 6. The abstract framing "outperforming existing baselines" is somewhat loose, but it is not misleading given the surrounding text. Removed — paper adequately addresses the asymmetry.

- **Harsh Critic: "YOLO failure traces to anchor assignment."** This is speculative and not supported by any analysis in the paper. Demoted — not a verifiable claim.

- **Harsh Critic: "Defense evaluation scope is a major weakness."** The paper proactively scopes this in Section 2.2 and Section 6. Explicitly out-of-scope limitations are not weaknesses; moved to Nice-to-Have/acknowledged limitation.

- **Harsh Critic: "FT-SAM on FCOS nearly neutralizes BadDet while BadDet+ is more resistant — claim is narrow."** Figure 2(d) does show this, and the paper reports it accurately. The scope limitation is real but already acknowledged. Not a flaw in the experimental design.

- **Strength Finder: "Theoretical analysis supporting penalty design."** The theoretical content is in Appendix A.7, which was stripped from the review copy. Cannot be verified. The claim is plausible but unverifiable; removed from confirmed strengths.

- **Strength Finder: "Robustness to fine-tuning defenses — BadDet+ maintains ASR@50 above 0.4 across architectures."** Partially supported by Figure 2, but for RMA, BadDet generally outperforms BadDet+ under FT-SAM (per the paper's own text in Section 5.3). The blanket framing overstates the result; removed as a standalone strength.

---

## Novel Insights

The paper's most actionable insight — which is genuinely novel for the object-detection backdoor community — is the observation that *object detection models can satisfy ASR without achieving misclassification* due to duplicate detections. The TDR metric cleanly formalizes this gap and retrospectively invalidates a substantial fraction of reported RMA results in prior work (e.g., BadDet TDR@50 of 75.94% on FCOS). The log-barrier formulation is a natural mechanism for closing this gap, and the unification of RMA and ODA by treating background as a special target class is clean and architecturally principled. The YOLO failure, if properly diagnosed, could itself become an insight about how assignment mechanisms in different detector families interact with training-time penalties — but this remains an open question after reading the paper.

---

## Suggestions

1. **Add an ablation baseline using a simple cross-entropy push toward the target class** (same threat model, different penalty) to isolate the log-barrier's specific contribution from the broader benefit of training-loss manipulation. Even a two-cell addition to Tables 1–2 would significantly sharpen the methodological claim.

2. **Report mean ± std across 2–3 training seeds for key rows in Tables 1–4**, at minimum for BadDet+ and BadDet to quantify how representative single-run numbers are.

3. **Consolidate the YOLO analysis from Appendix A.8 into the main results**, even as a single paragraph explaining the hypothesis. Deferring the one clear failure case entirely to the appendix weakens the paper's intellectual honesty about the method's scope.

4. **Report PTSD breakdown by at least one condition** (fixed high / fixed low / fixed both / random) rather than only averages — the MTSD setup already conditions on trigger position, so disaggregating PTSD is low-cost and directly informs the physical-world generalization claim.

---

## Evaluation on Key Axes

- **Originality:** Moderate. The TDR metric and the systematic evaluation critique are genuinely original contributions. The log-barrier penalty is a natural formulation, not a surprising one.
- **Importance:** High. Object detection backdoors are a direct safety concern for deployed systems; the evaluation methodology improvements benefit the entire subfield.
- **Claims well-supported:** Mostly. The core COCO and MTSD claims are strongly supported. The universality claim is weakened by YOLO. The specific superiority of the log-barrier form is not directly empirically isolated.
- **Soundness of experiments:** Good. Multi-architecture, multi-dataset, multi-placement, physical validation, and defense evaluation together constitute a thorough empirical study.
- **Clarity:** Good. The paper is clearly organized and the diagnostic motivation (Section 3) is well-presented.
- **Value to research community:** High. The TDR metric and evaluation protocol are immediately adoptable by other researchers, independent of BadDet+ itself.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>