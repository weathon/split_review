# Factor Graph-based Interpretable Neural Networks

- Decision: Accept
- Scores: 6, 8, 5, 6, 6

## Abstract
Comprehensible neural network explanations are foundations for a better understanding of decisions, especially when the input data are infused with malicious perturbations. Existing solutions generally mitigate the impact of perturbations through adversarial training, yet they fail to generate comprehensible explanations under unknown perturbations. To address this challenge, we propose AGAIN, a fActor GrAph-based Interpretable neural Network, which is capable of generating comprehensible explanations under unknown perturbations. Instead of retraining like previous solutions, the proposed AGAIN directly integrates logical rules by which logical errors in explanations are identified and rectified during inference. Specifically, we construct the factor graph to express logical rules between explanations and categories. By treating logical rules as exogenous knowledge, AGAIN can identify incomprehensible explanations that violate real-world logic. Furthermore, we propose an interactive intervention switch strategy rectifying explanations based on the logical guidance from the factor graph without learning perturbations, which overcomes the inherent limitation of adversarial training-based methods in defending only against known perturbations. Additionally, we theoretically demonstrate the effectiveness of employing factor graph by proving that the comprehensibility of explanations is strongly correlated with factor graph. Extensive experiments are conducted on three datasets and experimental results illustrate the superior performance of AGAIN compared to state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposed a method using factor graphs to correct errors in concept-based explanations caused by perturbations. 
Specifically, it constructs a factor graph using predefined logical rules between concepts or between concepts and categories. 
This graph helps identify logical errors in the output from concept-based interpretable neural networks by evaluating the likelihood of these errors. 
Additionally, by leveraging the factor graph, it is possible to correct these logical errors in the explanations. 
Experimental comparisons on three datasets demonstrate that the proposed method outperforms existing concept-based approaches.

### Strengths
- The proposed method enables both the detection of logical errors and the correction of these errors within a single framework.
- Compared to other concept-based interpretable neural networks, the proposed method achieves higher comprehensiveness in explanations, regardless of whether the perturbations are known or unknown.

### Weaknesses
 - While the proposed method assumes that explanations change due to perturbations without affecting predictions, this seems unrealistic. Particularly in interpretable neural networks with a concept bottleneck structure, as assumed in this study, changes in the concepts outputted by the neural network would naturally lead to changes in predictions, which undermines this assumption. It's unclear how the method would handle scenarios where perturbations cause both concept and prediction changes, potentially leading to a misalignment between the corrected explanations and the actual model behavior.
- The proposed method requires predefined logic rules between concepts and categories. If these rules are already known, wouldn’t it be possible to detect inconsistencies between concepts and predictions without the need for the factor graph? The advantage of using a factor graph is unclear. The paper does not sufficiently justify the necessity of the factor graph over simpler methods that directly apply the logic rules to check for inconsistencies. The added complexity of the factor graph should be more clearly motivated by demonstrating its unique capabilities in handling uncertainty or complex relationships that simpler methods cannot.
- As noted in the minor comments below, there is room for improvement in the writing.

### Questions
- Defining the logic rule set seems expensive. Would it be difficult to construct a factor graph by connecting concepts and categories with a bipartite complete graph and estimating the weights $w_i$?
- How do you distinguish between coexistence and exclusion in the factor graph?
- It would be better to describe the specific estimation algorithm of $w_i$ in the Appendix.
- Line 336-337: What is "attributional training"?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces AGAIN (fActor GrAph-based Interpretable Neural Network), which generates comprehensible explanations for neural network decisions even under unknown perturbations. Unlike traditional adversarial training methods, AGAIN incorporates logical rules through a factor graph to identify and rectify explanatory logical errors during inference. The model is validated on three datasets: CUB, MIMIC-III EWS, and Synthetic-MNIST, demonstrating superior performance compared to existing baselines

### Strengths
- **Good presentation and structure** The paper is well-structured and easy to read. The mathematical definition of the proposed method is clear and well-defined. 
- **Nice experimental campaign**: Extensive experiments on three datasets (CUB, MIMIC-III EWS, and Synthetic-MNIST) demonstrate the superior performance of AGAIN over the compared baselines, although these results hold mainly for a metric (LSM) that has been created ad-hoc.

### Weaknesses
## Major Issues

- **Novelty, Related work and Compared methods**: the main issue with the current paper is that it only considers methods injecting knowledge into the models by means of factor graphs. However, the integration of knowledge into model predictions has been fully studied under different point of views: probabilistic (e.g., DeepProblog [1] and all its variants), logic constraints (see the survey of Giunchiglia et al. [2]). Also, it is not the first method defending against adversarial attack with knowledge and without employing adversarial training. Some of these methods have been already employed to defend against adversarial attacks, such as [3-4]. [5] is a survey entirely dedicated to enhancing interpretability and adversarial robustness with prior knowledge. [6] has shown in the context of concept-based models that it can learn logic rules at training time and use them at inference time to defend against adversarial attacks. This is also reflected in the experimental campaign that is extensive but does not consider any methods injecting prior knowledge to defend against adversarial attacks. The only compared methods are CBMs or adversarial-trained versions of the same models. 


- **Paper positioning and Preliminaries**: the method provides explanations and a defence mechanism that is based on concept predictions; thus, it applies only to concept-based models. Most of the compared methods also belongs to this niche. While this is fully acceptable, explicit references to concept-based models only appears in Section 3-4. Therefore, I think it should state earlier that this is the focus of the paper, as most of the related work mentioned in the paper does not focus on concept-based explanations. Furthermore, there is no explicit mentions to concept-based models in the preliminaries. The “Interpretable Neural Network” paragraph should include citations to this literature and explain concept-based models.

## Minor Issues
- P.2 “[…] even if the adversarial samples are available, retraining is only effective for at most one perturbation type” I think this statement is quite strong, and although it may have been proved for some attacks in Tan & Tian, 2023, I don’t think it is a general assumption that we can make. I think this sentence should be soften to “retraining is effective only for few perturbation types at the same time”. 
- P.2 “[…] to ensure the expectation of the potential function is in its maximum value”. It is not clear at this point what is the potential function. Consider rephrasing this sentence.
- P.2 “The explanations that are further regenerated align with the exogenous logic.” Not clear in this case what are the exogenous factors. 
- P.2-3: The term "defenses against comprehensibility" seems a bit misleading. It implies that the goal is to prevent explanations from being understandable, which is not the case. Instead, the focus is on defending the comprehensibility of explanations against perturbations. “defenses of comprehensibility” colud be a more appropriate definition.

### Questions
- Can the authors provide a comparison against one of the methods injecting knowledge (prior or learnt)?
- Scalability: The two limitations that have been reported (domain knowledge changes, correct prediction categories) are non-negligible. How could this method be extended to face these limitations?

### Soundness
3

### Presentation
3

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
This paper proposes AGAIN (fActor GrAph-based Interpretable Neural Network), a new approach to maintain comprehensible neural network explanations when inputs are affected by unknown perturbations. AGAIN builds factor graphs from explanations, and integrates logical rules through the graphs. The system detects adversaries by identifying violations of real-world logic, and uses an interactive intervention strategy to fix incorrect explanations. Tested on three datasets (CUB, MIMIC-III EWS, and Synthetic-MNIST), AGAIN outperformed existing methods in generating comprehensible explanations under both known and unknown perturbations.

### Strengths
1. The paper proposes a novel and interesting idea that uses the logical correctness of explanation to detect and defense against noises and adversaries.
2. The three stage framework is reasonable to me. 
3. The examples used in the paper are intuitive.

### Weaknesses
1. The concept bottleneck model is not easy to scale, as it requires manual annotations of concepts.
2. The implementation details of Section 4.2 is not very clear (the introduction is too conceptual). For example, is $\mathcal{G}$ a graph or a model? At the beginning I thought $\mathcal{G}$ is a graph, but in Line 221 it "reasons about a conditional probability".
3. The datasets used in this work are not very strong. I doubt if the work is applicable to real-world situations. At least, the datasets used cannot reflect adversarial scenarios in practice.

### Questions
How is the reasoning conducted on G? How is the probability estimation implemented in Equation 1? Please provide more details.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes AGAIN, a neural network model that generates comprehensible explanations under unknown perturbations by integrating logical rules directly during inference, rather than relying on adversarial training. Using a factor graph to identify and rectify logical inconsistencies, AGAIN demonstrates superior interpretability and robustness compared to existing methods.

### Strengths
1. The paper presents an innovative method, AGAIN, that combines factor graphs with concept-level explanations to improve model interpretability under unknown perturbations.
2. The authors evaluate AGAIN across multiple datasets and baseline models, providing a broad view of its effectiveness.
3. The paper is clear and well-structured.

### Weaknesses
1. The factor graph requires predefined logical rules, which could be challenging to construct or generalize across different domains. The reliance on manually defined rules introduces a potential bottleneck, especially when dealing with complex or novel scenarios where such rules are not readily available or easily formulated. This could limit the applicability of the method in real-world settings where the underlying logic is not well-understood or is constantly evolving.

2. The algorithm’s process of exploring all possible intervention options to find the optimal solution could create computational overhead. The exhaustive search for the optimal intervention, while ensuring the best possible outcome, might become computationally infeasible as the number of concepts and their potential interventions increases. This could severely limit the scalability of the approach, making it impractical for large-scale problems or real-time applications where computational resources are constrained.

### Questions
1. The authors employed black-box perturbations to test robustness. Adding input noise could provide more convincing evidence.
2. I am concerned about the potential impact of large factor graphs on computational efficiency. I would like to see an analysis on this problem.
3. Currently, the algorithm explores all intervention options to select the optimal one. Is it possible to employ a simplified strategy, such as a heuristic or greedy algorithm, to reduce computational load?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose a novel method called AGAIN to generate comprehensible explanations under unknown perturbations by employing a factor graph approach. The method presents a significant contribution to the field, addressing an important gap with a new perspective. The paper is well-structured, and the authors have provided thorough theoretical justifications and experimental analyses. These analyses effectively demonstrate the superiority of the proposed method over existing ones.

### Strengths
The paper offers a well-motivated and clear presentation of a unique approach. The use of a factor graph to handle perturbations is innovative and highly relevant to the research community. Furthermore, the authors have provided sufficient theoretical support and empirical evidence to justify the effectiveness of their approach.

### Weaknesses
1. Clarification on Figure 3:
   In Figure 3, does the final output include hat{c}_{re} and prediction? Does the hat{c}_{re} mean the interpretation? Additionally, the figure lacks clarity on how hc is generated, which is crucial for understanding the method. Adding details on hc generation would make the figure more comprehensive.
 
2. Comparison Metrics:
   The authors compare their method with all baselines using the LSM metric. However, they only compare their method with CBM in terms of accuracy (P-ACC and E-ACC). It would be beneficial to extend the accuracy comparison to include all baselines to provide a more complete evaluation of the method’s performance.
 
3. Figure 7 Interpretation and Readability:
   In Figure 7, for each example, the authors provide two bar charts. Does the left bar chart represent the initial interpretation, and the right bar chart represent the interpretation combined with the factor graph? Clarification on this aspect would enhance the understanding of the figure. Additionally, some symbols and text in Figure 7 are overlapping.
 
4. Inconsistency in Line 463 and Table 5:
   The authors mention in line 463 that their method is compared with two baselines on the Synthetic-MNIST dataset. However, Table 5 lists four baselines. Furthermore, "ProbCBM" in Table 5 should be corrected to "ProCBM" for consistency. It is recommended that the authors proofread the paper to eliminate such inconsistencies and typographical errors.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
