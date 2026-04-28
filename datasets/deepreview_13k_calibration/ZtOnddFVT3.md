# Self-Alignment for Offline Safe Reinforcement Learning

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 5, 6

## Abstract
Deploying an offline reinforcement learning (RL) agent into a downstream task is challenging and faces unpredictable transitions due to the distribution shift between the offline RL dataset and the real environment. To solve the distribution shift problem, some prior works aiming to learn a well-performing and safer agent have employed conservative or safe RL methods in the offline setting. However, the above methods require a process of retraining from scratch or fine-tuning to satisfy the desired criteria for performance and safety. In this work, we propose a Lyapunov conditioned self-alignment method for a transformer-based world model , which does not require retraining and conducts the test-time adaptation for the desired criteria. We show that a transformer-based world model can be described as a model-based hierarchical RL. As a result, we can combine hierarchical RL and our in-context learning for self-alignment in transformers. The proposed self-alignment framework aims to make the agent safe by self-instructing with the Lyapunov condition. In experiments, we demonstrate that our self-alignment algorithm outperforms safe RL methods in continuous control and safe RL benchmark environments in terms of return, costs, and failure rate.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The author's present a method for self-alignment of offline transformer RL policies using Lyapunov Density Models. The method is an inference-time procedure for online transfer of an offline-trained policy. The algorithm assumes a trained decision transformer architecture, modified to also predict next state and to include a VAE, so that it can be used to generate imagined trajectories at test time. At inference time, this modified DT is used to rollout imagined trajectories conditioned on the current state. The imagined trajectories are then evaluated based on the Lyapunov stability condition and the least violating trajectory is selected. This trajectory is then used as a prompt to the DT model in order to produce a prompt-conditioned action to be executed in the environment. The author test their method on several Safety-Gym and Mujoco environments and compare to vanilla decision transformer and previous Safe RL methods

### Strengths
- The motivation for this work is  strong - being able to train policies entirely offline that are then able to be deployed with safety guarantees in the real environment would signigifcantly advance the applicability of RL to real-world scenarios
- The novelty is good - this is a new method which combines DT with Lyapunov conditioning
- The authors compare against many baseline methods on several different tasks

### Weaknesses
Major issues:
- I find several parts of the method hard to follow:
   - The training procedure for the DT+VAE model is not provided. It's unclear how the VAE is trained in conjunction with the Decision Transformer, specifically what loss function is used to train the VAE decoder and how this loss is combined with the DT loss. Furthermore, the specific architecture of the VAE is not described, making it difficult to reproduce the results.
   - on line 245-256 the authors mention "sampling policies" but I do not see where policies are sampled in Alg. 1. The algorithm appears to generate trajectories, but it's not clear how these relate to specific policies, and how these policies are parameterized or sampled from a distribution. The connection between the imagined trajectories and the concept of sampling policies needs clarification.
  - It is not clear how the results in Section 4 are used in Alg. 1. Specifically, the derivation of the control invariant set and the threshold $D$ in Section 4 do not seem to be directly used in the algorithm. The connection between the theoretical results and the practical implementation is missing.
  - It is not clear how the maximization in equation 8 is performed. This seems to correspond to the two loops in Alg 1, but does this mean that U and V are maximized individually? The algorithm description does not explicitly state how the maximization is performed, and whether it is a joint or sequential optimization. The relationship between the two loops and the maximization of U and V needs to be clarified.
  - What do $\theta$ and $\psi$ correspond to in the architecture? These are described as parameters of high and low level policies, but there only seems to be one transformer model in the archtiecture. It's not clear how these parameters are separated within the single transformer architecture, and how they are used to represent distinct high and low-level policies. The mapping of these parameters to the model needs to be explicitly defined.
- I am concerned about the rigor of the theoretical results:
   - Theorem 4.1 "The problem of finding a trajectory from Lyapunov stable controller is equivalent to solve the following
inference problem" refers to a proof in D2, but the proof ends with "Then, the maximizing the above equation implies that the trajectory get close to the Lyapunov condition". First this claim is not proven but also it doesn't match the claim of 4.1 (equivalence). The proof provided does not establish an equivalence, but rather a correlation, and the logical steps to arrive at the conclusion are not clear. The proof needs to be more rigorous and explicitly demonstrate the equivalence.
  - Theorem 4.3 - The proof in the appdenix is only two lines and starts with an equation that needs greater explanation. The proof is too brief and lacks the necessary detail to be convincing. The initial equation needs to be justified and the steps to reach the final conclusion need to be clearly explained.
- The experimental results lack statistical analysis and hence are not convincing. The results presented in Tables 1 & 2 are very hard to read and do not present a robust statistical analysis. No confidence intervals are included and in many cases it appears that the proposed method only improves over the baseline by very slight margins. Without confidence intervals, it is impossible to say if these results show a statistically significant improvement. Moreover, the experiments were only conducted over thee seeds which is quite small. Additional, in Fig 3. The unsafe regions do not appear to align particularly well with the hazards. The unsafe regions should at least cover the hazards, but this is not the case in many instances, raising questions about the method's ability to identify unsafe regions.
- The connection between this method and Safe RL does not feel substantive, since this is primarily a method of constraining an offline policy to the data distribution (which many Offline RL algorithms seek to do). The entire section 4 seems to primarily serve to motivate the threshold for the target control invariant set, however it introduces a margin hyperparameter D which essentially makes the threshold a tunable parameter. Is the derivation in Sec 4 necessary? Also, I do not see in Algorithm 1 where this threshold is used, and there is no discussion of how the hyperparameter D is chosen. The introduction of the hyperparameter D and its lack of direct use in the algorithm raises questions about the necessity of the derivation in Section 4. The connection to Safe RL is weak, as the method primarily focuses on staying within the data distribution, which is a common goal in offline RL, rather than explicitly addressing safety constraints.
- Again regarding the connection to Safe RL - the authors primarily compare their method to Offline Safe RL algorithms, but this does not necessarily seem like the best baselines, since these methods also use the cost in the offline dataset directly to train the algorithm, while this method does not. Would it not make more sense to compare to other offline methods that seek to constrain the policy within-distribution like CQL? A critical difference between the safe RL methods and the conservative RL methods is that Safe RL methods could avoid constraints even if the expert data is sub-optimal, wheres the conservative methods would rely on an assumption that the training data itself is mostly safe and hence staying in distribution results in safety. The comparison to offline safe RL algorithms is not ideal, as these methods use cost information directly during training, while the proposed method does not. Comparing to methods like CQL, which also aim to constrain the policy within the data distribution, would be more appropriate.


Minor issues:
- Citation for Def 3.1
- Several acronyms and variables are not defined, eg.:
   - Eq. 2 $B^c$ doesn’t seem to be defined
   - CDT is only cited in the Appendix but referenced many times in the main text - no where in the text is a description of the method provided.
- There are many very long paragraphs that combine multiple ideas that should be split. For example on the last page, third to last paragraph.
- There are several grammatical errors

### Questions
- Decision transformer is reward conditioned - how is the reward conditioning handled in your method?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors present a simple model-based RL method with a transformer and a world model, and propose a Lyapunov-conditioned self-alignment method, which does not require retraining and conducts the test-time adaptation for the desired criteria.

### Strengths
The idea of prompting a world model using self-generated trajectories is interesting and promising. Experimental results also show that the idea indeed improves the agent's test-time performance in some tasks.

### Weaknesses
1. The writing needs to be polished further.

2. Please use the correct citing format.

3. The Lyapunov condition does not seem to be the main contribution of this work, but the authors use a large part of the content to describe it, which misleads readers to correctly judge the novelty of this work.

4. It is unclear what connection between the proposed Self-Alignment and the original Self-Alignment that is used in LLMs is.

5. While the results show the effectiveness of SAS, experiments are conducted in several relatively easy safe RL benchmarks.

### Questions
It is better to shorten the method section and highlight the main contribution of your work.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The author present a self-alignment technique by self-generated prompt to guarantee the better safety. The self-generated prompt for safety is based on Lyapunov condition.  To implement selfalignment for safety, author present a novel formulation of Lyapunov condition as a probabilistic inference  and transformer-based RL world model as a model-based hierarchical RL agent, respectively, to  provide in-context learning based self-alignment.

### Strengths
In this work, the author presents a simple model-based RL method with a transformer and a world model and proposes a Lyapunov-conditioned self-alignment method, which does not require retraining and conducts the test-time adaptation for the desired criteria. The author shows that the model-based RL with the transformer architecture can be described as a model-based hierarchical RL. As a result,  the author can combine hierarchical RL and in-context learning for self-alignment in transformers. The proposed self-alignment framework aims to make the agent safe by self-instructing with the Lyapunov condition. In experiments,  the author demonstrates that the self-alignment algorithm outperforms safe RL methods in continuous control and safe RL benchmark environments in terms of return, costs,  and failure rate.
This paper is largely well-organized and clear in its presentation.

### Weaknesses
The paper introduces the SAS framework, which is built on promising theoretical foundations. However, its evaluation of practical applicability is somewhat limited. For instance, in Figure 3, the experiments focus solely on benchmarking environments like Safety Gymnasium and Mujoco. While these environments are commonly used, they do not fully capture the complexity and uncertainty of real-world scenarios. Specific scenarios such as autonomous driving simulations, dynamic obstacle avoidance in robotic systems, or high-variability logistics tasks (where demand changes unexpectedly) would offer greater insight.

Additionally, the paper does not provide information on the computational cost of this framework, particularly regarding how it scales with more complex environments or higher-dimensional tasks.  The SAS framework relies on self-generated prompts based on existing data, but the paper fails to discuss how well SAS adapts to environments that experience unexpected changes or previously unseen safety hazards.

### Questions
1. Could the authors elaborate on how SAS may generalize compared to non-Lyapunov methods? 
2. Additionally, could the authors provide specific metrics on computational costs, such as training time, inference time, or memory usage, and how these scale with environment complexity or dimensionality?
3. Lastly, do the authors discuss or demonstrate how SAS performs in scenarios with distribution shifts or novel hazards not present in the training data?

### Soundness
3

### Presentation
3

### Contribution
2
