# Influence-based Attributions can be Manipulated

- Decision: Reject
- Scores: 3, 3, 1, 5, 3

## Abstract
Influence Functions are a standard tool for attributing predictions to training data in a principled manner and are widely used in applications such as data valuation and fairness. In this work, we present realistic incentives to manipulate influence-based attributions and investigate whether these attributions can be \textit{systematically} tampered by an adversary. We show that this is indeed possible for logistic regression models trained on ResNet feature embeddings and standard tabular fairness datasets and provide efficient attacks with backward-friendly implementations. Our work raises questions on the reliability of influence-based attributions in adversarial circumstances

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studied a setup in which the influence scores of training samples can be manipulated through a modified training procedure by changing the loss function to maximize the influence scores of target samples on a subset of test samples. The paper aims to show that there could be vulnerabilities in influence scores that affect downstream applications, such as those related to fairness.

### Strengths
1. The paper is easy to follow, and the results and methodology are clearly presented in tables and figures/diagrams.

2. The overall idea of studying vulnerabilities in influence functions is interesting, especially as there are some applications built on using influence scores. However, I have some concerns, which are discussed in the following points.

### Weaknesses
1. The first and most important point to raise is that the attack setup does not seem practical in the real world. The paper provides a framework that includes two components: 1) Data Provider and 2) Influence Calculator. It is assumed that the data provider is truthful, while the Influence Calculator, which trains a "model" and calculates the influence scores, is maliciously manipulated. I can't think of a real-world scenario in which an Influence Calculator would deliberately aim to manipulate influence scores or would need to alter the influence score to indirectly affect the desired behavior, especially when it can directly train a model and is considered the target (or deployed) model. The reverse scenario seems more plausible, where a Data Provider among all providers aims to change the influence score distribution based on its own interests. Although the paper attempts to justify a scenario involving "fairness manipulation," this does not seem plausible to me. To modify the fairness of a model, it would need to be trained in a way that specifically adjusts the influence scores; however, there are more straightforward ways to alter this dynamic, specially when the training procedure can be altered.

2. Another key issue is that altering the influence scores distribution requires access to the test set to manipulate the top-k scores. This approach is problematic, as it risks causing the modified influence scores to overfit to the specific test set. This tendency is evident in Figure 2, where the "transfer" results (that uses held out test set) are notably less impactful, suggesting that the changes in influence scores are highly dependent on the specific test set used in the optimization process. The paper does not adequately address the potential for this overfitting to limit the generalizability of the attack.

3. While the paper discusses it, there seems to be a key limitation in the "Multi-Target Attack" setup: modifying the influence scores for a subset of samples is not an independent process for each sample. The authors attempt to mitigate this by employing multiple random initializations; however, this solution appears to be costly and does not guarantee convergence to a globally optimal solution for each target sample. The interdependence of the influence score modifications introduces a significant challenge to scaling the attack to larger sets of target samples.

4. The current version of the method appears to be computationally feasible only for linear models, which further limits the practicality of the methodology (in addition to my first point). However, there has been significant progress in making influence score calculations feasible for non-linear and large models, such as in "TRAK: Attributing Model Behavior at Scale" (https://arxiv.org/abs/2303.14186), which are more compelling for study. The restriction to linear models severely limits the applicability of the proposed attack in modern machine learning scenarios.

5. The writing style is not ideal; too many paragraphs begin with a bold sentence or title. While this may be acceptable to some readers, I found it somewhat confusing to determine what is truly important. I would suggest that the authors use bold text sparingly, reserving it for points that are especially significant.

### Questions
1. Regarding the first point mentioned above, how practical is this scenario in the real world?

2. Can changes in the influence scores be achieved on the data provider's side without needing access to the model or altering the training procedure? I assume this might be related to adversarial attacks and data poisoning literature; however, it would be beneficial to discuss this from the perspective of influence functions.

3. How does the scale of the data affect the difficulty of the task? Based on Figure 2, it appears that as the training data size increases, the task of changing the influence scores becomes more challenging. Given the trend that more data generally improves performance, does a larger dataset also make influence score modification more difficult?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper examines the potential for manipulating influence-based attributions. The authors explore two use cases: data valuation and fairness. In data valuation, an attacker aims to inflate the influence scores of specific data samples to increase their perceived value. In fairness, the attacker seeks to reduce the fairness of a downstream model by manipulating influence scores used for data reweighing. The paper presents targeted and untargeted attack algorithms, demonstrating their effectiveness on logistic regression models trained on ResNet features and standard fairness datasets. The authors also present a theoretical impossibility theorem.

### Strengths
- The paper is well-written and well-organized.
- The paper provides a practical and efficient algorithm to compute the backward pass through Hessian-Inverse-Vector Products for influence-based objectives. 
- The experimental results in the sources show that influence-based attacks, both targeted and untargeted, can successfully manipulate influence scores while maintaining model accuracy.

### Weaknesses
 - The setting of this working is confused to me. It presents a scenario where an adversary can manipulate the model training process to achieve desired influence scores. Is it a realistic scenario in practice and why would an adversary manipulate the influence score when he could manipulate the model itself?
- The method aims to manipulate the influence scores while maintaining the similar test accuracy, and this accuracy is measured by a `dist` function between the parameters and limited by a radius value $C$. However, the choice of $L_2$ norm to measure the distance between two high-dimensional vectors is not always consistent. For example, one can construct another network by multiplying all the parameters by $10^6$ and adding a normalization on each layer, which gives a same result but the $L_2$ distance will be much different. The authors should provide more justification for this choice.
- The experiments described in the paper primarily focus on logistic regression, which may not be representative of more complex models. Will the proposed attack methods be effective on more complex models? Is the objective function defined based on the `dist` function still valid due to the above reason?

### Questions
See weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper proposes an adversarial attack where an adversary seeks to train a malicious logistic regression model which attains similar performance to the original model but has a different distribution of influence estimates. The authors conduct experiments for the downstream tasks of data valuation and fairness.

### Strengths
- The paper conducts experiments on multiple datasets.
- The concept of adversarial attacks on influence scores is an interesting idea overall.

### Weaknesses
In my opinion, the paper possesses major limitations that invalidate its contributions. My major concern revolves around the proposed threat model itself, which seems untenable for real-world practical applications. Other issues are concerned with limited model and dataset evaluation, and the overall simplicity of the work:

- **Unjustifiable Threat Model**: The threat model makes multiple assumptions about the influence (and data valuation) problem pipelines in order to make the attack viable. First, it assumes that the data is a trivial commodity and that this will be provided as is by the data providers to an influence "calculator" who themselves are the adversary. I find this to be highly implausible-- data is generally protected and it is more likely for the data owners / model trainers to be benign as model training is a computationally costly process. It seems highly unlikely (especially if the influence calculator can potentially be an adversary) that the data providers will provide highly sensitive data to this third-party as its outputs cannot be guaranteed to be trustworthy (i.e. anyone can train a model as they would like-- why would they trust them and their outputted scores?). Second, the threat model assumes that the influence calculator who is training the model possesses malicious intent but the reasons for this are unclear. As the influence calculator is taking on the overhead of model training, what is their incentive in doing so? They are training the model to achieve similar performance on the test set (as the paper also measures) and hence, are likely going to serve it for potential production use. Why would they change the influence scores for their own model to compensate data providers differently while incurring the cost of another model retraining then? Their main incentive should lie in ensuring robust model performance for end-users. Perhaps these aforementioned issues can be justified with some real-world examples or use-cases, but it is not motivated sufficiently in the current version of the paper and I do not think this setting is tenable. 
- **Limited Models and Datasets**: The paper only considers a simple logistic regression model in experiments and all the datasets are tabular datasets obtained via embeddings from deeper models. Why is logistic regression a good base model for data valuation when the task itself might require a deep learning model that is non-convex? Overall, this is very restrictive as a setting and the paper needs to consider end-to-end models for experiments. 
- **Simplicity of Attack**: Owing to the assumptions made in the threat model, the attack is very simple-- the approach just requires training a model with an adversarial objective while putting a constraint on performance. This is technically quite trivial and somewhat lower than the bar for ICLR.

### Questions
Please see the weaknesses listed above-- each can be considered as a question.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper investigates the vulnerability of influence functions in adversarial settings. Influence functions are commonly used to assess the contribution of training data to model predictions, but they may be susceptible to manipulation in incentivized applications like data valuation and fairness. The authors propose two types of attacks: a targeted attack designed to increase the influence score of specific samples to raise their data valuation, and an untargeted attack that alters influence scores through simple model weight scaling, affecting model fairness. Experimental results show that these attacks can be effectively implemented on multiclass logistic regression models and standard datasets without significantly compromising model accuracy. Additionally, the paper presents an optimization method for inverse computation of influence functions to enhance memory and time efficiency. Finally, the authors propose possible defense strategies and highlight the limitations of influence functions in adversarial environments.

### Strengths
1. I find the exploration of weaknesses in influence attribution an interesting phenomenon with practical application support, as highlighted in the proposed applications.
2. The authors provide theoretical analysis, demonstrating that under certain conditions, the influence scores of specific data samples cannot be manipulated.

### Weaknesses
1. The paper references the instance attribution method from [1] (which relies on local model parameters), but there are currently many new instance attribution methods (incorporating model parameters from different training stages). The paper should at least discuss these instance attribution methods (as in "Training data influence analysis and estimation: a survey") to rule out that the vulnerabilities are due to flaws in the method itself.
2. Many logical details are placed in the appendix, which makes reading somewhat challenging. I believe it would be more reasonable to include core logic in the main text and place some logical explanations in the appendix, especially Section A.1 (this does not affect my scoring decision).
3. From reading the application, I can clearly understand the significance of this task, but I cannot precisely grasp how to achieve such a goal. The last formula on page 5 appears to be an intuitive attack method without proof of achieving the intended objective.
4. I believe the research task itself is meaningful but lacks discussion on the more advanced instance attribution methods [2]. If these methods could be included in the discussion, I would be more inclined to raise my score.

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposed an attack to manipulate influence-based attributions by training a malicious model with slightly reduced accuracy, while achieving the attacked influence scores. Specifically, the authors aimed to find a malicious model $\theta’$ that maintained a similar accuracy to the original model $\theta$, which maximizing the influence score of the target sample. The authors also discussed the potential scenarios for the proposed attack, including data valuation and fairness use cases.

### Strengths
The authors investigated the vulnerability of influence-based attributions, which was an interesting direction.

### Weaknesses
1. The main weakness was that the threat model on influence score was problematic. The influence score $I_\theta (z, z_{test})$ was computed based on a given model $\theta$ according to Eq. (1). When different model parameters $\theta$ were given, the influence score of a training point $z$ on the loss at a test point $z_{test}$ $I_\theta (z, z_{test})$ would indeed yield a different score. In other words, the discussion of the influence function was only meaningful within the context of the same model. Changes in model parameters would inevitably lead to variations in influence scores. Therefore, these variations should not be considered an attack on the influence function. The core issue is that the influence function is a property of the model itself, not a separate entity that can be attacked independently. Modifying the model parameters changes the function, and thus the influence scores, but this is not an attack on the influence function itself, rather a change in the model that results in different influence scores. The authors fail to establish a clear distinction between changing the model and attacking the influence function. 

2. The proposed attack scenarios were not reasonable. For instance, in data valuation tasks, why would an adversary be able to modify the model parameters? If the goal was to evaluate the importance of data for a specific model, the model parameters should remain fixed. For example, with large models like GPT-4, the adversary would not be able to alter the model parameters. Furthermore, if multiple models were used to evaluate the importance of data, why would the evaluator choose a malicious model over a set of trusted models? In other words, if the adversary cannot ensure that the evaluator uses the malicious model, then the proposed attack becomes impractical. The scenarios lack a clear justification for why the adversary would have the ability to manipulate the model parameters used for influence calculation, which is a crucial assumption for the attack to be feasible. The paper does not provide a convincing argument for why a data valuation process would be vulnerable to this type of manipulation.

3. The proposed attack constrained the L2 norm of the two parameters in Eq. (4) and in Lines 250-251 to ensure that the accuracies of the two models are similar. However, there is a lack of evidence that the L2 norm of parameters is related to the performance of the model. For example, consider a two-layer network with two categories $f(x) = Sigmoid(c\cdot Ax)$, where $c>0$. If $f(x)>0.5$, the class is 1; otherwise, the class is 0. In this case, changing the L2 norm of the parameters $B=c\cdot A$ (i.e., modifying $c$) does not affect the model's performance. The paper lacks a theoretical justification for using the L2 norm as a proxy for model performance similarity, and the provided example demonstrates a clear case where this assumption does not hold. This undermines the validity of the proposed attack strategy.

### Questions
1.	Why does $dist(\theta, \theta') <= C$ in Eq. (4) guarantee that the original and  malicious  models have similar accuracy? Given that different models with the same structure may have varying parameter magnitudes, how to determine the hyper-parameter $C$?

2.	Why does Eq. (3) compute the influence function of a training sample z on all test samples? Will the sum of the influence scores for all test samples cancel each other out, both positively and negatively?

### Soundness
1

### Presentation
2

### Contribution
1
