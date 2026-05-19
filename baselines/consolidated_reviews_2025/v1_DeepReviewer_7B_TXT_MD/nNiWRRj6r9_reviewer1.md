### Summary

This paper studies the online version of two classic geometric set cover problems, namely the online epsilon-net problem and the online piercing set problem. In the epsilon-net problem, the goal is to find a small-size epsilon-net (a set of points that intersects every large enough geometric object) for a given set of geometric objects. In the online version, the input is a stream of geometric objects, and the algorithm needs to maintain an epsilon-net for the current set of objects. The competitive ratio of the algorithm is the maximum ratio between the size of the epsilon-net maintained by the algorithm and the size of the optimal epsilon-net. The paper studies the online epsilon-net problem for intervals, axis-parallel rectangles, and axis-parallel boxes in R^d, and the online piercing set problem for intervals, axis-parallel rectangles, and axis-parallel boxes in R^d. For the epsilon-net problem, the paper gives tight competitive ratios for intervals and axis-parallel boxes in R^d. For the piercing set problem, the paper gives tight competitive ratios for intervals and axis-parallel boxes in R^d.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper is well-written and easy to follow. The results are interesting and contribute to the understanding of the online versions of the epsilon-net and piercing set problems. The paper gives tight competitive ratios for a wide range of geometric objects, including intervals, axis-parallel rectangles, and axis-parallel boxes in R^d. The techniques used in the paper are novel and interesting.

### Weaknesses

#### Some Related Works


#### comment

The paper is purely theoretical and does not have any practical implications. The algorithms and techniques used in the paper are quite complex and may be difficult to implement in practice. The paper does not provide any experimental results to validate the performance of the proposed algorithms. The paper is quite dense and may be challenging to read for people who are not familiar with the field.

### Suggestions

The paper would benefit significantly from a more thorough discussion of the practical implications of the proposed algorithms. While the theoretical results are interesting, the lack of connection to real-world applications limits the impact of the work. For instance, the authors could explore how their algorithms could be adapted for use in sensor networks, where data arrives in a streaming fashion and efficient coverage is crucial. This would involve not only adapting the algorithms but also considering the computational overhead and memory requirements in a resource-constrained environment. Furthermore, the authors could discuss the limitations of their approach in practical settings, such as the assumption of uniform distribution of objects, which may not hold in many real-world scenarios. A more detailed analysis of the trade-offs between the competitive ratio and the computational cost would also be valuable.

To improve the accessibility of the paper, the authors should consider providing more intuitive explanations of the key concepts and techniques. The current presentation is quite dense, and readers unfamiliar with the field may find it challenging to follow the arguments. This could involve using more visual aids, such as diagrams and illustrations, to explain the geometric objects and the algorithms. Additionally, the authors could provide more concrete examples to illustrate the behavior of the algorithms and the competitive ratios. For example, they could show how the algorithms perform on specific instances of the problem, such as a set of intervals or rectangles with varying sizes and shapes. This would help readers to better understand the practical implications of the theoretical results. The authors should also consider adding a section that summarizes the main results and provides a high-level overview of the techniques used in the paper.

Finally, the lack of experimental results is a significant weakness. While the theoretical analysis is important, it is crucial to validate the performance of the proposed algorithms through empirical evaluation. The authors should consider conducting experiments on synthetic or real-world datasets to assess the practical performance of their algorithms. This would involve comparing the performance of their algorithms with existing approaches and evaluating the trade-offs between the competitive ratio and the computational cost. The experiments should also consider different parameters, such as the size and shape of the objects, to understand the sensitivity of the algorithms to these factors. The authors should also discuss the limitations of their experimental setup and the potential for future work in this direction.

### Questions

1. How do the proposed algorithms perform in practice? Can the authors provide any experimental results?
2. Can the authors provide any practical applications of the proposed algorithms?
3. Can the authors provide a more intuitive explanation of the key concepts and techniques used in the paper?

### Rating

6

### Confidence

3

**********
