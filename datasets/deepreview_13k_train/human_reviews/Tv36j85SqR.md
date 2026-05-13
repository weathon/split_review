# Approaching Rate-Distortion Limits in Neural Compression with Lattice Transform Coding

- Decision: Accept
- Scores: 8, 8, 6, 8, 6

## Abstract
Neural compression has brought tremendous progress in designing lossy compressors with good rate-distortion (RD) performance at low complexity. Thus far, neural compression design involves transforming the source to a latent vector, which is then rounded to integers and entropy coded. While this approach has been shown to be optimal in a one-shot sense on certain sources, we show that it is highly sub-optimal on i.i.d.~sequences, and in fact always recovers scalar quantization of the original source sequence. We demonstrate that the sub-optimality is due to the choice of quantization scheme in the latent space, and not the transform design. By employing lattice quantization instead of scalar quantization in the latent space, we demonstrate that Lattice Transform Coding (LTC) is able to recover optimal vector quantization at various dimensions and approach the asymptotically-achievable rate-distortion function at reasonable complexity. On general vector sources, LTC improves upon standard neural compressors in one-shot coding performance. LTC also enables neural compressors that perform block coding on i.i.d.~vector sources, which yields coding gain over optimal one-shot coding.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes lattice transform coding (LTC), which uses lattice quantization beyond the conventional scalar quantization in neural lossy compression. The paper offers evidence that learned transforms in conventional nonlinear transform coding (NTC) are insufficient in overcoming sub-optimal quantization in the latent space, and shows that LTC with more efficient space-filling lattices indeed bring improvements in R-D performance. Besides new training and rate estimation techniques for LTC, the paper also proposes nested LTC to lower the practical computation cost of entropy coding, as well as block LTC to perform block coding in order to close the gap to the information-theoretic optimal performance (R(D)). 
Experiments on various synthetic and real-world data sources support the effectiveness of the proposed LTC approach and give insight to the suboptimality of current NTC approaches.

### Strengths
I consider the originality of the paper to be moderately high. Although the ideas of lattice coding, nested quantization, block coding, etc. have been known for a while, and lattice coding itself even explored in the contemporary work of Kudo et al. (2023), this paper brings these ideas together and gives novel insights for the performance gap between the current NTC methods and the theoretical optimum of R(D). 

The paper is well-written and mostly easy to follow (although see issues below), with insightful explanations and experiments. 

I consider the contribution of this paper timely and significant. Unlike much of current research on NTC which is in architectural / entropy modeling improvements, this paper examines a fundamentally different component of NTC and makes a compelling case of the advantage of lattice quantization over scalar quantization.  Achieving the theoretical advantage of block coding / VQ has been a non-trivial goal of lossy compression, and this paper offers valuable perspectives and a potential path forward.

### Weaknesses
1. A significant difficulty of lattice coding seems to be the complexity of implementing entropy coding. Nested lattice quantization was proposed but appears to come with a significant penalty to R-D performance. Therefore most of the R-D curves for LTC in this paper are theoretical. It remains unclear how to practically achieve the reported R-D performance, particularly how to derive a discrete entropy model from the normalizing flow prior that can be used by both encoder and decoder. The paper does not sufficiently address the practical challenges of implementing the proposed lattice quantization, such as how to ensure that the decoder can reproduce the same likelihood values as the encoder, given the continuous nature of the normalizing flow prior and the discrete nature of the lattice codebook.

2. Some of the the explanations around nested LQ and block LQ were a bit hard to follow. For example, the first two sentences on lines 334 - 335 seemed to come out of nowhere ( "The goal is for the majority of the latent mass to be placed in the Voronoi region of Λc. This happens when QΛc (yf ) = 0."). It's not clear why forcing the majority of the mass into the Voronoi region of the coarse lattice is beneficial for compression, and how this relates to the overall goal of nested quantization. Similarly, line 375 introduces a new pair of "analysis/synthesis transforms of LTC", denoted $c_a^{(i)}, c_s^{(i)}$ --- why are they necessary, given that we have already operate in the transformed space using $g_a, g_s$? And how should we choose  $c_a^{(i)}, c_s^{(i)}$ if they are indeed necessary? The explanation lacks sufficient detail on the motivation and implementation of these transforms. Also, a minor typographical error: there seems to be inconsistency between "n" and "d": line 368 explains "Note that we we retain n as the block-length parameter, but use d as the dimension of x." So should line 458 write "d = 16 and 32"?

### Questions
1. I'm confused by how LQ is applied when the source dimension does not equal the lattice dimension. It seems the lattice dimension used in this paper only goes up to 24, but the source dimension can be 33 (Speech) or even higher (Kodak). Is it based on some kind of product lattice then?


2. Related to above, in the block LTC scheme (Sec 4.3), what is the motivation for grouping columns of the transform coefficients matrix into length-n blocks? Given that the data $x$ and the resulting latent tensor $y$ is often high dimensional, can we do block coding on length-n blocks of $y$ in some other ways? I would expect more gains if the entries in each block are **not** i.i.d.

3. Any idea why the R-D performance is sometimes worse when a bigger latent space ($d_y$) is used, all else being equal (e.g., the $d_y=4$ curve is worse than $d_y=2$ at low rates in the Physics Figure 7)? The usual observation in NTC is that the R-D performance can be improved by increasing the latent dimensionality when the latter is too small (esp. towards the low distortion regime), but further increasing the latent dimensionality beyond a sufficient capacity generally does not harm the R-D performance.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper covers the application of lattice vector quantization to neural lossy compression.

The problem of how to address the suboptimality of scalar quantization for lossy compression has been studied for decades, and even today most practical methods use scalar quantization, and instead rely on other techniques to improve compression.

One important difference is that conventional methods normally rely on linear transform, nonadaptive methods, while this paper novelty is that it studies neural compression that uses nonlinear learned transformations. Numerical experiments demonstrate better compression results.

### Strengths
The authors correctly provide good evidence that the suboptimality of scalar quantization remains even with learned neural transformations.
Showing it on toy problems helps to make it clearer, but is not good at indicating how much worse on practical cases. 

The paper presents examples of application to other data, and a series of experimental tests are used to answer those question on those data sources.

### Weaknesses
The experiments are well planned with good comparisons, but somewhat limited. Maybe too much space is used to cover the synthetic cases, and could be better used with real practical data.

It would also be better to have more detailed analysis of the results in those cases. Comments like “…with the Leech significantly outperforming VTM and NVTC,” are too vague and not accurate.

It looks like there are good gains with the modifications to the Cheng2020 method, which may be the most important conclusion of the paper, and that should be more carefully reported.

### Questions
It would be interesting to see more information about the practical aspects of using lattice quantizers during training and for actual coding.

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
4

### Summary
1. This submission extends scalar-quantized non-linear transform coding of signals (Ballé et al., 2020) using lattice quantization and coding. A classical result from signal compression is that vector quantization can provide packing gains over scalar quantization especially when applied directly on correlated (i.e. non-decorrelated) signals, at the cost of higher encoding complexity. The authors propose to overcome the complexity of vector quantization using lattice quantization, which can be considered a constrained form of vector quantization. Experiments (on images and speech) were conducted to measure the gain from lattice quantization over the scalar quantization baseline.

### Strengths
1. The submission's attempt at marrying nonlinear transform coding (NTC) with lattice quantization (LQ) as a way of sidestepping computationally expensive vector quantization is highly relevant to the learned compression research community.

### Weaknesses
1. The fact that integer quantization of latent variables of NTC does not induce hexagonal quantization cells in the source domain—this is not a surprising or unexpected result, as non-linear transforms still define continuous / diffeomorphic mappings between the two domains. A transform that maps squares (scalar quantization cells in the latent domain) to hexagons (vector quantization cells in the source domain) would be highly discontinuous around cell boundaries, not a mapping that is readily learned by a neural transform in the first place. This point could be strengthened by explicitly stating that the learned transforms are typically designed to be smooth and invertible, which inherently limits their ability to create such discontinuous mappings required for optimal vector quantization boundaries.
2. Eq. (1) is central to this work, yet, no description of the Lagrange multiplier / rate–distortion tradeoff $\lambda$ appears in the manuscript. Wouldn't the choice of $\lambda$ have an impact on the characteristics/performance of the learned non-linear transform? Was an effort made to reparameterize $\lambda$ as in the work of Ballé et al. (2020)? Discussion around this is lacking in the current version of the manuscript. The absence of a clear explanation regarding how $\lambda$ is chosen and its effect on the training process makes it difficult to assess the validity of the experimental results. Specifically, it is unclear if the same $\lambda$ is used across different models and datasets, and if not, how these values were selected.
3. LTC (of latent variables) inducing near-hexagonal quantization cells in the source domain (in the 2D case) seems to be due more to the diffeomorphic / continuous nature of the learned non-linear transform itself. This would mean that one could take the non-linear transform of Ballé et al. (2020) and lattice-quantize the latent variables post-hoc, and achieve similar results to what this work is proposing. The benefits of incorporating the actual lattice structure in the rate term of the optimization should be discussed. The paper should provide a more thorough analysis of whether the lattice structure is actually being leveraged during training, or if the performance gains are solely due to the properties of the learned transforms.
4. Experimental results fail to clearly demonstrate the advantage of LQ over SQ. Could this be an optimization issue? For example, was $\lambda$ was fixed to some value to hurt the performance of the non-linear transform itself? The lack of a clear performance benefit raises concerns about the practical utility of the proposed method. It is essential to provide a more in-depth analysis of the experimental setup and results to justify the claims made in the paper.


------- 
4. The current presentation seems somewhat unbalanced, with the authors' actual work only starting on page 6. While this is not inherently a weakness per se, this does mean that the authors were perhaps not able to fully explore / describe the actual contributions of their work in the remaining 4–5 pages.

### Questions
1. Clarification surrounding the choice of hyperparameter $\lambda$ discussed in "Weaknesses" would be appreciated.
2. Experimental results: LTC performs worse than NTC at extremely low bit rates. This is surprising since the benefits of vector/lattice quantization should be more pronounced at such rates.

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
The authors show the suboptimality of existing neural compression models for simple multidimensional sources, such as 2-D Gaussians. They point out that the scalar quantization used in current neural compression models can lead to the suboptimality. They then propose a solution, *i.e.*, lattice transform coding, with lattice quantization in latent space. Extensive experiments verify the superiority of the proposed lattice transform coding.

### Strengths
1. The idea of using lattice quantization in neural compression has potential whose benefits cannot be achieved by improving transforms and the entropy model.
2. The theoretical analysis and experimental evaluation presented in this paper are convincing. The authors have carried out extensive experiments on both synthetic sources and on higher dimensional real sources.
3. The paper is well written and easy to follow.

### Weaknesses
1. The real-world application of the proposed Lattice Transform Coding (LTC) may be limited by the computational complexity of training and inference.

   - *On training.* The authors show that training an LTC model per rate point for image compression takes about 10 days. By comparison, training of nonlinear transform coding (NTC) models can be reduced by fine-tuning the lower rate model from a pre-trained higher rate model. I'm not sure if such tricks can also speed up the training process of LTC. It's unclear if the lattice quantization approach allows for similar transfer learning or if each rate point requires a full training cycle from scratch. This could be a significant barrier to practical adoption.
   - *On inference.* The authors provide a comparison of the NTC method (Cheng2020-NTC) with the proposed LTC method (Cheng2020-LTC-E8), which shows that the computational complexity of LTC is comparable to NTC. However, Cheng2020-NTC is a nonlinear transform coding method using spatial auto-regression in entropy modeling, which is notoriously time consuming. The method is further refined in subsequent work, such as wavefront coding, checkerboard context, and channel-wise auto-regression. Notably, the proposed lattice transform coding can be even more computationally expensive than spatial auto-regression, especially when considering the high dimensionality of lattices like the Leech lattice. The paper does not provide a detailed analysis of the computational cost of the CVP solver, which is crucial for understanding the practical limitations of the proposed method. This lack of analysis makes it difficult to assess the true computational overhead of LTC compared to state-of-the-art NTC methods with efficient entropy models. This can be a fatal flaw in applications.

2. Typos:

   - Line 470. The citation of Vimeo-90k should be realized by a `\citep` command instead of `\citet`.
   - Line 472. The citation of CompressAI is not included in the reference.

### Questions
1. Is it possible to further reduce the computational complexity of LTC models for training and inference? Authors can try the following things to reduce concern.
   - Provide more detailed computational complexity analysis, comparing LTC to state-of-the-art NTC methods beyond just Cheng2020-NTC.
   - Discuss potential approaches to reduce training and inference time for LTC, such as whether fine-tuning techniques used for NTC could be adapted.
   - Comment on how the complexity of LTC scales with different lattice dimensions and source dimensionality.
   - Address whether there are any trade-offs between computational complexity and rate-distortion performance for LTC.
2. Figure 5 does not show the learned lattice of LTC in the regions of lower probability density. How does LTC perform in these regions? Please provide visualizations or quantitative analysis of LTC's performance in lower probability density regions, and discuss any potential implications for overall compression performance.
3. LTC provides a construction on the quantization that is quite different from previous work. Then, how do the nonlinear transforms affect the rate-distortion performance of the LTC models? Please provide an ablation study or analysis that isolates the effects of the nonlinear transforms on LTC's rate-distortion performance.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper highlights the limitations of scalar quantization in neural compression and introduces lattice transform coding as a solution. Given the challenges in rate estimation within this approach, the authors propose a Monte Carlo-based method to address it. To manage complexity, they further introduce a nested lattice structure. Experimental results are presented using both synthetic datasets and real-world datasets, including speech and the Kodak image dataset.

### Strengths
The observation that neural transforms alone cannot overcome scalar quantization limitations is a valuable insight.
The use of dithered noise and Monte Carlo estimation for rate estimation is also noteworthy.

### Weaknesses
 - The presentation could be improved for clarity. All figures are too small, and Section 3 (on the suboptimality of scalar quantization) would benefit from additional detail beyond the currently limited Figure 2. 
- Additionally, the distinction in block LTC needs clarification.
- Lattice coding encoding complexity remains an issue (except for $n=24$). More specifics on how this scheme was applied to the Kodak image dataset would be helpful.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
