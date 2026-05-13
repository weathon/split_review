# A Bayesian Approach for Personalized Federated Learning in Heterogeneous Settings

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
In several practical applications of federated learning (FL), the clients are highly heterogeneous in terms of both their data and compute resources, and therefore enforcing the same model architecture for each client is very limiting. The need for uncertainty quantification is also often particularly amplified for clients that have limited local data. This paper presents a unified FL framework based on training customized local Bayesian models that can simultaneously address both these constraints. A Bayesian framework provides a natural way of incorporating supervision in the form of prior distributions. We use priors in the functional (output) space of the networks to facilitate collaboration across heterogeneous clients via an unlabelled auxiliary dataset. We further present a differentially private version of the algorithm along with formal differential privacy guarantees that apply to general settings without any assumptions on the learning algorithm. Experiments on standard FL datasets demonstrate that our approach outperforms strong baselines in both homogeneous and heterogeneous settings and under strict privacy constraints, while also providing characterizations of model uncertainties.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a personalized FL approach based on aggregating scores on publicly available dataset instead of aggregating model parameters. They use a Bayesian framework to model the heterogeneity, consequently the optimization problem. Score aggregation, which is motivated by the Bayesian framework, enables collaboration of clients with different architectures. They also utilize DP to prevent information leakage due to sharing scores on public dataset. They provide experiments on various dataset and provide utility-privacy tradeoff of the algorithm.

### Strengths
- The method is architecture agnostic, enabling the collaboration of resource heterogeneous clients. 
- Use of Bayesian modelling in formulating the problem is clearly explained. 
- The authors use DP to reduce information leakage due to sharing scores on a public dataset. 
- Presented experiments show significant performance increase compared to competing methods.

### Weaknesses
 - The major weakness is that many of the ideas presented in the paper was already explored in the literature. And these papers are not discussed in the related works. Let me elaborate,

The idea of aggregating scores on a public dataset instead of model weights was presented in [1] in 2019 although for training a global model. Using a Bayesian view for modelling the heterogeneity problem in FL through learning a prior was studied in [2,3,4]. Especially, [2,4] should be compared to in details in terms of modelling, note [4] also uses DP for enhancing privacy. The idea of collaborating resource and data heterogenous clients is presented in the paper as a novel contribution, however, [1,5] already did it (again there is no comparison to those methods).

Overall, it is not clear what is the contribution of the paper over those papers since they are not mentioned in the related works. 

- Public unlabeled dataset is seen as a mild assumption. But, imagine planting this additional dataset to millions of devices, this can introduce inefficiencies in the system and waste client's precious resources.

- Generating $\Phi^{corrected}$ requires tuning an additional hyper-parameter $\gamma$ which further introduces inefficiency, since each client might need to do validation runs to tune it. 

- There are several unclear points to me in the experiments. For instance what is the overall privacy budget for your DP method and DP-FedAvg, it says epsilon per round is smaller than 0.1 but what is the exact budgets?

- The majority of the experiments in the main text is done using 20 clients. It is not clear to me if the performance difference will persist in higher client regime, which is more realistic for FL.

- There is no comparison to local only training, this is a critical point.

- The supplementary material does not include code.

### Questions
Please address the points above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a Bayesian framework for personalized federated learning, allowing different clients to train different architectures. This approach assumes an auxiliary public dataset (AD), which is used to initialize the local priors and share information (aggregated model output logits) between client and server. Each client has its own Bayesian neural network and initializes its prior by optimizing its model outputs to be close to the global model outputs. The local optimization then approximates the local posterior via variational inference. Finally, the model outputs from the new local model are shared to the server. To protect the privacy, the authors proposed to add local DP to the shared model outputs with Gaussian mechanism. This approach is evaluated on several benchmark datasets with different heterogeneous settings and is shown to be superior to the previous works.

### Strengths
- This paper is well-motivated as Federated learning in practice can experience extreme heterogeneous settings and one global model architecture will likely not fit all clients. 
- The personalization method is novel where only the outputs instead of any weight parameters will be shared, which could be more communication-efficient for larger models. The local DP also provides a strong privacy guarantee. And the results from Table 1 indicated that the proposed method is superior to the others, though it does have an extra assumption that a good AD exists.

### Weaknesses
 - The proposed method seems to heavily depend on how good AD is. Indeed, for common image and text tasks, it might be easy to find such a public dataset. But for more sensitive tasks on devices, such a public dataset might not exist. The paper does not sufficiently explore the sensitivity of the method to the quality and relevance of the auxiliary dataset (AD). A more thorough analysis is needed to understand how performance degrades with increasingly dissimilar or noisy ADs. For example, what is the impact of using an AD with a different label space or significantly different data distribution?
- Scale of experiments is small, where the tasks such as MNIST or CIFAR10 are relatively simple. It is hard to know whether the method can generalize to larger models or harder tasks by just sharing the model outputs. The experiments should include more complex datasets and models to demonstrate the scalability and robustness of the approach. Specifically, the paper lacks experiments on tasks with higher dimensionality, more complex data distributions, or larger model architectures, which are common in real-world federated learning scenarios.
- Local DP noise results with such a small epsilon seems to be unreasonably good, as they are nearly all better than the non-DP baseline for CIFAR. From Theorem 2, with $(\epsilon, \delta)=(5, 10^{-4}), E=200, K=2000$, then $\rho\approx 1.7 * 10^{-6}$, the noise standard deviation is about 767 which is much larger than the output scale. It would be great if the authors can explain how local prior optimization is not impacted by DP noise and outperform the non-DP baselines. The paper needs to provide a more detailed explanation of how the local prior optimization is robust to the added DP noise, especially given the high noise levels implied by the privacy parameters. The current explanation is insufficient and lacks a rigorous analysis of the interaction between the noise and the optimization process. A more thorough investigation of the impact of different noise levels on the local prior optimization is necessary.
- Also since the authors considered a public dataset is available, then the DP baseline should also be those with such assumptions, such as [1]. The comparison with DP baselines should be expanded to include methods that also leverage a public dataset, as this is a key assumption of the proposed approach. The current comparison is not entirely fair as it does not consider other methods that operate under similar assumptions.
- Minor: presentation of the hierarchy in Algorithm 1 can be improved.

### Questions
- Why not consider central DP (where the noise is added once on the aggregated output), which is a more common practice in federated learning?
- In the appendix, why does SVHN (an OOD dataset) as AD give better results than CIFAR10 as AD? 
- Why is the sensitivity of the model outputs bounded by 2? How did this bound get enforced?
- There seems to be a simpler non-Bayesian alternative: clients can use the aggregated outputs and train a smaller model on AD using distillation, then fine-tune the distilled model on their private dataset. How would this baseline compare to the Bayesian approach?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies personalized federated learning algorithms under differential privacy constraints.  Consider a set of clients connected to a central server, where each client has a local dataset. The goal is to design individual models for each client while preserving privacy of the clients' data with the help of the Alignment Dataset (AD) available on the server side. DP federated learning algorithm based on the Bayesian approach has been proposed. At each round, each sampled client runs a local optimizer to update her own model, and then the client privately reports the output of the local NN on the alignment dataset (AD). The server aggregates the clients' reports and sends the aggregation to the sampled clients in the next round. The aggregated output obtained from the server represents the collaborative information between clients and is used to improve learning the individual models.

### Strengths
I think the new idea in this paper is the following. Instead of sharing the local models $\mathcal{W}_i$, each client shares how the local model $\mathcal{W}_i$ classifies the shared dataset (Alignment Dataset(AD)).  Then, each client improves her local training by distilling information from the aggregated outputs.  However, it is not clear to me why this might be a useful idea in personalized learning.

### Weaknesses
In my opinion, there is a lack of explanation and justification for the theoretical model. For example, what is the assumption on distributions $\mathbb{P}[\mathcal{X}]$, and $\mathbb{P}[\mathcal{X}|\mathcal{W}_i]$.  Also, there are missing lots of details of the main algorithm and a lack of theoretical analysis of the proposed scheme. The existence of a public dataset might be a strong assumption. Furthermore, it is not easy to share this public dataset with all clients in federated learning. Please, read my questions below.

- What is the assumption that connects the local model $\mathcal{W}_i$ and the local dataset $\mathcal{X}_i$? It is supposed to be a probabilistic model of how the data is generated for a given local model $\mathcal{W}_i$.

- In Section 3.2 (local setting): Are the prior distributions means $\lbrace\mu_i\rbrace$ and variances $\lbrace\sigma_i\rbrace$ are unknown to the clients? Why is the assumption that the models are generated from Gaussian distribution? Which step in the algorithm this assumption is used for?

- Why the shared data $\Phi_i(AD)$ is a useful information? What if the alignment dataset (AD) has a distribution that is completely different from the distribution of the local datasets $\lbrace \mathcal{X}_i\rbrace$?

- Why the assumption that the distribution $\mathbb{P}[\mathcal{W}_i|\mathcal{X}]$ lies in the family of Gaussian distributions? Even if $\mathbb{P}[\mathcal{W}_i]$ has a prior Gaussian distribution, that doesn't mean that $\mathbb{P}[\mathcal{W}_i|\mathcal{X}]$ is Gaussian.

- What is $p(\mathcal{W}_i;\psi)$ defined before Eqn (1) refers to and how this parameter is connected to the true distribution $\mathbb{P}[\mathcal{W}_i|\mathcal{X}]$

- Could you please explain in more detail how we get (2) from (1)?

- Please explain in Theorem 4.2 what is the value of the variance $\sigma_g^2$ to achieve $\left(\varepsilon,\delta\right)$-DP. 

- The $L_2$ sensitivity of the model is not clear to me. As far as I understand, $\Phi_i(AD;\mathcal{W}_i)$ denotes the output of the NN on the alignment dataset (AD). Thus,  $\Phi_i(AD;\mathcal{W}_i)$ has the same size as the number of samples in the dataset AD right? Thus, the sensitivity is supposed to be a function of the size of the AD. Please, explain as I might be missing something.

### Questions
- What is the assumption that connects the local model $\mathcal{W}_i$ and the local dataset $\mathcal{X}_i$? It is supposed to be a probabilistic model of how the data is generated for a given local model $\mathcal{W}_i$. 

- In Section 3.2 (local setting): Are the prior distributions means $\lbrace\mu_i\rbrace$ and variances $\lbrace\sigma_i\rbrace$ are unknown to the clients? Why is the assumption that the models are generated from Gaussian distribution? Which step in the algorithm this assumption is used for?

- Why the shared data $\Phi_i(AD)$ is a useful information? What if the alignment dataset (AD) has a distribution that is completely different from the distribution of the local datasets $\lbrace \mathcal{X}_i\rbrace$?

- Why the assumption that the distribution $\mathbb{P}[\mathcal{W}_i|\mathcal{X}]$ lies in the family of Gaussian distributions? Even if $\mathbb{P}[\mathcal{W}_i]$ has a prior Gaussian distribution, that doesn't mean that $\mathbb{P}[\mathcal{W}_i|\mathcal{X}]$ is Gaussian.

- What is $p(\mathcal{W}_i;\psi)$ defined before Eqn (1) refers to and how this parameter is connected to the true distribution $\mathbb{P}[\mathcal{W}_i|\mathcal{X}]$

- Could you please explain in more detail how we get (2) from (1)?

- Please explain in Theorem 4.2 what is the value of the variance $\sigma_g^2$ to achieve $\left(\varepsilon,\delta\right)$-DP. 

- The $L_2$ sensitivity of the model is not clear to me. As far as I understand, $\Phi_i(AD;\mathcal{W}_i)$ denotes the output of the NN on the alignment dataset (AD). Thus,  $\Phi_i(AD;\mathcal{W}_i)$ has the same size as the number of samples in the dataset AD right? Thus, the sensitivity is supposed to be a function of the size of the AD. Please, explain as I might be missing something.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a personalized federated learning framework based on Bayes Learning methods to tackle the heterogeneity. Specifically, this paper proposes FedBNN, which utilizes a globally shared alignment dataset to collect the information of the models on all the clients and find a better prior distribution for the local model. With the optimized prior, a personalized posterior is obtained by the local variational inference. DP-based methods can be applied to FedBNN to guarantee privacy.

### Strengths
This paper proposes a novel Bayes Learning framework FedBNN which attains significantly better performance compared with previous baselines under the heterogeneous settings. More specifically, the strengths of this paper lie in the following aspects:

1.	FedBNN successfully addresses both systematic and statistical heterogeneity in federated learning by adopting functional sharing instead of model sharing. This makes the framework more practical and flexible.

2.	A DP-based method is provided to guarantee the privacy of FedBNN with rigorous proof. 

3.	Sufficient experiments show that FedBNN outperforms previous baselines under highly heterogeneous settings while maintaining high privacy.

### Weaknesses
While the proposed method is shown to be promising, some clarity issues should be addressed to improve this paper. More specifically,

1.	More details of Bayes Learning could be introduced with mathematical definitions. For a reader who is not so familiar with Bayes Learning, it would be helpful to include a basic framework of Bayes Learning. For example, the optimization objective and training procedure of standard Bayes Learning, as well as the definition of $q(W_i|\theta)$ and $p(W_i;\psi)$. It is not clear how the variational posterior $q(W_i|\theta)$ is parameterized and optimized. Specifically, what is the form of the variational distribution, and what is the objective function being optimized during local training? The paper should explicitly state the form of $q(W_i|\theta)$, such as a Gaussian distribution with a mean and variance parameterized by $\theta$, and provide the explicit form of the Evidence Lower Bound (ELBO) that is being maximized.

2.	It appears to me that the significance of FedBNN mainly comes from the utilization of the public alignment dataset instead of Bayes Learning. It would be better to include a baseline that trains the model $W_i$ directly instead of using Bayes Learning. Namely, the public alignment dataset is used for knowledge distillation at the beginning of each communication round to initialize $W_i$, and then $W_i$ is trained with private local data. This would help to isolate the impact of the Bayesian approach from the effect of the alignment dataset. Without this baseline, it's hard to determine if the performance gains are due to the Bayesian framework or simply the use of the alignment dataset for pre-training.

### Questions
1.	What is the form of $p(W_i;\psi)$? Is it also a Gaussian Distribution parameterized by $\psi$?

2.	Are the local datasets of different clients overlapped? For example, in the full setting of CIFAR10, each client has 5 classes and thus 12500 samples, which requires 250000 samples in total without any overlapping. This is not a standard setting in Federated Learning.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
