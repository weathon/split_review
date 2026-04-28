# Denoising Task Routing for Diffusion Models

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
Diffusion models generate highly realistic images by learning a multi-step denoising process, naturally embodying the principles of multi-task learning (MTL).
Despite the inherent connection between diffusion models and MTL, there remains an unexplored area in designing neural architectures that explicitly incorporate MTL into the framework of diffusion models.
In this paper, we present Denoising Task Routing (DTR), a simple add-on strategy for existing diffusion model architectures to establish distinct information pathways for individual tasks within a single architecture by selectively activating subsets of channels in the model.
What makes DTR particularly compelling is its seamless integration of prior knowledge of denoising tasks into the framework:
(1) Task Affinity: DTR activates similar channels for tasks at adjacent timesteps and shifts activated channels as sliding windows through timesteps, capitalizing on the inherent strong affinity between tasks at adjacent timesteps.
(2) Task Weights: During the early stages (higher timesteps) of the denoising process, DTR assigns a greater number of task-specific channels, leveraging the insight that diffusion models prioritize reconstructing global structure and perceptually rich contents in earlier stages, and focus on simple noise removal in later stages.
Our experiments reveal that DTR not only consistently boosts diffusion models' performance across different evaluation protocols without adding extra parameters but also accelerates training convergence.
Finally, we show the complementarity between our architectural approach and existing MTL optimization techniques, providing a more complete view of MTL in the context of diffusion training. 
Significantly, by leveraging this complementarity, we attain matched performance of DiT-XL using the smaller DiT-L with a reduction in training iterations from 7M to 2M.
Our project page is available at \href{https://byeongjun-park.io/DTR/}{https://byeongjun-park.io/DTR/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces Denoising Task Routing (DTR), an add-on strategy for diffusion models that incorporates multi-task learning (MTL). The proposed channel masking strategy effectively boosts performance without introducing any extra parameters. The experiments demonstrate consistent improvement across evaluation protocols.

### Strengths
1. The proposed routing mask strategy is interesting as it leverages the task similarity between adjacent timesteps. 

2. The experiment conducted in this study is comprehensive and demonstrates significant performance improvement.

### Weaknesses
1. The idea of considering diffusion models as multi-task learning has previously been proposed by Hang et al. (2023) and Go et al. (2023a). The proposed masking strategy in this work is a simple modification of TR (Strezoski et al., 2019). Its novelty is limited.

2. It lacks an ablation study to evaluate the necessity of the proposed masking strategy. Ding et al. (2023) propose to divide channels into shared channels and task-specific channels. Assigning each time-step cluster (Go et al., 2023a) to the respective task-specific channels can serve as an important baseline.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Denoising Task Routing (DTR), a simple add-on strategy for existing diffusion model architectures to establish distinct information pathways for individual tasks within a single architecture by selectively activating subsets of channels in the model. The authors incorporate two prior knowledge aspects of diffusion-denoising tasks—task affinity and task weights—into the model architecture design to mitigate the negative transfer phenomenon. The paper provides empirical results on several image generation tasks and a qualitative analysis to validate the effectiveness of DTR.

### Strengths
* The paper effectively addresses the negative transfer phenomena by establishing task-specific pathways for multiple denoising tasks. The concept of integrating key prior knowledge in diffusion and task routing is well-presented and could potentially influence future work on architecture design in diffusion models.
* The implementation, although simple, is effective and yields significant performance gains on multiple benchmarks.
* The paper is structured well, making it easy to understand and follow.

### Weaknesses
 * The empirical analysis could be more comprehensive in decoupling the contributions of task weights and task affinity. As I understand, the results in Figure 4 only ablate the significance of the synergy of the two priors. To study the direct contribution of **Task Weights**, it would be helpful to compare `DTR with random routing but task-dedicated allocation channels` with `Random Task Routing (R-TR)`. Similarly, to study the contribution of **Task Affinity**, a comparison between `DTR with task-unified allocation channels but sliding window channels` and `R-TR` would be useful.
* The paper does not adequately explain the sensitivity of DTR to different masking strategies. The authors should elaborate on why they chose Equation (4) as the masking strategy and discuss potential alternatives.

### Questions
* Would DTR achieve better performance by reducing the overlap channels at higher timesteps? Given the authors' assertion in Figure 6 that "at higher timesteps, the model primarily focuses on learning discriminative features that are relevant to specific timesteps, whereas at lower timesteps, the model tends to exhibit similar behavior across different timesteps," it appears that denoising tasks at higher timesteps have less correlation. Would assigning these tasks entirely distinct channels be beneficial?
* Is there a typographical error in Equation (4)? Should the first $t$ be replaced with $t-1$?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, diffusion training is cast as multi-task learning, where each task corresponds to the denoising task at a specific timestep. The authors present Denoising Task Routing (DTR), a simple add-on strategy for existing diffusion model architectures to establish distinct information pathways for individual tasks within a single architecture by selectively activating subsets of channels in the model. Besides, the channel partitioning considers task affinity and task weights in diffusion models. Extensive experiments demonstrate the effectiveness and efficiency of the proposed method.

### Strengths
1. This paper proposes a simple add-on strategy for existing diffusion model architectures, which is simple yet effective, without introducing additional parameters, and contributes to accelerating convergence during training.
2. Extensive experiments demonstrate the effectiveness and efficiency of the proposed method.
3. The paper is well-written and easy to follow.

### Weaknesses
1. Some advanced routing methods [1, 2] improve the random routing by considering the inter-task relationship. Hence, it is better to discuss and compare the proposed method with them.

2. In Figure 9, the images generated by the baseline (the first row) look very strange and both R-TR and DTR methods alleviate it (the second and third rows). So why the random routing method can work well? In particular, in the fifth case/column, the image generated by R-TR looks better than the one generated by DTR. Why?

### Questions
Please address my concerns in the "Weaknesses" section.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
