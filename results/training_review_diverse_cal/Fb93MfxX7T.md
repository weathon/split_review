Now I have verified the key claims. Let me write the consolidated review.

## Summary

This paper presents a systematic, unifying empirical study of 14 parameter-efficient transfer learning (PETL) methods on Vision Transformers (ViT). Rather than proposing a new method, it provides a carefully controlled comparison across low-shot (VTAB-1K, 19 tasks), many-shot (3 full datasets), and distribution-shift robustness settings, with consistent hyperparameter tuning across all methods. Key insights include: (1) with careful tuning, most PETL methods achieve similar accuracy on VTAB-1K, contradicting prior reports of large gaps; (2) despite similar accuracy, methods make diverse predictions that could enable complementarity; (3) PETL remains effective in many-shot regimes, matching full fine-tuning with far fewer parameters; and (4) PETL better preserves robustness to distribution shifts than full fine-tuning.

## Strengths

1. **Carefully tuned hyperparameters reveal convergence of PETL accuracy on VTAB-1K, challenging prior beliefs.** The paper systematically tunes learning rate, weight decay, method-specific parameters, and drop path rate across 14 PETL methods. The low relative standard deviations reported in Table 1 (e.g., 0.54 for Natural, 0.94 for Specialized groups) demonstrate that the convergence is not an artifact of poor tuning. This provides a unifying reference and shows that simple methods like BitFit, previously reported as inferior, are competitive when properly tuned.

2. **PETL methods make diverse predictions despite similar accuracy, with strong evidence from prediction similarity analysis.** The prediction similarity matrices (Figure 3) show that different PETL methods disagree on ~20% of predictions in DTD/Retinopathy and ~35% in DMLab. The Venn-diagram analysis (Figure 3, subfigures) further reveals limited overlap in both high-confidence correct predictions and low-confidence wrong predictions across methods. This complementarity finding is well-supported and opens a new direction for leveraging PETL diversity.

3. **PETL is effective in many-shot regimes with far fewer parameters.** On CIFAR-100, RESISC, and Clevr-Distance full datasets, PETL achieves comparable or better accuracy than full fine-tuning with only 2–5% of trainable parameters, with performance plateauing quickly. This extends PETL's demonstrated utility beyond low-shot settings.

4. **PETL preserves distribution-shift robustness significantly better than full fine-tuning on CLIP ViT-B/16.** Table 2 shows PETL methods outperform full fine-tuning by 12–14% on average across four distribution-shift benchmarks (ImageNet-V2, -R, -S, -A), highlighting a practical advantage for deployment scenarios.

5. **Insightful decomposition of PETL's success into dual roles: high-capacity learner and effective regularizer.** By categorizing VTAB-1K tasks into those where full fine-tuning beats linear probing (case 1) and vice versa (case 2), the paper shows PETL excels in both regimes. In many-shot settings, PETL still outperforms full fine-tuning on case-2 tasks (e.g., CIFAR-100), indicating that even with ample data, full fine-tuning risks washing away pre-trained knowledge.

6. **Open-source framework enabling reproducible PETL evaluation.** The paper provides a systematic framework covering 14 methods, 19 low-shot tasks, 3 many-shot tasks, and 5 robustness datasets, with detailed documentation, lowering the barrier for future systematic comparisons.

## Weaknesses

### Fatal

None.

### Major

1. **Ensemble evaluation uses an inappropriate baseline, inflating the apparent gain.** In Section 4 (Figure 5 in the paper's enumeration, described in the text as Figure 4), the ensemble performance gain is computed using "the worst PETL method as the baseline" (verified, line 388). This is not standard practice: a practitioner would compare the ensemble to the *best* single PETL method (or at least the mean) to determine whether the ensemble actually improves over what is already achievable. Using the worst method as a baseline guarantees an apparent gain. The paper's claim of "consistent gain" from ensembling is thus unsubstantiated by this particular analysis. This is the paper's most significant methodological weakness and directly affects one of its supporting claims.

   *However*, the paper's stronger evidence for complementarity is the prediction similarity matrices (Figure 3), which convincingly show different methods make different mistakes. That finding is unaffected by the ensemble baseline issue. The ensemble analysis as presented weakens rather than strengthens the complementarity narrative and should be redone with a proper baseline or removed.

### Minor

1. **The many-shot study covers only 3 datasets, limiting the generality of the claims.** Section 5 uses CIFAR-100, RESISC, and Clevr-Distance (one from each VTAB group) to draw conclusions about PETL in many-shot regimes. While these results are suggestive and align with the paper's broader narrative, three datasets do not constitute a robust empirical basis for general claims about many-shot performance. The VTAB-1K low-shot study covers 19 tasks, creating an asymmetry in empirical breadth. The claim that "PETL is also effective in many-shot regimes" is reasonable as a preliminary finding but would benefit from either additional datasets or a more explicitly qualified statement.

2. **The robustness study uses a single backbone (CLIP ViT-B/16) and a single target distribution (100-shot ImageNet).** The finding that PETL preserves distribution-shift robustness better than full fine-tuning is interesting, but it is demonstrated in one setting. While the evaluation on 4 distribution-shift benchmarks (ImageNet-V2, -R, -S, -A) provides some breadth, the single-backbone design limits the generality of the conclusion. An additional backbone (e.g., a standard ViT pre-trained on ImageNet-21K) or a different target distribution would strengthen the claim.

3. **No variance or confidence intervals reported across runs.** The paper claims methods perform "similarly" on VTAB-1K, and Table 1 shows relative standard deviations *across methods* (not across runs). Without multiple random seeds or confidence intervals, the reader cannot assess whether the small accuracy differences between methods are meaningful or within noise. Given that the central claim is about similarity across methods, run-level variance information would substantially strengthen the argument.

### Trivial

None that survive filtering — the remaining points are either addressed below as Nice-to-Haves or were removed.

## Nice-to-Haves

- **Redo the ensemble analysis with a proper baseline.** Compare the ensemble average of all PETL methods against the *best* single PETL method per dataset, and report the fraction of tasks where the ensemble improves. If the ensemble does not consistently beat the best single method, that is itself an interesting finding worth reporting.
- **Add more many-shot datasets.** Even 2–3 additional full-dataset experiments (e.g., from the VTAB tasks with larger training sets) would substantially strengthen the many-shot claims.
- **Report run-level variance.** Adding results across 3 random seeds for the main VTAB-1K experiments would clarify whether the observed 3% range across methods is practically meaningful.
- **Deepen the analysis of why methods differ beyond descriptive observations.** The paper attributes prediction diversity to "different inductive biases" without analyzing what those biases are. A small probing analysis (e.g., examining attention maps or feature similarity across layers for a subset of methods) would move the complementarity narrative from observation toward mechanistic understanding.

## Removed Points

- *"The ranking analysis in Figure 2 is dense and difficult to read"* — The harsh critic themselves notes that "the takeaway...is clear" and the raw accuracy values in Table 1 already show the pattern. This is a presentation observation that does not affect the paper's validity or contribution.
- *Strength Finder claim that "WiSE is shown to be applicable to PETL, but full fine-tuning with WiSE achieves higher overall accuracy" as a strength* — This is a finding about a limitation (full fine-tuning+WiSE beats PETL+WiSE), not a strength of the PETL methods themselves. It is a valid observation but misplaced as a strength.
- *Request to add "different PETL methods apply to different tasks" analysis beyond stated scope* — The paper's domain-affinity ranking analysis already provides actionable guidelines; deeper mechanistic analysis is a follow-up direction, not a weakness of the current study.

## Novel Insights

The most interesting meta-insight from the reviews is that the paper's valid core contributions (the convergence of PETL accuracy under careful tuning and the prediction diversity finding) are somewhat undermined by a self-inflicted methodological error in the ensemble analysis. The paper would be *stronger* if it simply removed the flawed ensemble comparison and let the prediction similarity matrices stand as the primary evidence for complementarity. This suggests a broader lesson: when a paper already has clean, self-contained evidence for a claim (the similarity matrices showing 20-35% disagreement), adding an analysis with a questionable baseline (ensemble vs. worst method) does more harm than good. The reviews also surface a tension between the paper's breadth (14 methods, 3 regimes) and depth (limited many-shot/robustness settings) that is inherent to any large-scale empirical study, but the ensemble issue is the only problem requiring substantive correction.

## Suggestions

1. **Fix or remove the ensemble baseline comparison.** Either (a) redo Figure 4 comparing the ensemble to the *best* single PETL method per dataset, or (b) remove the ensemble analysis entirely and let the prediction similarity matrices stand as sufficient evidence of complementarity. Option (b) may be the cleanest path.
2. **Calibrate the claims in Sections 5 and 6.** Replace strong language like "PETL is also effective in many-shot regimes" with more precise phrasing: "on the three full datasets we tested, PETL achieves comparable results..." Similarly for the robustness claim: "on CLIP ViT-B/16 with 100-shot ImageNet, PETL preserves robustness better than full fine-tuning."
3. **Add a brief note on the 1.5% parameter cap choice.** The paper sets a cap of ≤1.5% of ViT-B/16 parameters for low-shot experiments but does not discuss whether conclusions are sensitive to this threshold. A short justification or ablation would help.

## Score and Decision

**Originality:** 7/10 — The paper's contribution is not a new method but a systematic empirical study. The key findings (convergence of PETL accuracy under careful tuning, prediction diversity) are novel and valuable as a community reference.

**Importance of research question:** 8/10 — Understanding when and how to use PETL is practically important given the growing size of pre-trained models. A unifying study fills a genuine gap.

**Claims well supported:** 5/10 — The VTAB-1K low-shot study is thorough and well-supported. The complementarity claim is well-supported by prediction similarity matrices. However, the ensemble analysis uses a flawed baseline, and the many-shot/robustness claims are supported by thinner evidence than their phrasing suggests.

**Soundness of experiments:** 6/10 — The systematic hyperparameter tuning is a strength. The main VTAB-1K experiments are sound. The ensemble analysis has a methodological flaw. The many-shot and robustness experiments are sound as far as they go but limited in scope.

**Clarity of writing:** 7/10 — The paper is well-organized and clearly written. The figures and tables are informative.

**Value to the research community:** 8/10 — The systematic comparison and open-source framework are practically valuable. The finding that methods converge under careful tuning is an important reference for practitioners. The complementarity finding opens a new research direction.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>