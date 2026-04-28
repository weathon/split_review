# The Role of Forgetting in Fine-Tuning Reinforcement Learning Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 3, 8

## Abstract
Fine-tuning is a widespread technique that allows practitioners to transfer pre-trained capabilities, as recently showcased by the successful applications of foundation models. However, fine-tuning pre-trained reinforcement learning (RL) agents remains a challenge. This work conceptualizes one specific cause of poor transfers in the RL setting: *forgetting of pre-trained capabilities*. Namely, due to the distribution shift between the pre-training and fine-tuning data, the pre-trained model can significantly deteriorate before the agent reaches parts of the state space known by the pre-trained policy. In many cases, re-learning the lost capabilities takes as much time as learning them from scratch. We identify conditions when this problem occurs, perform a thorough analysis, and identify potential solutions. Namely, we propose to counteract deterioration by applying techniques that mitigate forgetting. We experimentally confirm this to be an efficient solution; for example, it allows us to significantly improve the fine-tuning process on Montezuma's Revenge as well as on the challenging NetHack domain.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper examines finetuning of pretrained RL agents in a single environment. Two problematic mechanisms are identified. A state coverage gap occurs when the agent is pretrained on a part of the state space but, in the fintetuning phase, has to first learn a policy on a different part. Then, the policy on the first part of the state space is lost during finetuning and must be relearned. The second, the imperfect cloning gap, occurs when the agent is pretrained through imitation learning. As the policy is finetuned, the performance on states later in trajectories also degrades. 
The use of behavioru cloning on states from the first task and other forgetting mitigation techniques are shown to solve these issues. A variety of environments are considered including toy tasks, metaworld and Nethack to demonstrate the problem and the utility of the solutions.

### Strengths
- There are extensive experiments on a variety of environments. The sequence of metaworld tasks was an interesting custom addition. 

- The identified problem could be relevant in a variety of practical settings. The imperfect cloning gap seems to be particularly applicable since we may often want to start with imitation learning from previous policies if possible. 

- There was sufficient detail in the text to understand the experiments and the figures were clear in general.

### Weaknesses
 - The clarity of certain sections could be improved with more details. For example, for the initial toy example, it would help if the main text explained the motivation behind the MDPs design a little more: why that particular choice of transitions and rewards was made. Also, $f_0$ is not described in the main text and it looks like subfigures b) and c) are interchanged for this example.

- The main proposed solution, behaviour cloning from the pretrained policy, seems to be somewhat limited. Behaviour cloning is inherently limited by the quality of the pretrained policy. The experiments show that it's possible to retain the pretrained policy's performance but not exceed it. This raises concerns about the practical applicability of the method in scenarios where the pretrained policy is suboptimal or when the goal is to surpass the initial performance.

- While novelty is difficult to judge, it seems like the identified problematic phenomena are facets of catastrophic forgetting i.e. the idea that neural networks will forget on certain parts of the input space after being trained on others. In this view, it's not too surprising that pretraining on one part of the state space will lead to a detoriation of performance in another. I can appreciate that there's value in demonstrating this in an RL setting though.

### Questions
- Are the benefits of pretraining purely from learning a good policy? Are there benefits due to the representations learned in the pretraining phase? 

- Have you experimented with the agent only learning a decent, but not great, policy on the FAR tasks? Could we expect to surpass the performance of the pretrained policy? Using behaviour cloning would seem to be limited by the pretrained policy.

- Have you considered off-policy methods? It seems like there may be an advantage since these methods could simply keep around samples (or trajectories) from previous tasks in the replay buffer to learn from without having to necessarily imitate the previous behaviours.

- In the robotic sequence task, have you tried pretraining on the second and third tasks? Are there any learning benefits for the 4th task if you do so? 

- In Montezuma's revenge, how far is the agent able to reach without pretraining? Does it get past room 7 consistently? It would be nice to see the overall learning curves of the agent that has been pretrained vs. the one that has not.

- Nethack levels are generated procedurally. How are the sequence of levels chosen for these experiments? When the agent is reinitialized, is it to a fixed level with the same seed?

- For the Nethack experiment, Fig.6, how come the learning curve for finetuning only matches that of the original agent after 2 billion steps? It looks like, if training continued further, the pretrained agent would even do worse.

- The Sokoban results (fig.7) seem to be fairly poor for both agents since they can only fill less than 1.5 pits on average---not close to a solution. Is this to be expected?

Minor points:
- I would consider moving some more of the results from the appendix to the main text since it looks like there's still space remaining.

- In Fig. 4, I would consider changing the text "pre-trained optimal policy" to "pre-trained expert policy" since we don't necessarily have the optimal policy in those environments.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Summary:

This paper studies fine-tuning in RL, and specifically the issue of forgetting and potential mitigation strategies. They demonstrate in several settings (simulated robot manipulation, Montezuma's Revenge and NetHack) that if a policy is pretrained on some part of the state space which is far from the initial state distribution, the knowledge is often forgotten and there are little to no improvements over training from scratch. They furthermore investigate different knowledge retention strategies (such as L2 penalties between pretrained and fine-tuned policy weights, possibly weighted by fisher information, as well as simple BC regularization on the pretraining data). They find that BC regularization helps the most, and can help prevent forgetting the behaviors encoded in the pretrained policy.

### Strengths
- The paper's main takeaway message, that adding BC regularization helps avoid forgetting previous behaviors during fine-tuning, is well supported by the experiments. This is demonstrated in 3 environment, including continuous control (MetaWorld), a pixel-based Atari game (Montezuma's Revenge) and a procedurally generated, long-horizon game with complex dynamics (NetHack). 

- The paper does a nice job with their analysis and visualizations illustrating the forgetting behavior.

### Weaknesses
 - The main takeaway, which is essentially that co-training on the old tasks prevents forgetting when learning a new task, is pretty unsurprising and has been demonstrated before in previous works in continual learning both for the supervised case and the RL case. It's not clear what the contribution of this work adds.
- An obvious downside of co-training on previous tasks is that the memory requirement increases linearly with the number of tasks and the computation increases quadratically - this is not adequately discussed. 
- It would have been nice to include result for the L2 and EWC on Montezuma and NetHack.

### Questions
Some suggestions on the writing:

- In the intro, it would be helpful to give a bit more details on the "knowledge retention techniques" used to mitigate the forgetting problems. Currently, the ready does not have much idea on the methodological aspects going into the paper. 

- Example in 2-state MDP: the notation here is confusing. Both $theta$ and $f_\theta$ are used before being defined. Please add the definitions in the main text.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This is an experimental paper that studies the forgetting issue in finetuning pre-trained models with RL. The paper focuses on two special cases of the problem: state coverage gap and imperfect cloning gap. To study the two problems respectively, the paper compares several existing methods in Meta-World, Montezuma's Revenge, and NetHack. Results shows that RL with behavior cloning on the pre-training dataset outperforms other methods, maintaining the pre-trained capabilities better during RL.

### Strengths
1. Forgetting of the previously learned skills is a problem worth studying in RL. 

2. The paper refines this problem into two cases and conducts appropriate experimental evaluation.

### Weaknesses
1. As an experimental paper studying forgetting, it lacks evaluation on many related methods. The paper only evaluates two kinds of  methods: parameter regularization and behavior cloning. But there exists many other methods addressing the forgetting issue in the literature of continual RL and finetuning with RL, like using offline RL over previous data [1], adding KL-divergence loss to the pre-trained policy on the online data [2], and a lot of methods in sharing representations and structures [3]. Specifically, the paper does not explore methods that explicitly maintain a replay buffer of past experiences or those that use a dual-policy approach, where one policy is responsible for the original task and the other for the new task. Furthermore, the paper does not investigate methods that use knowledge distillation from the pre-trained policy to the fine-tuned policy, which could be a more efficient way to transfer knowledge than behavior cloning alone.

2. The experimental results do not provide different insights into the two problems. All the results demonstrate that Finetuning+BC outperforms other methods and the vanilla Finetuning method suffers from forgetting on the FAR states. But beyond that, the results lack further analysis of the two problems and do not reflect the significance of dividing the forgetting problem into the two types. The paper does not provide a clear analysis of why the state coverage gap and the imperfect cloning gap lead to different forgetting patterns. For instance, it is not clear if the forgetting in the state coverage gap is due to the lack of exploration in the new state space or if it is due to the catastrophic forgetting of the pre-trained policy. Similarly, the paper does not analyze how the imperfect cloning gap impacts the policy's ability to generalize to new states. A more detailed analysis of the forgetting patterns in each case is needed to justify the division of the forgetting problem into these two types.

3. The paper has no novel contributions in methods and techniques. It also cannot provide insights in how to better address forgetting in the future work. The paper does not propose any new method for addressing the forgetting problem, nor does it provide any theoretical insights into why the existing methods work or fail. The paper also does not provide a clear roadmap for future research, such as identifying the key challenges in addressing forgetting in RL or proposing new research directions.

### Questions
1. Can the experimental results provide different insights into the two problems? In addition to these two problems, does the problem of forgetting include other cases?

2. Based on the experimental results, are there any insights in improving the existing methods or further addressing the forgetting problem?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work investigates catastrophic forgetting in fine-tuning pre-trained reinforcement learning (RL) policies on subsequent tasks sequentially in a stationary environment while data distribution shifts. It first shows how fine-tuned policies would deteriorate in performance for previous tasks. Then, the paper identifies two conditions in which forgetting occurs, namely, state coverage gap and imperfect cloning gap. Experimentally, the work further shows how existing knowledge retention methods like elastic weight consolidation (EWC) mitigate forgetting during the fine-tuning process.

### Strengths
1. This is an important research problem for both the understanding of deep RL training and potential practical deployments. We have seen extensive studies on fine-tuning of supervised learning. The same aspect in RL is relatively less studied. As deep RL moves towards large-scale pretraining, understanding the best practices of fine-tuning with downstream tasks is crucial.
2. The paper shows strong empirical analysis in understanding the problem, accompanied with extensive experimental results. I find the identification of the two conditions to be informative to researchers of this subfield
3. The paper in general is clearly written with key results elaborately explained.
4. Experimental results are comprehensively displayed. I particularly find figure 4 to be intuitive and helpful in visualizing the forgetting phenomenon.

### Weaknesses
1. The choice of benchmarking algorithms for knowledge retention, although somewhat representative of existing methods, does not quite match with state-of-the-art approaches. Newer methods like [1], if added, can strengthen the conclusions of the paper. Specifically, the paper could benefit from including methods that explicitly address catastrophic forgetting in RL through techniques like replay buffers or parameter isolation, which are more advanced than the chosen baselines. The current selection seems to focus on simpler regularization techniques, which might not fully capture the capabilities of modern continual learning algorithms.
2. It is unclear to me how is this setting different from continual/lifelong RL. The paper does not sufficiently articulate the nuances that distinguish the presented fine-tuning scenario from the broader field of continual learning in RL. While the paper focuses on sequential task learning in a stationary environment with data distribution shifts, it needs to clarify how this differs from standard continual learning setups, which also deal with sequential tasks and changing data distributions. The specific constraints and assumptions of this work need to be made more explicit to justify its distinction from existing continual RL literature.
3. [Minor] the term ‘realistic RL algorithms’ is confusing

### Questions
1. How is non-stationary enironment different from data shifts in stationary environment? Is it not the same underlying data shift problem?
2. What if we pretrain ‘CLOSE’ states first instead? Do we see better forward transfer?
3. Can the authors provide their views on why pre-trained models (counterintuitively) do not seem to exhibit any signs of positive transfer? Existing methods do seem insufficient for RL to leverage pretraining
4. Why is EWC missing in some of the subsequent experiments?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
