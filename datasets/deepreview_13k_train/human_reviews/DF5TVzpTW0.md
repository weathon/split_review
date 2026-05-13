# Detecting and Perturbing Privacy-Sensitive Neurons to Defend Embedding Inversion Attacks

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
This paper introduces Defense through Perturbing Privacy Neurons (DPPN), a novel approach to protect text embeddings against inversion attacks. Unlike ex- isting methods that add noise to all embedding dimensions for general protection, DPPN identifies and perturbs only a small portion of privacy-sensitive neurons. We present a differentiable neuron mask learning framework to detect these neu- rons and a neuron-suppressing perturbation function for targeted noise injection. Experiments across six datasets show DPPN achieves superior privacy-utility trade- offs. Compared to baseline methods, DPPN reduces more privacy leakage by 5-78% while improving downstream task performance by 14-40%. Tests on real- world sensitive datasets demonstrate DPPN’s effectiveness in mitigating sensitive information leakage to 17%, while baseline methods reduce it only to 43%.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on defense strategies against embedding inversion attacks, a type of privacy attack where attackers attempt to reconstruct original sensitive data from its embedding representation. Existing defense methods commonly add noise uniformly across all embedding features. However, this approach is limited in maintaining model performance and is limited in effectively protecting privacy since, ideally, more noise should be directed towards privacy-sensitive features.

To address these issues, the authors first assume and validate that embeddings are composed of both privacy-sensitive and privacy-invariant features. Then, they propose an optimization problem in which a differentiable mask is optimized to isolate privacy-sensitive information within learned embeddings. The optimized mask becomes a tool to detect privacy-sensitive features, and by adding noise to these features, the authors achieve defense against embedding inversion attacks.

### Strengths
1. The method is technically sound, successfully enhances benign accuracy in downstream tasks, and prevents privacy leakage.

2. The hypothesis validated in this paper, that features can be divided into privacy-sensitive and privacy-invariant categories, is quite interesting. Building on this, the idea of using a mask to separate these features is also very novel.

### Weaknesses
1. The paper lacks a formal privacy guarantee. For instance, in methods like LapMech, the authors provide a proof to demonstrate the effectiveness of privacy protection, but this paper lacks such a discussion. Such a drawback raises doubts about the trustworthiness of the proposed method, especially if attackers know the defense mechanism.

2. This defense method requires two datasets, one containing privacy-sensitive data and one without, which necessitates labeling what information as private information. This adds a labeling burden in real-world datasets, as additional annotation is required.

### Questions
1. Is it possible to formulate privacy realized by this framework?

2. It is recommended that the authors consider adaptive attack scenarios to demonstrate that this defense method remains effective even if the privacy protection scheme is exposed to adversaries.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces DPPN (Defense through Perturbing Privacy Neurons), a novel method that protects text embeddings by selectively identifying and perturbing privacy-sensitive neurons. The experiments show the effectiveness of the method.

### Strengths
1. This paper has a clear format, highlighting important keywords throughout the paper.
2. The paper explains the methodology in details.

### Weaknesses
1. Is LapMech a variant of DP? What is the performance comparison with standard DP? The paper can add a new section on this.
2. What is "Downstream" in utility metric? The paper could explain more about how they measure the utility of the method.
3. How do you explain the results in Table 7? Table 7 gives more results of the method than Table 1, and It seems that DPPN does not outperform other defense methods in some datasets.
4. The paper can include some other defense methods in their comparison. Experiments with two baselines are not very convincing.
5. In Sec 4.1, they mention that "Vec2text serves as our primary attack model in subsequent experiments." So it seems that only one attack model is evaluated in the whole paper, making the defense performance not convincing again. Are there any results for other attack models?
6. Only Table 3 shows some results for attack models. However, only privacy metrics are presented. How about the utility metrics?
7. The paper could reorganize some experimental results based on some comments above, making the experiment section better.

### Questions
Please see those in weaknesses.

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
5

### Summary
The paper presents DPPN, a method for defending text embeddings against inversion attacks by selectively perturbing privacy-sensitive neurons. It demonstrates strengths in improving privacy-utility tradeoffs and shows robustness across different datasets and embedding models. However, it also has weaknesses, including the lack of theoretical privacy guarantees and potential challenges in generalizing to new data. Overall, DPPN is a promising approach for privacy protection in text embeddings, but further research is needed to address its limitations and ensure broader applicability.

### Strengths
Strengths:

1. Targeted Defense: DPPN focuses on identifying and perturbing only a subset of privacy-sensitive neurons, which is a more efficient approach compared to perturbing all dimensions of the embedding.

2. Improved Privacy-Utility Tradeoff: The paper demonstrates that DPPN achieves a superior balance between privacy protection and maintaining the utility of the embeddings for downstream tasks.

3. Effective Against Real-World Threats: DPPN shows significant effectiveness in mitigating sensitive information leakage on real-world datasets, such as medical records and financial data.

### Weaknesses
### 1. Personal Information Matching Issue

The DPPN method may not explicitly detail how to accurately match and process personal information. Ensuring accuracy and security, while protecting privacy, requires careful handling. This involves selecting and optimizing exact and fuzzy matching algorithms to provide accurate results without compromising privacy. The method uses a differentiable neuron mask learning framework to detect privacy neurons related to sensitive information. By assessing the importance of each embedding dimension, the top \( k \) dimensions with the highest importance are selected as privacy neurons. Visualizing the proportion of protected private data is necessary. The effectiveness of DPPN relies on accurately identifying and selecting neurons related to privacy information. Inaccuracies in this process may lead to sensitive information leakage. Furthermore, the reliance on Named Entity Recognition (NER) models for identifying PII introduces a dependency on the performance of these models; any PII not recognized by the NER system will not be protected by DPPN. This is a significant limitation, as NER models are not perfect and may miss nuanced or context-specific PII.

### 2. Lack of Theoretical Guarantees

DPPN does not provide theoretical guarantees like Differential Privacy (DP), meaning it cannot quantify the degree of privacy protection or ensure the statistical insignificance of including or excluding a single data point. Adapting DPPN's targeted perturbation method to meet DP standards is challenging, as DP requires perturbing all published data for strong privacy guarantees, whereas DPPN only perturbs a subset of dimensions. The lack of a formal privacy guarantee makes it difficult to assess the robustness of DPPN against sophisticated attacks and to compare its privacy protection level with other methods that offer formal guarantees. The authors should explore how to adapt their method to provide a formal privacy guarantee, such as by incorporating a noise injection mechanism that satisfies DP.

### 3. Challenges in Multilingual and Multicultural Backgrounds

Expressions of personal information vary across languages and cultural backgrounds. It is essential to discuss whether the DPPN method can adapt to and effectively handle these differences. The current evaluation of DPPN is limited to English datasets, and it is unclear how well the method would generalize to other languages and cultural contexts. The authors should investigate the performance of DPPN on multilingual datasets and consider how cultural differences in the expression of personal information might affect the method's effectiveness.

### 4. Real-Time Performance and Computational Cost

The real-time performance and computational cost of DPPN in practical applications are unclear. This is an important consideration for systems that need to process large volumes of data in real-time. The interpretability of the DPPN method is relatively low, potentially limiting its use in scenarios requiring high model interpretability, such as medical diagnosis. While the authors claim that the computational complexity is similar to baseline methods, they do not provide detailed analysis of the runtime overhead of the neuron selection process, which could be significant for large datasets. The lack of interpretability, while partially addressed by the concept of 'privacy neurons', still makes it difficult to understand why certain dimensions are selected and how they relate to the protected information.

### 5. Embedding Methods

The authors use embedding methods like GTR-base, Sentence-T5, and SBERT. It is suggested that traditional methods such as GloVe and Word2Vec be discussed and experimentally analyzed. The authors should also consider the impact of different embedding dimensions on the effectiveness of DPPN. It is not clear if the method is equally effective across different embedding models and dimensions, and this should be investigated.

### 6. Presentation Issues

Table 9 is too large. Using \resizebox \textwidth is not recommended. Table 8: Statistics of datasets. The caption is below the table; the authors should unify the format. Authors can add more related work in the context:
- Private Language Models via Truncated Laplacian Mechanism EMNLP 2024
- Differentially Private Language Models Benefit from Public Pre-training PrivateNLP 2020

The explanations for Figures 1 and 3 are not detailed enough, especially regarding the meaning of arrows and labels. It is recommended that the authors clarify these in the legend.

### Questions
1. What are the benefits of neuron mask learning and direct matching for replacing PII compared to constructing a series of regular expressions to match and transform PII in the corpus?
2. What are the benefits or advantages of the author's method compared to traditional DP-based methods?
3. Could the author fully describe the challenges faced in this research?
4. The author would be greatly appreciated if the code could be made open source and contributed to the community.
5. Six datasets were used in the experiments, but only two datasets' results are shown in the main text. Could the author explain in more detail the reasons for choosing these two datasets?
6. The results in Table 1 show the performance of different methods, but there is a lack of in-depth analysis of these results. It is suggested to add a discussion of the results, explaining why DPPN performs better in these cases.

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
The paper proposes a defense method DPPN to resist against embedding inversion attacks. In contrast to previous methods that add noise on all embedding dimensions, it recognize privacy neurons that contains more sensitive information and only perturbs them. Therefore, it achieve an excellent privacy-utility trade-off. Extensive experiments show that the defense method can protect private information while maintaining the origin semantic information.

### Strengths
Originality: The introduction of privacy neurons and targeted perturbation is innovative, departing from conventional methods that apply noise to all dimensions.

Quality: The conducted experiments are comprehensive. The study evaluates DPPN across six datasets, multiple embedding models, and various attack models, showcasing robust and thorough experimental design.

Clarity: The paper follows a clear structure, with a logical flow from problem motivation to solution, experiments, and results.

Significance: The ability to reduce privacy leakage without sacrificing utility makes DPPN relevant for real-world applications where maintaining both privacy and accuracy is critical.

### Weaknesses
 + The paper does not provide sufficient detail on how parameters $\xi$ and $\eta$ in formulas 3 and 5 are selected during the experiments. Please provide additional information about the selection process. This clarification would help readers understand their impact and ensure reproducibility.
+ The concepts of $D^+$ and $D^-$ are introduced on line 170, but their explanations are deferred until line 204. This gap may confuse readers. It would be clearer if a brief definition were provided when these concepts are first mentioned, or if the detailed explanation were moved closer to the first appearance.
+ In Fig. 2, the paper introduces the concept of sensitivity for privacy neurons. What if privacy neurons were selected based on their top dimension-wise sensitivity? The paper lacks a study on it.

### Questions
+ The paper uses a fixed top-k selection method for privacy neurons. What if we choose them based on a threshold of $m$, such as 0.5?

### Soundness
3

### Presentation
2

### Contribution
3
