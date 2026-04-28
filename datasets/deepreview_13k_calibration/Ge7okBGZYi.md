# How Learnable Grids Recover Fine Detail in Low Dimesions: A Neural Tangent Kernel Analysis of Multigrid Parameteric Encodings

- Decision: Accept
- Avg Score: 5.25
- Scores: 5, 5, 8, 3

## Abstract
Neural networks that map between low dimensional spaces are ubiquitous in
computer graphics and scientific computing; however, in their naive
implementation, they are unable to learn high frequency information. We present
a comprehensive analysis comparing the two most common techniques for mitigating
this spectral bias: Fourier feature encodings (FFE) and multigrid parametric
encodings (MPE). FFEs are seen as the standard for low dimensional mappings, but
MPEs often outperform them and learn representations with higher resolution and
finer detail. FFE's roots in the Fourier transform, make it susceptible to
aliasing if pushed too far, while MPEs, which use a learned grid structure, have
no such limitation. To understand the difference in performance, we use the
neural tangent kernel (NTK) to evaluate these encodings through the lens of an
analogous kernel regression. By finding a lower bound on the smallest eigenvalue
of the NTK, we prove that MPEs improve a network's performance through the
structure of their grid and not their learnable embedding. This mechanism is
fundamentally different from FFEs, which rely solely on their embedding space to
improve performance. Results are empirically validated on a 2D image regression
task using images taken from 100 synonym sets of ImageNet and 3D implicit
surface regression on objects from the Stanford graphics dataset. Using peak
signal-to-noise ratio (PSNR) and multiscale structural similarity (MS-SSIM) to
evaluate how well fine details are learned, we show that the MPE increases the
minimum eigenvalue by 8 orders of magnitude over the baseline and 2 orders of
magnitude over the FFE. The increase in spectrum corresponds to a 15 dB (PSNR) /
0.65 (MS-SSIM) increase over baseline and a 12 dB (PSNR) / 0.33 (MS-SSIM) increase over the
FFE.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The article proposes a multi-grid parametric encoding approach
to capture high-frequency information in images. 
Through a neural tangent kernel analysis angle,
it is proven that the proposed encoding can learn an NTK 
kernel with a higher eigenvalue spectrum than using no encoding. 
The superior performance of this approach is further analyzed 
in detail by separating the contribution from the learnable grid, and 
the embedding space. On the image regression task of ImageNet, 
the proposed encoding ourperforms Fourier feature encodings.

### Strengths
- It is an interesting idea to analyze the impact of different
encoding schemes of a coordinate of an image using the spectrum
in the  NTK framework to make the theory concise. 
- The proposed multi-grid parametric encoding works very well in 
the image regression task.

### Weaknesses
 - The writing of the article should still be improved
for the reviewer to understand the methodology. Please clarify the questions below.
- Conceptually, it is still unclear how the spectrum of the NTK 
is related to the high-frequency information of an image, i.e. 
the large modes of the Fourier transform of a signal X = (x_1,...,x_N) of length N.

- It is unclear in the definition (1), what is the dimension of x,  is it in R^d? 
If so what about the dimension of the output \gamma_F(x), is it 2d x L ? 
- It is not clear what is the notation round + in eq. 3 means.
- eq. 7 is hard to understand. If K_NTK is a matrix of size NxN, would the size 
of Q be also NxN? In this case, why it makes sense to write Q ( f_theta(x,t) - y ) if y is not on dimension N?
- Is there an expectation missing in eq. 9 to define the K_NTK, as in eq. 4?
- The statement of Theorem 1 is not so clear, it would be better to write directly what lambda_i^MPE means as in the proof.
What is the size of the training set X^n in this proof? Isn't it the X in the notation section?

### Questions
- It is unclear in the definition (1), what is the dimension of x,  is it in R^d? 
If so what about the dimension of the output \gamma_F(x), is it 2d x L ? 
- It is not clear what is the notation round + in eq. 3 means.
- eq. 7 is hard to understand. If K_NTK is a matrix of size NxN, would the size 
of Q be also NxN? In this case, why it makes sense to write Q ( f_theta(x,t) - y ) if y is not on dimension N?
- Is there an expectation missing in eq. 9 to define the K_NTK, as in eq. 4?
- The statement of Theorem 1 is not so clear, it would be better to write directly what lambda_i^MPE means as in the proof.
What is the size of the training set X^n in this proof? Isn't it the X in the notation section?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper provides a theoretical and empirical analysis demonstrating that Multigrid Parametric Encodings (MPEs) improve neural network performance in learning fine details and handling discontinuities. By deriving the neural tangent kernel (NTK) for MPEs, the authors show that multigrid encoding elevates the NTK's eigenvalue spectrum compared to coordinate-based MLPs, explaining why MPEs capture detail more effectively. Their analysis isolates this improved performance to MPEs’ learnable grid structure rather than the embedding space alone, a distinction from Fourier Feature Encodings (FFEs). Empirical results on 2D image regression with ImageNet data reveal that MPEs, especially those with smaller grid cells, achieve higher Peak Signal-to-Noise Ratio (PSNR) scores, indicating better detail preservation than both FFE and baseline MLP approaches.

### Strengths
1. The paper has a well-established theory.
2. The paper is well structured.
3. The authors aim to fill the gap in understanding why MPEs improve a network’s performance through the structure of their grid and not their learnable embedding.

### Weaknesses
1. The paper offers limited novelty and applicability. The authors demonstrate that MPEs enhance network performance through grid structure rather than learnable embeddings by analyzing a lower bound on the eigenvalues of the Neural Tangent Kernel (NTK). However, they use well-known methods to address the problem, which limits the work's novelty.
2. Most of the paper is focused on describing the existing theory which is well described in literature.
The evaluation process is insufficient; in my opinion, images from a single dataset (ImageNet) are not enough to thoroughly validate the theory.
3. In Equation (9), derivatives are denoted by a single prime symbol without specifying the parameter with respect to which they were calculated, creating confusion and potential errors in further derivations, which makes the paper difficult to follow. 
4. Furthermore, the analysis focuses primarily on a single-layer MLP network. While the authors state that the theory can be easily extended to deeper networks, they do not provide this extension, even in the appendix. The structure and width of individual layers in finite-width networks introduce variability in the NTK. For example, deeper layers in finite networks may capture complex feature hierarchies, while shallow layers contribute differently to the NTK. This dependency adds analytical challenges, as each layer’s contribution can influence the network’s performance and generalization in unique ways. This is the main reason why the evaluation process should also be conducted on deeper neural networks.

### Questions
1. Can the presented theory be applied to other neural network architectures, such as Convolutional Neural Networks (CNNs)?
2. Do the presented figures show results only for single-layer fully connected neural networks?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper studies how Multi-grid positional encodings affect the spectrum of the Neural Tangent Kernel of coordinates-based MLPs, and show that it forms a provably better encoding (compare to Fourier) to recover high frequency details.

### Strengths
- The paper doesn't make assumptions about what the reader knows or doesn't know and redefines terms and gives clear examples as well as clear expressions for the tools and objects mentioned.
- Isolating the effect of the embedding size and the grid is really important theoretically and practically. I wouldn't necessarily have thought to ask for this analysis, but seeing it in the paper is definitely a strength.
- The work is to the point with a clear theoretical contribution backed by solid experiments.

### Weaknesses
 - nit: in notations, it would be nice to discuss why $d \leq 3$ is important for the theoretical analysis and the limitation.
- nit: in notations, $f_\theta(x)$ is not a function, it's an expression. Same for $\gamma(x)$. Btw, they shouldn't both use $x$ as an input.
- FFE NTK contribution: line 256 says "we derive the kernel for MPEs and FFEs", while line 134 says "Previous analysis of the NTK for coordinate based MLPs has been restricted to FFEs". I think it's really important to clarify what exactly the contribution is when it comes to the NTK of FFE based MLPs. If the latter is what is actually the case, then a reference to this work would be appropriate.
- Use of PSNR: because PSNR is an MSE-based metric, it is actually not really sensitive to fine details. I think using a metric like HFEN or a multiscale-SSIM would make more sense in this context.
- Large-scale realistic experiments: while I do think the current state of the experiments is really solid, for a more impactful work I think larger scale experiments with NeRFs or other SotA models would be beneficial.
- The paper does not discuss the memory overhead of the MPE, which is a significant practical consideration when compared to other encodings like FFE. This is especially important when considering high-resolution or large-scale applications.

### Questions
- in Fig. 1, is $d=2$ dimension of the input in the notations or 3 as suggested by the input of the MLP? Either way it's a bit confusing
- In theorem 1, the result states that the spectrum of NTK of MLP+MPE is uniformly lower bounded by the spectrum of NTK of MLP, could it be possible to quantify given some assumptions how much above it it is? For now we have an empirical answer.
- What's unclear to me after reading this paper is: since there is a consensus in computer graphics that MPE is better + it seems to work so well out-of-the-box in this work, why isn't everyone (typically in scientific ML) using MPE?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
1

### Summary
The authors look at the Multigrid Parametric Encoding through the lens of Neural Tangent Kernel analysis.  They find that MPE have a raised eigenvalue spectrum compared to baseline encodings.

### Strengths
The approach seems straightforward and shows an improvement over the baseline.

I appreciate the theoretical contribution and subsequent evaluation of another approach.

### Weaknesses
I feel like the choice of the grid is not discussed enough.  There is either the choice of having a regularly spaced grid as well as having a learnable one.  There would at least be some intermediate option as well, like having an irregular grid, as it is done in the fast multipole method.  There it has also been observed that using a regular grid leads to unstable results.  Hence, it's not convincing that the grid actually needs to be learnable to be useful, like the authors claim.

The baseline network is not really defined.  After reading through the paper, I am still not sure what you mean by that and how you trained it.

While the analysis performed appears sound, it begs the question of what the take-away message is.  Does MPE always outperform FFE?  Figure 2 is missing the eigenvalue spectrum for FFE.  

As it stands, the examples seem a bit cherry-picked.  It would improve the paper, if the authors could provide an average eigenvalue spectrum for both approaches considered that gives an idea of how it generalizes.

### Questions
If you use non-parametric networks for encoding an image, maybe it would be useful to also include comparisons to classical image compression algorithms and show their signal to noise ratio?

What does Identity correspond to in the plots?

It would be nice to see the actual learned grid superimposed on the image itself.

### Soundness
3

### Presentation
2

### Contribution
2
