# Stochastic Sampling from Deterministic Flow Models

- Decision: Reject
- Scores: 3, 3, 3, 8

## Abstract
Deterministic flow models, such as rectified flows, offer a general framework for learning a deterministic transport map between two distributions, realized as the vector field for an ordinary differential equation (ODE).
However, they are sensitive to model estimation and discretization errors and do not permit different samples conditioned on an intermediate state, limiting their application.
We present a general method to turn the underlying ODE of such flow models into a family of stochastic differential equations (SDEs) that have the same marginal distributions.
This method permits us to derive families of \emph{stochastic samplers}, for fixed (e.g., previously trained) \emph{deterministic} flow models, that continuously span the spectrum of deterministic and stochastic sampling, given access to the flow field and the score function.
Our method provides additional degrees of freedom that help alleviate the issues with the deterministic samplers and empirically outperforms them.
We empirically demonstrate advantages of our method on a toy Gaussian setup and on the large scale ImageNet generation task.
Further, our family of stochastic samplers provide an additional knob for controlling the diversity of generation, which we qualitatively demonstrate in our experiments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper discusses the case of using linear interpolants for training deterministic flow models. The paper motivates using stochastic sampling instead of deterministic sampling.

### Strengths
Clearly written.

### Weaknesses
Lack of novelty. The conversion between SDEs with different state-independent diffusion coefficients (including zero for ODE) through the Fokker-Planck equation is very well-understood now. While Theorem 1 does cover a general case (state-dependent), this general case is not applied. An example of a paper that discussed stochastic sampling and classifier-free guidance is SiT [1]. The core idea of using stochasticity to improve the training of deterministic flow models, while presented with a different theoretical framing, does not represent a significant conceptual leap beyond existing literature. The paper's focus on linear interpolants, while a common choice, does not justify the limited exploration of more complex interpolations or their potential impact on the derived theoretical results. The theoretical results, while sound, do not offer substantial practical advantages over existing methods, especially given the computational overhead of stochastic sampling. The lack of empirical validation for the general state-dependent case further weakens the practical relevance of the theoretical contribution.

### Questions
Can the stochastic sampling be generalized to 2-Rectified Flows (i.e. after rectification / training with a non-independent coupling)?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper describes how deterministic dynamical transport models can be changed into stochastic samplers without retraining when the base distribution is Gaussian. They then provide a series of experiments exploring the benefits and trade-offs of using this velocity model under different settings of the SDE: extent of diffusivity and time-dependent schedule of its magnitude.

### Strengths
The paper provides a useful empirical exploration of the trade-offs/biases that emerge depending on how the sampling SDE is discretized and which diffusion coefficient is used, e.g. in Table 2. 

Section 4.2 itemizes useful takeaways for the tradeoffs in SDE-based sampling, and provides nice experiments to demonstrate how diffusivity alleviates e.g. sample degeneracy.

### Weaknesses
First off, thank you for your submission! It would be great if the authors could address the following *primary concern* about the work

Corollary 1 is already well known -- it is one of the main points of the interpolant procedure, and is the essential knob explored in 2303.08797, Corollary 2.18. This was then extensively tested (the variety of potential diffusion coefficients from the same velocity model) in 2401.08740. It's unclear to the reviewer how what this paper is proposing is different from these essential elements. In addition Corollary 1.2 in the given paper is already noticed by Song et al 2011.13456. The authors make remarks about these works in the "related work" section but do not seem to recognize this connection.

Because this is the main point of the paper given in this work, it is unclear to the reviewer what this paper sees as its main contribution to the literature.

### Questions
I think it's important for the author's to clarify what the novel contribution is. Could the authors address that?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a method to enhance deterministic flow models, such as rectified flows, by converting their underlying ordinary differential equations (ODEs) into a family of stochastic differential equations (SDEs) with the same marginal distributions. This approach allows for a continuous transition between deterministic and stochastic sampling, using both the flow field and the score function. The method addresses limitations of deterministic samplers, improving their performance on tasks like Gaussian modeling and large-scale ImageNet generation. Additionally, it offers a mechanism to control the diversity of generated samples, providing more flexibility in the sampling process.

### Strengths
1. This paper is well-written, with thorough ablation studies that carefully compare deterministic and stochastic samplers, which I greatly appreciate.

2. The paper is well-written and easy to follow.

3. The motivation is clear.

### Weaknesses
1.To the best of my knowledge, the paper lacks novelty. The core result of Theorem 1 appears straightforward to derive by combining existing results (Equation 4 and Appendix D in [1], Doob's h-transform, and Equation 37 in [2]).

Let me explain more. The Theorem 1 can be understood as
 
$\bar{f}=f-\frac{1}{2}[\nabla(GG^T-(\gamma_t GG^T+\tilde{G}\tilde{G}^T))]-\frac{1}{2}[GG^T-(\gamma_t GG^T+\tilde{G}\tilde{G}^T)]\nabla \log p$, 

$=f-\frac{1}{2}[\nabla(GG^T-\bar{G}\bar{G}^T)]-\frac{1}{2}[GG^T-\bar{G}\bar{G}^T)]\nabla \log p$, 
and

$\bar{G}=[\gamma_t GG^T+\tilde{G}\tilde{G}^T]^{1/2}$

According to [1], The original SDE eq.4 can be written as,
$dx_t= [f-\frac{1}{2}\nabla[GG^T]-\frac{1}{2}GG^T\nabla\log p]dt$

Ok then, all the tricks happen in the diffusion term of FPK. You can easily extend eq.28 in [1] with $x_t$ dependent $G(x,t)$ (it may give even more flexibility?), and absorbing the additional term into the drift term as shown in eq.37 in [2]. 

My understanding is that, once an equivalence is established between flow/bridge models and diffusion models, the remaining work can be readily extended. 

However, I want to acknowledge the authors' efforts; despite the challenges of the problem, the community still benefits from having researchers dedicated to addressing it.

### Questions
I do not have any further questions. And also, feel free to let me know if I misunderstood anything!

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a way to take a trained deterministic flow model and find a family of stochastic flow models that induce the same marginals and which can be simulated using the original learned deterministic flow. This allows one to sample from a much broader range of flow models targeting the same distribution without retraining the network.

The authors claim and then demonstrate that this can be desirable, since stochastic flows have been demonstrated to have better empirical performance in many settings. In particular, the authors show that their stochastic flows have perform better at estimating the variance of the target distribution in a toy setting, and have better FID score when targeting the ImageNet distribution.

### Strengths
- The paper's central observation, given in Theorem 1, that a learned deterministic flow can be converted into a family of stochastic flows targeting the same distribution is a neat theoretical result. It also has obvious practical relevance since, as the authors claim, stochastic sampling methods tend to perform better in practice.
- The presentation of the paper is extremely clear throughout, and I had no trouble understanding the authors arguments and contributions. Thank you for making it easy to engage with your work!
- The authors provide a compelling empirical demonstration of the practical success of their method, on both toy and real-world data distributions.

Overall, I believe this to be a very technically solid paper worthy of acceptance to ICLR. While the core idea of the contribution is not totally novel - the idea that one can convert between SDE and ODE sampling methods via rearranging the Fokker-Plank PDEs governing the marginals is implicit in previous work - this is the first work I'm aware of that demonstrates this practically in the ODE to SDE direction. This is a useful idea and I find the authors' empirical demonstrations of its relevance compelling.

### Weaknesses
There are no significant weaknesses with this paper that I would want to raise. I have just a couple of minor editorial points:
- $\bar G$ and $\tilde G$ are very hard to distinguish in print, and you might want to consider alterantive notation here.
- It took me a while to understand the plots in Figures 1, 2 and 3; for example what exactly was meant by "error in mean" and "error in variance", and which distributions you were measuring the KL between. If there's an easy way to clarify this, that might be worth adding.

### Questions
None in addition to the points raise above.

### Soundness
4

### Presentation
4

### Contribution
3
