# Smooth Probabilistic Interpolation Benefits Generative Modeling for Discrete Graphs

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Though typically represented by the discrete node and edge attributes, the graph topological information can be sufficiently captured by the graph spectrum in a continuous space. It is believed that incorporating the continuity of graph topological information into the generative process design could establish a superior paradigm for graph generative modeling. Motivated by such prior and recent advancements in the generative paradigm,  we propose Graph Bayesian Flow Networks (GraphBFN) in this paper, a principled generative framework that designs an alternative generative process emphasizing the dynamics of topological information. Unlike recent discrete-diffusion-based methods, GraphBFNemploys the continuous counts derived from sampling infinite times from a categorical distribution as latent to facilitate a smooth decomposition of topological information, demonstrating enhanced effectiveness. To effectively realize the concept, we further develop an advanced sampling strategy and new time-scheduling techniques to overcome practical barriers and boost performance. Through extensive experimental validation on both generic graph and molecular graph generation tasks, GraphBFN could consistently achieve superior or competitive performance with significantly higher training and sampling efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a graph generative model based on a Bayesian Flow Network, where noisy graphs serve as latent variables in the data generation process. The model employs sender and receiver distributions to define the posterior and joint distributions of these latent variables, along with an aggregated variable to efficiently calculate the ELBO objective. Additionally, the paper introduces several technical innovations, whose impacts are evaluated through comprehensive ablation studies.

### Strengths
1. While the Bayesian Flow Network is an established framework, adapting it for graph generation and introducing technical improvements bring novelty to the paper.

2. The experiments are comprehensive, and the results are promising. The ablation study demonstrates the effectiveness of the "Adaptive Flow Back" technique.

### Weaknesses
1. While the paper presents an interesting and promising approach to graph generation, the clarity of some key technical details could be improved to enhance understanding:

- Loss function: Further clarification is needed on the statistical assumptions over $q(y_1,\cdots y_n\mid x)$ that allow the derivation of Eq 4 from Eq 3, as well as on whether $\log p(x \mid \theta_n)$ is incorporated in the final loss function (Eq 11). Specifically, the assumption of a factorized posterior $q(y_1, \dots, y_n | x) = \prod_{i=1}^n q(y_i | x)$ needs to be explicitly stated and justified, as this is not a trivial assumption and has significant implications for the model's behavior. Furthermore, the role of $q_{noise}$ in Eq. 4 is unclear; it appears to be a component used to derive $q(y_t|x)$, but its precise definition and relationship to the overall posterior distribution require more explanation. The omission of $\log p(x \mid \theta_n)$ from the final loss needs a more thorough justification beyond efficiency considerations, as this term is crucial for ensuring the model learns a good representation of the data.

- The generative model: Additional background on the definitions of $y$ and $\theta$ would be helpful. Are these definitions 
modeling choices, or do they result from specific assumptions on the data generation process? It is not clear whether $y$ represents a noisy version of the graph structure or node features, or both. The connection between the continuous parameter $\theta$ and the discrete graph structure is also not well-defined. The paper should clarify whether $\theta$ parameterizes a distribution over graphs or if it is an intermediate representation that is later converted into a graph.

- The derivation of Eq 9 from Eq 6 should be elaborated at least in the appendix. The steps involved in going from the general form of the ELBO to the specific form in Eq. 9 are not obvious and require a more detailed mathematical derivation. This is especially important for readers who are not familiar with Bayesian Flow Networks.

- Adaptive Flow Back: Although the paragraph provides a thorough introduction to the technique, the motivation behind it and how the mechanism achieves this goal are not immediately clear. The intuition behind using the condition $\left\|\phi\left(\mathbf{G}^{\theta_t}, t\right)-\phi\left(\mathbf{G}^{\theta_{t-1}}, t-1\right)\right\|^2 \geq \epsilon$ to determine when to switch from exploration to fine-tuning is not immediately obvious. A more detailed explanation of why this specific condition is used and how it relates to the variance of $\theta$ is needed.

2. (minor) Typos and misuse of notations

- Eq 3: A negative sign should precede the KL term, and $\log p_{\phi}(x \mid \theta)$ should be $E_{q} \log p_{\phi}(x \mid \theta)$.

- Eq 4: the latent variable should use the notation $y_t$  instead of $z_t$ for consistency.

- Line 172: the categories should be defined with $\textbf{c} = [c_1, c_2, \cdots, c_K]$ to align with "$K$ categories".

- Line 272: "W the following notations" -> "With the following notations"

### Questions
Please address the concerns I raised in the "Weaknesses" section. I am open to revising my rating if these issues are satisfactorily addressed.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes Graph Bayesian flow networks which is a Bayesian flow networks for graph generation. Motivated from the claim that graph topology can be captured in a continuous space, Graph Bayesian flow networks were designed. The method was validated by 2d molecular graph generation.

### Strengths
Extension of Bayesian flow networks to graph generation domain.

### Weaknesses
If, as claimed, the graph topology information, particularly the spectrum of graph-related matrices, can indeed be well represented in continuous space, it might be feasible to design a generative model in the frequency domain [1]. Given this, the choice of a Bayesian flow network is unclear. The paper does not adequately justify why a flow-based approach is superior to other generative methods, especially considering the potential for spectral methods to directly capture graph structure. The lack of a clear rationale for using Bayesian flow networks, instead of exploring alternative methods that might be more naturally suited to the problem, is a significant weakness.

While spectral features are mentioned, there is no detailed explanation of how they are utilized. The paper lacks specifics on how spectral features are incorporated into the model architecture. It is unclear whether these features are used as input to the flow network or if they are used to condition the generative process. The absence of a clear description makes it difficult to assess the impact of spectral features on the model's performance.

Comparisons with the most closely related works are lacking. There is no discussion of differences from GeoBFN [2] and MolCRAFT [3], nor is there a performance comparison with the 2D molecular graphs generated by those models. The paper fails to contextualize its contribution within the existing literature, making it hard to evaluate the novelty and effectiveness of the proposed approach. The absence of comparisons with relevant baselines is a major oversight.

### Questions
Where are figures 1 and 6?

Could the authors explain the rationale behind the scheduling in Eq. 13, or is it a heuristic design?

Where are a detailed explanation of how spectral features were used and an assessment of their importance in generating 2D molecular graphs?

Compared to generated 2D molecular graphs from GeoBFN and MolCRAFT, what is the performance gap?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Graph Bayesian Flow Networks (GraphBFN), a novel approach to graph generation using Bayesian Flow Networks (BFNs). Unlike traditional discrete diffusion models, GraphBFN uses a continuous latent variable, created by sampling infinitely from a categorical distribution, to smoothly interpolate between a prior state and the desired graph structure. By mapping this continuous latent to a probability simplex, GraphBFN produces a probabilistic adjacency matrix, representing the likelihood of various edge types, which allows for more nuanced and smooth graph generation. This framework enables efficient and accurate modeling of complex graph structures, supports diverse node and edge features, and offers substantial speed improvements over diffusion-based methods. Extensive experiments demonstrate GraphBFN’s strong performance and efficiency in generating realistic, topologically accurate graphs.

### Strengths
- The paper applies a new framework to graph generation, namely Bayesian Flow Networks.
- If the results are statistically significant (see weaknesses), the model exhibits good performance across all benchmarks.
- The empirical evaluations seem to suggest a better sampling efficiency than graph diffusion models.

### Weaknesses
 - The concept of noisy channel is unusual in graph generation
- What is p_theta on l131 ? It's not defined anywhere.
- The definition of p_phi is unclear. What is y_i ? Reading section it seems that it can estimate both the density of y_t conditional to all previous states as well as the density of x given the sequence y_1:t in a diffusion model fashion. The role of this model is therefore hard to understand
- It took me some time to understand that your time axis goes from noise to data. Since you’re comparing to diffusion, which does the opposite, I think it is worth mentioning that somewhere.
- I find this sentence line 163 very unclear :
“For the discrete diffusion model (Vignac et al., 2022; Austin et al., 2021),
the Eq. 4 could be seen as one possible variant of the variational distribution q(yt|x) in Eq. 1, i.e. the extension of uniform transition diffusion (Austin et al., 2021) based on continuous-time Markov chain (CTMC) theory (Campbell et al., 2022).”
What do you mean by extension ? It seems that Austin et al. 2021 is based on Campbell 2022 …
- The introduction of noisy distribution is unclear. I would focus on clearly presenting the noisy distribution and provide a brief explanation of how this is achieved in appendix
- I think it would be worth introducing the sender and receiver distributions in section 2.2, to help the reader making the connection between section 3.2 and your optimization objective.
- The paragraph on Adaptive Flowback is poorly written, especially l 309-312
- You should provide error bars for all your experiments. Due to the limited size of the SPECTRE benchmark datasets, the metrics can exhibit high variance, casting doubt on the performance of some models such as Grum (cf e.g results in Siraudin et al. 2024)

### Questions
- Diffusion allows for direct model supervision, while you regress again y_t, which is a noisy quantity. This is downside compared to diffusion
- Where has the right hand side term of equation 3 gone in your loss ?
- What are the benefits of you method on graphs that do not exhibit community patterns such as SBM ?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims at the problem of graph generation. It models the graph generation process through Bayesian flow network. According to the topological information of the graph, a smooth probability interpolation method is defined to learn the topological properties of the graph.

### Strengths
1.Using BFN for graph generation is natural because it models the diffusion of discrete data very well.
The theoretical explanation and introduction of the article are very detailed, which strongly supports their views.

### Weaknesses
1.The authors do not clearly explain the relationship between spectral theory and their topological modeling.
The experiment selects too few datasets with different topological properties. The authors need to supplement common synthetic data such as community, ego, ba, etc., which have shown the efficient generation of their model on networks with various topological properties.

### Questions
1.Can the author give a more detailed explanation of the relation of spectral theory to your method?
Can the author give an the performance on other datasets?

### Soundness
3

### Presentation
2

### Contribution
3
