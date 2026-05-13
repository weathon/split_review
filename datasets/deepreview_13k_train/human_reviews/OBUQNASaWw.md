# SparsyFed: Sparse Adaptive Federated Learning

- Decision: Accept
- Scores: 5, 8, 6, 5, 3

## Abstract
Sparse training is often adopted in cross-device federated learning (FL) environments where constrained devices collaboratively train a machine learning model on private data by exchanging pseudo-gradients across heterogeneous networks. Although sparse training methods can reduce communication overhead and computational burden in FL, they are often not used in practice for the following key reasons: (1) data heterogeneity impacts more clients’ consensus on sparse, compared to dense, models, requiring training for longer; (2) a lack of sufficient plasticity to adapt to never-seen data distributions, crucial in cross-device FL; (3) requiring additional hyperparameters, which are notably challenging to tune in FL. This paper presents SparsyFed, a practical federated sparse training method that critically addresses all the aforementioned problems. Previous works have only managed to solve one, or perhaps two of these challenges, and at the expense of introducing new trade-offs, such as clients’ consensus on masks versus sparsity pattern plasticity. We show that SparsyFed simultaneously (1) can produce 95% sparse models, with negligible degradation in accuracy, while only needing a single hyperparameter, (2) achieves a per-round weight regrowth 200 times smaller than previous methods, and (3) still offers plasticity under this sparse design, by outperforming all the baselines at adapting to never-seen data distributions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper discusses utilizing sparse learning to reduce communication and computation costs in cross-device federated learning. The authors propose the SparsyFed algorithm, where in every round, the participants first reparameterize the weights and then perform the forward pass. In the next step, before calculating the gradient, each client prunes the activations in each layer. Finally, it only sends back the TopK large gradients to the server. This way, they can reduce client communication costs to the server.

### Strengths
* The writing, motivation, and related works have been clearly explained.

* The algorithm achieves high sparsity ratios and communication cost reduction with low-performance degradations.

* The authors have presented interesting results in the evaluation section.

### Weaknesses
 * The novelty of the algorithm is not apparent.

* While the paper is well-written, and the authors have successfully conveyed the problem statement, the algorithm is not clearly explained. For example, how does step 8 work?

* It is not clear why different decisions have been made and what effect each of them has on the final performance. For example, why does weight reparameterization work, or how does layer-wise top-k selection result in layers with different sparsities? 

* The experiment section only covers resent18, and it is unclear if this method works on other types or sizes of models.

* Based on my understanding, line 8 in Algorithm 2 only calculates the zeros/total num params ratio. Does it mean that there is no control over layer-wise sparsity? Can this method cause layer collapse or mostly uniform sparsities?

* I still believe ResNet models are very resilient to layer collapse because of their structure. However, they are not the most commonly used model in a federated setting. The authors could show that their method is also applicable to other standard model families; otherwise, it limits the scope of the paper.

* About the Powerpropagation baseline, is the only difference between Powerpropagation and Sparsyfed the fact that in Sparsyfed, the same pruning is applied at the **end of every FL round** instead of at the **end of the training** (besides the natural differences between FL and centralized training)?

### Questions
* Why did not the authors not consider other existing works they mention as their baseline?

* Could the authors explain the distinction between their paper and a naive federated version of [Schwarz et al. (2021)]? 

* Is the sensitivity of this method to client participation rate, number of clients, and number of data points within each client? Is it possible that when some clients do not have enough data, SparsyFed might fail to converge or find a proper sparse model?

* What is the computation cost of steps 8 - 9 - 10 in algorithm 2 compared to full training?

* In the appendix, the authors presented two versions of the FLASH algorithm, one of which does not fix the mask (G.4). Could the authors explain why they selected G.3 over G4? Because it seems that G4 does not have the plasticity problem.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
SparsyFed is designed for cross-device environments where devices have limited computational and communication resources. Traditional federated learning approaches struggle with communication overhead, computational demands, and data heterogeneity across devices, especially with dense models. SparsyFed addresses these challenges by introducing sparse adaptive federated training, which reduces the model’s memory and computational requirements while retaining high accuracy. The key innovations include a sparsity-inducing weight reparametrization technique that requires only a single additional hyperparameter and a method for pruning activations to reduce computational load on clients. SparsyFed achieves up to 95% sparsity with minimal accuracy loss, which is particularly beneficial for constrained edge devices in cross-device FL.  SparsyFed demonstrates significant improvements over traditional and recent sparse FL baselines, achieving a 19.29× reduction in communication costs and faster global model convergence. The challenges of data heterogeneity, limited client resources, and the need for high sparsity without complex hyperparameter tuning are addressed through its adaptive and lightweight design.

### Strengths
This paper is well written and has a solid motivation. The strength of this paper is as follows,

1. SparsyFed can achieve target sparsity levels of up to 95% while maintaining competitive accuracy. This is particularly beneficial in federated learning environments, where models often face challenges from heterogeneous data distributions​.

2. The method significantly reduces communication overhead, achieving up to 19.29 times less communication than dense models. 

3. This is crucial in cross-device federated learning where devices often have limited bandwidth unlike many federated learning methods that require multiple hyperparameters, SparsyFed simplifies the tuning process by needing only one hyperparameter.

### Weaknesses
This paper is experimentally solid but theoretically weak. The weaknesses of this paper are as follows,

1.	The authors mentioned the model’s sparsity by reducing the FLOPs and memory footprint in lines 207 and 208. However, the authors have not given any experimental evaluation of it. It would be good to give a FLOP analysis of SparsyFed with the dense model. Specifically, a breakdown of FLOPs reduction per layer would be beneficial to understand where the computational savings are most significant. This analysis should also consider the overhead introduced by the sparsity operations themselves, such as mask application and weight reparameterization.

2. In experiments (line 325) “19.29×less communication costs compared to the dense model” what is the convergence bound of the proposed algorithm? Is it similar to FedAvg? Why is SparsyFed more efficient in communication than state-of-the-art? The authors should provide a more detailed comparison of communication costs with other sparse federated learning methods, including a breakdown of uplink and downlink communication. Furthermore, it is unclear if the communication cost reduction is solely due to the reduced model size or if the proposed method also reduces the number of communication rounds required for convergence.

3. I do not understand Figure 1 (right). Is it the comparison of the different local models or the global model? What happens when the target sparsity is more than 90%? I think author should elaborate more on  Consensus on the spare masks across clients (Section 5.3). The figure caption is not clear enough, and the implications of the observed trends are not well explained. The authors should clarify whether the sparsity is measured on local models before aggregation or on the global model after aggregation. Additionally, the behavior of the method at very high sparsity levels (e.g., >90%) needs further discussion, including potential performance degradation and mask instability.

4. In Table 2, If we increase sparsity why SparsyFed with activation pruning perform worse in both IID and non-IID scenarios? What happens when $\alpha$ =0.1 ? The inference from the observation is not clear to me. The authors should provide a more detailed analysis of the impact of activation pruning on performance at different sparsity levels. It is unclear why activation pruning degrades performance at higher sparsity levels, and a more thorough investigation into the interaction between weight sparsity and activation sparsity is needed. The choice of $\alpha$ and its impact on the trade-off between sparsity and accuracy should also be discussed.

5. In Figure 3, the authors proposed these reparameterization methods or those available in the state-of-the-art ? What authors tried to show here is unclear to me could author please elaborate more on Figure 3 ? The figure lacks a clear explanation of the purpose of comparing different reparameterization methods. The authors should clarify whether these methods are novel or adopted from existing literature. The criteria for selecting these methods and the specific advantages of the chosen method should be explicitly stated.

### Questions
Asked in weakness

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
4

### Summary
SparsyFed introduces a novel approach to federated sparse training that achieves high model sparsity (95%) while maintaining accuracy. To create a practical federated sparse training method that addresses the issues of data heterogeneity, adaptability, and hyperparameter tuning, SparsyFed produces highly sparse models with negligible accuracy degradation, requires only one hyperparameter, achieves significant weight regrowth reduction, and maintains model plasticity under sparse design.

### Strengths
1. Only needs one hyperparameter (sparsity target), making it very practical for FL settings where tuning is challenging
2. Maintains accuracy up to 95% sparsity, significantly outperforming baselines
3. Good ablation studies on weight reparameterization and activation pruning

### Weaknesses
1. The explanation would be clearer if a figure illustrating the pipeline of the proposed method were provided.
2. This reviewer believes that focusing on fewer hyperparameter tuning efforts should not be considered the main contribution (or even the primary motivation), especially since addressing this challenge isn't the primary focus of the work. Furthermore, while the proposed method introduces only one hyperparameter, existing hyperparameter-related issues in FedOpt still persist.
3. The reviewer finds it confusing that Line 10 in Algorithm 2 appears redundant given the presence of Line 9.
4. Is sparse communication essential for the proposed method to address the three challenges it focuses on?
5. The paper lacks sufficient discussion on why the proposed method facilitates more effective consensus on the sparse pattern.
6. There is an absence of theoretical analysis or guarantees regarding the convergence properties of the method.

### Questions
see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work presents SparsyFed, an adaptive sparse training method tailored for cross-device federated learning. Authors show that SparsyFed can achieve impressive sparsity levels while minimizing the accuracy drop due to the compression. SparsyFed outperforms in accuracy three federated sparse training baselines, TopK, ZeroFL, and FLASH, using adaptive and fixed sparsity for three typical datasets used in cross-device FL.

### Strengths
1.The authors summarize three challenges when process sparse training in cross-device federated learning environments.

2.The authors propose the SparsyFed method to accelerate on-device training in cross-device FL.

3.Extensive experiments show the effectiveness of SparsyFed, which can target high sparsity levels (up to 95%) without compromising the model’s accuracy with a novel approach leveraging hyperparameter-less local activation pruning and thoughtful weight reparameterization.

### Weaknesses
1. It’s suggested that authors give a comprehensive survey on adaptive sparse training method. Although authors claim “Previous works have only managed to solve one, or perhaps two of these challenges”, can authors give a comprehensive comparison of existing methods? 

2. Considering different clients train different submodels, the server also maintains a full model. So can the sparsity of clients be different to apply for heterogeneous hardware?

3. Can authors further explain why clients should achieves consensus on the clients’ sparse model masks when server always maintain a full model.

4. What’s the definition of the model plasticity?

5. In experimental section, authors only compared with two baselines, there’re several works also focus on the same questions, for example [1,2,3], so it’s suggested to add more experimental to show the effectiveness of proposed method.

6. Considering the model architecture, authors only show the effectiveness on convolutional network, what’s the performance on other architecture, for example Transformer?

### Questions
See weaknesses.

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
This paper proposes a sparse FL method to tackle the following problems in FL: 1) data heterogeneity and its impacts on sparsity across clients; 2) adapt to never-seen data distributions; 3) hyperparameter turning in FL. The authors present *SparsyFed* and claim that it can produce very sparse models, while offering *plasticity* to data distributions.

### Strengths
The authors conduct comprehensive empirical evaluations of the proposed methods. In particular, the proposed method is tested on multiple datasets with different data distributions. Besides model accuracy, the authors also analyze reductions in communication costs when using the sparse training method. 

In addition, the authors also conduct necessary ablation studies to investigate 1) sparsity pattern dynamics during training; 2) different weight re-parametrization methods; 3) activation pruning.

### Weaknesses
 **1 Claims are not fully supported**: The authors claim that *SparsyFed* addresses all three problems mentioned in the abstract: data heterogeneity and its impact on clients' sparsity, a lack of sufficient plasticity to never-seen data distributions, and hyperparameter tuning. However, it is unclear that what techniques in *SparsyFed* address these problems. In particular, it is not convincing that consensus in sparsity is achieved by simply adopting a weight re-parameterization scheme. I believe more analyses are needed to support the claim.  

In addition, I am also confused about how *SparsyFed* can `adapt to never-seen data distributions`, as there is no technique used in the method that can specifically address this problem.

**2 Presentations in the introduction section**: I did not see any part in the introduction explaining technical details in *SparsyFed*. The authors mainly focus on describing the benefits of *SparsyFed*. However, it is confusing what techniques in *SparsyFed* bring these benefits.

**3 Contributions are not fully explained in Sec 3**: 

First, I am confused about lines 6-10 in Algo 2. Some functions like *GetLayer* and *SetLayer* are not explained. As these lines are the main contribution to the paper, it is hard to understand why *SparsyFed* achieves good performance without knowing its technical details. 

Furthermore, the authors did not explain why sparse activations help attain a sparse model. As it is not a theoretical work, more intuitive explanations and evaluations are needed to justify such operations.

### Questions
See the comments above.

### Soundness
2

### Presentation
2

### Contribution
2
