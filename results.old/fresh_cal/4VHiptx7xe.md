Now I have all the information needed. Let me construct the final consolidated review.

## Summary

STRAP proposes a non-parametric sub-trajectory retrieval method that uses off-the-shelf vision foundation models (DINOv2/CLIP) and subsequence dynamic time warping (S-DTW) to retrieve relevant sub-sequences from large multi-task prior datasets at test time, augmenting few-shot imitation learning. The key insight is that retrieving at the sub-trajectory level (rather than full trajectories or individual states) enables sharing of common low-level behaviors across semantically different tasks, improving data utilization. The method is evaluated on LIBERO-10 in simulation and on real-world DROID-Kitchen tasks, outperforming prior retrieval methods (BehaviorRetrieval, FlowRetrieval), multi-task policies, and fine-tuning baselines.

## Strengths

1. **Sub-trajectory retrieval via S-DTW yields a +4.1% improvement over full-trajectory retrieval across 10 LIBERO-10 tasks** (Section 5.2, Table 1). This directly validates the paper's central claim that sub-trajectory granularity enables better data utilization than whole-trajectory retrieval, as full trajectories can contain irrelevant segments that degrade performance.

2. **Off-the-shelf vision foundation models (DINOv2/CLIP) achieve strong retrieval without any in-domain training**, eliminating the need for dataset-specific encoder training required by prior work (BehaviorRetrieval, FlowRetrieval). The ablation shows DINOv2 and CLIP perform nearly identically (only +0.7% separation), and the method scales to a 5000-demonstration DROID dataset (Section 5.1), supporting the claim of broad applicability.

3. **Strong experimental design covering both simulation (LIBERO-10) and real-world settings (DROID-Kitchen)** with appropriate baselines: behavior cloning, fine-tuning, multi-task policy, BehaviorRetrieval, and FlowRetrieval. STRAP consistently outperforms all baselines, with the comparison against fine-tuning (which sees all prior data) being particularly informative.

4. **Automatic sub-trajectory segmentation via proprioceptive velocity thresholding** (Section 4.2) eliminates the need for manual labeling of sub-trajectories, making the pipeline practical for large-scale offline datasets without human annotation effort.

5. **Qualitative analysis of retrieved data (Figure 13)** provides direct evidence that STRAP retrieves semantically relevant sub-trajectories, selecting data from only 5/90 tasks that share sub-task components with the target task, while ignoring irrelevant data — confirming the mechanism behind the performance gains.

6. **Systematic ablation studies** validate key design choices: comparison of DINOv2 vs. CLIP, varying the number of retrieved segments K, and sub-trajectory vs. full-trajectory retrieval (Section 5.2), providing empirical grounding for design decisions.

## Weaknesses

### Fatal
None.

### Major

1. **Missing variance or per-seed reporting in the main quantitative results (Table 1).** The paper states it runs experiments over 3 seeds (1234, 42, 4325) and seeds both retrieval and training, but the main results table and accompanying text report only mean success rates without standard deviations, standard errors, or per-seed breakdowns. Without knowing whether the reported gains (e.g., STRAP 86.7% vs. FT 79.4%, a +7.3% margin) are stable across seeds, the reader cannot assess the reliability of the central quantitative claims. This is the primary evidential weakness, as the paper's core argument rests on these numbers. (Note: per-seed retrieval results are referenced to Appendix Table 9, but the main table lacks variance information.)

### Minor

2. **Segmentation threshold ε is not reported numerically.** Section 4.2 describes a segmentation heuristic based on end-effector velocity dropping below a threshold ‖ẋ‖ < ε, but the threshold value itself is never given (even as an appendix reference). Since this hyperparameter directly determines what sub-trajectories are segmented and thus what data is retrieved, it is a non-trivial detail. The paper acknowledges the heuristic could be improved, but the chosen value should still be reported.

3. **The DINOv2/CLIP model variant or layer used for image embeddings is not specified.** Section 4.3 uses a vision foundation model F(·) and computes L2 distances in embedding space, but never states which model variant (e.g., DINOv2 ViT-B/14 vs. ViT-L/14, CLIP ViT-B/16 vs. ViT-L/14) or which layer's features are used. This makes exact reproduction dependent solely on the promised code release rather than the paper itself.

4. **No discussion of retrieval computational cost or scalability.** The retrieval step compares each target sub-trajectory against every trajectory in the prior dataset using S-DTW — for LIBERO-90 that's up to 4500 trajectories × multiple sub-trajectories per target. The paper claims STRAP "scale[s] with minimal compute overhead" (Conclusion) but provides no wall-clock runtime, scaling analysis, or discussion of practical approximations. While not fatal, this omission prevents practitioners from assessing feasibility at larger dataset scales.

### Trivial

None.

## Nice-to-Haves

- A brief runtime/scaling analysis (e.g., retrieval time vs. prior dataset size for 500, 1500, 5000 trajectories) would substantiate the scalability claim and help practitioners gauge practical usability.
- Reporting per-task results with per-seed breakdowns (beyond the averages in Table 1) would further strengthen the evidence.

## Removed Points

These points are flagged to be removed — treat them with caution if considering them:

- **Algorithm 1 pseudocode not shown in main text / missing appendix content.** The harsh critic notes Algorithm 1 is referenced but not shown in the main paper body. The parser strips appendix/supplementary content from all papers; these sections exist in the original submission. REMOVED per rule on missing appendix content.
- **Tables 3, 9 referenced but not shown in extracted text.** Same issue — appendix content stripped by parser. REMOVED.
- **Section 3 (Preliminaries/DTW) described as "overly long."** This is a style/subjective judgment nitpick about presentation choices, not a substantive weakness. REMOVED.
- **Speculation about whether embeddings are normalized before L2 distance computation.** The critic hypothesizes this could affect results but provides no evidence this is an actual problem. REMOVED as speculative.
- **Request for comparison against a "train on all prior data" baseline.** The paper already includes multi-task policy (trained on prior + target) and fine-tuning baselines, which collectively address this concern. The existing comparisons are adequate. REMOVED as scope creep — the paper's claim is about retrieval, not about scale alone.
- **Strength Finder: "this paper addressed an important problem" — generic.** This particular framing was not explicitly included; all listed strengths were concrete. No strengths removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add standard deviations or per-seed results to Table 1** (and the real-world results) to allow readers to assess the reliability of the reported gains. With 3 seeds already collected, this requires no additional experiments.
2. **Report the numerical value of the segmentation threshold ε** (and the specific DINOv2/CLIP layer used) either in the main text or by explicit reference to an appendix section containing implementation details.
3. **Include a brief computational cost analysis** — even a single sentence with approximate wall-clock retrieval time for the LIBERO-90 and DROID-5000 settings would substantiate the scalability claim and address a natural practitioner question.

## Score and Decision

This paper presents a well-motivated, clearly described method with a sound technical approach. The experimental design is comprehensive (sim + real, multiple strong baselines, ablations), and the results consistently support the central claims. The main weakness — missing variance reporting — is significant but not structural, and the reported performance margins are large enough that the core conclusions are likely robust. The unspecified hyperparameter details are addressable in a final version. The contribution (sub-trajectory retrieval with off-the-shelf foundation models for few-shot robot learning) is novel, practical, and of clear interest to the robot learning community.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>