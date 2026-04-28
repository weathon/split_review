# Exploring Invariance in Images through One-way Wave Equations

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 8, 6, 3

## Abstract
In this paper, we empirically reveal an invariance over images – images share a set of one-way wave equations with latent speeds. Each image is uniquely associated with a solution to these wave equations, allowing for its reconstruction with high fidelity from an initial condition. We demonstrate it using an intuitive encoder-decoder framework where each image is encoded into its corresponding initial condition (a single vector). Subsequently, the initial condition undergoes a specialized decoder, transforming the one-way wave equations into a first-order norm+linear autoregressive process. This process propagates the initial condition along the x and y directions, generating a high-resolution feature map (up to the image resolution), followed by a few convolutional layers to reconstruct image pixels. The revealed invariance, rooted in the shared wave equations, offers a fresh perspective for comprehending images, establishing a promising avenue for further exploration.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper empirically investigates the invariance of images using wave equations. Interestingly, the paper showes that images share a wave-equations in latent space (Changes is vertical direction of the image is proportional to horizontal direction), where each individual image can be uniquely estimated by initial conditions.

 Initial condition is obtained using an encoder, where it goes through first-order norm+linear autoregressive process to produce a feature map (solutions of the wave equation). The image in pixel space is then  reconstructed using convolutional layer and upsampling layer from the feature map.

### Strengths
+ The proposed idea of the paper is very interesting. 
+ The authors have included numerous experimental results.

### Weaknesses
1. The paper lacks a logical flow, making it challenging to read. While each individual section is well-written, the overall structure makes it difficult for readers to follow a coherent narrative. Here are some specific points:
- **Focus of the Paper**: The title and much of the abstract emphasize "Exploring Invariance," with a focus on demonstrating invariance in images using wave equations. However, the paper appears to focus on FINOLA as the main contribution, focusing on its performance and characteristics. 

- **Purpose and Structure of Sections**: If the primary goal is to demonstrate invariance through FINOLA, then sections on *Parallel Implementation* and *Importance of Norm+Linear* relate more to the efficient training of FINOLA and the utility of norm+linear components. These sections feel tangential to the paper’s message and might be better suited to the experiments section or supplementary material.

- **Rationale for Generalization**: The paper does not completely explain the rationale for generalizing to a set of wave equations (section 3) beyond performance improvements. If enhancing performance is not within the paper's scope, as claimed by the authors, then extra clarification to why we need the generalization  is necessary.

- **Unexplained or Disconnected Claims**: The paper includes unrelated discussions and unexplained claims. For example, in the statement:
  
  > Relaxing the FINOLA constraint through FINOLA series: FINOLA represents a specific solution to Eq. 2,....
  
  there is no justification provided as to why relaxing the constraint would lead to a more optimal solution.


- **Section 5**: The introduction of FINOLA’s application in self-supervised learning is not fully explained. 



2. The paper shares significant overlap with reference [1]. This would be acceptable if the authors explicitly referenced this prior work and clarified how their approach differs, yet there is no mention of it.

  > **[1]** Yinpeng Chen, Xiyang Dai, Dongdong Chen, Mengchen Liu, Lu Yuan, Zicheng Liu, Youzuo Lin, "Image as First-Order Norm+ Linear Autoregression: Unveiling Mathematical Invariance," arXiv 2305.16319.



3. The authors suggest that the invariance property inherent to FINOLA could provide new insights into image analysis. However, the paper lacks a discussion on potential applications of this property or its implications for future research.

### Questions
- **Latent Speeds (Abstract, Line 2)**: What does "latent speeds" refer to in the second line of the abstract?

- **Optimality of FINOLA Solution (Eq. 2)**: Why might the solution of FINOLA in Equation 2 not be the optimal one? Isn’t it supposed to be unique?

- **Definition of $\widehat{\phi}$ (Equation 3)**: What is $\widehat{\phi}$ in Equation 3? If it represents a normalization of $\phi$, how is this performed? Is it similar to the normalization for $z$ in Equation 1?

- **Feature Map Resolution (Line 195)**: Is FINOLA unable to produce a feature map at a resolution of 1/8 of the original image?

- **Data Dependency of Learned A and B**: Are the learned matrices $A$ and $B$ data-dependent? If the test set changes, would the learned $A$ and $B$ no longer be applicable?

### Soundness
3

### Presentation
3

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
The authors have discovered a spatial auto-regression property of natural images in the inner domain of a specific autoencoder also proposed in this work.

The autoencoder is similar in spirit to U-net convolutional autoencoders, with the encoding part based on a previously reported Mobile-Former [Chen et al. CVPR 22]. The main differences of the proposed scheme are: (1) final part of the encoder (the bottleneck of reduced spatial resolution) is compressed to a single vector corresponding to a single spatial location, and (2) the initial decoding layers (instead of upscaling+convolution) are substituted by a process that spatially expands the encoding vector through a differential equation whose coefficients are learnt. After this (original) spatial expansion leading to an intermediate feature representation with low spatial resolution, the decoder consists of the usual (upscaling+convolution) layers.

The discovered property is that the coeffcients of the differential equation that govern the way the information of the encoding vector propagates to different spatial locations is valid for many different natural images. This represents a spatial-autoregression property of natural images (in that specific encoding domain), which is not intuitively illustrated in the work.

### Strengths
* The ablation study is thorough and highlights interesting properties either of natural images or of the encoding domain… or, better said ;-), of that specific signal in that specific domain (natural images in this encoding domain).
Examples of the intriguing properties include: the validity of the matrices of coefficients A and B for may images, the relevance of the variance normalization of the features in the encoding domain, and the meaningful reconstructions obtained from linear combinations in the encoding domain. 

* The comparison with other image autoencoders is extensive and suggest the good properties of the proposed domain is better than linear DCT and Wavelet encoders and nonlinear convolutional autoenc. (for the same number of coefficents or dimensions), and better than JPEG (for the same entropy). 

* Interesting references are given in the related work section. Thanks for those!

### Weaknesses
 * The important problem of this work is that no intuition is given, and all proposals and findings have to be taken as-they-are. If the meaning of the encoding vector is not explained (if it can be explained at all), then, the property found is of no use because one does not know how to understand the (otherwise interesting) constancy of the coefficients of the differential equation. For instance, when one derives classical autoregressive models of the images in the spatial domain, one can interpret the coefficients of these models as autocorrelation functions that describe the (prediction) relations between the luminances at different points of the images. The above sentence can be illustrated both visually and in predictive coders and in conditional probability markov models. However, what is the meaning of things here?. Specifically:

* What is the qualitative meaning of the encoder? (and hence of the encoding vector). Incidentally, this is not very much clear in the original paper on Mobile-Former [Chen et al. CVPR 22]. Can you show receptive fields of the coeficients of the encoding vector?. Can you compare vectors corresponding to different spatial locations?. Do they contain different seeds that are related using the differential equation?
  
* What is the meaning of the matrices A and B?. Can you visualize and interpret them? (this interpretation depends on the previous question). When you diagonalize, and you find the transformed coefficients, what (qualitative) information is transferred in the horizontal and vertical directions?

* You suggest that the normalization of the z features is critical for the wave equation. However, why is relevant the normalization over features?. In which way is this normalization similar or different from other normalization schemes sucha as the usual batch normalization, or the (more interesting) local normalization as in the biological Divisive Normalization [Heeger Science 92, Carandini & Heeger Nature Rev. Neurosci. 12, Malo et al. J.Nonlin.Sci. 24], also used in state-of-the-art end-to-end optimized autoencoders [Ballé et al. ICLR 17] and in the local normalization in Alexnet [Krizhevsky et al. NeurIPS 12]. A possibility is that this normalization captures predictable information [Schwartz & Simoncelli Nat Neurosci. 01, Malo & Laparra Neur. Comp. 10] and hence transforms the (complicated) nonlinear relations into (easier to describe) linear relations, which are more invariant [Hernandez et al. Patt.Rec.Lett.24] and hence, it may make the linear differential formulation possible.

* The comparison of the performance with other autoencoders is illustrative, however, I am curious about how this will compare with more interpretable autoencoders using not only the number of coefficients but the information they contain (i.e. entropy, as in the comparison with JPEG)... what about JPEG2000 [Marcellin Kluwer 02], or end-to-end divisive-normalized optimized linear transforms [Balle et al. ICLR 17].

### Questions
My questions are related to the above mentioned weaknesess

* Can you elaborate on the meaning/interpretation of your result? [I acknowledge this may be difficult to do within the 9 page restriction, but you can do it in the appendices. I would understand the "that is matter for further work" response, but you would understand that the reader may be not satisfied with that response. Understanding is what the reader wants].

* What is the qualitative meaning of the encoder? (see above)
  
* What is the meaning of the matrices A and B? (see above)

* Why is relevant the normalization over features?. Can you show reconstructions -both z and in the image domain- with and without normalization?. Discuss possibly related normalizations in related work.

* Can you compare to other (more interpretable) entropy autoencoders? (see above). Note that the dimension of the representation for unbounded variance/entropy is misleading. I guess the results of your model will be good given the comparison with JPEG.

### Soundness
3

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
The paper presents a novel encoder-decoder architecture for images and uses that architecture to argue for a new insight about natural images. The encoder consists of two stages: (1) an  encoder that produces a single vector q and (2) a linear+normalization autoregressor that converts q into a feature map that is the size of the image (or of smaller sizes). A relatively simple decoder can then reconstruct the original image from the feature map. Extensive experiments compare the psnr of the reconstruction to other methods but the authors point out that their main interest is in " it’s crucial to emphasize that our aim isn’t state-of-the-art performance but to empirically reveal a property inherent in images"

### Strengths
I like the author's goal of focusing on finding new properties of natural images and I find the approach original.

I also find the results intriguing: at first glance it seems as if the network is managing to encode the image without any spatial information. This is because the vector q is placed at a single location, and then all other locations are generated by two fixed matrices A, B which do not depend on the location. Upon further consideration, one can imagine the matrices A and B implicitly encoding a mapping that maps certain coordinates in q to certain locations.

### Weaknesses
At the end of the day, the proposed method is an auto-encoder and there is no inherent reason that this particular architecture for the encoder should be better than any other architecture. Indeed some of the other auto-encoder architectures are shown to outperform FINOLA according to the authors (e.g. stable diffusion in the appendix), and I am not sure what to make of the comparisons: surely the performance of all the architectures is highly dependent on hyperparameters.

Although the authors say that their main goal is to reveal "a property inherent in natural images", they do not say much in the paper about what they have learned from this property or what are the consequences of having such a property (see question below):

### Questions
What do you think your results teach us about natural images? 

How do you think the matrices A and B encode spatial information? Have you examined the learned matrices?

Does your network manage to compress other signals that are not natural images?

Do you think that the autoregressive approach is better than simply reshaping q so that it is a small image (e.g. reshape q which is 2048 into a 16x16x8 feature map)? 

Equation (1) is similar (although not identical) to the power method for finding eigenvectors of (I+A). If you iterate equation (1) many times, does it not forget the initial value of q and converge to some vector that does not depend on q?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors introduce a novel image encoder/decoder architecture, First Order Norm + Linear Autoregression (FINOLA). They compare against several other image representations, such as Discrete Cosine Transform, Discrete Wavelet Transform, several other autoencoders, and find that their method compares favorably. They perform many experiments on this encoder for lots of other applications; such as image inpainting/outpainting, self-supervised learning, and much more. However, their central thesis is situated around two claims: 1) that their latent representations are solutions to one-way wave equations and 2) that their experiments somehow reveal "an invariance over images". I am suspicious of both claims.

### Strengths
Experiments are very thorough, paper looks professional in formatting and presentation. The appendix contains an incredible 10 additional pages of results with 21 tables and 16 figures. Clearly an extensive amount of work has gone into this paper.

### Weaknesses
I am dubious of this paper’s core narrative. I don’t think this paper is about image invariance or one-way wave equations.

First, I don’t think the authors have discovered a meaningful image invariance. As I see it, the authors have devised an autoencoder with an unusual architecture. They claim that, since the autoencoder’s learned parameters are constant across all images, this represents some kind of invariance inherent in images. At best, I think this stretches the definition of invariance. At worst I think it is philosophically confused. The relationship to wave equations feels like an arbitrary constraint on the autoencoder's latent representations. If this characterization is unfair, feel free to debate me on this.

Second, I am also dubious that the FINOLA encodings really are solutions to a 1-way wave equation. Have you empirically checked that equation 1 actually holds for all x and y values in your solution $z(x,y)$, when $z(x,y)$ is constructed as shown in figure 4? Because I suspect this property may not hold, which would then invalidate your discussion about wave equations.

### Questions
Please respond to my criticisms in the weaknesses section. If the authors can persuade me of their core theoretical claims, I will revise my review.

### Soundness
1

### Presentation
3

### Contribution
2
