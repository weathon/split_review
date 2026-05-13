# AVID: Adapting Video Diffusion Models to World Models

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Large-scale generative models have achieved remarkable success in a number of domains. However, for sequential decision-making problems, such as robotics, action-labelled data is often scarce and therefore scaling-up foundation models for decision-making remains a challenge. 
A potential solution lies in leveraging widely-available unlabelled videos to train world models that simulate the consequences of actions. 
If the world model is accurate, it can be used to optimize decision-making in downstream tasks. 
Image-to-video diffusion models are already capable of generating highly realistic synthetic videos. 
However, these models are not action-conditioned, and the most powerful models are closed-source which means they cannot be finetuned.
In this work, we propose to adapt pretrained video diffusion models to action-conditioned world models, without access to the parameters of the pretrained model.
Our approach, AVID, trains an adapter on a small domain-specific dataset of action-labelled videos. AVID uses a learned mask to modify the intermediate outputs of the pretrained model and generate accurate action-conditioned videos. We evaluate AVID on video game and real-world robotics data, and show that it outperforms existing baselines for diffusion model adaptation. Examples available at \href{https://sites.google.}
Our results demonstrate that if utilized correctly, pretrained video models have the potential to be powerful tools for embodied AI.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a mechanism for adapting current image-conditioned video diffusion models to action-conditioned video diffusion models. They do this by training an additional UNet after the standard video diffusion UNet which predicts an adjustment to the noise output by the standard UNet. Because of this setup, their "adapter" does not need access to the parameters of the pretrained video diffusion model. Experiments show that this kind of noise adaptation helps for some metrics and does not for some others.

### Strengths
- The paper has a nice motivation: how does one adapt existing foundation models in order to add an action conditioning to them, so as to make it more relevant and useful for embodied robotics applications
- The paper writing is clear; first the limitations of prior work are built up and then a solution is proposed

### Weaknesses
 - The way the paper starts with the motivation near L51-52 is a bit misleading. The paper actually cannot fix the issues in L51-52 because they still assume access to the internal inference pipeline of these closed-source model, because if I understand it correctly, this method needs access to a diffusion model's noise prediction at each of the N reverse diffusion steps that happens at inference. For closed source models, this information is not available.
- The performance gain in the quantitative metrics is not substantial. The metrics where the proposed method shines are mostly photometric quantities. It is not clear if the error margin between prior work and this work just results from the standard deviation or variance of the models. I think a better reflection of the proposed approach would have come from an application to a downstream robot task (maybe manipulation) that would evaluate a robot in action. PSNR and other photometric errors with the shown gain do not say much about the performance of the method.
- The paper heavily leans on the limitations of the POE approach and that is how a learnable adapter is motivated but qualitatively there is no comparison to that approach (even though POE is slightly better than the action conditioned diffusion across some metrics and settings).

### Questions
See weaknesses.

### Soundness
2

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
3

### Summary
This paper focuses on the problem setting of action-conditioned video generation. It proposes to adapt pre-trained video generation model to action labeled dataset without access to parameters from pre-trained models. The goal is to add action information as conditioning to pre-trained models for more accurate video predictions. Authors also analyze limitations in previous related work, production of expert, under a specific case. The proposed approach, AVID, trains an adapter in smaller size on action labeled video datasets. It takes noise predictions outputs from pretrained models and action information as input, and learns to output a mask that is used to combine outputs from pre-trained model and adapter. The adapter is trained with reconstruction loss between final output from both models and ground truth on domain-specific datasets. Authors conducted experiments on two robotics datasets, Procgen and RT1, and compared proposed approach to several baselines that have full access and do not assume access  to pretrained model parameters. Experiments results demonstrate that AVID outperforms baselines in generating more realistic videos and better quality given action information on these domains.

### Strengths
1. The paper is well written and easy to follow
2. The main idea of training a lightweight adapter for action-labeled domains is reasonable. It balances finetuning efficiency and task performance.
3. Baseline comparisons are comprehensive. Authors compared to many alternative baselines to demonstrate effectiveness of their approach. Authors provide qualitative visualizations for quality of generated videos and usefulness of learned masks.

### Weaknesses
1. The presentation in Section 3.2 is a little unclear. It is hard to connect analysis about limitations of previous work [1] to motivations of the proposed approach
2. The novelty is somewhat limited. The main difference from previous work is to have domain-specific adapter output an element-wise mask that is used to combine noise predictions from pre-trained model and adapter.
3. The experimental domains are only two datasets within action-conditioned world modeling

### Questions
1. Regarding W1, can authors elaborate more on how and why this analysis motivates design choices in methodology of AVID?
2. In the ablation study of “No mask” (Table 3), is the adapter trained with $\epsilon_{\text{final}}$ given in Equation 5 or the adapter not being able to output a mask?
3. Since the mask is an important component in design choices of AVID, could author visualize what the mask looks like in different timesteps of diffusion denoising process, which corresponds to Figure 4d?
4. Since AVID performs two diffusion denoising process, does this increase inference time and thus limit the scope of downstream applications of synthetic videos generated from this approach?
5. Regarding W3, is it technically possible to apply this approach to domains other than world modeling?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
1. The authors propose a novel method to condition pre-trained video diffusion models on action sequences without access to the pre-trained model's parameters.
2. The authors demonstrate that their adaptation method is superior to the method proposed in "Probabilistic Adaptation of Text-to-Video Models" and mathematically highlight the limitations of this other approach.
3. The authors use different pre-trained base models and two different video domains, games and robotics to quantitatively evaluate their proposed method against the above adaptation approach and some other proposed baselines.

### Strengths
1. The authors propose a novel method to condition pre-trained video diffusion models on action sequences without access to the pre-trained model's parameters.
2. The authors mathematically highlight the limitations of the adaptation method proposed in "Probabilistic Adaptation of Text-to-Video Models" and  this other approach.
3. The authors demonstrate that their adaptation method has better action consistency compared to the other approach, using a new metric that they introduce. 
4. The authors also propose multiple baselines to compare against their proposed method.

### Weaknesses
1. In Table 2, Action conditioned diffusion has a better Action Error Ratio compared to the proposed approach for all three (small, medium, large) variants. While the authors do note this as a limitation, this needs to be explained/investigated more. If it is better to just train an action conditioned diffusion model from scratch why should there be a need to adapt pre-trained models ?

2. Instead of using the action embedding to just scale and shift the t-th frame feature, have the authors explored using cross-attention layers directly with the action embedding sequence similar to language conditioning ? Are there any specific challenges that prohibit such an approach ?

3. It would be interesting to see results for each task type in RT-1 . Are there tasks that are much harder to model than others and what does that tell us about the approach ?

4. Some video visualisations of the generated videos (especially for robotics) would also be very useful to judge the effectiveness of the approach. Are the videos temporally consistent visually ?

5. Why is IRAsim's Action error ratio empty in Table 7 ? is it not possible to evaluate the Action Error Ratio of IRAsim ?

### Questions
see weaknesses.

### Soundness
2

### Presentation
2

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
This work proposes a method for leveraging diffusion models pretrained on large-scale action-free video data for training action-conditioned diffusion world models on smaller action-labeled data from domains of interest. The motivation for training these world models is to solve downstream sequential decision-making tasks. The proposed method’s main novelty is that it requires access to some intermediate calculations of the pretrained diffusion model but not to its parameters. The proposed method, AVID, trains an adapter network which is conditioned on the pretrained model’s noise prediction and optimizes a denoising loss that incorporates both noise predictions from the pretrained model and the adapter’s output using a learned mask. The author’s evaluate world model performance on a real-robot and a video game domain based on multiple perceptual metrics as well as an action-prediction-based metric. Baselines include various diffusion-based methods some of which require full access to model parameters. The proposed method either outperforms or is comparable to baselines in most of the evaluated metrics while not requiring access to pretrained model parameters.

### Strengths
Summarized points:
- Tackle an interesting problem in the path for scaling robot learning
- Clear and well written paper
- Good positioning in related work
- Comparison to relevant baselines
- Thorough analysis of results
- Detailed appendix

### Weaknesses
Summarized points:
- Intermediate model calculations are not necessarily more likely to be accessible than the model parameters
- Limitation analysis of previous work (Section 3.2) does not clearly motivate the author’s specific choice of solution
- Main motivation is sequential decision-making but evaluation metrics do not assess the world models’ efficacy in solving such tasks
- It is not clear from the experimental results that training from scratch is not preferable to the proposed method for downstream sequential decision-making

**Evaluation - Metrics**

The main motivation of your method is to accommodate sequential decision-making but evaluation metrics do not assess the world models’ efficacy in policy learning or planning.
All metrics excluding ‘Action Error Ratio’ are perceptual metrics that may be dominated by aspects of the videos that are not important for control. For this reason, I believe the most interesting and relevant metric out of the ones you display in your evaluation is the ‘Action Error Ratio’. Your evaluation could benefit from including additional metrics that are a better proxy for the world model’s usefulness in sequential decision-making. In the Procgen dataset for example, you may want to measure the ability to predict the reward from the generated frames as well as the actions.

I understand that evaluating the world models by actually using them to solve a sequential decision-making task may not be straightforward. Doing this for the RT1 dataset would be hard for multiple reasons, but it may be more feasible for the Procgen environments. One possible evaluation pipeline is training a separate model to predict the reward from a given frame and then use the cross-entropy method (CEM) or a similar sampling-based planning algorithm with model predictive control (MPC) on top of the world model to maximize the sum of rewards in the prediction horizon. Any decision-making algorithm you choose doesn’t have to be SOTA to demonstrate the point that a given world model is better than the other for this purpose.

What is the accuracy of the action predictor on each dataset? I believe this is important in order to validate the use of the ‘Action Error Ratio’ metric and that this information should at least be in the appendix.

**Evaluation - Baselines**

Why do you tune baseline hyperparameters based on FVD and not based on e.g. normalized evaluation metrics? I find this choice puzzling since you explicitly write in the results section that this metric is less suitable than others in the setting of action-conditioned video generation.

How do you choose which baselines out of the 8 you suggested appear in the result tables?

Can the authors please explain what is the purpose of the ‘Full’ row in the result tables?

**Evaluation - Results**

It is not clear from the experimental results that training from scratch is not preferable to the proposed method for downstream sequential decision-making, a point that is also suggested in the limitations section and is mostly based on the ‘Action Error Ratio’ metric. This is not to say that it clearly is not beneficial. I suggest adding a discussion about the differences in performance in the two domains which would incorporate further insights as to when and why training an adapter is preferable to training from scratch.

**Evaluation - Ablation Study**

*Mask ablation*: It is not clear from your results that the learned mask has performance benefits and can’t be ‘absorbed’ into the adapter noise prediction, especially since it hurts performance on one dataset and doesn’t in the other.
How do you explain the difference in the effects of the mask on performance in each dataset? I think a discussion with respect to factors like the relationship between pre-training and fine-tuning data in each dataset and with respect to the results presented in Figure 4d could shed more light on this matter.

*Conditioning ablation*: I think the method and/or ablation section can benefit from an explanation or intuition behind why conditioning on the pretrained model’s output is beneficial, given that the pretrained output is already accounted for in the objective.

*Request for ablation*: As I see it, the fundamental difference between the proposed method and the PoE baseline is that the parameters of the adapter network are trained on the denoising loss containing noise predictions from both the pretrained network and the adapter network. Therefore an interesting ablation would be combining both the NM and NC ablations.

**Limitations of Naive Adaptation of Yang et al.**

Can the authors please highlight the exact source of discrepancy between the derivation in Yang et al. to the derivation presented in this section? Do you claim that there is an error in their derivation? Alternatively, are there different assumptions in your setting where their derivation does not hold?

### Questions
Most questions and suggestions are detailed in the 'Weaknesses' section.

**Limitations of Naive Adaptation of Yang et al.**

Can the authors please highlight the exact source of discrepancy between the derivation in Yang et al. to the derivation presented in this section? Do you claim that there is an error in their derivation? Alternatively, are there different assumptions in your setting where their derivation does not hold?

### Soundness
3

### Presentation
4

### Contribution
3
