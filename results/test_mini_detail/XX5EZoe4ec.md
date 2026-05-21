Now I have strong calibration. My round-1 bracket placed this paper between ~4.5 and ~7. The most topically similar anchors (ContextGNN at 5.8, SLMRec at 6.25, DARE at 5.5) all sit in the 5.5–6.25 range. The paper has clearer novelty than ContextGNN and DARE, comparable to SLMRec, but has evaluation weaknesses that the best papers in this band don't. The paper is stronger than the withdrawn Semantic Rep paper (5.0). I set the score at **6.0**.

Now writing the final consolidated review.

---

## Summary

This paper proposes RetrievalFormer, a dual-encoder architecture that replaces the ID-softmax output layer of transformer-based sequential recommenders with a feature-based item tower and Approximate Nearest Neighbor (ANN) retrieval. The user tower is a transformer that processes enriched interaction sequences, while the item tower encodes items from their metadata attributes. Shared embedding tables and an AttentionFusion module (self-attention over heterogeneous feature sets) unify the representation space. Training uses InfoNCE contrastive loss with mixed negative sampling. At serving time, user embeddings query a pre-built ANN index over item embeddings, avoiding the O(N) softmax bottleneck. Experiments on Amazon Beauty, Amazon Toys & Games, and MovieLens-1M show RetrievalFormer achieves 86–97% of the Recall@20 of strong transformer baselines while reporting up to 288× latency reduction at 10M items via ANN, and it can score completely unseen items (cold-start) where ID-softmax models cannot.

## Strengths

1. **Well-motivated architectural contribution — replacing ID-softmax with a feature-based dual-encoder is a genuine design innovation.** Transformer sequential recommenders rely on an O(Nd) output softmax over item IDs, which prevents ANN acceleration and blocks cold-start scoring. RetrievalFormer replaces this with a two-tower architecture that produces a shared embedding space trainable with contrastive loss. This is an explicit design choice (not just an engineering trick) and is validated by ablations: Table 1 shows 0.337 Recall@20 on MovieLens-1M vs. SASRec's 0.3483 (96.8%), confirming that the reformulation does not catastrophically lose accuracy.

2. **AttentionFusion consistently outperforms simpler feature aggregation.** The ablation on Amazon Toys (Section 4.3.1) shows self-attention fusion improves Recall@20 from 0.0960 to 0.1057 (+10.1%) over mean pooling. The paper also demonstrates contributions from shared embeddings (+3% on ML-1M) and the implicit uniformity effect of InfoNCE (+4.1%). These ablations are concrete and attribute-specific, not generic.

3. **Cold-start capability is demonstrated under a properly constructed no-leakage protocol.** The LOOC protocol (Section 4.4.1) ensures test items have zero interactions during training, with a principled seed-user expansion. Under this protocol, RetrievalFormer achieves meaningful Recall@20 (e.g., 0.2267 on ML-1M, Table 2), whereas ID-softmax baselines (SASRec, BERT4Rec, AttrFormer) cannot score such items at all. On a production email campaign dataset (Appendix G reported in text), it outperforms a content-based baseline (AUC 0.7770 vs. 0.6854). This provides direct evidence for the cold-start capability claimed in the introduction.

4. **Shared embedding design is a practical contribution with measurable benefits.** Section 3.2.2 describes how sharing embedding tables across user and item towers reduces parameters by ~3× while improving alignment. The ablation showing a ~3% Recall@20 improvement confirms this goes beyond simple weight tying.

## Weaknesses

### Fatal
None.

### Major

- **Baseline results are adopted from the AttrFormer paper (Liu et al. 2025) without re-implementation.** The paper states (Section 4.1, Table 1 caption) that all baseline numbers come from Liu et al. (2025). This is transparent but creates a significant methodological concern: AttrFormer's Recall@20 of 0.4128 on MovieLens-1M is ~15% higher than the next-best baseline (LightSANs at 0.3590), strongly suggesting differences in evaluation protocol or candidate sampling rather than genuine model superiority. Without re-running the baselines in a shared codebase, it is impossible to tell whether RetrievalFormer's relative accuracy (e.g., 96.8% of SASRec) is a stable property or an artifact of different preprocessing or metric computation. This weakens the core accuracy claim. The paper does acknowledge AttrFormer as an outlier, but the underlying issue remains unresolved.

- **The 288× efficiency claim mixes measurements from different hardware and implementations.** Figure 2 and the surrounding text compare RetrievalFormer's own IVF-PQ latency (measured on their hardware) against SASRec latency from the ETUDE benchmark (Kersbergen et al. 2024), which uses different hardware, framework, and implementation. The abstract and introduction state "up to 288× lower latency at a 10M-item scale via ANN retrieval" without clarifying that the comparison crosses systems. While the paper does label the SASRec points "(ETUDE)" in Figure 2, the headline claim would be far stronger if it compared exhaustive dot-product scoring and ANN scoring for RetrievalFormer's *own* embeddings on the *same* hardware — isolating the speedup from switching to ANN. The paper notes it measured exhaustive scoring but does not report those numbers in the main comparison table alongside the ETUDE numbers.

- **The cold-start evaluation on public benchmarks lacks a directly comparable baseline in the main paper.** While the paper states it compares against a Content-based KNN approach (Section 4.1), Table 2 shows only RetrievalFormer results under LOOC with no baseline contrast. A content-based KNN (or simple two-tower without the transformer user encoder) on the same LOOC splits would quantify how much the transformer sequence modeling contributes beyond feature-based retrieval. The email-dataset comparison (Appendix G) helps but is not reproducible.

### Minor

- **The "uniformity loss" ablation is uninterpretable without specifying what the alternative is.** Section 4.3.1 reports "Enabling implicit uniformity through InfoNCE provides consistent improvements (Recall@20: 0.1022 → 0.1064, +4.1%)." Since InfoNCE is the *main* training loss, the comparison must contrast two training objectives (e.g., InfoNCE vs. a margin-based ranking loss, or InfoNCE with vs. without MNS). The paper does not specify what "without uniformity" means, making it impossible to tell what was actually ablated.

- **The LOOC seed-user selection criteria are underspecified.** Section 4.4.1 states "select 500 seed users whose final items define the initial cold set" but does not describe how these 500 users are chosen (random? by activity level?). Selection bias could affect representativeness. Statistics on cold-item feature coverage and how users were selected would improve reproducibility.

### Trivial

- **Figure 2 caption describes SASRec scaling as "linear on the log-log plot,"** which is technically power-law scaling, not linear. Minor wording issue.

## Nice-to-Haves
- Re-run the three most important baselines (SASRec, BERT4Rec, AttrFormer) in the same codebase and report variance across splits.
- Include a non-transformer feature-based baseline (e.g., mean-pooled item features + shallow neural retriever) in the main LOOC table to contextualize cold-start performance.
- Add a controlled efficiency experiment: exhaustive dot-product vs. ANN for *RetrievalFormer's own embeddings* on the same hardware, reported alongside the ETUDE reference numbers.

## Removed Points

These points are flagged to be removed; treat them with caution.

| Removed Point | Reason |
|---|---|
| "Equation (1) clarity on multi-source feature combination" — reviewer asked how text tokens and categorical features are combined | The paper clearly states (line 91) that single-valued features produce one embedding, multi-valued features aggregate via mean pooling or attention, and all feature embeddings form a set processed by AttentionFusion. Not a real gap. |
| "Profile token fusion unclear" — reviewer asked how profile tokens are fused with interaction tokens | Section 3.4.2 explicitly says $\mathbf{p}_u = \text{AttentionFusion}(\text{UserFeatures})$ and the sequence is $[\mathbf{z}_1, \dots, \mathbf{z}_T, [\text{SEP}], \mathbf{p}_u, [\text{CLS}]]$. Sufficiently clear. |
| "Hyperparameter details not in main text" — reviewer wanted transformer depth/hidden size per dataset | The paper says "we use the same number of transformer layers and hidden dimension as in the corresponding transformer baselines" and defers full details to Appendix J. Appendices are stripped by the parser; the details exist in the original submission. |
| "Many baselines not cited/described" — reviewer complained about missing citations for DuoRec, CLASRec, etc. | These are established baselines in the sequential recommendation literature (cited through Liu et al. 2025). The paper's scope does not require describing a dozen baselines individually. |
| "Conclusion states 86-91% but not precisely supported" — reviewer claimed the range is imprecise | The 86-91% range is approximately correct: vs AttrFormer on Beauty (91.2%), Toys (86.1%), ML-1M (81.7% — outside range vs AttrFormer, but vs SASRec the paper achieves 96.8%). The range is a reasonable summary. |
| Harsh critic's "Strengthening the Paper on Its Own Terms" section | Already covered by the Major weaknesses and Nice-to-Haves above; no need to list separately. |

## Novel Insights

The two reviews offer contrasting perspectives: the harsh critic correctly identifies the uncontrolled baseline and efficiency comparisons as structural weaknesses, while the strength finder highlights the genuine architectural novelty and the soundness of the cold-start protocol. The most interesting tension is around the cold-start evaluation. The harsh critic asserts that no meaningful baseline exists on public benchmarks, but the paper *does* mention a content-based KNN baseline (Section 4.1) and provides comparison on the email dataset (Appendix G). However, the main paper indeed omits KNN results from the LOOC table, which is a genuine presentation gap. Neither reviewer noticed that the paper actually measures its own exhaustive scoring (mentioned in passing in Section 4.5) but does not plot it alongside the ANN curves — the efficiency weakness could be partially addressed by presenting that within-system comparison more prominently rather than relying on ETUDE numbers.

## Suggestions

1. **Re-run the key baselines (SASRec, BERT4Rec, AttrFormer) in your own codebase.** This single change would resolve the most serious weakness. Even if AttrFormer remains an outlier, at least you would know the gap is real rather than a protocol artifact.

2. **Add a controlled efficiency experiment:** measure exhaustive dot-product scoring and IVF-PQ for *your own model's embeddings* on the same GPU, and present this as the primary efficiency comparison. Keep the ETUDE reference as a secondary anchor but do not base the headline speedup number on it.

3. **Define what "without uniformity" means in the ablation.** If it means removing MNS (mixed negative sampling) or switching from InfoNCE to a pairwise ranking loss, say so explicitly.

4. **Add a non-transformer cold-start baseline to the main LOOC table** (e.g., Content-KNN or a simple dot-product of mean-pooled item features). This would help readers assess whether the transformer user encoder adds value beyond pure feature-based retrieval.

5. **Clarify how the 500 seed users are selected** in the LOOC protocol and report summary statistics on cold-item feature coverage.

## Score and Decision

**Calibration Anchors (all rounds):**

| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| ContextGNN | nzOD1we8Z4.md | 5.8 | R1/R2 | Two-tower rec paper, accepted poster. Had novelty/baseline concerns. RetrievalFormer has clearer novelty and comparable evaluation rigor. **Slightly stronger.** |
| EHI | ESq3U7z6FD.md | 6.0 | R1 | End-to-end indexing. Rejected (missing related work). RetrievalFormer has better topic fit and no missing-RW issue. **Comparable quality, but accepted vs. rejected outcome difference is due to different issues.** |
| Adaptive Retrieval | 1CPta0bfN2.md | 6.25 | R1/R2 | k-NN search with cross-encoders. Accepted poster, thorough evaluation. RetrievalFormer has comparable contribution but weaker evaluation control. **Slightly weaker.** |
| SLMRec | G4wARwjF8M.md | 6.25 | R2 | LLM distillation for sequential rec. Accepted poster, solid experiments. RetrievalFormer has clearer architectural novelty. **Comparable.** |
| DARE / Long-Seq | jkpGIxSsUD.md | 5.5 | R2 | Decoupled embeddings for long-seq rec. Accepted poster with mixed reviews. RetrievalFormer has stronger novelty. **Stronger.** |
| Semantic Rep (MoC) | medKq3cONT.md | 5.0 | R2 | Semantic IDs for recommendation. Withdrawn/rejected due to weak experiments. RetrievalFormer has far stronger evidence. **Stronger.** |

**Round 1 bracket:** 4.5–7.5 (confirmed by middle-band anchors around 5.5–6.25).  
**Round 2 narrowing:** Compared against the most topically similar anchors (SLMRec at 6.25, DARE at 5.5, ContextGNN at 5.8) and assessed the paper's relative position. The paper sits firmly in the 5.5–6.25 range: clearer novelty than ContextGNN and DARE, comparable to SLMRec, but weighed down by the uncontrolled baseline/efficiency comparisons. **Final score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>