# Inverse Engineering Diffusion: Deriving Variance Schedules with Rationale

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
A fundamental aspect of diffusion models is the variance schedule, which governs the evolution of variance throughout the diffusion process. Despite numerous studies exploring variance schedules, little effort has been made to understand the variance distributions implied by sampling from these schedules and how it benefits both training and data generation. We introduce a novel perspective on score-based diffusion models, bridging the gap between the variance schedule and its underlying variance distribution. Specifically, we propose the notion of sampling variance according to a probabilistic rationale, which induces a density. Our approach views the inverse of the variance schedule as a cumulative distribution function (CDF) and its first derivative as a probability density function (PDF) of the variance distribution. This formulation not only offers a unified view of variance schedules but also allows for the direct engineering of a variance schedule from the probabilistic rationale of its inverse function. Additionally, our framework is not limited to CDFs with closed-form inverse solutions, enabling the exploration of variance schedules that are unattainable through conventional methods. We present the tools required to obtain a diverse array of novel variance schedules tailored to specific rationales, such as separability metrics or prior beliefs. These schedules may exhibit varied dynamics, ranging from rapid convergence towards zero to prolonged periods in high-variance regions. Through comprehensive empirical evaluation, we demonstrate the efficacy of enhancing the performance of diffusion models with schedules distinct from those encountered during training. We provide a principled and unified approach to variance schedules in diffusion models, revealing the relationship between variance schedules and their underlying probabilistic rationales, which yields notable improvements in image generation performance, as measured by FID.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work introduces an approach to understand and design variance schedules in diffusion models, particularly in the context of score-based diffusion frameworks. It emphasizes the importance of the variance schedule in both training and sampling phases, proposing a probabilistic rationale for constructing these schedules. The paper introduces the concept of "rationales," which are functions that define how variance is distributed throughout the diffusion process. By treating the inverse of a variance schedule as a cumulative distribution function (CDF) and its derivative as a probability density function (PDF), the framework allows for more flexible and diverse variance schedules. The paper demonstrates that different schedules—such as those derived from the squared L2-norm or the VE schedule—can impact both model convergence during training and performance during sampling.

### Strengths
1. The introduction of the "rationale" concept offers a new way to understand and design variance schedules, allowing for better control over the behavior of the diffusion process.
2. The framework leads to noticeable improvements in image generation, as demonstrated by the enhanced performance metrics (e.g., FID) across different datasets like CIFAR-10 and ImageNet-32.
3. The comprehensive empirical evaluation provides valuable insights into the impact of different variance schedules on model convergence and sample quality.

### Weaknesses
1. The proposed framework introduces complexity by requiring a detailed understanding of probability distributions (CDFs, PDFs) and variance schedules, which may be difficult for some practitioners and impact its applicability. While the rationale approach is novel, it may be challenging for users to easily select or engineer appropriate rationales in real-world applications, especially without closed-form solutions for some CDFs. The reliance on numerical approximations for the inverse CDF, while practical, introduces potential inaccuracies, particularly in regions where the PDF changes rapidly. This could lead to instability or suboptimal performance in certain scenarios.
2. In some cases, such as training with the squared L2-norm rationale, the model showed overfitting on smaller datasets (e.g., CIFAR-10), which could be problematic for practical use in certain domains or tasks. The tendency to overfit with the squared L2-norm rationale suggests a potential sensitivity to the dataset size and complexity, requiring careful tuning of regularization parameters or alternative rationale choices for different datasets. This limits the general applicability of the proposed method.
3. Some of results shown in section 4 results seem not statistical significantly different if we consider its variance, for example in table 1 and table 2. Also in Figure 2 (b), the 3rd plot, there is extremely small difference among V2,  squared L2 sampling, normal sampling; and their superiority order change as number of optimization step increase. The lack of clear statistical significance in some results raises concerns about the robustness of the findings. The observed variability in performance across different sampling methods and optimization steps suggests that the conclusions drawn from these experiments may not be universally applicable.
4. some typos: row 132, "defintion"; row 478 has " 1×, 2×, 2×, and 2× the base feature-size": not sure if this is expected.

### Questions
1. What are the computational costs associated with using more complex rationales that do not have closed-form inverse solutions? How does this impact scalability for large-scale training or real-time inference?
2. Can the performance improvements in FID be sustained across a wider range of datasets, particularly those that are more challenging or less well-suited to the proposed variance schedules?

### Soundness
2

### Presentation
2

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
This study introduces a new framework for understanding and designing variance schedules in score-based diffusion models. It reinterprets variance schedules as being derived from probabilistic rationales, where the variance distribution is framed as a CDF with an associated PDF. 
Viewing variance schedules through this probabilistic lens, the approach enables direct engineering of schedules based on specific rationales, offering flexibility beyond traditional methods. 
This design allows for schedules with varied dynamics, such as rapid convergence to zero variance or extended periods in high-variance regions, making it possible to create novel schedules that conventional techniques cannot achieve. 
The framework is showcased using a process "inverse engineering" diffusion by constructing these schedules from the inverse of the CDF, providing a new means of controlling the diffusion process based on targeted variance rationales. 
The method is validated using empirical evaluations on benchmark datasets like CIFAR-10, results show that variance schedules based on different rationales can improve image generation quality, evidenced by superior FID scores.

### Strengths
The manuscript is clear and well-organized. This framework offers a unified perspective that clarifies the relationship between variance schedules and probabilistic rationales, revealing new opportunities to enhance performance in diffusion model applications. The approach is innovative, deriving variance schedules from probabilistic rationales, and is empirically validated on ImageNet-32, effectively expanding the design space for diffusion models.

### Weaknesses
- Minor typo on line 52 r/weighs/weights
- Insufficient guidance on choosing the most effective rationale for specific tasks or datasets
- A sensitivity analysis showing how different parameter values affect model performance or convergence would provide actionable insights for tuning the method in diverse settings.

### Questions
- Refer to the issues noted in the weaknesses section.
- How do computational requirements vary across different rationale-based schedules?
- Is there a recommended method for tuning parameters within each selected rationale?

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
3

### Summary
The paper proposes to design variance schedules (without drift, identical to noise schedules) for diffusion models in terms of a sampling density of the variance.  This sampling density is derived from the introduced rationale (the unnormalized density) and it is shown how the rationale relates to the variance schedule and2q1` can be used in place of the variance schedule.  Loss weighting is shown to be equivalent to selecting a different rationale at training time than sampling time, and the paper demonstrate that using a different schedule at sampling than training time can give improved performance.  The paper analyzes multiple metrics (FID, Inception Score) across two datasets (CIFAR-10, ImageNet-32), including metric measurements as a function of optimization step.

### Strengths
- Provides empirical evidence that separating out the choice of noise schedule at training and sampling time can be useful
- Reasonably large effects on sampling performance are shown as a function of the noise schedule, reconfirming that the choice of noise schedule can substantively alter training and sampling
- Demonstrates rationales without a closed form solution for sigma(t) may still be used, albeit with additional computational expense

### Weaknesses
 - The central concept of the paper, the rationale, is the unnormalized density of the variances.  It's introduced and described in an unclear fashion, yet the resulting computations follow from the 1-1 invertible relationship between sigma(t) and time.  Focusing design on the unnormalized density rather than the sigma(t) function is reasonable, especially given the connection to loss weighting as described in Section 3.4, but the reparameterization is straightforward.

- Many of the theoretical contributions have been used previously.  Including, for example, the ability to use different noise schedules at sampling and training, that loss can be written entirely in terms of SNR sampling (or equivalently variance sampling without mean scaling), and that loss weighting is equivalent to sampling from a different distribution.  The paper could be improved by clarifying what is novel.  

- The empirical results do not appear to lead to strong conclusions about what noise schedule should be used at training or sampling time.  While the conclusion that separating training and sampling schedules is reasonable and interesting, it follows from the pre-existing prevalence of loss weighting schemes.  Further, the variances schedules examined (VE, L2-Norm, and Gaussian) only include one from prior literature which limits the significance of the comparison.  The introduced L2-Norm and Gaussian rationales receive relatively little motivation.

### Questions
- I appreciate that the authors included the standard deviation for IS in their figures and tables.  Given the displayed error bars, are the differences between variance schedules statistically significant? In Table 1 VE, sampling and L2 training is bolded, yet the +- error overlaps quite strongly with other elements in the table.

### Soundness
2

### Presentation
2

### Contribution
2
