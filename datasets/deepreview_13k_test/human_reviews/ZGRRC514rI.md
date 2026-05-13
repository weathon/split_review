# DeFoG: Defogging Discrete Flow Matching for Graph Generation

- Decision: Reject
- Scores: 5, 6, 6, 3

## Abstract
\looseness=-1


Graph generation is fundamental in diverse scientific applications, due to its ability to reveal the underlying distribution of complex data, and eventually generate new, realistic data points.
Despite the success of diffusion models in this domain, those face limitations in sampling efficiency and flexibility, stemming from the tight coupling between the training and sampling stages.
To address this, we propose DeFoG, a novel framework using discrete flow matching for graph generation. DeFoG employs a flow-based approach that features an efficient linear interpolation noising process and a flexible denoising process based on a continuous-time Markov chain formulation.
We leverage an expressive graph transformer and ensure desirable node permutation properties to respect graph symmetry.
Crucially, our framework enables a disentangled design of the training and sampling stages, enabling more effective and efficient optimization of model performance.
We navigate this design space by introducing several algorithmic improvements that boost the model performance, consistently surpassing existing diffusion models.
We also theoretically demonstrate that, for general discrete data, discrete flow models can faithfully replicate the ground truth distribution -  a result that naturally extends to graph data and reinforces DeFoG's foundations.
Extensive experiments show that DeFoG achieves state-of-the-art results on synthetic and molecular datasets, improving both training and sampling efficiency over diffusion models, and excels in conditional generation on a digital pathology dataset.
\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a discrete flow matching framework for graph generation. Based on the existing discrete flow matching, the authors propose several techniques regarding the model architecture, the training process, and the sampling process. Specifically, 

**Model Architecture**
- To enhance the model expressivity, the authors adopt the Relative Random Walk Probabilities (RRWP) from the previous work [1] to encode the graphs more informatively.

**Training Process**
- The authors show that the marginal distribution is beneficial for discrete flow matching, adopting it from the previous discrete denoising diffusion model for graph generation [2].
- Instead of directly using the time $t$ sampled from a uniform distribution, the authors explore various methods for distorting the sampled time inspired by the previous work for image generation [3].

**Sampling Process**
- This work proposes distortion functions that vary the step size of the sampling process which is effective in yielding performance improvement.
- The authors introduce a guidance term to ensure the robustness when sampling.
- DeFoG introduces a hyperparameter ($\eta$) that can control the stochasticity of the generative process.
- The authors explore the exact computation of the expectation to guarantee the validity of the generated graphs by reducing unintended stochasticity.

Experimentally, the proposed DeFoG is evaluated on the synthetic graph generation, and molecular graph generation, which show comparable performances.


[1] Ma et al., "Graph inductive biases in transformers without message passing.", ICML 2023.

[2] Vignac et al., "DiGress: Discrete Denoising diffusion for graph generation", ICLR 2023.

[3] Esser et al., "Scaling Rectified Flow Transformers for High-Resolution Image Synthesis", ICML 2024.

### Strengths
- The authors propose several techiniques that are tailored to the discrete flow matching, and show these technique improve the performance.
- The ablation study on the proposed techniques both for the training and sampling process is well designed.

### Weaknesses
- The connection between the graph generation and the proposed method is weak. The authors argue that the proposed method is tailored to the graph generation. However, I am concerned that the proposed method is not specific to the graph-structured data except for the encoding part (i.e. RRWP). Specifically, the proposed methods for training and sampling are not motivated by the characteristics of the graph-structured data but by the discrete flow matching itself.

- It seems to be unfair as the proposed model architecture has a modification compared to DiGress [2]. Please provide the effect of using RRWP.

- Some related works are not experimentally compared. CatFlow [4] which is based on the flow matching for the graph generation and GruM [5] which is based on the diffusion mixture tailored for the graph generation are competitive baselines that shoulde be compared in this paper.

[4] Eijkelboom et al., "Variational Flow Matching for Graph Generation", NeurIPS 2024.

[5] Jo et al., "Graph Generation with Diffusion Mixture", ICML 2024.

### Questions
- How much does the exact computation of the expectation cost?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents DeFoG, a graph generation framework based on discrete flow matching (DFM) that overcomes limitations in existing diffusion-based methods for graph generation. DeFoG introduces a linear interpolation noising process and a denoising method using continuous-time Markov chains (CTMCs). It study how to disentangle training and sampling stages, thus enhancing model optimization flexibility and efficiency. Result of DeFoG is shown to achieve state-of-the-art results across synthetic and molecular datasets.

### Strengths
The paper make a first attempt on applying discrete flow matching on the graph generation problem. 

Particularly, the paper make a extensive exploration of how to make DFM work perfectly on it. It

(1) Explore on the design choice of marginal distribution and training timestep schedule.

(2) Explore on sampling design, including sampling time step schedule, stochaticity rate matrix(similar to the predictor-corrector ) as well as guided diffusion.

(3) Explore on model architecture design.

The exploration is extensive and provides valuable experience for the research community

### Weaknesses
The only weakness is in the innovation - DFM is a well-established framework in recent years. The paper does not make key methodology innovation rather than make exploration. Moreover, it's not clear what's the major limitation of the previous diffusion-based graph model, the paper should highlight how the paper address them.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper adds to the growing literature of graph generation using diffusion/flow models by adapting a continuous-time discrete-space flow matching framework. This framework is tailored for graph generation through a graph transformer architecture with Relative Random Walk Probabilities encodings, a loss function that differentially weights node connectivity and features, a finely-tuned noise schedule, an appropriate prior distribution, and optimized rate matrices for sampling. The method is evaluated on a comprehensive set of benchmarks, demonstrating strong results in sample fidelity and efficiency compared to previous diffusion-based methods.

### Strengths
The paper is clearly written and well-organized. Several changes to the adapted flow matching framework are proposed, each of which is well-motivated and theoretically justified, with its empirical impact thoroughly evaluated in an ablation study. The extensive numerical experiments cover small to medium-sized synthetic and molecular graphs, consistently showing competitive or state-of-the-art performance across all benchmarks. Notably, the comparison on sampling and training efficiency underscores the value of the proposed method over previous discrete-time graph diffusion approaches.

### Weaknesses
My primary criticism is the limited novelty of the contribution. There is a substantial body of work on graph generation by adapting generative models to the graph domain, recently including various diffusion/flow models. The proposed method is incremental in this context, primarily confirming the effectiveness of the adapted flow matching approach by Campbell et al. in the graph generation setting.

Although the method is extensively evaluated against previous work, the related work section is rather sparse and does not mention several works the authors compare against in the experiments. I recommend expanding this section to provide a more comprehensive overview of the existing literature on graph generation.

### Questions
When comparing the efficiency of the proposed method to ablated models and DiGress (Figures 2, 6a, 7a), which version of DiGress is used for the comparison? Is it the original version? As the proposed method also includes architectural improvements (e.g., Relative Random Walk Probabilities encodings), I suggest including a comparison of DiGress with the same architecture as the proposed method to better assess the impact of the continuous-time vs. discrete-time formulation.

Additionally, why do Figures 6b, 6c, 7b, and 7c not include the comparison to DiGress?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper adapts the Discrete Flow Model (DFM) for graph generation tasks and introduces the DeFog model, which utilizes a graph transformer as its backbone for handling graph data. The authors highlight the importance of a disentangled design for training and inference procedures, which enhances sampling efficiency and performance. Their approach achieves state-of-the-art results across extensive evaluation tasks.

### Strengths
1. This paper proposes Discrete Flow Matching (DFM) and achieves good generation results with significant sampling speed ups, on tasks raning from synthetic graph to molecular graph.
2. The writing of the paper is clear and organized, making it easy for readers to follow and understand.

### Weaknesses
The primary concern with this paper is its novelty, as it appears to be a straightforward application of Discrete Flow Models (DFMs) as in paper [1]. The technical advancements in the DFM model are either too trivial or lack sufficient justification.

1. The crucial decoupling technique that enhances efficiency and performance, using a sampling procedure different from training, is based on prior work rather than being an original invention.
2. The decoupling technique lacks justification. Theoretically, the paper does not adequately explain why the proposed decoupling would improve sampling efficiency and performance. Empirically, it lacks quantitative measures demonstrating its impact on performance.
3. In Table 1, metrics that measure the similarity between generated population and data distribution are not present, other MMD indicators, for example, Degree, Clustering coefficient etc are not considered in this paper.
4. The necessity of several Lemmas and Theorems in the paper is questionable. For instance, Lemma 1 concerning permutation equivariance and invariance for a transformer without positional embedding seems too obvious to formalize. Additionally, the practical need for an equivariance guarantee in a logical graph is not apparent, and the theoretical guarantees in Section 5 do not clearly connect with the main idea of the paper.
5. The paper's notation requires careful revision. For example, in Equation 4 (#189), the subscript of the expectation $p_{t|1}$ should be $p_{1|t}$. The notation $x^{1:n:N}$ at #219 seems peculiar; $x^{(n)}$ might be clearer than $x^n$. At #229, $p_{1|t}^\theta$ is a scalar rather than a set, and it is suggested to use boldface for $\theta$ as it represents a non-scalar value.

### Questions
1. In line #223, while the relationship between nodes and edges is managed by a graph transformer, what additional graph-specific challenges should be considered?
2. In line #278, what does the term "design space" refer to? Is it related to the data distribution or the noisy exploration space?
3. In line #280, the paper claims that flow models enable greater flexibility and efficiency due to decoupling the training and sampling procedures. This isn't immediately apparent; why would a decoupled procedure enhance sampling speed?
4. In lines #288-289, how is the factorization of graph probability related to permutation invariance?
5. In lines #334-337, shouldn't the new $R_t$ be normalized?

[1] Andrew Campbell, Jason Yim, Regina Barzilay, Tom Rainforth, Tommi Jaakkola. "Generative Flows on Discrete State-Spaces:
Enabling Multimodal Flows with Applications to Protein Co-Design"

### Soundness
3

### Presentation
2

### Contribution
1
