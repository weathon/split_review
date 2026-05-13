# Federated Class-Incremental Learning: A Hybrid Approach Using Latent Exemplars and Data-Free Techniques to Address Local and Global Forgetting

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Federated Class-Incremental Learning (FCIL) refers to a scenario where a dynamically changing number of clients collaboratively learn an ever-increasing number of incoming tasks. FCIL is known to suffer from local forgetting due to class imbalance at each client and global forgetting due to class imbalance across clients. We develop a mathematical framework for FCIL that formulates local and global forgetting. Then, we propose an approach called Hybrid Rehearsal (HR), which utilizes latent exemplars and data-free techniques to address local and global forgetting, respectively. HR employs a customized autoencoder designed for both data classification and the generation of synthetic data. To determine the embeddings of new tasks for all clients in the latent space of the encoder, the server uses the Lennard-Jones Potential formulations. Meanwhile, at the clients, the decoder decodes the stored low-dimensional latent space exemplars back to the high-dimensional input space, used to address local forgetting. To overcome global forgetting, the decoder generates synthetic data. Furthermore, our mathematical framework proves that our proposed approach HR can, in principle, tackle the two local and global forgetting challenges. In practice, extensive experiments demonstrate that while preserving privacy, our proposed approach outperforms the state-of-the-art baselines on multiple FCIL benchmarks with low compute and memory footprints.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper categorizes current work in federated class-incremental learning into exemplar-based and data-free approaches, noting that exemplar-based methods face memory constraints and potential privacy risks, while current data-free methods suffer from efficiency issues. The authors propose an HR mathematical framework to address both local and global forgetting. HR leverages a new autoencoder and Jones Potential formulations to generate synthetic data with minimal memory overhead, aimed at mitigating the forgetting problem.

### Strengths
1.	The authors accurately summarize the limitations of current exemplar-based and data-free approaches.
2.	Experimental results indicate that the proposed method achieves lower computational and memory overhead compared to several optimal baseline methods.

### Weaknesses
1. The motivation of this study appears somewhat outdated, as the results in the literature (e.g., [1]) indicate that method has already effectively addressed the issue of class imbalance within clients. 
2. The authors should clearly outline the specific problem their work addresses. For example, in Figure 1, it is necessary to further clarify the mechanisms causing local forgetting and global forgetting, with separate, detailed explanations for each. Specifically, the current description lacks a clear articulation of how client-specific data distributions contribute to local forgetting and how the aggregation process leads to global forgetting. The interaction between these two phenomena is also not well-defined.
3. The study lacks essential comparative methods. The absence of comparisons with state-of-the-art methods that address similar challenges makes it difficult to assess the true novelty and effectiveness of the proposed approach. The current baseline selection does not adequately cover the spectrum of existing techniques.
4. The study lacks visualized experimental results, such as accuracy on all old tasks after completing each task, and is missing essential forgetting metrics, such as Backward Transfer (BWT). The absence of these visualizations and metrics makes it difficult to fully understand the learning and forgetting dynamics of the proposed method.

### Questions
1.	In Equation (3), what do the subscripts $i$ and $j$ represent? Additionally, in Equation (4), what does $j_l$ signify?
2.	When clients train on the same task, they each have data from different classes. How is the classifier configured in this scenario? Is it set up in a task-incremental mode or a class-incremental mode?
3.	The authors should clearly explain how the proposed method achieves sample replay through Equations (10) and (11).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses Federated Class-Incremental Learning by focusing on two types of forgetting: local forgetting (at the client level) and global forgetting (between clients). The authors propose a hybrid approach, called Hybrid Replay (HR), which combines data-based and data-free methods to mitigate these issues. They introduce a mathematical formulation to formalize the forgetting problem and the presented approach HR. The approach uses autoencoders for synthetic sample generation and latent exemplars. Comparisons against other data-free and data-based approaches demonstrate that HR achieves better performance results.

### Strengths
* The paper addresses an important problem in FCIL by combining data-based and data-free approaches to overcome local and global forgetting.
* The hybrid approach integrates both latent exemplars and synthetic data generation, which are efficiently used to mitigate forgetting and results show that HR works better.
* The mathematical formulation provided to describe these forgetting issues offers theoretical foundation.
* Ablation studies in the paper contribute valuable insights into different aspects of HR and improve the interpretability of the approach.

### Weaknesses
Major Concerns:
* The methodology, particularly the role of the autoencoder in addressing local forgetting, is not fully clear and can be explained better. For instance, while the paper states that the autoencoder helps address local forgetting, the specific details of how this is achieved are somewhat vague. The paper would benefit from a more detailed, step-by-step breakdown of how the autoencoder is employed for both local and global forgetting. Specifically, it is unclear how the latent space is structured and how this structure facilitates the replay of previous classes. The paper should clarify whether the autoencoder is trained jointly with the classifier or separately, and how the gradients are backpropagated during the training process.
* The paper lacks a clear visual representation of the HR approach. Including a diagram of the proposed method could significantly enhance understanding, especially as the provided Figure 1 only illustrates the problem without outlining the proposed solution. I believe such visual representations make papers to understand much better. A detailed diagram should illustrate the flow of data, the interaction between the encoder, decoder, and memory components, and the specific steps involved in both local and global forgetting mitigation.
* The results mention comparisons with a "Hybrid Approach," but there’s little discussion on how HR stands out from other hybrid methods, such as  REMIND+ What makes HR approach unique when compared to other Hybrid Approach ? Clarifying these distinctions would strengthen the contribution of HR to the field. The paper needs to explicitly compare the architectural and algorithmic differences between HR and existing hybrid methods, highlighting the unique aspects of HR that lead to improved performance. This should include a discussion of the specific loss functions, optimization strategies, and replay mechanisms used in HR compared to other methods.
* The conclusion lacks discussion on the limitations of HR and potential directions for future work. Addressing this would provide a perspective on the approach’s implications and its broader applicability. The paper should discuss potential failure cases of HR, such as scenarios with highly complex data distributions or extreme class imbalances. It should also explore potential avenues for future research, such as incorporating attention mechanisms or exploring different types of generative models.
* The method heavily relies on data generation based on latent exemplars and class centroids, which raises concerns since we don't have a direct control of generated data and Variational Autoencoders (VAEs) are known to be suboptimal for high-quality synthetic data generation. Over time, this could degrade the quality of latent features and ultimately impact classification performance. The paper should provide an analysis of the quality of the generated samples and their impact on the classification performance. It should also consider alternative generative models that might produce higher-quality synthetic data.
* The paper frequently references the Lennard-Jones formulation, but it doesn’t provide enough explanation about its purpose or why it’s important for the proposed method. The paper should explain how the Lennard-Jones potential is used to align class centroids and how this alignment contributes to mitigating global forgetting. It should also discuss the parameters of the Lennard-Jones potential and their impact on the performance of the method.

Minor Concerns:
* In Section 4, line 232, the acronym "AHR" is introduced without prior definition.
* The caption for Table 1 could be made more descriptive to make the table more self-explanatory.

### Questions
* The paper mentions that exemplar-based methods are memory-intensive. Could the authors provide an estimate of this memory cost, along with a comparison of memory usage between HR and other exemplar-based methods? An example or comparison with HR could help clarify this point.
* While latent exemplars may save memory, the process of forwarding these exemplars through the decoder for sample generation could incur computational costs. It would be helpful if the authors discuss or quantify these costs when addressing the efficiency of their approach.
* What metric is used for evaluation? Motivation of paper is mainly local and global forgetting but there is not any result or evaluation for forgetting.The table results do not clearly specify whether they represent incremental accuracy or the accuracy of the last task. Besides, higher incremental accuracy does not directly indicate lower forgetting. 
* The authors state that local and global forgetting are caused by class imbalances at both the local and global levels. Do they have any scenarios or relevant results that illustrate this point better?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This proposes a mathematical framework to demonstrate the global/local forgetting of FCIL and propose the Hybrid Replay (HR) to addressed these issues.

### Strengths
1. This paper establishes the revolution of training loss functions within the scope of both training tasks and clients, demonstrating the two challenges of global and local forgetting.
2. A novel replay mechanism with centroids of each category is presented.

### Weaknesses
1. The presentation is not very clear. For example, exemplars in HR and other exemplar-based methods seem different but are used interchangeably in this paper. Also, I cannot get the indication of global/local forgetting in Figure 1.
2. The mathematical formulation of FCIL and the proposed approach are not linked closely. Can you provide more information that how you establish the method based on the framework, especially for the global forgetting? It seems that the HR benefits from the class centroid embeddings and use them to address the global forgetting, is there any further analysis?
3. Experiments are not sufficient. The results are limited to the LDA setting with alpha=1. Extended empirical results under different skewness (e.g., alpha=0.1 or more) should be included.
4. Analysis of memory footprint should be included, e.g., the number of parameters need to be stored and transferred during the communication.
5. Error in literature review. The Prototype reminiscence and augmented asymmetric knowledge aggregation [1] only addresses the CIL and it is placed within the FCIL methods.

### Questions
1. What is the data partition of FCIL? Are the classes in different tasks disjoint? In the traditional CIL, categories in different tasks are disjoint. From the setting of ImageNet-Subset (10/20/100/10, 20/10/100/10) and Tiny-ImageNet (10/5/300/30), if A denotes the number of tasks, B denotes the classes per task and the classes in different tasks are disjoint, the total numbers of classes will be 200 for ImageNet-Subset and 50 for Tiny-ImageNet. However, the total numbers of categories in these two datasets are 100 and 200 respectively. Could you explain more about this?
2。 Why does each client need to train from task 1? From Algorithm 1, the client only needs to update $theta_{h}$, but in the line 3 of Algorithm 2, the algorithm begins h=1.
3. The practical FL systems may have stragglers. It is interesting to know whether the proposed HR algorithm can deal with the issue of stragglers.

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
3

### Summary
The paper presents an approach named Hybrid Rehearsal (HR) for Federated Class-Incremental Learning (FCIL), addressing the challenges of local and global forgetting due to class imbalance. HR employs a customized autoencoder for both classifying data and generating synthetic data, leveraging latent exemplars to tackle local forgetting and synthetic data generation to overcome global forgetting. The paper's contributions include a mathematical framework to formalize forgetting in FCIL, a novel autoencoder design that balances class-specific clustering and data distribution modeling, and extensive experiments demonstrating HR's effectiveness over existing methods with low computational and memory costs.

### Strengths
1.The paper introduces Hybrid Rehearsal (HR), which combines the benefits of data-based (exemplar-based) and data-free approaches. This hybrid approach leverages latent exemplars for local forgetting and data-free techniques for global forgetting, providing a comprehensive solution to the forgetting problems in FCIL.
2. The authors develop a mathematical framework to formalize the challenges of local and global forgetting in FCIL. This framework not only aids in understanding the underlying problems but also provides a theoretical basis for the proposed solutions.
3. The paper provides extensive experimental evaluations across multiple benchmarks and compares the proposed approach with state-of-the-art baselines, demonstrating the effectiveness of HR.
4.The paper is well-organized and most related works are properly cited.

### Weaknesses
1. The paper mentions using a customized autoencoder to leverage features for replay. I'm curious about what would happen if the encoder itself experiences forgetting? Additionally, since the stored features are fixed, but the encoder is continuously updated, how is this distribution inconsistency handled? Specifically, the paper does not detail how the latent space is regularized to prevent drift as the encoder is updated, which could lead to the stored features becoming less representative over time. This is a critical point because the effectiveness of the replay mechanism relies on the quality of the latent representations.
2. The paper mentions that the client receives class centroid embeddings ${p_ij}$ (line 8 of Algorithm 1). These embeddings enable the client to generate synthetic data representing tasks from other clients. However, if the received class centroid embeddings {pij} are for classes that the client has not seen, how can synthetic data be generated, and could this be detrimental to the client's learning? The paper lacks a clear explanation of the synthetic data generation process when the client has not encountered the corresponding classes, and it's unclear how the model avoids generating meaningless or harmful data in this scenario. This could lead to instability or reduced performance.
3. How can the bias problem caused by multiple clients each learning a subset of categories be resolved when uploading the global model for model training and merging? The paper does not adequately address the potential for bias in the global model due to the heterogeneous nature of client data. It is unclear how the proposed approach ensures that the global model is robust to the imbalanced representation of classes across different clients.

### Questions
see the questions in the weakness.

### Soundness
3

### Presentation
3

### Contribution
2
