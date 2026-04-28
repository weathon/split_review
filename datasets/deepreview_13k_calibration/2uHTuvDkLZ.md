# Physics-aware Causal Graph Network for Spatiotemporal Modeling

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
Interpretable physics equations are widely recognized as valuable inductive biases for constructing robust spatiotemporal models. To harness these valuable pieces of knowledge, existing approaches often presuppose access to the exact underlying equations. However, such an assumption usually doesn't hold, especially in the context of real-world observations. Conversely, causality systematically captures the fundamental causal relations across space and time that are intrinsically present in physics dynamics. Nevertheless, causality is often ignored as a means of integrating prior physics knowledge. In this work, we propose a novel approach that effectively captures and leverages causality to integrate physics equations into spatiotemporal models, without assuming access to precise physics principles. 
Specifically, we introduce a physics-aware spatiotemporal causal graph network (P-stCGN). Causal relationships are analytically derived from prior physics knowledge and serve as physics-aware causality labels. A causal module is introduced to learn causal weights from spatially close and temporally past observations to current observations via semi-supervised learning. Given the learned causal structure, a forecasting module is introduced to perform predictions guided by the cause-effect relations. Extensive experiments on time series data show that our semi-supervised causal learning approach is robust with noisy and limited data. Furthermore, our evaluations on real-world graph signals demonstrate superior forecasting performance, achieved by utilizing prior physics knowledge from a causal perspective.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper aims to integrate a spatio-temporal graph neural network with physics-aware causality for spatio-temporal modeling. The major contribution is the soft integration of physics equations with causality. Experiments over several synthetic and real-world datasets can verify the effectiveness of the proposed model.

### Strengths
1. The paper is well-written and easy to follow. Integrating spatio-temporal graph neural network is of great importance to many real-world applications.
2. The paper conducts experiments over both synthetic and real-world datasets.

### Weaknesses
My major concerns are:
1. Insufficient related work. To the best of my knowledge, there is quite a large number of literature exploring the integration of physics law or causality into spatio-temporal graph neural networks [1,2,3,4,5,6]. For example, [1,2,6] employ neural ordinary differential equations to capture continuous ST dependencies. Ji et al. propose a physics-guided neural network for spatiotemporal modeling in traffic flows [3]. CaST designs a new framework for handling causality in spatio-temporal graphs [4]. However, this paper lacks a discussion on these studies and doesn't compare the proposed model with them either. What's the difference between them? Why should we use the proposed model? It would be good to survey more related publications before paper submission. What's more, the related work section should be included in the main body of the paper, instead of the appendix.
2. The technical contribution of this work against existing approaches is not significant, which is clearly below the acceptance level of ICLR.
3. The term "causality" in this paper is questionable. This causality is more similar to proximity in other spatio-temporal graph neural networks [7, 8], rather than the actual causality in causal inference. 
4. The learned causality in this paper lacks justification.
5. The baselines used in this paper are weak and outdated. Please consider more recent baselines for comparison (see the above references). 
6. This paper lacks the experiment over one of the most popular tasks -- traffic forecasting, which is also driven by inherent physics laws.
7. No source code for reproducing the results.
8. No discussion on the model efficiency and model size.

### Questions
Please reply to the questions in the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel approach called Physics-Aware Spatiotemporal Causal Graph Network (P-STCGN) for integrating physical equations into spatiotemporal models. The idea is to leverage causality to capture the fundamental causal relations present in physics dynamics. The proposed approach uses a causal module to learn causal weights from past observations to current observations and a forecasting module to perform predictions guided by cause-effect relations. Evaluations conducted on synthetic as well as real-world climate datasets demonstrate the superior performance for the proposed method.

### Strengths
1. The Integration of Physics Knowledge is quite innovative.
2. The paper provides an extensive evaluation of the proposed method on different datasets.

### Weaknesses
Weaknesses/questions
1.	How does the model perform when the prior physics knowledge is ambiguous or not well established? How to verify the accuracy of the physics knowledge being integrated?
2.	Can the authors elaborate on why the model is able to handle the noisy data?
3.	Besides the climate-related application, how easy it is to extend the model to other domains?

### Questions
See weaknesses above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the Physics-aware Spatiotemporal Causal Graph Network (P-STCGN), a approach that softly integrates the laws of physics into causal graph structures. This integration aims to enhance the robustness of spatiotemporal models by leveraging valuable inductive biases from interpretable physics equations. The primary challenges addressed involve the mismatch between the assumptions of existing models and real-world observations. The P-STCGN model capitalizes on the inherent causal relationships present in physical dynamics across both space and time.

### Strengths
(1) The authors' consideration of introducing causality into model construction is quite intriguing. Moreover, this approach contributes significantly to the model's interpretability. 

(2) The authors adeptly address the potential challenges of capturing real-world physical laws, showcasing a strong foundation in practical scenarios.

### Weaknesses
(1)	The coherence between the introduction and the main content of the paper is somewhat lacking. The introduction mentions the existence of various physical laws in the real world. However, in the model and specific dataset experiments, these physical laws were not introduced as prior knowledge in a way that is clearly defined or tested. Specifically, the paper does not explicitly state how the PDEs are incorporated into the model architecture. It remains unclear whether the causal relationships are derived from the PDEs or if the PDEs are merely used to define the causal labels. This ambiguity makes it difficult to assess the true impact of physics-awareness in the proposed model. Furthermore, the introduction suggests the possibility of discovering partial physical laws from real-world data, yet no experiments are conducted to validate this claim, creating a disconnect between the stated goals and the experimental validation.

(2) The paper emphasizes modeling using causal theory. However, learning causal correlations through an MLP (Multi-layer Perceptron) seems somewhat inappropriate. The use of an MLP, a black-box model, to determine causal relationships undermines the interpretability that the authors claim to achieve. While attention mechanisms can provide some insight into correlation, the core causal structure is still determined by the MLP, which lacks a clear logical foundation. The paper needs to justify why an MLP is suitable for capturing causal relationships, especially when the goal is to integrate physics-based causal structures.

### Questions
(1) The authors should consider comparing their approach with some state-of-the-art spatio-temporal GNN frameworks in the experiments. This would provide a clearer context for the performance and relevance of the proposed method. 

(2) The integration of causal relationships with real-world equations should be further elucidated in the model description. It would be beneficial for readers to have a comprehensive understanding of how these components interact within the proposed framework.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an approach for spatiotemporal modeling using physics-aware causality. The approach integrates domain knowledge with data-driven models to construct more robust and interpretable pipelines. The model learns causal weights from spatially close and temporally past observations to current observations via semi-supervised learning, allowing it to capture the underlying cause-effect relationships in the data. The approach employs a regularization term to capture the causal structures that align with the physics-aware causality, further improving the model's performance. The model's ability to handle noisy and limited data is demonstrated by extensive experiments on time series data, and its superior forecasting performance on real-world graph signals highlights its effectiveness in capturing the underlying physics principles governing spatiotemporal observations. Overall, the proposed approach is a promising direction forward in the field of machine learning, with potential applications in climate, traffic systems, and electricity networks.

### Strengths
1. The manuscript is clearly written, with a well-defined motivation. Incorporating causality into spatio-temporal data mining presents an intriguing perspective.

2. The experiments conducted are reasonable, validating the model's capabilities across multiple scenarios.

### Weaknesses
1. In real-world scenarios, a plethora of spatio-temporal graph data, often comes with inherent noise from various sources. Typically, methods based on physical principles might not perform well in real-world settings and can exhibit weak generalization capabilities. I would like to see the authors conduct tests on real-world graph data to better demonstrate the generalization ability of their model.

2. The authors should consider testing their approach on more challenging datasets, such as the n-body system, to further validate its effectiveness.

3. While the paper emphasizes causal theory, I did not observe explicit references or applications of foundational causal concepts, such as backdoor adjustment or front door adjustment. I encourage the authors to elucidate the underlying causal motivations and proofs in greater detail. This would significantly strengthen the paper's results and its overall contributions.

### Questions
see weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
