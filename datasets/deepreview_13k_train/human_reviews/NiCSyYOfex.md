# Node-Level Topological Representation Learning on Point Clouds

- Decision: Reject
- Scores: 5, 5, 8, 3, 5, 6

## Abstract
\noindent
	Topological Data Analysis (\textsmaller{TDA}) allows us to extract powerful topological, and higher-order information on the global shape of a data set or point cloud.
	Tools like Persistent Homology or the Euler Transform give a \emph{single} complex description of the \emph{global structure} of the point cloud.
	However, common machine learning applications like classification require \emph{point-level} information and features to be available.
	In this paper, we bridge this gap and propose a novel method to extract node-level topological features from complex point clouds using discrete variants of concepts from algebraic topology and differential geometry.
	We verify the effectiveness of these topological point features (\TOPF) on both synthetic and real-world data and study their robustness under noise.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Many machine learning applications like classification needs point-level information and features. This paper proposes a method to extract node-level topological features from 2D and 3D topologically structured point clouds.

### Strengths
The authors proposed topological point cloud clustering benchmarks that could benefit future works in TDA. The proposed method outperforms other methods on topological structured point cloud data and enjoys the `Robustness to noise' characteristic of persistence homology.

### Weaknesses
1. **Datasets:**

    a) The Topological Clustering Benchmark Suite => TPCC is introduced by the authors in this paper to evaluate the effectiveness of the proposed clustering method. The construction of these datasets in this benchmark has not been sufficiently discussed in the paper/appendix. For instance, it is unclear how the ground truth labels have been obtained since all the datasets are synthetic in nature. Specifically, the method used to generate the point clouds and assign ground truth labels based on the underlying topological structure is not clearly articulated. A more detailed explanation of the sampling process and the criteria used to define distinct clusters is needed.

    b) 3D datasets => What are the ground truth labels for these datasets, and how have these labels been obtained? Why were auxiliary points added in Cys123? The rationale for adding auxiliary points to the Cys123 dataset is not sufficiently justified. The impact of these points on the topological analysis and the resulting node-level features needs to be clarified. It is also unclear if the ground truth labels for the 3D datasets are based on manual annotation or some other automated process.

2. **Experiments:**
      a) There are a total of 12 datasets presented in the paper: seven 2D datasets in the TPCC benchmark and five 3D datasets, as shown in Figure 5. Then why are results on only four 2D and three 3D datasets presented in Table 1? The selection criteria for the datasets used in Table 1 are not provided. It is unclear why some datasets were excluded from the quantitative evaluation. A more comprehensive evaluation across all datasets would be beneficial.

      b) Please provide a quantitative comparison with the baselines on the 3D datasets. The lack of quantitative comparisons on the 3D datasets makes it difficult to assess the performance of the proposed method relative to existing techniques in higher dimensions. The paper should include a more thorough evaluation of the method's performance on 3D data.

      c) Why are some of the run-times in Table 1 0.0 seconds? What is the breakdown of TOPF run-times in terms of Steps 1-4 of Algorithm 1? The reported runtimes of 0.0 seconds are likely due to rounding, but this should be explicitly stated. The paper should also provide a detailed breakdown of the computational cost of each step in the algorithm to better understand the bottlenecks and potential areas for optimization.

3. **Computational Complexity:** What is the complexity of Algorithm 1, especially Steps 3 and 4? A detailed analysis of the computational complexity of each step in the algorithm is needed. This analysis should include the dependence on the number of points, the dimensionality of the data, and the maximum homology dimension. The complexity of the sparse matrix operations in Step 3 and the pooling operation in Step 4 should be discussed.
4. **Presentation:** The algorithm presentation needs significant improvement. Steps 3 and 4 of the TOPF algorithm are hard to read. Please explain these steps using a concrete, small-scale toy point cloud dataset. The terms “simplex-valued harmonic representatives” (line 337) and “simplex-valued vector” (line 341) are used without any explanation. What is the role of interpolation parameter $\gamma$?
The description of Steps 3 and 4 of the algorithm is too abstract and lacks sufficient detail. The paper should provide a step-by-step explanation of these steps using a concrete example. The meaning of the terms “simplex-valued harmonic representatives” and “simplex-valued vector” should be clearly defined. The role of the interpolation parameter $\gamma$ in the computation of the harmonic representatives needs to be better explained.
5. **Novelty:** Which component of the algorithm is novel? Is it step 4, since Steps 1-3 are standard tools of TDA? The paper should clearly identify the novel contributions of the proposed method. It is not clear whether the novelty lies in the combination of existing techniques or in a specific step of the algorithm. The paper should explicitly state which steps are novel and why.
6. **Limited Applicability:** TOPF only obtains meaningful results on point cloud with topological structure. However, many datasets do not have such a structure. Furthermore, TOPF is computationally expensive on datasets with a large number of points (e.g., those obtained from CAD designs or 3D Scanners).  While the authors mentioned using landmarks to improve performance, no experiments in the paper did so. It seems the method is only practical in a very limited setting, which is points with only topological shapes and a small number of points.

### Questions
1. What is the maximum homology dimension $d$ in the experiments?
2. What is the relation between the output of step 3 ($\hat {e}_k^i$) of Algorithm 1 with the Circular coordinates of De Silva & Vejdemo-Johansson (2009)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Paper proposes a novel idea for extraction of continuous topological features via projection of simplicial generators into harmonic subspaces. It works as follows. First, given a point cloud sample from a manifold, it computes persistent homology classes based on alpha or VR filtration of the point cloud. Second, it selects the most relevant classes based on the smallest quotient heuristic. Third, these relevant global classes are used to compute local topological features that indicate local ‘strength’ of chosen topological class. This is done via aggregation of simplices for chosen birth-depth timestep width and their projection into harmonic subspace of simplices. Finally, simplicial features are aggregated on point level to produce pointwise features. These features can be utilized to provide topology-aware visualizations and/or topology-aware clustering. 

Proposed method evaluates the Topological Clustering Benchmark Suite (TCBS) that consists of 7 point clouds that represent complex topological arrangements.

POST DISCUSSION UPDATE

I strongly appreciate replies by the authors and all additional work and experiments they have done. However, I think that paper still cannot be accepted in the current state because it need substantial rework. I am especially concerned about fair comparison to learning-based baselines using point cloud normalizations that were used to train them.

If this would be a journal paper I would recommend 'resubmit a major revision' but for conference I have to recommend reject.

Below are final justifications/suggestions (up to authors' discretion):

1) Main text of the paper needs to be adjusted to better balance theory and practical considerations of the method. I recommend checking the following paper as examples on how to balance heavy mathematical background and practical aspects Original diffusion models paper: https://arxiv.org/abs/1503.03585 Product Manifold learning: https://arxiv.org/pdf/2010.09908 SGLD: https://www.stats.ox.ac.uk/~teh/research/compstats/WelTeh2011a.pdf
As bare minimum, I recommend removing Theorem 4.1 completely and moving Figures 13 and 15 to main paper.

2) Experimental evaluation should use 'native' normalizations for all baselines. TOPF also ideally evaluated in 'standard' normalization space of baselines, otherwise there is a concern that hyperparameters of TOPF might require adjustment to 'standard' normalization.

3) I strongly recommend including results on sampling regularity and sampling density (for baselines as well) in the main paper.

4) I strongly recommend including stronger baselines like DGCNN.

5) TCBS benchmark data might benefit from additional examples.

6) I have also checked authors' discussion with reviewer smnw and I agree with the following reviewer's points: alpha*-complexes might be confusing both for readers who are familiar and who are unfamiliar with the theory; proposed work seem to be proposing isometric invariant and thus local shape descriptors probably should be mentioned in related work. That being said, I still think that main focus of the paper should be empirical validation of the paper because theoretical contribution seems to be very limited.

### Strengths
— Novel idea for extraction of continuous topological features via projection of simplicial generators into harmonic subspaces and subsequent extraction of pointwise features; 
— Good visual presentation of the method; 
— Somewhat good introduction into fundamentals of algebraic topology;
— Ablation with respect to some of the hyperparameters of the method;
— Quantitative results on the proposed TCBS benchmark seem to be strong.

### Weaknesses
— Main body of the paper focuses too much on introduction into algebraic topology and too little on practical considerations of the method; 
— Algorithm 1 is too schematic and it is hard to reproduce the method based on it. It can heavily benefit with more detailed substeps; 
— Applicability of proposed method to high-dimensional spaces (D>3) seems to be limited; 
— Related work discussion (including supplement) is limited; I recommend including some of the work discussed in [Rev 1] 
— Theorem 4.1 has very limited practical applicability for 3D data analysis; 
— No ablation with respect to sampling density; 
— No ablation with respect to non-uniform sampling from the manifold; 
— Learning-based baseline (PointNet) is very weak;
— Important details in some figures are missing (see suggestions/questions).




### Questions
My main issue with the paper is that it focuses too much on the theory of algebraic topology that works with continuous spaces; and focuses too little on practical considerations that stem from the discretization aspect of topological data analysis. Overall, the proposed model is built upon discrete approximation of the manifold through N-simplices based on localized Delaunay triangulation based on epsilon radius neighbors. It means that two considerations are important for the method. First, number of points: we want enough points to approximate manifold topology but not too much because dense sampling can be expensive or unavailable. Second, sampling density: we want points to be sampled somewhat uniformly from the manifold (if all samples are the same point, it does not help us much). Good TDA method should ideally require as few points as possible to recover structure of the manifold while being robust to non-uniformity and noise in sampling. I think the current iteration of the paper largely ignores these considerations. Namely:

— How sampling density affects performance of the method? For example, what happens with predicted labels in Figure 8 if we reduce sample sizes of point clouds by 2x? 3x? 5x? My concern is that the model might not work well on sparse point clouds. 

— Similarly, what happens with the method if we have non-uniform sampling from the manifold? For example, what happens when the target manifold has a high-curvature area that is not sampled densely enough? 

— My understanding is that the epsilon radius of local Delaunay triangulation (Definition B.2.) is the hyperparameter of the method. It is not clear how this parameter should be chosen and it looks like it can strongly affect the results: if it is too large, local Delaunay triangulation will start closing holes; if it is too small, the manifold will be disconnected. Do authors have some practical suggestions how this radius should be chosen, especially if we don’t have good priors about the data?

— Theorem 4.1 has very limited practical applicability to actual 3D data analysis. It assumes two sets of points: one set is sampled from the unit sphere; another set is sampled with distance at least 2 to this unit sphere. For the majority of 3D point cloud applications, point clouds are normalized to unit cube. My understanding is that in this case assumptions of Theorem 4.1 do not hold. Is my understanding correct? Maybe the setting that I have described can be adapted for Theorem 4.1 somehow?

— On a related note, what is the normalization of the data for the experiments? Are point clouds normalized to unit cube? Is this normalization the same across all evaluated methods? 

— PointNet baseline is very weak. It was introduced in 2016 and was superseded by a large number of architectures: PointNet++, several versions of PointTransformers and other attention-based architectures. PointNet performance on the majority of benchmarks is significantly worse than for all of the mentioned methods. More up-to-date method can give significantly better performance on proposed benchmark. 

— Applicability of the method to high-dimensional spaces seems to be very limited. How well does the proposed method scale with the number of dimensions? My understanding is that local Delaunay triangulation will be significantly slower for higher dimensions. It is also not clear, how to choose the triangulation radius. 

— On a related note, the experiment in Figure 11 has very limited applicability. To analyze image features with TOPF one needs to train additional variational autoencoder to map image features in 3D space. This scenario does not seem to be practically appealing What happens if relevant information cannot be contained in 3 dimensions? What if one wants to run TDA on original features? 

— What dictated the sampling density of the TCBS dataset? Point clouds in Figure 7 have a number of samples that can differ by order of magnitude: 267 points for SphereInCircle and 4600 points for 2Spheres2Circles. Does method assume/TCBS data assume some upper bound on minimum distance to nearest neighbor for each point and that is what dictates sampling density? Or is it something else?

— Figure 5 is missing information about the average distance from each point to its nearest neighbor. Without this information, it is hard to assess how large is the relative value of the noise compared to manifold sampling density. 

— Figure 10 is missing time units, so it is impossible to infer speed of the method from it. Also, how indicative are those running times (they are from two point clouds from the benchmark)?

— Figure 13 seems to be missing 9 of 12 subfigures.

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
This paper develops a method to assign _topological information_ to each point $x$ of a given point cloud $X \subset R^d$ a vector. 

Roughly speaking, assuming that $X$ exhibits a set $\mathcal{F}$ of significant topological features (connected component, loops, or cavities, etc.), the idea is to quantify for each $x \in X$ to which extend it contributes to each topological feature $f \in \mathcal{F}$. Eventually, each $x \in X$ is thus turned into a vector in dimension $\mathcal{F}$ that describes the relation between the local point $x$ and the global (topological / geometric) structure of $X$.

The construction is performed by relying on the Hodge decomposition theorem (in discrete form) and eventually boils down to a (actually two) least square problem(s) which can be solved efficiently. 

The approach is then showcased in a broad range of experiments. In particular, a "topological clustering benchmark" is introduced.

### Strengths
- Good introduction, clear and nicely written
- I really appreciate the step-by-step description of Section 3, making the flow of the exposition pretty nice despite the technicality of the construction.
- Nice illustrations overall.
- Elegant and fairly-well motivated construction. 
- Nice set of experiments. The introduction of a "topological clustering benchmark" is a valuable contribution of the work, we need more of these in the community.

### Weaknesses
 - The approach depends on several seemingly important hyper-parameters. This may be a necessary price to pay, but belongs to its weaknesses nonetheless. 
- Though acknowledged by the authors, the setting of Theorem 1 is very idealized. In particular, the $n$-sphere has somewhat "maximal reach" and it is less clear to me that the theorem remain (with probability $< 1$ but still reasonable) valid when the underlying manifold is a "pinched" sphere with low reach. The theorem remains nice nonetheless and its validity in applications is not crucial to the work.  

## Minor (not real weaknesses)

- Typo : "hull hull" in Theorem 1
- In the first experiment (Topological Point Cloud Clustering Benchmark), I believe that including topological regularization term in point embedding methods (node2vec and pointnet) has been attempted in some works (e.g. in Topological Autoencoder of Moor et al., some experiments in Optimizing Persistent Homology based function of Carriere et al., Topological Node2vec of Meehan et al., etc.). I believe that this would not invalidate the claims made in that paragraph, namely that these methods requires specific training to work and may be slower than the proposed approach, but it may be worth to briefly mention these.

### Questions
1. Points $v$ in $X$ are vectorized in dimension $|\mathcal{F}|$, where $\mathcal{F}$ designates the set of "most significant topological features", typically detected with the proposed heuristic. However, I believe that this embedding dimension may be somewhat unstable to even small perturbation of $X$ (e.g. $X$ is made of a circle of radius 2 and a circle of radius 1; then the persistence of the big circle is twice the one of the smaller one, which is itself twice the one of small circles arising from the noise). Similarly, if one (theoretically) refrain from using an heuristic and pick all topological features for $\mathcal{F}$, the dimension is (clearly, this time) unstable as well. Is there a way to somewhat "smooth" the choice of $\mathcal{F}$ to avoid relying on a hard threshold but rather considering (possibly infinitely) many dimensions but whose relative importance would be weighted by $\ell_i$? I ask this question out of curiosity, I do not expect an extensive answer in the rebuttal.

### Soundness
3

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
5

### Summary
The paper studies point-level features by using persistent homology.

### Strengths
The paper is written clearly enough.

### Weaknesses
Lines 177-178: "the filtration value of a k-simplex in the α-filtration is the radius of its circum-k-sphere, which differs from its filtration value in the VR filtration".

The concept of a "filtration value" appears here for the first time and is never defined in the paper, which leads to the major misunderstanding of persistence.

Lines 368-372: "Theorem 4.1 (Topological Point Features of Spheres). Let X consist of at least (n + 2) points (denoted by S) sampled uniformly at random from a unit n-sphere in R^n+1 and an arbitrary number of points with distance of at least 2 to S. When we now consider the α-filtration on this point cloud, with probability 1 we have that (i) there exists an n-th persistent homology class generated by the 2-simplices on the convex hull hull of S".

Even a non-expert can notice that n-th dimensional (?) homology class cannot be generated by 2-dimensional (?) simplices for n>2. Also, Theorem 4.1(i) fails for n=1 and any 3 points on a unit circle that form a non-acute triangle. 

There are infinitely many point clouds whose 1-dimensional persistence is empty. Look for a generic family of such clouds in J Applied and Comp Topology 2024.

Even Figure 3 in the paper demonstrates that only 3 points in the 1D persistence represent reasonable cycles, hundreds of others represent only noise. In fact, there is no sense to apply persistence to proteins whose atoms are ordered. In this ordered case, the complete isometry invariant of a point cloud is the classical distance matrix requiring only quadratic time, which was known at least since 1935, see I.Schoenberg, Annals of Mathematics, 724-732, 1935.

The persistence homology is more suitable for clouds of unordered points but is much weaker than the collection of all pairwise distances, which determine any generic point cloud in general position uniquely under isometry, which has been known in computational geometry for more than 20 years, see Boutin and Kemper, 2004.

The stronger invariant (a local distribution of distances) has been widely studied in shape analysis, e.g. see Memoli, "Gromov–Wasserstein distances and the metric approach to object matching" (FocM 2011), extended to a complete and polynomial-time invariant under rigid motion in any fixed Euclidean R^n (CVPR 2023).

The initial obstacle for the proposed research is the lack of a rigorous problem statement. The attempts to state problems in the final section seem a bit late:

Lines 514-520: "selection of the relevant features is a very hard problem" and "efficient computation of simplicial weights leading to the provably most faithful topological point features is an exciting open problem"

The words "relevant" and "most faithful" should be rigorously defined, else anyone can claim that their features are "relevant" and "most faithful".

### Questions
Can the authors consider 3 points (1,0), (0,1), (-1,0), draw three disks centered at the points with a growing radius alpha and check that the resulting union of disks always has trivial 1-dimensional homology without cycles?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper focuses on constructing node-level topological representation of point clouds. To achieve that, it proposes TOPF to do topological data analysis. By doing that, node-level topological features are extracted from complex point clouds through using discrete variants of concepts from algebraic topology and differential geometry. Experiments are conducted on both synthetic and real data for the verification.

### Strengths
1. The idea of topological representation on node-level for point clouds is somehow interesting;

2. The English writing is acceptable

### Weaknesses
1. Fig. 1 doesn't help understand the overall and core design of the TOPF. The authors are highly suggested re-drawing this part. From my personal perspective of view, this figure should consist the motivation and the overview of the proposed methods.

2. For the experimental part, point cloud matching and registration are typical tasks that require good representation point clouds. I would suggest the authors add comparisons to those related methods, like the unsupervised ones (PPF-FoldNet, ECCV 2018 & WSDesc, TVCG 2022).

### Questions
See weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method to extract node-wise topological information from point clouds. To extract the topological structure of a point cloud and to associate it with each point, they compute persistent homology and utilize information from the generators of these homology classes. Additionally, to make the topological information of each node more meaningful, they connect global and local information using the Hodge Laplacian.

### Strengths
1. The preliminaries and detailed explanations of the method in Sections 2 and 3 are appropriate and clear.
2. The authors employ an interesting idea to obtain node-wise features using the information in the generators of persistent homology.
3. They made an effort to stabilize the features by leveraging  insights from algebraic topology.
4. Theoretical results intuitively explain the advantages of the method.

### Weaknesses
1. Regarding the hyper-parameters, such as $\gamma$ on line 310 and $\delta$ on line 342, there are some concerns about robustness and the way to determine them. Although the authors test the robustness of the hyper-parameters in Appendix D, these results are limited to the topological clustering dataset. It remains uncertain if they are effective on more practical data. Furthermore, the method's reliance on these parameters, which control the scale at which topological features are considered, raises questions about its general applicability across diverse datasets with varying point densities and noise levels. The lack of a principled approach for setting these parameters could lead to inconsistent performance and requires further investigation.
2. The validity of the heuristics used in the paper should be further investigated. For example, the way to choose the points from persistence diagram in line 294, the strategy to give the topological information to each node in 342, and the process to aggregate the multiple information in line 350. These approaches should be validated with realistic datasets. The selection of representative points from the persistence diagram, especially when multiple features exist at similar scales, is not clearly justified. The method for assigning topological information to each node, which involves a weighted average based on distances, may not accurately capture the influence of topological features, particularly in regions with complex geometry. The aggregation of multiple topological features, which is done through a simple concatenation, may not be the most effective way to combine information from different homology dimensions.
3. Since various techniques are employed in the paper, it would be desirable to conduct an ablation study. Specifically, it should be tested on simple data how the effectiveness of features changes with or without the Hodge Laplacian. The Hodge Laplacian is used to project the homology generators into a harmonic space, which is claimed to stabilize the topological features. However, the impact of this projection on the final node-wise features is not clearly demonstrated. An ablation study should evaluate the performance of the method with and without this projection step to quantify its contribution to the overall performance. This is crucial to understand whether the added complexity of the Hodge Laplacian is actually necessary or if a simpler approach would suffice.
4. The intent of the experiments using VAE is unclear. It is difficult to understand what is meant by “topological structure inherent in the sample space,” as described in Figure 11. Additionally, it is unclear there are any implication for any specific applications.

### Questions
1. Why did you use VR filtration for n>3?  In higher dimension, doesn’t the computation cost of the persistent homology increase since the number of simplices in the VR complex increase?
2. Is it possible to effectively use TOPF for machine learning tasks other than clustering, such as point cloud classification? Additionally, is quantitative evaluation feasible for such tasks?
3. How did you choose the dimension of the persistent homology in the experiments?

### Soundness
4

### Presentation
3

### Contribution
3
