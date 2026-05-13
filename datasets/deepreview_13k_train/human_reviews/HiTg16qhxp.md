# Dynamic Neural Response Tuning

- Decision: Accept
- Scores: 5, 8, 3, 6

## Abstract
Artificial Neural Networks (ANNs) have gained widespread applications across various areas in recent years. The ANN design was initially inspired by principles of biology. The biological neural network's fundamental response process comprises information transmission and aggregation. The information transmission in biological neurons is often achieved by triggering action potentials that propagate through axons. ANNs utilize activation mechanisms to simulate such biological behavior. However, previous studies have only considered static response conditions, while the biological neuron's response conditions are typically dynamic, depending on multiple factors such as neuronal properties and the real-time environment. Therefore, the dynamic response conditions of biological neurons could help improve the static ones of existing activations in ANNs. Additionally, the biological neuron's aggregated response exhibits high specificity for different categories, allowing the nervous system to differentiate and identify objects. Inspired by these biological patterns, we propose a novel Dynamic Neural Response Tuning (DNRT) mechanism, which aligns the response patterns of ANNs with those of biological neurons. DNRT comprises Response-Adaptive Activation (RAA) and Aggregated Response Regularization (ARR), mimicking the biological neuron's information transmission and aggregation behaviors. RAA dynamically adjusts the response condition based on the characteristics and strength of the input signal. ARR is devised to enhance the network's ability to learn category specificity by imposing constraints on the network's response distribution. Extensive experimental studies indicate that the proposed DNRT is highly interpretable, applicable to various mainstream network architectures, and can achieve remarkable performance compared with existing neural response mechanisms in multiple tasks and domains. Code is available at https://github.com/horrible-dong/DNRT.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors developed a Dynamic Neural Response Tuning (DNRT) mechanism inspired by the dynamic response conditions of biological neurons, addressing the limitations of static response conditions in existing activation functions. DNRT consists of Response-Adaptive Activation (RAA) and Aggregated Response Regularization (ARR), which mimic biological neurons' information transmission and aggregation behaviors, respectively. RAA adjusts the response condition based on input signal strength and characteristics, while ARR enhances the network's ability to learn category specificity. Experiments show that DNRT is interpretable, compatible with various network architectures, and outperforms existing activation functions in multiple tasks and domains.

### Strengths
The authors developed a Dynamic Neural Response Tuning (DNRT) mechanism inspired by the dynamic response conditions of biological neurons, addressing the limitations of static response conditions in existing activation functions. DNRT consists of Response-Adaptive Activation (RAA) and Aggregated Response Regularization (ARR), which mimic biological neurons' information transmission and aggregation behaviors, respectively. RAA adjusts the response condition based on input signal strength and characteristics, while ARR enhances the network's ability to learn category specificity. Experiments show that DNRT is interpretable, compatible with various network architectures, and outperforms existing activation functions in multiple tasks and domains.

### Weaknesses
1. The author have established a series of baseline experiments; however, the performance demonstrated in these experiments appears to be inferior to the results reported in previous literature.

2. RAA method introduces an additional parameter, W, which may compromise the fairness of comparisons with other activation functions.

3. The authors did not state clearly of the significance of the study. What is the inspiration of this study for neuroscience, or for the development of deep learning?

### Questions
1. In the presented experiments, it is crucial to disclose the number of parameters employed for each model. To ensure a fair comparison, the parameters for the baseline models must be comparable. Please provide this information in a clear and concise manner.

2. It is imperative that the chosen baseline models are well-established and representative of the current state of the art in deep learning. Notably, state-of-the-art deep learning methods have demonstrated the ability to achieve accuracy levels exceeding 85% on the ImageNet dataset. Please confirm that the selected baselines adhere to this standard.

3. Apart from the aspect of biological plausibility, it is essential to elucidate the motivations behind the development of RAA and AAR for the deep learning community. Please provide a comprehensive explanation of the underlying inspirations.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper delves into the realm of Artificial Neural Networks and their foundational principles inspired by biological neural systems. A focal point is the discernible distinction between the static response conditions in traditional ANNs and the inherently dynamic nature of biological neurons. Recognizing this disparity, the authors propose the Dynamic Neural Response Tuning (DNRT) mechanism.

DNRT is a two-pronged approach comprising:

1. Response-Adaptive Activation (RAA): A novel activation function that dynamically modulates its response based on the characteristics and magnitude of the incoming signal. Unlike traditional activation functions, which maintain a static response, RAA adapts, mirroring the dynamic response conditions observed in biological neurons.

2. Aggregated Response Regularization (ARR): A mechanism designed to refine the aggregation of signals in the network. ARR aims to enhance the network's proficiency in discerning and classifying distinct categories, thereby boosting performance.

To validate the effectiveness of DNRT, the authors embarked on an extensive experimental evaluation across diverse architectures, including basic MLPs, ViTs and CNNs, Their findings suggest that DNRT not only integrates seamlessly across these architectures but also often outperforms traditional activation functions in terms of performance.

### Strengths
The paper introduces the DNRT mechanism, a fresh perspective in the realm of neural network activation functions. While traditional activation functions have been studied extensively, the idea of aligning ANNs with the dynamic response patterns of biological neurons offers a distinct and innovative approach. The two-pronged design of DNRT, with Response-Adaptive Activation (RAA) and Aggregated Response Regularization (ARR), presents a unique combination of ideas, each addressing specific challenges in neural network design. The inspiration drawn from the dynamic nature of biological neurons and the attempt to emulate that in ANNs is a commendable original endeavor.

The paper showcases a meticulous and rigorous experimental evaluation across various architectures, solidifying its claims about the efficacy of DNRT. The ablation studies provide deeper insights into the individual and combined contributions of the components of DNRT, enhancing the paper's technical quality. 

The paper is well-structured, with a clear flow from motivation to proposal, followed by experimental validation. Concepts like RAA and ARR are explained with precision, allowing readers to grasp the core ideas effectively. While there's room for more intuitive visualizations, the current presentation ensures that readers familiar with the domain can understand the proposed mechanism and its implications.

Addressing the static nature of traditional activation functions and attempting to bridge the gap with the dynamic responses of biological neurons holds significant implications for the field of neural networks.
If DNRT can be consistently shown to enhance performance across various architectures, as suggested by the paper's results, it can lead to a paradigm shift in how activation functions are designed and implemented.

### Weaknesses
While the paper draws inspiration from the dynamic nature of biological neurons, a deeper exploration into the biological underpinnings could have been beneficial. More direct parallels between the DNRT mechanism and real-world neural behaviors would strengthen the paper's foundational claims. Consider integrating more biological studies or references that showcase the parallels between DNRT and actual biological neural behaviors, reinforcing the biological accuracy of the proposed mechanism.

The paper provides comprehensive experimental evaluations, but a detailed discussion on potential limitations or scenarios where DNRT might not be as effective is missing. Understanding these limitations can provide a more balanced view and guide future work. Dedicate a section to discuss potential limitations, challenges in broader applicability, or scenarios where traditional activation functions might still be preferable.

While the paper does address prior work in the domain, a more detailed comparison or discussion regarding how DNRT builds upon or differs from existing methods would offer readers a clearer perspective on its novelty. The related work section could be expanded to include more direct comparisons with existing activation functions or mechanisms, highlighting the unique contributions of DNRT.

The paper mentions the adaptability of RAA and hints at additional parameters, but a clear breakdown of how DNRT introduces and manages these parameters, especially in comparison to traditional activation functions, is lacking. Provide a subsection detailing the parameterization of RAA, including how these parameters are learned, their impact on network complexity, and potential challenges in optimization.

### Questions
Could the authors elaborate on the specific biological studies or evidence that influenced the design of DNRT? How closely does DNRT emulate the dynamic behaviors observed in biological neurons?

Are there specific architectures, tasks, or datasets where DNRT might not provide significant benefits or might even be counterproductive? What are the potential challenges or drawbacks associated with DNRT?

How are the parameters in the Response-Adaptive Activation (RAA) introduced and managed? How do these parameters impact network complexity, and are there challenges in optimizing these parameters during training?

Beyond the experimental setups, how does DNRT fare in real-world applications or larger, more complex datasets? Are there scalability concerns or other practical challenges?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method using novel activation functions which allows neurons in an ANN to provide outputs that cluster around particular classes more closely, by analogy with some observed behaviors of biological neurons.

### Strengths
The program idea, to make individual neurons in an ANN responsive to context or input distribution or similar is a good one.

### Weaknesses
The text is somewhat confusing to me. Examples: 1. It does not clearly distinguish between ANNs and biological NNs (BNNs), which confuses the exposition; 2. The method is not (for me) explained clearly enough, so I did not come away with a clear sense of what it entailed.

I suspect that the literature grounding is incomplete (I'm not expert).

Reviewer limitation: I had trouble understanding this paper, the mechanics of the method, and why it would be beneficial. So perhaps I am not an optimal reviewer. Or perhaps this reflects the need for some degree of rewriting.

Notes to ICLR: 

1. Please include line numbers in the template. They make reviewing much easier! 

2. Please reformat the default bibliography style to make searching the bib easier! eg numbered, last name first, initials only except for last name.


Abstract: 

Is this first sentence an accurate summary of why ANNs have done so well? It seems there is much more to the matter.

"is achieved by triggering action potentials": Often. Neurotransmitters and non-spiking neurons can also have prominent roles.

"depending on neuron properties and": There is a broad literature on neurotransmitters and how they modulate neural behavior.

"dynamically adjusts": my sense from the paper is that the activation function is modified to weight inputs differently, but once trained the response does not change dynamically, ie its response properties are fixed. If this is correct, "dynamically" is not a correct word.

"ARR is devide": Maybe give some brief detail about this, to parallel the detail given about RAA is the sentence above.

1. Paragraph 1: Perhaps find more comprehensive reviews for ANN progress (eg Goodfellow, etc).

1. paragraph 3 "otherwise it suppresses": This is true for ReLU, but not for other activation functions eg tanh. Also, this would be a good place to cite some good literature reviews of flavors of activation functions.

"An input value ranked later among all inputs": Does this refer to time-dependent neural response? I did not see this addressed as a technique or effect in the paper. 

"always adheres to a gaussian curve": Always? This framing is too simple. Also in this paragraph: the distinction between when referring to ANNs or BNNs is unclear. 

"It is a a common ... final decision.": This strikes me as vague. Can the sentence be sharpened?

2.1 "surpasses the threshold": For spiking neurons (see above comment about non-spiking types and local spread of neurotransmitters).

2.2 "pivotal role in neural networks": Does this refer to ANN, BNN, or both?

Bottom of page 3, "Biological NNs...": This is an important observation. However, does the proposed method really emulate this, or does it modify the activation function to a new, static, form?

3.1, last sentence: While BNNs feature dynamically changing activation functions, does the proposed method do this (same as previous comment)? Perhaps this is really a statement about my lack of understanding of the proposed method.

3.2, first sentence: I believe this is too simple a description.

### Questions
Bibliography: Perhaps reformat the bibliography for easier searching, eg numbered, last name first, initials only except for last name.

Abstract: 

Is this first sentence an accurate summary of why ANNs have done so well? It seems there is much more to the matter.

"is achieved by triggering action potentials": Often. Neurotransmitters and non-spiking neurons can also have prominent roles.

"depending on neuron properties and": There is a broad literature on neurotransmitters and how they modulate neural behavior.

"dynamically adjusts": my sense from the paper is that the activation function is modified to weight inputs differently, but once trained the response does not change dynamically, ie its response properties are fixed. If this is correct, "dynamically" is not a correct word.

"ARR is devide": Maybe give some brief detail about this, to parallel the detail given about RAA is the sentence above.

1. Paragraph 1: Perhaps find more comprehensive reviews for ANN progress (eg Goodfellow, etc).

1. paragraph 3 "otherwise it suppresses": This is true for ReLU, but not for other activation functions eg tanh. Also, this would be a good place to cite some good literature reviews of flavors of activation functions.

"An input value ranked later among all inputs": Does this refer to time-dependent neural response? I did not see this addressed as a technique or effect in the paper. 

"always adheres to a gaussian curve": Always? This framing is too simple. Also in this paragraph: the distinction between when referring to ANNs or BNNs is unclear. 

"It is a a common ... final decision.": This strikes me as vague. Can the sentence be sharpened?

2.1 "surpasses the threshold": For spiking neurons (see above comment about non-spiking types and local spread of neurotransmitters).

2.2 "pivotal role in neural networks": Does this refer to ANN, BNN, or both?

Bottom of page 3, "Biological NNs...": This is an important observation. However, does the proposed method really emulate this, or does it modify the activation function to a new, static, form?

3.1, last sentence: While BNNs feature dynamically changing activation functions, does the proposed method do this (same as previous comment)? Perhaps this is really a statement about my lack of understanding of the proposed method.

3.2, first sentence: I believe this is too simple a description.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors' rebuttal have essentially addressed my concerns, so I have raised the score of the paper to a weak accept.

=========================================================================================

This paper proposes a novel Dynamic Neural Response Tuning (DNRT) mechanism inspired by the dynamic response conditions of biological neurons. The DNRT mechanism comprises Response-Adaptive Activation (RAA) and Aggregated Response Regularization (ARR), which mimic the information transmission and aggregation behaviors of biological neurons. The authors demonstrate that the proposed DNRT can be applied to various mainstream network architectures and can achieve remarkable performance compared with existing response activation functions in multiple tasks and domains. The paper contributes to the simulation of dynamic biological neural response patterns and provides new concepts and techniques for constructing Artificial Neural Networks (ANNs).

### Strengths
Originality: The paper presents an innovative approach to mimicking the dynamic response conditions of biological neurons in ANNs, which is a significant departure from existing static activation functions.

Quality: The proposed DNRT mechanism is well-motivated and grounded in neuroscience research. The Response-Adaptive Activation (RAA) and Aggregated Response Regularization (ARR) components are clearly explained and justified.

Clarity: The paper is well-written and organized, with clear explanations of the DNRT mechanism, its components, and the motivation behind it. The figures and tables help illustrate the concepts and results effectively.

Significance: The DNRT mechanism has the potential to improve the performance of ANNs in various tasks and domains, as demonstrated by the extensive experiments conducted by the authors. The paper also provides valuable insights into neural information processing research.

### Weaknesses
Limited comparison with existing methods: While the paper demonstrates the performance of DNRT compared to existing activation functions, it would be helpful to see a more in-depth analysis and discussion of the differences between DNRT and other approaches, including spiking neural networks (SNNs). SNNs are based on neural dynamics and employ dynamic activation functions, which share similarities with the ideas presented in this paper. Specifically, the paper lacks a detailed comparison of the computational overhead and performance trade-offs between DNRT and SNNs, particularly in scenarios where temporal dynamics are crucial. A more thorough analysis should include a discussion of the specific advantages and disadvantages of each approach in terms of implementation complexity, training stability, and sensitivity to hyperparameter tuning.

Lack of generalization analysis: The paper claims that DNRT is applicable to various mainstream network architectures, but it would be beneficial to provide a more detailed analysis of how the proposed method generalizes to other tasks and domains beyond those presented in the experiments. The current analysis lacks a rigorous examination of the method's performance on tasks with different data modalities or complexities, such as natural language processing or time-series analysis. It would be valuable to see a discussion of the potential limitations of DNRT when applied to tasks with significantly different characteristics than those used in the current experiments, including an analysis of how the hyperparameter settings might need to be adjusted for optimal performance in these new contexts.

Potential implementation challenges: The paper does not discuss the possible challenges in implementing the proposed DNRT mechanism in real-world applications or the computational cost associated with its use. The practical considerations of deploying DNRT in resource-constrained environments, such as embedded systems or mobile devices, are not addressed. This includes a lack of discussion on memory footprint, energy consumption, and the potential for hardware acceleration. A thorough analysis should also consider the potential impact of DNRT on the overall training time and inference latency of the model, especially in comparison to simpler activation functions like ReLU.

### Questions
Can the authors provide more in-depth comparisons between the proposed DNRT mechanism and existing activation functions, discussing the advantages and disadvantages of each approach? Additionally, please include a comparison with spiking neural networks, as they also employ dynamic activation functions.

How does the DNRT mechanism generalize to other tasks and domains beyond those presented in the experiments? Are there any limitations or challenges in applying DNRT to different network architectures?

What are the potential implementation challenges and computational costs associated with using the DNRT mechanism in real-world applications? Are there any strategies to mitigate these challenges?

Considering the mainstream view that "computation is all you need," it is important to evaluate the additional computational costs and bandwidth bottlenecks introduced by DNRT. This is a concern as activation functions like Softplus and ELU are not widely used due to their lower computational efficiency compared to ReLU. Additionally, there are ongoing discussions about replacing the softmax layer in transformers with ReLU for improved computational efficiency. Could the authors provide an assessment of the impact of DNRT on model inference speed when replacing ReLU?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
