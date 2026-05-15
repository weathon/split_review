Now I have all the information I need to produce the consolidated review. Let me synthesize everything carefully.

## Summary

This paper proposes STRAP, a method for retrieving relevant sub-trajectories from large offline robot datasets to augment few-shot imitation learning at test time. The key ideas are: (1) using off-the-shelf vision foundation models (DINOv2, CLIP) to compute frame-level similarities robust to visual domain shifts, (2) using subsequence dynamic time warping (S-DTW) to match variable-length sub-trajectories from a few target demonstrations to the most similar segments in a large multi-task corpus, and (3) automatically segmenting target demonstrations using a velocity-based heuristic. Experiments on LIBERO-90 and DROID-Kitchen show that STRAP outperforms full-trajectory retrieval, state-based retrieval (BehaviorRetrieval, FlowRetrieval), and multi-task/fine-tuning baselines.

## Strengths

1. **Well-motivated conceptual contribution.** The core insight — that retrieving sub-trajectories rather than full trajectories or individual states enables cross-task sharing of low-level behaviors (e.g., "close drawer" appears across many tasks) — is clearly articulated and convincingly motivated with concrete examples. This is a genuinely useful framing that differs meaningfully from prior work.

2. **Clean use of off-the-shelf foundation models for retrieval similarity.** By using DINOv2/CLIP embeddings with L2 distance (no per-dataset training required), STRAP avoids the main bottleneck of prior methods like BehaviorRetrieval and FlowRetrieval, which require training domain-specific encoders. The paper demonstrates empirically that DINOv2 features retrieve semantically relevant sub-trajectories and are robust to texture and pose variations (Figure 13).

3. **Empirical validation of the core claim: sub-trajectory > full-trajectory retrieval.** The ablation comparing STRAP (sub-trajectory S-DTW) to full-trajectory DTW (D-T) shows a +4.1% improvement averaged across 10 LIBERO tasks (Sec. 5.2, Table 1). This directly supports the paper's central hypothesis that finer granularity enables better data utilization.

4. **Practical automatic segmentation.** The velocity-based thresholding (Sec. 4.2) removes the need for manual annotation of sub-trajectory boundaries, operating only on the small target set (~3-5 demos) and not on the large offline corpus. This makes the pipeline practical without annotation overhead.

## Weaknesses

### Fatal

None.

### Major

1. **Computational complexity and scalability of the retrieval step are not analyzed.** S-DTW between a query of length L and a reference of length M costs O(L·M) per pair. The paper describes performing this exhaustively between each target sub-trajectory (from ~5 demos) and each trajectory in a corpus of up to 5000 trajectories. The text promises "a computationally efficient algorithm" (Sec. 4.4) and Algorithm 1, but provides no runtime analysis, wall-clock measurements, indexing scheme, approximation strategy, or discussion of how the O(Σ_i |D_prior|·|T_target|·L_i) complexity is made tractable. The abstract and conclusion claim "the ability to scale to much larger offline datasets" and "minimal compute overhead," but no evidence (runtime, memory, or scaling plot) supports this. This is not a reproducibility issue (the algorithm is clearly defined) but an evidential gap for a claimed strength of the method. The paper should either report runtime on the datasets used or qualify the scalability claim.

2. **No experimental comparison to SAILOR (Nasiriany et al., 2022) or any skill-retrieval baseline.** SAILOR retrieves skills — i.e., temporally contiguous sub-trajectories — using learned skill embeddings. The paper discusses SAILOR in the related work and distinguishes itself (foundation models + DTW vs. trained skill embeddings), but never compares against it experimentally. Since SAILOR is the most directly comparable prior that also retrieves sub-trajectory-like units, the absence of this comparison makes it difficult to isolate whether STRAP's gains come from sub-trajectory granularity per se, or from the specific combination of foundation models + DTW. The claim "to our knowledge, we propose the first robot sub-trajectory retrieval mechanism" (Sec. 2) is also somewhat overbroad given SAILOR's skill retrieval. Including SAILOR (or a skill-retrieval adaptation) as a baseline would both strengthen the evaluation and tighten the novelty claim.

### Minor

1. **No robustness analysis of the automatic segmentation.** The method segments target demonstrations using a velocity threshold (‖ẋ‖ < ε), and the entire retrieval pipeline inherits these boundaries. The paper provides no sensitivity analysis (sweep of ε), no quantitative segmentation quality metrics (e.g., precision/recall against manual boundaries), and no ablation using oracle (ground-truth) segmentation. The authors acknowledge "this could certainly be improved," but without analysis, it is unclear whether performance depends on near-perfect segmentation or whether the method is robust to poor boundaries. Given that segmentation is applied only to ~3-5 target demos (not the large corpus), the impact may be limited, but some validation would strengthen confidence.

2. **The claim that foundation models "capture strong notions of 'object-ness, discarding spurious visual differences'" (Abstract) is supported only qualitatively.** Figure 13 shows that retrieved sub-trajectories are semantically relevant, which is suggestive. But there is no quantitative retrieval metric (e.g., retrieval precision against ground-truth task labels, retrieval diversity, or ranking metrics like Recall@K) to substantiate the claim that the foundation model embeddings are the key driver of robustness.

3. **No discussion of limitations.** The conclusion (Sec. 6) summarizes contributions but does not discuss any limitations — e.g., reliance on segmentation quality, computational cost of exhaustive S-DTW matching, the assumption of expert-level trajectories in D_prior, or failure cases. Including a limitations paragraph would improve scholarly rigor and is standard practice.

### Trivial

None. The paper is generally well-written and the parsed text, despite loss of images/tables, reads clearly.

## Nice-to-Haves

- A comparison of S-DTW against simpler temporal matching alternatives (e.g., temporal averaging of frame embeddings + nearest neighbor, or sliding-window cosine similarity) would further justify the need for DTW.
- Reporting wall-clock retrieval time for the LIBERO-90 (4500 trajectories) and DROID-Kitchen (5000 trajectories) settings would directly address the scalability question.
- A failure case analysis (e.g., a task where STRAP retrieves the wrong sub-trajectory and the policy fails) would build trust in the method's known failure modes.

## Removed Points

- **"Failure to report variance or statistical significance"** — REMOVED. The paper states "we report runs over multiple seeds (1234, 42, 4325)" (Sec. 7). The tables are embedded as images in the original PDF and were stripped during parsing; whether standard deviations are shown in the original tables cannot be determined from the parsed text. The reviewer's concern may be valid in the original or may not be; this cannot be adjudicated on the parsed version alone.
- **"Real-world results not reported" and "tables not visible"** — REMOVED. These are parser artifacts; the original paper contains the tables as images.
- **"Algorithm body cut off"** — REMOVED as a reproducibility concern. The algorithm body is missing from the parsed text due to PDF extraction issues, not author omission. The computational tractability concern (KEPT above) is distinct and valid.
- **"No detail on which layer/representation is used (CLS token, patch average)"** — REMOVED. Trivial implementation detail that would belong in an appendix.
- **"L2 norm is a simple choice; alternatives not discussed"** — REMOVED. Nitpick that does not affect the paper's core claims.
- **"Conclusion suggests the paper would benefit from a quantitative metric for retrieval precision"** — Moved to Minor Weakness #2 above (rephrased).

## Novel Insights

None beyond the paper's own contributions. The reviews primarily confirm the paper's stated contributions and identify gaps the authors can address in a revision.

## Suggestions

1. **Add a runtime/complexity analysis.** Report wall-clock retrieval time for the LIBERO-90 and DROID-Kitchen settings. If any approximations or index structures are used (even simple ones like pre-computing trajectory embeddings), describe them explicitly. This would directly support the scaling claims in the abstract and conclusion.

2. **Include SAILOR as an experimental baseline** or, alternatively, rephrase the "first sub-trajectory retrieval mechanism" claim to accurately reflect that the novelty lies in the specific combination of foundation models + S-DTW rather than sub-trajectory retrieval per se.

3. **Add an ablation on the velocity threshold ε** and, if feasible, an oracle segmentation condition (using ground-truth subtask boundaries from LIBERO) to measure how much the automatic segmentation costs in performance.

4. **Add a limitations paragraph** discussing at least: (a) the computational cost of exhaustive S-DTW on very large corpora, (b) the assumption of expert-level demonstrations in D_prior, (c) the reliance on the velocity-based segmentation heuristic, and (d) known failure modes.

5. **Provide quantitative retrieval metrics** (e.g., precision@k against ground-truth task labels, or retrieval diversity) to substantiate the claim about foundation model robustness beyond the qualitative Figure 13.

## Score and Decision

The paper makes a clear, well-motivated contribution to test-time retrieval-augmented policy learning. The core idea — sub-trajectory retrieval with off-the-shelf foundation models and S-DTW — is novel, practical, and supported by empirical results showing meaningful improvements over full-trajectory and state-based retrieval. The writing is clear and the experimental design is sound.

The main weaknesses are: (1) the scalability claim is unsupported by any runtime analysis, (2) the most directly comparable prior work (SAILOR) is discussed but not benchmarked, and (3) the segmentation heuristic lacks robustness analysis. None of these invalidate the core contribution, but they leave the evaluation incomplete in ways that should be addressed.

I recommend **Accept** with the expectation that the authors address the major and minor weaknesses in a revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>