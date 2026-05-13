# GAQAT: Gradient-Adaptive Quantization-Aware Training for Domain Generalization

- Decision: Reject
- Scores: 5, 8, 3, 3, 5, 3

## Abstract
Research on loss surface geometry, such as Sharpness-Aware Minimization (SAM), shows that flatter minima improve generalization. Recent studies further reveal that flatter minima can also reduce the domain generalization (DG) gap. However, existing flatness-based DG techniques predominantly operate within a full-precision training process, which is impractical for deployment on resource-constrained edge devices that typically rely on lower bit-width representations (e.g., 4 bits, 3 bits). Consequently, low-precision quantization-aware training is critical for optimizing these techniques in real-world applications.
In this paper, we observe a significant degradation in performance when applying state-of-the-art DG-SAM methods to quantized models, suggesting that current approaches fail to preserve generalizability during the low-precision training process. To address this limitation, we propose a novel Gradient-Adaptive Quantization-Aware Training (GAQAT) framework for DG. 
Our approach begins by identifying the scale-gradient conflict problem in low-precision quantization, where the task loss and smoothness loss induce conflicting gradients for the scaling factors of quantizers, with certain layers exhibiting opposing gradient directions. This conflict renders the optimization of quantized weights highly unstable. To mitigate this, we further introduce a mechanism to quantify gradient inconsistencies and selectively freeze the gradients of scaling factors, thereby stabilizing the training process and enhancing out-of-domain generalization.
Extensive experiments validate the effectiveness of the proposed GAQAT framework. On PACS, \textcolor{black}{both 3-bit and 4-bit exceed directly integrating DG and QAT by up to 4.5\%. On DomainNet, our 4-bit results deliver nearly lossless performance compared to the full-precision model, while achieving improvements of up to 1.39\% and 1.06\% over the SOTA QAT baseline for 4-bit and 3-bit quantized models, respectively.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This submission proposed to conduct Quantization-aware Training (QAT) on Domain Generation (DG) task. Specially, it firstly observed and demonstrated empricially that objective of QAT is not aligned with GD: difference of accumlated gradient and perturbation of scaling factor in QAT. Based on the observation, it proposed a metric (gradient disorder) to measure the consistency of training. The metric is used to determine the optimization procedure of QAT and DG: During training, it calculates the disorder for QAT every K steps, if the metric is below a threshold, DG's optimization will be paused.

### Strengths
- The quantitative measurement on disalignment between QAT and DG (Sec.3.2) is interesting and convincing. Though it may be noticed in other works that QAT affects the training of main task, seldom empirical works have been conducted for demonstration.
- The method to circumvent effect of QAT to main task (alternative update with one fixed) is straight forward and promissing.

### Weaknesses
 - Though objective disalignment (gradient inconsistency) between QAT and main task is observed in DG, the method proposed (Line 296-303) is not coupled with DG: it does not used any properties from DG and it can be applied to other problems that are involved with QAT (such as image classification, LLM with QAT). The inconsistency (method proposed is not coupled with the scene where motivation is discovered) harm the contribution. Author can either improve the method using DG's related parts or prove the method (and observation) is universal in QAT (for example conducting more experiments on other fields).

- The tuning of hyper-parameter is sophisticated: author should explain how step K and threshold $\tao$ are discovered and prove that these parameters are insensitive.

- Grident disorderd is formulated as the dicrepancy between two gradient sequence in Eq.2, how is it applied to a solo $g_\text{task}$ or $\delta_{t, S_i}$? It is calcualted between evaluation between successive steps?

- How the update rule (Line 296-303) is determined? In other words, it is possilbe to use $g_\text{task}$ (if disorder of $g_\text{task}$ is under certain value, scaling factor in quantizer is not updated). How about simply alternatively update of QAT and DG every K steps, which should be listed as a baseline.

### Questions
- Grident disorderd is formulated as the dicrepancy between two gradient sequence in Eq.2, how is it applied to a solo $g_\text{task}$ or $\delta_{t, S_i}$? It is calcualted between evaluation between successive steps?

- How the update rule (Line 296-303) is determined? In other words, it is possilbe to use $g_\text{task}$ (if disorder of $g_\text{task}$ is under certain value, scaling factor in quantizer is not updated). How about simply alternatively update of QAT and DG every K steps, which should be listed as a baseline.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the degradation of domain generalization performance when conventional flatness based domain generalization are applied to quantized models. Existing flatness-based domain generalization techniques are typically used in full-precision training, which is impractical for deployment on resource-constrained edge devices. To address this limitation, the paper proposes a novel Gradient-Adaptive Quantization-Aware Training (GAQAT) framework for domain generalization. The authors first illustrate the scale gradient problem introduced by domain generalization in low precision quantization. In it the task loss and smoothness loss become contradictory therefore making the optimization highly unstable. To mitigate this problem, the proposed framework introduces a mechanism to quantify gradient inconsistencies and selectively freeze gradients, stabilizing the training process and enhancing out-of-domain generalization.

### Strengths
The paper is very well structured in clearly identifying the problem statement, identifying the possible cause of the problem and then providing a solution.
The authors have clearly demonstrated the problem of opposing gradients incurred during training the quantized model in Figure 2 therefore establishing the problem statement.
The authors introduce a smoothing parameter in the quantizer to jointly optimize for loss curvature and task loss.
The idea of introducing gradient disorder by looking at the number of direction flips of gradient for smoothing parameters over n training steps is novel and simple to implement.
The idea of dynamically freezing only the task loss gradients for cases with low gradient disorder is innovative.
The final results looking very promising with almost all tasks showing best results with the proposed method.
The authors have also addressed some obvious questions in the ablations like impact of number of steps used for gradient disorder calculation and effect of freezing strategy.

### Weaknesses
The experiments section seems a bit weak and might need a clearer explanation.

### Questions
I would be curious to see 2 ends of the quantization results. 1/2 bit and 8 bit quantized models using the same method compared to DG-SAM + LSQ.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the Gradient-Adaptive Quantization-Aware Training (GAQAT) framework to achieve efficient domain generalization for low-precision quantized model. GAQAT tries to address scale-gradient conflict between gradients from task loss and smoothness loss( used in SAM) by selectively freezing the gradients of scaling factors. The proposed approach is tested on two Domainbed datasets and shows some improvement.

### Strengths
1. GAQAT addresses domain generalization issue for low-precision quantized models, which is very practical. This is interesting and under-explored topic.
2. This work proposed an approach to tackle scale-gradient conflict by quantifying gradient inconsistencies and selectively freeze the gradients of scaling factors.
3. The paper is well written and easy to understand.

### Weaknesses
1. Incorporating QAT from scratch is not a good idea. QAT is generally performed on a pretrained model and literature shows that it can improve results significantly. You can significantly improve results if you perform quantization after some iterations.
2. The approach does not show any significant improvement in comparison to baseline methods. On DomainNet dataset, there is no difference between all three (Yours, LSQ, and LSQ +SAGM). On PACS you have a difference of less than 2% between LSQ and your method and you reported a difference of 4.5% in the abstract.
3. It's a norm in the literature[1,2,3,4,5] to show results on all DomainBed[1] datasets with the mean and standard error over multiple runs. I would recommend authors to add those results as the experiments are currently insufficient.

### Questions
1. Why in Table 2 and Table 4, "ours" result for 4 bits are different?
2. Have you looked at the experiments with higher bit-precision? Does gradient conflict problem exist with higher bit-precision as well e.g 6,7 bit?
3. I would recommend to explore the generalization aspect of the QAT as well. I can clearly see that combining QAT with SAGM does not help, especially in the results for 3 and 4 bits on PACS dataset. 
4. Having an empirical demonstration of flat minima like SWAD[1] would be good as there is no gaurantee that your proposed approach will result in a flatter minima as compared to LSQ+SAGM.

Minor recommendation:\
Please swap the colors in Table 1, green color can be used for improvement as red is generally considered negative.

[1] SWAD: Domain generalization by seeking flat minima. Cha et al., NeurIPS 2021.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the Gradient-Adaptive Quantization-Aware Training (GAQAT) framework for enhancing domain generalization in quantized models, specifically targeting low-bit-width settings often used in resource-constrained devices. Addressing the limitations of current domain generalization methods under quantization, the authors identify gradient conflicts that arise during training due to discrepancies between task loss and smoothness loss. To manage this, GAQAT uses a gradient disorder metric to detect these conflicts and applies selective gradient freezing, stabilizing training and improving generalization. Extensive experiments demonstrate GAQAT's effectiveness, showing significant accuracy improvements on PACS and DomainNet datasets compared to baseline methods​.

### Strengths
1. The paper identifies and addresses gradient conflicts between g_task and g_smooth, a key insight that stabilizes training and improves convergence. This reviewer fully agrees with this idea.

2. By dynamically freezing scaling factors based on gradient disorder, GAQAT mitigates gradient conflicts, leading to enhanced model performance in low-bit quantization.

3. Improved performance on quantized models in domain generalization scenario

### Weaknesses
First, I would like to clarify that I am not highly experienced in the specific domain of Domain Generalization (DG) using ResNet-50. My review reflects this perspective (and if other reviewers find the contributions significant, I am open to adjusting my evaluation). Given the field's recent emphasis on Transformer-based research and development, it has been a few years since I worked with or optimized models like ResNet.

1. Applicability of Quantization to ResNet-50 in DG Scenarios: I find it challenging to fully appreciate the motivation for applying quantization to ResNet-50 in the context of Domain Generalization, especially with a focus on deployment to resource-constrained devices. While the paper assumes such deployment scenarios, it seems unlikely that practitioners would choose to deploy a large CNN model like ResNet-50 on an edge device. It appears this choice may stem from the use of benchmarks typically associated with DG research, but for the edge-device assumption, studying alternative, more compact models seems essential.

2. The identified gradient conflict between g_{task}​  and g_{smooth} recalls the classic challenge of balancing overfitting on domain-specific data with generalization (or regularization) to achieve a smoother loss landscape. This insight may not be limited solely to DG + QAT settings but could have implications in broader contexts. I would be interested in seeing if this theoretical framework extends to general quantization-aware training (QAT) or even Vision Transformers, for instance. This paper could potentially expand its contributions beyond a localized scope, making the findings more universally relevant.

### Questions
included in weaknesses

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigate the domain generalization gap under quantization regime. The propose a gradient adaptive quantization aware training to be able to make the optimization of low precision and smoothness together. They found the reason for the failure of previous methods is the gradient approximation use in low precision training, and suggest a method to resolve it.

### Strengths
I think the main strength of the paper is the general idea that low precision training have different properties than the full precision counterpart, and we need to confront with them separately.

### Weaknesses
I think that the paper require a better examination of the domain generalization under different quantization datatypes, group sizes, gradient approximation before it get can a general conclusion and try to solve it.. I think it is a must to be at a level expected from an ICLR paper.
Showing results only for INT quantization with learnable scale is not enough in my opinion.

### Questions
1) Do you tried to use scaling factor that is not learnable and only is measured. It is a well used methods, not only for INT quantization also for FP quantization. It is interesting if in that cases we still see the gap between both losses - which is the main motivations for the paper.
2)  Interesting to see how to proposed methods work for other quantization method, such as FP. For example the MXFP4 datatype is a good candidate. Moreover, what about other gradients approximation that are not STE, like PWL or MAD (https://arxiv.org/pdf/2206.06501)
3) I would like to see also experiments in language models.

================================================

Dear authors,

Thank you for taking the time to try to address the questions and concerns raised.

Unfortunately, my two main concerns remain unresolved:

I believe the paper requires more in-depth research into different quantization techniques to achieve more accurate and comprehensive conclusions. In particular, the use of FP quantization, which is the preferred method for most AI accelerators, should be explored further.

The inclusion of language models is essential, as they face unique quantization challenges—such as handling outliers—that do not typically arise in models like ResNet.

I have decided to maintain my score.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper combines quantization-aware training with the domain generalization model. At first, the authors identify the scale factors (used in quantization) suffer from a gradient conflict problem, where the task loss and smoothness loss present conflicting gradients. As a result, GAQAT, which dynamically quantifies gradient conflicting and selectively freezes the gradients of scaling factors, is proposed to stabilize the training process and enhance domain generalization performance.

### Strengths
1 This paper provides detailed implementation settings to help re-production.
2 The experimental results are comprehensive, which helps prove the effectiveness of GAQAT.

### Weaknesses
I have some concerns about the writing and experiment comparison of this paper.

Writing:

1 In the main text, Figure 3 should be referred before Figure 4.

2 The gradient disorder is measured with two sequences according to Equation 4. However, in Line 254, the author says 'the gradient disorder of the  g_{task} decreases significantly as training progresses.' How do measure the gradient disorder of the g_{task} alone?

3 Line 259 - 263. Why lower layers with lower gradient disorder are more likely to exhibit the phenomenon of two gradients in suboptimal equilibrium state? How the Figure 2 and Figure 4 prove this? What is the suboptimal equilibrium state?

4 Totally lost when reading Line 287-294

5 Line 297, 'Continuously **freezing** the g_{task} without **unfreezing**'? How can you freeze g_{task} while unfreezing it?


Experiment comparison:

1 Why only 4/4 and 3/3 bit-width?
2 Maybe the author should add some experiments that quantized the trained model with PTQ methods.
3 Does the quantized model is initialized from the pre-trained full-precision model?

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
