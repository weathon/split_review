# The Role of Representation Transfer in Multitask Imitation Learning

- Decision: Reject
- Scores: 5, 5, 5, 6, 6, 8

## Abstract
Transferring representation for multitask imitation learning has the potential to provide improved sample efficiency on learning new tasks, when compared to learning from scratch. In this work, we provide a statistical guarantee indicating that we can indeed achieve improved sample efficiency on the target task when a representation is trained using sufficiently diverse source tasks. Our theoretical results can be readily extended to account for commonly used neural network architectures such as multilayer perceptrons and convolutional networks with realistic assumptions. Inspired by the theory, we propose a practical metric that estimates the notion of task diversity. We conduct empirical analyses that align with our theoretical findings on five simulated environments—in particular leveraging more data from source tasks can improve sample efficiency on learning in the new task. Our experiments further demonstrate that our proposed task diversity metric is positively correlated to the imitation performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper provides a tighter statistical guarantee in the sample-complexity of transferring what is learned from source tasks to target tasks and empirical evaluates this on some simple control tasks.

### Strengths
**Originality**
- The paper uses Rademacher complexity instead of Gaussian complexity, as used heavily by work that the paper references, in order to derive a tighter bound for a sample-complexity bound of the benefits of a representation in transfer learning in multi-task imitation learning (MTIL)

**Quality**
- Good to create and evaluate algorithms on discrete action space variants of continuous action environments while also evaluating on these continuous spaces to see whether theory that the paper proposes is actually empirically supported in both spaces for the same type of problem domain.
- The paper includes multiple correlation values in Tables 2 and 3 to cover certain limitations of individual ones.

**Clarity**
- The paper does a good job throughout explaining technical details and its experimental design.
- The paper provides intuitive explanations to accompany well-written rigorous definitions, which can help the reader better understand the concept being explained. For example, on page 3, the paper states "Intuitively, the Rademacher complexity of F measures the expressiveness of F over all datasets X through fitting random noise." after providing a rigorous definition of Rademacher complexity in its problem setup.

**Significance**
- The significance is potentially large, but I'm unsure how well it generalizes, especially due to the limitations of using only the KL-divergence and no other measure of dissimilarity between probability distributions.

### Weaknesses
1. The paper uses only KL-divergence to measure task-diversity for source and target tasks.

2. The paper doesn't compare using $D_{KL}$ to using other statistical measures of similarity between probability distributions, such as Bhattacharyya distance, which seem much more appropriate to do than the measures that the paper does compare $D_{KL}$ against.

3. **Generally when it comes to Rademacher Complexity in this context of this work, my concerns (really just an overarching single concern) are detailed in the paragraphs below.** However, I welcome thoughts on others from whether these are valid here or out of scope. If out of scope, then I also welcome discussion on how significant is the paper context, really?
- In the context of bounding sample-complexity in transfer learning, particularly for evaluating the richness of representation classes I wouldn't use Rademacher Complexity because of the importance of nuance in transfer learning on sequential tasks, which this measure avoids accounting for.
- Brief descriptions of Rademacher Complexity usefulness, main advantage, and main disadvantage for context:
  - Utility: Measures the ability of a function class to fit random noise, providing a general sense of the capacity of the function class.
  - Pro: Provides a general and well-understood measure of complexity that is applicable across various learning scenarios.
  - Con: It may not be as directly relevant to transfer learning scenarios because it doesn't specifically account for the nuances of transferring knowledge from a source to a target task.
- Given the specific requirements of transfer learning, which often involve understanding the relationship and distributional differences between source and target tasks, measures like Maximum Mean Discrepancy (MMD), Discrepancy Distance, and Task Similarity Measures become more pertinent. These measures are more directly aligned with the challenges of assessing how well a learned representation from one task can be applied to another, which is at the heart of transfer learning.
- Rademacher complexity, while powerful in many learning theory contexts, does not explicitly address these transfer-specific concerns. Therefore, it's more suited to general learning scenarios rather than the specific complexities of transfer learning.
- In fact, Gaussian complexity is somewhat similar but might be more suitable in certain contexts, especially in which approximately Gaussian assumptions naturally occur. Therefore, I again question the significance of this finding with Rademacher complexity in practice.

4. Evaluations do not include baselines using Gaussian Complexity in-place of Rademacher Complexity even though Gaussian Complexity may empirically be more useful on some tasks here.

### Questions
1. What insights do you have as to what causes the issue brought up in "We note that equation 5 is asymmetrical (i.e.  swapping τ with one of t ∈ [T] can yield different diversity estimate.)   This is a desirable property since model transfer generally is not symmetrical (Sugiyama et al., 2007). Suppose we have the expert policies π,π′ respectively for environments τ,τ′.  while π may stay performant in both τ,τ′, π′ may degrade when transferred to τ.  We demonstrate this in appendix D where the expert from each environment variation exhibits different robustness—one can stay performant in the target environment while another can degrade in performance."

2. On Page 2, the paper states "The consequence is that we can connect our result with deep-learning
theory, where the commonly used neural networks are quantified directly with Rademacher complexity (Bartlett et al., 2021)."
  a. Is this the best way to quantify neural network complexity here?
  b. Could you expound on your answer to 2a?
  c. What other options are available? 

3. Thoughts on using maximum mean discrepancy instead of Rademacher complexity?
4. Thoughts on using discrepancy distances, as these are directly applicable in assessing transfer learning effectiveness.
5. Thoughts on using local Rademacher complexities? This would be more nuanced and data-dependent though, and the Rademacher complexity avoids this nuance.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper posits that there exists a shared representation across a variety of tasks. It trains behavior cloning from a set of source tasks, learns a representation, and then learns a policy for a target task. It proposes that, the policy error is bounded by the diversity of the source tasks. It suggests that training in this paradigm will have better performance and uses less target task data than vanilla behavior cloning.


-----  Edit -----

I thank the author for writing the paper and their efforts in the rebuttal. They cleared some of my questions. But one of my major concern remains: How to define the shared representation? Since the objective of the paper is to provide a bound regarding learning a shared representation, it would be useful to define such representation clearly and setup appropriate experiment to learn said representation and validate the proposal. 

It would be helpful to explain, on the current experiments with low-dimensional state space like Pendulum, what does the learned shared representation capture?

Further, it would be really insightful to:
- (1) include environments commonly studied in multi-task setting that have different task rewards: e.g., MetaWorld of FrankaKitchen as mentioned by Reviewer Eicc. (Given the paper considers source tasks with varying rewards in Sec 3).
- (2) include environments on visual inputs: e.g., the Pendulum visual version mentioned by the author. (Given the author clarification response). 

I really appreciate the problem studied in the paper and the efforts of the author, looking forward to seeing more empirical validation of this paper in the future.

### Strengths
- Innovative Concept: The paper introduces an interesting hypothesis about the benefits of learning shared representations from diverse source tasks to improve policy learning in behavior cloning.
- Theoretical Contribution: It provides a theoretical framework that bounds policy error with respect to the source task diversity, offering a new perspective on the potential for generalization in behavior cloning.

### Weaknesses
 - Lack of Clarity: The paper does not sufficiently describe the "shared representation" it aims to learn. A more detailed exposition, possibly including visualizations or analysis of the learned representation, is needed. Specifically, the paper should clarify whether this representation is a fixed transformation or if it adapts during the target task learning phase. It's also unclear how the dimensionality of this representation is determined and if it's consistent across different tasks. The current description is too abstract to be practically useful.
- Theoretical Bound Practicality: The paper presents an order bound on policy error but does not provide a comprehensive discussion on its tightness or practical applicability, leaving its usefulness in question. The bound lacks concrete constants, making it difficult to assess its practical implications. Further, the assumptions under which the bound holds are not clearly articulated, making it challenging to determine when the bound is actually meaningful. The paper should also discuss how the bound scales with the complexity of the tasks and the size of the state-action space.


### Questions
Section 4 requires further detail on the nature of the source tasks for each target task investigated. The concept of "shared representation" is pivotal yet remains vague within the paper. Is this representation a transformation from a visual image to a latent space, or something else? A detailed analysis or visual depiction of this shared representation would greatly enhance the clarity, perhaps focusing on a single task as an example.

The paper introduces a theoretical bound but does not elucidate on its tightness or practical applicability. It is essential to quantify or provide conditions under which the bound holds with a fixed constant, thereby ensuring utility in policy improvement with additional data.

How do you define the “policy error” on Page 1? How can it be measured? Is the measurement done in the task reward, action space, or divergence perspective? Besides, you mentioned that f-divergence imitation learning states that a learned policy is minimizing the divergence between expert and learner trajectory. How does the policy error fit / contrast with such existing framework?

Given the focus on multi-task imitation learning, it is imperative to benchmark against state-of-the-art Meta Learning methods for a comprehensive comparison.

“However, current methods require thousands of demonstrations even in simple tasks (Mandlekar et al., 2022; Jang et al., 2021; Ablett et al., 2023)” => *Thousands* of demonstrations seems to misrepresent the SOTA of IL? Refer to https://www.roboticsproceedings.org/rss19/p009.pdf  https://medium.com/toyotaresearch/tris-robots-learn-new-skills-in-an-afternoon-here-s-how-2c30b1a8c573 https://deepmind.google/discover/blog/robocat-a-self-improving-robotic-agent/  Please clarify. 

For all experiments detailed in Section 4, please define the state and action space, including their dimensions.

Can the derived bound be applied to low-dimensional imitation learning that does not learn a representation? Assuming that the learned representation is the identity matrix, can we extend the bound to low-dimensional state space? Is the result implying that, adding more data into pre-training, will result in smaller policy error?  However, given what we saw in https://ieeexplore.ieee.org/abstract/document/10161474/ it seems that more data is not guaranteed to help imitation learning performance on the real robot. Can the author provide some insight? 


Our result is due to the objective of behavioral cloning, where the method aims to minimize the Kullback–Leibler (KL) divergence between the expert and the learner (Ghasemipour et al., 2019; Xu et al., 2020). => Could you elaborate how the findings from Xu et al., 2020 is related to this statement? 

Regarding Equation 4 and the "under some assumptions" qualifier, a more intuitive explanation of these assumptions and their impact on the model's generalizability would be essential.

---- Edit ---- 

I had a question on "what does this paper imply for low-dimensional state representation IL". I listed a paper that stated (Offline RL) "algorithms are not guaranteed to increase performance by including more data." It would be enlightening to extend this proposal to Offline RL. However, in retrospective, this request is probably out of scope for this proposal. I thank the author for clarification and sharing insights.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors consider, theoretically and empirically, the sample-complexity benefits pre-training a shared representation on multi-task data might provide for behavioral cloning. In theory, they prove a high-probability bound on the performance difference between BC learned on top of the shared representation and the expert data. In practice, they show that on a variety of discrete and continuous control problems, pre-training on multi-task data allows for effective policy learning with limited target-task data.

### Strengths
(+) The theoretical analysis is easy to follow and uses standard tools.

(+) I appreciated how the experiments section was broken down into the statement and testing of various hypotheses.

### Weaknesses
(-) Overall, I found the theoretical statements to be fairly simple extensions of known results by Tripuraneni et al. and Ross & Bagnell. In essence, by focusing only on behavioral cloning, the authors are able to almost entirely ignore the sequential nature of the imitation problem and apply the standard analysis for multi-task supervised learning. Then, once they have a bound on the KL divergence between the learner and the expert, they can apply the well-known upper bounds for behavioral cloning (https://www.cs.cmu.edu/~sross1/publications/Ross-AIStats11-NoRegret.pdf) to get an overall policy performance guarantee. So, I really didn't get much out of the theorems they proved.

(-) There's a few pieces of odd terminology throughout the paper. First, instead of "policy error", people usually use "performance difference" or "imitation gap" (https://arxiv.org/abs/2103.03236). Also, I think you're missing a $H^2$ or $\frac{1}{(1-\gamma)^2}$ in the first equation in the paper? Second, when people talk about "number of demonstrations" (i.e. $|\mathcal{D}|$ in the paper), they usually mean the number of whole trajectories rather than the number of state-action tuples (as you seem to use it in Table 1). Do you mind re-naming this? I got super confused for a while by why one would need millions of samples for BC to work on a Mujoco task. Can you also clarify whether $N$ and $M$ are measured in terms of trajectories or state-action pairs?

(-) Once you divide the numbers in table 1 by the horizon of the problem (1000 for Mujoco), you realize that they're attempting to learn based on effectively 1-2 demonstrations. This is a somewhat absurdly small amount of data (usually people do ~25 demos for Mujoco tasks). So, while the experimental results make sense to me, I think it is somewhat important to note that they are under fairly contrived settings.

(-) While the idea of a metric to capture the effectiveness of multi-task IL data for learning a transferrable representation is interesting, I found the ideas in Appendix B to be a bit sloppy and the empirical reported correlations in Tables 2/3 to be fairly low.

(-) Most analysis of imitation learning doesn't have to make assumptions about the optimality of the expert policy. In Footnote 1, you note that you do this. Is this actually important for any of your analysis?

(-) I might add some more citations for multi-task imitation learning outside of behavioral cloning. While they are clearly different than your work, it would be good to add in some references and discuss the differences: https://arxiv.org/pdf/1805.12573.pdf, https://arxiv.org/pdf/1909.09314.pdf, https://arxiv.org/pdf/1805.08882.pdf, https://arxiv.org/pdf/2309.00711.pdf. You might also want to cite some work on representation learning for sequential decision making (e.g. https://arxiv.org/abs/2207.08229).

### Questions
(1) I think it would be helpful if you could add in a comparable statement to Theorem 1 for single-task BC. You could then give ranges of T and N under which you'd have a meaningful difference in upper bounds between multi-task and single-task BC. The sharpest analysis I know for IL under a deterministic expert assumption is in https://arxiv.org/pdf/2205.15397.pdf -- you might be able to just copy some of their theorems.

(2) In Figure 1, why do some of the performances for the multi-task method start lower than the corresponding BC performances? Do you think this would be fixed if you included target task $\tau$ in the representation learning step?

(3) Do you have any hypothesis for why, in Figure 2, things look quite bad for CartPole? Is it perhaps because of the kinds of environment modifications you were considering?

(4) In Figures 3 and 4, you're giving the learner quite a bit of source data so perhaps the performance gap is already quite close. If you have the compute resources, could you ablate these results across smaller values of $N$?

(5) Generally, could you be more specific about the ranges over which you varied environment parameters to generate the multi-task data (e.g. what link sizes for Walker)?

### Soundness
4 excellent

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
This paper addresses the statistic guarantees of transfer learning with regards to its improvements in sample efficiency, specifically with regards to imitation learning paradigms. The main result of this paper is a bound on the policy error that is indirectly related to the task diversity of the source tasks $T$, the number of demonstrations of the source task $N$, and the number of demonstrations of the target class $M$, and directly related to the Rademacher complexity. Task diversity is intuitively defined as how closely can some learned policy $\pi^*$ perform on a new task given source tasks.

The proposed method is split into two stages: first learn a representation embedding $\hat{\phi}$ from source tasks, then learn a policy $\pi$ conditioned on the task-specific mapping $\hat{f}$ and $\hat{\phi}$. The training objective of the first phase is to minimize the log loss of $\pi$ given a task-specific mapping for source task $t$ and the parameter $\phi$. The training objective of the second phase is to minimize that same loss using $\hat{\phi}$ from above, this time varying the task-specific mapping $f_\tau$. The authors perform their analysis in the tabular setting, but mention that it may be possible to extend to continuous state-action spaces in theory, and provide empirical results to support this.

The empirical questions the authors aim to answer is whether multi-task behavioral cloning training can do better than single task behavior cloning training, and ablate over $N$, $T$, and $M$ to see which affects performance the most. They find that increasing $N$ and $T$ are most impactful in improving performance and reducing the demand on target data demonstrations.

### Strengths
The main contributions form this paper are two fold: 1) a tighter bound on sample efficiency of multi-task imitation learning paradigms, and 2) empirical results focus on the effectiveness of representation transfer and a new metric to measure task diversity. 

- The paper clearly presents the hyperparameters it is interested in that is relevant to their main bound, and does a thorough ablation over each parameter.
- The proposed KL metric is described in a digestible manner, and good to see thorough results testing its effectiveness. As mentioned, it is an important direction to prompt more empirical work analyzing task diversity.
- Empirical findings are interpretable, and good combination of graphs and tables.

Finally, the paper is generally free of grammatical errors and typos, and written in a clear manner. Overall, it is likely to be of interest to a smaller community in the multi-task learning space. However, if the authors could provide more results on experiments outside of Mujoco, such as the more challenging tasks mentioned below, it has the potential to raise interest in the larger multi-task imitation learning community.

### Weaknesses
### High Level Technicals:
- While the story told in Figures 1-4 are clear, it would have been nice to see some evaluations on at least one multitask environments such such as FrankaKitchen [[1](https://robotics.farama.org/envs/franka_kitchen/franka_kitchen/)] or Metaworld [[1](https://meta-world.github.io/)]. While the current results on Mujoco support the claim, the environments are relatively simple. The results of this paper would be of interest to a much larger community if the same compelling results are shown on just one of the above environments. Specifically, the Mujoco environments used are relatively low-dimensional and do not capture the complexities of real-world robotic manipulation tasks. Testing on FrankaKitchen or Metaworld, which involve more complex contact dynamics, visual inputs, and longer planning horizons, would provide a more rigorous evaluation of the proposed method's ability to generalize and scale to more challenging scenarios. This would also better highlight the benefits of the learned representations.
- It would have been nice to see some more interpretation on the results of Spearman and Kendall correlations on the bottom of page 8. The correlations, while positive, are rather weak in some cases, particularly for Frozen Lake, Cartpole, and Pendulum. It's unclear why these environments exhibit weaker correlations, and a deeper investigation into the underlying causes would be beneficial. For instance, is it due to the nature of the task itself, the sensitivity of the policy, or limitations in the task diversity metric? A more detailed analysis of the failure cases and the specific characteristics of these environments that lead to lower correlation would strengthen the paper's claims. Furthermore, the authors should discuss the implications of these weaker correlations for the applicability of their method in different task settings.
- Due to the boldness of the lines and overlap, it is a bit challenging to tell the differences between the blue, yellow, green, and red lines. I might suggest using different shapes in or decreasing the boldness of the lines. 

### Low Level Technicals
- On (ii) towards the bottom half of page 7, "let" should be capitalized in "let \hat{r}_t be the average rewar of the expert..."

### Questions
1. Is there any demand on the optimality of the source task demonstrations? For example, would a large batch of suboptimal demonstrations actually deteriorate or stagnate improvement given the proposed method?
2. I'm curious whether increasing amount of source task data would also make the policy more robust to covariate shift, since it theoretically should have a larger state-space coverage. Or when transition dynamics are stochastic.
3. Have the authors attempted to generalize their framework to imitation learning algorithms beyond behavioral cloning, such as IRL methods?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses the advantages of using transferred representations in multitask imitation learning. The authors propose that such transfer can improve the efficiency of learning the target task by using representations learned from sufficiently diverse and related tasks, which can lead to a reduced need for data when training on a new task. They provide theoretical guarantee to support the idea that representation transfer is beneficial, which can be extended to neural network architectures such as multilayer perceptron and convolutional networks. The paper also provides empirical analysis that validate the theoretical findings. Experiments are done in simulated environments to show that leveraging data from diverse source tasks can indeed improve learning efficiency on new tasks.

### Strengths
- The paper is well organized and nicely written. The contributions are outlined and well emphasized, and the settings/backgrounds are well introduced. Definitions and theorem are formally stated and discussed with remarks. 
- Theoretical results are reasonable as far as I read into. Extensive discussions are provided in the appendix.
- The topic on multi-task representation learning is interesting and important.

### Weaknesses
 - It would be better to state clearly in the main paper about what assumptions are made in the paper and discuss about the limitations.  For example, what are the requirements on the source tasks for the transfer to be effective? Are there specific properties or relationships that these tasks must satisfy? The paper mentions the tasks should be 'sufficiently diverse and related', but this is vague. A more precise definition or discussion is needed. Also, what kind of task is not suitable for transfer learning? What are the limitations of the theoretical results? Are there any assumptions on the data distribution or the network architecture that may not be realistic in practice? A discussion on these limitations is important to understand the scope of the theoretical results.
- It is difficult to read Figure 1-4. The lines are hard to distinguish from one another.

### Questions
See in weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides a statistical guarantee for multitask imitation learning for improved sample efficiency. Their contribution builds on others work such as Arora et al by using the Rademacher complexity. Using this they have a tighter bound which will provide benefits of transferring for imitation learning. With theoretical insights, they provide empirical results while comparing with multitask behavioral cloning. The environments they utilize are Cartpole, Frozen Lake, Pendulum, Cheetah, and Walker.

### Strengths
With the experiments, you have measured some scenarios in both discrete and continuous domains to show that it works. The additional experiments in the supplementary material show the amount of rigor especially with showing the task diversity metric.

The motivation of the theory makes sense and you provide a good amount of related works to show the relevance of the significance.

### Weaknesses
Writing
You state in the abstract “readily extended to account for commonly used neural network architectures such as multilayer perceptron and convolutional network with realistic assumptions” It would strengthen this claim if you had experiments with convolutional networks to show that it can be done. If not please reconsider modifying your claim.

In the theoretical contributions paragraph in page one, what do you mean by the second sentence, is that from the Arora et al. paper, if so please say that it refers to that because it sounds off?

Experiment
For the BC baseline, it seems like an easy one to compare and in the SM you have BC with 2|D| would it not be appropriate to also show that similar comparison with the main text experiments to show what if BC had more |D| to what your method has?

### Questions
Please refer to the weaknesses section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
