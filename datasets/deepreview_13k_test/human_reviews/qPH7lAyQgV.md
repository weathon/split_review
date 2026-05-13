# Graph Concept Bottleneck Models

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
The design of interpretable deep learning models working in relational domains poses an open challenge: interpretable deep learning methods, such as Concept Bottleneck Models (CBMs), are not designed to solve relational problems, while relational deep learning models, such as Graph Neural Networks (GNNs), are not as interpretable as CBMs. To overcome these limitations, we propose Relational Concept Bottleneck Models (R-CBMs), a family of relational deep learning methods providing interpretable task predictions. 
    As special cases, we show that R-CBMs are capable of both representing standard CBMs and message-passing GNNs. To evaluate the effectiveness and versatility of these models, we designed a class of experimental problems, ranging from image classification to link prediction in knowledge graphs. In particular we show that R-CBMs (i) match generalization performance of existing relational black-boxes, (ii) support the generation of quantified concept-based explanations, (iii) effectively respond to test-time interventions, and (iv) withstand demanding settings including out-of-distribution scenarios, limited training data regimes, and scarce concept supervisions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes Graph Concept Bottleneck Models (Graph CBMs) to address the limitations of existing CBMs. The authors identify that while CBMs provide interpretable models by mapping inputs to a concept score space, the assumption of conditional independence among concepts is often violated in practice. To capture the intrinsic structure and relationships within the concept space, Graph CBMs construct latent concept graphs and combine them with CBMs. The empirical results demonstrate that Graph CBMs outperform standard CBMs on image classification tasks, can utilize the concept graphs for more effective interventions, and are robust across different training and architecture settings. Overall, this work presents a significant advancement in improving the performance and interpretability of CBMs by explicitly modeling the hidden interactions within the concept space.

### Strengths
1. This paper is the first to propose CBM that utilizes a graph structure to facilitate interaction between concepts. This advancement represents a significant improvement over previous models in understanding the dependencies among concepts. Such an introduction enhances the model's ability to capture complex relationships between concepts effectively.

2. The research demonstrates the superior performance of Graph CBM across various tasks and different CBM architectures through detailed experiments. Furthermore, Graph CBM allows for human intervention, showcasing strong scalability and providing greater flexibility for real-world applications.

3. The graph structure of Graph CBM provides improved interpretability in the model's decision-making processes. This enables users to gain a clearer understanding of how the model operates and the rationale behind its decisions, thereby increasing the transparency of the model in practical applications.

### Weaknesses
1. While the incorporation of a combined contrastive loss from the score space and the embedding space is an innovative design, the paper may lack a detailed explanation of the motivation behind this choice. This insuff can hinder the readers' ability to fully understand the theoretical foundation and practicality of this approach. Furthermore, without supporting ablation studies, readers may struggle to assess the specific impact of this design on the model's performance.


2. Although Graph CBM claims to effectively learn dependencies between concepts through its graph structure, the paper may not provide systematic experimental results to convincingly validate this assertion. This raises questions about the source of performance improvements in Graph CBM, as any enhancements in specific cases may not be wholly attributed to the introduction of the graph structure.

3. Despite the enhanced capability of Graph CBM in learning dependencies, the absence of specific visual examples may limit readers' understanding of this improvement.

### Questions
1. Why was a combined contrastive loss from the score space and embedding space adopted during the training of Graph CBM? What is the motivation behind this design? Can ablation studies be conducted to provide more intuitive results demonstrating the specific impact of this loss formulation on model performance?

2. Does the performance improvement of Graph CBM over traditional CBM stem from its graph structure effectively learning the dependencies between concepts? Is there specific experimental evidence to support this claim?

3. Related to the second question, given that Graph CBM performs better than traditional CBM in learning dependency relationships, can specific visual examples be provided to clearly demonstrate this enhanced performance?

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
4

### Summary
This work proposes GraphCBMs, a CBM variant that aims to bypass the simplistic assumption of independent concepts via the construction of latent concept graphs.
The experimental results suggest that the proposed variant can lead to better generalization capabilities and intervention strategies.

### Strengths
Overcoming the commonly used assumption of independent concepts is very important to the interpretability community. Using Graph Networks is a novel and interesting approach in the context of CBMs.

### Weaknesses
To the best of my understanding, the proposed approach considers one concept graph per image. Even though this allows for a more flexible representation, 
it may lead to some inconsistent results in terms of interpretability. 

Is there a way to get a global representation of the latent structure from the localized representations?
Would it also be possible to have a variant that mainly considers a global representation that could be adjusted to individual examples?

In this context, Fig. 4 presents a concept graph for the Label-free trained CUB. Can the authors elaborate on how this graph was constructed?

Fig.4 can be improved by setting the weights of the  edges to denote the weight of the connection, or use dotted lines or other approaches. 
At this point, it's not exactly easy to interpret. The authors mention some pairs, e.g., "(241) black wings with white spots - (337) white and black coloration" but there are several other connections to other nodes that are not explained, e.g., for 241, the nodes 288, 4, 245, 239.

What is the impact of the different objectives introduced by the authors? An ablation study on the impact of the different terms is imperative. 

I find that some datasets for evaluating the approach are missing and specifically ImageNet and Places365. These are very common in the CBM community. Did the authors examine the behavior of the proposed approach in such a setting?

The concept prediction increase is marginal in most cases, while for CUB (in the CBM and G-CBM) case there exists a large gap. Some recent works also use other metric, such as the Jaccard index to assess the performance. Can the authors report the concept prediction performance using this metric?

There are other CBM variants that yield better results that LF-CBM and PCBMs, e.g., [1,2] (and also better than the proposed method). It would make sense to use the best performing CBM variant to assess if the emerging performance translates to such a setting.   Did the authors test any other CBMs for their approach? 

In this frame of reference, the SOTA approaches are missing quite relevant CBM variants, as the ones previously mentioned.

In Table 1 and Fig. 2, which backbone is used for LF-CBM? The results don't seem to match the ones reported in the original publication.

What is the complexity of the proposed approach in terms of both training and inference? How does it compare to the corresponding baseline methods? Some wall time measurements should be enough. 

Overall, I find the method to be very interesting and modelling the connections between concepts very important. However, at this time, the manuscript is missing some key datasets and comparisons with other better performing methods, 


[1] Panousis et al.,  Sparse Linear Concept Discovery Models, ICCW, 2023

[2] Vandenhirtz et al, Stochastic Concept Bottleneck Models, NeurIPS 2024

### Questions
Please see the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents Graph Concept Bottleneck Models (Graph CBMs), an advancement of Concept Bottleneck Models that incorporates learnable graph structures to capture interactions among concepts. Unlike traditional CBMs that assume concepts are independent, Graph CBMs model these relationships to enhance performance and maintain interpretability. Empirical results show that Graph CBMs outperform existing CBMs in image classification tasks, facilitate more effective interventions using concept graphs, and demonstrate robustness across various training settings and backbones.

### Strengths
1. The paper introduces Graph CBMs, which improve the interpretability of Concept Bottleneck Models by modeling interactions among concepts through a learnable graph structure.
2. The proposed contrastive learning framework can perform graph structure learning.
3. The proposed method is compatible with existing CBM approaches and improves performance across different backbones and training setups while maintaining interpretability.

### Weaknesses
1. The paper is challenging to follow because many design choices seem subjective with less clear, detailed explanations. I believe that the design processes of many components in the paper are not clearly explained, and the experiments do not sufficiently validate the claims. Further clarification is needed.
2. Figure 1 provides insufficient detail, as the graph calculation process is represented with a simplistic and unclear sketch, making it difficult to convey meaningful insights.
3. The rationale behind using the non-parameterized graph propagation mechanism is unclear. What is the actual meaning of the update rule of concept score?
4. The claim that the inverse matrix is hard to compute and may introduce unrelated long-range dependency noise requires further clarification. 
5. Additionally, the meaning of the "one-step approximation" are not explained and there is no any citations.
6. Lines 175-178 contain an ambiguous statement: "As an intrinsic structure, we expect that the concept graph should not depend too much on the labels; otherwise, the graph cannot be learned well in label-incomplete settings." This sentence is unclear and very subjective. I can not see any reason why the contrastive learning method should be used next.
7. Lines 196-197, there's no definition of $W_l^{'}$.
8. The description of "However, $c_i$ only plays a marginal role in $\mathcal{L}_{emb}$ which limits the performance. ... we design a second contrastive loss" is hard to understand. What is the logic behind $c_i$ playing a marginal role and thus limiting performance?
9. The experimental results in Table 2 and Figure 2 seem marginal compared to traditional methods.
10. The design of the loss function (Equation 6) appears unnecessarily complicated, and the justification for this complexity is insufficient. The experiment in Appendix A.9, which examines how the two contrastive terms affect model performance, only includes two datasets. Using just two datasets to infer the necessity of joint training for these losses seems inadequate. Why weren't experiments conducted across all five datasets? The results of the complex loss design do not appear to be well validated, and the paper does not clearly demonstrate through insights or experiments why this design is necessary.

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel variant of the Concept Bottleneck Model (CBM), called Graph CBM, which aims to capture the intrinsic correlations between concepts by incorporating graph structures. By constructing an underlying concept graph, Graph CBM enhances interactions between concepts, thereby improving both the interpretability and performance of the model.

### Strengths
1. Innovation: The introduction of graph structures into the concept bottleneck model addresses the limitations of traditional CBMs that overlook concept relationships, significantly enhancing the model's interpretability and performance.

2. Broad Applicability: Graph CBM can be integrated with existing CBM methods, offering strong extensibility and improving performance across various CBM applications.

### Weaknesses
Although the use of graph structures helps explain relationships between concepts, it still falls short in providing interpretability for individual neurons within the model.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
