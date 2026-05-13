# Adaptive Source Localization on Complex Networks via Conditional Diffusion Model

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Network propagation issues like the spread of misinformation, cyber threats, or infrastructure breakdowns are prevalent and have significant societal impacts. Identifying the source of such propagation by analyzing snapshots of affected networks is crucial for managing crises like disease outbreaks and enhancing network security. Traditional methods rely on metrics derived from network topology and are limited to specific propagation models, while deep learning models face the challenge of data scarcity. We propose \textbf{ASLDiff}~(\textbf{A}daptive \textbf{S}ource \textbf{L}ocalization \textbf{Diff}sion Model), a novel adaptive source localization diffusion model to achieve accurate and robust source localization across different network topologies and propagation modes by fusing the principles of information propagation and restructuring the label propagation process within the conditioning module. Our approach not only adapts to real-world patterns easily without abundant fine-tuning data but can also generalize to different network topologies easily. Evaluations of various datasets demonstrate ASLDiff's superior effectiveness, accuracy, and adaptability in real-world applications, showcasing its robust performance across different localization scenarios. The code can be found at https://anonymous.4open.science/r/ASLDiff-4FE0.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces ASLDiff, a new method for finding information sources in complex networks. ASLDiff combines diffusion models with information propagation principles to accurately locate sources across different network types and patterns. It uses pre-estimated source locations as guides, a diffusion process led by these estimates, and a GCN (Graph Convolutional Network) to capture key propagation details. ASLDiff outperforms certain existing methods, achieving up to 7.5%-12.1% higher accuracy on some real-world datasets and adapting effectively to some networks and scenarios.

### Strengths
1. The paper combines diffusion models with principles of information propagation, offering a unique solution to the source localization problem.

2. ASLDiff leverages pre-calculated source estimations as informative priors, potentially improving efficiency and effectiveness.

3. The authors test their model on both synthetic and real-world datasets, comparing it against several state-of-the-art methods.

4. The proposed model shows promise for some real-world scenarios, such as epidemiology, and cybersecurity.

### Weaknesses
1. While the authors use some real-world datasets, more extensive testing on diverse real-world datasets could further validate the model's effectiveness.

2. The paper doesn't discuss the computational complexity or resource requirements of ASLDiff compared to other methods.

3. The paper does not sufficiently address the scalability of the proposed method for large networks (millions of nodes), which is essential for real-world applications. The largest tested graph contains fewer than 15K nodes.

4. ASLDiff’s performance under the SIS diffusion pattern is inconsistent. Only three datasets are used, with performance varying across datasets and metrics. For instance, there is no improvement in AC on the Net and Jazz networks, and only a marginal increase from 0.984 (GCNSI) to 0.985 on the Power network.

### Questions
1. How does the computational complexity of ASLDiff compare to other state-of-the-art methods, especially for large-scale networks?

2. Can the authors provide more insights into the model's performance on large real-world networks (e.g., millions of nodes)?

3.  Why the performance of ASLDiff under the SIS diffusion pattern is inconsistent?

4. Can the proposed model handle dynamic networks where the topology changes over time?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In the social network background, the author employs the diffusion model to implement source detection tasks across different localization scenarios. The proposed ASLDiff can be trained in a few-shot manner.

### Strengths
ASLDiff can train based on the few-shot learning.

The appendix contains a sufficient review of related work, indicating the adequate preparations for the proposed ASLDiff.

ASLDiff using a single snapshot is superior to multiple-snapshot-based works. I think it is awesome!

### Weaknesses
One of the contributions of this paper is the development of few-shot learning due to the limited data available in real-world scenarios. This should be a key focus for the author; however, it seems that the main body of the paper provides a very limited description of few-shot learning. Moreover, despite the thorough survey and preparations of the work, there are many details that need attention. For example, 'Diffusion' instead of 'Diffsion';  Equation (1),  Equation (7) instead of Equation 1,  equation 7. Also, providing code is intended to enhance confidence for your work, but the code is not runnable.

The authors’ research scope is so wide that it may be incredible. They claim that they can solve problems in various fields, such as disease outbreaks, network security, etc. This is a great plan, however, maybe it is an exaggeration. The spread of infectious diseases and the spread of misinformation vary greatly. Maybe it is too ideal to solve these problems with only one model? This is my main concern for this paper, as complex networks are a very vast and intricate field.

### Questions
The authors’ research scope is so wide that it may be incredible. They claim that they can solve problems in various fields, such as disease outbreaks, network security, etc. This is a great plan, however, maybe it is an exaggeration. The spread of infectious diseases and the spread of misinformation vary greatly. Maybe it is too ideal to solve these problems with only one model? This is my main concern for this paper, as complex networks are a very vast and intricate field.

The author's review is complete, but there are relatively few comparative methods published in the year 2024. Compared with the newest algorithms in the year 2024, can ASLDiff still maintain its advantage?

After setting up the required environment for the author's code, I encountered an error stating "models.guide: No such file or directory." I can't verify the results of the model, even though it is impressive.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes an Adaptive Source Localization Diffusion Model to face the challenge of data scarcity without specific propagation models. And evaluations of various propagation patterns and real network datasets demonstrate ASLDiff’s effectiveness.

### Strengths
1. This paper provides comprehensive experimental validation of ASLDiff.
2. The code of ASLDiff is given.
3. ASLDiff shows significant improvement on some datasets.

### Weaknesses
1. As the authors mention, the diffusion model is highly complex. However, the extent of this complexity is not quantified, specifically in terms of computational cost (training time, inference time, memory usage) compared to existing methods. Additionally, considering the high complexity, the motivation for using the diffusion model should be fully explained, detailing why its specific properties are necessary for this task, rather than a simpler generative model or a graph-based approach.
2. The authors discuss the challenge that "real-world networks typically exhibit unknown propagation patterns", but they do not explain or demonstrate how ASLDiff understands different propagation patterns in different scenarios. It's unclear how the model adapts to variations in propagation dynamics, such as different infection rates or recovery probabilities, and whether it can generalize to unseen patterns beyond those used in training.
3. Sections 2.1 and 3.2 are confusing, as they both seem to explain the IC and LT models redundantly. This repetition makes the paper less clear and harder to follow.
4. The authors have demonstrated that the closeness centrality of infected nodes and sources is very consistent, but it appears that the advisor used in ASLDiff is not based on closeness centrality. The choice of advisor and its connection to the observed centrality properties should be clarified.

### Questions
see Weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies the source localization problem: given a graph with infection states of all nodes, aim to find the original propagation source. The paper proposes ASLDiff which utilizes diffusion model for source localization in complex networks and applies GNNs to enhance the model’s adaptability to diverse network topologies. Besides, it incorporates soft labels and a restructured label propagation process to capture essential propagation characteristics across various network topologies. However, the technique novelty is limited and methods are capped which subject to labelling dissemination methods.

### Strengths
S1. The problem of source localization is important.

S2. The problem statement and the rationale behind the method are clear.

S3. The paper is a reasonable attempt to apply diffusion modelling to traditional propagation problems.

S4. The evaluation is very comprehensive. The authors show strong quantitative results. Tables 1-2, with figs 3-6 give strong qualitative results and ablation.

### Weaknesses
W1. The forward process (e.g. the diffusion process) should be detailed. What is the state of the initial $X$ and what is the $X$ after noise added? Besides, it seems that you used the conditional diffusion method, but your condition is an approximate solution obtained from LPSI. This usually does not conform to our intuition, and I hope you can elaborate on the rationality of using the approximate solution of LPSI as a condition. And will using approximate solutions as conditions greatly limit the performance of your proposed model? If this impact does not occur, you should provide some theoretical proof. This is evident in the accuracy results, where ASLDiff underperforms compared to LPSI on some metrics.

W2. The description of the method in the paper is unclear, and the innovative aspects of the technical details are not sufficiently articulated. For example, the part of the LPSI advisor that employs the conditional diffusion model lacks an explanation of how the diffusion model introduces innovation for the specific task.

W3. The framework diagrams in the paper are not sufficiently clear. For instance, in Figure 1, the function $f(\theta)$, which corresponds to the denoising network, is not intuitive. It is suggested to use clearer module diagrams to explain this. Additionally, the input-output relationships in Figure 2 are unclear. For example, the concept of $Y_{label}$ is not explicitly defined in the text, even though the generation method is explained. Further clarification is recommended.

### Questions
If LPSI is used to generate enough training samples to train the DL-based method, is it possible to achieve an approximation with adaptability, and what are the advantages of using a diffusion model in comparison?

### Soundness
3

### Presentation
3

### Contribution
2
