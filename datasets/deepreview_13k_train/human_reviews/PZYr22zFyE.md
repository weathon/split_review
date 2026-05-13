# Connectome Mapping: Shape-Memory Network via Interpretation of Contextual Semantic Information

- Decision: Accept
- Scores: 5, 6, 8, 6

## Abstract
Contextual semantic information plays a pivotal role in the brain's visual interpretation of the surrounding environment. When processing visual information, electrical signals within synapses facilitate the dynamic activation and deactivation of synaptic connections, guided by the contextual semantic information associated with different objects. In the realm of Artificial Intelligence (AI), neural networks have emerged as powerful tools to emulate complex signaling systems, enabling tasks such as classification and segmentation by understanding visual information. However, conventional neural networks have limitations in simulating the conditional activation and deactivation of synapses, collectively known as the connectome, a comprehensive map of neural connections in the brain. Additionally, the pixel-wise inference mechanism of conventional neural networks failed to account for the explicit utilization of contextual semantic information in the prediction process. To overcome these limitations, we developed a novel neural network, dubbed the Shape Memory Network (SMN), which excels in two key areas: (1) faithfully emulating the intricate mechanism of the brain's connectome, and (2) explicitly incorporating contextual semantic information during the inference process. The SMN memorizes the structure suitable for contextual semantic information and leverages this structure at the inference phase. The structural transformation emulates the conditional activation and deactivation of synaptic connections within the connectome. Rigorous experimentation carried out across a range of semantic segmentation benchmarks demonstrated the outstanding performance of the SMN, highlighting its superiority and effectiveness. Furthermore, our pioneering network on connectome emulation reveals the immense potential of the SMN for next-generation neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper is about improving semantic segmentation by remembering past semantic context of the dataset used in training to enable live adjustment during inference influenced by the semantic context. In simple terms, suppose the training data for semantic segmentation of 3 object categories (A,B,C) reveals that Object A has a density of 0.3, B a density of 0.6, and C a density of 0.1 meaning the predictions for B should occupy nearly 60% of the image. This kind of semantic context can be estimated by a density map derived during training and used to influence the adjustment of parameters during inference in a self-supervised fashion. 


The rest of the wrapping and tie-in to neuroscience and brain Connectome is weak at best and add no further value to the paper.

### Strengths
The strength of the paper is in using a  methodology of adaptation during inference using learned semantic context beyond the learned parameters of the semantic segmentation network during training.  This has both advantages of achieving better domain generalization and self-supervision. 

If this method could be generalized for arbitrary semantic context, it can become interesting since the density map is only one of the cues that could be used for incorporating semantic context. How are others handled, for example, the typical color of an object, the average shape of an object etc.

### Weaknesses
The paper makes weak references to the Connectome and signaling mechanisms which detract from understanding the main idea. 
If the order of description in some of the sections had changed, it would be an easier read. For example, giving a simple example of what is the information they hope to capture in the density map, and the entropy map early on would make easy ready. It wasn't until line 281-283 that we start following along. The insertion of propositions and definitions is also a distraction until the method has been clearly explained.

### Questions
It seems to be the datasets have been carefully chosen to illustrate the method. How well does this method work for benchmark datasets.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the Shape Memory Network (SMN), a deep learning architecture designed to improve semantic segmentation by incorporating contextual semantic information. The SMN emulates the brain's connectome by adapting its structure based on the context of the visual data, specifically in tasks where objects' shapes and densities vary significantly. Through a novel "conditional neuron" mechanism, the SMN selectively activates connections in response to semantic cues, allowing it to dynamically adjust its architecture at test time. The authors validate SMN's performance across various segmentation benchmarks, showing that it achieves higher accuracy than several state-of-the-art models, particularly in scenarios involving complex object boundaries or high-density variations.

### Strengths
An innovative method for adaptive neural architectures, grounded in the idea of selective neuron activation inspired by the brain’s connectome.

The results across multiple benchmark datasets seem robust, highlighting SMN’s ability to outperform conventional segmentation models in handling complex object boundaries and densities.

The ability to dynamically adjust network structure during test time is a notable contribution, with potential implications for real-time applications where adaptability to context is beneficial.

### Weaknesses
The evaluation is confined to segmentation tasks, and while the biological inspiration is intriguing, its broader application to different tasks is not yet explored. Have authors tried testing on any other task?

The SMN’s "conditional neuron" mechanism is innovative but requires clearer exposition; some of the explanations are complex, making it challenging for readers to understand the "exact" workings of the adaptive architecture.

The SMN's test-time adaptation seems to demand substantial computational resources, which may limit its practicality in real-time or resource-constrained applications.

### Questions
Could the authors explain the SMN’s adaptability in tasks beyond segmentation to determine its generalization?

Are there specific strategies to reduce the computational demands of the SMN’s test-time adaptation for real-world deployment?

How does the SMN perform under scenarios with limited semantic information, and does this impact its segmentation accuracy?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Motivation:
<1>Conventional neural networks have limitations in simulating the connectome.
<2>The inference mechanism of conventional neural networks failed to account for the explicit utilization of contextual semantic information in the prediction process.
To overcome these limitations, this paper developed the Shape Memory Network (SMN) with two benefits: <1> emulating the intricate mechanism of the brain’s connectome, and <2> incorporating contextual semantic information during the inference process.

Method:
SMN consists of three key components:
<1>Segmentation Pipeline: Responsible for generating semantic segmentation maps.
<2>Density Regression Pipeline: Predicts the density of target objects, i.e., the proportion of the image area occupied by the target objects.
<3>Entropy Map Reconstruction: Uses Class Activation Maps (CAMs) to reconstruct entropy maps which represent the uncertainty of contextual semantic information in the input data.

The SMN is optimized during the training phase using three loss functions:
<1>Cross-Entropy Loss (L1): Minimizes the difference between the predicted segmentation map and the ground truth labels.
<2>Structural Similarity Loss (L2): Minimizes the similarity between the entropy map generated by the segmentation pipeline and the entropy map reconstructed from CAMs.
<3>Density Regression Loss (L3): Minimizes the difference between the predicted density and the density calculated based on the segmentation map.

Additionally, this work introduces the concept of control neurons to simulate the human brain: by calculating the value of the control signals received by each control neuron, the connection strength (weights) between neurons is altered. The value of the control signals is generated by a linear combination of predicted densities. Furthermore, control neurons can also self-activate.

This work has conducted experiments on multiple benchmark datasets, demonstrating its superior performance in segmentation tasks. It also discusses the adaptability of SMN in different domains, as well as how to improve prediction accuracy by dynamically adjusting the network structure.

### Strengths
<1> The control neuron approach proposed to simulate the working mechanism of human brain neurons.
<2> Comprehensive theoretical argumentation and mathematical proof.
<3> Ample experimental validation.

### Weaknesses
<1> There has not been further verification of the SMN's performance on larger-scale datasets and when facing more complex tasks.


### Questions
<1> Can this method of simulating human brain control neurons be applied to other deep learning models? 
<2> Considering the complexity of the human brain's neural system, will training on models with larger parameter sizes yield better results?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the Shape-Memory Network (SMN), a neural network model that mimics the connectome structure of the brain by incorporating contextual semantic information to improve segmentation performance. The model distinguishes itself by emulating conditional activation and deactivation within neural pathways, specifically targeting the need for networks that can interpret and utilize contextual clues in a manner like the human brain. The SMN achieves this through "conditional neurons" that adjust dynamically based on contextual cues and synaptic-like processes. Experimental results on diverse semantic segmentation datasets show SMN's effectiveness in improving segmentation accuracy, especially in environments where object density and context significantly impact performance.

### Strengths
- The SMN’s focus on context-sensitive "conditional neurons" for segmentation tasks is innovative and relevant in the realm of biologically inspired AI architectures.

- The SMN’s theoretical grounding is solid, and its performance is evaluated across a variety of datasets, underscoring its effectiveness in segmentation.

- This work contributes to the understanding of context-based adaptive mechanisms, potentially influencing the design of future segmentation-focused neural models.

### Weaknesses
 - The conditional neuron mechanism introduces significant overhead, which may hinder scalability and real-time application potential.

- Some of the claims about biological emulation could be tempered, as certain parallels drawn between SMN and synaptic transmission in the human brain may be speculative.

- The design is highly tailored to segmentation, and extending the SMN to broader tasks without significant modification may be challenging.

### Questions
- Are there alternative ways to reduce the SMN’s computational overhead, particularly for real-time scenarios?

- How might SMN be adapted or validated for other tasks beyond segmentation?

- What strategies could increase generalization to tasks with different structural demands, like sequential or non-spatial data?

### Soundness
2

### Presentation
3

### Contribution
3
