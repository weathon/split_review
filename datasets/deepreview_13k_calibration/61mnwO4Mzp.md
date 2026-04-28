# Denoising Diffusion Variational Inference

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
Latent variable methods are a powerful tool for representation learning that greatly benefit from expressive variational posteriors, including generative models based on normalizing flows or adversarial networks.
In this work, we propose denoising diffusion variational inference, which relies on diffusion models---recent generative algorithms with state-of-the-art sample quality---to fit a complex posterior by performing diffusion in latent space. Our method augments a variational posterior with auxiliary latent variables via a user-specified noising process that transforms a complex latent into a simple auxiliary latent. The approximate posterior then reverses this noising process by optimizing a lower bound on the marginal likelihood inspired by the wake-sleep algorithm. Our method can be used to fit deep latent variable models, which yields the DiffVAE algorithm. This algorithm is especially effective at dimensionality reduction and representation learning, where it outperforms methods based on adversarial training or invertible flow-based posteriors. We use this algorithm on a motivating task in biology---inferring latent ancestry from human genomes---and show that it outperforms strong baselines on the 1000 Genomes dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel latent variable inference method, DiffVAE that combines the variational autoencoder and diffusion models. More specifically, DiffVAE enhances the expressive power of the variational posterior by designing a denoising process on augmented latent variables which transforms a complex latent variable into a simple augmented latent variables. Alternative perspective from auxiliary variable models and regularization, and extensions to semi-supervised learning and the clustering are also provided. In experiments, the authors demonstrate the effectiveness of their method on both unsupervised learning, semi-supervised learning genotype clustering tasks. The results indicate that DiffVAE performs better in terms of NLL metric and clustering quality in the latent space.

### Strengths
- The paper proposes a novel method to enhance the expressive power of the variational posterior in VAE by diffusion model.
- The adaption of wake-sleep algorithm for a more informative training of the encoder is interesting.
- The paper is written clearly, especially on related background and alternative perspectives.

### Weaknesses
The DiffVAE method is natural and interesting. However, the method is closely related to auxiliary variable models/hierarchical variational models (HVM) [1] (albeit some small modifications such as additional regularizations). Also, the design of the training objective needs better justification.

1. The authors propose $\hat{\mathcal{L}}$ in equation (7) to replace the original lower bound $\mathcal{L}$ in order to address the requirement of sampling $x$ from $p_\theta$. They consider $L_{\mathrm{sleep}}(x,\phi)$ as a regularization of the original ELBO. I'm concerned that this part of the process may lack sufficient justification since the gradient of $q_\phi(z|x)$ is biased for the original ELBO. The introduction of the sleep loss, while presented as a regularization, appears to fundamentally alter the optimization landscape, moving away from the standard ELBO maximization. The justification for this shift, particularly in how it affects the learned posterior, is not sufficiently clear. Specifically, the impact of optimizing the encoder with a loss function that does not directly correspond to the ELBO needs more rigorous analysis.
2. There aren't much detail about the updating scheme of parameters $\phi$ and $\theta$ in the experiments.

### Questions
- In section 3.1.1., "learning signal from this procedure to be too weak to learn a good $q_\phi(z|y)$" is not clear enough, can you clarify this point more clearly? This is a crucial point that motivates your approach (otherwise, HVM would be enough)
- How are the parameters $\theta$ and $\phi$ updated? Is $\theta$ only updated from the reconstruction loss and $\phi$ only updated from the sleep loss?
- It seems that the $\mathcal{L}_{\mathrm{sleep}}$ term does nothing but pushing the encoder towards the prior. It is, therefore, no wonder that DiffVAE performs better in term of recovering the true prior. It would be better to compare the NLL (instead of latent NLL) for the learned generative model as well.
- The paper would be strengthened by including HVM with a fixed reversed model as a baseline model (which is equivalent to DiffVAE without $\mathcal{L}_{\mathrm{sleep}}$) in the experiments.
- As a method mentioned in the related work, [1] proposed LSGM, which can also be seen as a VAE with a reversed diffusion prior. Could you please provide a more detailed comparison between this method and DiffVAE, and clarify whether it can also be used for semi-supervised learning?

Typos

- In the third paragraph of the background section, the term $ D_{\mathrm{KL}}(p_\theta(z|x)||q_\phi(z|x)$ should be $ D_{\mathrm{KL}}(p_\theta(z|x)||q_\phi(z|x))$.
- Omissions that may lead to misunderstandings. For example, the expectation in equation (4) should be $p_\theta(x,z)$ rather than $p(x,z)$; $D_{KL}(p_\theta\|q(z|x))$ should be $D_{KL}(p_\theta\|q_\phi(z|x))$.
- The second row corresponding to the prior appears to be square rather than Swissroll in figure 2.

[1] Vahdat, Arash, Karsten Kreis, and Jan Kautz. "Score-based generative modeling in latent space." NIPS 2021.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies Denoising Diffusion Variational Inference - using diffusion models, a class of generative models known for high-quality sample generation, to fit a complex posterior through a diffusion process in the latent space. The approach involves augmenting a variational posterior with auxiliary latent variables introduced through a noising process $r$, which transforms a complex latent $z$ to a simple auxiliary latent $y$. The noising process r diffuses z into y through multiple steps, as in a denoising diffusion model. r is set to be a Gaussian diffusion but can be set to another stochastic process. To perform inference in the augmented latent variable model, an approximate posterior $q(y|z)$ is fit along with the forward (denoising) process $q(z|x,y)$. The learning objective is based on the wake-sleep algorithm, and it essentially the ELBO with an additional term which acts as regularization. The authors consider an instantiation of this framework in the context of VAEs, termed DiffVAE, leveraging this flexible encoder $q$. The approach is evaluated empirically in dimensionality reduction and representation learning tasks, outperforming methods based on adversarial training or invertible flow-based posteriors. Specifically. the authors consider a biology task—inferring latent ancestry from human genomes—and demonstrate that DiffVAE outperforms strong baselines on the 1000 Genomes dataset.

### Strengths
* Using a denoising diffusion model as an encoder enables modelling of complex posteriors leveraging the expressive power of diffusion models. This can be useful for representation learning tasks where we want latent space to match semantic structure which can require the encoder to express highly structured distributions. 

* By relying on a wake-sleep style approach, the method avoids adversarial training and requirements of constrained architectures like flows to enabling flexible modeling. 

* The noising process is a key component of the approach. While in the paper a Gaussian diffusion is used, the noising process can also provide a way to impose some structure based on prior knowledge.

* The method shows good empirical performance in semi-supervised tasks with label-conditional priors and genotype clustering tasks.

### Weaknesses
 * The paper presents the very general framework of using diffusion models to model expressive posteriors for variational inference. However, the specific instantiations studied here - semi-supervised learning and clustering - seem quite a bit limited. My main concern is about the generality of the approach. While in principle the approach is applicable to various LVM problems the experiments only study two specific problems. 
* Moreover, the tasks considered here seem relatively simple, not enough to demonstrate the effect of the increased expressivity. For example, the semi-supervised learning task uses relatively simple datasets like MNIST and CIFAR-10, which may not fully reveal the benefits of a more expressive posterior. Similarly, the clustering task, while on a real-world dataset, does not fully explore the potential of the method in more complex scenarios where the latent space needs to capture intricate relationships.
* The increased expressivity also comes at a computational cost - sampling from the diffusion model can be quite expensive (for example in the experiments the authors use 20 and 100 steps which means 20 forward passes of a neural network. The paper does not provide a detailed analysis of the computational overhead compared to other methods, making it difficult to assess the practical trade-offs. The computational cost is especially relevant given that the method is proposed for representation learning, where efficiency is often a key consideration.
* The method also introduces a critical new hyperparameter - the number of steps for diffusion. The paper does not discuss how this parameter is selected and how sensitive the results are to the choice of this parameter. This lack of discussion makes it difficult to understand the robustness of the method and how to properly tune it for different tasks. The absence of a sensitivity analysis is a significant gap in the evaluation.
* Reproducibility: The authors do not include code to reproduce their results but most details seem to be included in the paper.

### Questions
* What is the effect of the number of steps of the diffusion process on the performance? 
* Where do the authors believe would the increased expressivity would be useful enough to trade-off the computation cost?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a hierarchical variational auto-encoder (VAE) with latents structured in Markov chain that is regularized to follow a diffusion process. To achieve this, authors augment the standard ELBO training objective with a de-noising regularization term, motivated by the "sleep" term of the wake-sleep algorithm. Authors evaluate the method on unsupervised learning, semi-supervised learning, and clustering+visualization, measuring the quality of the learned latent space.

### Strengths
Originality. The additional regularization term in Eq. (3) is novel (to the best of knowledge), and has a sound motivation: it allows us to prescribe a "forward" process for the sequence of latents.

### Weaknesses
Originality. While the regularization term in Eq. (3) is novel, the rest of the paper presents a standard hierarchical VAE. In particular, ladder VAEs by Sønderby et al. (2016) use a similar Markov chain of latents with Gaussian conditional step distributions. Subsequent work, including by Vahdat et al. (2020), further demonstrates the benefits of this approach. While implementation details might differ, the proposed method should be put in the context of this well-established area of research.

Significance. The method is compared to weak baselines, with the newest method (IAF-VAE) having been published in 2016. Stronger baselines should be used, including some of the hierarchical VAEs mentioned above. Unsupervised and semi-supervised experiments feel contrived: why do we care about these particular toy priors? Are there realistic settings in which we can demonstrate the method's benefits? The semi-supervised and clustering+visualization extensions and experiments feel secondary to the main contribution, and add little to the paper. It is not clear what the expected results in Figure 3 should be.

Clarity and Quality. Section 3 is very dense, and could be structured better. The value of Sections 3.2 and 3.3 is limited: their main messages could be summarized in the main text, with details moved to the appendix. The mathematical notation is hard to follow, and at times inconsistent: conditioning variables and parameter subscripts are dropped silently, variable names are mixed up (e.g. $\bar{H}$ in Eq. (6) is referred to as $H$ in the main text). Figure 1 (the main figure summarizing the method) has an error: $q_\phi(y|z,x)$ should be $q_\phi(z|y,x)$. This makes an already dense paper even harder to read.

### Questions
The paper mentions that the standard ELBO in Eq. (2) provides too weak of a learning signal. How does this look in practice? Have authors evaluated this approach on the benchmarks in the paper?

In what sense is the "latent space sleep term" in Eq. (7) an approximation of the sleep term in Eq. (3)? Authors mention that this regularization term has less computational overhead, but is an approximation, and hence the overall training objective is not a tight bound. How does this trade-off look in practice? How much computation are we saving, and how big of a sacrifice in terms of results are we seeing?

How does the computational complexity (or at least wall-clock training/inference time) of the method compare to the baselines?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes denoising variational inference. Specifically, they introduce a  user-specified noising process, which transfers a latent variable $z$ from an intractable posterior to another easy to model variable $y$. Then, the authors propose a lower bound on the marginal likelihood inspired by wake-sleep. The method is then extended to the diffusion-based encoders, which can also be viewed as adding a new form of regularization. The authors also discuss some extension topics including semi-supervised learning and clustering.

### Strengths
This work propose a novel variational lower bound on the marginal likelihood. Besides, the analysis and experiments in dimension reduction are interesting and meaningful.

### Weaknesses
1. I see the point of adding auxiliary variables to the VAE encoder, but I can't find a strong reason to introduce auxiliary variables in diffusion models. 
2. Both Sec. 3.1 and 3.2 are introducing the main method. But it is hard to tell what I should take away for each section.
3. The experiments are comparing with classical VAE-based methods. It would be more convincing if more advanced VAE-based methods are considered.
4. In Fig. 3 of the experiments, using a more complicated prior does not improve the  visual quaility, and even don't see more diversity compared with AAE.

### Questions
1. Can you point out the difference between DiffVAE and Variational diffusionn models? 
2. Some other methods like two stage VAE[1] are also learning a more complicated prior (without knowing the true density), then what is the strength of DiffVAE over these methods?
3. Can you provide rigorous convergence and error analysis for your proposed bound?
3. What is the time consumption for the experiments? Compared with classical models?

[1] Dai B, Wipf D. Diagnosing and enhancing VAE models[J]. arXiv preprint arXiv:1903.05789, 2019.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
