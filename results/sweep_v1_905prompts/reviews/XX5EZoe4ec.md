Here is my consolidated review.

---

## Summary

RetrievalFormer proposes a dual-encoder transformer for sequential recommendation: a transformer-based user tower and a feature-based item tower, trained via contrastive loss so that dot-product similarity in the shared embedding space enables ANN retrieval and zero-shot cold-item scoring. The key ideas are (1) replacing the expensive softmax over all item IDs with ANN search over learned embeddings, (2) an attention-based fusion mechanism for heterogeneous features, and (3) shared embedding tables across towers. On Amazon and MovieLens benchmarks, the model achieves competitive accuracy (86–91% of transformer baselines on Amazon datasets) while the ANN index delivers a 288× speedup at 10M items.

---

## Strengths

- **Competitive accuracy with a retrieval-native architecture.** On Amazon Beauty, RetrievalFormer achieves Recall@20 of 0.1208 (exceeding SASRec at 0.1107 and reaching 91.2% of AttrFormer). On MovieLens-1M, it achieves 0.337 (96.8% of SASRec). These results demonstrate that a dual-encoder formulation with contrastive training can approach transformer-level accuracy while eliminating the costly softmax bottleneck.

- **Clear efficiency demonstration.** Figure 2 provides systematic latency benchmarks across catalog sizes from 10K to 10M, showing IVF-PQ maintaining sub-linear growth (1.02ms at 10M) vs. exhaustive scoring's linear growth (292ms). The 288× speedup is concretely measured with well-specified ANN parameters (nlist=4096, nprobe=32, PQ codes).

- **Well-designed cold-start evaluation protocol.** The LOOC protocol (Section 4.4.1) ensures zero item-ID leakage between training and test, and explicitly identifies that ID-softmax baselines cannot score unseen items. The protocol design (seed users → cold-item expansion) is clearly described and provides evaluation sets of meaningful size (1,542–4,681 users).

- **AttentionFusion ablation validated.** The ablation on Amazon Toys shows self-attention fusion improves Recall@20 from 0.0960 to 0.1057 (+10.1%) over mean pooling, providing concrete evidence that the proposed heterogeneous feature encoder adds value beyond simpler aggregation.

- **Shared embedding design motivated and tested.** Parameter sharing across towers improves Recall@20 by ~3% on MovieLens-1M and reduces parameters by ~3×, which is a clean, principled design choice with empirical support.

---

## Weaknesses

### Major

1. **Cold-start evaluation on public datasets lacks a comparative baseline.** Table 2 reports only RetrievalFormer's LOOC numbers (Recall@20 of 0.080–0.227) without any baseline for context. The paper mentions (Section 4.1) a "Content-based KNN approach" but its results do not appear on the public datasets. The only content-based comparison is on a proprietary email dataset (Appendix G). Without a baseline — even a simple one such as nearest-neighbor retrieval over mean item-feature vectors, or a content-based matrix factorization — the reader cannot assess whether RetrievalFormer's sequential modeling actually improves over straightforward feature-based alternatives for cold-start recommendation on these benchmarks.

2. **Ambiguity about the accuracy-evaluation regime.** The paper never explicitly states whether the RQ1 accuracy numbers (Table 1) are computed via exact dot-product scoring over all items or via ANN search. The text at line 183 confuses the issue further: "the performance gap stems from replacing the exact softmax scoring over all items with approximate nearest neighbor search in the learned embedding space." This conflates two distinct sources of accuracy loss — (a) the dual-encoder paradigm (dot-product vs. softmax) and (b) ANN approximation — and implies Table 1 results were obtained via ANN, which would be unusual for a standard benchmark comparison. The paper should clearly separate these: state that RQ1 uses exact scoring, and treat ANN accuracy as a separate measurement (or add that measurement). Without this clarity, the central claim about the accuracy-efficiency trade-off is not precisely supported.

### Minor

3. **Selective framing of the "86–91%" range.** The abstract and conclusion claim "86–91% of the Recall@20 of strong transformer-based sequential baselines." On MovieLens-1M, RetrievalFormer achieves 81.6% of AttrFormer (0.337 vs. 0.4128), which falls outside this range. The paper addresses this in the body by calling AttrFormer's result "a notable outlier" relative to the "established baseline cluster" of 0.34–0.36, but this nuance is absent from the abstract and conclusion. The honest range including all comparisons is 81.6%–100%+.

4. **Variance not reported for RetrievalFormer's own results.** Table 1 states that baseline results "are from Liu et al. (2025), averaged over five runs with std. < 0.001 not reported," but RetrievalFormer's own variance is not reported. Given that some gaps between models are small (e.g., on Toys: 0.1169 vs. MT4SR's 0.1148), this matters.

5. **Architectural ablations on a single dataset only.** The ablation for attention fusion and shared embeddings is conducted solely on Amazon Toys & Games (Section 4.3.1). Replicating these ablations on at least one more dataset (e.g., MovieLens-1M) would help establish generality.

6. **ANN recall not clearly specified.** Figure 2 labels the IVF-PQ latency as "≥0.95" but does not clearly define whether this refers to ANN recall (fraction of exact top-K hits retrieved), overall Recall@20, or another quantity. Without this, the reader cannot assess the accuracy trade-off at the reported latency.

### Trivial

7. The item tower uses self-attention fusion + DNN, not a full transformer. Calling the overall architecture "transformer-based" is slightly imprecise (the user tower is a transformer; the item tower is not), though the meaning is clear from context.

---

## Nice-to-Haves

- Report retrieval accuracy under ANN at various nprobe settings, showing an accuracy-recall curve to directly validate the claimed trade-off.
- Include a simple content-based baseline on the public LOOC datasets (e.g., KNN over mean item-feature vectors per user). This would substantially strengthen the cold-start evaluation.
- Replicate the architectural ablation on MovieLens-1M in addition to Amazon Toys.
- Report standard deviations for RetrievalFormer's results in Tables 1 and 2.
- Clarify what "≥0.95" means in the Figure 2 caption.

---

## Removed Points

The following points from the reviewers are removed for the stated reasons:

- **"The accuracy–efficiency trade-off is never actually measured" (framed as structural flaw/fatal):** The paper separately measures accuracy (exact scoring) and efficiency (ANN). The two claims — "competitive accuracy" and "enables 288× speedup" — are independently established. While the paper would benefit from showing accuracy under ANN, failing to do so does not invalidate either claim on its own. The reviewer conflated a clarity issue with a structural flaw. **Demoted from Fatal to Major issue #2 above (clarity gap, not fatal).**

- **"Two-tower retrieval models are well established, novelty overclaimed":** The paper explicitly cites Covington et al., Yi et al., and other two-tower recommenders in the related work, and positions its contribution as applying this paradigm to *sequential* recommendation with attention fusion and shared embeddings. This is adequate contextualization for a conference paper.

- **"The item tower is not a transformer" (naming issue):** This is acknowledged as a minor imprecision, retained as Trivial #7. The paper calls the overall architecture "transformer-based," which is accurate since the user tower is a transformer.

- **Various missing-hyperparameter / missing-appendix complaints:** The main text references Appendix J for full hyperparameters. The appendix is stripped by the parser; these details exist in the original submission.

- **Strength Finder claimed "86–91% of strong transformer baselines while enabling 288× speedup directly validates the claimed trade-off":** This conflates two separate measurements. Retained as a description of the paper's results but the caveat (accuracy vs. accuracy-under-ANN) is addressed in weakness #2.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the architecture or evaluation that the authors themselves do not already acknowledge.

---

## Suggestions

1. **In the experiments section, explicitly state how Table 1 accuracy is computed** (exact dot-product over all items vs. ANN). Add a sentence at the start of RQ1: "Unless otherwise noted, all accuracy results are obtained via exact dot-product scoring over the full item catalog."

2. **Add a content-based baseline to the LOOC evaluation on public datasets.** A simple baseline (e.g., compute each user's profile as the mean of their historical items' feature embeddings, then retrieve via dot-product) would contextualize the RetrievalFormer cold-start results and make the contribution clearer.

3. **Report variance** for all RetrievalFormer experimental results, especially where gaps to baselines are small.

4. **Clarify the "≥0.95" notation** in Figure 2: state explicitly that this is the ANN recall (fraction of exact top-K retrieved) and report accuracy under ANN at this setting.

5. **Adjust the abstract/conclusion framing** to reflect that the 86–91% range applies to Amazon datasets specifically, and note the wider range when including all comparisons.

---

## Score and Decision

### Calibration Anchors

**Round 1 (bracketing):**
- Low band (<3.5): QCR (3.0), Prompt2Rec (3.2), Diffusion + SNN (3.0) — These papers have fundamental evaluation or novelty issues that make them clearly weaker than RetrievalFormer.
- Middle band (3.5–7.5): EHI (6.0), Relevance-based Embeddings (5.75, 4.80) — Closest topical matches. EHI has a more novel methodological contribution (end-to-end index learning) but similar evaluation quality. Relevance-based Embeddings has theoretical grounding but weaker practical evaluation.
- High band (>7.5): Compositional Entailment Learning (8.0), Restructuring VQ (8.0) — These are top-tier papers on different topics and are clearly stronger.

**Round 1 bracket:** 4.5–6.0

**Round 2 (narrowing within bracket):**
- Lower mid (4.5–6.0): Language Models as Semantic Indexers (5.50), AdaRec (5.00), Long-Sequence Decoupled Embeddings (5.50), Relevance-based Embeddings (4.80)
- Upper mid (5.5–7.5): Non-Contrastive Learning for SR (6.50), EHI (6.00), Making Transformer Decoders Better Indexers (6.00)

**Comparison to anchors:** RetrievalFormer is comparable to Language Models as Semantic Indexers (5.50) and better-executed than Relevance-based Embeddings (4.80) while being less methodologically novel than EHI (6.00). Its evaluation is more thorough than many papers at the 5.0 level, but the missing cold-start baseline and ambiguity about the evaluation regime prevent it from reaching the 5.5–6.0 range.

**Final score:** 5.0

---

The paper presents a well-motivated architecture with solid engineering choices, competitive accuracy, and clear efficiency gains. However, two issues prevent a higher score: (1) the cold-start evaluation on public datasets lacks any comparative baseline, so the practical value of the sequential modeling for cold-start is uncalibrated; (2) the paper is ambiguous about whether its accuracy numbers reflect exact scoring or ANN search, making the central accuracy-efficiency claim less precise than it should be. These are addressable in revision but weaken the current submission.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>