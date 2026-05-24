Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes RetrievalFormer, a dual-encoder transformer architecture for sequential recommendation that replaces the standard ID-softmax output layer with feature-based item and user embeddings trained via contrastive learning (InfoNCE). This reformulation enables two key benefits: (1) efficient ANN-based retrieval at serving time (up to 288× speedup at 10M items vs exhaustive softmax scoring), and (2) zero-shot scoring of unseen items during cold-start. The architecture introduces AttentionFusion—a self-attention mechanism over heterogeneous item/user features—with shared embedding tables across towers. Experiments on Amazon Beauty, Amazon Toys, MovieLens-1M, and a production email dataset show competitive accuracy against transformer baselines while enabling dramatic efficiency gains and meaningful cold-start recommendation.

## Strengths

1. **Compelling efficiency-accuracy trade-off supported by direct measurement.** Table 1 and Figure 2 jointly demonstrate that RetrievalFormer achieves 96.7% of SASRec's Recall@20 (0.337 vs 0.3483) on MovieLens-1M and 91.2% of AttrFormer on Amazon Beauty (0.1208 vs 0.1324), while delivering a 288× speedup (1.02ms vs 292ms at 10M items) via IVF-PQ ANN search. The latency benchmarking is well-controlled (FAISS IVF-PQ with specified parameters, same ml.g6.xlarge instance, batch size 1024, warm-up phase), and the scaling curves (Figure 2) cleanly demonstrate the shift from O(N) to sub-linear scaling.

2. **Zero-shot cold-start recommendation demonstrated under a rigorous protocol.** The LOOC protocol (Section 4.4.1) is a principled evaluation design: it selects cold items by ensuring their IDs never appear during training and expands the evaluation set to maximize statistical power. Table 2 shows RetrievalFormer achieves meaningful Recall@20 (0.0804–0.2267) on completely unseen items across all three datasets, while ID-softmax baselines (SASRec, BERT4Rec, AttrFormer) cannot score these items at all. The production email dataset validation (AUC 0.6854→0.7770, +13.4% relative) provides additional external evidence.

3. **AttentionFusion ablation clearly demonstrates architectural benefit.** Section 4.3.1 shows that replacing self-attention fusion with mean pooling reduces Recall@20 by 10.1% (0.0960→0.1057) on Amazon Toys, and shared embedding tables contribute an additional ~3% on MovieLens-1M. These ablations isolate the contribution of the specific design choices beyond a simple dual-encoder.

4. **Well-motivated problem framing.** The paper clearly identifies the two concrete pain points of ID-softmax transformers (O(N) inference cost, inability to score unseen items) and shows how a dual-encoder reformulation addresses both simultaneously, which is a clean and practical contribution.

## Weaknesses

### Fatal
None.

### Major

1. **Cold-start evaluation lacks comparison to alternative feature-based methods.** The LOOC protocol (Table 2) only compares RetrievalFormer with itself under standard LOO vs LOOC. While ID-softmax baselines cannot score unseen items, there exist well-known feature-based methods (e.g., LightFM, VAE-CF with features, DropoutNet, or a simple two-tower MLP using the same item features) that *can* handle cold-start items. Without such comparisons, it is impossible to determine whether the observed cold-start capability comes from the specific architecture (AttentionFusion, transformer user tower) or simply from using item features—a decades-old technique. The paper acknowledges this framing ("capability diagnostic," Section 4.4.2), but the absence of even a simple dual-encoder MLP baseline makes it difficult to assess the value added by the architecture. The production email dataset comparison against a content-based KNN (Appendix G) is a step in this direction but is insufficient as the sole comparison, and its details are in the stripped appendix.

### Minor

2. **Selective framing of the "86–91%" accuracy claim.** The abstract states RetrievalFormer "reach[es] 86–91% of the Recall@20 of strong transformer-based sequential baselines." This range is computed relative to AttrFormer on the Amazon datasets (86.1% on Toys, 91.2% on Beauty). On MovieLens-1M, however, RetrievalFormer achieves only 81.6% of AttrFormer's recall; the paper instead compares to SASRec (96.8%) and characterizes AttrFormer as a "notable outlier" (Section 4.2). This explanation is not unreasonable—AttrFormer is 15% above the next-best method—but the abstract does not disclose the switch in reference point. All numbers are transparently reported in Table 1, so this is a presentation issue rather than a factual error, but it gives a more favorable impression than a uniform comparison would.

3. **Baseline results taken from Liu et al. (2025) without independent re-implementation.** The paper states it "adopt[s] the experimental protocol and baseline results from Liu et al. (2025) for fair comparison" (Section 4.1). While this is common practice, it introduces uncontrolled variables: dual-encoder models are sensitive to batch size, temperature, and negative sampling, whereas ID-softmax transformers are sensitive to learning rate and dropout. Without re-running baselines in the same codebase with controlled hyperparameter tuning, the reported accuracy differences cannot be fully attributed to architectural choice.

4. **ANN index recall (≥0.95) is annotated but never explained.** Figure 2 and the latency table denote the IVF-PQ curves as "IVF-PQ (ret only, ≥0.95)" and "IVF-PQ + encode (≥0.95)." The paper never defines what "≥0.95" refers to (presumably the fraction of true top-K nearest neighbors recovered by the index). Without this explanation, the reader cannot assess whether the 288× speedup comes at the cost of lost nearest-neighbor coverage, and whether any downstream recommendation accuracy drop is due to the dual-encoder formulation or the ANN approximation.

### Trivial

None.

## Nice-to-Haves

- The paper would benefit from reporting the ANN index recall@K explicitly (the overlap between exact nearest neighbors and ANN-retrieved neighbors) alongside the downstream recommendation metrics, to disentangle approximation loss from model architecture loss.
- Running SASRec (and ideally AttrFormer) in the same codebase with the same hyperparameter tuning budget would strengthen the accuracy comparison.
- Adding a simple dual-encoder MLP (or LightFM) as a cold-start baseline under LOOC would clarify whether the cold-start gains come from the architecture or from feature usage.

## Removed Points

- **Speculative evaluation metric sampling bias** (Harsh Critic's point about sampled vs. full-catalog ranking): The paper states it uses the same protocol as Liu et al. (2025), whose evaluation protocol is standard full-catalog ranking. The critic provides no evidence of a difference. Removed as speculative.
- **Missing appendix details / missing proofs / missing related works**: Per the instructions, appendix sections were stripped by the parser and exist in the original submission. Related works cannot be verified without external sources. Removed.
- **Overstated conclusions / "bridges the gap" phrasing**: Subjective opinion, not a specific, concrete weakness. Removed.
- **Typos, formatting nitpicks, reproducibility nitpicks about undisclosed hyperparameters**: Per-instruction removals. The paper provides hyperparameters (Section 4.1) and refers to Appendix J for further details.

## Novel Insights

**None beyond the paper's own contributions.** The reviews did not surface any observation about the paper that the paper itself does not already state or imply.

## Suggestions

1. **Add at least one feature-based cold-start baseline** (e.g., LightFM or a simple two-tower MLP with identical item features) under the LOOC protocol. This is the single most impactful improvement, as it would isolate the value of the architectural choices over feature usage alone.
2. **Clarify the "≥0.95" annotation** in Figure 2: define it explicitly as index recall@K and report the actual measured value, not just a threshold. Consider adding a table showing recommendation accuracy with and without ANN approximation.
3. **Re-frame the abstract's accuracy claim** to be transparent about reference points, e.g., "achieves 86–91% of AttrFormer's Recall@20 on Amazon datasets and 97% of SASRec's on MovieLens-1M."
4. **Report a parameter count comparison** to substantiate the "3× parameter reduction" claim from shared embeddings (Section 3.2.2).

## Score and Decision

The paper presents a clean architectural contribution (dual-encoder transformer with AttentionFusion for efficient ANN-based sequential recommendation) with strong efficiency evidence and a well-designed cold-start evaluation protocol. The main weakness—absence of feature-based cold-start baselines—limits but does not invalidate the core claims, which are well-supported otherwise. The accuracy comparison is slightly selectively framed but all data is transparently reported. Overall, the paper makes a genuine, practically-motivated contribution with solid empirical support.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>