# Revamping Diffusion Guidance for Conditional and Unconditional Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Classifier-free guidance (CFG) has become the standard method for enhancing the quality of conditional diffusion models. However, employing CFG requires either training an unconditional model alongside the main diffusion model or modifying the training procedure by periodically inserting a null condition.  There is also no clear extension of CFG to unconditional models. In this paper, we revisit the core principles of CFG and introduce a new method, independent condition guidance (ICG), which provides the benefits of CFG without the need for any special training procedures. Our approach streamlines the training process of conditional diffusion models and can also be applied during inference on any pre-trained conditional model. Additionally, by leveraging the time-step information encoded in all diffusion networks, we propose an extension of CFG, called time-step guidance (TSG), which can be applied to *any* diffusion model, including unconditional ones. Our guidance techniques are easy to implement and have the same sampling cost as CFG. Through extensive experiments, we demonstrate that ICG matches the performance of standard CFG across various conditional diffusion models. Moreover, we show that TSG improves generation quality in a manner similar to CFG, without relying on any conditional information.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes two methods, independent condition guidance (ICG) and time-step guidance (TSG), for conditional and unconditional sampling from a diffusion model, which are summarized below. 

**ICG**

They propose ICG in place of classifier-free guidance (CFG) such that instead of learning two separate models or having two different tasks, one conditional and one conditional, they learn a single conditional model with only a conditional task without making use of null tokens. They do based on the insight that:

1. A conditional model can be turned into an unconditional model by noting that:
    1. the marginal distribution $p(x_t)$ is equal to the expectation $E_{y \sim p(y)}[p(x|y)]$ which can be estimated using sampling a single independent sample $y \sim p_{data}(y)$, which implies that $s_\theta(x_t) \approx s_\theta(x_t, y)$. 

They propose ICG to “streamline” the training of conditional model and improve efficiency (line 534) and as an alternative to CFG, which requires either separate models or a single model with a null token, representing unconditional generation. With ICG, the authors show that training a conditional model is sufficient and the CFG update can be replaced by:

$D_{ICG} = D(z_t, t, \widehat{y}) + w_{ICG}(D(z_t, t, y) - D(z_t, t, \widehat{y}))$ 

where $\widehat{y}$ is a Gaussian vector or a class sampled independent of $y$ at each time-step $t$.

**TSG**

TSG is based on the insight that score model architectures add the class-conditioning embedding into the time-step embedding. Therefore, similar to ICG, they perturb the time-step $t$ by $\Delta t \sim N(0, \sigma)$ TSG then uses a linear combination of $D_\theta(x_t, t)$ and $D_\theta(x_t, t + \Delta t)$ as the “score” network update. The justification of TSG is based on a connection to Langevin dynamics. 

In practice, they do not perturb the time, but similar to ICG they perturb the time-step embedding vector by $s t^{\alpha} n$, where $s, t, \alpha$ selected to match the mean and scale of the “real” time-step embedding vectors and $n \sim N(0, 1)$, and they propose the following update instead of CFG:

$D_{TSG} = D(z_t, \tilde{t}, y) + w_{TSG}(D(z_t, t, y) - D(z_t, \tilde{t}, y))$ where $\tilde{t}$ is the perturbed embedding.

### Strengths
The paper is well-written and the authors perform extensive experiments and provide algorithmic and experimental details to reproduce their experiments. 

**Experiments**

The experiments show that ICG and CFG perform identically and ICG “simulates the behavior of CFG across several conditional models” (line 249). They also run a number of ablations, for instance, they compare using an independent Gaussian vector versus sampling $y \sim p(y)$ in ICG, providing stronger experimental evidence.

### Weaknesses
The main question left un-answered by this work is whether a marginal model, either trained separately or with a null token, is necessary for a sampling method like CFG:
1. An analysis of the variance of the estimate $s_\theta(x_t \mid y)$ is missing from the paper.
2. An analysis of the impact of the variance on sampling is also missing from the paper
3. Is there a trade-off between the slower convergence of training with a null token with estimation of the marginal model?

See the questions section.

The authors could improve the paper by providing a proof (or an empirical analysis) for the sampling procedure for a toy distribution where the $p_{data} = 0.5 N(-a, 1) + 0.5 N(a, 1)$. For instance, with a mixture of Gaussians as the data distribution, the marginal and conditional score functions are computable in closed form and a toy experiment, where various trade-offs can be examined, could make the paper stronger.

TSG
For connecting TSG to Langevin dynamics, the authors show that eq 9 resembles a Langevin dynamics step. However, by using the perturbed TSG denoising model $\widehat{D}$  to define the score $\nabla_{z_t} \log \widehat{p}(z_t)$, the connection seems circular. Could the authors clarify what the connection to Langevin dynamics is and the relevance of that connection?

In table 2, the report FID score for EDM2-XS is higher than the number reported by the EDM2 paper. Is there any explanation for this?

For the variance analysis, it would be better to do for the GMM example as well as if the authors could provide details regarding what exactly they ran on ImageNet, for instance:
1. how many samples were used
2. how many classes were sampled
3. rather than the sampling step, I was asking about the variance of the independent condition score approximation to the marginal score, that is a comparison between $s_\theta(x_t, t, \hat{y})$ and $s_\theta(x_t, t)$.

While it is true that in expectation the ICG gradient is equal to the marginal, my question was about the impact of such adversarial data distributions on the ICG sampling scheme, where the authors do not use the expected value of the independent condition score $s_\theta(x_t, t, \hat{y})$.

For the support, it is true that towards the end of sampling the inference process the supports of p(x_t|y=1) and p(x_t | y=0) match since the process mixes, while generating samples the supports will get disjoint and sampling the opposing class would in effect amount to a step in the opposing direction. Would it be possible for the authors to add a 2d experiment with 0.1 N(-5, 0.1) + 0.9 N(+5, 0.1) as their data distribution and run an analysis of ICG with various hyper-parameter choices such as the $p_0$ distribution, number of time-steps.

### Questions
The authors present an estimate of the marginal model $p(x_t)$, where instead of marginalizing over all possible $y$ by learning a score model with a null token, they use a Monte Carlo estimate. However, the variance of the estimate of the marginal score and it’s impact on sampling has not been addressed in the paper. 

1. Supports of $p(x_t | y=1)$ and $p(x_t | y=0)$ are different: In case of two classes and when $p(x_t | \widehat{y})$ is low, in such a case the ICG term is the score of $p(x_t | \widehat{y})^{1 - w_{ICG}} p(x_t | y)^{w_{ICG}}$, if $p(x_t | \widehat{y})$ is low then its score’s magnitude is high and would dominate the ICG update, potentially pushing in the direction of $p(x_0 | \widehat{y})$
    1. will more steps be required for ICG sampling compared to CFG? 
    2. What will happen when the support for $x_t$ all $t \in [0, T]$ is disjoint for the two classes, such that $p(x_t | \widehat{y}) = 0$ when $\widehat{y}$ is the wrong class? For instance, if $p_{data} = 0.5  N(-5, 1) + 0.5 N(5, 1)$, and the model prior is a centered Gaussian.
2. If the classes are imbalanced then sampling from the majority class can bias the sampling process when the user wishes to sample from the minority class. For instance, if $p(y = 0 | x_0) = 0.99$ and $p(y = 1 | x_0)= 0.01$,  and ICG samples $\widehat{y}$ with an equal probability. The authors should consider modifying the algorithm to sample from $p(y)$, when available, and not a uniform distribution. 

Some simple theoretical guidance with/or toy examples should suffice for an explanation. Potentially with $p(x_0)$  as a mixture of Gaussians in 2d and the authors could vary the guidance scale while sampling.

1. For text to image sampling with ICG, do the authors recommend sampling random text prompts to estimate the marginal model? 
2. For the text conditional experiments in Table 3, can the authors also include CFG performance as a baseline?
3. For the ControlNet experiment, I believe the authors describe training with an empty string for 50% of their text prompts. See section 3.3 in the ControlNet paper. Do the authors use a random text and/or image prompt for the ControlNet model to define a marginal model? 
4. In line 053, the authors claim that there is no clear extension of CFG to unconditional generation:
    1. However, CFG requires training a marginal model, which can be sampled easily. Moreover, one could randomly sample a label y to do generation as well.  
    2. Can the authors provide details about unconditional sampling with ICG? The update defined in algorithm 1, requires a condition $y$ as input. is it just randomly sampling a label and then running ICG?
    
    $D_{ICG} = D(z_t, t, \widehat{y}) + w_{ICG}(D(z_t, t, y) - D(z_t, t, \widehat{y}))$

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
Classifier-free guidance (CFG) is a common method for improving the quality of samples generated from diffusion models. One limitation of CFG is the added training cost due to the requirement for both a conditional and an unconditional model. The authors propose Independent Condition Guidance (ICG), claiming that it provides the same advantages of CFG on image generation quality without additional training costs. They also propose Time-Step Guidance (TSG), a guidance algorithm based on a mixture of score estimates given both perturbed and unperturbed time-step values, which overcomes CFG’s reliance on the availability of class labels. TSG is based on a mixture of scores pertaining to a perturbed and unperturbed time-step value. The authors empirically validate their methods against CFG and un-guided baselines, demonstrating improvements in image quality over unguided sampling that are comparable in magnitude to CFG, while avoiding its limitations.

### Strengths
1. The paper is generally well written and easy to follow.
2. The introduction and related works sections provided a good justification for the limitations of CFG and the benefits of solutions like ICG and TSG. There is certainly a potential for this paper to provide a meaningful contribution to the field of diffusion-guidance, if my concerns about the theoretical claims and empirical validation are adequately addressed by the authors.
3. The experiments are for the most part appropriate and the ablation study is useful to understand the effect of some of the hyperparameter choices.

### Weaknesses
1. A central claim is that ICG provides the same benefits of CFG without the need for additional training requirements. This hinges on the validity of the theoretical claim in Section 4, which avoids the need for a potentially expensive marginalization over classes. However, the theoretical justification appears insufficient. It seems incorrect to state that sampling a class label $\hat{y}$ independently from $z_t$ at time-step $t$ implies the equivalence $\nabla_{z_t} \log p_t(\hat{y} \mid z_t) = \nabla_{z_t} \log p_t(z_t)$, since conditional independencies are a property of the diffusion model parametrized by $\theta$, irrespective of what distribution $y$ was drawn from to compute the sum in $(6)$. Given the conditional score estimate parametrized by $\theta$, $z_t$ should be dependent on $y$. The authors later allude to a procedure to "bootstrap the score", but this is not reflected in their Algorithm 1. Moreover the authors describe the correct equivalence in Appendix A, which involves marginalizing over $y$, but they don't explain how this relates to the seemingly incorrect equivalence relation (7).
2. Empirical evidence supporting TSG is limited. There are no baseline comparisons other than an unguided model. The baseline comparisons for ICG are also limited given that other methods have been published with similar motivations as ICG.
3. The choice of distribution from which $\hat{y}$ is sampled seems non-trivial, and although the authors attempted to shed some light on this in their ablation study, it is unclear how such a distribution should be chosen in general, and how sensitive are their results to the choice of distribution.
4. Several hyperparameters are introduced in the paper, but the description of the hyperparameter tuning procedure seems incomplete. Importantly, on which dataset were hyperparemeters tuned, and using what evaluation criterion?
5. Code is not made publicly available, which diminishes the paper's impact and impairs reproducibility. The provided pseudocode does not seem to entirely capture the design choices that the authors made as part of their experiments.

### Questions
1. Please correct or clarify the theoretical justification behind ICG.
2. Are there not other perturbation-based guidance methods, such as the ones discussed in the Related Works section (in the same spirit as SAG), that TSG could be compared to?
3. Why not include a comparison between ICG and CADS alone (Appendix B only includes ICG+CADS)? It seems like it shares many similarities with ICG. If this is the case, why is this comparison not included in the main paper?
4. The connection between TSG and Langevin dynamics is interesting, but it is not clear how the hypothesized benefits of TSG relate to, or differ from, the theoretical benefits underlying the Langevin diffusion SDE that is implicit in the SDE corresponding to the forward diffusion process.
5. Can the authors better justify the need for two hyperparameters $s$ and $\alpha$ in TSG, and how they tuned these hyperparameters (and on which dataset)?
6. The conditional and unconditional samples from the ICG method seem to have slightly more contrast and are more saturated than the CFG baseline. If the authors agree with my impression, can they hypothesize as to why this should the case?
7. While the authors may be able to justify why ICG could theoretically perform as well as CFG, I don't understand why ICG would be expected to perform better than CFG, as concluded from the plots in Figure 3. Even if the authors can justify this, it would be helpful to understand how sensitive is this result is senstive to hyperparameter choices and random seeds.
8. Figure 5: I did not understand the rationale for testing ICG against the unguided baseline as opposed to ICG against CFG on the text condition. Can the authors clarify?

Minor:
9. Can the authors revisit Section 3,4, and 5, and ensure all variables and functions are properly defined? E.g. $\epsilon$ is undefined. This would help improve the readability.
10. It seems misleading to say that Equation (1) is "equivalent to" Equation (2), and that the denoiser $D_\theta$ "approximates" the score function.
11. It would be helpful to refer to the appendix sections in relevant sections of the main text.


---Post-rebuttal: The authors have addressed the majority of my questions and concerns in their responses to my review and in their global comment. I have therefore increased my rating.

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
4

### Summary
Reviewing the classifier-free guidance (CFG), this paper found that the unconditional score in CFG can be derived by a random label vector y_hat (termed ICG) without training the unconditional model by setting the y_null label. Furthermore, the authors stimulate the guidance by introducing a perturbated time-step embedding based on the original t embedding (termed TSG). Experiments show that ICG achieves similar results to CFG, and TSG improves the FID for conditional and unconditional tasks.

### Strengths
1. The idea of ICG is novel and theoretically simple to implement. ICG provides a new perspective on CFG.

2. The presentation is good and the paper is easy to follow.

3. Extensive experiments show consistent effectiveness of the proposed two methods

### Weaknesses
1. My major concern lies in the proposed TSG:
- the authors explain TSG from its connection to Langevin dynamics, but the connection is built up on Taylor approximation where $\tilde{t} = t + \Delta{t}$, and $\Delta{t}$ should be sufficiently small. But in practice, the authors use $\Delta{t}=st^\alpha n$ where $n \sim N(0, I), s=2, \alpha=1$ and $t$ is the time-step, therefore I do think $\Delta{T}$ is sufficiently small anymore. Furthermore, the use of a fixed scaling factor 's' and exponent '$\alpha$' across different timesteps seems overly simplistic and might not be optimal for all stages of the diffusion process. A more adaptive approach, perhaps based on the local curvature of the diffusion trajectory, could be more appropriate.
- I suspect the effectiveness of TSG comes from the error correction, rather than the guidance perspective, according to the results shown in Table 4. The results in Table 4, particularly the improved FID with TSG even in the absence of a conditional signal, suggest that the perturbation is primarily acting as a form of regularization or noise injection that smooths the sampling trajectory, rather than providing meaningful guidance towards a specific conditional target. This raises questions about the true nature of the improvement and whether it genuinely reflects a better understanding of the conditional distribution.
- Will TSG work in the diffusion models that do not embed class labels into timestep (for example, UViT)? It is unclear how TSG would interact with models where conditioning is achieved through mechanisms other than time-step embedding, such as cross-attention. The proposed method might not be directly applicable or effective in such architectures, limiting its generalizability.

2. please provide the NFE and samplers used to report FID throughout the paper. The lack of details regarding the specific samplers and number of function evaluations (NFE) used to generate the FID scores makes it difficult to reproduce the results and assess the true impact of the proposed methods. Different samplers and NFE can significantly affect the quality of the generated samples and the resulting FID scores, making this information crucial for a fair comparison.

3. some writing issues in section 3:
- According to eq 6 of the CFG paper [1], eq 4 in this paper looks wrong, eq 4 should be $\hat{D} = D_\theta (z_t, t, y) + w(D_\theta(z_t, t, y) - D_\theta(z_t, t, y_null))$. The current formulation of the CFG equation in the paper appears to be inconsistent with the standard formulation, potentially leading to confusion and misinterpretation of the method. This discrepancy needs to be addressed to ensure the accuracy and clarity of the paper.
- undefined notation $\beta_t$ in eq 2

### Questions
The authors mention that there are two methods to decide the random vector $\hat{y}$: draw from Gaussian distribution or a random class label, so that $\nabla_{z_t} log p_t (z_t | \hat{y}) = \nabla_{z_t} log p_t (z_t)$. I wonder how much would the conditional score $\nabla_{z_t} log p_t (z_t | \hat{y})$ change in practice given different samples $\hat{y}_1, \hat{y}_2, \hat{y}_3 ...$ and the same $z_t$

I would increase my rating if some of my doubts and concerns were resolved.

### Soundness
3

### Presentation
3

### Contribution
2
