---
job_id: 6f5d324a-72cb-4e19-95cd-58a842a9baf9
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ahpO7S1Ppi.pdf
paper: PCTX: Tokenizing Personalized Context for Generative Recommendation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies generative recommendation through learned discrete tokenizations and context-conditioned representations, which directly relates to representation learning and generative modeling.

## Minimum Quality
Pass ✅. The paper includes the required scientific components, namely abstract, introduction, method, experiments, results/analysis, related work, and conclusion, and it presents a coherent empirical study. While I have substantial concerns about methodological specification and evidence strength, these are review-level issues rather than desk-rejection-level flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions to reviewers, or other obvious attempts to interfere with automated or human review.

# Expected Review Outcome:
## Summary
This paper proposes Pctx, a personalized context-aware tokenizer for generative recommendation, where the semantic ID assigned to an item depends not only on item features but also on the user’s historical interaction context. The method builds context representations with an auxiliary sequential model, clusters per-item context embeddings into a small number of representative centroids, fuses them with item textual features, quantizes the fused embeddings into semantic IDs, and then trains a generative recommender with augmentation and multi-facet decoding. Experiments on three Amazon subsets show consistent gains over static semantic-ID baselines and standard sequential recommenders.

## Strengths
1. The paper tackles a real limitation of current semantic-ID based generative recommendation, namely that static tokenization implicitly fixes a single notion of item similarity for all users. This is a sensible problem formulation, and the motivation in **Figure 1** is intuitive and useful. The figure does a good job of illustrating the core claim that the same item can play different semantic roles under different user contexts, and that a static tokenizer cannot express this.

2. The overall pipeline is reasonably well structured. **Figure 2** helps clarify the intended workflow, from learning context representations, to fusing them with item features, to quantizing into multiple semantic IDs and decoding them in a multi-facet way. Even though some implementation details are underspecified, the high-level design is understandable and more thoughtful than simply assigning multiple random IDs per item.

3. The empirical results in **Table 2** are consistently in favor of Pctx across all three datasets and all reported metrics. The gains over the best GR baseline, especially over ActionPiece, are not trivial in magnitude for this benchmark family. The improvements on Scientific, for example, are reasonably noticeable: NDCG@10 improves from 0.0236 to 0.0257, which is directionally supportive of the main claim that longer-horizon personalized tokenization can help beyond adjacent-context tokenization.

4. The ablation study in **Table 3** is one of the stronger parts of the paper. In particular, the drop from Pctx to “w/o Redundant SID Merging” is large, which suggests that the authors are right to worry about the tension between personalization and sparsity. Also, the comparison to “TIGER w/ Pctx IDs” is useful because it partially separates the benefits of the tokenizer from the benefits of the downstream training/inference modifications.

5. The paper includes some analysis beyond a headline benchmark table. **Table 4** is helpful because it addresses a reasonable alternative explanation, namely that the gains may just come from blending the strengths of a conventional sequential model with a GR model. The fact that simple ensembling underperforms Pctx supports, at least to some degree, that the method is doing more than late fusion.

6. The case study in **Figure 4** is a decent qualitative example. It gives a concrete item with two semantic IDs and aligns those IDs with two distinct game preferences. I would not treat this as strong evidence on its own, but it does make the intended behavior of the method much easier to understand.

## Weaknesses
1. **The central methodological object, the context encoder \(f(\cdot)\) in Equation (1), is not sufficiently specified in the main paper, and this matters because the tokenizer depends on it.**  
   In **Section 2.2.1, Equation (1)**, the paper defines
   \[
   \mathbf e_{v_i}^{ctx} = f([v_1,\dots,v_i]),
   \]
   but the exact representation taken from the pretrained sequential model is unclear. Is \(\mathbf e_{v_i}^{ctx}\) the final hidden state, a pooled sequence embedding, or the representation at position \(i\)? The text says the model is “pretrained on the same training data” and that DuoRec is adopted “as an example,” but the paper never clearly states the objective used in this stage, whether the encoder is frozen afterward, and how the representation is extracted for each prefix. This is not a cosmetic detail. Since the whole personalized tokenizer is built on these embeddings, ambiguity here undermines reproducibility and makes it difficult to assess whether gains come from personalization or from a particularly favorable auxiliary representation learner.

2. **The mathematical formulation around representation fusion in Equation (2) is weak and somewhat inconsistent.**  
   **Equation (2)** defines
   \[
   \mathbf e_{v_i,k}=\text{concat}(\alpha \cdot \mathbf e^{ctx}_{v_i,k}, (1-\alpha)\cdot \mathbf e^{feat}_{v_i}),
   \]
   but the use of a scalar \(\alpha\) to “balance” the two components is odd under concatenation. Concatenation does not actually mix the modalities; it only rescales them before stacking. If \(d_1\) and \(d_2\) differ substantially, then the contribution of the two blocks to subsequent Euclidean-distance-based clustering/quantization depends not only on \(\alpha\), but also on dimensionality and variance. This is especially important because later steps rely on k-means and RQ-VAE-style quantization, both of which are sensitive to scale. The paper does not justify why this is the right fusion, whether embeddings are normalized before concatenation, or how the chosen \(\alpha=0.5\) should be interpreted when the two subspaces can have different dimensions and norms. If the intended operation is weighted feature fusion under Euclidean distance, then some normalization argument is needed.

3. **The adaptive clustering procedure is largely heuristic, and the main paper does not provide enough evidence that it is principled or stable.**  
   The core of personalization is the assignment of each item \(v_i\) to \(C_{v_i}\) context centroids, but in the main paper this is described only as “chosen proportionally to the number of available context representations” in **Section 2.2.1**, with actual details deferred to the appendix. In the appendix, the number of centroids is determined by grouping items using a Gamma-shaped prior and an arithmetic progression of capacities. This is quite a hand-crafted design, with multiple hyperparameters \((T, K, C_{\text{start}}, \delta)\). The problem is not merely that the method is heuristic, many practical systems are, the problem is that the paper makes strong conceptual claims about balancing generalizability and personalizability, but the proposed balancing mechanism is mostly a manually tuned allocation rule rather than a learned or theoretically justified one. Without sensitivity analyses for these clustering hyperparameters in the main paper, it is hard to know whether the reported improvements are robust or a product of extensive task-specific tuning.

4. **Several parts of the semantic-ID merging procedure are underspecified or mathematically sloppy.**  
   The main paper says low-frequency semantic IDs are removed if their frequency is below threshold \(\tau\), then reassigned to the “closest clustering centroids.” However, in **Appendix E**, the notation for frequencies is inconsistent. For example, **Equation (4)** uses \(D_{v_i}=\{M_{v_i,k}:R_{v_i,k}\}_{k=1}^{C_i}\), mixing \(C_i\) and \(C_{v_i}\). **Equation (7)** writes \(\widetilde{R}_i = \sum_{s=1}^d R_i^{k_s}\), which does not match the earlier notation \(R_{v_i,k}\). **Equation (10)** defines
   \[
   \operatorname{tgt}(k^\star)=\arg\min_{a\neq k^\star}\operatorname{dist}(M_{i,k^\star}, M_{i,a}),
   \]
   but the text then says \(\operatorname{dist}\) is the Euclidean distance between centroids of two personalized semantic IDs, which means the arguments should not be the discrete IDs \(M\) themselves but the associated centroid embeddings. This mismatch is not trivial, because the merge rule depends on whether proximity is measured in token space, fused embedding space, or centroid space. As written, the formulation leaves room for multiple materially different implementations.

5. **The training objective and data augmentation are underexplained relative to how central they are to the gains.**  
   In **Section 2.3**, the model is said to use “next-token prediction loss,” but the exact sequence formatting is not given in the main paper. More importantly, the augmentation strategy randomly replaces a personalized semantic ID by another ID of the same item with probability \(\gamma\). This may create training examples that are inconsistent with the original context-conditioned token assignment, and the paper essentially acknowledges this by saying the augmented sequences “may not always reflect the most accurate user interpretation.” That is a pretty big caveat. Why should this noise help rather than hurt? The ablation in **Table 3** shows it helps empirically, but the paper does not unpack what distribution is used for replacement, whether all alternative IDs are sampled uniformly, whether replacement is allowed for both input histories and targets simultaneously, and whether this creates label ambiguity during autoregressive training. A more careful statement of the actual training data distribution would strengthen the paper substantially.

6. **The inference procedure for multi-facet generation is too vague for a method that claims interpretability and personalized probability aggregation.**  
   In **Section 2.3**, the paper states that beam search yields distinct personalized semantic IDs for the same item and that the corresponding probabilities are aggregated to obtain next-item probabilities. However, the paper does not define this aggregation formally. Is the item probability the sum of path probabilities for all beams decoding to any semantic ID of that item? If so, are the beams normalized over complete sequences, and how are duplicate semantic-ID prefixes handled? This matters because in semantic-ID retrieval, prefix sharing can distort probability mass. The authors’ motivation in **Section 1** explicitly hinges on prefix-probability behavior, so a paper making that argument should be mathematically precise about how final item probabilities are assembled from token-level generation scores.

7. **The empirical evaluation is narrower than the claims.**  
   The paper makes broad claims about personalized semantic tokenization and user-specific interpretation, but all experiments are on three Amazon subsets with relatively short average sequence lengths, as shown in **Table 1** where AvgLen is around 8 to 9. This is a somewhat awkward setting for a method whose main conceptual advantage is supposed to come from leveraging “the entire user interaction history” rather than only adjacent actions. If most histories are short, the distinction between local context and long-range personalization is less convincing. The paper would be stronger with either datasets that have longer temporal structure or explicit stratified analysis showing that Pctx helps more for longer histories.

8. **Key baselines are not fully stress-tested against the paper’s own causal story.**  
   The main baseline comparison in **Table 2** includes ActionPiece, which is good, since it is the closest context-aware tokenizer. But the paper’s central claim is not merely “context helps,” it is “long-horizon personalized context helps because static prefixes impose a universal similarity standard.” To support that stronger claim, I would expect analyses such as: performance broken down by number of semantic IDs per item, by user-history length, or by item ambiguity level. **Figure 3** shows the distribution of personalized semantic IDs per item, but it does not connect that distribution to recommendation quality. Likewise, **Figure 7** in the appendix visualizes how the probability of using the popular semantic ID changes by position, which is interesting, but it still stops short of linking this behavior to downstream accuracy. Right now, some of the paper’s mechanistic claims remain more suggestive than demonstrated.

9. **The exposition contains multiple notation and presentation issues that make the paper harder to trust than it should be.**  
   There are several small but noticeable inconsistencies. In **Section 3.1**, the text says the datasets are three categories, but the table captioning and dataset names fluctuate between shortened labels and raw category names. In **Table 3**, the paper refers to “S1-Rec” in the main text while **Section 3.1** lists “S3-Rec,” which is likely a typo but still sloppy in a benchmark-heavy paper. In **Table 8**, the value “0.556” for Game / “with DuoRec Item Embedding” is obviously inconsistent with surrounding values and likely should be 0.0556. These may seem minor, but when combined with the notation inconsistencies in the equations, they reduce confidence that the full pipeline has been described carefully enough.

10. **The qualitative evidence is interesting but overstated.**  
   **Figure 4** is visually effective, but it relies on a hand-picked game example with genre semantics that are easy for humans to rationalize after the fact. The semantic IDs themselves, such as \([53,395,576,770]\) vs. \([53,412,576,770]\), do not intrinsically establish that one tokenization is story-driven and the other RTS-oriented; that interpretation comes from external narrative around the surrounding items. Similarly, the explainability experiment described later relies on GPT-4o judgments, which is not part of the main paper’s core evidence. So while the figure is useful for intuition, it should be treated as illustration, not as strong validation of semantic disentanglement.

11. **The comparison against static tokenizers may partly entangle tokenizer quality with downstream model/training choices.**  
   The paper compares Pctx against TIGER, LETTER, and ActionPiece in **Table 2**, but Pctx also introduces extra components at training and inference time, namely augmentation and multi-facet generation. The ablation in **Table 3** helps, yet it still leaves an attribution issue: the gain is not purely from personalized tokenization, but from a package of tokenizer plus specialized handling of one-to-many item-to-ID mappings. That is fine if presented as a system contribution, but several claims in the paper frame the advance primarily as a tokenizer contribution. The distinction should be made more carefully.

12. **The paper’s conceptual argument about prefix similarity is plausible, but not formally established.**  
   The introduction repeatedly states that semantic IDs sharing prefixes “inevitably receive similar generation probabilities,” and that therefore static tokenization imposes a universal similarity standard. There is intuition here, but the paper never formalizes the degree of this effect or under what decoding model assumptions it holds strongly enough to motivate the entire method. In modern autoregressive models, shared prefixes do create shared early decoding trajectories, but the final probability over complete ID sequences can still differ sharply after later tokens. Since this argument is foundational to the paper’s problem statement, it deserved a tighter formulation or at least a controlled empirical demonstration.

## Questions
1. For **Equation (1)**, what exact representation from DuoRec is used as \(\mathbf e_{v_i}^{ctx}\)? Is it the hidden state at position \(i\), a pooled prefix representation, or something else? Is the auxiliary model frozen before clustering and quantization, or updated jointly at any stage?

2. For **Equation (2)**, are \(\mathbf e^{ctx}\) and \(\mathbf e^{feat}\) normalized before concatenation? If not, how do you ensure that \(\alpha\) is meaningful when dimensions and scales of the two components may differ? A rebuttal that clearly states the preprocessing and distance computation would increase my confidence.

3. Please give a precise formal definition of the final item score during inference. If multiple beams map to different semantic IDs of the same item, is the item probability computed by summing beam probabilities, summing token-sequence probabilities before truncation, or something else? A small equation here would help substantially.

4. Can you quantify how much of the gain comes from personalization specifically on longer histories? Since **Table 1** shows average sequence lengths around 8 to 9, it would be helpful to report performance stratified by user-history length, or at least compare short vs. long histories. This would directly test the paper’s key narrative that broader history helps beyond adjacent context.

5. The clustering scheme for choosing \(C_{v_i}\) seems fairly heuristic. Could you provide evidence that the method is robust to this design, for example by comparing against simpler alternatives such as a fixed \(C\), a log-scaled count rule, or a validation-selected per-item cap? This would clarify whether the reported gains are due to the personalized tokenization idea itself rather than a carefully tuned allocation heuristic.

6. In **Table 3**, “w/o Redundant SID Merging” performs much worse than the full model. Can you report the actual number of semantic IDs used in each ablation? This would make the sparsity-personalization tradeoff more concrete and help interpret the ablation.

7. Could the authors clarify the implementation inconsistencies around **Appendix E**, especially the notation in **Equations (4), (7), and (10)**? If these are merely typos, please provide the corrected formulation. If not, the exact merge operation should be specified more carefully.

8. A useful additional analysis would be to connect **Figure 3** to accuracy, for example reporting performance as a function of the number of semantic IDs an item possesses, or comparing ambiguous items versus items with a single ID. That would directly test the paper’s core premise.

## Flag For Ethics Review
- Yes, Discrimination / bias / fairness concerns  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper is in recommendation, so personalization methods can amplify historical behavioral biases and popularity patterns, even if the datasets are public and contain no directly identifying information. In this work, the tokenizer is explicitly conditioned on user history, and low-frequency semantic IDs are merged using frequency thresholds, which could preferentially collapse minority or niche behavioral patterns into dominant interpretations. This is especially relevant to the merging procedure in **Section 2.2.2** and the thresholding discussion around \(\tau\), because rare user perspectives may be exactly the ones most at risk of being removed. I do not see this as a reason for rejection by itself, but the ethics statement is too quick in saying the authors are “not aware of any ethical concerns or potential risks.” Some discussion of representational bias and possible over-amplification of majority preferences would be appropriate.

## Soundness Rating
2: fair. The empirical results are promising and mostly consistent, but core parts of the method, especially the context representation extraction, fusion, and probability aggregation, are under-specified, and the mathematical formulation contains enough ambiguity that I cannot rate the paper higher on soundness.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures are helpful, but there are too many notation inconsistencies, underdefined equations, and small presentation errors for a stronger score.

## Contribution Rating
2: fair. The idea of personalized semantic IDs for generative recommendation is interesting and relevant, but the paper does not yet make the case with enough methodological precision and mechanistic evidence to count as a strong contribution for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper has a good core idea and some encouraging results, especially in **Table 2** and the ablations in **Table 3**, but I see too many unresolved issues in method specification, mathematical clarity, and evidence supporting the stronger causal claims. In its current form, it feels promising but not sufficiently nailed down.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with recommendation and semantic-ID based generative retrieval, and I checked the main technical claims and experimental evidence carefully.