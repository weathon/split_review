# Bayesian Domain Invariant Learning via Posterior Generalization of Parameter Distributions

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
Domain invariant learning aims to learn models that extract invariant features over various training domains, resulting in better generalization to unseen target domains. Recently, Bayesian Neural Networks have achieved promising results in domain invariant learning, but most works concentrate on aligning features distributions rather than parameter distributions. Inspired by the principle of Bayesian Neural Network, we attempt to directly learn the domain invariant posterior distribution of network parameters. We first propose a theorem to show that the invariant posterior of parameters can be implicitly inferred by aggregating posteriors on different training domains. Our assumption is more relaxed and allows us to extract more domain invariant information. We also propose a simple yet effective method, named PosTerior Generalization (PTG), that can be used to estimate the invariant parameter distribution. PTG fully exploits variational inference to approximate parameter distributions, including the invariant posterior and the posteriors on training domains. Furthermore, we develop a lite version of PTG for widespread applications. PTG shows competitive performance on various domain generalization benchmarks on DomainBed. Additionally, PTG can use any existing domain generalization methods as its prior, and combined with previous state-of-the-art method the performance can be further improved. Code will be made public.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates a new approach to domain invariant learning using Bayesian neural networks. In particular, the paper first considers a theorem to show that the invariant posterior of parameters can be implicitly inferred by aggregating posteriors on different training domains. This theorem is under an assumption that the domain invariant information $\mathcal{D}^{c}$ and the domain-specific information $\mathcal{D}^{v}$ are independent. Based on this, the paper proposes a method named Posterior Generalization (PTG) and its lite version to estimate the distribution of the invariant posterior. The proposed method is validated on some benchmarks.

### Strengths
- The code is provided and will be public. 
- The experimental results are good at least from Table 1.

### Weaknesses
 - The paper is not very sound as it attempts to consider learning domain invariants using the Bayesian framework on the parameter space. This is different from the existing work where the feature space is considered. However, this may lead to challenging problems as the parameters of neural networks are extremely high-dimensional and unidentifiable. It is extremely difficult to align and aggregate the posteriors in the parameter space. Therefore, the authors propose some ad-hoc solutions in Section 3.3 such as neural networks for different domains should be initialized from the same point, the parameters of the last layer should be shared between neural networks, and the learning rate should be carefully decayed. These solutions are not well-motivated and do not guarantee that the posteriors of parameters are well-aligned and aggregated properly. The lack of theoretical justification for these specific architectural and training choices significantly weakens the proposed approach. The paper does not provide sufficient analysis or empirical evidence to demonstrate that these constraints effectively address the challenges of aligning posteriors in high-dimensional parameter spaces.
- The authors propose PTG-Lite, which is a lite version of the main method. Due to the difficulty of employing Bayesian treatment to the neural network’s parameters, PTG-Lite just uses maximum-a-posteriori MAP solutions. We can see from Table 1 that PTG-Lite performs comparably with PTG. This somehow downgrades the main narrative of the paper which is to propose a Bayesian framework for aggregating posteriors on domains and inferring domain invariant posteriors. The fact that a non-Bayesian approximation performs similarly to the full Bayesian method raises serious questions about the practical benefits of the proposed Bayesian approach. It suggests that the core contribution, which is the Bayesian treatment, might not be essential to the observed performance gains.
- One of the main contributions is the Theorem 3.1. However, it is trivial. Although the authors claim in the abstract that this theorem relies on relaxed assumptions. However, the assumption of full independence between the domain invariant and domain-specific information is quite strong. This assumption is unlikely to hold in real-world scenarios, where domain-specific and invariant features are often entangled. The theorem's reliance on this unrealistic assumption limits its practical relevance and theoretical contribution. The paper does not adequately address the implications of this assumption not holding, nor does it provide any justification for why this assumption is reasonable in the context of domain adaptation.
- The authors should experimentally compare with other approaches using Bayesian neural networks such as Xiao et al. (2021) and follow-up works. The lack of comparison with relevant Bayesian methods makes it difficult to assess the novelty and effectiveness of the proposed approach within the broader landscape of Bayesian domain adaptation. Without these comparisons, it is unclear whether the proposed method offers any significant advantages over existing Bayesian techniques.
- The writing should be improved. There are some citation and grammar typos and sentences that need further clarification. For example, in the second row from the bottom of page 3, what are the parameters?

### Questions
- In Section 3.1, the paper claims that “we do not need to specify how $\mathcal{D}^{c}$ and $\mathcal{D}^{v}$ are extracted from $\mathcal{D}$”. Is this useful as it would be important to learn which information from the data is invariant or not? Is it possible to interpret the inferred domain-invariant posterior?
- In Equations (5) and (7), what are the expectations with respect to?

### Soundness
1 poor

### Presentation
2 fair

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
The work focuses on tackling domain generalization from the view of parameter posterior learning, aiming to extract invariant “information” for better generalization across training domains. Their work is built upin Bayesian Neural Networks (BNNs), the approach directly learns domain invariant posterior distributions of network parameters. A theorem (conditional distribution marginalization) shows implicit learning of invariant posteriors by aggregating network parameter posteriors from different domains, allowing for a relaxed assumption. The proposed PosTerior Generalization (PTG) employs variational inference to estimate the invariant parameter distribution, demonstrating competitive performance on diverse benchmarks. The proposed PTG is built upon the existing DG methods, where PTG needs the existing DG methods to provide initilization for their parameter posterior aggregation.

### Strengths
1. The explanation of the intractability of the defined problem is clear, offering a compelling rationale for employing variational inference to estimate the posterior density.

2. The paper is well-written with a clear flow to understand the proposed PTG.

### Weaknesses
## Majors:

1. The lack of precise definitions for "parameter" and "feature" within the context of the proposed method introduces ambiguity. Specifically, it is unclear whether the samples drawn from the posterior distribution after the Bayesian neural network converges represent model parameters, latent features, or some other entity. Furthermore, the dimensionality of these posterior samples is not explicitly stated. A clear definition of what constitutes a sample from the proposed posterior and its corresponding dimensionality is crucial for understanding the mechanics of the method.

2. Presenting  p(w|D^{c}) = E_{p(D^{v})}(p(w|D^{c}, D^{v})) as a theorem is unnecessary. This is a standard application of the law of total expectation in probability theory. Labeling it as a theorem and providing a proof for such a fundamental concept adds redundancy to the paper.

3. The specific contributions of this work are not clearly articulated. The paper currently reads more like a review of Bayesian methods applied to domain generalization rather than presenting novel advancements. The authors need to explicitly highlight their unique contributions to the field. The claim regarding the theorem, which appears to be a standard marginalization, needs further justification to demonstrate its novelty.

4. The assumption that \(\mathcal{D}_{c}\) remains constant across the entire dataset \(\mathcal{D}\) is concerning, especially considering the notation \(\mathcal{D}_{i}^{N}\) used by the authors. This raises questions about whether the authors are considering the possibility of subsets of data within a dataset being entirely domain-specific or domain-invariant, as opposed to specific features within data samples being domain-invariant. For instance, in the context of dog images, it is commonly understood that backgrounds can be domain-specific while the features of the dogs themselves are domain-invariant. However, the authors seem to suggest the existence of entire images within the "dog" category that are either wholly domain-specific or domain-invariant, which is a less intuitive concept. This assumption needs further clarification and justification, as it forms the basis for the proposed work's motivation. A more accurate framing might involve focusing on domain-invariant features rather than entire data samples.

5. The literature compared in this study seems outdated. The highlighted SOTA method, CORAL, dates back to 2017. Since the proposed method relies on an existing domain generalization (DG) method for initialization, it is imperative to benchmark against more recent approaches. Demonstrating how the proposed method improves upon current state-of-the-art frameworks would significantly strengthen the paper's impact. Comparisons with the latest methods are necessary to provide a comprehensive evaluation in the context of contemporary DG frameworks.

## Minors:

1. An ablation study assessing the performance of the proposed PTG without relying on other domain generalization (DG) methods for initialization is necessary. Evaluating PTG using only a pre-trained ResNet-18 as initialization for model training on each domain would provide valuable insights into its standalone effectiveness.

2. Several grammatical errors need correction, such as the use of "show" instead of "shown" on page 4, section 3.2.


### Questions
1. The authors in section 3.3 suggest initializing the BNN on each domain with a uniformly well-generalized model, such as a BNN trained using Empirical Risk Minimization (ERM). The confusion arises regarding the connection between initializing the model on each domain and selecting the best model through ERM. To clarify, the authors advocate training a BNN using ERM on a specific dataset before initializing it on different domains. The dataset used for this ERM training is not explicitly mentioned in this section, but it is the dataset that provides the well-generalized model used as the starting point for initialization across various domains. In essence, the ERM-trained BNN serves as a kind of starting point. It is trained on a particular dataset that captures general patterns. My understanding is that this well-generalized model is then employed as the initial configuration for the BNN when dealing with different domains. The emphasis is on using a model that has already demonstrated good generalization capabilities through ERM, ensuring a solid starting point for adaptation to diverse domains.

2. The terminologies used in the paper are confusing. In the introduction, the authors equate domain-invariant features to domain-invariant parameters. In typical deep-learning contexts, parameters refer to learnable model weights and biases, while features denote the encoder's output. To prevent potential misinterpretations, it would be helpful if the authors could offer clear definitions for parameters and features within the scope of their work.

3. Could you provide clarity on the definition of the prior model in the proposed work? Is it initialized from the pretraining of ResNet, or is it initialized from the pretraining of another domain generalization (DG) method? Please elaborate on this aspect.

4. Could you specify the space in which domain-invariant and domain-specific information is defined? Is it in the input space, latent space, or output probability space? If it's in the input space, how does \mathcal{D} change? If it's in the latent and output spaces, how does p(\mathcal{D}^{c}) remain constant? Clarification on this aspect would enhance understanding.

5. In Algorithm 1, when the authors mention updating the model parameters with a Gaussian distribution, are they referring to sampling the model parameters from the Gaussian distribution outlined in Equation (4)? If so, could you provide clarification on the method used for this sampling process? Is it achieved through random sampling? Please provide additional details.

6. In Figure 2, the authors mention extracting domain-invariant information from domain-specific features (Z^V). Given that these features reside in the encoded space (the output space of ResNet-18) if the training of ResNet-18 is indeed effective in extracting domain-invariant features, it raises a question: How can domain-invariant information also be present within features specifically identified as domain-specific? The term "information" is used without a clear definition from the authors. This ambiguity, coupled with an unclear definition of \mathcal{D}, restricts readers from fully grasping the paper's content. Could the authors provide more clarity on interpreting "information" and a more explicit definition of \mathcal{D}? My understanding is that the authors are trying to claim that the feature map might not effectively capture the domain-invariant information from the data. If my understanding is correct, then the claim is very ambiguous. The authors should at least provide some ways to quantify or visualize it. In the current version of the paper, this claim is not supported theoretically or empirically.

### Soundness
3 good

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a posterior generalization method for domain invariant learning. Different from the previous methods that do invariant learning on features, the proposed method directly infers the invariant posterior of the parameters by posterior aggregation. The authors also propose a lite version of posterior generalization for widespread applications. Experiments on DomainNet show the effectiveness of the proposed method.

### Strengths
1. The idea of directly inferring the invariant posterior of the model parameters is novel and interesting.

2. The experiments show the effectiveness of the proposed method.

### Weaknesses
1. Although the idea is interesting, it is still unclear why directly inferring the domain invariant model posteriors is better than feature invariant learning. The authors argue that the proposed method can extract more invariant information from features but the reason is also not clear. Specifically, it's not well-explained how the parameter-level invariance translates to improved feature invariance, or why learning a posterior distribution over parameters is inherently superior for capturing invariant information compared to learning invariant feature representations directly through methods like adversarial training or domain-specific normalization layers. The paper needs a more rigorous justification for this design choice, perhaps through theoretical analysis or a more detailed empirical comparison with feature-based methods.

2. As the author posted, the proposed method is not memory efficient since BNNs require more parameters than the deterministic models. This is a significant practical limitation, especially when considering the computational resources required for training and deploying large-scale models. The paper should acknowledge this limitation more explicitly and discuss potential strategies to mitigate the increased memory footprint, such as using more efficient BNN architectures or approximation techniques.

### Questions
It seems there are three stages of PTG, first pre-training the BNN models by ERM, then learning source domain-specific posteriors, at last generating the invariant posterior and training the classifier. It is better to make this procedure clear in the paper for easier following. And there are some details also need to be clarified. 

1. Before pretrained on the source domains by ERM, is the BNN parameters initialized randomly or by ImageNet pretrained parameters? 

2. In eq.(4), what are the mean and variance for each BNN convolutional layer? are they channel-wise vectors or scalers?

3. once obtained the mean and variance of the invariant posterior f_0, how to sample the parameters? By Monte-Carlo sampling?

4. In the algorithm, I found that in each training iteration, the source-specific posterior f_i is updated first, then the method aggregates them as the invariant posteriors and trains it together with the classifiers. However, in the next iterations, the f_i is updated again without considering any information in f_0, and f_0 is updated according to the new f_i, also without the f_0 in the previous iterations. If it is, why need to update f_0 by the cross-entropy loss functions?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to directly learn the domain invariant posterior distribution of network parameters. The theoretical analysis shows that the invariant posterior of parameters can be implicitly inferred by aggregating posteriors on different training domains. Accordingly, this paper proposes a simple yet effective method, named PosTerior Generalization (PTG), that can be used to estimate the invariant parameter distribution.

### Strengths
This paper introduces parameter posterior distributions into domain generalization for the first time. And propose two simple yet effective domain generalization methods named Posterior Generalization based on their theories. 
The proposed method is simple in theory and algorithm implementation, yet effective as shown by the empirical studies.

### Weaknesses
 There are some typos, and the writing can be improved.

 There are some conceptual issues. Please give clear definitions of $\omega$ and $\theta_i$. How they are related, and how they determine $f_i(\dot)$. In equations (4), (5) and (6), the notations of expectation and variance do not follow the convention of probability theory. The reviewer fails to figure out what the expectation is taken of, and with respect to what. Even when the reviewer turns to the appendix, it is difficult to understand because $\theta$ and $\omega$ is not clearly defined. The reviewer understands it as the follows: $\omega$ is the model parameter, like the weight of a neural network? $\theta$ corresponds to the mean, $\mu$, and variance, \sigma, when the variational distribution takes Gaussian distribution form.  But if it is the case, by variational inference, \theta is a function of $\omega$ determined by the model (e.g., a neural network); then, how to understand $q(\omega|\theta_i)$. Maybe when your model (the neural network) is not a deterministic model, meaning, both $\omega$ and $\theta$ are random, the above seems right. 

The proposed algorithm needs to train a featurizer for each domain. It is computationally expensive.

### Questions
1.	Please give clear definitions of $\omega$ and $\theta_i$. How they are related, and how they determine $f_i(\dot)$. 
2.	In equations (4), (5) and (6), the notations of expectation and variance do not follow the convention of probability theory. The reviewer fails to figure out what the expectation is taken of, and with respect to what. Even when the reviewer turns to the appendix, it is difficult to understand because $\theta$ and $\omega$ is not clearly defined. The reviewer understands it as the follows: $\omega$ is the model parameter, like the weight of a neural network? $\theta$ corresponds to the mean, $\mu$, and variance, \sigma, when the variational distribution takes Gaussian distribution form.  But if it is the case, by variational inference, \theta is a function of $\omega$ determined by the model (e.g., a neural network); then, how to understand $q(\omega|\theta_i)$. Maybe when your model (the neural network) is not a deterministic model, meaning, both $\omega$ and $\theta$ are random, the above seems right. 
3.	The proposed algorithm needs to train a featurizer for each domain. It is computationally expensive.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
