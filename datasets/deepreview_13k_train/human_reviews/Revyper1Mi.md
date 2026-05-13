# Sailing in high-dimensional spaces: Low-dimensional embeddings through angle preservation

- Decision: Reject
- Scores: 3, 3, 6

## Abstract
Low-dimensional embeddings (LDEs) of high-dimensional data are ubiquitous in science and engineering. They allow us to quickly understand the main properties of the data, identify outliers and processing errors, and inform the next steps of data analysis.
 As such, LDEs have to be \textit{faithful} to the original high-dimensional data, i.e., they should represent the relationships that are encoded in the data, both at a local as well as global scale.
 The current generation of LDE approaches focus on reconstructing \textit{local distances} between any pair of samples correctly, often outperforming traditional approaches aiming at all distances.
 For these approaches, global relationships are, however, usually strongly distorted, often argued to be an inherent trade-off between local and global structure learning for embeddings. We suggest a new perspective on LDE learning, reconstructing \textit{angles} between data points.
 We show that this approach, \ourmethod, yields good reconstruction across a diverse set of experiments and metrics, and preserve structures well across all scales.
 Compared to existing work, our approach also has a \textit{simple formulation}, facilitating future theoretical analysis and algorithmic improvements.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose a new technique that embeds a given dataset on  a 2-dimensional sphere within 3-dimensional space, while approximately preserving the angles between any triplets of points.

### Strengths
See questions.

### Weaknesses
The idea behind the paper is interesting, and the authors even try to convey theoretically how to extract relevant information from the given dataset (angles between triplets of points). However, from the main text it is hard to find clear results why angle preserving embedding is preferable over the current embedding techniques. I did not see a clear theorem or clear empirical results on real datasets that show the preferability of such embedding. In the next lines I will go over some of the problems I had with the main text-

1. General comment- From my understanding of the paper you are working on visualization problems which is more specific than the low dimensional embedding algorithms. 

2. The Related work is one big paragraph of 32 lines. It would be preferable if this would have been broken into multiple paragraphs.

3. Initialization- The proposed method is initialized using the projection of the first two PC components onto half a sphere far away from the poles. It would be beneficial if the authors can discuss why is PCA a good initialization with respect to angles. For example, if the data is a 2-dimensional swiss roll that is embedded in 3-dimensional space I am not sure that PCA is preferable.

4. Theoretical - It will be beneficial if the authors will add a theorem that describes which data structures can be embedded based on angles.  For example, in manifold learning the intrinsic dimension plays a main role when considering to embed data.

5. Theoretical- It would be beneficial to a proof for for the conclusion that appears in Equation 4 (derived from equation 2 and theorem 2).

6. Experiments- Each evaluation metric is described in a few words and only in the Appendix they describe it technically. It will be beneficial to discuss them a bit.

7. Experiments- The proposed algorithm embeds the data in 3-dimensional space with some restrictions, while it compares to visualization techniques that use 2-dimensional space. Some of the compared algorithm can be used to generate a 3-dimensional embedding, it will be beneficial to compare to their 3-dimensional embedding version.

8. Experiments- It will be beneficial to add the PCA embedding in the different experiments, as the proposed method uses it as initialization. This will allow the reader to understand the adjustments made by your method to it. For example, in Fig 2. /"Low Dimensional data" experiment - the embedding of the proposed method seems to be close to the PCA embedding.

9. Experiments- I think that it will be beneficial to show the embedding of spectral algorithms such as Laplacian Eigenmaps and Diffusion maps.

10. Experiments-  Cluster data- The authors considered experiments on Cluster Data within the main text. However, the visualization and the tables with the performance measure were left out in the Appendix.  It will be beneficial if the authors add a figure/table about it in the main text.

11. Experiments- Real data- Some of these dataset have labels. It will be beneficial to see how well the different embeddings techniques embeds samples with similar labels together. I think that such visualization/ performance measures will be more beneficial than current performance measures.

### Questions
The idea behind the paper is interesting, and the authors even try to convey theoretically how to extract relevant information from the given dataset (angles between triplets of points). However, from the main text it is hard to find clear results why angle preserving embedding is preferable over the current embedding techniques. I did not see a clear theorem or clear empirical results on real datasets that show the preferability of such embedding. In the next lines I will go over some of the problems I had with the main text-

1. General comment- From my understanding of the paper you are working on visualization problems which is more specific than the low dimensional embedding algorithms. 

2. The Related work is one big paragraph of 32 lines. It would be preferable if this would have been broken into multiple paragraphs.

3. Initialization- The proposed method is initialized using the projection of the first two PC components onto half a sphere far away from the poles. It would be beneficial if the authors can discuss why is PCA a good initialization with respect to angles. For example, if the data is a 2-dimensional swiss roll that is embedded in 3-dimensional space I am not sure that PCA is preferable.

4. Theoretical - It will be beneficial if the authors will add a theorem that describes which data structures can be embedded based on angles.  For example, in manifold learning the intrinsic dimension plays a main role when considering to embed data.

5. Theoretical- It would be beneficial to a proof for for the conclusion that appears in Equation 4 (derived from equation 2 and theorem 2).

6. Experiments- Each evaluation metric is described in a few words and only in the Appendix they describe it technically. It will be beneficial to discuss them a bit.

7. Experiments- The proposed algorithm embeds the data in 3-dimensional space with some restrictions, while it compares to visualization techniques that use 2-dimensional space. Some of the compared algorithm can be used to generate a 3-dimensional embedding, it will be beneficial to compare to their 3-dimensional embedding version.

8. Experiments- It will be beneficial to add the PCA embedding in the different experiments, as the proposed method uses it as initialization. This will allow the reader to understand the adjustments made by your method to it. For example, in Fig 2. /"Low Dimensional data" experiment - the embedding of the proposed method seems to be close to the PCA embedding.

9. Experiments- I think that it will be beneficial to show the embedding of spectral algorithms such as Laplacian Eigenmaps and Diffusion maps.

10. Experiments-  Cluster data- The authors considered experiments on Cluster Data within the main text. However, the visualization and the tables with the performance measure were left out in the Appendix.  It will be beneficial if the authors add a figure/table about it in the main text.

11. Experiments- Real data- Some of these dataset have labels. It will be beneficial to see how well the different embeddings techniques embeds samples with similar labels together. I think that such visualization/ performance measures will be more beneficial than current performance measures.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a low-dimensional embedding method named MERCAT that preserves angular relationships to maintain both local and global data structures. Unlike traditional methods that prioritize local distances and often distort global structures, MERCAT maps high-dimensional data onto a 2D unit sphere by optimizing angles between points. This approach is claimed to achieve consistent structure preservation across scales and advantages over methods like UMAP and tSNE in retaining meaningful relationships within complex datasets.

### Strengths
* An alternative way for nonlinear dimensionality reduction
* Some theoretical guarantees are provided

### Weaknesses
 * The paper is about visualization. But there are no figures that visualize any real-world datasets in the main paper. There are some visualizations in the appendix. However, the results are even worse than t-SNE and UMAP. Especially when the colors are removed in an unsupervised setting, the MERCAT results are messy and show little useful global pattern.
* The paper addresses faithful visualization. But faithfulness is not defined.
* The method is expensive O(n^3) and has to rely on subsampling data points.

### Questions
* PCA is used in Algorithm 1 to get \hat{X}. Much high-frequency information is lost in this step.
* Subsampling can lose much information about the manifold.
* Why do you multiply with 0.7*pi in the algorithm?
* Where are the definitions of performance metrics (angle preservation, distance preservation, neighborhood preservation, and density preservation)?
* A reference and discussion is missing. Faithfulness has already been discussed in the following paper.

J. Venna et al. Information Retrieval Perspective to Nonlinear Dimensionality Reduction for Data Visualization. In JMLR 2010.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The current generation of LDE approaches focus on reconstructing local distances between any pair of samples correctly, often outperforming traditional approaches aiming at all distances. For these approaches, global relationships are, however, usually strongly distorted, often argued to be an inherent trade-off between local and global structure learning for embeddings. The authors suggest a new perspective on LDE learning, reconstructing angles between data points. Then they show that this approach, MERCAT, yields good reconstruction across a diverse set of experiments and metrics, and preserve structures well across all scales. Compared to existing work, the proposed approach also has a simple formulation, facilitating future theoretical analysis and algorithmic improvements.

### Strengths
1. Originality. he authors suggest a new perspective on LDE learning, reconstructing angles between data points. Then they show that this approach, MERCAT, yields good reconstruction across a diverse set of experiments and metrics, and preserve structures well across all scales. 

2. Quality and Clarity. There are no technical errors, and the presentation and writing are clear.

3. Significance. The authors show that this approach, MERCAT, yields good reconstruction across a diverse set of experiments and metrics, and preserve structures well across all scales. Compared to existing work, the proposed approach also has a simple formulation, facilitating future theoretical analysis and algorithmic improvements.

### Weaknesses
I am absolutely not in this field and the comments from me are not relatively professional. The comments in the following are just raised from the presentation or organization.

1. In the abstract part, the authors just state that their approach also has a simple formulation, facilitating future theoretical analysis and algorithmic improvements compared to existing work. I think the authors can add the specific values of performance gains here to better show the effectiveness of the proposed method.

2. The authors report the angle preservation, distance preservation, neighborhood preservation and density preservation between computed low-dimensional embeddings and original data. However, the authors use "-" to indicate method do not terminate within 24h. As far as I know, some experiments still report the final results that do not terminate within 24h. I think the authors can give more detailed explanations here.

3. For the real data results shown in Table 1, the authors should add more recent methods for comparison in the experiment to better show the effectiveness of the proposed method.

4. In the related work part, the authors just discuss three methods proposed after 2023, then the authors can add more recent related work for discussion in this part.

### Questions
1. Why choose these parts, i.e., Smiley, Mammonth, and Circle in the embeddings of low-dimensional examples？The related reasons can be given here.

2. Why choose PCA instead of the others as the manner of reduction for robustness, whihc is shown in Algorithm 1.

### Soundness
2

### Presentation
2

### Contribution
2
