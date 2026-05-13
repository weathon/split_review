# Topograph: An Efficient Graph-Based Framework for Strictly Topology Preserving Image Segmentation

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
\iffalse
- Motivation: Topology is important 
- Existing methods either do not provide topo guarantees, work only for specific usecases, or are computationally expensive
- we propose a novel graph-based approach that is generally applicable, holds strict topological guarantees and is computationally efficient
- furthermore, we introduce a topological metric capturing homotopy equivalence between union and intersection of a prediction-label pair
- Our method creates a superpixel graph that completely encodes/captures the topology of prediction and ground truth. This enables us to efficiently identify topologically critical regions (using only a node's local neighborhood), and aggregates a loss for these regions
- we formally prove topological guarantees and empirically validate the effectiveness of our proposed loss on various binary and multi-class datasets compared to the state-of-the art
\fi
Topological correctness plays a critical role in many image segmentation tasks, yet most networks are trained using pixel-wise loss functions, such as Dice, neglecting topological accuracy. Existing topology-aware methods often lack robust topological guarantees, are limited to specific use cases, or impose high computational costs. 
In this work, we propose a novel, graph-based framework for topologically accurate image segmentation that is both computationally efficient and generally applicable. Our method constructs a component graph that fully encodes the topological information of both the prediction and ground truth, allowing us to efficiently identify topologically critical regions and aggregate a loss based on local neighborhood information. Furthermore, we introduce a strict topological metric capturing the homotopy equivalence between the union and intersection of prediction-label pairs. We formally prove the topological guarantees of our approach and empirically validate its effectiveness on binary and multi-class datasets. Our loss demonstrates state-of-the-art performance with up to fivefold faster loss computation compared to persistent homology methods.\footnote{Code is available at \url{https://anonymous.4open.science/r/Topograph}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new loss function, called **Topograph**, for image segmentation, which aims to preserve the topological accuracy of predictions. The authors highlight the importance of **topological correction** in many segmentation tasks, especially in the medical domain where it is crucial for accurate diagnosis and functional analysis. The approach relies on the construction of a component graph that encodes the topological information of both the ground truth and the prediction. 

The main innovations are:
* **A DIU (Discrepancy between Intersection and Union) metric:** This new metric captures topological correctness with strict theoretical guarantees, notably by capturing the homotopy equivalence between the union and the intersection of a label/prediction pair. The DIU metric is more sensitive to fine-grained topological differences than existing metrics such as the Betti number error and the Betti matching error.
* **A graph-based loss function:** This general loss function preserves topology and can be used to train various segmentation networks. It is based on a component graph that combines topological information from the ground truth image and the prediction.
* **Computational Efficiency:** Topograph outperforms existing methods in terms of topological correction of predictions while being efficient in terms of time and resources due to its low asymptotic complexity (O(n α(n))).

### Strengths
0. The paper is clearly written and easy to understand. 

1. The paper presents **theoretical guarantees** for Topograph, demonstrating that if their novel introduced loss is zero, then there is homotopy equivalence. This means that Topograph not only guarantees homotopy equivalence between the ground truth and the segmentation, but also between their union and intersection, thus capturing the spatial correspondence of their topological properties.

2. The approach has a lower complexity than persistent-homotopy (PH) based ones, and, experimentally, a faster running time.  

3. Experimental results show that Topograph improves topological accuracy compared to pixel-based loss functions and other topology-preserving approaches, as shown by the best scores on DIU and BM metrics. At the same time, it maintains pixel-level accuracy comparable to the best benchmarks, indicating that there is no trade-off between pixel-level accuracy and topological correctness.

### Weaknesses
1. The binarization used in Topograph may result in a loss of topological information compared to PH-based methods. It might be possible to extend the construction of the component graph similarly to what is done with component trees (as defined in mathematical morphology), but it is not straightforward to do so. Specifically, the method thresholds the probability maps, which can discard potentially relevant topological features that exist at different intensity levels. For instance, a thin, low-probability connection between two regions might be crucial for topological correctness but could be eliminated by a single threshold, while PH methods would retain this information through persistence analysis. This loss of information could be particularly problematic in cases where the intensity variations within the image carry significant topological meaning.

2. The method is currently limited to 2D images. Its extension to 3D images is considered, but I believe it is not obvious to do. The component graph as currently defined is difficult to extend to 3D. The current approach relies on a 4-connectivity for defining connected components, which is not directly transferable to 3D where 6- or 26-connectivity are more common. Furthermore, the topological features in 3D are more complex, involving not only connected components but also tunnels and voids, which are not captured by the current component graph. The method's reliance on a simple graph structure may not be sufficient to represent the more intricate topological relationships present in 3D data.

### Questions
Although the method demonstrates superior results in 2D, I am not convinced that it will be easy to extend to 3D, and I would like to understand the authors' intuition and thoughts about a 3D extension. The authors may want to discuss some specific challenges they anticipate in extending Topograph to 3D, and to outline potential strategies they are considering to address these challenges.

Regarding the binarization, I am wondering if it is possible to quantify or estimate how much topological information is lost through
the binarization approach compared to PH methods. Is it possible to suggest some strategy that mitigate this information loss while maintaining Topograph computational efficiency advantages?

### Soundness
4

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
2

### Summary
The authors present a method to address the segmentation problem with a focus on preserving the topology of segmented regions. They also introduce a metric for evaluating the accuracy of the predicted segmentation. The proposed approach consists of several stages: (1) The input image is binarized and overlapped with ground truth segments; (2) A graph is constructed based on this overlapped image; (3) Superpixels are created, with each node in the graph representing a superpixel; (4) A set of misclassified nodes is identified, and nodes that do not impact topological structure are removed; (5) Optimization is performed only on the nodes in this remaining set. The authors evaluate their method on multiple datasets using a range of metrics.

### Strengths
The proposed method seems to preserve the topology of segmented regions, addressing a challenge in segmentation tasks.

### Weaknesses
The minimization problem formulation is not well-defined (objective function, parameters, and regularization).

### Questions
How does the method handle edge cases with the $\alpha$ parameter? Specifically, what is the outcome if $\alpha$ is set to 0 or to a very large value?

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
3

### Summary
This paper presents a method that improves the topological consistency of segmentation while preserving overall performance, like IoU. Besides, a more topologically precise metric is also introduced in this paper.

### Strengths
1. The method proposed in this paper demonstrates a better solution for tasks emphasizing topological accuracy. 
2. Besides, a new metric aims at topology consistency is also presented showing it's advantage over previous ones.
3. With a lower asymptotic complexity, the loss introduced in this paper can be computed in linear time which make the loss easy to implement.

### Weaknesses
1. The proposed method works well with relatively small datasets and UNet with fewer parameters. My concern is that if we have a larger dataset, can we achieve similar performance with a larger model without the implementation of Topograph? Specifically, it's unclear if the topological improvements are maintained when the model capacity and data scale increase, or if the benefits diminish as the model learns to fit the data more closely, potentially making the topological loss less impactful. It would be beneficial to see experiments with larger models and datasets to understand the scalability of this approach.
2. In terms of binarization, this paper suggests that introducing a small random value would be helpful. But could it be beneficial if applied automatic thresholding like Otsu method? The paper does not explore alternative thresholding methods, which could potentially offer more robust and adaptive binarization strategies. The current approach relies on a fixed threshold with random variation, which might not be optimal for all datasets or scenarios. Exploring methods like Otsu's could provide a more principled way to determine the threshold.
3. In terms of DICE, Topograph seems to have similar performance with other methods. Is that indicating a tradeoff between topological critical pixels and topological irrelevant pixels? It's unclear whether the topological improvements come at the expense of pixel-wise accuracy. The similar Dice scores suggest that the method might be prioritizing topological correctness over overall segmentation accuracy, potentially leading to a trade-off where some pixel-wise errors are introduced to correct topological errors.

### Questions
See Weakness.

### Soundness
4

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
The authors present a novel loss and a novel error metric for topology-aware image segmentation. The loss reflects homotopy equivalence between union and intersection of predicted and ground truth-segmentation. It is computed by establishing a component graph on (thickened/thinned) TP, FP, TN and FN components, and identifying "regular" vs non-regular nodes in the graph, where non-regular nodes point to topology-critical, spatially meaningful pixels in the prediction which are then penalised by the loss. Computation is 3-6 times faster than for related works on persistent homology-based losses.

### Strengths
The work provides an efficient loss that is nevertheless formally grounded, with strong topological guarantees. A comprehensive evaluation shows its strengths over existing approaches. Rich figures (also in the supplement) greatly facilitate the read.

### Weaknesses
-- Some definitions are not comprehensive and some Figures appear to be not in line with the text, making the work hard to grasp (see Questions)

-- A more thorough discussion of some related work might render the work significantly more insightful (see Questions)

-- The authors do discuss the 2d nature of the presented approach as a limitation. However, to clearly convey the significance of this limitation, it should be mentioned in this context that their evaluation features some 3d data (evaluated as 2d slices) -- here, imposing a 2d topological loss on slices appears unsuitable / overly strict.

-- The definition of 'nontrivial' intersection of closures is unclear. It seems to imply a non-empty intersection, but this would lead to edges between TP and TN components in the component graph, violating the bipartite nature of the graph. The figures are inconsistent in this regard, with some showing edges between TP and TN (e.g., Fig. 2) and others not (e.g., Fig. 3). This inconsistency makes it difficult to understand the precise construction of the component graph and the topological guarantees of the method. The corrected Fig. 2 still shows four points in the intersection of TPs and TNs, which are finite, further highlighting the ambiguity of the definition.

-- The relationship between the proposed DIU metric and common segmentation error metrics, such as 'false split' and 'false merge' errors, is not clearly established. While the authors mention the DIU metric captures topological errors, it is not clear how this relates to the more intuitive notions of over- and under-segmentation. A more detailed discussion of how these metrics compare and contrast, especially in edge cases, would be beneficial. The current discussion does not fully clarify whether DIU is a simple sum of false splits and merges or if it captures more complex topological errors.

-- The discussion of related work is incomplete. For example, the work by Funke et al. (2018) is cited as having a PH-based loss function, which is incorrect. The relation of the proposed method to their loss, which also focuses on topologically critical regions that are spatially correct, should be discussed in more detail. Additionally, the work by [1] is not discussed, despite being highly relevant to the problem of segmentation error evaluation in connectomics, which is a key application area for the proposed method.

### Questions
Re clarity:

-- "Nontrivial" intersection of closures (p. 4 l. 190) needs to be precisely defined (i.e., please provide a formal definition) -- I guess it has to mean "not finite", otherwise there could be edges between TP and TN and the component graph would not be bipartite? This confusion is furthered by Fig. 2 (see below) where such edge is actually present (so does "nontrivial" mean non-empty after all? but how is the comp. graph bipartite then?); Also, the respective edge is not present in Fig. 3. Please clarify.

-- In Fig. 2 (bottom right) the prediction foreground appears double-thickened, while later you settle for double-thickening of ground truth foreground; this causes an edge between intersection and background in Fig. 2 which should not be there and causes confusion; The same edge is also present in Fig. 7.3 -- I do not understand why; Same holds for the edge from the rightmost (thin) FN component to the spurious component in Fig. 7.3, I do not understand why this is there -- shouldn't it go from the FN component directly to the background node? 

Re rel. work:

-- E.g., how is the DIU metric related to the common practice of counting "false split" and "false merge" errors, as commonly done for segmentation problems (cf [1] for one out of many examples where these are evaluated)? Could it be that DIU is the sum of false splits and false merges (at least for dim. 0 features?)? If not, do you see any other relation?

-- A discussion of [1] as related work appears warranted

-- Funke et al. (2018) is listed in rel. work as having a PH-based loss function, but this is not correct? Please discuss in more detail the relation of your work to their loss, which also focuses on topologically critical regions that are spatially correct

[1] https://doi.org/10.1016/j.ymeth.2016.12.013

Minor: 

-- A pointer to Fig. 11 earlier in the text would be very helpful, latest on page 6 line 297 (in addition to pointing to Fig. 3)

### Soundness
3

### Presentation
3

### Contribution
3
