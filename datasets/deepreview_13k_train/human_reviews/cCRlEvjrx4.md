# Learning Conditionally Independent Marginals Enables Logical Compositions in Conditional Diffusion Models

- Decision: Accept
- Scores: 6, 6, 6, 5, 8

## Abstract
How can we learn generative models to sample data with arbitrary logical compositions of statistically independent attributes? The prevailing solution is to sample from distributions expressed as a composition of attributes' conditional marginal distributions under the assumption that they are statistically independent. This paper shows that standard conditional diffusion models violate this assumption, even when all attribute compositions are observed during training. And, this violation is significantly more severe when only a subset of the compositions is observed. We propose CoInD to address this problem. It explicitly enforces statistical independence between the conditional marginal distributions by minimizing Fisher’s divergence between the joint and marginal distributions. The theoretical advantages of CoInD are reflected in both qualitative and quantitative experiments, demonstrating a significantly more faithful and controlled generation of samples for arbitrary logical compositions of attributes. The benefit is more pronounced for scenarios that current solutions relying on the assumption of conditionally independent marginals struggle with, namely, logical compositions involving the NOT operation and when only a subset of compositions are observed during training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers the problem of conditional generation for logical compositions of attributes. The authors claim that existing conditional diffusion models violate the conditional marginal independence assumption of the attributes. This makes them struggle in generating samples given arbitrary logical compositions of attributes, even if trained with uniform data over all possible combinations of attributes, and even worse if there is a statistical correlation or only some attribute combinations are seen. The paper then tackles this problem by training score-based models (with their diffusion model interpretation) with an additional loss term to enforce this conditional independence assumption, motivated by Fisher’s divergence between the joint and product of marginals of attributes. The assumption about marginal independence empirically validated by observing that Jensen-Shannon divergence of joint distribution and the product of conditional marginal distributions has a negative correlation with an accuracy metric called conformity score (CS).

### Strengths
The paper addresses the problem of generating samples for logical compositions of attributes, including combinations previously not seen in data, which is highly relevant.

The proposed approach trains a single model to handle arbitrary compositions of attributes, and thus scales with the number of attributes. The proposed loss function is derived from a theoretically sound objective based on the Wasserstein distance between the true conditional likelihood and the learned likelihood satisfying the conditional independence assumption.

Experiments are thorough, including different support settings (uniform, non-uniform, partial/orthogonal) for two benchmark datasets, and the results support the claims about conditional independence assumption. 

The paper is overall well structured, although some details could be clarified (see below).

### Weaknesses
I have a couple of concerns about soundness and clarity. While the proposed loss function (Eq 6 and 7) has a clear theoretical justification of bounding Wasserstein distance, this is somewhat lost in the actual training objective of CoInD (Eq 8 and 9) due to simplifications for practical implementation. Specifically, the connection between the theoretical bound in Eq. 8, involving the square root of the score and conditional independence losses, and the final training objective in Eq. 9, which uses a linear combination, is not clearly explained or justified. It was also not very clear how the modified L_{CI} in Eq 9 is derived, and why a pairwise approximation is sufficient for enforcing conditional independence among all attributes. The paper mentions that this approximation is based on Hammon and Sun (2006), but a more detailed explanation of how this approximation is derived and its implications for the overall objective is needed.

In several places (including the problem statement), the authors seem to conflate the distribution of attributes being uniform vs. conditionally independent. The conditional distribution of attributes can be factorized without necessarily being uniform. For example, a Gaussian distribution over attributes can be factorized into independent Gaussians without each marginal being uniform. Another issue is that even if each attribute had uniform probability, after conditioning on a logical formula in general, each marginal probability may no longer be uniform. The paper should clearly distinguish between the uniformity of attribute distributions and the conditional independence assumption.

Moreover, the paper mentions “incorrect marginals” multiple times as being a limitation of current approaches, but I believe the main claim is about conditional independence (factorizability). It would be clearer to refer to independence directly because it’s possible to have the correct marginal probability of each attribute while still violating the conditional independence assumption. For instance, a model could learn the correct marginal distribution for 'color' and 'shape' attributes, but still fail to generate the correct combinations when conditioned on a logical expression like 'red AND circle', if the conditional independence between these attributes is not enforced. As the authors also discuss, the proposed method is restricted to a composition of a closet set of attributes, and cannot easily add compositional attributes without retraining from scratch. However, while a limitation, open-set compositions are outside of the scope of this paper and not a major weakness.

### Questions
I found the definition of conformity score to be not very clear. First, I assume results are reported in percentage rather than as defined (between 0 and 1). My main confusion is about the distribution p(X,C) in the definition (line 199). For the generated samples, is the score measuring whether all consistent combinations of attributes appear following a certain distribution, or is it only measuring whether the attributes (given by the classifier) satisfy the logical composition?

Can this method be used for compositions using general logical formulas beyond single AND and NOT operations?

Can CoInD generate attributes having non-uniform probability (while still being conditionally independent)? For instance, to generate shapes in a scene following a certain distribution, or images for demographic groups following a certain population distribution.

The causal graph in Fig 2a implies independence among the attributes, but not necessarily conditional independence given X. It wasn’t clear whether (around line 121) the claim is that conditional independence is implied by this causal graph or it is an additional assumption made by the authors.

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
3

### Summary
This paper shows that standard conditional diffusion models violate this assumption, even when all attribute compositions are observed during training. The authors propose COIND to address this problem. It explicitly enforces statistical independence between the conditional marginal distributions. Quantitative experiments demonstrate a significantly more faithful and controlled generation of samples for arbitrary logical compositions of attributes. The benefit is more pronounced for scenarios that current solutions relying on the assumption of conditionally independent marginals struggle with, namely, logical compositions involving the NOT operation and when only a subset of compositions are observed during training.

### Strengths
The problem is interesting and the authors proposed a solution to the problem. The writing of the paper is clear and easy to follow. The method is simple and effective. The authors provide experiments to validate the proposed method.

### Weaknesses
1. The datasets in the paper are simple MNIST and synthetic 3D shapes. Experiments on real-world images could strengthen the paper. Experiments on natural images could provide more convincing evidence for the proposed method.

2. What are the practical applications of NOT operation in the composition generation? What are the motivations for applying logic operations on the attributes with multiple values, e.g. c_i  in  [0, 1, 2, 3, 4, 5]?

3. How does the model process logic expressions? How is the model implemented to process logic expressions? If not implemented, what are the motivations for applying logic operations? Are AND operations sufficient for composition generation with different attributes?

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper performs compositional image generation with and, or, and not operators. The proposed method trains the diffusion models with a score function that enforces the attributes in the generated images to be independent. Finally, the authors show performance on two synthetic datasets.

### Strengths
The paper is very well written. Every detail is provided in a clear manner. The description is intuitive. The authors also provided insightful observations.

### Weaknesses
### Minor weakness:
* Some motivational examples of the utility of the proposed method in the introduction would be nice.
* The conformity score with notation should be defined/discussed briefly in the experiment section again.
* An initial look at Figure 3 might give readers the impression that the proposed approach is effective for such scenarios as well. This should be made clearer.
* The numbers in line 417 can be written in a more detailed way.
* The authors should give some examples of open and closed set attribute compositions.

### Major weakness:
* The only major issue with this paper is that there is no experiment on a real-world image dataset. One of the baselines, LACE, presents results for human faces with independent attributes, e.g., smile, eyeglasses, etc. Can the authors show performance on such datasets?

### Questions
### Questions:

* What happens if $\lambda$ is set to a very high value? Would that give perfect conditional independence? Will that be an issue while minimizing $L_{\text{score}}$?
* What issues will the proposed algorithm face if the attributes are actually dependent in the true data-generating process?
* How many attributes can be composed together? How does the proposed approach behave when you increase the number of attributes?
* Based on Figure 3: if the training dataset has no [color: green, digit: 9], can the model generate such images? The proposed approach has a 55% conformity score (CS) for partial support. Does that mean that, among the generated images with the attributes [color: green, digit: 9], 55% contain these attributes correctly?
* Can the authors provide images with minimal attribute combinations where the proposed method, along with all baselines, fails?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the limitations of standard diffusion models in sampling data with arbitrary logical compositions of statistically independent attributes. It reformulates the problem as minimizing the Fisher divergence between the joint distribution and the product of marginals, demonstrating the effectiveness of this approach.

### Strengths
This paper provides a clear and well-articulated statement of the problem, supported by intuitive examples that help the reader understand the limitations of current conditional diffusion models. It effectively highlights the insufficiencies in these models, particularly in capturing accurate marginal distributions, and offers a novel solution to address these gaps. The authors ensure that the proposed model is designed to learn precise marginal distributions, an essential improvement over existing methods. The paper also includes rigorous experimental validation, utilizing a range of extensive datasets, which adds credibility to the findings and demonstrates the model’s effectiveness across diverse scenarios.

### Weaknesses
(1) Some claims in the paper need additional rigor. For instance, the assertion that the drop in conformity scores is due to the violation of independence relations in the learned model lacks clear justification. The paper states that the drop in conformity score between joint sampling and marginal sampling indicates a violation of conditional independence, but it does not provide a formal proof or a clear explanation of how the conformity score is directly linked to the violation of conditional independence. Specifically, it is not clear how the conformity score, which measures the agreement between the generated samples and the conditional attributes, is affected by the incorrect marginal distributions. A more detailed analysis, possibly involving a mathematical derivation or a more thorough explanation of the underlying assumptions, is needed to support this claim.

(2) The proof process could be clarified for readers. For example, the derivation of Equation 6 from previous equations is not immediately clear, and similar issues appear in other parts of the theoretical development. The paper uses the 2-Wasserstein distance and its relationship to the score function, but the intermediate steps in deriving the final objective function are not sufficiently detailed. It would be beneficial to include a step-by-step derivation, explaining how the triangle inequality is applied and how the upper bound based on the score function is obtained. Additionally, some expected theoretical support is missing from the appendix, which could help make the proofs more accessible. For example, the assumptions required for the application of the 2-Wasserstein distance bound should be explicitly stated and justified.

(3) In the experiments section, the model is only evaluated on two real-world datasets, with no simulation results to provide more quantitative insights into the model’s effectiveness. While the real-world datasets are valuable, they may not fully capture the range of scenarios where the proposed model is expected to perform well. Including simulation studies with controlled parameters would allow for a more thorough evaluation of the model's behavior under different conditions. For example, it would be useful to see how the model performs with varying degrees of attribute independence or with different types of marginal distributions.

### Questions
(1) How is the failure of standard diffusion models linked to the violation of independence assumptions? Could you provide evidence or proof supporting this claim?

(2) How does the model perform on more diverse datasets? Could additional results on simulated data be included to further validate its effectiveness?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce COIND, a novel approach that enforces conditional independence between marginal distributions by minimizing Fisher's divergence between joint and marginal distributions. Traditional models struggle to handle arbitrary compositions, especially when only partial data compositions are available during training. In comparison, COIND leverages causal independence to improve the generation of images that meet desired attribute compositions. The experiments show COIND’s performance in generating images with diverse and accurate compositions.

### Strengths
1. This paper introduces conditional independence analysis into the training of conditional diffusion models, integrating insights from both causal structure learning and generative modeling. By uncovering latent causal structures, it enhances the performance of traditional conditional diffusion models, which is quite innovative.

2. The derivation of error decomposition in Section 4 is particularly impressive. By decomposing the Wasserstein distance, the paper introduces a novel loss function, providing a strong theoretical justification for incorporating causal structures like conditional independence, which is very intriguing.

3. On the selected datasets, the proposed method consistently outperforms comparative approaches across various settings, demonstrating a significant improvement. Moreover, the presentation of experimental results is comprehensive and meticulous. Notably, Appendix A.7 provides an exhaustive comparison of experimental settings across methods, which is commendable.

### Weaknesses
1. While the paper uses illustrative images to present the experimental settings for Non-uniform and Partial support scenarios, the lack of mathematical descriptions limits the rigor of this section. Specifically, the paper does not provide a formal definition of how the non-uniform and partial support distributions are generated, making it difficult to reproduce the experiments or understand the precise nature of the data distributions used. This lack of formalization weakens the claims about the model's performance under these conditions.

2. The paper’s exploration of causal structures introduced during training remains relatively simple, focusing primarily on conditional independence, and lacks investigation into more complex causal graphs and mechanisms. The current approach only considers direct conditional independence between attributes and the generated image, without exploring potential dependencies between the attributes themselves. This simplification limits the model's ability to handle real-world scenarios where attributes might be causally related, which could lead to suboptimal performance in such cases.

3. The study only examines the model's performance on the Colored MNIST and Shapes3D datasets, which, compared to papers like Liu et al. (2023), leaves it without results on more complex, real-world datasets to substantiate the research conclusions. The limited dataset choice makes it difficult to assess the generalizability of the proposed method to more complex and diverse data distributions. The absence of experiments on real-world datasets, such as those with more intricate attribute relationships, raises concerns about the practical applicability of the method.

### Questions
1. As pointed out by (Karras et al. (2022), Fu et al. (2024)), generative diffusion models often introduce an early stopping time rather than reverting completely to time zero in the generation process to avoid numerical instability. Did you consider the impact of setting an early stopping time in your experiments? If so, could you elaborate on it? If not, could you explain why this setting might not significantly affect the results?

2. The selection of the hyperparameter λ in the loss function is crucial. Could you share the principles you followed when choosing it (e.g., Bayesian optimization, cross-validation)? The analysis in Section 5.2 does not seem to fully address this aspect.

3. In the experimental scenarios considered in this paper, the features are all  discretized. Do you believe it is possible to extend this method to continuous features, or potentially adapt it with certain techniques to handle continuous feature scenarios?

4. The paper uses Jensen-Shannon Divergence (JSD) to measure conditional independence, though there are many metrics for conditional independence. For instance, Conditional Mutual Information (CMI) (Mukherjee et al., 2020; Li et al., 2023) has shown strong performance for continuous feature scenarios mentioned in Q3. Could you explain the advantages of using the JSD metric in this context?

Reference:
1.	Liu, N., Li, S., Du, Y., Torralba, A., & Tenenbaum, J. B. (2022, October). Compositional visual generation with composable diffusion models. In European Conference on Computer Vision (pp. 423-439). Cham: Springer Nature Switzerland.

2.	Karras, T., Aittala, M., Aila, T., & Laine, S. (2022). Elucidating the design space of diffusion-based generative models. Advances in neural information processing systems, 35, 26565-26577.

3.	Fu, H., Yang, Z., Wang, M., & Chen, M. (2024). Unveil conditional diffusion models with classifier-free guidance: A sharp statistical theory. arxiv preprint arxiv:2403.11968.

4.	Mukherjee, S., Asnani, H., & Kannan, S. (2020, August). CCMI: Classifier based conditional mutual information estimation. In Uncertainty in artificial intelligence (pp. 1083-1093). PMLR.

5. Li, S., Zhang, Y., Zhu, H., Wang, C., Shu, H., Chen, Z., ... & Yang, Y. (2023). K-nearest-neighbor local sampling based conditional independence testing. Advances in Neural Information Processing Systems, 36.

### Soundness
3

### Presentation
3

### Contribution
2
