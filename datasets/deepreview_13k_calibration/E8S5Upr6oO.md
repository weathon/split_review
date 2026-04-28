# MGMapNet: Multi-Granularity Representation Learning for End-to-End Vectorized HD Map Construction

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The construction of Vectorized High-Definition (HD) map typically requires capturing both category and geometry information of map elements. Current state-of-the-art methods often adopt solely either point-level or instance-level representation, overlooking the strong intrinsic relationships between points and instances. In this work, we propose a simple yet efficient framework named MGMapNet (Multi-Granularity Map Network) to model map element with a multi-granularity representation, integrating both coarse-grained instance-level and fine-grained point-level queries. Specifically, these two granularities of queries are generated from the multi-scale bird's eye view (BEV) features using a proposed Multi-Granularity Aggregator. In this module, instance-level query aggregates features over the entire scope covered by an instance, and the point-level query aggregates features locally. Furthermore, a Point Instance Interaction module is designed to encourage information exchange between instance-level and point-level queries. Experimental results demonstrate that the proposed MGMapNet achieves state-of-the-art performance, surpassing MapTRv2 by 5.3 mAP on nuScenes and 4.4 mAP on Argoverse2 respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents MGMapNet, a multi-granularity map network for end-to-end vectorized HD map construction based on multi-scale bird’s eye view (BEV) images. Evaluations on four datasets show the effectiveness of MGMapNet over multiple baseline models.

### Strengths
1. The contributions are highlighted. The novel contributions compared with previous approaches are also discussed properly.
2. Both quantitative and qualitative results are shown and discussed. Ablation studies are conducted in a meaningful way.

### Weaknesses
1. The citations of the whole paper are wrong. It should be \citep{} instead of \cite{}.

2. From Figure 1 and 3. we can see the advantages of MGMapNet over other models. However, I can still see that the extracted lanes by MGMapNet are sometimes zigzagged while the ground truth lines are straight lines. I wonder whether you can add some regularity or loss terms to avoid this. Maybe for those straight lines, resample their vertices along the straight lines every times during model training so that the model learns the linear feature instead of individual point locations?

3. Can you describe each loss term in detail? Do you use the distance from each point to the ground truth points as the loss for L_{pts}?

### Questions
See the weakness.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces MGMapNet, designed to effectively model map elements through a multi-granularity representation by integrating both coarse-grained instance-level and fine-grained point-level queries to enhance map modeling. The framework employs a Multi-Granularity Aggregator. Besides, there is a Point Instance Interaction module, which facilitates the exchange of information between the instance-level and point-level queries, thereby improving the overall modeling capability of the network.

### Strengths
1.	The problem studied in the paper is very important in practice and find applications in real world.
2.	The paper is clearly written and easy to follow. 
3.	Experiments are conducted to verify the performance of the proposed method.

### Weaknesses
1.	The challenges and contributions of the proposed techniques require further elaboration. What are the specific challenges to design these techniques in section 3? It's unclear why a multi-granularity approach is necessary beyond simply stating that it combines instance and point-level queries. The paper needs to articulate the specific limitations of existing single-granularity methods that this approach overcomes, and why those limitations are significant.
2.	The encoders and decoders are mostly MLP-based. It is difficult to understand the logic, rationale and difficulty to apply the techniques. The paper does not provide sufficient justification for using MLPs over other encoding/decoding methods, particularly given the spatial nature of the data. The choice of MLP needs to be motivated by specific properties of the problem, and the limitations of alternative approaches should be discussed.
3.	Some evaluation metrics in experiments are not explained, e.g. AP_ped and AP_div, and AP_bou in table 1. The lack of explanation for these metrics makes it difficult to assess the significance of the results. The paper should also discuss why these specific metrics were chosen and how they relate to the overall goal of the work.
4.	How are the proposed techniques related to High-Definition? The paper does not clearly articulate how the proposed method contributes to the specific challenges of high-definition map construction. The connection between the method and the practical requirements of HD maps needs to be made explicit.
5.	Quality of figures and tables can be improved. For example, Table 4 has too big font size.

### Questions
1.	Is it possible to consider instance-2-instance attention? Why not compare this?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents MGMapNet, a framework designed for end-to-end vectorized High-Definition map construction. MGMapNet introduces a multi-granularity representation that integrates both instance-level and point-level queries to effectively capture both category and geometric information of road elements. The proposed Multi-Granularity Aggregator and Point Instance Interaction modules allow information exchange between the two granularities, resulting in enhanced prediction accuracy. Experimental results demonstrate state-of-the-art performance on benchmark datasets such as nuScenes and Argoverse2, surpassing various baseline methods.

### Strengths
S1. The paper introduces a method that combines both coarse-grained instance-level and fine-grained point-level queries, effectively capturing both global category information and local geometric details of map elements. 

S2. The design of the Multi-Granularity Aggregator and Point Instance Interaction modules facilitates efficient and effective information sharing between instance-level and point-level queries.

S3. The proposed MGMapNet framework outperforms several baseline models, achieving the state-of-the-art performance in HD map construction.

### Weaknesses
W1. The paper’s description can be overwhelming for readers who are not deeply familiar with the HD map construction topic (e.g., me). For example, it lacks a formal problem formulation, which would help in grounding the research context. Additionally, the method's explanation is a bit difficult to follow. Specifically, the paper does not clearly define the input and output spaces for the proposed model. It is unclear how the raw sensor data (presumably camera images) is transformed into the BEV feature representation, and how this representation is then used to generate the vectorized map elements. The description of the Multi-Granularity Aggregator and Point Instance Interaction modules lacks sufficient detail, making it difficult to understand the precise mechanisms of information exchange between the instance-level and point-level queries.

W2. The paper could be strengthened by providing a detailed analysis of the time and space complexity of MGMapNet compared to baseline models. Given that efficiency is a key motivation, understanding how MGMapNet performs in terms of computational and memory resources would be beneficial. The paper does not provide a breakdown of the computational cost associated with each module of the proposed architecture. It is unclear how the multi-granularity representation impacts the overall computational complexity and memory footprint. A detailed comparison of the inference time and memory usage with other state-of-the-art methods would be necessary to assess the practical applicability of the proposed method.

W3. It is not clear why the training epochs are set to have multiple values for various models, and why the long training schedule leads to fair comparison. The paper does not provide a clear rationale for using different training epochs for different models. It is unclear whether the models were trained until convergence or if the training epochs were chosen arbitrarily. The lack of a consistent training protocol makes it difficult to compare the performance of the proposed method with other baselines.

### Questions
Please clarify the comments for W1-W3.

### Soundness
3

### Presentation
3

### Contribution
3
