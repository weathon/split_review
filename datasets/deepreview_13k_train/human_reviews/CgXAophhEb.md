# G-AlignNet: Geometry-Driven Quality Alignment for Robust Dynamical Systems Modeling

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
The Neural ODE family has shown promise in modeling complex systems but often assumes consistent data quality, making them less effective in real-world applications with irregularly sampled, incomplete, or multi-resolution data. Current methods, such as ODE-RNN, aim to address these issues but lack formal performance guarantees and can struggle with highly evolving dynamical systems. To tackle this, we propose a novel approach that leverages parameter manifolds to improve robustness in system dynamical modeling. Our method utilizes the orthogonal group as the underlying structure for the parameter manifold, facilitating both quality alignment and dynamical learning in a unified framework. Unlike previous methods, which primarily focus on empirical performance, our approach offers stronger theoretical guarantees of error convergence thanks to the novel architecture and well-posed optimization with orthogonality. Numerical experiments demonstrate significant improvements in interpolation and prediction tasks, particularly in scenarios involving high- and low-resolution data, irregular sampling intervals, etc. Our framework provides a step toward more reliable dynamics learning in changing environments where data quality cannot be assumed.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
The paper proposes a G-align net framework that unifies high and low data modeling in parameter manifolds. The paper provides a theoretical guarantee for the performance and also empirically shows that it can outperform other baselines.

### Strengths
Originality: The idea of leveraging parameter geometry to enhance learning dynamics is novel.

Clarity: The paper includes several math propositions and some clear math derivations, though I cannot verify if they are correct. 

Quality: The paper provides comprehensive results on several datasets for interpolation and extrapolation tasks. Most of the results can be output as baseline models. 

Significance: It looks like the proposed framework could better preserve the geometry of the dataset and could also be used for some control tasks, in addition to better interpolation/extrapolation performance. However, I don't quite understand the significance of the work, and the author is welcome to illustrate it further in the case of the application value for physics systems.

### Weaknesses
The experiment is not always the best. And Figure 3 is confusing. Also training cost is not included for a better comparison. The dataset looks pretty simple so it is hard to evaluate its performance on complex physics dataset.

### Questions
1. In Figure 3, what does the green dot mean? The legend didn't mention the green dot where section 4.2 mentioned it. Moreover, the predictions don't align well with the truth in the rightmost column.

2. In Table 1, G-Align Net doesn't always perform the best. Could you further improve the result or explain it?
 
3. Could you include the training cost for all the algorithms?

4. Can a more complex dataset like weather/fluid dynamics be included?

5. A general setting about the LR and HR data. The paper mentioned that the amount of LR data is far less than that of HR data. However, in my understanding, the LR data is of low quality and is supposed to be easier to get than high-quality data. Could you elaborate on why your LR data is far less than HR data?

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
4

### Summary
This manuscript presents a method to handle data of inconsistent quality for the modeling of dynamic systems. The method draws influence from geometric method of the parameter manifold, in particular weight matrix flow-based geometric representation. Extensive experimental results are presented in the manuscript.

### Strengths
The manuscript tries to address an important problem. The author(s) cited a few practical applications, e.g., the residential electricity consumption and photovoltaic systems, as well as power system event measurement dataset. The paper is written reasonably well. The theoretical contribution appears to be solid.

### Weaknesses
My biggest concern is the motivation and problem definition of the paper. The manuscript appears to address low-quality and high-quality of data, but the author(s) never provided a clear definition how the "quality" of the data is defined. In line 130, it is only indicated that the amount of low quality data can be much larger than the number of high quality data. Near line 273, two potential causes of *low quality* are presented: 1) sensor noise, and 2) the *approximate error* of the Neural ODE. Near line 364, the term *Low Resolution* and *High Resolution* are used. One obvious question is what the relationship between LQ/HQ and LR/HR is. Finally near line 385, it appears that the so-called *LR* data are generated by dropping certain number of data points. The problem definition gradually downgrades from *Quality of data* to *Rate of data*, to *dropping some data*. Although even with dropping data, it could be a very interesting problem in practice, and the topic is well deserve a treatise, it is not the paper as presented here.

Related to the *quality* of data, the Assumption 1 in line 156 appears very strong. If the problem definition is indeed the data with different and unequal sampling rate, intuitively Assumption 1 holds. If the *quality* of the data is represented not only by sampling rate, but also with sensor noise, Assumption 1 is too strong and can very well be invalid. One counter example I can give is that unless the system is inherently linear, and there is no external forcing terms, then the additive noise to the sensor data may well cause different trajectory.  The consideration of data vs physics for modeling dynamical systems have been discussed in prior publications, especially from the perspective of uncertainties (both aleatoric and epistemic)

### Questions
Reiterate my concerns related to the definition of *data quality*, please consider:

1. Provide a precise definition of "data quality" early in the paper
2. Clarify if and how concepts like resolution, sampling rate, and noise relate to their definition of quality
3. Consistently use terminology throughout the paper when referring to data quality
4. Explain the relationship between the theoretical framework and the experimental setup, particularly how "dropping data points" relates to their notion of data quality

Related to the validity of Assumption 1, please consider:

1. Clarify what aspects of data quality (e.g. sampling rate, noise) are covered by Assumption 1
2. Discuss the limitations of this assumption, particularly for nonlinear systems or in the presence of sensor noise
3. Provide justification for why this assumption is reasonable for their target applications, or acknowledge where it may break down
4. Consider addressing the specific questions about how Assumption 1 holds for nonlinear systems with sensor noise and/or linear systems with external forcing terms

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces G-AlignNet, a model designed to handle heterogeneous dynamics data comprising both high-quality (HQ) and low-quality (LQ) measurements. Despite being sparse and noisy, LQ data shares the underlying dynamics of HQ data, allowing it to be interpolated by appropriately transforming the information from HQ data. 

G-AlignNet achieves this through a time-dependent parameter flow governed by a Neural ODE for the orthogonal group. Particularly, G-AlignNet interpolates the parameter flow of LQ data by orthogonally (isometrically) transforming that of HQ dynamics. This orthogonal transformation ensures that the geometry of the parameter flow of LQ data remains invariant to that of HQ data. The constructed parameter flows for HQ and LQ data are then applied to either the RNN, INR, or another NODE to forecast the data dynamics (i.e., the main flow). 

The authors present some theoretical properties of G-AlignNet, such as an error bound, and validate the model across various synthetic and real-world benchmarks.

### Strengths
This paper is well motivated and interesting. It is important to address the heterogeneous situations of LQ and HQ in real-world scenarios. 
***
Additionally, this paper is quite novel. Although the use of parameter flow with orthogonal groups is a structure already proposed in [1], applying it to LQ data imputation is, at least to me, very interesting. 
***
The authors evaluated G-AlignNet on various real-world data, demonstrating that it generally outperformed the baseline model.
***
The paper is well written and contains sufficient detail regarding the technical aspects.
***
[1] Choromanski, K. M., Davis, J. Q., Likhosherstov, V., Song, X., Slotine, J. J., Varley, J., ... & Sindhwani, V. (2020). Ode to an ODE. Advances in Neural Information Processing Systems, 33, 3338-3350.

### Weaknesses
I believe Assumption 1 is important, but its current form lacks sufficient support. While it is clear that the observed responses of HQ and LQ (i.e., $x(t)$ and $y(t)$) should have similar dynamical behaviors, it is less obvious why this similarity should implies that the underlying parameter flows (of deep learning models) must also align in shape. Since this is a key assumption underpinning the paper, I believe the authors should support it either theoretically or experimentally.

For example, from a theoretical perspective, could the authors derive an error bound for the LQ prediction results (i.e., the prediction of $y(t)$) by utilizing the invariance of the parameter flow? 

Another suggestion is, could the authors experimentally demonstrate that the parameter flow $\Theta_y(t)$, trained with *the perfect (HQ)* $y(t)$, has an orthogonal relationship with the parameter flow $\Theta_x(t)$ for $x(t)$? This is somewhat an inverse version of the experiment of Figure 3, which shows that the shape matching encourages the better prediction results of the green LR data $y(t)$. Will training with the green *HR data* result in alignment between $\Theta_y(t)$ and $\Theta_x(t)$?

***

It is not a critical issue, but it seems that bolding is incorrect in some tables. For example, in Table 2 under the Load Data's Missing Scenario, the MAPE results show that RNN performs better, but the bolding is currently on G-AlignNet.

***

What are the definitions of $\Theta_0$ and $\Theta_1$? It seems like they might be the initial conditions of the parameter flows, but I cannot find their definitions.

### Questions
- Could the authors derive an error bound for the LQ prediction results (i.e., the prediction of $y(t)$) by utilizing the invariance of the parameter flow? 
- Could the authors experimentally demonstrate that the parameter flow $\Theta_y(t)$, trained with *the perfect (HQ)* $y(t)$, has an orthogonal relationship with the parameter flow $\Theta_x(t)$ for $x(t)$? 
- What are the definitions of $\Theta_0$ and $\Theta_1$?

### Soundness
2

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
3

### Summary
This paper presents a novel method, G-AlignNet, to align the quality between high-quality (HQ) data and low-quality (LQ) data from the geometric perspective. The method directly works on the parameter flows, using orthogonal groups as the underlying structure for the parameter manifold. This method works on data with different qualities.

### Strengths
- Even though I have some concerns about one proposition, the theoretical foundation of this method is still strong. The use of geometry and manifold theory provides a solid framework that offers valid guarantees for the learning process. 
- The method is tested on a series of systems, demonstrating the outstanding performance of the proposed method.

### Weaknesses
To be honest, I am not an expert in manifold. Maybe I am wrong, but based on my understanding and research experience related to Neural ODEs, I think the following issues should be addressed or answered by authors:

- The claims regarding the limitations of Neural ODEs in LQ data are not sufficiently convincing. Specifically, the authors attribute the poor performance of Neural ODEs and their variants on LQ data to an assumption of consistent data quality. However, this explanation lacks depth and fails to convincingly argue why Neural ODEs would inherently struggle with inconsistent data.

  1. **Assumption of Consistent Data Quality**: Based on my understanding of related work and my research experience, Neural ODEs are designed to handle irregularly-sampled time series data due to their continuous nature. This characteristic inherently makes them flexible and adaptive. So I don’t think there exists the assumption of consistent data quality for Neural ODEs and their variants. The authors should provide a more detailed analysis to convince me. Furthermore, the argument that Neural ODEs assume consistent data quality is not well-defined. What specific aspect of Neural ODEs makes this assumption? Is it the continuous-time formulation, the training process, or something else? The authors need to pinpoint the exact mechanism that leads to this limitation.
  2. **References and Support**: The references provided to support these claims do not adequately substantiate the argument. The only relevant reference is [1], mentioned in the related work section, lines 80-81. However, this paper primarily focuses on addressing Neural ODEs' limitations in processing incoming data streams, rather than tackling issues related to data quality. The paper does not delve into the performance of Neural ODEs under varying data quality scenarios, which is the core claim of the authors. Therefore, the provided reference does not support the authors' argument about the inherent limitations of Neural ODEs with low-quality data.

  In conclusion, If this is a limitation identified by the authors, a more detailed explanation and theoretical proof should be provided to justify this claim. Otherwise, The authors should either provide more suitable references that support their assertions. If these claims cannot be supported convincingly, then the motivation of this paper is really unclear.

- I have significant concerns regarding the correctness of Proposition 4, which addresses the approximation error of Neural ODEs:

  1. The proof for Proposition 4 provided in Appendix A.5 is based on [2]. However, that paper mainly discussed the approximation error of PINNs on ODEs. Since PINNs and Neural ODEs are fundamentally different [3, Section 1.1.5, Page 19], it seems inappropriate to derive the approximation error for Neural ODEs based on conclusions about PINNs, unless the authors offer more detailed theoretical justification for this connection. The authors need to clarify how the error bounds derived for PINNs, which typically involve a loss function based on the residual of the differential equation, can be directly applied to Neural ODEs, where the loss function is typically based on the difference between predicted and observed states. The fundamental difference in the training objectives and architectures makes this connection non-trivial.
  2. The approximation error of Neural ODEs is closely related to the training method used. For example, when employing the optimize-then-discretize approach (i.e., the adjoint method, as described in [4]), there is an additional discretization error that must be considered [3, Section 5.1.2.3, Page 99]. The authors do not specify which method they use for training, nor do they account for this discretization error in the proof, which could significantly affect the results. The adjoint method, for instance, introduces errors due to the reverse-mode differentiation through the ODE solver, which can accumulate over time and affect the overall approximation accuracy. This error is not accounted for in the current proof, and the authors need to clarify how this discretization error is handled or if it is negligible in their specific implementation.

- The experimental results appear incomplete.

  1. The authors claim that the proposed G-AlignNet can work with RNNs, INRs and PINNs. Therefore, G-AlignNet applied to these models applied to INRs should be compared with the baselines in all experiments. However, the authors only present results for one version in the tables and figures, leaving the other unreported. It is essential to demonstrate the performance of G-AlignNet with all claimed base models across all experiments to provide a comprehensive evaluation. The absence of results for G-AlignNet with INRs in all experiments raises questions about the generalizability and robustness of the proposed method.
  2. Regarding the extrapolation results in Figure 4, it is unclear why Neural CDE is not included as a baseline. Neural CDEs are highly relevant for extrapolation tasks and have been compared in Table 2, so it would be logical to include them in the figure for consistency and completeness. The omission of Neural CDE in the extrapolation results makes it difficult to assess the relative performance of G-AlignNet against a relevant and competitive baseline, especially since Neural CDEs are designed to handle irregular time series data, which is related to the low-quality data scenario.

- This paper does not clearly explain the problem formulation and experimental settings, as noted in the Questions section.

- The green points in the right Figure 3 are not explained.

### Questions
To be honest, I really think the writing of this paper should be improved. So many things are not explained clearly.

- The problem formulation in the paper requires more clarity, particularly regarding the definitions of HQ and LQ data.

  - I think this paper tries to train the learning model of the form $\boldsymbol{s}(t_i)=\boldsymbol{f}(\boldsymbol{s}(t_{i-1}))$, where $\boldsymbol{s}(t_i)$ is the state for the system. Let’s assume $\boldsymbol{s}(t_i) \in \mathbb{R}^d$. Based on the defintion in line 133-134, $\boldsymbol{s}=[\boldsymbol{x}, \boldsymbol{y}]$, it seems that the authors assume some variables in the state are sampled with high quality, but others are sampled with low quality, meaning that $\boldsymbol{x}\in\mathbb{R}^{d_x}$, while $\boldsymbol{y}\in\mathbb{R}^{d - d_x}$. 

  - However, in lines 151-152, the authors appear to redefine $\boldsymbol{s} = [\boldsymbol{x}, \boldsymbol{y}]$ or $\boldsymbol{s} = \tilde{\boldsymbol{y}}$. So which one is correct? 
  - If the correct definition is $\boldsymbol{s} = [\boldsymbol{x}, \boldsymbol{y}]$, does this imply that the authors are always assuming some variables are sampled with high quality, while others are sampled with low quality?
  - Additionally, if $\boldsymbol{y}$ is just a downsampled version of $\boldsymbol{x}$, which means $\boldsymbol{s}(t_i) = \boldsymbol{y}(t_i)$ or $\boldsymbol{s}(t_i) = \boldsymbol{x}(t_i)$ it raises the question of why we would use LQ data at all if HQ data $\boldsymbol{x}$ is already available given $\mathcal{N}_y \subset \mathcal{N}_x$.

- The authors should provide a more detailed explanation of experimental settings. 

  - Although the authors have provided citations for each dataset or system used in the experiments, I believe it is still important to introduce the dimensions and size of each system. This additional information would help readers better understand the experimental settings and provide more context for evaluating the results. 
  - Although the authors account for measurement noise in the theoretical analysis, it appears that noise is not addressed in the experimental section. This is particularly evident in Figure 5, where the LR samples align perfectly with the ground truth line, suggesting that noise may not have been considered in the experiments.

- This paper primarily discusses the application of G-AlignNet to RNNs and INRs. Could the proposed architecture also be applied to other common sequence models, such as Transformers or Mambas? I think such discussions can significantly improve the quality of this paper.

### Soundness
2

### Presentation
1

### Contribution
2
