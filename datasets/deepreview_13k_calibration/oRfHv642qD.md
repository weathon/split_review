# A prescriptive theory for brain-like inference

- Decision: Reject
- Avg Score: 4.40
- Scores: 5, 3, 6, 5, 3

## Abstract
The Evidence Lower Bound (ELBO) is a widely used objective for training deep generative models, such as Variational Autoencoders (VAEs). In the neuroscience literature, an identical objective is known as the variational free energy, hinting at a potential unified framework for brain function and machine learning. Despite its utility in interpreting generative models, including diffusion models, ELBO maximization is often seen as too broad to offer prescriptive guidance for specific architectures in neuroscience or machine learning. In this work, we show that maximizing ELBO under Poisson assumptions for general sequence data leads to a spiking neural network that performs Bayesian posterior inference through its membrane potential dynamics. The resulting model, the iterative Poisson VAE (\ipvae), has a closer connection to biological neurons than previous brain-inspired predictive coding models based on Gaussian assumptions. Compared to amortized and iterative VAEs, \ipvae learns sparser representations and exhibits superior generalization to out-of-distribution samples. These findings suggest that optimizing ELBO, combined with Poisson assumptions, provides a solid foundation for developing prescriptive theories in NeuroAI.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Iterative Poisson VAEs (IP-VAEs) for performing approximate Bayesian inference. The work builds on recently proposed P-VAEs, which use Poisson distributions to approximate the posterior and thus employ discrete spike counts for inference. A major limitation of P-VAEs is their large amortization gap, which the authors address here through iterative inference. Unlike the original one-shot P-VAE, iP-VAE refines its representations over multiple iterations. Empirically, the authors demonstrate that this iterative approach enables an explicit trade-off between performance and computation while requiring significantly fewer parameters than competing methods. The model shows strong performance across several benchmark datasets, particularly closing the performance gap with sparse coding that existed in the original P-VAE.

### Strengths
- The paper adds to the literature of biologically-inspired inference. The extension introduced is simple and elegant and allows generalizing P-VAE to dynamically trade-off performance for compute.

- The experiments show that despite IP-VAE being order of magnitude more parameter efficient, they show significant improvement in terms of reconstruction error both for in- and out-of-distribution data.

-The general presentation is good and the paper is easy to follow.

### Weaknesses
 - The biggest limitation is the large number of test-time iterations required to perform inference on relatively simple, downsampled datasets. While the authors mention plans to extend the approach to sequential data in future work, there is almost no discussion of the computational implications of these high iteration counts, which could potentially prohibit real-world applications. Specifically, the paper lacks a detailed analysis of the computational cost per iteration, and how this scales with the size of the latent space and input data. This makes it difficult to assess the practical applicability of the method, especially when compared to standard amortized inference techniques.

- The authors only compare performance against P-VAEs and other variants of iterative VAEs. It would be valuable to include well-tuned baselines with standard VAEs (amortized, Gaussian distributions) to better contextualize the model's performance. The absence of these standard baselines makes it difficult to determine if the performance gains are due to the iterative inference procedure or simply a consequence of the specific model architecture and training procedure. It is crucial to compare against models that are known to perform well on these datasets to properly evaluate the contribution of the proposed approach.

- In the appendix, the authors question the validity of the Poisson assumption, which is a known issue in computational/systems neuroscience. It would be valuable to move part of this discussion to the introduction to better contextualize the model's assumptions and limitations. This is important because the choice of the Poisson distribution as the posterior approximation is a key aspect of the model, and its limitations should be clearly stated upfront to avoid misleading interpretations of the results.

### Questions
- Why does the model require so many iterations (1000) at test time when trained with far fewer iterations? The significant disparity between training and test-time iterations needs theoretical justification.
- How does the performance scale with the dimensionality of the latent space? How would that affect the sparsity performance? It is difficult to assess this point without conducting a sensitivity analysis on the dimension of the latent states.
- In the appendix, the authors question the validity of the Poisson assumption, which is a known issue in computational/systems neuroscience. It would be valuable to move part of this discussion to the introduction to better contextualize the model's assumptions and limitations.
- How prone are the models to posterior collapse? Given that the objective penalizes large rates, how robust is the training of these models? Can the authors comment on the sensitivity of hyperparameters?

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
Variational autoencoders (VAE) are useful types of generative models, but they are not generally brain-like. In particular, they do not typically operate with spikes, and they are not typically 'dynamic' (beyond the single encoding-decoding pass). The authors introduce a novel type of VAE that involves Poisson (and hence spike-like) latent variables and iterative updating. They claim that this VAE, the iP-VAE, exhibits a number of nice properties, including sparse representations and a "compositional code" that supports performant generalization. They also relate various aspects of the iP-VAE to well-known frameworks from neuroscience, including sparse coding, predictive coding, and the Free Energy Principle (FEP), and claim that it may provide a "solid foundation" for further work in neuroAI.

### Strengths
The core idea of the work, which is to modify VAEs to have a latent space that is dynamic and more neurally plausible, is interesting and seems to lead to nontrivial performance gains, at least on the data sets the authors tested. 

The authors do a nice job reviewing relevant literature and relating their proposal to existing frameworks and models from neuroscience.

### Weaknesses
My major concerns are related to (1) experimental support for claims about the iP-VAE, (2) technical details related to the iP-VAE, and (3) the abundance of wildly overstated claims, particularly related to how the authors' contribution is framed. As a minor concern, there are some citation typos (e.g., line 521, no parentheses).

**1. Experimental support.** As far as I can tell, the authors only trained iP-VAEs on MNIST, and checked its out-of-distribution generalization performance on a few other data sets (including extended MNIST and ImageNet-32). Given the grandiosity of some of the claims (see below), it seems reasonable to expect results for more and/or more complex data sets. In order to contextualize the performance of iP-VAEs, the authors only compare it to very similar models, including the recently introduced P-VAE; it would be extremely helpful to also compare its performance to the vanilla VAE and other types of generative models, like diffusion models (which the authors mention). If the iP-VAE does not perform as well, and its benefits are better thought of as related to its brain-like properties, the authors should state this explicitly.

In Sec. 4.4, the authors claim that the iP-VAE learns a "compositional code that generalizes across domains". This is a really strong claim, and is very interesting if true, but only some sample reconstructions and reconstruction loss performance (Fig. 5) are shown to back it up. At least to me, such a claim requires some quantitative analysis of the learned representations. If the authors cannot do such an analysis or consider it out of scope, they should modify the claim to something like "suggests the existence of a compositional code", and note that verifying this would require additional work analyzing representations.

**2. Technical details regarding iP-VAE.** First, there is the high-level concern that the iP-VAE is pretty similar (in terms of details and motivation) to the recently introduced P-VAE, so there is a novelty issue. Second, I am slightly confused by the way certain details of the construction are motivated and presented in Sec. 3.

The authors claim (line 176-177) assuming a Markovian relationship between consecutive data points is a reasonable starting point for modeling the world, but this seems wrong. What people usually do is assume that *latent variables* are Markovian, and that observations are generated from those latent variables. It is obvious that observations should not be treated as Markovian: how the current scene in front of me changes strongly depends on what is happening in the world (most of which I can't see at that moment), and is not usually even approximately Markovian. 

Related to the previous point, I would have expected instead an assumption that the $z_t$ variables are Markovian, and that the $x_t$ variables are viewed as 'noisy' observations of them. In general, I find the structure of the generative model kind of confusing (a schematic figure to illuminate this would help). Also, even though the 'iterative' aspect of the iP-VAE is presented as the main novel contribution (at least to my knowledge), on all inputs the authors consider there is no dynamics; instead, the same input is presented to the model many times.

The authors claim that the iP-VAE performs Bayesian posterior updates using membrane potential dynamics, but this seems like an overstatement. Usually membrane potential dynamics involve some kind of spiking threshold rule (e.g., consider leaky integrate and fire neurons), and there is no such rule here. It is more accurate to say that updates occur in log-rate space, and that this is 'membrane-potential-like' somehow. Even though the authors mention the possibility of including a leak term to make their model more neurally plausible, they do not include one in any experiments.

**3. Grand claims.** Perhaps the biggest issue with this paper, beyond the need for more experimental support, regards the grandiose claims throughout. The title of the paper is "A prescriptive theory for brain-like inference", but the authors' theory is neither prescriptive nor particularly brain-like, or at least it is not especially *more* brain-like than other models that have been proposed. 

The word "prescriptive" suggests that the authors demonstrate how one *ought* to do brain-like inference. But this is not what they showed. They showed that a specific modification of a VAE is slightly brain-like and performs decently well when trained on MNIST. There are many other ways of doing brain-like inference: for example, a NeurIPS paper I am familiar with (Masset and Zavatone-Veth et al. 2022, "Natural gradient enables fast sampling in spiking neural networks") discusses ways based on Langevin and MCMC sampling. Is the proposed approach substantially better (along some axis of 'brain-like-ness') than other approaches? This is not clear from the paper, since existing approaches also involve membrane-potential-like dynamics and sampling from some kind of latent space. Noting difficulties with other approaches, as in done in a comparison to predictive coding on line 63, would be helpful. Incidentally, saying predictive coding doesn't involve spikes is a little unfair, considering forms of it exist (to my knowledge) that address this issue.

The term "brain-like" here may be a bit overstated. What the authors propose is more brain-like in certain ways (e.g., Poisson distributions are used in the latent space, and representations are relatively sparse), but the extent of brain-like-ness in other ways is unclear (e.g., Is the proposed update rule, described by Eq. 7 and derived in Appendix D, neurally plausible? This depends somewhat on how the Jacobian is computed or approximated.). As a related point, real neurons are only approximately Poisson, and only sometimes. It is probably *more* brain-like to consider them than something like a Gaussian, but it's still far from an actual brain. Also (line 236), an exponential is not the only (or obviously best) way to model the spike threshold of real neurons, at least to my knowledge.

The authors claim that their work provides a "solid foundation for developing prescriptive theories in NeuroAI", but this seems overly strong. If I want to solve problem X subject to a set of constraints Y, how does the iP-VAE work help me? Only a narrow problem setting is considered here compared to the galaxy of problems and constraints relevant for neuroAI.

The authors claim that the iP-VAE is particularly well-suited to neuromorphic implementations (paragraph starting on line 522), but this seems premature given the content of the paper. 

Overall, many big claims regarding how the iP-VAE solves fundamental problems, or is prescriptive, or is particularly well-suited to some future thing, should probably be tamped down, and more time should be spent on supporting the claim that it works well and is especially (along some axes) brain-like.

### Questions
1. Can the authors clarify the structure of their proposed generative model? Why are observations assumed to be Markov, and what real-world assumption does this relate to? 
2. Does iP-VAE perform well compared to vanilla VAEs and other types of generative models, like diffusion models?
3. Can the iP-VAE be trained on a more complex data set than MNIST? If there are technical difficulties, what are they?
4. In what sense does the iP-VAE learn a "compositional code"? Can the authors show representation analysis results to support this?
5. How would a leak term affect the iP-VAE?
6. How is the iP-VAE more brain-like than other proposed brain-like inference approaches? See the earlier Masset and Zavatone-Veth et al. citation, although there are many more such examples (e.g., recent modifications of predictive coding), and the specific paper isn't that important. More comparisons here would be really helpful.
7. How is the authors' proposal "prescriptive"?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes iterative Poisson VAE (iP-VAE) which maximizes ELBO for sequence Poisson observations. The authors demonstrate the superior generalization to out of distribution samples of the proposed method by evaluating on a few real datasets.

### Strengths
- The paper is clearly written.
- The idea of drawing connection to membrane potential dynamics is interesting. 
- The authors have done extensive experiments on a few real datasets, and the results seem good.

### Weaknesses
 - I listed some clarification questions in the section below.

 - Intuitively, why modeling the latent variable z_t as Poisson distribution is better than choosing it as Gaussian as in the vanilla VAE?
- In the experiment section, T_test for iP-VAE is much higher than ia-VAE and sa-VAE. What's the running time comparison for training and inference on test samples?

### Questions
- Intuitively, why modeling the latent variable z_t as Poisson distribution is better than choosing it as Gaussian as in the vanilla VAE?
- In the experiment section, T_test for iP-VAE is much higher than ia-VAE and sa-VAE. What's the running time comparison for training and inference on test samples?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper shows that iterative Poisson VAE can be a reasonable prescriptive model for biological neural networks. Compared to Poisson VAE, iterative nature of the IP-VAE reduces the amortization gap, leading to superior reconstruction performance, sparse features, and OOD generalization.

### Strengths
The paper is well-motivated, and the experiments are extensive.

Interesting results on the sparse features learned by iP-VAE is shown.

### Weaknesses
My biggest concern for this paper is that the authors did not show the generative performance of IP-VAE, which is important for any Bayesian model of the brain. Also, if I understand the paper correctly (line 242-245), at each time point the IP-VAE receives the ground truth image, making the superior reconstruction performance, generalization and parameter efficiency less impressive. For generative models, the info about the data distribution is usually stored in the parameters, it is natural that iP-VAE does not need many parameters if the ground truth samples are provided.

In Figure 4 towards the bottom row of features learned by iP-VAE, it seems some features also overfit to digit-like shape. I wonder if iP-VAE can achieve better generalization performance without these features (by deleting those overfitted features and freezing the rest of the features)

### Questions
1. In Figure 4 towards the bottom row of features learned by iP-VAE, it seems some features also overfit to digit-like shape. I wonder if iP-VAE can achieve better generalization performance without these features (by deleting those overfitted features and freezing the rest of the features)

2. What is $\beta$ in Table 1?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors introduce a new Variational Auto Encoder Architecture based on Poisson distribution and iterative inference (iP-VAE) and connect their new algorithm to sparse coding. They derive an Evidence lower bound for a sequence of poisson distributed latent encodings. 
They evaluate the utility of their model in terms of convergence, efficiency, and out of distribution generalisation.

### Strengths
The topic is of interest. The goal of matching Machine learning concepts to the neuroscience literature is important. 
The related work (section 2) is, in general, well written and structured.

### Weaknesses
I have, unfortunately, a hard time understanding most parts of the experimental section and what the authors aim to convey. 
Variational Auto Encoders (VAEs) are generative models. The loss they are (mostly) trained with (which derives from the ELBO) has two components, a reconstruction-term and a regularisation-term. The reconstruction-term typically refers to the term in the ELBO encapsulating the expected conditional log likelihood of the observation given the latent variable. The regularisation-term typically measures the KL-divergence between the posterior and the prior distribution. 

In their experimental section, the authors chose to merely measure the reconstruction performance, i.e. only part of the loss function.  This is problematic because it does not fully capture the trade-off between reconstruction accuracy and the regularization imposed by the KL divergence term. By only focusing on reconstruction, the authors are effectively evaluating the model's ability to memorize the training data rather than its capacity for generalization or meaningful latent space representation. Generally, by putting small weights on the regularisation term (KL-Divergence) a VAE becomes better in reconstruction but loses its generative capabilities. The works the authors compare with, semi amortised VAE [1] and amortised VAE [2] generally report either the actual ELBO loss function or conditional loglilekelihood (reconstruction) together with KL-Divergence (regularisation). They are also both six years old but have reported on datasets of higher complexity than the authors of the paper at hand.

### Questions
Please refer to the Weaknesses section for questions and concerns. 
I suggest the authors try to compare to more recent (and peer-reviewed) papers. I also suggest that the authors either illustrate why only comparing reconstruction is reasonable, or align their work more closely with the existing literature by a more comprehensive comparison between models (reflecting both regularisation and reconstruction)

### Soundness
2

### Presentation
2

### Contribution
2
