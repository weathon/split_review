# Do WGANs succeed because they minimize the Wasserstein Distance? Lessons from Discrete Generators

- Decision: Accept
- Scores: 6, 1, 6, 6

## Abstract
Since WGANs were first introduced, there has been considerable debate whether their success in generating realistic images can be attributed to minimizing the Wasserstein distance between the distribution of  generated images and the training distribution. In this paper we present theoretical and experimental results that show that successful WGANs {\em do} minimize the Wasserstein distance but the form of the distance that is minimized depends highly on the discriminator architecture and its inductive biases. Specifically, we show that when the discriminator is convolutional,  WGANs minimize the Wasserstein distance between {\em patches} in the generated images and the training images,  not the Wasserstein distance between images.
Our results are obtained by considering {\em discrete} generators for which the Wasserstein distance between the generator distribution and the training distribution can be computed exactly and the minimum can be characterized analytically.   We present experimental results with discrete GANs that generate  realistic fake images (comparable in quality to their continuous counterparts) and present evidence that they are minimizing the Wasserstein distance between real and fake patches and not the distance between  real and fake images.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents theoretical and experimental results demonstrating that WGAN actually minimizes the Wasserstein distance (W1), though this depends on the architecture of the discriminator. Using a convolutional discriminator as an example, the paper shows that the W1 distance is minimized over batches rather than individual images.

Specifically, the authors begin with a discrete GAN, where the latent vector z is uniformly sampled from M fixed noise vectors, using this setup as a tool to investigate the Wasserstein distance, as it allows for a more exact computation of the W1 distance. They introduce an iterative algorithm, OTmeans, to compute the W1 distance, serving as a baseline for investigating W1 distance minimization in WGAN. Using this tool, the authors present two main findings in the paper:

Finding 1: Using a 2D discrete GAN to motivate the theorem, the authors observe that when M≥N (where M is the number of noise samples and N is the number of training samples), the discrete GAN reproduces the training examples. Otherwise, it generates outputs as linear combinations of the training examples. They also study cases with images where M=64<N=1000, resulting in blurry images that look similar between WGAN and the OTMeans algorithm. When M=N, there are copied training example.

Finding 2: The authors design two discriminator architectures to demonstrate that optimizes the W1 distance over batches with the convolutional discriminator. The first architecture is a standard convolutional model with convolutional layers followed by a fully connected (FC) layer that operates on batches. The second architecture inserts Global Average Pooling (GAP) between the convolutional layers and the FC layer, making it act on entire images. This setup is then compared with the OTMeans approach on images, where OTMeans uses SGD and Sliced Wasserstein Distance (SWD) to make computations tractable. The authors show that the CNN with GAP behaves similarly to global patch W1, while the other approach resembles local patch W1 distances. They also provide evidence from histograms that demonstrate how GANs learn local patch statistics similar to those in the training set.

### Strengths
This is an important finding that sheds light on how WGANs learn, making a valuable contribution to the GAN research community. Overall, it is a well-written paper with interesting results.

### Weaknesses
The experiments are limited to simple CNN architectures, and there is no exploration of regularization techniques to enforce the Lipschitz constraint, which might behave differently depending on the hyperparameters used.

I have a few questions and also some suggestions for further experimenents:

1. Regarding the case where M=N, do all generated examples match the data examples, or are only a few of them exact matches by chance? And what GANs might behave when M>N or M>>N, e.g., do it generate by copying one training sample for more than different fixed noise inputs? Could the authors please provide quantitative results on the percentage of exact matches when M=N and test and report results for cases where M>N and M>>N? 

2. WGAN’s learning behavior might also depend on the ratio of M and N. The GANs bahavior could be smoother than just for the concrete cases of M<N, N=N and M>N. Do the authors have any deeper analysis on this aspect? One way to investigate e.g., could the authors conduct experiments with a range of M/N ratios and plot key metrics (e.g., FID score, exact match percentage) as a function of this ratio to visualize if any smooth transitions in behavior.

3. The study is based on a small CNN with two configurations: CNN-GAP and CNN-FC. Is it not clear what method is used to regularize the Lipschitz constraint while training these models. The results might vary considerably depending on the regularization strength and hyperparameters used. If strong regularization were applied, the results could be quite different. Could the authors explicitly provide details of the Lipschitz constraint regularization method used, also the hyperparameters, and conduct an ablation study showing how different regularization strengths affect the results.

4. The study focuses on the W1 distance but DCGAN used in some studies, which also shows similar patch-local distribution behavior. Does this suggest that GANs learn on batches when the discriminator is convolutional, regardless of the GAN loss function used? I’m curious why the authors didn’t use WGAN-GP, given that the study is about the W1 distance. Could the authors include experiments with WGAN-GP for direct comparison, and if possible extending the analysis to other GAN variants to test the generality of the findings across different loss functions?

5. What are Direct_Patch_SWD vs. Direct_LocalPatch_SWD? Can the authors explain how SWD is computed for Direct_Patch_SWD vs. Direct_LocalPatch_SWD?

6. Can the authors explain how to histograms on patches in experiments are generated?

7. Are the generators identical across the two convolutional designs? What was the architecture of the generator used? Could the authors include the details of architectures used in the studies?

### Questions
I have a few questions and also some suggestions for further experimenents:

1. Regarding the case where M=N, do all generated examples match the data examples, or are only a few of them exact matches by chance? And what GANs might behave when M>N or M>>N, e.g., do it generate by copying one training sample for more than different fixed noise inputs? Could the authors please provide quantitative results on the percentage of exact matches when M=N and test and report results for cases where M>N and M>>N? 

2. WGAN’s learning behavior might also depend on the ratio of M and N. The GANs bahavior could be smoother than just for the concrete cases of M<N, N=N and M>N. Do the authors have any deeper analysis on this aspect? One way to investigate e.g., could the authors conduct experiments with a range of M/N ratios and plot key metrics (e.g., FID score, exact match percentage) as a function of this ratio to visualize if any smooth transitions in behavior.

3. The study is based on a small CNN with two configurations: CNN-GAP and CNN-FC. Is it not clear what method is used to regularize the Lipschitz constraint while training these models. The results might vary considerably depending on the regularization strength and hyperparameters used. If strong regularization were applied, the results could be quite different. Could the authors explicitly provide details of the Lipschitz constraint regularization method used, also the hyperparameters, and conduct an ablation study showing how different regularization strengths affect the results.

4. The study focuses on the W1 distance but DCGAN used in some studies, which also shows similar patch-local distribution behavior. Does this suggest that GANs learn on batches when the discriminator is convolutional, regardless of the GAN loss function used? I’m curious why the authors didn’t use WGAN-GP, given that the study is about the W1 distance. Could the authors include experiments with WGAN-GP for direct comparison, and if possible extending the analysis to other GAN variants to test the generality of the findings across different loss functions?

5. What are Direct_Patch_SWD vs. Direct_LocalPatch_SWD? Can the authors explain how SWD is computed for Direct_Patch_SWD vs. Direct_LocalPatch_SWD?

6. Can the authors explain how to histograms on patches in experiments are generated?

7. Are the generators identical across the two convolutional designs? What was the architecture of the generator used? Could the authors include the details of architectures used in the studies?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper tries to prove that when the discriminator is convolutional, WGANs minimize the Wasserstein distance between patches in the generated images and the training images, not the Wasserstein distance between images. Yet no solid proof is provided.

### Strengths
The motivation seems to be good.

### Weaknesses
 - The symbols used in the paper is chaos, what's $x$, is it the input of the generator or its output?
- The paper is generally not well organized and hard to follow. 
- The proofs are not rigorously proven. For example, in theory 3.2, how to justify the so called $N/M$? It is wrong, for example, $M=3, N=5$, while one $x_i$ and $y_j$ overlaps to each other. To prove the theorem, I think the discrete metric need to be introduced.
- The paper claims to prove that WGANs with convolutional discriminators minimize the Wasserstein distance between image patches, but the theoretical arguments are weak and lack sufficient detail. The connection between the discriminator's convolutional structure and the patch-based Wasserstein distance is not clearly established. The paper does not provide a rigorous mathematical framework to support this claim, relying on intuitive arguments rather than formal proofs.
- The use of $N/M$ in the context of overlapping patches is particularly problematic. The authors do not account for the fact that patches can overlap, which invalidates the assumption that the number of patches is simply $N/M$. This oversight undermines the validity of the theoretical results. The paper also fails to adequately define the patch extraction process, leading to ambiguity in the analysis.

### Questions
- Please see above.
- The paper seems unfinished since there are empty sections in the appendix.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The Wasserstein GAN (WGAN) is a generative model that attempts to minimize the Wasserstein distance between the distribution of generated samples and the distribution of the training data. Several papers have pointed out that successful WGANs don't seem to minimize the Wasserstein distance. These papers further claimed that this is actually a good thing, as minimizing the Wasserstein distance would lead to blurry generated images.
This paper presents more rigorous experiments that support the conclusion from previous works. This is done by training discrete WGANs - models that are constrained to generate one out of M images - which allows to precisely compute the Wasserstein distance between the distribution of the GAN outputs and the empirical distribution of the training set.
A key observation in the paper is that when the discriminator is a convolutional network, WGANs minimize the Wasserstein distance between the distribution of patches of generated images and the distribution of patches of the training images. This is while when the discriminator is fully connected, WGANs do minimize the Wasserstein distance over whole images.

### Strengths
- The systematic analysis using discrete distributions is clever and makes a lot of sense.

- The theoretical characterization of the solution minimizing the Wasserstein distance in the the discrete case is nice.

- The paper does a pretty good job of empirically demonstrating the main claim, which is that WGANs with convolutional discriminators don't minimize the Wasserstein distance between distributions of whole images, but rather between distributions of patches.

- The paper is well written. Arguments are easy to follow.

### Weaknesses
 - The main takeaway message that the paper highlights is the fact that WGANs with convolutional discriminators minimize the Wasserstein distance between patch distributions. The paper doesn't provide sufficient context and discussion about why this observation is novel. As stated in the paper, Isola et al. (2017) called GANs with a convolutional discriminator "patch GANs", suggesting they minimize distances between patch distributions. This was also explicitly stated by Rott-Shaham et al. (2019). In fact, the origins of these GANs can be traced back to [1] which called them "Markovian GANs", and to [2,3] which called them "spatial GANs". The latter two papers explicitly expressed the loss as a sum of GAN losses over patches of the size of the receptive field, which implies that these GANs attempt to minimize distances between patch distributions and not whole images. From that standpoint it could seem to the readers that this fact is well known and also that it is not unique to WGANs, but rather applies to any GAN. Nevertheless, I believe that this might not be a material weakness, but rather a weakness in the exposition in the paper (see Questions section below).

- The topic is not timely. The popularity of GANs has constantly decreased over the last few years, as diffusion models gained popularity. I consider this to be a minor weakness but I do believe that it affects the potential impact of the paper.

### Questions
Regarding the first weakness stated above, I would be happy to hear the authors' thoughts about the following. As opposed to [2,3], which explicitly attempt to minimize a loss that is the sum of GAN losses over patches, standard GAN training applies the GAN loss after the pooling in the discriminator. In that case, the loss can be expressed as a sum of GAN losses over patches (i.e. swapped with the pooling operation) only if the loss is linear. This is the case for WGANs but not for other types of GANs. Therefore, other types of GANs with a convolutional discriminator don't directly minimize distances between patch distributions. This is while WGANs do. Is that correct?

If this statement is correct, then the paper would benefit a lot from emphasizing and discussing it. Otherwise, as stated above, it seems that the main claim in the paper is well known and not specific to WGANs (namely, it seems that all types of GANs with a convolutional discriminator minimize distances between patch distributions).

### Soundness
4

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
4

### Summary
In this paper, the authors propose a framework to analyzing Wasserstein GANs, and in particular, understanding if the model truly minimizes the W1 loss while training. The insights derived help explain the visual quality of the images generated by certain GAN architectures, and also pave the way for similar analysis of other GAN variants.

### Strengths
- The presentation of the paper is good and the writing is easy to follow
- The overall results derived make sense, and correlate well with the observed performance of existing patchGAN and DCGAN-style architectures. 
- The theoretical formulation is sound, to the best of my reading. The results also make intuitive sense. 
- I am also able to corroborate when I read, with the empirical evidence I’ve seen while training GANs, which, in my view, suggests that the paper succeeds at what it does

### Weaknesses
 - While the analysis carried out is good, I do find it to be somewhat lacking in breadth. It might be good to see how this theory could be applied outside of the Lipschitz-constraint-based W1 loss. For example, could one draw insights into the various gradient regularization strategies that people have used to approximate W1 (i.e., the Sobolev spaces). E.g., [1,2,3] (just to name a few), where we observe very similar artifacting to the ones derived and analyzed in this paper. Would analyzing such other discriminator architectures/losses yield a more holistic view of the space of WGANs?

- The ablation concerning the Convolutional GANs seemed lacking. Given such a strong correlation between the receptive field of the convolution layers and the patch-based W1 minimization, some insights into how we control or interpret this value would be useful for future design. While I understand from Section 5 that estimating S is not practical for DCGAN-style architectures, maybe toy experiments involving a single convolution layer might show links between the filter size of the convolution and S. 

- There have many other works that propose and analyze well-defined loss function that allow one to monitor learning algorithms and check for their convergence (See [4,5,6]). It might be worth discussing such approaches too in the related works. 

- Overall, I still feel that the insights developed by this paper outweigh the weaknesses mentioned, and some of them, such as generalizing to other losses could be discussed now, but more thoroughly explored in future works. I am therefore inclined towards an accept. 

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
