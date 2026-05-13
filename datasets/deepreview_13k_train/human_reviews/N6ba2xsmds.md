# Outlier Synthesis via Hamiltonian Monte Carlo for Out-of-Distribution Detection

- Decision: Accept
- Scores: 6, 8, 8, 5

## Abstract
Out-of-distribution (OOD) detection is crucial for developing trustworthy and reliable machine learning systems. Recent advances in training with auxiliary OOD data demonstrate efficacy in enhancing detection capabilities. Nonetheless, these methods heavily rely on acquiring a large pool of high-quality natural outliers. Some prior methods try to alleviate this problem by synthesizing virtual outliers but suffer from either poor quality or high cost due to the monotonous sampling strategy and the heavy-parameterized generative models. In this paper, we overcome all these problems by proposing the Hamiltonian Monte Carlo Outlier Synthesis (HamOS) framework, which views the synthesis process as sampling from Markov chains. Based solely on the in-distribution data, the Markov chains can extensively traverse the feature space and generate diverse and representative outliers, hence exposing the model to miscellaneous potential OOD scenarios. The Hamiltonian Monte Carlo with sampling acceptance rate almost close to 1 also makes our framework enjoy great efficiency. By empirically competing with SOTA baselines on both standard and large-scale benchmarks, we verify the efficacy and efficiency of our proposed HamOS.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Many existing OOD detection methods rely on a large, high-quality set of natural outliers. To address limitations with synthetic outliers, this paper introduces the Hamiltonian Monte Carlo Outlier Synthesis (HamOS) framework, which uses Markov chains to generate diverse and representative outliers based solely on in-distribution data. HamOS achieves efficient and high-quality synthesis, showing superior performance over state-of-the-art baselines on standard and large-scale benchmarks.

### Strengths
- The motivation behind this method is clear and compelling, focusing on synthesizing effective virtual OOD data to enhance the robustness of machine learning models. 
- Unlike traditional approaches that rely heavily on large, high-quality pools of natural outliers, this method leverages the technical innovation of Markov chains to generate diverse and representative outliers from only in-distribution data. 
- This framework not only provides high-quality synthetic outliers efficiently but also demonstrates superior performance across multiple datasets, validating its effectiveness and efficiency compared to state-of-the-art methods in OOD detection.

### Weaknesses
 - There are several detailed errors in the article that affect the reader's experience. For example, the caption of Figure 1 mentions ImageNet.
- The manuscript's explanations are difficult to follow, especially in the method section regarding how OOD samples are synthesized and how HMC is utilized. This is particularly challenging in the part involving Equation 3.

### Questions
- How does the proposed method compare to NPOS and VOS in terms of time cost? 

- How stable are the experimental results (e.g., what is the standard deviation)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes HamOS (Hamiltonian Monte Carlo Outlier Synthesis), for out-of-distribution (OOD) detection that uses Hamiltonian Monte Carlo sampling to generate synthetic outliers from in-distribution data. The key innovation is using HMC to sample diverse outliers in a learned hyperspherical feature space, guided by an OOD-ness density estimation based on k-nearest neighbors. The framework combines classification, contrastive learning, and OOD discernment losses to learn representations that better separate ID and OOD data.

### Strengths
- This provides a novel application of HMC for outlier synthesis, and provides an elegant integration of hyperspherical embeddings with HMC sampling. Novel synthesis framework avoids the need for access to real outlier data. 
- The benchmarks studied are comprehensive, written up in a well-structured experimental section. SoTA performance is achieved.
- The code in the supplementary section is cleanly integrated, kudos!
- Visualizations are intuitive and informative, well presented!

### Weaknesses
The paper presents Hamiltonian Monte Carlo (HMC) for sampling outliers in latent space, sharing similarities with score-based generative models. It defines an OOD-ness energy function: $U_{OOD}(z; Z_u, Z_v) = -\log P_{OOD}(z; Z_u, Z_v) = -\log \sum_{i=u,v} P_{OOD}(z; Z_i) + \text{constant}$, which is analogous to score models' $\nabla_x \log p(x)$ and HamOS's $\nabla_z U_{OOD}(z)$

The HMC sampling procedure follows $q^{(ℓ+1/2)} = q^{(ℓ)} - \frac{\epsilon}{2}(I_d - z^{(ℓ)}(z^{(ℓ)})^\top)\nabla_{z^{(ℓ)}} U_{OOD}(z^{(ℓ)})$, similar to Langevin dynamics $x_{t+1} = x_t + \frac{\epsilon}{2}\nabla_x \log p(x_t) + \sqrt{\epsilon}z_t$. 

The main differentiator - HamOS's objective function $L_{HamOS} = L_{CE} + L_{ID-con} + \lambda_d L_{OOD-disc}$ combines classification, contrastive learning, and OOD detection, differentiating it from traditional diffusion models by sampling between ID clusters to find OOD regions rather than sampling from noise to data distribution.

To improve the paper, the authors should add a section comparing their work to score-based sampling, properly cite relevant prior work on gradient-based sampling in latent spaces, and explain their advantages over traditional score-based approaches. These advantages include computational efficiency, direct optimization for OOD detection, and class-conditional sampling between clusters. The paper could also discuss potential cross-pollination opportunities, such as incorporating score network architectures for OOD-ness estimation, adopting noise scheduling strategies from diffusion models, and utilizing classifier-free guidance techniques.

### Questions
- How does the performance of HamOS scale with feature dimension? Hyperspherical geometry might become problematic at higher dims.
- How sensitive is the method to choosing initial midpoints between the clusters?
- Could you provide more theoretical insight into what hard margin to choose and a principled way to select values for different datasets?
- What makes HMC-based sampling more effective than simpler Gaussian sampling approaches?
- See, above "weaknesses". I'd be willing to revise score upwards, provided this is addressed.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper used Spherical HMC to generate OOD data and then from that figure out which data is ID and which data is OOD.

### Strengths
Uses Spherical HMC to better sample from the energy basin to sample OOD points. 

Principled and theoretically sound way to generate OOD samples and consistently outperforms other methods on the compared tasks and datasets.

### Weaknesses
In Fig 7 TNSE HMC is working a lot better to sample the OOD regions compared to NPOS, but in Figure 10 NPOS actually seems to be performing just as well or maybe even better as Spherical HMC. 

One thing that is not clear to me is how we can understand the quality/utility difference between the OOD points sampled between the two methods other than the effect of outlier detection, but this might be out of the scope of the paper.

### Questions
I know HMC can be a bit computationally heavy, can the authors talk about this a bit? It is not immediately obvious to me if one should care about computational load in this setting, but it would be good to discuss runtimes or theoretical cost vs other methods non the less. 

Do the authors think something like Spherical RMHMC would do a better job or is Spherical HMC (SpHMC) good enough? 

I am wondering if the authors have any idea about the quality of the generated samples? Can they be used to boost the ID or OOD classification accuracy of the underlying models? I ask this because there was a paper that used MCMC to sample from an EBM and then train on those samples. They found this reduced performance unless the images were of high quality. It would be interesting if the samples generated via SpHMC are of high enough quality and diverse enough to actually directly boost acc performance of the model. 

[1 ]Pooladzandi, Omead, et al. "Generating High Fidelity Synthetic Data via Coreset selection and Entropic Regularization." arXiv preprint arXiv:2302.00138 (2023). https://arxiv.org/abs/2302.00138

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
5

### Summary
The paper proposes a novel framework called Hamiltonian Monte Carlo Outlier Synthesis (HamOS) for out-of-distribution (OOD) detection. The primary goal of HamOS is to address the limitations of current outlier synthesis approaches, which often rely on either extensive collections of natural OOD data or generative models that are computationally demanding.

HamOS uses Hamiltonian Monte Carlo (HMC) to generate diverse and representative virtual outliers directly from the feature space of in-distribution (ID) data. Unlike previous methods that use Gaussian sampling or generative models, HamOS utilizes Markov chains to sample new virtual outliers by traversing a broad area of the feature space. The process ensures that the synthesized outliers are well-distributed and possess varying degrees of OOD characteristics, which helps in improving OOD detection capabilities.

The framework is evaluated on standard benchmarks like CIFAR-10, CIFAR-100, and ImageNet-1K, and shows significant improvements in OOD detection metrics compared to state-of-the-art baselines. The proposed HamOS achieves a balance between diversity and representativeness of synthesized outliers.

### Strengths
1. Using HMC for generating diverse virtual outliers is a creative adaptation of a well-known sampling technique in statistics and machine learning. Unlike the conventional generative or Gaussian-based sampling methods, this approach allows the model to extensively traverse the latent feature space, thus creating diverse and representative OOD samples. This unique utilization of Markov Chain Monte Carlo (MCMC) methods for OOD detection offers an innovative approach that is distinct from prior generative and noise-based sampling strategies.

2. The concept of OOD-ness estimation to guide the sampling process is also a good addition. By focusing on hyperspherical embeddings and using distance metrics to determine the likelihood of being OOD, the paper contributes a perspective on how to quantify and synthesize OOD characteristics in feature space.

### Weaknesses
1. The paper's claims regarding the novelty of using Markov chains for outlier synthesis are overstated. Specifically, the statement in the first contribution on page 1 claims that outlier synthesis using Markov chains is a "new paradigm" for OOD detection, which is misleading. Markov chains are a well-established approach in sampling, and the application to outlier synthesis does not represent an entirely new paradigm, but rather a new technique within an existing category.

2. In the current era, large language models (LLMs) and multimodal foundational models have demonstrated remarkable performance in numerous domains, including computer vision, text understanding, and scientific knowledge discovery. The paper only evaluates HamOS on natural image datasets (e.g., CIFAR-10, CIFAR-100, ImageNet-1K), which raises concerns about its significance and practical applicability in other fields.

3. The concept of "OOD-ness" is central to the proposed approach, but its definition remains unclear. Specifically, it is not evident how OOD-ness is formally quantified or measured, which complicates understanding how diverse outliers are synthesized. There is a lack of clarity regarding whether OOD-ness is defined solely based on distance metrics (such as k-nearest neighbors) or if other factors are considered.

4. The advantages of Hamiltonian Monte Carlo (HMC) over other sampling methods, such as Gaussian sampling or Random Walk MCMC, are not sufficiently discussed. The reader is left wondering why HMC is particularly suitable for OOD detection and how it performs better than other, potentially simpler, methods.

5. In Table 3, HamOS shows low inter-class dispersion, which is concerning as it suggests poor separation between different ID classes in the feature space. This could potentially affect the performance of the method on in-distribution (ID) classification, as class separation is critical for robust classification.

### Questions
1. Could you provide additional context that clearly distinguishes this work from existing generative or sampling-based methods for OOD detection? Specifically, how does your approach go beyond being a new method and qualify as a new paradigm?

2. In the era of large language models (LLMs) and multimodal foundational models, what role do you envision for OOD detection, especially for image data? How does your proposed method relate to or complement the capabilities of LLMs?

3. Can the proposed HamOS be adapted to other domains, such as text (e.g., natural language processing) or scientific discovery? If feasible, could you elaborate on the generalization of HamOS to these other types of data? Providing a discussion or a hypothetical example would help establish the broader applicability of your work.

4. How does HMC sampling compare to other sampling methods, such as Gaussian sampling or Random Walk MCMC, in the context of OOD detection? Can you provide either a theoretical or empirical comparison to justify the choice of HMC?

### Soundness
2

### Presentation
3

### Contribution
3
