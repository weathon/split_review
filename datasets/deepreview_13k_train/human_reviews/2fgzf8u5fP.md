# Derivative-Free Guidance in Continuous and Discrete Diffusion Models with Soft Value-Based Decoding

- Decision: Reject
- Scores: 5, 3, 5, 3, 3

## Abstract
Diffusion models excel at capturing the natural design spaces of images, molecules, and biological sequences of DNA, RNA, and proteins. However, for many applications from biological research to biotherapeutic discovery, rather than merely generating designs that are natural, we aim to optimize downstream reward functions while preserving the naturalness of these design spaces. Existing methods for achieving this goal often require ``differentiable'' proxy models (\textit{e.g.}, classifier guidance) or computationally-expensive fine-tuning of diffusion models (\textit{e.g.}, classifier-free guidance, RL-based fine-tuning). Here, we propose a new method, \textbf{S}oft \text{V}alue-based \textbf{D}ecoding in \textbf{D}iffusion models ({\alg}), to address these challenges. {\alg} is an iterative sampling method that integrates soft value functions, which looks ahead to how intermediate noisy states lead to high rewards in the future, into the standard inference procedure of pre-trained diffusion models. Notably, {\alg} avoids fine-tuning generative models and eliminates the need to construct differentiable models. This enables us to (1) directly utilize non-differentiable features/reward feedback, commonly used in many scientific domains, and (2) apply our method to recent discrete diffusion models in a principled way. Finally, we demonstrate the effectiveness of {\alg} across several domains, including image generation, molecule generation (optimization of docking scores, QED, SA), and DNA/RNA generation (optimization of activity levels).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a method for diffusion models to sample data that is both within target distribution and maximizing some downstream reward function. The problem the paper studies is of great importance, and the method shows empirical effectiveness in some downstream tasks.

### Strengths
- The paper is generally well-written, and the motivation is also clear. It starts with an important problem and proposes a well-motivated solution that requires no finetuning or differential proxy model. 

- The paper is clear about how two critical challenges (the soft-value function is both unknown and unnormalized) are addressed by the proposed algorithm.

### Weaknesses
 - The soft value function seems to difficult to approximate in general. Is there any anlysis or justification to quantify the quality of the approximation? How does one know a good approximation is indeed attained? Moreover, how does the approximation quality matter for the generation? More ablation study can improve the paper further.

- Is there any additional computational overhead for the proposed method? Is the approximation to the soft value function costly?

- The performance gain does not seem to be very significant compared to simple baselines, say Best-of-N. From Table 2, Best-of-N baseline is only incrementally worse than the proposed method in molecule-related experiments.

- A minor question: Does the size of the diffusion model affect the performance of SVDD? I will be interested to see how this method works for diffusion models of different size.

### Questions
See the weakness section.

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
4

### Summary
The paper introduces SVDD, a method which aims to sample from the product distribution $p^*(x_0) \propto p^{pre}_0(x_0) \exp(R(x_0)/\alpha)$ for some non-negative reward function $R(x)$, constant $\alpha \geq 0$ and pre-trained diffusion model $p^{pre}_t(x_t | x_{t + 1})$.

The method employs an SMC-inspired procedure for iteratively sampling and reweighting samples according to a soft value function and its corresponding optimal policy.  Providing two options to obtain the soft-value function (which is required for the method's importance sampling step), the authors show that SVDD can be used with a cheap approximation based on the diffusion model's denoiser or an amortized version based on regression to a Monte Carlo estimate.  The authors evaluate the performance of SVDD on a series of tasks -- images, molecule design, and DNA/RNA design.

### Strengths
The paper presents a number of strengths, such as

- Presenting a novel application of nested Sequential Monte Carlo to the difficult problem of sampling from the product distribution $p^*(x_0)$ given a pre-trained diffusion model.
- The method, especially SVDD-PM, provides a particularly efficient method to sample from the product distribution when no differentiable reward is available and the reward function is cheap.  The manuscript shows that SVDD can indeed increase the reward over the pre-trained model, offering a compelling option to sample from the target product distribution with little overhead.
- The problem of cheaply sampling from the product distribution in the presence of non-differentiable rewards is especially significant as existing methods typically require availability of gradients or expensive (typically simulation-based) fine-tuning algorithms.  Non-differentiable rewards are often seen in scientific discovery, a target area aptly pointed out by the authors.

### Weaknesses
Overall I had a some issues regarding clarity of the paper, concerns about sources of bias that are not discussed in the manuscript, and am worried that the experimental section does not paint a fair picture of SVDD's performance relative to baselines.  I will discuss each of these in turn



### Unclear focus of probabilistic inference vs reward maximization

Section 3.2 states that the objective of this paper is to perform probabilistic inference and sample from the target distribution $p^*(x_0) \propto p^{pre}(x_0)\exp(R(x_0) / \alpha)$.  However, towards the beginning of the experiment section and throughout the appendix the manuscript begins to say that SVDD is actually meant for reward maximization, not the problem of sampling from $p^*(x_0)$.  In particular, the manuscript states that in practice they set $\alpha = 0$ for all experiments, which corresponds to a constrained reward maximization where $p^*(x_0)$ is a Dirac centered at $x_0^* = \underset{x_0 \in Support(p_0^{pre}(x_0))}{\arg\max}R(x_0)$.  This is quite different from sampling from the $p^*(x_0)$ for any $\alpha$ and if this is the goal of SVDD it should be compared to baselines which try to do reward maximization.



### Missing discussion and investigation on bias of soft value function estimates

The manuscript defines the soft value function as $v_t(x_t) = \alpha \log \mathbb{E}_{x_0 \sim p^{pre}(x_0 | x_t)}[\exp(R(x_0) / \alpha)]$.  Next, due to issues with numerical stability for small values of $\alpha$ the authors make use of an approximation

$v_t(x_t) = \alpha \log \mathbb{E}_{x_0 \sim p^{pre}(x_0 | x_t)}[\exp(R(x_0) / \alpha)]$

$ \approx \alpha \log \exp(\mathbb{E}_{x_0 \sim p^{pre}(x_0 | x_t)}[R(x_0)] / \alpha)$

$ = \mathbb{E}_{x_0 \sim p^{pre}(x_0 | x_t)}[R(x_0)]$

The second step takes the $\exp$ function outside of the expectation and as such requires an application of Jensen's inequality, implying that $v_t(x_t) \geq \mathbb{E}_{x_0 \sim p^{pre}(x_0 | x_t)}[R(x_0)]$.  This means that the Monte Carlo regression used for SVDD-MC is in fact biased (although consistent), a fact which is not mentioned in the paper.

The situation is more complicated for SVDD-PM which first applies Jensen's and then another approximation as 

$v_t(x_t) \geq \mathbb{E}_{x_0 \sim p^{pre}(x_0 | x_t)}[R(x_0)]$

$ \approx R(\mathbb{E}_{x_0 \sim p^{pre}(x_0 | x_t)}[x_0])$

It is unclear to me whether the error of the posterior mean estimate can be shown to be bounded as the reward function is potentially non-convex, but would be happy if the authors had some insight into this.

Given that SVDD requires accurate estimates of the soft-value functions to sample from the target distribution $p^*(x_0)$ I would be more convinced of SVDD's abilities were there a more detailed (potentially including an empirical results) analysis of the bias of the Monte Carlo regression and posterior mean estimates.



### Issues with inconsistent setting of $\alpha$ for baselines

The stated goal of SVDD is to sample from the target distribution $p^*(x_0;\alpha) \propto p^{pre}(x_0)\exp(R(x_0) / \alpha)$, where the temperature parameter $\alpha$ controls how peaky $p^*(x_0;\alpha)$ becomes.  As discussed above, as $\alpha \rightarrow 0$ the target distribution becomes focused on the maximizer of the reward which is in the support of the pretrained model such that 

$\mathbb{E}_{x \sim p^* (x;0^+)}[R(x)] = \underset{x_0 \in Support(p^{pre}(x_0))}{\arg\max}R(x_0)$.  

In general, as the value of $\alpha$ is decreased the expected reward under the target distribution should increase.  As such, comparing the distribution of rewards of generated samples for methods using different values of $\alpha$ does not paint an accurate picture of each method's performance as one method having a higher quantile reward may simply be a consequence of the setting of $\alpha$. 

Unfortunately, the manuscript's experiments use significantly different values of $\alpha$ for its method and baselines while using the reward at different quantiles as the main performance metric.  This is more problematic as the value of $\alpha$ for their method is set to $0$ (where the true expected reward is the maximum reward value) and a larger value of $\alpha$ for baselines.  Because the value of $\alpha$ is not set to be equal for SVDD and all baselines I do not believe that the experimental results in Table 2 paint a fair picture of SVDD's performance.



### Overall comments

I generally have concerns with the settings of either the number of particles $M$ being too small or the bias of the soft-value function estimates being too large.  As far as I understand (and perhaps I am missing something!) by setting $\alpha=0$ for SVDD in the experiment section the method _should_ be suffering from mode collapse and generating very high reward samples as the target distribution $p^*(x_0)$ is a Dirac centered at $x_0^* = \underset{x \in Support(p_0^{pre}(x))}{\arg\max}R(x)$.  However, samples from SVDD do not exhibit this expected mode collapse, which seems to indicate that either many more particles $M$ need to be used or the bias from the value function estimation is preventing the algorithm from properly sampling from the target distribution.

I note that the main reason for my score mostly due to the issue with inconsistent setting of $\alpha$ for SVDD and baselines in the experiments section as well as the missing discussion.  A missing discussion/analysis of the bias of the value function estimates and their impact on SVDD's ability to sample from the target distribution also contributes significantly to my score.

### Questions
1. I did not see it mentioned in the manuscript -- how many seeds were used for experiments?
2. Could the authors provide a discussion of the relation between the consistency of nested SMC and the consequence of using more or less particles in their method?
3. How expensive is training the soft-value function estimate in SVDD-MC?  If it is reasonably long would it be worth adding a fine-tuning based method (e.g., relative trajectory balance https://arxiv.org/abs/2405.20971).  On the other hand, if training the soft-value estimate is especially cheap it would be worthwhile to emphasize this more in the manuscript as a benefit of this method compared to direct fine-tuning methods.
4. Since the goal of SVDD is to sample from the product distribution of reward and pretrained model could they add some metrics evaluating the diversity of their samples or their naturalness (e.g., likelihood under the pre-trained model when available)?

### Soundness
1

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
3

### Summary
This work provides a unified framework of guidance in diffusion models, both discrete and continuous, with minimal additional training and applicability in domains where a downstream reward might not even be differentiable. The proposed method SVDD (MC and PM) is applicable in discrete diffusion where a continuous gradient of energy cannot be directly added to the discrete state space, as well as cases where the reward is non differentiable which is the case in a lot of scientific domains. The work tackles an important problem in the scientific domain and leads to controllable generation without having to fine-tune large scaled models. Their results show that generations from SVDD lead to higher downstream rewards than the baselines considered.

### Strengths
- The authors provide a widely applicable method that can be applied both to discrete and continuous diffusion settings.
- The proposed method, unlike previous guidance algorithms, does not rely on an explicitly trained conditional diffusion model (eg. for classifier free guidance), or on differentiable reward terms (eg. classifier based guidance).
- Results on both image and scientific domains highlight the benefits of the approach towards controlled generation of objects with high downstream reward, as intended.
- The work also conducts experiments in a wide variety of domains, ranging from images, molecules and DNA.

### Weaknesses
 - The authors consider setting $\alpha=0$ in their experiments. However, prior work highlights that setting $\alpha=0$ leads to over-optimization and increasingly reduces the diversity and realistic nature of the samples. Could the authors provide clarity on why this is not a problem in their setup?
- The work relies on two major assumptions (one for SVDD-MC and the other for SVDD-PM), which are neither well motivated theoretically nor are there any details provided about it. 
- **Assumption about SVDD-MC**: The authors replace the logarithm of expectation with the expectation of logarithm in their quantity of interest, which in reality is only a bound on the actual quantity. Could the authors consider experimenting on some synthetic domain to describe the bias and variance caused by this approximation? When is this approximation reasonable and when would it be extremely incorrect?
- **Assumption about SVDD-PM**: This algorithm combines the above approximation with pushing the expectation inside the reward function $r(\cdot)$. As with above, could the authors conduct experiments on synthetic domains and highlight when and where such an assumption is reasonable, and when is it violated?
- While the approach leads to generation of samples with high reward, the authors do not provide any kind of metrics that test for diversity of the samples generated.

### Questions
- Is there a typo under the first equation in Section $4.1$, where the expectation is induced by $p_t^{pre}(\cdot | x_{t-1}) -$ note the negative instead of positive sign.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces SVDD which is a new method to fine-tune diffusion models in both continuous and discrete spaces. SVDD-MC learns a soft value function by regression to $x_t$ while SVDD-PM exploits the posterior mean parametrization of masked diffusion models to estimate the soft value function directly. Given a soft value function, SVDD can be applied to a general class of reward functions, including non-differentiable ones, at inference time without further fine-tuning. This can be seen as a variation of the famous Sequential Monte-Carlo algorithm but applied and modified for diffusion models. Experiments are done on images, molecules, and docking and show improvements in fine-tuning performance under a specified reward metric.

### Strengths
The paper tackles a timely problem in considering fine-tuning diffusion models. Moreover, the suggested approach of SVDD-PM enjoys being computationally cheap to use as it does not require any further training while both SVDD-MC and SVDD-PM are applicable in settings where the reward function is non-differentiable. This is impactful because this unlocks a lot of potential application domains that have black-box rewards where learning a surrogate reward model is non-trivial. Finally, the paper considers a diverse set of experimental settings to showcase the universality of the proposed approach.

### Weaknesses
While the paper has some notable strengths there are a few lingering questions that point to potential weaknesses. I will try to list them below.

**Theoretical weaknesses**

Two main questions arise when looking at the setup. The first one is the actual target distribution and whether SVDD hits it. In the continuous setting, I have severe doubts about whether the correct terminal distribution is reached due to the initial value function bias problem as introduced in Adjoint Matching (Domingo-Enrich et. al 2024). Certainly, nothing in the current theory suggests the process during fine-tuning is memoryless. Moreover, it is unclear what ramifications and bias we introduce in the MC setup when the regression is done using $r(x_0) \to x_t$ as opposed to the more numerically unstable soft value function. For example, I believe when you remove the $\exp$ from your regression target, this is a based value function but there is no discussion on this point outside of the fact that it is less numerically stable. As a result, I am dubious about the claims made about hitting the correct target distribution.


Another question is the connection to Sequential Monte Carlo. There is a discussion on this in the paper but I think it's not accurate enough. I disagree with the statement made in the paper. The algorithm you propose is quite literally SMC but adapted to reward maximization, there is even a resampling step which is exactly what is done in SMC. The arguments that SMC is done over a batch are lukewarm. There is nothing wrong with demonstrating that SMC can be effectively applied to sampling from discrete diffusion---like analogously done for an autoregressive model by Zhao et. al 2024---and this is a valuable contribution. I suggest the authors be a bit more forthright with their claims as I would buy it a lot more. In fact, with the right framing, you achieve novelty by showing how SMC applies to a newer more interesting problem domain.

**Additional Technical weaknesses**

One of the main selling points of SVDD is the fact that it is supposed to be a cheap inference time algorithm. This I believe is not quite true because of the need to estimate the soft value function in SVDD-MC. Indeed, one must estimate the soft value function using rollouts which I believe adds a heavy pre-processing step. I also did not see SVDD-MC in the ablation studies about computational cost---likely because it's significantly more expensive than SVDD-PM. Thus, I believe the main claim for SVDD-MC being a lightweight method is a bit misleading. Of course, if you had the perfect estimated value function then inference scales as indicated in the plot for 3c,d but this is not the full picture.

**Experimental weaknesses**

A glaring missing baseline is Relative Trajectory Balance (Venkataraman et. al 2024) which does fine-tuning exactly like this paper considers for both discrete and continuous diffusion models. I kindly request the authors to consider adding this important baseline. Moreover, it is a bit surprising that there is no text experiment given the heavy emphasis on using Masked Diffusion Models which have primarily been introduced for text. I would be encouraged to see a text experiment---perhaps of a similar scale to Zhao et. al 2024---to highlight that SVDD can be applied in the text setting.

The current experimental findings in Table 2 are not complete as they do not show other important aspects of the generated sample. They simply show that reward is maximized but this could also happen through gamification of the reward function. For instance, I would appreciate the authors providing sample-based diversity metrics to quantify how bad the drop in diversity is among the baselines. At the very minimum, FID scores for images should be provided and I'll let the authors determine appropriate diversity metrics for the other domains to complement the findings in Table 2.

**Closing remarks**

Having said all of these weaknesses, I will note that I am open to significantly raising my score if **all of my concerns** are adequately addressed to my level of satisfaction. I will also state that I did not read the appendix so if I have missed something I would appreciate a pointer to the result there.

I encourage the authors in their rebuttal endeavors and I hope they can strengthen the paper which I would like to eventually recommend for acceptance but not in its current state.

### Questions
I would appreciate it if the authors could address my theoretical concerns regarding 1.) what is the optimal distribution hit by SVDD 2.) what is the bias introduced in the MC estimate and 3.) the actual computational cost of SVDD-MC.

In addition, I would appreciate it if the authors could carry out the additional experiments I have suggested with added diversity quantification.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new method called Soft Value-based Decoding in Diffusion models (SVDD) for optimizing diffusion models to generate samples with desired properties while maintaining naturalness. The contributions include:
- SVDD is an inference-time technique that doesn't require fine-tuning the original diffusion model
- Can work with non-differentiable reward functions, unlike previous methods that required differentiable proxy models
- Applicable to both continuous and discrete diffusion models in a unified way

The algorithm works in the following way:
1. Uses "soft value functions" that predict future rewards from intermediate noisy states
2. At each denoising step:
   - Generates multiple samples using the pre-trained model
   - Selects samples based on their predicted value
There are two variants:
   - SVDD-MC: Uses Monte Carlo regression to learn value functions
   - SVDD-PM: Directly uses reward feedback without additional training

Experimental Results span across multiple domains: image generation, molecule generation, DNA/RNA sequence generation. The proposed method consistently outperformed baseline methods while maintaining sample validity. 
The paper demonstrates that SVDD provides an effective way to guide diffusion models toward desired properties while preserving the natural characteristics learned during pre-training.

### Strengths
There are several advantages of SVDD over previous methods:
1. No need for differentiable proxy models
2. No fine-tuning required
3. Works with both continuous and discrete spaces
5. Maintains better sample diversity compared to other approaches

The writing of this paper is clear.

### Weaknesses
The main weakness is about novelty. To be more specific, I can not see significant difference with twisted SMC methods (e.g., the papers mentioned in Sec 6 and App B). In the writing I see two differences claimed by the authors:
1. In previous works such as Wu et al., the reward is a classifier; while here it is "reward maximization" setting. 

First, I think the setting in this work should not be called "reward maximization" but be called "alignment" or "reward sampling" or similar names, due to the reasons in Sec 3.2 "HIGH REWARDS WHILE PRESERVING NATURALNESS". Second, whether the reward function is a classifier is not critical, as even for an usual reward r(x), we can understand it as an unnormalized probability prob(optimality | x).

2. "SMC methods involve resampling across the “entire” batch, which complicates parallelization. Additionally, when batch sizes are small, as is often the case with recent large diffusion model"

I do not quite understand this part. I may miss the difference between SVDD and twisted SMC methods. Does the batch size mean the number of particles in SMC? It will be good if there could be a clarification.

### Questions
I do not have further questions.

### Soundness
3

### Presentation
2

### Contribution
2
