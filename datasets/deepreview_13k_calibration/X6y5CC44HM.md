# MANTRA: The Manifold Triangulations Assemblage

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 3, 8

## Abstract
The rising interest in leveraging higher-order interactions present in complex systems has led to a surge in more expressive models exploiting high-order structures in the data,
    especially in topological deep learning (TDL), which designs neural networks on high-order domains such as simplicial complexes. However, progress in this field is hindered by the scarcity of datasets for benchmarking these architectures. To address this gap, we introduce MANTRA, the first large-scale, diverse, and intrinsically high-order dataset for benchmarking high-order models, comprising over 43,000 and 249,000 triangulations of surfaces and three-dimensional manifolds, respectively. With MANTRA, we assess several graph- and simplicial complex-based models on three topological classification tasks. We demonstrate that while simplicial complex-based neural networks generally outperform their graph-based counterparts in capturing simple topological invariants, they also struggle, suggesting a rethink of TDL. Thus, MANTRA serves as a benchmark  for assessing and advancing topological methods, leading the way for more effective high-order models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces MANTRA, a large-scale, diverse, and high-order dataset of triangulations for benchmarking models in the topological deep learning space. The authors also assess graph and simplicial complex-based models on tasks like betti number estimation, homeomorphism type, and orientability detection. The introduction section is written well with enough definitions/context about various topological properties. The dataset specification includes all properties that are being computed for each object. Furthermore, nine different neural nets are evaluated on the classification task.

Overall, this paper could be a good contribution to topological deep learning, especially for developing advanced TDL methods and benchmarking them. However, the limiting factor is the evaluations (just MP networks) as they do not give a full picture of the impact of the dataset.

### Strengths
1. Extensive evaluation of currently available graph and simplicial complex-based models on MANTRA.

2. Provides a foundation for developing and benchmarking advanced TDL methods.

3. Insight into the ability of higher-order models to be invariant to triangulation transformations.

### Weaknesses
1. Evaluations are mostly focused on MP networks. It would help get better overall picture of the impact the dataset has by evaluating on other architectures like equivariant high-order neural nets and topological transformers.

2. The variance across results is surprising and I am not sure if running for more epochs/more hyperparameter tuning will address this.

### Questions
1. I'm not sure if you mention this in the paper but how are the initial labels and triangulations generated for each surface and three-dimensional manifold?

2. For a given surface, how much computational time is required for computing the fields mentioned Section 2?

3. Would MANTRA be useful for developing models for topological reconstruction (to recover incomplete surfaces or perform noise correction)? If so, how?

### Soundness
3

### Presentation
3

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
The paper introduces MANTRA, a new dataset designed for benchmarking topological deep learning (TDL) models. MANTRA consists of triangulations of two- and three-dimensional manifolds, labeled with various topological invariants such as Betti numbers, Homology torsion, homomorphism type (four options for 2D manifold and five options for 3D manifolds), and more. Using this dataset, the authors benchmark standard graph methods and TDL models on three types of tasks: Betti number prediction (2D + 3D), homeomorphism type prediction (2D), and orientability prediction (2D). Their results suggest that while TDL models are better at predicting higher order topological properties, they struggle with invariant to topology preserving transformations. The latter is demonstrated through additional experiments where barycentric subdivision -- a form of remeshing that preserves topological properties -- is performed on the test set.

### Strengths
- MANTRA is a large dataset specifically designed for topological property prediction, filling an important a gap in the TDL literature. Existing datasets are limited in scope, size, topological diversity and often rely on artificial topological lifting of graph data.
- The paper presents systematic analysis of graph methods vs. topological methods on fundamental topological property prediction tasks, establishing important baselines for future research in TDL.
- TDL models' ability to capture topological properties (**Q2** in the paper) is a fundamental question in TDL that remained under-explored to this point. Empirical results presented in the paper suggest that TDL models are better, compared to graph based methods, at learning topological properties from data.
- The question of invariance to topology preserving transformations (**Q3**) is also under-explored (albeit less clearly motivated). This paper demonstrate TDL models' sensitivity to remeshing by barycentric subdivisions -- a simple topology preserving transformation.
- The paper is clearly organized, with well defined questions, answered in a methodical manner. 
- The authors ensure reproducibility by providing well-documented code repos, versioned datasets, and multiple data format options (raw and PyTorch Geometric), making it easy to build upon this work.

### Weaknesses
 - **Topological diversity**
  - Other than the genus, first Betti number, and homeomorphism type for 2D manifolds, the distribution of topological invariants is limited and unbalanced.
    - For 3D manifolds:
       - Most Betti numbers, homeomorphism types, and torsion subgroups have only one or two possible values.
       - When two values do exist, one value represents over 99% of the cases.
  - All triangulations are limited to 10 or fewer vertices.

- **Limited model coverage**
  - The only TDL baselines included in the evaluation are simplicial complex models, excluding:
      - Cellular complex methods (e.g. [1, 2]).
      - Combinatorial complex methods (e.g. [3]).
      - Hypergraph methods (e.g. [4, 5]).
  - For both TDL and graph based methods, the evaluation only includes message-passing based architectures, excluding non-message passing graph neural networks (e.g. [6, 7, 8, 9]) and attention based TDL models (e.g. [3, 10]).
  - It would be informative to report the best performing model for each class in the main text.

- **Training methodology**
  - Models were trained for only 6 epochs, hyperparameters were not optimized. The can possibly lead to underestimation of the fully optimized performance of some of the architectures, limiting the scope of the conclusions that can be drawn from the experiments

### Questions
- **Dataset Generation**
  - How were the manifolds and triangulations generated?
  - What considerations did you make, if any, in order to encourage topological diversity in the dataset?

- **Experimental Results**
  - For the standard deviation results in Table 2, do they represent variation within a single model or across the entire class of models?

- **Computational Issues**
  - The authors cite computational constraints for limiting some aspect of the experiments, can the authors elaborate on the nature of these limitations given that all triangulations have 10 or fewer vertices?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper aims to benchmark the performance of graph-based and simplicial complex-based models on a newly-introduced 2-/3- manifold triangulation dataset. The paper focused on topological feature prediction tasks, including predicting Betti numbers, homeomorphism type and orientability.
Overall, the research question is interesting but the paper requires more work to be considered for publication. Please see my detailed comments and questions below.

### Strengths
The research question is interesting. It is novel to investigate the performance of graph and high-order network models on predicting topological features.

### Weaknesses
- There are various works on estimating Betti numbers, but the authors did not mention them. They should provide as solid baselines. For example:
  - Estimating Betti Numbers Using Deep Learning
  - A (simple) classical algorithm for estimating Betti numbers
- The experiments are rather unclear, for example, details on how the architectures are not provided. As a paper in datasets and benchmarks, this is necessary and as a reviewer, I'm interested in knowing how the architectures are designed and if they are reasonable.
  - Some experimental setup choices are not well-justified. For example, why randomly generated scalars are used as input features for graph-based models and randomly generated eight-dim vectors are used as feature vectors for simplicial complex-based models?
- Authors made a few claims which are not well-supported by either the experiments or literature.

Note: Please see my detailed questions below related to these points.

### Questions
1. about claims in the paper: 1) (058-060) To the best of our knowledge, the only publicly-available high-order dataset is the “Torus” dataset proposed in Eitan et al.(2024), which consists of a small number of unions of tori triangulations. 2) (069-071) The authors claimed this is the __first__ instance of a large, diverse, and intrinsically high-order dataset, comprising triangulations of combinatorial 2- and 3-manifolds. 

  - Authors refer to datasets that contain nontrivial higher-order structures as higher-order datasets. It's worthwhile to point out that such structure and the datasets have been long- and well-studied by network science community, as well as numerical modeling, and there has been numerous efforts in building and modeling higher-order topological structures in various networks. However, there are way more such datasets as far as I'm aware of. 
    - In computation biology and social networks, such datasets with higher-order structures appear very often. 
    - in numerical modeling, computational geometry, 2D and 3D manifold triangulations are almost everywhere and they easily grow to the order of millions. 
    - In topological deep learning community, such datasets have been applied by different papers as well, e.g., 1) SaNN: Simple Yet Powerful Simplicial-aware Neural Networks; 2) Unsupervised Parameter-free Simplicial Representation Learning with Scattering Transforms. 

  - As a reviewer, I really shouldn't provide a more complete list of such literatures. I believe this paper could benefit from a more thorough literature review. Note that _there is no such dataset_ does not work as a strong motivation. Moreover, this work is hardly the __first__  dataset involved with high-order topological structures.

2. about the experiment tasks: as a researcher in TDA, I would like to see how graph- and simplicial complex-based models compare to the TDA methods for the investigated three tasks in this paper. Again, this is necessarily needed for being a datasets and benchmarks paper.

3. I do not agree with authors *define* the lower/upper degree of a simplex as the number of simplices which share a face/coface with it. This number is merely the number of neighboring simplices, but not the degree for simplices. The _degree_ of a simplex is the number of faces/cofaces it has. Please refer to _Spectra of combinatorial Laplace operators on simplicial  complexes_ and _RANDOM WALKS ON SIMPLICIAL COMPLEXES AND THE NORMALIZED HODGE 1-LAPLACIAN_ for such definitions. 

4. Confusing experimental setup: 
   1. Randomly generated scalars are used as feature vectors for graph-based models and randomly generated eight-dim vectors are used as feature vectors for simplicial complex-based models? 
      - Questions: What is the motivation of using randomly generated values as input features? Any useful information do they provide to the models or tasks? 

   2. In predicting 0-betti numbers, you only have label 1. When seeing results on predicting $\beta_0$, I have the following questions:
      -  If graph-based models have 100% accuracy, how come simplicial-complex based models can be poor not nearly 50%? My question comes from the fact that: simplicial complex based models are __generalizations__ of graph-based models. If GAT/GCN has an accuracy of 100%, then SAN/SCCN, which are really extensions to higher-order simplices, should be able to achieve the same accuracy _when using the same output_ (Note that here I assume authors considered using the same type of output for predictions, e.g., when using node representations of GCN for predicting $\beta_0$, one should also use node representation of SCCN for predicting $\beta_0$). 
      -  On the other hand, most of the models implemented in this paper are performing representation learning, there is a need for a classifier or a regressor to predict the labels. Here it matters how a classifier/regressor, which takes the learned representation and computes the needed output, is defined. Yet, I couldn't find any details on this, but only __readout__ layers of different models, which are either mean, or sum of all embeddings. I wonder if authors simply used the readout to predict topological features. It doesn't make much sense to apply a direct readout to predict different topological features. 
   3. what is the dataset $2-\mathcal{M}_H^1$? I tried to check the appendix but couldn't find it. If I guessed correctly, it is a refined version of $2-\mathcal{M}_H^0$. But how is this refinement performed? 
   4. I appreciate the authors'effort in investigating the topological invariance of the models. This however is not well-analyzed in the paper, yet, the authors made the claim that high-order MP-based models are not invarinat relative to topological transformations ... in line 284. 
      1. First of all, how is topological transformation defined? Is it only refinement of the triangulation? 
      2. A proper topological predictor should be considered, yet this is unclear from the paper. 
      3. I do not really see message-passing models are implemented. By that, I mean Bodnar et al., 2021a. 
  

other minor suggestions:
- line 150: It seems incorrect to say something was degraded. I'm not an English major, but I think it should be "someone was degraded" or "something degraded". Please ignore it if I'm wrong. 
- Please figure out a way to present Tables 9-22 without rotating them 90 degrees. Though I tried reading them, they are still not easy for readers.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes a synthetic benchmark dataset for topological deep learning. Contrary to graphs representing pairwise interactions, this dataset focuses on higher-order interactions. It is generated by considering the simplicial complexes of 2 and 3-dimensional manifolds, resulting in structures with up to 10 vertices. Samples are labeled with topological descriptors, such as Betti numbers, torsion, orientability, genus, or homeomorphisms.

After introducing the dataset, several experiments are carried out to compare the performance of five graph and four topological learning models on topological prediction tasks. The main findings are that topological models perform better than graph models on these tasks, however, topological models are far from having a strong performance on these tasks.

### Strengths
- The paper is very well presented in terms of structure, rigor, and backing statements with relevant references or evidence.
- As far as I can tell, good conventions are followed to make the dataset easily available and usable.
- The experimental protocol is overall solid and the drawn conclusions are relevant and adequate.
- Limitations are discussed.

### Weaknesses
I have two minor remarks:
- The scope of the dataset is limited in dimension (order of interactions) and number of vertices, as well as being purely synthetic. While these are not bad aspects in their own right and this certainly is justified given that TDL is in its early days as it allows to study basic properties of models (e.g., remeshing invariance), the benchmark could potentially quickly lose its relevance. The restriction to simplicial complexes derived from 2 and 3-dimensional manifolds with a maximum of 10 vertices limits the complexity and variety of topological structures that can be explored. This narrow scope might not adequately represent the diversity of higher-order interactions found in real-world datasets, potentially hindering the generalization of models trained on this benchmark.
- As the authors acknowledge, several non-message passing TDL architectures were not included in the experiments. As such, one of the most intriguing interpretations of the results is somewhat diminished ("suggesting that new approaches are needed to leverage higher-order structure associated with the topological information in the dataset"). The exclusion of these architectures, particularly those that do not rely on message passing, limits the conclusions that can be drawn about the effectiveness of different topological learning approaches. For example, spectral methods or persistent homology based approaches might offer different insights into the data, and their absence makes the comparison incomplete.

### Questions
- What is your view on the scope of the dataset in terms of the vertices and dimensionality? I would suggest adding a short discussion on this in the limitations. 
- I am not sure if I agree with the statement in line 204: "To ensure fairness, all configurations use the same learning rate of 0.01". Different models may work best with different learning rates, which likely requires cumbersome hyperparameter tuning. The authors acknowledge this as a limitation, but I would reconsider the phrasing of this sentence -- is this really a "fair" comparison?

### Soundness
4

### Presentation
4

### Contribution
3
