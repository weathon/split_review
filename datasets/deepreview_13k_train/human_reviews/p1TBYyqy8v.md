# Spreading Out-of-Distribution Detection on Graphs

- Decision: Accept
- Scores: 8, 6, 8, 6, 5

## Abstract
Node-level out-of-distribution (OOD) detection on graphs has received significant attention from the machine learning community. However, previous approaches are evaluated using unrealistic benchmarks that consider only randomly selected OOD nodes, failing to reflect the interactions among nodes. In this paper, we introduce a new challenging task to model the interactions of OOD nodes in a graph, termed spreading OOD detection, where a newly emerged OOD node spreads its property to neighboring nodes. We curate realistic benchmarks by employing the epidemic spreading models that simulate the spreading of OOD nodes on the graph. We also showcase a ``Spreading COVID-19" dataset to demonstrate the applicability of spreading OOD detection in real-world scenarios. Furthermore, to effectively detect spreading OOD samples under the proposed benchmark setup, we present a new approach called energy distribution-based detector (EDBD), which includes a novel energy-aggregation scheme. EDBD is designed to mitigate undesired mixing of OOD scores between in-distribution (ID) and OOD nodes. Our extensive experimental results demonstrate the superiority of our approach over state-of-the-art methods in both spreading OOD detection and conventional node-level OOD detection tasks across seven benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This research addresses a significant gap in node-level out-of-distribution (OOD) detection by introducing a novel task that considers the interactions among nodes in a graph. Previous methods have relied on unrealistic benchmarks that randomly select OOD nodes, which do not reflect real-world scenarios where OOD properties can spread among neighboring nodes. The key contributions of this paper include:
1. Introduction of Spreading OOD Detection: This new task models how newly emerged OOD nodes can influence their neighbors, simulating more realistic scenarios of OOD detection.
2. Realistic Benchmark Creation: The authors develop benchmarks using epidemic spreading models to simulate the dynamics of OOD node interactions within graphs. 
3. “Spreading COVID-19” Dataset: A specific dataset is introduced to illustrate the practical applications of spreading OOD detection, showcasing its relevance to real-world situations.
4. Energy Distribution-Based Detector (EDBD): The paper presents a new detection approach that employs an energy-aggregation scheme aimed at reducing the overlap in OOD scores between in-distribution (ID) and OOD nodes, enhancing detection accuracy.
5.Extensive Experimental Validation: Results from comprehensive experiments demonstrate that the proposed EDBD approach outperforms existing state-of-the-art methods in both spreading OOD detection and traditional node-level OOD detection tasks across seven benchmark datasets.
Overall, this work advances the field of OOD detection by incorporating the complexities of node interactions in graph structures, providing both theoretical and practical contributions.

### Strengths
This research addresses a significant gap in node-level out-of-distribution (OOD) detection by introducing a novel task that considers the interactions among nodes in a graph. Previous methods have relied on unrealistic benchmarks that randomly select OOD nodes, which do not reflect real-world scenarios where OOD properties can spread among neighboring nodes. The key contributions of this paper include:
1. Introduction of Spreading OOD Detection: This new task models how newly emerged OOD nodes can influence their neighbors, simulating more realistic scenarios of OOD detection.
2. Realistic Benchmark Creation: The authors develop benchmarks using epidemic spreading models to simulate the dynamics of OOD node interactions within graphs. 
3. “Spreading COVID-19” Dataset: A specific dataset is introduced to illustrate the practical applications of spreading OOD detection, showcasing its relevance to real-world situations.
4. Energy Distribution-Based Detector (EDBD): The paper presents a new detection approach that employs an energy-aggregation scheme aimed at reducing the overlap in OOD scores between in-distribution (ID) and OOD nodes, enhancing detection accuracy.
5.Extensive Experimental Validation: Results from comprehensive experiments demonstrate that the proposed EDBD approach outperforms existing state-of-the-art methods in both spreading OOD detection and traditional node-level OOD detection tasks across seven benchmark datasets.
Overall, this work advances the field of OOD detection by incorporating the complexities of node interactions in graph structures, providing both theoretical and practical contributions.

### Weaknesses
Theoretical Justification for EDBD: While the energy-aggregation scheme is introduced as a key component of the EDBD, the paper would benefit from a more rigorous theoretical foundation explaining why this method effectively mitigates the mixing of OOD scores. Specifically, the paper lacks a detailed explanation of how the proposed energy aggregation differs from existing methods, such as those based solely on graph structure, and why this difference leads to improved performance. A mathematical analysis comparing the energy update rules of EDBD with those of other aggregation methods would be beneficial. Providing a more formal analysis, perhaps using concepts from spectral graph theory or dynamical systems, could strengthen the credibility of this contribution.

Sensitivity Analysis: Conducting a sensitivity analysis on the parameters of the EDBD model could provide valuable insights into how different configurations affect performance. The paper should explore how the hyperparameters, such as the weighting factors in the energy aggregation scheme and the number of aggregation steps, impact the model's ability to distinguish between in-distribution and out-of-distribution nodes. Understanding the robustness of the model to variations in these parameters is crucial for practical applications. For example, the paper could investigate how the performance changes when the parameters are varied within a reasonable range, and whether there are specific parameter settings that consistently lead to better results across different datasets.

### Questions
Theoretical Foundations of EDBD:
Question: What theoretical framework supports the effectiveness of the energy-aggregation scheme in EDBD?
Suggestion: A more detailed theoretical justification for why this approach mitigates the mixing of OOD scores would strengthen your argument and improve the method's credibility.

### Soundness
4

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
This paper introduces a more realistic benchmark for node-level out-of-distribution (OOD) detection on graphs, called “spreading OOD detection”, where  OOD characteristics spread across connected nodes, similar to real-world diffusion processes like disease spreading. The paper dedicates one part to defining this benchmark in detail, using the “Spreading COVID-19” dataset to show its practical value. This benchmark is different from traditional approaches that treat OOD nodes as isolated and do not consider interactions. Another part of the paper is focused on a new method, the Energy Distribution-Based Detector (EDBD), designed to address this benchmark. EDBD uses an energy-aggregation scheme to keep OOD and in-distribution (ID) scores from mixing, helping to identify OOD nodes more accurately.

### Strengths
Although the benchmark is presented as realistic, it relies on assumptions in simulations that may be hard to verify, particularly given the use of the LastFM dataset, which may not accurately represent human contact patterns essential for modeling disease spread. The suitability of LastFM’s social connections as a proxy for physical contact is uncertain, as are other factors like spatial constraints and the presence of high-degree nodes that could act as unrealistic “super-spreaders.” To address this concern and enhance the benchmark’s realism, the authors could validate these assumptions against datasets explicitly designed for human contact networks (such as those used in epidemiology studies) or test the model on multiple datasets with diverse structural properties to better reflect real-world contact interactions.

The EDBD method’s performance appears closely tied to assumptions within the benchmark setup, making it difficult to assess its independent technical relevance. The method seems to build on GNNSAFE with the addition of energy similarity and consistency matrices, yet these connections and differences are not fully discussed. To clarify the contribution, the authors could provide a more detailed comparison between EDBD and GNNSAFE, explaining how the added matrices influence performance and to what extent the results depend on benchmark-specific assumptions.

### Weaknesses
Although the benchmark is presented as realistic, it relies on assumptions in simulations that may be hard to verify, particularly given the use of the LastFM dataset, which may not accurately represent human contact patterns essential for modeling disease spread. The literature in this area includes foundational works from over a decade ago, which should be discussed, e.g. [1,2,3].
The suitability of LastFM’s social connections as a proxy for physical contact is uncertain, as are other factors like spatial constraints and the presence of high-degree nodes that could act as unrealistic “super-spreaders.” To address this concern and enhance the benchmark’s realism, the authors could validate these assumptions against datasets explicitly designed for human contact networks (such as those used in epidemiology studies) or test the model on multiple datasets with diverse structural properties to better reflect real-world interactions.

The EDBD method’s performance appears closely tied to assumptions within the benchmark setup, making it difficult to assess its technical relevance. The method seems to build on GNNSAFE with the addition of energy similarity and consistency matrices, yet these connections and differences are not fully discussed. To clarify the contribution, the authors could provide a more detailed comparison between EDBD and GNNSAFE, explaining how the added matrices influence performance and to what extent the results depend on benchmark-specific assumptions.

### Questions
Q1: Since the dataset is central to the benchmark, it is crucial to understand how well it reflects realistic contact-driven networks for virus spreading. Information on whether the dataset’s assumptions have been validated against more realistic epidemic scenarios would also help clarify its suitability for simulating disease dynamics. Could the authors provide detailed information on the construction and structure of the LastFM dataset, including the main mechanisms of edge formation, the presence of high-degree nodes that could act as super-spreaders, and the dataset’s time span in relation to episode durations required to reach 75% node infection? 

Q2: Could the authors discuss the sensitivity of the proposed method to variations in the SIS model parameters and its adaptability to different diffusion patterns? Understanding this sensitivity is important for evaluating the method’s robustness in various scenarios. Additionally, could the authors clarify why OOD detection is not approached as a binary classification between ID and OOD, or as a one-class classification in cases where only ID labels are available? Addressing these points would provide valuable insights into the generalizability of the benchmark and the chosen approach for OOD detection.

Q3: Given the high error bars in Tables 2 and 3, how conclusive are the results? Could the authors explain if the similar performance of EDBD and the Energy method suggests that data features, rather than graph structure, drive the performance? Also, since Eq. 4 of the paper is quite similar to Eq. 7 of GNNSAFE, could the authors clarify the exact differences between EDBD and GNNSAFE beyond adding the energy similarity and consistency matrices? For example, does the first row in Table 4 represent GNNSAFE?

Q4: Since hyperparameter tuning can greatly impact performance, could the authors explain how it was done for both EDBD and baseline methods? Was the search for competitors restricted compared to EDBD? For GNNSAFE, was only the supervised loss used, or did the authors include GNNSAFE++ with energy regularization? If only the supervised loss was used, what motivated this choice?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces "spreading OOD detection," for node-level out-of-distribution (OOD) detection on graphs. It addresses limitations in existing methods by modeling the spread of OOD samples through graph structures. The authors propose a new dataset, "Spreading COVID-19," and present a novel approach called Energy Distribution-Based Detector (EDBD) that outperforms existing methods in both spreading and conventional OOD detection tasks.

### Strengths
1. The concept of spreading OOD detection is novel and addresses a gap in existing methods.
2. A new dataset is introduced which will help future research
3. The figures used in the paper manage to illustrate the problem and approach well.

### Weaknesses
1. It would be interesting to see comparison of EDBD with SOTA in terms of computational complexity and scalability.
2. Some discussion on how the proposed dataset compares to real-world datasets and its characteristics would benefit the paper

### Questions
1. Are there any specific graph structures or spreading patterns where EDBD might underperform compared to other methods?
2. How sensitive is the performance of EDBD to the choice of hyperparameters in the energy-aggregation scheme?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel task called spreading out-of-distribution (OOD) detection, which focuses on identifying OOD nodes within graph structures, particularly emphasizing the interactions and influence these nodes have on their neighbors. The authors leverage epidemic spreading models to create realistic benchmarks that reflect the dynamics of OOD node propagation in real-world scenarios. The authors propose an innovative approach known as the Energy Distribution-Based Detector (EDBD), which utilizes energy scores to enhance the aggregation process of node information. This method aims to mitigate the mixing of OOD scores between in-distribution (ID) and OOD nodes, thereby improving the accuracy of OOD detection.

### Strengths
1.The creation of the Spreading COVID-19 dataset provides a realistic and relevant context for evaluating OOD detection methods. This dataset simulates real-world scenarios, making the findings more applicable to practical situations.
2. The authors conducted comprehensive experiments, comparing EDBD against several state-of-the-art methods across multiple datasets.
3. The paper is well-structured and clearly presents the methodology, experimental setup, and results, making it accessible for readers and researchers interested in the topic.

### Weaknesses
1. While the results demonstrate superior performance, the paper may lack comprehensive statistical analysis (e.g., significance testing) to support the claims of superiority over existing methods.
2.The energy-based aggregation approach may introduce additional complexity compared to simpler methods. This complexity could make the method less accessible for practitioners who may prefer more straightforward solutions.

### Questions
1. What is the sensitivity of EDBD to different hyperparameter settings? How do variations in these parameters affect the model's performance?
2. How does EDBD perform on larger graphs or more complex networks? Are there any scalability issues that arise when applying the method to real-world scenarios with extensive node interactions?
3. How interpretable are the results produced by EDBD? Can the authors provide insights into why certain nodes are classified as OOD based on the energy aggregation process?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper formulates spreading OOD detection, a new benchmark setup for node-level OOD detection method that incorporates interactions among OOD samples and establishes a new dataset called Spreading COVID-19 to benchmark the spreading OOD detection scenario in real-world data.

A node-level OOD detector called EDBD employs an attentive energy aggregation scheme that prevents the mixing of energies between ID nodes and OOD nodes. EDBD is applied to enhance the OOD detection.

### Strengths
**S1.**  This paper proposes a new benchmark that models the realistic spread of OOD properties across graph nodes. This setup provides a more applicable framework for real-world scenarios.

**S2.**  This paper leverages EDBD to prevent unwanted mixing of OOD and in-distribution (ID) nodes. By controlling the influence of energy distribution, EDBD achieves better OOD discrimination on proposed datasets and spreading situations.

**S3.**  The paper's aggregation scheme in EDBD is versatile and adaptable to various scenarios on graph-structured data.

### Weaknesses
 **W1.** 	The paper’s reliance on COVID-19 to introduce and validate the spreading OOD detection model may feel outdated. As COVID-19 has become less urgent as a topic, using it as the central example could reduce the model's perceived relevance. A more contemporary application, such as misinformation spread or novel pathogens, might enhance the model's applicability and appeal

**W2.** What’s the relationship of this new problem with other problems, e.g., node classification or outlier detection on graphs? I’m not sure what’s the main difference between this problem and the outlier detection problem. The outliers are not seen in the training set? Can these algorithms be used as the baselines? 

**W3.** The effectiveness of the EDBD approach heavily depends on the graph structure and quality of connectivity information. In cases where graph structures are incomplete or noisy, the method’s performance may degrade, potentially affecting its robustness in real-world scenarios.

**W4.** While the paper employs SI and SIS models for simulating OOD spreading, it leaves the integration of more complex epidemic models for future work. This limits the current approach's applicability to more intricate real-world spreading phenomena that may not be accurately represented by simple models.

**W5.** Although the "Spreading COVID-19" dataset simulates virus spread, the lack of training on actual epidemic or contagion data might reduce the generalizability of the model when faced with real-world data that includes nuanced spreading patterns not captured by synthetic simulations.

### Questions
**Q1.** How might the proposed spreading OOD detection model adapt to more complex epidemic models, such as SEIR (Susceptible-Exposed-Infectious-Recovered) or multi-host transmission models? Are there specific limitations or computational challenges that prevent their integration?

**Q2.** What steps could be taken to ensure the model’s robustness on graphs with missing or noisy edges and nodes? Would incorporating graph-denoising techniques or imputing missing links improve EDBD’s performance?

**Q3.** Have alternative case studies, such as the spread of misinformation or emergent diseases, been considered to showcase the model’s versatility? How might these cases impact the model's applicability and reception in current contexts?

**Q4.** What’s the relationship of this new problem with other problems, e.g., node classification or outlier detection on graphs?

### Soundness
2

### Presentation
3

### Contribution
2
