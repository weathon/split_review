# Impact of Dataset Properties on Membership Inference Vulnerability of Deep Transfer Learning

- Decision: Reject
- Scores: 3, 3, 8, 3

## Abstract
We analyse the relationship between privacy vulnerability and dataset properties, such as examples per class and number of classes, when applying two state-of-the-art membership inference attacks (MIAs) to fine-tuned neural networks. 
We derive per-example MIA vulnerability in terms of score distributions and statistics computed from shadow models.
We introduce a simplified model of membership inference and prove that in this model, the logarithm of the difference of true and false positive rates depends linearly on the logarithm of the number of examples per class.
We complement the theoretical analysis with empirical analysis by systematically testing the practical privacy vulnerability of fine-tuning large image classification models and obtain the previously derived power law dependence between the number of examples per class in the data and the MIA vulnerability, as measured by true positive rate of the attack at a low false positive rate.
Finally, we fit a parametric model of the previously derived form to predict true positive rate based on dataset properties and observe good fit for MIA vulnerability on unseen fine-tuning scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the impact of dataset properties on membership inference attacks (MIAs). The authors analyze two state-of-the-art MIA methods, LiRA and RMIA, by deriving a relationship between dataset properties (e.g., number of examples per class) and MIA vulnerability. They introduce a simplified model for membership inference and demonstrate that a power-law relationship exists between per-example MIA vulnerability and the dataset's properties. The authors also fit a regression model to predict MIA vulnerability, providing insights into privacy risks for fine-tuned classifiers.

### Strengths
1.	The paper formalizes the effect of dataset properties on membership inference vulnerability for two advanced MIA methods (LiRA and RMIA), enriching the analytical framework for MIA.
2.	The study includes a comprehensive and well-designed set of experiments across multiple datasets.

### Weaknesses
1.	In the abstract and introduction, the authors emphasize that their focus is on the privacy analysis of fine-tuned image classification models. However, sections 2 and 3 lack specific analyses that are tailored to fine-tuned neural networks, relying instead on a general theoretical model. The theoretical model does not explicitly account for the nuances of fine-tuning, such as the transfer of knowledge from the pre-trained model or the potential for overfitting on the target dataset, which could significantly impact MIA vulnerability. The analysis should include how the pre-training dataset and the fine-tuning process affect the observed power-law relationship.
2.	The authors need to clarify the differences in membership inference vulnerability between standard image classification models and fine-tuned models. This would strengthen the argument for fine-tuning as a key focus in their work. It is unclear whether the observed power-law relationship is unique to fine-tuned models or if it is a general property of all models. The paper should include a comparative analysis between models trained from scratch and fine-tuned models to highlight the specific vulnerabilities introduced by fine-tuning.
3.	As the regression model is presented as one of the main contributions, the methods section would benefit from a more detailed description of this model, its design, and its implementation process. The paper lacks details on the specific features used in the regression model, the choice of regression algorithm, and the evaluation metrics used to assess the model's performance. Without these details, it is difficult to assess the validity and generalizability of the regression model.
4.	Although LiRA and RMIA are currently the best methods, it is also necessary to analyze other MIA methods to validate the generalizability of the proposed arguments. The paper should consider other types of attacks, such as those based on prediction probabilities or confidence scores, to ensure that the observed power-law relationship is not specific to the chosen attack methods. This would strengthen the claim that the power-law relationship is a fundamental property of MIA vulnerability.

### Questions
1.	As the authors mention in the introduction, prior work has already explored the impact of the number of examples per class (shots) on MIA vulnerability. How does this study differ from previous work, and what new insights does it provide beyond existing findings?
2.	While LiRA and RMIA represent state-of-the-art approaches in MIA, it is also essential to assess the generalizability of the presented results to other MIA techniques. How might other methods differ in vulnerability patterns under the same dataset conditions?
3.	As a widely used method for privacy protection, it is necessary to discuss the impact of differential privacy on the arguments presented in this paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a theoretical result that links the success of membership inference attacks (MIAs) to the number of training data points per class. This theoretical link is shown for the RMIA and LiRA attack, and empirical evaluation is performed through fine-tuning vision encoders on multiple downstream datasets.

### Strengths
First, I'd like to note that I did enjoy reading the paper: it is clearly written, nicely presented, and well executed. Particularly the plots are extremely visually appealing.

Overall, the attempts to provide some interesting theoretical underpinning for a long known and well studied problem.

### Weaknesses
The core weaknesses of the paper can be grouped as follows:

**Studying a well established problem, while not taking prior work into account**

The underlying causes of MIA risks have been studied in a long line of work since 2017. The findings made in the paper, showing that vulnerability decreases as you have more samples per class, and with fewer classes have been made already. Hence, the expected impact and relevance of the presented findings is negligible. Given the enormous amounts of prior work, it is particularly surprising that the paper does not even have a related work section.

This section could start at early work. E.g. [1] (2021) has an extremely related approach where they assign privacy risk scores that implicitly expresses a similar phenomenon: with the probability of a sample being part of the training set yielding a per point privacy risk: here, it is over classes. Additionally, they add a very valuable angle (not considered in this present work here excessively): Classes with less members have on average lower probability: "the class labels with high generalization errors tend to have higher privacy risk scores".
Given the results by [2], this seems extremely crucial to analyze. For the given work, I am wondering how much this power law connection really holds when data is not well curated. We can imagine a really "malformed" class that consists of extremely rare and outlier data points with high variance. How much will having more of those really help reduce membership risk?
Starting from these works, a related work section could help put the given work into context.

Additionally, another line of work that needs to be taken into account is the one around [3,4,5] where it has been shown that with less data points per class, the class is more vulnerable and that privacy attacks have disparate success.

**Generality of Results**

While LiRA and RMIA are *current* state-of-the-art, it is, undoubtably reasonable to derive the bounds for those concrete attacks. However, the results are presented "as is", i.e., without embedding them into any broader context and without generalization. This makes it questionable, how well the results will age, i.e., how much can we benefit from them in 2-3 years, when LiRA and RMIA are obsolete and have been replaced by new and more powerful attacks.

In a similar vein, a suggestion would be to improve the writing in Section 3.4. The results are interesting, but it is not discussed what they mean: "Hence we can have the LiRA vulnerability arbitrarily close to zero in this non-DP setting by simply increasing S" -> this seems to mean that if every class has more and more train data, the membership risk decreases. Formulating such intermediate "checkpoints" in plain English would be genuinely helpful to position the results.

**Evaluation done for fine-tuning might skew the results**

Overall, I am not convinced that the chosen evaluation setup is sensible for the presented results. The paper considers transfer learning where the heavy lifting is done by a pre-trained vision encoder. However, the pre-training data itself has a distribution that will play a role for the vulnerability of the fine-tuning data. Data points that have high overlap with the classes / concepts present in the pre-training will have a significantly different vulnerability than data from an entirely different distribution. Hence, to underline the theoretical results, the correct approach, would have been training from scratch.

While the paper tries to argue that the pre-training encoder has no influence ("Figure 4a shows that the regression model is robust to a change of the feature extractor"), this statement is too broad and not backed up by results: The experiments were conducted on only two encoders, both pre-trained on ImageNet. These encoders will have the same biases, and will expose the fine-tuning data equally. If any, to make such a statement, it would be required to assess more encoders, especially ones trained on entirely different distributions, including non-object centric dataset.

The fact, that the expectations do not match the from-scratch training ("underestimates the vulnerability of the from-scratch trained target models") is another indicator that comparing with fine-tuning is not the right approach.


**Minor Comments**

- In the intro, the paper says: "and apply two state-of-the-art MIAs", it would be good to cite them there already for the readers to understand what to expect
- Would it make sense to add the values from the theoretical model in Figure 3, such that one can compare how much the empirical one deviates?

### Questions
NA

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates the relationship between inherent properties of a dataset, such as the number of classes and the number of samples belonging to each class, and its impact on privacy. Privacy is examined through the perspective of membership inference attacks (MIAs), which seek to determine if a sample has been used to train a model of interest. The authors present theoretical results that establish a power-law relation between dataset properties and vulnerability to MIAs, and support their claims with experimental evaluations.

****
Updated score after examining author response.
*****

### Strengths
1. Membership inference is an important attribute that can explain vulnerability of machine learning models to privacy attacks. The extensive theoretical results help provide generalizable and explainable interpretations of impacts of multiple characteristics of datasets on model vulnerability. 

2. Theoretical results are presented in a manner that is easy to follow for an informed reader, and supported by detailed proofs in the Appendix. 

3. Extensive experiments on multiple datasets validate theoretical claims. The datasets have been carefully chosen to encompass different numbers of classes and image domains. 

4. The work presented has the potential for high impact beyond traditional computer science, for example, balancing the requirements of various regulatory regimes such as GDPR with a need to obtain `useful' information from possibly sensitive data.

### Weaknesses
1. The authors indicate that the paper considers two types of MIAs. There have been a wide variety of MIAs examined in the literature, including some which may not rely on confidence scores (e.g., label-based MIAs). Is there a claim (perhaps speculative) that the authors can make about similar relationships for other classes of MIAs? Specifically, could the authors comment on how the power-law relationship might be affected by attacks that leverage different information sources, such as gradient-based attacks or those exploiting model weights directly, rather than just relying on output confidence scores? It is unclear if the observed power-law is a fundamental property of the dataset or an artifact of the specific attack methodology.

2. The experiments focus on datasets and models related to image classification. Can the results be extended to other domains, such as audio or video? Multi-modality can strengthen the scope of the proposed contribution. For example, how would the power-law relationship be affected by the higher dimensionality and temporal dependencies inherent in video data, or the sequential nature of audio data? Are the findings robust to different data modalities, or are there modality-specific factors that might influence the observed relationships?

3. The authors point out that analyses and experimental results rely on an assumption that the datasets are balanced. Some perspective on what might happen if this is not the case can shed more light on real-world applicability of the work. For instance, in a highly imbalanced dataset, would the power-law relationship still hold for the minority classes? Would the overall vulnerability be dominated by the majority class, or would the minority classes exhibit different scaling behaviors? A discussion of how class imbalance might affect the observed power-law is needed.

4. A more detailed discussion or comparison of the effect of dataset characteristics on other aspects of privacy- e.g., differential privacy, which has an extensive literature and supported by theoretical guarantees- will strengthen the submission. Could the authors comment on this? Specifically, how do the dataset properties that influence MIA vulnerability relate to the parameters of differential privacy mechanisms, such as the privacy budget and noise scale? Is there a potential for a unified framework that considers both MIA vulnerability and differential privacy guarantees?

### Questions
Please see Weaknesses above.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The study investigates privacy vulnerabilities through Membership Inference Attacks (MIA), with a particular focus on how dataset size affects model privacy. Through detailed per-sample evaluations, the researchers discovered that models become more resistant to privacy attacks as the number of examples per class increases, following a power law distribution. To further examine this phenomenon, the researchers evaluated the findings using few-shot learning and developed a regression model to predict a model's vulnerability to MIA based on dataset properties, such as the number of classes and examples per class.

### Strengths
- The work presents comprehensive experiments on privacy vulnerabilities using two SOTA MIA methods. It conducts a fine-grained analysis of vulnerabilities at the individual sample level. 
- The findings are robustly validated across diverse architectures and datasets.
- The study provides theoretical analyses of a power-law relationship between dataset properties (e.g., shots per class) and MIA vulnerability.

### Weaknesses
1. The paper needs to clarify its motivation. While it discusses transfer learning and few-shot learning, it's unclear whether these techniques are studied as potential privacy protection methods or whether the authors simply examine their privacy risks. The introduction introduces these learning approaches but doesn't explicitly position them against existing differential privacy (DP) defenses. This makes it difficult to understand whether the main goal is to propose new privacy protection strategies or to analyze privacy vulnerabilities in these methods.

2. The paper's organization should be reversed. It would be clearer to show the experimental results first and then explain the theory behind them rather than the other way around.

3. The authors need to revise their claimed contributions. For example, their first contribution about analyzing privacy attacks at the individual sample level isn't new - other researchers have already done similar work (such as [1], [2]).

4. It is unsurprising that larger datasets exhibit lower overall vulnerability to MIA, as models trained on larger datasets tend to rely less on individual samples, reducing the risk of memorization.

5. The authors predicted the overall dataset vulnerability using a regression model with properties such as the number of classes and examples per class. While it offers useful insights,  individual-level vulnerabilities are often more actionable for user privacy protections. It's much more meaningful to investigate the per-sample vulnerabilities. However, considering varying dataset sizes, it may be challenging to derive consistent per-sample results, as the same sample could behave as an outlier in some datasets but not in others.

### Questions
see above

### Soundness
3

### Presentation
2

### Contribution
1
