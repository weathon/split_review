# Denoising Task Difficulty-based Curriculum for Training Diffusion Models

- Decision: Accept
- Scores: 6, 6, 6, 8, 6

## Abstract
Diffusion-based generative models have emerged as powerful tools in the realm of generative modeling. 
Despite extensive research on denoising across various timesteps and noise levels, a conflict persists regarding the relative difficulties of the denoising tasks. 
While various studies argue that lower timesteps present more challenging tasks, others contend that higher timesteps are more difficult. 
To address this conflict, our study undertakes a comprehensive examination of task difficulties, focusing on convergence behavior and changes in relative entropy between consecutive probability distributions across timesteps.
Our observational study reveals that denoising at earlier timesteps poses challenges characterized by slower convergence and higher relative entropy, indicating increased task difficulty at these lower timesteps.
Building on these observations, we introduce an easy-to-hard learning scheme, drawing from curriculum learning, to enhance the training process of diffusion models. 
By organizing timesteps or noise levels into clusters and training models with ascending orders of difficulty, we facilitate an order-aware training regime, progressing from easier to harder denoising tasks, thereby deviating from the conventional approach of training diffusion models simultaneously across all timesteps.
Our approach leads to improved performance and faster convergence by leveraging benefits of curriculum learning, while maintaining orthogonality with existing improvements in diffusion training techniques.
We validate these advantages through comprehensive experiments in image generation tasks, including unconditional, class-conditional, and text-to-image generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper notices that the diffusion training at low noise levels is more challenging than at high ones. 
Based on this observation, the authors propose a curriculum learning approach for diffusion models (DMs) that facilitates faster convergence and improves overall performance.

### Strengths
**S1 |** The authors directly answer the question, "Which timestep intervals are more challenging during training?" and provide a convincing analysis for different diffusion parameterizations.
 
**S2 |** The experiments demonstrate that the proposed approach can improve the convergence and final performance of several popular DM methods.

**S3 |** The ablation study explores important questions, such as whether the performance gains persist with larger models and how the approach interacts with other training techniques, e.g., MinSNR loss weighting.

### Weaknesses
 **W1 |** The proposed method has limited scientific contribution: the clustering is adopted from [1], the pacing function, while reasonable, is rather trivial, and the idea behind curriculum learning is pretty general. This could be fine if accompanied by very insightful and comprehensive analysis and strong results. Currently, I feel that the overall contribution is not sufficient.

**W2 |** Most experiments are performed using DiT, which currently seems to be a relatively weak baseline. EDM may also be considered outdated. I believe it is important to apply the proposed approach to EDM2[2] and demonstrate the gains on top of it. EDM2 focuses on training techniques and outperforms DiT and EDM by a large margin. Also, it proposes the dynamic loss weighting, which strongly relates to the proposed approach. 

**W3 |** The analysis is performed only on FFHQ256 while the dataset and image resolution can be important factors as well. For example, [3] observed that larger models are more beneficial at high noise levels for CIFAR10 and ImageNet 64x64, and, in contrast, larger models are preferable at low noise levels for the LSUN dataset. [4] revealed different optimal timestep intervals for various datasets under the same noise schedule. Thus, it seems valuable to perform analyses across different datasets and discuss any observed trends. It would also be interesting to discuss whether pixel and latent spaces exhibit different behaviors.

### Questions
**Q0 |** Please address the concerns and questions in Weaknesses.

**Q1 |** In Section 4.2, the relative entropy analysis indicates that marginal distributions become less similar as $t$ approaches 0. Could the authors elaborate on why this leads to the conclusion that training is more challenging at low noise levels? If I understand correctly, at small $t$, the tasks become more independent, which may limit the model to share knowledge between adjacent timesteps. Does this explanation seem reasonable?

**Q2 |** The method uses the SNR-based clustering. Did the authors consider using gradient-based clustering [1,2] in their approach? Perhaps, it may provide more accurate intervals for different datasets.

### Soundness
3

### Presentation
3

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
The paper proposes a curriculum learning based training of diffusion models, where the model is progressively trained on easier to harder tasks. The authors identify the task hardness based on the timestamps used for the training. For this, they train multiple models, where each model is trained to denoise only a particular subset of timestamp ranges. The loss curve of these models with training steps, depict that model trained on earlier timestamp ranges converges slower than the models trained on later timestamp ranges. Apart from the loss curves, the authors also look at the FID score by sampling from these models during training(to denoise or timestamps other than what the model is trained on, a model trained on all timestamps is used for denoising). Again the FID of models trained on later timestamps is lower than those trained on earlier timestamps. 

Based on these analysis, the authors conclude that denoising for earlier timestamps is harder than denoising for later timestamps. Base on this, the authors then devise a curriculum learning-based training of diffusion models. The model is iteratively trained on later to earlier timestamps(easier to harder tasks) clusters. Instead of uniformly dividing the total timestamp into each cluster, the authors use an SNR-based interval clustering technique. Furthermore, since the hardness of different timestamp clusters varies, so the authors propose a better approach than training on each cluster for a fixed number of steps. They define a maximum threshold hyper-parameter(patience), which determines whether to switch to the next training cluster. If the loss in that cluster stays constant for more than patience steps, then the training proceeds to the next cluster. 

The authors conduct experiments across different diffusion training architectures, such as as DiT, SiT and also over different training datasets such as FFHQ, ImageNet. Across different architectures and datasets, the proposed approach consistently outperforms the vanilla approach of training without a curriculum learning schedule.

### Strengths
* The authors show consistent improvement across a variety of architectures and datasets thus denoting the effectiveness of their approach.

* I like the anti-curriculum learning ablation, where instead of training on easier to harder tasks, the authors instead train on harder to easier tasks which doesn't perform any better than the baseline.

* I like the analysis done by the authors in determining the hardness of different timestamp schedules.

### Weaknesses
I have a few concerns regarding the paper - 

* It seems that the effectiveness of the approach is reduced when the model is trained for longer steps. The difference in performance between the baseline and test after 2M training steps is much smaller than the difference at 400k steps. In that way, the main effectivess of the approach is just faster convergence, instead of improved performance. How do the authors justify the improved performance then?

* Can the authors show comparison between the curriculum and anti-curriculm approach for unconditional image generation also instead of just class-conditional generation?

* The authors should explain more in the paper about the SNR-based interval clustering technique and why it is a better interval technique than uniformly clustering.

### Questions
I have already asked questions in the weakness ection

### Soundness
3

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
This paper aims to improve the learning process of image generation using diffusion models through a technique called curriculum learning. The authors first observed the progress of diffusion model training. They found that denoising images with more noise (larger time steps) is easier than denoising images with less noise (smaller time steps). This was confirmed by examining the convergence of loss functions and FID scores at each noise level.

Furthermore, by analyzing the KL divergence between marginal probability distributions of consecutive time steps, they also demonstrated that the denoising task becomes more difficult with larger time steps.

Based on these observations, the authors adopted a common curriculum learning approach called "easy-to-hard training scheme." Specifically, they proposed a strategy that starts learning from time steps with more noise and gradually expands the range of time steps being learned. This strategy requires designing a "pacing function" to determine how to expand the learning range. The authors adopted a technique that transitions to the next phase based on the status of the training loss.

In experiments, they confirmed that the proposed method improves performance compared to vanilla learning strategies across multiple baseline models. Additionally, they demonstrated faster convergence and orthogonality (i.e., compatibility) with existing learning improvement methods.

### Strengths
The key features of this paper are as follows:

1. The motivation for the research is clearly explained in Section 4 (Observations). In particular, Figures 1 and 2 effectively illustrate the problems that need to be addressed.
2. The proposed method requires the design of a pacing function and scheduling, as described in Section 5.2. However, the core idea itself is simple and elegantly solves the identified problems.
3. In the experimental section, the method is tested on multiple baseline models, confirming that the proposed approach brings improvements in each case. Additionally, appropriate ablation studies have been conducted, suggesting the generalizability of the proposed method.

### Weaknesses
1. While the motivation in section 4 is clear, there is insufficient explanation as to why this method is expected to improve performance. Even though the "easy-to-hard training scheme" is well-known in the field of curriculum learning, the paper lacks discussion on why it works effectively and its connection to theoretical aspects.
2. It is appealing that the proposed method can generally improve upon baselines. However, from my understanding, the reported performance seems to be significantly different from the current state-of-the-art results. While achieving state-of-the-art performance is not mandatory for this type of paper, the lack of discussion about this performance gap raises concerns about the generalizability of the method.
3. This method presents a novel approach in applying curriculum learning to diffusion model training. However, there seems to be a lack of discussion regarding its relationship and comparison with other learning improvement techniques.

### Questions
1. Regarding Weakness 1: Can authors add theoretical justification or explanation, perhaps by citing other curriculum learning literature?
2. Also related to Weakness 1: Diffusion models differ from networks in other curriculum learning literatures in that the time step conditioning changes at each training phase. This might cause behaviors at different time steps (which should ideally be learned independently) to influence each other through shared network parameters. Therefore, I guess that the traditional curriculum learning framework might not fully explain the effectiveness of this method. Can you provide any references or discussion to address this question?
3. Regarding Weakness 2: Can you discuss why the performance of the proposed method is significantly inferior to current SoTA methods? For instance, the latest results on the ImageNet 256x256 dataset had FID scores below 5 as of 2022. (While additional experiments are not expected, if you could demonstrate improvement on a very high-performing model, it would strongly support the claims and effectiveness of this paper's method.)
4. Also related to Weakness 2: From Table 2, it seems that the results in Table 1 are from models that haven't fully been converged. While improved convergence performance is promising, it would be beneficial to show that performance improvements are still observed with further training for other models as well.
5. Regarding Weakness 3: Can you discuss the relationship between the proposed method and other diffusion model learning improvement techniques? For example, while this method is compatible with noise weighting techniques, I feel they might not be completely orthogonal in theory.
6. Can the KL divergence analysis in Section 4.2 be explicitly calculated in the forward process of diffusion?

Additional Notes
1. In the supplementary material, references are not properly cited.
2. When discussing convergence speed, for example in Figure 6, I believe it's important to include data points that show full convergence. Reaching the performance ceiling quickly is an advantage, so demonstrating this would be valuable.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a curriculum-based training schedule for diffusion models that trains the model on progressively increasing task difficulty, which corresponds to different bins of the diffusion noise schedule. The authors provide empirical evidence that task difficulty increases with decreasing time steps (as SNR increases), and provide a simple scheme of dividing the training into difficulty tasks. Results show that the scheme improves the convergence and quality of diffusion samples with no training overhead.

### Strengths
- Dividing training into difficulty phases determined by diffusion timestep clusters is novel to my knowledge. 
- The paper is well structured and the method is well motivated. The presentation of evidence that difficulty varies depending on diffusion timestep (Sec 4) into the proposed method (Sec 5) is well thought and makes the paper flow nicely.
- Comprehensive experiments show improved performance over baselines at same number of training iterations, i.e., with no additional training overhead, with sensible ablations justifying design choices made by the authors.

### Weaknesses
 - Overall the main novelty of the work is on the proposed training schedule, which is simple and on the lower side. Sec 4 is more of an empirical confirmation that lower noise levels is more difficult, which I believe is already well-known. I think this is not a big negative point however, as there is merit to simple ideas that work.
- Some missing citations as the general idea of training diffusion models from easy to difficult tasks is not new. The earliest and most influential ones to my knowledge are progressive distillation [1] (many to few sampling steps) and cascaded diffusion [2] (low to high-res).
- Sec 4.2, it is not clear to me why high KL between marginals of two time steps implies higher task difficulty. I assume it is because higher KL means the model has to make larger changes to the image between timesteps, thus making it more challenging. I think this can be more clearly stated.

### Questions
- Interesting that the anti-curriculum training (hard to easy) can also improve performance over vanilla, even if not consistently (Table 3). Do the authors have insight on why? This might come across as contradictory to the main claims of the paper and I suggest the authors explain it clearly to avoid confusing the reader.
- Might be small typo in line 294. As time step increases, the expression in parenthesis suggests KL increases which contradicts Fig 2.
- It seems like the diffusion community is moving more towards flow/ODE-based/consistency models, rather than DDPM-style models. Have the authors tried applying their method to flow-based methods?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, a new analysis of the levels of difficulty of different parts of diffusion model is presented followed by the introduction of new curriculum-based approach for improved training. Authors first show that it is harder to learn how to denoise samples that are less noisy in the diffusion process. On top of this observation they introduce a new method for the training of diffusion models, where model is first trained with only simpler timesteps, followed by the harder ones and full training. The extensive evaluation validates that such approach leads to better performance of the final model and faster convergence.

### Strengths
- The idea of curriculum learning for faster and more efficient diffusion training is interesting and, to the best of my knowledge, novel. The experimental evaluation is convincing as the method seems to improve the performance of the models across several benchmarks and with different architectures 
- Submission provides interesting experiments in the preliminary observation. I particularly appreciate experiments where part of the sampling trajectory was generated using a separate model trained for a limited period of time. This experiment brings valid observations regarding how challenging the training of earlier/later diffusion steps is. However, there is still one question remaining - what is the influence of the training on the remaining steps on other steps - see the questions section.
- On top of the proposed method and main benchmarking, the authors present an extensive additional experiments section that provides an in-depth analysis of the solution’s strengths.

### Weaknesses
 - I’m left with a single concern. Is it really thanks to the curriculum learning, or is it just important to first learn how to do denoising in the initial steps of the diffusion process - which define the mapping between random Gaussian noise and training data so that later training is easier? Driven by the confusing results of the evaluation presented in Figure 4, I lack one last experiment where the model is first trained using only timesteps from the C_N cluster followed by random ordering or standard training. Would it be significantly worse than the presented approach?
- In Section 5.2 there is a statement that “the convergence rate of each curriculum phase varies significantly, as demonstrated in Fig. 1.” - - - This is true, but I hope that I understand correctly that in the CL scenario, the model is first trained with the easy task, but then the same model is further finetuned with harder tasks. This should affect the convergence speed.
- Figure 4 is very puzzling. It suggests that it actually doesn’t matter how much we split the process used by the curriculum training, the results are almost identical except for the magical 20 splits used throughout the rest of the submission.  It is unclear why the performance is so similar across different numbers of splits, and why 20 splits is optimal. The lack of a clear explanation for this behavior undermines the overall argument for the proposed curriculum learning approach. The precision metric, in particular, shows a concerning drop when the number of clusters is increased to 30, suggesting that the method may not be robust to changes in the granularity of the curriculum.
- Small errors/suggestions: Section 5 describes the Method rather than the Methodology. Table 2, Figure 4 are not within the specified margins

### Questions
- How splitting the process into separate models for separate parts affected the loss convergence? I can imagine that when training a single model on all of the steps, there is some positive/negative transfer between different tasks.
- Are all of the models in the evaluation section trained for the same number of steps? How is it achieved in the CL training with maximum patience iteration that introduces various number of training steps in each CL task?
- The results presented in Table 1 for some methods are relatively close to each other. How many examples were used to calculate FID, are those results statistically significant (as there are no confidence intervals)
- Were all of the models trained with a linear noise scheduler? How would the results be affected by changing it?

### Soundness
3

### Presentation
3

### Contribution
3
