# Efficient Neural Common Neighbor for Temporal Graph Link Prediction

- Decision: Reject
- Scores: 6, 3, 5, 6

## Abstract
Temporal graphs are ubiquitous in real-world scenarios, such as social network, trade and transportation. Predicting dynamic links between nodes in a temporal graph is of vital importance. Traditional methods usually leverage the temporal neighborhood of interaction history to generate node embeddings first and then aggregate the source and target node embeddings to predict the link. However, such methods focus on learning individual node representations, but overlook the pairwise representation learning nature of link prediction and fail to capture the important pairwise features of links such as common neighbors (CN). Motivated by the success of Neural Common Neighbor (NCN) for static graph link prediction, we propose \textbf{TNCN}, a temporal version of NCN for link prediction in temporal graphs. TNCN dynamically updates a temporal neighbor dictionary for each node, and utilizes multi-hop common neighbors between the source and target node to learn a more effective pairwise representation. We validate our model on five large-scale real-world datasets from the Temporal Graph Benchmark (TGB), and find that it achieves new state-of-the-art performance on three of them. Additionally, TNCN demonstrates excellent scalability on large datasets, outperforming popular GNN baselines by up to 6.4 times in speed.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes TNCN, which is  a temporal version of NCN based on a memory-based backbone. Comprosing with three key parts: the memory module,the temporal CN extractor,,and the NCN-based prediction head, TNCN improves the performance in terms of efficiency and effectiveness. Comparing with a diverse set of baseline models, the experiments on five datasets demonstrate its outstanding performance.

### Strengths
1. The experiments is substantial and the result is good.  Comparing with 9 baseline models, TNCN performs best on three of the five selected datasets, which emphasizes its effectiveness.
2. The method section is clearly described using formulas. With clear definition and detailed formulas, the method is well-presented.
3. There are proofs on the theorems in appendix, which improves the professionalism of the paper.

### Weaknesses
1. Since the process is relatively complicated, it is recommended to provide a pseudo code to make it easier for readers to understand.
2. I suggest that the experimental part be supplemented with an analysis of the hyperparameters, which can make the values of the hyperparameters more reasonable.

### Questions
1. High surprings values will degrade TNCN's performance. So will the model performance decrease monotonically as the surprise value increases? In other words, will TNCN have the best performance when the surprise value is the lowest?
2. Why is the result of TNCN-0∼2-hop-CN lower than TNCN-0∼1-hop-CN on the commen dataset in Table 2, which is different from the other three datasets?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method for link prediction on continuous-time dynamic graphs (CTDGs), aiming to unify two prominent model families: memory-based models and neighbor-based models. The authors introduce TNCN, demonstrating experimentally that it performs better in certain configurations and is more efficient than existing models in the literature.

### Strengths
- **Evaluation**: The proposed model is evaluated on established benchmarks, enhancing the reliability of the results.

- **Engineering**: The paper introduces an engineering approach to combine common neighbor (CN) techniques with memory-based methods, integrating these two modeling approaches.

### Weaknesses
 **Presentation**: The abstract implies that common neighbor methods are primarily used in static graphs, overlooking their established role in dynamic graph modeling. Additionally, the motivation for combining memory-based and neighbor-based techniques is presented only briefly at the end of the introduction.

**Limited Novelty**: The proposed model's core components primarily consist of established techniques. For instance, the memory-based module closely resembles TGN, lacking additional innovations or a clear positioning relative to other memory-based approaches. Similarly, while TNCN incorporates common neighbor (CN) techniques with optimized computation, it employs multi-hop methods similar to those in models like CAWN, further limiting its novelty. The combination of these techniques, while potentially useful, does not represent a significant conceptual leap.

**Theoretical Claims**: The paper presents familiar results as novel contributions, such as the $O(∣E∣)$ memory complexity for event aggregation, along with upper and lower bounds that are established in prior work (e.g., Caen, 1998). Presenting these as new theoretical results may be misleading. The specific application of the result to memory-based methods, while technically correct, is not a novel insight, as the connection between event aggregation and the number of edges is well-established in the field of dynamic graph analysis.

The paper exhibits strong engineering but lacks clear new contributions. Theoretical results on memory complexity and specific experimental results are weak, with minimal performance gains in dynamic link prediction tasks. Given the limitations in presentation, contribution, and experimental validation, I recommend rejection.

**Experimental results**: While combining memory and neighbor-based methods is interesting, the observed performance gains are minimal, with certain results (e.g., in Table 5) showing limited improvement using unclear metrics (possibly AUC or AP). Furthermore, the reported improvements on some datasets are not substantial enough to justify the complexity of the proposed model, especially given the incremental nature of the core components.

### Questions
1. Could you clarify the main novelty of your memory-based module and its differentiation from TGN?
2. What is the specific metric used in Table 5? Understanding whether it's AUC or AP is essential for interpreting the results.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The author focuses on link prediction tasks in temporal graphs, which have ubiquitous applications in real-world systems. Instead of implicitly encoding common neighbor features from the historical neighborhood of the target node, the author proposes the Temporal Common Neighbor Extractor to explicitly integrate these features into the process of temporal graph representation learning, achieving both effectiveness and efficiency compared to existing methods on the TGB benchmark. Additionally, the author provides theoretical analysis based on their proposed method, offering a more thorough illustration of the model.

### Strengths
This paper has several strengths worth noting:

* **Interesting Motivation.** The motivation for extracting common neighbor features is compelling.
* **Extensive Experiments.** The author has designed a variety of experiments to demonstrate the effectiveness and efficiency of their methods.
* **Well-Organized Representation.** The paper is well-structured, and the theoretical analysis provides strong support for the proposed methods.

### Weaknesses
However, the paper also has some weaknesses, outlined as follows:

*   **Lack of Novelty.** Firstly, the idea of extracting common neighbors in temporal graphs has certainly been explored before. It seems that the design of your key component, the "CN Extractor," closely resembles existing work in KDD2024 [1]. Moreover, your CN extracting component does not appear to include any specific improvements for temporal graphs. Simply extracting "monotone k-hop events" does not substantiate this claim.
*   **Lack of Important Baselines.** Since you "extend Neural Common Neighbor for static prediction methods," these static methods should also be included in your comparisons.
*   **Lack of Case Study.** Providing specific case studies could enhance the understanding of your method.
*   **Ambiguous Expression.** What does $emb$ mean in Equation 2? It seems you haven't explained it anywhere—does it refer to memory? Your method encodes the common neighbor neighborhood composed of source-destination node pairs; might this lead to a loss of other information (e.g., nodes that are not common)?
*   **Parameter Analysis.** Given that your method is based on multi-hop common neighbors, analyzing parameters across different multi-hop settings could better validate the robustness of your model.

### Questions
Q1: In what ways does your approach build upon or differ from existing methods that also extract common neighbors in temporal graphs?

Q2: Can you clarify the importance of including static baselines in your experiments, and how their absence affects the interpretation of your results?

Q3: What specific case studies can you provide to illustrate the practical application and effectiveness of your proposed method?

Q4: Can you provide a detailed explanation of the notation used in your equations, particularly regarding $emb$ in Equation 2, and how this impacts the overall methodology?

Q5: How do you plan to conduct a thorough parameter analysis for the multi-hop common neighbors, and what insights do you anticipate this will provide regarding your model's robustness?

### Soundness
3

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
4

### Summary
The paper is about temporal link prediction, which is an interesting topic. The authors propose a temporal version of NCN for link prediction in temporal graphs, which dynamically updates a temporal neighbor dictionary for each node and utilizes multi-hop common neighbors between the source and target node to learn a more effective pairwise representation. The paper is well written and well organized. However, there are several concerns in the current version of the paper that addressing them will increase the quality of this paper.

### Strengths
1 Cutting-edge research directions.

2 Clear writing logic.

3 Sufficient experimental results.

### Weaknesses
1 The authors should have a special discussion on whether the biggest difference between TNCN and NCN is the core contribution of this paper. If so, this should be highlighted. If not, more introduction is needed on the importance of the new scenario.

2 Since the strategy proposed in the paper is built around the batch processing mode of sequential graph learning, whether the batch size will have a different impact on the strategy is something that needs to be considered and discussed.

3 The motivation and contribution of the paper are worthy of recognition, but in the main text, the authors can consider putting more emphasis on the contribution description and logical arrangement. At present, it seems that the proof takes up a certain amount of space, making the method and experiment part seem less substantial, and the information that can be expressed is not clear and comprehensive enough.

4 The authors could consider discussing the computational complexity, especially comparing it to similar methods (including static graphs and temporal graphs).

### Questions
As above.

### Soundness
3

### Presentation
3

### Contribution
3
