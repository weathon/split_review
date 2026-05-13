# LossAgent: Towards Any Optimization Objectives for Image Processing with LLM Agents

- Decision: Reject
- Scores: 3, 5, 5, 5, 3

## Abstract
We present the first loss agent, dubbed LossAgent,  for low-level image processing tasks, \egno, image super-resolution and restoration, intending to achieve any customized optimization objectives of low-level image processing in different practical applications. Notably, not all optimization objectives, such as complex hand-crafted perceptual metrics, text description, and intricate human feedback, can be instantiated with existing low-level losses, \egno, MSE loss. which presents a crucial challenge in optimizing image processing networks in an end-to-end manner. To eliminate this, our LossAgent introduces the powerful large language model (LLM) as the loss agent, where the rich textual understanding of prior knowledge empowers the loss agent with the potential to understand complex optimization objectives, trajectory, and state feedback from external environments in the optimization process of the low-level image processing networks. In particular, we establish the loss repository by incorporating existing loss functions that support the end-to-end optimization for low-level image processing. Then, we design the optimization-oriented prompt engineering for the loss agent to actively and intelligently decide the compositional weights for each loss in the repository at each optimization interaction, thereby achieving the required optimization trajectory for any customized optimization objectives. Extensive experiments on three typical low-level image processing tasks and multiple optimization objectives have shown the effectiveness and applicability of our proposed LossAgent.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work, an LLM-Agent-like mechanism is proposed to determine optimal weights of multiple differentiable loss functions for low-level image processing tasks. Specifically, the authors first set up a set of differentiable loss functions. Afterwards, they introduce a well-crafted prompt that consists of a system prompt, external feedback, and customized needs. By passing this structured prompt through an LLM, the system outputs optimal loss weights, effectively integrating both differentiable and non-differentiable information into the optimization process. Experiments are mainly conducted on three low-level image processing tasks with three common losses.

### Strengths
+ This work attempts to incorporate undifferentiable scores and textual information into loss optimization by leveraging the powerful reasoning capabilities of Large Language Models (LLMs). This presents an interesting idea. 


+ The authors propose an enhanced prompt strategy that incorporates system information, historical context, and customized needs. It allows for more effective utilization of undifferentiable scores and textual descriptions during the optimization process.

### Weaknesses
However, there are several weaknesses as follows:

1. The scope of this work is limited to only three low-level image processing tasks with just three common losses. Furthermore, the losses are combined using a simple weighted approach. To enhance the contribution of this work, it would be beneficial to explore the LossAgent's performance on a broader range of tasks with a more diverse set of loss functions and combination strategies.

2. A thorough analysis of the loss weights is missing, including their initialization and constraints to ensure the values range from 0 to 1. The paper should provide details on how these weights are initialized and managed throughout the optimization process.

3. The use of test images for external feedback generation at the end of each stage raises concerns about overfitting. It would be more appropriate to use images from a validation set rather than the test set. Additionally, using the same metric for both external expert evaluation and final loss assessment may lead to bias towards that specific metric. To address these issues and provide a more comprehensive evaluation, the authors should: 1) Use a separate validation set for external feedback generation; 2) Employ diverse external experts that are distinct from the final evaluation metrics; 3) Demonstrate how all metrics change when optimizing for single, double, and textual objectives.

4. The baseline results in Table 2 are presented with fixed loss weights. It's unclear whether these fixed weights are the same as the initial loss weights or how they were determined. Moreover, the authors don't provide information on how they ensured these weights are optimal for each task.

5. The results shown in Tables 4 and 5 fail to provide compelling evidence for the effectiveness of the proposed method, as they show only marginal improvements or, in some cases, even inferior performance compared to baselines. The evaluation is limited to optimizing only one or two objectives, which raises questions about the method's scalability and efficacy when dealing with more objectives. A more comprehensive assessment would involve testing the proposed LossAgent in multi-objective optimization contexts, incorporating both quantitative metrics and qualitative textual descriptions.

### Questions
Please see the above weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a loss agent for low-level tasks. LossAgent introduces a large language model (LLM) as the loss agent, where the rich textual understanding of prior knowledge empowers the loss agent with the potential to understand complex optimization objectives, trajectory, and state feedback from external environments in the optimization process of the low-level image processing networks.

### Strengths
This paper explores employing LLMs for low-level tasks.

### Weaknesses
1. Missing SOTAs. This paper does not compare some low-level SOTA approaches, such as HAT [1], IPG [2] for SR tasks, and AirNet [3] for all-in-one IR tasks. Besides, the authors need to report the results using classic metrics in these experiments, e.g., PSNR and SSIM.
2. This paper employs an 8B LLM in the experiment; therefore, comparisons with other competitive low-level baselines on training cost and parameters are necessary.


[1] Activating more pixels in image super resolution transformer. CVPR 2023.

[2] Image Processing GNN: Breaking Rigidity in Super-Resolution. CVPR 2024.

[3] All-In-One Image Restoration for Unknown Corruption. CVPR 2022.

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a novel loss agent, which is quite interesting for fine-tuning models. My major concerns are as below.
1. will the prompt being used be unique? will it be adjusted according to different applications/tasks?
2. How to ensure that the optimization in this way will not get into local minimum? could you provide some demonstration?
3. Will there be a comparison of different LLMs?
4. Is an agent necessary?

### Strengths
The idea is interesting, and the method is with high practical value.

### Weaknesses
Overall, I cannot see the necessity of Agent. I think a regular LLM is enough. Also, the work is still at very early stage, lots of demonstrations are needed.

### Questions
Actually I had seen several similar works that introduce LLMs to fine tuning models. Could the authors double check if there will be similar works that use LLMs to adjust loss?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This manuscript uses LLMs to bridge some unoptimizable metrics and optimizable losses by adjusting the weights of different loss terms.

### Strengths
1. The investigated problem of the relationship between unoptimizable metrics and optimizable losses is interesting. 
2. The paper is easy to follow.

### Weaknesses
1. **Important related works are missed**. This manuscript uses LLM to optimize hyperparameters. A similar idea has been proposed and explored in [R1] from Google DeepMind. However, this paper is never cited or discussed. 

    [R1] Large Language Models as Optimizers

2. **The classification criteria is wrong**. This manuscript uses the differentiability of a metric as the judgment of being loss / objective. However, as studied in [R1], the problem is not differentiability. Many non-reference IQA metrics are differentiable (including some metrics used in this manuscript), but directly optimizing these non-reference IQA metrics will cause quite poor image quality. A metric is differentiable does not mean it can serve as a loss. Therefore, whether a metric can serve as the loss to improve the quality (instead of differentiability) should be the judgment of being loss / objective.

    [R2] Comparison of No-Reference Image Quality Models via MAP Estimation in Diffusion Latents 

3. **The relationship between losses and metrics is not analyzed**. This manuscript aims to bridge some unoptimizable metrics and optimizable losses. What are the results of the bridge? Are there some connections between unoptimizable metrics and optimizable losses? 

4. **Confusing formulas and no explanation of loss selection**. In Sec. 4, only the objective metrics are given, while the multiple differentiable losses are not given. How many losses does this manuscript use? What is L1, L2, L3, …, respectively? These are all quite important information, but they are never clearly described. I can only find them in Tab. 1 with only abstract formulas and without detailed explanations. For example, in the third row of Tab. 1 (All-in-one IR), there are $L_{perceptual}$ and $L_{LPIPS}$, what is the difference between them? In my view, they are the same. If they are different, which perceptual loss does this manuscript use? Also, why use L1 loss instead of MSE loss?

5. **Missing information and the necessity of double optimization objectives is not enough**. In Tab. 5, what are the metrics are not stated. I can only guess through the description of Sec 4.2.2 that the metrics are Q-Align / PSNR. In this case, MSE loss (same as PSNR) is differentiable, so why use an LLM to optimize PSNR instead of directly optimizing MSE? Will using an LLM to judge PSNR bring better results than optimizing MSE? 

6. **Conclusion of double optimization objectives is not convincing**. In Tab. 5, the experiment is conducted on the classical image SR task whose losses contain L1 loss. Given PSNR results, LLM can increase PSNR results easily by increasing the weight of L1 loss. In this case, the experiment can only show LLM can link PSNR with L1 loss, which is very easy. What is the meaning of this experiment? 

7. In Fig. 3, there is a clear advantage of LossAgent over baseline only for the third case (CLIPIQA). 

8. Writing.
- In Tab. 3, the upper arrows of MANIQA and CLIPIQA are mixed.
- In Tab. 7, the “W” in the caption should be “w/”.

### Questions
1. Discuss and compare with [R1], highlighting any key differences or novel contributions of the proposed method.
2. Clarification about why using differentiability as criteria of being loss / objective, and discuss with the observations in [R2]. 
3. Discuss some relationship between losses and metrics proven by experiments.
4. Provide explanation of loss selection and clarify the confusing formulas. 
5. Clarify the necessity of double optimization objectives and the importance of its conclusion.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes an LLM agent framework to address the problems in the field of optimization for low-level vision models. Facing the large gap between the single optimization objective and the real-world applications, the authors come up with a novel LLM-agent-based method to adjust the combination weights of each loss component as well as follow the external feedbacks. Several benchmarks have demonstrated some of the potential of the proposed LossAgent.

### Strengths
1. This paper points out an interesting direction of leveraging the reasoning and instruction-following capabilities of LLMs to address the conventional low-level vision optimization problems.

2. LossAgent is easy to implement and can be generalized to many vision tasks and LLM models.

3. The paper conducts comprehensive experiments across many benchmarks, different numbers, and types of objectives.

### Weaknesses
1. The proposed LossAgent focuses on adjusting the weights of each loss component, which narrows the scope of research. In fact, LLMs with powerful instruction following capabilities can serve as stronger rewards generators for learning better low-level vision models, rather than tuning the weight of losses.

2. The method uses an external evaluation expert to evaluate the restored image, which is somehow inferior to using a VLM for image quality assessment. Since the LLM for loss weight generation does not align well with the image perception model, the weights can be inaccurate.

3. The paper lacks results in diffusion-based image restoration models and video restoration tasks.

### Questions
1. Typo: Line 015, before "which" there should be a comma.

2. The term "customized needs" is not quite ordinary. Consider using "user demand," which would be better.

3. For weakness 1, the paper should also discuss some RL-based methods with LLM as reward models in this direction.

4. For weakness 2, the paper is encouraged to provide comparisons on fine-tuning or prompting some VLMs and using separate evaluation experts.

5. For weakness 3, the author should give some results on the abovementioned models and tasks.

### Soundness
2

### Presentation
3

### Contribution
3
