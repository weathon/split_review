# Scaling Laws for Sparsely-Connected Foundation Models

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
We explore the impact of parameter sparsity on the scaling behavior of Transformers trained on massive datasets (i.e., ``foundation models''), in both vision and language domains.
In this setting, we identify the first scaling law describing the relationship between weight sparsity, number of non-zero parameters, and amount of training data, which we validate empirically across model and data scales; on ViT/JFT-4B and T5/C4.
These results allow us to characterize the ``optimal sparsity'', the sparsity level which yields the best performance for a given effective model size and training budget. For a fixed number of non-zero parameters, we identify that the optimal sparsity increases with the amount of data used for training. We also extend our study to different sparsity structures (such as the hardware-friendly n:m pattern) and strategies (such as starting from a pretrained dense model).
Our findings shed light on the power and limitations of weight sparsity across various parameter and computational settings, offering both theoretical understanding and practical implications for leveraging sparsity towards computational efficiency improvements.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a formulation of scaling laws for sparsely-connected foundation models. Beginning with the scaling laws proposed by previous works, which are related to the parameter count N and the amount of training data D, the authors add parameter sparsity S into consideration and construct a formulation based on observations and actual data points. After obtaining the formulation, the authors investigate the optimal sparsity and limit performance for training sparse models. Furthermore, the authors consider two practical applications, including N:M sparsity and pruning, to validate the scaling laws.

### Strengths
1. This paper investigates a topic highly relevant to current trends in large-scale models, namely the scaling laws of sparse large models. The authors present the formulation of scaling laws along with their derivation process and validate them on T5 and ViT models.
2. The authors also validate several applications related to scaling laws, providing reasonable experimental designs and detailed experimental results.
3. The writing throughout the article is quite commendable.

### Weaknesses
1. This paper investigates a topic highly relevant to current trends in large-scale models, namely the scaling laws of sparse large models. The authors present the formulation of scaling laws along with their derivation process and validate them on T5 and ViT models.
2. The authors also validate several applications related to scaling laws, providing reasonable experimental designs and detailed experimental results.
3. The writing throughout the article is quite commendable.

1. This paper posits that sparsity can reduce training costs, thus presenting research on optimal sparsity. However, in reality, the training costs of current sparse training methods are often the same as those without sparsity. Under these circumstances, is it meaningful to study optimal sparsity?

### Questions
Please refer to the weakneses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The key message of this paper is a scaling law describing the relationship between sparsity (weight sparsity rate), the number of nonzero parameters, and the amount of training data proposed. The most intuitive effect on our training of sparse models is that for a fixed number of non-zero parameters, it is found that optimal sparsity increases with the amount of data used for training. And the benefit of long training seems more obvious compared with dense models. The experiments are using Vision Transformer and T5 language models and conducted on large-scale C4 and JFT4B datasets.

### Strengths
This study is the first paper to use large-scale experiments and theoretical analysis to explore in detail the effects of sparsity on neural network training and efficiency. The authors propose new scaling laws describing the relationship between sparsity, the number of non-zero parameters, and the amount of training data, which is important.
On the one hand, the findings of this paper can help us configure the training parameters more scientifically and thus improve the efficiency and performance of the model in large-scale training. It also shows that as the amount of training data increases, the model sparsity required to achieve optimal performance also rises. In this case, appropriately increasing the model sparsity and optimizing the model structure may be a more effective solution.
Meanwhile, according to this finding, the sparsity of the model can be dynamically adjusted according to the change in data volume during the training process to balance the model performance and computational cost better.

### Weaknesses
Overall, I think this is a good paper; my only concern lies in the scale of the data and modeling. Compared to Chinchilla's law, the author's data and model sizes are significantly smaller. Also, since the authors mentioned the optimal sparsity setting as an empirical design or product of this claim, could you elaborate on what specific improvements in downstream task or operational efficiency the sparsity of our actual model would bring us under the authors' theoretical guarantee?

### Questions
Please see the weakness.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studied the scaling laws for sparse foundation models. Specifically, they built a scaling law for how sparse models would perform as a function of sparsity, model size and pre-training data size. The authors evaluated on ViT and T5 architectures and showed that the constructed scaling laws can be used to easily predict the optimal sparsity without manually re-training the models.

### Strengths
1. The experimental results are comprehensive. I appreciate that the authors include experiments on hardware friendly structured sparsity.  
2. Deriving scaling laws for sparse foundation models is important. As foundation models require huge compute to train, understanding their scaling behavior and relationship to sparsity is crucial for predicting model performance.  
3. The empirical results show that ViT and T5 show strong scaling curves for sparsity and their performances can be well predicted from the constructed scaling law.

### Weaknesses
1. My main concern lies in the contribution of section 2 on fair evaluation, which argued that a sparse network should be compared with a dense model with the same number of parameters and compute. A very similar argument is made in [1] (See “training budget” in section 3), which argued that the compute budget for comparing sparse and dense models should be the same. It would be good to clarify the differences to [1] in the paper.
2. The evaluation on the encoder-decoder architecture T5 seems limited. The paper do not evaluate the more popular autoregressive decoder-only architecture but the original scaling laws is built on such autoregressive language models.

### Questions
1. I am curious as to whether lottery ticket hypothesis would hold as to foundation models, as it is the most impactful pruning paper in recent years. Since this work is closely related, i am wondering if the authors have explored the LTH setting for sparse training. If not, it would be good to add a discussion on LTH [2].   
2. Can the proposed scaling laws be useful in the extreme sparsity regime, e.g. 95% or even 99%? Or is it applicable only for the sparsity level within a range? 

[2] The Lottery ticket hypothesis: Finding Sparse, Trainable Neural Networks. ICLR 2019.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work uses scaling law to describe the relationship between weight sparsity, number of non-zero parameters and amount of training data.

### Strengths
1, In-depth investigation of the relationship between validation loss and sparsity, number of non-zero parameters and training data. Useful for understanding sparsification better.

2, Derived optimal sparsity for a given inference size and training budget.

### Weaknesses
1, Experiments are only tested on two examples. Though due to limited resources, more examples may be challenging, two examples may not be very convincing.

2, The scaling law has too many degrees of freedom (7 free parameters) that could be hard to generalize to new dataset without sufficient information.

### Questions
1, What are the 7 free parameters fitted and how are these parameters changes for different dataset and different hyperparameters $N, D, S$?

2, Procedure to identify $S_{opt}$ in 2.2 Optimal Sparsity is confusing. Could you explain this procedure with more details?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
