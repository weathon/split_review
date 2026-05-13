# Fast Imitation via Behavior Foundation Models

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Imitation learning (IL) aims at producing agents that can imitate any behavior given a few expert demonstrations. Yet existing approaches require many demonstrations and/or running (online or offline) reinforcement learning (RL) algorithms for each new imitation task. Here we show that recent RL foundation models based on successor measures can imitate any expert behavior almost instantly with just a few demonstrations and no need for RL or fine-tuning, while accommodating several IL principles (behavioral cloning, feature matching, reward-based, and goal-based reductions). In our experiments, imitation via RL foundation models matches, and often surpasses, the performance of SOTA offline IL algorithms, and produces imitation policies from new demonstrations within seconds instead of hours.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper leverages advances in behavior foundation models (BFMs) based on successor measures to build a BFM that can be pre-trained on a dataset of unsupervised trajectories without any prior knowledge of subsequent imitation behaviors. To that end, they describe several imitation learning methods that are based on a pre-trained Forward-Backward (FB) model. In the experiments the authors verify if an FB model that is pre-trained on one environment is able to imitate a wide range of tasks given only a few additional demonstrations on the target task.

### Strengths
1) The paper is easy to follow and well-structured with the main contributions listed clearly in the introduction alongwith grounding in related works and building blocks that make up this method. The paper is also technically sound with no methodical kinks that I could find. 
2) Experimental details are sufficiently described for reproducibility.
3) Experimental evaluation in the paper is very extensive covering a variety of methods with different pre-training methodologies on multiple tasks in the DeepMind Control suite.

### Weaknesses
Clarity: I think the clarity of the preliminaries can be improved. The paper assumes understanding of the FB framework which can make it hard to understand the core foundation of this work without going through previous papers. Effort should be made to make this work as self-contained as possible.

### Questions
Re future directions: Do the authors have any comments on utilizing FB pre-training for domain adaptation from sim to real? For example adapting to a locomotion task on a real robot from sim pre-training to overcome a low-dim parameter shift, and if this formulation will remain viable at all.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper leverages recent work on the successor measure, i.e., a generalization of the successor representation to continuous (or large) state spaces. In particular, the authors leverage the Forward-Backward (FB) representation, which learns a low-rank decomposition of the successor measure conditioned on a policy embedding z. These policy embeddings should be approximately optimal for a particular reward function. The authors show how to leverage the FB representation to perform various forms of imitation learning by reusing the FB representation and learning an appropriate policy embedding for the imitation task.

The work is well-motivated, and the importance is perhaps understated; imitation learning is a staple in many communities, and this paper provides notable improvements over well-established methods. As I see it, the primary contributions are:
* The authors provide a novel application of the FB factorization of the successor measure to imitation learning.
* Provide an extensive empirical analysis of FB applied to different forms of imitation learning, i.e., behavior cloning, reward-based imitation learning, distribution and feature matching, and goal-based imitation.

### Strengths
* The paper is very well written and easy to follow; each subsection detailing the application of FB is succinct but still provides many insights on the FB representation that prior work hadn’t touched on.
* FB is unique in that it can be pre-trained from offline non-expert transitions and subsequently used to derive a reusable imitation policy from expert trajectories with very little overhead.
* Well-designed empirical methodology with abundant baselines (both published and unpublished) on various continuous control domains. The experimental results are convincing and show significant improvement over the baselines.

I also want to mention that I appreciate the level of detail in the supplementary materials and the lengths the authors went to describe how the baselines were implemented and tuned. This gives me confidence in the results and the ability to reproduce said results.

### Weaknesses
* I appreciate 21 tasks across four domains, but one concern is that the general findings might not extrapolate to other continuous control domains.
* The results are limited to lower dimensional state spaces. I would appreciate at least discussing the method's limitations when scaling to higher-dimensional state spaces. It seems like FB has never been scaled beyond these low-dimensional continuous control tasks.

### Questions
* The DMC Maze tasks seem relatively straightforward; can you help give a better intuition as to why some methods fail to learn in this environment?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work leverages recent behavior foundation models (BFMs) that are based on successor features for fast imitation without RL or fine-tuning. Notably, this work uses the forward-backward (FB) framework to build BFMs that can solve any imitation learning tasks. The resulting set of algorithms is called FB-IL.  FB-IL accommodates several IL principles, including behavior cloning, feature matching, reward-based, and goal-based reductions. Experiments show that FB-IL can produce imitation policies from new demonstrations within seconds.

### Strengths
It is interesting and novel to leverage behavior foundation models based on successor features to enable fast imitation learning. Building on top of the forward-backward (FB) framework, FB-IL has several important and useful properties:

1.	Pre-training the BFM only requires a dataset of unsupervised transitions/trajectories.

2.	The BFMs solve imitation tasks without any complex reinforcement learning problem, and the computation is minimal,

3.	The BFM is compatible with different imitation learning settings, which is impressive. 

4.	The proposed FB-IL algorithms perform three orders of magnitude faster than offline IL methods, because FB-IL does not need to run full RL routines to compute imitation policies. 

5. It is nice to see the proposed framework can be extended to IL tasks with non-stationary demonstrations.

### Weaknesses
1.	The proposed method is motivated and based on the previous work in zero-shot reinforcement learning (Touati et al., 2023). However, the forward-backward framework contents in section 3 are not easy to follow. Don’t assume readers are familiar with the framework proposed by Touati et al.

2. The proposed methods are only evaluated in the tasks with low-dimensional states. I am wondering if the proposed methods still do not require RL routine or fine-tuning in environments with high-dimensional states.

### Questions
1.	This work leveraged BFMs based on successor measures, notably the forward-backward (FB) framework to solve fast imitation tasks. However, the introduction of successor measures is not clear enough. From section 3, we know that the successor measure describes the cumulated discounted time spent at each state following policy. The FB framework learns a tractable representation of successor measures that provides approximate optimal policies for any reward. What is the merit of achieving this goal?  And how does this property relate to FB-IL?

2. Will the proposed methods require RL routine or fine-tuning in environments with high-dimensional states?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The study extends prior research research into the Forward-Backward (FB) representation framework, a framework for training behaviour foundational models that hinges on representing agents + environment using an embedding space of policy representations and a set of two functions (F and B) that can be used to generate policy representations that are optimal with respect to emperically measuires rewards or reward functions unknown at model learning time.

In this study, the framework is extended to address Imitation Learning (IL), where policies need to be learned from one or more expert demonstrations. The paper introduces multiple FB-IL methods, each mimicking existing IL approaches. However, these FB-IL models, are trained using pre-trained domain-specific FB models (that were not exposed to reward or demonstrations of tartidular tasks), reducing computation time significantly. This is because he model of the environment and how the agent can interact with it are pre-trained, and IL training primarily focuses on finding the right policy embedding (z).

### Strengths
The various proposed methods are extremely sample efficient (doing about as well with a single expert example as they do with 200), are orders of magnitude faster to compute (excluding the FB training time which is performed once per domain and can then be used learn any task within that domain, so long as the space was adequarely explored at FB training time).
The results show that the IL-trained models can nearly match the performance of the expert models which they need to imitate (which were fully trained with RL).

There are many IL methods and this paper aims to show that the FB framework can support them all. As such, the paper lists the main IL approaches and for each, introduces an FB-based variant that mimics that approach. In that respect this paper presents not one but **multiple** methods that are quite distict from one another yet all sare the same (FB) representation framework, thus driving home the point that the FB framework is quite versatile and does not limit the IL approaches.

### Weaknesses
The basic FB framework is skimmed though very quickly, requiring the unfamiliar reader to go back to 1-2 previous papers on the topic to fully inderstand the representational framework.

The sheer number of "new" methods is a bit more that the reader might have bargined for in a 9-page paper (the very lengthy appendix serves as emphasis). Note that this can be seen as a strength of the work it self.

Prior work on the FB framework has been limited to the somewhat simplistic gym environments, This work is no different. While the FB framework can scale by increasing the complexity of the embedding functions and the dimensionality of the policy representation space, it is unclear, at this point, that the framework can serve well in non-simulated environments. IL seems to me to be a practical method for real world problems and it would be nice to see FB applied to non-simulation (or more complex) environments.

### Questions
I found it quite surprizing that the method cannot improve generated policies in any significant way with more than a single IL example. I wonder if that is a reflection of the simplicity of the environments (given that it *is* doing about as well as the expert that generated the single example)?

It was not clear to me how $\pi_𝑧(𝑠)= \arg \max _a  F (s, a, z)^T z$ is implemented. Is the arg max optimization occuring at every step or is the policy represented in yet another model that needs to be trained to estimate this arg max? If so how fast is that trainig?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
