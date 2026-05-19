### Summary

The authors study the problem of computing a coupling between two distributions with a small amount of joint entropy. They unify existing iterative approaches to this problem under a single formalism, and derive a new algorithm, ARIMEC, that can handle arbitrary discrete distributions. They also introduce a technique to make the algorithm robust to suboptimal hyperparameter settings. The authors evaluate their approach in two settings: Markov coding games and steganography.

### Soundness

4

### Presentation

4

### Contribution

3

### Strengths

* The paper is very well written and easy to follow.
* The authors provide a unifying framework for existing iterative approaches to the minimum entropy coupling problem, which is a nice contribution in itself.
* The new algorithm, ARIMEC, seems to be a significant improvement over existing methods, especially in terms of its ability to handle arbitrary discrete distributions.
* The authors also introduce a technique to make the algorithm robust to suboptimal hyperparameter settings, which is a valuable contribution.
* The authors provide a thorough evaluation of their approach in two different settings, which demonstrates its effectiveness.

### Weaknesses

#### Some Related Works


#### comment

 * The paper could benefit from a more detailed discussion of the limitations of the proposed approach. For example, how does the performance of ARIMEC scale with the size of the input distributions? Are there any specific types of distributions for which ARIMEC is not well-suited? While the authors mention that the algorithm can handle arbitrary discrete distributions, it would be helpful to understand the practical limitations in terms of computational resources and time complexity. For instance, how does the runtime grow with the number of states in the distributions, and what are the memory requirements for storing intermediate results? A more thorough analysis of these aspects would be beneficial.
* The paper could also benefit from a more detailed comparison to existing methods. While the authors mention that ARIMEC is an improvement over existing methods, it would be helpful to see a more detailed comparison in terms of performance, computational complexity, and other relevant metrics. Specifically, it would be useful to see a breakdown of the computational cost of each step in the ARIMEC algorithm and how it compares to the cost of similar steps in existing methods. This would allow for a more precise understanding of the trade-offs involved in using ARIMEC.

### Suggestions

The paper would be significantly strengthened by a more detailed analysis of the computational complexity of the ARIMEC algorithm. While the authors mention that their approach can handle arbitrary discrete distributions, it is crucial to understand how the runtime and memory requirements scale with the size of the input distributions. For example, providing a theoretical analysis of the time complexity in terms of the number of states in the distributions would be very helpful. Furthermore, it would be beneficial to include empirical results that demonstrate the runtime and memory usage of ARIMEC on distributions of varying sizes. This would allow readers to better assess the practical applicability of the algorithm. It would also be useful to discuss the specific data structures used to represent the distributions and how these choices impact the overall performance of the algorithm. For instance, are hash tables or other efficient data structures used to store and access the probability values? A more detailed discussion of these implementation details would be valuable.

In addition to the computational complexity analysis, a more detailed comparison to existing methods is needed. While the authors claim that ARIMEC is an improvement, a more rigorous comparison is necessary to substantiate this claim. This comparison should include not only the final performance metrics, such as the joint entropy of the resulting coupling, but also the computational cost of each step in the algorithms. For example, how does the time required to compute the partition function in ARIMEC compare to the time required for similar computations in existing methods? Furthermore, it would be helpful to compare the memory requirements of the different algorithms. This would allow readers to understand the trade-offs between the different approaches and to choose the most appropriate algorithm for their specific needs. The comparison should also include a discussion of the limitations of existing methods and how ARIMEC addresses these limitations.

Finally, the paper could benefit from a more detailed discussion of the practical considerations for applying ARIMEC to real-world problems. For example, how should the hyperparameters of the algorithm be chosen? Are there any specific types of distributions for which ARIMEC is particularly well-suited or ill-suited? Providing practical guidance on these issues would make the paper more useful to practitioners. It would also be helpful to include a discussion of the potential limitations of the merging technique and when it might not be effective. For instance, are there any specific types of distributions or scenarios where the merging technique could lead to suboptimal results? Addressing these practical considerations would further enhance the value of the paper.

### Questions

* How does the performance of ARIMEC scale with the size of the input distributions?
* Are there any specific types of distributions for which ARIMEC is not well-suited?
* How does the computational cost of ARIMEC compare to existing methods?
* What are the specific advantages of ARIMEC over existing methods?

### Rating

8

### Confidence

3

**********
