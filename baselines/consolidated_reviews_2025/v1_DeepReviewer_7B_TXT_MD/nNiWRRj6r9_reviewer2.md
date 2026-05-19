### Summary

The paper studies the online epsilon-net problem and the online piercing set problem. For the online epsilon-net problem, the authors study the problem for intervals, axis-parallel boxes, and axis-parallel boxes in R^d. For the online piercing set problem, the authors study the problem for intervals, axis-parallel boxes, and axis-parallel boxes in R^d. The authors show that the competitive ratios of the online algorithms are tight for intervals and axis-parallel boxes in R^d.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper studies the online epsilon-net problem and the online piercing set problem, which are important problems in computational geometry.
2. The paper shows that the competitive ratios of the online algorithms are tight for intervals and axis-parallel boxes in R^d.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide any experimental results to validate the performance of the proposed algorithms.
2. The paper is quite dense and may be challenging to read for people who are not familiar with the field.

### Suggestions

The lack of experimental validation is a significant weakness. While theoretical analysis is crucial, it's essential to demonstrate the practical relevance of the proposed algorithms. The authors should consider conducting experiments on both synthetic and real-world datasets. For instance, they could generate synthetic datasets with varying sizes, shapes, and distributions of intervals and axis-parallel boxes, and then evaluate the performance of their online epsilon-net and piercing set algorithms. This would involve comparing the competitive ratios achieved by their algorithms against known lower bounds or against simpler heuristics. Furthermore, the authors could explore the sensitivity of their algorithms to different parameters, such as the size of the input stream or the distribution of the geometric objects. Such experiments would provide valuable insights into the practical applicability of their theoretical results and help identify potential limitations or areas for improvement.

To improve the accessibility of the paper, the authors should consider adding more intuitive explanations of the key concepts and techniques. The current presentation is quite dense, and readers unfamiliar with the field may find it challenging to follow the arguments. This could involve using more visual aids, such as diagrams and illustrations, to explain the geometric objects and the algorithms. Additionally, the authors could provide more concrete examples to illustrate the behavior of the algorithms and the competitive ratios. For example, they could show how the algorithms perform on specific instances of the problem, such as a set of intervals or rectangles with varying sizes and shapes. This would help readers to better understand the practical implications of the theoretical results. The authors should also consider adding a section that summarizes the main results and provides a high-level overview of the techniques used in the paper, making it easier for readers to grasp the key contributions.

Finally, the authors should consider providing a more detailed discussion of the limitations of their approach. While the paper presents tight competitive ratios for intervals and axis-parallel boxes in R^d, it would be beneficial to discuss the challenges in extending these results to more complex geometric objects or higher dimensions. For example, the authors could discuss the computational complexity of their algorithms and whether they can be efficiently implemented in practice. They could also explore the possibility of developing approximation algorithms with better performance guarantees. A thorough discussion of these limitations would provide a more balanced view of the paper's contributions and help guide future research in this area.

### Questions

1. Can the authors provide any experimental results to validate the performance of the proposed algorithms?
2. Can the authors provide a more intuitive explanation of the key concepts and techniques used in the paper?

### Rating

6

### Confidence

3

**********
