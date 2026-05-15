Now I have a thorough understanding of the paper. Let me synthesize the final review after verifying all key claims against the source text.

---

## Summary

This paper proposes FIRM (Focused In-distribution Representation Modeling), a multi-positive contrastive loss for anomaly detection. The key idea is to treat all in-distribution (ID) samples as mutual positives to encourage compact ID clustering, while keeping synthetic outliers as single-positive to preserve their diversity. The method is evaluated on CIFAR-10/100, Fashion-MNIST, and Cats-vs-Dogs for anomaly detection, and on CIFAR-10 as ID for unlabeled multiclass OOD detection.

## Strengths

- **Novel multi-positive objective with a clear anomaly-detection-specific motivation.** FIRM explicitly diagnoses the conflict between standard contrastive losses (which induce intraclass variance) and the anomaly detection requirement of compact ID representations, then designs the objective to resolve it: multi-positive for ID samples, single-positive for synthetic outliers. The loss landscape visualization (Figure 1) provides helpful intuition for how this differs from NT-Xent and SupCon. This conceptual framing is the paper's main contribution.

- **Strong results against DROC and CSI in standard anomaly detection benchmarks.** In Table 1, FIRM w/ OE achieves the highest reported AUROC on CIFAR-10 (mean 96.7% with ensemble), CIFAR-100 superclass (90.7%), Fashion-MNIST (97.9%), and Cats-vs-Dogs (92.8%), outperforming DROC and CSI. FIRM *without* OE also shows improvements over these baselines across multiple scoring functions. These gains are substantive.

- **Effective transfer to unlabeled multiclass OOD detection.** Table 3 shows FIRM (without OE) outperforms CSI on LSUN (94.8% vs. 93.2%), LSUN\* (97.5% vs. 96.9%), and ImageNet\* (98.2% vs. 98.0%) in the setting where all 10 CIFAR-10 classes are treated as unlabeled ID. This demonstrates the method's versatility beyond the homogeneous-ID setting it was designed for.

- **Ablation study directly comparing NT-Xent, SupCon, and FIRM under identical conditions (Table 4).** This is a clean, well-controlled experiment that honestly reveals where FIRM helps and where it doesn't — even though the results complicate the paper's narrative, the authors deserve credit for including it.

## Weaknesses

### Fatal
None.

### Major

- **The paper's headline claims are not supported by its own best-controlled comparison.** Table 4 directly compares NT-Xent, binary SupCon, SupCon\* (per-sample labels in a supervised contrastive framework), and FIRM. On three out of four datasets (CIFAR-10, CIFAR-100, Fashion-MNIST), **SupCon\* achieves equal or higher AUROC than FIRM** (e.g., 0.831 vs. 0.827 on CIFAR-10, 0.779 vs. 0.778 on CIFAR-100, 0.922 vs. 0.913 on Fashion-MNIST). Only on Cats-vs-Dogs does FIRM clearly lead (0.888 vs. 0.868). The abstract claims FIRM "surpasses other contrastive methods in standard benchmarks" and "significantly enhanc[es] anomaly detection compared to both traditional and supervised contrastive learning objectives" — yet SupCon\* is a supervised contrastive objective, and FIRM does *not* surpass it on 3 of 4 datasets. The paper's discussion around Table 4 (line 133) only claims FIRM outperforms "NT-Xent and SupCon" (binary), which is technically correct but the broader framing in the abstract and conclusion is overbroad and misleading. This is the most significant weakness: the core comparative advantage the paper claims is not empirically established.

- **The unlabeled multiclass OOD detection setup (Section 3.1) contradicts the paper's stated design principle without analysis.** Section 1 motivates FIRM with the claim that "minimizing intraclass variance and tightly clustering ID representations is essential… particularly when the ID is *naturally homogeneous*." Yet in the multiclass OOD setting, the ID is *all 10 classes of CIFAR-10* — highly heterogeneous. Forcing all 10 classes into a single cluster directly conflicts with the paper's design rationale. The paper presents this as an "extension" without analyzing the trade-off, why it works, or whether the benefit comes from FIRM's objective vs. the strong OE and ensemble scoring. This weakens the coherence of the contribution narrative.

### Minor

- **The OE confound is not fully disentangled in the main benchmark comparisons.** Table 1 shows "FIRM w/ OE" achieving the best results, but it is not clear whether the baselines (DROC, CSI) are evaluated with or without OE in the cited numbers. The paper acknowledges FIRM benefits "substantially from using OE" but does not provide a controlled comparison (e.g., DROC+OE, CSI+OE trained under the same conditions). While the ablation in Table 4 partially addresses this by comparing objectives under identical conditions (same outlier source for all), the main results table lacks this control, making it difficult to attribute the gains to FIRM's objective versus the presence of OE data.

- **The claim dismissing UniCon-HA (line 142) as relying on "complex data augmentation strategies" is not substantiated.** FIRM itself uses rotations, crops, CutPaste/NSA, and OE — which are similarly non-trivial. The paper does not quantify the "complexity" advantage or compare against UniCon-HA experimentally, weakening this dismissal.

### Trivial
None (the paper is reasonably well-written at the sentence level).

## Nice-to-Have

- A controlled version of Table 1 where *all* methods (DROC, CSI, NT-Xent, SupCon, SupCon\*) are trained with the same OE data as "FIRM w/ OE" to separate the effect of the objective from the effect of additional data.
- t-SNE/UMAP visualization comparing FIRM vs. SupCon\* representations (Figure 2 only compares FIRM vs. NT-Xent and binary SupCon — the more informative comparison is missing).
- Analysis of when and why SupCon\* matches or exceeds FIRM: does it depend on ID homogeneity? On dataset size? This would help practitioners understand when FIRM is actually preferable.

## Removed Points

These are flagged as unreliable; treat with caution.

1. **"No statistical significance / variance reported"** — Line 103 of the paper explicitly states: "We report the mean and standard deviation of evaluation metrics over five runs." The tables are embedded images that likely contain the std values; the parser simply did not extract them. This is a parsing artifact, not an author omission.

2. **"Outdated baselines / missing post-2021 methods"** — The paper compares against DROC (2021) and CSI (2020), which are the standard and most directly relevant baselines for contrastive anomaly detection. The paper cites UniCon-HA (2023) in related work. Missing comparisons to every recent method is normal for a conference paper; this is scope creep.

3. **"Missing Table 5, Table 6"** — These are appendix tables stripped by the PDF parser. Per instructions, parser artifacts are not author errors.

4. **"Underspecified P(i) definition"** — Equations (2)-(3) and the accompanying text on lines 49, 55-59 clearly define the positive set. The "otherwise" case is explicitly specified: for outlier anchors, P(j) = {j^+} only.

5. **"Formatting / style nitpicks"** — All removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews surface an important empirical tension (SupCon\* vs. FIRM) that the paper itself does not adequately address, but this is a limitation of the paper's framing rather than a novel observation from the reviews.

## Suggestions

1. **Reframe the claims to match the evidence.** The abstract and conclusion should acknowledge that SupCon\* (per-sample-label supervised contrastive) achieves comparable AUROC to FIRM on most benchmarks, and characterize FIRM's advantage as being specific to the most homogeneous ID settings (Cats-vs-Dogs) or when combined with ensemble scoring. This would make the paper more honest and the contribution more defensible.

2. **Add a controlled OE experiment.** Train NT-Xent, SupCon, and SupCon\* with the same OE data used for "FIRM w/ OE" and report results in a side-by-side comparison. This is needed to attribute gains to the objective rather than to the presence of additional data.

3. **Analyze the SupCon\* comparison.** The paper should investigate why SupCon\* — which in the multiclass setting with per-sample labels is essentially equivalent to instance discrimination — matches FIRM. Does FIRM's advantage correlate with how homogeneous the ID is? This analysis would significantly strengthen the paper's contribution by revealing *when* FIRM is genuinely better.

4. **Address the multiclass OOD tension explicitly.** A brief paragraph explaining why FIRM works for heterogeneous ID (e.g., does the multi-positive strategy still help because all ID classes are "normal" relative to true OOD data?) would resolve the conceptual contradiction.

## Score and Decision

The paper introduces a well-motivated loss function and demonstrates competitive results against established baselines. However, its own ablation reveals that a simpler baseline (SupCon\*) matches or outperforms FIRM on most datasets, yet the paper's abstract and conclusion claim unqualified superiority over "supervised contrastive learning objectives." This framing gap is the central weakness: the claimed advance is not empirically supported relative to the strongest baseline. The paper is not fatally flawed — the method is novel and the experiments are otherwise solid — but the claims need significant revision. With honest reframing and additional controlled experiments, this could be a solid paper.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>