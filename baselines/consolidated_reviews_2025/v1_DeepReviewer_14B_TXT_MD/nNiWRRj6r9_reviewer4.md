### Summary

The paper studies the online $\epsilon$-net problem for geometric concepts with bounded VC-dimension and the online piercing set problem. The authors present the first deterministic online algorithm for intervals in $\mathbb{R}$ with an optimal competitive ratio. They also give a randomized online algorithm with a near-optimal competitive ratio for axis-aligned boxes in $\mathbb{R}^d$ for $d \leq 3$. Furthermore, they introduce a novel technique to analyze similar-sized objects of constant description complexity in $\mathbb{R}^d$. For the online piercing set problem, they propose asymptotically optimal competitive deterministic algorithms for boxes and ellipsoids in $\mathbb{R}^d$ for any $d \in \mathbb{N}$.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper studies the online $\epsilon$-net problem for geometric concepts with bounded VC-dimension, and the online piercing set problem, which are important problems in computational geometry and learning theory.
2. The authors present the first deterministic online algorithm for intervals in $\mathbb{R}$ with an optimal competitive ratio, and a randomized online algorithm with a near-optimal competitive ratio for axis-aligned boxes in $\mathbb{R}^d$ for $d \leq 3$.
3. They introduce a novel technique to analyze similar-sized objects of constant description complexity in $\mathbb{R}^d$, which may be of independent interest.
4. For the online piercing set problem, they propose asymptotically optimal competitive deterministic algorithms for boxes and ellipsoids in $\mathbb{R}^d$ for any $d \in \mathbb{N}$.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on specific types of geometric objects, such as intervals, boxes, and ellipsoids. It is unclear whether the results can be generalized to other types of geometric objects.
2. The paper only provides theoretical analysis of the algorithms. It would be beneficial to have some experimental results to demonstrate the practical performance of the proposed algorithms.
3. The paper does not discuss the limitations of the proposed algorithms and potential future research directions.

### Suggestions

The paper makes a significant contribution by providing optimal competitive ratio algorithms for online ε-nets and piercing sets for specific geometric object types. However, the scope of the results is limited to intervals, boxes, and ellipsoids. It would be valuable to explore the possibility of extending these techniques to more general geometric shapes, such as arbitrary polygons or curved shapes. For instance, could the core ideas of the deterministic algorithm for intervals be adapted to handle more complex object types? This would involve considering how to define a suitable notion of 'piercing' for these objects and how to maintain a competitive ratio in the online setting. Furthermore, the analysis of similar-sized objects of constant description complexity is interesting, but it would be beneficial to see a more detailed discussion of the specific types of objects that fall under this category and the challenges in extending the analysis to objects with varying sizes or more complex structures. This would help to clarify the practical relevance and limitations of this technique.

While the theoretical analysis is strong, the lack of experimental results is a notable weakness. The authors should consider implementing their algorithms and evaluating their performance on synthetic or real-world datasets. This would provide valuable insights into the practical efficiency of the algorithms and their sensitivity to various parameters. For example, how does the performance of the randomized algorithm for boxes scale with the dimension d? Are there specific scenarios where the deterministic algorithm for intervals performs significantly better or worse than the randomized algorithm for boxes? Such experiments would help to validate the theoretical findings and provide a more complete picture of the algorithms' behavior. Furthermore, it would be useful to compare the performance of the proposed algorithms with existing online algorithms for related problems, even if they do not achieve the same theoretical guarantees. This would help to contextualize the contributions of the paper and identify potential areas for future improvement.

Finally, the paper should include a more thorough discussion of the limitations of the proposed algorithms and potential future research directions. For example, are there specific types of geometric objects for which the current algorithms are not applicable or for which the competitive ratios are not optimal? Are there any known lower bounds on the competitive ratio for these problems that the proposed algorithms approach? What are the main challenges in extending the results to higher dimensions or to more general object types? Addressing these questions would provide a more complete understanding of the current state of the art and highlight the open problems in this area. Furthermore, it would be beneficial to discuss potential applications of the proposed algorithms in other areas, such as machine learning or data analysis, and to identify specific research directions that could lead to further advancements in this field.

### Questions

1. Can the results be generalized to other types of geometric objects?
2. Are there any experimental results to demonstrate the practical performance of the proposed algorithms?
3. What are the limitations of the proposed algorithms and potential future research directions?

### Rating

6

### Confidence

3

**********
