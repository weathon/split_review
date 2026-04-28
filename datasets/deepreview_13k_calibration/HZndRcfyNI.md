# Principled Architecture-aware Scaling of Hyperparameters

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Training a high-quality deep neural network requires choosing suitable hyperparameters, which is a non-trivial and expensive process.
Current works try to automatically optimize or design principles of hyperparameters, such that they can generalize to diverse unseen scenarios.
However, most designs or optimization methods are agnostic to the choice of network structures, and thus largely ignore the impact of neural architectures on hyperparameters.
In this work, we precisely characterize the dependence of initializations and maximal learning rates on the network architecture, which includes the network depth, width, convolutional kernel size, and connectivity patterns.
By pursuing every parameter to be maximally updated with the same mean squared change in pre-activations, we can generalize our initialization and learning rates across MLPs (multi-layer perception) and CNNs (convolutional neural network) with sophisticated graph topologies.
We verify our principles with comprehensive experiments.
More importantly, our strategy further sheds light on advancing current benchmarks for architecture design.
A fair comparison of AutoML algorithms requires accurate network rankings.
However, we demonstrate that network rankings can be easily changed by better training networks in benchmarks with our architecture-aware learning rates and initialization.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work provides an extension of $\mu$transfer to arbitrary network structures and an application of the resulting method to neural architecture search (NAS), specifically in order to make NAS benchmarks more comparable by ensuring all competing networks are given a better chance to train. The major contributions:

* An improved way to set initializations and layer specific learning rates to stabilise training over network scales
* Experimental results demonstrating that NAS benchmarks are flawed: making the training process more stable massively changes the results

Weights are initialized to be normally distributed with variance:
$$
\sigma^2 = \frac{C^{(l', l)}}{n} = \frac{2}{d_{in}^{(l')}}
$$
for an $n \times n$ weight matrix with $d_{in}^{(l')}$ in-degree (the number of connections to the layer from the previous layer).
Also, the final layer is scaled by $\propto \frac{1}{n^2}$.

Scale the layerwise learning rates according to
$$
\eta^{*} \simeq c \left( \sum_{p=1}^{P} L_p^3 \right)^{-1/2}
$$
where $c$ is a layer-independent constant and $L_{p}$ is the number of relu layers on path $p$.

### Strengths
Neural Architecture Search needs a way to verify that the networks being searched over are actually being trained sufficiently. The goal of this paper to standardise that process around a framework that should allow much more reliable results in this area of study.

I have not checked all the derivations but the theory appears to be correct. I am confident that I could verify the results if I had more time.

The contributions as presented are met:

* The initialization is provided, justified and works in the experiments
* The extension to $\mu$P is introduced clearly and also works in experiments
* Experiments demonstrate a key failing of NAS benchmarks and present a solution

The two limitations in the literature that this paper addresses are:

1. $\mu$P is not defined for arbitrary DAGs, only feedforward networks
2. Neural Architecture Search benchmarks are useless if we can't trust that the networks have been trained well

The presentation is good, explaining the key points of the $\mu$P paper in a brief way, better than the original paper.
The authors use an idiosyncratic system of emphasis, using both underlines and bold fonts on key points. This actually works quite well and I found the points being emphasised generally did earn more attention. The authors also use § in place of "Section", which I guess saved space, and works just as well.

### Weaknesses
The initialization, learning rate tuning and layer specific learning rates are introduced to maintain the update scale at $O(1)$ but the update scale during training doesn't appear to have been measured. It would be nice to see empirical verification that the method is working as intended. Although, I understand that the results in 4.1 and 4.2 both indicate that it is.

Given the equations above it is not easy for the reader to replicate the exact initialization and learning rate scaling required. Some pseudocode or a reference implementation would help a lot. It's been a problem for $\mu$P adoption as well, that practitioners find that there were ambiguities in the description that make it hard to implement in practice. For example, I don't know where the $c$ parameter is set and I'm not fully confident how to count the number of paths to produce $L_p$.

It is stated "the final layer weights are initialized with variance $1/n^2$ instead of $1/n$" on page 5, and I know this is from $\mu$P but it is never stated in this paper why.

Minor presentation issues:

1. "most designs of principles" in abstract doesn't make sense
2. Why is the MSE loss introduced in equation 6? The experiments are mostly classification results using a cross-entropy loss
3. Equation 8 contains $L_p$ but $L_p$ is only defined in the Appendix, it should be defined near the equation
4. Section 3.5 "speed-up" -> "speeds up"

### Questions
For each network architecture sampled in the NAS-Bench experiments, the network learning rate is first tuned at small scale. Was the learning rate also tuned on the networks being trained without this hyperparameter transfer method? This may already be in the experiments section or the Appendices and I may have missed it.

Why are the maximal LRs found by experiment in Section 4.1 and 4.2 not the same as those computed by the theory? Is there any way they could be brought closer together?

How was the experiment in Sections 4.1 and 4.2 performed? I guess you find the optimal learning rate at a small scale on a set of networks, then scale the network up using the method described in the paper to scale the initalization and learning rates, then perform a grid search to find the optimal learning rates to compare against?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper aims to establish principles for initializing and selecting learning rates in neural network architectures characterized by directed acyclic graphs (DAGs), which can be highly irregular in structure. The authors propose an initialization method to maintain pre-activation variance during forward propagation and derive architecture-specific learning rates using a maximal update prescription. Experimental validation demonstrates their effectiveness and potential for improving neural architecture search benchmarks by enhancing network training and rankings.

### Strengths
-	The paper builds on previous research in hyperparameter and architecture search, aiming to establish a principled connection between weight initialization and learning rate choices with both MLP and CNN architectures.
-	It introduces an architecture-aware modified fan-in initialization scheme that preserves information flow through various graph topologies.
-	The paper analytically derives formulas for scaling learning rates based on architecture topology, specifically using the maximal update (μP) heuristic.
-	Experimental results demonstrate the superior performance of the proposed methods and highlight their potential to reshape network rankings in standard NAS benchmarks.
-	These findings suggest that implementing the proposed principles may lead to improved evaluations of NAS algorithms.

### Weaknesses
 - The clarity of the main body could be improved a lot, via providing a concise summary of main derivations, potentially by reducing the repetitive criticism of architecture search.
- The experimental section raises several concerns. The strategy of finding a base maximal learning rate for one epoch may not be meaningful for practical training cycles, where learning rates follow complex schedules. The criticism of NAS for using "the same hyperparameters" overlooks the intricate learning rate strategies commonly employed. Specifically, many NAS methods employ sophisticated learning rate schedules like cosine annealing with warm restarts, which are far from a single fixed learning rate. These nuances are not adequately addressed, and the critique is therefore not fully justified.
- The empirical results are also not entirely convincing. Figure 2 exhibits a weak correlation with questionable linearity and the data points appear quite scattered, making the claimed relationship less robust. Figure 3 has a limited range of learning rates, which makes it difficult to assess the true effectiveness across a broader spectrum of learning rates. The proposed improvements in Figure 4 seem to be primarily in lower accuracy regimes, raising doubts about absolute improvement on the top-performer architectures (which are of the most interest). The improvements at higher accuracies are marginal and could be attributed to random variations rather than a significant benefit of the proposed method.
- The discussion of prior art is limited, particularly regarding weight initialization and learning rates, and it's unclear how the proposed method advances over existing insights in the literature. The paper does not sufficiently engage with the extensive body of work on adaptive learning rate methods (e.g., Adam, RMSprop) or more advanced initialization techniques beyond basic fan-in/fan-out approaches. This lack of contextualization makes it difficult to understand the novelty and contribution of the proposed method.

### Questions
See previous section of weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for optimizing hyperparameters in deep neural networks that takes into account the impact of neural architectures on hyperparameters. The authors characterize the dependence of initializations and maximal learning rates on the network architecture, including depth, width, conv kernel size, and connectivity patterns. They generalize their initialization and learning rates across MLPs and CNNs with sophisticated graph topologies. The authors verify their principles with comprehensive experiments and demonstrate that network rankings can be easily changed by better training networks in benchmarks with their architecture-aware learning rates and initialization.

### Strengths
-	The paper begins with a compelling motivation, shedding light on prevalent trends in the current literature landscape. It questions the evaluation of architectural choices and the often overlooked dependency on hyperparameters.
-	The paper provides thorough and well-supported proofs for its derivations related to initialization and maximal learning rates. It introduces a straightforward adjustment to weight initialization by scaling with the layers' in-degree, leading to notable performance enhancements downstream.
-	While the derivation draws substantial inspiration from previous works, it seems technically correct (and original to certain extent), and diligently cites these sources. Although maybe not the most groundbreaking, gaining a deeper understanding of how to determine initial learning rates for specific architectures holds significant importance. 
-	The paper critiques the evaluation methodology employed in NAS benchmarks, uncovering significant shortcomings in the process in their experiments. The evaluation of NAS encompasses a wide range of comprehensive datasets, adding to the paper's robustness and relevance. There is a strong likelihood that the rules derived from this work could prove relevant and valuable for practitioners.
-	The paper exhibits excellent writing and organization, ensuring a smooth reading experience.

### Weaknesses
A few questions seem to hinder my understanding of this paper’s contributions, particularly with regard to the root causes behind the perceived limitations of the μP method.

First, the paper argue that their proposed method outperforms the μP initialization and scaling method introduced by Yang et al. in 2022, often achieving significantly better results. Noting that μP results were not included in the main paper and were instead instead deferred to a much later section E.3.

From a theoretical standpoint, Yang et al. (2022) primarily derived their scaling strategy for multi-layer perceptron (MLP) architectures in their main text, with additional derivations provided in Appendix L. On the empirical side, Yang et al. (2022) also presented experimental results on hyperparameter transfer for ResNet and Transformer architectures.

The present paper introduces a novel Directed Acyclic Graph (DAG) tool to derive "architecture-aware" hyperparameters. However, a fundamental question remains: What are the specific failure modes of the μP when it encounters intricate network topologies? Is the limitation attributed to a violation of Desiderata L.1, or are there other contributing factors at play?

Additionally, further clarification is needed regarding the assumptions made and the empirical comparisons drawn, especially across various architectural configurations. For example, it was not clearly mentioned until late, that the authors’ theory cannot apply to normalization layers.

### Questions
Same as Weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provides valuable insights into the dynamic relationship among network architecture, initialization methods, and learning rates. It combines theoretical advancements with compelling empirical evidence, offering a precise characterization of how network architecture influences the interdependence of initialization strategies and the determination of optimal learning rates. The empirical evaluation is carried out on the NAS-Bench dataset, and the findings hold relevance not only for MLPs but also for CNNs with complex architectural designs. As a result, the implications of this research extend beyond the confines of deep learning theory, sparking meaningful reflections within the practical neural network design and NAS.

### Strengths
This paper delivers a compelling contribution that encompasses both theoretical and empirical dimensions. The clarity of its exposition, coupled with effective visual aids, greatly enhances comprehension of the concepts presented.

In terms of theoretical advancements, the authors expand upon the maximal-update (μP) scaling strategy initially introduced by Yang et al. in 2022. The authors delve into an investigation of how hyperparameters depend on various aspects of network architecture, including depth, connectivity patterns such as residual skips and long-range connections, kernel sizes, layer types, and convolution extensions. 

The authors establish a link between learning rate scaling and layer depth for the first time, demonstrating its effectiveness over approaches that do not account for depth. Section E2 shows that the method also extends to GeLU neurons.

The authors showcase that the proposed scaled learning rates and initializations bring improvements in achievable accuracies across a broad spectrum of neural network architectures within the NAS-Bench search space. This outcome bears significant implications for the practical design of neural networks and the field of NAS, particularly considering the widespread adoption of NAS-Bench as a guiding benchmark.

The introduction of scaled learning rates and initializations yields a noteworthy consequence by narrowing the performance gap between "good" and "bad" architectures within NAS-Bench (Figure 4). They prompts questions about the ranking of architectures within NAS-Bench, prompting a critical reassessment of progress within the NAS field.

### Weaknesses
While this paper, on the whole, demonstrates a commendable effort, I encountered two noteworthy concerns while reading the experimental section:

- The rankings of architectures may be influenced by various factors during training, including random seeds. It raises the question of how the authors determined that their revised learning rates and initializations would have the most significant impact on their observation of updated rankings. Specifically, it's unclear if the authors performed a rigorous sensitivity analysis with respect to random seed variations, and if the observed changes in ranking are statistically significant or simply due to random fluctuations. The paper should provide more details on how the observed ranking changes are not simply artifacts of the training process itself, especially given the known variability in training neural networks.

- It's recognized that NAS-Bench typically selects learning rates closer to those utilized by "good architectures" that are in practical use, reflecting an intentional bias towards favoring such architectures over "bad architectures." However, in Section 4.3, I could not discern evidence that the new learning rate/initialization approach improves upon the performance of the top-performing architectures, while it appears to only boost many of the "bad architectures." Given this, it raises the question of why this new learning rate/initialization strategy is relevant for practical NAS if it cannot enhance the performance of the best-found architectures. The paper should clarify if the proposed method is intended to improve the overall performance of all architectures, or specifically target the performance of previously underperforming architectures. If the latter, the implications for real-world NAS are less clear, as the goal is typically to discover the best architecture, not to make all architectures perform similarly.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
