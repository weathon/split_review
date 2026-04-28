# Steering Masked Discrete Diffusion Models via Discrete Denoising Posterior Prediction

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Generative modeling of discrete data underlies important applications spanning text-based agents like ChatGPT to the design of the very building blocks of life in protein sequences. However, application domains need to exert control over the generated data by steering the generative process—typically via RLHF—to satisfy a specified property, reward, or affinity metric. In this paper, we study the problem of steering Masked Diffusion Models (MDMs), a recent class of discrete diffusion models that offer a compelling alternative to traditional autoregressive models. We introduce Discrete Denoising Posterior Prediction (DDPP), a novel framework that casts the task of steering pretrained MDMs as a problem of probabilistic inference by learning to sample from a target Bayesian posterior. Our DDPP framework leads to a family of three novel objectives that are all simulation-free, and thus scalable while applying to general non-differentiable reward functions. Empirically, we instantiate DDPP by steering MDMs to perform class-conditional pixel-level image modeling, RLHF-based alignment of MDMs using text based rewards, and finetuning protein language models to generate more diverse secondary structures and shorter proteins. We substantiate our designs via wet-lab validation, where we observe transient expression of reward-optimized protein sequences.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This is a very interesting paper that design a new framework DDPP to sample from a target Bayesian posterior by steering pretrained MDMs. The author derived 3 primary objectives within the DDPP: DDPP-IS, DDPP-LB, DDPP-KL, providing different methods to handle the intractable partition function in the Bayesian posterior. This framework demonstrated strong performance across diverse tasks. In synthetic tasks, DDPP generated target-aligned samples with higher fidelity than baselines. For image modeling on the CelebA dataset, it produced attribute-specific images with competitive fidelity. In protein sequence modeling, DDPP generated high-quality sequences optimized for specific structural features, validated by wet-lab testing. In text generation, DDPP achieved alignment with sentiment and toxicity targets, producing fluent and reward-optimized outputs. Overall, DDPP consistently outperformed baselines, effectively steering model outputs to meet specific reward criteria across varied domains.

### Strengths
1. The authors introduce the DDPP framework for steering MNDMs  by treating the task as sampling from a Bayesian posterior, which is an innovative approach for discrete generative models. They derive three scalable, simulation-free objectives that make fine-tuning computationally efficient, even for large pre-trained models.
2. Extensive experiments were conducted across diverse tasks, including image modeling, text generation, and protein sequence design. DDPP demonstrated strong performance across all domains, highlighting its adaptability to various data types and applications.
3. The paper includes wet-lab validation for protein sequence tasks, confirming the practical applicability of the model in real-world protein design. This physical validation of AI-generated outputs adds quite a lot credibility.
4. The paper is clearly written and well-structured. The presentation is overall good.

### Weaknesses
1. Including autoregressive models as baselines could be useful, as they are widely used and effective in many generative tasks. Specifically, comparing against fine-tuned autoregressive models, which are often optimized for similar objectives, would provide a more comprehensive understanding of DDPP's performance. This is particularly important given the prevalence of autoregressive models in sequence generation tasks, and would help contextualize the benefits of using a masked diffusion approach.
2. Since DDPP-IS involves MCMC, it would be helpful to analyze the computational cost of each method, covering both training and inference phases. The analysis should include a breakdown of the time complexity of each step, such as the number of forward passes through the model, the number of reward function evaluations, and the overhead of the MCMC sampling process. This is crucial for understanding the practical applicability of DDPP-IS, especially when dealing with large models or computationally expensive reward functions.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper construct transition distributions of discrete diffusion models for sampling from the composed distribution $\pi_0(x_0) = p(x_0) R(x) / Z$, sometimes referred to as "guided" generation with reward function $R(x)$. Unlike in continuous space diffusions, the transition distribution  $p(x_{t-1} | x_t)$ corresponding to $\pi_0(x_0)$ cannot be approximated using a Taylor expansion around $x_t$. The method proposed by the authors instead trains a second model $q(x_0 | x_t)$ to match the effective transition distribution of $\pi_0(x_0)$. The primary challenge of matching the transition distribution of $\pi_0(x_0)$ is estimating the log partition function $\log Z$, and the authors propose three approaches to overcoming this challenge: (1) approximating $\log Z$ through importance sampling (2) parameterizing $\log Z$ with a neural network (3) foregoing approximation of $\log Z$ by matching the reverse KL, which instead requires back-propagation through stochastic discrete sampling. Each of these variants has slightly different requirements for inference/train time compute, or differentiability of $R$. The authors evaluate their proposed variants on a few toy tasks as well as on conditional image generation and protein design. Overall they find that the proposed method (DDPP) achieves better reward values while maintaining plausible samples.

### Strengths
The paper provides a nice overview of the problem of discrete guidance and several sensible solutions to it. I appreciate that the authors implemented several variants and compared them to each other, as it offers more signal to the community about promising directions. The significance of the work is substantial because discrete diffusion models are increasingly popular in both text applications, where guidance can equate to controllability/alignment, and for scientific modalities, where guidance is used for solving inverse problems. I personally don't find the originality to be high, as the method largely adopts pre-existing tools to solve the problems that arise in implementing each variant of their method, but I don't think this relatively low originality outweighs the quality of the work's presentation and analysis. To this end, I found the evaluation of the method mostly satisfactory, as it spanned multiple modalities and even included some wet lab experiments.

### Weaknesses
As I stated briefly above, I don't see the paper as making any foundational contributions that are broadly applicable beyond guidance of discrete diffusion models or any observations that are deeply surprising in nature. The paper is driven by a narrow and practical goal of finding a good method for approximating $\log Z$ (or foregoing its approximation) when training a secondary model $q$ to approximate the transition distribution of $\pi_0 (x_0)$. I personally don't find these contributions lackluster, as guidance of discrete diffusions is an open problem with practical impact. In terms of evaluation, the results seem fairly reasonable and there are some helpful baseline comparisons, though it's a little challenging to conclude much from the wet lab experiments when the only non-control methods are DDPP, so it's unclear how much heavy lifting the posterior inference method is doing versus other facets of sampling and filtering.

One notable limitation of the proposed method is that it requires training a secondary model in the first place. Once trained, this secondary model has relatively fast sampling, and therefore the training amortizes depending on how much inference is performed. In many scientific applications, inference can be relatively limited and throughput is often more important than latency, so in some cases maybe this tradeoff is not entirely worth it depending on the cost and complexity of setting up the post-training procedure, but I don't think these considerations disqualify the approach in general. It's also worth noting that best-of-N sampling seems to perform quite well in many experiment for relatively small N, even approaching the performance of DDPP in some cases, and this method can be deployed essentially out of the box, with only inference time overhead (which might be relatively minor).

### Questions
1. Why was no comparison made to other methods that post-train diffusion models with preference data, e.g. Diffusion-DPO [1]? Is there a fundamental limitation of these methods in the discrete setting or would porting these methods to a discrete setting just end up looking similar to DDPP-KL? 
2. Was any variance reduction method required to make DDPP-KL work in practice? 
3. Why is it sufficient that DDPP-LB provides a lower bound on the log partition? As far as I can tell the loss functions can incentive minimizing the value of log partition, in which case minimizing a lower bound is not analogous to minimizing the bounded quantity. 
4. In the language examples, DDPP appears to perform much better than the provided baselines. Do you have any sense for how these conditional samples might compare to samples from a similar sized autoregressive model used in tandem with "steering" methods for autoregressive models (e.g. PPLM, fudge, twisted SMC). These models a probably capable of generating samples with higher likelihoods and many of these methods are "plug-and-play", meaning they don't require training a secondary model. Therefore, in practical settings, they might still be preferred over this method. 

[1] Diffusion Model Alignment Using Direct Preference Optimization. Wallace et al. (2023)

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
This paper addresses the task of controlled generation of a pretrained masked diffusion model (MDM) $p^{\rm pre}(x)\approx p _0(x)$ towards an altered target distribution $\pi _0(x)\propto p _0(x)R(x)$, where $R(x)$ is a reward function. The approach involves fine-tuning the MDM to align with the new target distribution. The paper introduces a simulation-free framework called "discrete denoising posterior prediction" (DDPP) to train the amortized MDM. The framework has shown promising empirical results for various tasks in image, text, and proteins.

### Strengths
The paper addresses the important problem of controlled generation, which has significant applications as discussed in the paper. The proposed DDPP framework, consisting of three different versions, is a novel approach that efficiently tackles this problem without simulating the reverse diffusion process. The empirical results demonstrate the superiority of the DDPP method over several baseline methods, including best-of-$N$, SVDD, and RTB. This highlights the effectiveness and potential of the proposed framework in the context of discrete diffusion models.

The paper is well-written and clearly organized, and provides sufficient details to understand and replicate the experiments. However, further improvement can be made in the clarity of the mathematical explanations.

### Weaknesses
The methodologies introduced in the paper are somewhat confusing to me, and I am unable to fully grasp the underlying intuition behind their design. Please check the question part for details.

The writing of the paper, particularly the mathematical explanations, could benefit from improvement. I have provided comments and suggestions in the part regarding these issues.

### questions:
 1. Questions for the framework.

- Could the author(s) provide further insight into the rationale behind choosing an $L^2$-based loss in learning $q _\theta({\bf x} _0,...,{\bf x} _{t-1}|{\bf x} _t,\hat{\bf x} _0)$ in DDPP-IS/LB? The use of an $L^2$-based loss comparing the difference of log-densities is not commonly seen in the literature of learning probability distributions (e.g., variational inference), and it requires learning or estimating the normalizing constant ${\cal Z} _{\pi _t}({\bf x} _t)$, which involves computational overhead. Furthermore, what is the probability of ${\bf x} _{0:t}$ in the losses in equations (7,8,11,43)? Although this can be any trajectory, it would be beneficial to clarify your choice for the experiments.

- In DDPP-KL, the author(s) employ the reverse KL loss instead of forward KL loss. However, this requires the differentiability of reward function $R(x)$, and needs the Reinmax trick to estimate the discrete gradients. It would be valuable if the author(s) could elaborate on why the forward KL loss is not suitable in this context.

2. As discussed in Ou et al. (2024) and later Zheng et al. (2024), the time component in MDMs does not play a significant role. An MDM $\mu _\theta({\bf x},t)\in(\Delta^d)^n$ is equivalent to an any-order autoregressive model, i.e., it predicts the one-dimensional conditional probability distributions of the masked positions given the observed ones in a partially observed sequence. If we formulate the MDM without time component, how would your fine-tuning framework be adapted?

3. Questions regarding the experiments.

- In the MNIST experiment, what would be the possible reason why SVDD having a higher reward value $\log R({\bf x} _0)$ compared with DDPP? Additionally, why is there no BPD metric for the samples generated by SVDD?

- In the CelebA experiment, it seems that the quality of samples from DDPP (Figure 3) is worse than those from the pretrained model (Figure 5).

4. Minor comments

- In lines 89 and 97, it seems that the notation $\cal V$ should be $\cal X$ instead.

- In line 98, the RHS of the equation $p({\bf X}={\bf x})$ is a bit confusing. Does it imply that each position is mutually independent? Clarification would be helpful.

- In line 105, it might be more appropriate to say "drop $t$ and write $i$" instead. Since the paper uses a discrete time setting, replacing $\tau({\bf x} _{0:1})={\bf x} _1\to\cdots\to{\bf x} _t\to{\bf x} _0$ with $\tau({\bf x} _{0:T})={\bf x} _T\to\cdots\to{\bf x} _t\to{\bf x} _0$ would be more appropriate.

- In section 2.1, when dealing with multiple dimensions, $\mu _\theta({\bf x},t)$ should be in $(\Delta^d)^n$, which predicts the probabilities $\Pr({\bf X} _0^i=\cdot|{\bf X} _t={\bf x})$.

- In line 260, it would be better to move the training objective (Eq. 11) to this location for better readability.

- Furthermore, I noticed a few typos or errors in the paper. For example, in line 323, it states "In settings, where the reward model is differentiable", and in line 430, it says "We provide full a deeper description of evaluation metrics and experimental setup". I strongly recommend that the author(s) carefully review and polish the writing in this paper during the rebuttal period to ensure clarity and accuracy.

### Questions
1. Questions for the framework.

- Could the author(s) provide further insight into the rationale behind choosing an $L^2$-based loss in learning $q _\theta({\bf x} _0,...,{\bf x} _{t-1}|{\bf x} _t,\hat{\bf x} _0)$ in DDPP-IS/LB? The use of an $L^2$-based loss comparing the difference of log-densities is not commonly seen in the literature of learning probability distributions (e.g., variational inference), and it requires learning or estimating the normalizing constant ${\cal Z} _{\pi _t}({\bf x} _t)$, which involves computational overhead. Furthermore, what is the probability of ${\bf x} _{0:t}$ in the losses in equations (7,8,11,43)? Although this can be any trajectory, it would be beneficial to clarify your choice for the experiments.

- In DDPP-KL, the author(s) employ the reverse KL loss instead of forward KL loss. However, this requires the differentiability of reward function $R(x)$, and needs the Reinmax trick to estimate the discrete gradients. It would be valuable if the author(s) could elaborate on why the forward KL loss is not suitable in this context.

2. As discussed in Ou et al. (2024) and later Zheng et al. (2024), the time component in MDMs does not play a significant role. An MDM $\mu _\theta({\bf x},t)\in(\Delta^d)^n$ is equivalent to an any-order autoregressive model, i.e., it predicts the one-dimensional conditional probability distributions of the masked positions given the observed ones in a partially observed sequence. If we formulate the MDM without time component, how would your fine-tuning framework be adapted?

3. Questions regarding the experiments.

- In the MNIST experiment, what would be the possible reason why SVDD having a higher reward value $\log R({\bf x} _0)$ compared with DDPP? Additionally, why is there no BPD metric for the samples generated by SVDD?

- In the CelebA experiment, it seems that the quality of samples from DDPP (Figure 3) is worse than those from the pretrained model (Figure 5).

4. Minor comments

- In lines 89 and 97, it seems that the notation $\cal V$ should be $\cal X$ instead.

- In line 98, the RHS of the equation $p({\bf X}={\bf x})$ is a bit confusing. Does it imply that each position is mutually independent? Clarification would be helpful.

- In line 105, it might be more appropriate to say "drop $t$ and write $i$" instead. Since the paper uses a discrete time setting, replacing $\tau({\bf x} _{0:1})={\bf x} _1\to\cdots\to{\bf x} _t\to{\bf x} _0$ with $\tau({\bf x} _{0:T})={\bf x} _T\to\cdots\to{\bf x} _t\to{\bf x} _0$ would be more appropriate.

- In section 2.1, when dealing with multiple dimensions, $\mu _\theta({\bf x},t)$ should be in $(\Delta^d)^n$, which predicts the probabilities $\Pr({\bf X} _0^i=\cdot|{\bf X} _t={\bf x})$.

- In line 260, it would be better to move the training objective (Eq. 11) to this location for better readability.

- Furthermore, I noticed a few typos or errors in the paper. For example, in line 323, it states "In settings, where the reward model is differentiable", and in line 430, it says "We provide full a deeper description of evaluation metrics and experimental setup". I strongly recommend that the author(s) carefully review and polish the writing in this paper during the rebuttal period to ensure clarity and accuracy.

I would be happy to raise the score if the author(s) could address my concerns.

**References**

Ou et al. Your Absorbing Discrete Diffusion Secretly Models the Conditional Distributions of Clean Data. Arxiv 2406.03736.

Zheng et al. Masked diffusion models are secretly time-agnostic masked models and exploit inaccurate categorical sampling. ArXiv 2409.02908.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces Discrete Denoising Posterior Prediction (DDPP), a framework for guiding Masked Discrete Diffusion Models (MDMs) toward a reward model. DDPP offers three scalable, simulation-free objectives—DDPP-IS, DDPP-LB, and DDPP-KL—suited for fine-tuning MDMs in tasks like image modeling, protein design, and text generation.

### Strengths
1. The paper presents DDPP, a method to align Masked Diffusion Models (MDMs) with reward functions directly at inference, skipping RL and costly sampling typical for autoregressive models.

2. DDPP is backed by theories.  Additionally, its three variants—DDPP-IS, DDPP-LB, and DDPP-KL— are designed for both differentiable and non-differentiable rewards. These enable efficient MDM fine-tuning with strong performance across tasks, which is impressive.

3. The writing flow of this work is somehow clear. I find the presentation smooth and easy to follow.

### Weaknesses
1. First of all, while the presentation was good, I found the paper’s theoretical parts were not very easy to follow. I would suggest simplifying theory sections and providing illustrations to improve readability. It is still not crystal clear to me what are the motivations and the differences for making such 3 variants. For instance, for DDPP-KL, which involves a reverse KL divergence objective, the authors break down its computational pathway further, which might help readers better grasp the core mechanisms quickly.

2. Since the study centers on MDMs, it remains unclear if DDPP can generalize to other types of discrete diffusion models or if the results depend heavily on the MDM-specific setup.

3. The authors claimed that DDPP enabled efficient MDM fine-tuning across many domains. There's still limited discussion of the computational costs relative to baseline approaches. For example, I assume SVDD is computationally friendly as it is purely inference time. Furthermore, it can balance memory and time for lighter computation demands. Thus, in terms of computation efficiency, I would assume DDPP is not superior to SVDD. Would the authors comment on this?

Firstly, regarding the novelty of this work,  technically, I found it is just a variance of path consistency learning in the discrete setting (gflownet papers often used these loss functions). Thus, it becomes unclear (1) why this algorithm is special in the discrete setting as compared to standard continuous setting and (1) what the technical difficulty is for making this extension.

Second, the experimental part is incomplete. This work lacks lots of baselines/discussions that should be compared with, in terms of fine-tuning-based alignments, there is no comparison with classifier free guidance, DDPO/DPOK, and direct reward backpropagation which are all prevailing approaches for guided generations. Comparisons with the most common inference-time guidance methods are also missing, such as classifier guidance in discrete diffusion [1]. In a continuous setting, it is common that new alignment/guidance methods will take classifier guidance as a standard baseline to compare with. In a discrete setting, it is also probably considered essential.

Moreover, omitting comparisons with sequential Monte Carlo (SMC) methods is another significant gap. These methods are relevant for inference in diffusion processes, and their inclusion would provide a more comprehensive understanding of DDPP's efficiency and performance. Other reviewers have flagged this part as a common concern.

The authors' discussion of SVDD performance is similarly incomplete. After investigating this baseline, I found it is basically a nested-SMC whose performance depends heavily on the duplication number. However, this paper does not even include a detailed analysis or discussion of this dependency. The lack of mention or exploration of this aspect weakens the empirical evaluation, which is problematic: have the baseline implementations in this work achieved their best performances?

Furthermore, the authors state that certain rewards used in their experiments are not differentiable, which limits comparisons with baselines like discrete guidance. This claim is imprecise as far as I am concerned. Many protein forward/inverse folding models, including AlphaFold, are differentiable (as highlighted in sources like (https://onlinelibrary.wiley.com/doi/full/10.1002/pro.4653). This raises questions about why such differentiable rewards were not incorporated.

### Questions
1. Could DDPP be adapted to other types of discrete generative models beyond MDMs such as autoregressive or flow-based discrete models?

2. Relevant to weakness, how does the computational cost of DDPP compare to other fine-tuning/inference-time approaches, especially in larger-scale applications?

3. Protein design applications can involve sequences of varying lengths, which might affect DDPP’s performance. How does the method scale with longer or structurally complex sequences? I suppose an ablation study on sequence length is critical.

4. The paper introduces three variants of DDPP (DDPP-IS, DDPP-LB, and DDPP-KL) but does not make it clear which one is preferred in what scenarios. Could the authors comment on selecting the right variant given specific reward functions or computational constraints?

### Soundness
2

### Presentation
3

### Contribution
2
