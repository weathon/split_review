# Contrastive Preference Learning: Learning from Human Feedback without Reinforcement Learning

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Reinforcement Learning from Human Feedback (RLHF) has emerged as a popular paradigm for aligning models with human intent. Typically RLHF algorithms operate in two phases: first, use human preferences to learn a reward function and second, align the model by optimizing the learned reward via reinforcement learning (RL). This paradigm assumes that human preferences are distributed according to reward, but recent work suggests that they instead follow the \emph{regret} under the user's optimal policy. Thus, learning a reward function from feedback is not only based on a flawed assumption of human preference, but also leads to unwieldy optimization challenges that stem from policy gradients or bootstrapping in the RL phase. Because of these optimization challenges, contemporary RLHF methods restrict themselves to contextual bandit settings (e.g., as in large language models) or limit observation dimensionality (e.g., state-based robotics). We overcome these limitations by introducing a new family of algorithms for optimizing behavior from human feedback using the \textit{regret}-based model of human preferences. Using the principle of maximum entropy, we derive \fullname (\abv), an algorithm for learning optimal policies from preferences without learning reward functions, circumventing the need for RL. \abv is fully off-policy, uses only a simple contrastive objective, and can be applied to arbitrary MDPs. This enables \abv to elegantly scale to high-dimensional and sequential RLHF problems while being simpler than prior methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents Contrastive Preference Learning (CPL), an algorithm to learn optimal policies from preferences without learning exlicitly a reward function which is commonly done in RLHF scenario. This circumvents the issue of having an underoptimized/overoptimized reward model. The authors then show the performance of CPL for MetaWorld benchmark.

### Strengths
1. learning a reward model from human preferences has flaws. And on top of that, using RL to optimize for this reward model can sometimes lead to poor performance. This paper solves this issue by not having a reward model.
2. CPL has supervised objectives so it is scalable 
3. The proposed algorithm is generic

### Weaknesses
1. In my experience, learning a "good" reward model and then doing RL always outperforms offline RL algorithms. The authors only compare it with IQL and not with methods that explicitly learn a reward model to highlight more. It would be beneficial to see comparisons against methods that learn a reward function and then use it for policy optimization, as this is a common approach and it's not clear if the proposed method is superior in those cases.
2. The authors claim that the method is generic but then it is only applied to MetaWorld benchmark. The RLHF scenario is much more interesting in aligning language models with human feedback. The evaluation is limited to a single benchmark, MetaWorld, which is a relatively narrow domain. The paper would be strengthened by demonstrating the method's effectiveness on a wider range of tasks, particularly those involving more complex state spaces and action spaces. The claim of generality is not fully supported by the experimental results.

### Questions
How does CPL compare with RLHF for language models scenario?
How does CPL compare with other baselines, which may or may not have reward models

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a Contrastive Preference Learning (CPL) framework for learning optimal policies from human preference data without learning the reward function. Specifically, the paper models human preferences using the advantage function and proposes a general loss function for learning policies. The loss function ensembles the contrastive learning objective and can be optimized directly without learning a reward function. As a result, the method can scale to high-dimensional environments and sequential RLHF problems (i.e., beyond contextual bandits). Theoretically, by optimizing the loss function, CPL provably converges to the optimal policy of the underlying max-entropy RL problem. The paper tests one instantiation of the CPL framework and shows its promising performance in practice.

### Strengths
- The proposed algorithmic framework is novel and elegant. The motivation for the problem is clear.

- The method is scalable without the use of RL.

- The experimental results are adequate.

- The paper is very well-written and easy to follow.

### Weaknesses
I did not identify any noticeable weaknesses.

### Questions
Since the CPL loss function has a super elegant form, is it possible to derive finite sample analysis for learning a near-optimal policy like [1]?

[1] Zhu et al., Principled Reinforcement Learning with Human Feedback from Pairwise or K-wise Comparisons, ICML 2023

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors address critical aspects of the PBRL framework, with a specific emphasis on the optimization challenges in the RL phase. To solve this problem, the authors introduce a novel approach called Contrative Preference Learning (CPL). This method leverages a regret-based model of human preferences, from which a contrastive objective is derived with the principle of maximum entropy. This approach bypasses the need for reward learning and RL, instead directly learn the policy through a supervised learning paradigm. To evaluate the effectiveness of CPL, the authors conducted experiments within the offline PbRL setting, comparing it against strong baselines in terms of the success rate across distinct tasks in the Metaworld domain. The experimental results show that CPL outperforms baselines with less runtime and smaller model size. The primary contribution of this work lies in the conversion of the traditional two-phase PbRL framework into a novel paradigm capable of directly learning the policy with a new contrastive objective.

### Strengths
This work focuses on addressing critical challenges in PbRL. It is well-motivated and accompanied by a clear and thorough discussion of existing issues within both the reward learning and RL phases.

The proposed CPL bypasses the need for reward learning and RL by optimizing a supervised objective, enabling it to learn policy from offline high-dimensional suboptimal data. Moreover, it can be applied to arbitrary MDPs. I feel this approach can be seen as a counterpart to DPO, as discussed by the authors in the paper—one for NLP tasks with LLMs and the other for continuous control tasks. This work has the potential to make a significant impact in the community, and I am eager to see how CPL performs in broader applications.

Generally, the organization and presentation of the content are well-structured, facilitating ease of reading and comprehension. The authors provide comprehensive theoretical proofs that make the work sound. The experimental results are impressive in terms of runtime, model size, and performance. In the limitation section, I appreciate the authors acknowledge the imperfections of the human model and raise considerations regarding the application of this approach to online human feedback.

### Weaknesses
Please see Questions.

1. I still have questions regarding regret-based preference model. I agree with the authors that the regret-based preference model makes more sense when we consider the hand-engineered example in section 2. However, when we talk about data collection with a real human, the human labeler would have a preference over two trajectory segments. This implies the existence of underlying dense rewards that explain the human's preferences. In such cases, I feel that the key issue lies in the hand-engineered reward is incorrect (i.e., reward design issue) in your example, rather than in the issues of the reward-based preference model.

Therefore, when we consider experiments with real humans and apply the reward-based preference model, could it also perform effectively? Is it possible that the learned reward captures the regret information to a large extent? Please correct me if I have misunderstood.

2. Despite considering the model complexity of CPL, the results are promising. In terms of feedback efficiency, does CPL require more human preference data compared to the conventional two-phase PbRL framework in order to perform well? This is especially relevant considering the Metaworld tasks in the experiments, where obtaining dense data could be challenging if collected from real humans.

3. In the experiments, the authors pretrain the model with behavior cloning. To what extent does this pretraining phase impact the model's final performance? Does P-IQL also have this pretraining phase?

4. Similar to DPO, CPL employs a supervised learning framework without reward learning and RL. Does it potentially lose the generalization power of RL?

### Questions
1. I still have questions regarding regret-based preference model. I agree with the authors that the regret-based preference model makes more sense when we consider the hand-engineered example in section 2. However, when we talk about data collection with a real human, the human labeler would have a preference over two trajectory segments. This implies the existence of underlying dense rewards that explain the human's preferences. In such cases, I feel that the key issue lies in the hand-engineered reward is incorrect (i.e., reward design issue) in your example, rather than in the issues of the reward-based preference model.

Therefore, when we consider experiments with real humans and apply the reward-based preference model, could it also perform effectively? Is it possible that the learned reward captures the regret information to a large extent? Please correct me if I have misunderstood.

2. Despite considering the model complexity of CPL, the results are promising. In terms of feedback efficiency, does CPL require more human preference data compared to the conventional two-phase PbRL framework in order to perform well? This is especially relevant considering the Metaworld tasks in the experiments, where obtaining dense data could be challenging if collected from real humans.

3. In the experiments, the authors pretrain the model with behavior cloning. To what extent does this pretraining phase impact the model's final performance? Does P-IQL also have this pretraining phase?

4. Similar to DPO, CPL employs a supervised learning framework without reward learning and RL. Does it potentially lose the generalization power of RL?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces Contrastive Preference Learning (CPL), a novel algorithm designed for learning optimal policies from preferences, eliminating the need to learn reward functions. CPL integrates the regret-based preference framework with the principle of Maximum Entropy, establishing a one-to-one correspondence between advantage functions and policies.
The experimental results highlight CPL's superior performance compared to SFT and offline Reinforcement Learning (P-IQL).

### Strengths
1. The motivation is evidently well-defined.
2. It adeptly combines theoretical analysis with empirical findings.
3. The proposed method is written in a clear and easily understandable manner.

### Weaknesses
This article exclusively compares CQL with offline RL, but to my knowledge, the majority of RLHF (Reinforcement Learning from Human Feedback) algorithms employ **online** RL algorithms [1]. There appears to be a fundamental distinction between these two training paradigms. Offline algorithms exclusively train the model on static datasets, whereas online algorithms train the model on the trajectories gathered by the training policies.

I strongly encourage the authors to include a baseline that trains the reward model using the dataset and subsequently employs an **online** training methodology, such as PPO. This addition is crucial to substantiate the authors' claims.

### Questions
What if you were to employ an online RL algorithm for the reinforcement learning experiment instead of an offline one?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
