# Discrete Copula Diffusion

- Decision: Accept
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Discrete diffusion models have recently shown significant progress in modeling complex data, such as natural languages and DNA sequences. However, unlike diffusion models for continuous data, which can generate high-quality samples in just a few denoising steps, modern discrete diffusion models still require hundreds or even thousands of denoising steps to perform well. In this paper, we identify a fundamental limitation that prevents discrete diffusion models from achieving strong performance with fewer steps -- they fail to capture dependencies between output variables at each denoising step. To address this issue, we provide a formal explanation and introduce a general approach to supplement the missing dependency information by incorporating another deep generative model, termed the \emph{copula} model. Our method does not require fine-tuning either the diffusion model or the copula model, yet it enables high-quality sample generation with significantly fewer denoising steps. When we apply this approach to autoregressive copula models, the combined model outperforms both models individually in unconditional and conditional text generation. Specifically, the hybrid model achieves better (un)conditional text generation using 8 to 32 times fewer denoising steps than the diffusion model alone. In addition to presenting an effective discrete diffusion generation algorithm, this paper emphasizes the importance of modeling inter-variable dependencies in discrete diffusion.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the dependency issue of multivariables in each step of discrete diffusion model.  The paper claims that discrete diffusion model requires many steps because that each step of the diffusion model cannot fully capture the required inter-variable dependency. To model the dependency among these variables, the author proposes an interesting setting, that given both accurate estimation of marginal distribution and approximated estimation of full distribution, how to obtain a much accurate estimation of the full distribution. An optimization algorithm,  I-projection, is proposed to solve the problem. 
To inject inter-variable dependency for each diffusion step, the author proposes to estimate the full distribution with an fixed-ordering autoregressive model, and then approximate each step's target distribution of certain marginalization of the autoregressive model. Many approximations are proposed to achieve the final "correction" step.

### Strengths
1. The proposed issue of inter-variable dependency of generated elements within diffusion model is an interesting observation and a valid issue. 

2. The proposed mathematical problem that finding a better estimation of full distribution given both marginal distributions and inaccurately estimated full distribution is a very interesting problem that can combines two type of methods together. The author shows that diffusion model and autoregressive model can be combined under the proposed setting. 

3. The author proposed a good realization of the proposed combination: how to estimate an approximated target distribution with inter-variable dependency using autoregressive model, and how to find the I-project's solution to derive the much accurate estimation of the target distribution. (Under absorbing 

4. In experiment, the author shows that the method can achieve better performance than all baselines even given a few diffusion steps.

### Weaknesses
1. Lack an detailed explanation of why the inter-dependency issue is only for discrete diffusion model but not for continuous diffusion model, which can affect the soundness. Specifically, the paper does not adequately explain why the independent sampling of variables in discrete diffusion models leads to a more severe inter-dependency problem compared to the infinitesimal changes in continuous diffusion models. The argument that discrete models change a few variables 'by a lot' while continuous models change all variables 'by a little' is not sufficiently rigorous and lacks a formal connection to the underlying mathematical formulations of each model type. A more detailed analysis of how the loss functions and sampling procedures differ in their treatment of inter-variable dependencies is needed.
2. Section 2 line 121 mentioned that continuous-time case the objective is optimizing likelihood ratio. This is not fully correct, given [1] shows that the SEDD's objective can be exactly derived from ELBO setting. The author also lacks reference for its continuous extension. The statement about likelihood ratio optimization is misleading, as the ELBO derivation is more fundamental and widely applicable. The lack of a reference for the continuous extension further weakens the theoretical grounding of the paper.
3. Lack a clear definition of "copula", while it appears many times in many different ways. The term "copula" is used without a precise definition, leading to ambiguity in its interpretation. The paper should clearly define what type of copula is being used, how it is parameterized, and how it relates to the odds ratios mentioned later. The connection between the copula and the autoregressive model is not clearly established, making it difficult to understand how the copula is being modeled.
4. Section 5.1 needs a major revision: it is hard to read while the described equations are not that hard. Some suggestions: define the each variable's meaning before putting them into equations. like X-tilde, which I don't understand before read equation (5) in detail. Also, give an illustration figure to describe the setting of each variable shown in equation (5) under absorbing state case. Most importantly, describing your easy-to-understand intuition and main thought before throwing all equations that hide your thoughts deeply. The presentation of Section 5.1 is confusing and difficult to follow. The variables are not clearly defined before being used in equations, and the lack of a visual illustration makes it hard to grasp the setting. The intuition behind the equations is not explained, making it difficult to understand the motivation and derivation of the proposed approach. The introduction of X-tilde is particularly unclear.
5. Need certain consistency, for example, equation (5) and (6) 's last part: one use element case while the other use combined case. Notation/equation should be consistent. I also don't like the notation of I and J which does not have the t+1 subscript but only represent the case for t+1 time. These notation/equation issues make the paper hard to follow. The inconsistency in notation between equations (5) and (6), specifically the use of element-wise vs. combined notation, is confusing. The lack of a t+1 subscript for I and J, despite them representing the t+1 time step, further adds to the notational inconsistencies and makes the paper harder to read and understand.
6. The proposed analysis has many approximations that can introduce huge approximation error, in both copula distribution of I-projection. I personally think the error within the copula distribution can be huge, given that the autoregressive method is based on the inherent ordering of the sequence (like text), while the conditioned part of equation (6) clearly needs more unmasked tokens. Ideally, one would like to train an "autoregressive diffusion" model proposed by Emiel Hoogeboom [2], which can make the ordering issue less problematic. The ideal copula model should work for any combination of J and I ordering for any time step t, which is a huge requirement. I suggest the author think about how to quantify the influence of these approximations in copula model and the I-projection stage. The reliance on approximations, particularly in the copula distribution and I-projection, introduces potential for significant error. The use of an autoregressive model, which is inherently order-dependent, may not be suitable for capturing the complex inter-dependencies between variables, especially when the conditioning in equation (6) does not consider all unmasked tokens. The paper should address how these approximations are quantified and their impact on the final results, and consider alternative copula models that are less sensitive to ordering.
7. Another limitation is that the current copula model only works for absorbing state diffusion model. Which is not ideal and not widely used for many other domains such as graphs given it does not address many symmetry problems.

### Questions
Except these weaknesses, I have the following question to inference and experiment. 

1. While the proposed method requires few diffusion steps, it does contain many additional steps (line 5 6 7) shown in Algorithm 1. Can the author give a fair comparison of inference time instead of diffusion steps, given that each diffusion step has different cost?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes the Discrete Copula Diffusion (DCD) method. It addresses the inability of discrete diffusion models to capture inter-variable dependencies during denoising, which hampers their few-step generation performance. DCD combines a discrete diffusion model with an autoregressive copula model at inference. By integrating the univariate marginals from the diffusion model and the dependencies captured by the copula model, it approximates the true denoising distribution. Experiments in unconditional and conditional text generation and antibody sequence infilling demonstrate that DCD outperforms individual models, achieving better results with significantly fewer denoising steps, thus emphasizing the importance of modeling inter-variable dependencies in discrete diffusion.

### Strengths
1. Originality: the paper proposes an interesting approach of combining a discrete diffusion model with a copula model to address the issue of capturing inter-variable dependencies in discrete diffusion, which is a relatively new direction.

2. Quality: the paper provides a formal analysis of the problem in discrete diffusion models, showing the limitations of the independent denoising assumption and how to improve it with the copula model.

3. Clarity: The paper is well-structured, and explanations of concepts like copula models, I-projection, and the noising process in discrete diffusion are detailed and understandable, making it easy to follow the flow of ideas.

### Weaknesses
My main concerns are about the experiment setup and results.

1. Reasonability of assumption: from Sec 4, the motivation is that the diffusion model learns better the marginal distributions, while copula (which is AR model) captures correlation but may be more biased in marginals. I think it's better to show empirical evidence for this assumption. Specifically, the paper should include an ablation study that isolates the performance of the marginal distributions learned by the diffusion model and the copula model separately, perhaps by comparing the quality of samples generated using only the diffusion model's marginals and only the copula model's marginals. This would provide direct evidence for the claim that the diffusion model is superior in learning marginals.

2. Computational cost: this is my main concern. Could the author provide a simple complexity analysis for sampling time? According to Alg 1, I think line 5 requires twice forward computation with bidirectional and causal attention, and line 7 (eq 6) even needs another computation. As shown in Fig, this process is extremely slow. The paper should provide a more detailed breakdown of the computational cost, including the time complexity of each step in Algorithm 1, and also discuss the memory requirements of the method, especially considering the need to store intermediate results from both the diffusion and autoregressive models. The current analysis is insufficient to assess the practical feasibility of the approach.

3. I suggest having another plot like Fig 3 but making the x-axis the wall clock time, so it shows efficiency directly. As indicated by Fig 5, I guess the practical acceleration is limited. The current plots focus on the number of denoising steps, but a more practical comparison would be to plot performance against wall-clock time. This would allow for a direct comparison of the efficiency of DCD against other methods, including baselines, and would be more informative for practical applications.

4. An important baseline is missing. I suggest also comparing DCD against MDLM [1] where the cache sampler can also significantly reduce timestep and accelerate the sampling speed. The paper should include a comparison with MDLM [1] using its cache sampler, as this is a relevant baseline for efficient discrete diffusion models. This comparison should include both generation quality and speed, to show whether DCD offers a significant advantage over this optimized baseline.

5. Evaluation protocols are too synthetic. The paper just studies 128-length text generation and shows the significance, but typical studies are all done on longer sequences such as 1024 length. Besides, it's critical to also report diversity scores for the generations. Generative PPL is known to suffer from mode collapse generation without consideration for diversity. The evaluation should be extended to longer sequences, such as 1024, and should include diversity metrics such as self-BLEU or distinct-n, in addition to perplexity. This would provide a more complete picture of the model's performance and address the potential for mode collapse.

### Questions
1. Is the combined distribution $\hat{p}$ (Eq 3) a normalized distribution? Otherwise, the notation should be proportionate.

2. Could we compute the likelihood (or bound) for DCD model? Is so, it will be good to have a perplexity metric which is also a common benchmark; if not, what's the challenge for it?

### Soundness
3

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
Traditional Discrete Diffusion models suffer from severe degradation in sampling quality when the number of sampling steps is reduced. In contrast, continuous Diffusion Models don't have this issue. This paper first points out that this is because discrete diffusion models cannot capture the dependencies between output variables at each denoising step. To address this problem, the paper proposes incorporating another deep generative model, named the copula model. The copula model can be trained independently and only needs to be incorporated during the sampling process of the Discrete diffusion model. Experiments demonstrate that the proposed method can significantly improve the sampling speed of discrete diffusion models.

### Strengths
1. This paper addresses a very important issue: how to improve the sampling efficiency of diffusion models (reducing sampling steps while maintaining sampling quality) is a crucial topic. While this problem has been well solved in continuous diffusion models, it remains unresolved in discrete diffusion models.

2. This paper is well-written, and I particularly appreciate its insightful illustrations. For example, Figure 1 provides an excellent clarification of the existing problems in traditional Discrete Diffusion models.

3. The paper provides solid theoretical analysis for the proposed method.

4. The proposed method doesn't require modifications to the diffusion model during training, thus offering excellent scalability.

### Weaknesses
1. Since this paper requires training an additional (new) generative model, the training requirements of the proposed method might be higher. Considering that Autoregressive methods are already very well-suited for generative modeling of discrete data, I am uncertain if this paper feels like using a complex model to improve a relatively simple model.

2. Using perplexity metrics alone is not sufficient. For example, we expect the generated text to be sufficiently diverse, but perplexity metrics struggle to reflect the diversity of generated samples. Furthermore, perplexity, while a common metric, primarily measures the model's ability to predict the next token in a sequence, and may not fully capture the quality of the generated text in terms of semantic coherence or long-range dependencies.

3. Most experiments were conducted with a generation length of 128, which does not reflect real-world scenarios, e.g., with a length of 1024. This limited sequence length makes it difficult to assess the method's ability to generate long, coherent text, which is crucial for many practical applications. The performance on longer sequences might reveal limitations not apparent in shorter ones, particularly regarding the maintenance of semantic consistency and overall structure.

### Questions
1. I have questions about the results in Figure 4. The figure gives me the impression that if we further increase the number of denoising steps, SEDD's performance could still improve, while DCD's results can't improve anymore. I would like to know how the performance comparison between the two would look if the number of denoising steps were further increased.

2. Since I'm not very familiar with synthetic text data, I'm unsure whether perplexity is an appropriate metric for measuring the quality of generated data (especially the ability to restore the ground-truth data distribution). Are there any other metrics to measure if the dependencies between different variables are correctly captured? For other types of discrete data, such as tabular data, there are more metrics available to measure the quality of generated data (such as metrics for correlation between different dimensions). I would like to know how the method proposed in this paper performs on these types of data.

3. Can the authors provide a more detailed comparison of the computational costs and training requirements between their proposed method and existing approaches?  As demonstrated in Figure 5, your methods look much slower.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes using copulas to enhance the approximation accuracy of the backward process in masked diffusion models. Specifically, it shows that the true posterior $q(x_t|x_{t+1})$ can be decomposed into a latent auxiliary variable model $q(x_t|x_{t+1}) = \sum_{\tilde{x}_t} q(\tilde{x}_t | x_{t+1}) q(x_t|\tilde{x}_t, x_{t+1})$, in which $q(x_t|\tilde{x}_t, x_{t+1})$ has a closed form and $q(\tilde{x}_t | x_{t+1})$ can be approximated using a pre-trained auto-regressive model. To further enhance modelling capabilities, the paper suggests learning an I-projection of $q(\tilde{x}_t | x_{t+1})$, so that the univariate marginals align with the true data marginals. Experimental results demonstrate that this approach reduces the number of sampling steps.

### Strengths
The paper is well-motivated and  proposes a theorectically sounded framework to improve masked discrete diffusion models. Decomposing the true posterior into a latent auxiliary variable model is a very interesting observation.

### Weaknesses
I have two main concerns:

1. Although the proposed method reduces the number of sampling steps, the number of function evaluations (NFE) appears to be quite large. Unlike discrete diffusion, which requires only one NFE per step, each step in the proposed method involves evaluating the autoregressive model, the diffusion model, and solving a convex optimization problem. This suggests that the computational cost is significantly higher than that of discrete diffusion and autoregressive models.
2.  As shown in Eq.6, the paper uses a pre-trained auto-regressive model to approximate $q(\tilde{x}_t | x_{t+1})$. However this is a biased approximation. This bias can impact the overall fidelity of the backward process, potentially leading to discrepancies in the modeled distribution.

### Questions
- In line with weakness 1, could you add a plot in Figure 3 showing the relationship between running time and perplexity, and include the running time for GPT-2 models as well?
- In addressing weakness 2, could you consider a variant model that solely uses Equation 5 for denoising, without applying the copula? This would provide insight into how well the autoregressive model approximates the conditional distribution of the data.
- Moreover, one interesting idea to address weakness 2, could be to use generative marginal models [1] to learn p(x_0), and the conditional in eq.5 has close form. Specifically,  p(x^I | x^J) could be computed using Bayes’ rule: p(x^I , x^J) / p(x^J). The trade-off here is that while enerative marginal models may not be as expressive as autoregressive models, they provide exact computations, offering a different balance between model power and precision.
- Proposition 1 is confusing. There is no model distribution in Equation 2, so it's not obvious how relaxing the independent denoising assumption would reduce the negative ELBO. Additionally, in line 727 of the appendix, could you explain in more detail how the inequality holds?
- Could you also apply the proposed discrete copula diffusion to MDLM [2,3] and present results for running time versus perplexity? This would help address concerns about the method’s broader applicability across all masked diffusion models. Additionally, it would be valuable to explore whether improvements in the autoregressive model lead to better performance in the proposed method, which raises an interesting question worth investigating.
- Some suggestion in tmers of writing
    - On line 293, instead of stating "it can be decomposed...," it would be clearer to explicitly write out: $q(x_t|x_{t+1}) = \sum_{\tilde{x_t}} q(\tilde{x_t} | x_{t+1})q(x_t|\tilde{x_t}, x_{t+1})$
    - Could you add a paragraph in the main text discussing the limitations of the proposed method and potential directions for future work? Including this would help motivate readers to explore further improvements and applications.

[1] Liu, Sulin, Peter J. Ramadge, and Ryan P. Adams. "Generative Marginalization Models." *arXiv preprint arXiv:2310.12920* (2023).

[2] Shi, Jiaxin, et al. "Simplified and Generalized Masked Diffusion for Discrete Data." *arXiv preprint arXiv:2406.04329* (2024).

[3] Sahoo, Subham Sekhar, et al. "Simple and Effective Masked Diffusion Language Models." *arXiv preprint arXiv:2406.07524* (2024).

### Soundness
3

### Presentation
3

### Contribution
3
