Now I have a thorough understanding of the paper and the reviews. Let me construct the final consolidated review.

---

## Summary

STRAP proposes a test-time retrieval paradigm for few-shot robot imitation learning: from a small set of target demonstrations, it automatically segments them into sub-trajectories, then uses subsequence dynamic time warping (S-DTW) on DINOv2 embeddings to retrieve relevant sub-trajectories from a large offline corpus. A policy is trained on the union of target and retrieved data, avoiding expensive generalist pre-training. Experiments on LIBERO-10 (simulation) and DROID-Kitchen (real-world) show gains over state-based retrieval (BR, FR), full-trajectory retrieval, and fine-tuned multi-task policies.

## Strengths

- **Sub-trajectory retrieval consistently outperforms full-trajectory and state-based retrieval.** The paper reports a +4.1% improvement over full-trajectory S-DTW (D-T) across all 10 LIBERO tasks (Sec. 5, line 167), and the textual descriptions further indicate substantial margins over BR and FR. This directly supports the core claim that sub-trajectory granularity enables better cross-task data sharing than existing retrieval units.

- **Off-the-shelf DINOv2 embeddings work competitively without any in-domain training.** STRAP replaces the domain-specific, trained-from-scratch encoders used by prior work (BR, FR) with DINOv2 features, yet outperforms those methods. The ablation showing DINOv2 and CLIP differ by only +0.7% (line 172) confirms the robustness and practical scalability of this choice—no re-training is needed when scaling to larger datasets like DROID (5000 demonstrations).

- **S-DTW enables matching variable-length sub-trajectories, maximizing cross-task sharing.** Figure 13 qualitatively shows STRAP retrieves data from only 5/90 tasks that share subtask components with the target (e.g., "close the drawer"), while ignoring irrelevant tasks—a selectivity that full-trajectory and state-based methods cannot achieve. The +4.1% improvement over full-trajectory S-DTW quantitatively validates this advantage.

- **Comprehensive ablations on retrieval parameter K and foundation model choice.** The paper reports task-dependent sensitivity to the number of retrieved segments K (with full search deferred to Tab. 9) and compares DINOv2 vs. CLIP, providing actionable insights for practitioners.

- **Automatic proprioception-based segmentation removes manual labeling.** The velocity-threshold method (Sec. 4.2) segments target demonstrations without human annotation or semantic parsing, making the pipeline practical for large-scale offline datasets. The paper also honestly acknowledges this heuristic can be improved.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The segmentation heuristic is not ablated.** The velocity-threshold method (Sec. 4.2) is a key component whose sensitivity to the threshold parameter ε is not analyzed. It is unclear how performance degrades on tasks without clear motion pauses (e.g., continuous stirring, wiping) or whether an oracle/manual segmentation would yield different results. The paper acknowledges this "can certainly be improved" but provides no quantitative boundary on when it works or fails. This is the most significant methodological gap.

- **No ablation isolating the benefit of DTW from the benefit of sub-trajectory granularity.** The paper shows sub-trajectories + S-DTW (STRAP) outperform full-trajectory + S-DTW (D-T), but does not compare against a simpler baseline: averaging DINOv2 embeddings over sub-trajectories and using cosine similarity (no DTW). Such a baseline would isolate whether the gains come from DTW's temporal alignment or merely from sub-trajectory decomposition. The paper mentions averaging "lose[s] out on the actions and dynamics" (line 80) but does not quantify this loss. While not fatal, this omission leaves ambiguity about which component drives the improvement.

- **Computational cost of S-DTW retrieval is not characterized.** STRAP must match each target sub-trajectory against every possible subsequence in the prior dataset. The algorithmic complexity and wall-clock time for the largest setting (5000-demo DROID prior) are not reported. The paper claims "minimal compute overhead" (line 181) in the conclusion without supporting evidence. For a method positioned as a practical alternative to training generalist policies, this omission is relevant.

- **Real-world results are only available in a table that was rendered as an image and garbled during parsing** (Tab. 3). Quantitative results for the DROID-Kitchen evaluation are referenced but not readable in this extracted version. This is a PDF-extraction artifact, not an author error, but it means the claim of "robust performance in challenging real-world scenarios" cannot be fully verified from this version.

### Trivial

None.

## Nice-to-Haves

- Adding a baseline where sub-trajectories are represented by averaged DINOv2 embeddings + cosine similarity would cleanly isolate the benefit of S-DTW alignment from the benefit of sub-trajectory decomposition.
- A sensitivity analysis of the velocity threshold ε for segmentation, or a comparison against oracle/manual segmentation, would strengthen confidence in the method's robustness.
- Reporting retrieval wall-clock time for the largest prior dataset (5000 demos) would help practitioners assess practicality.
- Exploring whether using language embeddings (e.g., CLIP text encoder) for retrieval (in addition to policy conditioning) further improves performance, as the paper currently conditions on language only during policy training.

## Removed Points

These points were raised by reviewers but are removed per the consolidation rules:

1. **"Real-world results absent from supplied text" / "Real-world experiments described only for setup, not results"** — REMOVED. The paper states results are in Tab. 3. Table contents were lost due to PDF-to-text parsing (the table appears as an embedded image that could not be extracted). The original submission contains these results; this is a parser artifact, not an author omission.

2. **"Experimental tables unreadable / garbled"** — REMOVED. The garbled rendering of Table 1 is a PDF extraction artifact. The original submission has properly typeset tables.

3. **"No comparison to full-trajectory mean-pooling baseline"** — REMOVED. The paper already compares against D-T (full-trajectory S-DTW), which is a stronger full-trajectory baseline than mean-pooling. The core comparison (sub-trajectory vs. full-trajectory) is already established. This specific ask is a subset of the more general "DTW vs. averaging" concern already listed as a Minor weakness.

4. **"Missing Tab. 9" (K search), "Missing policy architecture details"** — REMOVED. These are in the appendix/body of the original submission and were lost during parsing. The parser strips appendix content; they exist in the original.

5. **Formatting/style/presentation nitpicks, "unclear phrasing" criticisms** — REMOVED as parser artifacts or generic complaints.

## Novel Insights

None beyond the paper's own contributions. The reviews surface standard methodological improvement requests (ablations, baselines, complexity analysis) but do not identify a novel angle or reinterpretation of the work.

## Suggestions

- Add an ablation that replaces S-DTW with simple averaging of DINOv2 embeddings over sub-trajectories (cosine similarity for retrieval). This would cleanly quantify the contribution of temporal alignment via DTW vs. sub-trajectory decomposition alone.
- Add a sensitivity analysis of the segmentation threshold ε, and ideally compare against an oracle segmentation (e.g., using ground-truth task boundaries) to bound the headroom for improvement.
- Report retrieval runtime statistics (e.g., seconds per query sub-trajectory) for the largest prior dataset used, to support the claim of practical scalability.

## Score and Decision

**Originality** — Good. Retrieving sub-trajectories (rather than states or full trajectories) with off-the-shelf foundation models and S-DTW is a well-motivated and relatively underexplored direction. The combination is novel, though each component individually (foundation models for robotics, DTW, sub-trajectory decomposition) is known.

**Importance of research question** — High. Enabling few-shot policy learning from large, diverse offline datasets without expensive generalist training is a practically important problem.

**Claims well supported** — Moderately. The LIBERO simulation results (reported in prose) support the core claims. However, the real-world quantitative results are only in Tab. 3 (rendered unreadable by parsing), and the missing ablations (segmentation sensitivity, DTW vs. averaging) leave some ambiguity about what drives the gains. The core claim is supported; the finer-grained mechanistic claims are partially supported.

**Soundness of experiments** — Adequate. Multiple seeds, standard LIBERO benchmark, qualitative visualizations, and real-world setup are described. Main gaps: no segmentation ablation, no DTW-vs-averaging ablation, no computational cost characterization.

**Clarity of writing** — Clear. The motivation, method, and experimental setup are well-articulated. The extracted text has parsing artifacts but the underlying writing is strong.

**Value to the research community** — Moderate to high. The sub-trajectory retrieval paradigm is practically useful and the method is designed for easy adoption (off-the-shelf models, no in-domain training). With the suggested ablations, this could become a widely used baseline.

The paper has a solid core contribution and presents credible evidence for its main claims. The identified weaknesses (segmentation not ablated, DTW benefit not isolated, computational cost not characterized) are addressable in a revision and do not invalidate the central finding that sub-trajectory retrieval outperforms state-based and full-trajectory retrieval. The paper deserves acceptance over rejection.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>