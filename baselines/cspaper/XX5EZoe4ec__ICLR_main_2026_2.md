---
job_id: ed375a0e-6ee9-4112-9046-1cf4ed7549fc
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: XX5EZoe4ec.pdf
paper: RetrievalFormer: A Dual-Encoder Transformer for Efficient Approximate Nearest Neighbor Retrieval and Cold-Item Recommendation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, it studies representation learning and scalable neural recommendation via dual encoders, contrastive learning, transformer sequence modeling, and ANN retrieval.

## Minimum Quality
Pass ✅ The paper contains the expected core sections, namely Abstract, Introduction, Related Work, Methodology, Experiments with quantitative results, and Conclusion. While I have substantial concerns about novelty, empirical support, and several mathematical/experimental claims, these are review-level issues rather than desk-reject-level incompleteness or fatal integrity violations.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find hidden prompts, suspicious instructions to reviewers, or other signs of prompt injection/manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes RetrievalFormer, a dual-encoder recommender with a transformer user tower and a feature-based item tower, trained with an InfoNCE-style objective so that recommendation can be served via ANN retrieval instead of full-vocabulary softmax scoring. The method also uses an attention-based feature fusion module and shared feature embeddings across user and item towers. Experiments on Amazon and MovieLens benchmarks study recommendation accuracy, a cold-item protocol where held-out items are absent from training, and latency scaling with ANN indexes.

## Strengths
The paper targets a real and important systems-meets-modeling problem: bringing stronger sequential recommenders closer to production constraints, especially when catalog size is large and item churn is high. That problem matters, and the paper is at least aiming at a practically meaningful trade-off rather than only squeezing out another small benchmark gain.

The overall architecture is easy to understand. **Figure 1** is helpful in conveying the end-to-end pipeline, from heterogeneous feature encoding, to the transformer user tower, to precomputed item embeddings and ANN retrieval. In particular, the asymmetric-tower design and the role of shared embedding tables are visually clear, which makes the central modeling idea accessible.

The main empirical message in **Table 1** is reasonably straightforward: the method does not match the strongest reported transformer baselines, but it remains in the same rough ballpark on Recall@20 for some datasets while enabling retrieval-based serving. On Amazon Beauty, for example, RetrievalFormer reaches 0.1208 Recall@20, which is above SASRec’s 0.1107 and not too far from several feature-aware baselines. On MovieLens-1M, 0.337 Recall@20 is below several baselines, but still near the older baseline cluster around 0.35. I appreciate that the paper does not hide this trade-off.

The cold-item framing is also useful. The authors are correct that ID-softmax models cannot directly score unseen item IDs under the proposed cold protocol. Even though I have concerns about the way this evaluation is positioned, **Table 2** does make one thing explicit: the model can produce non-trivial rankings for held-out items constructed from metadata alone, and the drop from LOO to LOOC quantifies how hard that setting is.

The latency section communicates the intended systems benefit clearly. **Figure 2** effectively shows the scaling gap between exhaustive scoring and IVF-PQ retrieval on a log-latency axis; the qualitative message, namely near-linear growth for exhaustive scoring versus much slower growth for ANN search, is easy to grasp.

## Weaknesses
1. **The methodological novelty is limited, and the paper does not convincingly separate what is actually new from a fairly standard assembly of known parts.**  
   The core recipe is a two-tower retrieval model with a transformer user encoder, feature-based item encoder, dot-product scoring, contrastive training, and ANN serving. Each of these ingredients is individually standard in recommendation and retrieval systems, and the paper’s main novelty claim seems to rest on their combination plus attention-based feature fusion and shared embeddings. The problem is that the paper does not make a sharp case for why this combination constitutes a sufficiently distinct research contribution for ICLR rather than an engineering integration.  
   Section 2 mentions two-stage retrieval models, feature-enriched sequential recommenders, and ANN search, but the positioning remains too soft. For example, the claimed distinction from standard two-tower retrieval systems on **Page 3** is essentially that the user tower is stronger and more sequential. That may be true, but this is more incremental than the paper acknowledges. Similarly, attention over heterogeneous features is not a surprising leap given Set Transformer / AutoInt-style precedents already cited by the authors themselves. The paper would need a much sharper isolation of what specific ingredient is responsible for the claimed gains and why prior retrieval architectures could not already do something close.

2. **The central accuracy claim is weaker than the framing suggests, and the paper sometimes oversells “transformer-quality” performance.**  
   The abstract and conclusion repeatedly emphasize competitive accuracy with strong transformer baselines, but **Table 1** paints a more mixed picture. On Amazon Toys, RetrievalFormer’s Recall@20 is 0.1169, which is below LightSANs (0.1273), FEARec (0.1297), TiSASRec (0.1325), DIF-SR (0.1342), and AttuFormer (0.1357). On MovieLens-1M, RetrievalFormer’s NDCG@20 is 0.1390, which is materially below SASRec’s 0.1745 and well below AttrFormer’s 0.2088.  
   The paper tries to soften this by comparing against an “established baseline cluster” and calling AttrFormer an outlier on **Page 7**, but that is not a convincing scientific move. If a recent baseline is in the table and reported under the same protocol, then the paper needs to either match it, explain why it is not comparable, or tone down the broader claim. Right now the narrative selectively emphasizes percentages of SASRec performance while downplaying larger absolute ranking gaps, especially on NDCG. This matters because the paper’s selling point is a quality-efficiency trade-off, and the “quality” side should be characterized more soberly.

3. **The efficiency evidence is not apples-to-apples enough to support some of the stronger serving claims.**  
   The latency section on **Pages 9–10** compares exhaustive scoring against IVF-PQ ANN retrieval for “the same dual-encoder scoring function,” but the broader paper narrative frames this as overcoming the inference bottleneck of transformer baselines. That is not exactly what is shown. The benchmark seems to isolate the item-scoring stage and does not provide an end-to-end comparison that includes user encoding cost for RetrievalFormer versus a real sequential baseline under matched implementation conditions.  
   This distinction matters. A dual encoder can precompute item embeddings, yes, but the user tower is still a transformer. The latency numbers in **Figure 2** and the accompanying paragraph mainly demonstrate the obvious fact that ANN search is faster than exhaustive dot-product scan as \(N\) grows. They do not fully establish production superiority over strong baselines under the same hardware/software stack. The paper also states on **Page 10** that RetrievalFormer changes scaling “from \(O(N)\) to \(O(\log N)\),” which is too casual. ANN complexity depends on index family, implementation, probes, graph traversal, and accuracy targets. For IVF-PQ in practice, query time is not cleanly summarized as \(O(\log N)\). This matters because the asymptotic claim is stronger than the empirical evidence provided.

4. **The cold-start evaluation is framed as rigorous, but the experimental evidence is still too narrow to support the broader cold-item contribution.**  
   The authors are right that ID-softmax baselines cannot score unseen IDs under LOOC. However, that does not mean the cold-start evaluation is sufficiently convincing. In **Table 2**, the authors mostly compare RetrievalFormer against itself under LOO versus LOOC, which is informative as a stress test but not as a competitive evaluation. The paper mentions a content-based KNN baseline for cold-start in Section 4.1, yet no public-dataset cold-start comparison against that baseline is reported in the main paper.  
   This is a substantive issue, not a cosmetic one. The central claim is not merely “our model can produce a score,” but that it handles cold items effectively. For that, the relevant comparison set should include feature-based retrieval methods, content-based recommenders, and simpler metadata encoders. Without that, the cold-start story risks becoming a capability demo rather than evidence of superiority. The paper even acknowledges on **Page 9** that LOOC is used “as a capability diagnostic,” which is fair, but then the abstract and conclusion still use stronger language about successful cold-item recommendation. That mismatch weakens the contribution.

5. **Several key experimental details are underspecified in the main paper, making it hard to assess fairness and reproducibility from the core submission alone.**  
   The main text repeatedly defers important information to appendices, especially for the exact feature sets, negative sampling details, ANN settings, and ablations. For example, Section 4.1 says the Amazon and MovieLens setups use the same features and preprocessing as Liu et al. (2025), but the main paper never clearly lists what features are actually available on each dataset, how text-derived features are tokenized, how many tokens per item are used, or what user features exist on each benchmark.  
   This matters because RetrievalFormer’s value proposition depends heavily on side information. If the model is given richer metadata than some baselines, the comparison is not purely architectural. Conversely, if feature-poor settings are used, that should be explicit because it explains the cold-start limits. Right now the reader has to infer too much. For a paper built around heterogeneous features, the omission of a compact dataset-feature table in the main paper is a notable weakness.

6. **The treatment of the training objective is mathematically and algorithmically incomplete in the main paper.**  
   The core objective in **Equation (9)** is standard one-directional InfoNCE:
   \[
   \mathcal{L}_{\text{InfoNCE}}=-\frac{1}{B}\sum_{i=1}^{B}\log\frac{\exp(\mathbf{x}_{i}^{\top}\mathbf{y}_{i}/\tau)}{\sum_{j=1}^{B}\exp(\mathbf{x}_{i}^{\top}\mathbf{y}_{j}/\tau)}.
   \]
   But the paper then states that it employs Mixed Negative Sampling (MNS) by “augmenting each batch with uniformly sampled items from the catalog” on **Page 6**, without giving the actual objective used in the main text. Are the sampled negatives appended to the denominator of Equation (9)? Are they weighted? Are false negatives filtered? Is the denominator normalized differently when extra sampled negatives are used? These are not minor implementation details, they change the loss actually optimized.  
   There is also a direct inconsistency between the main text and the later ablation language. Section 4.3.1 discusses “Uniformity Loss: Enabled vs Disabled,” implying some additional explicit uniformity term, yet the main text in Section 3.5 says uniformity is obtained implicitly through InfoNCE. In the main paper, no explicit regularizer \(\lambda \mathcal{L}_{\text{uniform}}\) is ever defined. So what exactly is “enabled” in the ablation? If the comparison is actually “InfoNCE with vs without some extra regularization term,” that term should be stated formally in the main methodology. If not, the ablation wording is misleading.

7. **There are representation-level ambiguities and notation inconsistencies in the architecture description.**  
   In Section 3.2, **Equation (1)** defines
   \[
   \mathbf{H} = [ \mathbf{W}_1 \mathbf{E}_{f_1}(f_1); \dots ; \mathbf{W}_M \mathbf{E}_{f_M}(f_M)] \in \mathbb{R}^{M \times d},
   \]
   which suggests each feature contributes one vector. But the text on **Page 5** says multi-valued features and text features are themselves aggregated either by mean pooling or attention before entering AttentionFusion. That means the operator \(\mathbf{E}_{f_m}(f_m)\) is overloaded and can denote either a single embedding lookup or an already pooled set representation, depending on feature type. The paper should define this cleanly, otherwise Equation (1) hides non-trivial preprocessing.  
   Similarly, **Equation (7)** writes
   \[
   \mathbf{z}_t=\text{AttentionFusion}(\mathbf{h}_{i_t}\oplus\text{InteractionContext}(e_t)),
   \]
   where \(\oplus\) is said to denote feature concatenation. But AttentionFusion in Equations (2)–(4) is described as operating on a set or sequence of feature embeddings, not on one concatenated vector. Concatenation followed by self-attention is not the same as attention over a set of feature embeddings. This is not just notation pedantry, it obscures what the user tower token actually contains and how interaction context is fused with item metadata.

8. **The ablation evidence in the main paper is too thin relative to the number of claimed design insights.**  
   Section 4.3 summarizes several findings, but almost all detailed numbers are deferred. In the main paper, only a few isolated ablation statements are provided, and they are not enough to substantiate the claimed importance of attention fusion, shared embeddings, sequence construction choices, or context tokens.  
   The problem becomes visible when one compares the breadth of design claims in Section 3 with the narrowness of the evidence in Section 4.3. For example, shared embeddings are highlighted as a “critical design choice” in Section 3.2.2, yet the main paper gives only one brief statement that they improve Recall@20 by approximately 3% on MovieLens-1M, with no table in the main body. Likewise, the user-tower sequence design, [SEP]/[CLS] arrangement, and profile incorporation are central in **Figure 1**, but they are not meaningfully ablated in the main paper. At ICLR level, a paper making many architectural design claims should isolate them more rigorously.

9. **The paper’s discussion of figures is partly persuasive but also reveals untested assumptions.**  
   As noted above, **Figure 1** is visually useful, but it also highlights a concern: the architecture pushes a very rich feature-processing stack into both towers, including multiple fusion layers and shared embeddings. The paper attributes the final gains to the dual-encoder retrieval formulation, yet the figure suggests a large fraction of the improvement could come from simply using richer metadata and repeated feature conditioning. Without stronger controlled baselines, the figure almost works against the paper’s intended attribution.  
   **Figure 2** is also somewhat too convenient. It plots ANN retrieval against exhaustive scoring on a log scale and includes ETUDE reference lines, but it does not show the standard retrieval-quality trade-off, such as Recall@K of the ANN index versus exact top-\(K\), nor does it vary \(n_{\text{probe}}\) or index parameters. So the figure supports the “speed” half of the story while leaving the “without sacrificing recommendation quality” phrasing under-supported. For an ANN-based paper, the absence of an ANN recall-speed curve in the main paper is a noticeable gap.

10. **Some claims are stronger than what the paper actually establishes, especially around theory and scaling.**  
   The paper repeatedly invokes alignment/uniformity arguments and avoidance of representation collapse, but these are mostly motivational rather than demonstrated. In Section 3.5, the claim that the contrastive objective “helps to avoid representation collapse and makes the learned space more suitable for ANN retrieval” is plausible, but no main-paper metric or diagnostic is shown. Similarly, the sentence on **Page 4** that learning a shared embedding space via contrastive training lets the same representations support both training and ANN inference is true at a high level, but not yet evidence that the learned space is especially ANN-friendly.  
   More broadly, the paper sometimes slides from empirical observation into generic theoretical-sounding statements. The jump from observed latency curves to “changes scaling from \(O(N)\) to \(O(\log N)\)” is one example; the jump from InfoNCE usage to improved uniformity/anti-collapse behavior without direct evidence is another. These are not fatal flaws individually, but together they make the paper read as more certain than the actual evidence justifies.

## Questions
1. In the main paper, please write the exact training objective actually optimized when mixed negatives are added. Is the loss
   \[
   -\log \frac{\exp(x_i^\top y_i/\tau)}{\exp(x_i^\top y_i/\tau)+\sum_{j\in \mathcal{N}_i}\exp(x_i^\top y_j/\tau)}
   \]
   with \(\mathcal{N}_i\) including both in-batch and uniformly sampled negatives, or something else? Are any importance weights or debiasing terms used? A precise equation in the rebuttal would materially increase my confidence.

2. What exactly is meant by “Uniformity Loss: Enabled/Disabled” in Section 4.3.1? Is there an explicit auxiliary regularizer beyond InfoNCE, or is this shorthand for using InfoNCE versus some other objective? Please clarify because, as written, the main-paper methodology and the ablation description do not match.

3. Can the authors provide a stronger cold-start comparison on the public datasets, not only LOO vs LOOC for RetrievalFormer itself, but also against one or more feature-based baselines that can score unseen items? Even a simple metadata MLP/two-tower/content-based baseline under the exact LOOC protocol would help substantially.

4. For **Table 1**, were all compared models given the same side-information inputs where possible, or are the attribute-aware models and RetrievalFormer operating with richer inputs than the plain ID baselines? A compact table of features used by each model would make the comparison much easier to trust.

5. For the latency study in **Figure 2**, please report at least one measure of ANN retrieval fidelity, for example overlap with exact top-\(K\) or recall of exact nearest neighbors, as a function of \(n_{\text{probe}}\) or index configuration. Otherwise it is difficult to evaluate the speed-quality trade-off of the retrieval layer itself.

6. The paper claims the performance gap is due mainly to replacing full softmax scoring with dual-encoder retrieval rather than weaker sequence modeling. Can the authors support this with an experiment where the same user tower is paired with exact exhaustive retrieval over item embeddings, or with a stronger re-ranking analysis? That would directly test the attribution.

7. Please clarify the exact tokenization and aggregation pipeline behind **Equations (1)** and **(7)**. In particular, how are multi-valued/text features converted into vectors before AttentionFusion, and does \(\oplus\) in Equation (7) mean vector concatenation or set union of feature tokens? This ambiguity is central to understanding the architecture.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns rise to the level of flagging based on the main paper. The only mild caveat is that one case study uses a proprietary email campaign dataset, but the paper’s central evaluation rests on public benchmarks, and no sensitive-user analysis or deployment-risk discussion appears necessary for the review outcome here.

## Soundness Rating
2: fair. The paper is built on plausible components and addresses an important problem, but several central claims are only partially supported, and the training objective, ablations, cold-start evidence, and efficiency analysis leave important gaps.

## Presentation Rating
2: fair. The paper is readable and the high-level story is easy to follow, aided by **Figure 1** and **Figure 2**, but the exposition becomes slippery in the technical details, especially around Equations (1), (7), and (9), the precise loss with mixed negatives, and the interpretation of the ablations.

## Contribution Rating
2: fair. The paper tackles a meaningful practical problem and assembles a usable system, but the conceptual advance over prior dual-encoder/two-tower recommendation pipelines appears limited, and the empirical support is not strong enough to elevate it to a clear ICLR contribution.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is relevant and practically motivated, but in its current form it feels more like a competent integration paper than a sufficiently sharp research contribution for ICLR. The main blockers are limited novelty, underdeveloped cold-start comparisons, incomplete specification of the actual training loss, and efficiency evidence that is directionally convincing but not fully fair or comprehensive.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the main equations, figures, and result tables carefully; however, some implementation details are deferred beyond the main paper, which limits certainty on a few points.