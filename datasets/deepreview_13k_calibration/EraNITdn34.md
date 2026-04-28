# Unlocking the Transferability of Tokens in Deep Models for Tabular Data

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Fine-tuning a pre-trained deep neural network has become a successful paradigm in various machine learning tasks. However, such a paradigm becomes particularly challenging with tabular data when there are discrepancies between the feature sets of pre-trained models and the target tasks. In this paper, we propose \name, a method aims at enhancing the quality of feature tokens (\ie, embeddings of tabular features). \name allows for the utilization of pre-trained models when the upstream and downstream tasks share overlapping features, facilitating model fine-tuning even with limited training examples. Specifically, we introduce a contrastive objective that regularizes the tokens, capturing the semantics within and across features. During the pre-training stage, the tokens are learned jointly with top-layer deep models such as transformer. In the downstream task, tokens of the shared features are kept fixed while \name efficiently fine-tunes the remaining parts of the model. \name not only enables knowledge transfer from a pre-trained model to tasks with heterogeneous features, but also enhances the discriminative ability of deep tabular models in standard classification and regression tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a method to enhance the transferability of deep models on tabular data. Tabular data contain unique column features with their categorical or numerical values, making it challenging to transfer knowledge from pretraining data to unseen downstream data. To address this issue, the authors employ a contrastive regularization objective to learn semantic tokens for each column feature. Few-shot downstream tasks can leverage these overlapping semantic tokens. Experimental results demonstrate that the proposed method outperforms previous approaches in few-shot classification and regression tasks.

### Strengths
- The paper is well-written and easily understandable.
- The proposed method is simple yet effective, delivering superior performance on each dataset compared to previous methods.
- The paper provides a comprehensive analysis and visualization of the experiments.
- The proposed method exhibits a slight improvement in standard tabular tasks, which is a noteworthy point.

### Weaknesses
 - The contrastive loss with the label has limited novelty. 
- The section on related works should be integrated into the main article, as it is difficult to discern the specific improvements in comparison to previous methods.
- While the authors experimented with diverse domains of datasets, both the pretraining and finetuning datasets for each experiment originate from the same dataset. It remains uncertain whether the proposed method can be generalized across domains.
- The proposed method necessitates annotated labels for learning semantic tokens, limiting its application to supervised training. A self-supervised pretraining approach without annotations could be more appealing.

### Questions
Since the current model focuses on pretraining on one dataset and finetuning on the same dataset, is it feasible to explore pretraining on a large-scale cross-domain dataset?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes introducing semantics to feature tokens in order to improve the transferability of feature tokenizers through (1) averaging to represent an instance, (2) introducing a contrastive token regularization objective in pre-training to minimize the distance between instances and their respective class centers. Proposed solution is quite simple, but yet effective based on the empirical evaluation. I recommend the paper for acceptance, particularly given the importance of the problem they are solving in real-world applications.

### Strengths
(1) Clear and intuitive presentation.
(2) Well-motivated problem based on the analysis they conduct (see Figure 4 in particular).
(3) Simple but effective solution based on empirical analysis.

### Weaknesses
 (1) They do not characterize the heterogeneity of the datasets they evaluate on -- hence, I do not have a sense for how hard it actually is to transfer between feature sets.
(2) There is no investigation on how the size of the models affect the described behavior of transferrability of feature tokenizers.

### Questions
n/a

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose TabToken which is a regularization & token feature learning method to incorporatee semantics at the token level during pre-training. This is specifically for tabular datasets with a mixture of real and categorical feature values. The authors claim that pretraining features and the top layer model during pre-training and subsequently finetuning the top layer allows better token feature transfers to other types of complex datasets.

### Strengths
- Consideration of real world problems: The authors considered using datasets that reflect the complexities of real world datasets where there is a mixture of data formats. 
- Holistic testing: The authors evaluated their method on 10 tabular datasets spanning different domains.

### Weaknesses
 - Significance: Lin et al. 2023 [1] demonstrated that the output layer of pre-trained text encoders do encode similarities or structure in tokens. This seems to contradict the authors claim and Figure 4 that vanilla training does not contain structure of the features? Is the lack of feature token transferability specific to tabular datasets? If so, is this solving a narrow or a domain specific problem, or would it generalize to any language model that uses a tokenizer? The authors need to clarify whether the lack of structure in tabular feature tokens is due to the nature of tabular data itself, or if it's a limitation of current pre-training methodologies for tabular data. Specifically, are the feature spaces inherently less structured compared to text or image data, or is it that pre-training on tabular data lacks the scale and diversity to learn meaningful token representations?
- Incremental performance: Table 1 shows that TabToken only leads to a marginal improvement (< 0.2 accuracy and < 3 RMSE), some of the baselines are non deep learning methods. Figure 6, also shows marginal improvement of TabToken compared to other methods with increasing feature ratios. Table 2 also shows incremental improvement or even a decrease in performance when combining existing models with CTR. Is this why the improvement or deprovement with CTR was not highlighted using bold numbers in table 2? The performance gains are not substantial enough to justify the added complexity of the proposed method. The improvements should be more significant to demonstrate the practical value of TabToken, especially when compared to simpler, non-deep learning baselines. The authors should also provide a more detailed analysis of why CTR sometimes decreases performance and under what conditions it is beneficial.
- Difficulty of datasets used: The number of features in the datasets span between 8 to 54 in table 3. With a small dataset scale, non deep learning methods actually perform better. Could the paper be a case of using an over-engineered solution? More importantly, the benefits of using TabToken to improve deep learning algorithms becomes questionable since the dataset complexity is not at scale to employ deep learning methods. Perhaps pre-training or finetuning only the tokenizer might be relevant and the encoded features can be passed to a non deep learning classifier such as SVM? This could alleviate the complexities of training deep learning classifiers and focus the problem of learning good feature representations. The authors need to justify the use of deep learning models on such small datasets, and explore alternative approaches that might be more suitable for the given data complexity. The paper should also investigate whether the proposed method is still beneficial when using non-deep learning classifiers with the learned feature representations.

### Questions
- will the algorithm be released as a pytorch or tensorflow module that can be incorporated into other models? 
- what is the difference between TabToken and CTR? The difference can be delineated better.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
