# Can Model Randomization Offer Robustness Against Query-Based Black-Box Attacks?

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6, 6, 5, 6

## Abstract
Deep neural networks are misguided by simple-to-craft, imperceptible adversarial perturbations to inputs. Now, it is possible to craft such perturbations solely using model outputs and black-box attack algorithms. These algorithms compute adversarial examples by iteratively querying a model and inspecting responses. Attacks success in near information vacuums pose a significant challenge for developing
mitigations. We investigate a new idea for a defense driven by a fundamental insight—to compute an adversarial example, attacks depend on the relationship between successive responses to queries to optimize a perturbation. Therefore, to obfuscate this relationship, we investigate randomly sampling a model from a set to generate a response to a query. Effectively, this model randomization violates the attacker's expectation of the unknown parameters of a model to remain static between queries to extract information to guide the search toward an adversarial example. It is not immediately clear if model randomization can lead to sufficient obfuscation to confuse query-based black-box attacks or how such a method could be built. Our theoretical analysis proves model randomization always increases resilience to query-based black-box attacks. We demonstrate with extensive empirical studies using 6 state-of-the-art attacks under all three perturbation objectives ($l_\infty, l_2, l_0$) and adaptive attacks, our proposed method injects sufficient uncertainty through obfuscation to yield a highly effective defense.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a defense mechanism against query-based black-box attacks relying on model randomization. The proposed method aims to hinder the estimation of the gradients needed to compute adversarial examples obfuscating the relationship of successive queries by randomly sampling a model from a set of models for each query. The paper includes a theoretical analysis showing how this strategy forces the attacker to increase the number of queries to obtain an accurate estimate of the gradient and how model diversity helps to enhance robustness against gradient-free attacks. The experimental evaluation shows that this method is more robust than other strategies relying on randomization for defending against query-based black-box attacks and that the proposed approach to increase models’ diversity helps also to increase robustness.

### Strengths
+ The authors propose a novel approach to generate output diversity for defending against query-based attacks relying on randomization. The propose a new strategy to enhance models’ diversity minimizing the impact on the clean accuracy. 

+ The authors provide a nice theoretical analysis justifying why model randomization is effective against both gradient estimation and gradient-free attacks. In the first case, Proposition 1 shows that this approach forces the attacker to increase the number of queries to produce accurate gradient estimates and, for gradient-free attacks, Proposition 2 shows how increasing model´s diversity increases the probability of misleading an attack direction, enhancing the robustness to query-based attacks. 

+ Compared to other defenses that have a negative impact on the clean accuracy, the proposed defense aims to achieve both high robustness and clean accuracy. For this, the proposed strategies to select models’ subsets and increase diversity show good empirical results. 

+ The experimental evaluation includes a good representation of state-of-the-art attacks and defenses against query-based attacks. The results show that the proposed method improves robustness compared to other competing methods relying on randomization and that the mechanism proposed by the authors to increase diversity is important to achieve such goal.

### Weaknesses
 + Compared to other randomization-based strategy, training and storing a diverse set of models can be computationally demanding, especially for large models and training datasets. In this sense, the computational complexity is not well discussed. It would be convenient to compare the complexity of this approach with the other competing randomization-based defenses mentioned in the paper, as well as to discuss better the trade-offs between robustness and computational burden. 

+ Following up with the previous point, the computational complexity of model sampling and diversity training can have important scalability and latency issues in some practical applications (e.g. real time) or in common scenarios of modern machine learning systems, where the models and the datasets are large. In contrast, for smaller models, other alternatives to query-based strategies, like transfer attacks, can be more appealing to attackers, which can limit the capacity of the proposed approach to defend against attacks. In this sense, I think that the authors should position better the paper and discuss the type of scenarios where such a defense can be useful and applicable. 

+ Although the theoretical analysis provides some good insights that support the benefits of the proposed method, the result in Proposition 1 is somewhat limited, as it relates the number of queries to achieve some quality in the gradient estimation as a function of the upper and lower bound for the gradient’s value. Thus, the result does not relate to the characteristics of the random model selection method. For instance, it would be interesting to analyze how the size of the subset K has an impact on the number of queries required to achieve an error estimation in the gradient lower than Delta. 

+ Although the empirical endorse the use of equation (10) to train diverse models, the motivation for proposing this approach is not well motivated and justified. Perhaps the authors could provide a more detailed explanation about the motivation and justification.

### Questions
+ Computational complexity: Can the authors provide some insights about the computational complexity and the applicability of the proposed defense compared to other competing methods based on model randomization?

+ Can the authors provide more details on the motivation and justification of equation (10) to train more diverse models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes to defend against query-based adversarial attacks by randomization. Existing defenses use this principle by injecting a random noise into the input, feature, or parameters of the model. On the other hand, this work suggests creating many diverse models and randomly ensembling their predictions to fool the attacker. Their method, named Disco, employs a Bayesian framework to learn a diverse set of models. To handle the accuracy degradation, this work proposes a novel asymmetric training objective that forces each model to perform well. The paper also provides a theoretical analysis showing that randomly ensembling significantly increases the number of queries for a successful attack. Experimental results demonstrate the effectiveness of Disco against score-based attacks, decision-based attacks, and adaptive attacks.

### Strengths
- The paper provides a novel approach for randomized defense against query-based attacks. Instead of fixing the model and injecting random noise, they suggest creating many diverse models and randomly selecting some of them to predict.
- The paper proposes a novel training objective to avoid an accuracy drop in each model.
- Theoretical analysis shows that randomly ensembling is effective against score-based attacks.
- Experimental results for a wide range of attacks demonstrate that Disco safeguards the model against query-based attacks.

### Weaknesses
 - The main disadvantage of this approach is that we need to store a set of models instead of one. Ensembling also requires querying many models during inference, which incurs significant computational costs. This problem is even more severe when we deploy large-scale models in practice. An analysis of the training time, storage, and inference time of Disco compared to other defenses such as RND and RF could be helpful.
- The experiments are conducted on low-resolution datasets only. 
- The architecture of the target model in the experiments is also quite limited. There is only one model for each dataset and they are all convolutional networks.
- The paper does not explain why the proposed objective helps each individual model perform well. Can we instead randomly sample a subset of model when training?

### Questions
- What is the training time, inference time, and storage of Disco?
- Is Disco still effective on high-resolution datasets such as Imagenet?
- What is the performance of Disco on other types of architectures such as transformers?

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
The paper proposes a defense mechanism called Disco against query-based black-box adversarial attacks by randomizing model responses. The core idea is that model randomization—drawing models from a pool of well-trained diverse models for each query—can obfuscate the consistent feedback adversarial attacks depend on. By breaking the static relationship between query responses, this method aims to degrade an attacker's ability to generate effective adversarial examples. The authors conduct extensive theoretical and empirical evaluations, examining attacks across multiple threat models and perturbation types, and find that Disco is shown to outperform existing defenses against black-box attacks.

### Strengths
- The proposed defense is straightforward and simple to implement, making it a practical solution for enhancing model robustness against adversarial attacks.
- Theoretical analysis thoroughly supports the effectiveness of model randomization in the proposed defense.
- The paper conducts an extensive evaluation across various threat models and perturbation types, providing a robust assessment of the defense's performance.

### Weaknesses
 - The approach requires substantial resources, as multiple models must be trained during the training phase. Additionally, switching between models during inference could increase response time and demand more server resources. Specifically, the need to train and store multiple full-sized models, each with potentially millions or billions of parameters, represents a significant computational and storage burden. Furthermore, the inference process, which involves selecting a random model for each query, adds latency compared to a single model deployment. This increased latency could be a critical issue for real-time applications.
-  Models trained on the same dataset may share similar adversarial boundaries, posing a risk that attackers could exploit if the decision boundaries are too alike across models in the pool. If the models, despite training with a diversity objective, converge to similar feature representations, then adversarial examples crafted for one model might transfer to others, thus diminishing the effectiveness of the defense. This is particularly concerning if the diversity objective is not sufficiently strong to push the models towards truly distinct decision boundaries.

### Questions
1. Could you give some solution about how to reduce the resource overhead in both training and inference phase?
2. Could you explain how possible or impossible that all models in the pool share a similar adversarial boundaries?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores whether model randomization can enhance robustness against query-based black-box attacks. Traditional defenses involve random noise injections, but this study proposes a novel defense: generating responses by sampling from an ensemble of diverse models. Theoretical analysis and extensive empirical tests across various attacks and perturbation metrics validate the efficacy of this strategy, achieving robustness with minimal performance compromise.

### Strengths
1. Good writing with clear motivation and insights.
2. Authors provide a strong theoretical foundation, with proofs demonstrating how randomization increases the difficulty of gradient estimation and search-based attacks.
3. By selecting models with a diversity-promoting training objective, the paper manages to keep clean accuracy relatively stable.

### Weaknesses
1. How does increasing model diversity impact clean accuracy, and is there a systematic way to balance these two metrics?
2. Disco tests VGG and ResNet architectures, I think it would be useful to know whether this approach is effective across more different model types.
3. Although Disco's results on MNIST, CIFAR-10, and STL-10 are promising, these are relatively small datasets. It would strengthen the paper to see how this defense performs on more challenging datasets, like ImageNet.
4. In the paper, authors mention that they use a larger number of models (40) for the MNIST task and a lower number of models (10) for high-resolution CIFAR-10 and STL-10 tasks. Have the authors tested the impact of different ensemble sizes, and is there an optimal balance between model count and robustness?

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates model randomization as a defensive strategy against query-based black-box attacks on deep neural networks. The authors argue that these attacks exploit the correlation between successive model responses to queries. By randomizing the model responsible for each response, this correlation can be obscured, thereby making the attack more challenging. A theoretical framework is proposed in which models are sampled from a diverse pool to respond to queries, increasing uncertainty for the attacker and degrading the quality of information that can be extracted from query responses. 

To encourage model diversity without compromising individual model performance, the authors introduce a novel learning objective. Extensive empirical evaluations demonstrate that the proposed method, named Disco, substantially enhances model robustness against advanced query-based black-box attacks across various perturbation norms ($\ell_\infty$, $\ell_2$, $\ell_0$) and adaptive attack strategies, while maintaining high accuracy on clean data.

### Strengths
This work proposes an interesting insight and analyzes its validity theoretically, then presents supporting evidence experimentally.
Experimental results show that the proposed method is highly effective, maintaining strong robustness without compromising accuracy.

### Weaknesses
1. The emphasis on specific architectures, such as Convolutional Neural Networks (CNNs), and small datasets, including MNIST, CIFAR-10, and STL-10, offers valuable insights. However, this focus may restrict the generalizability of the approach's effectiveness across a broader spectrum of models and large data types (such as the ImageNet dataset or the COCO dataset).

2. While the proposed method demonstrates enhanced robustness, could the authors provide an analysis of its computational overhead?  In particular, how do time and resource requirements measure up when comparing inference time and memory usage with existing techniques on a standardized hardware setup?

3. The abstract mentions that state-of-the-art attacks were employed to evaluate the proposed method; however, current query-based black-box attacks that incorporate prior knowledge, such as PBO [1], have demonstrated significantly better performance than the methods discussed in the paper. It would be beneficial to consider these more advanced techniques in the evaluation, where the souce code of P-BO can be found in https://github.com/machanic/P-BO.

4. The mathematical notation in Section 3.3.1 is ambiguous. For clarity, vector $\mathbf{u}$ should have the same dimension as $\mathbf{x}$ to allow summation in Equations (4), (5), and (6). Similarly, $g(\mathbf{x})$, as the estimated gradient, should align dimensionally with $\mathbf{x}$. In Proposition 1, it is unclear how $g(\mathbf{x})$ is bounded by the constants $a_i$ and $b_i$. If $a_i$ and $b_i$ are vectors, why would the lower bound for $n$ in the conclusion then be represented as a vector?

5. While the theoretical analysis considers two aspects (GRADIENT ESTIMATION ATTACKS and GRADIENT-FREE ATTACKS), some uncertainties persist. For example, as noted in Section 3.3.2, $P(\frac{\tilde{H}(\mathbf{x}, \mathbf{u})}{\hat{H}(\mathbf{x},\mathbf{u})})<0$ represents the probability of misleading an attack direction. However, in practical applications, it may sometimes be necessary to consider the opposite direction due to potential inaccuracies in direction (as seen in methods like SignOPT [2]). Thus, relying solely on the sign may not fully capture the misleading nature of the search direction.

### Questions
1. The abstract mentions that state-of-the-art attacks were employed to evaluate the proposed method; however, current query-based black-box attacks that incorporate prior knowledge, such as PBO [1], have demonstrated significantly better performance than the methods discussed in the paper. It would be beneficial to consider these more advanced techniques in the evaluation, where the souce code of P-BO can be found in https://github.com/machanic/P-BO.

2. The mathematical notation in Section 3.3.1 is ambiguous. For clarity, vector $\mathbf{u}$ should have the same dimension as $\mathbf{x}$ to allow summation in Equations (4), (5), and (6). Similarly, $g(\mathbf{x})$, as the estimated gradient, should align dimensionally with $\mathbf{x}$. In Proposition 1, it is unclear how $g(\mathbf{x})$ is bounded by the constants $a_i$ and $b_i$. If $a_i$ and $b_i$ are vectors, why would the lower bound for $n$ in the conclusion then be represented as a vector?

3. While the theoretical analysis considers two aspects (GRADIENT ESTIMATION ATTACKS and GRADIENT-FREE ATTACKS), some uncertainties persist. For example, as noted in Section 3.3.2, $P(\frac{\tilde{H}(\mathbf{x}, \mathbf{u})}{\hat{H}(\mathbf{x},\mathbf{u})})<0$ represents the probability of misleading an attack direction. However, in practical applications, it may sometimes be necessary to consider the opposite direction due to potential inaccuracies in direction (as seen in methods like SignOPT [2]). Thus, relying solely on the sign may not fully capture the misleading nature of the search direction.

[1] Cheng, S., Miao, Y., Dong, Y., Yang, X., Gao, X.-S., & Zhu, J. Efficient Black-box Adversarial Attacks via Bayesian Optimization Guided by a Function Prior. In *Proceedings of the 41st International Conference on Machine Learning (ICML)*, pp. 8163–8183, 2024.

[2] Minhao Cheng, Simranjit Singh, Pin-Yu Chen, Sijia Liu, and Cho-Jui Hsieh. Sign-OPT: a query-efficient hard-label adversarial attack. In *International Conference on Learning Representations*, pp. 1–16, 2020.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores a novel defense mechanism to improve the robustness of deep learning models against query-based black-box adversarial attacks. The authors propose using model randomization as a defense. This obfuscates the relationship between successive responses, thereby hindering the adversary's optimization process for generating adversarial examples. The paper provides both theoretical analyses and empirical results showing that model randomization improves resilience across various attack types and perturbation objectives.

### Strengths
1. Well-written and Clear: The paper is clearly articulated, making complex concepts accessible to the reader. The structure of the paper allows for an easy understanding of the problem, solution, and results.
2. Theoretical Justification of Randomization: The paper provides a strong theoretical foundation, demonstrating how model randomization can enhance robustness against adversarial attacks.
3. Rigorous Experiments: The experiments are comprehensive and rigorously conducted, covering multiple types of adversarial attacks (score-based, decision-based) and perturbation objectives (l∞, l2, l0). This enhances the credibility of the paper's claims regarding the method’s efficacy.

### Weaknesses
1. Over-Reliance on Test Accuracy: As noted in Appendix C (around line 1020), it appears that model selection is primarily based on test accuracy. Specifically, the paper seems to select the model checkpoint that achieves the highest test accuracy across the ensemble of randomized models. This approach is problematic because it can lead to overfitting on the test set, which is meant to be an unbiased measure of generalization performance. The selection process should ideally use a separate validation set to avoid this issue. (If I have misunderstood this aspect, I would appreciate any clarification. Addressing this concern would greatly encourage me to consider a more favorable evaluation of the paper.)

2. Experiments Limited to Low-Resolution Data: The experiments are conducted on relatively low-resolution datasets like MNIST, CIFAR-10, and STL-10. While these datasets are useful for initial experimentation, they do not fully capture the complexities of real-world, high-resolution data. The performance of the proposed defense mechanism may not generalize well to more complex datasets with higher dimensionality and more intricate feature spaces. This limits the practical applicability of the method to scenarios involving high-resolution images, which are more common in real-world applications.

3. Dataset-Specific Models: The paper uses different models for each dataset, which raises concerns about whether the results are model-specific. The choice of architecture can significantly impact the effectiveness of adversarial defenses, and using different models across datasets makes it difficult to isolate the effect of the proposed randomization technique. It remains unclear if the observed robustness improvements are due to the randomization method itself or are influenced by the specific architectural choices for each dataset. This lack of consistency makes it challenging to assess the generalizability of the defense mechanism across various model architectures.

4. Incomplete Released Code: Although the paper mentions that the code is available on GitHub, the provided repository does not include the training code, which is crucial for reproducing the results. The absence of key components, such as the implementation of the SVGD+ method, the model randomization procedure, and any custom loss functions or optimizers used, makes it difficult to independently verify the claims made in the paper. The lack of these details hinders the reproducibility of the results and limits the ability of other researchers to build upon this work.

### Questions
1. Model Selection: Could the authors clarify the exact process used for model selection? If test accuracy was indeed a criterion, it would be helpful if the authors could explain why this approach was chosen over using a validation set. Addressing this concern would greatly encourage me to consider a more favorable evaluation of the paper.

2. High-Resolution Data: Have the authors conducted experiments on high-resolution datasets (e.g., ImageNet)? It would be valuable to assess how the proposed defense mechanism performs on more complex, high-dimensional data commonly found in real-world applications.

3. Dataset-Specific Models: The paper uses different models for each dataset, which raises concerns about whether the results are model-specific. Could the authors clarify the reasoning behind selecting different models for each dataset and provide results that demonstrate the method’s effectiveness across a wider range of models? This would help ensure the robustness of the method across various architectures.

4. Incomplete Released Code: Although the paper mentions that the code is available on GitHub, the provided repository does not include the training code, which is crucial for reproducing the results. To ensure full reproducibility and transparency, it would be helpful if the authors could include specific components of the training process in their code release, such as the implementation of the SVGD+ method, the model randomization procedure, and any custom loss functions or optimizers used. Including these details would provide clearer guidance on what is needed for accurate replication of the results.

### Soundness
3

### Presentation
4

### Contribution
3
