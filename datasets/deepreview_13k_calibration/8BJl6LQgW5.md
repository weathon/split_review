# Visual Representation Learning for World Models by Predicting Fine-Grained Motion

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Originating from model-based reinforcement learning (MBRL) methods, algorithms based on world models have been widely applied to boost sample efficiency in visual environments. However, existing world models often struggle with irrelevant background information and omit moving tiny objects that can be essential to tasks. To solve this problem, we introduce the Motion-Aware World Model (MAWM), which incorporates a fine-grained motion predictor and entails action-conditional video prediction with a motion-aware mechanism. The mechanism yields compact and robust representations of environments, filters out extraneous backgrounds, and keeps track of the pixel-level motion of objects. Moreover, we demonstrate that a world model with action-conditional video prediction can be interpreted as a variational autoencoder (VAE) for the whole video. Experiments on the Atari 100k benchmark show that the proposed MAWM outperforms current prevailing MBRL methods. We further show its state-of-the-art performance across challenging tasks from the DeepMind Control Suite.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents the Motion-Aware World Model. It integrates a fine-grained motion predictor with an adaptive motion-aware scheduler and involves action-conditional video prediction to filter out backgrounds and track object motion at the pixel level.

### Strengths
1. The attention that the authors give to relevant foreground information and moving tiny objects is meaningful for constructing world models.

2. The performance gain of the proposed method is considerable on the Atari 100K benchmark and DeepMind Control Suite.

### Weaknesses
 1. The author elaborates on some details in the method section; however, many technical aspects, like the Convolutional Block Attention Module, were not employed in previous approaches. Nevertheless, the relevant experiments have not undergone ablation, which could readily prompt people to doubt the fairness of the experiments.

 2. The results of the ablation experiments are rather confusing. It appears that MAWM is not consistently the best choice. Moreover, for the majority of the experiments, it doesn't seem that they have reached convergence.

 3. The motivation of this paper is to solve the problem of struggling with irrelevant background information and omitting moving tiny objects. Is there any corresponding visualization to verify this?

 4. Many experimental details are not clearly stated. For example, what are the values of $\alpha$ and $r_{dizzy}$?  

 5. Discussions on limitations are necessary.

### Questions
Please see weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a novel approach in terms of model-based reinforcement learning (MBRL), where an image-based world model is utilized to improve sample efficiency by mimicking a scalable digital copy of the environment, such as DreamerV3. The authors claims that traditional world models tend to ignore moving tiny objects and their connections with tasks, thereby they propose a Motion-Aware World Model (MBRL) to account for them. Specifically, MAWM 1. focuses on small objects via pixel-level attention mechanisms and 2. deals with rapid changes of them via an adaptive control scheduler. The results on Atari 100k and DeepMind Control Suite (DMC) depict the superiority of the proposed method against DreamV3.

### Strengths
The paper presents several strengths:
1. The experimental validation of the proposed model on two standard datasets, Atari 100k and DMC, demonstrates its effectiveness and generalizability.
2. The writing of the paper is clear, making it easy for readers to understand the proposed method and its experimental validation.
3. The details of the model in the appendix are valuable contributions to the community, as it enables other researchers to reproduce the results and build upon the proposed method.

### Weaknesses
1. One concern is regarding the novelty of the proposed two techniques. The motion-aware auxiliary loss is not a novel topic [1]. Additionally, the technical contributions of the proposed pixel-level attention and scheduler are not clear enough to me. Specifically, the paper does not adequately explain how the pixel-level attention mechanism differs from standard attention, or how it is adapted for motion. The adaptive control scheduler also lacks a clear explanation of its novelty; it's unclear how it specifically addresses rapid changes in small object motion beyond a basic adjustment of parameters. The connection between the scheduler and the 'dizziness mechanism' is also not well-established or explained with sufficient technical detail.

2. Is it possible to compare MAWM with pretrained video generation models like stable video diffusion, to figure out whether they can capture the patterns of moving targets or not?

3. I also have some concerns about the experimental results. As an example, Table 1 is confusing. In the last row, the Median score of a counterpart SimPLe is 1.34, which seems to obtain the best results without being marked bold. Besides, the different components proposed in this paper don’t demonstrate convincing improvement in Figure 4. The ablation study in Figure 4 is not sufficiently detailed, and it's difficult to ascertain the individual contributions of each component. The lack of statistical significance testing on the ablation results further weakens the claims. A more comprehensive and significant ablation study, including more tasks and statistical analysis, could help address this.

### Questions
Please see the weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new method for learning the model in model-based RL with special considerations in motion prediction modeling. The authors introduces motion awareness by adding foreground motion prediction and adaptive motion-blur losses over traditional video generative pipelines. The resulting model achieves comparable results against existing MBRL methods.

### Strengths
The proposed motion awareness in model learning is intuitive and the proposed method achieves comparative results with state-of-the-art methods.

### Weaknesses
One concern about this paper is the significance of the proposed method. First, except in curves and Fig.3 from the ablation studies, the authors might want to provide more visualizations on the effect of the motion awareness introduced, especially when considering the current experiment setting is only in atari and dm-control-suite where data are all synthetic and should potentially be simpler compared to real-world videos. Specifically, the paper lacks a clear demonstration of how the foreground motion prediction and adaptive motion-blur losses contribute to improved performance in complex scenarios. The ablation study only shows the overall performance difference, but it does not provide insights into how motion awareness helps the model learn better representations or make more accurate predictions. Second, I wonder if the same pipeline could be applied to real-world videos as currently there is increasing trend in leveraging video generative models as "world models" to facilitate various tasks. It would be better if the authors could find a proper way to compare or address such line of methods. The current experiments are limited to synthetic environments, and it is unclear how the proposed method would perform on real-world data with more complex dynamics and visual variations. Lastly, the paper organization could be improved for better clarity.

### Questions
See the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper tackles the problem that model-based visual RL methods tend to ignore small objects that are essential for tasks while learning irrelevant background information. The proposed approach MAWM introduces a pixel-level loss function based on motion information together with adaptive motion-aware scheduler based on timesteps and video prediction loss instead of image reconstruction as representation learning objective. Authors perform experiments on Atari and DM control benchmarks. Authors compared MAWM to several model-based and model-free RL baselines, and demonstrated improvements averaging across multiple tasks. Ablation studies show contributions of each component in this framework.

### Strengths
1. The proposed approach shows improvements over baselines in benchmark evaluations
2. Authors perform various ablations to demonstrate effectiveness of each component
3. Paper is well structured and experiments are well organized

### Weaknesses
1. The main difference from existing model-based RL methods is an auxiliary objective based on pixel-wise motion information and replacing image reconstruction loss with video prediction objective, both of are not significant changes.
2. Since the motivation of MAWM is to avoid distractions from irrelevant background information, in addition to standard control benchmarks, environments such as distracted DM control [1] and DM control generalization [2] can better demonstrate benefits of the proposed approach than baselines.
3. Current experiments do not quantitatively establish correlation whether proposed approach has more benefits in environments or tasks where objects tend to be smaller, which is a main motivation in method design.

### Questions
1. In ablation study (L486-L491), why video prediction loss instead of image reconstruction loss in MAWM framework is important for DM control experiments but not Atari experiments?
2. What is the intuition and rationale to use an adaptive Gaussian mixture model to extract ground truth label of whether each pixel belongs to foreground or background?
3. How does MAWM compare to MWM [3] that uses MAE objective on convolution features to better learn representations, which is also shown specifically more suitable for small objects?

[3] Seo, Younggyo, et al. "Masked world models for visual control." Conference on Robot Learning. PMLR, 2023.

### Soundness
2

### Presentation
3

### Contribution
2
