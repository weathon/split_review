# Fairness without Sensitive attributes via Noise and Uncertain Predictions

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
While model fairness improvement has been explored previously, existing methods invariably rely on adjusting explicit sensitive attribute values in order to improve model fairness in downstream tasks. However, we observe the trend of sensitive demographic information being inaccessible as public concerns around data privacy grow. In this paper, we propose a confidence-based hierarchical structure of variational autoencoder (VAE) architectures called ``Reckoner" for reliable fairness learning under the assumption of missing sensitive attributes. First, we present the results of exploratory data analyses conducted on the widely-used COMPAS dataset. We observed significant disparities in model fairness across different levels of confidence. Inspired by these findings, we devised a dual-model system in which the model initialised with a high-confidence data subset learns from the model initialised with a low-confidence data subset, enabling it to avoid biased predictions. To maintain predictiveness, we also introduced learnable noise into the dataset, forcing the data to retain only the most essential information for predictions. Our experimental results show that Reckoner consistently outperforms state-of-the-art baselines on both the COMPAS and the New Adult datasets in terms of both accuracy and fairness metrics.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study tackles the problem of fairness without demographics by initially partitioning the training data into subsets characterized by low and high confidence. The rationale behind this division lies in the observation that low-confidence encodes fairness-related knowledge, while high-confidence pertains to discriminative information. The refinement process employs dual Variational Autoencoders (VAEs), where the high-confidence VAE extracts label-related features for classification. Simultaneously, it injects fairness knowledge from the low-confidence VAE, following an Exponential Moving Average (EMA) style. The low-confidence VAE operates in an unsupervised manner, with its latent representation encouraged to be proximate to the expectation of high-confidence samples. The efficacy of this approach is demonstrated on Adult and COMPAS datasets.

### Strengths
1) The problem of fairness without sensitive attributes is important and practical.

2) The writing of this article is well-organized.

### Weaknesses
1) (main concern) The proposed method is based on the observation that “when data is close to the decision boundary, non-sensitive information associated with those data tends to be similarly distributed across demographic groups, leading to lower accuracy but increased fairness”. However, it is unclear why and when it happens. For example, does this just happen to be due to the data distribution nature of the COMPAS dataset? The author should provide more explanations and discussions about this, theoretically or empirically, since this key property affects the scope of application of the proposed method.

2) It is also unclear that why the learnable noises need to be added in this paper. Is it to block information of sensitive information? In addition to the final classification results, I suggest that the author give some relevant analytical experiments to prove the validity of the learned noises. For example, if we train a classifier for sensitive attributes on the data with learned noises, is it difficult to predict sensitive attributes accurately?

3) (main concern) It seems that the compared baselines are not strong enough. Please note that some works have gone beyond the baselines used in this paper such as CvaR DRO, LfF, JTT. Moreover, only two tabular datasets are used. I encourage the author to perform experiments on more datasets to illustrate the effectiveness of the proposed method.

### Questions
Please refer to Weakness.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies how to mitigate bias when having no access to the full sensitive attributes. The idea is that they find empirically the low-confidence samples (predicted by a classifier) are more biased than the high-confident samples. Therefore, they train a classifier to split the data into low- and high-confidence subsets, and then train VAE on each data together, and the final prediction comes from both VAEs.

### Strengths
1. The problem is a practical and important problem given it is harder and harder to access full sensitive attributes

### Weaknesses
1. I have trouble understanding the high-level insights of the paper. The authors did not do a good job of presenting their method. e.g. why do they need VAEs? If the idea is to leverage low- and high-confidence data, why not just train two separate classifiers and then use ensemble? What is the purpose of adding learnable noise? I do not understand the author's explanation in 4.3.1. What is $\eta$ in Eq. (1)? What is the corresponding mathematical definition of "Pseudo-distribution" in Figure 1? Is it $\mathcal{L}_L$ in Eq.(2)? In general, I think the technical part is poorly written, and would cause unnecessary confusion to readers.

2. Can authors explain why the design can mitigate bias well when has no access to full sensitive attributes? The sensitive attribute $S$ is rarely mentioned after the problem formulation in Section 3. How does the method connect to missing $S$? I might miss it, but it shows the paper does not highlight how the method works.

3. The experiment on COMPAS does not seem to outperform other methods in an obvious way. The two fairness measures improve but the accuracy also drops. It would be clearer if the results could be presented in an accuracy vs. fairness Pareto frontier style plot.

4. The evaluation is done only on two tabular datasets. This is rare in fairness literature. Can authors justify why it is only tested on two tabular datasets?

### Questions
See weakness.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses "fairness without demographics" by first splitting the training data into low-confident and high-confident subsets because they observe that low-confident encodes the knowledge of fairness while high-confident is for discriminative information. The refinement is based on dual VAEs in which the high-conf one is to extract most label-related features for classification while simultaneously injecting fairness knowledge from the low-conf one (in an EMA style). Low-conf one is a set unsupervised whose latent representation encouraged to be close to high-conf samples's expectation. They demonstrated the idea on new Adult and COMPAS datasets.

### Strengths
1. The overall framework looks good and two stage presentation is clear and logical.
2. The idea of training dual VAEs for two subsets and passing fairness knowledge from low-conf to high-conf is interesting.
3. The improvement on New Adult dataset is significant in terms of EO metric.

### Weaknesses
1. The inconsistence between motivation, methodology, and experiments. It will be better if authors can position this paper in a more consistent way.
2. I felt that although authors tried to provide some hints before presenting a component of the method, some of the refinement techniques are still heuristic, which underscores the overall method quality.

I will give the detailed comments in Questions.

### Questions
1. In the first paragraph of Introduction, the evaluation to works that maximize the utility of the worst-case group is not precise. The Rawsian fairness (no sensitive attribute) based research leveraged side information (e.g., group ratio) to identify protected group, instead of relying on the correlation with observed features. Following this concern, DRO and ARL used as baselines in this paper are not very suitable, because they both highlighted that accuracy-related utility should be equal across different groups. Note that EO and DP are not criteria designed for these works, although you can conduct so.

2. Given a threshold of 0.6 for splitting the training dataset and the resultant subsets have the distinct performance on EO and DP, which might be questionable. Recalling the definition of EO and DP, we see that they are both computed over predicted y. Since low-conf data tend to appear near to decision boundary, they certainly will yield small EO and DP values. Thus, letting low-conf data represent fairness is not very convincing for me. OOD data is NOT unbiased data.

3. In the refinement stage, notice that only high-conf data will be trained for classification while low-conf examples only contributes some "fair features" in a regularization style. However, from Fig.2, the label in the purple box tried to suggest all data were well mapped to their ground truth labels. So, have you checked if the model has correctly classified low-conf data after training? If yes, why not incorporate a supervised loss therein? If not, how to guarantee a better generalization on test set?

4. As low-conf generator is thought having the desired fairness knowledge, then how about using its mu and sigma as a pseudo supervision (regression) for high-conf data? Any theoretical or experimental evidence of your method? Basically, you are minimizing the distance between any two of N(mu1, sigma1), N(mu2, sigma2), and N(0,I).

5. Generator in the method should refer to the entire VAE. As the final model only takes encoder, can you clarify the role of decoder during training? 

6. Two compared methods are from Chai's recent work, leading me to check the connection with this baseline. In Chai's work, they have pointed out the samples near to the decision influence the fairness, while this paper starts from confidence, similar to my insight mentioned above. Authors should clarify their connections.

7. The applied baselines are not very supportive to the targeted challenges. I felt confused why using proxy attributes and fairness-accuracy trade-off works are not included. Also, why only two datasets are used in the paper? Are the proposed method restricted to some specific datasets? 

8. Regarding the learnable noise, it is like a patch to this framework, as you have to learn additional model parameters. To make latent features only related to label, one can encourage H(z,y) and reduce H(x,z), from the information theory perspective.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
