# Diffusion Random Feature Model

- Decision: Reject
- Avg Score: 4.17
- Scores: 5, 3, 6, 3, 3, 5

## Abstract
Diffusion probabilistic models have been successfully used to generate data from noise. However, most diffusion models are computationally expensive and difficult to interpret with a lack of theoretical justification. Random feature models on the other hand have gained popularity due to their interpretability but their application to complex machine learning tasks remains limited.  In this work,  we present a diffusion model-inspired deep random feature model that is interpretable and gives comparable numerical results to a fully connected neural network having the same number of trainable parameters. Specifically, we extend existing results for random features and derive generalization bounds between the distribution of sampled data and the true distribution using properties of score matching. We validate our findings by generating samples on the fashion MNIST dataset and instrumental audio data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new model, called a diffusion random feature model (DRFM), that incorporates the interpretability of random feature models with the data-generating capability of diffusion models. This hybrid model, DRFM, aims to produce results comparable to fully connected neural networks while maintaining interpretability and using a comparable number of trainable parameters. The model's effectiveness is tested through experiments on the fashion MNIST dataset and instrumental audio data. The results demonstrate that DRFM can learn to generate data from a limited number of training samples (as few as one hundred) and within a limited number of timesteps (one hundred).

### Strengths
The paper highlights the interpretability and computation efficiency of the DRFM, noting that it allows for the derivation of theoretical upper bounds on the quality of the samples generated. Numerical experiments show that DRFM outperforms both a traditional fully connected network with all layers trainable and a standard random features model where only the last layer is trainable. The result is clear and opens up a theoretical direction for analyzing random feature models with high-dimensional spaces for diffusion models.

### Weaknesses
1. I did not get the point of focusing on random Fourier-type feature models in Eq. (15). Following, the proof of the paper, it is possible to include more general activation functions. I did not find the motivation why we only consider this specific random feature model defined in Eq. (15) and Eq. (16). The authors may need to provide additional explanation of the choice of the random feature or empirical evidence of the advantage of this specific random feature model.

2. The theory of this paper seems to directly come from Chen et al. (2022) and Ranhimi & Recht (2008b; a). The authors may need to emphasize the difference between the current paper and the references, and the difficulty in the analysis in the current paper. In particular, the authors derived the generalization bounds via the approximation error of the random feature model, which, I think, lacks explanations in the proof in the Appendix.

3. Although there may not be a theory, for completeness, the authors may need to provide additional simulations for deeper neural networks with random features, showing the advantage of this architecture, and comparing it with more commonly used U-Net or other neural network models. The random feature models will reduce the computation complexity but I am not sure the performance is still comparable with conventional diffusion models.

### Questions
1. It is a standard practice to introduce an abbreviation by providing its full form for the first time. For instance, DDPM appears in the paper first time without explaining the full name.

2. Between (5) and (6), there are typos in $q(x_{k-1}|x_k,x_0)=\mathcal{N}(\tilde{\mu}_t,\tilde{\beta}_t)$: you should specify $t$ and insert identity matrix for covariance. And the same issue for (6).

3. Please explain ''U-Nets not only preserve the dimension of input data, they also apply techniques such as downsampling using
convolution which helps to learn the features if the input data.'' on page 4.

4. In Algorithm 1, line 4, did you use uniformly sampling from $K$ time points to update the training parameters? For line 7, how do you minimize the loss $L$? Did you assume it will attain some global minimizer after training? Further explanations may be needed.

5. In Lemma 3.1, please explain the notion $\mathcal{F}_{\omega}$ and $\mathbf{\theta}_j^{(2)}$.

6. In Lemma 3.2, is $\rho(\omega)$ the density function of $\rho$? 

7. In Theorem 3.3, you assume a bounded second moment for $q(x_0)$ but Chen et al. (2022) require $(2+\eta)$-th moment bound for some $\eta>0$. Is there any extra work to relax this assumption in your proof? Right now, there is a lack of explanation of the proof and how you applied Lemmas 3.1, 3.2, and A.2 to conclude the main theorem. Lemma 3.2 shows the approximation error of the random feature model but in the DRFM, how do you use (18) to finish the proof of Theorem 3.3 and ensure $|\theta^{(2)}_{ij}|$ are always uniformly bounded by some constant?

8. Any explanation for why neural networks may fail in denoising images in Figure 3 sometimes but DRFM works better and is stable?

9. There should be more details of how you trained the models in the captions of Figures 2-7, e.g. which optimizers are used.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper applies the idea of random features model to the diffusion-based generative model. Specifically, the paper proposes using a denoiser of the form Eq. (15), where $W, b$ are fixed and $\theta^1, \theta^2$ are trained. Then, the paper presents theoretical results regarding the TV distance between the true distribution and the estimated distribution. Experiments on fashion-MNIST and audio data are provided, and the advantage over other methods is discussed.

### Strengths
- The paper provides a well-written description of diffusion model and related concepts.

- The proposed algorithm is straightforward to understand.

- Combining random features model and diffusion model is a novel approach.

### Weaknesses
 - The random features model was first introduced as an approximation scheme for the kernel method and later used as a toy model for studying neural networks. I personally understand it as a theoretical tool rather than a practical algorithm. Therefore, I think that the idea of using the random features model in generative modeling is not particularly interesting unless it provides a fundamentally new understanding of diffusion-based generative modeling. While the paper provides some theoretical results, they appear to be simple extensions of previously known results. Specifically, the theoretical results seem to be a direct application of existing bounds on the TV distance, with the only modification being the specific form of the denoiser. The paper does not offer any novel insights into the underlying mechanisms of diffusion models or the properties of the data distribution itself.

- To my understanding, the finding of the experiment section can be summarized as "training only $\theta^1, \theta^2$ showed better performance than training all parameters or training only $\theta^2$". Can the authors provide results for different $N$'s? The current experiment is using huge $N$, and it is not surprising that restricting the model class can lead to a better generalization. The paper does not investigate the impact of varying $N$ on the performance of the proposed method. It is crucial to understand how the number of random features affects the trade-off between approximation accuracy and generalization ability. The current choice of a large $N$ might be masking potential issues with the method's performance under different parameter regimes.

### Questions
- Can the authors provide other popular evaluation metrics for generative models such as inception score, Frechet inception distance, etc.?

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to use random features in the training of diffusion models for interpretability and ease of computation. In more details, the authors estimate the score function by a class of functions generated by random features. They demonstrate the method on FASHION-MNIST and Audio data.

### Strengths
The proposed method replaces deep neural nets, which are commonly used when approximating score functions, with random feature functions and shows that experimentally the new method is competitive.

### Weaknesses
1. The theorem 3.1 essentially combines error decomposition results from diffusion models and approximation results from random feature functions. Is it possible to have more fine-grained results for the specific feature map (Eq 17) chosen in the paper? Specifically, while the authors leverage the general approximation properties of random features, the analysis does not delve into how the specific choice of sinusoidal features impacts the approximation error in the context of the diffusion model's score function. A more detailed analysis of the approximation error, considering the frequency spectrum of the score function and the spectral properties of the chosen random features, would be beneficial.

2. How do other choices of random feature maps behave compared to the sin/cos map chosen in the current paper? A sensitivity analysis would improve the validity of the paper. The paper lacks a thorough investigation into the sensitivity of the method to different random feature maps. While the authors mention the use of Fourier-type features, they do not explore other common choices such as Gaussian or polynomial kernels. A comparative analysis, including a discussion of the trade-offs between different feature maps in terms of approximation accuracy, computational cost, and generalization performance, is needed.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors propose a diffusion model-inspired random feature model. This model is interpretable and is able to achieve comparable numerical results to a fully connected neural network (of the same size). The authors then give generalization bounds between the distribution of sampled data and the true distribution for their proposed model.

### Strengths
- The authors propose a diffusion RF model. The model they propose is quite simple and interpretable.
- The model achieves the same performance as a fully connected network on some toy datasets.
- The generalization bound in Theorem 3.3 is novel and interesting.

### Weaknesses
 - Most of the heavy lifting in the proof of Theorem 3.3 is done in Lemma A.2 which is from Chen et al. (2022).

 - The authors only experiment with very simple and small datasets such as fashion MNIST. It is not that clear what happens for more complex datasets. Here, in the diffusion RF model, feature learning is absent because W is fixed at initialization. It is hard to believe that the model can be successful for more complex tasks.

 - The main goal of the paper is not clear to me. Are the authors proposing the RF model as a tool to decrease computational complexity (like Rahimi and Recht) or some theoretical tool to analyze a more sophisticated phenomenon (like Mei and Montanari, 2019)? Do the authors expect such models to achieve similar accuracies to state of the art methods? 

 I agree that there models are analyzable; e.g., Theorem 3.3 is interesting. However, what phenomenon is this model tryin to describe? For example (Mei and Montanari, 2019) and others use RF models to analyze double descent and to show that this phenomenon exists even in very simple models. 

 - What motivates this particular choice of random features? Why did you choose W to be the random weights and train the other parameters?

 - I think in the model that the authors are analyzing, it is more interesting to study the case where the dimension d is proportional to N. Can the authors explain what will happen in that regime to the bound in (19)? In general, I think a more thorough discussion after Theorem 3.3. would benefit the paper a lot. What do we understand from the generalization bound?

### Questions
Please see above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to model the score of image distributions with a one-hidden-layer random features network. The first layer weights are frozen to their initialization, while the second layer weights are learned and depend on the noise level (through a factorization to reduce the number of parameters). The model is compared with a classical one-hidden-layer network where the first layer is learned and a random features model where the dependence on the noise level is not trained.

### Strengths
The paper is clearly written (except for section 2 which redundantly exposes both the discrete and continuous formulations of diffusion models).
The parameterization of the second-layer weights dependence on the noise level is interesting and to the best of my knowledge novel.

### Weaknesses
As noted in the final sentence of the conclusion, there is nothing deep about this random features model (despite the name), leading to a very weak expressivity that is plagued by the curse of dimensionality. The paper thus studies a very restricted, toyish setting. This is not a problem for a theoretical paper, but the theoretical analysis is lacking in rigour and novelty. In particular, Theorem 3.3 is a straightforward combination of classical results (from Rahimi and Recht and Chen et al.) and does not state key assumptions (namely, that the true scores of the image distribution are in some function class for all noise levels). It also only tackles score approximation, not optimization and generalization from a finite training set, but this is not stated in the text. Finally, the bound holds in probability, but is stated as if it were almost sure. On the numerical side, there are no quantitative comparisons between the different approaches, and I'm frankly not convinced that the proposed approach really outperforms the one-hidden-layer neural network.

### Questions
Minor suggestions:
- choose either discrete or continuous framework to present diffusion models
- Typo on page 4: "features [if -> of] the input data"
- page 5: "random and trainable" is confusing phrasing
- notation $p_\theta$ for the network is confusing (usually used for probability density), prefer e.g. $\varepsilon_\theta$
- Put definition of $\mathcal F_\omega$ in the main text if it is used in a lemma
- How can denoising requires 100 steps when it should just be a direct evaluation of the score network? This should be explained in the text.

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents the Diffusion Random Feature Models (DRFMs) as a solution to ongoing challenges in both interpretability and computational complexity of diffusion models. The introduced DRFM yields numerical outcomes comparable to those of a fully connected neural network with an equivalent number of trainable parameters. From a theoretical perspective, the authors expand the random features and establish generalization bounds between the sampled data distribution and the actual distribution, leveraging score-matching properties. The efficacy of the proposed method is validated experimentally using samples from the Fashion MNIST dataset and instrumental audio data.

### Strengths
- The presentation is overall clear and easy to follow. 

- The overall method is clearly stated. The mathematical notations are well-defined, but some are redundant. The theoretical results are sound. The authors have made comprehensive proof and have quantified the error in the estimation, which is good.  

- The authors expand the random features and establish generalization bounds between the sampled data distribution and the actual distribution, leveraging score-matching properties, making contributions in both perspectives.

### Weaknesses
### Novelty

- The proposed framework is inspired by boththe denoising diffusion probabilistic model introduced by Ho et al. (2020), and the semi-random features introduced by Kawaguchi et al. (2018). It seems the proposed Diffusion Random Feature Model (DRFM) is incremental in integrating the above two works. Specifically, in Kawaguchi et al. (2018), a parameterization of one single-hidden layer is defined in a similar form to Eq (15). The authors employ this parameterization for the noise-prediction network in training DDPM. The core novelty of the DRFM, therefore, appears limited, as it primarily combines existing techniques without introducing a fundamentally new approach to the parameterization of the noise prediction network.

- Throughout the paper, it is not straightforward to understand the advantage of the parameterization in Eq (15) in terms of interpretability and computation complexity. Any analysis or experimental results should be provided to address these challenges stated in the introduction. The paper lacks a clear explanation of how the specific parameterization in Eq (15) directly addresses the interpretability and computational complexity issues it claims to solve. The authors should provide a more detailed analysis, potentially including theoretical arguments or empirical evidence, to support these claims.

### Technical quality
- The experiments validate the efficacy of the proposed DRFM. However, when considering the challenges diffusion models face in terms of interpretability and computation, the experiments seem to omit direct comparisons. Additionally, many of the presented results are not quantified using specific metrics, as observed in Fig 2. This makes it challenging to identify the model's superior performance. The experimental section needs to include more quantitative metrics to support the claims of the proposed method. For example, the FID scores should be included for all the experiments, and the computational cost of the proposed method should be compared with the baseline methods.

- The paper currently compares the DRFM solely with a fully-connected layer. Given the prominence of both the Unet and transformer architectures in noise prediction networks, it would be beneficial for the authors to discuss the relationship of DRFM to these models. In particular, considering that transformer layers utilize a combination of the attention mechanism and fully-connected MLPs, they align more closely with the scope of the fully-connected layer baseline. It would be valuable to explore this connection further. The paper should include a comparison with more complex architectures, such as U-Nets and transformers, to demonstrate the practical relevance of the proposed method. The authors should also discuss the potential of using DRFM as a building block for these more complex architectures.

- Since the authors have generalized the random features with the properties of score-matching, it remains unknown whether DRFM can improve the performance in the tasks evaluated in Kawaguchi et al. (2018).

### Presentation quality
- In the abstract, the authors state that diffusion models suffer from a lack of theoretical justification. This assertion is somewhat unclear and could benefit from further specificity. It would be helpful if the authors could elucidate whether this deficiency refers to aspects within statistical, optimization, or other theoretical domains. The authors should clarify the specific theoretical gaps they are addressing, whether they are related to statistical properties, optimization challenges, or other theoretical aspects of diffusion models.

- Mathematical notations are redundant and inconsistent. For example, 
$	ilde \epsilon_i$ does not seem to be used anywhere in section 2.1 the following sections. The notation $\tilde \epsilon_i$ is introduced without a clear explanation of its purpose or how it differs from $\epsilon_i$. The authors should clarify the distinction between these two notations and ensure that all notations are used consistently throughout the paper.

- Since this work is inspired by the DDPM, and the semi-random features. The authors need to introduce the semi-random features liked done in section 2. Without the knowledge of semi-random features, it is hard to understand the importance and contribution of the proposed method. The paper should include a more detailed explanation of the semi-random features and their connection to the proposed DRFM. This will help the reader to understand the motivation and contribution of the proposed method.

### Questions
Please see the point-to-point review in the Weakness section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
