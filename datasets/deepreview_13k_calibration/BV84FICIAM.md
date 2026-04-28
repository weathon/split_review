# Energy-Based Conceptual Diffusion Model

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Diffusion models have shown impressive sample generation capabilities across various domains. However, current methods are still lacking in human-understandable explanations and interpretable control: (1) they do not provide a probabilistic framework for systematic interpretation. For example, when tasked with generating an image of a "Nighthawk", they cannot quantify the probability of specific concepts (e.g., "black bill" and "brown crown" usually seen in Nighthawks) or verify whether the generated concepts align with the instruction. This limits explanations of the generative process; (2) they do not naturally support control mechanisms based on concept probabilities, such as correcting errors (e.g., correcting "black crown" to "brown crown" in a generated "Nighthawk" image) or performing imputations using these concepts, therefore falling short in interpretable editing capabilities. To address these limitations, we propose Energy-based Conceptual Diffusion Models (ECDMs). ECDMs integrate diffusion models and Concept Bottleneck Models (CBMs) within the framework of Energy-Based Models to provide unified interpretations. Unlike conventional CBMs, which are typically discriminative, our approach extends CBMs to the generative process. ECDMs use a set of energy networks and pretrained diffusion models to define the joint energy estimation of the input instructions, concept vectors, and generated images. This unified framework enables concept-based generation, interpretation, debugging, intervention, and imputation through conditional probabilities derived from energy estimates. Our experiments on various real-world datasets demonstrate that ECDMs offer both strong generative performance and rich concept-based interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces concept bottleneck model into the diffusion generation process.

### Strengths
1. The paper is well-written and easy to read.

2. The paper introduces concept bottleneck model into the generative diffusion model. Now the model has probilistic interpretation about the generated images.

### Weaknesses
1.  Although I appreciate the idea of using concept sets to explain the generation, the proposed formulation does not make sense to me. The paper transforms a text embedding into a probility vector that represents the concepts. The point is that it is a deterministic mapping. For instance, "polar bear" outputs a determinsitic vector that represents the "paws", "furry" and "big".  In many situations, we would expect a polar bear could be of different size, so "big" dim should vary from [0,1] in different polar bear images. In other words, I am expecting that the concept probability vector changes with generated image (not only the input tex prompt).  

2. Given a binary concept labes set, I am wondering the optimal output of the concept energy model with input y?  It seems that a binary output is also expected from y to minimize the loss? If yes, can we just use a logic mapping, i.e., "polar bear"-> paws=1, big=1. (So, we do not have to learn the first energy model).  If not, can you provide any explanation why it would not learn a binary vector given the target is binary?

### Questions
as above

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
3

### Summary
This paper introduces Energy-based Conceptual Diffusion Models (ECDMs), which integrate diffusion models and Concept Bottleneck Models within an energy-based framework. The key contribution is providing a unified approach for concept-based generation, interpretation, debugging, intervention, and imputation. The method enables both high-quality image generation and human-interpretable control through concepts. The authors demonstrate effectiveness on three datasets (CUB, AWA2, CelebA-HQ) through quantitative and qualitative evaluations.

### Strengths
1. Novel integration of concept bottleneck models with diffusion models through an energy-based framework

2. Comprehensive theoretical framework with detailed proofs

3. Multiple practical applications (generation, interpretation, debugging, intervention)

4. Strong empirical results across different datasets

5. Clear improvement over baseline methods in both generation quality and concept accuracy

### Weaknesses
The paper fails to acknowledge pioneering work on energy-based diffusion models, particularly "Diffusion Recovery Likelihood" and "Cooperative Diffusion Recovery Likelihood" and also fail to include a wide range of works using EBM as compositions such as "a theory of generative convnet", "Implicit Generation and Generalization in Energy-Based Models" etc.

### Questions
1. How does the method scale with increasing number of concepts?

2. What is the computational overhead compared to standard diffusion models?

3. Could the framework be extended to handle continuous concept values rather than binary?

4. How robust is the concept interpretation when handling out-of-distribution samples?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a framework that integrates diffusion models and Concept Bottleneck Models in an energy based model structure. ECDM aims to address interpretable control in current diffusion models. It allows concept-based generation, interpretation, debugging, intervention, and imputation. ECDM unifies tasks through energy networks, which enables modifications in the generated images based on probabilistic estimates. The model is evaluated on datasets like AWA2, CUB, and CelebA-HQ in concept accuracy, class accuracy, and FID scores with existing diffusion models.

### Strengths
1. ECDM combines diffusion models with concept bottlenecks in a way that supports both generative and interpretive tasks.
2. The model allows users to modify generated images based on specific concept-level controls, which is a practical tool.
3. The experiments on multiple datasets shows quantitative improvements in image quality and concept alignment.

### Weaknesses
1. The paper lacks comparisons with some related methods like COMET or CBGM, which are relevant energy-based interpretive frameworks for diffusion models.
2. While FID, class, and concept accuracy are used, other metrics like diversity or user-study-based interpretability scores could further validate the model's effectiveness.
3. Code for reproducibility is not provided.
4. The experiments rely on a fixed pretrained stable diffusion model, while other models are not explored.
5. Limitations: The method struggles with precise regional control over concept-based edits. Also, the energy-based approach is computationally intensive, especially during joint optimization steps.

### Questions
1. Concepts like "pivotal inversion" and "energy matching inference" could be better explained for clarity.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a concept-based diffusion model that enables conditional generation, concept interpretation and debugging, as well as image operations like intervention and imputation.

### Strengths
1. The paper is clearly written and well-organized, making complex concepts more accessible.
2. The authors conduct thorough experiments across various datasets and tasks, providing clear comparisons to existing benchmarks.
3. The concept-based framework is versatile and seems applicable to any conditional data generation task.
4. The framework enhances the interpretability of the elements and features in the generated images.

### Weaknesses
1.  I have to mention that I have not previously conducted research about concept-based generation, but the significance of this work within the broader field of generative models is unclear for me. It appears to be a straightforward combination of concept bottleneck models and standard conditional diffusion models.
2. The concept-based generation method described in (11)-(13) resembles a Gibbs sampling or coordinate-wise algorithm, but equation (11) focuses on maximizing mapping energy $ E^{map} $ rather than the entire joint energy $E^{joint}$. This raises questions about the rationale behind this approach, as $ E^{joint}=E^{map} +E^{concept}  $ incorporates dependencies on the concept $c $ in both terms. Additionally, maximizing  $ E^{map} $ with respect to the binary vector $c$ suggests an integer programming problem, which the paper does not sufficiently address regarding efficiency.

### Questions
1. Is the code for the model available now?
2. How is the number of concepts  $K$ in the concept vector $ c \in \set{0,1}^K $ determined? Is $ K $ fixed?
3. How is the concept embedding $v_k $ modeled?
4. What distinguishes the generation process described in equations (12) and (13) from that of a standard conditional diffusion model? It seems the only change is replacing the conditioning input $ y $ with the processed conditioning input $ c $ obtained from $y$.

### Soundness
2

### Presentation
3

### Contribution
2
