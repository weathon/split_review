Now let me run the calibration search in parallel to find appropriate anchor papers.**Round 1 Bracket:** Based on anchor comparison, the paper sits between DOTA (6.0, rejected) and READ (8.0, accepted). The paper is clearly stronger than DOTA in terms of novelty, scope, and methodological clarity. It is comparable to but somewhat weaker than READ (which had new benchmarks, cleaner theoretical contributions, and strong consensus acceptance). Initial bracket: **6.0–8.0**.

Let me now narrow within this bracket.Now I have sufficient calibration. Let me write the final review.

---

## Summary

L-TTA is the first test-time adaptation framework specifically designed for long-tailed distributions in Vision-Language Models (VLMs). It proposes three co-designed mechanisms: Synergistic Prototypes (Deterministic + Exclusionary), Rebalancing Shortcuts with a class re-allocation loss, and Balanced Entropy Minimization with theoretical justification. Evaluated across 15 datasets under three imbalance ratios with multiple backbones, L-TTA demonstrates consistent improvements over prior TTA methods in both accuracy and macro-F1.

---

## Strengths

- **Novel and well-motivated problem formulation.** The paper identifies and rigorously motivates a genuinely underexplored problem: long-tailed test-time adaptation of VLMs. It further characterizes two concrete, VLM-specific failure modes (text-induced tail erosion, modality-bias amplification), providing empirical evidence for each in Figure 1b that justifies the three-component design.

- **Exclusionary Prototypes provide confirmed tail-class enrichment.** The EP update in Eq. 5 is designed so that every image updates the EPs of *all* classes, not just the predicted class, giving tail classes access to signal from the entire datastream. Ablation in Table 6 confirms: replacing SyP (DP+EP)+RS with DP+RS alone degrades macro-F1 by 1.05% (ViT-B/16) and 0.80% (ResNet-50), demonstrating EPs' practical contribution even when ablated within the full system.

- **Balanced Entropy Minimization has both theoretical grounding and empirical support.** Propositions 1 and 2 formally show that standard EM creates an optimization gradient gap between head and tail classes, and that BEM reduces this gap. Empirically, Figure 4d confirms that the BEM penalty (β=1) outperforms both the class-prior-only variant (β=8) and the raw logit variant (β=0.1) by up to 0.64%/0.85% in accuracy/macro-F1.

- **Broad experimental coverage with strong results.** 15 datasets across four benchmarks (OOD, Cross-Domain, Corruption, multi-backbone), three imbalance ratios, ablation studies for every component, and robustness analysis against dynamic head/tail-class reordering (Table 7) — this is comprehensive by any standard. Key cross-domain result: +2.20% average macro-F1 over the next-best method (Table 2). Critically, L-TTA's macro-F1 degrades only 1.29% as imbalance ratio goes from 10 to 50 (OOD Average), while TDA drops 4.86% and DPE drops 4.72%.

- **Competitive efficiency.** Table 4 shows L-TTA runs in 1.45h on ImageNet with 1.89GB GPU memory, outperforming SCAP (2.96h) and vastly outperforming WATT (27.70h), while achieving the highest harmonic mean (67.20) on LT-CDB. This is possible because the visual backbone receives no gradient — only the prototypes and shortcuts are updated.

---

## Weaknesses

### Fatal
None.

### Major

- **Variance is not reported in main tables, undermining several claims.** The paper states "5 runs for each experiment" (Table 1 and 2 captions) but reports only mean values. Several head-to-head improvements in the tables are below 0.5–1% (e.g., L-TTA vs. DPE on ImageNet-A at imb=50: 60.07 vs. 60.21 in accuracy; L-TTA macro-F1 leads of 1–2% on OOD Average). Without uncertainty estimates, whether these margins are statistically significant cannot be assessed. This is especially important for accuracy columns where head-class dominance means macro-F1 improvements are more trustworthy than accuracy improvements. The paper should either add standard deviations to main tables or at minimum include them in appendix tables.

- **Non-i.i.d. TTA baselines (SAR, DELTA, LAME, DA-TTA) are discussed in related work but absent from quantitative comparison.** Section 2.1 correctly notes these methods address class imbalance under non-i.i.d. test data; Figure 1b shows SAR degrades on VLMs. However, no quantitative table compares L-TTA to these methods. Since DELTA and DA-TTA explicitly address class imbalance, their omission from Tables 1–3 leaves open the question of how much gain is attributable to VLM-specific design versus a strong general non-i.i.d. TTA baseline. The paper's argument for VLM-specific design would be stronger with at least one such comparison.

### Minor

- **Modality-bias amplification claim rests on a single method (SAR).** Figure 1(b.2) shows SAR degrades on a VLM backbone vs. a pure visual backbone. This is consistent with the claim, but the comparison is confounded: SAR uses group/layer normalization assumptions tuned for visual-only models, so the degradation could reflect an architecture mismatch rather than a general "modality-bias amplification" phenomenon. Showing that at least two or three unimodal non-i.i.d. methods degrade on VLMs would more robustly establish this as a systematic failure mode rather than an SAR-specific artifact.

- **EP mechanism explanation is largely post-hoc.** The update rule (Eq. 5) is clear, and the ablation confirms EPs help, but the paper's theoretical account of *why* they help is underdeveloped. Eq. 8 subtracts EP similarity from the logit of class c; for this to improve tail-class predictions, the cosine similarity between tail-class queries and the corresponding EP (built from diverse head-class images) must be lower than for non-tail-class queries. This sign relationship is assumed but never demonstrated empirically. A simple diagnostic (plot cosine similarity between EP_c and held-out tail-class queries vs. non-tail queries) would either confirm the mechanism or reveal it works for different reasons than claimed.

- **K notation inconsistency.** Section 3.2 introduces K as the number of hyper-class vectors ("there are K hyper-class vectors"), yet the implementation sets K=0.3 and Figure 4c ablates "b" over values 0.2–1.0, implying K is actually a fraction of the number of classes C. This inconsistency is never resolved in the main text and affects the interpretation of the ablation.

- **Imbalance ratios are mild compared to standard LT benchmarks.** The paper uses imb ∈ {10, 20, 50}, while canonical LT benchmarks like ImageNet-LT have imb ≈ 256. The paper explains this ("if the calculated cardinality is less than the class cardinality itself, we simply keep that class unchanged"), but does not discuss whether L-TTA's gains generalize to more extreme imbalances or characterize where performance begins to degrade.

### Trivial

- **Pseudo-label feedback loop in BEM prior estimation.** The text notes the class prior π "is continually updated based on the current predicted pseudo-labels." In the early datastream, the model's pseudo-label distribution is biased toward head classes, meaning π could initially reinforce rather than correct the head-class bias. The paper does not analyze whether this feedback loop is significant in practice. Given the consistent 5-run results, this appears empirically manageable, but a brief note or ablation (estimated prior vs. true prior) would close the gap.

---

## Nice-to-Haves

- Bringing a compact version of the per-class head/tail accuracy splits (currently deferred to Appendix C) into the main text would directly support the failure-mode-to-design mapping, showing that EPs specifically benefit tail classes and BEM specifically reduces head-class dominance.
- An experiment at extreme imbalance ratios (e.g., imb = 100 or 200) or on ImageNet-LT would demonstrate scope boundaries and inform practitioners about when L-TTA starts to degrade.
- A diagnostic experiment plotting cosine similarity distributions between EP prototypes and tail-class vs. non-tail-class queries would turn the post-hoc mechanistic claim into verifiable evidence.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Table 4 WATT memory entry '1.54<×n' is a weakness"** — This is a PDF/parser artifact (the hard rule explicitly excludes formatting artifacts from criticism). Removed.

- **Proposition 2 proof cannot be verified** — The proofs are deferred to Appendix A. Per hard rules, appendices exist in the original submission; criticizing the absence of in-paper proof is not valid. Removed.

- **Reproducibility concerns about hyperparameter disclosure** — The paper reports all key hyperparameters (η=1, λ₁=6, λ₂=6, K=0.3, β=1, optimizer=AdamW) in Section 4. No missing hyperparameters. Removed.

- **Missing related work on comparable non-i.i.d. VLM methods** — Per hard rules, we cannot confirm which specific papers exist without external sources. The specific papers mentioned in the review (SAR, DELTA, LAME, DA-TTA) are cited by the *authors themselves* in Section 2.1, so the criticism about missing quantitative comparison is retained; but the missing-related-work framing is removed.

- **"Variance omission is consequential for all results"** — The severity is Major for the main tables (as retained), but the Strength Finder's claim that "removing EPs costs ~3.22% macro-F1" conflates different ablation rows. Table 6 shows the EP contribution (SyP+RS minus DP+RS) is 1.05% for ViT-B/16, not 3.22%. The 3.22% figure comes from comparing EP-only vs. SyP+RS+BEM, which conflates multiple components. The strength finder's specific number is inaccurate; the retained weakness (missing variance) stands on its own. Removed the specific 3.22% claim.

---

## Novel Insights

The Exclusionary Prototype concept — updating each class's "anti-prototype" from all samples proportional to how unlikely those samples are to belong to that class — is an elegant inversion of standard prototype caching. While the ablation confirms EPs help, the deeper insight is that tail classes benefit not from seeing more tail-class samples (which they cannot, by definition) but from accumulating structured *negatives* from the abundant head-class samples. This enrichment mechanism is structurally different from prior TDA/negative-cache approaches that select samples based on entropy thresholds; the weight modulation in Eq. 5 creates a soft, continuous enrichment signal rather than a hard threshold. If the mechanism can be empirically validated (the diagnostic experiment suggested above), it could generalize well beyond VLM adaptation as a general strategy for long-tail prototype learning under streaming data constraints.

---

## Suggestions

1. Report standard deviations in at least one set of main result tables (or add them to the appendix with a pointer); for improvements under 1%, this is needed for credibility.
2. Include at least one quantitative comparison with a non-i.i.d. TTA baseline adapted to VLMs (e.g., SAR applied to CLIP, or DELTA); even a small table would help justify the VLM-specific design choices.
3. Resolve the K notation inconsistency — clarify in the main text that K is a fraction of C, and unify terminology between the text, implementation details, and Figure 4c (which uses "b").
4. Add a simple cosine-similarity diagnostic for EP prototypes vs. tail-class vs. head-class queries in the appendix to validate the claimed exclusionary mechanism.

---

## Score and Decision

**Calibration anchor summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| BAT-CLIP | z7PhIgVmZU.md | 5.50 | R1 | Clearly weaker — methodological violations, narrow experiments |
| DOTA | yD2JMeKumt.md | 6.00 | R1 | Weaker — methodology ambiguities, limited scope |
| READ | TPZRq4FALB.md | 8.00 | R1 | Stronger — unanimous consensus, new benchmarks, cleaner theory |
| Label Shift Correction | u1yvEwYfK9.md | 5.67 | R2 | Weaker — methodological gaps, limited evaluation |
| Multi-modal Concept Drift | b20VK2GnSs.md | 7.00 | R2 | Comparable — novel VLM problem, similar scope but weaker methodology |

**Round 1 bracket:** 6.0–8.0  
**Round 2 narrowing:** The closest anchor is b20VK2GnSs (7.0, Accepted). L-TTA is **stronger** than that anchor in terms of: clean experimental setup (no fairness issues), broader experiments (15 vs. a few datasets), more principled components with ablations, and consistent results across multiple backbones. L-TTA is **weaker** than READ (8.0) in that READ had unanimous perfect scores, created new benchmarks, and had a cleaner theoretical story.

The missing variance in main tables (Major weakness) and the missing comparison with non-i.i.d. TTA baselines (Major weakness) are real issues that prevent this paper from reaching the 8.0 tier. However, the paper's contributions — novel problem formulation, three well-motivated components with ablation support, 15-dataset evaluation, competitive efficiency, theoretical propositions — place it comfortably above the 6.0 rejected papers.

**Final score: 7.0** — a clear Accept with identified weaknesses addressable in revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>