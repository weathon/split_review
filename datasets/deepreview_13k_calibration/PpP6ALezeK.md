# Exploring Diffusion Models' Corruption Stage in Few-Shot Fine-tuning and Mitigating with Bayesian Neural Networks

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6

## Abstract
Few-shot fine-tuning of Diffusion Models (DMs) is a key advancement, significantly reducing training costs and enabling personalized AI applications. However, 
we explore the training dynamics of DMs and observe an unanticipated phenomenon: during the training process, image fidelity initially improves, then unexpectedly deteriorates with the emergence of noisy patterns, only to recover later with severe overfitting.
We term the stage with generated noisy patterns as \textit{corruption stage}.
To understand this corruption stage, we begin by theoretically modeling the one-shot fine-tuning scenario, and then extend this modeling to more general cases. 
Through this modeling, we identify the primary cause of this corruption stage: a narrowed learning distribution inherent in the nature of few-shot fine-tuning. 
To tackle this, we apply Bayesian Neural Networks (BNNs) on DMs with variational inference to implicitly broaden the learned distribution,
and present that the learning target of the BNNs can be naturally regarded as an expectation of the diffusion loss and a further regularization with the pretrained DMs.
This approach is highly compatible with current few-shot fine-tuning methods in DMs and does not introduce any extra inference costs. 
Experimental results demonstrate that our method significantly mitigates corruption, and improves the fidelity, quality and diversity of the generated images in both object-driven and subject-driven generation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to analyze the progress of few-shot fine-tuning of diffusion models and improve it. First, they present the empirical analysis on the few-shot fine-tuning, which shows the corruption stage with the abnormal decrease in the fidelity of generated images. Then, they propose heuristic modeling, that a marginal distribution of $x_0$ with a parameterized diffusion model $\theta$ is approximated by a multivariate Gaussian distribution, to explain the few-shot fine-tuning procedure. Based on this modeling, they tried to understand why the corruption stage occurs. Finally, they propose the Bayesian neural network (BNN) approach. Through their experiments, they show that their method improves various fine-tuning methods including Dreambooth, LoRA, and Orthogonal Finetuning.

### Strengths
- This work tries to analyze the foundational diffusion model’s fine-tuning process. 
- The authors incorporate the user study to support the effectiveness.

### Weaknesses
 **W1: Observed Issues with Incomplete Linkages**


1. **W1-1 Incomplete Rationale for “Finding a Sample to Minimize the Error Term”**
   - In line 229, the statement, *“pre-trained diffusion model finds a sample $( x^\star )$ to minimize the error term”*, appears potentially misleading. First, diffusion models do not involve an explicit search mechanism; the phrase *“finding a sample”* might imply a deliberate search process that does not actually occur within the diffusion framework. The model's denoising process is a deterministic function of the input $x_t$ and the model parameters, not a search for a sample that minimizes an error term. The description suggests an optimization process that is not present in standard diffusion model inference.
   - Second, I question whether the experiments in Fig. 3 adequately support the claim that the diffusion model *“minimizes the error term.”* It seems the authors imply that an unchanged $ x_0 $ when $ x_t = 0 $ is an indicator of error minimization ($ \delta $). However, my understanding is that diffusion models generate $ x_0 $ as a memorized sample from the training dataset, rather than as a result of minimizing an error term. Specifically, two points should be considered:
      - **Corrupted State of $ x_t $:** If $ x_t $ is initialized in an out-of-distribution state, the pre-trained diffusion model may fail to denoise such samples effectively. This would challenge the claim that the model consistently generates a sample from the training data. The choice of $x_t = 0$ is a very specific case and it is not clear how this generalizes to other values of $x_t$. The model's behavior with $x_t = 0$ may not be representative of its behavior with other, more typical, noisy inputs.
      - **Validation of Training Data:** It’s unclear whether the sample $ x_0 = 0 $ corresponds to a specific instance in the training data. The prompt used, *“a simple, solid gray image with no textures or variations,”* may merely cause the model to generate a gray image without textures, as prompted, rather than replicating a sample from the training dataset. The experiment does not demonstrate that the model is minimizing an error term, but rather that it is generating an image consistent with the prompt, which is not the same thing.


   **Suggestion:** The authors might consider initializing $ x_t $ with actual samples from the training dataset used to train the diffusion model, alongside corresponding text labels. If the model does not alter $ x_t $ in these cases and the pixel-wise differences between generated samples and training data remain small, this would better support the claim. The current experimental setup is too narrow to support the claim of error minimization.


2. **W1-2 Lack of Theoretical Validation for Error Minimization in Fine-Tuning**
   - To establish that the fine-tuning process drives the error term $ \delta $ to zero, the authors should consider providing a theoretical analysis showing how diffusion losses are minimized. Without such a theoretical basis, it is challenging to understand why the heuristic modeling is effective or whether the error term $ \delta $ indeed approaches zero at the optimal point. The paper lacks a rigorous mathematical argument to support the claim that the error term is minimized during fine-tuning. A theoretical analysis of the diffusion loss landscape would be necessary to understand the behavior of the error term.


3. **W1-3 Incomplete Explanation for the Corruption Stage during Fine-Tuning**
   - Building on W1-2, without a theoretical analysis of how $ \delta $ changes throughout fine-tuning, it’s difficult to comprehend why the corruption stage occurs. According to the authors’ experiments, fine-tuning the diffusion model on a limited number of samples results in significant errors after several iterations. This raises questions about why naive fine-tuning leads to this corruption stage (i.e., why $ \delta $ is high and $ \sigma $ remains high), which remain unanswered by the current modeling and experimental outcomes. Consequently, I believe the cause of corruption is not thoroughly studied in this work, and the conclusion that *“after some fine-tuning stages, error exists due to limited training steps”* seems somewhat trivial. The explanation of the corruption stage is too simplistic and does not provide a deep understanding of the underlying mechanisms.


4. **W1-4 Unclear Justification for Using Bayesian Neural Networks (BNNs)**
   - Extending from W1-3, without a clear understanding of the corruption stage, I am not fully convinced why a Bayesian Neural Network (BNN) is presented as the solution. The authors mention that *“the modeling of BNNs hinders the diffusion models from learning the exact distribution of the training dataset $ D $”* but do not elaborate sufficiently on why this is beneficial in mitigating the corruption stage. Additional clarification about the cause of the corruption stage and further explanation of how BNNs address this underlying issue are needed. The connection between the proposed BNN approach and the identified corruption stage is not well-established. The paper needs a more detailed explanation of how BNNs specifically address the root cause of the corruption, rather than just stating that they do.

### Questions
Please see weakness

### Soundness
2

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
This paper investigates the phenomenon of the "corruption stage" observed in few-shot fine-tuning of Diffusion Models (DMs), where image fidelity initially improves but then deteriorates due to noisy patterns, before recovering with severe overfitting. Through heuristic modeling, the authors attribute this corruption stage to the narrowed learned distribution inherent in few-shot fine-tuning. To address this, they propose using Bayesian Neural Networks (BNNs) to expand the learned distribution via variational inference, thereby mitigating the corruption. Experimental results demonstrate that this method significantly enhances image fidelity, quality, and diversity in both object-driven and subject-driven generation tasks.

### Strengths
- This work identifies and thoroughly investigates the "corruption stage" in few-shot fine-tuning of DMs, and it presents an innovative solution using BNNs to expand the learned distribution.
- The rigorous experimental design compares different fine-tuning methods across object-driven and subject-driven tasks. Multiple quantitative metrics (e.g., Clip-T, Dino, Clip-I) validate the effectiveness of the proposed method, and user studies support these quantitative results.
- The paper follows a clear logical flow, beginning with an explanation of the corruption stage, followed by an introduction to the application and benefits of BNNs.

### Weaknesses
1. Most experiments focus on specific datasets like DreamBooth and the Stable Diffusion v1.5 model without testing other diffusion models or more advanced Stable Diffusion versions, such as SDXL, SD-v3/3.5. I understand that the authors may be trying to solve a fundamental problem, but whether this problem exists on more advanced models still needs to be proven.

2. While BNNs offer significant performance improvements, the paper lacks a detailed analysis of computational costs, such as memory usage and inference time, compared to traditional methods, which is essential for assessing applicability in real-world scenarios. In my experience, there is often a trade-off between computational cost and performance for BNN. Does this exist in this work? If it exists, could the author provide a quantitative comparison of memory usage and inference time between their BNN approach and traditional methods?

3. Although the paper claims that BNNs mitigate corruption and reduce overfitting, there is limited information on how BNNs dynamically balance image diversity and fidelity at different training stages. Could the authors provide plots or other metrics demonstrating this balance across various training stages?

### Questions
1. While BNNs reduce corruption, has the paper considered additional regularization methods to prevent overfitting in later stages?

2. Impact of Hyperparameter Tuning.

3. Does the use of BNNs significantly increase training time or memory consumption?

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
The paper investigates the “corruption stage” in diffusion models during few-shot fine-tuning, where initial image quality improvements degrade as training progresses, leading to noise and overfitting. The authors propose using Bayesian Neural Networks (BNNs) to mitigate this by broadening the learned distribution, effectively improving the fidelity and diversity of generated images. BNNs add no additional inference cost and are compatible with current fine-tuning methods.

### Strengths
1. The use of BNNs to address noise and degradation in diffusion models’ fine-tuning is innovative, providing new insights and effective mitigation strategies for this issue.

2. The paper provides a robust theoretical foundation and demonstrates the effectiveness of BNNs through various empirical tests, showcasing the improvement in image quality and diversity.

3. BNNs integrate smoothly with existing fine-tuning frameworks, and by not increasing inference costs, they retain practical relevance for computationally constrained applications.

### Weaknesses
1. Although the study shows reasonable results within the specific task context, its testing is limited to the dataset used in DreamBooth, which is too small in scope. While the authors have experimented with fine-tuning using 1, 2, and 6 images, it remains unclear whether the observed phenomena ("corruption stage") would still occur when the dataset size is increased to 1000 images or when batch size is adjusted. Given approaches like ControlNet and IP-adapter, how can it be demonstrated that the issues observed by the authors persist in large-scale fine-tuning scenarios? Furthermore, while the authors express hope that their observations might inform future research on diffusion models, it is uncertain if the proposed use of BNNs remains effective in large-scale data fine-tuning settings.

2. The paper essentially identifies a new problem and applies BNNs to few-shot fine-tuning tasks such as LoRA, which makes the novelty of the contribution somewhat limited.

3. The experiments mainly focus on score-matching-based Stable Diffusion models. It is uncertain how the proposed approach would perform with the more recent flow-matching models or with models using DiT as the denoising backbone.

### Questions
See Weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an empirical observation of diffusion models during fine-tuning in a few-shot setting, where the generated image quality undergoes a “corruption stage.” The authors analyze this corruption phenomenon through a series of experiments, beginning with single-sample fine-tuning, and provide an explanation based on noise correction terms. Building on this, they propose using Bayesian Neural Networks (BNNs) to mitigate corruption across different fine-tuning mechanisms.

### Strengths
- The observed phenomenon is compelling and would be of significant interest to the community, especially as many works focus on fine-tuning pre-trained diffusion models for downstream tasks. 
- The analytical experiments are well-designed and supported by reasonable explanations. 
- The proposed use of BNNs consistently improves performance across various fine-tuning methods.

### Weaknesses
 - This paper could benefit from a broader coverage and discussion of related works on the similar topic of generation dynamics, such as [a] and [b]. There are quite a few existing works that reveal relevant phenomena, despite that they tackle more broadly instead of focusing purely on fine-tuning scenarios. 
- Fig. 4 is somewhat confusing; the text indicates that it shows the average value of $\sigma_{1,t}$ across different values of t, yet later mentions t=100. It’s unclear how t-values are defined in Fig. 4 and in the experiments, and how t specifically impacts the BNN mitigation effects
- The authors include qualitative examples of the best and average-case generations; however, I am curious about the worst-case scenarios. A detailed discussion of failure cases would be equally important and valuable, in many generation related works.
- Something more minor, I think it would be beneficial to compare the actual fine-tuning cost versus the BNNs applied tuning cost in Tab. 3 (or separately in Appendices).
- There is one missing "**(**" in Eq. 3. Also isn't it $KL(Q_w(\theta)||P(\theta))$ rather than $KL(P(\theta)||Q_w(\theta))$, or did I miss anything?

### Questions
Please see the weaknesses for my detailed questions.

### Soundness
3

### Presentation
3

### Contribution
2
