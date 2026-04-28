# Improving Generalization of Alignment with Human Preferences through Group Invariant Learning

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 1, 8

## Abstract
The success of AI assistants based on language models (LLMs) hinges crucially on Reinforcement Learning from Human Feedback (RLHF), which enables the generation of responses more aligned with human preferences. 
As universal AI assistants, there's a growing expectation for them to perform consistently across various domains. 
However, previous work shows that Reinforcement Learning (RL) often exploits shortcuts to attain high rewards and overlooks challenging samples.
This focus on quick reward gains undermines both the stability in training and the model's ability to generalize to new, unseen data.
In this work, we propose a novel approach that can learn a consistent policy via RL across various data groups or domains. 
Given the challenges associated with acquiring group annotations, our method automatically classifies data into different groups, deliberately maximizing performance variance.
Then, we optimize the policy to perform well on challenging groups. 
Lastly, leveraging the established groups, our approach adaptively adjusts the exploration space, allocating more learning capacity to more challenging data and preventing the model from over-optimizing on simpler data. Experimental results indicate that our approach significantly enhances training stability and model generalization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an innovative method addressing the challenge of 'reward hacking' and neglect of complex samples in AI assistants powered by language models, through Reinforcement Learning from Human Feedback (RLHF). The proposed technique advances a consistent policy learning across different data groups, enhancing the AI’s performance evenly across domains. It innovatively classifies data into groups to highlight performance variances, optimizes policy for difficult groups, and adaptively regulates exploration space, thus boosting training stability and generalization.

### Strengths
1. **Organization and Accessibility**: The paper is well-structured and the content is presented in a manner that is accessible to readers.

2. **Significance of Addressed Problems**: The authors tackle critical issues within RLHF, such as reward hacking and the overlooking of complex samples, which are pertinent for the advancement of universal AI assistants.

3. **Innovative Concept**: The application of group-invariant learning to the alignment problem is both a novel and a promising idea.

### Weaknesses
1. The explanation in Section 4.4 regarding the probability of assigning samples to the highest-performing group lacks clarity and warrants further detail. Specifically, the mechanism by which the group inference classifier $\phi$ assigns probabilities and how these probabilities are then used to adjust the training process is not sufficiently elaborated. It's unclear how the classifier is trained and what specific features of the trajectories it uses to determine group membership. The connection between the classifier's output and the subsequent penalty or relaxation of constraints needs a more detailed explanation.

2. The term $R_{g}(\theta)$ is not clearly defined within the paper. It’s assumed to represent the expected return of group $g$, yet its relationship to the last term in Equation 6 is ambiguous and needs clarification. The paper should explicitly define how this expected return is calculated, including the precise mathematical operations and the scope of the expectation (i.e., over what distribution or set of trajectories). The connection between the per-trajectory returns and the aggregated group return is not clearly established.

3. The first term of the final learning objective in Equation (8) does not appear to be directly related to group $g$, raising questions about its role in achieving invariant learning. While the overall objective is to achieve group-invariant learning, the standard policy gradient term seems to optimize for overall performance without explicitly considering group-specific performance. The paper needs to explain how this term interacts with the group-specific regularization term to achieve the desired invariant behavior. The lack of explicit group-awareness in this term is a potential concern.

4. The paper would benefit from the inclusion of code or detailed pseudocode to clearly convey the training process, as the current description does not sufficiently outline the methodology. The paper lacks sufficient detail on the practical implementation of the proposed method. The training loop, the update rules, and the interaction between the different components of the method (e.g., the group inference classifier, the policy, and the regularization term) are not clearly described. A more detailed algorithmic description is needed to allow for reproducibility.

5. The connection between group invariant learning and its ability to address issues of shortcut exploitation and neglect of challenging samples is not clearly articulated. The paper does not provide a strong theoretical or empirical justification for why group invariant learning should inherently mitigate shortcut exploitation or prevent the model from neglecting challenging samples. It would benefit from a more detailed explanation of the underlying mechanisms and how they relate to these specific issues.

### Questions
Please refer to weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is motivated by the notion that maximizing only the expected return of a policy can be suboptimal when the return distribution has high variance or long tails. In Reinforcement Learning, the goal is to learn a policy that performs consistently across different data groups or scenarios. Here the group refers to different data distributions with varying performance characteristics. To achieve this, the authors propose incorporating a group inference classifier in the critic model to softly assign data points to groups. They maximize a variance objective to amplify the differences between groups. Additionally, they introduce an adaptive KL regularization scheme that allows different groups to have varied regularization strengths. This balances exploration and exploitation based on the group's difficulty. In summary, the paper aims to improve policy generalization by minimizing performance disparities between automatically identified data groups, while dynamically adapting the regularization to enable optimized exploration.

### Strengths
pros: 
1. This paper introduced a framework for policy invariant learning that does not reply on prior domain or group knowledge, where labeling is inefficient.
2. They propose a novel dynamic KL penalty based on group labels discovered before. Easier groups get stricter constraints, potentially preventing overoptimization.
3. Good experimental results. 	The method demonstrates good experimental results, outperforming baselines on in-distribution data. This highlights its capabilities in known domains. On out-of-distribution data, it shows even greater performance gains, underscoring its generalization abilities.
4. Ablation studies validate that both core components - group invariant learning and adaptive KL - contribute to the overall performance gains.

### Weaknesses
Cons: 
1. The experiments seem to imply a static number of groups, binary in the experiments,(best and challenging groups) which is not ideal with multi-modal data in dynamics environments. Experimenting with varying number of groups would be better to see how well does the method perform when the number of data groups increases?
2. The approach relies on accurate group label inference. Incorrect initial grouping could potentially lead to improper KL penalties. How robust is the method to errors in initial group assignment?
3. question: how do the newly introduced hyperparameters add complexity to tuning the algorithm? as training PPO is already known to be hard to tune.

### Questions
please see weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a method for improving LLMs' response quality on rare or difficult examples in the training data. Rather than treating all examples as equally important, the paper proposes to separate the data into groups so as to maximize the variance in quality among groups, then train the model to minimize that variance so that the model performs at roughly the same quality for all groups. Essentially this automatically adds additional training weight to difficult examples. The paper then presents empirical evidence that the proposed approach substantially improves response quality.

### Strengths
The paper is well motivated, proposes a novel idea, describes it clearly, and presents compelling evidence that it works. In short, this is an excellent paper!

It also has immediate practical significance for training LLMs to produce higher quality outputs, and initial evidence suggests this would be more helpful and less harmful for users.

Figure 1 is an excellent visualization of the problem and the proposed solution.

Figure 4 clearly demonstrates that the proposed method is much more stable than vanilla PPO.

### Weaknesses
- Sec 4.3 para 1: "the changes *to which* the algorithm needs to remain invariant..."
- p6, Stage 2:
    - "binary groups": Is there an advantage to using just 2 groups? I would have expected more. Variance is really just a simple difference unless there are more than two groups
    - "narrows the performance gap between the two groups": Relative to PPO, yes, but it still stays flat or increases over time. Why is that? It's unclear if this is a fundamental limitation of the approach or an implementation detail.
- p7, Table 1: It would be helpful to know how statistically significant these results are. Is there some way to do that? It would also be helpful to add a calibration where a method is evaluated against itself. It should be a 100% tie, but obviously it will be more like 33/34/33.
- p9, ablation study: "it enables the model to explore a larger action space on challenging samples, leading to the discovery of a superior policy". How does it enable that? The mechanism by which the dynamic KL penalty leads to increased exploration on challenging samples is not fully explained. It is not clear how the reduction in penalty translates to the model exploring a larger action space rather than just making more aggressive updates within the same space.
- p9, reward distribution: "which will aid in its generalization to unseen data." Why will it do that? Did you show this somewhere? The claim that a reward distribution approximating a Gaussian will aid in generalization is not sufficiently justified. It's not clear why this specific shape of reward distribution would lead to better generalization, and the paper does not provide any empirical evidence to support this claim.

### Questions
I don't have any major questions. The authors can feel free to respond to my questions in the previous section if they have time.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper suggests a method for Improving RLHF by preventing it to learn shortcuts/reward-hacking using a concept data groups where groups are classified rather than given beforehand. At the training time, the suggested approach puts more focus on learning the best behavior for challenging groups.

The grouping objective is adversarial to find groups with maximum discrepancy in reward, while the RL objective is encouraging reduction of loss variance across groups

-- Updated my evaluation after reading the responses and revisions

### Strengths
- The paper is well written and clear
- The method is generally sound and intuitive
- Promising experiment results

### Weaknesses
1- It is unclear how to find the optimal number of groups? The paper seems to miss discussion of this and sharing what settings used in the presented results, and how authors reached that setting.

2- The adversarial objective may pickup noisy or outliers and divert the optimization. I think this deserves more investigations. 

3- The learning objective is encouraging reduction of loss variance across groups, I was wondering why authors didn’t directly go for optimization macro average of loss which is a bit more intuitive and has less chance to have side-effects on the overall performance as mean is generally more stable than variance?

4- Robust optimization has been extensively studied in the general optimization context. Many of such methods could be applicable to the RLHF/LLM problem and the method proposed in this paper is also also applicable to other settings. I do not see any comparisons to support this method is optimal for RLHF compared to existing robust optimization methods.

5- Related to the previous two comments, we we should have compared with other robust optimization methods and variations of applying the group loss

6- In Section 3, “The training of an AI assistant consists of three main stages...“ is not necessarily the case for all AI Assistants. I suggest revising this statement and connecting the presented method to more broader usecases as it is not really limited to this case.

### Questions
(see points mentioned above)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
