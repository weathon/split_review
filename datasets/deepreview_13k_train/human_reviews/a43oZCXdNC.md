# Space-time self-attention for graph signal processing

- Decision: Reject
- Scores: 5, 5, 1, 3, 5

## Abstract
This work introduces a Transformer-based approach for graph signal processing that leverages a novel task-specific attention mechanism, namely NTAttention. 
Unlike conventional self-attention mechanisms, our method attends to all nodes across multiple time steps, enabling the model to effectively capture dependencies between nodes over extended time periods. This addresses a key limitation faced by traditional methods.
Additionally, we propose geometry-aware masking (GMask), which incorporates  the graph topology into the sparsification of the self-attention matrix. This enhances efficiency while preserving the rich temporal information conveyed by the nodes. 
We demonstrate the effectiveness of our approach on two critical applications: EEG seizure detection and traffic forecasting. Both tasks involve data collected from fixed sensors, such as electrodes or road sensors, where data from one sensor can influence others temporally and spatially. Our model enhances sensitivity in fast seizure detection by 20 percentage points compared to  state-of-the-art and significantly outperforms current methods in traffic forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes NTAttention, a Transformer-based approach for graph signal processing that effectively captures spatio-temporal dependencies. Additionally, a geometry-aware masking technique (GMask) is proposed to enhance computational efficiency while preserving temporal information. The authors extensively validated the effectiveness of NTAttention on EEG seizure detection and traffic forecasting tasks

### Strengths
1. The model proposed in the article has good computational efficiency by GMask.
2. The model can better address long-range space-time dynamics.

### Weaknesses
1.Comparing Table 1 and Table 2, why is the model not discussed in terms of capturing the temporal nature in traffic forecasting, and why is spatial dependency not discussed in seizure detection?
2.Why can the method proposed in the article capture long-range information? We hope the authors can provide some methods and insights to solve this problem. At the same time, we hope the authors can provide specific examples of long-range information in EEG seizure detection and traffic forecasting. For tasks related to high-frequency, where capturing long-range information is not necessary, would the use of NTAttention lead to a decrease in performance?
3.In line 229, how is vector r obtained; in line 290, how is the calculation of \sigma obtained, it seems that the standard deviation of the distances requires N^2 samples.
4.We hope the authors can provide the calculation method of the metrics, such as sensitivity, specificity, and their meanings.
5.NTAttention seems to have a large variance; we hope the authors can provide significant experimental evidence.

Minor problems:
1.It is suggested to remove the frames from Figure 1, 2, and Figure 4.
2.There are issues with the layout of the article, such as Table 7, 8, etc.

### Questions
Please see my comments for details

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
NTAttention, introduced in the paper, incorporates temporal encoding and spatial encoding within the self-attention framework, effectively capturing spatial and temporal long-term dynamics of graphs. It dynamically attends to all nodes, gated by geometric distance between nodes derived from the Gaussian kernel with a threshold, namely GMask. Use of this mask effectively sparsifies the attention matrix by limiting attention to spatially relevant nodes, improving both efficiency and accuracy. NTAttention is evaluated on two main tasks, EEG seizure detection and traffic forecasting where each exhibits highly complex spatial and temporal dynamics across graphs.

### Strengths
1. Efficient Spatio-Temporal Attention: NTAttention with GMask enables dynamic geomtery-aware attention based on geometric distances, allowing it to effectively capture long-term dependencies in complex graph structures.

2. NTAttention + GMask achieves competitive result in terms of both model performance and efficiency in comparison to various other baseline models.

### Weaknesses
- Lack of novelty : Used methods (temporal encoding, spatial encoding, and Gaussian kernel with a threshold as an adjacency matrix between nodes) are all pre-existing techniques. NTAttention simply suggests a new combination of all those. While this combination well serves the purpose of handling complex spatial and temporal dependencies in graphs, it lacks fundamental novelty in core architecture.

- The reported score (AUROC, F1-score) for transformer in the referenced paper REST (Afzal et al., 2024) is different from yours in Table 5 (Clip Size 12-s). Any reason why?

- Seizure detection results in table 5 show notable drops in performance across all metrics when using GMask, failing to achieve SOTA scores. Seems like while GMask improves computational efficiency by sparsifying attention, it limits the model's capacity to capture spatiotemporal interactions between nodes to some degree. These results raise concerns about the practical usability of GMask, as the trade-offs in performance may outweigh its benefits, especially for certain tasks requiring high sensitivity and precision.

### Questions
- Please explain how NTAttention introduces novelty beyond existing techniques, particularly in terms of core architectural contributions.

- It seems unclear how exactly the relative temporal encoding is done to construct $r_{tt'}^{V}, r_{t't}^{Q}, r_{tt'}^{K}$. Are they simply trainable bias vectors that depends solely on the temporal difference between time steps $t$ and $t'$?

- The reported score (AUROC, F1-score) for transformer in the referenced paper REST (Afzal et al., 2024) is different from yours in Table 5 (Clip Size 12-s). Any reason why?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
- This paper introduces NTAttention, a novel self-attention mechanism designed for processing temporal graph signals. The proposed method allows nodes to attend to both spatial and temporal dimensions simultaneously while incorporating graph topology through geometry-aware masking (GMask). 
- The authors show the effectiveness of their approach on 2 applications: EEG-based seizure detection and traffic forecasting.
- They achieve state-of-the-art performance on 2 applications.
- The proposed method maintains computational efficiency through GMask while offering a flexible framework.

### Strengths
- The authors introduce an innovative unified attention mechanism that simultaneously handles node and temporal relations.
- The proposed method achieves state-of-the-art performance in two distinct applications.
- The proposed method demonstrates robustness across multiple domains with minimal architectural changes.
- The proposed method improves performance while maintaining computational efficiency, making it practical for real-world deployments.
- The geometry-aware masking strategy provides a general approach that may benefit other attention-based architectures.

### Weaknesses
 - The paper's primary contribution appears incremental rather than novel:
  - The NTAttention mechanism is essentially a standard Transformer with added spatio-temporal encoding
  - The primary motivation of capturing "long-range dependencies" conflicts with GMask's function of blocking distant node attention
  - The complexity analysis $(O(N^2T^2))$ contradicts claims of computational efficiency
  - The theoretical foundation for selecting GMask threshold $k$ appears heuristic.

- The experimental evaluation lacks crucial analyses.
  - No rigorous comparison between GMask and random masking with equivalent masking ratios
  - Missing analysis of attention weight distributions compared to baseline models
  - Absence of ablation studies on the impact of different masking strategies in seizure detection
  - Limited scale validation (only 19 and 207 nodes)

- Several technical aspects require clarification.
  - The motivation for 2D coordinate-based spatial encoding versus traditional graph topology representations
  - The relationship between the attention mechanism and traditional GNN message passing
  - The stability guarantees for the learning process, especially with small k values in GMask
  - The impact of GMask on optimization dynamics

- Table 1's binary comparison (checkmark/x-mark) oversimplifies complex methodological differences
- The paper's title "Graph Signal Processing" is misleading.

### Questions
**Visualization and Presentation Issues:**
1. Why are $v_i^t$ and $v_j^{t'}$ depicted at position (5,5) on the diagonal in the self-attention matrix in Figure 1? This visualization needs clarification or correction.

2. The related work section on Traffic Forecasting primarily references studies up to 2021. Please include more recent developments in this rapidly evolving field.

**Comparative Analysis Concerns:**

3. Table 1 appears overstated. Notably, REST [1] shows a checkmark for criterion "C" in their paper, yet your table marks it with an x-mark. Please explain this discrepancy.

4. The binary (checkmark/x-mark) representation in Table 1 oversimplifies the comparison. A more thorough analysis of similarities and differences would serve readers better and avoid potential misunderstandings.

**Masking Analysis:**

5. Table 7's comparison between GMask and RandomMask requires more rigorous analysis. Can the authors compare where the random masking ratio matches GMask's masking ratio?

6. Please explain why "No Mask" performs comparable to GMask while RandomMask, WindowMask, and BigBird show significantly higher errors.

7. Can the authors extend the analysis in Table 7 to include Seizure Detection results?

**Methodological Clarifications:**

8. How does NTAttention differentiate itself from existing Transformer-based time-series forecasting models beyond adding spatio-temporal encoding?

9. The selection of GMask's threshold parameter $k$ appears heuristic. Can the authors provide domain-specific insights into why optimal $k$ values differ between traffic forecasting and seizure detection?

10. Particularly, why does your method perform best with $k=0$ for seizure detection when REST[1] reports optimal performance at k=0.9?

11. Given that STGCN[2] uses a similar adjacency matrix creation method with a threshold of 0.5, does this suggest similar operational principles between masking matrices and graph convolution in traffic forecasting?

**Performance Analysis:**

12. Please analyze why the GMask application degrades performance in seizure detection (Table 5).

13. The paper's emphasis on capturing "long-range dependencies" seems to contradict GMask's function of blocking attention between distant nodes. Can the authors quantify the extent of this attention blocking to better support your claims?

**Comparative Framework:**

14. In traffic forecasting, Please include and compare with recent studies using adaptive adjacency matrices[3,4] and alternative spatial dependency approaches[5,6].

15. Can the authors analyze the distributional differences between your attention matrices and the adjacency matrices used in STGCN and DCRNN?

16. How do your attention weights compare with other self-attention baseline models?

**Theoretical Concerns:**

17. The claim that "traditional methods have struggled to account for long-range dependencies" needs stronger experimental or theoretical support.

18. Please provide detailed analysis of how $\alpha(N)$ affects computational complexity in practical applications, given the $\mathcal{O}(N^2T^2)$ theoretical complexity.

19. Is 2D coordinate encoding sufficient for representing graph topology? How does this compare to Hadamard Attention's use of pre-defined adjacency?

20. Can the authors discuss the expressiveness of your attention mechanism compared to traditional GNN message passing?

21. How do you ensure learning stability with GMask, particularly regarding potential node isolation with small $k$ values?

22. From the perspective of model optimization, the proposed structure of GMask seems to affect the optimization of the model. Can you discuss this further?

**Title Recommendation:**

23. The title "Graph Signal Processing" may mislead readers as the paper doesn't employ traditional GSP concepts (graph Fourier transform, spectral analysis, graph wavelets). Consider revising to reflect the actual content better.

> [1] Afzal, Arshia, et al. "Rest: Efficient and accelerated eeg seizure analysis through residual state updates." ICML 2024
>
> [2] Yu, Bing, Haoteng Yin, and Zhanxing Zhu. "Spatio-temporal graph convolutional networks: a deep learning framework for traffic forecasting." IJCAI 2018.
>
> [3] Bai, Lei, et al. "Adaptive graph convolutional recurrent network for traffic forecasting.” NeurIPS 2020
>
> [4] Choi, Jeongwhan, et al. "Graph neural controlled differential equations for traffic forecasting." AAAI 2022
>
> [5] Fang, Zheng, et al. "Spatial-temporal graph ode networks for traffic flow forecasting." KDD 2021


---


---

# $\color{red}{\text{Final Recommendation to Area Chair}}$ **(Edited at 2:15 PM on 3rd Dec (AOE))**

During the final stage of discussion with the authors, I discovered a critical flaw that drive me to reduce my score from `3` to `1`. Through careful code inspection, I identified that their unusual error trends in different forecasting horizons stemmed from a fundamentally incorrect evaluation protocol (see `Table 6`).

The authors' implementation reveals they train separate models for different forecasting horizons (3, 6, 12 steps) by using only the last few timestamps of historical data, as evidenced by their code:

```python
self.timepoints = 3
self.node_time_proj = torch.nn.Linear(207*self.timepoints, 207)
```

This approach fundamentally violates the standard practice in traffic forecasting where:
1) models receive a complete 12-step historical sequence as input
2) forecast a complete 12-step future sequence
3) report metrics for horizons 3, 6, and 12 from this single predicted sequence

The authors' claim of fair comparison is weakened by this serious error, which makes their results incomparable with existing work and could mislead future researchers in the spatiotemporal forecasting community.

The authors need to completely revise their experimental setup to align with established practices in traffic forecasting. Thus, I believe the reduction in score is warranted.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This study proposed NTAttention for targeting seizure detection and traffic forecasting.NTAttention effectively utilizes the inherent positional and temporal information in the data by integrating spatial encoding into the features of each node and integrating relative temporal encoding into the attention matrix. Simultaneously using geometric perceptual masks to improve model efficiency.

### Strengths
1.The authors address the challenge of capturing long-range dependencies in temporal graph signals, which is a non-trivial extension of existing methods. 
2.By integrating spatial encoding into node features and relative temporal encoding into the attention matrix, NTAttention combines graph topology with temporal dynamics in a creative way. 
3. The authors provide a solid theoretical basis for NTAttention, including the formulation of the attention mechanism and the geometry-aware masking (GMask).

### Weaknesses
1.The authors demonstrate the effectiveness of NTAttention on EEG seizure detection and traffic forecasting. However, 
testing the model on more diverse datasets, particularly those with different characteristics, could further validate the 
generalizability of the approach. 
2.This article compares NTAttention with several baselines, but can be compared with the latest developments in GNN models, 
especially those designed for spatiotemporal data, which can provide more rigorous benchmarks. 
3.Providing theoretical insights into the convergence properties of NTAttention, especially in the context of non-stationary graph signals, could be a valuable contribution

### Questions
1. Generalizability Across Datasets: 
Will the authors consider testing NTAttention on additional datasets to further demonstrate its generalizability beyond 
EEG seizure detection and traffic forecasting? 
2. Comparison with State-of-the-Art GNNs: 
Could the authors comment on why they chose not to compare NTAttention with the most recent GNN models designed for spatio-temporal data, and would they consider adding these comparisons in a revised version? 
3. Data Privacy and Ethical Considerations: 
Could the authors discuss how they ensure data privacy, particularly for sensitive health data used in the EEG seizure 
detection task? 
4. Scalability to Large Graphs: 
Can the authors provide more details on the scalability of NTAttention to very large graphs, including any potential limitations they have encountered?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposed NTAttention for graph signal processing tasks, specifically targeting
seizure detection and traffic forecasting. By incorporating spatial encoding into each node’s features
and relative temporal encoding into the attention matrix, NTAttention provides a new way to learning with spatial-temporal data.

### Strengths
1. Developing a representation learning framework that could integrate both spatial and temporal information from the data is an important and meaningful learning problem.

2. The proposed method achieves good performance on the seizure detection and traffic forecasting tasks.

### Weaknesses
Overall, I think the empirical evaluation should be more solid, to provide more understanding of the problem and the proposed method:

1. Lack of intuition behind the method: it is quite unclear to me why the proposed way to encode spatial information in the node embedding, then add in the temporal information in the attention mechanism is a good way to encode these two types of information. For example, why not add in the temporal information in the node embedding, and then use the spatial information in the attention mechanism. I think the paper could strengthened by adding a discussion about reasons leading to the specific design choices. Specifically, the paper lacks a clear explanation of why fixed spatial encodings are added to node embeddings, while relative temporal encodings are incorporated into the attention matrix. The rationale for this specific combination, as opposed to other possibilities, is not sufficiently justified. The paper should explore the impact of alternative encoding combinations, such as using temporal encodings within the node embeddings and spatial encodings within the attention mechanism, to demonstrate the superiority of the chosen approach.

2. Lack of comparison and ablation studies: to study the problem above, I feel it would be helpful to conduct more ablation studies investigating the design choices. It is good that the proposed mechanism seems to work well for the two proposed tasks, but I think it would also be worthwhile to see how robust the performance is to the specific design, and how would different components affect the performance (besides the effect of the mask in 4.3). The ablation study should include a more comprehensive analysis of different encoding strategies, including fixed vs. rotational spatial encodings and fixed vs. relative temporal encodings, to understand their individual and combined effects on performance. Furthermore, the impact of different masking strategies should be investigated more thoroughly, beyond just comparing GMask with other methods. It would be beneficial to understand why certain masking strategies fail and how their failures relate to the specific characteristics of the spatiotemporal data.

### Questions
1. In equation (2), what is $T_{tt'}$?

2. What are the criteria used when selecting the seizure detection task and the traffic forecasting task in this work? I understand these are important tasks, but given how many potential applications that could involve space-time dynamics, I am wondering what characteristics a task should have that make the proposed framework suitable and effective.

3. Is there a reason why GMask seems only to help with the traffic forecasting task but not the seizure detection task? Could you investigate this further? Also any idea why other masking strategies seem to work worse than even no masking?

### Soundness
2

### Presentation
3

### Contribution
2
