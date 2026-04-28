# Reinforced In-Context Black-Box Optimization

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 3, 8, 3

## Abstract
Black-Box Optimization (BBO) has found successful applications in many fields of science and engineering. Recently, there has been a growing interest in meta-learning particular components of BBO algorithms to speed up optimization and get rid of tedious hand-crafted heuristics. As an extension, learning the entire algorithm from data requires the least labor from experts and can provide the most flexibility. In this paper, we propose RIBBO, a method to reinforce-learn a BBO algorithm from offline data in an end-to-end fashion. RIBBO employs expressive sequence models to learn the optimization histories produced by multiple behavior algorithms and tasks, leveraging the in-context learning ability of large models to extract task information and make decisions accordingly. Central to our method is to augment the optimization histories with \textit{regret-to-go} tokens, which are designed to represent the performance of an algorithm based on cumulative regret over the future part of the histories. The integration of regret-to-go tokens enables RIBBO to automatically generate sequences of query points that satisfy the user-desired regret, which is verified by its universally good empirical performance on diverse problems, including BBO benchmark functions, hyper-parameter optimization and robot control problems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper is about learning a black-box optimization algorithm in an end-to-end fashion. In terms of meta learning, this approach falls in the category of "meta-learning the entire algorithm". The reason for doing this is that it is more flexible than learning something that replaces heuristics in an existing black-box optimization algorithm.  The approach proposed in this paper builds on a large sequence model (causal transformer). The goal is that this model can learn from the sequential behavior of many BBO algorithms on many tasks for making decisions. The supervision signal in this learning task is the regret-to-go which captures the performance of the optimization algorithm. The training regime is offline and the training sequences consist of query points and function values. During the test phase, the model is used in an autoregressive way to generate new query points. Experiments are performed on synthetic functions / data and robotic control problems. The proposed method is compared to state-of-the-art baselines.

### Strengths
The paper is well-written and clear. The presentation is easy to follow and the claims and contributions are clearly stated. The method is novel and performs better than state-of-the-art approaches on the selected experiments.

### Weaknesses
The main weakness of this method is the fact that it has to transfer or generalize to new optimization problems, while algorithmic optimizers have to be tuned to new optimization problems. It is hard to judge how much training is needed for this method to perform well on any "similar" problem.

### Questions
In practice, it is also possible to just run the algorithmic optimizer longer to get better solutions and it would be interesting if this is also true for this approach. 

Some algorithmic optimizers use local approximations of the objective functions to estimate higher order informations (e.g., gradients) would this be useful for this approach or does this already happen inside of the learned model?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a method to solve black-box optimization (BBO) problems end-to-end, using a "decision transformer"-like approach.
This involves learning a transformer that given a context of query-observation pairs and regret-to-go tokens, selects the next query. This appears to learn from offline meta-training, how to build a model and use this model to make sequential decisions.

### Strengths
The BBO problem is a very relevant problem. Given that BBO can be framed as a special case of RL (where the state is kept constant), applying a decision transformer (DT) (or something similar) to this problem seems like an interesting approach.

### Weaknesses
I see some weaknesses both in the proposed method (and how it differs from DT), and the experimental evaluation.

Methodology:

* In my opinion, the manuscript would benefit from a more careful distinction from decision transformers, especially, since the BBO setting is a special case of the standard RL setting (where the state is constant). Why do the authors use regret-to-go tokens as opposed to returns-to-go in DT? In DT, no "observation tokens" are added to the sequence, and instead returns (i.e., function "observations") are subtracted from the RTG. Furthermore, I would like to see a comparison against DT as a baseline in the experiments. From the current paper, it does not become evident why RIBBO would be preferable over DT. Specifically, the use of regret-to-go tokens, which require knowledge of the optimal value, is a significant departure from the standard return-to-go used in DT, and the paper does not sufficiently justify this choice, nor does it explore the implications of this change on the method's performance and applicability.

* The assumption that the "true" optimum value $y^*$ is known seems off to me. How would this value be known in practice, e.g., for a molecular design task? Other BBO algorithms such as UCB/EI/... do not require knowledge of $y^*$, and instead effectively balance exploration & exploitation. This seems like a fundamental assumption of the proposed approach, and to my understanding is why regret-to-go tokens might not be so practical (DT uses return-to-go tokens which do not have this problem). The paper should more clearly acknowledge that this assumption limits the applicability of the method to scenarios where the optimum is known or can be accurately estimated, which is not always the case in real-world BBO problems.

* Setting $R_t = 0$ before choosing the next action suggests to me that the acquisition function is executed in the "exploitation regime". That is, in the meta-training set, I would assume that actions from algorithms that follow $R_t = 0$ are most likely from a stage where the optimum has already been almost perfectly determined, and the BBO algorithm purely exploits the model (i.e., does not focus on further exploration). Perhaps "knowing" the true $y^*$ a priori can compensate for this lack of exploration, but I would assume that this does not work in challenging exploration tasks where $y^*$ is unknown a priori. Can the authors elaborate why they expect setting $R_t = 0$ would lead to explorative behavior? The paper does not provide a clear explanation of how setting $R_t = 0$ encourages exploration, particularly when the model is trained on data where such a setting typically indicates exploitation. This raises concerns about the method's ability to handle scenarios where exploration is crucial.

Experimental evaluation:

* It is not clear to me why "imitating" a BBO algorithm (like UCB, EI, ...) with a transformer is preferable over optimizing said algorithm directly. The "imitation" setting seems more applicable to cases where we want to imitate decisions of a "human expert" that cannot be expressed in closed-form, as is done in BC. This paper seems to claim that the main reason for learning a transformer is that this can leverage meta-training data to select the right BBO algorithm on the fly, however, in my view the experiments are insufficient to support this claim. This is because (1) the experiments do not compare against any other ad-hoc method of choosing BBO algorithms on the fly based on their performance on similar tasks in a meta-training set (this would not require re-learning the BBO algorithm, just learning when to apply which one), and (2) the experiments do not appear to compare against baselines that also use the meta-training set. In other words, I believe that the experiments are heavily skewed in RIBBO's favor since RIBBO uses a meta-training set while most BBO baselines have not seen this extra data. It might be that RIBBO exploits additional patterns in the meta-training set beyond just imitating one of the BBO algorithms. In my view, the experiments should compare against BBO algorithms that operate over meta-learned models which incorporate knowledge from the meta-training set. See, for example, [1]. In my opinion, convincing experiments would have to evaluate against such approaches that meta-learn individual components. The paper needs to provide a more compelling justification for why an imitation learning approach is superior to directly optimizing BBO algorithms, especially when considering the potential for meta-learning in both approaches.

* It seems to me that the most important results are in Appendix D where the authors test RIBBO in scenarios where the same function family are not included in the offline meta training set. In the results from the main test, RIBBO might make extensive use of offline information that is not available to most of the tested baselines (for example, GP-EI). It seems that in Appendix D, RIBBO is frequently outperformed by GP-EI. Can the authors elaborate on why that could be? This seems concerning to me. The paper should discuss the limitations of the method when generalizing to unseen function families, and the fact that RIBBO's performance can degrade significantly in such scenarios, as evidenced by the results in Appendix D.

### Questions
* I would suggest that before Eq. (2) it is highlighted that this is the standard behavioral cloning baseline.

* Can't the proposed HRR also lead to OOD RTGs, in case the $R_t \gg 0$ when no similar data was seen before in the meta-training set? That is, if the tasks encountered are more difficult than the tasks in the meta-train set.

* What is the size of $M$ and $T$ in the experiments? Do the results look different with smaller meta training sets? What are the minimal values where RIBBO starts to outperform basic BBO algorithms (that do not use the meta training data)?

* In Figures 3b,3c,3d, why were the specific functions chosen / "cherry-picked" for this visualization? Can you add the visualizations with the other test-functions to the supplementary material?

* In multiple places (for example, line 534), the authors claim that RIBBO can be used to generate optimization trajectories satisfying a user-specified regret. This claim does not seem to be sufficiently supported by the experiments. The experiments do indicate that there is a correlation between the user-specified regret and the obtained regret, but even in Figure 3c, the mean regret when a user specified regret $10$ is significantly larger than $10$.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Black-Box Optimization (BBO) is the process of optimizing an objective function where neither analytic expression nor derivatives of the objective function are available. Although Bayesian Optimization (BO) and Evolutionary Algorithms (EA) are the main BBO algorithms developed, they solve BBO problems from scratch while relying on expert-derived heuristics. Recently, the meta-learning paradigm has been adopted to learn some components of the algorithms from previously collected data, yet it requires a degree of expert knowledge. On the contrary, learning the entire BBO algorithm in an End-to-End (E2E) fashion from data requires no expert knowledge at all while providing flexibility among a wide range of BBO problems. However, learning such algorithms is challenging, and in practice, selecting the specific BBO algorithm is needed during inference (as in OptFormer [1]). In this work, an approach named Reinforced In-context BBO (RIBBO) is proposed to learn a general BBO algorithm from offline data collected using multiple BBO algorithms. Using a causal transformer, RIBBO can predict the next query point, given the optimization history. To alleviate the need for expert knowledge during inference when selecting the desired BBO algorithm, RIBBO augments the optimization history with regret-to-go RTG tokens representing the future performance of an algorithm. Consequently, RIBBO can automatically identify different algorithms and generate sequences of query points that satisfy the specified regret. So, it adds an interpretable component that is easy to manipulate during inference. To update the RTG tokens during testing, this work proposes a novel Hindsight Regret Relabelling (HRR) strategy by setting the immediate RTG as 0. Finally, the potential of this approach has been demonstrated in three problem domains: BBOB synthetic functions, hyperparameter optimization, and robot control problems while comparing to classical approaches (that generated the offline dataset) and related baselines like Behavior Cloning (BC) and OptFormer [1].

[1] Chen, Yutian, et al. "Towards learning universal hyperparameter optimizers with transformers." Advances in Neural Information Processing Systems 35 (2022): 32053-32068.

### Strengths
- The paper is well-written and clear.
- The literature is covered nicely in addition to motivating the proposed approach of learning the BBO algorithm in an E2E fashion. 
- The experiments and the baselines demonstrate the potential of the proposed approach.
- The discussion section and ablation studies are comprehensive to understand the impact of each component in the algorithm.

### Weaknesses
 There are no significant weaknesses in this work, yet some important comments should be mentioned to improve this work.
- The limitation of this approach is not well highlighted.
- The quality of plots can be improved. I personally don't like the overlapping vertical lines that represent the standard deviation. A shaded region could be better.

### Questions
- What are the major limitations of this approach? 
- During inference, as a user, how can I select the initial RTG? Could you please provide examples where a low or a high initial RTG value is preferred? I believe I didn't get this part well.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a meta-learning algorithm designed for black-box optimization (BBO) problems, which are often derivative-free and lack a gradient signal. The proposed method uses an offline dataset collected from behavioral optimization algorithms, each of which generates sequences of optimization steps across various problems. The algorithm then trains a sequence-to-sequence model based on the Transformer architecture to replicate these sequences, aiming to generalize effectively and produce a high-quality optimization sequence when applied to new problems sampled from the training problem distribution.

In a typical optimization sequence, each step includes a pair of values, (x_i, y_i), where x and y represent the input and output of the BBO problem, respectively. The authors propose enhancing this dataset by adding a Regret-To-Go (RTG) scalar, represented as (x_i, y_i, r_i), where r_i is the sum of future regrets for t > i. This paper distinguishes between Behavioral Cloning (BC), which learns without RTG, and RIBBO, which incorporates RTG into the model training.

The authors test their algorithm across three datasets: (1) BBOB, a collection of synthetic optimization problems grouped by shared characteristics; (2) HPO-B, a set of machine learning hyperparameter optimization problems targeting base models such as XGBoost and SVM; and (3) Rover trajectory planning, where the goal is to optimize a sequence of 30 two-dimensional points that minimize a cost function. The algorithm is evaluated against other meta-learning BBO approaches, such as OptFormer and BC, as well as traditional BBO methods, including CMA-ES. RIBBO demonstrates strong performance, outperforming the alternatives in these experiments.

### Strengths
1. Data-Efficiency: 

RIBBO addresses a significant problem in BBO by learning from sequences of sub-optimal trials. This approach enables the algorithm to learn from incomplete or unsuccessful trials, potentially reducing computational costs.

2. Implementation and Training Simplicity: 

The method is relatively straightforward to implement and train, given the simplicity of the Transformer architecture and the offline training process.

### Weaknesses
1. Behavioral Policy Limitations:

The potential of RIBBO to outperform the behavioral policies it learns from is uncertain. Unlike reinforcement learning (RL), RIBBO lacks a policy optimization component; it merely learns to output the next query, x_i, based on past inputs, outputs, and RTG. This approach is essentially behavioral cloning that might favor sequences with lower regret if the RTG functions as intended. However, without optimizing the output sequences (e.g., by approximating the target output value, y, and deriving a gradient signal [1]), RIBBO’s ability to surpass the behavioral policies remains unclear. The method's reliance on imitation learning means it is fundamentally limited by the quality of the offline data. If the behavioral policies in the dataset are suboptimal, RIBBO may struggle to find significantly better solutions, especially in complex BBO landscapes. The paper does not provide a clear analysis of how the quality of the behavioral data affects the final performance of RIBBO.

2. Justification for RTG Inclusion:

The authors could strengthen their argument and visual representation of why RTG enhances solution quality. It is not evident why augmenting the input data with RTG would encourage the model to generate lower-regret sequences. Why is the network motivated to generate sequences of lower RTG? The paper lacks a clear explanation of the mechanism by which the RTG signal influences the model's decision-making process. While the authors claim that RTG guides the generation of subsequent sampled points, the exact way this happens is not well-defined. A more detailed analysis of how the model uses the RTG information to select better query points would be beneficial. It is not clear if the model is learning to predict the RTG itself or using it as a contextual cue for generating better sequences. 

3. Transferability Across BBO Problems:

Domains like RL or few-shot learning provide clear justifications for what knowledge can transfer across tasks, such as environment dynamics or domain distribution, respectively. However, in black-box problems, a shared generative function across tasks is not always present. Even in cases where tasks are sampled from a common distribution, such as in the same group in the BBOB testbench or the rover trajectory planning problem, RIBBO lacks an adaptation mechanism like MAML[2], which would help in adjusting to different environments. Consequently, the paper should address whether and why RIBBO is truly adaptable to unseen tasks. The paper does not discuss the potential for negative transfer, where learning from one set of BBO problems could hinder performance on a different set. The lack of an explicit adaptation mechanism raises concerns about the robustness of RIBBO when applied to BBO problems that are significantly different from those in the training data.

### Questions
1. BBOB Experiment Clarifications: 

In the BBOB experiments, what dimensions were selected, and what is the interpretation of the x-axis (number of evaluations)?

2. Hyperparameter Sensitivity: 

A primary motivation for RIBBO is to alleviate the challenge of manually tuning hyperparameters (lines 13–16 in the abstract). However, RIBBO itself requires hyperparameter tuning due to the nature of neural network training. Some of these parameters are listed in Table 1 (Appendix). How were these hyperparameters tuned, and could the authors provide sensitivity metrics to show their impact on performance?

3. Literature Review Addition: 

Opt-GAN [1] is another BBO method that aims to learn a global optimizer through a neural network, predicting the next candidate point based on previous points sampled in an off-policy fashion. It would be beneficial to include this work in the literature review.

References
1[] Lu, Minfang, et al. "OPT-GAN: a broad-spectrum global optimizer for black-box problems by learning distribution." Proceedings of the AAAI Conference on Artificial Intelligence, vol. 37, no. 10, 2023.

### Soundness
2

### Presentation
2

### Contribution
1
