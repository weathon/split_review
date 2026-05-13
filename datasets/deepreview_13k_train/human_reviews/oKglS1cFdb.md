# Feature Accompaniment: Is It Feasible to Learn Out-of-Distribution Generalizable Representations with In-Distribution Data?

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Learning representations that generalize out-of-distribution (OOD) is critical for machine learning models to be deployed in the real world. However, despite the significant effort in the last decade, algorithmic advances in this direction have been limited. In this work, we seek to answer the fundamental question: is learning OOD generalizable representations with only in-distribution data really feasible? We first empirically show that perhaps surprisingly, even with an "oracle'' representation learning objective that allows the model to explicitly fit good representations on the training set, the learned model still underperforms OOD in a wide range of distribution shift benchmarks. To explain the gap, we then formally study the OOD generalization of two-layer ReLU networks trained by stochastic gradient descent (SGD) in a structured setting, unveiling an unexplored OOD generalization failure mode that we refer to as feature accompaniment. We show that this failure mode essentially stems from the inductive biases of non-linear neural networks and fundamentally differs from the prevailing narrative of spurious correlations. Overall, our results imply that it may be generally not feasible to learn OOD generalizable representations without explicitly considering the inductive biases of SGD-trained neural networks and provide new insights into the OOD generalization failure, suggesting that OOD generalization in practice may behave very differently from existing theoretical models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work tries to answer "Can we learn OOD generalizable representations from in-distribution data?" empirically and theoretically. 

In the empirical part, the term **OOD generalizable representation" mainly indicates a representation that contains rich features. The author investigates the OOD linear probing performance of three kinds of pretrained models: 1) a CLIP pretrained model on super large&diverse dataset; 2) a supervised pretrained model on Imagenet dataset; 3) a supervised pretrained model on Imagenet dataset with more objective information (i.e. prediction the representation of a CLIP model). 

The author treats the 3rd model as the oracle objective function --- *"representation learning objective itself cannot be further improved in general"*. Hence concludes that *"OOD generalizable representations may not be learnable using only ID data without explicitly taking into account the inductive biases of the model or the task."*

In the theoretical part, however, the term **OOD generalizable representation** changes to indicate "a representation that doesn't contain spurious signals (or background feature signals) and only contains invariant signals (or core feature signals). The author uses a 2-layers Relu network to show that --- a non-convex network (especially with asymmetric activations) could "learn and store" some background feature signals in the representation even though these background features have no correlation with the target label.

### Strengths
- It is interesting to investigate out-of-distribution generalization problem through the rich-representation (a representation contains a rich set of features that could be redundant in-distribution but crucial out-of-distributation) point of view.  

- It is also interesting to show that a non-convex network could "learn and store" some irrelative signals (per-example level spurious features) in the representation even though these signals are not (or weakly) correlated with the target label in the whole-dataset level.

### Weaknesses
 - As I commented in the **Summary**, the empirical part and theoretical part use different principles. So that they can not support each other. Please check **Summary** for details. In my opinion, that is the biggest weakness.

- In the empirical part, this work treats "good OOD linear probing performance" as "good generalization representation" (Figure 1). The principle here is "rich-representation"[1][2]. I suggest the author clarify the principle. 

- The author treats -- a supervised pretrained model on Imagenet dataset with more objective information (i.e. prediction the representation of a CLIP model) -- as the **oracle** objective function. By comparing this model (pretrained on Imagenet) with CLIP (pretrained on a large dataset), the author concludes that *"OOD generalizable representations may not be learnable using only ID data without explicitly taking into account the inductive biases of the model or the task."*

On one hand, this comparison doesn't support the conclusion. From the rich-representation's principle (which is used in the linear probing experiment), OOD linear probing benefits from a representation that contains diverse and simple features. Indeed, CLIP (pretrained on a large dataset) contains rich features. But please remember that CLIP uses more data. It is possible that the model  above (pretrained on Imagenet) is already the best (by say "best", I mean a model that achieves the best OOD linear probing performance) imagenet pretraining model. In short, CLIP model (pretrained on a large dataset) should not be assumed as an achievable upper bound of other Imagenet pretrained model. 

On the other hand, this Imagenet pretrained model is not **oracle** in terms of rich-representation. Compared with Imagenet's 1k target categories, indeed this object contains more supervision information (with the help of CLIP and CLIP's pretraining dataset). But how about 22k target categories, for example? 

- The theoretical section didn't discuss the relationship between works about SGD and features, e.g. [3][4][5].

### Questions
- please see weaknesses

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tries to study whether it is possible to learn OOD-generalizable representations with only in-distribution data. The authors discover a new failure model that they refer to as feature accompaniment, which is caused by the inductive biases of training process of nonlinear neural networks.

### Strengths
* This paper studies OOD from the perspective of inductive bias, which has rarely considered in existing literature. They consider the training process of neural network, which is more practical than directly considering the global minimum.
* From their theoretical analyses, they find an interesting failure mode ''feature accompaniment''. In my understanding, this means that due to the asymmetry of activation, each neuron tends to correlate more with one class than another. Then, this can further make the projection of gradients onto background features non-zero, which makes the final model also use background features to classify. I think this ''feature accompaniment'' may be a very fundamental phenomenon caused by the asymmetry of activation, which can also be used to understand other properties of neural network. I think my own research can draw some inspiration from it.

I hope to obtain more insights from upcoming discussions with the authors and I'm happy to further raise my score.

### Weaknesses
 * I think the experiment part in Section 2 is a bit disconnected from the theoretical part in Section 4. They consider different settings and different learning objective. I don't think theory in Section 4 can explain the experimental results in Section 2. Specifically, the experiments in Section 2 focus on a distillation setup with a pre-trained teacher model and a student model trained on a subset of the data, while the theory in Section 4 analyzes the training dynamics of a single model trained from scratch using ERM with regularization. The learning objectives are also different; Section 2 uses a distillation loss, while Section 4 considers a standard classification loss. This makes it difficult to directly relate the empirical observations to the theoretical findings. I know that Section 2 is probably just a starting point of studying whether OOD-generalizable representations are learnable, so this's okay. But I think it could be better to connect them more in the writing. 
* The training process the authors mainly studied is based on ERM with regularization. Since there is only one training domain, this is okay. But I want to know if there are several domains whose background distributions are different, will the training process of Equation (1) (instead of ERM) still cause "feature accompaniment"? Are there any cases even if we have multiple domains we can still not learn a OOD-generalizable neural network?

### Questions
Please see Cons.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers the question of whether it is feasible to learn good representations for OOD generalization with only ID data, without considering inductive biases of the architecture and learning algorithm. First, the paper looks at an experiment where models are trained to learn the features of pretrained models that exhibit good OOD performance. It is found that these distilled models have OOD performance better than standard models only trained on the ImageNet training set, but not as good as the original pretrained models, suggesting that it is not possible to learn good OOD representations from ID data, even given access to “oracle” representations known to perform well OOD. Via theoretical analysis of 2-layer ReLU networks, the paper then unveils a novel failure mode of OOD generalization called feature accompaniment. This failure mode is shown theoretically to stem from inductive biases of nonlinear networks, and is absent in deep linear models.

### Strengths
* The paper identifies a novel and intuitive failure mode of out-of-distribution generalization, distinct from the prevailing attention on spurious correlations
* The paper provides principled theoretical foundations that prove the existence of this failure mode for 2-layer
* The takeaways of the study are applicable to future theoretical study of OOD generalization. In particular, the paper attempts to make the highly of-interest case that existing theoretical models of OOD generalization may not cover why OOD generalization failure happens in practice.

### Weaknesses
 * The claim in Section 2 of the existence of an OOD generalization failure mode beyond the reach of generalization theory, and related to feature learning may not be fully justified by the empirical results in the section. Please see Question 1 below.
* The study does not suggest how one might make the findings actionable in an empirical setting to improve or predict OOD generalization ability. It is thus unclear how significant the results or the identified failure mode are.
* Relatedly, the paper does not make a case for how much OOD generalization failure is attributable to this failure mode in empirical settings, if any at all.

### Questions
Question 1:
I am unconvinced that the empirical results of section 2 imply the existence of a failure mode related to the feature learning process. The empirical result may not necessarily be due to nonlinear feature-learning dynamics in this experiment, but rather just that pre-trained CLIP models contain features covering a much larger data distribution than is captured by models distilled on ImageNet. In particular, if you distill a model from CLIP on the ImageNet training set, are some CLIP features that are not represented in ImageNet not likely to be left out? These features could still be helpful in OOD classification. For example, the OOD bird and car could have core features that look different from the core features seen in-distribution. Pretrained models may contain these features, while distilled models may not have learned them if they do not appear in the training set.


Question 2:
Could there be discussion on how feature accompaniment relates to the previous studies on simplicity bias and gradient starvation [1,2], which find that networks rely on simple features and ignore more complex features? In particular, work on Gradient Starvation [2] suggests that an increase in strength of a simpler feature inhibits the learning of other more complex features. Are these results contradictory to those suggested by feature accompaniment?



[1] The Pitfalls of Simplicity Bias in Neural Networks, https://arxiv.org/abs/2006.07710

[2] Gradient Starvation: A Learning Proclivity in Neural Networks, https://arxiv.org/abs/2011.09468

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
