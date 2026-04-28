# Self-Consuming Generative Models Go MAD

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Seismic advances in generative AI algorithms for imagery, text, and other data types has led to the temptation to use synthetic data to train next-generation models.
Repeating this process creates an 
autophagous (``self-consuming'') loop  whose properties are poorly understood.
We conduct a thorough analytical and empirical analysis using state-of-the-art generative image models of three families of autophagous loops that differ in how fixed or fresh real training data is available through the generations of training and in whether the samples from previous-generation models have been biased to trade off data quality versus diversity.  
Our primary conclusion across all scenarios is that {\em without enough fresh real data in each generation of an autophagous loop, future generative models are doomed to have their quality (precision) or diversity (recall) progressively decrease.}
We term this condition Model Autophagy Disorder (MAD), making analogy to mad cow disease.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates performance degradation of generative models in self-consuming (or autophagous) loops. The paper categorizes three scenarios of self-consuming based on real-world applications. In particular, a new scenario called "fresh data loop" is considered for the first time, where new data comes into the self-consuming loop. The empirical investigation on the scenarios reveals that, while the self-conuming loop tends to couse the degradation of the generative models, we can avoid it if the generative models in the loop continues to be exposed to new data. Also, the paper investigates how sampling techniques for better generation affects the degradation in the loop. It is empirically confirmed that these findings hold for different generative models or datasets.

### Strengths
- The paper is clearly written and easy to follow. Their problem is appropriately formulated in a mathematically sound way.
- In Section3, a toy example of gaussian models is analyzed, which provides a theoretical evidence for their heuristic Claim in Section 2.
- It is predictable but also insightful that the performance degradation in the loop is caused only when using fixed samples over the loop.

### Weaknesses
 - It is unclear what Claim in Section 2 aims for. Although it is proved for a toy model of gaussians, I assume that it is aimed for a hypothesis for general case but the authors seem not to explain such aspects. For example, the claim describes a behavior of the model's parameters, but it is not clear if this behavior is actually observed in practical models. If not, the claim would be overclaimed and somewhat doubtful for general case. Finally note that "Claim" in a paper is usually considerred as to be proven in the paper, not a hypothesis.
- Eq. (2) is totally unclear. Is it a hypothesis or theorem? Where is $WD(n_r, n_s, \lambda)$ defined? If it is just a hypothesis, the author should make it clear in the text. The lack of a clear definition for $WD$ makes it difficult to assess the validity of the equation. Furthermore, the relationship between the variables $n_r$, $n_s$, and $\lambda$ and the Wasserstein distance should be more explicitly stated.
- It is unclear why $n_{ini}$ is considered in the first part of Section 5. How does it relate to the main claims in Introduction? The role of $n_{ini}$ in the experimental setup and its connection to the overall findings are not well-motivated. The authors should clarify how varying $n_{ini}$ contributes to the understanding of the self-consuming loop phenomenon.
- The observation of a phase transition is interesting, but it suddenly appears at Section 5. I recommend to briefly discuss the motivation and the results in Introduction. The sudden introduction of the phase transition without prior discussion leaves the reader unprepared for this finding. A brief mention in the introduction would help to contextualize this result and highlight its significance.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the effect of repetition of the process that generated data of a generative model are included in the training data of generative models of next generation (self-consuming loop).
They categorize possible scenarios to 1. training data are fully generated, 2. training data are partially generated and real data are fixed, and 3. training data are partially generated and real data change.
Theoretical and empirical analyses reveal that scenarios 1 and 2 lead generative models to collapse after some iterations of the loop.

### Strengths
The topic, self-consuming loop, is relevant to the community, as generative models are more and more common and a plenty of generated data are released to the internet. This paper assumes three possible scenarios of the loop and analyzes each of them, which distinguishes this work.
It is also important that the authors discuss how to alleviate the effect of "MAD".

### Weaknesses
Although the authors define the autophagous mechanisms such that "each generative model $\mathcal{G}^t$ is trained on data that includes samples from previous models" (p3), but to my understand, the theory (around eq 1) and the experiments (described in A.1 and A.2 diffusion model) only consider the case that each model $\mathcal{G}^t$ is trained on data generated by $\mathcal{G}^{t-1}$. 
The discrepancy between the definition of autophagous mechanisms and the theory and experiments is worth noting otherwise it diminishes the soundness.

It is also unclear if the empirical results obtained using MNIST are applicable to more complex datasets. MNIST is a relatively simple, low-dimensional dataset where data points are already well-clustered. The behavior of generative models, especially diffusion models, can be significantly different when applied to higher-dimensional, more complex data distributions. The paper does not adequately address whether the observed collapse in performance would also occur in more realistic scenarios with higher-dimensional data.

### Questions
* To my understand, Huang et al. 2022 (cited in p3) considers "synthetic data augmentation", but Hataya et al. 2022 (cited in p3) focuses on the effects of the first loop of synthetic augmentation loops or fully synthetic loops on some downstream tasks, such as classification. Do I misunderstand something?
* Why the authors choose StyleGAN2 with FFHQ and DDPM with MNIST?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work investigates autophagous generative processes, where generative models train on data that includes samples from AI-synthesized data, and identifies a phenomenon termed Model Autophagy Disorder (MAD). MAD refers to the progressive deterioration of both quality and diversity in synthetic data over generations. The presence of sampling bias, common in generative model training, influences the impact of MAD. This paper shows that with enough fresh real data, the quality and diversity of the generative models do not degrade over generations. Additionally, the paper reveals a phase transition in the admissibility of synthetic data in fresh data loops, with excessive synthetic data potentially leading to MADness.  This work also discusses that autophagous loop behaviors hold across a wide range of generative models and datasets.

### Strengths
(1) This paper identifies and addresses a novel issue in the field of generative modeling, the phenomenon of Model Autophagy Disorder (MAD) resulting from autophagous generative processes. This issue, which has not been extensively explored before, carries potential consequences for data quality and diversity in AI systems

(2) The paper exhibits a well-structured and easily understandable presentation. It offers clear definitions, explanations, and visualizations to elucidate the concept.

(3) The study conducts extensive experiments to probe autophagous generative processes across diverse scenarios, encompassing fully synthetic loops, synthetic augmentation loops, and fresh data loops. The inclusion of various generative models, approaches, and datasets enhances the robustness of the findings.

(4) The paper's findings hold practical implications for the training of generative models, especially in situations involving synthetic data. They offer valuable insights and guidance for future model training endeavors.

### Weaknesses
(1) This work would benefit from a dedicated section discussing potential solutions or mitigations for Model Autophagy Disorder (MAD) in the training of generative models. This could enhance the paper's practical utility in the field.

(2) A more in-depth exploration of the broader implications of MAD is expected.  This could involve exploring the impact of MAD in various domains beyond image generation, such as NLP or audio synthesis. Additionally, discussing real-world scenarios and applications where MAD could manifest would make the paper more informative.

(3) To enhance the rigor of the paper, a more comprehensive theoretical framework should be developed to formalize the concept of MAD and its implications. A deeper exploration of the mathematical foundations underlying MAD would contribute to a stronger theoretical basis for the research.

(4) The work lacks a detailed description of the sources or methods used to generate the synthetic data used in this study. Providing specifics on how synthetic data was created for experiments would enhance transparency and reproducibility.

### Questions
(1) Could the authors provide more insights into potential strategies or mitigations for addressing MAD in generative model training?

(2) How might MAD impact domains beyond image generation, such as NLP or audio synthesis? Can the authors hypothesize on potential challenges and solutions in these areas?

(3) The paper discusses the impact of sampling bias (λ). Could the authors provide a more nuanced analysis of how varying levels of sampling bias affect MAD, particularly in terms of quality and diversity?

(4) Could the authors elaborate more on the mathematical foundations of MAD and its implications?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
