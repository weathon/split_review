# Fast Conditional Intervention in Algorithmic Recourse with Reinforcement Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Explaining the decisions made by machine learning classifiers aids individuals in identifying critical factors and charting future plans. Recent studies have shown that incorporating causal graphs of input features provides more realistic explanations; however, this also introduces new challenges such as handling noisy graphs and efficiently performing inference with black-box classifiers. In this work, we tackle these issues by presenting an efficient reinforcement learning (RL)-based approach with an idea of conditional intervention. Our intervention method is theoretically preferable and considers both feature dependencies and incompleteness of graphs. Simultaneously, the RL-based method offers the capacity to learn the intervention process while guarantees computational complexity at inference stage. In the experiments, we showcase the efficiency and superior performance of our solution when compared to baseline methods on both synthetic and real datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an efficient RL-based approach with the idea of conditional intervention, with the goal of handling noisy and/or incomplete graphs, as well as efficient performance of inference for black-box classifier. The experimental results show the efficiency of the proposed method on both synthetic and real datasets.

### Strengths
The paper tackles an important problem in algorithmic recourse, which is causal sequential recourse, using the technique from reinforcement learning that works in a boarder setting compared to the previous paper.

### Weaknesses
One weakness of the paper is the assumptions are pretty strong-- it feels like a lot of assumptions (e.g., the formulation of intervention cost) are made for mathematical convenience rather than for accurate modeling. Specifically, the intervention cost, which is based on the conditional variance of a feature given its parents, seems like a proxy for uncertainty rather than a direct measure of the impact of intervention. The paper does not provide a strong justification for why this specific form of intervention cost is the most appropriate, and it's unclear how sensitive the results are to this choice. In addition, the writing and structure of the paper can be improved; for example, it is still unclear to me how CIR is especially superior to existing methods in preserving causality and how the method handles incomplete graph cases. The paper claims that the method works in a broader setting compared to previous works, but the exact limitations of prior methods and how the proposed method overcomes them are not clearly articulated. Answering the questions in the Questions section might help make some clarifications.

Typo:

1. At the bottom of page 5, "...$X_k$ is intervened upon is calculated by.."

### Questions
1. The paper mentions that "The less it is determined by their parents, the more _space_ we can intervene." Could you explain more why that's the case? in particular, what does "space" mean? And why do we want to primarily intervene in higher uncertainty endogenous features? 

2. Does the size of the action space grow exponentially as a function of the feature space? If so, how does the algorithm handle this?

3. Intuitively, what is the benefit of conditional intervention compared to traditional intervention? 


Typo:

1. At the bottom of page 5, "...$X_k$ is intervened upon is calculated by.."

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of finding realistic and causally-grounded counterfactual explanations. They propose a reinforcement learning (RL)-based approach with conditional interventions. The proposed intervention method has theoretical properties, e.g., it considers both feature dependencies leveraging the SCM. For the RL strategy, computational complexity is provided. Experiments are performed on synthetic and real datasets.

### Strengths
This paper brings together counterfactual fairness, causality, and reinforcement learning. 
The strategy tries out several interventions using reinforcement learning to identify a realistic recourse given an SCM. It is mathematically interesting.

The challenge arises since at each stage the RL agent has to decide which feature to intervene and also with what value. To address this challenge, the RL agent will leverage a structural causal model. Then, it would perform conditional interventions, i.e., interventions conditioned on the parents of that feature. Ultimately, the goal is to obtain a counterfactual that will respect the SCM and also be as close to the original point as possible in fewer steps than the number of features changed. Additionally, they require the number of interventions T to be less than p which is the number of actionable features.

They have included relevant baselines in their experiments, and show time benefits.

### Weaknesses
One limitation is that the SCM may not always be available.

The scenario of incomplete causal graphs as mentioned in the abstract was not very clear to me. What is the assumption here?

The experiments directly seem to use the causal discovery method of another paper. Is this done for the proposed method as well?

I also wonder if RL is a bit of an overkill for this problem since the number of features (p) is often quite small. It is often desirable to intervene on fewer features. For instance, the experiments drop the feature Capital Gain since intervening only on that one feature suffices for recourse. Also, what about exploration? Could the authors strengthen the motivation behind this approach?

And also, how is the time being calculated in the experiments? It seems to be only the inference time. What about preprocessing time? Could the authors discuss/elaborate on the preprocessing time of various methods?

The experiment section does not provide enough details on how the causal graph was generated for the real-world datasets and if that causal graph is reliable.

Ultimately, human evaluations might also be necessary at some point to compare different methods.

### Questions
Already discussed in weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to use RL agent for helping design more efficient and accuracy intervention strategies for explanations.  By the desgined architecture with the so-called interventional cost as loss functions, the method shows some advantage over existing ones on some datasets.

### Strengths
1. The use of RL is interesting.
2. The experiments concerning interventions are convincing.

### Weaknesses
1. Some theoretical properties need more justifications. Specifically, the connection between the proposed intervention cost and the causal proximity measure needs more rigorous analysis. The claim that the intervention cost (IC) degrades to the causal proximity under certain conditions is not sufficiently justified. It is unclear how the variance or entropy of features directly translates to the strength of missing causes, and how this is incorporated into the IC. The paper needs to provide a more concrete theoretical framework for how the IC bounds the endogenous features and how the error from eq. 7 is related to the difficulty of changing the classifier output. 
2. The efficiency of training needs more evaluations. While the authors mention training time, they do not provide a detailed analysis of how the training time scales with the number of features, data points, or complexity of the model. It is also unclear how the choice of RL hyperparameters affects the training time and the final performance. The paper should include a more thorough evaluation of the computational cost of the proposed method, including memory usage and convergence analysis.

### Questions
1. About Fig 2. Is this graph representative? It seems the only confounder is U_0, and other Us can be considered as additive noise. Why this graph is used as an example for experiments?
2. About the theoretical aspects of "incomplete SCM". Is there any theoretical justification of how "incomplete" your method works? Or under some quantification of missing nodes, can you show some error bounds or something like that?
3. About the RL part. Is there anything related to the choice of reward, policy that have impacts on the final experimental outcomes?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an RL-based method for the recourse generation problem. The paper incorporates causal graphs of input features to calculate a new cost for conditional intervention called Intervention Cost. The experiments conducted on synthetic and real-world datasets show a better performance than baselines.

### Strengths
- The paper is easy to read and follow.
- The construction of the Intervention Cost is sound and highly motivated. 
- The proposed Markov Decision Process is well-defined and reasonable.

### Weaknesses
 - The paper assumes that all subjects share the same prior causal graph. However, in reality, each individual typically possesses a distinct causal graph. To address this concern, De Toni et al. (2022) [2] propose a solution. They initially establish a fixed causal graph and then iteratively learn the subject-specific cost function. Subsequently, they seek an appropriate sequence of interventions.
- The author omits the description of the reinforcement learning algorithm used to solve the MDP and its parameters. Specifically, the choice of the RL algorithm, its hyperparameters, and the training procedure are not discussed, making it difficult to reproduce the results.
- The way the author handles the noisy graphs (incompleteness of the casual graph) is unclear. The paper mentions modeling incompleteness via variance, but it lacks a concrete explanation of how this variance is estimated and incorporated into the intervention cost or the RL framework. The connection between the variance and the proposed intervention strategy is not well-established.
- The learning curve of rewards, objectives, and metrics should be reported. The evaluation can be improved by comparing the proposed method and baselines on more datasets. The current evaluation is limited in scope, and it is hard to assess the generalizability of the proposed method.
- In Section 3.2.3, the authors state that architectural corrections can alleviate the instability of the PASVG(0). However, there is no justification or ablation study for this claim. The specific architectural corrections are not detailed, and the lack of experimental evidence makes this claim unsubstantiated.

### Questions
- In section 3.2.2, when finding the longest path length between $X_i$ and $X_k$, what is the edge weight between two vertices of the graph?  Does the algorithm find the longest path on the casual graph?
- The reward function and the objective function in Section 3.2.2 are not related to each other, making me confused about interpreting their role in the training.

**References**

[1] Sahil Verma, Varich Boonsanong, Minh Hoang, Keegan E. Hines, John P. Dickerson, and Chirag Shah. Counterfactual explanations and algorithmic recourses for machine learning: A review, 2020.

[2] Giovanni De Toni, Paolo Viappiani, Bruno Lepri, and Andrea Passerini. Generating personalized counterfactual interventions for algorithmic recourse by eliciting user preferences, 2022.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
