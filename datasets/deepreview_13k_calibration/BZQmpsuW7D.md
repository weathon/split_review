# SPARK: Physics-Guided Quantitative Augmentation for Dynamical System Modeling

- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 6, 3, 6

## Abstract
In dynamical system modeling, traditional numerical methods have a solid theoretical foundation but are limited by high computational costs and sensitivity to initial conditions. Current data-driven approaches use deep learning models to capture complex spatiotemporal features, but they rely heavily on large amounts of data and assume a stable data distribution, making them ineffective against data scarcity and distribution shifts. To address these challenges, we propose SPARK, a physics-guided quantized augmentation plugin. SPARK integrates boundary information and physical parameters, using a reconstruction autoencoder to build a physics-rich discrete memory bank for data compression. It then enhances selected samples for downstream tasks with this pre-trained memory bank. SPARK then utilizes an attention mechanism to model historical observations and combines fourier-enhanced graph ODE to efficiently predict long-term dynamical systems, enhancing robustness and adaptability to complex physical environments. Extensive experiments on benchmark datasets show that our approach significantly outperforms various baseline methods in handling distribution shifts and data scarcity.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a new approach to spatiotemporal surrogate modeling. Their approach aims to target some of the limitations of data-driven models as they pertain to distribution shift. The framework, SPARK, combines physics-guided data augmentation and compression to enhance generalization. Key architectural innovations include a discrete memory bank for storing previous physical samples, physical prior and BC incorporation with graph neural nets, and a curriculum learning strategy to incorporate augmented data progressively. SPARK's superior performance is then evaluated on a relatively large suite of benchmark datasets.

### Strengths
- The incorporation of a data bank to progressively generate augmented samples is an intelligent design choice, enabling the model to store physical information for use in OOD prediction. Combined with the work on storing physical parameters and boundary conditions, the authors have presented many useful tricks for physical surrogate modeling. 
- Extensive tests across numerous datasets and benchmarks conclusively demonstrate the superior performance of this training strategy, particularly in OOD scenarios. The benchmarks are extensive as well, and helpful in framing the work.
- The theoretical framework is helpful, providing solid support for the model's architecture and approach.
- The paper is well-written and well-presented.

### Weaknesses
 - Many new architectural design choices are proposed (handling of physical parameters, boundary conditions, data banks, curriculum learning, etc.). However, it is unclear how much each strategy contributes to the success of the model, and some ablation studies would be useful.

### Questions
- Can the data bank be used for direct retrieval-augmentation?
- How well does the model perform in the very low-data regime (just a few samples for transfer learning)?
- Have the authors explore generalization to 1-D or 3-D data at all?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Data-driven methods for dynamical systems often face distribution shift challenges. To tackle this, this paper proposes SPARK, a physics-guided plugin to address both environmental distribution shift (due to changes in boundary conditions and physical parameters) and temporal distribution shift.
SPARK achieves this by incorporating the boundary information and physical parameters into a discrete memory bank constructed through solution reconstructions.
By embedding these physical priors, the memory bank can then be used to augment data samples in downstream tasks, thereby increasing model generalizability.
To handle the temporal distribution shift, SPARK encodes historical information into initial states through attention and uses Fourier-enhanced graph ODE for long-term prediction.
In the end, the paper evaluates SPARK on several benchmarks.

### Strengths
1. The idea of increasing model generalizability by augmenting data in downstream tasks with a pre-trained memory bank that contains boundary information and physical parameters is nice.
2. The paper evaluates the method on a good number of benchmarks.

### Weaknesses
1. The degree of originality is not high. It shares quite some similarities with the DGODE model in (Prometheus by Wu et al. 2024, cited by the paper), which proposed the idea of "codebank" to include the environmental factor for OOD and graph ODE for future predictions.
2. The algorithm is not clearly presented. The paper presented reasonable ideas but without enough technical details to tell a clear story. 
Mathematical notation is not clearly defined, which makes it hard to follow the method. For example, how is the "real boundary" ("p^{boun}")represented? Is it a list of spatial coordinates of discrete boundary nodes? Time index does not make sense in section 3.3. For example, T in equation 8 is the length of history observations but then it is also used in loss function in equation 11 to represent the number of future predictive steps, which is confusing. Index notation does not make sense in the pretraining loss equation (6).
3. It's unclear how the discrete memory bank is built. What are the e_i in E and how are they constructed ?

### Questions
1. How are the with and without OOD datasets constructed in the experiments? Is there an explanation for why SPARK achieved better performance on OOD cases even than other models did on non-OOD cases? 
2. Given the big accuracy difference, what is the training cost comparison?
3. What are the training details, e.g., model architecture, optimizer, training devices?  Is boundary information injected at two places, i.e., through node features and directly through the boundary latent vector B?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces SPARK, a physics-guided augmentation framework for modeling dynamical systems that overcomes the limitations of traditional numerical and data-driven methods. By incorporating a unique compression and augmentation plugin, along with an attention mechanism and Fourier-enhanced graph ODE, SPARK improves model generalization and robustness, especially in data-scarce situations and distribution shifts. Experimental results highlight SPARK's strong performance in accurately predicting complex spatiotemporal dynamics, particularly in challenging cases like sea ice evolution, effectively capturing intricate physical phenomena.

### Strengths
1. By incorporating boundary information and physical parameters, SPARK enhances the model's ability to generalize across different physical scenarios, which is crucial for real-world applications.
2. The paper provides extensive experimental results across various benchmark datasets, demonstrating SPARK's superior performance compared to existing models, particularly in handling out-of-distribution scenarios.

### Weaknesses
1. The symbols and formulas appear to be somewhat disorganized, which makes it difficult for readers to understand the meaning.  Clear definitions and a more structured presentation of the equations would greatly enhance the paper's accessibility and overall readability.
2. The lack of novelty. This paper claims to be the first to use physics-guided compression and augmentation. But there has been a paper [1] doing like this. The techniques of the two papers are very similar, including : (1) using VQ-VAE to compress information (2) augmenting training set by the top-K discrete embeddings.
3. The proposed methodology, may be complex to implement in practice. The paper could provide more guidance or examples on how to effectively apply SPARK in different contexts.

### Questions
1. In line 163, it needs references for those methods which simply concatenate boundary information with node features.
2. What does boundary information refer to? Give some examples please.
3. In abstract, what's the meaning of "stable data distribution"? Provide explanations about it and why does it can cause ineffectiveness of data scarcity and distribution shifts.

### Soundness
3

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
4

### Summary
This paper proposes SPARK to address the challenges of data scarcity and distribution shifts in dynamical system modeling. SPARK integrates boundary information and physical parameters by using an autoencoder, and then a pre-trained memory bank is obtained. It further combines Fourier-enhanced graph ODE to efficiently predict long-term dynamical systems. The experimental results have demonstrated the superiority of the proposed method against the baseline models across many dynamical systems under distribution shifts and limited data conditions.

### Strengths
- This paper presents an interesting idea for handling data scarcity and OOD, which are important topics in scientific machine learning. 

- This paper is well-written and has a detailed presentation of methods, experimental setup, and results discussion.

- This paper has tested multiple challenging datasets, such as ERA5 and 3D systems.

### Weaknesses
 - The motivation for using each component in SPARK can be further clarified. The paper will benefit from discussing the interconnection between each network component.  

- It would also be good to have ablation studies on incorporated physics. The authors may consider reducing physical information (i.e., boundary information and physical parameters) for pre-training. Then, we can see the contribution of each physical component.

### Questions
- On Page 6, for RQ2, could you be more specific on what challenging tasks?

- What is the setup for OOD experiments?

- How do you compute PSNR and SSIM for scientific data? Image data has a fixed range of [0,255] but scientific data doesn’t. 

- Energy Spectrum is a common metric for fluid dynamics. Is it also commonly used for reaction-diffusion equations? How does this paper compute the energy spectrum?


- Some minor typos: 

    - On Page 2, “effectively long-term prediction” should be “effective …”.

### Soundness
3

### Presentation
3

### Contribution
3
