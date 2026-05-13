# Text-Aware Diffusion Policies

- Decision: Reject
- Scores: 6, 5, 5, 3, 6

## Abstract
Training an agent to achieve particular goals or perform desired behaviors is often accomplished through reinforcement learning, especially in the absence of expert demonstrations.  However, supporting novel goals or behaviors through reinforcement learning requires the ad-hoc design of appropriate reward functions, which quickly becomes intractable. To address this challenge, we propose Text-Aware Diffusion for Policy Learning (TADPoLe), which uses a pretrained, frozen text-conditioned diffusion model to compute dense zero-shot reward signals for text-aligned policy learning.  We hypothesize that large-scale pretrained generative models encode rich priors that can supervise a policy to behave not only in a text-aligned manner, but also in alignment with a notion of naturalness summarized from internet-scale training data.  In our experiments, we demonstrate that TADPoLe is able to learn policies for novel goal-achievement and continuous locomotion behaviors specified by natural language, in both Humanoid and Dog environments. The behaviors are learned zero-shot without ground-truth rewards or expert demonstrations, and are qualitatively more natural according to human evaluation. We further show that TADPoLe performs competitively when applied to robotic manipulation tasks in the Meta-World environment, without having access to any in-domain demonstrations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present TADPol, a method that leverages a pretrained text-to-image diffusion model to provide a dense reward signal for control tasks based on only a text prompt. They demonstrate success on several locomotion tasks, show improved performance over a CLIP-based baseline, and also evaluate a video-diffusion-based version of their method.

### Strengths
The paper is overall well-written, clearly presented, and very easy to follow. The idea of using a diffusion model to provide a dense reward signal is interesting and novel (as far as I know). On the environments that are tested, the method is successful and performs better than CLIP, which is a natural baseline. The result of successfully performing locomotion tasks in zero-shot from text prompts is impressive.

### Weaknesses
While the idea of the paper is sound and interesting, I think the experiments are insufficient to demonstrate the efficacy of the method, particularly due to the lack of baselines.

- The experiments are overall very thin. The tested tasks are very simple and not very numerous, which does not really convince me that TADPol is generally applicable or works consistently.
- Baselines are lacking, with a CLIP-based reward being the only baseline. There are other methods use various pretrained models to provide a dense reward: e.g., LIV, which is mentioned in the related works section. Comparison to some other reward learning methods would be appropriate.
- While the paper is overall fairly clear, I feel that the title is a bit of a misnomer and the narrative constructed at the beginning of the paper caused some confusion. The method does not involve a diffusion policy at all; it leverages a text-to-image diffusion model, but only to provide rewards in a policy-agnostic way. I also found all of the talk about the policy as an implicit video-generating model distracting, as well as the discussion of video-generating diffusion models in the related work. I don't think these are fundamentally related to TADPol, since the end goal of the method has nothing to do with generative modeling, but is instead just about achieving good performance in traditional RL tasks. I really think the authors should edit the paper to make sure it does not claim to perform any sort of video synthesis since this is a gross overstatement.

### Questions
None

### Soundness
1 poor

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
While previously text-to-video models are trained using text-video pairs. This paper instead proposes to do text-to-video generation, using an existing physics simulator. This helps in preventing the text-to-video model from modelling low-level pixels, physics etc.
Instead now the model learns on how to act in the physics simulator, given a description of the task. The model proposes to use text-to-image diffusion models as reward signals to learn a policy that can act in the physics simulator such that it can generate a video of the text description.

### Strengths
- Proposes a novel way of rendering videos.
- Uses a generative model for getting a reward function to learn new behaviours, to my knowledge previous works have mainly use discriminative models such as CLIP for this.
- Shows results indicating that on a some environments they achieve rewards similar to the ground truth reward.

### Weaknesses
- the motivation of using simulator to render videos is unclear to me. Like in what realistic scenarios would such a method be useful? As to the best of my knowledge current simulators are not realistic in terms of the RGB they render aka sim2real gap. It's unclear to me in what end use cases would they be useful, also given that we have millions of videos available on the web widely.

- there are no comparisions with existing video rendering methods, thus making it unclear in what cases would they get better results. This point  is linked with the above point.
 
- The other motivation of the paper is learning robot behaviours, however there are mainly approaches previously proposed that do so such as : https://arxiv.org/abs/2310.12921 https://arxiv.org/abs/2203.12601 https://arxiv.org/abs/2210.00030. The paper fails to compare against any of them.

### Questions
Any answers to address the three points above would help me make the final decision.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes TextAware Diffusion Policies (TADPols) to leverage  text-to-image diffusion models to generate the reward signals for RL policies, which is from the prediction error between the diffusion model and the rendered images. The experiments show that the TADPols have comparable performances to the baselines with original rewards in some tasks.

### Strengths
The method is novel and interesting.

### Weaknesses
(1) The writing of this paper requires improvement in a great deal. 

(2) The experimental setting is not sufficient. 
- There are few baselines for introducing diffusion models for policy learning and other methods (not diffusions) for reward generations.
- The tasks are simple. What about some tasks with the DMControl suite, as other works do.

(3) The reward signal lacks of motion information or temporal information. For example, the diffusion model can not distinguish whether the walker is walking forward or backward. How to identify rewards in these scenarios?

### Questions
(1) Because the image is generated by the frozen diffusion model, it must be blurry and quite different from the current scene. In this case, the reward noise will be large, and RL is sensitive to the rewards. So I am wondering why the generated rewards can share comparable performances to the vanilla ones. Can you do some visualization to explain this phenomenon?

(2) The inference of the diffusion model is at a quite low speed. I am wondering how computation-efficient of this work is. Is it necessary to generate rewards every step?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose Text-Aware Diffusion Policies (TADPols), which attempt to learn the text-aware policy through reward function with the help of the generative prior contained in pre-trained text-image models. In particular, the reward function measures the alignment of provided instructions and images rendered of agent actions. The authors compared the proposed framework with baselines that use a reward function defined by CLIP similarity or using a text-to-video diffusion model.

### Strengths
- Overall, the paper is well-organized and easy to follow. 

- The idea is intuitive and straightforward. The authors defined an explicit and simple reward function to optimize the policy.

### Weaknesses
- The authors need to compare with other works such as LangLfP, Text-Conditioned Decision Transformer, or Hiveformer.

- As mentioned in section 4, the choice of noise step might be sensitive to the performance of the proposed method. It would be helpful if the authors could provide some experiments on the choice of noise step or even try to sample a range of noise steps to make the training more stable. Besides, the function k(t) in the defined function is not described clearly. Is the method sensitive to the choice of function k(t)?

- The method is only tested on a simulated environment within only three scenarios. It is hard to evaluate the method's effectiveness without testing on real-world scenarios.

### Questions
- Why is the stick not always in the air if we provide instructions with the verb “jump up” since the rendered images will align more with the states in the air? 

- The results with the velocity metric is a bit confusing. Why the diffusion-based ones are faster than the clip-based one? The reward function is to match the text descriptions, which does not imply the velocity.

- How will the model perform if provided with descriptions like “move forward” and “move backward”. Will they generate different policies?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a policy learning method that uses text-visual alignment as a reward signal. Diffusion models are used to compute the matching scores between text and images. The authors then conduct experiments on a variety of locomotion experiments, and the results show that the proposed method can learn to perform following the text while performing the motion as autonomous agents.

---

Post rebuttal: the authors provided extensively more experiments, which not look very good but it's reasonable. As a result, I upgrade my score from five to six.

### Strengths
1. The idea of adopting diffusion models as a reward model is novel in my feeling. I think this idea may have other applications and this is very insightful.
2. I love the provided video demos. They demonstrate that the proposed method can work in several environments.
3. The proposed approach outperforms a CLIP-based method, which is promising and it indicates that diffusion models may be a better measurement model.

### Weaknesses
I have a few concerns in my mind. However, I'll re-rate this paper after the rebuttal and after seeing other reviews.
# The soundness of this work.

1. The game environments are not natural images but the diffusion models are trained on natural images. How will this work in a game environment? I doubt the effectiveness of diffusion models in such a scenario. Can the authors show some generated images in this locomotion environment? Otherwise, I doubt the effectiveness of using diffusion models here.

2. If the video is not used, why doesn't the model get stuck into some best-matching frames? Since policy learning often involves some non-trivial procedures, it is not convincing if the authors only use text-to-image techniques but not video encoding methods. The matching should be conducted in the temporal space.

3. I see that the provided video demos do not have a very complex procedure. Most videos are nearly static and do not move much. This problem may be due to the use of images in the reward calculation.

# Comparisons and experiments.

1. Why don't the authors compare their methods in other language-guided tasks such as language-guided navigation?

2. The results shown in Table 1-2 are not very surprising. The authors are recommended to try harder problems. Also, comparing it to pure RL methods is a must.

### Questions
1. Why do the authors construct a large model for shaping rewards? This requires a good explanation.

2. How reliable the noise is to calculate the reward? Sometimes the noise may not mean much thing.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair
