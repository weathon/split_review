# Towards Improving Exploration through Sibling Augmented GFlowNets

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Exploration is a key factor for the success of an active learning agent, especially when dealing with sparse extrinsic terminal rewards and long trajectories. We introduce Sibling Augmented Generative Flow Networks (SA-GFN), a novel framework designed to enhance exploration and training efficiency of Generative Flow Networks (GFlowNets). SA-GFN uses a decoupled dual network architecture, comprising of a main Behavior Network and an exploratory Sibling Network, to enable a diverse exploration of the underlying distribution using intrinsic rewards. Inspired by the ideas on exploration from reinforcement learning, SA-GFN provides a general-purpose exploration and learning paradigm that integrates with multiple GFlowNet training objectives and is especially helpful for exploration over a wide range of sparse or low reward distributions and task structures. An extensive set of experiments across a diverse range of tasks, reward structures and trajectory lengths, along with a thorough set of ablations, demonstrate the superior performance of SA-GFN in terms of exploration efficacy and convergence speed as compared to the existing methods. In addition, SA-GFN's versatility and compatibility with different GFlowNet training objectives and intrinsic reward methods underscores its broad applicability in various problem domains.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper is about exploration when learning generative flow networks. This is particularly relevant in a setting with sparse extrinsic terminal rewards. The proposed methods uses second, sibling, network along the main behavior network and use an intrinsic reward scheme (random network destination) for exploration. Using the two networks, it is possible to share re-labeled training data from the sibling network which is trained with the non-stationary intrinsic reward to the main behavior network with learns with the true reward. A set of abstract experiment evaluate the claims of better learning and the results show success of the proposed method. Ablation studies are also provided.

### Strengths
The paper addresses a relevant and interesting problem. The choice of an intrinsic reward methods and the parallel sibling network is interesting and novel for generative flow networks. Most of the experiments are fairly abstract but relevant.

### Weaknesses
The related work is short and makes it hard to assess novelty and relevance. The description of generative flow networks in 3.1 is short it does not become clear what the policy does and how it interacts with states and objects. RND is far from the only intrinsic reward scheme in reinforcement learning and it would strengthen the contribution to not compare against several alternative schemes.

### Questions
Given that RL and generative flow networks are not exactly the same, is there a way to improve RND for the generative flow network setting?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes a decoupled GFlowNet (Sibling) parallel with the main GFlowNet (Behavior) to improve the exploration of the learning process with sparse rewards. The auxiliary GFlowNet is trained on the original rewards combined with novelty-based intrinsic rewards, while the main network is trained only on the original rewards. Due to GFlowNet's off-policy property, the main network can use both its on-policy data and the data sampled using the sibling network. The proposed method achieves strong results in the tasks considered.

### Strengths
The paper is well-structured and written clearly. The storyline from the original GFlowNet through GAFN with additional intrinsic reward to SA-GFN with a decoupled network is clear and makes a lot of sense. The decoupled networks and relabeled rewards are simple yet effective methods. It is interesting to see the performance improvement by using the trajectories sampled with novelty exploration while only using the original rewards. Although intrinsic rewards are not a new idea for reinforcement learning, decoupling its samples and rewards for training has rarely been explored. The experiments are comprehensive.

### Weaknesses
- In the introduction, the authors claim to “expand the set of previous exploration benchmarks to include non-zero…” I assume they mean the experiment environment in section 5.1.2. It seems unfair to say so because the HyperGrid with non-zero rewards has already been used in previous work [1].
- Many references are incomplete, without information like the publisher.
- For the experiment results in Fig. 4, it would be better to plot the curves for more steps so that we can see the plateaued values of baselines, such as in 32x32, 64x64, 96x96, and so on.
- Last paragraph of 5.2. The indices of the three metrics and findings for the metrics are the same (a,b,c), which makes reading difficult.

### Questions
- How is the intrinsic reward calculated? According to equation 2, the intrinsic reward depends on the terminal states and all intermediate states. Would it be different if it is only calculated for the terminal states?
- Why do some L1 error curves of baselines increase in Fig. 4, such as 8x8x8x8? I have not observed this in other related work. Please explain.
- Out of my own curiosity, do the authors see potential methods for using the decoupled intrinsic reward network in RL tasks, such as navigation?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel architecture named Sibling Augmented Generative Flow Networks (SA-GFN), to improve the exploration capabilities in Generative Flow Networks (GFlowNets). The authors propose using a dual-network architecture, which consists of a Behaviour Network and a exploratory network (Sibling Network), which uses intrinsic rewards. By decoupling the two networks, it allows the Sibling Network to perform exploratory tasks, providing diverse data samples by relabelling the rewards with the true ones to the Behavior Network. With this design, the training objective of the behaviour network is stationary. Results shown in the selected datasets that SA-GFN outperforms baselines.

### Strengths
1. The paper is well written and the core idea is presented in a very clear way.
2. The idea itself is simple yet helpful for combining various intrinsic rewards methods and GFlowNets.
3. In the selected dataset, the proposed methods achieve the best performance compared to all baselines.
4. A detailed ablation study has also been provided.

### Weaknesses
1. Intrinsic reward method used as the baseline covers only RND. Other intrinsic reward methods such as NovelD, DEIR and others, which are shown better performance compared to RND are not included. In the appendix, NovelD is used as intrinsic reward for the sibling network but itself is still missing as a baseline
2. The tested environment is relatively simple. Testing in more complicated/hard-exploration tasks would be desirable.
3. The training of the Sibling network is unclear to me. See question section
4. An ablation study of the hyperparameter tuning of SN-GFN would be great. See question 3

### Questions
1. How does SA-GFN compared with other SOTA intrinsic methods, such as NovelD  then?
2. Is the sibling network also periodically updated using the data collected by the behaviour policy or directly using the behaviour policy's weight? If not, does this mean, by only trianing on the data collected by the RND, the sibling network is already sufficiently exploring the environment?
3. Currently, the training frequency of the sibling network and behaviour network seems to be 1:1. How does this ratio influence the training?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Sibling Augmented Generative Flow Networks are proposed to solve the exploration problem in sparse reward reinforcement learning. This approach decouples the exploration policy from the exploitation policy: the exploitation policy is responsible for maximizing the cumulative extrinsic reward (enlarging the trajectory of the generation of the labeled exploration policy at the data level), and the exploration policy is responsible for maximizing the combination of the cumulative intrinsic and extrinsic reward. The authors claim that this can enhance the performance and stability of policy learning. A series of experiments verify the proposed method.

### Strengths
1. This paper is well-written and easy to follow.
2. The sibling policy and the algorithm is new but can be quite straightforward to come up with.
3. The experiments part provides a wide range of comparisons with existing methods.

### Weaknesses
1. The experimental environment is too monotonous. There is only a grid world, and there are many other environments in the sparse rewards-related research, such as Montezuma's Revenge and some robot manipulation simulation tasks in Mujoco. I am curious to see if SA-GFN would be as effective for other tasks. If the author thinks it is difficult to provide corresponding experiments, I hope there will be a qualitative analysis or discussion.
2. If I understand correctly, the author seems to think that the GFlowNets presented in this paper do not fall under the category of reinforcement learning, which I have reservations about. The goal of GFlowNets is also to maximize the cumulative discount reward, and the training paradigm of off-policy RL is also used. This is the category of reinforcement learning in my opinion. I hope the author can further explain the positioning of the method proposed in this paper.
3. In the training of SA-GFN, the critic network is not used. In general, without the critic network, policy training will be unstable because of the high variance. This paper does not provide related discussion or experiments on this aspect. I would like to hear the author's thoughts on this aspect.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
