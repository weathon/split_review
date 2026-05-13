# Energy and Memory-Efficient Federated Learning with Ordered Layer Freezing and Tensor Operation Approximation

- Decision: Reject
- Scores: 6, 3, 5

## Abstract
The effectiveness of Federated Learning (FL) in the context of the Internet of Things (IoT) is hindered by the resource constraints of IoT devices, such as limited computing capability, memory space and bandwidth support. These constraints create significant computation and communication bottlenecks for training and transmitting deep neural networks. Various FL frameworks have been proposed to reduce computation and communication overheads through dropout or layer freezing. However, these approaches often sacrifice accuracy or neglect memory constraints. In this work, we introduce Federated Learning with Ordered Layer Freezing (FedOLF) to improve energy efficiency and reduce memory footprint while maintaining accuracy. Additionally, we employ the Tensor Operation Approximation technique to reduce the communication (and accordingly energy) cost, which can better preserve accuracy compared to traditional quantization methods. Experimental results demonstrate that FedOLF achieves higher accuracy and energy efficiency as well as lower memory footprint across EMNIST, CIFAR-10, CIFAR-100, and CINIC-10 benchmarks compared to existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The edge applications leveraging FL are highly constrained by resources, in terms of computation and communication. Existing efficient FL solutions either compromise accuracy or ignore memory usage. They introduce the ordered-layer-freezing and Tensor Operation Approximation for reducing memory footprint & communication overhead.

### Strengths
Tensor Operation Approximation is used to reduce the communication overhead of FL.
Various test results across small datasets are demonstrated.

### Weaknesses
layerfeezing technique is not new. Novelty seems to be marginal


### Questions
No.

### Soundness
2

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
The proposed approach, FedOLF, combines the layer freezing method and Tensor Operation Approximation (TOA) to reduce the memory and computation requirements of the training process in federated learning settings for the memory-constrained IoT devices/systems. Experimental results show better overall accuracy with low memory, and energy usage compared to prior works, for different datasets like EMNIST, CIFAR-10, CIFAR-100, and CINIC-10.

### Strengths
1.	Applying TOA to frozen layers preserves model accuracy while reducing the communication cost.

2.	The experimental results of FedOLF on different iid and non-iid datasets and architectures demonstrate its adaptability and advantage in both energy and accuracy over baseline methods.

### Weaknesses
1.	The paper offers limited novelty, as FedOLF's approach combines previously explored techniques, partial neural network freezing and TOA. The combination of existing techniques, although seems useful, requires more thorough evaluation to distinguish the scenarios and system configurations in which it outperforms the state-of-the-art techniques and scenarios and systems configurations in which it offers sub-optimal results. Specifically, how well the technique performs compared to state-of-the-art for system configurations in which most of the clients are resource constrained (in terms of memory and compute both)? Also, the paper should demonstrate the performance of the proposed technique for non-uniform clusters of devices. Additionally, the proposed technique should be evaluated for cases with a skewed distribution of classes. All these analyses will provide a detailed performance comparison with the state-of-the-art techniques and a better understanding of the significance of the novel contributions presented in the paper.

2.	FedOLF assumes that "low-level layers across various local models usually have higher degrees of Centered Kernel Alignment (CKA) similarity," allowing frozen layers to generalize across clients without retraining. While Table 1 shows strong accuracy compared to the benchmark models in non-IID settings, supporting FedOLF's effectiveness, it does not directly validate this assumption of universal feature similarity. In real-world scenarios with highly diverse data (e.g., medical vs. satellite images), this may not hold true, and the frozen layers will become less useful for some clients. To validate this assumption, the experimentation should include more types of non-IID characteristics, such as label distribution skew, feature distribution skew, and quantity skew across clients. Additionally, a theoretical analysis of the conditions under which CKA similarity holds or fails, as well as experiments for validating this similarity across different layers and datasets, would be useful. Moreover, it could be interesting to perform a more in-depth analysis of the performance of the individual layers when considering the heterogeneity of the data; it may offer more detailed insights into the practical limits of the proposed approach.

3.	The number of frozen layers is determined just based on the memory footprint of different options, and the computational requirements are not considered. The authors should highlight how this is scalable to systems composed of devices with diverse set of computational capabilities. Moreover, is considering just the memory footprint for real systems sufficient? If not, what modifications are required in the proposed technique, and how incorporating computational requirements into the layer freezing decision can improve the performance of the proposed technique for practical systems?

4.	By freezing specific low-level layers, FedOLF implicitly assumes that the representation error from these frozen layers will diminish as training progresses. While the paper claims that these errors vanish empirically, a detailed analysis of error propagation through frozen layers seems missing. To address this, a layer-by-layer analysis of error propagation throughout training, using visualizations like heat maps to track error dynamics, is required. Additionally, experiments that vary the number and position of frozen layers could provide crucial insights into how these changes impact error propagation and overall model performance.

### Questions
The overall contributions seem marginal and further evaluations are necessary to uncover the true potential and limitations of the proposed technique. Besides addressing the above-raised comments in the weakness section, following questions also need particular attention.

1.	What general guidelines or thresholds can be provided for setting the scaling factor s in TOA, beyond using a grid search, to balance accuracy and communication costs effectively? or maybe is there a way to determine the optimal value of s without using grid search?
2.	The TOA technique in FedOLF uses a fixed scaling factor across all clients, which might not fit well for devices with different processing power (different hardware). Therefore, it is important to explore a more flexible, client-specific scaling factor to improve FedOLF's efficiency on diverse IoT devices?
3.	To emulate system heterogeneity, why only the case of uniform clusters is considered? 
4.	In the context of Section 3.5, how many clients with full network training capacity are necessary for this technique to offer reasonable (and fast) convergence? Also, can this technique be used when most of the devices are significantly memory constrained. If yes, what are the limits? Also, how does the proposed technique compare with the state-of-the-art techniques under such scenarios. 
5.	How well the technique performs in cases with a skewed distribution of classes (and general categories) across devices? Are there any data-level assumptions that have to be valid for the technique to offer reasonable results? 
6.	What is the impact of the proposed technique in cases with significant computational power imbalance between devices? What is the impact of such cases on the overall training time?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes the FedOLF framework that aims to improve the efficiency of FL for resource constrained devices. The key observation behind the work is that by allowing the update of the layers of a network in an ordered manner, energy and memory costs can be reduced without significant sacrifices in the performance of the system. The authors move further and enhance the efficiency of their system by employing Tensor Operation Approximation demonstrating better results in their setting compared to traditional quantization approaches. 

One of the main claimed contributions of the work, which is also the basis of the method, is the vanishing representation error. That is by imposing an ordering of the layers that are frozen in any update, the authors demonstrate a bound on the representation error of the active layers as a function of the last frozen layers.

### Strengths
The idea (and proof) of bounding  the approximation of the true gradient through layer freezing under certain condition is important and can be used for the design of topologies that operate under such regime. 

The experimental results show significant performance gains in the specific benchmark tests.

### Weaknesses
 The idea of tackling the energy and memory consumption in FL by frozen a number of layers is not new and many works have already utilised this approach. The novel claimed contribution is the strategy of the ordering of the updating. Given that it is well known that more high level layers are more important for specific tasks compared to the early layers that have the job to extract more generic features, such approach is not so surprising.

The memory footprint can also be tackled by re-evaluating part of the results in an on-demand manner. As such, someone can trade off time for training vs memory footprint. Given that for many devices the computational cost (in terms of energy) is less than the communication cost, it is unclear how such approach would compare on the overall energy cost vs quality of training with the proposed method that chose to freeze some of the layers for addressing the memory requirements.

A key observation/assumption that underpins the theoretical working of the method is that the upper bound B is likely smaller that one. However this is only based on few networks and datasets and I found difficult to justify the above statement 

In the experimental section, it was not clear to me what is the assumption of the quality of the training of the original network. For example, I would expect ordered layer freezing to perform well if the original model was not very far (and especially the initial layers) from the true one, where if you give to the system a network with random parameters (extreme case) then the initial layers would not be very informative and any imposed freezing on them would not lead to meaningful training for the rest of the layers. The authors should comment on that.

### Questions
it is not clear to me how the communication energy consumption is captured in this experiment. How do the authors provide their relative weights? 

Regarding Table 1. There is no evidence that the final achieved accuracy would be better in the proposed system compared to the rest. Is the target number of iterations that give this result? How the performance of the above algorithms change with the iteration number T?

Someone would expect the benefits of the method to become more profound as the number of layers in the network increases. However, Table 1 shows that this is not the case and the gap between the proposed method and STL closes (even for T=500). Can the authors comment on that?

### Soundness
2

### Presentation
3

### Contribution
2
