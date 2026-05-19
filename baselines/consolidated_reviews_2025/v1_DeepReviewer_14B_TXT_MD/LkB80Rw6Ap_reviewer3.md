### Summary

This paper proposes a new message passing scheme that relies on edge curvature to improve the performance of GNNs. The authors propose a new homophily metric based on edge curvature and use it to guide the message passing. The authors show that their method outperforms existing graph rewiring methods on several node classification tasks.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is generally well-written and easy to follow.

2. The idea of using edge curvature to guide message passing is interesting.

3. The authors conduct experiments on a variety of datasets and show that their method outperforms existing graph rewiring methods.

### Weaknesses

#### comment

1. The motivation of the method is not clear. In Section 1, the paper describes the over-squashing phenomenon, and states that "To overcome this problem, GNNs must be able to incorporate additional global graph features in the process of learning representations." and "Another popular approach is to rewire the input graph to improve the connectivity and avoid over-squashing." However, it is not clear to me how the proposed method relates to either of these two high-level approaches. It is even less clear how curvature comes into play, and why we should expect CCMP to mitigate over-squashing.

In Section 2, the paper describes a few different approaches to mitigating over-squashing, including rewiring the input graph. However, no such motivation is given for the specific curvature-based rewiring that is proposed. While some intuition is given in Section 3.4, it is unclear to me why we should expect the proposed method to perform well.

2. The paper has a limited novelty. While the specific method may be novel, the overall idea of using graph rewiring to mitigate over-squashing has been explored in the literature. The experimental evaluation also has limited novelty, as the datasets and baselines have been explored in prior work.

3. The presentation of the paper can be improved. There are several spelling and grammatical errors. The figures are also not of high quality, with a small font size making them hard to read.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
