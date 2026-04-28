# Dynamic Post-Hoc Neural Ensemblers

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
Ensemble methods are known for enhancing the accuracy and robustness of machine learning models by combining multiple base learners. However, standard approaches like greedy or random ensembles often fall short, as they assume a constant weight across samples for the ensemble members. This can limit expressiveness and hinder performance when aggregating the ensemble predictions. In this study, we explore employing neural networks as ensemble methods, emphasizing the significance of dynamic ensembling to leverage diverse model predictions adaptively. Motivated by the risk of learning low-diversity ensembles, we propose regularizing the model by randomly dropping base model predictions during the training. We demonstrate this approach lower bounds the diversity within the ensemble, reducing overfitting and improving generalization capabilities. Our experiments showcase that the dynamic neural ensemblers yield competitive results compared to strong baselines in computer vision, natural language processing, and tabular data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces "Neural Ensemblers," a novel approach that uses neural networks to dynamically weight ensemble members for each input instance. Authors propose regularization technique of randomly dropping base model predictions during training.

### Strengths
- Paper is well written.  
- Experimental results span different modalities

### Weaknesses
 - Benefit of the proposed method is not super clear in Table 2. Given the variance of different methods, efficacy of the proposed method is unclear

- POC example given in the paper can be misleading as their dynamic ensemblers train more parameters as compared to baseline. It remains unclear if this would be a problem in the first place if we could train base models that are sufficiently overparameterized

- It remains unclear what are the main reasons due to which the proposed methods improves on top of simple ensembling baselines.

- Post-hoc ensembling in the name can be misleading for someone who is not aware of the literature. In particular, to obtain the ensemble we need to train the parameters of the ensemble model.

I am not very well aware of the literature to comment on the novelty of paper, so I will leave that on other reviewers and the area chair.

### Questions
- It is not clear when dynamic ensemblers would benefit? Is it the case that dynamic ensemblers improve because base models underfit the data? Does benefit of these ensemblers persist in cases when the base models are over parameterized neural networks? 

- More data is needed to train the parameters of the dynamic ensemblers  It is unclear if we can reuse the training data used for base models or do we need more training data? In case we need more training data, a favorable comparison would be using that data in the first place for base models and perform standard ensembling techniques.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Dynamic Post-Hoc Neural Ensemblers for replacing the traditional ensemble method. Their main contribution is the use of two MLPs to dynamically generate weights for ensemble members. Additionally, when training these MLPs, they randomly drop base models to reduce overfitting and improve generalization capabilities. Lastly, their empirical results demonstrate that Neural Ensemblers consistently form competitive ensembles across diverse data modalities, including tabular data (classification and regression), computer vision, and natural language processing.

### Strengths
**Innovative Approach:** The paper introduces Dynamic Post-Hoc Neural Ensemblers,  aiming to generate dynamic weights for ensemble members.

**Reduced Overfitting:** By randomly dropping base models during training, the method addresses overfitting and potentially improves generalization.

**Empirical Validation:** The paper provides empirical results showing the method’s outperformance and robustness across diverse datasets.

### Weaknesses
1. The study lacks consideration of computational efficiency. The Neural Ensemblers’ performance depends on a strong subset of 50 base models, selected by `DivBO`, which may increase computational requirements. The author should compare the Neural Ensembler's performance with that of a single model of equivalent size to better evaluate its efficiency. For example,  to evaluate Neural Ensember, the author could provide some specific efficiency metric comparisons, such as training time, inference time, or memory usage compared to baseline methods, or analyze the computational complexity of their approach. 

2. My review of the author's code confirmed that the meta-datasets are limited to a tabular format, making the paper's description somewhat vague. A clearer explanation of the data structure would have been beneficial. Otherwise, the application scope should be limited to tabular data or metadata in a tabular format from fields like computer vision or natural language processing. 

In line 126, the author states that NasBench 201 is a neural architecture search (NAS) method for computer vision (Dong & Yang, 2020). However, I think the Neural Ensembler is actually trained on tabular data, as indicated in the code at SearchingOptimalEnsembles/metadatasets/nasbench201/metadataset.py, lines 93-95. The author can compare the following two different pipelines:
- The author selects some base models and computes their predictions for each example. These predictions are then stored in tabular data format as examples to generate the training set. Lastly, train the Neural Ensembler on this set.
- Freeze all base models. Then, sample a mini-batch of examples from the raw training set. Lastly, Train the Neural Ensembler to generate the weights.

I believe the second schema is worth considering because 1) the input is raw data from the dataset, not the predictions from base models, 2) data augmentation can be used to avoid overfitting, and 3) for some recognition tasks, such as object detection, the predictions of different base models cannot be aligned, making it impossible to store base models' predictions in a tabular format.

I guess that the author may have used too many base models to construct the Neural Ensembler, which made it hard to train in the second mode with limited computing resources. This is just my guess, so I provide several solutions in the questions section for the author to refute this weakness.

### Questions
Overall, this paper requires some clarifications on theory and experiments. Given these clarifications, if provided in an author's response, I would consider increasing the score. 

---

For the experiments, `any of the following` should be addressed.

1. We note that the authors compare the Neural Ensembler to a single model (see **lines 321-322**). It would have been better also to explore the efficiency of the Neural Ensembler, particularly considering the **number of model parameters** or **FLOPS** (see [1]). Otherwise, model scaling is a better choice for improving model performance. For example, we have a list of models:

| Model    | # Params | Acc@1  |
| -------- | -------- | -------|
| VGG19    | 143.7M   | 72.376 |
| ResNet18 | 11.7M    | 69.758 |
| ResNet34 | 21.8M    | 73.314 |
| ResNet50 | 25.6M    | 76.13  |
| ViT-B16  | 86.6M    | 81.072 |

- If ResNet18 and ResNet34 are used as base models for the Neural Ensembler, the Neural Ensembler’s performance should exceed that of ResNet50 due to its higher parameter count of over 33.5M (11.7M + 21.8M). 
- When comparing with the VGG16 baseline, we should avoid using ResNet18, ResNet34, ResNet50, or ViT-B16 as base models for the Neural Ensembler, as each has better performance and a smaller scale.
- To demonstrate the advantages of the Neural Ensembler in computer vision and natural language processing, the author should use corresponding neural networks as base models and conduct experiments on image or text datasets.

2. It's important to note that the paper focuses on post-hoc ensembling of pre-trained models, rather than training base models from scratch. Thus, the author can clarify how their method compares the computational cost to other post-hoc ensembling methods.


[1] Shazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., & Dean, J. (2017). Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. arXiv preprint arXiv:1701.06538.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
A common approach to combining predictions from multiple ensemble members is to assign equal weights to each prediction, as seen in hard and soft voting methods. However, it is clear that certain ensemble members may offer better predictions for specific instances, and it leads to the concept of weighted voting. This work proposes obtaining such instance-wise ensemble weights through a separate neural network, referred to as the Neural Ensembler.

### Strengths
1. The problem statement is well-motivated; it would be beneficial to adaptively determine ensemble weights for a given instance.

2. The authors propose two setups: "stacking" and "model-averaging." In the stacking setup, the Neural Ensembler directly outputs the ensembled prediction. In contrast, the model-averaging setup has the Neural Ensembler provide the weights for each ensemble member. While the stacking setup aligns with the ultimate goal of obtaining an ensembled prediction, the model-averaging setup is also valuable as it explicitly reveals the contribution of each ensemble member.

### Weaknesses
1. There are concerns about fair comparison since the proposed Neural Ensemble ultimately learns from additional validation data. While baseline methods also train statistical models based on validation data, the issue is that the Neural Ensemble is significantly larger than the baseline methods. For example, methods like Greedy, Quick, and BO train statistical models with $M$ (unnormalized) ensemble weights as parameters. In contrast, NE-Stack trains a statistical model (neural network) with $D \times 32 + 32 \times 32 + 32 \times 32 + 32 \times D$ parameters, which amounts to $2688$, $8448$, and $66048$ parameters for $D=10$, $100$, and $1000$, respectively. Given the significant difference in the scale of the introduced statistical models, ranging from hundreds to tens of thousands of times larger, it is questionable whether introducing the same additional validation data could make a fair comparison. The concern is not simply about using validation data, but the vastly different capacity of the models being trained on it. The Neural Ensembler, with its significantly higher parameter count, has a greater capacity to overfit to the validation set, potentially leading to an inflated performance advantage that does not generalize well to unseen data. This discrepancy in model complexity makes it difficult to isolate the true benefit of the proposed instance-specific weighting approach.

2. I believe the assumption of having a sufficiently large amount of validation data, which can be used to train the neural network model, is quite strong. If the "Avg. samples for Validation" shown in Table 1 indicates the size of the validation dataset used to train the Neural Ensembler and the statistical models of the baseline methods for each dataset, it appears particularly large for NASBench and FTC. Conducting an ablation study on this would be valuable to assess how much validation data is necessary for the Neural Ensembler to be effective. Currently, the only ablation study presented is on the dropout probability, aimed at preventing overfitting on the given validation data. The lack of an ablation study on the validation set size is a significant oversight, as the performance of the Neural Ensembler is likely to be highly dependent on the amount of available validation data. Without this analysis, it is difficult to assess the practical applicability of the method in scenarios with limited validation data.

3. Additionally, the Neural Ensembler is implemented using an MLP architecture with a hidden dimension of 32 and a depth of four. Such architectural choice also warrants an ablation study; a model that is too large may incur significant costs and increase overfitting, while one that is too small may not perform adequately. Currently, there is no discussion regarding the size of the Neural Ensembler model. The specific choice of 4 layers with a hidden dimension of 32 seems arbitrary without any justification or exploration of alternative architectures. The performance of the Neural Ensembler could be highly sensitive to these architectural parameters, and without an ablation study, it is difficult to determine if the chosen configuration is optimal or if the observed performance is simply due to a lucky choice of hyperparameters.

4. The key feature of the proposed Neural Ensembler is its ability to adjust the weights of each ensemble member in an instance-specific manner, either implicitly (in a stacking setup) or explicitly (in a model-averaging setup). However, there is currently no direct evidence regarding its effectiveness from this perspective. One potential approach could involve directly learning the weighting coefficients for each instance (i.e., oracle) and evaluating how closely the ensembled predictions (or ensemble weights in the model-averaging setup) generated by the Neural Ensembler align with them. Without such analysis, it remains unclear if the Neural Ensembler is truly capturing instance-specific patterns or if it is simply learning a more complex, but not necessarily more effective, weighting scheme. The absence of a direct comparison with an oracle weighting scheme is a significant limitation in validating the core claim of instance-specific adaptation.

5. Above all, are the values reported in the tables the averages and standard deviations of the results for the sub-datasets within each meta dataset? The fact that nearly all results overlap within the range of standard deviations suggests that the experimental results may not be statistically significant. A clear clarification on this matter seems necessary. The lack of statistical significance would severely undermine the validity of the experimental results. It is crucial to establish whether the observed performance differences are statistically meaningful or simply due to random variation.

### Questions
1. I think the assumption of having a sufficiently large amount of validation data (that can be used to train the neural network model) is quite strong. In such cases, further exploration of existing methodologies based on well-grounded principles (such as Bayesian principles) would be valuable.

2. Specifically, one can approximate the model probability in Bayesian model averaging using the Bayesian Information Criterion (BIC), where the likelihood is estimated from the validation set.

3. Following BIC, the harmonic mean estimator and its variants come to mind. A recent relevant work is "Machine Learning Assisted Bayesian Model Comparison: Learnt Harmonic Mean Estimator" by McEwen et al. (2023). Have you explored such classical methods grounded in Bayesian principles alongside BO-based approaches?

4. I recognize the value of presenting normalized metrics for relative comparisons in the main text. However, it would be helpful to include the raw numbers in the appendix. Relying solely on relative metrics can make it challenging to assess the significance of the results for each methodology.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces a novel approach to post-hoc ensembling using neural networks, termed "Neural Ensemblers." These ensemblers dynamically generate weights for each base model in the ensemble on a per-instance basis, addressing the limitations of static ensembling methods. The authors propose a regularization technique inspired by DropOut in deep learning to mitigate the risk of overfitting and diversity collapse. The method is evaluated across various data modalities, including tabular data, computer vision, and natural language processing, demonstrating competitive performance against strong baselines.

### Strengths
1) The introduction of Neural Ensemblers as a dynamic post-hoc ensembling method is a significant contribution to the field. The use of neural networks to dynamically assign weights to base models on a per-instance basis is a novel and effective approach.

2) The proposed regularization technique, which involves randomly dropping base model predictions during training, is theoretically sound and empirically validated. This technique effectively mitigates the risk of overfitting and enhances ensemble diversity.

### Weaknesses
While the paper mentions the use of a fixed set of hyperparameters across all experiments, it does not explore the sensitivity of the Neural Ensemblers to hyperparameter changes. A more detailed analysis of hyperparameter tuning, specifically examining the impact of varying the number of layers and hidden dimensions within the neural ensembler, could provide deeper insights into the robustness and generalizability of the proposed method. This is crucial to understand the method's performance across different datasets and tasks. 

Does the author carefully tune the hyper-parameters of other baselines e.g., XGBoot?

The author should also compare their method with other advanced methods, e.g., LightGBM, CatBoot, which can be directly used in the open source libraries. The absence of LightGBM, which is known for its efficiency and performance on tabular data due to techniques like Gradient-based One-Side Sampling (GOSS) and Exclusive Feature Bundling (EFB), is a significant oversight. 

Lack of references and comparisons to Ensemble NN [1] and SCARF [2]. Both of these papers explore the ensemble or pretraining in Deep neural networks on tabular datasets.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
