# Differentiation and Specialization of Attention Heads via the Refined Local Learning Coefficient

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
We introduce refined variants of the Local Learning Coefficient (LLC), a measure of model complexity grounded in singular learning theory, to study the development of internal structure in transformer language models during training. By applying these \textit{refined LLCs} (rLLCs) to individual components of a two-layer attention-only transformer, we gain novel insights into the progressive differentiation and specialization of attention heads. Our methodology reveals how attention heads differentiate into distinct functional roles over the course of training, analyzes the types of data these heads specialize to process, and discovers a previously unidentified multigram circuit. These findings demonstrate that rLLCs provide a principled, quantitative toolkit for \textit{developmental interpretability}, which aims to understand models through their evolution across the learning process. 
  More broadly, this work takes a step towards establishing the correspondence between data distributional structure, geometric properties of the loss landscape, learning dynamics, and emergent computational structures in neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce a novel approach to understanding the internal specialization of attention heads in Transformer models through Refined Local Learning Coefficients (rLLCs). By measuring the complexity of attention heads and tracking their developmental process during training, the authors reveal how different heads gradually specialize in performing specific tasks.

### Strengths
1. The rLLC provides an innovative, quantitative tool for tracking specialization in Transformer models, which could have applications beyond this study.

2. The paper includes a comprehensive analysis of attention head specialization, backed by clustering and ablation studies that demonstrate the functional roles of different heads.

3. The discovery of "multi-phrase circuits" and the evidence of cross-layer head collaboration provide valuable insights into how Transformer models handle complex linguistic patterns.

### Weaknesses
1. While the method is effective on smaller models, the paper does not discuss the computational implications for larger models. Specifically, the scaling of the rLLC calculation with respect to model size (number of parameters, layers, attention heads) and training dataset size is not addressed. This is crucial because the practical applicability of the method hinges on its feasibility for state-of-the-art models.

2. The study focuses on understanding Transformer models without discussing how these insights could guide architecture optimization or training strategies in practice. The paper lacks concrete examples of how the identified specialization patterns could be leveraged to improve model performance, such as through targeted regularization or pruning techniques. The insights remain largely descriptive rather than prescriptive.

3. The comparison with existing interpretability metrics is limited. While the authors mention Hessian-based metrics and ablation techniques, a more thorough comparison with other established methods, such as those based on information theory or causal analysis, is needed to fully contextualize the contribution of rLLCs. The absence of a direct comparison with metrics that quantify the information content or causal influence of attention heads leaves a gap in the analysis.

### Questions
1. Could insights from rLLC tracking be used to optimize training processes, such as by dynamically adjusting learning rates or selectively freezing layers based on head specialization patterns?

2. How well does the rLLC methodology generalize to larger models, such as GPT-like architectures?

3. How do rLLCs compare with the existing interpretability metrics? The authors could refer to these related works: [Michaud, Eric, et al. "The quantization model of neural scaling." Advances in Neural Information Processing Systems 36 (2024).] ; [Xiao, Xiongye, et al. "Exploring neuron interactions and emergence in llms: From the multifractal analysis perspective." arXiv preprint arXiv:2402.09099 (2024).]

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces refined Local Learning Coefficients (rLLCs) as a method to analyze the internal structural differentiation within transformer models. 
In particular, they introduce weight refined LLCs and data-refined LLCs.
By applying rLLCs to individual attention heads of a two-layer attention-only transformer model on different types of data, the authors aim to track how these components specialise and differentiate into distinct functional roles across training. The work provides insights into attention head specialisation based on the types of data processed, discovers specific structural patterns (e.g., multigram circuits), and highlights the correspondence between data distributional structure, loss landscape geometry, and model learning dynamics.

### Strengths
The paper presents a novel metric to track structure during training based on data structure and tracking the evolution and specialisation of attention heads, overcoming some of the limitations of previous metrics. The paper presents some novel insights into how heads specialise and the effect of data.
- The presented metric (rLLC) overcomes some of the existing limitations of the LLC method, including the assumption that the $w^*$ is a local minima (which during training, it is very unlikely to be)
- rLLC seems to in practice be able to differentiate attention heads by their specialisation, it is interesting to observe the higher complexity of heads performing memorisation and n-gram heads vs the induction ones (Figure 1)
- The authors show how with a different data (Github) the head specialisation changes and more importance is given to the induction heads (Figure 3)
- The experiments are well-documented, with comprehensive comparisons against other interpretability measures like Hessian and Fisher Information Matrix traces, adding robustness to the findings.

### Weaknesses
 - the experiments limit themselves to a two layer transformer, it would have been interesting to see how the proposed rLLC metric would behave in a bigger transformer. Is it still trackable? Does it lead to a meaningful interpretation of results?
- what about different architectures? Line 465 in the related section mentions AlexNet, it would have been interesting to carry out a similar analysis on layers of AlexNet

### Questions
- it was not clear to me how the K-means clustering was obtained to generate the colours for the different lines in e.g. Plot 1. What is the K-means over? 
- Have you considered how the rLLCs would scale with deeper, more complex transformer models? Are there any preliminary results or hypotheses about the performance and practicality of this method on architectures with more layers or MLP components?
- Beyond interpretability, have you explored any practical use cases where rLLCs could directly influence model design or training strategies (e.g. model pruning)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce refined variants of the Local Learning Coefficient (LLC), a measure of model complexity grounded in singular learning theory, to study the development of internal structure in transformer language models during training. By applying
these refined LLCs (rLLCs) to individual components of a two-layer attention- only transformer, they were able gain novel insights into the progressive differentiation and specialization of attention heads. The methodology used in this paper reveals how attention heads differentiate into distinct functional roles over the course of training, analyzes the types of data these heads specialize to process, and discovers a previously unidentified multigram circuit. The authors conclude that their findings demonstrate that rLLCs provide a principled, quantitative toolkit for developmental interpretability,

### Strengths
The work is well grounded in the existing literature and theories. A good number of appropriate citations back this up that the authors build the work in this paper on. 

The mathematical descriptions are brief and concise but sufficiently detailed and understandable. Appropriate level of detail.

Section 3.3 Limitations and the comparisons to related work within was much appreciated. 

The degree and amount of supplementary information and detail in the appendices was excellent and greatly supports the main paper.

### Weaknesses
It would be beneficial to even if briefly define how the authors are explicitly using the terms 'component' and 'arbitrary data distribution' earlier on since it is the differentiating elements to other LLC metrics. The reader is left wondering and speculating as they continue to read in the way it is presented in the original paper. 

The immediate next statement says "We focus mainly on the rLLCs of individual attention heads ...", implying diversity in how their new rLLC metric can be defined, tweaked, and/or applied.  But the authors have not even defined what it is. It is introducing a degree of variability prematurely that comes across as confusing. Before implying what they are 'focusing' on among several possibilities of (how?) their rLLC metric is defined, how about saying what it is first clearly and explicitly. 

Similarly, the use of the term 'development' at the bottom of page 2 would be strengthened by giving the reader at this stage a brief one or two sentence understanding of the explicit meaning of the term as adopted in the paper. Italicizing it alone is not enough. The reader understands its important, but please help them in building understanding along the way.

### Questions
See comments above.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes two types of refined local learning coefficients (LLC), weight-refined LLC and data-refined LLC, and applies them to a two-layer attention only transformer to study the progressive differentiation and specialization of the attention heads. Both LLCs (defined in eq 5) are based on the estimated LLC (defined in eq 2), where suppressing q or V leads to weight-refined or data-refined LLC. The limitations of the proposed LLCs are given in Sec 3.3. Experimental results show that the refined LLCs reveal how attention heads differentiate (featured in Fig 2) and specialize (featured in Fig 3). In addition, combining the refined LLCs reveal internal structure related to multigram prediction that enables nested bracket-matching.

I am not an expert in this area, and therefore read the paper multiple times. I enjoyed reading it. My rating is 6, but I'm willing to raise the score if weakness #1 is addressed because it is preventing me from understanding the general applicability/feasibility of the proposed method.

[update during discussion] The authors have added experiments on a larger model, I therefore raised my rating.

### Strengths
- This paper is well-written, even a non-expert can easily follow the content if they are willing to spend some time figuring out the math.
- Although on a toy network, the results presented by this paper are strong and interesting.

### Weaknesses
 - In Sec 6, the authors mentioned that *"The techniques pioneered in this paper for understanding internal structure in two-layer attention-only transformers can of course be applied to models at a larger scale or with different architecture."*. It would be more convincing if they present some results in the paper. [I'm willing to raise my rating if this can be addressed]
- [This is a suggestion] When I read the paper for the first time, I didn't immediately understand "what this paper unlocks" or "why this work is important" after finishing the introduction section. I suggest improving the writing of this section. For example, moving some text from Sec 6 to the introduction may be a good option.

### Questions
1. If the analysis is applied to transformers learned in different domains (e.g., decision transformer in RL), will we have similar observations?
2. Tiny issues in equations:
    1. In eq (1), if $f_w$ is a function from contexts to probability distributions, do you still need $\texttt{softmax}$?
    2. Is $\lambda$ in equation (5) missing a hat?
    3. Is the threshold $t$ in eq (4) and (5) the time steps? If not, consider changing it as $t$ is used in the figures as time steps.

### Soundness
3

### Presentation
3

### Contribution
3
