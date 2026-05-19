# A Geometric Framework for Understanding Memorization in Generative Models

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
As deep generative models have progressed, recent work has shown them to be capable of memorizing and reproducing training datapoints when deployed. These findings call into question the usability of generative models, especially in light of the legal and privacy risks brought about by memorization. To better understand this phenomenon, we propose the \emph{manifold memorization hypothesis} (MMH), a geometric framework which leverages the manifold hypothesis into a clear language in which to reason about memorization. We propose to analyze memorization in terms of the relationship between the dimensionalities of $(i)$ the ground truth data manifold and $(ii)$ the manifold learned by the model. This framework provides a formal standard for ``how memorized'' a datapoint is and systematically categorizes memorized data into two types: memorization driven by overfitting and memorization driven by the underlying data distribution. By analyzing prior work in the context of the MMH, we explain and unify assorted observations in the literature. We empirically validate the MMH using synthetic data and  image datasets up to the scale of Stable Diffusion, developing new tools for detecting and preventing generation of memorized samples in the process.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Memorization in Generative model occurs when model reproduce its training data instead generalising from it. This phenomenon is undesirable because it represent to modelling failure. The paper introduces the "manifold memorization hypothesis" (MMH) to explain memorization geometrically. It suggests that memorization happens when the manifold learned by the model at a point has a lower dimensionality than the true data manifold at that point. This framework defines two types of memorization:
Overfitting-Driven Memorization (OD-Mem): This occurs when the model assigns low dimensionality to a region of the manifold, overfitting specific training data points.
Data-Driven Memorization (DD-Mem): This happens when the true data distribution inherently has low dimensionality in certain regions, leading the model to reproduce specific details in these regions even if it generalizes well.

The paper introduces the Manifold Memorization Hypothesis (MMH) as a geometric framework to analyze and understand memorization in deep generative models (DGMs). It explores memorization through the lens of local intrinsic dimension (LID), a metric used to assess whether a model's manifold dimension aligns with that of the underlying data. The authors identify two types of memorization: overfitting-driven memorization (OD-Mem) and data-driven memorization (DD-Mem), categorizing instances of memorization based on LID discrepancies. This hypothesis is validated empirically with synthetic and real datasets, demonstrating how MMH can predict memorization tendencies and proposing methods to mitigate memorization in diffusion models, particularly Stable Diffusion.

### Strengths
The introduction of MMH offers a fresh perspective on memorization, connecting it to geometric properties and adding depth to existing theoretical understandings.
 The paper proposes actionable techniques to reduce memorization in generative models, which has direct implications for improving model safety and compliance.

### Weaknesses
The reliance on geometric and measure theory could make it challenging for a broader audience to fully understand and appreciate the framework. 
There should be more experiments
While LID proves to be an effective measure, there is some overlap between memorized and non-memorized samples in LID estimates, which may affect its reliability in distinguishing memorized samples in real-world applications.

### Questions
How does the MMH framework extend to discrete generative models, such as those in NLP (transformer)?
Could alternative LID estimation methods reduce the overlap issue observed in the experiments, or is this an inherent limitation of the current approach?
Are there specific types of datasets or model architectures where MMH may not apply effectively?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Memorization is a big issue in deep generative models. Recent works have highlighted that such models are prone to duplicating their training points, given certain prompts, or generating samples that appear very close to training points with slight modifications (e.g., background and color). To combat and understand this phenomenon, this paper proposes a geometric framework which leverages the manifold hypothesis. Particularly, the work analyzes memorization in terms of the relationship between dimensionalities of the ground truth data manifold and the manifold that is learned by the model. This is done by analyzing and calculating the Local Instrinsic Dimension (LID) of the data and generated points, and building a theoretical understanding around the model's memorization behaviors. Overall, the paper validates the applicability of the manifold analysis in the detection of memorized samples through the development of new tools and prevention methods in generating such samples.

### Strengths
The paper provides a very valuable and interesting perspective about memorization, which comes in two forms: Overfitting-driven Memorization (OD-Mem) and Data-driven Memorization (DD-Mem). These two forms of memorization highlight that memorization is a convoluted aspect of trained deep networks, and it should not always be naively thought of as just overfitting. The paper does a decent job with making a case for this topic, by using LID as a metric of identifying memorized samples. 

Furthermore, the work introduces a differential metric, $\mathcal{A}^\text{FLIPD}$, which allows for the optimization of a conditional variable $c$ to prevent the reproduction of training points during sampling. Specifically, the authors extended and combined the work of [Wen at al. (2024)](https://arxiv.org/pdf/2407.21720) and [Kamkari et al. (2024)](https://arxiv.org/pdf/2406.03537) to produce the aforementioned metrics, which show promising results in the prevention of memorization for stable diffusion models.

### Weaknesses
The comparison of various LID metrics to other memorization detection metrics is not quite clear, especially in figure 6. It is difficult to tell how much more effective LID metrics are since the authors did not contrast them well in their written text, and it is difficult to interpret the results in the density histograms of fig. 6 without showcasing what is classified as memorization, visually.

Furthermore, it is still unclear on how to quantitatively differentiate between OD-Mem and DD-Mem samples. The description, visualization (fig. 1), and toy example (fig. 4) certainly highlight the differences, but for natural datasets, it is difficult to tell still.

### Questions
For definition 3.1, could you elaborate on condition (2) or why $p_\theta$ cannot be equal to $p_*$?

Could you elaborate the differences between $s_\theta$ and $s_\theta^\text{CFG}$ in equation 41 of the Appendix D.2? 

What is the conclusion of figure 6? The importance of this figure/result is not clear to me. 

Could you provide more figures like figure (a), of memorized samples, in Figure 5? What was the threshold used in the detection metric from [Carlini et al. (2023)](https://arxiv.org/pdf/2301.13188), which was used to identify memorized samples?

Both $\hat{LID_\theta}$ and $\hat{LID_*}$ are estimators of LID. Is it fair to assume that $\hat{\text{LID}}_*$ is more accurate? Or, is that the wrong interpretation?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes MMH, a geometric framework for understanding memorization in generative models by focusing on the dimensions of learned manifolds. It aims to analyze memorization as a function of the ground truth data manifold and the learned model manifold. The framework distinguishes between two types of memorization: overfitting-driven and data-driven, providing a theoretical base and empirical tools for detecting memorization across a range of models, from synthetic data to image generation using Stable Diffusion.

### Strengths
1. The authors combine the manifold memorization hypothesis and a geometric perspective to memorization, potentially unifying existing observations into a cohesive framework.
2. The paper provides clear motivation and background on memorization in DGMs, connecting memorization to legal and ethical implications.
3. The empirical experiments well support the propositions and theorems.

### Weaknesses
1. Some minor typos, for example ''subtantial'' should be ''substantial'' in line 44.
2. The MMH concept does not introduce substantial novel contributions beyond covering DD-Mem rather than only considering OD-Mem. This work is more like summarizing the existing work with their framework. For example, Proposition 3.5 is a (in)-formal summary of the findings in [1]'s experiments with MMH.

[1] Yuxin Wen, Yuchen Liu, Chen Chen, and Lingjuan Lyu. Detecting, explaining, and mitigating memorization in diffusion models. In Proc. ICLR, 2024.

### Questions
1. I am confused about the definition of LID. From the whole paper, I can tell the smaller the LID is the more memorization. In line 134, it is defined as ''the number of degrees of freedom'' instead of the number of variables needed in a minimal representation of the data. However, based on lines 125-126, it seems to be the same as the intrinsic dimension. Could you clarify?
2. In line 182: ''a notable consequence is that it cannot be detected by comparing training and test likelihoods''. Can you elaborate more about this?
3. As mentioned in the weaknesses, could you explicitly state your novel contributions more, or provide specific examples of how the framework goes beyond existing work? Currently, there is no comparison with the existing frameworks, such as [2]. I will be happy to increase my score if this is resolved.

[2] Robi Bhattacharjee, Sanjoy Dasgupta, and Kamalika Chaudhuri. Data-copying in generative models: a formal framework. In International Conference on Machine Learning, 2023.

### Soundness
2

### Presentation
3

### Contribution
3
