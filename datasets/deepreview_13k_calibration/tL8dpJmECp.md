# Improving Fairness and Mitigating MADness in Generative Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
Generative models unfairly penalize data belonging to minority classes, suffer from model autophagy disorder (MADness), and learn biased estimates of the underlying distribution parameters.  Our theoretical and empirical results show that training generative models with intentionally designed hypernetworks leads to models that 1) are more fair when generating datapoints belonging to minority classes 2) are more stable in a self-consumed (i.e., MAD) setting, and 3) learn parameters that are less statistically biased.  To further mitigate unfairness, MADness, and bias, we introduce a regularization term that penalizes discrepancies between a generative model’s estimated weights when trained on real data versus its own synthetic data.  To facilitate training existing deep generative models within our framework, we offer a scalable implementation of hypernetworks that automatically generates a hypernetwork architecture for any given generative model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes penalized autophogy estimation (PLE), which is a method that impproves fairness and reduce MADness of generative models.
The key idea is to make the model recursively stable via a regularization term on the MLE loss.
A naive formulation of this loss is intractable and the author(s) solve this issue by a hypernetwork that generates the parameters of the generative model
Experiments show that the proposed method can improve fairness and reduce MADness of generative models on various datasets.

### Strengths
- Novel theoretical contribution connecting statistical bias in MLE to fairness and MADness issues in generative models
- Comprehensive empirical validation across multiple types of distributions and models (VAE, BigGAN)
- Strong technical foundation with clear connections to existing statistical theory
- Results show meaningful improvements in both fairness metrics and stability against MADness

### Weaknesses
 - The motivation and problem setup in the introduction is not well structured, making it difficult to grasp the core contribution initially
- Limited ablation studies on the choice of hyperparameters (e.g., PLE penalty $\lambda$=0.1)
- Some experimental results show inconsistent trends across different distributions without sufficient explanation
- The presentation could be more accessible to readers less familiar with statistical estimation theory

### Questions
1. How sensitive is the method to the choice of $\lambda=0.1$? Was this value chosen empirically or is there theoretical justification?
2. In Figure 2, why does FID still increase with PLE, albeit more slowly? Is this related to the hyperparameter choice (e.g. number of data points in equation 6)?
3. In Figure 4, some distributions show stable performance while others show increasing MADness---why?
4. How does the hypernetwork architecture choice and hyperparameters like $\lambda$ affect performance? I think we need a systematic study on this?

In general I really like the paper and I'd like to increase my rating if the presentation is improved and my question on hyperparameter is answered.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper sets out to address the important problem of representation bias in generative models and MADness (decreased models’ performance when trained using their outputs). The authors propose a method that enforces the parameters of the generative model to remain consistent when trained on the original or synthetic data. To alleviate the challenges of intractable search over generative models’ parameters trained on different synthetic data, the proposed method uses hypernetworks to sample generative model weights. Experiments show the ability of the proposed method to mitigate unfairness and MADness.

### Strengths
1. The paper is well-written and addresses important problems in generative models. 
2. The proposed method is intuitive and easy to understand. 
3. The experiments are well conducted and demonstrate the effectiveness of the method.

### Weaknesses
The paper lacks discussion and comparisons with existing bias mitigation methods in generative models. The authors could consider the following methods and explain how their method differs conceptually from these existing approaches and provide empirical comparisons that can support the benefit of the proposed method in the considered setup:

- Xu, Depeng, et al. "Fairgan: Fairness-aware generative adversarial networks." 2018 IEEE international conference on big data (big data). IEEE, 2018.
- Choi, Kristy, et al. "Fair generative modeling via weak supervision." ICML 2020.
- Sabbagh, Kamil, et al. "RepFair-GAN: Mitigating Representation Bias in GANs Using Gradient Clipping." Tiny Papers @ ICLR (2023).
- Rajabi, Amirarsalan, and Ozlem Ozmen Garibay. "Tabfairgan: Fair tabular data generation with generative adversarial networks." Machine Learning and Knowledge Extraction 4.2 (2022): 488-501

The experiments are not consistent enough; specifically, the datasets used in the paper are considered for different types of experiments. For example, fairness is evaluated only on MNIST using VAE, and MADness mitigation is evaluated on CIFAR 10 using GANs. The authors should provide justifications for the experimental design or consider evaluating different datasets under the same set of experiments, i.e., show that the method also mitigates MADness/fairness on MNIST with GANs, and similarly for CIFAR 10. This would demonstrate the generalizability of the proposed method under the metric being evaluated (e.g., fairness or MADness).   

Another important concern is the authors did not provide sufficient justification or insights into how the method can mitigate bias in generated data, particularly when a generative model trained on the original data is already biased, which can be exacerbated in the follow-up generation. More specifically, it is unclear how constraining the MLE to find the model parameters that remain consistent with synthetic and original data (Eq. 4) mitigates unfairness. The authors could provide a more detailed explanation or intuition for how their method addresses bias, particularly in cases where the original training data is biased.

The authors did not provide ablation on the impact of the parameter $\lambda$ in Equation 5. As the regularization term proposed is the core contribution of the paper, providing these experiments would provide more insights into how the regularization term influences several aspects of the work: the quality of the generated data, the number of generations after which “MADness” occurs, and the fairness of the synthetic data. These experiments could be provided for synthetic distributions used in Figure 4.  In addition, the authors can discuss the range of $\lambda$ values they think would be most interesting to explore and why.  

The Appendix contains unnecessary materials (e.g., B, C, D, E). While this material is interesting and well-written, it can confuse the reader since it is not directly linked to the paper's main contribution. Instead, the authors should consider referring the readers to books/papers that contain this background information.  

For the experiments on the MNIST dataset, Line 334 reads: _The majority class was the digit 3, and the minority class was the digit 6 (this choice was arbitrary)_. Instead of arbitrarily choosing the minority class, the authors should consider the class with the highest false negative rate when classified as the minority. This means the minority class confuses the most with other classes and can be harder to learn when it is underrepresented, for example, see how reference [1] chooses the class to artificially under-represent. 

The paper highly depends on hypernetworks, which increase the complexity of the method and its practical usage.

### Questions
Please see the weaknesses above. In addition, the paper needs proofreading to fix minor typos. Here is a non-exhaustive list of them:
- Line 060: Autophogy Estimation => Autophagy
- Line 078: [...] some events events[...] => some events
- Line 088: [...] and is is described => and is described
- Line 322: [...] S ompares the representation => S compares the representation
- Line 414: For hyeprnetwork training [...] => For hypernetwork

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper addresses fairness and bias in generative models, which often penalize minority classes and suffer from model autophagy disorder (MADness). The authors propose training generative models with hypernetworks to make them more fair, stable, and less biased. They introduce a regularization term to reduce discrepancies between a model's performance on real data versus synthetic data, helping mitigate bias and improve representation fairness. The experimental results show that their framework is scalable, supporting integration with existing deep generative models such VAEs and GANs.

### Strengths
+ The overall paper is well-structured and clearly written, with concise explanations that make concepts like hypernetworks and MADness accessible to a broader readers.

+ This paper tackles an important and timely issue by addressing fairness and bias in generative models, particularly focusing on challenges such as minority class penalization and model autophagy disorder (MADness).

+ The discussion related to large language models (LLMs) adds practical relevance to this research, as the content generated by LLMs is widely distributed across the internet.

### Weaknesses
 - The experiments are relatively weak, especially given the small dataset and the older models used (VAE and BigGAN). It would strengthen the paper significantly if the method were tested on diffusion models.
- There is extensive discussion of ChatGPT and other LLMs in Section 1.3. It would enhance the paper if the proposed method could be applied directly to LLMs.

### Questions
1. In Section 1.1, why does it say that GAN is trained with MLE?

2. In Line 087-088, should $ R_I = C_{Maj} / C_{Min} $ actually be $ R_I = |C_{Maj}| / |C_{Min}| $?

3. In Equation 2, why is $S(M)$ linear? Could the authors provide a detailed explanation for this?

4. In Line 316, how should we interpret $ R_{Fair} < |C_{Maj}| / |C_{Min}| $? According to your conclusion about the linearity of $ S(M) $, shouldn’t the optimal $ R_{Fair} $ that fits the data be equal to $ |C_{Maj}| / |C_{Min}| $?

5. How are the hypernetworks $H_\phi$ trained?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper contains two new innovations:
- A metric of fairness when there is a minority and majority class in the training data.
- A hyperparameter network and corresponding loss function intended to prevent autophagous collapse (MADness)

The authors demonstrate the efficacy of their method to mitigate MADness over multiple generate-train loops and improve fairness.  They do this in both a deep generative model and a statistical context.

### Strengths
The proposed method is certainly interesting, and if it truly works as claimed it would be an impressive and efficient way to train new networks.  The paper is clear and well-motivated.  It poses an original solution to mitigate MADness in generative models.  The results regarding fairness seem experimentally compelling.

### Weaknesses
 - Concerns about the validity of the method: Using a 3-layer FC neural network with the objective stated in the paper will likely result in pathologies.  Suppose that $\theta*$ is the MLE.  It is likely that the FC network H is learning to set its weights close to 0 and its biases close to $\theta*$.  In this way, changing the data is unlikely to alter the parameters very much, making any additional training/retraining using $H$ redundant.  One experiment that you could do to test this (which would alleviate my concerns and requires no additional training) is as follows.  Let G be the BigGAN from figure 2, and let H be the corresponding hyper-network.  If H is really doing it's job, then when you fit $\theta = \sum_{i=1}^n H(x_i)/n for x_i$ only in the category of "airplanes", the resulting generative network $G(x|\theta)$ should produce only images of airplanes.  I suspect that instead one of two things will happen: either the network will barely change, or it will produce images that are not discernible as anything.

- Quality concerns: although the authors report an FID score, there are no generated images from CIFAR in the paper or the appendix.  There also is no clear explanation for why there is a sudden spike in MADness at iteration 4.  

- The evaluations are rather limited: The deep generative models are restricted to CIFAR-10.

- There is no theoretical explanation for why this method improves what the authors call fairness.  It is non-obvious to me why the method should improve fairness.

### Questions
See the weaknesses section.

Also:
- The definition of fairness seems overly simple-- it would be helpful to understand how statistics deals with this issue and what the existing metrics are.  For instance, how do you adapt the current definition when there are multiple classes?
- How does the method compare to more standard statistical techniques (i.e. upweighting the loss from the minority classes)?

### Soundness
2

### Presentation
3

### Contribution
2
