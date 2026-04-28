# GOLD: Graph Out-of-Distribution Detection via Implicit Adversarial Latent Generation

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
Despite graph neural networks' (GNNs) great success in modelling graph-structured data, out-of-distribution (OOD) test instances still pose a great challenge for current GNNs. One of the most effective techniques to detect OOD nodes is to expose the detector model with an additional OOD node-set, yet the extra OOD instances are often difficult to obtain in practice. Recent methods for image data address this problem using OOD data synthesis, typically relying on pre-trained generative models like Stable Diffusion. However, these approaches require vast amounts of additional data, as well as one-for-all pre-trained generative models, which are not available for graph data. Therefore, we propose the GOLD framework for graph OOD detection, an implicit adversarial learning pipeline with synthetic OOD exposure without pre-trained models. The implicit adversarial training process employs a novel alternating optimisation framework by training: (1) a latent generative model to regularly imitate the in-distribution (ID) embeddings from an evolving GNN, and (2) a GNN encoder and an OOD detector to accurately classify ID data while increasing the energy divergence between the ID embeddings and the generative model's synthetic embeddings. This novel approach implicitly transforms the synthetic embeddings into pseudo-OOD instances relative to the ID data, effectively simulating exposure to OOD scenarios without auxiliary data. Extensive OOD detection experiments are conducted on five benchmark graph datasets, verifying the superior performance of GOLD without using real OOD data compared with the state-of-the-art OOD exposure and non-exposure baselines. The code will be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a framework designed to detect out-of-distribution data without requiring pre-existing OOD datasets or pre-trained models. The proposed GOLD framework includes:
- A latent generative model to generate synthetic embeddings that imitate in-distribution embeddings from a GNN.
- A GNN encoder and OOD detector to classify in-distribution data and maximize energy divergence between in-distribution and synthetic embeddings.

### Strengths
- *No OOD Data Required*: Synthesizes pseudo-OOD data through adversarial training, alleviating the need for real OOD samples.
- *Implementation Flexibility*: Supports both LDM and VAE variants, offering trade-offs between performance and computational efficiency.
- *Strong Empirical Performance*: Outperforms non-OOD methods and matches/exceeds methods using real OOD data.

### Weaknesses
 - Using generative models to generate samples for downstream tasks has been widely adopted in previous methods. For example, generated samples are commonly used in continual learning for experience replay. It seems that the use of generators in GOLD applies the same concept to different tasks. Energy-based detection is also widely used. The major contribution seems to lie in a new divergence regularisation (Eq.12).
- Further ablative studies on divergence regularisations may be needed to better reflect their effectiveness.
- The presentation needs to be improved.

### Questions
- Could the author better clarify the key novelty of GOLD compared to existing works? What distinguishes the usage of the generator in GOLD from previous works?
- The training procedure has two stages: one stage involves fixing the GNN and training the LGM, and the second stage involves fixing the LGM and training the GNN. Is it possible to combine these two stages using a gradient reversal layer?
- Further ablative studies on  $L_{DReg}, L_{Unc}, L_{EReg}$  (removing each of them or applying each individually) may help to better demonstrate the effectiveness of the proposed new divergence regularization (Eq. 12).
- What modifications would be needed to extend the framework beyond node-level detection, such as to graph-level OOD detection tasks?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a new framework called GOLD, which aims to address the challenges faced by graph neural networks (GNNs) when dealing with out-of-distribution (OOD) test instances. The GOLD framework detects OOD nodes in graph data through an implicit adversarial learning process without relying on pre-trained models. The core of the framework is the alternating optimization framework.

### Strengths
1. The paper presents a method with notable novelty, particularly in how it handles the generation of OOD (Out-of-Distribution) samples based on ID (In-Distribution) data. This approach demonstrates creative problem-solving and provides a potentially valuable contribution to OOD detection research.
2. The experimental section is comprehensive, covering multiple datasets and providing a range of performance metrics. This thorough evaluation supports the robustness of the method and suggests that it may perform effectively across diverse scenarios.

### Weaknesses
1. Certain issues in the manuscript reduce its overall clarity and precision. For example, Figure 1(d) appears to be blank, which may hinder understanding and interpretation of the paper’s content.


### Questions
1. Regarding the generation process of pseudo-OOD samples based on ID data, if these generated samples are overly close to the ID distribution, it could lead to confusion in the OOD detector, potentially causing ID samples to be misclassified as pseudo-OOD. Could the authors elaborate on whether any specific techniques were applied during training to control this distributional proximity?
2. Additionally, I noticed that the model exhibits substantial variance in the FPR95 metric on the Amazon and Coauthor datasets. Could the authors clarify whether this variance is linked to the aforementioned distributional control during the generation process?

### Soundness
3

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
The paper presents GOLD, a novel framework aimed at enhancing Out-of-Distribution (OOD) detection in graph neural networks (GNNs) without relying on external OOD data. GOLD introduces an implicit adversarial training pipeline where a latent generative model (LGM) is trained to generate embeddings that mimic in-distribution (ID) data, while an OOD detector is optimized to increase divergence between ID embeddings and these synthetic pseudo-OOD embeddings. It effectively simulates OOD exposure, helping the model distinguish OOD nodes in graph data. Extensive experiments demonstrate that GOLD outperforms state-of-the-art methods in OOD detection across several benchmark datasets without the need for real OOD data.

### Strengths
- GOLD’s adversarial latent generation is a novel approach that synthesizes pseudo-OOD data without auxiliary datasets, making it efficient and broadly applicable.

- GOLD’s effectiveness is demonstrated through comprehensive experiments on five benchmark datasets, showing its robustness across various graph types and OOD scenarios.

-  The implicit adversarial objective and energy-based detection approach lead to a clear divergence between ID and OOD embeddings, validated by experimental visualizations.

- This paper is well-structured.

### Weaknesses
This paper has no obvious weaknesses except for the training computational cost induced by the pseudo-OOD data. However, this cost increase is acceptable. And the authors have also discusses this issue in POTENTIAL LIMITATIONS section.

### Questions
1. What does subscript (i.e., [0], [1]) in Eq(10) mean?

2. Have the authors tried other backbone models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes the GOLD, a novel framework for graph OOD detection that employs implicit adversarial learning to generate synthetic OOD instances without the need for pre-trained models or additional OOD data. By utilizing a latent generative model to produce embeddings mimicking in-distribution data, which are then differentiated from actual in-distribution embeddings by a graph neural network encoder and an OOD detector, the method is able to effectively simulate the OOD exposure. The framework is evaluated on five benchmark graph datasets, demonstrating superior OOD detection performance without using real OOD data compared with the state-of-the-art OOD exposure and non-exposure baselines.

### Strengths
1. The idea of implicit adversarial learning is novel.
2. The experiments are solid and comprehensive, especially the improvements achieved on the FPR95 dataset is impressive.
3. The paper is easy to follow and well-structured. The writing is good. The theoritical proofs are provided.

### Weaknesses
I didn't see obvious weaknesses. Here I provide some suggestions:

Could you provide a more in-depth analysis of the performance achievements on the FPR95 dataset, including an analysis from the perspective of the dataset's characteristics? Additionally, could you explain why similar significant improvements were not observed on other datasets (although the improvements on other datasets are also quite good)?

### Questions
See weakness.

### Soundness
4

### Presentation
4

### Contribution
4
