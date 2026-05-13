# Overcoming Catastrophic Forgetting in Federated Class-Incremental Learning via Federated Global Twin Generator

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Federated Class-Incremental Learning (FCIL) increasingly becomes important in the decentralized setting, where it enables multiple participants to collaboratively train a global model to perform well on a sequence of tasks without sharing their private data. In FCIL, conventional Federated Learning algorithms such as FedAVG often suffer from catastrophic forgetting, resulting in significant performance declines on earlier tasks. Recent works, based on generative models, produce synthetic images to help mitigate this issue across all classes, but these approaches' testing accuracy on previous classes is still much lower than recent classes, i.e., having better plasticity than stability. To overcome these issues, this paper presents Federated Global Twin Generator (FedGTG), an FCIL framework that exploits privacy-preserving generative-model training on the global side without accessing client data. Specifically, the server trains a data generator and a feature generator to create two types of information from all seen classes, and then it sends the synthetic data to the client side. The clients then use feature-direction-controlling losses to make the local models retain knowledge and learn new tasks well. We extensively analyze the robustness of FedGTG on natural images, as well as its ability to converge to flat local minima and achieve better-predicting confidence (calibration). Experimental results on CIFAR-10, CIFAR-100, and tiny-ImageNet demonstrate the improvements in accuracy and forgetting measures of FedGTG compared to previous frameworks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduce FedGTG (Federated Global Twin Generator), a novel FCIL framework that leverages generative models on the server side without accessing client data. FedGTG trains a data generator and a feature generator to produce synthetic representations of all seen classes, which are then shared with clients to help balance knowledge retention (stability) and learning new tasks (plasticity). Through extensive experiments on CIFAR-10, CIFAR-100, and tiny-ImageNet, FedGTG shows significant improvements in both accuracy and resistance to forgetting

### Strengths
1. The paper writing is clear and easy to follow.
2. The proposed FedGTG absorbs the advantage of many other algorithms, leading to a strong framework for FCIL.
3. The experimental results are good. The proposed FedGTG outperforms all baselines on each benchmark and each incremental task. And the ablation study shows that each loss term is crucial and  has a large impact on the final results.

### Weaknesses
1. The proposed lacks enough novelty. All loss functions used in FedGTG are proposed by other papers.
2. The framework contains too many hyperparameters, as each loss term needs one. It seems the framework is hard to be finetuned to the optimal result, as there are too many combinations of choice of hyperparameters. And the paper lacks the experiments and discussion of these hyperparameters.
3. More baselines should be compared. Except for generative-based methods, authors should compare FedGTG with other SOTA FCIL algorithms.

### Questions
Why do you design the model architecture of data and feature generation as you shown in the paper? Are there any key ideas of why using these architectures?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Federated Global Twin Generator (FedGTG), and proposes a framework leveraging generative models on the global side, sending synthetic data to clients for retaining knowledge and learning new tasks effectively. FedGTG shows enhanced accuracy, reduced forgetting, and robustness against domain shifts on CIFAR-10, CIFAR-100, and tiny-ImageNet.

### Strengths
1. The paper is overall well-written in terms of writing.
2. The introduction part clearly especify the problem about generators.
3. The experiments are showing nontrivial improvements over compared techniques.

### Weaknesses
1. Not clear what the biggest contributions are. Is it the two generator structure? If so, the novelty does not seem very high. The paper also introduces a direction-controlling objective, which should also stand out, but not very clearly in the paper (e.g., Figure 1). The interplay between the two generators and the direction-controlling objective is not clearly articulated, making it difficult to assess the true novelty and impact of each component. Specifically, it's unclear how the feature generator's output is used to guide the data generator, and how the direction-controlling objective ensures that the generated features are both diverse and representative of the global feature space.
2. Need to include training time or cost in the comparison. It seems that training two generators are quite costing, and it already needs more parameter during the training. The lack of a detailed analysis of the computational cost makes it difficult to evaluate the practicality of the proposed method. The paper should include a breakdown of the training time per task, the memory footprint of the generators, and the computational resources required for training, especially in comparison to other methods. This is crucial for assessing the feasibility of the approach in real-world scenarios.
3. Is the method an exemplar-free technique? If so, the literature reviewer is not very complete. Quite a few new works on exemplar-free CIL are missing in the continual learning section, such as the analytic continual learning branch [1-3], and prototypes-based CIL. The absence of a thorough discussion of exemplar-free continual learning methods limits the paper's ability to contextualize its contribution within the broader field. The paper should discuss how the proposed method compares to other exemplar-free approaches, particularly those based on analytic learning and prototypes, and highlight the advantages and disadvantages of the proposed method in comparison.

### Questions
see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- This paper focuses on federated continual learning, federated class-incremental learning to be more specific. It proposes a new method of using two generator to generate synthetic data and feature. The synthetic data and feature are sent to the client for local training. In local training, this work proposes multiple losses to improve the training process.

### Strengths
- The propose method of using an additional generator is simple and intuitive, while it is not straightforward to make it work. It is technically sound that the authors propose additional loss functions to stablize the training. 
- The paper is generally well-written and easy to follow.
- Extensive experiments are conducted through 3 datasets with detailed ablation studies. Sufficient exisiting works are compared. The proposed method achieves much strong performance than the compared counterparts.

### Weaknesses
 - Figure 1 is not easy to  understand. It would be useful if the authors could provide more explanations or making it more intuitive.
- The abstract claims that “these approaches’ testing accuracy in previous classes is still much lower than recent classes”, but it seems the paper does not provide experiments showing that the proposed method addresses this issue. The Average Forgetting metric is provided, but this is an indirect measure of the claim in the abstract. Direct evaluation of accuracy on previous classes would be more convincing.
- It seems that only a single backbone is used in the evaluatiion. The evaluation should be performed on multiple backbones to show the generalizability of the proposed method.
- Typo in line 83, should be “methods”.

### Questions
- Does this work focus on cross-silo or cross-device FL? What is the number of clients evaluated?
- What is the meaning of “stability-plasticity” ?

### Soundness
3

### Presentation
3

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
Federated Learning (FL) is a privacy-preserving machine learning approach, but it faces challenges related to resource limitations and data heterogeneity, especially as client data distributions evolve over time. Federated Class-Incremental Learning (FCIL) combines FL and Class-Incremental Learning (CIL), enabling models to continuously learn new knowledge from distributed data sources without forgetting prior knowledge. However, existing methods such as TARGET and MFCL, which use data generation to balance knowledge retention for new and old tasks, still encounter forgetting issues. To address this, this paper proposes the Federated Global Twin Generator (FedGTG) framework, which trains and shares data and feature generators on the server side, using direction-control loss to enhance stability and plasticity on the client side. Experiments demonstrate that FedGTG outperforms existing methods in terms of accuracy and forgetting rate.

### Strengths
1. This paper enhances current GAN methods for Federated Incremental Learning by integrating both a feature GAN and a data GAN, with the feature GAN employing regularization to achieve improved performance and stability across incremental tasks.  
2. Extensive experiments across multiple datasets demonstrate the robustness and validity of the proposed model, showcasing its effectiveness in various scenarios.  
3. Unlike prior GAN-based methods, which often suffer from catastrophic forgetting, this work introduces innovative mechanisms that significantly mitigate such issues, representing a valuable contribution to the field.

### Weaknesses
1. The experiments in the paper lack critical details, including the ratio of generated data used in each training cycle, the proportion within individual batches, and the hyperparameters for each loss function, which should ideally be explored through ablation studies. Additionally, the class-incremental setup is not clearly explained, leaving me unsatisfied with the experimental rigor.

2. The datasets used throughout the paper are relatively simple; I recommend conducting further experiments on high-resolution datasets such as ImageNet to strengthen the evaluation.

3. The contributions of the paper are limited. For instance, incorporating a feature GAN as a regularization term is not substantially different from traditional regularization methods in incremental learning.

4. It is unclear whether the GAN trained after each task is independently trained or incrementally trained based on the previous task. If trained independently, this approach would impose excessive storage and communication costs; if incrementally trained, the GAN itself could suffer from catastrophic forgetting. These aspects present limitations in the proposed method.

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
2
