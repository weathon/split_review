# Differentiable Euler Characteristic Transforms for Shape Classification

- Decision: Accept
- Scores: 8, 6, 5, 6

## Abstract
The \emph{Euler Characteristic Transform}~(ECT) is a powerful
  invariant, combining geometrical and topological characteristics
  of shapes and graphs.
  However, the ECT was hitherto unable to learn task-specific
  representations.
  We overcome this issue and develop a novel computational layer that
  enables learning the ECT in an end-to-end fashion.
  Our method, the \emph{Differentiable Euler Characteristic Transform}~(\modelname) 
  is fast and computationally efficient, while exhibiting performance on a par with 
  more complex models in both graph and point cloud classification tasks.
  Moreover, we show that this seemingly simple statistic
  provides the same topological expressivity as more complex topological
  deep learning layers.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes a differentiable graph descriptor based on Euler Characteristics Curves.  In practice, given a graph and a simplex order k, an ECC is constructed by computing, for each d-simplex, the cosine of the angle of the simplex feature with a predefined direction (filtering function) and counting the number of simplices above a given sequence of thresholds. The idea of the paper is to replace the counting with a sum after a soft thresholding, letting the gradient to be backpropagated to both simplex features and the predefined direction. 
The paper shows promising results on graph classification and a proof of concept experiment for pointcloud optimization.

### Strengths
The proposed method to compute differentiable ECC is straightforward and consists of simply replacing the counting of the elements above a threshold with a sum after a softmax. Nevertheless, the method has significant potential and allows not only the use of ECCs as a graph descriptor but also to investigate of the most significant direction (it is differentiable w.r.t. the ECC direction) and to ‘invert’ the descriptor and optimize directly the input graph.

### Weaknesses
The method description is not easy to follow, and many relevant details are not clear or missing. A detailed list is provided in the question section.
In particular, the architecture description is a bit confusing. In “Integration into deep NN” it is written that MLP + global pooling is used to achieve rotation permutation invariance, but the architecture is then described as a CNN over a 16x16 image. Wouldn’t this break permutation invariance?

A discussion about limits is missing.  For instance, since performing sums over simplices, the method is probably dependent on the sampling density. This is particularly relevant for PC classification. The authors also briefly mention the rotation equivariance of the method, but this is not elaborated much. For instance, if the network is invariant w.r.t. rotation permutation invariance, wouldn’t it make the model also rotation invariant (this probably depends also on the distribution of angles)?

My last concern is about the experimental part. In particular, to prove the importance of optimizing angles, I believe that the paper should compare DECT with building the ECT with fixed angles. Also, the method should be compared with more recent GNN methods, especially based on higher-order simplices. (e.g. Weisfeiler and Lehman Go Topological: Message Passing Simplicial Networks, Provably Powerful Graph Networks)

### Questions
- In the case of point clouds, how is the graph built? Do you consider all disconnected points?
- Eq 1 is not clear: what is k in the exponent? 
- Notation in eq 3 and 4 is not straightforward, is the second row the actual function definition? What is x?
- I find eq 5 difficult to read, especially the definition of the indicator function 1. Also, what is \sigma_k?
-Table 3 reports 2 times ECT-CNN.

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a differentiable topological shape descriptor that is conceptually based on the Euler characteristic transform (ECT).  Given a shape in its discrete representation as a n-dimensional simplicial complex, ECT computes a descriptor that is a function of a direction and the height function for the topological filtration. The idea is to project the simplices of the shape in all directions and compute the topological property of those directional signatures. Taken together, all these signatures can be concatenated and used together as a global shape descriptor. The main contribution in this paper is to rewrite the ECT in terms of an indicator function (Equation 5), that can be relaxed into a differentiable formulation using the sigmoid, leading to DECT.

The authors have shown a series of experiments to show the benefits of their approach. Table 1 demonstrates a simple proof of concept that DECT classifies shapes of different topologies. Section 5.2 demonstrates how to use it as a loss as well as optimize the descriptor for best directions and section 5.3 for their use in classifying geometric graphs.  Generally, the experiments make a favorable proof of concept.

### Strengths
- I find the core idea of this paper to be interesting. Rewriting the topological formulations using more computable components like indicator functions and sigmoids is nice. 
- Overall, the paper has been compiled quite well. Despite the relative inaccessibility of the core material, the writing and structure are quite good.
- The choice of experiments to demonstrate the benefits of the descriptor is refreshing. I particularly enjoyed the angle of investigation in sections 5.1 and 5.2, validating the main message of this paper.

### Weaknesses
 - I find it hard to truly appreciate a more stronger impact of the proposed descriptor for a wide range of applications. Despite the simplicity and comparable accuracies of Table 2, it would be nice to be more direct in explaining what features of data are simply not achievable using standard feature descriptors and how the proposed contributions alleviate it. 
- More significantly, I see no baseline comparison with other prior topological descriptors. For eg, how do some of the methods in: (Hajij et al., 2023; Hensel et al., 2021,  (Moor et al., 2020; Trofimov et al., 2023; Vandaele et al., 2022) compare with the proposed construction in section 5.1, 5.2 and 5.3?  
- It would be valuable to elaborate more concretely on the multi-scale aspect of the descriptor. I suspect it comes as a result of the height h, but it's hard to easily make this observation in the paper. Please confirm and elaborate.

### Questions
- How do you take inner products along given directions for higher dimensional simplices like the edge and face on a mesh? 
- The ECT and DECT are a set of descriptors lying on the unit hypersphere, and in higher dimensions working with directions sampled on the unit hypersphere becomes computationally very demanding. How can this be alleviated in the current framework? 
- Please annotate/reference the direction and height components in the image of Figure 2, to make it clear. 


Overall I am on the border for this paper. On the positive side, the paper has been compiled well and the main idea has been enumerated and experimented as a good proof of concept. However, the lack of comparison with conceptually similar baselines is a strong drawback, and more generally the wider applicability of the method is not promoted well. Taken together, I vote for a borderline accept as a pre-rebuttal rating.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel computational layer called DECT, which enables learning the Euler Characteristic Transform (ECT) in an end-to-end fashion. The ECT is a powerful representation that combines geometrical and topological characteristics of shapes and graphs. The authors overcome the computational limitations of the ECT and demonstrate its scalability and integration into deep neural networks. They also show that DECT achieves competitive performance in graph and point cloud classification tasks.

### Strengths
- DECT enables learning the ECT in an end-to-end fashion, overcoming the previous inability to learn task-specific representations.

- The method is highly scalable and can be integrated into deep neural networks as a layer or loss term.

- DECT exhibits advantageous performance in different shape classification tasks for various modalities especially graphs.

### Weaknesses
 - Although ECT is theoretically injective, it happens only when the number of directions is sufficient. For example, for point cloud classification it could be the case that the number of directions is required to be no less than the cardinality of the point set, for ECT to be injective. This restricts the expressivity, especially for the application on point clouds, and explains why the results on point cloud classification is relatively weaker than graph classification. The paper does not adequately address this limitation in terms of the number of directions required for practical applications, especially given the computational cost of increasing the number of directions.

- One key contribution of the method is the differentiation on both the coordinates and the directions \ksi. I would like to see an ablation showing the advantage of being able to optimise the direction \ksi, compared to uniformly sampling the direction. The current results do not sufficiently demonstrate that optimizing the direction \ksi provides a significant advantage over simpler sampling strategies. This is a crucial point, as the optimization of directions adds complexity to the method and needs to be justified by empirical evidence.

- Number of directions \ksi is set as 16 and I would expect an ablation on different numbers. The choice of 16 directions seems arbitrary without any exploration of the impact of this parameter on performance. It is unclear how the performance of the method varies with different numbers of directions, and this could significantly affect the practicality of the proposed method.

-  To apply the method to graph learning, it requires the graph to have spatial coordinates. This requirement limits the applicability of the method to graphs that are embedded in a spatial space. Many graphs in real-world applications do not have such spatial coordinates, and the paper does not discuss how to handle such cases or the potential limitations this imposes.

### Questions
- In Eq 1, (-1)^k should be (-1)^n?

- See weaknesses 2 and 3.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a differentiable version of a geometry descriptor - ECT aka Euler Characteristic Transform, and apply it to the shape classification. In a nutshell, it computes a curve(s) describing a shape (which can be formalized as an exponential family model) as a alternating sum of sigmoids (a "smooth counter" of primitives above / below a collection of hyperplane directions).
Experimental evaluation is provided on a set of benchmarks, and methods performs on-par with a set of GCN-like baselines.

### Strengths
- (Clarity) Paper is well-written and is easy to follow, a concise description of the math background will be appreciated by the readers.
- (Originality) Looking at shape descriptors like ECT and studying their performance on realistic applications seems like a novel direction which could benefit a lot of downstream tasks. 
- (Significance) Method produces close to state-of-the-art results, and also seems to be quite scalable. 
- It looks like the method can also be used when defining loss functions as a way to compare shapes, which is nice.

### Weaknesses
 - (Novelty, minor) One of the main technical contributions of this work is swapping a Dirac function to a sigmoid with a hyperparameter. It is unclear if this is a non-obvious contribution. The use of a sigmoid to approximate the indicator function, while providing differentiability, seems like a relatively straightforward substitution. The impact of the specific choice of sigmoid (e.g., compared to other smooth approximations of the step function) and the sensitivity of the results to the introduced hyperparameter are not thoroughly explored.
- (Evaluation) Not sure if 5.1 is very meaningful - isn't the task trivial? Providing baseline results would help interpretation. The reported results in section 5.1 lack context. Without comparison to simpler methods or a clear explanation of the difficulty of the task, it's hard to assess the significance of the reported performance. Is the task simply to distinguish between a few simple shapes? A more rigorous evaluation with a more challenging dataset would improve the paper.
- (Evaluation) 5.3 - point cloud classification - it is a bit of an overstatement to say that "accuracy of 77%" is "surprising close to" 87.0? The comparison between 77% and 87% accuracy is not as 'surprisingly close' as suggested. A 10% difference in accuracy is significant in many classification tasks. The authors should be more precise in their claims and perhaps provide a statistical analysis of the performance differences.

### Questions
- How important is the differentiability aspect of DECT? E.g. one could potentially take a predefined set of parameters for (6), and use the output of that as a descriptor? Do you actually estimate the parameters of the transform, and does it add to the performance? 
- In Table 2, CNN performs significantly worse than ECT + MLP. A "vanilla" MLP also leads to performance which is quite a bit higher than GCN, which seems strange. Some commentary of reliability of these numbers would be useful.
- (purely out of interest) Would it be possible to combine the proposed description with methods like GCN, e.g. for dense prediction tasks (point cloud segmentation), where descriptor would be per-primitive (e.g. per point).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
