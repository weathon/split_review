# DO GENERATIVE MODELS LEARN RARE GENERATIVE FACTORS?

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Generative models are becoming a promising tool in AI alongside discriminative learning. Several models have been proposed to learn in an unsupervised fashion the corresponding generative factors, namely the latent variables critical for capturing the full spectrum of data variability. Diffusion Models (DMs), Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs) are of particular interest due to their impressive ability to generate highly realistic data. Through a systematic empirical study, this paper delves into the intricate challenge of how DMs, GANs and VAEs internalize and replicate rare generative factors. Our findings reveal a pronounced tendency towards the memorization of these factors. We study the reasons for this memorization and demonstrate that strategies such as spectral decoupling can mitigate this issue to a certain extent.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a systematic study of generative models (VAEs, GANs, and DMs) and their capability to learn rare generative factors (RGFs). By creating both balanced and skewed datasets, it is investigated, whether these models generalize RGFs or merely memorize them. Authors show that Spectral Decoupling (SD) helps alleviate memorization in GANs.

### Strengths
1.	The study addresses a crucial problem, focusing on how models handle rare but impactful factors in data. Very valuable for applications in medicine and other fields with inherently imbalanced datasets.
2.	The authors develop a decent experimental setup to surface the problem in an approachable manner.

### Weaknesses
Relation to disentanglement and causality literature missing: This is my main criticism of this work. The problem that it tackles is very well-known in deep generative modeling. DGMs are known to take `shortcuts` instead of learning the causal generative mechanism if the problem is not well constrained. A rich body of work on learning disentangled representation in VAEs and GANs tackles practically the same issue. More recently, there are works at the intersection of causality and disentanglement in DGMs, for example [1]. The current work, as presented does not relate back to these works or clarifies if and how its findings are different or complimentary to the domain of disentangled and/or causal DGMs.  

[1] Zhang, J., Greenewald, K., Squires, C., Srivastava, A., Shanmugam, K., & Uhler, C. (2024). Identifiability guarantees for causal disentanglement from soft interventions. Advances in Neural Information Processing Systems, 36.

Experimental Setup and Memorization: I am not sure if memorization is the cause behind the observation. In the current experimental setup, the DGMs seem to learn exactly what the training data distribution implies. Unless there are additional constraints (disentanglement, causal or SD) there is no reason for the DGM to necessarily learn the causal mechanism. This is known as the `shortcut problem` but it is not a form of memorization.

### Questions
See above for the main clarifications I seek, a minor question is:
- Why do you call the evaluation classifier, oracle? As far as I understood, it is a trained classifier on the uniform dataset, while very good, it does not know the ground truth class of any data from the true distribution.

### Soundness
2

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
This paper discusses difficulties of the generative models like VAEs, GANs, and DMs in learning rare generative factors. The paper designs a framework to systematically study the learning of rare generative factors in generative models and concluded that GANs and DMs exhibit a stronger tendency towards memorization of rare generative factors compared to VAEs. It also demonstrates that regularization techniques, such as spectral decoupling, can mitigate this memorization tendency to some extent.

### Strengths
1.	The paper designs a novel framework to systematically study the learning of rare generative factors in generative models.
2.	The paper proposed spectral decoupling to mitigate this memorization tendency of generative models.

### Weaknesses
1.	The motivation is not clear. In the introduction section, it is only mentioned that the purpose of this paper is to examine whether generative models can derive rare generative factors, but a clear motivation is lacking. For example, what is the purpose of deriving rare generative factors? What negative impacts might arise if rare generative factors are not effectively learned?
2.	Generative models typically learn latent representations automatically, however, this paper manually defines Generative Factors, and all experiments are based on these predefined factors. This approach may create a discrepancy with the stated objective in line 92: “Our work provides valuable insights into the limitations of current generative models in learning robust, transferable representations from imbalanced datasets, opening new avenues for improving their generalization capabilities.”
3.	The experiments are not consistent with the examples. In these examples, the rare factor has a strong relationship with the label. However, in the dataset D_u, the numbers of samples with two rare factors are the same. From my point of view, it is more like an imbalanced classification problem, while the authors experiments did not take it into account. 
4.	p>0.05 only means that one cannot reject the null hypothesis, and is not strong evidence that the model has effectively learned the model. 
5.	The paper lacks a detailed explanation of how Spectral Decoupling mitigates this memorization tendency
6.	Some parts of the paper are verbose and convoluted, making it difficult to understand.

### Questions
Please see weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper explores how generative models like VAEs, GANs, and DMs learn rare generative factors. Through an empirical study on skewed datasets, it finds that these models often fail to generalize rare factors and instead memorizing rare generative factors. The paper proposes a mitigation strategy using spectral decoupling for GANs, which partially addresses this issue.

### Strengths
1. This paper explores an interesting problem in the learnability of rare generative factors.
2. It provides concrete examples of the downstream applications of RGFs, such as in medical imaging, literary text generation, and vehicle classification.

### Weaknesses
1. There is no dedicated section for related work, which makes it difficult to understand how the proposed approach builds on or differs from existing work on memorization and generalization in generative models.
2. A single statistical method (z-test) is insufficient to fully evaluate RGF learning.
3. The spectral decoupling technique should be introduced more comprehensively earlier in the methodology section, with a justification for its potential effectiveness across all generative models, not just GANs.
4. Lack of other comparison methods of mitigating RGF memorization.
5. Focusing only on GANs for the memorization analysis weakens the generalizability of the results. A detailed investigation of memorization in VAEs and DMs is needed to support broader conclusions.

### Questions
Please see the weakness above.

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
The paper answers the question of whether generative models learn rare generative factors (RGFs), which are latent variables whose frequency is highly skewed in the real world but play an important role in the generative process. The ability to capture RGFs is crucial for many real world tasks e.g. successfully diagnosing Alzheimer's disease in younger patients.

To test this hypothesis, the authors train and test three different generative models, namely a generative adversarial network (GAN), a variational autoencoder (VAE) and a diffusion model (DM) on two different types of datasets. One dataset has the generative factor uniformly distributed across all training instances, and the second dataset has the RGF concentrated to a singular class to simulate the most extreme case of RGFs. Classifiers are trained to discern the RGFs from samples generated by the learned models, and a statistical test is applied to determine whether the generative models have successfully learned the RGF, or instead memorized it.

The results show that generative models are capable of learning RGFs, but GANs and DMs are particularly biased towards memorization than VAEs, highlighting the nuances in how various generative models approach learning of RGFs. The authors then attempt to understand and potentially mitigate RGF memorization in GANs, noting that GANs have the greatest tendency for memorization possibly due to the adversarial discriminator. The authors suggest that the discriminator learns a spurious correlation between the RGF and the training instance, which the authors note is reminiscent of the "gradient starvation" phenomenon. To that end, the authors train a GAN using spectral decoupling, which prevents gradient starvation, and notice that it mitigates RGF memorization to a certain degree.

### Strengths
The subject is well-defined and presentation of the paper is good. There are numerous examples throughout the paper that describe RGFs and their significance from a real-world perspective. The experiments were well-defined and rigorously designed, making the results empirically sound. Overall, the paper was easy to follow from start to finish and the significance of the subject easy to capture.

### Weaknesses
The paper notably lacks novelty; learning of rare-generative factors is small part of the much larger problem of effectively capturing a data distribution by generative models. More specifically, generative models have difficulty capturing all the modes of the data distribution while also assigning high probability to areas of low probability in the distribution's manifold [1, 2, 3, 4].

Additionally, this topic has been explored in several other papers, with [5] in particular coming to similar conclusions of GANs assigning spurious correlations between generative factors, albeit from a different motivation. In a similar vein, the explanation for why GANs failed in particular were mainly empirical and post-hoc in nature, which I believe makes the results rather weak.

References
[1] Danilo Jimenez Rezende and Shakir Mohamed. Variational inference with normalizing flows, 2016. URL https://arxiv.org/abs/1505.05770.

[2] Bin Dai and David Wipf. Diagnosing and enhancing vae models, 2019. URL https://arxiv.org/abs/1903.05789.

[3] Partha Ghosh, Mehdi S. M. Sajjadi, Antonio Vergari, Michael Black, and Bernhard Scholkopf. From variational to deterministic autoencoders, 2020. URL https://arxiv.org/abs/1903.12436.

[4] Danilo Jimenez Rezende and Fabio Viola. Taming vaes, 2018. URL https://arxiv.org/ abs/1810.00597.

[5] Sergio Garrido, Stanislav S. Borysov, Francisco C. Pereira, & Jeppe Rich. Prediction of rare feature combinations in population synthesis: Application of deep generative modelling. 2020. Transportation Research Part C: Emerging Technologies, 120, 102787.

### Questions
My suggestion to the authors is to discuss the fundamental objectives of the various types of generative models and how they relate to the RGF memorization behaviour on a theoretical basis.

As an example; the KL divergence objective in VAEs is zero-forcing, and therefore will underestimate the support of the true data distribution. In a "dumb" Gaussian latent VAE, the posterior may fail to assign probability to certain low-probability areas in the latent manifold, preventing VAEs from generating rare-but-valid combinations of data. It may also help if the authors could train a VAE with normalizing flows (see [1] in "Weaknesses") to see if the RGF memorization problem is mitigated further, putting theory into practice.

Without needing to go too in depth, a basic explanation of the models' respective objectives and how they relate specifically to learning of RGFs will greatly improve the meaningfulness of the contributions, and by extension the novelty.

### Soundness
3

### Presentation
3

### Contribution
2
