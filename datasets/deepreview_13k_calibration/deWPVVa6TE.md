# FedL2G: Learning to Guide Local Training in Heterogeneous Federated Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Data and model heterogeneity are two core issues in Heterogeneous Federated Learning (HtFL). In scenarios with heterogeneous model architectures, aggregating model parameters becomes infeasible, leading to the use of prototypes (\ie, class representative feature vectors) for aggregation and guidance. However, they still experience a mismatch between the extra guiding objective and the client's original local objective when aligned with global prototypes.}) method that adaptively learns to guide local training in a federated manner and ensures the extra guidance is beneficial to clients' original tasks. With theoretical guarantees, \ld efficiently implements the learning-to-guide process using only first-order derivatives \wrt model parameters and achieves a non-convex convergence rate of $\mathcal{O}(1/T)$.
    We conduct extensive experiments on two data heterogeneity and six model heterogeneity settings using 14 heterogeneous model architectures (\eg, CNNs and ViTs) to demonstrate \ld's superior performance compared to six counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the FedL2G method, designed to address challenges in Heterogeneous Federated Learning that arise from data and model heterogeneity. The proposed method focuses on optimizing the training process by ensuring that additional guiding objectives introduced during the federated learning process are beneficial and align with clients' original local objectives.

### Strengths
1. The paper is well-written and easy to follow.
2. The paper is well-motivated that Heterogeneous Federated Learning is quite realistic.
3. The authors provide rigorous convergence analysis.

### Weaknesses
1. The paper may overlook some important related methodologies, such as FedPCL[1] and FPL[2], which also address the central issue highlighted by the authors: the deviation of aggregated global prototypes from client-specific feature vectors due to data heterogeneity. Specifically, FPL tackles similar challenges, making its comparison with FedL2G pertinent for a comprehensive evaluation.
2. The proposed method introduces complexity by requiring an additional small quiz set and a warm-up period, which could complicate implementation. The quiz set, while beneficial for validating model updates, may also introduce an unfair advantage over other baselines that do not use this approach.
3. It would be beneficial for the authors to include more recent federated learning methodologies like FedPCL[1] and FPL[2] in the experimental comparisons. The current baseline methods, while foundational, may not represent the state-of-the-art, limiting the robustness of the comparative analysis presented.
4. Including experiments on the DominNet dataset could enhance the applicability and robustness of the FedL2G method across diverse scenarios.

### Questions
Please see the weakness above.

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
The paper under review studies heterogeneous federated learning (HtFL) and aims to address the mismatch between local and global learning objectives. By learning a set of local guiding vectors during model training, the local loss is prioritized when minimizing the global loss. The guiding vectors are compact in size and are updated based on feedback from clients’ local quiz sets. Therefore, the proposed FedL2G method is claimed to be lightweight, efficient, and adaptable.

### Strengths
1. Sections 1 and 2 clearly introduce the research problem, relevant literature, and contributions, making the paper easy to follow.

2. The mismatch between model personalization and generalization is identified as a primary research problem in the field of HtFL. 

3. Guiding vectors, which are compact in size, are communicated between clients, thereby reducing communication overhead compared to direct model sharing.

4. Relevant benchmarks and theoretical analysis are included to support the paper’s contributions.

### Weaknesses
1. Feature Extraction Consistency: The consistency of feature extraction is not discussed in detail. With heterogeneous models and quiz sets across different clients, distributed feature extraction may produce varying representations (i.e., guiding vectors) for the same class. How can the averaging of vectors in line 13 of Algorithm 1 be effective in this context? Are there any explanations of feature extraction consistency when local models and private datasets are heterogeneous? Specifically, the paper lacks a discussion on how the feature spaces of different local models align, and how the averaging of guiding vectors can be meaningful when these feature spaces are potentially very different. The paper should include an analysis of the variance in feature representations across clients and how this variance impacts the effectiveness of the global guiding vectors.

2. Warm-Up Period in Large-Scale Distributed Learning: In practical settings, a warm-up period may not be feasible in large-scale distributed learning scenarios. Does the warm-up phase require all clients to join the system for at least 50 rounds, as indicated on line 236? An ablation experiment should be added to help readers understand why the warm-up is necessary or to quantify the accuracy loss if it is omitted. The paper should clarify whether the warm-up phase requires all clients to participate, or if a subset of clients is sufficient. Furthermore, the impact of the warm-up duration on the final performance and convergence speed should be analyzed in detail.

3. Data Heterogeneity Settings: The data heterogeneity settings may be overly strict. Using a Dirichlet distribution with control parameters like 0.1 and 0.01 makes the dataset highly skewed. The authors should explore a range of settings, from 0.01 to 1, to show how data heterogeneity impacts the performance of FedL2G. The current evaluation focuses on highly skewed data distributions, which may not reflect real-world scenarios. A more comprehensive analysis is needed to understand the method's performance under various degrees of data heterogeneity, including less skewed distributions.

4. Quiz Set Requirement: The proposed approach assumes that each client can maintain a quiz set, which implies that clients have sufficient training data. The authors should clarify a practical scenario to support this assumption and ensure that the settings are realistic. The paper should address the practical limitations of requiring a quiz set for each client, especially in scenarios where clients have limited data or resources. The authors should discuss the sensitivity of the method to the size of the quiz set and explore alternative strategies if maintaining a quiz set is not feasible.

### Questions
1. How can the averaging of vectors in line 13 of Algorithm 1 be ensured to be effective? Are there any explanations regarding feature extraction consistency when local models and private datasets are heterogeneous? The authors should provide quantitative analysis to assess how the consistency of feature extraction impacts the performance of the guiding vectors, for example, measuring cosine similarity between guiding vectors from different clients for the same classes, or examining how variance in feature representations correlates with model performance.

2. Does the warm-up phase require all clients to join the system for at least 50 rounds, as indicated on line 236? An ablation experiment should be included to help readers understand the necessity of the warm-up phase or to quantify the accuracy loss if it is omitted. The review suggests the authors compare performance with different warm-up durations (e.g., 0, 25, 50, 100 rounds) and analyze how it affects convergence speed and final accuracy across various client participation scenarios.

3. Will the proposed method outperform benchmarks in both homogeneous and heterogeneous data settings? The authors should explore a range of heterogeneity settings, with a verity of Dirichlet parameters, to demonstrate how data heterogeneity impacts the performance of FedL2G. The reviewer suggests adopting specific Dirichlet parameter values to test (e.g., α = 0.01, 0.1, 0.5, 1, 10) and suggests key metrics to report for each setting, such as accuracy, convergence speed, and communication efficiency.

4. What real-world scenario allows for sufficient quiz sets and warm-up phases? The authors should clearly state a practical scenario to justify the feasibility of these settings. The reviewer suggests that the authors may provide specific examples of real-world applications where these requirements could be met, or discuss potential modifications to the method for scenarios with limited data or stricter time constraints.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To address the objective mismatch in Heterogeneous Federated Learning, this paper proposes a Federated Learning-to-Guide method that adaptively learns to guide local training in a federated manner and ensures the extra guidance is beneficial to clients’ original tasks. The technique efficiently implements the learning-to-guide process using only first-order derivatives and achieves a non-convex convergence rate of $\mathcal{O}(1/T)$. The authors provide empirical validations on the theoretical results as well.

### Strengths
The proposed method is well-motivated, the paper shows that existing methods suffer from the objective mismatch issue, and show how to fix it.

The empirical results show that Federated Learning-to-Guide method is better than other lightweight HtFL methods, as expected, and the authors conduct ablations that show the influence of the server learning rate and visualizations of data distributions.

### Weaknesses
The analysis only covers FedOpt with SGD as the optimizer. Still, recent work [1] shows a different combination (Nesterov-accelerated SGD as the outer optimizer and AdamW as the inner optimizer) is much better for practical performance.

In the theorems that are presented, summarizing the main insights of these theorems may be needed since currently they are just written as long paragraphs.

In experiments, the least partial client participation ratio is set as 0.5. In more realistic settings, the participation ratio is lower with more clients.

### Questions
See in weaknesses.

### Soundness
2

### Presentation
2

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
This paper focuses on two classic challenges in Federated Learning (FL): data heterogeneity and model heterogeneity, both of which are crucial for deploying FL in real-world scenarios. In model-heterogeneous settings, aggregating model parameters is not feasible, making the aggregation of class prototypes a common approach. However, the authors observe that the simple aggregation of locally uploaded class prototypes into a global prototype fails to effectively guide the local training process. Thus, the authors propose a Federated Learning-to-Guide (FedL2G) method, which adaptively learns to guide local training in a federated manner and ensures that the additional guidance is beneficial to clients’ original tasks.

### Strengths
1) The paper tackles two critical challenges for deploying Federated Learning: data heterogeneity and model heterogeneity, which are essential for real-world FL deployment.
2) The authors identify that simple aggregation of class prototypes can even harm local updates, and therefore propose a learnable approach to generate global prototypes that effectively guide local training processes.
3) The paper provides a convergence proof, validating the theoretical feasibility of the proposed method.
4) Extensive experiments are conducted to demonstrate the effectiveness of FedL2G.

### Weaknesses
1) The meaning conveyed by Figure 1 is unclear. It lacks sufficient explanation, making it difficult to understand the challenges the paper aims to address based on the illustration.
2) Figure 2 has poor readability, and the lines are overly complicated and cluttered, making it hard to capture the key points. I recommend adding some descriptions to aid in understanding.
3) Although Figure 1 somewhat points out the challenges to be solved, the paper lacks sufficient motivation to validate this phenomenon. Specifically, there is no clear demonstration of how simple prototype aggregation fails or why it leads to performance degradation in the context of heterogeneous models and data.
4) I am concerned about whether uploading local class prototypes or features of local data samples may leak local data privacy since these data represent local statistical information. The paper does not sufficiently address the privacy implications of sharing these intermediate representations.
5) There is a misuse of symbols. In Equation 1, the denominator uses "n" to represent the overall data, which may be misunderstood as "n" representing a specific device, especially since there are a total of N clients.
6) There is a lack of qualitative or quantitative analysis to prove that the proposed method effectively reduces the cross-entropy loss on users' local data. It is not clear if the proposed guidance truly aligns with the local objectives of each client.
7) Equation 6 aggregates gradients uploaded by all clients in a simple manner, which I believe may further introduce bias. This is because the information uploaded by strong clients (with stronger feature extraction capabilities and more data) should be more valuable than that from weaker clients. The aggregation method does not account for the varying quality of information from different clients.

### Questions
1) For the prototypes uploaded by different clients, can dynamic aggregation be performed based on the performance of each client? Strong clients often have richer information, so the initial global prototype could be aggregated based on their information to guide the training of weaker clients. As weaker clients produce more robust prototypes, they can also upload their local class prototypes to aggregate a new global prototype.
2) For other issues, see weakness.

### Soundness
3

### Presentation
3

### Contribution
2
