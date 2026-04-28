# Atlas Gaussians Diffusion for 3D Generation

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Using the latent diffusion model has proven effective in developing novel 3D generation techniques. To harness the latent diffusion model, a key challenge is designing a high-fidelity and efficient representation that links the latent space and the 3D space. In this paper, we introduce Atlas Gaussians, a novel representation for feed-forward native 3D generation. Atlas Gaussians represent a shape as the union of local patches, and each patch can decode 3D Gaussians. We parameterize a patch as a sequence of feature vectors and design a learnable function to decode 3D Gaussians from the feature vectors. In this process, we incorporate UV-based sampling, enabling the generation of a sufficiently large, and theoretically infinite, number of 3D Gaussian points. The large amount of 3D Gaussians enables the generation of high-quality details. Moreover, due to local awareness of the representation, the transformer-based decoding procedure operates on a patch level, ensuring efficiency. We train a variational autoencoder to learn the Atlas Gaussians representation, and then apply a latent diffusion model on its latent space for learning 3D Generation. Experiments show that our approach outperforms the prior arts of feed-forward native 3D generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Atlas Gaussians, a new latent representation learning framework designed to improve the efficiency of 3D object generation by addressing the current challenges faced by VAEs. By modeling 3D shapes as a union of local patches, the authors develop a transformer-based decoder to map the low-dimensional latent representations of each patch via UV-based sampling and promote time efficiency when generating large samples of 3D Gaussians. Additionally, the introduced Atlas Gaussian representation considers a disentangled learning of geometric and appearance features, resulting in faster convergence.

### Strengths
- The paper is well-written and organized; hence it is easy for readers to follow. 

- Addressing the current challenges of VAEs in extracting efficient latent representations for generative diffusion models is important. 

- The introduction of the Atlas Gaussians representation with disentangled learning of geometry and appearance features of 3D shapes is novel.

### Weaknesses
 - The proposed approach includes both the Atlas Gaussian representation with disentangled geometry and appearance learning mechanism, as well as a transformer-based encoder. It is unclear which component contributes more significantly to the overall performance.

- It is unclear how geometry and appearance features are disentangled in the latent space. While the loss function is designed to learn each patch’s center and appearance features through supervision, the process for learning geometric features remains vague.

### Questions
- It is unclear how geometry and appearance features are disentangled in the latent space. While the loss function is designed to learn each patch’s center and appearance features through supervision, the process for learning geometric features remains vague.

### Soundness
3

### Presentation
4

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
The authors introduce Atlas Gaussian, a 3D generation approach grounded in diffusion models. 

First, they train a VAE to map 3D shapes into a compact latent space, which is then decoded through a two-branch structure into patch centers and features. These patch centers and features can subsequently be decoded into 3D Gaussian distributions.
Next, they train a Latent Diffusion Model (LDM) within the learned latent space to serve as the generation model. 

Atlas Gaussian offers three main advantages:
1. Using UV-based sampling within a unit square, it can generate a large quantity of 3D Gaussians efficiently.
2. It incorporates a nonlinear, learnable weight function through an MLP-projected positional encoding, enhancing representational power compared to traditional linear interpolation weights.
3. It is computationally efficient with minimal memory usage.

These benefits are substantiated by comprehensive experiments and ablation studies.

### Strengths
1. I appreciate how the introduction section clearly explains and flows through the limitations of recent works, outlining how the authors address these challenges with their proposed method.

2. I appreciate how each section of Section 2: Related Work clearly connects to the proposed method.

3. Sufficient experimental results support the contributions claimed.

4. I value the release of code which enhances transparency and reproducibility.

### Weaknesses
1. I suspect the term “atlas” is intended in the same sense as in AtlasNet (L125~128). If so, adding an explanation would be helpful, as it is part of the method’s name but is not clarified in the text.

2. The method section is presented in a list-like format, making it difficult to read smoothly.

3. The clarity of the writing is lacking. Although the text contains many details, the explanations are somewhat vague, requiring readers to infer and interpret a great deal.

4. Some notations lack sufficient explanation. Although readers might deduce their meanings through context, clearer descriptions would be beneficial. (Also see questions below.)

5. Figure 3 lacks detail and does not clearly relate to the main text, particularly Section 3.2, Stage 1: VAE. For instance,

(1) The steps from $\bar{z} \rightarrow z_0$ are ambiguous. Is the process 

$z' = \mathnormal{CrossAttn}(\bar{z}, \mathcal{P})$

$z'' = \mathnormal{CrossAttn}(z', \mathcal{I})$

$z_0 = \mathnormal{MLP}(z'')$

($z'$ and $z''$ notations arbitrarily assigned as they are not explicitly defined)

correct? 

(2) My understanding is that $z_0$ of Figure 3 represents the end of the VAE encoder, while subsequent steps are part of the decoder. It would help to indicate these details explicitly.

6. The conditioning ($\mathcal{C}$ of Section 3.3) mechanism lacks detail; although some information is provided in the supplementary material, it remains insufficient.

7. An ablation study should be conducted to analyze the impact of the loss hyperparameters ($\lambda_r$ and $\lambda_{KL}$).

### Questions
1. L060 "However, these approaches often focus solely on modeling geometry without considering the appearance attributes."
Can you give a more detailed explanation?

2. What does $d$ represent in L189 and L135 (Equation 4)?

3. What does $n$ represent in L256 and L268?

4. What is the exact relationship between the shape information $\mathcal{S}$ (L263) and the point cloud $\mathcal{P}$ as well as the sparse-view RGB images $\mathcal{I}$? 
From my understanding, the feature dimension of $\mathcal{P}$ is $\mathbb{R}^{|\mathcal{P}| \times d}$, and the feature dimension of $\mathcal{I}$ is $\mathbb{R}^{(|\mathcal{I}| \times h \times w) \times d}$. 
How, precisely, are these features of $\mathcal{P}$ and $\mathcal{I}$, and the feature dimensions related to $\mathcal{S}$, particularly in mathematical terms?

5. How is the learnable query $y$ of the VAE decoder (L277, L284) initialized?

### Soundness
3

### Presentation
2

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
The paper introduces a new framework called Atlas Gaussians Diffusion for 3D shape generation. It models the shape as a union of local patches as 3D Gaussians defined in UV space. This allows the generation process to generate theoretically unlimited number of points while capturing more underlying details of the 3D shape. Extensive quantitative and qualitative experiments demonstrate their results are better than the current SOTA.

### Strengths
The paper nicely integrates 3DGS with diffusion generation scheme and achieves state of the art results in 3D shape generation.

The use of Atlas Gaussians to represent 3D shapes as union of local patch makes it capable of capturing better details and higher scalability.

Decomposing the 3D shape generation into local Gaussian patches and using UV-based sampling to handle shapes of varying complexity.

The evaluation is thorough with reasonable qualitative and quantitative results and achieves SOTA results in 3D shape generation.

### Weaknesses
While in 4.4 discuss about memory consumption and # of patches, the paper is lacking thorough comparison on inference times (esp. with the increase of # of 3DGS) to further justify the value of the framework.

How could the current approach address gap for even finer details of the shapes as Gaussian representation struggles in fine details and often results in blurry effect. Is it only a matter of the # of Gaussians or patches? 

The author mentioned "We take inspiration from the literature that 3D-based neural networks learn better 3D features for recognition and outperform multi-view based networks that leverage massive 2D labeled data." without any citation. There are arguments on both sides about overall performance with both approaches. This sentence seems to be subjective.

### Questions
Do the authors plan to open source the model?

Can UV-based sampling potentially generate artifacts? (e.g. inconsistency or distortions)

How well does the proposed framework handle noisy or sparse data?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors proposed a representation model for generating 3D Gaussians from local patches, named Atlas Gaussians. They parameterized each patch as a sequence of feature vectors and designed a learnable function to decode 3D Gaussians, followed by the integration of UV-based sampling to generate large and theoretically infinite Gaussian points. To learn the Atlas Gaussians, the authors employed a latent diffusion model in the latent space of a VAE.

### Strengths
**S1.** Methodological development is clear and well presented.

**S2.** The paper is very well written and has strong motivation.

**S3.** Consideration of generation 3D Gaussians in latent diffusion model is unique and well-motivated.

### Weaknesses
While this paper explores a unique perspective on 3D generation, it primarily lacks proper experimental support and validation. It is difficult to discern the specific novelties and contributions (considering the three contributions outlined in L102-L107) that this paper offers compared to recent SOTAs, e.g., LN3Diff and others. Although the current methodological development is generally clear, the contributions are still not well-supported by the qualitative findings and significantly improved quantitative results reported in the paper.


**W1. Latent Diffusion Novelty:** I believe the variational diffusion model is not a novelty in terms of technical development. Besides, the authors directly utilized the EDM algorithm as their latent diffusion. What makes the integration of the latent diffusion model a unique/novel contribution other than working with a different data type such as 3D Gaussians? Please highlight specific contributions with details in the revised version.


**W2. Experimental Validation:** 
*(i)* Going through the generated samples reported in the LN3Diff and this paper, it is difficult to understand the effectiveness of the proposed model. The qualitative comparison with the LN3Diff model in Fig. 5 raises concerns regarding whether the baselines have been trained to their optimal or not. Besides, for most of the pictorial depictions, I can guess that either the sampling or training has not been done properly for all the SOTA, specifically in Fig. 6. In the SOTA baselines papers, the structure of the synthesized images seems to be well preserved. Then why the authors could not achieve that? *(ii)* Did the authors run all the baselines, and try to reproduce their results? Or they just copied the FID/KID numbers from the papers? *(iii)* I would suggest reporting the mean along with std to see the robustness of the scores. *(iv)* Inference times in Tab. 2 are not comparable with GVGEN and LN3Diff as they carried out their experiments on different GPU setups. *(v)* As one of the contributions of this paper is using a transformer-based decoder, I would suggest the authors show a very brief ablation carrying out the experiments on a vanilla decoder. Also, compared to the LN3Diff which used a transformer-base decoder, what is the uniqueness of their proposed architecture?


**W3. Loss function and optimization:** According to the derived loss function, the optimization process seems to be quite complex to converge to the optimal stage as one needs control around 10 distinct losses, including the KL divergence term. I suggest the authors to shed some light onto the complete optimization process other than simply denote large number of losses with weighting parameters.


**Minor.** Please cite necessary papers that are relevant to the proposed methodology, other than just scrapping eight pages of references which includes papers that do not fall into the problem of this paper.


In its current format, I believe the paper falls below the threshold for acceptance. The score reflects an evaluation of the problem definition, motivation, and presentation. However, I am open to raising my score if the above concerns are properly addressed. Besides, I request the authors to specifically highlight the methodological contributions and novelties (compared to the current SOTA), beyond the focus on generating 3D Gaussians.

### Questions
Please refer to the Weaknesses section, where the primary questions have been outlined. Additional points are provided below -

1. How are the local patches parameterized as a sequence of feature vectors, and how is the learnable function designed to decode 3D Gaussians from these feature vectors?

2. Why is UV-based sampling used instead of directly generating an infinite number of 3D Gaussian points? Why is it necessary, and does it help in preserving the topology of the synthesized 3D objects?

3. How does a large number of 3D Gaussians contribute to achieving high-quality details?

4. How transformer-based decoder help to remove all the existing limitations posed by a vanilla decoder (other than the transformer decoder in LN3Diff)? Are there any strong quantitative and qualitative ablations?

5. What is the corner-encoding scheme?

### Soundness
3

### Presentation
3

### Contribution
2
