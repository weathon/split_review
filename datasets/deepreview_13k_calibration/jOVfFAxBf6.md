# Bi-continuous and complete SE(2)-invariants parametrize all clouds of unordered points

- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 6, 6, 3

## Abstract
The most basic form of a rigid object is a cloud of unordered points, for example, a set of corners or other salient features. The rigid shape of a point cloud in the Euclidean plane is its SE(2)-equivalence class under rigid motion (a composition of translations and rotations). We introduce complete invariants (with no false negatives, no false positives) and a bi-Lipschitz continuous metric that satisfies all axioms, provides a 1-1 matching between points in clouds, and is computable in a quadratic time of the number $m$ of points.  The realizability property implies that the space of all rigid clouds is efficiently parametrized by vectorial invariants like geographic coordinates. The new invariants justified that any of 130K+ molecules in the QM9 database is uniquely determined by the rigid shape of its atomic cloud.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces an invariant and metric for unordered point clouds in the Euclidean plane, designed to meet specific desirable properties. The invariant is complete, ensuring that two point clouds related by a rigid transform can be uniquely matched. It is also realizable, enabling the reconstruction of the point cloud from the invariant up to an unknown rigid transform. The metric is Lipschitz continuous, meaning that bounded perturbations in the point cloud result in bounded changes in the distances between the invariants. Additionally, it guarantees that two close invariants correspond to point clouds that can be matched through a rigid motion, with a small Euclidean distance between matching points. Both the invariant and the metric are computable in polynomial time.

The paper includes experiments in chemistry using a publicly available dataset, demonstrating the method’s ability to identify closely related molecules based on the positions of their atom centers.

### Strengths
The paper formally defines the problem of finding complete invariants and their corresponding metric for clouds of unordered points, providing formal proofs for all proposed solutions.  According to the authors, this is the first complete invariant and associated metric fulfilling the conditions proposed in the paper. In this regard, the paper makes a significant theoretical contribution to the field.

The method's practical applicability is demonstrated through experiments in molecule matching within the field of Chemistry. The completeness of the invariant has a real impact on the results, separating molecules that are at a close distance from other invariants and metrics from the state-of-the-art.

Additionally, the paper includes extensive appendices that extend the invariant to any dimension d>2

### Weaknesses
The main issue with the paper is its readability, which is affected by several factors:

- Notation is introduced gradually throughout the paper, making it difficult to refer to where certain concepts are defined. This requires extensive back-and-forth searching, disrupting the reading flow. While Table 1 attempts to consolidate key acronyms, it does not fully mitigate the issue of gradual introduction, as the reader still needs to trace back to the original definitions within the text.
- The number of acronyms is excessive and often very similar (e.g., NDP, NCP, BMD, NBM), making them hard to distinguish. Using different names or aliases could help reduce this confusion. The similarity between NDP and NCP is particularly problematic, as they represent related but distinct concepts within the same definition, increasing the cognitive load on the reader.
- Some sections of the paper lack clarity, such as the computation of the Bottleneck Distance in Definition 4.1. While the paper references Efrat et al. (2001) for the computational algorithm, the specific steps involved in applying that algorithm to the context of the defined invariant are not sufficiently detailed, leaving the reader to infer the connection.
- The paper does not follow a traditional structure and lacks a conclusion section. While the paper includes concluding remarks in Section 6, they are not presented as a distinct conclusion section, which is typically expected in academic papers to summarize the key findings and contributions.
The length of the paper and appendices is overwhelming. The extension for d>2 dimensions should be in a separate paper to better focus the content.

The invariant and metric are more computationally complex than other existing (incomplete) invariants and metrics.

### Questions
Q1: More insight is needed on the NBM computation in Definition 4.1. How is it derived using Efrat et al. (2001)? Additionally, why does the Point-Based Representation Metric require normalization for rigid motions without scale difference?

Q2: Corollary 5.5 on continuous morphing requires further clarification. How is the continuous path defined between NDP(A) and NDP(B)?

Q3: What would be the impact of the proposed invariant and its metric when applied to learning-based approaches?

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel approach to parametrize and analyze clouds of unordered points in the Euclidean plane, with a focus on their rigid shape under translations and rotations. The authors give a rigorous theoretical foundation for the proposed invariant and metric, proving their properties and demonstrating their effectiveness in higher dimensions. Experiments on QM9 database also reveal the efficacy of the designed invariant and metric.

### Strengths
1. The authors solve a central problem, i.e., Problem 1.1 defined in the paper, which aims finding an invariant that satisfies completeness, metric axioms, Lipschitz continuity, realizability, point matching, and computability in polynomial time.

2. The methods and results are not limited to two dimensions.

### Weaknesses
1. Although the proposed invariants are bi-Lipschitz continuous, meaning they mainly maintain a continuous relationship regarding small perturbations in the point cloud. This maybe difficult for large perturbations.  

2. The method can be extended to higher dimensions, but the computational complexity in determining the invariants and metrics could become more demanding. Similarly, the method's scalability, especially for very large point clouds, might also be a concern. Specifically, the nested nature of the complete invariant, while theoretically sound, could lead to significant computational overhead when dealing with large datasets or high-dimensional spaces, potentially limiting its applicability in real-world scenarios where efficiency is paramount. 

3. My another concern is regarding the experiments. The current experiments are primarily conducted on the QM9 database of molecules. While this provides a strong proof of concept, the method's performance in other domains, such as different types of geometric data or in higher dimensions, requires further investigation. The reliance on a single dataset, even one as comprehensive as QM9, raises questions about the generalizability of the findings. It would be beneficial to see results on datasets with different characteristics, such as those with varying point densities or noise levels, to fully assess the robustness of the proposed approach.

### Questions
Please see the weakness part.

### Soundness
2

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
3

### Summary
The paper studies unordered points-clouds in n-dimensional Euclidean space, under the equivalence of rigid motion (translation and rotation).
The main idea, which extends previous limited attempts, is in defining a *complete invariant*, which is a function that maps an m-point point-cloud to a point in a higher dimemsional space, over which a metric is defined such that point-coulds are mapped to a single point if and only if they are equivalent. In addition, the invariant is proven to have several other desired properties, such as bi-directional Lipschitz continuity and efficient ways to compute both directions of the mapping as well as and an approximate rigid motion for point-clouds that are close to being equivalent.
The requirements of the invariant are stated in a main Problem, followed by a detailed construction, with full proofs for the claimed properties (in the appendix).
An experimental section focuses on analyzing a large-scale dataset of 3D molucule structures, with the focus being on differentiating the proposed NDP from previous invariants (which are generally much faster to compute, but are not complete - i.e. they might map non-equivalent clouds to a single point).

### Strengths
1] The paper is well written - I like the way that the limitations in previous work are clearly presented, including by simple examples, and the decision to present the ideas in 2D and defer the proofs to the appendix. Writing is very accurate, but at the same time accessible to non-experts. 
2] I believe that the new characterization (in Problem 1.1) of the conditions required from the parameterization captures different desired properties of such invariants in a good way, including the addition of properties like 'point-matching' and 'realizability' that were lacking in previous definitions. This definition, includes some properties, which were not demonstrated to be useful, but might be so in different applications. Especially, the bi-directional continuity, which gives a type of smoothness that might be useful for settings where one is interested with approximate forms of equivalence.
3] The discussions and examples for the 2D case of m=3 (triangles) and m=4 (quads) is very helpful for understanding both the limitations of previous work as well as the specifics of the construction, including very good visualizations.
4] The experiment is very original and interesting. It is done in a clever way, by hierarchically classifying pairs as being different, by gradually increasing the quality of the invariant. It is nicely shown on data that is real, even though not including measurement noise, with true new conclusions (that I presume were unknown) that could not be made using the reference techniques.

### Weaknesses
1] While the suggested parameterization is an elegant mathematical result, with clear progress made, it's applicability is still questionable. Computationally, the quadratic complexity in the number of points is clearly prohibitive, making it impractical for most real-world point-cloud datasets, or general n-dimensional sets (e.g., of features). The paper could have benefited from a more thorough discussion of the computational bottlenecks and potential strategies to mitigate them. The focus on *completeness* of the invariance, while mathematically interesting, seems less relevant for real-world data, where exact equivalence is rare due to noise and measurement errors. In such scenarios, the robustness and stability of the invariant under perturbations become more critical than its completeness. The bi-directional Lipschitz continuity is indeed a valuable property, but its practical implications need to be more thoroughly explored, especially in the context of noisy or incomplete data.
2] The experimental section focuses primarily on demonstrating the advantage of the proposed invariant in terms of its completeness, but it does not sufficiently analyze the benefits of the other properties, such as bi-directional Lipschitz continuity. While the hierarchical approach is interesting, the experiment does not provide a clear picture of how the proposed invariant behaves under different types of perturbations, such as measurement noise, non-rigid transformations, or partial overlaps. It would be beneficial to see a more detailed analysis of the invariant's performance in such scenarios, perhaps through controlled synthetic experiments. The current experiment, while original, is somewhat limited in its scope, focusing on exact equivalence rather than the more common scenarios where approximate equivalence is more relevant.
3] There is a lack of discussion on how the proposed invariant could be integrated into more common tasks performed on unordered point-clouds. The paper does not address how the proposed method could be beneficial for tasks such as alignment (perhaps with noise or partial overlap), classification, detection, segmentation, or generative modeling. The potential for using the invariant in these contexts is not explored, which limits the practical impact of the work. The paper would be strengthened by a discussion of how the proposed invariant could be adapted or extended to address these common point-cloud processing tasks.

Some typos/mistakes:
* Wrong referencing, e.g. in lines 81 and 86
* bipartute (line 321)
* 'one four pairs' (line 336)
* sayss (line 411)

### Questions
1] I'm note sure whether there is a clear charcterization regarding what are the cases in which one would decide to use the suggested NDP, over the simpler and cheaper alternatives. Is there a principled way the you would suggest? The 'hierarchical' way used seems to only be suitable for the particular case of classifying data by exact equivalence (where the cheaper invariants provide fast 'rejection'). 
2] It is claimed in the experiment that the NDP provides best seperation. Is there any evidence that the metric on it is well aligned with what would be considered a good measure for the distance from being equivalent (under rigid transformation)? Have you tried testing how it looks when starting from perfect equivalence and degrading in different ways (such as noise in the points, or non-perfect rigidity)?
3] Computation wise - Are there relaxations with major gains that could make the approach more practical? Such as computing smoother (non permutation-like 1-1 mappings) matchings?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper addresses the problem of the exact matching of full (not partially observed, as in e.g. CV/LIDAR data) point clouds. It proposes a descriptor (NDP/NCP) that can uniquely identifies a specific point cloud and from which a unique point cloud can be reconstructed, as well as a distance metric (NBM) between point clouds that permits exact identification and is proven to be Lipschitz-smooth. The descriptor requires set matching for point cloud matching though - it cannot be directly compared by comparing descriptor vectors. The main paper discusses the 2D case; general dimensions (as well as all of the proofs) are presented in the appendix.

The writing of the paper is quite technical, so I might be missing something important somewhere. To the best of my understanding, the whole method hinges on the well-known fact that one needs only $d$ point-to-point correspondences (with linearly independent difference vectors) to fix a rigid mapping in $d$ dimensions (because a rigid coordinate frame can be derived from these), which makes searching for correspondences under rigid mappings much easier than general correspondence problems.

Naively, one could fix one reference point (e.g., the center of mass) and try correspondences between one (in 2D, two in 3D, etc.) of the source and every single target points (in 2D, all possible pairs in 3D, etc.) to find the mapping and efficiently check whether the clouds match. The complexity is polynomial for each fixed $d$ and exponential in $d$.

The paper exploits this mathematical fact (not sure if implicitly or explicitly) and builds systematically enumerates all coordinate frames in a single point cloud by using the center of mass and every point in the cloud as correspondences. The center of mass must match, thus only all other points have to be considered. It projects into the coordinate system induced by the difference to the center (scaled by the length of this vector to maintain smoothness) and then enumerates all of the points, giving an $O(n^2)$ representation of $n$ points (there are $O(n)$ coordinate frames with $O(n)$ entries each). The descriptor is then the set of the set of points. By comparing these via set-matching, exact matches can be found in polynomial time. 

To compute distances, a cascade of two perfect bi-partite graph matching steps is used to first reconstruct a good ordering of the rotated and scaled copies of the point cloud and then match their points as much as possible. The paper states a theorem and provides a proof for Lipschitz-continuity of this process (which involves discrete decisions).

Finally, the paper shows some examples of comparing point clouds using the QM-9 data set as an example.

### Strengths
The paper seems to provide a solution for the rigid point cloud comparison problem that addresses all of the formal requirements that one would probably desire in theory and practice (with the exception, as far as I understand, of encoding the descriptor as a vector in a linear vector space with simple $L_p$ distance and literal equality computations, which would be useful for efficient querying in geometric data bases).
It makes great effort in formalizing requirements and formally proving the results, and gives a comprehensive account of a broad set of earlier work. It also provides examples to illustrate the challenges of distance-based rigidity.
If my understanding of the method outlined above is correct, I would also see the method as in its core rather straightforward and easy to understand, which increases confidence in correctness and might make it easier to implement the ideas in other contexts.

### Weaknesses
My understanding of potential weaknesses hinges upon my understanding of the method as a whole; as the paper is technical and extensive, I might be misunderstanding something.

A major restriction of the submission is its focus on exact matching of full point clouds, excluding partially acquired data and significant outlier issues, both of which is very common in practical handling of, for example, 3D point clouds acquired from real-world scenes (for cases like molecular data bases, such as QM-9, this restriction probably does not matter). The exact matching is relaxed by providing a continuous metric, but partial matching still remains impossible. The method is also restricted to rigid motions, and due the exponential costs in $d$, it can only be realistically applied to low-dimensional data.

I think that the exact matching algorithm, which is described first, is not very useful: First, it is not new - guessing a small number of point-wise correspondences, e.g. via RANSAC or randomized forward-search, and then verifying the match is an established technique, see e.g. [Huang et al., Reassembling Fractured Objects by Geometric Matching, Siggraph 2006], which is already robust to deteriorated and partial data. Second, it requires a large amount of memory (squared the number of input points) and accordingly significant runtimes, which can be avoided by not storing the intermediate results and using heuristics filters in matching candidates (such as Huang et al.'s and many similar papers), as well as by implicitly excluding impossible matching candidates (see e.g. 4PCS-Matching [Aiger et al., Siggraph 2008]).

The continuous metric, on the other hand, is a bit more interesting. While the basic procedure (using bi-partite graph matching to find the closest matching points) seems again to be a canonical path for comparing full point clouds, the design of two nested matching procedures does not appear very straightforward, and the smoothness guarantees obtain in that way might be appealing in applications where such a tool is needed. Unfortunately, I have not been able to verify the formal proof, but the intuitively, the I would assume that this should work (as nearest points change discretely, but only at points where distances coincide, thus plausibly maintaining smoothness).

The writing of the paper could be improved. While I would see the strive for a formal treatment positively, the paper in its current form, to a reader like me (different people have of course different inclinations to intuition vs. abstraction) seems to obscure the main ideas behind formal details to much. Then, the appendix, where a lot of the most interesting contributions reside (such as proofs of the theorems), is even harder to parse. For example, I was looking the proof of Theorem 3.5, where I would see a minor technical difficulty but could only find a treatment of a much more general statement in arbitrary dimensions, which made it very difficult to verify the statements made in the paper. In my perception, one could reorganize and rephrase the text to make everything much more accessible. Overall, I have to say that I was not able to read and understand much of the appendix in its current form (maybe fellow reviewers who were able to can give a better assessment of the overall work).

Finally, I see a small technical issue in Theorem 3.5: The representation computed for the NDP/NCP descriptors consists of a set of matrices (in a tuple with the base-point distance), which are compared by equality. The matrices are descriped as unordered in terms of the ordering of the 2D points (after projection, which is of course ordered by the two coordinate axes). Comparing sets then implicitly matches the unordered matrices, restoring correspondences between rearranged points. However, within the matrices, a "standard" equality / comparison would perform a column-wise comparison, which matches points in the specified order, which can differ between point clouds A and B to be matched. I think that here, again, a set comparison rather than a column-wise matrix comparision would be required. The continuous metric uses two nested linear assignment / bi-partite graph matching steps, the inner one corresponding to such a (soft) set matching here.

Overall, I think that the paper is (most likely, limited by my ability to follow the appendix and some remaining doubts wrt. potential misunderstandings) correct in essence and solves the problem that it states. However, the conceptual step over known work seems a bit narrow to me (given the limited setup and that we do not get vector-valued invariants but only an encoding of point matching / finding of closest points in mathematical language), potentially with the exception of proving continuity. However, that part was hard to understand. The set of practical problems that can be solved with the new proposal but not with already known methods also seems to be limited (in particular given the large costs). The problem statement also seems to be to some degree tangential to the focus of ICLR.

### Questions
First of all, it might be possible that I fundamentally misunderstand how all of this work - then it would be important to rectify this. If not, I would be curious about the matrix-matching problem discussed above.

### Soundness
3

### Presentation
2

### Contribution
2
