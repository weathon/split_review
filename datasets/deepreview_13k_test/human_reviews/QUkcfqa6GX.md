# Spatio-Temporal Graph Learning with Large Language Model

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Spatio-temporal prediction holds immense significance in urban computing as it enables decision-makers to anticipate critical phenomena such as traffic flow, crime rates, and air quality. Researchers have made remarkable progress in this field by leveraging the graph structure inherent in spatio-temporal data and harnessing the power of Graph Neural Networks (GNNs) to capture intricate relationships and dependencies across different time slots and locations. These advancements have significantly improved representation learning, leading to more accurate predictions. This study focuses on exploring the capacity of Large Language Models (LLMs) to handle the dynamic nature of spatio-temporal data in urban systems. The proposed approach, called STLLM, integrates LLMs with a cross-view mutual information maximization paradigm to capture implicit spatio-temporal dependencies and preserve spatial semantics in urban space. By harnessing the power of LLMs, the approach effectively captures intricate and implicit spatial and temporal patterns, resulting in the generation of robust and invariant LLM-based knowledge representations. In our framework, the cross-view knowledge alignment ensures effective alignment and information preservation across different views while also facilitating spatio-temporal data augmentation. The effectiveness of STLLM is evaluated through theoretical analyses, extensive experiments, and additional investigations, demonstrating its ability to align LLM-based spatio-temporal knowledge and outperform state-of-the-art baselines in various prediction tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studied incorporating large language models (LLM) to enhance GNNs’ spatial temporal graph learning ability. To achieve this goal, the authors proposed an approach named STLLM, which first used GNN and LLM to encode the spatial temporal graph into region representation, respectively, and then optimized mutual information maximization objective to align the representation learned from these two views. Experiments on three different spatial temporal prediction tasks were conducted to evaluate the proposed approach.

### Strengths
1.	This work provided a simple idea to leverage the rich real-world knowledge in LLM to enhance the GNN-based spatial temporal graph learning.


2.	The LLM-based representation can be viewed as a kind of augmentation with global real-world knowledge, which can benefit spatial temporal prediction tasks, especially for some data sparsity scenarios where there are only limited supervision signals for model training.


3.	Extensive experiments on different tasks were conducted for evaluation. In addition to common experimental settings, the author also compared the proposed approach with baselines over data sparsity, along with the ablation study, parameter analysis, and case study.

### Weaknesses
W1 The method proposed in this paper achieved good results, but I think some points of the claimed contributions still need further explanation and justification. 


W1.a) The author pointed out that the framework can preserve both short-term and long-range dependencies. There is a need to better explain which part of the approach captured the long-range information on the spatial-temporal graph. 

W1.b) As discussed in the paper, this approach can distill invariant representation from LLM to benefit scenarios involving spatial-temporal distribution shifts. However, when prompting the LLM, the handcraft prompt was constructed by the dynamic spatial-temporal context of the region, so it’s a bit confusing about what the ‘invariant representation’ referred to. Moreover, it seems that there is no experiment in this paper to evaluate the model performance over distribution shift.


W1.c) Although the method performed well under data sparsity, this seemed not equivalent to good denoising capabilities. It would be better to conduct additional experiments with varying levels of noise added to the data to further justify it.


W2. The experiments can be further improved.


W2.a) Since task-specific baselines were used to compare with the proposed method in the crime prediction and traffic prediction tasks, it’s recommended to add a specific baseline for house price prediction.


W2.b) According to Table 1, some result values are relatively small. This suggests that the experimental results may be susceptible to random factors. Therefore, I recommend reporting the standard deviation under different random runs and adding a significance test to provide further insights.


W2.c) The loss function comprises many terms and different combinations of the four loss weights are likely to affect the model performance. It’s advisable to analyze their effects.

W2.d)  The adoption about the LLM used in the experiment is not very clear.

### Questions
Q1) Please explain why the experimental conclusions related to the method GraphST in the case study of this paper are so divergent from the conclusions in the case study of previous papers [1].


Q2) If constructing the graph using POI feature similarity, similar to [1], what would be the results in the case study?


Q3) What is the workflow for using the framework? Is it first learning region representations with STLLM, and then using these representations as inputs for a downstream predictive model? If so, how will it perform if directly using the LLM-based representation as inputs without the GNN part?

Q4）What LLM do you use for the LLM-based spatio-temporal knowledge learner?  There is only a mention in related work that : “This study applies decoder-only LLM (GPT-3.5) to enhance the quality of the spatio-temporal graph with effective augmentation.” However, if the GPT3.5 is used,  how can GPT3.5 to obtain the latent representation vectors F (in Section 3.2.2)? Is it to use the OpenAI’s text embeddings? What is the cost of conducting training and prediction for experiments?

[1] Qianru Zhang, Chao Huang, Lianghao Xia, Zheng Wang, et al. Spatial-temporal graph learning with adversarial contrastive adaptation. In International Conference on Machine Learning, pp. 41151–41163. PMLR, 2023b.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes the integration of a large language model (LLM) into the problem of spatio-temporal prediction. The main idea is to input each region's POI information, geographical relationship with other regions, and population flow relationships extracted from human mobility trajectories as prompts into a LLM like ChatGPT. The model then summarizes the available information for that region. The embedding of the summary text provided by GPT is then used as a constraint to train the Graph Convolutional Network, resulting in the final region embedding for downstream spatio-temporal prediction tasks.

### Strengths
1. The application of LLM to spatio-temporal prediction modeling is, to my knowledge, a novel approach.
2. The paper is well-organized, clear, and easy to understand.
3. The experiments are extensive and the results seem promising.

### Weaknesses
There are parts of the paper that require clearer explanations.
1. The paper's main innovation is the use of LLM to summarize region Spatio-temporal information, but Appendix 5 only provides a simple and incomplete example. For an LLM like ChatGPT, the design of the prompt significantly impacts the final result. Therefore, the complete prompt needs to be provided to improve reproducibility.
2. I assume that the region embedding used in the final downstream task should be $h_i$ and not $f_i$, but this is not clearly stated in the paper.
3. In Equation (6), the differences between $h$, $h^M$ and $h^D$ (also for f) are not clearly stated.
4. In Equation (6), it seems that the definitions of $L_{M,D}$ and $L_{G}$ are missing a negative sign.

### Questions
Please address the issues mentioned in the Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a contribution on combining spatiotemporal knowledge with LLM knowledge using cross-view information maximisation for spatio temporal graph representation. The method is evaluated across three different tasks: crime prediction. traffic prediction, and house price prediction.
The stated contribution however may be an overclaim in two parts: the contribution of the LLM information to the overall method, and the claim on distribution shift is non existent. 
There is also a potential issue with bias in the evaluation.

### Strengths
The proposed approach integrating cross-view mutual information maximisation with LLM knowledge is interesting.

The model has been tested in three different datasets and tasks.

The proposed approach has been compared with many popular baselines.

### Weaknesses
•	Although the paper has an interesting contribution in combining information maximisation with LLM, the contribution is limited. 

•	I disagree with the author that the LLM part is a main contribution. The proposed method seems only LLM-related part is the summarization part in Section 3.2.2. There is no further interaction between the model and the LLM. 

•	In the Introduction, the contribution part claims that incorporating LLM-based knowledge could handle the distribution shifts. However, it seems that there is no experiment to support/justify this claim.

•	In ablation study, is there a variant that removes the entire LLM knowledge vector part? Also, removing both S & T should be worse than either removing S or removing T. However, from Figure 2, this seems not the case. 
Providing more detailed information (instead of just the analysis of NYC-Larceny and CHI-Assault two cases) could further strengthen the discussion.

•	Another minor issue: providing the code repository is good. However, there are some comments given in Chinese, which is not friendly to other readers.

### Questions
•	Is the proposed method trained end-to-end? Or the ChatGPT summarization part should be pre-processed before the entire model training? 

•	How would you ensure that the LLM knowledge is actually helping the model? This isn't shown in the ablation study.

•	How would you ensure if the potential bias from the sparse spatiotemporal data especially in crime and house price cases are not exacerbated with the use of LLM?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paragraph discusses the significance of spatio-temporal prediction in urban computing for anticipating events like traffic flow and crime rates. It highlights the use of Graph Neural Networks (GNNs) to improve prediction accuracy by leveraging the inherent graph structure in spatio-temporal data. The study introduces STLLM, an approach that integrates Large Language Models (LLMs) to handle dynamic urban data, effectively capturing spatial and temporal patterns and outperforming existing methods in various prediction tasks.

### Strengths
The authors presents a really interesting study that integrates LLM with GNN for spatio-temporal prediction task. By integrating LLMs and a cross-view mutual information maximization paradigm, the study effectively captures intricate spatial and temporal patterns and implicit dependencies, resulting in robust knowledge representations. Furthermore, the research evaluates the proposed approach through  extensive experiments, and comparisons to state-of-the-art methods, demonstrating its ability to outperform existing techniques in various prediction tasks.

### Weaknesses
The contributions of this study are weakly linked with the claimed challenges. I am not convinced that the proposed method address these challenges sufficiently. 

Intuitively, LLM is able to provide mode general semantic context about geospatial location information. Using semantic information for spatio-temporal prediction task is not well formulated. 

The contribution of using LLM is not fully investigated. 

Detailed information of the applied LLM is not fully disclose, weakening reproducibility of the paper.

### Questions
* LLM is pretrained, in most of cases. How to make sure the information that used to train LLM is within the same range of time for the data that is used to evaluate the model performance. The knowledge of LLM can be stable, how to make sure the information is robust and updated for the spatio-temporal prediction. 

* Which LLM is used here?

* Can you compare your model performance between using and w/o using LLM?

* Does different LLM impact your model performance?

* Does different training data using for LLM impact your model performance?

* Could you elaborate more how semantic information generated by LLM provide meaningful contribution to improve the model performance?

* Any interpretability insight you can share to help readers to better understand how STLLM works?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
