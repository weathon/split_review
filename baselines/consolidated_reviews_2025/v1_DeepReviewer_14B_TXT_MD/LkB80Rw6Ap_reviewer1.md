### Summary

The paper proposes a framework for MPNNs to improve upon over-squashing, called Curvature-Constrained Message Passing (CCMP). CCMP uses two different edge curvature measures (Ollivier curvature and Augmented Forman curvature) to sparsify or rewire the graph. The different curvature measures give rise to different variants of CCMP. These different variants are empirically evaluated on 11 datasets (4 homophilic, 7 heterophilic), with CCMP consistently outperforming the evaluated baselines.

### Soundness

2 fair

### Presentation

1 poor

### Contribution

2 fair

### Strengths

The experimental evaluation, while limited in scale, is thorough in the number of datasets and baselines evaluated on. The proposed method, while arguably having limited novelty, is empirically successful across these datasets.

### Weaknesses

#### comment

The paper has several weaknesses which prevent me from recommending it for acceptance.

The motivation of the method is not clear. In Section 1, the paper describes the over-squashing phenomenon, and states that "To overcome this problem, GNNs must be able to incorporate additional global graph features in the process of learning representations." and "Another popular approach is to rewire the input graph to improve the connectivity and avoid over-squashing." However, it is not clear to me how the proposed method relates to either of these two high-level approaches. It is even less clear how curvature comes into play, and why we should expect CCMP to mitigate over-squashing.

In Section 2, the paper describes a few different approaches to mitigating over-squashing, including rewiring the input graph. However, no such motivation is given for the specific curvature-based rewiring that is proposed. While some intuition is given in Section 3.4, it is unclear to me why we should expect the proposed method to perform well.

The paper has a limited novelty. While the specific method may be novel, the overall idea of using graph rewiring to mitigate over-squashing has been explored in the literature. The experimental evaluation also has limited novelty, as the datasets and baselines have been explored in prior work.

The presentation of the paper can be improved. There are several spelling and grammatical errors. The figures are also not of high quality, with a small font size making them hard to read.

### Questions

1. Why should we expect CCMP to mitigate over-squashing?
1. Can you derive any theoretical guarantees for CCMP?
1. Can you improve the quality of the figures?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
