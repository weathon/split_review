# Continuous Diffusion for Mixed-Type Tabular Data

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
\looseness=-1 Score-based generative models (or diffusion models for short) have proven successful for generating text and image data.
However, the adaption of this model family to tabular data of mixed-type has fallen short so far. 
In this paper, we propose CDTD, a Continuous Diffusion model for mixed-type Tabular Data. Specifically, we combine score matching and score interpolation to ensure a common continuous noise distribution for \emph{both} continuous and categorical features alike. 
We counteract the high heterogeneity inherent to data of mixed-type with distinct, adaptive noise schedules per feature or per data type.
The learnable noise schedules ensure optimally allocated model capacity and balanced generative capability.
We homogenize the data types further with model-specific loss calibration and initialization schemes tailored to mixed-type tabular data.
Our experimental results show that CDTD consistently outperforms state-of-the-art benchmark models, captures feature correlations exceptionally well, and that heterogeneity in the noise schedule design boosts the sample quality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a continuous diffusion model for mixed-type tabular data, which
combines score matching and score interpolation techniques and imposes Gaussian diffusion
processes on both continuous and embedded categorical features. 

It proposes several strategies to balance model capacity between continuous and categorical features, including
weighted loss calibration, adjusted model initialization, and the adaptive noise schedule
designs.

### Strengths
1. The problem is well motivated, and the intuition of this research is quite clear, which is to propose a unified pipeline to deal
with mixed type tabular data, which contains both continuous and categorical features.  In addition, the proposed strategies effectively deal with the imbalance and calibration between these two types of data.

2. Mathematical derivations are quite solid and appear to be valid, though having not checked completely.  

3. Implement comprehensive experiments to demonstrate the effectiveness of the overall pipeline as well as each design component.

### Weaknesses
Weaknesses:   


1. The overall pipeline has limited novelty, as the key idea to push categorical data into
embedding space and use a Gaussian diffusion process to deal with it is a common
practice.


2. The preliminary section 2.2 that introduces diffusion for categorical features is not as clear
as that in 2.1. I wish the author to elaborate this part a bit more since this should be the
basic foundation of CDTD.


3. The customization on tabular data in section 3.4 is quite heuristic, are they supported by
theoretical proof or are they simply determined from empirical results?

### Questions
The section that introduces learnable noise schedules is unclear. For example, its
motivation is confusing.   What does it mean that “given the same embedding dimension,
more noise is needed to remove the same amount of signal from embedding of features
with fewer classes”? 

Can you explain the difference between Feature-specific Noise Schedules and Adaptive Noise Schedules in more detail ?

[post rebuttal comment]. Some of the questions above are addressed by the author. I am happy to upgrade my rate for the paper.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a joint continuous diffusion model for mixed type tabular data. Due to the mixed type of data format, the paper designs a score matching method and a score interpolation method for both continuous and categorical data. It presents a loss calibration method to balance the losses between the continuous and categorical data, and proposes an adaptive noise schedule.

### Strengths
+ the paper is relatively easy to follow. The presentation of the paper is good
+ comparing with baseline methods, the proposed method seems to be working relatively well, although I have not directly worked on diffusion model for tabular data. There could be related work I am missing
+ contributions and limitations of the paper are properly discussed

### Weaknesses
 - the scope of the method is relatively limited on just mixed type tabular data. Diffusion model for tabular data had already been studied (e.g. Kotelnikov, 2023), and the contribution of this paper seems to be rather incremental in the sense that it just makes the diffusion model work a bit better in mixed type tabular data
- the method, although makes sense, is not novel in the whole landscape of diffusion models. Modeling continuous and categorical features has been studied in the past and many had been cited by the authors. This seems to be mostly applying these to this particular type of data

### Questions
See the weakness section

### Soundness
2

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
3

### Summary
This paper combines score matching and score interpolation to ensure a common continuous noise distribution for both continuous and categorical features in tabular data generation. The proposed method focuses on adjusting noise schedules to enhance performance in generating synthetic tabular data.

### Strengths
1. Superior Performance: The results reported in the paper demonstrate strong performance on existing datasets, showing significant improvements compared to baseline methods.

2. Simplicity and Clarity: The methodology centers on adjusting noise schedules, which is straightforward and easy to understand, making the approach accessible and replicable.

### Weaknesses
1. Limited Novelty: The primary method introduced is Adaptive Noise Schedules, an area that has been extensively explored in prior research. Additionally, the paper addresses the homogenization of different data types—a problem that has been widely studied in previous tabular data generation works [1],[2]. Consequently, the novelty of this paper is significantly diminished, and the authors need to clearly articulate the innovative aspects of their approach. Specifically, the paper does not adequately differentiate its approach from existing methods that also tackle mixed-type data, such as those employing latent space diffusion or other homogenization techniques. The core idea of adjusting noise schedules, while practically useful, lacks a strong theoretical underpinning or a novel perspective that advances the field beyond incremental improvements. The paper needs to highlight more clearly how its method goes beyond simply applying existing techniques to a new context.

2. Insufficient Experimental Reporting: The experimental results are not thoroughly reported. The authors compare their method with baseline approaches using only an average metric across various datasets, which leads to the loss of detailed information. To provide a more comprehensive evaluation, the authors should conduct detailed comparisons on each individual dataset, referencing methodologies from previous studies [1]. The use of an average metric obscures the performance variability across different datasets, making it difficult to assess the robustness and generalizability of the proposed method. Reporting only average performance masks potential weaknesses on specific datasets, which is crucial for a thorough evaluation of the method's applicability and limitations.

### Questions
Please see the weakness part

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
This paper trains a diffusion model for mixed-type (continuous and categorical) tabular data. The authors combine score matching with score interpolation to derive a diffusion model that add noise of categorical data in the embedding space, which makes it able to apply denoising process to mixed-type tabular data. To deal with the heterogenity of different types and features of data, the author further use noise calibration to balance the scale of continuous and categorical data. They also experimented on different types of noise schedules for better model training. The authors performed experiments and ablation studies on multiple datasets and used different metrics, the results showed that their model was able to achieve great performance on mixed-type tabular data.

### Strengths
- The authors proposed the first model to allow diffusion models to train on mixed-type tabular data, and allows the use of advanced techniques such as classifier-free guidance in training.
- To allow training on mixed-type tabular data, the authors have introduced several customizations to diffusion models: such as loss balancing, and noise schedules.
- The experiments and comparisons look quite complete for me: the authors compared with seven methods on eleven datasets, using different kinds of metrics. The analysis of the results are also quite good. Results have shown that their method can achieve good results and higher efficiency.
- The authors have provided details of all the implementation and experiments, they also provided their code in the supplementary. I believe this is quite useful for further researchers.

### Weaknesses
 - The paper is more like a combination of existing models: diffusion models have already been applied to both categorical data and continuous data before. The authors combine them to deal with mixed-type data.
- The introduced changes: reweighting losses and changing noise schedules, although useful, but I think they are a bit minor to be counted as big technical contributions. The main reason is that they are a bit straightforward and also limited to current data setting. I am also curious that whether the noise schedules are also useful for data beyond mixed-type tabular data.

### Questions
Please see weaknesses part. I would like to discuss with the authors on those points.

### Soundness
3

### Presentation
3

### Contribution
2
