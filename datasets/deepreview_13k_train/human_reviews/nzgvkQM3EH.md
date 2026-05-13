# Identification of Nonparametric Dynamic Causal Model and Latent Process for Climate Analysis

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
The study of learning causal structure with latent variables has advanced the understanding of the world by uncovering causal relationships and latent factors. However, in real-world scenarios, such as those in climate systems, causal relationships are often nonparametric, dynamic, and exist among both observed variables and latent variables. These challenges motivate us to consider a general setting in which causal relations are nonparametric and unrestricted in their occurrence, which is unconventional to current methods. To solve this problem, with the aid of 3-measurement in temporal structure, we theoretically show that both latent variables and processes can be identified up to minor indeterminacy under mild assumptions. Furthermore, we establish that the observed causal structure is identifiable if there is generation variability, roughly speaking, the latent variables induce sufficient variations in generating the noise terms, by the established functional equivalence. The primary idea of this framework is to learn causal representations from causally-related observations, and subsequently address this problem as a task of general nonlinear causal discovery. Based on these theoretical insights, we develop an estimation approach simultaneously learning both the observed causal structure, latent representation, and latent Markov network. Experimental results in simulation studies validate the theoretical foundations and demonstrate the effectiveness of the proposed methodology. In the climate data experiments, we show that it offers a powerful and in-depth understanding of the climate system.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors proposed an estimation framework named NCDL to identify the latent causal variables, the structures among them, and the observed causal DAG, assuming that the temporal structure of the data follows a 3-Measurements Model for the climate system. They establish the conditions required for the identification of latent variables, enforcing sparsity on the latent Markov network.

### Strengths
1. The proposed framework aims to address a realistic problem in the climate system using a novel setting, the 3-Measurements Model.

2. The framework of the paper is straightforward, and the paper is well organized.

3. There are theoretical guarantees for the identifiability of the latent Markov network and the observed DAG.

4. The proposed framework has been applied to a series of simulations and a case study.

### Weaknesses
1. It is unclear what the motivation is for using the 3-Measurements Model instead of an $n$-Measurements Model with $n \neq 3$. Could you provide a brief explanation of why the 3-Measurements Model was chosen over other options, and how it specifically relates to climate system analysis. It would be helpful to understand the theoretical underpinnings of this choice, particularly in the context of identifiability. For instance, are there specific conditions under which a 3-measurement model is guaranteed to be identifiable while models with more or fewer measurements are not?

2. The motivation and limitations of the proposed setting are unclear. There seems to be no time-lag effect among $x_{t-1}, x_t, x_{t+1}$. Could you clarify the implications of not including time-lag effects between the observed variables, and how this might impact the model's applicability to real-world climate systems. Many climate phenomena exhibit lagged effects, and it is unclear how the model would perform in such scenarios. A discussion of the assumptions made about temporal dependencies is needed.

3. In Equation 2, $pa_{x_t}(x_{t,i})$ only includes parents $x_{t,j}$, where there is no time lag in $t$. Does this mean that the parent of $x_{t,i}$ is restricted to instantaneous cases in the observed space? If so, could you elaborate on the details in comparison with constraint-based methods, which allow for multiple time lags for observed variables but do not yield time-lagged causal structure among latent variables? The restriction to instantaneous effects seems limiting, and a more detailed comparison with existing methods is necessary.

### Questions
1. Could you explain the statement in line 122 that $x_{t-1},x_{t}, x_{t+1}$ are different measurements of $z_t$?

2. In Figure 3, there are two $Z_{t-1}$; is this a typo?

3. Where is the starting point of the framework visualized in Figure 6? Could you briefly summarize the framework based on Figure 6?

4. In the experiment, is there a specific reason for choosing PCMCIZ as a baseline instead of LPCMCI, which allows for latent variables?

5. Could you explain the definitions of $pa_{z_{t-1}}(z_{t,i})$ and $pa_{z_t}(z_{t,i})$?

6. Could you briefly explain what the inputs are and what estimations/DAGs are obtained from the model?

7. What does the estimated DAGs look like in terms of the dimension of the observed variables? Are the estimated DAGs a full-time causal graph or a summary causal graph?

8. In Table 3, is there a reason why the metric for the Independent and Sparse cases is MCC while the metric for the Dense case is $R^2$? Can all three cases be evaluated using both metrics?

9. Could you also use F1, recall, and precision as metrics in the comparison shown in Figure 7?

10. Are you assuming that there is no causal effect from future variables to past variables?

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
In this paper, the authors consider a general setting where causal relations are nonparametric in  climate systems. Using  three measurements in temporal structure,  the paper  shows that both latent variables and processes can be identified up to minor indeterminacy. the authors  proved  that the observed causal structure is identifiable. They also develop a  very nice procedure, which can simultaneously learn both the causal structure and latent representation. They conduct an extensive experiment, which demonstrates the  usefulness of the proposed  method.

### Strengths
The paper proposed the innovative approach, which  offers a powerful and in-depth understanding of climate system. The paper established the theoretical results of the  proposed methodology, and therefore setted up the   solid foundations  in real-world scenarios, including climate systems. Real data analysis demonstrated the impact of the new methods.

### Weaknesses
The main concern to the paper is a presentation. In many places the meaning of sentences is vague.   It is very difficult to understand the meaning. It is better to elaborate it  and make sentence shorter.



### Questions
I have several comments and suggestions for the authors to address.


1.  It is of interest for the authors to compare the computational cost of proposed method with existing methods in the experiments. Some metrics of computational cost (e.g., runtime, memory usage) are considered  for comparison.

2.  On page 9, line 475 of Table 3, I am not clear to the  meaning of bold type of fonts.  It is helpful for the authors to  give an illustration. Consider explaining the meaning of the bold font in Table 3 to improve the clarity. 

3.  The presentations are not clear to us. In  in real-world scenarios, such as those in climate system. In the paper,  many places  are confused to me.  There are exampes below for the authors to improve clarity. 

4.  There are  many typos, grammatical errors, etc. spotted in the paper. Please proofread and check it carefully.

Page 2, line 060, "e.g." -> "e.g.,".

Page 2, line 066, "can" -> "to".

Page 2, line  071, "sparsity" -> "a sparsity".

Page 2, line 099,  ", thus" -> ". Thus".

Page 3, line 124, "Appx" -> "Appendix".

Page 3, line 136, "denotes" -> "denote".

Page 4, line 190,  add  ".".

Page 4, line  214, "e.g." -> "e.g.,".

Page 5, line 216,   hat is "if to".

Page 6, line 281, "proof" -> "a proof".

Page 7, line 365, "12" -> "(12)".

Page 7, line 377, add   ".".

### Soundness
3

### Presentation
1

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
The work introduces a nonparametric framework for identifying causal relationships in climate data, addressing the complex interactions between latent variables and observed data. It advances a methodology that integrates latent variable identification and causal inference in dynamic environments.

### Strengths
1.This work introduces a new framework of nonparametric dynamic causal models and, by extending the application of nonlinear independent component analysis (ICA), proposes a novel approach for identifying latent causal relationships in complex systems.

2.The NCDL framework in this paper demonstrates strong performance across various experimental settings, including applications in climate data, showcasing the model's adaptability and robustness.

3.The paper is well-structured, with clear divisions into theoretical analysis, model framework, and experimental validation, presenting a logical flow. However, given the study involves multiple complex concepts, such as equivalence transformations and nonlinear independent component analysis, certain theoretical derivations and symbol definitions may seem challenging for non-specialist readers. Some figures and formulas also lack sufficient explanation, which might affect readers' understanding.

### Weaknesses
1.The paper involves numerous symbols and matrix operations (e.g., in Definition 3.4 and Equation (5)), but some symbols lack clear explanations. It is recommended to define each symbol's meaning the first time it appears to avoid ambiguity.
    
2.Although the paper compares the performance of various existing methods, the experimental comparisons in Section 5 on constraint-based methods (e.g., FCI, CD-NOD) and temporal representation learning methods do not further explain why the NCDL method outperforms them.

3.Could you provide details on the hyperparameters $\alpha$ and $\beta$ used in your experiments' loss function? How were these hyperparameters chosen, and did you observe any impact on performance from varying these values?
    
4.Although Figure 6 shows the overall structure of the NCDL model, the module arrangement is complex and may be difficult to understand by visualization alone. It is recommended to provide a concise explanation of each module’s function in the caption or describe each module's specific role in the text, especially the interactions among the "Encoder," "Decoder," and "Prior Network."
    
5.Table 4 appears not to have been referenced or discussed in the main text.
    
6.The "Assumption Ablation Study" in Section 5.1 does not provide sufficient explanation of parameter choices, which may hinder the reproducibility of the experiments.
    
7.The conclusion mentions that future work could address performance degradation in high-dimensional data, but it does not provide specific directions or solutions. It is suggested to further discuss possible research paths that could be explored based on this issue.
    
8.In line 494, "Directed Acyclic Graph (DAG)" could be simplified to "DAG" since it was already defined in line 120.

### Questions
N/A

### Soundness
3

### Presentation
2

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
The paper focuses on uncovering nonparametric dynamic causal structures and latent processes within complex systems like climate data, where both observed and unobserved (latent) variables interact through nonlinear relationships over time. The study introduces a comprehensive framework to identify and analyze these hidden causal processes under various assumptions, even in cases with nontrivial dynamics. The authors present a theoretical framework for identifying latent variables and causal structures within climate data, establishing conditions under which these variables can be detected when they induce significant variability. Through the novel Nonparametric Causal Discovery and Learning (NCDL) model, an extension of nonlinear Structural Equation Models (SEM) adapted for dynamic, time-based dependencies, they reframe SEM within a nonlinear Independent Component Analysis (ICA) structure to enhance causal identification. Validation on synthetic and CESM2 climate data demonstrates that NCDL outperforms traditional methods like FCI and PCMCI in accurately identifying latent variables and their relationships. This methodology, applied to sea surface temperatures and related climate variables, effectively identifies underlying factors such as CO2 levels and ocean currents, advancing insights into climate dynamics.

### Strengths
By introducing the Nonparametric Causal Discovery and Learning (NCDL) framework, the authors extend nonlinear Structural Equation Models (SEM) into a dynamic setting, embedding time-based dependencies in a way that transforms SEM into a nonlinear Independent Component Analysis (ICA) model. To the best of my knowledge, this approach is novel. Moreover, I also find the application of this framework to climate-specific variables, such as sea surface temperatures and CO₂ levels, very interesting. Both the theoretical and empirical contributions of this submission are sound. The authors provide identifiability results based on a set of assumptions, such as Functional Faithfulness. This theoretical contribution is complemented by comprehensive experimental validation across synthetic and real-world datasets, specifically with climate data from the Community Earth System Model Version 2 (CESM2). By benchmarking their method against existing approaches like Fast Causal Inference (FCI) and PCMCI and showing consistent improvements, the paper provides strong evidence for the superiority of their approach. Overall, this submission is overall well-written and easy to follow. Furthermore, I believe that this contribution is significant to the field of Causal Inference, due to the novelty of the proposed framework. Furthermore, the application to climate analysis is broadly relevant.

### Weaknesses
The main weakness of this work is the functional faithfulness assumption, which, to the best of my understanding, is essential to prove identifiability. Although the analogous concept of causal faithfulness has been extensively used in the literature, in my opinion these assumptions are restrictive. Furthermore, it is unclear why a dataset should exhibit functional faithfulness and how it can be verified from samples. Specifically, the assumption that a zero derivative in the Jacobian implies no causal edge, and a non-zero derivative implies a causal relation, is a strong condition that may not hold in many real-world scenarios. The paper does not adequately address the potential for non-linear relationships where a derivative might be zero at a particular point or region, yet a causal relationship exists. This is particularly concerning in complex systems like climate data, where interactions are often highly non-linear and may exhibit such behaviors.

### Questions
How does functional faithfulness impact your results? 
Why is it natural to assume functional faithfulness in this context? 
Is is possible to verify this assumption from samples? 
Can you discuss potential limitations or scenarios where functional faithfulness may not hold?
What is the relationship between functional faithfulness and other common assumptions in the related literature?

### Soundness
3

### Presentation
3

### Contribution
2
