### Summary

The paper studies the online version of the epsilon-nets and piercing set problems. While the offline version of these problems has been extensively studied, there are no known theoretical results for the online version. The authors present the first deterministic online algorithm with an optimal competitive ratio for intervals in R. They also give a randomized online algorithm with a near-optimal competitive ratio for axis-aligned boxes in R^d, for d≤3. Furthermore, they introduce a novel technique to analyze similar-sized objects of constant description complexity in R^d. For the online piercing set problem, they propose asymptotically optimal competitive deterministic algorithms for boxes and ellipsoids in R^d, for any d∈N.

### Soundness

3

### Presentation

2

### Contribution

3

### Strengths

1. The paper studies the online version of the epsilon-nets and piercing set problems, which are fundamental concepts in statistical learning theory and discrete geometry. The online version of these problems has not been extensively studied before, and the authors make significant progress in this area.

2. The authors present the first deterministic online algorithm with an optimal competitive ratio for intervals in R. They also give a randomized online algorithm with a near-optimal competitive ratio for axis-aligned boxes in R^d, for d≤3. These results are significant contributions to the field of online algorithms.

3. The authors introduce a novel technique to analyze similar-sized objects of constant description complexity in R^d. This technique may be of independent interest and could be useful in other areas of computer science.

4. For the online piercing set problem, the authors propose asymptotically optimal competitive deterministic algorithms for boxes and ellipsoids in R^d, for any d∈N. These results are also significant contributions to the field of online algorithms.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on specific types of geometric objects, such as intervals, boxes, and ellipsoids. It is unclear whether the results can be generalized to other types of geometric objects.

2. The paper only provides theoretical analysis of the algorithms. It would be beneficial to have some experimental results to demonstrate the practical performance of the proposed algorithms.

3. The paper does not discuss the limitations of the proposed algorithms and potential future research directions.

### Suggestions

The paper makes significant theoretical contributions by providing optimal competitive ratio algorithms for online epsilon-nets and piercing sets for specific geometric object types. However, the scope of the results is limited to intervals, boxes, and ellipsoids. It would be valuable to explore the possibility of extending these techniques to more general geometric shapes, such as arbitrary polygons or curved shapes. For instance, could the core ideas of the deterministic algorithm for intervals be adapted to handle more complex object types? This would involve considering how to define a suitable notion of 'piercing' for these objects and how to maintain a competitive ratio in the online setting. Furthermore, the analysis of similar-sized objects of constant description complexity is interesting, but it would be beneficial to see a more detailed discussion of the specific types of objects that fall under this category and the challenges in extending the analysis to objects with varying sizes or more complex structures. This would help to clarify the practical relevance and limitations of this technique.

While the theoretical analysis is strong, the lack of experimental results is a notable weakness. The authors should consider implementing their algorithms and evaluating their performance on synthetic or real-world datasets. This would provide valuable insights into the practical efficiency of the algorithms and their sensitivity to various parameters. For example, how does the performance of the randomized algorithm for boxes scale with the dimension d? Are there specific scenarios where the deterministic algorithm for intervals performs significantly better or worse than the randomized algorithm for boxes? Such experiments would help to validate the theoretical findings and provide a more complete picture of the algorithms' behavior. Furthermore, it would be useful to compare the performance of the proposed algorithms with existing online algorithms for related problems, even if they do not achieve the same theoretical guarantees. This would help to contextualize the contributions of the paper and identify potential areas for future improvement.

Finally, the paper should include a more thorough discussion of the limitations of the proposed algorithms and potential future research directions. For example, are there specific types of geometric objects for which the current algorithms are not applicable or for which the competitive ratios are not optimal? Are there any known lower bounds on the competitive ratio for these problems that the proposed algorithms approach? What are the main challenges in extending the results to higher dimensions or to more general object types? Addressing these questions would provide a more complete understanding of the current state of the art and highlight the open problems in this area. Furthermore, it would be beneficial to discuss potential applications of the proposed algorithms in other areas, such as machine learning or data analysis, and to identify specific research directions that could lead to further advancements in this field.

### Questions

1. Can the results be generalized to other types of geometric objects?
2. Are there any experimental results to demonstrate the practical performance of the proposed algorithms?
3. What are the limitations of the proposed algorithms and potential future research directions?

### Rating

6

### Confidence

4

**********
