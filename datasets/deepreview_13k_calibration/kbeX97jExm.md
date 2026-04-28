# Neural Wave Equation for Irregularly Sampled Sequence Data

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Sequence labeling problems arise in several real-world applications such as healthcare and robotics. In many such applications, sequence data are irregularly sampled and are of varying complexities. Recently, efforts have been made to develop neural ODE-based architectures to model the evolution of hidden states continuously in time, to address irregularly sampled sequence data. However, they assume a fixed architectural depth and limit their flexibility to adapt to data sets with varying complexities. We propose the neural wave equation, a novel deep learning method inspired by the wave equation, to address this through continuous modeling of depth. Neural Wave Equation models the evolution of hidden states continuously across time as well as depth by using a non-homogeneous wave equation parameterized by a neural network.  Through d'Alembert's analytical solution of the wave equation, we also show that the neural wave equation provides denser connections across the hidden states, allowing for better modeling capability.  We conduct experiments on several sequence labeling problems involving irregularly sampled sequence data and demonstrate the superior performance of the proposed neural wave equation model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the neural wave equation, a novel approach to handling irregularly sampled sequence data by modeling hidden state evolution using wave equations. The authors propose using a non-homogeneous wave equation with a neural network-parameterized source function to capture sequence dependencies. The method allows continuous modeling across both time and depth dimensions, addressing limitations of existing approaches that use discrete depth transformations. The authors demonstrate the effectiveness of their approach through experiments on various sequence labeling tasks, including person activity recognition, Walker2d kinematic simulation, sepsis prediction, and stance classification, showing competitive or superior performance compared to existing baselines.

### Strengths
- Strong theoretical foundation with clear mathematical derivations
- Comprehensive experimental evaluation across diverse datasets
- Thoughtful comparison with existing approaches, especially heat equation-based methods
- Detailed ablation studies showing the importance of different components

### Weaknesses
 - The motivation for choosing wave equations could be stronger
- Memory consumption issues are noted but not thoroughly addressed
- The connection between theoretical advantages and empirical improvements could be clearer
- Limited discussion of computational complexity trade-offs
- Some implementation details about boundary conditions could be more explicit

### Questions
- How sensitive is the model to the choice of wave speed parameter c?
- Could you elaborate on how boundary conditions are handled in practice?
- How does the computational complexity compare to existing methods?
- Have you explored any techniques to reduce memory consumption?
- How does the model perform with very long sequences?

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
4

### Summary
This paper introduces a novel architecture for latent space modeling and prediction using the Wave equation. Motivated by the homogeneous and non-homogeneous wave equations, the authors proposed neural wave equation to model the hidden layer transformations. In the experiments, the authors tested and showed superior performances on person activity recognition, walker2d-v2, sepsis, and social media posts datasets.

### Strengths
This paper proposed a very innovative idea which utilizes the wave equation to model the latent space. From the reviewer's perspective, this is good since this kind of structure could model physical/natural phenomenon(s) better. And the model is still generalizable from the non-homogeneous formulation with F(z,t). 

Experimentally, neural wave equations also dominated the baseline methods in most of the metrics. 

In general, this paper introduces a very innovative method which requires further study, and could have huge potential impact to the field.

### Weaknesses
There are several weaknesses of this manuscript. 

1. The presentation of this manuscript is not optimal. For example, the Figure 1 requires some imagination to understand the design to distinguish the three methods. 

2. The experiments are nice, but the neural wave equation might not perform as well as the baseline methods for some data. This could potentially be because the form of the wave equation acts as a strong prior that might not fit the data. It would be nice to understand further the limitation of this framework. The ablation study could potentially be extended.

### Questions
1. Can the neural wave equation be applied only to irregularly sampled sequence data, or could it also work in more general sequence modeling settings? What is the reason for only putting this framework into the irregularly sampled sequence data setting? 

2. The reviewer suggests improving the quality of Figure 1. Some fonts are too small to read, so please use PDF or SVG formats to enhance the visual clarity. Additionally, could the authors consider redesigning the figure? The current design makes it difficult to distinguish between straight and curved lines. While it makes sense that curved lines represent continuity, there may be a clearer way to convey this distinction.

3. Practically, is this algorithm fast to run? 

4. What will be the limitation for incorporating this structure of wave equation. What happens if the real latent dynamics follows another PDE that cannot be modeled as a wave equation? 

5. What is the reason that in some experiments, the performance is suboptimal compared to baseline methods? 

6. In page 6, Line 302, please consider changing the '-' to ":". 

7. The algorithm description of neural wave equation would require a significant rewrite. The current version is hard to be understood. 

8. The appendix provides an introduction of the solution of wave equation. The reviewer believes that the authors should provide proper citations here and it is very important.

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the limitation of fixed architectural depth in modeling irregularly sampled sequence data. A neural wave equation method is proposed to 1) continuously model the hidden states across time and depth and 2) allow denser connections across hidden states. Empirical results show improved performance compared to baseline methods.

### Strengths
1. The problem of fixed assumption in architectural depth is important. 
2. The method of using the wave equation to continuously model the time and depth is creative. Developing the neural network based on the analytical solution to the wave equation allows more dependencies in hidden states.
3. Experiments were performed on different scenarios to show the effectiveness of the proposed method.

### Weaknesses
1. The introduction and related work need to be better structured. For instance, what is the concept of hidden state depth in real-world problems? Could the authors elaborate on why PDE-based models are a better model for continuous modeling on depth? What is the benefit of the wave equation over the other PDEs? The authors could provide more details in both sections for a smoother transition from the problem setting to the proposed method.
2. Section 3 and 4 could be better presented. For example, instead of presenting Figure 2, the authors could provide a comparison between ODE-RNN and the proposed method in terms of how they model in depth. In fact, Figure 2 should be in an ablation study and needs a better explanation of how the depth affects the three comparison models. Also, using $t’$ for depth is confusing given that $t$ is used for time. For Figure 3, the authors should explain the blue arrows with the description in Section 4.2.
3. The experiments should be performed and analyzed in more detail. For each experiment, could the authors highlight the purpose, such as how the depth of hidden states or the number of missing data affects the model performance? What is the depth of each group of data? Could the authors group the comparison baselines as the categories in Figure 1? Table 1 could be separated by the experiments. Also, it would be better to have visualizations about the predicted sequences vs the ground truth to better understand the improvement in metrics.

### Questions
Please check the questions listed in the Weaknesses section.

### Soundness
4

### Presentation
3

### Contribution
3
