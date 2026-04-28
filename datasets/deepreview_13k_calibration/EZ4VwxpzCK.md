# PROSPECT: Learn MLPs Robust against Graph Adversarial Structure Attacks

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 3, 6

## Abstract
Current adversarial defense methods for GNNs exhibit critical limitations obstructing real-world application: 1) inadequate adaptability to graph heterophily, 2) absent generalizability to early GNNs like GraphSAGE used downstream, and 3) low inference scalability unacceptable for resource-constrained scenarios. To simultaneously address these challenges, we propose PROSPECT, the first online graph distillation multi-layer perceptron (GD-MLP) framework for learning GNNs and MLPs robust against adversarial structure attacks on both homophilous and heterophilous graphs. PROSPECT fits into GraphSAGE seamlessly and achieves inference scalability exponentially higher than conventional GNNs. Through decision boundary analysis, we formally prove the robustness of PROSPECT against successful adversarial attacks. Furthermore, by leveraging the Banach fixed-point theorem, we analyze the convergence condition of the MLP in PROSPECT and propose a quasi-alternating cosine annealing (QACA) learning rate scheduler, inspired by our convergence analysis and the alternating iterative turbo decoding from information theory. Experiments on five homophilous and three heterophilous graphs demonstrate the advantages of PROSPECT over current defense methods and offline GD-MLPs in adversarial robustness and clean accuracy, the inference scalability of PROSPECT orders of magnitude higher than existing defenders, and the effectiveness of QACA.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a bidirectional distillation method, called Prospect, between a GNN and MLP to mitigate the vulnerability of GNNs w.r.t. structure perturbations. The authors propose a custom learning schedule based on cosine annealing with warm restarts and prove some properties of their method using cSBMs. The authors demonstrate the effectiveness of their approach on homophilous and heterophilous datasets using a transfer poisoning attack.

### Strengths
1. Theoretical motivation of architecture on cSBMs
1. Prospect consistently outperforms the baselines in the empirical evaluation
1. Prospect is demonstrated to defend against adversarial transfer attacks on homophilic and heterophilic datasets
1. Prospect can handle scalable GNN architectures like GraphSAGE

### Weaknesses
1. The paper is full of overstating claims like "Theorem 1 implies the adversarial robustness of Prospect". While Theorem 1 might imply robustness on cSBMs, it is merely conjectured that this robustness extrapolates to real-world graphs.
2. Poisoning defense heavily uses the restricted threat model to solely perturb the graph structure and not the node features. It is one thing to follow the many other works in this simplifying assumption that focuses on the distinct characteristics of the robustness of GNNs; however, exploiting the clean node features seems highly questionable. The authors should discuss this and evaluate w.r.t., e.g., a joint attack on the graph structure and node features.
3. The empirical evaluation is insufficient: The authors solely evaluate using a non-adaptive transfer attack. As pointed out previously, it is vital to assess neural networks with adaptive attacks [C, D] to get a proper estimate of the model's robustness.
4. The authors claim scalability. Thus, they should compare to other works using large graphs [A, B]
5. Just because an MLP is robust w.r.t. structure perturbations does not imply it is useful. Moreover, there might be an interaction between the GNN and MLP. If the authors make a claim about evasion (e.g. second last line of page 3), they should also verify that empirically.
6. The presentation of the Theorems in the main part could be improved. It is unclear how the reader should deduce Theorem 1 from Proposition 1&2. Perhaps it would be better to move the propositions to the appendix and instead add a proof sketch to the main part.

### Questions
1. Can the authors please provide a full list of assumptions required for Proposition 1 & 2 as well as Theorem 1? For improved readability, the assumptions could be stated more explicitly and organized in the main text.
1. Could the theory be extended to further data-generating distributions like Barabasi–Albert? [E] 

[E] Community recovery in a preferential attachment graph, Hajek and Sankagiri, IEEE Transactions on Information Theory 2019.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To address 1) low adaptability to heterophily, 2) absent generalizability to early GNNs, and 3) inadequate inference scalability of current defense methods for GNNs, the authors introduce PROSPECT, a defense framework incorporating an online mutual distillation approach between a GNN and an MLP, which enhances the performance on node-level classification tasks for both poisoned and clean graphs. Additionally, the authors apply a quasi-alternating cosine annealing (QACA) learning rate scheduler to improve the optimization process. The proposed approach is supported by detailed theoretical analysis and extensive empirical experiments to validate its effectiveness in mitigating the identified issues in GNNs.

### Strengths
- Incorporating the mutual distillation method into the existing GD-MLP to impart the MLP’s robustness to adversarial structure attack to GNNs is a concept of interest and significance in practice.

- The theoretical assessment of MLP-to-GNN distillation and QACA learning rate schedular is well discussed and convincing to me.

- Reducing inference time to the level of an MLP while improving the robustness to untargeted poisoning attacks and performance on clean graphs is both uplifting and commendable, with a series of empirical experiments conducted on both graphs of homophily and heterophily.

### Weaknesses
While the application of mutual distillation to the GD-MLP is inspiring, it’s worth noting that the novelty of the proposed approach appears somewhat limited, since there has been extensive research and discourse surrounding mutual distillation and distillation from GNNs to MLP. The absence of a specific design tailored to accommodate the unique characteristics of graph-structured networks might dilute the distinctiveness of this approach.





### Questions
- The empirical examination of PROSPECT's robustness against a specific untargeted poisoning attack, Metattack, is commendable. However, it could potentially enhance its persuasiveness by extending the experiment to include targeted attack scenarios and additional untargeted attack methods, such as GraD.

- Considering that PROSPECT is designed to be adaptable for various GNNs, it might be practical and insightful to explore its performance under more powerful GNN architectures, such as EvenNet and GPRGNN. This could offer insights into the performance limitations and strengths of the proposed framework.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces PROSPECT, a graph distillation framework for learning robust GNNs/MLPs against graph adversarial attacks. Specifically, authors leverage two loss functions for GNN-to-MLP and MLP-to-GNN distillation. By alternately minimizing the loss functions, PROSPECT learns robust GNNs/MLPs that are resistant to graph attacks. Experimental results show that PROSPECT improves clean and adversarial accuracy over defense baselines on both homophilous and heterophilous graphs.

### Strengths
- Overall, the paper is well-written.
- Authors have evaluated PROSPECT on both homophilous and heterophilous datasets.

### Weaknesses
 - Missing relevant defense models for evaluation. Authors mentioned that prior purification methods are computationally expensive and restricted to homophilous graphs. However, there are some recent studies (e.g., [1]) that have addressed these limitations. It would largely improve the paper to include comparisons against proper baselines.
- Missing adaptive attack results. As shown by [2], most prior defense GNN methods can be easily broken by adaptive attacks, which are aware of the given defense method during attacking. Thus, it is very important to adaptively attack PROSPECT to demonstrate its true robustness. Specifically, the current evaluation relies solely on transfer attacks, which may not accurately reflect the model's resilience against a more informed adversary. The absence of adaptive attacks leaves a significant gap in the robustness assessment.
- The heterophilous datasets used in this work (e.g. Chameleon) are known to have some critical issues (e.g., train-test data leakage) [3]. Hence, the experimental results would be more compelling if authors could evaluate on the datasets from [3,4].
- Missing detailed hyperparameter settings for baselines. Note that many defense methods (e.g., ProGNN) require decent hyperparameter tuning to achieve their best performance. It is unclear whether authors put in enough efforts on tuning those baselines.
- Claim 3 is too strong. Given that PROSPECT is only integrated with GraphSAGE in this work, it is improper to claim PROSPECT can boost clean accuracy of GNNs, unless authors conduct more experiments with different GNNs integrated into PROSPECT.

### Questions
- It does not seem reasonable to adopt GCN as the surrogate model for MetaAttack on heterophilous datasets. Why didn't the authors choose heterophilous GNNs as the surrogate model?
- Are baseline models trained with cosine annealing learning rate scheduler?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an online GNN-MLP distillation framework, PROSPECT, that is able to handle heterophily and robust to graph structural attacks.
The online framework is enhanced via a specified learning rate scheduler.
The effectiveness of both the framework and scheduler is theoretically verified.
The robustness of PROSPECT is empirically validated via extensive experiments against structural attacks.

### Strengths
1. It is interesting to study how distillation methods perform under heterophily. 
2. Good theoretical guarantees for the proposed methods.
3. Desirable robustness against structural attacks.

### Weaknesses
1. **About Motivation.** The most concern of mine is that the improvement with respect to robustness and performance under heterophily results from the introduction of distillation but not the proposed PROSPECT. 
Based on the analysis, any GNN-MLP distillation framework seems to surpass a single GNN in the two fields.
While the advantage of PROSPECT over previous distillation methods regarding clean accuracy is slightly discussed on page 4, how PROSPECT excels against attacks and heterophily is unclear. Specifically, the paper does not clearly articulate why the proposed *mutual* distillation approach is superior to a simpler, unidirectional distillation from GNN to MLP, especially in the context of robustness and heterophily. The core argument for the mutual approach seems to be missing, leaving the reader to wonder if the gains are simply due to the presence of *any* distillation, rather than the specific proposed method.
2. **Number of Hyperparams.** The whole framework, together with the scheduler, includes quite a few hyperparameters compared to the baselines. 
It would be a concern if the hyperparameters varied a lot between different datasets. 
Also, if the performance is highly affected by the hyperparameters. The paper needs to provide a more thorough analysis of the sensitivity of the model to these hyperparameters, including how they are selected and if they require significant tuning for each dataset. The lack of a clear hyperparameter selection strategy and sensitivity analysis makes it difficult to assess the practical applicability of the proposed method.
3. **Baseline Missing.** A robust defense model that also tackles heterophily is not included. It would be better to have a comparison to it. [1] The absence of a direct comparison to a state-of-the-art robust defense model that also addresses heterophily significantly weakens the empirical evaluation. It is crucial to demonstrate that PROSPECT offers a competitive advantage over existing methods that explicitly target both robustness and heterophily, rather than just showing improvements over standard GNNs.
4. **Presentation.** The current version is not friendly to those unfamiliar with distillation and graph adversarial attacks. It would be better if more details about distillation (like the online/offline settings) and a pseudo-code of PROSPECT were offered. The paper assumes a level of familiarity with distillation techniques and graph adversarial attacks that may not be universal among the target audience. Providing a more detailed explanation of these concepts, along with a clear pseudocode of the PROSPECT algorithm, would significantly improve the accessibility and clarity of the paper.

### Questions
1. **Training time.** While the framework shows the desirable inference efficiency, what about its training time? 
2. **About Figure 1.** It is good to see that the proposed QACA works through the ablation study in Figure 1. 
However, the fixed version seems noncompetitive against other defense baselines. 
Is the QACA scheduler the one that actually contributes to the performance?
Can the previous distillation methods be enhanced by QACA as well?
3.  **Concerns when faced with other attacks.** 
It makes sense that MLP is robust against structural attacks and acts as good teachers to GNNs, but when faced with feature attacks or graph injection attacks, the introduction of distillation could lead to worse performance.
As the robustness is only tested against Metattack, it would be more convincing if PROSPECT is tested under more attack settings.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
