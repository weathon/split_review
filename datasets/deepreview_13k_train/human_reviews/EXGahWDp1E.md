# Optimization Proxies using Limited Labeled Data and Training Time - A Semi-Supervised Bayesian Neural Network Approach

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Constrained optimization problems arise in various engineering system operations such as inventory management and electric power grids. However, the requirement to repeatedly solve such optimization problems with uncertain parameters poses a significant computational challenge. This work introduces a learning scheme using Bayesian Neural Networks (BNNs) to solve constrained optimization problems under limited labeled data and restricted model training times. We propose a semi-supervised BNN for this practical but complex regime, wherein training commences in a sandwiched fashion, alternating between a supervised  learning step (using labeled data) for minimizing cost, and an unsupervised learning step (using unlabeled data) for enforcing constraint feasibility. Both supervised and unsupervised steps use a Bayesian approach, where Stochastic Variational Inference is employed for approximate Bayesian inference. We show that the proposed semi-supervised learning method outperforms conventional BNN and deep neural network (DNN) architectures on important non-convex constrained optimization problems from energy network operations, achieving up to a tenfold reduction in expected maximum equality gap and halving the optimality and inequality (feasibility) gaps, without requiring any correction or projection step. By leveraging the BNN's ability to provide posterior samples at minimal computational cost, we demonstrate that a Selection via Posterior (SvP) scheme can further reduce equality gaps by more than 10\%. We also provide tight and practically meaningful probabilistic confidence bounds that can be constructed using a low number of labeled testing data and readily adapted to other applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes Bayesian Neural Networks (BNNs) for solving the OPF problem under uncertain demand. It employs a novel semi supervised training procedure that reduces the dependence of the training to labelled input-output pairs. The study also suggests using Bernstein bound with Mean Predictive Variance to assess the BNN model performance on out-of-sample inputs.

The authors consider two BNN training methods: a supervised approach using labelled data and a semi-supervised approach, or sandwich learning, which alternates between supervised and unsupervised loss functions iteratively. The latter enforces feasibility by utilizing a function that takes the value 0 if the constraints are satisfied. 

The model was applied to 57-, 118-, 500- and 2000-bus test cases and compared against 5 alternative methods in the literature.

### Strengths
1.	The main advantage is that the BNN seem to have some performance advantages over DNNs for small and large systems even with training datasets as small as 512 observations. While the optimality gaps are close among all methods, there are notable power balance gap differences between BNN and DNN methods.
2.	In case of large systems such as 2000-bus system, with 512 observations, while DNN training fails, all BNN models still able to perform well. This is particularly useful when it is computationally expensive to generate datasets.
3.	Another contribution is using unsupervised loss term in the training loop, which can work like regularization term, focusing the attention of training to model parameters that would generate more realistic (feasible) solutions. The sandwich training that alternates between supervised and unsupervised data is akin to Physics Informed Neural Network training proposed by [1]. While PINN training contains all KKT conditions in one loss function, the proposed Sandwich learning alternates between two loss functions.

[1] Nellikkath, Rahul, and Spyros Chatzivasileiadis. "Physics-informed neural networks for minimising worst-case violations in dc optimal power flow." 2021 IEEE International Conference on Communications, Control, and Computing Technologies for Smart Grids (SmartGridComm). IEEE, 2021.

### Weaknesses
1.	The optimality gaps among different methods are very close for 118- and 500-bus cases. The only exception is 57-bus system where sandwich learning shows some improvement. It looks the only consistent advantage is less power balance violations.
2.	It is not clear if sandwich learning improves BNN model performance. The differences among proposed BNN approaches seem marginal and is not consistent among all test cases. Furthermore, the paper does not provide a clear ablation study to isolate the effect of the unsupervised loss term. It is difficult to determine if the observed performance differences are due to the sandwich learning approach itself or other factors such as the specific initialization or hyperparameter tuning of the BNN models.
3.	If I understand correctly, the DNNs in the study are also trained with 512 data points and the training was terminated after 600 seconds (please correct me at this point if I missed the relevant part of the script). My main concern is that training DNNs (with two hidden layers and n_hidden = 2 x input size) with 512 observations is not fair. DNNs are universal function approximators with number of linear facets are determined by hidden layer depth and width [2] and the training must be carried out with dense enough datasets for a good estimation especially in case of larger systems. I understand this is one of the advantages of using BNNs but larger training datasets can still be feasible to construct. The paper does not explore the sensitivity of DNN performance to training data size, which would be important for a fair comparison.
4.	It is not surprising that in case of 2000-bus system, the training would fail with a small dataset and short training time because the NN model (with hidden layer width of 2 x input size) has too many trainable parameters. The authors could find the required training size for DNNs to perform as well as BNNs as a proof of scalability of the latter. The paper should provide a more detailed analysis of the failure modes of DNNs under these conditions, such as examining the loss landscape or the convergence behavior during training.

### Questions
1.	How many data points were used to train the DNN models?
2.	I wonder if the authors tried to use Sandwich learning to train DNNs. As it reduces the dependence on labelled datasets, it can be a good improvement to scale up to larger systems with limited observations. 
3.	Some papers in the literature call a shallow NN a model with two hidden layers i.e. input -> hidden and hidden -> output. Others refer shallow NNs as one layered models. If it is the case of the former, to name it as DNN it must have more than two layers. I wonder which is the case in this study. If a shallow NN was trained, then it deeper models can have better advantages.

### Soundness
2

### Presentation
3

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
This paper proposes a Bayesian neural network-based semi-supervised learning framework for tackling constrained optimization problems. The authors target engineering problems where labelled data and computational resources are limited. The proposed approach alternates between a supervised learning step which minimizes the cost of the optimization problem and an unsupervised learning step which enforces the related constraints. The authors claim that their approach outperforms conventional methods while significantly reducing equality and feasibility gaps.

### Strengths
- The paper is relatively well-organised and easy to understand;
- The paper offers a fairly well-executed application/combination of Bayesian semi-supervised learning techniques to a realistic real-world problem in constrained optimization;
- The Sandwich BNN framework idea is fairly interesting and seems to have direct applicability to general time-sensitive and resource-limited engineering optimization problems

### Weaknesses
 - As far as I can tell, the work is primarily applied and there is limited technical novelty, which could reduce the community's interest in this paper;
- The paper emphasizes the benefits of Bayesian neural networks for uncertainty estimation but offers no uncertainty calibration analysis or comparisons with other viable uncertainty estimation methods. It is important to note that Bayesian neural networks tend to underestimate variance (partly) due to the mean-field assumption;
- The assumption that the problem has a feasible solution strikes me as quite strong in the general case, for example in complex highly non-convex settings. I would be interested in hearing the author's thoughts on this;
- There is very limited discussion about the drawbacks and/or limitations of the approach.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a semi-supervised learning framework based on BNN to solve constrained optimization problems when labeled data is limited and model training times are restricted. 
The authors propose a sandwich-style training approach alternating between supervised and unsupervised learning. Additionally, they employ BNNs to generate multiple predictions and improve feasibility through a selection process. Experimental results demonstrate that BNNs outperform DNNs in settings with low data and limited computational resources.

### Strengths
1. The work considers a practical and important scenario of solving constrained optimization problems when labeled data is limited and model training times are restricted.
2. The authors derive tight confidence bounds for the testing error by utilizing Bernstein's inequality.
3. The experiments conducted on the case 2000 demonstrate the scalability of the proposed approach.

### Weaknesses
1. While the main challenges addressed in this work are limited labeled data and restricted model training times, it is unclear how BNNs specifically contribute to addressing these challenges. The sandwich-style semi-supervised training approach proposed by the authors can be applied to any NN structure.
    - Training BNNs is computationally more expensive than regular NNs. The authors should discuss it and present the complexity explicitly.
    - In section 3.1., the authors propose a selection via posterior strategy to reduce the constraint violation. It is unclear what the benefits of BNN are in this strategy since one can add Gaussian noise to regular DNN prediction and select the one with minimum constraint violation. Theoretically, how does the equality constraint violation decrease with the increased generated samples?
    - In Section 4, the authors derive confidence bound for the testing error using the MPV as a proxy for the TVE in the Bernstein bound. They hypothesize an inequality (line 286) without providing sufficient justification. The authors should explicitly state and discuss the assumptions made in deriving this confidence bound.
    - The authors should discuss and compare their confidence bound with existing generalization analyses or confidence bounds for DNNs based on the number of training samples, such as those presented in [1].

2. The authors propose an alternated training approach where supervised and unsupervised learning are performed in separate iterations. However, the benefits of this approach are unclear. Since one can easily combine the supervised and unsupervised loss together at each iteration, it may save more training time.

3. Overall, this work combines sandwich training, BNN, and SvP, so a comprehensive ablation study is needed to evaluate the individual contributions and importance of each component.

4. In experiments, the authors only include supervised training methods as baselines, excluding self-supervised and primal-dual learning approaches due to their higher training times and computational demands.
    - The sandwich training approach can also be applied to regular NNs, serving as a meaningful baseline.
    - There are efficient unsupervised approaches for solving AC-OPF problems that the authors did not discuss in the related work section or compare against in their experiments [2].

### Questions
1. How does the number of labeled or unlabeled training data affect the BNN performance?
2. How does the number of posterior samples affect the constraint violation?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduces a semi-supervised Bayesian Neural Network (BNN) framework to efficiently solve constrained optimization problems common in engineering applications like energy networks, where uncertain parameters and limited labeled data pose computational challenges. By alternating between supervised cost-minimization with labeled data and unsupervised constraint satisfaction with unlabeled data, the model achieves a tenfold reduction in equality gaps and halves feasibility and optimality gaps compared to standard BNNs and deep neural networks. Additionally, a novel Selection via Posterior (SvP) scheme leverages BNN uncertainty estimates to further minimize errors, while the framework’s probabilistic confidence bounds offer a scalable solution adaptable to various high-stakes optimization problems with minimal labeled data requirements.

### Strengths
The strengths of this paper lie in its development of a semi-supervised Bayesian Neural Network (BNN) approach that addresses constrained optimization challenges under strict time and data constraints. First, the choice of BNNs over DNNs enhances uncertainty quantification, facilitating more reliable predictions by integrating prior beliefs, and is novel. The introduction of a novel Sandwich learning method further strengthens the model by enforcing feasibility through unlabeled data, bypassing the need for additional labeled instances. Moreover, the use of predictive variance within the BNN framework enables the formulation of tight expected error bounds.

### Weaknesses
- The authors should correct the citation formatting throughout the paper, particularly the use of \citet and \citep. For example, the citation of Ibrahim et al. (2020) should be formatted as (Ibrahim et al. 2020) rather than including it in the narrative.
- The overall presentation of the study is weak and requires enhancement for improved clarity and impact.
- A comparison against methods that require more training time is necessary. Since the neural networks proposed by Park & Van Hentenryck (2023) and others do not necessitate extensive training time, it is crucial to understand the implications of low computational requirements. Although low compute restrictions during test time are typically essential for inference on new examples, we need to train fewer models and thus it may render such restrictions (e.g., a hard limit of 10 minutes of training time on a single CPU core) unnecessary.
- What is the justification for including equation 1d as part of the constraints?
- The assertion that constructing the feasibility dataset Df​ incurs no additional computational cost should be revisited. While input sampling may indeed be inexpensive, obtaining feasible solutions can be resource-intensive, necessitating a more accurate representation.
- The authors should clarify why they did not compare their approach with the primal-dual self-supervised learning method proposed by Park & Van Hentenryck (2023). Additionally, the methods of DC3, and Zamzam & Baker (2020) should be included in the comparison. A new table could have been created to compare the training times of these methods, as it is possible to obtain outputs from these models without fitting them completely.
- Completely omitting state-of-the-art baselines does not appear to be a prudent choice. The authors should include the results of these methods while indicating that they require more time and thus cannot be used for direct comparison.
- Additionally, the authors have not accounted for the supervised dataset creation time within the 10-minute limit. Since self-supervised methods do not necessitate this step, the current comparison may be considered unfair. The authors should revise the training time to reflect a total of 10 minutes for training plus T minutes for generating true labels for the supervised dataset. This revised training time should then be applied uniformly to both the supervised and self-supervised methods, even when the latter do not require true labels.
- Is the statement, “Moreover, unsupervised methods still require testing data and consequently the associated data generation time in order to perform validation and provide confidence bounds on error with respect to true solution,” not applicable to the proposed method? Although the proposed method does not require data generation for confidence bounds, it does require labeled training data, which is not needed for self-supervised methods. Additionally, to compute the gap and constraint violations, wouldn’t the proposed method also need true labels?
- The manuscript contains several grammatical mistakes that should be addressed, including but not limited to:
    - "The fundamental idea of this training method is to update the network weights and biases through multiple rounds of training in which each round alternates between using the labeled dataset."
    - "Next, we present results for Probabilistic Confidence bounds, described in Section 4. Figure 3 shows that..."
    - "In Bayesian Neural Network (BNN) literature, the standard approach is to use the mean posterior prediction Ep​(w∣D)\[fw​(xt​)] for a test input xt​." Please clarify the context for "a standard approach."

### Questions
Please refer to the section on weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2
