# Efficient Distribution Matching of Representations via Noise-Injected Deep InfoMax

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Deep InfoMax (DIM) is a well-established method for self-supervised representation learning (SSRL) based on maximization of the mutual information between the input and the output of a deep neural network encoder.
    Despite the DIM and contrastive SSRL in general being well-explored, the task of learning representations conforming to a specific distribution (i.e., distribution matching, DM) is still under-addressed.
    Motivated by the importance of DM to several downstream tasks (including generative modeling, disentanglement, outliers detection and other), we enhance DIM to enable automatic matching of learned representations to a selected prior distribution.
    To achieve this, we propose injecting an independent noise into the normalized outputs of the encoder, while keeping the same InfoMax training objective.
    We show that such modification allows for learning uniformly and normally distributed representations, as well as representations of other absolutely continuous distributions.
    Our approach is tested on various downstream tasks.
    The results indicate a moderate trade-off between the performance on the downstream tasks and quality of DM.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work introduces  noise injection to shape a self-supervised learning represenation as Gaussian or Uniformed representation. In short, by injecting a Guassian noise and restricting the convariance of f(x), f(x) tends to be gaussian distirbutioned. By injecting an uniformed distribution within a narrow range $[-\epsilon, \epsilon]$ and restricting the range of f(x) (e.g. within [0,1]), f(x) tends to be uniformly distributioned.

The reason for the gaussian distribution comes from the fact that the Gussian distribution has the max entropy of all distributions with a fixed covariance. The reason for the uniform distribution comes from uniform distribution U(a, b) has the max entropy of a distribution within range [a,b]. 

Apart from the theorical analysis, this work also present interesting plots to demenstrate the two kinds of learned representation, i.e. Gaussian and Uniformed.

### Strengths
- The intuition of two noise injection, Gaussian and Uniform, methods are resonable. The reason for the gaussian distribution comes from the fact that the Gussian distribution has the max entropy of all distributions with a fixed covariance. The reason for the uniform distribution comes from uniform distribution U(a, b) has the max entropy of a distribution within range [a,b]. 

- This work provides a theorical proof of the effect of these two noise injections. 

- This paper provides rich background knowledges. 

- The experiments in this paper (cifar, mnist) demenstrate the usefulness of the two noise injection methods.

### Weaknesses
 - line 236-239 explains why injecting a gaussian noise helps learn a gaussian representation. This sentence is helpful for understanding. It would be good to have a similar short explaination before the proof of uniform noise injection. For example, the reason of small $\epsilon$, discrete support $A$, and the entropy of uniformed distribution. 

- Large experiments beyond cifar and mnist are helpful to convince readers.

### Questions
- what is the meaning of "nats" in Figure 1 caption "Capacity, nats"? Does it refer to $C = d/2 log(1 + 1 / \sigma^2)$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper propose to add gaussian or uniform noise to the output of the encoder in contrastive methods.

### Strengths
The paper defines the notation and robustly use it throughout the paper making it easy to follow along as a    reader. I appreciate the clarity and reading the method and the experimental section. I was also pleasantly  surprised of the novelty of the idea proposed, while being very simple.

### Weaknesses
The main weakness of the paper is that the experiments are conducted on simple and sometimes trivial           benchmarks. The raw input space of MNIST can already be well represented using t-SNE [1] and thus any SSL      representation learning experiments performed on this dataset are dubious. I encourage the authors to          reproduce the visualization obtained on MNIST with CIFAR-10 or CIFAR-100.

One potential issue with adding noise to the output representation is that we limit the bandwith of the        representation. Therefore, while we may see improvement on small datasets such as CIFAR-100, this improvement  may vanish as we scale up the size of the dataset. I encourage the authors to consider running their           experiments on ImageNET to validate the their method scales up to larger and more diverse datasets. 

[Minor] There are some issues with the formatting. E.g. in page 1, the citation overflows to the second page   breaking the reference.

### Questions
* Is the linear probe trained on the output of the encoder or on some intermediate layer?
* Are the gains observed in Table 1 transferrable when training on ImageNet?

### Soundness
2

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
This paper proposes an improved Deep Infomax (DIM) method for self-supervised representation learning. Overall, an independent noise $Z$ is added to the normalized representations of the data. The authors demonstrate that the method is effective since it keeps the same training objective as the DIM. Experimental results also show the effectiveness.

### Strengths
1. The research has been well accomplished since both the theoretical effectiveness and experimental results are provided.

2. The background and fundamental method are well described, so readers can easily follow the idea.

### Weaknesses
The only improvement in this work is the additive noise in DIM, which may be not very overwhelming. However, if this small improvement can be thoroughly discussed and analyzed, the contribution of this work could still be significant. Therefore, my concerns mainly focus on the discussions and analysis:

1. Since the authors claim in the title that the proposed method is an efficient matching method, it should be clarified why the improved approach is efficient. However, I only see that adding noise will not impact the DIM objective while improving the performance. The efficiency is not discussed.

2. The advantage of adding noise is also not well discussed. It is stated that Lemma 3.1 highlights the importance of both additive noise and input data augmentation. Still, I only see the analysis of the significance of augmentation and do not understand why adding noise is also necessary.

### Questions
If the authors can clarify the significance of the additive noise in the theoretical view, this work will be complete, in my opinion. Then, I will consider changing my rating.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper modifies the Deep InfoMax approach to learning representations that match specific distributions (uniform and normal). Specifically, it suggests adding noise to the normalized representations encoded from the inputs, before training them to maximize the mutual information with encoded input augmentations. It provides theoretical upper bounds for the mutual information between the noisy representation and the representation of the augmentation. It shows empirical results demonstrating the distribution matching, and the trade-off regarding the amounts of noise - a high noise level facilitates better distribution matching, but might result in worse representation learning.

### Strengths
1. The paper is very clear and well-written. It is easy to follow the derivations and the main ideas. 

2. It provides a good theoretical and empirical analysis of the method and the trade-offs between representation learning and distribution matching.  

3. The presented modification is simple, and yet it provides a non-negligible improvement in usefulness (sampling).

### Weaknesses
1. The quality of conditional and unconditional sampling, the main property that can be achieved from a distribution matching is not tested on larger scale data. The paper can significantly improve with generation results on a larger scale of data (e.g. ImageNet/Cifar100).

2. Even for the representation learning tests, this paper can improve with testing on larger datasets. The results of Figure 1, for example, are mostly saturated on MNIST and it will be useful to verify the same on larger more diverse datasets. 

3. While the paper has a section that argues that the same method can be applied to other SSRLs, it lacks empirical results that can demonstrate the usefulness/fragility of the training regime with noise.

### Questions
My main questions are about scaling: 

Will the representation learning improve over the baseline InfoMax in more conventional large-scale settings - ImageNet linear-probing/fine-tuning? 

How stable is the training with noise under large-scale settings?

For generation and sampling - can you show interpretable individual directions in the learned representation distribution (again - on more advanced datasets like FFHQ/ImageNet)?

### Soundness
3

### Presentation
4

### Contribution
3
