# Residual-MPPI: Online Policy Customization for Continuous Control

- Decision: Accept
- Scores: 6, 5, 8, 6

## Abstract
Policies learned through Reinforcement Learning (RL) and Imitation Learning (IL) have demonstrated significant potential in achieving advanced performance in continuous control tasks. However, in real-world environments, it is often necessary to further customize a trained policy when there are additional requirements that were unforeseen during the original training phase. It is possible to fine-tune the policy to meet the new requirements, but this often requires collecting new data with the added requirements and access to the original training metric and policy parameters. In contrast, an online planning algorithm, if capable of meeting the additional requirements, can eliminate the necessity for extensive training phases and customize the policy without knowledge of the original training scheme or task. In this work, we propose a generic online planning algorithm for customizing continuous-control policies at the execution time which we call \textit{Residual-MPPI}. It is able to customize a given prior policy on new performance metrics in few-shot and even zero-shot online settings. Also, Residual-MPPI only requires access to the action distribution produced by the prior policy, without additional knowledge regarding the original task. Through our experiments, we demonstrate that the proposed Residual-MPPI algorithm can accomplish the few-shot/zero-shot online policy customization task effectively, including customizing the champion-level racing agent, Gran Turismo Sophy (GT Sophy) 1.0, in the challenging car racing scenario, Gran Turismo Sport (GTS) environment. Demo videos are available on our website: \url{https://sites.google

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Residual-MPPI, a method for online policy customization in continuous control tasks. Residual-MPPI enables immediate policy adaptation at execution time by utilizing only the action distribution of a pre-trained policy, without needing additional training data or detailed knowledge of the original policy. Experiments demonstrate its effectiveness in adapting the champion-level racing agent GT Sophy 1.0 to custom constraints within the challenging Gran Turismo Sport (GTS) simulator environment, as well as in the robotic MuJoCo environment.

### Strengths
- The paper is well-written and easy to follow.
- The methodology is novel and well-structured.
- The approach is validated in complex environments, including MuJoCo and GTS.

### Weaknesses
 - The paper lacks SOTA baselines for policy customization. For instance, methods like those in [1, 2] demonstrate few-shot adaptability to new environments without an additional parameter training phase. A comparison with such method would strengthen the evaluation.

 - The performance difference between Residual-MPPI and the comparison baseline, Greedy-MPPI, is not sufficiently analyzed. In Table 1, Residual-MPPI and Greedy-MPPI show very similar performance, yet the paper only briefly mentions on Line 430 that “Greedy-MPPI, as mentioned above, also leads to severe failure in complex GTS tasks” without further explanation. A more detailed analysis of Off-course Steps across different baselines would add clarity to the comparison.

### Questions
- I am curious about the performance difference caused by the inclusion of $\log \pi$. How does the trajectory change when the hyperparameter $\omega'$ is increased or decreased?
- When performing policy customization without a given reward, how can the proposed Residual-MPPI be applied if only expert data or instructions are provided instead?
- I am willing to raise the score if the authors respond to the weaknesses and questions.

### Soundness
3

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
3

### Summary
The paper studies the problem of online-fining pre-trained policies and proposes to combine the residual q learning and Model Predictive Path Integral (MPPI) together to form a new method, called Residual-MPPI, to address the problem. The paper provides a theoretical analysis of the proposed formulation and a comprehensive empirical evaluation of the method on Mujoco and GTS domains. The results are reported to be promising and the proposed method turns out to be effective.

### Strengths
* [Originality] The paper attempts to integrate the residual Q learning into the Model Predictive Path Integral (MPPI) and show some promising results of such attempt. 
* [Quality and clarity] The paper is well written, and the structure is good in general. It is good to see the empirical evaluation has been conducted on multiple different domains and a relatively thorough results are reported. 
* [Significance] The proposed method considers an important problem of adapting a policy to new setting, which can be very useful for RL to be applied to many real-world applications.

### Weaknesses
### [Empirical evaluation appears to be weak] 
1. The empirical performance of the proposed method, Residual-MPPI, is quite similar to the heuristic modification of MPPI, i.e., Greedy-MPPI. On the main metrics, Full-task and Add-on Task, the reported performance of Residual-MPPI is approximately the same as that of Greedy-MPPI. The paper pointed out one difference on Ant Full Task. But it is unclear how the total reward was computed here and why this total reward should matter more than the add-on reward, given that Greedy-MPPI yields higher rewards than Residual-MPPI on add-on task. So please **provide a more detailed analysis of the differences between Residual-MPPI and Greedy-MPPI, particularly in cases where their performance is similar**. Also please **clarify how the total reward is calculated and why it's considered more important than the add-on reward in certain cases, especially for the Ant Full Task**.

2. The baseline methods only cover some variants of MPPI. The paper only compared its proposed method with different variants of MPPI. However, as mentioned in the related work, there are many more baseline methods that had been discussed in contrast to the proposed method. So the paper should at least provide convincing argument that why these mentioned methods in related work should not be included as baselines. I think at least RL-driven MPPI, JSRL, and AWAC can be applied to the Mujoco environment to solve the online fine-tuning tasks. So please **include RL-driven MPPI, JSRL, and AWAC (if appropriate) to the baseline methods as they are discussed in the related work as important previous works**, or please **explain why these preivous methods in related work could not be included in the experiment**.

3. Some metrics adopted in the experiments are debatable. The paper adopted two metrics, add-on reward and basic task reward, as the main measures of the required performance. However, I’m not sure if I understand it correctly: should we always focus on the augmented reward (or the add-on reward) as the sole measure? Since this is the main objective in the policy customization. See my questions in the Question Section. 

4. Results on GT Sophy and sim-to-sim experiments seem to be incomplete. It’s good to see the paper evaluates the proposed method on GT Sophy and sim-to-sim domains. But the results are relatively incomplete (e.g., no quantitative results are reported for Full, Guided, Greedy and Valued variants of MPPI). Given that the Greedy-MPPI was reported to perform similarly to the proposed method, Residual-MPPI, it would be necessary to see how Greedy performs in other domains.  So please **provide quantitative results for the missing MPPI variants in the GT Sophy and sim-to-sim experiments**.

### [More clarifications and ablations are needed to understand the method]
In section 3.2, the paper introduced three main techniques to improve the learning of the transition dynamics function. However, the paper did not explicitly describe how these techniques are used in the method. At least, it’s not apparent to find them in the algorithm 1 (can’t find the multi-step error used as a loss function). Neither is clear about fine-tuning with online data. So please **provide a more detailed explanation of how the three techniques (multi-step error, exploration noise, and fine-tuning with online data) are integrated into the algorithm, possibly by updating Algorithm 1 or providing additional pseudocode.**

Further, there are no ablation studies on many design choices reported by the paper. Specifically,  it is not reported that how the above three techniques of learning the transition dynamics can affect the empirical performance of Residual-MPPI. Also, comparing Greedy-MPPI against Residual-MPPI, it can be hard to say it is necessary to include $\log\pi$ as a reward in Residual-MPPI since the two perform very similarly on HalfCheetah, Swimmer, and Hopper. 

### Clarity and the rigorousness 
Some sections lacks clarity. Section 3.2: DYNAMICS LEARNING AND FINE-TUNING appear to be disjoint to Section 3.1 since the proposed techniques in Section 3.2 cannot be found in Section 3.1 or the algorithm. Re Section 5.2.2, it is vague as to how the evaluation was conducted and what quantities had been compared against to draw the conclusions there.

### Questions
1.  In the experiment part, why the customised the policy need to maintain the same level of performance on the basic tasks? I understand that the full task is given by $wr+r_R$ and the add-on task is given by $r_R$. It makes sense to report results of customized polices on these two tasks. But what’s the motivation of comparing the results on task defined by $r$? since it is irrelevant to the customization objective. 
2. The paper formulated the policy customization as an augmented MDP, with the reward to be defined as $w’\log \pi(u|x) + r_R$. I’m wondering, in Table 1, the total reward refers to $ w’\log \pi(u|x) + r_R$ or $wr+r_R$? 
3. Re Theorem 1, I can’t understand why such theorem is needed? And what does it imply?

### Soundness
2

### Presentation
3

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
This work approaches the challenge of policy customization: given a prior policy (trained on a task, represented by a reward function), how should one adapt it at test-time to account for a different objective (add-on reward)? To tackle this problem, the paper introduces Residual-MPPI, which bridges Residual Q-Learning (an RL algorithm for policy customization) and MPPI (a planning method for model predictive control). The work firstly introduces a theoretical motivation for this mix of techniques (Section 3.1) and then provides experiments in continuous control tasks on MuJoCo and the GTS environment. Empirical results demonstrate Residual-MPPI is capable of adapting the policy with fewer samples than prior work, and not considerably compromising performance on the prior task.

### Strengths
- The work is well written and structured, easy to follow. The adopted motivation and proposed method are also clear;

- The evaluation setup is interesting: it brings MuJoCo benchmarks (which, although toy problems, are not trivial for continuous control) and also on GTS (which is a more complex setup for control). Therefore, the presented results are grounded in solid benchmarks.

- The discussion in Section 4.2 is very elucidative, and convincingly justifies the failures of the baselines in comparison to the proposed method. This helps understand the strengths of Residual-MPPI.

- Noticing that it is possible to replace the terminal value estimator for the log probabilities of the policy (into the MaxEnt framework) sounds particularly clever and also justifies well the proposed method.

### Weaknesses
While my concerns are not major, there are some suggestions that could improve the clarity of the results in the paper:

- In Section 5.1, the paper argues that the metrics to evaluate on GTS are lap time and off-course steps since the rewards are complex. Nonetheless, I believe the work should provide both the prior task reward and the add-on reward for each method, as in the MuJoCo case, to understand how the method influences the returns that are optimized. Perhaps the considered small changes in lap time are associated with big changes in the returns, which would mean that Residual-MPPI is actually considerably deviating from the prior task designed by the environment. It's crucial to understand if the method is truly adapting while maintaining the original task performance or if it's simply optimizing the add-on reward at the expense of the prior task.

- Similarly, the work could provide results for Residual SAC in the MuJoCo environments, as the most direct comparison baseline in the literature. Currently, the only results are in GTS. Providing MuJoCo results should also give a better understanding about this direct comparison. This is particularly important since MuJoCo environments are standard benchmarks, and the lack of this comparison makes it harder to assess the general applicability of the method.

- Another baseline that is important is training the “prior policy” on the full task (prior reward + add-on reward). Since MPPI is just a local search around the prior policy, perhaps it is too regularized towards the prior task. By providing the prior policy on the full task, the work provides a potential upper bound on joint performance, which contextualizes the performance of Residual-MPPI (as a policy customization method) to standard full RL training. This also helps clarify the trade-off of retraining a policy from scratch (expensive, but potentially better asymptotic performance) OR performing policy optimization (cheap, but potentially suboptimal). It would be beneficial to see how much performance is sacrificed by using a policy customization approach versus a full retraining approach.

- Lastly, the work should probably highlight more the results in terms of sample efficiency. I understand that sample efficiency is key to policy customization, particularly in the physical world. The work just mentions that MPPI leverages 2100 laps while Residual-SAC leverage 80000 laps, which is a big difference. From my understanding, this is a big contribution of the method and should be highlighted. Some suggestions are either bringing a temple of sample analysis to the main paper or at least highlighting these results in the text. A more detailed analysis of the number of samples required for convergence, and a comparison with other methods, would strengthen the paper's contribution.


Typo: Section 5.2.1: “Compration”

### Questions
As mentioned in my previous points, how does Residual-MPPI performs in comparison to training a prior policy on the full task (initial task + add-on reward)?



**Summary of the Review**:

The work is well written, the method is clearly presented and well motivated, the evaluation setup is also interesting. I do believe the work could improve in some directions, particularly adding a few more baselines and highlighting some important contributions. Nonetheless, I believe it is already in a good shape for acceptance.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an algorithm, Residual-MPPI, for customizing continuous control policies at execution time, without fine-tuning, in order to perform better at an auxiliary task while maintaining performance on the original task. Residual-MPPI does not require knowledge of the original task reward or value function; only the prior policy. However, the algorithm requires learning a dynamics model if one is not available, requiring additional online data to train and possibly iteratively improve as the policy changes (although apparently less data is required than the primary external baseline for policy customization, residual Q-learning). The approach is benchmarked against other variants of the algorithm on MuJoCo, with code provided, before being evaluated on the motivating use-case in Gran-Turismo Sport (GTS).

In summary, the paper has a strong problem motivation and proposed solution, but the quality and clarity of the paper could be significantly improved. As a result, this paper does not feel ready for publication yet, but I would be happy to increase my rating if these issues were improved before the end of the discussion period.

### Strengths
- **Motivation / Significance**
  - The problem of customizing a policy at execution time without knowledge of the original objective, and while minimising additional online data collection/fine-tuning, is an interesting and important problem.
  - This problem is well-motivated in the paper.
- **Approach / Originality** 
  - The use of MPPI as a model-based approach to customize the policy at execution time seems sensible and original.
- **GTS Application**
  - The GTS results provide a clear use-case for the use of the method.
  - The videos and results appear to show a clear improvement in the policy as a result.

### Weaknesses
 - **Quality**

  - The quality of the work should ideally be improved before the work is published. The full 10 pages are used, but there are many aspects which are unclear/undefined (see below), while there are large sections of text for which the key point is not clear. For example:
    - The discussion (first paragraph of section 4.2) should be made more concise by breaking it up into the key conclusions. 
    - The abstract could also be made more concise e.g. 'Residual-MPPI can be used to improve new performance metrics at execution time, given access to the prior policy alone.' 
    - The related work could similarly be made more concise by focusing on the key difference with each work.
  - Citations should be in brackets, not highlighted. 
  - The appendix should come after the references in the main paper, not in the supplementary materials.
  - Other small typos and mistakes such as:
    - L416: 'Compration'
    - L361: 'apperant'

- **Clarity / Novelty of Theory**

  - The relevance and novelty of the theory is unclear to me. The approach seems to be a direct application of MPPI to Resdiaul-SAC. What is the intended contribution of Theorem 1 to the paper? It is derived in the Appendix, but the resulting Equation 5 just appears to be a direct result from [1] and it is mentioned that reference [2] already combines MPPI with SAC. Calling it a Theorem seems unnecessary if it is not a new theoretical result. The purpose of this theorem and the logic behind the derivation of Residual-MPPI could be made clearer.
  - 'Few-shot' and 'zero-shot' are mentioned throughout the paper, but not defined until Section 5.1 and it is not clear what these terms refer to until this point. These should be defined in this context before use.

- **Experiments / Significance**

  - The add-on rewards used for the MuJoCo tasks are not stated in the main paper, only the Appendix. Some examples or at least the kind of add-on tasks considered should be included in the main paper to help the reader intuitively understand what kind of customization is being considered, and to define the last but one column of Table 1, which is meaningless otherwise. 

  - There are no external baselines for the MuJoCo experiements. Could residual-SAC be used as a baseline here? It is claimed that these results are zero shot, but Residual-MPPI would need a dynamics model for this to be the case. Where does the dynamics model come from for these experiments? If it is learned from data, then could Residual-SAC be trained on this data? The experimental evaluation would be strengthened by the inclusion of external baselines, or justification as to why these are not possible.

  - Residual-MPPI seems to fall between the baseline GT Sophy and Residual-SAC in terms of both Lap Time and Off-course Steps in Table 2, so Residual-SAC performs more conservatively as claimed. However, the authors mention that Residual-SAC takes much more data (80k laps) compared to Residual-MPPI (~2k laps). What would happen if Residual-SAC was trained on the equivalent smaller amount of data? I wonder if it might customize the policy less and therefore perform less conservatively on the original task, better matching the performance of Residual-MPPI? I believe this would provide a fairer comparison of the two methods so would be helpful to include if possible.

### Questions
- How were the MuJoCo add-on tasks chosen?
- How was a dynamics model obtained for Residual-MPPI for these environments?
- Why does Greedy-MPPI only degrade the performance for the Ant environment? It is stated that ignoring the log $\pi$ would degrade performance when the add-on reward is orthogonal to the basic reward in the discussion which makes sense, but why is this only the case for the Ant environment?
- Table 1 states that the evaluation results are over 500 episodes, but does not provide the number of training seeds/independent runs. How many training seeds were used? If only one seed was used, it should be stated that the std is over the evaluation period, not over different training runs, and this should be justified. 
- Why are two decimal places used in Table 1? This would be clearer to the nearest integer (except the undefined last but one column).

### Soundness
3

### Presentation
2

### Contribution
3
