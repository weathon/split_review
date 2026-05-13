# Bayes Adaptive Monte Carlo Tree Search for Offline Model-based Reinforcement Learning

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Offline reinforcement learning (RL) is a powerful approach for data-driven decision-making and control. Compared to model-free methods, offline model-based reinforcement learning (MBRL) explicitly learns world models from a static dataset and uses them as surrogate simulators, improving the data efficiency and enabling the learned policy to potentially generalize beyond the dataset support. However, there could be various MDPs that behave identically on the offline dataset and so dealing with the uncertainty about the true MDP can be challenging.  In this paper, we propose modeling offline MBRL as a Bayes Adaptive Markov Decision Process (BAMDP), which is a principled framework for addressing model uncertainty. We further introduce a novel Bayes Adaptive Monte-Carlo planning algorithm capable of solving BAMDPs in continuous state and action spaces with stochastic transitions. This planning process is based on Monte Carlo Tree Search and can be integrated into offline MBRL as a policy improvement operator in policy iteration. Our ``RL + Search" framework follows in the footsteps of superhuman AIs like AlphaZero, improving on current offline MBRL methods by incorporating more computation input. The proposed algorithm significantly outperforms state-of-the-art model-based and model-free offline RL methods on twelve D4RL MuJoCo benchmark tasks and three target tracking tasks in a challenging, stochastic tokamak control simulator.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper propose to use a Bayesian adaptive method to train the model instead of end to end training approach used by MuZero. As indicate by the authors, this can modify the difficulty of model training in complex scenarios like continuous action space. Specifically, the method can be described in three main designs:1) it adapts DPW to handle continuous action and state spaces. 2) it use BA to refine the model during interactions and search process 3) It adapts MuZero’s supervised way to perform policy improvement. The experiment section shows methods using BA generally have a better performance than baselines, but the advantage of certain design seems not significant.

### Strengths
1. The authors describe the entire method in a clear way using pseudocode in Algorithms 1 and 2, and the insight of separating the model training from end-to-end process is explained in experiment section by comparing to sampled EfficientZero (sez). 
2. The experimental results indicate the effectiveness of the BA model training. Although the effectiveness of certain designs like MCTS search and supervised policy learning is not significant according to Table 1, I am glad to see the authors report the results honestly.

### Weaknesses
1. It seems the main improvement comes from BA model training according to Table 1. Thus, I wonder if there are other model-based RL methods using BA and deep ensembles to train the models, and why the authors did not include them in the baseline.
2. In my opinion, the BA process adjust the belief of the models according to the sample results of current belief instead of the interaction with true environment, which may lead to accumulated error. For example, if the belief mistakenly concentrates on a wrong model and the sample results are likely to come from the wrong model, then future belief are likely to be more inclined to this wrong model. Could the authors provide some insights that why this not happen according to the experiment results?

### Questions
1. I am not sure about the necessity of adjusting the belief not only in the acting process but also in the searching process. Could the author explain the different influences of adjusting the model at the two stages?
2. The authors indicate that sez does not work well due to the difficulty of end to end model training, but sez also use a different way of choosing actions nodes from DPW. Can the authors explain why they do not consider it as a main factor?
3. I am curious about why the authors choose to update the policy in a trajectory way. MuZero just sample a series of transitions from the buffer, which can avoid the interaction in learned models. Could the authors explain the reason behind this design?

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
This paper addresses model uncertainty in offline MBRL by framing it as a BAMDP, allowing for adaptive belief updates over multiple potential world models. The authors propose a novel continuous MCTS method to solve BAMDPs in continuous and stochastic settings, integrating this planning approach as a policy improvement step in a policy iteration framework. The approach, which combines Bayesian RL with search, is shown to improve performance across a range of continuous control tasks.

### Strengths
* Practical MCTS implementation for offline MBRL formulated as BAMDP: the paper introduces a practical implementation of the MCTS algorithm specifically adapted for continuous control tasks under the BAMDP framework. Though a straightforward approach, this integration is effective and brings continuous MCTS to offline MBRL with clear potential.

* Well-executed ablative studies: the paper provides ablation studies that dissect the individual contributions of the algorithm’s components, demonstrating the benefits of the BAMDP formulation, MCTS planning, and the search-guided policy learning approach.

### Weaknesses
 * Insufficient discussion of related work in Bayesian RL and offline MBRL: the related work section could better connect with existing research on modeling offline RL as a Bayes Adaptive MDP or epistemic POMDP. Ghosh et al. (2022) introduced a model-free approach to handling model uncertainty by training offline RL policies to adapt to belief changes, while Dorfman et al. (2021) framed offline meta-RL as a Bayesian RL problem, leveraging a belief-augmented MDP. Discussing these connections would position the current work more clearly within the broader landscape of Bayesian treatments of offline RL.

* Lack of connection to prior policy learning with model-based search: using model-based search outcomes for policy learning within an actor-critic framework was introduced by Feinberg et al. (2018) and later applied to offline MBRL in Jeong et al. (2023). Although these methods do not use MCTS for rollouts, they share the concept of leveraging generated trajectories to improve action-value estimation for policy learning. Discussing these earlier works would clarify the paper’s contributions in relation to prior approaches.

* Clarity issues in the experiment section: the structure of the experiment section could be improved to clarify the main research questions and key takeaways. At present, the content lacks focus on specific questions, making it challenging to follow the significance of each result. Organizing the discussion around clearly defined research questions could improve readability and focus.

* Omission of recent offline MBRL baselines: the empirical evaluations rely on older methods (e.g., MOPO and MOReL), making it difficult to assess claims about state-of-the-art performance. Comparisons with more recent baselines, such as RAMBO (Rigter et al., 2022), MAPLE (Chen et al., 2021), and CBOP (Jeong et al., 2023), would strengthen the experimental claims and provide a more comprehensive evaluation of the proposed method’s effectiveness.

### Questions
* Belief updates during training: are the beliefs updated using imaginary rollouts sampled from the model ensemble? If so, could this introduce systematic biases? The paper mentions applying a reward penalty within a pessimistic MDP framework, but it would be useful to assess whether this is sufficient for accurate belief updates under the BAMDP setup.

* Representation of returned policy in Algorithm 1: how is the policy $\pi_{\mathrm{ret}}$, returned by the SEARCH procedure, represented in practice? Further details would clarify its applicability to real-time policy learning.

* Clarification on state representation: footnote 5 states that the policy takes the states consisting of both $s$ and $h$, but line 416 describes differently. Could the authors clarify this discrepancy? Additionally, MAPLE (Chen et al., 2021) employs an RNN-based policy network, which aligns well with the BAMDP framework. Using MAPLE as a baseline could enhance consistency with the proposed architecture.

### Soundness
3

### Presentation
2

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
This paper models offline model-based reinforcement learning as a Bayes Adaptive MDP, which enables the agent to leverage the model uncertainty during learning. By using MCTS with double progressive widening, the agent achieves good performance on the D4RL benchmark and three target-tracking tasks.

### Strengths
The paper investigates a promising direction of leveraging the Bayesian RL framework combined with MCTS in offline RL. The paper is well-motivated and the performance on the D4RL benchmark outperforms baselines.

### Weaknesses
Experiments:
- A more thorough analysis of the proposed method's performance is necessary. The observed performance improvement appears to result primarily from two factors: (1) the use of BAMDP, and (2) planning with MCTS. To verify this, it would be helpful to see an experiment where only BAMDP is applied, keeping other elements unchanged. While the BA-MBRL variant seems intended to isolate the effects of BAMDP, the paper does not clearly explain how this differs from other models like MOPO or MoReL. For instance, it’s unclear if the performance gap is solely due to BAMDP. Specifically, it is not clear if the ensemble is trained with the same data and hyperparameters as the other baselines, and whether the belief update mechanism is the only difference. Additionally, tracking the evolution of $b(\theta)$ during updates would strengthen the claims about the role of BAMDP.
- A comparison of runtime across methods would be valuable, especially to understand the impact of using BAMDP and MCTS on computational efficiency. Providing runtime metrics could help illustrate any trade-offs between performance gains and computational cost. (The paper only reports the runtime of Sampled EfficientZero.) It would be beneficial to see a breakdown of the computational cost for each component of the proposed method, such as the model training, the belief update, and the MCTS planning.
- The inclusion of Figure 1 is somewhat ambiguous. The authors seem to suggest that the proposed method outperforms Sampled EfficientZero. However, a more detailed analysis is needed. For example, what factors contribute to the performance difference with BA-MCTS-SL? Is the advantage primarily due to using the Bayesian RL framework? It is unclear if the performance difference is statistically significant or if it is consistent across different environments and random seeds. A more rigorous statistical analysis is needed to support the claims.
-  In Line 472, the paper states, "both Sampled EfficientZero and BA-MCTS-SL rely on supervised learning... Thus, purely mimicking the search result may be less sample-efficient than policy gradient methods." However, in Line 406, "BA-MCTS-SL performs similarly to MA-MCTS, validating the effectiveness of both policy update mechanisms." This conclusion seems inconsistent. It is not clear how the supervised learning is implemented in BA-MCTS-SL and how it differs from the policy gradient methods. The paper needs to clarify the specific learning algorithms used in each method.

Writing: 
- Notation: what is hars'. It appears many times but I haven't found the definition. For example, in Algorithm1, the inputs of SIMULATE are defined as ($s, h$), $b(\theta)$, $d$ (Line 225), while in Line 231, the inputs of SIMULATE are $(s', hars'), b', d-1$. The paper needs to provide a clear definition of $hars'$ and its relationship with $h$.
- The update of $b(\theta)$ in Eq 4. should be clarifed. It is not clear how the likelihood $P_{\theta}^{i}(s' | s, a) R_{\theta}^i(r | s, a)$ is computed and how it is used to update the belief $b(\theta)$. The paper needs to provide more details on the implementation of the Bayesian update.
- The figures should be added via PDF or SVG, otherwise, the figure can be blurry.

### Questions
See weaknesses above.

### Soundness
3

### Presentation
2

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
Model-based offline reinforcement learning is a promising approach to improve the data efficiency and the generalization capability beyond the training dataset. To address the uncertainty issue when fitting the model with a static dataset, the conventional approach is to use an ensemble of world models, from which the uncertainty can be estimated. This work focuses on the adaptive ensemble mechanism where the belief over each model in the ensemble will be updated when the new samples are experienced by the algorithms. The proposed Bayes Adaptive Monte-Carlo planning algorithm has two key contributions: cast the offline MBRL as Bayes Adaptive MDP (BAMDP), based on which a Monte Carlo tree search method is used for planning. The experiments on D4RL MuJoCo and the three target tracking tasks show that the proposed method has better performance compared with state-of-the-art model-based and model-free offline RL methods.

### Strengths
- Experiments. This work considers both the D4RL MuJoCo and challenging stochastic target tracking tasks. The experiments also include an ablation study where each component of the proposed algorithms is verified, i.e., BA-MBRL, BA-MCTS, BA-MCTS-SL. The results are compared with many SOTA methods such as COMBO, MoReL, MOPO.
- Problem Formulation. I find the adaptive ensemble mechanism is indeed a crucial problem in the ensemble-based method, and the proposed method using the BAMDP as a backbone to address this issue is novel. The algorithms are well-motivated.  I do believe that this paper has good contribution on the offline model based RL community.

### Weaknesses
 - The comparison with related work is unclear. In particular, MuZero is a major  comparison object to motivate this study, while the statement in the paper is not clear. In Section 3, the paper claims that MuZero does not apply uncertainty estimation of the learned model, which has no direct relation with using latent models (i.e., estimating uncertainty in the latent space is possible). Please provide a more structured comparison of key related works to highlight the specific gaps. The current discussion lacks a detailed analysis of how the proposed method differs from MuZero in terms of model learning, uncertainty handling, and planning mechanisms. Specifically, the paper should clarify whether MuZero's latent space model inherently prevents uncertainty estimation or if the method simply chooses not to implement it, and how this contrasts with the proposed approach.
- Method section is confusing. Section 4.1 titled “ key role of deep ensemble,” while the contents are more about introducing BAMDP and reward design to incorporate the pessimistic-MDP. In Section 4.2, the newly introduced $(s,h)$ as a decision point seems out of nowhere, what is the connection with $(s,b)$ as introduced in BAMDP? The introduction of the algorithm in Section 4.2 is very hard to follow, and a paragraph title can help a lot. For instance, in the last paragraph where introducing the Bayes-optimal policy,  the author should directly introduce the design choice and then compare it with the previous methods. The connection between the theoretical BAMDP framework and the practical implementation using deep ensembles is not clearly articulated. The paper needs to explicitly state how the belief $b(\theta)$ is represented and updated in the deep ensemble context, and how this relates to the history $h$. The introduction of $(s,h)$ as a decision point requires more context and a clear explanation of its role in the overall algorithm.
- Lack of comparison of the uncertainty evaluation. One of the key motivations of the proposed method is to use the samples to update the belief of ensembles. In the experiments, the related results on the benefits of such adaptation for ensemble-based methods are lacking (e.g., set the adaptive parameter to be zero). The paper should include experiments that isolate the impact of the adaptive belief mechanism. A comparison with a non-adaptive ensemble method, where the belief is not updated, would provide crucial insights into the effectiveness of the proposed approach. Furthermore, the paper should demonstrate how the belief adaptation improves the accuracy of model predictions and reduces uncertainty in the planning process.

### Questions
- what is the major purpose of having Fig.1? 
- What is the explanation of the lack of the convergence in Figure 2 for optimized method? Why in the last subfigure all the curves seem to struggle  to converge?
- How to select $\lambda$ in the reward and the number of the ensembles in practice?

### Soundness
3

### Presentation
1

### Contribution
2
