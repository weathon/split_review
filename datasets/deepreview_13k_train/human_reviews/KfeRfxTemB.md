# Accelerating Task Generalisation with Multi-Level Hierarchical Options

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Creating reinforcement learning agents that generalise effectively to new tasks is a key challenge in AI research. This paper introduces Fracture Cluster Options (FraCOs), a multi-level hierarchical reinforcement learning method that achieves state-of-the-art performance on difficult generalisation tasks. FraCOs identifies patterns in agent behaviour and forms options based on the expected future usefulness of those patterns, enabling rapid adaptation to new tasks. In tabular settings, FraCOs demonstrates effective transfer and improves performance as it grows in hierarchical depth. We evaluate FraCOs against state-of-the-art deep reinforcement learning algorithms in several complex procedurally generated environments. Our results show that FraCOs achieves higher in-distribution and out-of-distribution performance than competitors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces fractures for learning bottom-up abstractions by clustering agent behavior across tasks.

### Strengths
* Paper is generally well-written.
* Related work appears exhaustive.
* Limitations are adequately addressed. 
* Results are generally compelling.
* Findings (with potential caveats; see below) are likely to be useful to the broader field.

### Weaknesses
 - The only domain where appropriate baselines are compared against is ProcGen. The results are still compelling, but another domain where baselines are also evaluated would have been useful to benchmark FraCO's relative utility. Additionally, some didactic experiments in the tabular settings with more appropriate baselines would be useful. 
- Despite discussing more advanced baselines in the related work (most notably HOC, which can support multiple levels of hierarchy), OC is the only one used.

### Questions
- HOC is not used as a baseline; why not? 
- FraCO is not compared against OC-PPO (or any other hierarchical approaches) in the tabular settings; why not?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the problem of reinforcement learning policies having a limited ability to generalize or adapt quickly to new environments. In order to overcome this limitation, the authors propose Fracture Cluster Options (FraCO). FraCOs leverage the history of trajectories on a set of training tasks, to create a set of options (alongside the primitive actions of the environment) for the agent to use during the testing phase where the agent is trained on the test tasks. The fracture is defined as the induced trajectory from state $s_t$, using actions $a_t, a_{t+1}, a_{t+2}, ..., a_{t+b-1}$ up to some length $b$. The motivation for doing this is given through a visualization of the latent space of the four rooms environment in which clusters of fractures show similar behaviours. In order to determine what options should be learned in this post-training phase, the authors create an Expected Usefulness metric based on the (1) Appearance Probability of a fracture in a trajectory, (2) Relative Frequency that some fracture appears in a successful trajectory, and (3) Entropy of Usage of that fracture. 

The authors then demonstrate the performance of their FraCO method on 4 standard grid-world environments, Metagrid environments, and Procgen environments.

### Strengths
1. Novel approach for discovering re-usable options to accelerate generalization abilities
2. Thorough empirical evaluation of the FraCO method across several benchmarks
3. Clear & honest evaluation of how well the FraCO method may work going forward to additional environments/settings

### Weaknesses
1. The paper is written in a manner to accelerate the generalization abilities of RL agents. However, there isn't a single mention of sample complexity in the paper. All of the plots and figures are concerned with the overall success rate of the agent. 
2. The given results across the 3 benchmarks are difficult to understand given that they are all success rate plots. In reinforcement learning, it is much better practice to use IQM plots [1] in order to compare the performance of multiple algorithms/configurations.
3. I strongly disagree with the decision to not tune the hyperparameters of the PPO algorithm when adding the additional option methods. It is very difficult to argue that PPO + options with the same hyperparameters as PPO alone. The hyperparameters of each method should have been tuned to ensure that a fair comparison has been made. 
4. The organization of the paper could be vastly improved. It was very difficult to find relevant formulas/definitions/etc in the current version because they are mixed in with the motivating example(s). I think it would benefit the overall quality of the writing to separate these two components. 
5. The final experiments in the Procgen environments should be run for more random seeds. I would say that 5 is a minimum, 10 is ideal. 
6. The weights of the Expected Usefulness should be empirically chosen. In addition, each component should be ablated (i.e. only use component 1) in order to determine what each of the 3 components of the metric add to the framework.

### Questions
1. In the Procgen experiments the authors disregarded the state information and only clustered based on the action sequences. Did you experiment with the addition of state information and find that it was causing issues (i.e. it was too noisy to use) ?
2. Could FraCO be used to facilitate better exploration of the state space? Or any other goals of learning options?
3. The use of a GAN to augment the dataset of Fracture Clusters was really interesting. Could this also be used in other regimes (i.e. a fixed computational budget regime) to learn FraCOs (or options in general) ? 
4. What kinds of skills/actions do the FraCOs learn?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a method for learning options which can be used to generalize across tasks.
FraCOs are learned based on patterns of a state and multiple subsequent actions observed in trajectories which reach a desired return threshold and are thus deemed successful.
The authors present results from multiple environments which demonstrate how the use of FraCOs improves learning across tasks which may vary in state space or reward function.

### Strengths
The problem of learning options (or other forms of sub-tasks) is an important issue in hierarchical RL.

The paper is well-written and generally easy to follow.

The motivation for the method provided in Section 4 is strong.

The experimental results effectively demonstrate the benefit of FraCOs in terms of generalizing between tasks and accelerating learning in new tasks in discrete state spaces.

### Weaknesses
There is a lack of discussion of continuous state spaces and no experiment(s) involving them.

It seems that a lot of data is required to learn the FraCOs before learning the actual policy, e.g., allowed to discover FraCOs in 50 of the 60 tasks used in Experiment 1. It would be nice to see a comparison of how the amount of FraCO pre-training affects the learning in later tasks and how that relates to, e.g., OC-PPO.

### Questions
Is there a reason that no continuous state spaces are used?

While the components of the usefulness metric all seem reasonable to include, is there any justification (possibly experimental) for why they are weighted the same?

### Soundness
3

### Presentation
3

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
The paper introduces Fracture Cluster Options (FraCOs), a multi-level hierarchical reinforcement learning method designed to improve generalization in new tasks. By identifying patterns in agent behavior and forming options based on expected usefulness, FraCOs achieves outperformance in both in-distribution and out-of-distribution settings. The approach demonstrates generalization and performance over existing deep reinforcement learning algorithms across complex procedurally generated environments.

### Strengths
•	Originality: The concept of fractures to find recurring patterns is innovative for hierarchical reinforcement learning. This paper proposes a method to cluster and select fractures, as well as a framework to utilize fractures in hierarchical reinforcement learning.

•	Quality: The paper effectively uses descriptive language and figures to illustrate core concepts.

•	Significance: The proposed method is shown to outperform several baselines.

### Weaknesses
1.	The Grid-world environments used in the experiments are limited in variety where all tasks are navigation across rooms. While Procgen environments were also tested, some details are lacking, such as the result of each environment, and the result of FraCOs in Figure 6 (also see question 5). In addition, I suggest that more baselines work on Procgen should also be compared (e.g. PPG[1]).

2.	In Section 4.1 and Figure 2, fractures are visualized with distinct clusters in 2D. I wonder if clusters in other tasks are as clearly separated as in this example, especially since the clustering approach is unsupervised and does not consider semantics.

3.	Based on the concern in question 2, I wonder about the reliability of using UMAP and HDBSCAN for clustering fractures. In Section 4.2, you state that fracture clusters are based on behavioral similarity, and you use an unsupervised approach to identify them. However,  Section 4.1 has provided a mathematical definition of fractures. It is unclear whether the identified clusters consistently align with this definition. Do you compare it with other clustering methods? Please clarify the methods further and provide additional analysis of the clustering results.

4.	The definition of usefulness (normalized sum) lacks explanation, with no supporting experiments or rationale for this decision. Would the proportion of each factor affect the result? Is there any ablation study to demonstrate the impact of each component?

5.	The FraCOs results without SSR are unconvincing, and Figure 6 does not even include FraCOs without SSR. SSR assumes shared convolutional layers encode the state, which is a strong assumption. The results would be more convincing with a clearer explanation of why SSR are applied to FraCOs in this part, including assumption and an analysis of its impact on the results. Providing the complete result on Procgen would also be helpful.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
3
