# Fast Ensembling with Diffusion Schrödinger Bridge

- Decision: Accept
- Scores: 5, 8, 6, 8, 6

## Abstract
\gls{de} approach is a straightforward technique used to enhance the performance of deep neural networks by training them from different initial points, converging towards various local optima. However, a limitation of this methodology lies in its high computational overhead for inference, arising from the necessity to store numerous learned parameters and execute individual forward passes for each parameter during the inference stage.
We propose a novel approach called~\gls{dbn} to address this challenge. Based on the theory of the Schr\"odinger bridge, this method directly learns to simulate an \gls{sde} that connects the output distribution of a single ensemble member to the output distribution of the ensembled model, allowing us to obtain ensemble prediction without having to invoke forward pass through all the ensemble models. 
By substituting the heavy ensembles with this lightweight neural network constructing \gls{dbn}, we achieved inference with reduced computational cost while maintaining accuracy and uncertainty scores on benchmark datasets such as CIFAR-10, CIFAR-100, and TinyImageNet.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to use Diffusion Schrodinger Bridge (DSB) as a way of bridging two arbitrary distributions, namely that of the output activations space of deep models, thereby achieving more efficient ensemble. In contrast to the previous Bridge Network approaches, the DSB approach imposes no (direct) restriction on the low-loss subspace of the parameter manifold, but instead learn a diffusion that solves the SB problem to diffuse from any ensemble member to the "target" ensemble model. The authors claim that the empirical results demonstrate superior performance and FLOPs requirement of the Diffusion Bridge Network (DBN).

### Strengths
- The paper generally tackles the important issue of accelerating/simplifying the costly deep ensemble process.
- The overall idea is clearly presented, and it's interesting to motivate a generative solution on the ensemble problem.
- Relatively comprehensive comparison to baseline approaches.

### Weaknesses
 - The baseline performances shown in the experiment section does not completely agree with the prior works. The scale of the experiments were somewhat small.
- Lack of analysis on the diffusion part of the design.
- The methodology somewhat concerns me (see questions below).

- The introduction of temperature does define a distribution, but essentially at a cost of compromising the performance of the original ensemble member (for example, if you look at the NLL loss of the logits after applying temperature, it will be worse). Is this really a reasonable design? If you look for bridging on logit space with another, wouldn't it make more sense to consider the logit space as is (e.g., get a distribution via input perturbation, etc.)?

- Why DSB rather than a conditional diffusion from Gaussian? In $\textsf{I}^2\textsf{SB}$ the motivation was clearer as they hoped to leverage the structural prior of the image. Empirically, how big would the difference be?

- The paper has a bunch of analysis on the ensemble approach, but little (almost none) on the diffusion portion. For example, how much training (data and speed) is needed for the DSB training? Why diffusion instead of some simpler approaches like normalizing flows, and bringing all ensemble members to a (same) tractable distribution?

- About the baseline: the Bridge Network paper seems to have better numbers on TinyImageNet than what the authors reported in this paper (e.g., 65.82% accuracy for 3-BN-sm and the FLOPs seems to be much smaller (1.15x). The BN paper also evaluated on ImageNet, where in my experience the accuracy is **much less volatile**. If, as authors claim that the BN approach has more training cost (at the end of Sec. 2.1), perhaps the DSB approach should be compared with BN on that turf as well.

### Questions
1. The introduction of temperature does define a distribution, but essentially at a cost of compromising the performance of the original ensemble member (for example, if you look at the NLL loss of the logits after applying temperature, it will be worse). Is this really a reasonable design? If you look for bridging on logit space with another, wouldn't it make more sense to consider the logit space as is (e.g., get a distribution via input perturbation, etc.)?

2. Why DSB rather than a conditional diffusion from Gaussian? In $\textsf{I}^2\textsf{SB}$ the motivation was clearer as they hoped to leverage the structural prior of the image. Empirically, how big would the difference be?

3. The paper has a bunch of analysis on the ensemble approach, but little (almost none) on the diffusion portion. For example, how much training (data and speed) is needed for the DSB training? Why diffusion instead of some simpler approaches like normalizing flows, and bringing all ensemble members to a (same) tractable distribution?


--------------

Post-rebuttal edit: I'm raising my score slightly from 3 to 5, in light of the amendments the authors make during the rebuttal. However, I still believe this paper is not completely ready for publication at the venue. See comment below for details. 

4. About the baseline: the Bridge Network paper seems to have better numbers on TinyImageNet than what the authors reported in this paper (e.g., 65.82% accuracy for 3-BN-sm and the FLOPs seems to be much smaller (1.15x). The BN paper also evaluated on ImageNet, where in my experience the accuracy is **much less volatile**. If, as authors claim that the BN approach has more training cost (at the end of Sec. 2.1), perhaps the DSB approach should be compared with BN on that turf as well.

### Soundness
2 fair

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
This work proposes to lower the inference costs associated with running a full ensemble of neural networks. 
One problem with other fast ensembling approaches is that they require mode connectivity between the ensemble members, but finding such a low-loss path or subspace through the weight space is difficult. other methods either assume the location of these parameters directly, or else learning-based approaches learn a subspace between just two modes (ensemble members). This method uses a diffusion model to transform logits from a single ensemble member, into a sample from the logit distribution of the ensemble itself.

### Strengths
I think this is a strong approach, it alleviates inference costs in a straightforward way that makes use of novel techniques. 

* Interesting approach to speed up ensemble inference
* Frames ensemble knowledge distillation as a diffusion problem
* Linear scaling of bridges in the worst case, where bridges are smaller than ensemble members. 
* Good results on accuracy across benchmarks. DEE is very good.

### Weaknesses
 * DBN models are notably less calibrated  than ensembles or bridge networks across tasks.
* No evaluation on in / out of domain uncertainty / calibration. IMO this is a huge reason why ensembling is done in the first place. 
* Evaluation is with relatively small models

Comments but not weaknesses:
* Section 4.1 "?? of ??" still in text. 
* I think parameter-count/memory savings is useful here and could be reported.

### Questions
1. Given a path from model z_1 to the ensemble model z, can anything be said about the intermediate logit distributions in terms of their loss? 
2. I'm not clear how useful the source distribution construction is when its just annealing T. This preserves relative ordering over classes, which is not adding much additional information about the "distribution" of z_1. Are we in some sense integrating over paths from the set of temperature-augmented z_1 -> z?  Is that a non-trivial path? 
3. In algorithm 1: is a single temperature value drawn for each member, for all data points in the minibatch?
4. Does performance increase with multiple diffusion steps?
4a. What's the "cost" of each diffusion step in term of % of DE inference speed. Can DBN admit more than diffusion step at inference and still be faster than DE?  
5. Can the authors comment on the calibration error increase with this method?

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
This article presents a framework to approximate Deep Ensembles (DE) called Diffusion Bridge Network (DBN). Following the theory of the Schrödinger bridge, a conditional diffusion bridge is learned between single models' logits and the target ensemble's logits. The score network learned is distilled during the training process and multiple score networks can be ensembled when the number of models increases.

[Edit: as indicated in my response, I am increasing my rating from 5 to 6 considering the strong improvements in writing for both the theory and the implementation, despite limited results on TinyImageNet after correction of the authors mistake]

### Strengths
The main idea of the article is well-motivated, improving on Bridge Networks with the strong Schrödinger bridge to learn the ensemble distribution. 

The results obtained show that the conditional diffusion bridge can be learned, leading to efficient deep ensemble estimation, with a strong Deep Ensemble Equivalent score. However with limited insight on the networks used and their training, it is hard to conclude and compare with Bridge Networks.

### Weaknesses
 **Writing** This article's writing is very hard to follow. There are many spelling or grammar mistakes (see Questions). Ideas are presented poorly or too quickly, leaving the reader confused. The theory, which originates from Liu et al. 2023 is presented very quickly and unclearly, with some mistakes. ($f'$?, no definitions of $W_t$, $\bar W_t$, $\beta_t$, no dimensions, Schrödinger systems are not presented, it's never clarified that $f=0$, although $f$ was never even defined. It's not clear how equation (8) is obtained.

**Training** Many important points are missing, in particular, the architecture of the score network is never given anywhere in the article. Contrary to what the authors claim, the appendix does not give any hyperparameter settings: the training details of both the ensemble networks and the DBN are left unclear (Optimizer, scheduler, number of epochs/steps, distillation schedule...) This is not a detail, in particular for the DBN. If its training is particularly expensive/slow, it is an important drawback despite the speedup it provides during inference. Are Bridge Networks also using distillation, and is their training comparable to DBN? Without this information, it is hard to compare the results obtained.

**Number of ensembles** I find unclear the number of ensembles that a score network is trained on. Section 4 indicates that a score network is trained on 3 ensembles, with no clarification on why this number is chosen (presumably Section 4.3). Why also not simply increase the size of the DBN network? For more than 3 ensembles, 2 or more DBNs are trained. In this case, are the DBN trained on all of the ensembles at the same time? Are they limited to a given subset of 3 ensembles, as indicated previously? 
This becomes even more confusing in Section 4.2, where the number of ensembles increases to 9, and the number of DBNs is left unclear ("two or more"), as well as for BNs. 

Despite promising results, this article needs a serious rewrite before I can accept it for now.

### Questions
* Is the DSB not able to learn if there is no temperature annealing?

* Why choose in particular ResNet-32x2 and x4 rather than a standard ResNet-32?

* Do the authors have an idea why DBN shows poor EC scores compared to the other metrics?

**Various mistakes or remarks:**
* Abstract: "theory of [the] Schrödinger bridge"
* Introduction: "incurrs an extra"
* 2.2 "has rarely been demonstrated its practicality" "demonstrated for real-world image dataset" "Gaussain" "by a certain PDEs" 
* 3.2 "Based on the formulation" ??
* 3.3 "super performance". No use for the (NFE) abbreviation if it's never used after.
* 3.4 $\Phi$ or $\Phi'$? 
* 4. "because Ryabinin et al. (2021) refined poor convergence of" "more profound formulations"
* 4.1 "results on CIFAR-10 is shown in ?? of ??"
* Conclusion "Additionally,  [...] of 3 DE models", nominal sentence.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this manuscript, the authors endeavor to address the limitations of existing bridge networks by introducing a novel "diffusion bridge networks" framework, inspired by the celebrated Schr\"odinger Bridge problem. Specifically, the authors commence by elucidating the shortcomings inherent in constructing bridges within the feature space represented by bridge network, and subsequently propose their diffusion bridge as a solution to generalize from a single network output to an ensemble output. In order to empirically substantiate the efficacy of their method, a variety of experiments are executed across the CIFAR-10, CIFAR-100, and TinyImageNet datasets, utilizing ResNet-$32\times2$, ResNet-$32\times4$, and ResNet-$34$ as backbone architectures. Overall, the paper offers an intuitive approach to the problem at hand, and I will delineate its strengths and weaknesses in the subsequent sections.

### Strengths
1. **Problem Reformulation** In the domain of problem formulation, the authors ingeniously recast the challenge of deep ensembles as an optimal transport problem, subsequently addressing it through a dynamical optimal transport methodology. This novel perspective not only refines the research question but also paves the way for utilizing advanced mathematical tools to provide robust solutions.

3. **Ample Experiments** With regard to empirical validation, the authors carry out an extensive array of experiments on multiple datasets and furnish an in-depth analysis of the experimental outcomes. This comprehensive experimental setup serves to fortify the credibility of their proposed method and provides valuable insights into its performance characteristics.

### Weaknesses
1. **Other Transport Models** To the best of my understanding, related works such as "Rectified Flow" [1] and "Flow Matching" [2] are capable of accomplishing similar functionalities. Additionally, when compared to the Schrödinger bridge approach, these models operate through a deterministic process, which could potentially benefit from lower variance properties. The omission of such deterministic flow models from the discussion may limit the generalizability and applicability of the method proposed in the current manuscript. Specifically, the paper lacks a clear justification for choosing a stochastic approach over deterministic alternatives, particularly given the potential for reduced variance in the latter. A more thorough comparison, including empirical results, would be necessary to validate the choice of the Schrödinger bridge approach.

0. **Inference Algorithm** In the manuscript, it appears that the authors have not provided details regarding the inference algorithm for the proposed DBN during the model inference stage. This omission leaves a critical gap in the paper, as understanding the inference mechanism is essential for a comprehensive evaluation of the proposed method. The paper should explicitly detail how the reverse-time process is implemented, including the specific steps and equations used to generate samples during inference. Without this information, it is difficult to assess the practical applicability and computational cost of the proposed method.

2. **Annealing of Temperature** In Section 3.2, the authors discuss the concept of temperature distribution, yet the experimental section lacks elaboration on how the temperature distribution is selected and what principles govern temperature annealing. This absence of information creates a gap in the methodological clarity and poses questions regarding the thoroughness of the experimental design. Furthermore, from a scholarly perspective, treating the distribution as a Gumbel-Softmax distribution [3] could raise additional questions. Specifically, one might inquire whether the training variance of the Diffusion Bridge Networks (DBN) is influenced by the temperature parameter. Addressing such intricate relationships between the temperature and training variance would enhance the paper's academic rigor and contextual relevance. The paper should also discuss the sensitivity of the method to different temperature annealing schedules and provide a rationale for the chosen schedule.

3. **LaTeX Compile** In Section 4.1, line 3, the manuscript contains two instances of "??", which clearly indicate placeholders or unresolved references. The authors should rectify this issue to enhance the document's professionalism and completeness prior to submitting the finalized manuscript. The presence of such markers detracts from the paper's overall quality and could create potential ambiguities for the reader.

### Questions
My questions are listed in weakness, please refer to weakness.

----
Post Rebuttal Comments:  
Thank you for the comprehensive response to my queries and for conducting additional experiments. Having thoroughly reviewed your revised manuscript and the expanded experimental evidence, I am inclined to revise my evaluation. Accordingly, I am considering raising my score from a 6 to an 8, reflecting the improvements and clarifications you have made.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a diffusion-based approach for enhancing Deep Ensemble (DE) performance. In particular, it suggests the direct transfer of samples from a chosen source model to the ensemble, utilizing the Image-to-Image Schrödinger bridge (I2SB). This proposed method seems to perform well on the conventional benchmark for ensembling tasks.

### Strengths
- The paper presents a compelling application of I2SB in the context of deep ensembles.

- The proposed method delivers impressive performance across various benchmarks, by achieving minimal performance degradation when compared to the ground-truth oracle, all while using significantly fewer FLOPs, making it an exciting development.

### Weaknesses
 - Equation (4) contains an error: the forward and backward drifts should not be the same, and I2SB specifically provides a tractable solution only for the backward drift. Additionally, the definition of $f_t^\prime$ is missing. I suggest presenting the analytical backward drift directly, similar to what is provided for the target in (9), and ignore the forward diffusion. Moreover, the use of a capitalized $Z$ in equation (4) is misleading, as it typically denotes a random variable, while in this context, it represents a function evolving over time, which is deterministic. Using $z$ instead would be more appropriate, avoiding confusion with the solutions of (3) or (5).

- It is also inaccurate to state that "(4) and its time-reversal directly follows the Fokker-Planck equation of the SDE in (3)". Equation (4) is indeed the Fokker-Planck equation for a family of SDEs, but (5) is one example, not (3).

- The variables "y" in (11) and (12) lack proper definitions. While their meanings can be inferred from the context, it would be better to provide clear definitions.

- The labels in Figure 2 are too small and may need to be enlarged for better readability.

- There appears to be a typo in (11). I think it should be "Softmax(Z_0)" instead of the current notation.

- Missing references in Sec 4.1

- It's unclear why additional distillation is necessary, given that I2SB has demonstrated decent performance with NFE=1. An ablation study or justification is needed to understand the necessity of further distillation for optimal performance, especially considering that DE-1 already performs quite well, indicating the boundary distributions are likely close.

### Questions
- I believe I2SB remains applicable without the use of temperature annealing ($T$). Can the authors provide further clarification on the role of $T$ and explain how it contributes to differences in performance?

- It's unclear to me how multiple DBNs are combined in Sec 3.5. For instance, if there are 5 models (M=5) and each DBN is trained with 3 ensembles (as suggested in Sec 4), what is the appropriate value for $L$ and what're the ensembles for each DBN?

- I2SB has demonstrated decent performance with NFE=1. Can the authors present an ablation study or provide justification for why additional distillation is necessary for achieving optimal performance?

- The font size in Alg 1 seems to be smaller than the one in the main paper. Is this intended?

I am open to reevaluating the score, with the condition that the authors thoroughly address my questions and make improvements to the presentation, particularly addressing the weaknesses I've highlighted.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
