Now I have enough context to write the draft review. Let me verify the equation (3) claim specifically and the figure 4 label issue before drafting.Now let me calibrate with Round 1.Now for Round 2 narrowing within my bracket of 4–6.5.Based on my calibration rounds, I can now finalize the review.

**Round 1 bracket**: 4.0–6.5 (paper is clearly better than the weak anchors at ~3.0–3.5, but needs comparison against mid-range ANNS papers)

**Round 2 narrowing**: 
- wtNxByjLW3.md (4.80, Reject) — ARDG for MIPS: similar breadth of experiments but DiskHIVF has more dramatic improvements and cleaner deployment motivation; DiskHIVF is slightly better
- ESq3U7z6FD.md (6.00, Reject) — EHI hierarchical index: more ambitious end-to-end learning but has unfair baseline initialization concerns; DiskHIVF has cleaner experiments but an unresolved memory discrepancy
- oRNus243R6.md (5.67, Reject) — Diverse graph-based NNS: has theoretical guarantees but limited empirical scope; DiskHIVF has broader experiments but the 14× memory gap weakens its primary quantitative claim

DiskHIVF sits between wtNxByjLW3.md (4.80) and ESq3U7z6FD.md (6.00) — closer to the lower anchor given the major unexplained memory discrepancy which directly undermines the paper's headline complexity claim. Final score: **5.0**.

---

## Summary
DiskHIVF introduces a disk-resident hybrid memory-disk ANNS algorithm using a two-level hierarchical inverted file index, achieving a claimed memory complexity of O(√N·d + N) by sharing second-level cluster centers across first-level clusters. Experiments on four datasets (SIFT1M, GIST, BIGANN, DEEP at 1M–1B scale) report 10–30× memory reduction and 1.2–2.3× latency improvement at 90% recall@1 compared to graph-based baselines (DiskANN, Starling, SPANN), plus quantified disk-access savings from centroid reordering and a query-aware dynamic pruning mechanism.

---

## Strengths

- **Sub-linear memory complexity validated empirically across scales**: Table 2 demonstrates consistent 10–30× memory reduction across all four datasets — from 2.9 MB vs. 30–181 MB on SIFT1M to 1,213 MB vs. ~32,000 MB on BIGANN. The structural reason is clear: sharing m second-level centers across n first-level clusters requires only n+m = O(√N) centers rather than SPANN's ~16%-of-N centroid count.

- **Speed advantage at 90% recall@1 confirmed across multiple datasets and metrics**: Table 2 reports 1.2–2.3× speedup on all four datasets. Figure 3 extends this to full recall-latency curves for both recall@1 and recall@10, consistently showing DiskHIVF as the Pareto-dominant curve.

- **Robustness where graph-based competitors fail**: Starling cannot process GIST (960 dimensions) because individual vertex sizes exceed the 4096-byte disk page limit (Section 1, confirmed missing from Table 2). DiskHIVF handles GIST at 6.9 MB and 10.058 ms — the only method to do so at competitive performance.

- **Disk-access optimization quantitatively effective**: Table 3 shows 3.8× reduction in disk accesses at L=5000 cells (1000.94 vs. 3769.18) from the merge-read strategy. Figure 4 confirms consistent recall-latency improvement from this strategy on SIFT1M.

- **Query-aware dynamic pruning provides latency reduction without recall loss**: Figure 5 on BIGANN shows pruning reduces latency at matched recall levels (e.g., ~18 ms vs. ~22 ms at recall 0.95), justified by the CDF analysis in Figure 2a showing 80% of queries require only 16 cells.

---

## Weaknesses

### Fatal
None.

### Major

- **Memory footprint unexplained — primary quantitative claim cannot be reconciled**: The paper's headline contribution is O(√N·d + N) memory complexity. For BIGANN (N=10⁹, d=128), with n≈7,906 and m≈1,265 per Section 4.2's documented hyperparameters, the theoretical memory is ~4.7 MB for (n+m) centers plus ~80 MB for ~10⁷ disk pointers — approximately 85 MB total. Table 2 reports 1,213 MB — a 14× discrepancy with no accounting in the paper. Section 4.4.1 simply states the memory numbers without explanation of what the additional ~1.1 GB comprises (e.g., prefetch buffers, OS metadata, cached inverted list headers). The memory savings relative to the ~32 GB baselines are still large and practically significant, but the theoretical framing O(√N·d + N) as written is misleading until this gap is explained. A reader cannot verify the paper's core quantitative claim.

- **Billion-scale latency comparison is confounded by memory ceiling**: Table 2 shows DiskANN at 32,768 MB, SPANN at 32,524 MB, and Starling at 32,425–32,625 MB for BIGANN and DEEP — all at or near the test machine's 32 GB limit ("the instance used for search tasks has a maximum memory limit of 32 GB," Section 4.2). The paper acknowledges this in Section 4.4.2 ("DiskANN and Starling...are affected to varying degrees under the 32GB memory constraint") but frames it as an advantage rather than a confound. Baselines operating at their memory ceiling may have degraded I/O performance from memory pressure. The SIFT1M and GIST results (baselines at 30–1,207 MB, well within limits) are the cleanest comparisons; the billion-scale latency advantage is suggestive but not fully controlled.

### Minor

- **Figure 4 ablation has duplicate labels**: The parsed figure description confirms three series but both non-baseline lines are labeled "DiskHIVF w/o Merge-Read." Based on Section 4.5's text, the third series should isolate the centroid reordering contribution. The duplicate label makes it impossible to determine the individual contribution of merge-read vs. centroid reordering from the figure.

- **Writing error in Section 4.4.1**: The text states "our method shows a latency 1.2 to 2.3 times higher than existing methods." This is directly inverted — Table 2 and all of Section 4.4.2 establish DiskHIVF as 1.2–2.3× *faster*, not slower.

- **Inconsistent system name (DiskHIVF vs. DiskHIVE)**: The title, abstract, tables, and conclusion use "DiskHIVF"; Sections 3–4 use "DiskHIVE" (e.g., "we propose DiskHIVE" in Section 3 intro, "In DiskHIVE, we used the same default hyperparameter configuration" in Section 4.2). The paper appears assembled from two divergent drafts.

- **Dynamic pruning polynomial fitting protocol ambiguous**: Section 3.5 derives polynomial coefficients from "the 99th query coverage curve" (Figure 2b shows this on SIFT1M). Section 4.2 states "we used the same default hyperparameter configuration method across all four datasets," but it is unclear whether the polynomial is refit per dataset using that dataset's query distribution or whether the SIFT1M-fit polynomial is transferred to BIGANN/DEEP. If the former, this is test-time dataset adaptation requiring explicit documentation; if the latter, cross-dataset generalization should be demonstrated.

### Trivial
None.

---

## Nice-to-Haves
- Direct per-query I/O analysis (bytes read, sequential vs. random ratio) comparing DiskHIVF against DiskANN/SPANN at matched recall: would clarify whether the speedup stems primarily from reduced memory footprint (less thrashing) or from the sequential merge-read pattern.
- QPS throughput numbers for concurrent queries, since production deployments typically optimize throughput rather than single-query latency.
- Experimental comparison with GNO-IMI (Babenko & Lempitsky, 2016), whose two-level codebook structure is the structural precursor. The paper explains it differs by using full-precision disk-resident vectors, but a direct comparison or clear quantitative separation of contributions over GNO-IMI would strengthen the positioning.
- For billion-scale, add a memory-controlled comparison where DiskANN/Starling are given a matched ~1–2 GB memory budget, to isolate algorithmic difference from memory-ceiling effects.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Equation (3) is incorrect (Harsh Critic)**: REMOVED — factually wrong criticism. The harsh critic claimed the expansion ‖p − (S_k + T_i)‖² = ‖p − S_k‖² − 2pT_i + (T_i² + 2S_kT_i) omits -2p·S_k. However, ‖p − S_k‖² = ‖p‖² − 2p·S_k + ‖S_k‖², so the term is captured. Verified: the full expansion is ‖p‖² − 2p·S_k − 2p·T_i + ‖S_k‖² + 2S_k·T_i + ‖T_i‖² = ‖p−S_k‖² + (−2p·T_i + 2S_k·T_i + ‖T_i‖²), exactly matching Equation (3). The equation is correct.

- **Algorithm 2 originality not acknowledged (Harsh Critic, minor)**: REMOVED — the paper says "simple yet effective," a modest claim. Section 3.3 cites multiple prior IVF works with similar reordering. The paper does not overclaim this as a novel invention.

- **GNO-IMI distinctiveness understated / missing comparison (Harsh Critic, major → Nice-to-Have)**: DEMOTED to Nice-to-Have. GNO-IMI is an in-memory method; direct adaptation to a disk-resident context is non-trivial. The paper cites and acknowledges it as a precursor, which is sufficient. Not having an explicit GNO-IMI baseline is a missed opportunity, not a fatal gap.

---

## Novel Insights
The paper's most interesting finding — that DiskHIVF is *simultaneously* lower memory AND faster than graph-based methods — is counter-intuitive. One might expect a memory/speed tradeoff. The underlying mechanism (sequential disk access from centroid reordering enabling large merged reads, vs. random page-level access in graph traversal) is hinted at in Section 3.4 and supported by Table 3, but not explicitly analyzed as the root cause. This observation — that IVF-style sequential access can dominate graph-based random access at billion scale, even before accounting for memory ceiling effects — is a reusable design principle for disk-resident retrieval systems that extends beyond this specific contribution.

---

## Suggestions
1. Add a memory breakdown table for BIGANN/DEEP showing exactly what comprises the reported 1,213 MB (centers, pointers, buffers, OS overhead) and revise the theoretical complexity statement to either include or exclude each component explicitly.
2. Fix Figure 4's legend to give unique names to all three ablation series, enabling readers to isolate merge-read and centroid reordering contributions separately.
3. Standardize the system name to "DiskHIVF" throughout the paper (currently mixed with "DiskHIVE" in multiple sections).
4. Correct the writing inversion in Section 4.4.1: "latency 1.2 to 2.3 times *higher*" → "latency 1.2 to 2.3 times *lower*."
5. State explicitly whether the polynomial pruning coefficients are fit once on SIFT1M and reused, or refit on each dataset's observed query distribution.
6. Add a memory-controlled experiment for billion-scale baselines (e.g., DiskANN capped at 2 GB) to cleanly separate memory-ceiling effects from algorithmic gains.

---

## Score and Decision

**Anchor comparison summary:**

| Paper | Avg Score | Round | Comparison to DiskHIVF |
|---|---|---|---|
| 4Hf5pbk74h.md | 2.33 | R1 | Much weaker — unrelated topic, no clear contribution |
| NYPJz0CL5X.md | 3.00 | R1 | Weaker — HDC encoding, incremental improvement |
| ySJSGZxN7M.md | 3.67 | R1 | Weaker — HNSW variant, limited evaluation |
| iQtz3UJGRz.md | 4.00 | R1 | Weaker — bi-metric NNS, contrived setup |
| a2eBgp4sjH.md | 4.25 | R1 | Weaker — multi-filter graph ANN, less evaluation breadth |
| KmdwGYbMv0.md | 4.50 | R2 | Somewhat weaker — binary hyperbolic embeddings, narrower scope |
| wtNxByjLW3.md | 4.80 | R2 | Slightly weaker — ARDG for MIPS, comparable breadth but DiskHIVF has more dramatic improvements |
| oRNus243R6.md | 5.67 | R1/R2 | Comparable — diverse graph-based NNS with theory; DiskHIVF has better experiments, but the memory gap is a real weakness |
| ESq3U7z6FD.md | 6.00 | R2 | Slightly stronger — EHI hierarchical index; more ambitious but has fairness concerns; DiskHIVF has the memory discrepancy issue |

**Round 1 bracket**: 4.0–6.5

**Round 2 narrowing**: DiskHIVF sits between wtNxByjLW3.md (4.80) and ESq3U7z6FD.md (6.00). The memory discrepancy is a genuine major issue that places it below the 6.0 anchor but above the 4.80 anchor due to broader evaluation and cleaner deployment motivation. The paper is closer to the lower end of this sub-bracket given the primary quantitative claim cannot be reconciled with reported numbers without additional explanation. Final score: **5.0**.

**Axes summary:**
- *Originality*: Moderate — builds directly on GNO-IMI's two-codebook structure with practical disk-resident adaptations; centroid reordering and dynamic pruning are incremental.
- *Research question importance*: High — disk-resident billion-scale ANNS is a practically important and active area.
- *Claim support*: Mixed — SIFT1M and GIST results are clean and credible; billion-scale results are confounded; the primary memory complexity claim cannot be reconciled with reported numbers.
- *Experimental soundness*: Moderate — four datasets including billion-scale is good; but memory confound, missing ablation label, and unexplained memory discrepancy reduce confidence.
- *Writing clarity*: Below average — naming inconsistency, inverted comparison sentence, and duplicate ablation label are concrete quality issues.
- *Value to research community*: Moderate to good — a working system with public code and genuine memory savings, but the memory accounting needs to be fixed for practitioners to trust the theoretical framing.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>