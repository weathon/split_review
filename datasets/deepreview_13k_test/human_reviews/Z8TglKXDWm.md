# PhyloVAE: Unsupervised Learning of Phylogenetic Trees via Variational Autoencoders

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Learning informative representations of phylogenetic tree structures is essential for analyzing evolutionary relationships. Classical distance-based methods have been widely used to project phylogenetic trees into Euclidean space, but they are often sensitive to the choice of distance metric and may lack sufficient resolution. In this paper, we introduce *phylogenetic variational autoencoders* (PhyloVAEs), an unsupervised learning framework designed for representation learning and generative modeling of tree topologies. Leveraging an efficient encoding mechanism inspired by autoregressive tree topology generation, we develop a deep latent-variable generative model that facilitates fast, parallelized topology generation. PhyloVAE combines this generative model with a collaborative inference model based on learnable topological features, allowing for high-resolution representations of phylogenetic tree samples. Extensive experiments demonstrate PhyloVAE's robust representation learning capabilities and fast generation of phylogenetic tree topologies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
PhyloVAE adopts the architecture of variational autoencoders and is specially designed to handle phylogenetic tree topologies. It maps any point in the latent space to a specific tree topology, and this architecture makes it excel at distinguishing between different tree shapes, outperforming traditional distance-based methods. Moreover, PhyloVAE's generative property, which enables the mapping of any point in the latent space to a specific tree topology, is an important advantage over other models that lack this functionality. This property enhances the visualization and interpretability of the learned representation.

### Strengths
* **(S1)** The proposed PhyloVAE framework is highly innovative. To my knowledge, a variational autoencoder is applied to the representation learning of phylogenetic trees for the first time, demonstrating the potential of deep learning methods in this field.

* **(S2)** This paper is overall easy to follow to some extent (but also has some drawbacks, as mentioned weaknesses). The model architecture and training process are described in detail, especially the mapping function in potential space and visualization of tree topology.

* **(S3)** The effectiveness of PhyloVAE is fully verified through experiments, especially its performance in dealing with complex tree structures, which shows the advantages over traditional distance-based and density-based estimation methods. The experimental design is reasonable, and the used datasets are appropriately selected.

### Weaknesses
* **(W1)** Some important assertions are unclear or unsupported. The author mentioned that the *model has high-resolution representations of phylogenetic tree samples*. How was this proven through experiments and theatrical analysis? Meanwhile, the authors mention that *their effectiveness heavily depends on the choice of distance metric and can sometimes exhibit counterintuitive behaviors*. What specifically does this counterintuitive behavior refer to?

* **(W2)** The specific application scenarios described in the manuscript are vague. Although the importance of tree visualization is emphasized in the intro and abs sections, the main goal of the model is not clearly distinguished between representation learning and generative modeling. I suggest the authors further clarify the core goal of the proposed methods (or tackled problem) in the introduction section and clearly distinguish the relationship between representation learning and generative modeling. Meanwhile, the author might provide a specific discussion on the potential use of the model in different application scenarios to enhance the logic and practical significance of the manuscript.

* **(W3)** This paper mentions the limitations of distance-based and density-based estimation methods. Still, it lacks an in-depth analysis of the PhyloVAE model settings to clarify its advantages in representation learning and visualization. What model settings or methods can perform well in representation learning and visualization?

* **(W4)** More minor issues could be clarified:
  - **(a)** What is the impact of different phylogenetic inference software choices?
  - **(b)** Why is the formula for the data distribution in line 157? Are there any a priori constraints?
  - **(c)** The simulated dataset used in the experiments in Section 5.1 only contains tree topologies with five and eight-leaf nodes, and experiments on large-scale tree structures are lacking.
  - **(d)** The paper does not clearly explain the specific generation process of the tree topologies in the experiments in Section 5.1.
  - **(e)** The paper's formula 3 has a variable K, and so does line 346. Do they represent the same variable?

### Questions
* **(Q1)** One of the motivations mentioned in the text is: *The classical approach to visualize and analyze distributions of phylogenetic trees is to calculate pairwise distances between the trees and project them into a plane using multidimensional scaling (MDS) .* *However, these approaches have the shortcoming that one can not map an arbitrary point in the visualization to a tree, and therefore do not form an actual visualization of the relevant tree space.* However, as the main motivation of this paper, it does not explain in detail the limitations of this mapping and its specific impact on visualization and analysis. Why is this operation a disadvantage? And what are the shortcomings of the MDS method in representing tree space?

* **(Q2)** The encoding mechanism in Section 3.2 is clearly written, but there is a potential problem:

  - **(a)** In the Decomposition stage, when selecting edge e_n, the conditional probability $Q(e_n | e_{<n})$ is based on the selected edge set $e_{<n}$. As the depth of the tree and the number of edges increases, the calculation of the conditional probability may become complicated.
  - **(b)** In the Reconstruction stage, if an error occurs in the previous Decomposition process, the reconstructed tree may not be consistent with the original tree. How should this be corrected?

* **(Q3)** The paper claims that PhyloVAE is ‘the first representation learning framework that targets the topology of phylogenetic trees’, but existing methods such as VBPI-GNN also have representation learning capabilities. This statement lacks discussion and comparison with relevant existing work, making its claim of innovation seem less rigorous and may make readers question the contribution of the article. Similarly, why not compare with baselines?

* **(Q4)** Where is the hyper-parameter experiment, e.g., how to decide the parameters $d$, $K$, $L$, Iterations, and batch size?

### Soundness
3

### Presentation
2

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
The paper introduces PhyloVAE, an unsupervised learning framework for phylogenetic tree topologies that utilizes variational autoencoders (VAE). PhyloVAE is designed to both learn informative representations of phylogenetic tree structures and generate new tree topologies efficiently. The model combines a novel encoding mechanism inspired by autoregressive topology generation, creating a deep latent-variable model that maps arbitrary points in the latent space to tree topologies, enabling high-resolution and parallelized topology generation. The framework demonstrates its effectiveness in representation learning and generative modeling, outperforming traditional distance-based methods by providing both visualization and probabilistic modeling for tree topology distributions.

### Strengths
1. Highly Relevant and Practical Topic: The paper addresses the generation and representation of phylogenetic trees, a critical problem in evolutionary and computational biology. By introducing an unsupervised generative model, the paper offers a novel approach for analyzing complex evolutionary relationships. This work is practically significant as it enables researchers to gain deeper insights into biological evolutionary paths and diversity, advancing the field substantially.
2. Significant Efficiency Gains: PhyloVAE achieves efficient phylogenetic tree generation through its non-autoregressive design, enabling faster and parallelized tree structure generation. Compared to traditional stepwise generation methods, this improvement is especially meaningful for handling large-scale biological data, accelerating the computational process and enhancing the model’s feasibility and applicability in real-world scenarios.

### Weaknesses
1. Need for Generalizability Testing Across Datasets: The paper primarily focuses on evaluating PhyloVAE across different benchmark datasets (DS1-DS8) without testing its generalizability across distinct datasets. For example, testing a model trained on DS1-DS4 and then assessing its performance on DS5 would offer insight into the model’s robustness across varied evolutionary patterns. Such cross-dataset evaluations are crucial for demonstrating the model’s applicability beyond specific training sets.
2. Lack of Comparison with True Phylogenetic Trees: While PhyloVAE performs well in capturing tree structures, there is no direct comparison between the generated phylogenetic trees and real, experimentally derived species trees. This comparison would help validate the biological relevance of the model’s output by assessing how closely PhyloVAE’s generated trees align with known evolutionary relationships. In-depth analysis of these discrepancies would offer valuable insights into the model’s accuracy.
3. Marginal Improvements in Performance Metrics: The paper demonstrates efficiency gains in tree generation time but does not show substantial improvements in accuracy metrics compared to state-of-the-art methods. As shown in Table 1, while PhyloVAE’s performance is comparable, it does not significantly outperform traditional models like ARTree in KL divergence to ground truth trees. This raises questions about the trade-offs made between efficiency and accuracy in the model’s design.

### Questions
1. How does PhyloVAE perform when trained on one set of datasets (e.g., DS1-DS4) and tested on a distinct dataset like DS5? Could the authors provide insights or additional experiments to demonstrate the model’s robustness across varied evolutionary patterns? Cross-dataset evaluations would enhance the assessment of PhyloVAE’s broader applicability. To make this clearer, could the authors also analyze specific aspects of the datasets—such as the number of species, evolutionary rates, or tree shapes—that might influence generalization performance? Additionally, specific metrics or visualizations for comparing performance across datasets would help clarify how different components, like the encoding mechanism or the inference model, contribute to the model’s generalizability.
2. Has PhyloVAE been directly compared to real, experimentally derived species trees? Such a comparison could provide essential validation for the model’s biological relevance by examining how closely the generated trees align with established evolutionary relationships. Could the authors explore potential discrepancies between PhyloVAE-generated trees and actual species trees and analyze their implications for the model’s accuracy? Including specific datasets or types of experimentally derived trees, as well as visualization techniques or metrics, would help quantify and illustrate these similarities and differences.
3. While PhyloVAE offers efficiency gains, it appears not to outperform traditional models like ARTree in terms of accuracy metrics, as noted in Table 1’s KL divergence comparisons. Could the authors clarify the trade-offs made between efficiency and accuracy in the model design, and whether further refinements might enhance both speed and accuracy? A detailed analysis of how specific model components or hyperparameters affect this trade-off would be helpful. For example, it would be insightful to explore how increasing the latent space dimension or adjusting the number of particles in importance sampling impacts both computational efficiency and accuracy (e.g., KL divergence). These investigations could offer valuable directions for potential model refinements.

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
The authors introduce a cheap approximation of the ARTree generative model for phylogenetic trees (by assuming independence of the actions executed sequentially to construct a tree). This allows faster training compared to ARTree because generation (or reconstruction variational bound) can be done in parallel (over all tree construction actions) rather than sequentially, which yields a runtime speedup on modern computers. They evaluate the new model (PhyloVAE) for the purpose of 2D visualization and quantify the loss in modeling power (in terms of KL divergences to the ground truth).

I have increased my ratings after reading the rebuttal.

### Strengths
Phylogenetic trees are interesting objects to model and visualize and it could be the case that training on vary large collection of very large trees could be computationally expensive with previous methods such as ARTree.

### Weaknesses
(1) to be convincing, the paper should show a case where ARTree is really too slow for being practical

(2) The experiments reported take on the order of seconds or less than a minute to train, so one wonder if the gain in computing power is so useful, if that would be at the expense of worse modeling of the tree distributions.

(3) Although two different capacities were tested for PhyloVAE (dimension 2 and 10), that was not the case for ARTree, making it unclear if ARTree could have obtained a better KL divergence with a different capacity.

(4) In terms of modeling power, assuming independence of the actions seems very strong. It is not clear that it will work well for other tree distributions not tested in this paper.

### Questions
Please try to address the weaknesses in the above section.

### Soundness
3

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
4

### Summary
The authors propose a VAE for learning latent representations of phylogenetic tree topologies and generative processes thereof. Arguably the main contribution lies in the clever encoding structure that runs in the order of leaf nodes. A crux to making the VAE work for trees is to use pre-computed tree topologies as training data (inputs to the encoder). They experiment on standard and less standard real phylogenetic data.

### Strengths
This is a very nice submission that is well-written and which proposes a clever approach to learn representation and generative processes of phylogenetic trees. The experimental results are convincing and significant, especially taking into account the run times compared to ARTree. It utilizes previous results and ideas from the VI-based phylogenetic tree inference literature to, in a non-trivial way, devise a VAE algorithm.

### Weaknesses
* It is appreciated that it is clearly stated that the inputs to the encoder are collections of topologies. In [1; Fig. 5] the posterior coverage of the pre-computed topologies was evaluated and compared with those obtained from MrBayes. Can you provide a similar quantification? It might even suffice to merely reference their work to guard aganst the common suspicion that pre-computed tree topoplogies are not good representations. 

* On the same topic, in Sec. 5.2 the topologies are gathered from a 1 milion MCMC run, but this is not this quite short, in order to ensure that the samples are coming from the posterior?  To be clear, I do not think that it is an issue to learn posteriors over a pre-computed set of topologies, if the set of topologies is a good representation of the true posterior's support.

* The collection of trees are tuples of the topologies and their corresponding weights. The weights are then in a footnote described to be the frequency of the topology (right?). Then in all experiments, the weights are explicitly mentioned to be uniform. Why is this? Is a topology never sampled more than once in the pre-processing stage? What would happen if the trees were weighted by scores obtained, for instance, from MrBayes? Or simply the Felsenstein likelihood of the topology, normalized over all samples.

* Recently there have been works for applying mixtures of variational distributions in VAEs [2], phylogenetic posterior inference [3] as well as in VAEs *and* phylogenetics [4] (note that [4] does not propose a VAE for phylogenetics, but applies mixtures in both settings). I think at least [3] and [4] should be mentioned in the list of works referenced at line 463 to emphasize the great, current interest in Bayesian phylogenetics at ML conferences. 

## Minor
* There is a clash of notations for $w$ notating both internal node connections in Sec. 3.2 and the weights of the tree topologies.

* I would be good to disambiguate the proposed method to other tree-based VAEs such as [5, 6] and [7] (although [7] appears to not be published). None of these references experiment on phylogenetic data, but the originality of the proposed method would be emphasized by contrasting your encoder and generative processes to these works.

[1] https://jmlr.org/papers/volume25/22-0348/22-0348.pdf

[2] https://proceedings.mlr.press/v202/kviman23a.html

[3] https://arxiv.org/abs/2310.00941

[4] https://arxiv.org/abs/2406.07083

[5] https://arxiv.org/pdf/2306.08984

[6] https://arxiv.org/pdf/1810.06891

[7] https://openreview.net/forum?id=Hy0L4t5el

### Questions
* Relating to the references provided regarding mixtures of variational distributions, I am wondering if your proposed method could benefit from the mixture techniques provided in [2,3,4]? Potentially they could help PhyloVAE to outperform ARTree in Table 1? In [4] the estimators make the learning of the mixture components efficient in terms of run time.

* Is Algorithm 1 parallellizable on a GPU? Can you use batches of tree topologies during training?

### Soundness
4

### Presentation
4

### Contribution
3
