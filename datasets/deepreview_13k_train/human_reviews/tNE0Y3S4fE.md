# Exploring the Design Space of Diffusion Bridge Models via Stochasticity Control

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Diffusion bridge models effectively facilitate image-to-image (I2I) translation by connecting two distributions. However, existing methods overlook the impact of noise in sampling SDEs, transition kernel, and the base distribution on sampling efficiency, image quality and diversity. To address this gap, we propose the Stochasticity-controlled Diffusion Bridge (SDB), a novel theoretical framework that extends the design space of diffusion bridges, and provides strategies to mitigate singularities during both training and sampling. By controlling stochasticity in the sampling SDEs, our sampler achieves speeds up to $5 \times$ faster than the baseline, while also producing lower FID scores. After training, SDB sets new benchmarks in image quality and sampling efficiency via managing stochasticity within the transition kernel. Furthermore, introducing stochasticity into the base distribution significantly improves image diversity, as quantified by a newly introduced metric.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Stochasticity-controlled Diffusion Bridge (SDB), a generalized diffusion bridge-based model framework that enables flexible control of stochasticity. Specifically, SDB considers stochasticity in 1) the transition kernel, 2) sampling SDE, and 3) the base distribution. This is achieved by designing a noise schedule for the transition kernel, regulating the drift term in the sampling SDEs, and adding noise into the base distribution. The paper also proposes a score reparameterization and a discretization sampling scheme to mitigate singularity. Experiments show that the proposed SDB has better image quality, efficiency, and diversity than other baselines in the image-to-image translation task.

### Strengths
1. The proposed SDB framework provides a more generalized view of diffusion bridge-based models (DBM). Under the framework, this work highlights the importance of randomness in DBM. It shows that carefully selected randomness in sampling SDEs, transition kernel, and the base distribution can significantly improve sampling efficiency, image quality, and diversity.

2. The proposed score reparameterization and discretization sampling scheme by design is more likely to avoid singularity and instability in training and sampling.

3. In experiments, the proposed method SDB notably outperforms previous DBM methods in quality, efficiency, and diversity, as evaluated by several quantitative metrics.

### Weaknesses
1. The main issue of this paper is insufficient evaluation. First, the ablation study is not thorough enough. It is not shown how different choices of $\gamma_{max}$ affect the results. In addition, there's no ablation study to show the effects of the proposed reparameterization and sampling algorithm. Thus, it is unclear how much gain each technique contributes to the final model.  
Regarding the verification of reparameterization, apart from the normal metrics, I also suggest analyzing the numerical stability during training/sampling to show that the proposed technique indeed mitigates singularity.

2. Qualitative comparison is insufficient. In the main paper, only Fig. 4 shows the qualitative comparison between SDB and DDBM. However, a comparison to other methods such as DBIM should also be provided. I also suggest including DBIM in Table 4 so that the SDB is compared to more than one baseline in terms of diversity.

3. The randomness added to the base distribution lacks further explanation. Why convolving $\pi_{cond}$ with a Gaussian rather than adding Gaussian noise to $\pi_{cond}$? What's the kernel size for the Gaussian?

4. DBIM is not discussed in related works.

Typo: Line 212 ODE -> SDE.

### Questions
The settings of Table 2 and Table 3 are not matched. For example, Table 2 shows that $\eta = 0.3$ is the best, but Table 3 uses $\eta = 1$. The quantitative scores are also not matched for $\eta = 1$ on edges2handbags. Please explain the inconsistency.

### Soundness
2

### Presentation
3

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
This paper introduces the Stochasticity-Controlled Diffusion Bridge (SDB), a framework that enhances diffusion-based generative models by using a flexible, transition kernel-based approach. Unlike standard DDMs, which start from Gaussian noise, SDB can transition between arbitrary distributions, making it more versatile for tasks like image-to-image translation. Key innovations include a Stochasticity Control (SC) mechanism that regulates noise and drift terms, boosting stability, efficiency, and output diversity. Experiments show SDB operates 5× faster than DDBM and achieves an FID score of 0.89 with just five evaluations, setting a new quality benchmark.

### Strengths
1. The paper ensures the sampled distributions adhere to a mathematically sound process. Additionally, the proofs offered for Lemma 1 and Theorem 3 validate that the stochastic control can maintain desired marginal distributions across time

2. The method demonstrates strong performance in preserving alignment and detail within conditional sampling tasks. The model captures and retains critical details between the source and target distributions, resulting in high-fidelity outputs that stay true to the given conditions.

### Weaknesses
1.  The presentation of stochastic control in sections 3 and 4 mixes well-known stochastic process theory with the paper’s innovations, making it challenging to identify what is genuinely novel. Clarifying how the proposed SC mechanism specifically advances the field would help distinguish the paper’s contributions from established concepts.

2. The paper doesn’t clearly demonstrate why the proposed stochastic control outperforms other methods. While several design choices are introduced, their practical advantages and rationale are not sufficiently justified, leaving the reader uncertain about the improvements gained from these specific approaches.

3.The experiments appear simplistic and don’t convincingly support the claims, especially regarding generalization to real-world applications. Additionally, the diversity metric (Average Feature Distance) and image quality metrics could be better validated on more extensive benchmarks to strengthen the results.

### Questions
Is it possible to convert the sampling process into an ODE process by leveraging the Fokker-Planck equation?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The authors introduce the Stochasticity-controlled Diffusion Bridge (SDB), a new theoretical framework that expands diffusion bridge design. SDB mitigates singularities during training and sampling, achieving speeds up to five times faster than the baseline while improving image quality and diversity by managing stochasticity in the transition kernel and base distribution.

Due to my limited familiarity with the field addressed in this paper, it is challenging for me to provide in-depth insights. However, I can offer some feedback from a more application-oriented perspective.

### Strengths
The Stochasticity-controlled Diffusion Bridge (SDB) demonstrates significant improvements in image quality, sampling efficiency, and conditional diversity, establishing new benchmarks in these aspects. Furthermore, the authors' introduction of score reparameterization and specially designed discretization effectively addresses challenges related to singularities.

### Weaknesses
SDS is a crucial loss function in the text-to-3D domain. Could the authors explore similar applications in this paper? It would be beneficial to demonstrate its extension in a 3D context.

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes the Stochastic-controlled Diffusion Bridge (SDB) model to improve the effect of noise generated by SDEs, transition kernel, and base distribution on sampling when the existing Diffusion Bridge models (DBMs) are sampling image-to-image translation. The authors introduce stochasticity control (SC) in three areas—sampling stochastic differential equations (SDEs), transition kernels, and base distributions—to improve sampling efficiency, image quality, and diversity in output. In this process, the paper presents a metric for measuring the diversity of output. The SC mechanism mitigates singularities during training and sampling, and introduces flexibility in design, allowing SDB to outperform existing models like DDBM and DBIM on benchmark tasks, achieving lower FID scores, faster sampling, and improved image diversity.

### Strengths
**1. Existing Model Shortcomings: Identification and Solutions**  
Recognize the limitations of existing diffusion bridge models as stemming from noise introduced during image-to-image translation sampling. The SC mechanism effectively addresses these shortcomings by introducing enhanced flexibility and precise control over the noise at various stages of the diffusion process, thereby mitigating the inherent limitations of conventional diffusion models. 

**2. Experimental Validation**  
The paper provides extensive quantitative comparisons with multiple baseline models, demonstrating superior performance in FID, sampling efficiency, and conditional diversity on I2I tasks.

**3. Expression Reconfiguration**  
The paper introduces score reparameterization and discretization schemes to address stability issues in previous diffusion bridge methods, offering novel insights into stochastic diffusion processes.

### Weaknesses
 **1. Limited Discussion on Computational Overhead**  
Although the model achieves lower FID scores with fewer function evaluations, the added complexity of SC mechanisms (especially in tuning multiple noise schedules) may increase computational overhead. A direct comparison of computational resources (e.g., time or memory) required by SDB versus other DBMs would provide a clearer picture of the trade-offs. Specifically, the paper lacks a detailed breakdown of the computational cost associated with each component of the proposed Stochastic-controlled Diffusion Bridge (SDB) model. While the authors mention the number of function evaluations (NFE), they do not provide a comprehensive analysis of the time spent on operations such as the calculation of the stochasticity control parameters or the score reparameterization. This makes it difficult to assess the practical applicability of the model, especially in resource-constrained environments. A more detailed analysis should include a breakdown of the computational cost of each step, including the time required for calculating $\alpha_t$, $\beta_t$, $\gamma_t$, and $\epsilon_t$, and compare these costs with those of existing DBMs.

**2. Lack of Detailed Analysis on the Contribution of Each Stochasticity Control Component**  
While the authors claim that SC enhances image quality, sampling efficiency, and conditional diversity, there is a lack of detailed analysis on how each component (e.g., SC in the transition kernel, SC in the base distribution) individually contributes to these improvements. Although overall performance gains are evident, the authors have divided Stochasticity Control into three distinct components, yet the extent to which each component contributes to the model's improvement is not adequately demonstrated through ablation studies. The paper would benefit from a more granular analysis, such as ablating each SC component separately and measuring its impact on metrics like FID, sampling speed, and diversity. For instance, the effect of varying the noise added to the base distribution ($b$) should be isolated from the effect of varying the noise in the transition kernel ($\gamma_t$) and the sampling SDEs ($\epsilon_t$). This would provide a clearer understanding of the role of each component and allow for more targeted optimization.

**3. Lack of Clear Design Guidelines for Stochasticity Control**  
The paper introduces various strategies for enhancing performance through Stochasticity Control (SC). However, it lacks clear principles for determining optimal parameters in SC design. For instance, the design of the ϵt value used in SC is largely determined empirically, which complicates the systematic selection of SC parameters suitable for specific tasks. Additionally, the proposed method includes several hyperparameters (e.g.,  αt, βt, γt, ϵt), yet there is no concrete guideline on how these should be chosen. While certain values were empirically set during experiments, it remains unclear how these can be applied in more general cases. To address this, it would be helpful if the authors could provide a sensitivity analysis for these key hyperparameters, showing how performance varies across different settings. Additionally, we suggest the authors share any rules of thumb or heuristics they relied on when selecting these parameters, which would provide practical guidance for applying the method in various contexts. The paper should include a more systematic exploration of the hyperparameter space, potentially through a grid search or other optimization techniques, to provide more concrete guidelines for parameter selection.

**4. Lack of Reliability for the Proposed Evaluation Metric**  
The authors propose Average Feature Distance (AFD) as a metric for assessing diversity. However, there is insufficient analysis to establish the reliability and validity of this metric. To substantiate AFD as a credible measure of diversity, the authors should have demonstrated its application across multiple existing baselines and metrics, thereby enhancing its reliability. In particular, there is a lack of comparative analysis and explanation on how AFD interacts with other evaluation metrics and effectively represents trustworthy conditional diversity. To establish the reliability of AFD, it would be beneficial for the authors to compare AFD scores with human judgments of diversity or apply AFD to datasets with known diversity characteristics. Additionally, case studies illustrating how AFD addresses insights that are missed by similar existing metrics would strengthen its credibility as a measure of diversity.

### Questions
**1. Lack of Theoretical Explanation**  
The various concepts and mechanisms introduced in the paper, such as Stochasticity Control and Score Reparameterization, are not sufficiently clear or intuitively explained. While the mathematical descriptions provide a theoretical foundation, the paper would benefit from a figure or diagram that illustrates how Stochasticity Control interacts with other components of the model. Including a main figure to depict the overall framework and interconnections within the proposed model would greatly enhance readers' understanding of the core concepts.

**2. Purpose of Figure 1**  
Figure 1 aims to provide an intuitive illustration of how the transition kernels in image-to-image (I2I) translation can incorporate noise through the configuration of multiple hyperparameters, as proposed by the authors. However, since the ultimate goal of I2I translation is to transform the source image into the target image, evaluating only the final translated result may suffice. Figure 1 merely demonstrates the progressive addition of noise, making it challenging to discern the specific impact of these parameters. A clearer explanation of the intended purpose of Figure 1 would be beneficial.

I would be willing to consider increasing the rate if clear responses are provided to the points raised in the Weakness and Question sections.

### Soundness
3

### Presentation
2

### Contribution
2
