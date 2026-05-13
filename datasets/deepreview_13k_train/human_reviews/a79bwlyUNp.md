# In-Context Learning for Full Bayesian Inference

- Decision: Reject
- Scores: 5, 5, 8, 6

## Abstract
Transformers have emerged as the dominant architecture in the field of deep learning, with a broad range of applications and remarkable in-context learning (ICL) capabilities. While not yet fully understood, ICL has already proved to be an intriguing phenomenon, allowing transformers to learn in-context---without requiring further training. In this paper, we further advance the understanding of ICL by demonstrating that transformers can perform full Bayesian inference for commonly used statistical models in-context. More specifically, we introduce a general framework that builds on ideas from prior fitted networks and continuous normalizing flows and enables us to infer complex posterior distributions for models such as generalized linear models and latent factor models. Extensive experiments on real-world datasets demonstrate that our ICL approach yields posterior samples that are similar in quality to state-of-the-art MCMC or variational inference methods that do not operate in-context. The source code for this paper is available at https://anonymous.4open.science/r/ICL_For_Full_Bayesian_Inference-3F53

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work aims to investigate whether the In-context learning (ICL) using the transformer can yield similar samples with fully Bayesian inference. To this end, the authors first set the distribution of the dataset, induced by GLM models and factors models, as the target distribution. Then, they demonstrate that when the transformer-based model is trained using the variant of ICL loss $d_{CFM}$ and continuous normalization flow (CNF), then the trained model can yield the posterior distribution that more accurately approximates the targeted posterior than the existing laplace and variational inference methods.

### Strengths
* This work demonstrates that in-context learning can yield the posterior distribution of datasets on more complex real datasets as the posterior distribution obtained by fully Bayesian inference can sample. 

* This work is well written to understand the proposed methodology.

### Weaknesses
 * Based on [1], it has been already investigated that transformer-based in-context learning (ICL) can do Bayesian inference. 
Without presenting the advantage of fully Bayesian inference of ICL,  demonstrating the extension of ICL capability, seems incremental contribution.



* In experiment, the baseline models for Laplace and VI except for (IAF) seem small compared to the size of the transformer used for ICL because the baseline of LA and VI use GLM or Factor models, whereas the ICL uses the transformer.




### Questions
*   Why do the authors consider extending the ICL capability to fully Bayesian inference? What is the advantage of extending the ICL capability to full Bayesian inference beyond Bayesian inference? In this work, most experiments seem to focus on demonstrating the good approximation of the true posterior distribution for GLM and the factor models by the ICL without its upcoming benefits. 


* To strengthen the novelty of this work, it would be better if the authors could demonstrate that the ICL capability of being good at posterior approximation, can be effective for improving the performance of Bayesian optimization or few-shot learning as conducted in [1].


* If ICL uses other distribution match methods such as VAE or Score matching instead of the continuous normalization flow (CNF), could the ICL still approximate the posterior distribution accurately? It seems less clear how important the type of loss in Eq. (5) is in the sense of accurate approximation for ICL.  It would be better to conduct the ablation study comparing the loss of Eq. (5) with the loss of other distribution matching methods, and thus explaining why the loss of Eq. (5) is necessary.


* In Tables 1, 2, 3, and 4, how complex models are used for the baseline of VI and Laplace approximation (LA)? Could you compare the mode size used for LA, VI, and ICL? If the model size of ICL is too large compared to that of LA and VI, I am worried about whether this comparison is fair.  If each model size is different, could compare the LA, VI, and ICL under the same model size ? 


[1] Transformers Can Do Bayesian Inference - ICLR 22

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores using in-context learning within transformers to perform full Bayesian inference on complex statistical models. The authors propose a framework leveraging continuous normalizing flows and flow matching, enabling transformers to infer posterior distributions in-context without explicit parameter updates. The approach is applied to GLMs, latent factor models, and GMMs, which often require techniques like Hamiltonian Monte Carlo (HMC) or variational inference (VI). The reliance on synthetic data for training may introduce biases when tested on real-world distributions that differ from synthetic priors. The results highlight ICL's potential as an efficient, flexible Bayesian inference tool that can operate directly on a diverse range of models and posterior complexities. This paper opens up further exploration into using ICL for full probabilistic modeling, potentially extending its use beyond traditional Bayesian inference.

### Strengths
1. Innovative Framework for Bayesian Inference: The paper introduces a novel approach to using in-context learning (ICL) with transformers for Bayesian inference. By employing continuous normalizing flows (CNFs) and flow matching, the framework effectively handles high-dimensional posterior distributions, making it relevant for complex statistical models like generalized linear models (GLMs) and Gaussian mixture models (GMMs).

2. Strong Empirical Comparisons: The authors conduct extensive experiments, benchmarking ICL-based Bayesian inference against both Hamiltonian Monte Carlo (HMC) and various variational inference (VI) methods. Their approach shows promising results, especially in scenarios where VI models struggle with multimodality or non-normal distributions.

3. Real-World Applications: This paper evaluates performance on real-world datasets, enhancing the practical applicability of the proposed method. This broadens the scope of ICL by demonstrating its potential to rival or even outperform established inference techniques on complex, non-synthetic data.

### Weaknesses
1. Computational Expense and Scalability Issues. While ICL may yield accurate approximations of posterior distributions, it requires a high computational investment in training. This can limit the approach’s scalability, especially in real-world applications requiring quick adaptability across various data regimes. The paper's acknowledgment of this limitation highlights the need for optimization and scalability improvements, which were not sufficiently addressed.

2. Lack of Detailed Architectural Justification. Although the authors introduce a transformer-based architecture with flow matching for Bayesian inference, the rationale for specific architectural choices, such as the reliance on continuous normalizing flows over other methods, is underexplored. This omission leaves unanswered questions regarding the necessity or superiority of these choices compared to simpler or more established architectures for similar tasks.

### Questions
N/A. See weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel approach to in-context learning that leverages transformer architectures and continuous normalized flow for a fully Bayesian inference framework. The main objective of this method is to simplify the conditions of fully bayesian inference by employing the in-context learning with transformer architecture, which is widely used in large language models and is recognized for its generalized capabilities across various tasks. Unlike existing algorithms that rely on pre-defined tractable distribution for latent variables, this approach enables the model to implicitly learn the relationship between latent and output variables. This implicit learning led by continuous normalizing flow aligns with both the data and a tractable distribution, thus removing the need for precise proxy distributions.

To validate the effectiveness of their method, the authors performed experiments on latent variable models, specifically GMM, Factor Analysis, and GLM. Results indicate that the in-context learning approach provides a more generalizable and efficient means of utilizing learned information across synthetic datasets, consistently achieving robust generalization on latent variable models. Further analysis of the marginal distributions demonstrates that the proposed method more closely aligns with the true latent distributions compared to existing approximate techniques.

### Strengths
- The paper offers comprehensive explanations of each concept, articulating the roles and functions of all elements with clarity. Additionally, it effectively contextualizes the research within the scope of existing studies, highlighting connections to prior work and establishing a solid foundation in the literature.

- The paper provides a clear account of the experimental design and the significance of the findings. By testing the model on diverse latent variable models, it illustrates the model’s applicability and potential impact, offering valuable insights into its relevance and effectiveness across multiple contexts.

### Weaknesses
 - The paper does not clearly present the inherent limitations of its approach. Specifically, except for the GMM case, there is insufficient discussion regarding concerns and constraints related to model specification. I believe that this limitations are not fully addressed in the most cases. To strengthen the paper, it is essential to explicitly outline potential failure cases for this model and specify how it may underperform compared to existing models in certain scenarios by varying model specification. Without such clarification, there is a potential risk that the contributions of this paper may be overrated.

- Although the paper briefly mentions synthetic data, a more thorough exploration of design of synthetic datasets is essential. I observed simple describing synthetic data in appendix, however, it is important to consider how variations in the datasets or hyper-parameters impact model performance. Additionally, I believe that analysis of the model’s behavior in out-of-distribution scenarios would be valuable insights. Including these aspects would offer a more comprehensive understanding of the model’s robustness and applicability across diverse conditions.

### Questions
I would like to inquire whether a comparison with gradient descent-based VI approaches, such as Langevin dynamics[1] or stochastic variational inference[2], would be feasible in terms of evolving latent samples. Since this paper uses flow-matching to model changes, comparing the latent variable sampling steps with these gradient-based VI methods could provide further insights. Such a comparison may help demonstrate that the proposed approach more effectively captures variations in the latent variables, potentially highlighting its advantages in representing the implicit distribution of latent spaces.


**Reference**  

[1] Welling, Max, and Yee W. Teh. "Bayesian learning via stochastic gradient Langevin dynamics." Proceedings of the 28th international conference on machine learning (ICML-11). 2011.

[2] Hoffman, Matthew D., et al. "Stochastic variational inference." Journal of Machine Learning Research (2013).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work proposes an in-context learning (ICL) approach for full Bayesian inference.
Specifically, PFN is used as a prior, and flow matching is adopted for posterior inference.
Experiments show that ICL can perform similarly to the Hamiltonian Monte Carlo sampler, and its sample quality is better than variational inference.

### Strengths
- The experimental results demonstrate that the proposed method approximates the posterior more accurately than VI-based approaches.
In particular, Figure 2 clearly illustrates that the ICL's posterior aligns well with the ground-truth HMC's, while the posteriors by VIs fail to approximate multi-modal distributions. Interestingly, the autoregressive flow-based VI also fails in that way, contrary to its expected property.

### Weaknesses
 - How to infer the posterior using the proposed method is not explicitly explained.
- The writing could be improved. For example, the current manuscript carefully explains continuous normalizing flows, which is appreciated, but it is unclear how they are used in the proposed method.
- To my understanding, in the ICL framework, the (foundation) model, typically, Transformer, learns algorithms implicitly through the pre-training (e.g., Garg's work).
In this work, however, the model seems designed for inference and pre-training on many related tasks.
I would call such a framework meta-learning, rather than ICL.

### Questions
- It would be interesting if the runtime of both pre-training and inference of the proposed mthod was shown.

### Soundness
3

### Presentation
2

### Contribution
3
