# Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
We propose semantic entropy probes (SEPs), a cheap and reliable method for uncertainty quantification in Large Language Models (LLMs).
Hallucinations, which are plausible-sounding but factually incorrect and arbitrary model generations, present a major challenge to the practical adoption of LLMs.
Recent work by \citet{farquhar2024detecting} proposes semantic entropy (SE), which can detect hallucinations by estimating uncertainty in the space semantic meaning for a set of model generations.
However, the 5-to-10-fold increase in computation cost associated with SE computation hinders practical adoption.
To address this, we propose SEPs, which directly approximate SE from the hidden states of a single generation.
SEPs are simple to train and do not require sampling multiple model generations at test time, reducing the overhead of semantic uncertainty quantification to almost zero.
We show that SEPs retain high performance for hallucination detection and generalize better to out-of-distribution data than previous probing methods that directly predict model accuracy.
Our results across models and tasks suggest that model hidden states capture SE, and our ablation studies give further insights into the token positions and model layers for which this is the case.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a technique called Semantic Entropy Probes (SEP) for detecting hallucinations in large language models (LLMs). SEP leverages the internal states of LLMs to predict the semantic entropy (SE) of their responses. By doing so, the method empirically achieves an accurate approximation of SE without the computational overhead of multi-sampling. Furthermore, SEP effectively identifies model hallucinations in both in-distribution and out-of-distribution settings.

### Strengths
* This paper addresses a timely and significant research problem in LLMs. Detecting hallucinations is crucial for ensuring the safety of LLM applications in real-world scenarios.
* The experiments are extensive and compelling. The authors conduct experiments on and report results for several popular open-source models.
* The paper is generally well-written and easy to follow.

### Weaknesses
 * I think the main weakness of this work is the lack of clear motivation and explanation for the outcomes. The SEP method appears to simply switch the prediction goal of previous internal state detection methods from accuracy to semantic entropy (SE), which seems like a simple 'a+b' combination. Although the results are promising, I am still expecting more insights from the experimental results regarding the mechanisms of LLMs. For example, why is it possible to use internal states to predict SE? And why does switching the prediction goal from accuracy to SE result in better performance in out-of-distribution settings? A clearer explanation of these questions would further enhance the solidness of this work and our understanding of LLMs.
* An obvious limitation is the applicability of the proposed method to black-box LLMs. I recommend that the authors discuss this in the limitations section.
* Most of the experiments compare the proposed method with accuracy-based probing methods. However, there are insufficient details provided to describe these counterpart methods. It would be more helpful to provide a comprehensive introduction to these methods for readers who are unfamiliar with them.

### Questions
1. Do authors have a clear explanation of why it is feasible to predict semantic entropy (SE) from internal states and why SE could serve as a better supervisory signal than accuracy in out-of-distribution training settings?
2. One of the advantages of SEP is that it does not rely on ground truth labels from the dataset. However, as mentioned by the authors, there are also existing works [1,2] that predict the trustworthiness of LLMs from internal states using unsupervised methods. I am curious about how these methods would perform under the same settings as SEP.


---
[1] Discovering Latent Knowledge in Language Models Without Supervision
[2] Representation Engineering: A Top-Down Approach to AI Transparency

### Soundness
3

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
4

### Summary
The paper proposes a new method Semantic Entropy Probes (SEPs) for hallucination detection of LLMs, which aims to capture semantic entropy by training a linear classifier on top of LLM hidden states. The authors perform various ablation studies to understand different design choices (model family, layer, token position) across common benchmarks. Experiments suggest the effectiveness of the proposed method over various baselines.

### Strengths
- The method to estimate semantic entropy by linear probing is simple to implement and alleviates repeated sampling at test-time. 
- The experiments and ablations are thorough to demonstrate the effectiveness of the proposed method. 
- The overall organization of the paper is clear and coherent.

### Weaknesses
 - **Motivation of SEP Efficiency**: The primary motivation for SEP, as stated in the paper, is that it is "cheap" and significantly enhances computational efficiency compared to the baseline semantic entropy (SE). However, this claim appears to be poorly substantiated. The comparison between a training-based method (SEP) and a test-time method (SE) is insufficiently justified. For a fair comparison, it might be better to provide analysis of the overall cost: SE with sampling v.s. the total cost (training and inference) of SEP.

- **Improvement in Long Generation Experiments**: The long generation experiments could be improved. Currently, long generation is primarily conducted with prompts that request "a single brief but complete sentence," resulting in relatively short responses. This approach diverges from recent practices, where models are often prompted to generate detailed reasoning or more elaborate outputs for long-form generation.

### Questions
- To calculate semantic entropy (L185), how is the number of clusters K determined? 
- Can authors further discuss why "the discrete variant of SE" should be used instead of the plain version Eq (1)? How is the "fraction of generations in the cluster" related to "avoid problems for generation of different length" (L193)?
- In Sec 5, it seems that the prompt "single brief but complete sentence" also promotes short responses. Does a Chain-of-Thought style prompt work for the long-form answer generation?

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
3

### Summary
The paper describes an approach to hallucination detection. Unlike existing methods, that generate multiple samples at inference time to derive an estimate of uncertainty (semantic entropy), the method trains a linear model on a subset of the LLM's hiddens to predict it efficiently. The paper shows that this works reasonably well, although the accuracy is behind that of the sampling based methods.

### Strengths
The paper is well-written, quite polished and very easy to follow. Empirical evaluations seem reasonably detailed and the findings clear.

### Weaknesses
The accuracy of the semantic entropy prediction is quite significantly behind the sampling-based estimate. In addition, it seems hard to quantify how much prediction accuracy for hallucination detection would actually impact any practical applications. Since there are many possible avenues to improve accuracy, some investigation in this direction - even just in a preliminary fashion - would make this work stronger.

The improved efficiency comes at a significant accuracy hit as compared to SE. How would the SE results be affected for smaller sample size N? The potential benefits of the proposed method would be significantly diminished if SE tends to be more or less stable in response to reducing N.

In this work, probes are applied only to separate layers. Have the authors considered combinations of multiple layers? This would make sense if one assumes that different layers may contribute different evidence for model uncertainty.

How OOD is the OOD setting really? How (dis-)similar are the different datasets from one another?

I assume the values in Figure 2 are for held-out not training data. Is that correct?

What is the actual potential time efficiency benefit of the method as compared to SE, for example, as measured in in wall clock time? And how much would the possibility to generate samples in batch-mode affect those numbers?

The proposed method is very simple and seems somewhat "obvious". I'm a bit surprised this hasn't been studied before, but not being an expert in this work I give the paper the benefit of the doubt and consider this simplicity a plus.

### Questions
The improved efficiency comes at a significant accuracy hit as compared to SE. How would the SE results be affected for smaller sample size N? The potential benefits of the proposed method would be significantly diminished if SE tends to be more or less stable in response to reducing N. 

Would it make sense to use significantly higher N during training as a way to improve SEP accuracy? 

In this work, probes are applied only to separate layers. Have the authors considered combinations of multiple layers? This would make sense if one assumes that different layers may contribute different evidence for model uncertainty. 

How OOD is the OOD setting really? How (dis-)similar are the different datasets from one another? 

I assume the values in Figure 2 are for held-out not training data. Is that correct? 

What is the actual potential time efficiency benefit of the method as compared to SE, for example, as measured in in wall clock time? And how much would the possibility to generate samples in batch-mode affect those numbers? 

The proposed method is very simple and seems somewhat "obvious". I'm a bit surprised this hasn't been studied before, but not being an expert in this work I give the paper the benefit of the doubt and consider this simplicity a plus.

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
This paper proposes Semantic Entropy Probes (SEPs) for hallucination detection in LLMs. The primary motivation of this work is to reduce the computational cost associated with semantic entropy, a representative sampling-based method for detecting hallucinations. SEPs are trained using the hidden states of LLMs to predict semantic entropy. The authors demonstrate that SEPs can effectively predict hallucinations and offer better generalization compared to probes that are directly trained for accuracy.

### Strengths
1. The motivation is intuitive and clear, the paper is well written and easy to implement.
2. Training linear probes on the hidden states of large language models to capture semantic entropy is a promising approach. It offers new insights for reducing the cost of traditional sampling-based hallucination detection.
3. Comprehensive ablation studies have been conducted across various models, tasks, layers, and token positions. The experimental results align with expectations.

### Weaknesses
1. The related work section lacks several crucial references [1,2,3,4]. For example, ref [1]  also adopt a supervised method for uncertainty estimation of LLMs. ref [2,3] explores the internal states of LLMs for hallucination detection. The author should introduce more hallucination detection methods based on internal states or linear probs. I have seen at least 5 papers that train a classifier for hallucination detection. Therefore, I suggest the authors to add a paragraph discussing internal state-based and probe-based hallucination detection methods, highlighting key differences between those approaches and SEPs

2. The performance of SEPs is unsatisfactory, and the author should include more competitive baseline methods. According to Fig. 7, SEPs fall short by 5-10 points compared to SE. Furthermore, SE is not the state-of-the-art (SOTA) method for hallucination detection [2,5]. It is recommended that the author include comparisons with the SOTA methods. I acknowledge that SEPs aim to balance performance and computational efficiency, I would suggest the authors to discuss this trade-off more explicitly in relation to SOTA methods.

3. There seems to be no clear explanation for why predicting SE yields better performance compared to predicting labels. I would appreciate a more detailed analysis explaining why predicting SE outperforms label prediction. The current discussion lacks both theoretical support and sufficient experimental evidence to substantiate the claim that predicting semantic entropy is inherently superior to predicting accuracy labels, particularly in out-of-distribution scenarios. The paper needs a more rigorous analysis of why the learned representations for semantic entropy generalize better than those for accuracy labels.

### Questions
1. α represents the optimal threshold for partitioning raw SE scores into high categories, and I'm interested in how this threshold varies across different datasets. Additionally, I'm uncertain about the generalizability of trained SEPs across these datasets.
2. Would using hidden state information to predict SelfCheckGPT scores [1], Eigenscore [2], or other uncertainty scores potentially lead to better results?

[1] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models

[2] INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection

### Soundness
3

### Presentation
3

### Contribution
2
