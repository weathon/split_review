# HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuning LLM with Zeroth-order Optimization

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
Fine-tuning large language models (LLMs) poses significant memory challenges, as the back-propagation process demands extensive resources, especially with growing model sizes. Recent work, \mezo{}, addresses this issue using a zeroth-order (ZO) optimization method, which reduces memory consumption by matching the usage to the inference phase. However, \mezo{} experiences slow convergence due to varying curvatures across model parameters. To overcome this limitation, we introduce \helen{}, a novel scalable and memory-efficient optimizer that integrates annealed A-GNB gradients with a diagonal Hessian estimation and layer-wise clipping, serving as a second-order pre-conditioner. 
This combination allows for faster and more stable convergence. Our theoretical analysis demonstrates that \helen{} improves convergence rates, particularly for models with heterogeneous layer dimensions, by reducing the dependency on the total parameter space dimension. Instead, the method scales with the largest layer dimension, making it highly suitable for modern LLM architectures. Experimental results on RoBERTa-large and OPT-1.3B across multiple tasks show that \helen{} achieves up to a $20\times$ speedup compared to \mezo{}, with average accuracy improvements of 1.5\%. Furthermore, \helen{} remains compatible with both full parameter tuning and parameter-efficient fine-tuning (PEFT), outperforming several state-of-the-art optimizers.
The codes will be released after reviewing.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes HELENE, which builds upon prior work, MeZO, by integrating a second-order preconditioning method designed to achieve faster, more stable convergence while maintaining a low memory footprint. The authors evaluate HELENE on prominent models, RoBERTa-large and OPT-1.3B, and report promising results in terms of speedup and accuracy.

### Strengths
HELENE’s integration of annealed A-GNB gradients and layer-wise clipping shows the authors' awareness of the specific computational nuances of finetuning LLM architectures, the discussion of EMA showed the and other related discussion showed good motivation.

Plus, memory saving is always crucial for better finetuning LLMs these days, HELENE's layer-wise approach is a solid step to conserve memory.

### Weaknesses
In the core algorithm:
- Gradient Computation (Steps 4–5): HELENE computes the gradient based on Simultaneous Perturbation Stochastic Approximation (SPSA), a zeroth-order optimization technique, which allows it to approximate gradients without needing backpropagation. This step saves memory, which is important for large models. However, SPSA tends to converge more slowly than direct gradient methods, and while the authors use annealing, it’s unclear if this fully mitigates the slower convergence. The use of SPSA, while memory-efficient, introduces a fundamental trade-off with convergence speed, which is particularly concerning when fine-tuning large models where convergence time is a critical factor. The paper needs to provide a more detailed analysis of this trade-off, perhaps by comparing the number of iterations required for HELENE to reach a certain level of accuracy against first-order methods.
- Annealing Schedule (Step 6): The annealing parameter α=Anneal(t) in Step 6 adjusts the moving average coefficient based on iteration count. the improvement here compared to EMA is not obvious in figure 5? (is this a wrong figure link) The annealing mechanism's effectiveness is not clearly demonstrated, and the paper lacks a clear explanation of why the specific annealing schedule is superior to a standard EMA approach. The ablation study should include a wider range of annealing schedules to justify the chosen approach. Furthermore, the paper should provide a more detailed analysis of how the annealing parameter affects the convergence rate and final performance.
- Although layerwise clipping seems beneficial, it also introduces additional hyperparameters and tuning complexity. The layer-wise clipping, while potentially beneficial for stability, introduces a significant hyperparameter tuning burden. The paper needs to provide a more in-depth analysis of the sensitivity of the model's performance to the clipping thresholds for each layer. It is unclear how these hyperparameters should be chosen in practice, and the paper should provide more guidance on this process.
- The authors assert that the inclusion of the Hessian diagonal significantly improves convergence rates, but diagonal Hessian approximation methods generally struggle to capture the full curvature dynamics in deep networks. For HELENE to have a true advantage, empirical evidence comparing convergence rates with Adam and other optimizers is crucial: the accuracy improvement of 1.5% might not fully justify the added implementation and tuning complexity, especially if simpler optimizers (like Adam or AdamW)

### Questions
The 20× speedup is largely theoretical here, as HELENE’s slower convergence due to SPSA may offset this benefit in practice. 
could you kindly provide a detailed profiling log comparing the actual run time?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a novel zeroth-order fine-tuning method, HELENE, designed to enhance the efficiency and stability of model training through three core components. First, HELENE introduces an annealing mechanism in the momentum's exponential moving average (EMA) to mitigate bias in the SPSA-estimated gradients and reduce the impact of noise in the gradients during the later stages of training. Second, it proposes a new estimator for the Hessian matrix, known as the Asymptotic Gauss-Newton-Bartlett (A-GNB) estimator, which enables diagonal Hessian estimation without the need for label sampling, simplifying the computation process. Finally, HELENE implements layer-wise Hessian clipping, which more effectively preserves essential second-order information, ultimately improving the convergence and stability of the optimization process. Experimental results on RoBERTa-large and OPT-1.3B demonstrate that HELENE achieves an improvement over MeZO, with notable gains in both convergence speed and model performance.

### Strengths
1. The design of HELENE is elegant, addressing various issues that arise during the optimization process. The incorporation of mechanisms such as gradient annealing and layer-wise clipping demonstrates a thoughtful approach to enhancing training stability and convergence.
2. The analysis of the convergence steps is welcome, providing insights into the efficiency of the optimization process and enhancing the overall contribution of the paper.
3. Experimental results provide evidence of HELENE's improvements over MeZO, particularly in fine-tuning tasks with RoBERTa-large and OPT-1.3B, showcasing the effectiveness of the proposed method.

### Weaknesses
1. The presentation and structure of the paper exhibit significant issues. While the paper claims to introduce a zeroth-order optimization method, the entire methodology section appears disconnected from both zeroth-order principles and MeZO. Three key components lack intuitive connections, making them seem disjointed at least from the writing perspective. Specifically, the paper introduces three components—an annealing mechanism for momentum's EMA, an Asymptotic Gauss-Newton-Bartlett (A-GNB) estimator for the Hessian, and layer-wise Hessian clipping—without clearly articulating how these components synergistically address the challenges inherent in zeroth-order optimization, or how they relate to the MeZO framework. The lack of clear motivation for each component and their interdependencies makes the method seem ad-hoc.
2. HELENE incurs substantial memory overhead compared to MeZO. The introduction of momentum and Hessian as optimizer states brings memory costs close to full parameter fine-tuning, which is significantly higher than that of parameter-efficient fine-tuning methods like LoRA. The paper does not adequately quantify this overhead, making it difficult to assess the practical trade-offs between performance gains and increased memory consumption. A detailed analysis of memory usage, especially in comparison to parameter-efficient methods, is missing.
3. The experimental component is lacking, as there are no evaluations on larger models such as LLaMA2-7B or LLaMA2-13B. Additionally, the ablation study is insufficiently detailed. Given the three key designs in HELENE, it would be beneficial to create three variants, each removing one of the designs to observe the impact on performance. The current ablation study does not isolate the effects of each component, making it difficult to understand their individual contributions. The absence of experiments on larger models limits the generalizability of the findings.
4. The writing contains typos. For example, Line 134 states "first-order methods like MeZO," which should be corrected to "zeroth-order methods like MeZO." In statement 1 of Algorithm 1, there is a repeated $\epsilon$, and "hyperparameters $\lambda_i$" should be written as "hyperparameters {$ \lambda_i  $}."

### Questions
1. I would like to know the GPU memory usage of HELENE in your experiments. In theory, HELENE’s memory requirements should exceed those of LoRA, so it’s important to provide a detailed comparison with LoRA (without MeZO). Could you please provide a table listing the actual memory consumption and performance results of HELENE, MeZO, LoRA, and full-parameter Adam fine-tuning when fine-tuning OPT-1.3B with the same batch size?
2. What is the time overhead of HELENE compared to the original MeZO? Could you please report the wall clock time per iteration for both HELENE and MeZO when fine-tuning OPT-1.3B with the same batch size?
3. In Section 3.3.1 on the annealing mechanism, the paper mentions that this mechanism helps reduce the impact of noisy or outdated gradients in the later stages of training. However, since $\alpha$ decreases as the time step increases, the actual weight of momentum from earlier steps actually increases, seemingly contradicting the claim that it “reduces the impact of past gradients.” Could you clarify this statement? Also, please explain the phrasing in Line 258: “reducing the learning rate as training progresses”?
4. In Algorithm 2, Statement 4 appears without clear derivation. Could you please explain how this statement was derived?
5. From my understanding, HELENE seems decoupled from MeZO, meaning it should theoretically be applicable in standard first-order optimization as well. Is my understanding correct? If so, do you have any preliminary results showing whether HELENE is effective in first-order methods?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Helene with 3 components adds to MeZO: (1) A-GNB estimator of Hessian diagonal without label sampling (2) layerwise adaptive clipping (3) momentum update annealing. The convergence steps improve from Sophia's $O(d)$ to $O(\text{max}_i d_i)$. The experiments follow the settings of MeZO and are conducted for RoBERTa-large and OPT-1.3B across multiple tasks.

### Strengths
1. A-GNB estimator removes the need to sample label from the model.
2. The experiments are comprehensive.

### Weaknesses
1. The theory is significantly mismatched with the experiments. The theory is actually proven under the case of first-order gradients, but the method and the whole experiments are performed under zeroth-order SPSA estimated gradient (this is obfuscated by their notations in Algorithm 1 that I believe they should use $\hat{g}$ instead of $g$ when they are referring to ZO estimated gradient. I also checked their codes and the experiments are fully in ZO). A direct transfer from FO or second-order optimizer's convergence rate to ZO convergence rate is *a nontrivial task* and usually *unapplicable*.

2. I don't see the annealing momentum and A-GNB is used in Lemma 10. If I understand correctly, the Lemma 10 applies to the case that we have exact gradient and clipped Hessian diagonal, but Algorithm 1 uses estimators for both. 

3. A comparison with other ZO optimizers, such as HiZZO [1], that also leverage second-order information to address the varying parameter curvature issue is missing. 

4. By employing "A-GNB estimator" that uses true labels, Helene's Hessian estimator becomes clipped second moment of (SPSA-estimated) gradient, which is also shown in their code. The difference from Helene and Adam seems only to be (1) clipping second-moment term, (2) update second-moment term in less frequency, and (3) annealing momentum update. In this case, I would doubt how Helene outperforms Adam in general cases. From Figure 5a, it seems that the greatest performance boost from MeZO to Helene is actually momentum annealing. 

The first weakness is critical and I would vote for a reject score at this moment.

### Questions
1. Is there any proof or reference that shows A-GNB is an unbiased estimator of Hessian? *A-GNB's construction is similar to the empirical Fisher's construction on the diagonal part*, and the expectation of empirical Fisher is known to *not equal* to the Hessian. On the other hand, Fisher information matrix needs label sampling from the model and its expectation is equal to the negative of Hessian.

2. The ICL baselines in Table 2 seem dubiously weak for some trials (ICL show no or minimal improvements from the zeroshot in RTE, WSC, COPA, and ReCoRD). For COPA, the ICL's performance is even worse than zeroshot's.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes to incorporate diagnonal hessian information to improve zero-order optimization methods.

### Strengths
Proposed method is better than MeZO.

### Weaknesses
The practical utility of the proposed optimizer is very questionable.

During training and fine-tuning, the GPU memory is consumed by two things:
a) Parameters + optimizer buffers.
b) Stored forward pass activations.

Let's call the memory needed for parameters P. Let's call memory required for storing activations G.
G can be easily reduced by doing gradient checkpointing (this is oneliner with current models).
Also, as the model's size grows, G becomes much smaller than P (because G scales linearly with model width and P quadratically).
When doing ordinary Adam, one needs 4P + G memory.
When doing something like LoRA or GaLORE, one needs P + G + <a little> memory.
Everybody is doing LoRA & friends because gradient activations are small, and storing parameters more than once is a big problem.
In extreme case, we are doing LoRA over quantized parameters (QLoRA), which needs P/4 + G memory. Again, testament than in practice G is much smaller than P.
Also, it is possible to drop most of the optimizer buffers and update parameters during a backward pass (like AdaLOMO), which again takes P + G memory.

Yet, this method just proposes using 2P memory because, in addition to parameters, it also needs to store diagonal Hessians. 
If I have space for 2P memory, I can probably make my batch size very small and just use SGD with momentum (note that I can do tricks like AdaLOMO does and not store more than one computed gradient).
I just cannot imagine any setting where I would want to use this method. It also seems that the method requires 3*P memory (not 2*P as I thought) and 32 bits of precision, based on the 16 GB used for OPT-1.3B tuning. That's 3 * 32 = 96 bits per parameter. I can achieve similar or better memory usage with AdamW using 16-bit storage plus a precision correction term, requiring only 5 * 16 = 80 bits per parameter, and also use gradient checkpointing to reduce activation storage. Furthermore, this approach allows for gradient accumulation, which is not possible with the proposed method.

### Questions
How does this method compare to properly tuned low-memory first-order methods (like AdaLomo, GaLore, ...)?

### Soundness
2

### Presentation
3

### Contribution
1
