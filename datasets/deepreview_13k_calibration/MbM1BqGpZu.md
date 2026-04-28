# Diffusion Transformer Captures Spatial-Temporal Dependencies: A Theory for Gaussian Process Data

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 6, 8

## Abstract
Diffusion Transformer, the backbone of Sora for video generation, successfully scales the capacity of diffusion models, pioneering new avenues for high-fidelity sequential data generation. Unlike static data such as images, sequential data consists of consecutive data frames indexed by time, exhibiting rich spatial and temporal dependencies. These dependencies represent the underlying dynamic model and are critical to validate the generated data. In this paper, we make the first theoretical step towards bridging diffusion transformers for capturing spatial-temporal dependencies. Specifically, we establish score approximation and distribution estimation guarantees of diffusion transformers for learning Gaussian process data with covariance functions of various decay patterns. We highlight how the spatial-temporal dependencies are captured and affect learning efficiency. Our study proposes a novel transformer approximation theory, where the transformer acts to unroll an algorithm. We support our theoretical results by numerical experiments, providing strong evidence that spatial-temporal dependencies are captured within attention layers, aligning with our approximation theory.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores transformers as denoisers within diffusion models for generating spatiotemporal data, motivated by recent advancements in video foundation models, such as SORAH.
The approach begins by assuming a Gaussian process as the underlying data distribution and simplifies it to a scale-varying Gaussian process where the covariance changes only in scale over time. In this framework, the score function is related to the inverse of a modified covariance matrix. Since directly calculating this inverse is computationally prohibitive for high-dimensional latent vectors (dimension = d * N), the paper introduces a convex quadratic relaxation solvable via gradient descent. The authors then design a transformer architecture inspired by unrolled gradient descent steps. They also derive sample complexity bounds for the transformer’s ability to learn the covariance based on the smoothness and decay properties of the kernel matrix.
The paper includes basic experiments with synthetic Gaussian process data and a simple ball-motion scenario to validate the proposed method.

### Strengths
- The paper addresses a timely and relevant problem, aiming to understand why spatiotemporal transformers effectively learn distributions in spatiotemporal data.

- The writing is clear, making the methodology and findings accessible.

### Weaknesses
 - The goal of the paper lacks clarity. If the aim is to demonstrate the expressiveness of transformers for correlated or spatiotemporal data, this doesn’t necessarily relate to diffusion models and could be examined independently in a more simplified setting. The current framing makes it unclear whether the core contribution is about diffusion models or transformer expressiveness, and the theoretical analysis seems somewhat disconnected from the practical application of diffusion models.

-The assumption of a Gaussian process with scale-wise stationarity is a strong simplification, limiting the applicability to realistic distributions. This assumption drastically reduces the complexity of the problem, potentially overlooking key challenges in modeling real-world spatiotemporal data. Consequently, the results offer limited insights into transformer design for broader, more complex distributions. The analysis does not address how the proposed method would handle non-Gaussian or non-stationary data, which are common in practical scenarios.

-The experiments are weak and unconvincing. The use of synthetic Gaussian process data and a simple ball-motion scenario does not adequately validate the proposed method. To substantiate the theory, more realistic data should be used, and comparisons with alternative architectures, such as UNet (3D or 2+1D), known for capturing spatiotemporal correlations, would strengthen the argument. The current experiments do not demonstrate the practical advantages of the proposed transformer architecture over existing methods.

### Questions
- In the quadratic formulation in Equation (3), the score function estimation remains non-separable over timesteps (i.e., across x1,t, ..., xN,t). Would further decomposition allow for a distributed solution with minimal inter-timestep communication?

- Prior work, such as [Sahiner et al., 2022], has already shown that attention layers capture correlations and reflect low-rank priors, so it’s unsurprising that attention proves effective for correlated and stationary data.

Sahiner, A., Ergen, T., Ozturkler, B., Pauly, J., Mardani, M., & Pilanci, M. (2022, June). Unraveling attention via convex duality: Analysis and interpretations of vision transformers. In the International Conference on Machine Learning (pp. 19050-19088). PMLR.

### Soundness
2

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
This paper scrutinises diffusion transformers under a simplified setting where the input time series is assumed to follow a Gaussian process. The paper carefully derives the analytical forms of the dynamics and provides score approximation as well as data-distribution estimation guarantees in the simplified setting of interest. The authors cast this paper as a first step towards building more sophisticated theories.

### Strengths
I really like the framing in this paper. While sounding like toy settings, GPs can be quite general and could be a good starting point of analysis. I especially appreciate the analytical forms, for example in the score approximator, and how the covariance function relates to positional embeddings. The paper is also quite well written. I have gone through parts of the proofs and they made sense - although I have not exhaustively verified every step.

### Weaknesses
 - Can we have a section in the appendix where all the assumptions and simplifications are listed? This would really ease the conclusions that the reader can draw from this paper.
- Ln. 397: What's a "properly transformer" architecture? It is unclear what specific architectural constraints are implied by this term, and how it differs from other transformer variants.
- Could the authors give more elaborations on what motivates the choices of $\epsilon$ and $T$ in Thm. 2? The current explanation lacks sufficient detail regarding the practical implications of these choices. For instance, how does the choice of $\epsilon$ affect the trade-off between bias and variance in the score function approximation, and how does $T$ relate to the convergence of the forward diffusion process to a standard Gaussian?
- What about empirically testing the learning on GPLVMs? Wouldn't this be a natural fit? Given the assumption that the data comes from a Gaussian process, it would be valuable to see how the proposed method performs on data generated from a Gaussian Process Latent Variable Model (GPLVM), which is a common approach for modeling high-dimensional data with underlying low-dimensional structure. This would provide a more concrete evaluation of the method's performance in a setting that aligns with the theoretical assumptions.
- There are some duplicate looking sections in the appendix, for example relating to the size of the transformer blocks. Can't we gather those in a big table instead of repeating them after each relevant section?

### Questions
Please see weaknesses.

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
2

### Summary
This paper provides a theoretical study on the limits of the learning capabilities of transformer-based diffusion models on learning spatial-temporal data. The authors achieve this by reformulating the task of learning the score function of Gaussian process data as a gradient descent algorithm. This algorithm can then be unrolled using a transformer archtitecture where the attention layers can be studied to evaluate how spatial-temporal dependencies are learned. 
The results are thoroughly motivated and dervied and validated using a few numerical examples. 
 
I believe that the theoretical results could have an impact in terms of understanding the learning of temporal dependencies but currently the practical results are not extensive and the take away messages are not clear enough

### Strengths
- studying gaussian processes to asses spatio-temporal dependencies is inherently reasonable and could be used as an important theoretical framework to study neural architectures.

- The method mathematically is well grounded and derived

- High-quality figures visualizing key components of the contribution

### Weaknesses
 - While the results convincingly show that transformers can learn spatial-temporal dependencies, the experiments only show examples of properly learned tasks. Given that theoretical boundaries were derived, I would have loved more experiments investigating these limits. For example something like Figure 1 but with a degradation for higher length. The same goes for Section 6.2. What I am missing is a clear connection between model complexity and performance.

- Lack of comparison to other methods: I think it would be helpful to see how typical diffusion models, including Unet-based architectures, perform on the task of learning Gaussian processes. Clear results could help in shifting the design towards transformer-based diffusion architectures.

- Generalization to real-world problems: There are no experiments showing how well the insights generated by the experiments translate to real-world problems. You present the ball experiment but even there you have to consider how well your experiments align with the assumption of using Gaussian process data (cmp. l. 504-506). Real-world problems will often not follow Gaussian process dynamics

- It would be nice if you could state some take-home messages for the reading. Ideally some general information such as design choices for the model architecture.

- The learned temporal dependencies presented in Figure 5 look very similar to what you get when you just plot the attention between two uncorrelated matrices with positional embedding (l. 300). What is the difference between these maps and the ones you present, e.g., in Fig. 5

### Questions
- The learned temporal dependencies presented in Figure 5 look very similar to what you get when you just plot the attention between two uncorrelated matrices with positional embedding (l. 300). What is the difference between these maps and the ones you present, e.g., in Fig. 5

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, authors explore the reasons for Diffusion Transformer (DiT)’s capability of capturing spatial-temporal dependencies within the sequential data. They theoretically establish score approximation and distribution estimation guarantee of DiT for learning Gaussian process data. Specifically, they replace the score function in diffusion models with gradient descent process defined by truncated covariance, which are further implemented with transformer models. Authors conduct some experiments to prove the effectiveness of their theory under their assumptions.

### Strengths
1. This paper studies the principle behind the Diffusion Transformer and provides a theoretical explanation of its capability of modeling spatial-temporal correlations within data, which is the very first trial in related fields. 
2. Authors propose a novel score function approximation theory as well as the sample complexity bound. All the lemmas and theorems are well defined with sufficient mathematical proofs. 
3. The correctness of the proposed theory has been evaluated on both synthesized and real data through experiments.

### Weaknesses
1. Although the overall writing is relatively clear, there’re some suggestions:
1.a) The object of this paper is sequential data, which has the axis of time (real world time, $h$). while in the diffusion process, there’s another axis of diffusion step ($t$), and authors also name it as ‘time’. To avoid confusion, authors should use some other descriptions to make it clearer. For instance, consistently using "diffusion step" for $t$ and reserving "time" for the temporal axis $h$ of the sequential data would improve clarity. 
1.b) The symbols should be consistent. E.g., the definitions of $v_t$, $\mathcal{D}$ and $v_0^t$, the use of subscripts of data $\mathbf{x}$ are confusing. Specifically, the notation $v_t$ could be easily confused with the velocity at time $t$ in other contexts. A more descriptive notation, such as $v(t)$ or $v_{diffusion}(t)$, might be clearer. The relationship between $\mathcal{D}$ and the data distribution $p(\mathbf{x})$ should be explicitly defined in the preliminaries. The notation $v_0^t$ is also not immediately clear and requires a more thorough explanation when first introduced. Finally, the use of subscripts for data $\mathbf{x}$ is inconsistent. Sometimes it denotes different data points, and at other times, it denotes different dimensions of the same data point. A unified notation, such as $\mathbf{x}^{(i)}$ for the $i$-th data point and $x_j$ for the $j$-th dimension, would be beneficial.
1.c) The font size of Figures could be larger, e.g. Fig.2, otherwise the equations and words are difficult to recognize under normal physical paper size.   
2. Although the effectiveness of the theory has been proved on synthesized Gaussian process data and semi-synthetic video data. More real data with complex contents should also be tested on. Specifically, testing on datasets with non-stationary patterns or datasets with abrupt changes in dynamics would provide a more comprehensive evaluation of the proposed theory's applicability.

### Questions
1. The theorems proposed in the paper are based on the authors’ assumptions, then:
1.a) Does it mean that the theory is only valid under these assumptions, or does the model only work on the data satisfying these assumptions? 
1.b) How to ensure that the assumptions can represent the case in real sequential data? 
1.c) How do authors derive these assumptions? E.g., in Assumption 1, why the definition of the covariance function has that formula, are there any theoretical basis for it?

### Soundness
3

### Presentation
3

### Contribution
4
