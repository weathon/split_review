# FedMAP: Unlocking Potential in Personalized Federated Learning through Bi-Level MAP Optimization

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6

## Abstract
Federated Learning (FL) enables collaborative training of machine learning models on decentralized data while preserving data privacy. However, data across clients often differs significantly due to class imbalance, feature distribution skew, sample size imbalance, and other phenomena.
Leveraging information from these not identically distributed (non-IID) datasets poses substantial challenges. FL methods based on a single global model cannot effectively capture the variations in client data and underperform in non-IID settings. Consequently, Personalized FL (PFL) approaches that adapt to each client's data distribution but leverage other clients' data are essential but currently underexplored. We propose a novel Bayesian PFL framework using bi-level optimization to tackle the data heterogeneity challenges. Our proposed framework utilizes the global model as a prior distribution within a Maximum A Posteriori (MAP) estimation of personalized client models. This approach facilitates PFL by integrating shared knowledge from the prior, thereby enhancing local model performance, generalization ability, and communication efficiency. 
We extensively evaluated our bi-level optimization approach on real-world and synthetic datasets, demonstrating significant improvements in model accuracy compared to existing methods while reducing communication overhead. This study contributes to PFL by establishing a solid theoretical foundation for the proposed method and offering a robust, ready-to-use framework that effectively addresses the challenges posed by non-IID data in FL.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new personalized federated learning algorithm based on maximum a posteriori (MAP). Each client constructs the personalized model given global model as prior.

### Strengths
The paper proposes a novel federated learning algorithm. In appendix the paper analyses the convergence of the algorithm. The performance of the proposed algorithm is compared against some well-known federated learning algorithms on common datasets.

### Weaknesses
 - The paper should provide more concrete and technical explanation about their novelty compared to existing works. Reading the related works section, I believe the discussion is incomplete and the advantages of FedMAP compared to other methods are not clear. I suggest to provide such discussion after introducing the proposed algorithm.
- Although the paper provides some theoretical analyses, these analyses are in appendix and not in the main text of the paper. This makes these analyses disconnected from the paper for readers. It is not clear how important the theoretical contributions of this paper is. I suggest makes these conclusions from the theoretical analysis more clear. This can better show the contribution of the paper relative to other works.
- I felt that the literature review of the paper is not very up-to-date. This can be improved by including more 2024 papers in the related works section.
- The experiments can benefit from adding more baselines although I think it may not be necessary.

### Questions
Can you please give more explanation about the challenges and problems that is solved by FedMAP which cannot be solved by other personalized federated learning algorithms?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents FedMAP, a framework designed for Personalized Federated Learning (PFL) to handle the challenges of non-IID (non-identically distributed) data across clients. FedMAP integrates Maximum A Posteriori (MAP) estimation into the federated learning process, allowing each client to personalize its model by updating a shared global prior with its local data through a bi-level optimization procedure.

The approach aims to improve on standard federated learning methods, which often struggle with heterogeneous data, by balancing global knowledge sharing with local adaptation. The paper provides a theoretical analysis of the convergence properties of FedMAP and evaluates its performance through experiments on non-IID datasets, comparing it to existing federated learning methods, such as FedAvg, FedProx, and FedBN.

### Strengths
- The writing is clear and the presentation is well-structured, making it easy for readers to follow and understand the proposed approach and its contributions.
- Bi-Level Optimization Framework: The paper provides a theoretical analysis based on bi-level optimization, offering insights into how the proposed FedMAP converges under heterogeneous data conditions.
- Although not ground-breaking, the convergence analysis (in Appendix A) is nice. I think it is better to place somewhere in the main text rather than in the appendix.
- FedMAP can be applied in various federated learning scenarios with minimal changes to the standard federated learning process, making it adaptable for different use cases.
- The experimental results show that FedMAP outperforms traditional federated learning methods in a range of non-IID scenarios, demonstrating improved performance in tasks involving skewed or imbalanced data distributions.

### Weaknesses
 - The proposed method assumes an isotropic Gaussian prior for the global model, and the paper does not explore how the choice of prior might affect the model's performance or consider alternatives that could be more suited for specific tasks. Can the results be relaxed to the setting where the prior is still Gaussian  with diagonal variance-covariance, but non-isotropic Gaussian?
- The paper does not explicitly mention whether FedMAP reduces communication costs compared to existing methods. Instead, the focus is on improving model performance in non-IID settings through bi-level optimization and personalization. While these methods might introduce computational overhead, the communication efficiency aspect is not fully addressed. Can you elaborate on this?

### Questions
See the questions in the weakness section.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose FedMAP, a Bayesian PFL framework which applies Maximum A Posteriori (MAP) estimation to effectively mitigate various non-IID data issues, by means of a parametric prior distribution, which is updated during aggregation. In this FL approach, the authors formulate the local training problem as a MAP estimation of the local models, in which the global model acts as a prior distribution on the hypothesis set of probabilistic models.

### Strengths
- The framework applies Maximum A Posteriori (MAP) estimation to tackle non-IID problems in the personalized FL framework.

- The problem formulation is clearly described.

### Weaknesses
 - The idea of personalized FL as bi-level optimization with Moreau envelops was proposed first in the pFedMe paper (https://proceedings.neurips.cc/paper/2020/hash/f4f1f13c8289ac1b1ee0ff176b56fc60-Abstract.html).  Basically, this work decorated pFedMe with MAP, especially the Local Optimization at eq. (7). Therefore, the contribution of this work is very limited. But ironically, this paper did not cite pFedMe for some reason. 

 - The theoretical results did not show why the global aggregation (line 5, Algorithm 3) can converge to the unique optimal solution of the bilevel optimization problem with Moreau envelop.  The convergence proof relies on the assumption that the aggregation step results in a global model that is closer to the true optimum, but this is not explicitly demonstrated. The analysis should include a more rigorous treatment of how the specific form of the aggregation impacts convergence, especially in the context of non-convex loss functions often encountered in deep learning.

 - In the experiments, the work compared the framework only with a very old framework like FedAvg and two other methods like Fedbn and FedProx. However, the work did not compare the result with similar approaches (pFedMe, Ditto, FedDyn). This makes it difficult to assess the true performance gains of the proposed method relative to state-of-the-art personalized FL techniques. The choice of baselines is not sufficient to demonstrate the advantages of the proposed method.

 - The datasets used for experiments are relatively small (only 4110 images). Similar FL experiment setups used much larger datasets (pFedMe, Ditto, FedDyn), eventually regarding non-IID problems. We suggest that the authors test with popular and large FL datasets, like GLUE and FEMNIST. The limited scale of the experiments raises concerns about the generalizability of the results, particularly in more complex and realistic scenarios with larger datasets and more pronounced non-IID characteristics.

### Questions
- Can you provide a detailed comparison between FedMAP and pFedMe by highlighting any key differences or improvements? Why was pFedMe not cited, and how does this work build upon or differ from this prior research?

- The paper uses only small datasets to test the benchmark of the proposed approach. How is the non-IID problem improved with a relatively small dataset?

- Why did you not compare the benchmark with pFedMe/Ditto/FedDyn while using the same technique at local rounds?

- Do you have any theoretical results to show that the global aggregation (line 5, Algorithm 3) can help the algorithm converge to the unique optimal solution of the bilevel optimization problem with the Moreau envelop?

- If not, can you provide additional theoretical analysis specifically addressing the convergence properties of the global aggregation step?

- Can you discuss the scalability of FedMAP to larger datasets? For example, can you conduct experiments on GLUE and FEMNIST or provide a detailed justification for why the current datasets are sufficient to demonstrate the effectiveness of FedMAP, particularly in non-IID settings?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work introduces FedMAP, a Bayesian Personalized Federated Learning (PFL) framework that addresses data heterogeneity in federated learning (FL) by using Maximum A Posteriori (MAP) estimation. FedMAP applies a parametric prior distribution updated during aggregation, allowing it to handle non-IID data across clients.

### Strengths
The paper takes an alternative approach to addressing the non-iid data in federated learning though a Bayesian approach, which might be of the interest to the community.

### Weaknesses
The paper in its current form suffers from the following weaknesses:

1) The flow of the technical contents is extremely hard to follow. To provide some context, I actively publish in the federated learning domain and I could still not follow the contents. To be more precise, it will only take 10-11 lines after the beginning of Section 2 until the reader gets lost. This is because an alternative representation of federated learning process is studied, which is unconventional to the people in this area, without building the background for the reader. To address this, I suggest that authors provide more background on their alternative representation of federated learning early in Section 2, and include a high-level overview of their approach before diving into technical details.

2) The theoretical results of the paper are quite obscure. In particular, they are all provided in the appendix. Even the statement of the main theorems are not mentioned in the main text, which makes following the text even harder. To address this, I suggest that the authors bring some of the theoretical results (at least the main ones) to the main text and add explanations about them.

3) The simulation results are not well justified. After reading the sections I was left with several major questions:

3-1) Why standard federated learning datasets (MNIST, Fashion MNIST, Federated MNIST, SVHN, CIFAR-10, CIFAR-100) are not considered? Please add justifications about this.

3-2) Why standard personalized federated learning frameworks (mentioned in line 94-105) are not considered for performance comparison and only the most naive methods of FL (that by the way are not personalized FL), i.e., FedAVG and FedProx, are considered in conjunction with FedBN? In particular, the pressing need for having meta-learning based approaches as baselines is not addressed. Please add justifications about this issue to the paper.

### Questions
Please refer to my comments above about the weaknesses of the paper.

### Soundness
2

### Presentation
2

### Contribution
3
