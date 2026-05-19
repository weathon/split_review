# Evaluating graph generative models with graph kernels: what structural characteristics are captured?

- Decision: Reject
- Scores: 6, 5, 3, 3

## Abstract
For a number of practical problems, it is important to measure the similarity between graphs. In particular, it is essential for assessing the quality of graph generative models. In evaluation measures for graph generative models, graph kernels are often used to measure the similarity of graphs. Recently, it has been shown that the choice of a graph kernel may drastically affect research outcomes in this area. Therefore, it is essential to choose a kernel that is suitable for the task at hand. In this paper, we propose a framework for comparing graph kernels in terms of which high-level structural properties they are sensitive to. For this, we choose several pairs of random graph models that are different in one particular property: heterogeneity of degree distribution, the presence of community structure, the presence or particular type of latent geometry, and others. Then, we design continuous transitions between these models and measure which graph kernel is sensitive to the corresponding change. We show that using such diverse graph modifications is crucial for evaluation: many kernels can successfully capture some properties and fail on others. One of our conclusions is that simple and long-known Shortest Path and Graphlet kernels are able to successfully capture all graph properties that we consider in this work.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on identifying the topological or structural features captured by different graph kernels, enabling them to be compared, in the context of generative graph models.

The authors consider the Erdös-Rényi model as a baseline from which the features under consideration are absent. They propose different ways of departing from this model by randomly adding one of the features under consideration to the graph. For each feature (e.g. degree heterogeneity), they obtain a probabilistic graph model parameterized by $\theta$, where $\theta=0$ corresponds to the absence of the feature (Erdös-Rényi model), and $\theta=1$ to maximum presence.

The sensitivity of a kernel to each of these features is then numerically evaluated by Spearman's correlation between $\theta$ and maximum mean discrepancy along the interval with respect to each of the two endpoints.

Numerical results show that most kernels identify some features easily and others less well, although the Shortest Path kernel and the Graphlet kernel have good performance on all models.

### Strengths
The subject covered in this article is certainly very interesting, and in my opinion goes beyond the question of generative graph models.

The methodology employed seems to me original and could be reapplied to other contexts.

The observations made on the various kernels provide further insight into their ability to detect certain topological features, which may already be valuable for practitioners.

Last but not least, the paper is well written and pleasant to read.

### Weaknesses
From my point of view, the paper's main weakness lies in the numerical part: the only results presented concern graphs with 50 nodes and 190 edges (on average). We would like to know whether the results obtained are robust when we vary the size of the graph (in number of nodes and number of edges).

Another limitation is that the results obtained depend on the probabilistic models chosen. For instance, each may introduce random features other than the one targeted, which may bias the results obtained. Figure 2 gives some interesting examples of this phenomenon. This may be an intrinsic limitation of the approach, but it can be overcome by considering different probabilistic models for the same feature.

### Questions
In addition to the comments above, I think the points below should be addressed.

To have a self-contained paper, the Erdös-Rényi and Chung-Lu models should be described.

For some models, the authors explain precisely the link between the parameters and the average number of edges (triadic closure in Appendix B.1 and dimensionality in Appendix B.2). For others (e.g. latent geometry) there is no explanation at all.

As a reader, we are left a little disappointed by the two correlation measures. A single indicator would greatly simplify the statement of results. The data suggest that, in most cases, they are equal. For features such as the triadic model and for the Graphlet kernel, the link between the two correlations might be studied theoretically, which would provide a valuable piece of information on this question.

On page 2, one reads that computing a distance is as hard as graph isomorphism, while a few lines down, it says that any kernel can be easily transformed to a distance measure. Can the authors address this apparent contradiction?

Typos:

page 2: popular

page 3: $\mathcal{G}_i$ is not defined

page 4: triadic model in Appendix B.1

page 8: colors in Table 1?

page 8: 4.1 Results?

page 13 (B.2): $h\geq 2h$

page 13 (B.2): Solving... $r^=$

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper generate random graphs with different models and compute different kernels of the graphs. It then show how the kernels are sensitive to the interpolations of parameters between generative models.

### Strengths
- I think the question is reasonable to ask and the paper is an attempt in the right direction.

### Weaknesses
- I find the paper shows some relationship between generative models of graphs and kernels, it is hard to see what are the applications of these findings in real life. The conclusion is rather qualitative.
- One of the key step of the paper is to interpolate between generative models, its formula is not clearly stated. It seems to "interpolate" probabilities of different models, and the idea of "interpolating graph characteristics" has to be properly defined as the characteristics are not mutually exclusive. It is difficult to understand what it means by having "100%" of a characteristic and "0%" of another when the two are related. 
- The "performance" of kernels is difficult to grasp and it is related to what is needed to be performed as in also the last point. 
Overall, I'd suggest to go on this direction with a clear, deeper study of what exactly are the different between generative models. At the moments, it doesn't show concrete conclusion yet for any practical purpose.

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a graph similarity technique based on graph kernels and their capacity to capture high-level structural properties. The properties considered by the paper include: degree distribution, community structure, latent geometry, and others. The paper presents a continuous transitions between the models and measures the sensitivity of the graph kernels to the changes.
The experiments show this property — that different graph kernels have different sensitivity with Shortest Path kernel and Graphlet kernel showing the best performance in terms of capturing graph properties.

### Strengths
Among the strengths this paper has is that the proposed model is relatively easy to follow and the writing and organization are relatively good. Some aspects are subtle due to the nature of the kernel organization and abstraction of features. The most relevant positive aspect is the number of baselines used, and the transparency of the global architecture comparison. That is, this paper could serve as a reference of graph kernel performance across metrics, which is in itself an interesting idea.

### Weaknesses
However, the paper comes with several weaknesses. The most noticeable one is the nature of the graphs used for evaluation. With n = 50 nodes and m = 190 edges, the size of the graphs is hardly what we see in practice, where datasets contain [hundreds of] thousands of nodes and many more edges. While this does not disqualify this paper's potential application, it limits the applicability of the insights provided. Other considerations could be improved in the paper. For instance, the Chung Lu models require the use of very heavy parameterization where every node's weight is used for modeling the degree distribution of a graph. Another weakness is that the concept of dimensionality, in page 5, is introduced in the paper in a very general manner and without sufficient rigor to incorporate it in the framework. Thus, something like a pseudocode could be useful to clarify some of these imprecisions.

### Questions
What would be your main argument to ensure the method is generalizable to larger graphs?

What is the effect of using Chung Lu models computationally?

Can you describe algorithmically how you incorporated/modeled dimensionality in your framework?

How did you encoded these graph characteristics in the kernels?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper claims that graph kernels are commonly used to evaluate the performance of graph generative models. The paper then investigates whether some standard graph kernels can capture structural properties of graphs such as the degree distribution, the presence of community structure and others. The empirical results demonstrate that the shortest path and graphlet kernels can better capture the considered properties than the rest of the kernels.

### Strengths
- This is an interesting paper. Even though graph kernels have been extensively studied for two decades, it is still not clear what graph properties are encoded into the explicit (or implicit) representations created by those methods. This work actually complements [1] which theoretically investigates whether graph kernels can capture properties such as triangle-freeness, connectivity and planarity.

- The work is useful to practitioners since the reported results suggest that some kernels can better capture some properties than other kernels. Thus, if a practitioner is interested in a specific property, this work can help them choose the right kernel.

- The presentation is reasonably clear.

[1] Kriege, N. M., Morris, C., Rey, A., & Sohler, C. "A Property Testing Framework for the Theoretical Expressivity of Graph Kernels". In Proceedings of the 27th International Joint Conference on Artificial Intelligence, pp. 2348-2354, 2018.

### Weaknesses
- The paper claims that graph kernels are commonly used to evaluate the performance of graph generative models, however, no references are given. The authors should add some references and also motivate the use of graph kernels for this task. What are the advantages of graph kernels over competing evaluation approaches?

- The paper focuses on 7 graph properties, but it is not clear why those 7 specific properties were chosen and not others. Are there any applications of graph generative models where graphs that exhibit those properties need to be generated? Please provide more details.

- Since no theoretical results are provided, I would expect the authors to provide some explanation or intuitions about why some kernels fail to capture some of the considered properties. An explanation is provided in the case of the WL kernel, but not for all the kernels. 

- The experimental evaluation is not fully convincing because all the generated graphs consist of 50 nodes and 190 edges (in expectation). It is not thus clear whether the results generalize to graphs of different sizes. I would suggest the authors construct other datasets where graphs are of different size and different density.

### Questions
- In page 9, it is mentioned that "there are only two different graphlets of size k=3: wedges and triangles". This is true if connected graphlets are only considered. However, the standard graphlet kernel also counts disconnected graphlets and there are 4 such graphlets for k=3. Did the authors use an implementation that counts connected graphlets?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
