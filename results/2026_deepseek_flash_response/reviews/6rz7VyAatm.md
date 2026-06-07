Now I have enough anchors. Let me synthesize the final review.

My round-1 bracket: **4.5–6.0** (above the 3.0–4.33 rejected anchors, comparable to the 4.75–6.33 accepted/mixed anchors).

After reading the 5.50 (BaDLoss), 5.75 (Efficient Backdoor Attacks), and 4.33–4.75 (rejected) anchors in full, my assessment is that the current paper sits between the 5.50 and 5.75 anchors — it has stronger novelty than the 5.75 paper (which had a reviewer claiming the idea was already exploited) but has framing issues that the 5.50 paper doesn't. I'm placing it at **5.5**.

Here is the final review:

## Summary

This paper identifies evaluation blind spots in object-detection backdoor research — chiefly that ASR overstates RMA success by ignoring duplicate detections, and mAP is a poor proxy for ODA success — and proposes BadDet+, a penalty-based attack framework that unifies region misclassification (RMA) and object disappearance (ODA) under a single log-barrier mechanism. The framework augments the detector's loss with a penalty that suppresses original-class predictions on trigger-bearing objects. Across COCO, MTSD, and PTSD with four architectures (FCOS, Faster RCNN, DINO, YOLOv5), BadDet+ achieves strong attack success rates while substantially reducing True Detection Rate (TDR) in RMA settings.

## Strengths

- **TDR metric exposes a failure mode prior work completely misses.** Section 3 and Table 2 provide concrete evidence: BadDet on FCOS achieves ASR@50 of 99.45% (appearing near-perfect) but TDR@50 of 75.94%, meaning ~76% of trigger-bearing objects still receive original-class detections alongside the target. BadDet+ reduces TDR@50 to 2.78% on the same setting. This is a genuine diagnostic contribution — the metric is well-motivated, easy to adopt, and the evidence base (Table 2) is clean.

- **Clean unified formulation subsuming both RMA and ODA.** Equations (1) and (2) formalize ODA as a special case of RMA where the target is background, enabling one loss function to handle both attack types. This is a conceptual advance over prior work (BadDet, UBA, Align, Morph) that uses separate, task-specific procedures. Tables 1 and 3 validate empirically across both settings.

- **Synthetic-to-physical world transfer outperforming prior methods on PTSD.** Table 3 (PTSD rows) shows BadDet+ achieves substantially higher ASR@50 than Morph, UBA, and UBA Box — e.g., 85.16 on DINO vs. 54.87 for Morph. This directly addresses the generalization gap from synthetic to physical triggers identified by Doan et al. (2024).

- **Comprehensive ablation establishing that data poisoning alone is unreliable.** Figure 3 shows that simply increasing the poisoning ratio for UBA and BadDet either fails to improve ASR or does so only by collapsing clean mAP. BadDet+ achieves high ASR with 50% poisoning and minimal mAP degradation. This provides clear motivation for the stronger threat model.

- **Systematic evaluation of trigger placement robustness.** Tables 3 and 4 compare Fixed vs. Random trigger placement across four architectures. Prior methods degrade sharply under random placement (e.g., UBA ODA drops from 61.91 to 32.79 on FCOS), while BadDet+ maintains high ASR (83.68–92.31 across architectures on MTSD). This dimension is absent from prior work.

## Weaknesses

### Major

1. **Threat-model asymmetry inflates comparative claims.** BadDet+ assumes the attacker can modify the training loss (a training-time penalty added to the detector's loss). Baselines (BadDet, UBA, Align, Morph) assume standard data poisoning only — the attacker modifies training data but cannot touch the optimizer or loss. Tables 1–4 present these as direct comparisons, and the abstract/introduction use phrases like "outperforming existing RMA and ODA baselines." This is not a level playing field; adding a training-time loss term to baselines would trivially give them more leverage. The paper acknowledges the stronger threat model in Section 4 ("Compared to related existing work, our design assumes a stronger adversarial setting") but does not calibrate its comparative claims accordingly. The question of whether BadDet+'s *specific penalty formulation* adds value over simply giving baselines access to loss manipulation remains unanswered.

2. **BadDet+ is *less* robust to fine-tuning defenses than BadDet for RMA, contradicting the "robust" framing.** The defense evaluation (Section 5.3, Figure 2) shows that for RMA, BadDet generally retains higher ASR after FT and FT-SAM than BadDet+. The text acknowledges this directly: "For RMA, BadDet generally outperforms BadDet+ under both FT and FT-SAM." The paper is titled "Robust Backdoor Attacks for Object Detection" and emphasizes robustness in the abstract, yet on the most important robustness test (fine-tuning defenses), BadDet+ is *less* robust than the data-poisoning-only baseline for half the threat models it claims to unify. While the paper is honest about this in Section 6, the framing throughout the title, abstract, and introduction is misleading.

### Minor

3. **No error bars or variance reporting for main results (Tables 1–4).** The defense evaluation uses 10 runs (Figure 2), but the main tables appear to report single runs. Backdoor ASR can be sensitive to initialization and data splits; variance reporting is standard practice and essential for reliability.

4. **YOLO RMA failure case acknowledged but unexplained.** For YOLO RMA (Table 4), BadDet underperforms BadDet+ on neither ASR@50 (96.57 vs. 91.97) nor TDR@50 (3.14 vs. 7.54), and λ=0 is optimal. The paper notes this but provides no diagnostic analysis of *why* the log-barrier penalty fails for YOLO's loss structure or architecture. This is the most informative failure case for understanding the method's scope.

5. **PTSD transfer gap underdiscussed as a limitation.** ASR drops substantially from MTSD to PTSD for all methods. For FCOS ODA, BadDet+ goes from 93.77% ASR@50 on MTSD to 59.59% on PTSD (Fixed) — a ~34-point drop. The abstract claims "stronger synthetic-to-physical transfer than prior work" (true), but the absolute transfer rates remain low enough to question practical threat in unrestricted physical deployments. The paper mentions this in passing but does not contextualize it as a limitation.

### Trivial

None.

## Nice-to-Haves

- Allow baselines access to loss manipulation to disentangle whether BadDet+'s specific penalty formulation adds value over generic loss manipulation.
- Discuss the YOLO failure diagnostically (e.g., vary λ systematically, examine conflict with YOLO's loss structure).
- Add error bars to main tables.
- Report duplicate/phantom detection rates for ODA baselines that motivated the TDR critique.

## Removed Points

These points were raised by reviewers but are excluded from the main weaknesses for the reasons noted:

- *"Theoretical framing disconnected from empirical evidence"* — The theoretical discussion is deferred to Appendix A.7, which was stripped by the parser. The claim that the analysis is "purely intuitive" cannot be verified against the full paper. The main text theory is indeed brief, but whether there is formal analysis in the appendix is unknowable from the available text.
- *"PTSD table formatting is garbled/unreadable"* — This is a parser artifact, not a paper formatting issue.
- *"Missing evaluation of object-generation attacks (OGA)"* — The paper explicitly scopes this out (Section 6), which is reasonable.
- *"UBA achieves competitive ASR on DINO ODA"* — This is an observation about the data, not a weakness. The paper presents the full table faithfully.
- *"Standard trigger only"* — Alternative triggers are evaluated in the appendix. Having the primary evaluation on one trigger is standard practice.
- *Generic criticisms about the importance/scope* — Removed per filtering guidelines.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the comparative claims.** Either level the playing field by giving baselines access to loss manipulation, or clearly separate the paper's contributions into (a) diagnosing evaluation blind spots (uncontroversial, no threat-model dependency) and (b) demonstrating that loss manipulation enables stronger attacks (which should be presented as a demonstration, not a head-to-head comparison).

2. **Disambiguate "robustness."** Separate robustness to trigger variation (which BadDet+ achieves) from robustness to fine-tuning defenses (which it does not achieve for RMA). The title and abstract should be adjusted to match the evidence.

3. **Investigate the YOLO failure diagnostically.** A systematic ablation (varying λ across orders of magnitude, examining whether YOLO's architecture inherently suppresses original-class logits differently) would clarify the method's scope and may reveal a deeper insight about the interaction between loss design and detector architecture.

## Score and Decision

**Calibration anchors consulted (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 7vKWg2Vdrs.md (LeBD YOLO defense) | 3.25 | R1 | Weaker — less rigorous evaluation, narrower scope |
| 66e22qCU5i.md (Certified Copy) | 3.00 | R1 | Weaker — less convincing results |
| S5JCqTJyKj.md (Deferred Backdoor) | 3.00 | R1 | Weaker — different problem framing |
| zQXX3ZV2HE.md (Adversarial Instance) | 3.00 | R1 | Weaker — different problem |
| ZyPRwskBli.md (Model Editing Backdoor) | 4.75 | R1 | Comparable weaknesses (unfair baseline comparison) but weaker novelty |
| H6XiAoyugv.md (VSSC Trigger) | 4.33 | R1 | Weaker — marginal gains, limited novelty |
| vRyp2dhEQp.md (Efficient Backdoor) | 5.75 | R1 | Comparable — novel method but novelty concern (reviewer claimed idea exploited); current paper has stronger novelty |
| tZozeR3VV7.md (VLOOD) | 6.33 | R1 | Slightly stronger — cleaner evaluation, fewer framing issues |
| rK0YJwL69S.md (BaDLoss) | 5.50 | R2 | Comparable — similar rigor, different weaknesses |
| 1OfAO2mes1.md (Backdoor Secrets) | 6.00 | R2 | Slightly stronger — cleaner presentation, all 6s |
| lOsF9k1sxW.md (FIM Purification) | 5.75 | R2 | Comparable quality |
| s56xikpD92.md (BaDExpert) | 6.25 | R2 | Slightly stronger |
| 9rtlfjWMXI.md (PADetBench) | 4.75 | R2 | Weaker — benchmark without novel method |

**Round 1 bracket:** 4.0–6.0. Paper is clearly above the 3.0–4.33 weak anchors (stronger contributions, more rigorous evaluation) and below the 7.5+ strong anchors.

**Round 2 narrowing:** Paper compared to the 5.50 (BaDLoss) and 5.75 (Efficient Backdoor) anchors in the 5–6 band. The current paper has stronger novelty than the 5.75 anchor (which had a major novelty concern) but weaker framing/claim calibration. It is comparable to the 5.50 anchor but with different tradeoffs. Placing it at 5.5.

**Final score: 5.5.** The paper makes real contributions (TDR metric, unified formulation, thorough evaluation) but overstates its claims in two important ways: comparisons with baselines are asymmetric, and the "robust" framing is contradicted by the RMA defense results. These are fixable through reframing and do not invalidate the core contributions.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>