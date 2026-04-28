# Learning multi-modal generative models with permutation-invariant encoders and tighter variational bounds

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 6, 3, 5, 3

## Abstract
Devising deep latent variable models for multi-modal data has been a long-standing theme in machine learning research. Multi-modal Variational Autoencoders (VAEs) have been a popular generative model class that learns latent representations that jointly explain multiple modalities. Various objective functions for such models have been suggested, often motivated as lower bounds on the multi-modal data log-likelihood or from information-theoretic considerations. To encode latent variables from different modality subsets, Product-of-Experts (PoE) or Mixture-of-Experts (MoE) aggregation schemes have been routinely used and shown to yield different trade-offs, for instance, regarding their generative quality or consistency across multiple modalities. In this work, we consider a variational objective that can tightly approximate the data log-likelihood. We develop more flexible aggregation schemes that avoid the inductive biases in PoE or MoE approaches by combining encoded features from different modalities based on permutation-invariant neural networks. Our numerical experiments illustrate trade-offs for multi-modal variational objectives and various aggregation schemes. We show that our variational objective and more flexible aggregation models can become beneficial when one wants to approximate the true joint distribution over observed modalities and latent variables in identifiable models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a varational bound for multi-modal variational autoencoders. The bound is, to my knowledge novel, and is an extension of previous work on variational bounds defined over subsets of the latent variables. The proposed bound extends these concepts to an arbitrary number of modalities, by defining the bound over all possible subsets of the data distribution (1. Equation after Eq. 4). The paper contains an extensive literature review of related work (with 8 pages of references). Experiments are performed on synthetic data and on rather "small scale" datasets MNIST and SVHN (Street View House Numbers).

### Strengths
The biggest strength of this work is the extensive literature review. The paper serves as a good reference for related work on variational bounds for different distributions, especially for multi-modal latent distributions and also discusses related aspects, for example identifiablity.
The proposed bound is derived from previous work which is clearly presented as its basis.

### Weaknesses
Writing style: The paper introduces a lot of related work before discussing the actual contributions. It would be beneficial for the camera ready version if the authors could revise the manuscript and dedicate more room to the actual contributions of the paper. Also the conclusion and discussion part is a little to short. The experimental evaluation is perhaps below the current standard (see below).

Experimental evaluation:
- 5.1 Linear Multi-Modal VAES: The bounds presented in Table 1 do not show a big difference between each other. However, this experiment is on synthetic data and perhaps the experimental setup could be improved to show more significant differences between the different approaches (See also the questions below).

5.3. MNIST and SVHN are rather small datasets, and nowadays usually we would expect a more challenging evaluation on larger datasets.

Technical remarks: Please number all the equations (at least for review)

### Questions
- 5.1 Linear Multi-Modal VAES: The bounds presented in Table 1 do not show a big difference between each other. However, this experiment is on synthetic data. Could the dataset be modified, e.g. a different number of mixture components, larger (or smaller) variance of the mixture components, such that the differences become more significant?

5.3. MNIST and SVHN are rather small datasets, and nowadays usually we would expect a more challenging evaluation on larger datasets. Is there a larger dataset which could also be used for the rate-distortion analysis?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new variational lower bound for VAEs in the multimodal setting.  The lower bound leverages a permutation invariance property and the resulting architecture seems to yield performance improvements in several experimental settings.

### Strengths
The paper is clearly written and the limitations of this work and related works are well-articulated.  

The contribution appears to be novel, and it nearly always results in models with improved LLs/bounds in the provided experiments.

This application of invariance is novel to me and may be of broader interest in latent variable modeling problems.

### Weaknesses
Many of the technical details have been relegated to the discussion section.  While this is somewhat common practice, there are, in my opinion, a lot of details in the supplementary material.  Taking everything into account:  there seems to be more than enough here to constitute a journal submission.   Cramming this into a conference paper makes it difficult for reviewers to adequately assess the correctness.

While this approach does yield improvements with respect to LLs, it comes at a higher computational cost.  In addition, while I know that LL scores are often focused on in these kinds of works, I often find that LL can provide a misleading picture of the model, especially in continuous settings.  From that perspective, it would have been nice to see more task specific results, e.g., inference, etc. Specifically, it's unclear how the improved log-likelihood translates to better performance on downstream tasks that involve, for example, generating or manipulating data from different modalities. The paper would benefit from experiments that demonstrate the practical utility of the proposed approach beyond just improving the variational lower bound.

I don't really understand why permutation invariance, specifically, is a good thing here.  Why not other forms of symmetries?  I think I would benefit from some higher level intuition here.  It seems to be central to the approach, but I couldn't tease its importance out of the presentation. The paper does not adequately explain why permutation invariance is the right inductive bias for this problem. While the authors mention that it allows for modeling exponentially many functions, it's not clear why this is a desirable property in this context. A more detailed explanation of the theoretical motivation behind this choice, and perhaps a comparison with other potential invariances, would be beneficial.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a method to train a multi-modal VAE.
The authors focus on permutation-invariant encoder which is invariant to the modalities order.
The authors demonstrate on a simple dataset that the proposed method works and explore different model configurations.

### Strengths
* The authors discusses an important area of research - multi-modal generative models.

### Weaknesses
 * The novelty is rather limited (the aggregation schemes are marginally novel, and the invariance is trivially achieved using known architectures).
* The experimentation over a single dataset is not satisfactory.
* Comparison to competing models is missing.
* Optimization using MCMC typically limits the scaling of the proposed method from being used for more complex data (e.g., high dimensional) and architectures (i.e., more expressive models).

### Questions
* Have you tried scaling the method to higher dimensional and more complex data?
* Did you encounter any issues and challenges during optimization?
* What is the optimization procedure? What is the final loss? Can you provide a clear pseudo code?
* Did you compare the proposed model to external baselines?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The article builds upon previous work on Variational Auto-Encoder models designed to work on data with multiple modalities (such as text, images, etc...), on the modelling hypothesis that the different modalities are independently generated from a single common latent representation. The core task that is used to train those models is thus to recover said latent representation from a subset of the observed modalities, and use that to reconstruct the missing modalities.

The paper builds upon a previous bound developed in the restricted context of 2 modalities (Wu and Goodman, 2019), and generalizes to an arbitrary number of them, and an arbitrary observed subset. Alongside this, the paper uses permutation-invariant neural architectures (Zaheer et al, 2017) to build probabilistic encoders that can work on arbitrary subsets of observed modalities, while having more expressive power than the previously-used Mixture-of-Experts and Product-of-Experts constructions.

The resulting architecture is experimentally evaluated on several combinations of encoder architecture and training bounds to evaluate the impact of those two contributions, showing a general improvement to the reconstruction quality.

### Strengths
The main contribution of the paper seems theoretically solid: the bound is properly derived with explicit and reasonable assumptions, and provides a promising framework for formulating the training of multi-modal latent variable models such as VAEs. The proposed construction brings together several ideas from the wider literature in a justified and sound way.

The 2 main contributions are extensively experimentally evaluated, both independently and combined, to previous models on the same data and tasks. Detailed quantitative results are provided, covering a large range of tasks and metrics (reconstruction, cross-reconstruction, utilization of the latent representation for downstream classification, ...), illustrating their contextual strengths and weaknesses fairly.

### Weaknesses
I find the general structure of the paper to be imbalanced: a large portion of the paper is used to reference and restate the literature in a way that in my opinion does not bring much, while most results and observations are stated and barely discussed, even in the extensive appendix.

Listing the points that should in my opinion be expanded:

1) Proposition 1 relies strongly on the assumption on the structure of $q_\phi$ given at the top of page 4 (without being clearly expressed as an assumption), which amounts to stating that the partial encoder should be identical to the empirical marginalization of the full encoder:
$$
q_\phi(z|x_\mathcal{S}) = \int_{x_{\setminus\mathcal{S}}} p_d(x_{\setminus\mathcal{S}} | x_{\mathcal{S}}) q_\phi(z | x_{\mathcal{S}}, x_{\setminus\mathcal{S}}) \text{d}x_{\setminus\mathcal{S}}
$$
While the text below proposition 1 suggests that the training loss encourages the model to bring these two distributions close to each other, there is no discussion about this assumption.

2) At the end of section 2, it is shown that the mathematical optimal partial encoder $q^\star(z|x_\mathcal{S})$ of the mixture-based objective is not equal to the true Bayesian posterior of the model $p(z|x_\mathcal{S})$ (as opposed to the proposed objective), but instead an additional factor is added to it. Unfortunately, this additional factor and how it may impact the model is not discussed at all.

3) In the experimental results of the MINST-SVHN-Text problem, a lot of quantitative performance measures are provided, but they are barely discussed or interpreted.

Also, I have a few more minor points regarding phrasing and clarity:

4) Section 2 makes heavy use of inline math for rather long expressions. While I understand the space constraint, this makes these paragraphs difficult to parse.

5) Lemma 2 and Corollary 3 use the names $Z_\mathcal{M}$ and $Z_\mathcal{S}$ without them being first defined. While we can guess what they are probably supposed to mean, this hurts readability.

6) The legend of Figure 2 is very small and difficult to read without zooming a lot. Furthermore, it uses the name "Masked" to (I suppose) refer to the proposed bound, while this name is not used anywhere else in the paper.

### Questions
My questions directly mirror points that are in my opinion under-discussed:

Regarding the assumption about the structure of $q_\phi$ being compatible with empirical marginalization:
- Is the proposed loss still a proper lower-bound if this assumption is not respected?
- If yes, why is this assumption needed? If not, why is it not a problem?

Regarding the experimental results on MINST-SVHN-Text:
- Why are the model performance so different between the various modalities?
- Why does adding private latent variables seem to overall reduce the performance of the models in terms of conditional coherence (see tables 9-12)?
- Figure 2b suggests that the Mixture loss yields better cross-reconstruction overall, while tables 9-12 suggest the opposite, is there a contradiction?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work describes a new variational bound to train multimodal VAE models and proposes to use two new aggregation functions rather than the mixture of experts (MoE) and product of experts (PoE) that have been typically used in the literature. The proposed variational bound is claimed to address the known limitations of previous variational bounds, while the new aggregation functions should help in learning identifiable models, and achieve higher log-likelihood.

After an introduction to the multimodal generative model problem and a discussion the multimodal VAE literature, the authors describe a  new variational lower bound that is used as a proxy to learn model parameters. This bound is computed using two non overlapping subsets, randomly sampled at each training step. The bound consists of the sum of the conditional bound and a marginal bound of these two subsets, respectively.  In other words, this approach is a generalization to the bound derived in [1].
This bound is claimed to become tighter than the ones from the literature, provided that the encoding distribution closely approximates the true posterior distribution. The authors then discuss an information theoretic perspective of the proposed bound.

Then, new aggregation functions are presented, whereby PoE and MoE are considered as fixed, special cases, and two new,  learnable, aggregation functions, which are permutation invariant, are proposed: (i) Sum pooling, (ii) Transformer encoder.

The authors also discuss the unidentifiability of nonlinear models. It's claimed that the proposed bound generalises some identifiability properties that have been studied in the context of unimodal VAEs, to the case of multiple modalities. Then the authors discuss alternatives to the choice of uni-modal prior densities via Gaussian mixture priors.

Experimental validation of proposed approach and the new aggregation functions consists in a comparison to vanilla PoE and MoE methods: first, on a synthetic dataset, by considering both linear and non-linear problems, then, using a real world dataset, MINIST-SVHN-Text, where the performance of the proposed approach is studied.

[1] M. Wu and N. Goodman. Multimodal generative models for scalable weakly-supervised learning. Advances in neural information processing systems, 31, 2018.

### Strengths
- This work targets an important problem, which is related to multimodal generative modeling. It proposes new aggregation functions, e.g. attention-based functions, which are an interesting addition to the current methods to aggregate latent modalities into a single latent space. 

- The study of identifiability properties of multimodal models is, to the best of the reviewer's knowledge, novel and important.

- The editorial quality of the paper is very good, albeit some related work are missing.

### Weaknesses
 - The work does not directly demonstrate that the proposed bound is tighter than previously reported bounds in the literature. It's not clear how the new bound overcomes the multimodal VAE limitation detailed in [2], which are related to sub-sampling of modalities, which has the problematic effect of inducing an undesirable upper bound.

- The well known limitations from Multimodal VAE literature consist of the undesired trade-off between generation coherence and quality. Additionally, the modality collapse problem due to gradient conflicts [3] can also affect the training process. These limitations are not discussed, although the paper claims that the new proposed bound solves the limitations of Multimodal VAE.

- Some works are missing from the literature review, such as [4].

- The results on the MNIST-SVHN-Text dataset, using the proposed approach, do not seem to improve the overall conditional generation coherence. LLH improvements do not correlate with the overall conditional coherence / latent classification accuracy. In table 9, the cross generation of SVHN given MNIST is slightly better using the proposed approach but the generation of MNIST given SVHN is a lot worse. The proposed extensions do not perform very well across all modalities in terms of coherence: some recent works obtain far superior results with respect to the multimodal VAE literature [5].

- The experimental campaign misses many competitors and benchmarks that are widely used in the literature: for example, competitors such as  Nexus [4],  MMVAE+ [6], MOPOE [7], MVTCAE [8] are not included as baselines. 

- The evaluation protocol adopted in most of the related literature sheds light on two desired properties of multimodal generative models which are generative coherence and quality. Measuring the generation quality is not considered in this work. Joint generation (unconditional generation) by sampling from the prior is one setting in which, in general, Multimodal VAEs fail. Results on joint generation are not included.

- The author considers only one real world dataset containing highly correlated modalities, with the label digit (Text modality). Other benchmarks widely studied in the literature are missing from the experimental section: for example, the Polymnist [7], MHD [4], CUB [2, 9] datasets. This latter showed to be a challenging case for VAE models [2].

### Questions
- Why the proposed bound is tighter than the bound studied in the larger family of multimodal VAE models? Is this an empirical claim via LLH estimation?

- How does the new bound overcome the limitations of Multimodal VAEs, such as the undesirable upper bound due to sub-sampling of modalities? In practice, the new proposed bound is also based on a similar sub-sampling approach as in [1]

- How does the new bound and the presented aggregation methods handle other limitations of Multimodal VAEs, such as the coherence-quality trade-off and modality collapse where stronger modalities dominate over weaker ones [3]?

- The evaluation of the generative quality of the compared models using metrics such as the FID score should be considered. Joint generation results (sampling from the prior) should be reported to evaluate if the new approach helps in this challenging scenario.

- Several missing baselines from the multimodal generative models literature should be included in the experimental comparison: VAE based models such as Nexus,  MMVAE+, MOPOE, MVTCAE are typical baselines (please, see references above).

- The experimental section should be enriched with more challenging datasets, such as Polymnist, MHD, and CUB datasets (please, see references above).

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
