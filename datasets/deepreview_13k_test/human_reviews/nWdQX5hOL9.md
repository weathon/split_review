# Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking from A Spectral Perspective

- Decision: Accept
- Scores: 6, 6, 3, 6

## Abstract
Graph Neural Networks (GNNs) have achieved remarkable success in various graph-based learning tasks. While their performance is often attributed to the powerful neighborhood aggregation mechanism, recent studies suggest that other components such as non-linear layers may also significantly affecting how GNNs process the input graph data in the spectral domain. Such evidence challenges the prevalent opinion that neighborhood aggregation mechanisms dominate the behavioral characteristics of GNNs in the spectral domain. To demystify such a conflict, this paper introduces a comprehensive benchmark to measure and evaluate GNNs' capability in capturing and leveraging the information encoded in different frequency components of the input graph data. Specifically, we first conduct an exploratory study demonstrating that GNNs can flexibly yield outputs with diverse frequency components even when certain frequencies are absent or filtered out from the input graph data. We then formulate a novel research problem of measuring and benchmarking the performance of GNNs from a spectral perspective. To take an initial step towards a comprehensive benchmark, we design an evaluation protocol supported by comprehensive theoretical analysis. Finally, we introduce a comprehensive benchmark on real-world datasets, revealing insights that challenge prevalent opinions from a spectral perspective. We believe that our findings will open new avenues for future advancements in this area.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to study the effect of non-linear layers in graph neural networks (GNNs) on their spectral characteristics, in terms of their ability to represent information of different graph frequencies. Prior work focuses only on neighborhood aggregation and seeks to design filters that can represent graph frequencies more flexibly, but the current work considers GNNs holistically (including their nonlinearities) to empirically study their ability to represent different graph frequencies.

They first conduct a motivating experiment to show that GNNs can still recover frequency components which are filtered out by neighborhood aggregation, indicating the crucial role of nonlinear layers. Then, they construct a benchmark aiming to understand how well models can represent graph frequencies in different bucketized ranges. This is done by constructing classification tasks where the input is constructed using signals from one block of graph frequencies, and the output is a discretization of signals from a different block of graph frequencies, and then we measure the performance on this classification task. Theoretical results show that the discretization process does not give significant deviation in the spectral characteristics. 

Then they empirically find using the benchmark that (1) GNNs show a U curve in their frequency response; (2) certain (mostly spatial) GNNs like SAGE perform better on this task; (3) the benchmark gives a useful ordering of methods that correlates with their performance on real-world (heterophilic?) node classification tasks; (4) the shape of the accuracy curves does not significantly change with the number of layers.

### Strengths
- Interesting and seemingly understudied problem aiming to consider GNNs holistically (including their nonlinearities) in the spectral domain. 

- The accuracy curves seem like an interesting way of testing the ability of different GNNs to represent different frequencies, and provides an interesting "V curves" insight in RQ1.

- A real world case study is done, finding that the GNN rankings obtained from the benchmark are informative for deciding which GNNs are better than others on a series of real-world graph datasets.

### Weaknesses
- Clarity: some parts of the motivation are hard to understand, particularly due to some overly vague statements. For example, in the introduction, to make the motivation clear (particularly for readers who are less familiar with the cited works), I suggest precisely stating the common belief you are arguing against, and which papers exactly have demonstrated this common belief, and in what ways they use it. Similarly, Problem 2.1 is also too vague, e.g. it is unclear to the reader what "the key information" means. Similarly, in page 7, the paper also writes that RQ1 disagrees with "the prevalent opinion", without making it clear what this prevalent opinion is exactly, who expresses it, and why it is significant. 

- The notion and computation of "accuracy curves" seems to be a main contribution of the paper, but I find it hard to appreciate what the reader should exactly take away from these accuracy curves, partly due to the complexity of their definition. From what I understand, they group the eigenvalues into (low, medium, high) frequencies, and then the mean of eigenvectors from 1 group to predict another group (as done in section 3), and then in section 4 it is the same except discretizing the outputs. So in figure 2, what are the input frequencies being used? Overall, it seems that the main goal of this section is to give the reader some useful insights, but it is hard to extract useful insights as the definitions are rather complex. In terms of insights, the V shape behavior in RQ1 is indeed somewhat interesting, but I still find that there is a lack of clearly practical insights.

- While the ranking of methods is also a practical insight in some sense, I am not quite convinced that this is really a practical way of ranking methods that one would actually want to use for real use cases. If I wanted to decide which GNN to use on a particular dataset, it seems more reasonable to rely on (1) the performance on the validation set or a held-out subset of the training set, or in the worst case (2) the performance on some other real-world datasets (which are ideally reasonably similar to mine). Does the current benchmark really perform better (or otherwise preferable in some way) at least compared to option (2) above (if so, it may be good to validate this assumption empirically)? Alternatively, if the authors could show that the benchmark provides some useful insights about methods (e.g. what causes SAGE to perform significantly better on this benchmark than other methods), that may also be useful.

- It is not clear how robust the rankings are to different choices of hyperparameters for the methods. Although the experiment in RQ4 does test the effect of different layer numbers, there is a lack of quantitative results (as the 3d plots are not clear enough to see to what extent the different hyperparameters actually affect the statistics such as normalized AUC or the ranking between methods).

Additional points (minor)

- Section 4.1: when describing the experimental protocol, please either describe all the necessary details, or cross-reference (e.g. to the appendix) to where they are given. For example, you should explain how the discretization is done (or cross-reference).

### Questions
- In the experiment in section 5.4, I could not understand what the authors mean by r4 being defined as "Original Task Ranking", or describing it as "the node classification rankings r4 directly derived from the node classification task on the chosen six datasets." In particular, how does this differ from r1 (which also seems to be the ranking of methods on the node classification task)?

- In the same experiment, please clarify if the datasets were specifically chosen as examples of heterophilic datasets (or if not, why these 6 datasets in particular were chosen).

- Figure 3 is somewhat confusing - the caption states that the 3 subfigures correspond to low, medium, and high frequency ranges, but then the x-axis of each subplot also corresponds to low, medium and high frequency ranges? Could you clarify what is the difference between these?

### Soundness
3

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
The paper shows that GNN is not only a neighbor's filter but can handle different types of graph information better than previously thought. This is interesting!

### Strengths
I really appreciate the thorough empirical work they did. Instead of just making claims, they:
did careful preliminary experiments to show this unexpected capability, tested on real-world datasets and made everything with theoretical analysis.

Another strength is how they formalized this into an evaluation framework. It's not just about showing this phenomenon - they developed systematic ways to measure and compare different GNNs' capabilities in handling various frequency components. This gives the field new tools to understand GNN behavior.

Their findings suggest we might need to rethink how we design and analyze GNNs. If GNNs aren't just filters but can actually generate new frequency patterns.

### Weaknesses
The benchmark may be overly simplified, as real-world tasks rarely exhibit such clear-cut frequency separations, limiting the applicability of the results to more complex, real-world scenarios.

Most experiments were done with 2-layer GNNs.

### Questions
Your findings suggest GNNs struggle with middle-frequency information. Could you elaborate on potential modifications or techniques that might specifically enhance GNN performance in this range? How can we evaluate it?


Have you validated the benchmark against any real-world applications (e.g., molecular biology, recommendation systems) to confirm its predictive capability in practical settings?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a benchmark designed to evaluate Graph Neural Networks (GNNs) from a spectral perspective. Through the benchmarking process, along with theoretical analysis and empirical evaluation, the authors aim to demonstrate that GNNs can flexibly produce outputs with a diverse range of frequency components, even when certain frequencies are missing in the input.

### Strengths
1.	The paper is well-structured.
2.	Many experiments are conducted.

### Weaknesses
1. Flawed assumptions in Experimental Design: The key assumption presented on line 183, which states, "We note that graph filters cannot generate frequency components that are not originally contained in the input graph data," appears flawed.

    * In a graph Laplacian space, high and low frequencies are interpreted relative to the eigenvalue spectrum rather than by fixed boundaries (which the authors also do not specify). For instance, even if all eigenvalues are small in magnitude, they can be ordered to produce relative high or low frequencies for graph filters. This explains why, in Figure 1, low-frequency inputs can recover high-frequency signals—because the model filters out relatively high-frequency portions within the low-frequency signal, which the neural network then amplifies to align with the high frequency target.

    * The performance using certain frequency as the training target cannot be used to explain the results produced by using label as the training target as they are not causally linked, and the theoretical analysis of the paper does not convincingly resolve this concern.

        * While models may learn high-frequency signals by training on low-frequency inputs, this does not guarantee that supervised learning with labels inherently captures the necessary high-frequency information. No evidence is provided to substantiate a causal relationship between certain frequency components and labels; either may be fitted independently. As noted on line 77, these ground-truth are usually a composition of different frequency components and does not show clear incentive patterns preferring certain frequency components.
        * While the theoretical analysis shows that discretizing a continuous energy distribution related to frequency has minimal deviation, it does not substantiate a fundamental connection between label distributions and discretized energy distribution. In other words, the discretization of energy distributions does not necessarily correlate with labels. The authors need to provide more detailed proofs to clarify a causal relationship between energy distribution and labels. However, given previous work [4][5], which shows that nodes of the same label on a heterophilic graph often present a mixed homophily of structures (demonstrating various frequencies), this causal link remains questionable.
2. Benchmark Design Limitations: On line 52, the authors mention that heterophilic graphs are more likely to benefit from high-frequency components in graph data. However, the benchmarking evaluation relies solely on homophilic graphs, which may inadequately capture GNNs' adaptive learning capabilities across different frequencies under label supervision. (Except for several heterophilic graphs only presented in case study).
3. Lack of Novel Insights in Experimental Results:
    * Qualitative Findings: Similar findings with explanations have been reported in existing works [2][3]. For example, traditional GCNs perform well in extreme low-frequency (high-homophily) and extreme high-frequency (low-homophily) conditions, struggling in mid-homophily settings. This is explained as low-homophily neighborhoods with sufficiently distinct averages can still benefit from low-frequency filtering.
    * Quantitative Performance Analysis Misrepresentation: The quantitative analysis lacks accuracy. In line 419, the authors claim that the spectral filtering ability of GCNII is “rarely discussed and evaluated,” yet the original study explicitly highlights its polynomial graph filtering capability. Additionally, since all datasets used are homophilic (dominated by low frequencies), this setup fails to provide sufficient evidence to support the claims made about GNN flexibility in frequency handling.
4.	Lack of Necessity in the Study's Focus:
    * Many GNNs are inherently capable of flexible filtering (e.g., GCNII and ChebNet used in benchmarking, both of which offer polynomial graph filtering), enabling them to encode a range of frequency components by design.
    * Theoretical results for GCNII also show that GNNs with initial residual connections can achieve polynomial graph filtering, implying that even standard GCNs can encode various frequencies with basic modifications such as residual connections. As shown in [1], classic GNNs can serve as strong baselines on heterophilic graphs requiring high-frequency information when paired with simple techniques like residual connections and dropout.

Reference
[1].	Luo, Yuankai, Lei Shi, and Xiao-Ming Wu. "Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification." arXiv preprint arXiv:2406.08993 (2024).

[2].	Ma, Yao, et al. "Is homophily a necessity for graph neural networks?." arXiv preprint arXiv:2106.06134 (2021).

[3].	Luan, Sitao, et al. "When do graph neural networks help with node classification? investigating the homophily principle on node distinguishability." Advances in Neural Information Processing Systems 36 (2024).

[4].	Yang, Liang, et al. "Diverse message passing for attribute with heterophily." Advances in Neural Information Processing Systems 34 (2021): 4751-4763.

[5].	Suresh, Susheel, et al. "Breaking the limit of graph neural networks by improving the assortativity of graphs with local mixing patterns." Proceedings of the 27th ACM SIGKDD conference on knowledge discovery & data mining. 2021.

### Questions
The meaning of "original task ranking" in Section 5.4 remains unclear. If node classification is the only task, does the benchmarking task ranking refer to an averaged ranking across multiple GNNs, with the original task ranking denoting the rank of a single GCN? A clearer explanation of this experimental setup would help clarify the significance of the conclusions presented in this section.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work focusses on benchmarking current GNNs concerning their spectral perspective. It first conducts an exploratory study to show that GNNs can predict unseen frequency from the graph data and such ability is then evaluated in the protocol along with the node classification performance against 14 GNNs. The framework to measure the GNNs’ capability to capture and
leverage information across different frequency components is interesting.

### Strengths
1-	The evaluation from the spectral perspective is interesting and provides new insights.

2-	The presentation is good, making the paper easy to read.

### Weaknesses
1-	The EXPLORATORY STUDY needs more elaboration/evaluation. Current experiments show that GNNs can predict unseen frequency signals from graph data, which is not necessarily supports that “the filter resulted from the neighborhood aggregation does not dominate the behavioral characteristics of GNNs in the spectral domain”. Extra comparison with GNNs without graph signal input is needed to evaluate the extent of “A”.

2-	The scope of GNNs and datasets are restricted mostly to homophily ones. It would be helpful to incorporate heterophily GNNs considering their capability of high frequency domains.

3-	Lacks of discussion of existing spectral GNN benchmarks, for example [1].

[1] Benchmarking Spectral Graph Neural Networks: A Comprehensive Study on Effectiveness and Efficiency.

### Questions
In line 431, the author said “Instead, GNNs such as GATv2 and GCN achieve clear superiority over other GNNs in learning from middle frequency components.” Could you elaborate more why GCN is superior here? Upon middle frequency, the neighbors are often connected with mixed labels. GCN’s uniform aggregation can hardly distinguish such results.

I'm willing to raise the score if concerns can be well addressed.

### Soundness
3

### Presentation
4

### Contribution
2
