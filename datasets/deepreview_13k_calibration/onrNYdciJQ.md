# Improving Consistency Models with Generator-Induced Flows

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 3, 8

## Abstract
Consistency models imitate the multi-step sampling of score-based diffusion in a single forward pass of a neural network.
They can be learned in two ways: consistency distillation and consistency training. The former relies on the true velocity field of the corresponding differential equation, approximated by a pre-trained neural network.
In contrast, the latter uses a single-sample Monte Carlo estimate of this velocity field.
The related estimation error induces a discrepancy between consistency distillation and training that, we show, still holds in the continuous-time limit.
To alleviate this issue, we propose a novel flow that transports noisy data towards their corresponding outputs derived from the currently trained model --~as a proxy of the true flow.
Our empirical findings demonstrate that this approach mitigates the previously identified discrepancy.
Furthermore, we present theoretical and empirical evidence indicating that our generator-induced flow surpasses dedicated optimal transport-based consistency models in effectively reducing the noise-data transport cost.
Consequently, our method not only accelerates consistency training convergence but also enhances its overall performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper identifies a previously overlooked discrepancy between training and distillation in consistency models and introduces a novel approach called generator-induced flows to address it. This method improves model convergence speed and performance. Additionally, to tackle the distribution shift issue between independent coupling (IC) and generator-induced coupling (GC), the paper proposes a mixed training strategy, resulting in efficient and high-quality image generation.

### Strengths
- This paper is well-structured and easy to read. Each section clearly states its claims and conclusions, making it easy to understand.
- The Generator-Induced Coupling introduced by the authors is very straightforward and serves as a convincing method for resolving the discrepancy. Additionally, the paper's contribution is significant, as it points out aspects of the discrepancy that have been overlooked in previous studies.
- The proposed method surpasses the state-of-the-art iCT, demonstrating high practicality and effectiveness. Therefore, I believe this paper should be accepted.

### Weaknesses
The main difficulty of the proposed method in this study lies in the dilemma that, while aiming to reduce the discrepancy by predicting endpoints from the model, the model itself is still being trained and thus has weak performance as an endpoint predictor, leading to distribution shifts. To address this, the authors propose mixing IC and GC during training, but this solution is a compromise supported mainly by empirical evidence, and introduces a new challenge in determining the appropriate mixing ratio as a tunable parameter. Furthermore, the paper does not fully explore the theoretical implications of these distribution shifts, particularly how they might affect the convergence properties of the model. The mixing strategy, while effective, lacks a deeper justification beyond empirical success, leaving open the question of whether there are more principled ways to mitigate the distribution mismatch between IC and GC.

### Questions
- Could you please explain more about the "weak $g_\phi$ partially-trained as iCT-IC" mentioned in Section 5.2? Does this imply that the endpoint predictor is trained on both GC and IC, similar to the final proposed method?
- The performance of varying $\mu$ values on CIFAR-10 is shown in Figure 10, but what about the performance on other datasets with different mixing rates? I would also like to know how sensitive this parameter is for other models.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper, "Improving Consistency Models with Generator-Induced Flow," studies the coupling mechanism used in training consistency models. Consistency models are a recently developed class of generative models that learn to perform the multi-step sampling of score-based diffusion in a single forward pass.Instead of relying on sampling trajectories from a pre-trained diffusion model, consistency training uses stochastic interpolation between the data distribution and noise distribution, known as independent coupling (IC). This approach shows a discrepancy from consistency distillation. The authors analyze the differences between consistency training under IC and consistency distillation. To address the limitations of IC, the paper proposes a new type of flow called generator-induced flow, which relies on generator-induced coupling (GC) for training consistency models. This proposed generator-induced coupling accelerates convergence and enhances model performance compared to the base IC method and optimal transport approaches.

**Theoretical Results**

- This paper characterizes the discrepancy between consistency distillation and consistency training in values and gradients using different couplings. 
- Under mild conditions, the loss values differ between consistency distillation and consistency training for distance functions other than the standard L2 loss. 
- Though the limiting gradient in the continuous time coincides with the L2 metric, the gradient of the limiting loss values still differs due to the error term when using the independent coupling (IC).
- Authors show that the proposed GC could reduce the discrepancy between consistency training and consistency distillation.

**Algorithmic Improvements**

- The authors discuss potential couplings that could reduce the gap with the velocity field.
- The paper introduces generator-induced coupling (GC) that capitalizes consistency models to approximate the velocity field.

**Empirical Performance**

- The proposed GC adds an affordable cost to training while reducing the transport cost on CIFAR10 compared with batched optimal transport and independent coupling.
- The mixed strategy using IC and GC achieves improved FID compared with IC and batched OT baselines.

### Strengths
- The theorectical analysis investigates the discrepancy between consistency distillation and consistency training. This analysis is novel for understanding consistency models.
-  The proposed generator-induced coupling (GC) is cost-effective compared to other methods like optimal transport (OT).
- This paper is well-written. The logical flow from the consistency model definition to the theoretical results on the gradient discrepancy, followed by the generator-induced coupling (GC) for reduced transport cost.
- The analysis and experiments on the transport cost induced by different couplings are helpful for understanding.
- Key insights are clear and discussed in detail. For example, theorem 1 characterizes the discrepancies between consistency distillation and consistency training under IC. This is a clear motivation for the proposed method. The authors also discuss the implication of this analysis, showing how coupling could lead to different transport costs for consistency models.

### Weaknesses
 - The paper acknowledges that consistency models trained exclusively on GC can suffer from distribution shift issues. Specifically, the marginal distribution shift between IC and GC during intermediate timesteps affects performance. Using a pre-trained consistency model through independent coupling could avoid divergence points to an inherent limitation but largely increase the computational cost.

- While the mixed IC-GC strategy helps mitigate this, the need for careful balancing complicates its application.

- The baseline used in the current draft is a relatively weak benchmark modified from iCT-IC. The mixed strategy of GC and IC improves upon this baseline only by a small margin. It is unclear whether these improvements would diminish when compared to the standard iCT-IC or iCT-OT. Including ReFlow [1] as a baseline coupling for comparison would strengthen the analysis. Additionally, conducting comparisons with efficient benchmarks like ECMs [2] for larger model sizes and comparing them with the standard iCT-IC would provide a better evaluation.

While I acknowledge that this paper presents interesting insights into analyzing consistency models, the proposed generator-induced coupling is less attractive in practice and may suffer from distribution shifts. Therefore, I am not fully convinced of its practical impact at this stage.

### Questions
Some of these questions have been already mentioned in the weaknesses.

It would be helpful if the authors could discuss the following questions.

- Why does the distribution shift occur specifically at intermediate timesteps between IC and GC trajectories? 
- When generator-induced coupling (GC) improves convergence speed, the model reaches saturation early during training. Is there a deeper analysis of why this phenomenon occurs?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the estimation error in the single-sample Monte Carlo estimates in the consistency training. The authors show that in the continuous-time limit, there exists a discrepancy between consistency training and consistency distillation (consistency distillation uses a pre-trained model to sample adjacent points instead of a single-sample Monte Carlo estimate. To remedy this issue, the authors propose generator-induced flows, which introduce a correlation between noise and the data at $t=0$. Experiments on image datasets show that the coupling leads to improved performance.

### Strengths
- The paper studies a new way of sampling the "clean" data in consistency training. The clean data $\hat{x}_0$ are online predictions of the current neural network, given $x_t \sim p_t$ , where $x_t=x_0+t z, x_0 \sim p_0, z \sim N(0,I)$. In this way, it introduces a "generator-induced coupling" (GC) between $\hat{x}_0$ and $z$

- The paper studies the distribution shift between independent coupling in the original consistency training and the GC. The authors propose a mix-training strategy to overcome this issue.

- Experimental results show that the mix-training strategy gives best results across image datasets.

### Weaknesses
 - The paper has severe flaws in the main theorem (theorem 1) and the algorithm. I kindly request the authors to address them carefully or correct me if I'm wrong:

1.  The time derivative of the CT model (Eq.9 in theorem 1) is incorrect. Indeed, when the CT converges, $\dot{x}_t = v_t(x_t)$, as the CT will learn ground-truth ODE instead of "single-sample estimate" (please refer to the proof in the original consistency model paper). The idea is very similar to how the denoising score-matching objective works: the posterior of the "single-sample estimate" gives a ground-truth score, and CT is theoretically sound in the continuous-time limit. Also, the authors keep referring to the time derivative $\dot{x}_t$ as a "single-sample estimate", which is quite confusing. Could the authors crisply state the exact mathematical formulation of $\dot{x}_t$ in the theorem?

2. As the theorem is incorrect, so is Algorithm 1. Think of a counter-example in Algorithm 1: the current online model $f_\theta$ only maps all the intermediate points $x_t$ to a certain class, say "dog" class. As a result, the model will only learn to generate the doggy images since the algorithm replaces the clean data with the generated one by $f_\theta$. This scenario is very likely, as the initial $f_\theta$ likely drops many modes in the data distribution when $t$ is relatively large --- once it drops the modes, these lost modes will never be recovered.

3. The observations in Fig.4a and Fig.4b can be easily explained by the point 2 above. The authors utilize a hacky way (mix-training) to fix this.


- Despite the flaws discussed above, the proposed algorithm seems to improve over baseline on several image datasets. I think there are two possible reasons:

1. The current FID is in a poor regime, and the baselines are not well-tuned. For example, the iCT model can achieve a FID < 3 on CIFAR-10, instead of >7 in the paper. These poor FIDs make the results look unliable. In addition, could the authors test the results on ImageNet-64? This dataset is more representative than the datasets used in the paper.

2. There are some other benefits of using the generator-induced clean data. For example, the online $f_\theta$ could potentially "purify" the samples, e.g., make the samples more smooth. These purified data distributions at $t=0$ are easier to learn in the CT setting. It's analogous to training a model with soft labels instead of one-hot labels. I wonder what the authors' view on this is.

### Questions
Please see the weakness section above.

### Soundness
1

### Presentation
2

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
The paper gave a negative answer to the  resorbent in the continuous-time limit of the discrepancy between consistency distillation
and training. Further, they had a new disovery that the an induced flow inside the generator, which could be used to train a consistent model.
They conducted great work on verifying their discovery in theory.

### Strengths
A very nice work on observation and anlysis  that showed some very interesting insight on CM. It remove an unclear fact about the CMs, which will be very useful for later discussions.

### Weaknesses
The experiments are not extensive. To make the observation and analysis more convining, the authors may try more datesets with different iamge sizes, and more imange generation metrics as those in paper in Ho 2020, Song 2021, Karras 2022, LIu 2023 et. al.

### Questions
It will be better to give some  high-level intuitive explanation of the key ideas behind the mathematics in the proofs; e.g., Lemma 1 and its restatement

### Soundness
3

### Presentation
3

### Contribution
3
