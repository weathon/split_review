# RankNovo: A Universal Reranking Approach for Robust De Novo Peptide Sequencing

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
De novo peptide sequencing is a critical task in proteomics research. However, the performance of current deep learning-based methods is limited by the inherent complexity of mass spectrometry data and the heterogeneous distribution of noise signals, leading to data-specific biases. We present RankNovo, the first deep reranking framework that enhances de novo peptide sequencing by leveraging the complementary strengths of multiple sequencing models. RankNovo employs a list-wise reranking approach, modeling candidate peptides as multiple sequence alignments and utilizing axial attention to extract informative features across candidates. Additionally, we introduce two new metrics, PMD (Peptide Mass Deviation) and RMD (Residual Mass Deviation), which offer delicate supervision by quantifying mass differences between peptides at both the sequence and residue levels. Extensive experiments demonstrate that RankNovo not only surpasses its individual base models, which are used to generate training candidates for reranking pre-training, but also sets a new state-of-the-art de novo sequencing benchmarks. Moreover, RankNovo exhibits strong zero-shot generalization to unseen models—those whose generations were not exposed during training, highlighting its robustness and potential as a universal reranking framework for peptide sequencing. Our work presents a novel reranking strategy that fundamentally challenges existing single-model paradigms and advances the frontier of accurate de novo peptide sequencing. Our source code is provided at an anonymous link.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
It is an interesting paper that proposes a deep learning-based reranking framework and introduces two new metrics, PMD and RMD, to characterize quality differences at the peptide and residue levels. The new framework leverages the strengths of multiple de novo peptide sequencing models to achieve improved performance through reranking.

### Strengths
- The paper is written very clearly and is easy to understand.
- The motivation is highly meaningful, revealing that different models have distinct advantages.
- A general framework is proposed, adaptable to any de novo peptide sequencing model.
- The experiments are thorough.

### Weaknesses
 - The discussion of transformer-based approaches in the introduction is insufficient.

- The meaning of some mathematical symbols is unclear.

- Specifically, the symbol 'M' is used to represent both residue mass (line 270) and prefix mass (line 306), which is confusing and could lead to misinterpretations. A more precise notation is needed to differentiate these two concepts.

- Furthermore, in formula (7) on line 309, the term \overline{m}_{q\tilde{j}} - \overline{m}_{k\tilde{j}} appears to be incorrect. It should likely be \overline{m}_{qi} - \overline{m}_{k\tilde{j}} to accurately represent the prefix mass difference. The current notation does not clearly indicate which prefix masses are being compared, and the use of \tilde{j} in both terms is likely a typo.

### Questions
- Recently, many transformer-based de novo peptide sequencing methods have emerged, such as HelixNovo[1], InstaNovo[2], AdaNovo[3], PrimeNovo[4], GraphNovo[5], etc. The discussion of these transformer-based approaches in the introduction is insufficient.
  
- In line 270, M  represents the residue mass, but the same symbol is also used in line 306 to denote prefix mass. It would be better to add a subscript or identifier to distinguish prefix mass or, alternatively, use a different symbol to represent it.

- In the mathematical formula (7) on line 309, should  \overline{m}_{q\tilde{j}} - \overline{m}_{k\tilde{j}} be corrected to  \overline{m}_{qi} - \overline{m}_{k\tilde{j}}  to represent the prefix mass difference more accurately?

[1] π-HelixNovo for practical large-scale de novo peptide sequencing

[2] De novo peptide sequencing with InstaNovo: Accurate, database-free peptide identification for large scale proteomics experiments

[3] AdaNovo: Adaptive \emph{De Novo} Peptide Sequencing with Conditional Mutual Information

[4] π-PrimeNovo: An Accurate and Efficient Non-Autoregressive Deep Learning Model for De Novo Peptide Sequencing

[5] Mitigating the missing-fragmentation problem in de novo peptide sequencing with a two-stage graph-based deep learning model

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents the first deep learning-based reranking framework that enhances de novo peptide sequencing by leveraging the complementary strengths of multiple sequencing models. RankNovo scores the output sequences of multiple de novo models to train the model (training phase) or to obtain the optimal sequence through scoring (inference phase). The paper also introduces novel metrics such as PMD and RMD.

### Strengths
1. The paper demonstrates a high degree of novelty by proposing a method that utilizes predicted sequences from multiple de novo models, challenging the traditional single-model paradigm.
2. It achieves performance that surpasses all baselines and base models on two datasets.
3. The introduction of novel metrics such as PMD and RMD is likely the first of its kind in de novo sequencing, providing valuable reference points.

### Weaknesses
1. The performance improvement seems modest. RankNovo's peptide recall only surpasses the baseline by 0.037 (V1) and 0.023 (V2). Since RankNovo is trained and inferred based on these base models, it theoretically can only outperform them. The evaluation of RankNovo's performance should be based on its improvement relative to SOTA baselines. Otherwise, for such minor improvements, why not simply use the predictions from other models instead of inference multiple models through RankNovo?

2. There seems to be a lack of analysis regarding the parameter number, training time, and inference time of RankNovo compared to other de novo models, which should be addressed in the experimental section. Given that RankNovo requires inference results from multiple (2 to 6) other models during training and inference, it can be inferred that its training and inference times would be slower than those of other models.

### Questions
1. The definition of robustness in the paper seems somewhat ambiguous. On one hand, it appears to refer to the model's robustness to noise in mass spectrometry data (Lines 12–14, Lines 81–84), but RankNovo might not sufficient to address this issue. On the other hand, it seems to refer to the issue of having inconsistent baseline models available during training and testing phases.


2. Based on the disadvantage mentioned earlier regarding modest performance improvement, there should be experiments to demonstrate whether naive methods (instead of RankNovo) can also achieve reasonable results. For instance, during inference, for multiple predicted peptides from different base models, one could select: (1) the peptide with the highest score from a model output, (2) the most frequently predicted peptide, or (3) the peptide closest to the precursor mass, and compare the performance of these methods against RankNovo. This approach would help demonstrate that RankNovo indeed learns some knowledge from the predicted results of multiple models.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents RankNovo, a list-wise deep reranking framework for de novo peptide sequencing that uses outputs from multiple base models, applying axial attention and novel metrics for effective peptide reranking.

### Strengths
1. Introduces a unique list-wise reranking approach that effectively leverages outputs from multiple de novo peptide sequencing models.
2. Introduces PMD and RMD metrics, designed for precise quantification of mass differences between peptides.
3. The model demonstrates significant improvements over existing methods.

### Weaknesses
1. The approach heavily depends on outputs from existing peptide sequencing models, which may limit its novelty. The reliance on multiple base models, while demonstrating a practical application of ensembling, does not fundamentally advance the core algorithms of de novo peptide sequencing. The method's performance is intrinsically tied to the quality of the base models; if the base models are weak or biased, the reranking framework will likely inherit these limitations. Furthermore, the computational cost of running multiple base models and then a reranking model could be substantial, potentially limiting its applicability in resource-constrained environments.
2. The conclusion is somewhat simple and could be expanded to discuss the limitations of the current approach and potential future research directions.

### Questions
1. RankNovo incorporates six de novo sequencing models. Is there any rationale for the selection of these?
2. See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents the first deep reranking framework, RankNovo, based on a list-wise reranking approach, which enhances de novo peptide sequencing by leveraging the complementary strengths of multiple sequencing models. Experimental results show that RankNovo achieves state-of-the-art performance on de novo sequencing benchmarks, outperforming each of its component base models.  Moreover, RankNovo exhibits strong zero-shot generalization to unseen models that highlight its robustness and potential.

### Strengths
1. The paper introduces a deep learning-based reranking framework for peptide de novo sequencing, and focus on addressing the preferential bias challenges inherent in peptide sequencing.
2. The paper introduces two novel metrics, PMD and RMD, for accurate measurement of mass differences between peptides, which enable the model to more accurately distinguish complex similar sequences.
3. In the experiments, RankNovo surpasses each of its individual ensemble components on the 9-species-V1 and the 9-Species-v2 dataset, demonstrating superior performance in amino acid and peptide.
4. RankNovo generalizes effectively to unseen models in a zero-shot setting, which underscores the potential and value for future applications in de novo peptide sequencing.

### Weaknesses
1. The proposed RankNovo relies on the setting of multiple base models, which increases the computational cost. While the authors mention this, a more detailed analysis of the computational overhead is needed, including the time complexity of the attention mechanism and the impact of the number of candidates generated by base models on overall runtime. It would be beneficial to see a breakdown of the time spent in each stage of the pipeline, not just the overall inference time.
2. In formula 10, L_coarse and L_fine are not clearly defined. It seems more appropriate to use L_PMD and L_RMD? The lack of clarity makes it difficult to understand the precise nature of the loss functions and their contribution to the overall objective.
3. In formula (1) and formula (10), λ is confused. The inconsistent use of the same symbol for different parameters is a significant issue that needs to be addressed for clarity and mathematical rigor.
4. The setting of λ in Equation 10 is unclear. Is the λ used in different tasks inconsistent? The author needs to clarify the setting of λ and the impact of λ on performance. Specifically, how was the value of λ chosen, and what is the sensitivity of the model performance to changes in this parameter? A more detailed ablation study is needed to understand the impact of this hyperparameter.
5. In order to study the influence of the number of base models and each model, you select five subsets. Could you explain the basis for sequentially removing the strongest model? Why not remove the poorest ones? The rationale for this specific selection process is not clear, and it's important to understand if this choice biases the results. Exploring alternative selection strategies would strengthen the analysis.
6. In Table 8, compared with the 5 models, the 6 models introduced the strongest ByNovo, but the average performance was reduced. What is the possible reason? This counterintuitive result requires a more in-depth explanation. It's not sufficient to simply state that peptide recall is the primary metric; the underlying reasons for the decrease in amino acid precision should be investigated.
7. In Conclusion, there is relatively little content on the prospects and challenges of future optimization and applications, research limitations. It is suggested to supplement some to make it more comprehensive and forward-looking.

Minor issues:
1. typo error: Please confirm if the term ‘expriment’ is used correctly in the titles of Section 4 and 4.1 of the article.
2. There are three models in "The latter four models, ByNovo, R-ContraNovo, and R-ByNovo".

### Questions
Please see the questions and suggestions raised in the section Weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2
