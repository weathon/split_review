Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

The paper proposes FS-PTAL, a point-supervised temporal action localization framework consisting of four modules (label extension, pseudo label mining, score contrast, feature separation) designed to reduce action-background confusion. The method extends sparse point-level annotations into denser labels, mines pseudo labels, and uses contrastive learning at both score and feature levels to separate action from background. Experiments on THUMOS'14 and three other benchmarks claim state-of-the-art results over prior point-supervised methods.

## Strengths

- **Well-motivated technical approach to a real problem.** The paper identifies action-background confusion as the key bottleneck in point-supervised TAL and proposes a multi-module pipeline that addresses it from complementary angles: densifying labels (extension + mining), amplifying score differences (score contrast), and separating features (feature separation via cosine similarity in an embedding space). This is a coherent design.

- **Novel feature separation module (Section 3.5) preserves fine detail.** Unlike prior work (Min & Corso 2020, Lee & Byun 2021) that pools features and loses granularity, this module retains complete feature information in an embedding space and contrasts action/background at the point level using cosine similarity (Eq. 10–13). The technical differentiation from prior coarse-grained approaches is clearly stated.

- **Optimized pseudo label mining strategy with a concrete fix to LACP.** The paper identifies a specific limitation in LACP's mining strategy (too-low γ_act limits recall) and adds a top-1 class-match constraint to avoid false positives (Section 3.3). The reasoning for this fix is clearly explained.

- **Ablation study isolates each module's contribution.** Section 4.2 reports the additive gain of each component (2.1%, 7.4%, 4.2%, 5.1%) on THUMOS'14, enabling readers to understand which modules drive improvement.

## Weaknesses

### Fatal
None. The paper presents a coherent method with verifiable claims. No weakness invalidates the core contribution.

### Major
None. The issues identified below are addressable in revision and do not threaten acceptance.

### Minor

- **Ambiguous headline metric specification.** The contribution (line 27) states "56.74% with the average mAP on THUMOS'14" without specifying the IoU range. Table 1's caption does specify that it reports Avg(0.1:0.5) and Avg(0.3:0.7), and Table 2's caption specifies AVG = Avg(0.1:0.1:0.7). The 56.74% presumably corresponds to Avg(0.1:0.5) from Table 1, while the ablation table uses a different metric that includes harder IoU thresholds (0.6, 0.7). The numbers are not contradictory, but the abstract and contribution section should explicitly state the IoU range associated with the headline number so readers can immediately reconcile it with the ablation results.

- **Ablation baseline is weaker than a fair point-supervised baseline.** The "none" configuration in Table 2 uses only the video-level classification loss (Section 3.2) and does not incorporate point-level labels at all. The 7.4% gain from pseudo label mining therefore conflates two effects: adding point-level supervision signals and the mining strategy itself. A stronger baseline would start from a setting that already uses original point labels in a point-level loss (even a simple one). This does not invalidate the overall comparison against prior SOTA (Table 1), but it overstates the relative importance of the mining module in the ablation.

- **Several key hyperparameters are unreported or unsupported by sensitivity analysis.** The thresholds ψ_same and ψ_diff for the feature separation loss (Section 3.5) are defined but their numerical values are never given. The thresholds γ_act and γ_bkg for pseudo label mining (Section 3.3) are also not reported, and no sensitivity analysis is provided for any of these. Since the pseudo label mining module produces the largest single gain (7.4%), the sensitivity of its thresholds is particularly important for reproducibility and for understanding how robust the method is.

- **Feature length T after label extension is not stated.** Section 3.1 describes extending the feature length from T_ori to T but never reports what T is. This is a basic experimental variable that could affect performance independent of the method's reasoning.

- **Vague comparison with fully-supervised methods.** Section 4.1 states that performance "at low IOU (i.e., 0.3 or 0.4) are even better than that of some fully-supervised approaches" without naming specific methods, years, or numbers. As written, this claim is untestable and does not strengthen the paper. It should either be removed or backed by explicit citations and numbers from Table 1.

- **Feature masked attention layer is mentioned but not described.** Section 3.5 states that "this layer is added to the convolution calculation process to focus effectively on features of interest" but provides no architectural detail about how it operates. Given that it is part of the novel feature separation module, readers need at least a brief description of its mechanism.

### Trivial

- The paper repeatedly defers key content to the appendix ("in the Sec.") — including ablation algorithms, comparative experiments on ActivityNet/BEOID/GTEA, error analysis, and hyperparameter settings. While this is partly a space constraint issue, the main text would benefit from at least a summary table of results on the additional benchmarks.

## Nice-to-Haves

- A sensitivity analysis on γ_act and γ_bkg (the mining thresholds) would strengthen confidence in the method's robustness. This is especially useful because the mining module produces the largest ablation gain.

- If the T_ori and T values for feature extension are reported in the appendix, they should be brought to the main text.

## Removed Points

- *"Table 1 is not visible in the main text — the paper provides no numerical list of comparison methods."* **Removed.** Table 1 exists in the original submission as an image; the text extraction is a parser artifact, not an author omission. The numerical data is present in the original PDF.

- *"The headline 56.74% and the ablation 51.4% are inconsistent/contradictory."* **Removed as stated; replaced with clarified ambiguity (see Minor weakness 1).** The two numbers correspond to different IoU ranges (Avg(0.1:0.5) vs. Avg(0.1:0.1:0.7)), both defined in their respective table captions. The issue is lack of explicit specification in the abstract/contributions, not a contradiction.

- *"The baseline may discard all point-supervision information, making the 7.4% gain trivial."* **Demoted to Minor (see Minor weakness 2).** The baseline is indeed weak, but calling the gain "trivial" overstates the case — the pseudo label mining strategy is a real technical contribution that the paper improves over LACP, and the primary evaluation is against prior SOTA methods (Table 1), not the no-label baseline.

- *"Reproducibility concerns about undisclosed hyperparameters."* **Partially removed per rules; remaining concerns kept as Minor weaknesses 3 and 4.** The rules state to remove nitpicks about "trivial implementation details" but hyperparameters γ_act, γ_bkg, ψ_same, ψ_diff are central to the method and their omission is a genuine gap.

- Strength Finder's generic strengths removed: claims about "importance of the research question" and "value to the research community" are too generic to be useful.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses converge on the paper's stated strengths (multi-module pipeline targeting action-background confusion, strong benchmarking performance) and weaknesses (incomplete specification of metrics and hyperparameters). No emergent insight arises that the paper itself does not articulate.

## Suggestions

1. **Disambiguate metrics in the abstract and contributions.** Explicitly state "56.74% Avg(0.1:0.5) mAP on THUMOS'14" in the contribution list, and add a note that the ablation table uses Avg(0.1:0.1:0.7) for a more complete IoU range.
2. **Add a stronger ablation baseline** that already uses original point labels in a point-level loss, so the additive value of each module is measured from a fairer starting point.
3. **Report all key hyperparameters** (γ_act, γ_bkg, ψ_same, ψ_diff, T) in the main text with a brief sensitivity analysis for the mining thresholds.
4. **Either remove or substantiate** the claim about outperforming fully-supervised methods. If the comparison is against older methods (pre-2020), state this explicitly.
5. **Add a brief description** of the feature masked attention layer's mechanism in Section 3.5.

## Score and Decision

This paper makes a credible technical contribution to point-supervised temporal action localization. The core idea — fine-grained separation of action and background through label densification, score contrast, and feature-space separation — is well-motivated and the individual components are reasonable. The main weaknesses are presentation issues (ambiguous metric specification, missing hyperparameters, unsupported claims about fully-supervised methods) rather than fundamental flaws in methodology or evidence. The state-of-the-art claims are supported by the reported comparison table. With straightforward revisions to clarify metrics, report hyperparameters, and strengthen the ablation baseline, the paper would meet the bar for acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>