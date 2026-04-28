# Discrete Distribution Networks

- Decision: Accept
- Avg Score: 7.00
- Scores: 5, 8, 8

## Abstract
We introduce a novel generative model, the Discrete Distribution Networks (DDN), that approximates data distribution using hierarchical discrete distributions. We posit that since the features within a network inherently capture distributional information, enabling the network to generate multiple samples simultaneously, rather than a single output, may offer an effective way to represent distributions. Therefore, DDN fits the target distribution, including continuous ones, by generating multiple discrete sample points. To capture finer details of the target data, DDN selects the output that is closest to the Ground Truth (GT) from the coarse results generated in the first layer. This selected output is then fed back into the network as a condition for the second layer, thereby generating new outputs more similar to the GT. As the number of DDN layers increases, the representational space of the outputs expands exponentially, and the generated samples become increasingly similar to the GT. This hierarchical output pattern of discrete distributions endows DDN with unique property: more general zero-shot conditional generation. We demonstrate the efficacy of DDN and its intriguing properties through experiments on CIFAR-10 and FFHQ.  The code is available at \url{https://discrete-distribution-networks.io/}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes to generate samples in a sequential way: pass the output of the previous module into a function randomly selected from a set of K functions in the current module, with the initial input to the first module being a zero vector. To train each module in the space, one first collect a trajectory with these modules except that one does not do random sampling out of K functions but pick the one with the output closet to the data sample $x$. With this trajectory, one computes L2 distances between the output of each module and $x$ and optimize it. The paper shows some empirical results on the CIFAR-10 dataset.

### Strengths
The proposed method is simple and seemly intuitive, and has been experimented on small-scale datasets like CIFAR-10.

### Weaknesses
Purely based on the presentation of the paper, I find the proposed method neither theoretically attractive, as it does not explicitly model probability distributions or model some complex distributions, nor empirically useful due to its worse performance compared to simple baselines like DCGAN. Indeed, the paper claims that VQ-VAE is unsatisfactory (e.g., in the abstract) but it does not even compared against VQ-VAE.

If we take a closer look into the proposed method, it seems to me not too different from a slightly-different VQ variant of diffusion models (e.g., https://arxiv.org/abs/2111.14822) -- running discrete diffusion (as the proposed model is basically trained in a similar way) on a latent space represented by a codebook of features, probably with some additional gradients of hierarchical latent spaces. The paper fails to connect the proposed method to a lot of existing papers and explain 1) what is different and novel given these existing methods and 2) why these design choices.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes Discrete Distribution Networks (DDN) a new class of image generative models. Discrete Distribution Layers within a DDN output multiple images at a time, and one image is sampled and concatenated as a feature to input to the next layer in an autoregressive fashion. During training, the loss is a reconstruction loss of the output sample of each DDL that best matches with the input image. Several tricks are provided to help optimization. During sampling, external signal can be provided without using gradients in order to condition generation. Qualitative and quantitative results are provided for unconditional CIFAR-10, FFHQ, and Celeb-A generation in addition to qualitative results for MNIST.

### Strengths
* The idea of sampling an image and autoregressively feeding it back in through each layer in a forward pass is novel to the best of my knowledge. 
* The ability to condition generation on external signals without gradients is a useful property. 
* DDN is showcased for a variety of applications such as inpainting, colorization, denoising, super-resolution, CLIP-guided editing. 
* A variety of tricks are provided to help training, such as the Split-and-Prune algorithm, chain dropout, residual learning, leak choice.

### Weaknesses
 * I understand that this paper serves as a proof-of-concept for a new type of generative model, but the model is validated on small scale datasets (e.g., CIFAR-10, MNIST, CelebA, FFHQ-64x64). Furthermore, it does not compare against more modern approaches such as diffusion models, and quantitatively lags behind DC-GAN. However, I do not think it is fair to hold this novel method to the same standard as more matured, modern approaches. 
* The method relies on generating multiple samples in parallel and requires multiple layers for further refinement. This seems quite expensive and hard to scale to higher resolutions. 
* The placement of tables and figures reduces the quality of presentation. For instance, Figure 9 has a large white space above it. Table 2 is presented on page 8 even though ablations are not addressed in text until page 10. Figure 5 showcases an experiment which is not addressed in the main text of the paper. So it would be more fitting in the appendix.

### Questions
* Can DDN scale to larger and higher resolution datasets, such as FFHQ 256x256, or ImageNet 256x256? 
* What are the parameter counts of the baselines compared (DC-GAN, IGEBM, VAE, etc.)? DDN benefits from more layers since it can refine more, so the baselines should have similar parameter counts. 
* How does a single shot DDN compare against a default DDN allowing for the same number of refinements?
*  Generating multiple samples in parallel for sampling is expensive. What are the memory requirements compared to the baselines in the paper?

### Soundness
3

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
4

### Summary
The authors propose a new generative model, based on generating K examples at each layer and choosing the one closest to a ground-truth instance. This formulates a discrete hierarchical distribution. At inference, taking a random node at each layer provides a random sample. Both conditional and unconditional generation are demonstrated.

### Strengths
1. I find the method novel and elegant.
2. The ability to produce visualization of the hierarchical generation (figs 8, 18) is a very enlightening feature.
3. The authors propose some practical techniques to deal with this non-differentiable sampling. The proposed "split-and-prune" trick is clever and elegant.
4. The novelty is very strong, and this should not be overlooked. This is a whole new method, very different from any of the existing generative models.

### Weaknesses
1. Theoretical analysis is missing. No mathematical derivation that shows why the distribution of generated images should converge to the real data distribution. Specifically, a formal proof is needed to demonstrate that the proposed hierarchical sampling process, guided by the split-and-prune algorithm, will provably converge to the target data distribution under reasonable assumptions about the model's capacity and the training data. The paper lacks a rigorous treatment of the conditions under which the learned discrete hierarchical distribution will approximate the true data distribution. This includes an analysis of the approximation error introduced by the discrete sampling and the impact of the split-and-prune algorithm on the convergence properties.
2. Eventually, if I understand correctly, for unconditional generation, the model has a finite number of specific examples it can produce K^L. Even if this number is big, this suggests that the model essentially is a compressed way of storing all its possible results in a tree based database. This might make a problem to scale up. Since the demonstrated data relatively has few dimensions, this suggests that actually holding the entire dataset might require more or close storage to the model itself. A quick calculation to demonstrate: MNIST has 70k images (train+test) of 28x28, this is 54880000 integers: ~55MB. EDM smallest model has 62M parameters, even if we take these as 1 byte each it is heavier. The core concern is that the model's generative capacity is fundamentally limited by the discrete nature of its latent space, where the number of possible outputs is bounded by K^L. This raises questions about the model's ability to generalize beyond the training data and its scalability to high-dimensional datasets. The finite number of possible outputs suggests that the model may be memorizing the training data rather than learning a true generative distribution.
3. I am adding the weakness of low quantitative results and lack of demonstration of higher scales. To be clear, I think it is legitimate for novel methods but it is still a weakness. (i.e. if this model would have produced SotA generation results it would have been rated higher). The experiments are limited to relatively low-resolution datasets, and the quantitative results do not demonstrate state-of-the-art performance. The lack of experiments on more complex, high-dimensional datasets raises concerns about the model's practical applicability and scalability.

### Questions
While has some notable weaknesses, I think this is a very good paper that can open a door to new directions in generative modeling. It is important for me to point to the courage of trying new refreshing approaches (as opposed to building upon current trends). Such papers should always be judged under the understanding that for existing methods, a lot of engineering has taken place and should be thought of as the first GAN paper or the first Diffusion models paper (Sohl-Dickstein 2015).

### Soundness
4

### Presentation
4

### Contribution
4
