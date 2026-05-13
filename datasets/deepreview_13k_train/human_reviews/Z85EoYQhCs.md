# One-Step Diffusion Policy: Fast Visuomotor Policies via Diffusion Distillation

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Diffusion models, praised for their success in generative tasks, are increasingly being applied to robotics, demonstrating exceptional performance in behavior cloning. However, their slow generation process stemming from iterative denoising steps poses a challenge for real-time applications in resource-constrained robotics setups and dynamically changing environments.
In this paper, we introduce the One-Step Diffusion Policy (\ours), a novel approach that distills knowledge from pre-trained diffusion policies into a single-step action generator, significantly accelerating response times for robotic control tasks. We ensure the distilled generator closely aligns with the original policy distribution by minimizing the Kullback-Leibler (KL) divergence along the diffusion chain, requiring only $2\%$-$10\%$ additional pre-training cost for convergence. We evaluated \ours on 6 challenging simulation tasks as well as 4 self-designed real-world tasks using the Franka robot. The results demonstrate that \ours not only achieves state-of-the-art success rates but also delivers an order-of-magnitude improvement in inference speed, boosting action prediction frequency from 1.5 Hz to 62 Hz, establishing its potential for dynamic and computationally constrained robotic applications. We share the project page here \href{https://research.nvidia.nvidia. %, and the code will be publicly available soon.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
How can we distill diffusion policies into fast, one-step action generators? The authors propose One-Step Diffusion Policy (OneDP), a distillation-based approach to improve inference time of diffusion policies for robotics tasks from 1.5Hz to 62Hz. Diffusion policies have shown impressive results in imitation, and this work improves imitation learning by allowing for more responsive control due to fast inference. In order to distill Diffusion Policy, the authors opt for an SDS-based approach rather than one based on Consistency Models. The authors learn a generator (initialized from the pretrained imitation policy), which is updated via an SDS loss. For stochastic One-DP, an addition network is learned to approximate the score.

### Strengths
The paper is relatively straightforward. The contribution presented in this paper is limited, because the tasks presented don’t necessarily require such dynamic control and fast inference. However, the results seem reasonable, and the distillation approach is different from Consistency Policy.

OneDP consistently outperforms Consistency Policy. It matches DDPM / EDM, for the most part.

### Weaknesses
1. The contribution is limited. Although faster inference is a worthy contribution for imitation learning, none of the tasks, neither sim nor real, necessitate faster inference. If existing imitation learning algorithms can solve these tasks with their existing control frequency, what necessitates faster inference? What would be convincing is if there were tasks that genuinely required responsive, closed-loop control.
2, Figure 2 is unclear. In part a, it is unclear what the action generator is optimizing exactly. Part b seems to make more sense, although it is not immediately clear from the figure what the authors are trying to convey. The paper could benefit from a clearer diagram on both ends.
3, The input and output of the generator and action generator are unclear. 
4. In the introduction, it is unclear the difference between the generator and action generator. Which one is actually being used as the policy?
5. Typo Line 212: “prertrained” should be “The parameters of the pretrained diffusion policy are fixed”

### Questions
1. In Section 2.2 Line 203, why can’t you obtain the score for Equation 1? Why do you have to learn an auxiliary diffusion network? This feels unnecessary and computationally burdensome, if you are training three separate identical diffusion models (since the generator and action generator are initialized from the pretrained DP). 
2. What is the input and output of the generator? The generator is defined as an implicit policy and a one-step policy. Since the generator is initialized from Diffusion Policy parameters, is the time embedding (e.g. noise timestep 0, … 100) simply set always to 1? Or 100? Is the output just the predicted noise? 
3. Why not learn an explicit policy and use the SDS loss?
4. How would distilling Diffusion Policy into a smaller DP model perform? For instance, reduce the number of parameters for DP and train it to match the pretrained DP outputs. DDIM with 10 steps should be faster due to the smaller size of the smaller DP model. 
5. What is a deterministic action generator? Is z simply set to 0? 
6. Is Diffusion Policy natively 1Hz? Even large VLAs like OpenVLA or Octo can run at 5Hz… Where exactly does this number come from?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Summary:

This paper proposes a One-step Diffusion Policy (OneDP) that distills a pretrained diffusion policy into a single-step action generator by minimizing the KL divergence along the reverse chain. 
Experiments on the robomimic benchmark and real-world tasks show that OneDP reduces inference time while maintaining state-of-the-art success rates.

### Strengths
Strengths


1) High inference time is a major limitation of diffusion policies. The proposed OneDP demonstrates less inference time through distillation.

2) OneDP introduces a weighted score estimation method from Diffusion-GAN to address the intractable KL divergence during the diffusion process.

3) The authors integrate the proposed distillation algorithm with two scheduling methods for discrete and continuous denoising time spaces.

### Weaknesses
Weaknesses

1) The contribution of this method is unclear, as score distillation sampling is well-explored in prior text-to-3D research. The paper does not discuss the differences between VSD and OneDP, nor does it consider the temporal control characteristic in OneDP.

2) Training an auxiliary diffusion network could increase computational costs and optimization complexity. Could the author provide further details on the computational costs and optimization complexity introduced by the generator score network?

3) Distilling to a deterministic policy may diminish the stochastic advantages of diffusion policies.

4) The claim that the student policy slightly outperforms the teacher policy is interesting. However, it requires further discussion and empirical validation.

### Questions
Questions

1) The clarity of the Method section could be enhanced by using consistent terminology for the auxiliary diffusion network in Lines 204 and 222. Additionally, consider removing some unnecessary subscripts in equations such as (5) and (8). Relocate expressions like $A_{\theta} = G_{\theta}(z, O), \quad z \sim N(0, I)$ to a "where..." explanation following the equation if needed.

2) About  “OneDP-S even slightly outperforms the pre-trained DP”.

    2.1 In Lines 345-347, the authors claim that “OneDP-S even slightly outperforms the pre-trained DP” and provide an explanation. However, this slight improvement may be due to stochastic effects caused by limited training seeds, as indicated by results in Square-mh, Square-ph, and Transport-ph in Table 1. Will this empirical ranking hold if the environment initialization state is expanded (both in the numbers and range)? 
    
    2.2 Additionally, the authors' explanation requires further discussion. If the improvement stems from the pre-trained diffusion model (teacher) accumulating more errors, this suggests the teacher is not overfitted to the training set. Then, how could the student policy outperform the teacher? Including results on the training scenarios may offer further insights.

3) There is a lack of empirical results on inference efficiency. The authors should include comprehensive comparisons of inference efficiency between OneDP, the original diffusion model (DDPM), and other distillation methods like DDIM, CP, and Progressive Distillation (Salimans & H, 2022), using simulation experiments (if real-world ones are expensive).

### Soundness
3

### Presentation
2

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
This work proposes an inference-efficient diffusion policy by distilling a pre-trained DP into an action generator with one-step inference. It greatly improves the practicality of DP methods in real-world tasks, especially for responsive tasks.

### Strengths
1. This work tackles a popular yet significant problem concerning accelerating inference in diffusion policy.
2. The authors conduct extensive experiments on visuomotor tasks in both simulation and real world.
3. The idea is straight-forward and the paper is well-written and easy to follow.

### Weaknesses
1. Consistency Policy (CP) [1] in the real world is missing in the experiment part, which can be a representative baseline considering accelerating DP. An additional experiment can be added to compare OneDP with CP in terms of inference speed and success rate.
2. More experiments on responsive or dynamic tasks can be added in the experiment part since potential application on responsive or dynamic tasks is a contribution of this work. A simple example can be randomly resetting the object pose sometime during the task execution.

### Questions
1. A reverse KL is employed to align the distributions of the action generator and pre-trained DP, which is known to induce mode-collapse problems. How does the reverse KL affect the multi-modal property of DP? 
2. I am confused about the fourth bar chart in Figure 1. Since OneDP requires first pre-training a DP, it seems confusing that the training cost of OneDP can be lower than DP itself; in other words, only considering the distillation procedure in OneDP can be an unfair comparison with DP in terms of training cost. Can you explain how you are measuring and comparing the training costs between OneDP and DP?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposed One-Step Diffusion Policy (OneDP) to reduce inference time through diffusion distillation. The method outperforms diffusion policy in both simulated and real-world environments.

### Strengths
- The proposed approach is straightforward and easy to follow.
- The method is evaluated on a wide range of tasks in both simulation and real-world.
- The paper is well written and easy to follow.

### Weaknesses
 - The method of distillation follows the methodologies in image generation. The novelty is limited.
- Only one baseline (DDIM in Tab. 1 and CP in Tab. 2) is compared. There are many methods speeding up diffusion models that can be compared.


### Questions
- What are the limitations of OneDP?  (like ability on modeling mutimodality, capacity, etc.)
- Can the authors elaborates on why stochastic policies perform better in complex environments compared to deterministic ones? The stochastic policies seem to outperform deterministic ones in all the tasks.

### Soundness
3

### Presentation
3

### Contribution
2
