# Discretized Quadratic Integrate-and-Fire Neuron Model for Direct Training of Spiking Neural Networks

- Decision: Reject
- Avg Score: 4.60
- Scores: 3, 5, 3, 6, 6

## Abstract
Spiking Neural Networks (SNNs) are a promising alternative to traditional artificial neural networks, offering significant energy-saving potential. Conventional SNN approaches typically utilize the Leaky Integrate-and-Fire (LIF) neuron model, where voltage decays linearly, decreasing proportionally to its current value. However, this linear decay can inadvertently increase energy consumption and reduce model performance due to extraneous spiking activity. To address these limitations, we introduce the discretized Quadratic Integrate-and-Fire (QIF) neuron model, which applies a non-linear transformation to the voltage proportional to its magnitude. The QIF neuron model achieves substantial energy reductions, ranging from $1.43 - 4.21\times$ compared to the LIF neuron model. On static datasets (CIFAR-10, CIFAR-100) and neuromorphic datasets (CIFAR-10 DVS, N-Caltech-101, N-Cars, DVS128-Gesture), the QIF neuron model demonstrates competitive performance and improved accuracy over state-of-the-art results. Furthermore, the QIF neuron model produces smoother loss landscapes and larger local minima, leading to faster training convergence. Our findings suggest that the QIF neuron model offers a promising alternative to the widely adopted LIF neuron model.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The author proposes a targeted neuron modeling approach to address existing issues in Spiking Neural Networks (SNNs). This approach reduces the energy consumption of Leaky Integrate-and-Fire (LIF) neurons to some extent and also facilitates faster model convergence. The author conducted validation experiments on both static and dynamic datasets and achieved successful results. This type of Quadratic Integrate-and-Fire (QIF) model could potentially become a widely applied neuron modeling paradigm.

### Strengths
1.  A new neuron modeling approach is proposed, along with an appropriate surrogate gradient window.
2.	The effectiveness of this method is demonstrated across multiple datasets.
3.	Evidence is provided that the QIF model can reduce energy consumption and facilitate model convergence.

### Weaknesses
1.	The generalizability of QIF has not been verified. QIF has only been tested on CNN-based models, and it remains unproven whether this model has good generalization to other types of SNNs. Specifically, the experiments focus on relatively shallow CNN architectures. It's unclear if the observed benefits of QIF would extend to more complex architectures, such as those with skip connections or attention mechanisms, which are common in modern SNNs. Furthermore, the datasets used, while diverse, are still primarily image-based. The performance of QIF on other types of sequential data or graph-structured data remains unexplored.
2.	Although visualizations suggest that QIF can guide models to converge quickly, this conclusion is derived post hoc. Is there any theoretical basis for this? The analysis lacks a rigorous mathematical explanation of why the QIF neuron's dynamics would lead to faster convergence. While the empirical results are promising, a theoretical framework that explains the observed behavior is needed. For example, an analysis of the loss landscape or the gradient flow during training could provide more insight into the convergence properties of the QIF model.

### Questions
see weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes replacing the traditional Leaky Integrate-and-Fire (LIF) neuron model with a Quadratic Integrate-and-Fire (QIF) neuron model in spiking neural networks (SNNs). The authors argue that QIF neurons retain more complex nonlinear dynamics that may better approximate biological neuron behavior. They introduce a custom surrogate gradient window to stabilize the training of QIF neurons and conduct experiments on multiple datasets to demonstrate potential advantages. However, the paper lacks extensive theoretical analysis and validation on larger datasets such as ImageNet and more complex network architectures (more deeper Spiking ResNet and Spiking Transformer). The experimental scope is limited, and there is minimal discussion on hardware implementation challenges, making the current contribution modest.

### Strengths
The paper makes a meaningful attempt to address the limitations of the traditional Leaky Integrate-and-Fire (LIF) neuron model by introducing the Quadratic Integrate-and-Fire (QIF) neuron model, which retains more complex nonlinear dynamics that may better approximate biological neurons. This choice is theoretically promising, as it could enhance the modeling capabilities of spiking neural networks (SNNs) by introducing more biologically realistic dynamics. Additionally, the paper introduces a surrogate gradient window tailored to QIF neurons, a practical contribution that improves training stability in spiking neural networks, and presents experimental results on multiple datasets showcasing QIF's potential benefits.

### Weaknesses
The paper lacks theoretical depth and sufficient experimental validation for QIF neurons in more complex scenarios. The primary contribution seems limited to replacing LIF neurons with QIF neurons and conducting experiments on small-scale datasets with simpler models. There is no comprehensive analysis of the impact of QIF-specific parameters (such as the resting potential and critical spiking threshold) on network performance or stability. Furthermore, the experiments are limited without testing on larger datasets like ImageNet or deeper, more complex architectures such as Transformers or deeper Spiking ResNet. These limitations make it challenging to assess the broader applicability and stability of QIF neurons in practical scenarios, and the hardware deployment considerations for QIF neurons are not adequately addressed. The paper also does not sufficiently address the novelty of the approach, given that the QIF neuron model is a well-established model in computational neuroscience. Simply incorporating this model into a spiking neural network, without substantial methodological innovation or theoretical justification, may not be a significant contribution. The paper needs to clarify how the specific implementation and training of QIF neurons in deep SNNs goes beyond a simple substitution of neuron models.

### Questions
1.	Could the authors provide a more comprehensive analysis of QIF-specific parameters, such as the resting potential, critical spiking threshold, and decay rate? How do these parameters affect stability and convergence in different scenarios?
2.	Are there any plans to extend the experiments to larger datasets, such as ImageNet, or to more complex network architectures like Spiking ResNet or Transformers? This would significantly strengthen the paper’s claims about the general applicability of QIF neurons.
3.	How does the QIF neuron model compare to LIF in terms of computational and energy efficiency, especially in the context of neuromorphic hardware? Since QIF introduces more complex dynamics, it might face practical limitations when deployed on resource-constrained hardware.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a discretized Quadratic Integrate-and-Fire (QIF) neuron model for SNNs to better preserve the complex non-linear dynamics of biological neurons compared to the LIF model. This enhanced model addresses issues like reduced performance and increased energy consumption caused by extraneous spiking activity in LIF-based SNNs.

### Strengths
1. Significance: The paper addresses the critical issue of energy consumption in neural networks by introducing a novel QIF neuron model. This focus on reducing energy usage is highly relevant and contributes meaningfully to the SNN community.

2. Clarity: The paper is well-written and easy to understand, with clear explanations of the QIF model’s formulation.

### Weaknesses
1. Limited Experimental Validation: The study primarily employs a single, outdated neural network architecture, lacking evaluations on more modern and diverse models such as Transformers. Additionally, experiments do not cover a range of model sizes, which restricts the assessment of the QIF model's generalizability and scalability. The absence of experiments on larger models, such as ResNet architectures with varying depths, makes it difficult to ascertain the model's performance characteristics across different scales of complexity.

2. Absence of Large-Scale Dataset: The paper does not include evaluations on the ImageNet dataset. This omission is significant as ImageNet is a standard benchmark for evaluating image classification models, and its absence limits the ability to compare the proposed QIF model with state-of-the-art methods under challenging conditions.

3. Increased Hyperparameter Complexity: Compared to the traditional LIF model, the QIF model introduces additional hyperparameters. Although parameter insensitivity is claimed, the supporting evidence relies heavily on simple architectures and datasets, which is not convincing. The lack of a thorough hyperparameter sensitivity analysis, particularly on more complex models and datasets, raises concerns about the practical applicability of the QIF model.

4. Marginal Performance Improvements: While the QIF model achieves significant energy reductions, its performance gains in terms of accuracy are not consistently superior to existing methods. This raises questions about whether the additional complexity and parameter overhead are justified by the modest performance enhancements. The paper does not adequately address the trade-offs between energy efficiency and accuracy, especially when the accuracy improvements are not substantial.

5. Lack of Neuromorphic Hardware Adaptability Discussion: The paper does not discuss the compatibility and adaptability of the QIF neuron model with neuromorphic hardware. This is a crucial oversight as the primary motivation for using SNNs is their potential for efficient implementation on neuromorphic platforms. The absence of such a discussion limits the practical relevance of the proposed model.

### Questions
1. Could you provide a more detailed sensitivity analysis of the additional parameters introduced in the QIF model?

2. Could you provide insights into the theoretical foundations that explain the improved energy efficiency?

3. What are the potential solutions for hardware deployment?

4. Please provide all the experiments I mentioned in the Weakness to demonstrate the effectiveness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a new spiking neuronal model to overcome the shortcomings of previous discretized neuron model. The method is widely validated on several datasets and compared with other methods.

### Strengths
1. The methods are validated on two image recognition datasets and several neuromorphic datasets, which make good contributions. Though ImageNet results are not presented, it can be understandable that surrogate gradient learning on such dataset is very expensive.

2. The loss landscape is visualized in the supplementary materials, which is very helpful for better understanding the method

### Weaknesses
The context and motivation are very unclear.

The paper mentions that a technique is used before it is first proposed. See questions for details. The author should explain this.



### Questions
1. Line 41 to Line 45. Could you explain what "discretization techniques" really mean? Also, it is confusing that TrueNorth used such a technique in 2015 but the paper said this technique was introduced in 2018. Could you explain in detail how this happens? 

2. Line 207 "Therefore, we introduce our discretized QIF neuron model". The current story is that the "discretization" of the current spiking neuron model is not good so you introduced a new one. However, the proposed neuronal model is still discretized. This makes the motivation of this paper not clear. Could you explain more about the motivation of your method?


--------------------------
Updates after rebuttal
The author responded to the two questions I raised and addressed them. Thus, I increase my score from 5 to 6.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents the discretized Quadratic Integrate-and-Fire (QIF) neuron model for training deep Spiking Neural Networks (SNNs). The QIF model is proposed as an alternative to the commonly used Leaky Integrate-and-Fire (LIF) neuron model, aiming to retain non-linear, biologically plausible dynamics after discretization. Through extensive evaluation, the paper demonstrates the QIF model's competitive performance on static datasets (CIFAR-10, CIFAR-100) and superior accuracy on several neuromorphic datasets (CIFAR-10 DVS, N-Caltech-101, N-Cars, DVS128-Gesture). Additionally, it shows that the QIF model improves energy efficiency by 20-123% compared to LIF neurons and offers faster convergence due to smoother loss landscapes and greater robustness to hyperparameter selection.

### Strengths
The introduction of a discretized QIF neuron model addresses a gap in the literature by capturing more complex, non-linear neuronal dynamics, potentially advancing SNNs closer to biological realism. The authors derive an equation to calculate surrogate gradient windows directly from QIF parameters, which minimizes issues with gradient mismatch and naive initialization. This analytical insight is a valuable addition to the SNN field. The model is extensively benchmarked on both static and neuromorphic datasets, demonstrating its generalizability and competitiveness with state-of-the-art methods. The focus on energy efficiency and robustness is particularly relevant for neuromorphic computing. The authors report significant energy efficiency improvements over LIF, along with smoother loss landscapes and faster convergence. This is crucial for the deployment of SNNs in real-world applications where power constraints are critical.

### Weaknesses
While the paper claims that the QIF model is more biologically plausible, it would benefit from a brief explanation of how the non-linear dynamics in QIF neurons more accurately reflect biological neurons, particularly compared to LIF. Specifically, the paper should elaborate on which aspects of biological neuron behavior are better captured by the quadratic relationship in the QIF model versus the linear integration of the LIF model. The reported 20-123% improvement in energy efficiency is broad, and it is unclear what factors influence this range. Clarifying whether architecture, dataset, or another factor contributes to this variation would improve interpretability. For instance, do deeper networks or datasets with higher temporal resolution show a more pronounced energy efficiency gain? The claim of greater robustness to hyperparameter selection is promising, yet the paper would be strengthened by including more detailed ablation studies to substantiate this claim. The current hyperparameter sweeps are limited to a single network architecture and dataset, and it's unclear if these findings generalize to more complex models or different data modalities. Furthermore, the paper should explore the sensitivity of the QIF model to specific hyperparameter choices, such as the reset potential or the time constant, and compare this to the LIF model.

### Questions
The paper could address potential trade-offs between QIF and LIF neuron models, such as computational cost or latency, as these may be factors in deciding the appropriateness of QIF for specific applications.

### Soundness
3

### Presentation
2

### Contribution
2
