# Grounding Video Models to Actions through Goal Conditioned Exploration

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
Large video models, {pretrained on massive amounts of Internet video},  provide a rich source of physical knowledge about the dynamics and motions of objects and tasks.
However, video models are not grounded in the embodiment of an agent, and do not describe how to actuate the world to reach the visual states depicted in a video.
To tackle this problem, current methods use a separate vision-based inverse dynamic model trained on embodiment-specific data to map image states to actions. 
Gathering data to train such a model is often expensive and challenging, and this model is limited to visual settings similar to the ones in which data are available.
In this paper, we investigate how to directly  ground video models to continuous actions through self-exploration in the embodied environment -- using generated video states as visual goals for exploration.
We propose a framework that uses trajectory level action generation in combination with video guidance to
enable an agent to solve complex tasks without any external supervision, e.g., rewards, action labels, or segmentation masks.
We validate the proposed approach on 8 tasks in Libero, 6 tasks in MetaWorld, 4 tasks in Calvin, and 12 tasks in iThor Visual Navigation. 
We show how our approach is on par with or even surpasses multiple behavior cloning baselines trained on expert demonstrations while without requiring any action annotations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a framework for grounding large pretrained video models to actions within an embodied environment through self-exploration. By generating visual goals from video states, the authors propose a goal-conditioned exploration strategy that allows agents to solve complex tasks without needing external supervision like rewards or action labels. A set of methods, including chunked action prediction and exploration with randomized exploration, are proposed to enable robust exploration. The proposed method is validated on several simulated environments, such as Libero, MetaWorld, Calvin, and iTHOR, where it demonstrates performance on par with or exceeding that of behavior cloning baselines trained on expert demonstrations.

### Strengths
1. The unsupervised grounding of video models to actions eliminates the dependency on expensive action annotations, efficiently addressing the problem of mapping video-based observations to actionable policies.
2. The proposed method achieves strong performances across multiple evaluation environments, outperforming supervised methods in quantitative and qualitative resutls. Besides, the method show adaptability across different domains, from robotic manipulation to visual navigations, demonstrating the robustness and generalization ability.
3. The ablation studies are comprehensive, demonstrating the effectiveness of the each proposed components.
4. Video-guided exploration allows the agent to focus on task-relevant state spaces, resulting in more targeted exploration and more effective data collection. This targeted approach enables the model to gather high-quality training data efficiently, especially for complex, long-horizon tasks that would otherwise require extensive manual annotation.

### Weaknesses
This paper is well-written with strong motivation and comprehensive evluation results. I only have some minor weakness and questions.

1. The reliance on random exploration may not be able to achieve high performance in tasks requiring high precision, such as tasks involving fine-grained manipulation or exact positioning. This approach may struggle to find optimal actions in environments where precise control is crucial, limitations is applications.
2. The proposed method is highly rely on the quality and generalization ability of the pretrained video generation models. If these models fail to generalize well to new environments, the effectiveness of the approach could be significantly constrained, especially in dynamic or unfamiliar settings.
3. The computational requirements might be high due to the chunk-level action prediction.
4. In algorithm 1, line 10-12 lacks an indentation, making it hard to read what is the condition and what is the content of the end-if sentence.

### Questions
1. Would the computational efficiency be improved by using distilled video diffusion models, which could generate videos in a very fast manner? Would the distilled models affect the performance of the proposed method?
2. Given the reliance on the pretrained video generation model, how does the framework handle cases where the video model’s generalization is limited? Are there specific techniques that could be employed to improve the model’s adaptability to novel or dynamic environments?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a method to "distill" a video-diffusion model to a goal-conditioned  policy for robot manipulation. The authors proposed to leverage the conditional generation capability of video generative models to sample future trajectories as goals for refining the goal-conditioned policy, which can gradually align its action prediction with the actual ground truth. The resulting method achieves state-of-the-art results on several commonly-used benchmarks.

### Strengths
The paper is clearly written and easy to follow, the method proposed achieves state-of-the-art results on several commonly used datasets with consistent improvement. The ablation study does show the effect of each designed module.

### Weaknesses
One concern about the proposed method lies in the selection of video-guidance. As assumed in this paper, a good enough conditional video generative model is key in improving the goal-conditioned policy in the iterative refining process. This leads to questions on the availability of such models for specific tasks with limited demonstrations. Though the authors mentioned leveraging pre-trained text-to-video models could be discussed in the future, it seems necessary even at the current scope (or if there is other work arounds or model performance guarantees on the data needed for a good enough task specific video generator). Specifically, the paper lacks a discussion on the sensitivity of the proposed method to the quality of the video generation model. What are the failure modes when the video generation model produces unrealistic or physically implausible future trajectories? How does the method perform when the generated videos contain artifacts or inconsistencies? The paper should also discuss the computational cost associated with training and using the video generation model, especially in scenarios with limited data, and how this impacts the overall efficiency of the proposed approach. Furthermore, the paper does not explore the potential for compounding errors in the iterative refinement process, where errors in the generated videos could propagate and degrade the performance of the goal-conditioned policy.

### Questions
See the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes leveraging video guidance to learn goal-conditioned policies without access to any external supervision. By leveraging pre-trained task conditioning video generative models, they propose sampling a sequence of frames demonstrating how to complete a task. These frames serve as sub-goal supervision for training a downstream goal-conditioned policy. The policy is initialized via behavior cloning with random action bootstrapping, and then proceeds to improve by sampling the video model to generate more conditioning data for the policy. The self-supervised learning proceeds by collecting the rollouts in the replay-buffer and fine-tuning the policy on the replay-buffer. The video generative model is trained with just image pairs and no action labeled data and can be replaced with large internet-scale pre-trained models in the future. 

Overall, this paper could be a significant contribution in combining self-supervised learning with video generative models to enable agents to solve complex tasks. But currently, there is confusion regarding the success of this method when random action bootstrapping fails. If addressed sufficiently, the rating can be increased.

### Strengths
The paper has several strengths including:
1. The work is well-motivated, well-written, and clear
2. The method is unique in proposing video models as a way to enable strong goal conditioning for the policy without needing action labels. 
3. The idea of self-learning is unique compared to current RL approaches
4. Good set of ablations performed in the main paper and supplement to analyze the method well 
5. The authors sufficiently addressed most of the limitations of their work. Despite these limitations, the method is still very interesting.

### Weaknesses
Some weaknesses of the paper include:
1. There is a lot of confusion around random action bootstrapping. Mainly, I am confused if it is possible to learn a policy without any successful actions (assuming random action bootstrapping does not result in any successful trajectories). Please see the first 6 points under ‘questions’ to know what needs to be added to the paper to address this weakness. Specifically, it's unclear how the policy can learn meaningful behaviors if the initial random actions do not lead to any goal-achieving states. The paper needs to clarify if the method relies on rare successful random actions, and if so, how many are needed for the policy to begin learning. The success rate of the policy after random action bootstrapping alone, before any video-guided training, should also be explicitly stated.
2. The cost of training this kind of model compared to BC is not mentioned in the limitation section. (The number of rollouts and iterations during self-training is high compared to the number of expert demonstrations for a BC policy). The computational cost of the self-supervised training, including the number of rollouts and iterations, needs to be compared to the cost of training a standard Behavior Cloning (BC) policy. This comparison should be included in the limitations section to provide a more complete picture of the method's practical applicability.
3. A real world experiment is not provided. Seems that such an experiment would be high cost, maybe that is why it is not shown? Would be good to discuss if there is a way then to transfer easily from sim2real, but I acknolwedge sim2real is an existing open question, so possibly ok to not address this.
4. Unsure if 3.3 is a novel contribution. Diffusion policy generates action chunks already. What is the new ‘mean sampling’ proposing beyond the standard diffusion policy action generation scheme? Lines 239-242 are unclear. The novelty of the 'mean sampling' approach within the context of action chunking needs further clarification. It's not clear how this differs from existing diffusion policy action generation schemes. The explanation in lines 239-242 is insufficient to understand the contribution of this specific sampling method.

### Questions
Key questions that should be addressed:
1. Maybe I have misunderstood, but how is it possible that without any ‘good’ actions ever given, the model can find actions that satisfy the goal eventually? Is it relying on the fact that at some point during random action bootstrapping there must be a few success cases? If so, how many successes in random action bootstrapping is required to learn the policy? Also, what is the performance of the policy with just random action bootstrapping (after line 3 of Algo 1) compared to performance after fine tuning with the video model in the self-supervised learning stage?
2. It is mentioned that random action bootstrapping is also performed at periodic intervals during training, but this is not indicated in Algorithm 1 (Algo 1 only shows random action bootstrapping before the loop starts). Please add that to the algorithm.  
3. How is random action bootstrapping implemented in experiments? Specifically, what values are used a_low and a_high in equation 3 for all the different experiments? These details seem important to include in main or supplemental given that w/o random has a 0% success rate. 
4. How frequently is the random action bootstrapping done? Would be a good point to add to the method (Sec 3.2) if this is a consistent number, or to the experiments if this is a hyperparameter.
5. Please provide details on how 'random extra' is performed. How many times extra do you do the random action bootstrapping? 
6. For each experiment, it would be good to note the number of iterations of self-supervised exploration used (N in Algorithm 1). 
7. If time permits, it would be good to understand the dependency of the policy during training on the model: What happens if the video model changes the sample rate it produces frames after the policy has been trained? For example, once the policy is trained, if the video model that is used changes to a pretrained model, does the policy produce viable actions? A simple experiment to run for this would be to just use the current trained policy, and replace the video model at test time, and see if the policy can still work. 

Additional minor comments:
1. Would be good to include more details in the caption for Figure 2. What are these pairs of images showing (the start and goal image of the task or something else)?
2. Please mention the metric you use to evaluate the ‘success’ or ‘failure’ of a rollout? Is there some check in the simulation environment? 
3. Typo line #147: should say ‘benefits both sides’
4. Typo line #423: should say ‘natural’ not ‘nature’
5. Line #314: Sure the video-model is zero-shot but the policy requires self-supervised training afterwards, so just change this sentence so it doesn't over-claim.

### Soundness
3

### Presentation
4

### Contribution
4
