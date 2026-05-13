# Understanding and Controlling a Maze-Solving Policy Network

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
To understand the goals and goal representations of AI systems, we carefully study a pretrained reinforcement learning policy that solves mazes by navigating to a range of target squares. We find this network pursues multiple context-dependent goals, and we further identify circuits within the network that correspond to one of these goals. In particular, we identified eleven channels that track the location of the goal. By modifying these channels, either with hand-designed interventions or by combining forward passes, we can partially control the policy. We show that this network contains redundant, distributed, and retargetable goal representations, shedding light on the nature of goal-direction in trained policy networks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study generalization of an image-based RL agent trained to find cheese in a maze. During training time, the cheese is always in the top right corner of the maze. During test time, the cheese can be anywhere. As a result, in a new maze at test time, the agent sometimes finds cheese, and sometimes goes to the top right corner.

They carefully analyze the network's behavior and internal mechanisms, and find key situations in which the agent decides between finding the cheese, or just going to the top right corner. Next, they analyze the network structure and find key neurons in the network that track the cheese. By modifying these neurons, they can somewhat control the behavior.

### Strengths
The authors tackle a very important problem in RL - generalization. Their specific definition of generalization, "goal misgeneralization", is less studied, yet is extremely important in the context of modern LLMs, RLHF, and  alignment. Even if we give the agent the "correct" reward function, it may still act unpredictably in OOD situations.

Their analysis of the maze task and policy is quite deep, and has some interesting studies and findings. They find that the agent chooses to pursue the cheese or the corner based on visual proximity.  Their experiments on controlling the policy by modifying internal activations is quite interesting as well.

### Weaknesses
The paper's deep analysis of the maze-cheese task and policy is its strength, and also main weakness. Many of the analyses and experiments hinge on their knowledge of the task, and also their design of the policy. This leads me to question 1) if these findings hold true for more realistic, complicated and relevant tasks, and 2) if the particular methodology used here, can be applied to other RL agents.

For example, the interpretability and controllability of the policy hinges on architecture and input image - an image-only, CNN-based policy.  Because the task is a 2D image, and the policy is CNN based, the authors can manually inspect all feature maps to find correlations with the 2d position of the cheese.  

Many tasks though, may be multimodal, non-image based, or even if they are image-based, may be first-person views of a 3d world. Many deep RL agents have different architectures - MLPs, LSTMs, Transformers, etc. The wide variety of possible tasks and agents seems to make it hard to use this approach for future studies.

Next, I did not see any mention of seed variance. Is it possible that these findings only emerge with the correct seed? How general are these results across RL agents, even if we fix the task to the Maze task?

### Questions
Could the authors address this point about task / policy specificity? 

Could the authors address the concern on seed variance? 

Top-right corner motivational vector - is the definition ordering swapped?
Figure 7 - the columns seem to be out of order.

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
This paper focuses on a pretrained reinforcement learning policy which solves mazes problem. The authors find certain circuits correspond to one of these goals and identify eleven channels which track the location of the goal. What’s more, they modify these channels by hand-designed interventions or by combining forward passes to partially control the policy.

### Strengths
1: The first to pinpoint internal goal representations in a trained policy network.
2: The visualization of activations is relatively clear and intuitive.
3: Experiments have been conducted to explore how the activation of specific channels affects the behaviors of policy.

### Weaknesses
1: The paper lacks further validation of whether the discovered intrinsic representation of the goal in the pre-training policy can be generalized to different policies. This would weaken the value attributed by the article to its exploration of the representation of the goal within the policy. This is because the phenomena mentioned in the article are only specific to a particular parameterized strategy rather than a general family of strategies trained on that environment.
2. The experimental phenomena and conclusions of the author cannot fully support their core contribution. We cannot demonstrate from the experiments that the 'intrinsic representation' of the goal in the policy can be represented by the activations of these 11 channels that are selected by human visual inspection. The selection process of these channels is not clearly defined, and it is unclear how much the conclusions depend on this specific selection. The authors should provide a more rigorous method for identifying these channels, such as using an automated feature selection algorithm, rather than relying on visual inspection.
3: The presentation of some of the experiments is confusing, and it may be helpful to detail the setup of these experiments in the appendix to help understand the work. For example, the method of combining forward passes to control the policy is not clearly explained, and it is difficult to understand how the authors achieve the reported results. The paper would benefit from a more detailed explanation of the experimental setup, including the specific parameters used and the steps taken to obtain the results.

### Questions
Question 1: 
Are the activations influenced by the agent's location or different steps? When we aim to control the policy by adjusting the activations, should we modify the activation of the initial state or all other states?
Question 2: 
Does the number of the most effective channels change when the size of the maze is altered? Or will the features found in 11 selected channels maintain consistency with respect to such changes in experimental settings?
Question 3: 
On page 6, what does it mean by "the geometric mean of the action probabilities to a given square from the start position"? I'm asking because I'm uncertain about the calculation of the "normalized path probability."
Question 4:
Why did you choose activations after the first residual block of the second IMPALA block as your target? Are there any insights or observations behind it? 
Question 5:
As authors said, we can control the behavior of the policy by combining different forward passes of the network, is it possible to control the policy to exhibit more flexible behavior in this way? For example, let the policy tend to move toward the upper-left corner (neither the position of the goal nor the "upper-right corner" bias introduced in the training phase).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors analyze the internal representations learned by a policy network trained to solve mazes. They identify channels that contain the goal information and analyze several interventions that modify the behaviour of the agent.

### Strengths
The paper is very well-written. The idea is simple and the presentation is clear, which makes the contents easy to follow. The experiments are well-designed to illustrate the discussion. The overall goal of understanding the internal representations learned by our agents is an important topic and clearly deserves a study.

### Weaknesses
The scope of the paper is far too narrow. The study is exhaustive, but it is focused on a particular architecture in a particular environment. Is there any chance of applying those results to other agents in other domains? I don't see any simple way. Thus, this work would have a very low impact on the community. Besides, the presented analysis is based on the 11 layers _found by visual inspection_. While suitable for a single experiment, this method can't be applied broadly.

The numerical results you obtain are far from convincing. If the logistic regression can predict the goal reachability in 82% compared to naive 71%, then quite few hard cases were actually explained. Certainly, there are more important features. I'd like to see that you define like 20 different features, exceed 95% accuracy, and then identify those that contribute most. Now, I think that you still miss important features. Also, when you analyze the interventions in Section 3.1 (and others as well), I see quite little difference between no intervention and intervening on all 11 channels. I'm not convinced that you _control_ the policy. I'm convinced that _there is some correlation between the intervention and the intended behaviour_. Furthermore, I think this analysis would be useful if you exceed the impact of moving the cheese. Only then you can confidently claim that you can control the policy and convince me. Now, it seems more like a bias than a control.

Overall, after reading this paper I would agree that you identified _some_ features that contribute to the behaviour, although (as you claim yourself) clearly there are much more of them, which makes the contribution even lower.

### Questions
Can the results that you present be generalized to other architectures and environments?

Can all those steps you describe (choosing the layer, identifying the channels, retargeting the goal, etc.) be automated?

Are there any reasons for the network to learn the goal location as a separate feature? Technically, it could be arbitrarily mixed with other features (as long as it can be extracted with linear transformations), rendering the visual inspection impractical.

Why did you choose this specific layer to inspect? Are those observations valid for many layers and you've just chosen an arbitrary one, or was it a careful decision?

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
1 poor
