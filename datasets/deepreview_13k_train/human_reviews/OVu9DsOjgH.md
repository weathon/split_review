# FEDNET: FREQUENCY ENHANCED DECOMPOSED NETWORK FOR OUT-OF-DISTRIBUTION TIME SERIES CLASSIFICATION

- Decision: Reject
- Scores: 5, 5, 6, 5, 5

## Abstract
Time series classification is a crucial task with widespread applications in various fields such as medicine and energy. Due to the non-stationary property of time series, its data distribution will change over time, which makes it challenging for models to generalize to the out-of-distribution (OOD) environment. However, limitations persist in the current research on OOD time series classification, particularly the absence of a unified consideration addressing both domain distribution shift and temporal distribution shift. To this end, we view the time series distribution shift from the frequency perspective and propose a novel method called Frequency Enhanced Decomposed Network (FEDNet) for OOD time series classification. FEDNet utilizes frequency domain information to guide the decomposition of time series and further eliminates domain shift and temporal shift, it then obtains domain-invariant features for adapting to OOD data. Finally,we provide theoretical insights of FEDNet to validate its superiority for OOD time series classification. Comprehensive results on synthetic and real-world datasets demonstrate that FEDNet achieves state-of-the-art performance in OOD time series classification tasks, surpassing previous methods by up to 7%.Our code is available at https://anonymous.4open.science/r/FEDNet-743E

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel approach (FEDNet) for out-of-distribution (OOD) generalization in time series classification by leveraging frequency decomposition. FEDNet decomposes time series data into two components: a time-deterministic part, which is stable across different domains, and a time-stochastic part, which captures time-dependent variations.

### Strengths
- The paper presents an interesting and potentially impactful approach to OOD generalization in time series classification using frequency decomposition.
- The frequency-based separation into time-deterministic and time-stochastic components is theoretically motivated and could offer a meaningful advancement for handling domain and temporal shifts.
- The authors conduct experiments across multiple datasets and compare FEDNet with a wide range of baseline methods, demonstrating its potential strengths in OOD scenarios.

### Weaknesses
 - The authors claimed that traditional IRM-based domain generalization methods are "not applicable" to time series data. I find this statement inaccurate. They could be applicable but suboptimal.


- The definition of temporal distribution shift (def 3) is unclear. It is not clear why or how different temporal positions in the raw data imply different distributions. It is quite normal the timesteps are different. It should rather be on the temporal segment level.
- Also, definition 4 introduces the connection between temporal shifts and frequency shifts, but the reason why temporal shifts inherently lead to frequency shifts is not clear for me. 

- Wold’s Theorem is the basis for separating deterministic and stochastic components, but the connection to FEDNet is weakly established. The decomposition itself is mentioned without context on why Wold’s Theorem specifically supports this approach for OOD time series classification.

- Also, using Hilbert space and Bochner’s theorem is poorly integrated. The authors mentioned that "we can transform such data into a Hilbert space" without explaining why this transformation is needed or how it benefits the model. If Bochner’s theorem and Hilbert space are central to the method, they need more justification and background.

- There are some issues with the usage of notations. For example, in Equation 3, terms like ωλ and λ-th frequency component are introduced without any definition, and their role in the decomposition is unclear. Similarly, the notation for masking (Mask [S_α]) lacks detail.
- Also, λ is reused again in Eq. 13 as a hyperparameter, causing an inconsistency issue.
- I find that variational inference to disentangle domain-invariant and domain-specific features in the time-deterministic block is ok. However, the explanation lacks clarity on how this disentanglement process specifically aids in handling domain distribution shifts in OOD classification. 
- In Proposition 4.1, it is not clear how frequency decomposition leads to time-deterministic and time-stochastic components that address OOD challenges.

- It would be great if the authors could study the impact of frequency filter masking levels to assess the impact of different frequency filtering thresholds and the masking operation in isolating stable (time-deterministic) components.

- The authors observe that the coefficient of variation is lower for time-deterministic components than for time-stochastic components. However, they do not discuss the implications of this finding in enough depth.

- The authors state that removing the time-stochastic block has only a "small effect" on performance (which is also clear from the ablation study). Does this mean that this component is less crucial and adds extra unnecessary computations?

- Page 3, sentences 109 to 112 are not clear.
- The authors have an issue with the named citation, which causes a readability issue. Note that ICLR template has several ways of citations. Check the difference in the output of these two statements.
     - Domain Generalization \cite{wang} is a difficult … -->  Domain Generalization (Wang et al. 2022a) is a difficult …
     - \citep{athor_x} mentioned that DG is a difficult … --> Wang et al. (2024) mentioned that DG is a difficult …

Use the first when you want just to cite. Use the second when you want to include the author's name in the text.

### Questions
- The authors need to revise:
    - the motivations
    - the definitions
    - the clarity of the writing

based on the above comments.

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
The paper proposes a novel method from the frequency perspective, FEDNet. The paper identifies the limitations of the IRM-based approach for domain generalization in time series classification tasks. To address this, the proposed FEDNet method utilizes frequency domain information to decompose time series into stable features and applies filtering and denoising techniques from a frequency domain perspective. This approach mitigates the distribution shift in sequence data to some degree. The experiments demonstrate that FEDNet achieves state-of-the-art performance in OOD time series classification tasks.

### Strengths
* The paper examines the issues associated with traditional IRM algorithms for time series data and explores out-of-distribution (OOD) time series classification from a frequency standpoint.

* The paper decomposes time series into two components: time-deterministic and time-stochastic, distinguishing the temporal distribution based on frequency information.

* The experiments show that the proposed frequency information is effective and the frequency component exhibits stability to temporal distribution shift.

### Weaknesses
 * The key motivation of the paper seems weak because temporal distribution shift and frequency distribution shift actually consider the same data distribution shift from different perspectives. The benefits of approaching the distribution shift from the frequency view are unclear. In addition, the paper argues that the temporal distribution shift is influenced by the window division. However, to the reviewer, increasing the window size might help mitigate this shift, as it could provide a more stable representation of the data over time.
  
* The paper provides two schemes for constraint loss, but no experiments are designed to compare them. The proposed method also involves multiple different loss functions, it is not clear how to balance them in the model optimization.

* The baseline method ERM algorithm actually demonstrates a very competitive performance, which further weakens the motivation of the paper. The adopted datasets in the experiments lack diversity since they only include the human activity datasets.

* In the time-stochastic block, a two-layer transformer encoder is used with a patch length of 16 and a hidden size of 512. However, as shown in Figure 4, such a complex module only brings limited performance gains, which questions the necessity of such complexity. Besides, the symbols are not clearly defined, such as $x_p$ in Eq. 11 and there are also labeling errors in Table 4.

### Questions
See the weaknesses.

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
4

### Summary
This manuscript presents a new approach to improving domain generalization in deep neural networks. The authors introduce FEDNet, a model designed to enhance frequency-based generalization capabilities, focusing on its application to time series classification. The paper thoroughly evaluates the performance of FEDNet across multiple synthetic and real datasets, including Opportunity, HHAR, UCIHAR, and UniMiB-SHAR, comparing it against baseline methods like VREx, GroupDRO, ANDMask, and others of different flavors.

### Strengths
S1. Overall, this paper is well-written and easy to follow.

S2. The design intuition of this paper, i.e., isolating the sift-relevant components to the time-deterministic block only, makes sense and demonstrates its advantage in empirical evaluations.

### Weaknesses
W1. The connection between the two major components, i.e., (1) the frequency-domain decomposition and (2) the sift-relevant deep architecture, is not well-justified in the paper. If my understanding in S2 (which I just realized after reading the whole methods section) in the design target of the authors, I would suggest the authors to revise the paper and clearly motivate this. The paper lacks a clear explanation of why separating the time series into deterministic and stochastic components, and then processing the deterministic part with a specialized architecture, is beneficial for domain generalization. Specifically, the paper does not adequately explain why the frequency-domain decomposition is expected to isolate domain-specific information into the deterministic component, and why this isolation is crucial for improving generalization. A more detailed explanation of the theoretical underpinnings of this approach is needed.

W2. There are some minor presentation ambiguity and revision suggestions:

W2-1. The equation in line 152 seems a bit weird to me, P(x_i, y_i) and P(x_j, y_j) are the probabilities of two individual examples, while P^Dk(x, y) is the probability distribution of the entire subset D_k. These two cannot be directly compared. The notation used in this equation is confusing and does not clearly define the relationship between individual sample probabilities and the overall distribution of a domain. The paper needs to clarify how these probabilities are related and why this comparison is meaningful in the context of domain generalization.

W2-2. It would be very useful if the authors can briefly summarize the impact of Proposition 4.1 in the beginning of Section 5.4. This should include what are introduced (the per-domain constraint) in this paper and how Equation 15 is realized in FEDNet. The paper should provide a more intuitive explanation of the theoretical contribution of Proposition 4.1 and how it translates into the practical implementation of FEDNet. Specifically, the authors should clarify how the per-domain constraint is enforced and how it contributes to the overall goal of domain generalization.

### Questions
Q1. Despite I agree that the domain/distribution/etc sift information should be more reflected in the time-deterministic decomposed part of the time series, will these sifts also influence the time-stochastic part of the series?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a significant advancement in handling OOD time-series classification by providing a unified framework that considers both types of distribution shirts, domain and temporal.

The frequency-based approach appears to be particularly effective in capturing invariant features that generalize well to OOD scenarios. 

The main novelty of FEDNet is to use frequency information to guide the decomposition of time-series data. By separating deterministic and stochastic components, it can be better identify and leverage invariant features that remain consistent across dirrerent domains.

### Strengths
- The FEDNet is a novel approach to address challenges in out-of-distribution time-series classification using frequency domain information for feature decomposition. Unlike existing methods that primarily focus on the time domain, FEDNet uses both frequency and time domains, guided by theoretical insights from Wold’s Theorem.
- This paper is supported by empirical results through experiments.
- Theoretical insights with time-deterministic and time-stochastic components.

### Weaknesses
There are a few unresolved clarifications in the question below.

- The challenge presented in Figure 1 is unclear. It would be helpful to explicitly indicate the specific problem being targeted, such as domain shift or temporal distribution shift, and the key solution proposed. Additionally, clarifying why the frequency domain is used and why the decomposition into deterministic and stochastic components is necessary would improve understanding. The current description lacks the necessary detail to understand the motivation behind the approach. For example, it is not clear if the temporal distribution shift is due to changes in the underlying generating process or simply due to sampling variations.
- It is unclear why deterministic features undergo the top-k process and why stochastic features undergo both the top-k and masked frequency processes. A more detailed explanation or a visual diagram illustrating these processes would be beneficial. The rationale for applying different processing steps to deterministic and stochastic features is not well-justified. Specifically, why is masking applied only to stochastic features after the top-k selection? A more detailed explanation of the masking process and its impact on the extracted features is needed.
- Please provide a clearer rationale for dividing the stochastic and deterministic features in the frequency domain. A brief theoretical justification about this necessity or empirical evidence linking frequency domain characteristics to the properties of time series data would strengthen the argument. The paper needs to elaborate on the theoretical underpinnings of separating deterministic and stochastic components in the frequency domain. It is not clear what specific properties of time series data justify this separation and how it relates to the goal of out-of-distribution generalization. For example, are there specific frequency bands that are more indicative of deterministic or stochastic behavior?
- In the performance comparison section, it is noted that FEDNet is not the best across all datasets. Could you provide an analysis of the conditions or characteristics of datasets where FEDNet does not outperform other methods? Discussing potential limitations or specific scenarios where other methods are superior would provide valuable insights. The paper should include a more detailed analysis of the datasets where FEDNet underperforms. Are there specific characteristics of these datasets, such as the length of the time series, the number of classes, or the nature of the domain shift, that might explain the performance differences? A more thorough investigation of these factors would be beneficial.

### Questions
- The challenge presented in Figure 1 is unclear. It would be helpful to explicitly indicate the specific problem being targeted, such as domain shift or temporal distribution shift, and the key solution proposed. Additionally, clarifying why the frequency domain is used and why the decomposition into deterministic and stochastic components is necessary would improve understanding.
- It is unclear why deterministic features undergo the top-k process and why stochastic features undergo both the top-k and masked frequency processes. A more detailed explanation or a visual diagram illustrating these processes would be beneficial.
- Please provide a clearer rationale for dividing the stochastic and deterministic features in the frequency domain. A brief theoretical justification about this necessity or empirical evidence linking frequency domain characteristics to the properties of time series data would strengthen the argument.
- In the performance comparison section, it is noted that FEDNet is not the best across all datasets. Could you provide an analysis of the conditions or characteristics of datasets where FEDNet does not outperform other methods? Discussing potential limitations or specific scenarios where other methods are superior would provide valuable insights.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes a method called FEDNet for out-of-distribution (OOD) time series classification. FEDNet extracts the information from frequency domain to decompose the time series into time-deterministic and time-stochastic components, and obtains the domain-invariant features for OOD data. By presenting both theoretical  and experimental insights, the authors claims the superiority of FEDNet for OOD time series classification.

However, the mathematical formulation (e.g., which references their definition relies on) is rather confusing, and it is hard to justify the authors' claim. But the results and their proposal are interesting.

### Strengths
(1) By specifying the notions of domain,  temporal, and frequency distribution shift, the paper addresses the issues of inconsistent distribution between time series from different domains and a solid analysis is provided for an insight into the improvement of OOD time series classification tasks. 

(2) The experiments are conducted comprehensively along with well-illustrated insights. 

(3) The proposed schemes of constraint loss for learning domain-invariant and domain-specific space is novel.

### Weaknesses
(1) It is not clear what are the shortcomings of the method. For example, to what degree of noises in time series can FEDNet can tolerate (still perform well)?  Specifically, the paper lacks a rigorous analysis of the method's sensitivity to various types of noise, such as additive white Gaussian noise, impulsive noise, or colored noise. It is unclear how the frequency decomposition is affected by these noises and whether the domain-invariant features remain robust under noisy conditions. Furthermore, the paper does not discuss the limitations of the method when the time series are corrupted by missing data, which is a common issue in real-world applications.

(2) Just suggestions typos: the first letter in line 239 should be capitalized.

(3) The ablation study only concerns the constraint loss, study on time-stochastic block is lacking. Would be nice to explain more empirically/theoretically on how time-stochastic block actually contributes the performance compared to the other model components. The paper does not provide a detailed analysis of the contribution of the time-stochastic block, particularly in comparison to the time-deterministic block. It is unclear whether the time-stochastic block is essential for the performance gains or if similar results could be achieved with a simpler approach. The ablation study should also include an analysis of the impact of different parameters of the time-stochastic block, such as the patch size and stride, on the overall performance.

### Questions
(1) What are the disadvantages of the method? It is not clear when the method will fail. 

(2) How is the performance for general data instead of OOD data compared to existing SOTA methods?

(3) What is the time complexity for learning the time deterministic and stochastic features? e.g., space complexity and any potential trade-offs between computational requirements and performance gains compared to existing methods?

### Soundness
2

### Presentation
2

### Contribution
2
