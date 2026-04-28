# Pretrained deep models outperform GBDTs in Learning-To-Rank under label scarcity

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
On tabular data, a significant body of literature has shown that current deep learning (DL) models perform at best similarly to Gradient Boosted Decision Trees (GBDTs), while significantly underperforming them on outlier data \cite{gorishniy2021revisiting,rubachev2022revisiting,mcelfresh2023neural}. However, these works often study idealized problem settings which may fail to capture complexities of real-world scenarios. We identify a natural tabular data setting where DL models can outperform GBDTs: tabular Learning-to-Rank (LTR) under label scarcity. Tabular LTR applications, including search and recommendation, often have an abundance of unlabeled data, and \emph{scarce} labeled data. We show that DL rankers can utilize unsupervised pretraining to exploit this unlabeled data. In extensive experiments over both public and proprietary datasets, we show that pretrained DL rankers consistently outperform GBDT rankers on ranking metrics---sometimes by as much as $38\%$---both overall and on outliers.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the effectiveness of unsupervised pretraining in tabular Learning-To-Rank (LTR) problems. First, authors show how two well-known self-supervised training methods (SimCLR, SimSiam) can be formulated in LTR problems. Next, authors proposes SimCLR-Rank, which is a variant of SimCLR. SimCLR-Rank sample negatives in SimCLR loss only from the same query group. Experimentally, authors show that pretrained models can outperform GBDTs, which is one of the strongest baselines, under label scarcity setting. Additionally, authors compare self-supervised methods (SimCLR, SimSiam, SimCLR-Rank) in various settings (datasets, data augmentation methods, outlier NDCG, etc.)

### Strengths
- Representation learning in tabular LTR has not been studied much.
- SimCLR-Rank provides a strategy specific to the structure of LTR task.

### Weaknesses
 - Technical novelty is limited.
- Datasets in experiments are limited to three datasets and one private dataset.
- Representation learning on tabular data not necessarily needs to consider LTR setting, since multi-layer MLP will be finetuned for LTR task. As a paper that proposes a new tabular self-supervised learning method, it lacks the comparison with other existing methods, such as
    - Hajiramezanali, E., Diamant, N. L., Scalia, G., & Shen, M. W. (2022, October). STab: Self-supervised Learning for Tabular Data. In *NeurIPS 2022 First Table Representation Workshop*.
    - Wang, W., KIM, B. H., & Ganapathi, V. (2022). RegCLR: A Self-Supervised Framework for Tabular Representation Learning in the Wild.
    - Ucar, T., Hajiramezanali, E., & Edwards, L. (2021). Subtab: Subsetting features of tabular data for self-supervised representation learning. *Advances in Neural Information Processing Systems*

### Questions
- What’s the intuition behind SimCLR-Rank working better?
- Why does pretraining improve outlier NDCG?
- Typically, pretraining has advantages by learning useful representations from large datasets, while this paper seems to use unlabeled data in the same downstream task for pretraining. Am I understanding correctly? Can pretraining in one downstream dataset transfer to other datasets?
- GBDT could use some well-known semi-supervised learning methods such as pseudo-labeling or consistency regularization to use unlabeled dataset. Do the pretraining methods still outperform GBDT with semi-supervised learning?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates the application of unsupervised pretraining to deep learning models for Tabular Learning-To-Rank (LTR) problems and demonstrates consistent outperformance of Gradient Boosted Decision Trees (GBDTs) and other non-pretrained rankers when there is more unlabeled data than labeled data. They introduce LTR-specific pretraining strategies, including the SimCLR-Rank loss, and show significant improvements in NDCG. Additionally, the paper highlights the superior performance of pretrained deep rankers, especially on outlier queries, in scenarios with limited labeled data.

### Strengths
1. This article is characterized by clear and comprehensible writing, presenting methods that are straightforward and easily implementable.

2. Through experimentation, this paper demonstrates that pre-trained deep models can achieve performance levels close to, or even surpass, GBDT in ranking tasks. This discovery holds practical value.

3. The paper introduces a pre-training approach that leverages the nature of learning to rank problems, demonstrating reasonable effectiveness, and in certain scenarios, outperforming simclr.

### Weaknesses
1. This paper exhibits notable deficiencies in the aspects of experimental comparisons and discussions on related work. The experimental comparison methodology only considers comparisons between fine-tuning or probing methods based on pre-trained models, as well as MLP models. I believe that in the realm of learning to rank and tabular data, there are likely more recent deep learning methods that could serve as baselines for comparison. Proper discussions about these methods should also be incorporated into the related work section. Currently, I find the discussion on related work to be inadequate. This would aid in addressing certain evident issues, such as whether current methods for using deep learning to learn tabular data also employ contrastive learning for pre-training and what distinguishes them from the approach presented in this paper.

2. Regarding the methodology, apart from applying SimCLR and SimSiam directly to pre-training for ranking tasks, the primary contribution of this paper is the SimCLR-Rank method. The key difference between this method and SimCLR lies in narrowing down the computation of contrastive learning from the entire batch to a single QG. This method possesses a degree of rationality and can effectively exploit the characteristics of the learning to rank task. However, in essence, this approach distills the semantic information contained in QG itself into the pre-trained model, similar to knowledge distillation (typically, QG is obtained through some form of retrieval, and the retrieval model can be viewed as a strong "teacher" model, while the pre-training model in this paper serves as a "student" model). Based on this observation, I believe that if the features from the retrieval model are input into GBDT, it could potentially achieve better performance, which is easily attainable in practical industrial applications. If this were the case, the application prospects of the method proposed in this paper would become rather limited.

3. In SimCLR, dissimilar embeddings correspond to smaller weights, while similar embeddings correspond to larger weights, indicating its adaptive ability to mine hard samples. In the learning to rank scenario, samples from the same QG should be relatively similar, and samples from different QGs should be dissimilar. This implies that the original SimCLR method, even when calculating softmax over the entire batch, primarily emphasizes the samples from the same QG, aligning with the role of SimCLR-Rank. Therefore, I believe that the potential improvement that SimCLR-Rank can bring to typical ranking situations may be somewhat limited. I hope the authors can provide further explanations regarding this issue.

### Questions
Please refer to Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies pre-trained DNN for tabular LTR problems, which is an underexplored problem. The major contribution of the paper is to identify areas where this might help, including query sparsity and label sparisity scenarios. Technically the paper proposes a loss function specific to ranking data nature based on existing contrastive learning objectives. Experiments are mainly compared against GBDT and DNN without pre-training, and it’s shown that there’re some benefits in the discussed scenarios. Experiments are also conducted offline on a private industry dataset.

### Strengths
S1: To the reviewer’s knowledge, this is the first work that shows some promises for pre-trained DNNs for the LTR task. The reviewer thought about the direction but It was not intuitively clear how to do it or if it has benefits. The paper still has several caveats but is a decent exploration in some aspects.

S2: the motivation of the ranking contrastive loss is clear and easy to understand - it is clear what the hard negatives are for LTR problems, so it is good to leverage that.

S3: It is good to identify two scenarios where pre-trained deep models might help, including query sparse and label sparse scenarios.

### Weaknesses
W1: change over SimCLR is incremental - the major weakness of SimCLR for non-ranking problems was complexity. The authors made a good point that hard negatives are clear for LTR (mentioned in S1), but SimCLR using small batches will likely largely resolve the issues? So the necessity for a new loss is not very convincing - in fact, the authors did not comprehensively compare with that baseline. - also, sometimes having easy negatives may improve the generalization of learning - this may need deeper study. SimSiam does not look to be a competitive baseline considering the factors. So the proposal of the new loss is not very convincing.

W2: extendability. The reviewer thought about this problem before and one major difference between tabular vs text is, tabular datasets assume a feature space, while text encoders are for text in general that is easy to generalize. E.g., one can easily add more text fields and everything is still kind of in the “text space”, but adding new features to the tabular table may completely invalidate the pre-training in the previous feature space. So when the feature space changes, which can be common in practice, the pre-training needs to be done again. Also, the pre-training needs to be done for each dataset separately, unlike text domains where one model may be sufficient. Thus pre-trained models on tabular datasets may be much limiting in general.

W3: It is unclear why no online results are provided for the industry dataset. Overall it is not clear how significant the results are in this section due to unclear baselines, private dataset, and unclear real-world implications.

### Questions
Please discuss the weaknesses listed above.
Typo in figure2 caption? non-pretrained counterparts?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
