### Summary

This paper presents new results on the problem of minimum entropy coupling (MEC). The authors develop a new algorithm (ARIMEC) for approximately solving the MEC problem for certain classes of input distributions, building on past work by Sokota et al. (2022). The authors demonstrate the effectiveness of their algorithm in a series of experiments.

### Soundness

3

### Presentation

2

### Contribution

3

### Strengths

The paper develops an algorithm that efficiently solves an important problem in a new setting. The experiments are convincing and demonstrate the usefulness of the new algorithm.

### Weaknesses

#### Some Related Works


#### comment

The presentation could be improved in certain parts of the paper. In particular, the introduction is quite dense and would benefit from being restructured. Some of the technical sections are also dense and somewhat hard to parse (e.g., Section 4.2). The paper could also benefit from additional explanation of certain key concepts, such as the "prefix tree" and the "touching" of nodes.

### Suggestions

The introduction could be improved by breaking it down into smaller, more digestible sections. Currently, it attempts to cover too much ground, including the problem definition, prior work, and the authors' contributions, all in one dense paragraph. A better approach would be to separate these into distinct sections, starting with a clear and concise problem statement, followed by a discussion of the existing literature, and then a detailed explanation of the authors' specific contributions. This would make it easier for the reader to understand the context of the work and the novelty of the proposed approach. Furthermore, the introduction should clearly articulate the limitations of existing methods and how the proposed algorithm overcomes these limitations. This would help to motivate the need for the new algorithm and highlight its significance.

Section 4.2, which deals with the efficient implementation of the ARIMEC algorithm, is particularly dense and difficult to follow. The authors should consider breaking this section down into smaller, more manageable parts. For example, they could start by providing a high-level overview of the algorithm, followed by a detailed explanation of each step. The use of pseudocode or flowcharts could also be helpful in clarifying the algorithm's logic. Additionally, the authors should provide more intuition behind the design choices of the algorithm. For example, why is the maximum-entropy partition search necessary? What are the trade-offs involved in using this approach? Providing this kind of context would make the section much easier to understand. The explanation of the prefix tree and the 'touching' of nodes needs to be more detailed. A concrete example, perhaps with a small illustration, would be very helpful. The authors should explain how the prefix tree is constructed, how it is used to represent the input distributions, and how the 'touching' of nodes relates to the algorithm's logic. The current explanation is too abstract and lacks the necessary detail for a reader to fully grasp these concepts.

Finally, the paper would benefit from a more thorough discussion of the limitations of the proposed algorithm. While the experiments demonstrate the algorithm's effectiveness in certain settings, it is important to acknowledge its potential shortcomings. For example, what are the computational complexity and memory requirements of the algorithm? Under what conditions might the algorithm fail to produce a good solution? Addressing these questions would provide a more balanced and realistic assessment of the algorithm's capabilities. Furthermore, the authors should discuss potential avenues for future research, such as how to extend the algorithm to handle other types of input distributions or how to improve its computational efficiency. This would help to position the paper within the broader research landscape and highlight its potential for future impact.

### Questions

1. In the experiments, what is the "Rate" in Figure 5?
2. In the introduction, the authors state that ARIMEC is the "first approach to computing low-entropy couplings for large-support distributions that can be applied to arbitrary distributions." Is this a strict theoretical statement, or is it based on the authors' empirical observations? If it is the former, then a proof should be provided. If it is the latter, then this statement should be relaxed.
3. The authors should include a discussion of the limitations of their algorithm. In which settings might ARIMEC fail to produce a good solution?

### Rating

6

### Confidence

3

**********
