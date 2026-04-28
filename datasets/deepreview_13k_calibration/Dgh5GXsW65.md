# There and Back Again: On the relation between noises, images, and their inversions in diffusion models

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 3, 8, 8

## Abstract
Denoising Diffusion Probabilistic Models (DDPMs) achieve state-of-the-art performance in synthesizing new images from random noise, but they lack meaningful latent space that encodes data into features. Recent DDPM-based editing techniques try to mitigate this issue by inverting images back to their approximated staring noise. In this work, we study the relation between the initial Gaussian noise, the samples generated from it, and their corresponding latent encodings obtained through the inversion procedure. First, we interpret their spatial distance relations to show the inaccuracy of the DDIM inversion technique by localizing latent representations manifold between the initial noise and generated samples. Then, we demonstrate the peculiar relation between initial Gaussian noise and its corresponding generations during diffusion training, showing that the high-level features of generated images stabilize rapidly, keeping the spatial distance relationship between noises and generations consistent throughout the training.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors perform an in-depth analysis of the DDIM inversion technique by analyzing the relationship between initial Gaussian samples, the corresponding generated samples, and their inverted latents. The empirical analysis is presented on pixel and latent space diffusion models for CIFAR-10, ImageNet, and CelebA datasets.

### Strengths
The authors attempt to demonstrate the relationship between diffusion latents, their corresponding generated samples, and latents obtained using DDIM inversion. Since DDIM inversion is of interest to practitioners working in controllable synthesis using diffusion models,  some of the analyses presented in the paper in Fig. 4 can be useful.

### Weaknesses
Since the paper primarily analyzes the relationship between the diffusion latents, generated samples/ data points, and the reverse DDIM latent without any methodological contributions, I would expect the experiments section to be more detailed and clear. More specifically, the following observations stand out:

1.  **Missing experimental details**: For instance, the image resolution at which the models were trained is missing for all datasets. Similarly, details on the network architecture used for the diffusion denoiser and training hyperparameters are missing for both pixel space diffusion models and LDMs. Moreover, it is unclear from the text how the angles between different vectors were computed in Figure 2. While these are only a few examples, I would request the authors include all experimental details in the Appendix.

2.  **Limited experiments and overclaiming**: Firstly, if I understand correctly, Sections 4.2 and 4.3 reaffirm already existing conclusions about the DDIM Inversion procedure (as the authors note in lines 172-173) using a different experimental methodology. In this context, can the authors point out additional insights that can be drawn from these experiments? Secondly, the authors note the following in Line 175: We study the implications of this fact and show its far-reaching consequences. However, it is not clear from the main text what these implications are, as these are never discussed and, therefore, seem like overclaiming. Can the authors discuss this in detail? I would have liked to see the impact this can have on the DDIM inversion-based editing or reconstruction capabilities, which would justify this claim. Lastly, I don't see any results on a large-scale experiment (say ImageNet-256), and it is unclear how severe this problem is at scale. Can the authors comment on this and include relevant experiments?

3. While the experiments in Section 4.4 are interesting, what is their significance in the context of the broader picture of the paper? If I understand correctly, the focus of the main text is to highlight issues with DDIM inversion by analyzing the relationship between the inverted latents, the original latents, and the generated samples, and therefore it is not clear how Section 4.4 fits here since there seems to be no reference to DDIM inversion here. Secondly, in Section 4.4, what is the minimum L2 distance criterion for the assignment of images to noise mentioned in line 321?

**Minor Comments**

1. The introduction can be improved. For instance, the authors note the following:
```
Nevertheless, one of the significant drawbacks that distinguishes diffusion-based approaches from other generative models like Variational Autoencoders (Kingma & Welling, 2014), Flows (Kingma & Dhariwal, 2018), or Generative Adversarial Networks (Goodfellow et al., 2014) is the lack of implicit latent space that encodes training data into low-dimensional, interpretable representations.
```
While GANs and VAEs indeed are designed to assign low-dimensional latent codes to the data, Flows/Continuous flows also do not possess a low-dimensional latent space and are similar to diffusion models in that aspect. In fact, the ODE sampling in diffusion models is equivalent to simulating a continuous normalizing flow with a vector field defined in terms of the score function. Therefore, this claim is misleading, and it would be great if the authors could revise this in the main text.

2.  **Missing citations**: Reference to related work is missing in some places. For instance, in line 37, `combining diffusion models with additional external models`, references to several related works are missing [1,2]

3. Figure 1c: There is a single latent $\hat{x}_T$ for a panel of 4 images, and it is thus confusing. Could the authors clarify which image in this panel the generated latent corresponds to?

4. Table 1: What does each row correspond to? Does it denote the correlation of the pixels in the latent (pure Gaussian noise or reversed DDIM) vector vs data samples?

### Questions
See the Weaknesses section.

### Soundness
1

### Presentation
1

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
This paper presents some empirical observations between noise, image, and its inversion: (1) the inversion contains some structure of the original image and is different from the noise; (2) the inversion approximately lies in the trajectory from noise to image; (3) it is possible to assign noise to the corresponding generated images from L2 distance and this mapping is learned at an early stage of training

### Strengths
This paper presents intriguing empirical observations, particularly the ability to assign noise to corresponding generated images based on L2 distance. This phenomenon appears to relate to diffusion models and optimal transport, and further exploration could deepen our understanding of diffusion model training dynamics and properties of image manifold.

### Weaknesses
The paper feels incomplete to me.

For the empirical observations in Sections 4.2 and 4.3, I don’t see any clear applications based on these findings. I suggest taking it a step further; for example, how could we reduce the divergence between the inversion and the noise? What insight does it provide if the inversion lies along the trajectory from noise to image?

The observation in Section 4.4 is interesting, but the paper doesn’t explore any theoretical insights or potential applications related to this phenomenon. One possible direction could be to link it to optimal transport, building a theoretical framework to better understand the training dynamics of diffusion models.

Overall, without applications or theoretical insights, the empirical analysis lacks clear motivation. I hope the authors can identify relevant scenarios where these observations could be put to practical use.

### Questions
1. From Table 2, are there any insights into why LDM could achieve 100% accuracy for both $x^0 \rightarrow x^T$ and $x^T \rightarrow x^0$, but DDPM could only achieve high accuracy for $x^0 \rightarrow x^T$. What key differences between LDM and DDPM might explain this discrepancy?

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
This work examines the relationship between the initial Gaussian noise, generated images, and latent representations produced using the DDIM inversion technique in diffusion models.

### Strengths
* The paper provides comprehensive empirical evidence to support its claims, using various metrics and visualizations.
* The study demonstrates the limitations of DDIM inversion, particularly its deviation from theoretical expectations and the persistence of inversion errors despite prolonged training.

### Weaknesses
 * The analysis focuses primarily on DDPM and LDM models, leaving open the question of whether the observed phenomena generalize to other diffusion model architectures.
* While the paper empirically observes the inaccuracy of DDIM inversion and the early formation of noise-to-sample mapping, it lacks a theoretical explanation for these findings. Specifically, the paper does not delve into the underlying mathematical reasons why the DDIM inversion deviates from its theoretical ideal, nor does it explore the mechanisms that cause the noise-to-sample mapping to solidify prematurely during training. This absence of theoretical grounding limits the impact of the empirical findings.

### Questions
* Does the observed early formation of the noise-to-sample mapping have
  connections with the stages of reverse diffusion process as discussed
  in https://arxiv.org/abs/2402.18491?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper analyzes intriguing properties of the relationship between the triplet (image, noise, latent) in diffusion models, where “latent” refers to the noise computed by the inverted diffusion process in deterministic diffusion models (DDIM). Even if from a theoretical point of view, noise and latent should match, in practice this does not happen due to approximations required to practically implement the inverted diffusion process. This analysis is performed in two stages: first of all, the authors shows that the latent variable is located next to the trajectory mapping noise to the generated image, by analyzing both the angles of the triangle with vertices (image, noise, latent), and by computing the distance of each element x_t of the trajectory with the edge connecting the noise to the latent. Moreover, they show that this behavior emerges at the beginning of the training, and never changes as the training advances. In the second stage, the authors argue that the mapping between noise and the generated image is “predictable”, in the sense that the noise gets mapped to the closest feasible generated data, measured in L2 loss. Again, they show that this behavior emerges at the very beginning of the training.

### Strengths
The idea presented in the paper is original, as not many authors analyzed the relationship that occurs between the noise that generates an image and the latent encoding of the image itself in deterministic diffusion models. Due to the nowadays popularity of DDIM, I also believe that this work is significant for the scientific community, as it describes intruguing properties of these models.

### Weaknesses
I believe the paper has a few aspects that require to be improved to allow for a precise decision. In particular:
- the description of the experiments is too hasty and does not go enough into the details, making it very hard to understand. In particular, the whole paper is very confusing in the distinction between DDPM and DDIM. In Section 2, the authors define DDPM as the model obtained by setting $\eta = 1$ in the definition of $\sigma_t$ in Equation (2), while DDIM is the model obtained by setting $\eta = 0$, and its reverse process is fully deterministic, once $x_T$ is given. Clearly, the inversion map, mapping $x_0$ to its latent, is only defined in the DDIM setting. In Section 4, however, the authors continuously interchange the names DDPM and DDIM, making it very hard to understand which model they are using. For example, both Table 1 and Figure 1 uses the name “DDPM” to indicate the models, while the first paragraph of Section 4.2 refers to them as “DDIM”. Therefore, I suggest the authors to rewrite this section by paying more attention to the definitions of DDIM and DDPM. Therefore, I suggest the authors to:
   1. clearly define DDPM and DDIM early in the paper and consistently use these terms throughout.
   2. explicitly state which model (DDPM or DDIM) is being used in each experiment in Section 4.
   3. explain how the inversion process is applied to DDPM models if that is indeed what they are doing.
- in Section 4.4, they refer to “the smallest L2 criterion” without introducing it. Moreover, the obtained results are confusing to me since I didn't expect a discrepancy in the accuracy of $x_0 \to x_T$ vs $x_T \to x_0$. In a final version of this work, I expect the authors to:
   1. Formally define the "smallest L2 criterion" when it's first mentioned.
   2. Explain the classification process using this criterion in more detail. Specifically, how are the $N$ initial Gaussian noises and their corresponding $N$ image generations used in the assignment process? How does the iteration over noises and calculation of distances to all generations lead to an assignment, and how is the accuracy of this assignment determined?
   3. Address the apparent discrepancy between the accuracies of $x_0$ -> $x_T$ and $x_T$ -> $x_0$, given the symmetry of the L2 norm. Provide a theoretical justification or empirical evidence to explain why the assignment process is not symmetrical.
- In line 348, after discussing the accuracy of the metrics between image and noises, the authors say “we can observe that the distance between noise and latents accurately defines…”. Note that, in this section, the latents were not considered, since all the experiments were performed on images and noises. Therefore I do not understand what they want to say with this sentence. In general, I suggest the authors to re-check Section 4 to correct the errors and improve the readability, better clarifying all the steps they performed. Please note that the length of the paper is at most 10 pages EXCLUDING the citations, therefore you still have 3 pages left, which you can use to expand the description of the experimental section.

**Minor Comments.**

- In line 092, you say “DDIM inversion approximates this equation by assuming linear trajectory”. Explain these in more detail, since it is not clear to me why this assumption implies Equation (4). Specifically, how does the assumption of a linear trajectory between $x_t$ and $x_{t-1}$ allow for the approximation used in the DDIM inversion, and how does this relate to the noise-prediction model's output?
- In Equation (4), remove the bold from $x_{t-1}$ to be coherent with the notation employed in the paper.
- In line 107, the referred equation should be Equation (3).
- In the related works, I believe you should also consider at least the ODE inversion paper by Song et al. [1], and also Asperti et al., 2023 [2], which introduces the DDIM inversion through neural network training.
- In the list of models with “meaningful latent space encoding”, the authors considers also GAN. I believe this is not the case, since GAN has a similar behavior as DDIM, i.e. there is no meaningful nor explicit latent space, and it has to be recovered by techniques that are very similar to the ones used to invert DDIM, like GAN inversion.
- I believe lines 158-159 should be postponed since they refer to the “two models” that you introduce in lines 159-160.
- In lines 215 and 221 you say that the latent is located along the trajectory, while you actually show that it is next to the trajectory.

### Questions
I included a few questions in the "Weakness" section

### Soundness
2

### Presentation
2

### Contribution
4
