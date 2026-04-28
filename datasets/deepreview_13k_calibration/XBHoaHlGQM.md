# DOCS: Quantifying Weight Similarity for Deeper Insights into Large Language Models

- Decision: Accept
- Avg Score: 6.60
- Scores: 8, 6, 6, 5, 8

## Abstract
We introduce a novel index, the Distribution of Cosine Similarity (DOCS), for quantitatively assessing the similarity between weight matrices in Large Language Models (LLMs), aiming to facilitate the analysis of their complex architectures. Leveraging DOCS, our analysis uncovers intriguing patterns in the latest open-source LLMs: adjacent layers frequently exhibit high weight similarity and tend to form clusters, suggesting depth-wise functional specialization. Additionally, we prove that DOCS is theoretically effective in quantifying similarity for orthogonal matrices, a crucial aspect given the prevalence of orthogonal initializations in LLMs. This research contributes to a deeper understanding of LLM architecture and behavior, offering tools with potential implications for developing more efficient and interpretable models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces Distribution of Cosine Similarity (DOCS), a new method for measuring similarity between LLM weights.  Unlike previous methods that focused on analyzing representations, DOCS directly examines weight matrices, providing a more precise tool for understanding the internal structure of these complex models. DOCS reveales two important insights, (i) adjacent layers in LLMs often share similar weights and (ii) tend to form functional clusters suggesting depth-wise functional specialization. The findings show that the conventional use of uniform layer configurations in large language models may not be optimal, suggesting hints for more efficient architectures design.

### Strengths
- The method provides a quantitatively similarity score for LLM weights (not representation) which may be helpful for model merging and pruning research.
- The method is proposed with a good level of interpretability and visualization with impressive analysis.

### Weaknesses
While the paper showed an impressive set of analysis (with page limitations), I would very much like to see an analysis on what makes DOCS work. Especially in Algorithm 1, which step is the most crucial one. A small set of experiments may help.

### Questions
- Please follow weakness

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the Distribution of Cosine Similarity (DOCS), a novel index designed to quantitatively assess the similarity between weight matrices in large language models (LLMs). This tool aims to enhance the analysis of LLM architectures by revealing significant patterns within them. Using DOCS, the authors identify that adjacent layers in contemporary open-source LLMs often show high weight similarity and tend to cluster, indicating a trend toward depth-wise functional specialization. Furthermore, the paper demonstrates that DOCS effectively quantifies similarity for orthogonal matrices, an important consideration given the common use of orthogonal initializations in LLMs.

### Strengths
1.	This paper is overall well-written.

2.	This paper proposes to better calculate the parameter similarity between different layers by computing the cosine similarity between corresponding vectors and analyzing their distribution.

3.	Using the technique they propose, the authors observed that: 1) neighboring transformer layers exhibit similar weights, 2) clusters of similar transformer layers exist, 3) the difference of parameters among different models.

### Weaknesses
1.	Some experimental designs could be more detailed and justified, such as the use of the gumbel distribution.

2.	No direct application could be derived from this analysis paper, which could be a weakness of the paper. The authors could add a discussion section to further point out the practical value of the findings in this paper.

### Questions
1.	Why did you choose to use Gumbel distribution to summarize each distribution to a parameter? Is there any specific reason or proof for that?

2.	Could you suggest some other potential applications besides what people have already done (e.g., leveraging layer clusters to reduce computational requirements) that could benefit from the findings in this paper?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces DOCS, a novel matrix-similarity index that measures weight similarity of LLMs. It provides a more reliable and accurate measure of similarity between LLM weight matrices.

### Strengths
1.The approach is novel. It is a discriminative index which captures meaningful differences between weight matrices than other methods.

2.This paper encompasses detailed theoretical derivation on discriminative property and comprehensive experiments, which demonstrate discriminative nature of DOCS and provides some insights into the structure of LLMs.

### Weaknesses
1.Some of findings are not straightforward in this paper. For example, the authors associate multiple reasoning phases with clusters and attribute different numbers of clusters across LLMs to different training strategies. However, they do not clarify the rationale behind these conclusions.

2.Although the authors claim that DOCS satisfies all desired mathematical properties, they do not provide corresponding proofs in the paper.

### Questions
1.Could you provide a detailed explanation on the relation between clusters of similar phases and multiple reasoning phases?

2.Proofs of DOCS satisfying all desired mathematical properties could be added to improve the rigorousness of the claim.

3.I am curious about other similarity indices could achieve similar findings on LLMs. I believe this is important to further demonstrate the superiority of DOCS over other methods.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new metric for measuring the similarity between the weights of transformer models with the goal of gaining insights into LM learning. It is pointed out that existing methods like Canonical Correlation Analysis (CCA) and Centered Kernel Alignment (CKA) do not discriminate between orthogonal matrices well enough, which is a requirement for handling transformer weights. Moreover many existing metrics do not have certain desirable mathematical properties such as transformation and scaling invariance, symmetry, and reflexivity. The proposed metric, DOCS has all these properties.

Empirical justification for the suitability of DOCS for measuring similarity among transformer weights is provided by visualizing the similarity between pairs of MLP layers in a pretrained model.

The main findings using DOCS are that
1. neighboring layers in pretrained LMs are very similar to each other, and there exist clusters of similar layers, both indicating that the transformer architecture can be made more efficient by minimizing such redundancy.
2. the weights of base and instruction tuned models are generally highly similar to each other, and no clear trends exist at which layers weights are most dissimilar (i.e., impacted by instruction tuning).
3. some experts in MoE models are different from others.

### Strengths
The approach, mathematical notation, and the visualizations presented in the paper are easy to follow. The comparison of mathematical properties of similarity functions is informative.

### Weaknesses
 **Motivation**: The main motivation behind studying the similarity between weights instead of representations is unclear. The arguments about discriminating between orthogonal matrices, and the mathematical properties of scaling invariance etc. are built on top of the assumption that studying similarity between the weight space is more insightful than in the representation space, but it is not clear to me why that is the case. After all, is it not the representations that directly affect the outputs and the behavior of a model? Moreover, representational similarity is arguably agnostic to the depth of a network, which is not the case with weight-space similarity. It would be great if the authors could clarify their motivation in the response.

**Empirical justification**: The empirical justification provided for DOCS being superior to other similarity measures is a) that the visualization of the similarity between layers lack a clear structure and appear noisy for CCA and Linear Regression in contrast to DOCS (Section 4.1), and b) the Gini coefficient of DOCS is higher than that of other metrics.
- (a) is not a convincing justification. A metric showing clearer patterns is not necessarily better.This could also mean that DOCS is missing out on useful information other metrics are capturing. It would be more meaningful to compare metrics against a ground truth, e.g., are models that have similar output distributions, like different training checkpoints of the same model, more similar according to one measure than the other?
- (b) requires elaboration. How is the Gini coefficient computed? Why is t relevant? How should one interpret these results?

**Impact of the findings**:
- That there is potential redundancy of knowledge in the weights of neural networks is an interesting finding, but it is not new. This has been empirically studied in many works that are well cited in this paper.
- The experiments comparing base and finetuned models and MoE do not show clear trends, and it is unclear what can be inferred from them.

### Questions
- It makes sense that the mathematical properties listed in Section 2 are desirable in a similarity measure of transformer weights. But are these properties *sufficient* for such a metric?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel similarity index, DOCS, designed to measure the similarity between two matrices, with a focus on its application to neural network matrices. A key feature of DOCS is its ability to distinguish between orthogonal matrices, which the authors claim is crucial for training neural networks. In addition, DOCS possesses desirable properties such as symmetry and reflexivity.

The computation of DOCS is both simple and elegant, making it easy to understand and computationally efficient. It calculates the maximum cosine similarity between the rows and columns of two matrices, then fits a Gumbel distribution to each of these values. Finally, it averages the two scores to produce the final similarity measure.

The authors present a series of experiments demonstrating the results of applying DOCS to several large language models, comparing the results to other similarity indices such as CCA and SVCCA.

Overall, the paper introduces a promising new similarity index, DOCS, with several interesting properties for comparing neural network weight matrices, particularly in the context of language models. The authors provide an extensive set of experiments with recent open-weight models, comparing DOCS with other indices. However, while the contributions are valid, there are several issues that need to be addressed in the current version of the paper:

Evaluation
------

It is unclear how to evaluate DOCS or whether it captures a truly desirable property. The experiments in the paper show results, but it is not clear why DOCS should be considered superior to other similarity indices. How should we interpret these results? Are the similarities computed by DOCS more meaningful than those computed by other indices? The paper does not provide sufficient justification for why the "elegant" similarity matrices obtained by DOCS are more informative or useful than those obtained by other methods. The authors also suggest that DOCS could help in developing more efficient models (L.124) or provide deeper insights into model behavior (L.134), but there is no empirical evidence to support these claims.
Providing some empirical evidence that using DOCS can lead to better empirical results, or new insights about models are crucial as part of the evaluation of this method.

The authors attempt to justify DOCS by presenting heatmaps of weight matrices, suggesting that these show clearer patterns with less noise. However, this is a highly subjective measure and not convincing. They also compute the Gini coefficient (which should be explained more thoroughly) and claim that its higher value supports DOCS’s superiority. I find this reasoning unconvincing.


Overclaiming
--------
Several claims made in the paper are either overstated or lack sufficient evidence.

- The assertion that neural network matrices require a similarity index that discriminates between orthogonal matrices is one such claim. The authors should (1) empirically demonstrate that the matrices are orthogonal, which should be straightforward, and (2) show that this property is important in practice. Currently, these claims are made without adequate justification.
- L93-98: The authors claim that the heatmaps demonstrate the effectiveness of DOCS. Why do these heatmaps prove effectiveness? Why should we expect the DOCS index to be more informative than other similarity indices?
- L.113: The paper claims that DOCS shows high similarity, but the values are around 0.12, which seems quite low to me.
- L.124: The statement that DOCS "could lead to more efficient models" feels like an overreach.
- L.420-421: The claim that large language models (LLMs) might consist of multiple reasoning phases based on the similarity clusters is speculative and not well-substantiated.
- L.424: The argument that multiple clusters imply multiple training strategies is unconvincing. This could easily be tested by comparing models at different training stages (e.g., base model, fine-tuned model, RLHF model) and examining whether the number of clusters changes.
- L.477: The trends in similarity scores across different layers are minimal (e.g., differences of <0.001 in Llama-3.1-8B), so I question how meaningful these differences really are.


Missing Details
---------
(Note: these are smaller issues, but still important to address in the paper.)

- When computing DOCS, part 3 of the algorithm involves fitting a Gumbel distribution to the obtained values. However, it is unclear how the final single numeric value is derived. Is it the mean, median, or another statistic from the distribution?
- The claim that DOCS can distinguish between orthogonal matrices (L.267) is not explicitly demonstrated in the paper. More details should be provided.
- There is no information on how the baselines for comparison were computed. These details should be included for transparency.


Need for Elaboration
-------------
The paper discusses at length DOCS’s ability to discriminate between orthogonal matrices, but it is unclear why this is a valuable property. Expanding on why this distinction matters in practice would strengthen the paper.

The theoretical proof in Section 3.1 is also not entirely clear. It would be helpful if the authors could expand on the practical implications of this proof.


-------
Rebuttal summary:

After the authors' response I decided to increase my scores due to the satisfying responses that satisfied most of my concerns.
I still believe it's not completely clear how the metric can be used, but I believe some may find it useful, and I do not object of having another similarity metric, especially since it operates on matrices, unlike most previous work that operates on hidden representations.

### Strengths
- Introduction of a new similarity index, DOCS, which possesses intriguing properties that make it well-suited for comparing neural network similarities.
- Extensive experimentation on recent language models, with comparisons to established similarity indices.

### Weaknesses
Evaluation
------

It is unclear how to evaluate DOCS or whether it captures a truly desirable property. The experiments in the paper show results, but it is not clear why DOCS should be considered superior to other similarity indices. How should we interpret these results? Are the similarities computed by DOCS more meaningful than those computed by other indices? The paper does not provide sufficient justification for why the "elegant" similarity matrices obtained by DOCS are more informative or useful than those obtained by other methods. The authors also suggest that DOCS could help in developing more efficient models (L.124) or provide deeper insights into model behavior (L.134), but there is no empirical evidence to support these claims.
Providing some empirical evidence that using DOCS can lead to better empirical results, or new insights about models are crucial as part of the evaluation of this method.

The authors attempt to justify DOCS by presenting heatmaps of weight matrices, suggesting that these show clearer patterns with less noise. However, this is a highly subjective measure and not convincing. They also compute the Gini coefficient (which should be explained more thoroughly) and claim that its higher value supports DOCS’s superiority. I find this reasoning unconvincing.


Overclaiming
--------
Several claims made in the paper are either overstated or lack sufficient evidence.

- The assertion that neural network matrices require a similarity index that discriminates between orthogonal matrices is one such claim. The authors should (1) empirically demonstrate that the matrices are orthogonal, which should be straightforward, and (2) show that this property is important in practice. Currently, these claims are made without adequate justification.
- L93-98: The authors claim that the heatmaps demonstrate the effectiveness of DOCS. Why do these heatmaps prove effectiveness? Why should we expect the DOCS index to be more informative than other similarity indices?
- L.113: The paper claims that DOCS shows high similarity, but the values are around 0.12, which seems quite low to me.
- L.124: The statement that DOCS "could lead to more efficient models" feels like an overreach.
- L.420-421: The claim that large language models (LLMs) might consist of multiple reasoning phases based on the similarity clusters is speculative and not well-substantiated.
- L.424: The argument that multiple clusters imply multiple training strategies is unconvincing. This could easily be tested by comparing models at different training stages (e.g., base model, fine-tuned model, RLHF model) and examining whether the number of clusters changes.
- L.477: The trends in similarity scores across different layers are minimal (e.g., differences of <0.001 in Llama-3.1-8B), so I question how meaningful these differences really are.


Missing Details
---------
(Note: these are smaller issues, but still important to address in the paper.)

- When computing DOCS, part 3 of the algorithm involves fitting a Gumbel distribution to the obtained values. However, it is unclear how the final single numeric value is derived. Is it the mean, median, or another statistic from the distribution?
- The claim that DOCS can distinguish between orthogonal matrices (L.267) is not explicitly demonstrated in the paper. More details should be provided.
- There is no information on how the baselines for comparison were computed. These details should be included for transparency.


Need for Elaboration
-------------
The paper discusses at length DOCS’s ability to discriminate between orthogonal matrices, but it is unclear why this is a valuable property. Expanding on why this distinction matters in practice would strengthen the paper.

The theoretical proof in Section 3.1 is also not entirely clear. It would be helpful if the authors could expand on the practical implications of this proof.

### Questions
- It could be valuable to experiment with an initialized model and compute similarity indices, including DOCS. Given the presence of residual connections, the results may exhibit non-random patterns.
- L.115: This sentence is unclear. Are you suggesting that the layer configurations remain uniform during the initialization of the model?
- Suggestion: The font sizes in Figure 3 panels (1-3) and (d-f) are inconsistent. Ensure uniform font sizes across the figures for clarity and visual consistency.

### Soundness
3

### Presentation
3

### Contribution
3
