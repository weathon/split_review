# $\textit{One Stone Three Birds:}$ Three-Dimensional Implicit Neural Network for Compression and Continuous Representation of Multi-Altitude Climate Data

- Decision: Reject
- Scores: 5, 6, 3

## Abstract
Wind energy stands out as a promising clean and renewable energy alternative, not only for its potential to combat global warming but also for its capacity to meet the ever-growing demand for energy. However, analysis of wind data to fully harness the benefits of wind energy demands tackling several related challenges: 
(1) Current data resolution is inadequate for capturing the detailed information needed across diverse climatic conditions;
(2) Efficient management and storage of real-time measurements are currently lacking;
(3) Extrapolating wind data across spatial specifications enables analysis at costly-to-measure, unobserved points is necessary.
In response to these challenges, we introduce a modality-agnostic learning framework utilizing implicit neural networks. Our model effectively compresses a large volume of climate data into a manageable latent codec. It also learns underlying continuous climate patterns, enabling reconstruction at any scale and supporting modality transfer and fusion. Extensive experimental results show consistent performance improvements over existing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an implicit neural network-based approach to analyzing wind data, addressing key challenges like limited data resolution (super-resolution downscaling task), high storage demands (data compression), and efficient extrapolation to unmeasured locations (spatial extrapolation).

### Strengths
- Meaningful motivation and nice problem settings - addressing several challenges (various resolutions, high-dimension, unobserved areas) in climate data.
- Nice application of Kolmogorov-Arnold Network (KAN) to climate domain.
- Fluent paper representation and enough experiments.

### Weaknesses
- Lack of state-of-the-art ML baselines for comparison. 
- Several claims are not precise (please see the questions below).
- No available codes.

### Questions
- You claim your work is **continuous** super-resolution, how finer is it to say "continuous"?
- I believe there is some related work using diffusion models and generative adversarial networks (GANs) for downscaling tasks. You may want to consider them as ML baselines. The current comparison against ML baselines is relatively weak.
- As you mentioned in the related work, data sources could be text, images, audio, and video. This is why it is called multi-modal learning (generally in the AI domain). In your work, you call the data at different altitudes as different modalities. It is confusing for users, especially for ICLR readers.
- You claim your model enables reconstruction at any scale. Do you use one model or train separate models for different scales?
- PSNR, SSIM, and CR are used as evaluation metrics. It would be better to provide the details on how to compute them? Any equations? Adding them in the appendix also helps if you have a limited-space problem.
- In Figure 4, it is surprising to see the model performance does not drop as the super-resolution scale increases. Could you please provide any possible reasons?
- In section 5.6, you train the ML model on one region and test it on other regions. This is actually an out-of-distribution (OOD) problem. You may want to add a short discussion on it (FYI). And, what is the meaning of the $x$-axis in Figure 6? Why are there some values between 1 and 2 or between 2 and 3?

### Soundness
2

### Presentation
3

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
Authors introduce a multi-modal architecture inspired by the implicit neural representation literature for cross-modal super-resolution. Their architecture's design is motivated by its usefulness for wind profile prediction, which tackles the following three points: 
1. **Resolution**: They build a continuous representation which allows their implicit super-resolution decoder to infer the wind field at any given coordinate.
2. **Data storage**: Their 3D Encoder Implicit Neural Network (INN) allows them to downsample the input low-resolution wind field that is later used for continuous reconstruction, which provides memory savings and efficient storage.
3. **Generalization**: Their achitecture allows for modality transfer using ther 3D Decoder INN which transfers the downsampled input wind field at one altitude level to a different altitude with the same resolution as the input, allowing them to later continuously reconstruct the higher-resolution wind profile.

### Strengths
- The paper is well motivated and presents three challenges in the face of wind energy deployment, which guided the design of their proposed architecture.
- Extensive experiments for demonstrating the strength of the architecture for super-resolution, compression and modality transfer
- OOD experiments for cross-region wind profile prediction
- Extensive ablation experiments motivate the utility of introduced architectural components

### Weaknesses
- Previous works have introduced architectures for doing similar things albeit in the related PDE solving and Neural Operator literature and the authors neither cite them nor do they compare against (at least one of) them:
  - [MeshfreeFlowNet: A Physics-Constrained Deep Continuous Space-Time  Super-Resolution Framework (SC20: International Conference for High Performance Computing, Networking, Storage and Analysis 2020)](https://arxiv.org/pdf/2005.01463.pdf)
  - [MAgNet: Mesh Agnostic Neural PDE Solver (Advances in Neural Information Processing Systems 2022)](https://arxiv.org/pdf/2210.05495.pdf)
  - [Fourier Neural Operator for Parametric Partial Differential Equations (International Conference On Learning Representations 2020)](https://arxiv.org/pdf/2010.08895.pdf)
 To name a few

### Questions
# Questions
- In line 302, it's said that the model is optimized using the L1 loss, however, it's not clear what exactly are the inputs of this loss. It's a loss between what and what?
# Comments
- The paper doesn't contain visualizations of the upscaled frames. Regression learns the mean of the conditional distribution which leads to a loss of the high-frequency information that is usually present in the wind profile (especially with turbulence).
- It's a bit hard to parse the PSNR/SSIM figure since there's no space between them, it would be better to have a small vertical space between them.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper designed a deep learning model to achieve scalable multi-modality learning, data dimensionality reduction, and continuous super-resolution for climate data. It addresses three emergent issues related to wind power generation: insufficient resolution of wind data, lack of storage of wind data, and high cost of wind data gathering at specific locations.

### Strengths
originality: It provides a new architecture for continuous super-resolution, which makes multi-modality learning more scalable.

quality: It provides rather comprehensive experiments to support its architecture modification and superiority.

clarity: The paper is readable to catch its main idea, but to get deep understanding of technique details requires effort.

significance: It addresses wind power generation challenges claimed in the paper.

### Weaknesses
Not enough justification of its architecture modification even though experimentally supported.

The notation system is extremely hard to follow. 

The paper requires extra effort on the writing. 

Your model is capable of arbitrary scale super-resolution after training. The model should be tested for zero-shot super-resolution which means to test on a different upsampling factor from the one it was trained on.

Your model is a super-resolution model. But there is not extensive comparison to other super-resolution models.

### Questions
Line 60: the framework name is very confusing.
Line 134: It is hard to read and understand. It requires to rephrase.  
Figure 1: The figure is too busy and hard to digest. For example, there are many dashed lines intersecting
L289: You did not split a part of your data into validation set. Then how did you choose your model hyper parameters?
L289: Why would you choose a rather small dataset for your method? Is it enough to train your model? 
L296: why are training data and test data constructed differently?

### Soundness
2

### Presentation
2

### Contribution
2
