# Dual Variance Reduction with Momentum for Imbalanced Black-Box Discrete Prompt Learning

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Black-box prompt learning has proven to be an effective approach for customizing large language models (LLMs) offered as services to address various downstream tasks. 
Within this domain, policy gradient-based methods have garnered substantial attention as a prominent approach for learning discrete prompts.
However, the highly imbalanced data distribution in the real world limits the applicability of such approaches by influencing LLMs' tendency to favor certain categories.
To tackle the challenge posed by imbalanced data, this paper pioneers the integration of pairwise AUC loss into the policy gradient optimization of discrete text prompts and proposes learning discrete prompts with doubly policy gradient.
Unfortunately, the doubly policy gradient estimation suffers from two variance components, resulting in unstable optimization.
As a further improvement, we propose (1) a novel unbiased variance-reduced doubly policy gradient estimator and (2) incorporating the STORM variance reduction technique. 
Ultimately, we introduce a novel momentum-based discrete prompt learning method with doubly policy gradient (mDP-DPG).
Crucially, we provide theoretical convergence guarantees for mDP-DPG within standard frameworks.
The experimental results show that mDP-DPG surpasses baseline approaches across diverse imbalanced text classification datasets, emphasizing the advantages of our proposed approach for tackling data imbalance.
Our code is available at the following URL: https://anonymous.4open.science/r/DPDPG-1ECB.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper considers the (discrete) black-box prompt tuning for LLM for binary classification problems with imbalanced data. The main contributions are as follows:

1. The authors propose the mDP-DPG (momentum-based Discrete Prompt learning with Doubly Policy Gradient) approach. This approach combines pairwise AUC loss and variance reduction techniques to deal with imbalanced data.

2. A theoretical analysis is provided, showing that mDP-DPG achieves optimal convergence rates for imbalanced data scenarios, under some conditions such as bounded variance of the gradient.

3. Experiments on benchmark datasets (like CoLA and MRPC) and real-world imbalanced datasets (Amazon reviews) demonstrate that mDP-DPG outperforms baseline methods.

### Strengths
1. This is the first paper that studies how to address imbalanced data in NLP prompt learning.

2. The theoretical results might be insightful in the realm of black-box policy optimization.

### Weaknesses
1. Scenario

The paper considers prompt tuning involving:
- black-box LLM (e.g., API-only LLM)
- classification tasks
- imbalance data

However, prompt tuning for black-box LLMs is generally more relevant to complex generative tasks rather than simpler classification tasks. It is uncommon for entities to use models like GPT-4 primarily for text classification, especially when manually designed prompts can already yield strong performance on tasks like GLUE. This positioning may reduce the appeal of the proposed method to the main audience of ICLR.

2. Experiments

The paper does not include experiments on widely used API-only LLMs, such as GPT-3.5 or GPT-4. Additionally, it lacks comparisons with other existing black-box prompt tuning methods like APE [R1], EvoPrompt [R2], and ZOPO [R3].

### Questions
Please see "weakness".

### Soundness
3

### Presentation
3

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
The authors propose a variance-reduced policy gradient descent method for black-box prompt learning. To deal with the class imbalance issue, the authors use AUC as the objective function. To accelerate the algorithm convergence, the authors propose to use two variance reduction techniques. The proposed algorithm has a convergence guarantee and good experimental performance.

### Strengths
1. To deal with the class imbalance issue, the authors propose to use AUC as the objective function.

2. To get fast convergence, the authors propose to reduce variance from both policy estimation and optimization.

### Weaknesses
1. The authors assume that the tokens in the prompt are sampled independently from their marginal distribution. However, it seems that tokens in the prompt should have some relation.

2. The proposed method can only for binary classification. How to extend to the multi-class? Do we need to train multiple different prompts?

### Questions
1. Can the authors describe why the probability they use assuming the tokens in the prompt sampled independently?

2. Is there a simple way to extend from binary classification to multi-class classification, since binary classification is rare in practice?

3. How concentrated the final solution P is? If the probability spread out to many different tokens, how can we generate a stable prompt to use?

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
4

### Summary
This paper considers the problem of discrete prompt learning with black-box language models. The authors propose an unbiased variance-reduced doubly policy gradient estimator for optimizing prompts through policy gradient optimization. By incorporating the STORM variance reduction techniques, the algorithm obtains a stable prompt. Experimental results on several benchmark tasks show the effectiveness of the proposed algorithm.

### Strengths
1. This work studies the challenge of data imbalance in discrete prompt learning with black-box models, a significant issue in many practical applications.

2. Discrete prompt learning is widely necessary for practical applications with black-box models. The proposed method has the potential to serve as a fine-tuning approach for many commercial black-box models.

### Weaknesses
1. The proposed method, along with its theoretical analysis, largely combines existing techniques, which limits its technical novelty.

2. Several of the backbone models used in the experiments, such as RoBERTa-large and GPT2-XL from 2019, are outdated for current black-box applications. Additionally, the Llama 3 8B model is relatively small. In real-world applications, more commonly used models might include Llama 3 70B or GPT-4, accessed via API. How does the proposed algorithm perform on these state-of-the-art language models?

### Questions
see weakness 2

### Soundness
3

### Presentation
3

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
This paper tackles the challenges of learning discrete prompts for large language models (LLMs) in the context of imbalanced data distributions. The authors integrate pairwise AUC loss into a policy gradient optimization framework and introduce a doubly policy gradient approach. To improve stability, they introduce the variance-reduced doubly policy gradient estimator (VR-DPGE) and the STORM technique into their method, momentum-based discrete prompt learning with doubly policy gradient (mDP-DPG). They demonstrate their method with theoretical proof and experimental results.

### Strengths
1. the paper presents a novel approach for optimizing prompts in the context of imbalanced classification problems with LLMs.  The authors introduce VR-DPOGE and STROM strategy to  effectively address the dual variance involved in gradient calculation. 
2. The paper offers rigorous theoretical guarantees for the mDP-DPG method. Additionally, the experimental results validate the effectiveness of the approach, demonstrating a clear advancement over baselines across diverse imbalanced text classification datasets.

### Weaknesses
The paper lacks sufficient explanation on how it addresses the stated problem.

For instance, while the authors introduce the "unbiased VR-DPGE estimator," they do not provide adequate references for VR-DPGE, nor do they explain how Equation (8) specifically reduces variance. Some notation such as $T^{(k)}$  used in Equation (8) is not clearly defined.

A similar issue arises with the STORM strategy, where there is no explanation of the role of momentum. The equation appears only within the algorithm section. There is no definition on the  proj$_{C}$ function.

The theoretical results also require further discussion on what the theorem indicates about the resulting prompts.

### Questions
1. Please provide more intuitive discussion on how the VR-DPOGE and STORM strategy can reduce the variance of gradient estimation.

2. The paper assumes  independent categorical distribution on each token distribution, and proves that this distribution will converge. However, will the distribution converge to a delta distribution centered on a single optimal prompt? Could a correlated distribution over prompt tokens lead to convergence on such a single optimal prompt and potentially improving performance?

3. In Tables 1 and 2, several AUC values fall below 0.5. What could be the possible reasons for this performance being worse than a random guess?

### Soundness
4

### Presentation
3

### Contribution
3
