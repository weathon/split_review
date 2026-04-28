# LLM-guided spatio-temporal disease progression modelling

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 1, 5, 6

## Abstract
Understanding the interactions between biomarkers across brain regions during disease progression is essential for unravelling the mechanisms underlying neurodegenerative disease. For example, in Alzheimer's Disease (AD) and other neurodegenerative conditions, there are typically two kinds of methods to contract disease trajectory. Existing mechanistic models describe how variables interact with each other spatiotemporally within a dynamical system driven by an underlying biological substrate often based on brain connectivity. However, such methods typically grossly oversimplify the complex relationship between brain connectivity and brain pathology appearance and propagation. Meanwhile, pure data-driven approaches for inferring these relationships from time series face challenges with convergence, identifiability, and interpretability. We present a novel framework that bridges this gap by using Large Language Models (LLMs) as expert guides to learn disease progression from irregular longitudinal patient data.  Our method simultaneously optimizes two components: 1) estimating the temporal positioning of patient data along a common disease trajectory and 2) discovering the graph structure that captures spatiotemporal relationships between brain regions. By leveraging multiple LLMs as domain experts, our approach achieves faster convergence, improved stability, and better interpretability compared to existing methods. When applied to modelling tau-pathology propagation in the brain, our framework demonstrates superior prediction accuracy while revealing additional disease-driving factors beyond traditional connectivity measures. This work represents the first application of LLM-guided graph learning for modelling neurodegenerative disease progression in the brain from cross-sectional and short longitudinal imaging data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a novel disease progression model for neurodegenerative diseases that leverages a mixture of large language models (LLMs) to infer brain region interactions for predicting temporal dynamics. The approach uses prompts to query LLMs about potential interactions between brain regions, which are then used to construct a graph that informs disease progression

### Strengths
### Strengths

1. **Innovative Use of LLMs in Disease Progression Modeling (DPM)**:
The paper introduces a creative and potentially impactful approach by leveraging large language models (LLMs) for graph-based disease progression modeling  in neurodegenerative diseases.

### Weaknesses
### Weaknesses 

1. **Vague Language and Disorganized Manuscript**:  
   The paper uses terms like "causal interactions" without justification. The use of graph learning alone does not establish causation, as this typically requires specific assumptions or experimental design elements, such as interventions or causal inference techniques. Without these, the inferred relationships are associative rather than causal. Also,  the term "long-term" is not clearly defined, despite its critical importance in temporal modeling of disease progression. The lack of a precise timeframe (e.g., years or decades) makes it difficult to understand the model's intended scope and applicability. A clearer definition of "long-term" would strengthen the paper. Additionally,  there are instances where equations or concepts are referenced before they are defined, disrupting the logical flow and making it difficult for readers to follow. For instance, equation 9 is mentioned in the text (Section 2.2) before it is officially introduced (Section 2.5.1). Finally, there are several typos throughout the manuscript. Minor notice, but important, evaluation measures like SSE should be introduced first and then utilized with abbreviation for more clarity.

2. **Lack of Comparisons with Baselines and Limited Qualitative Results**:  
   Although the authors cite several relevant baseline methods, such as Bellot et al. (2021), they do not provide empirical comparisons. Without benchmarking against these established approaches, it is difficult to assess the advantages of the proposed method. 
Also, there are no qualitative results with predicted trajectories that would showcase that the method works in several test examples.
Additionally, in section 3.3 and 3.4 of the results authors use only the Claude3.5 LLM. However, their proposed method is the mixture of the LLMs and not only a single LLM (Claude3.5). This inconsistency, weakens result's coherence  as well as the validity of the proposed method. 

3. **Questionable Prompt Strategy for LLMs**:  
   The approach relies on querying LLMs with prompts for each brain region to infer relationships, which raises several concerns:
   - **Scientific Validity**: General-purpose LLMs lack domain-specific scientific knowledge and are prone to hallucinations. This means that the generated weights or connections could be inaccurate or even fabricated.
   - **Scalability**: The strategy of creating prompts for each brain region does not scale well for fine grained ROI brain representations, making it computationally intensive and potentially inconsistent.
   - **Stability and Consistency**: Since LLM responses can vary with prompt phrasing, it’s unclear if these outputs are reliable across prompts. An analysis of prompt sensitivity or consistency checks would be necessary to validate this approach.

4. **Limited Longitudinal Data for Temporal Modeling**:  
   With only 254 samples from 185 subjects, it appears that most subjects have only a single acquisition (baseline) and one follow-up. This data limitation raises doubts about the model’s ability to learn meaningful temporal dynamics. The authors do not address how the model captures progression trends with such limited longitudinal data, leaving the temporal component of the model questionable.

5. **Limited Discussion of Practical Application and Real-World Feasibility**:  
    The paper lacks a detailed discussion of how the proposed Disease Progression Model could be applied in real clinical or research settings. The reliance on prompts and general-purpose LLMs may hinder broader adoption, as access to specific LLMs, prompt engineering, and technical resources may not be feasible in clinical environments. Addressing these practical challenges and offering guidance for real-world application would enhance the paper's relevance.

### Questions
### Questions

1. **Handling of Repeated Measures**:  
   - "Authors mention that they leverage longitudinal population-data. How do you handle repeated measures in the training process?"

2. **Ratio Specification for Mixing LLMs**:  
   - "How do you specify the ratio (0.865:0.135) for mixing the two LLMs? Could you provide a rationale or any empirical basis for choosing this specific ratio?"

3. **Cross-Validation for Robustness**:  
   - "A simple splitting of the 255 subjects into train-test-validation is not enough. A fold cross-validation (train-test-validation) splitting multiple times would produce more powerful results. Could you comment on the reason for choosing a single split rather than cross-validation?"

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This work presented a proof-of-concept approach to model Alzheimer's disease (AD) using LLM. The idea is interesting. However, the feasibility and power of LLM in understanding the etiology of AD is not clearly demonstrated. Our current understanding on disease mechanism is still elusive in the AD field. Not sure how the proposed approach could advance our current understanding on AD. 

Another main concern is the data sample size. Neuroimaging data from ADNI is used in this work. There is only couple hundreds (<300) subjects having both modalities (structural connectome and pathology data). It is not clear how to address the issue small sample size.

Also, the data pre-processsing is not clear. Which brain atlas is used? Based on the node number, looks like the Desikan-Killiany Atlas. Please note this atlas does not include sub-cortical regions, means it is not a perfect brain parcellation for studying AD.

Result interpolation lacks biological underpinnings and supporting evidence from current literatures in AD.

### Strengths
First try of LLM in understanding disease progression.

### Weaknesses
This work presented a proof-of-concept approach to model Alzheimer's disease (AD) using LLM. The idea is interesting. However, the feasibility and power of LLM in understanding the etiology of AD is not clearly demonstrated. Our current understanding on disease mechanism is still elusive in the AD field. Not sure how the proposed approach could advance our current understanding on AD.

Another main concern is the data sample size. Neuroimaging data from ADNI is used in this work. There is only couple hundreds (<300) subjects having both modalities (structural connectome and pathology data). It is not clear how to address the issue small sample size.

Also, the data pre-processsing is not clear. Which brain atlas is used? Based on the node number, looks like the Desikan-Killiany Atlas. Please note this atlas does not include sub-cortical regions, means it is not a perfect brain parcellation for studying AD.

Result interpolation lacks biological underpinnings and supporting evidence from current literatures in AD.

### Questions
What is the essential motivation of employing LLM in modeling AD progression?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel spatio-temporal framework guided by large language models (LLMs) to model long-term disease progression on brain graphs, utilizing structure discovery from longitudinal, population-level patient data. A key innovation lies in addressing the unknown temporal alignment of observations by embedding the method within a dual-optimization framework. This framework simultaneously estimates the disease progression model—capturing common biomarker trajectories across a population—and performs structure discovery, learning a graph that represents the spatiotemporal interactions among biomarkers. The proposed approach achieves superior prediction accuracy, faster and more stable convergence, and enhances the interpretability of the model.

### Strengths
This paper explores the use of Large Language Models (LLMs) as expert guides to enhance graph inference by integrating expert knowledge.

### Weaknesses
1. There are a lot of typos, such as "To address these limitations, we **consder** use Large Language Models (LLMs) as
expert guides to enforce the graph inference with expert **knowlegdge**" and so on.
2. In Eq. (5), why **p**  is calculated from the **99th** percentile of the tau distribution at each region?
3. In Eq. (8), what does $D_{LLM}$ represent? Could you clarify the statement, "This not only accounts for the diffusion process along the white matter bundles but also considers additional factors related to tau accumulation from the knowledge base of various LLMs"? From Equations (7-9), I am not seeing how structural connectivity is addressed (i.e., the diffusion process along the white matter bundles).
4. In Eq. (10),  what does $X$ stand for? what's the relationship between this section and the previous sections? I can't follow this.
5. What's the dataset you use? How about the performance on other diseases? What's the sample size? How many time point for each subject do you use?
6. Insufficient experiments and lack of comparison of many disease progression modeling models.
7. This method claims to estimate regional tau-pathology propagation over the brain. Can authors provide the related propagation pattern in the brain over time?

### Questions
Please refer to weaknesses.

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
The authors propose a novel LLM-guided spatio-temporal framework for modeling regional variable changes during disease progression. The key innovation of this paper lies in utilizing a large language model (LLM) to enhance graph initialization and regularization in both mechanistic and data-driven settings, demonstrating improvements in accuracy and convergence. The models were evaluated on regional tau-pathology propagation across the brain.

### Strengths
1. The paper is well-written and engaging. The idea of leveraging LLM knowledge for graph initialization is particularly intriguing. Given the recent advancements in LLM, effectively incorporating this knowledge into fundamental clinical research is crucial, and the authors demonstrate this integration in a good way. 
2. The authors provide solid background information that helps readers easily grasp the context of their work. 
3. Sufficient detail is offered on critical components, including prompting strategies, clear mathematical definitions, and experimental details, allowing readers to understand the underlying processes. 
4. The evaluation of the model through critical edge numbers is both interesting and effective, showcasing the advantages of LLM-based graphs. 
5. The authors conduct an extensive analysis, covering prompt ablation, synthetic data, different contexts (both data-driven and mechanistic), and model convergence.

### Weaknesses
1. I may have missed it, but the calculation of the metric "SSE" lacks a clear definition, making it challenging to assess its scale effectively. 
2. The experiments appear to be conducted on a single data split, without cross-validation or random splitting. Given the relatively small variances reported in Table 2, it’s difficult to evaluate the significance of differences and reproducibility. Incorporating additional splits and reporting standard deviations would enhance the findings. 
3. The representation of faster convergence (A.3), particularly between the second and third figures, could be clearer. Adjusting the scale might help elucidate this aspect. 
4. While the authors emphasize the importance of identifiability and interpretability, their discussion primarily revolves around reducing the number of edges in the graph. There is limited exploration or discussions on how the derived graphs enhance understanding of regional interactions and differences during disease progression compared to other graphs.
5. In figure 4, descreasing the critical edge number throgu “7-factor” prompt is not very clear to me. It seems that the other factors provided by LLM does not lead to much advantages. 
6. It appears that the model assumes a single typical progression path of phenotypes per disease, potentially overlooking disease heterogeneity. Recent research has demonstrated significant heterogeneity in disease progression, particularly in brain diseases, including amyloid and tau spreads.

### Questions
1. In Section A.3, why is the summation limited to four types of brain connectivities rather than five? 
2. For clarification, when comparing Model 1 and Model 2, are the authors directly comparing the performance of these two methods, or are they comparing the graphs used in these models within the context of Method 3?

### Soundness
3

### Presentation
3

### Contribution
3
