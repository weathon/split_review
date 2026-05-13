# DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
The ability to predict future outcomes given control actions is fundamental for physical reasoning. However, such predictive models, often called world models, have proven challenging to learn and are typically developed for task-specific solutions with online policy learning. We argue that the true potential of world models lies in their ability to reason and plan across diverse problems using only passive data. Concretely, we require world models to have the following three properties: 1) be trainable on offline, pre-collected trajectories, 2) support test-time behavior optimization, and 3) facilitate task-agnostic reasoning. To realize this, we present DINO World Model (DINO-WM), a new method to model visual dynamics without reconstructing the visual world. DINO-WM leverages spatial patch features pre-trained with DINOv2, enabling it to learn from offline behavioral trajectories by predicting future patch features. This design allows DINO-WM to achieve observational goals through action sequence optimization, facilitating task-agnostic behavior planning by treating desired goal patch features as prediction targets. We evaluate DINO-WM across various domains, including maze navigation, tabletop pushing, and particle manipulation. Our experiments demonstrate that DINO-WM can generate zero-shot behavioral solutions at test time without relying on expert demonstrations, reward modeling, or pre-learned inverse models. Notably, DINO-WM exhibits strong generalization capabilities compared to prior state-of-the-art work, adapting to diverse task families such as arbitrarily configured mazes, push manipulation with varied object shapes, and multi-particle scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a visual dynamics learning approach called DINO-WM, leveraging pre-trained DINOv2 latent features for predictive modeling. DINO-WM incorporates a visual transformer that processes DINO features and action sequences to forecast future observations in an auto-regressive manner, trained through teacher forcing. The model demonstrates zero-shot planning capabilities when integrated with MPC using CEM. The study evaluates DINO-WM across a diverse set of tasks—PointMaze, PushT, Rope, and Granular Manipulation—and achieves 
better performance compared to state-of-the-art model-based reinforcement learning approaches.

---

post rebuttal: The authors addressed several concerns. Though I am still worried about the novelty but I will not argue for a rejection as the contribution of the paper is clear. So I increased my score.

### Strengths
- Effectively leverages a pre-trained vision model to enhance world model learning.
- Conducts comprehensive evaluations across multiple tasks, validating the model's effectiveness.

### Weaknesses
 - The paper's writing needs to be improved. The citations should be clearly separated from the main text using brackets when needed.
- Although DINO-WM uses DINOv2's latent features, the approach of learning a visual dynamics model in the latent space is not groundbreaking. Pretraining latent features for world model learning or learning latent world models through rewards are both exploited in previous literature. Leveraging existing vision models is not novel to me.
- In one comparison, the authors evaluate TD-MPC2 without rewards, which might not provide a fair assessment. Since reward signals are central to TD-MPC2’s optimization, omitting them potentially undermines its performance.
- The work does not include results on established image-based RL benchmarks, such as DM-Control or Minecraft, which are widely used to validate model-based approaches like TD-MPC2 and Dreamer. Including these benchmarks would strengthen claims of general applicability​.
- The model’s lack of Q-learning hinders its capacity to handle tasks requiring long-term planning. In RL, Q-learning or similar approaches are often necessary for efficiently solving complex, high-horizon tasks. This limitation may affect DINO-WM’s scalability to challenging environments.​

### Questions
- I wonder what causes the low performance of TDMPC, is the reward fully ignored or the reward depends on the latent representation that it just learned?

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
4

### Summary
The authors present a world model to facilitate solving control problems in the physical world. The world model learns the dynamic of the environments in the latent space based on pre-trained DINOv2 that extracts both spatial-aware and object-centric latent representation from 2D images. The approach enables gradient-based trajectory optimization at inference time to deal with various control problems (maze navigation, robot manipulation, etc.). Moreover, it achieves so by only using offline trajectory data during model learning.

### Strengths
+ The proposed world model learns to generalize to different variants of several tasks (maze navigation, robot manipulation, etc.) by using only the offline trajectory data. This makes it a potential candidate for training robot foundation models with large quantities of offline data.
+ The trajectory optimization-based test-time control enabled by the proposed world model achieves good results in a range of navigation and manipulation tasks.
+ The comparison of DINOv2 over others (e.g., R3M) as the pre-trained backbone for the world model gives us insights into how good these visual foundation models are for facilitating solving control problems.

### Weaknesses
 - As the authors have pointed out, latent world models are not a new thing. While the proposed framework might be unique in terms of a reconstruction-free reward-free latent-space world model, I do feel the overall novelty is a little bit limited here.
- While the authors have shown results on a range of control tasks, IMO they are more or less 2D tasks (e.g., in the particular manipulation the particles mostly move on a plane). I am curious how will the approach perform for more complicated manipulation or control tasks (e.g., Humanoid Run from DMControl and Move Chair from ManiSkill2). These tasks might require a much more accurate level of physical reasoning capabilities (objects have momentum and move in a more complex way) which can help us understand better the limit of DINOv2.

### Questions
- What is the inference speed of the framework? This show how well they can potentially deal with tasks that heavily require reactive controls.
- Missing references to some recent work that uses Transformers [1] or Diffusion Models [2] to learn to perform latent/visual planning for control problems from offline data.

[1] Chain-of-Thought Predictive Control

[2] Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes Dino-WM a method to model visual dynamics without reconstructing the visual world by leveraging patch features from pretrained visual encoder DinoV2, allowing it to learn the world model from offline datasets of trajectories. This formulation allows Dino-WM to realize observational goals by using action sequence optimizing enabling task-agnostic behavior planning. The paper demonstrates Dino-WM can generate solutions for tasks at test-time zero-shot without any expert demonstration, reward modeling or inverse dynamics models. In addition, Dino-WM outperforms existing methods like DreamerV3 and TD-MPC2 on complex control environments. Additionally, paper present additional analysis on using various pretrained visual encoder for world modelling to demonstrate effectiveness of using DinoV2 features and show generalization to novel environment configurations.

### Strengths
1. The paper is well written and easy to follow
2. The idea proposed in the paper is quite simple, scalable and effective as demonstrated by the results. 
3. The experiments section is thorough and clearly demonstrates effectiveness of Dino-WM compared to existing methods.

### Weaknesses
1. The authors argue in the intro and abstract of the paper that a world model should enable learning from **only passive data** but the experiments demonstrated in the paper always require action metadata during training of Dino-WM which contradicts the motivation. I’d suggest authors to make that argument a bit less constrained to convey the world model training should include both passive and action conditioned data.
2. The comparisons presented in experiments section 4.1 do not include comparisons to diffusion based methods. I understand it might not be feasible to get results for all environments but I’d recommend authors to add comparison of AVDC or another diffusion based methods for whichever task possible in table.1. If not possible, I’d recommend authors to add a discussion about why the comparison is not possible. Currently, the section 4.2 implies there’ll be quantitative comparison with diffusion based methods.
3. The generalization experiments in section 4.5 tests generalization to unseen configurations of environments seen during training but the description in section 4.5 (L 450-451) implies that experiments test generalization to new environments on which the model was never trained which is not true. I’d recommend authors to please fix the text description in this section. 
4. I couldn’t find any training details for world models used in experiments section. It is not clear to me what datasets were used for training Dino-WM, how were the trajectories collected, what was the scale of those datasets,etc.  The appendix has hyperparam details but no training details. It’d be great if authors can add description for those details in the paper. 
5. I would also be interested in seeing scaling laws analysis for the a subset of environments presented in the paper. It’d be interesting to see how evaluation performance improves as the size of training dataset used for Dino-WM pretraining was used. I believe it will make paper stronger and would be a nice analysis to have.

### Questions
In addition to AVDC there are more recent WM style methods based on generative methods like Genie [1] that work quite well. I'd like authors to either present comparison with this method or add a discussion addressing why the comparison is not possible.

[1] Genie: Generative Interactive Environments

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
5

### Summary
This work proposes a simple approach for learning a task-agnostic world model from offline data. They use frozen DINOv2 tokens and a Transformer transition model with a single-step forward prediction loss. This world model is then shown to enable model predictive control in toy environments as well as two simulated robotic environments involving manipulating a rope and many particles.

### Strengths
1. The authors demonstrate that frozen visual tokens from DINOv2 are enough to learn a forward model that successfully predicts the dynamics of several different robot control environments.
2. It is further shown that the world model is able to plan in altered environments because, in part, it does not depend on a task-specific reward function.
3. The proposed world model compares favorably to task-specific world models, DreamerV3 and TD-MPC2, and its decoder generates more plausible trajectories than a prior video prediction method, AVDC.
4. The rope and granular manipulation environments demonstrate the simulation of difficult transition dynamics.

### Weaknesses
1. The paper includes an insufficient set of benchmarks. I would recommend including more standard reinforcement learning and robotics benchmarks, such as DMControl, RoboMimic, MimicGen, RLBench, MetaWorld, FrankaKitchen, ManiSkill, etc. These benchmarks would better assess the world model’s ability to capture robot-object dynamics and sequential tasks. For example, the TD-MPC2 paper (used as a baseline) includes MetaWorld, DMControl, ManiSkill and MyoSuite as benchmarks. It would only be fair to compare the proposed method on some subset of the benchmarks used in TD-MPC2 or DreamerV3. I would recommend adding at least one benchmark from TD-MPC2 to strengthen the comparison. E.g., MetaWorld covers a diverse set of manipulation tasks.
2. The paper focuses on learning task-agnostic world models from offline data, but this entails a major assumption. It is assumed that the training dataset sufficiently covers the environment’s state-action space. This appears to be the case in Point Maze, Two Room, Rope Manipulation and Granular Manipulation, where the datasets are collected by executing random actions. This would not work in, e.g., RoboMimic or FrankaKitchen, where the agent has to execute a sequential task that is difficult to solve with random actions. Here, we have a chicken-and-egg problem. We need an expert dataset to train an accurate world model, but we need an accurate world model to plan expert behavior. This is why prior world modeling approaches focus on online improvement and joint learning of world models and policies.
3. I am confused by the first sentence of Section 3.1.2. It states that the ViT model is used as the transition model. But ViT is just a Transformer with tokenized images and the input to the transition model is already tokenized. Wouldn’t it be more accurate to say that a decoder-only Transformer is used as the transition model?
4. Section 3.1.2 further describes a causal masking approach of treating patch vectors of one observation as a whole unit. This design decision should be ablated in the experiments. In particular, comparing the planning success rate of DINO-WM with and without the per-image causal mask.
5. The comparison with baselines would be more fair if DreamerV3 and TD-MPC2 were modified to also use a DINOv2 image encoder, which I assume is not the case in the current experiments. Could you swap the convolutional encoder of DreamerV3 with DINOv2 and measure the impact on its planning success rate?
6. Embed to Control (https://arxiv.org/abs/1506.07365) is a major missing citation, which also investigates offline world model learning without rewards.

### Questions
1. The decoder could propagate gradients into the transition model if you first predicted the next state, then decoded it and compared it to the original next state image? Have you considered this design decision?
2. Some world modeling approaches roll out trajectories N steps into the future to improve the consistency of predictions over time. Would that be compatible with your approach?
3. Do you fine-tune AVDC on your datasets?

### Soundness
3

### Presentation
3

### Contribution
2
