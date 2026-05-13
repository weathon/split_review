# HaDeMiF: Hallucination Detection and Mitigation in Large Language Models

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
The phenomenon of knowledge hallucinations has raised substantial concerns about the security and reliability of deployed large language models (LLMs). Current methods for detecting hallucinations primarily depend on manually designed individual metrics, such as prediction uncertainty and consistency, and fall short in effectively calibrating model predictions, thus constraining their detection accuracy and applicability in practical applications. In response, we propose an advanced framework, termed HaDeMiF, for detecting and mitigating hallucinations in LLMs. Specifically, hallucinations within the output and semantic spaces of LLMs are comprehensively captured through two compact networks—a novel, interpretable tree model known as the Deep Dynamic Decision Tree (D3T) and a Multilayer Perceptron (MLP)—which take as input a set of prediction characteristics and the hidden states of tokens, respectively. The predictions of LLMs are subsequently calibrated using the outputs from the D3T and MLP networks, aiming to mitigate hallucinations and enhance model calibration. HaDeMiF can be applied during both the inference and fine-tuning phases of LLMs, introducing less than 2% of the parameters relative to the LLMs through the training of two small-scale networks. Extensive experiments conclusively demonstrate the effectiveness of our framework in hallucination detection and model calibration across text generation tasks with responses of varying lengths.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the issue of knowledge hallucinations in large language models (LLMs), which can undermine their reliability in critical domains. The authors propose a framework called HADEMIF to detect and mitigate hallucinations in LLMs using two compact networks: a Deep Dynamic Decision Tree (D3T) and a Multilayer Perceptron (MLP). These networks capture hallucinations in both the output and internal semantic spaces of LLMs, allowing for prediction calibration and improved reliability.

### Strengths
Comprehensive Detection: HADEMIF captures hallucinations in both output and internal spaces, providing a more holistic approach compared to previous methods that focus on single aspects.

Interpretable Model: The D3T model offers interpretability, allowing for the identification of key characteristics that impact hallucination detection.

Efficiency: The framework introduces less than 2% additional parameters relative to the LLMs, making it efficient in terms of computational resources.

Versatility: HADEMIF can be applied during both inference and fine-tuning phases, enhancing its applicability across different stages of LLM deployment.

Improved Calibration: The framework significantly reduces the expected calibration error and Brier scores, indicating better alignment between model confidence and accuracy.

### Weaknesses
Dependency on Internal States: The approach requires access to the internal states of LLMs, which may not be feasible for black-box models where such access is restricted. This is a significant limitation as many deployed LLMs offer only API access, making it impossible to extract the necessary hidden representations for the proposed framework. The reliance on specific internal layers also introduces a potential fragility; changes in model architecture or layer configurations could necessitate retraining or adjustments to the hallucination detection networks.

Limited Metric Scope: While the framework considers multiple metrics, the scope is still relatively constrained, potentially limiting detection performance in more complex scenarios. The current metrics may not fully capture the nuances of different types of hallucinations, such as logical inconsistencies or subtle factual errors that require deeper semantic understanding. The framework's ability to generalize to unseen types of hallucinations is therefore unclear.

Complexity in Implementation: The integration of two separate networks (D3T and MLP) may increase the complexity of implementation and maintenance. The need to train and manage two distinct models adds overhead, particularly in resource-constrained environments. Furthermore, the interaction between these two networks and their impact on overall performance needs further analysis, as the framework's effectiveness could be sensitive to the training process and hyperparameter settings of both networks.

### Questions
Scalability: How does the framework perform with even larger models or in real-time applications where speed is critical?

Generalizability: Can the framework be adapted to other types of hallucinations beyond those related to factual inaccuracies?

Black-box Applicability: Are there potential adaptations of HADEMIF that could work with black-box models where internal states are not accessible?

Metric Expansion: What additional metrics could be integrated into the framework to enhance its detection capabilities?

User Trust: How does the framework impact user trust in LLMs, and are there ways to quantify this improvement?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces HADEMIF, a framework designed to detect and mitigate hallucinations in large language models (LLMs). It integrates a novel interpretable Deep Dynamic Decision Tree (D3T) for output space analysis and a Multilayer Perceptron (MLP) for internal state analysis. HADEMIF effectively calibrates LLM predictions with minimal parameter increase, enhancing model reliability.

### Strengths
- Originality: Novel use of D3T and MLP for multifaceted hallucination detection.
- Quality: Demonstrated robustness through extensive evaluations, including accuracy and Expected Calibration Error (ECE).
- Clarity: Mostly lear methodology, though technical details may be challenging for broader audiences.

### Weaknesses
 - Some parts in the method lack explanations. For example, before line 184 "Following the approach of DNDT, D3T replaces ..." there should be clearer explanations for the DNDT method
- Limited explanation of the interpretability benefits of D3T in practical application.

### Questions
- Could the authors clarify the choice of metrics (such as consistency [1]) and their weights within D3T? (Line 209 "Extraction of Prediction Characteristics"). Better motivated metric selection would facilitate the understanding of the numeric values for these metrics. 
- Is there a threshold for model applicability when training complexity increases, particularly with LoRA?

[1] Better to Ask in English: Cross-Lingual Evaluation of Large Language Models for Healthcare Queries.

### Soundness
3

### Presentation
3

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
This study introduces HADEMIF, a comprehensive framework for hallucination detection and mitigation in large language models (LLMs). HADEMIF leverages both the output space and internal hidden states of LLMs through two compact networks to effectively identify and reduce hallucinations. The framework is applicable in both inference and fine-tuning stages, and experiments demonstrate its superior performance in hallucination detection and calibration across various open-source LLMs compared to existing methods.

### Strengths
1. The authors integrate multiple metrics to simultaneously assess hallucination in both output space and hidden states, achieving a certain degree of interpretability.
2. The author considers hallucination at multiple levels in the experiments and employs various LLM backbones.

### Weaknesses
1. Is there a direct relationship between calibration and hallucination? This gap has not been clearly addressed. Although some related work is cited in line 45, this key issue underpinning the entire paper has not been convincingly articulated. Furthermore, we observe in the experimental results that the ECE metric, representing calibration, and the acc@50 metric, representing hallucination, show an inverse relationship to some extent in certain methods.

2. In the authors' statement on line 165, they suggest that single metrics may limit the effectiveness of hallucination detection, but this is not substantiated in the paper. To our knowledge, the authors' method can be summarized as manually extracting certain features and feeding them into a deep decision tree, with these features having appeared to some extent in previous work. Therefore, we have reason to doubt that this combination effectively addresses the challenge of discovering metrics for hallucination detection.

3. The authors use an improved DNDT for hallucination detection in the paper, but they did not conduct related ablation experiments to assess the performance difference between D3T and DNDT.

4. During the training process, it appears that the LLM evolves in conjunction with the detector. However, the authors did not specify the initialization of the detector's weights, which we believe could lead to incorrect gradients being applied to the LLM initially, thereby reducing its generalizability. We also note that the authors did not conduct related experiments on this matter.

5. The authors emphasized interpretability. However, they only provided the impact of various metrics on the output space in the experiments, without focusing on the interpretability of metric itself.

6. The authors seemingly did not compare their method with finetune-based methods or methods specifically designed for hallucination mitigation in their experiments. Instead, they only compared it with some calibration methods and lacked data on finetuning the backbone on these training sets. This omission may lead to unfair comparisons when introducing training in their method, and the comparison methods might also be relatively weak.

7. It would be beneficial to provide experimental results on the computational costs of the model due to the introduction of new modules and the calculation of new metrics, especially consistency.

### Questions
Refer to weakness.

### Soundness
2

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
The paper presents a new approach to addressing hallucinations in large language models, a significant issue where models generate nonfactual or incorrect information with high confidence. The proposed framework, HADEMIF, uses two neural networks: a Deep Dynamic Decision Tree (D3T) to detect hallucinations in the output space and a Multilayer Perceptron (MLP) to analyze hidden states in the internal semantic space. These models help calibrate the LLM’s predictions to reduce hallucinations.

### Strengths
1. A comprehensive approach that addresses both external outputs and internal token states for hallucination detection.
2. The framework introduces less than 2% additional parameters, making it lightweight.
3. Extensive experiments to show the reduced hallucination rates.

### Weaknesses
1. Shaky Methodology: The fundamental approach relies on using additional black-box models (D3T and MLP) to detect hallucinations in the LLM, which itself is a black box. This raises concerns about the interpretability and transparency of the method. The use of a Deep Dynamic Decision Tree (D3T) as a black box is particularly concerning, as the decision-making process within the tree is not transparent. While the authors claim interpretability, the specific features and their combinations that lead to a hallucination detection are not clearly elucidated, making it difficult to understand the model's reasoning. Furthermore, the reliance on another black-box model, the Multilayer Perceptron (MLP), to analyze hidden states further compounds the issue of interpretability. The interaction between these models and the LLM remains opaque, hindering a clear understanding of how hallucinations are mitigated. 

2. Unclear Training Data: The paper lacks clarity on where the training data for the D3T and MLP models come from. It is unclear whether hallucinations are labeled manually, generated synthetically, or detected through other processes. This makes it difficult to assess the generalizability of the framework. The absence of a clear explanation regarding the source and nature of the training data for the D3T and MLP models is a significant weakness. Without knowing how the training data is generated or labeled, it is impossible to determine if the models are learning to detect true hallucinations or simply overfitting to a specific dataset. The paper needs to specify whether the training data is manually annotated, synthetically generated, or derived from other automated processes. The lack of transparency in the training data undermines the reliability and generalizability of the proposed framework.

3. Unfair Comparison with Training-Free Methods: The paper compares its method to training-free approaches, like self-consistency, without accounting for the difference in training requirements. A more balanced evaluation against similarly trained methods would provide a clearer picture of its effectiveness. Comparing the proposed method, which requires training additional models, to training-free methods like self-consistency is not a fair comparison. The authors should compare their method against other trained models that also aim to mitigate hallucinations. This would provide a more accurate assessment of the method's effectiveness relative to other approaches that require similar computational resources and training data. The current comparison does not adequately demonstrate the advantages of the proposed method over other training-based approaches.

### Questions
Here are a few questions and suggestions for the authors that could help clarify key points and potentially address limitations in the paper:

1. Training Data Source: Can you provide more detail on how the training data for the D3T and MLP models is collected? Specifically, how are hallucinated outputs labeled and validated? Is there a manual annotation process involved, or are automated methods used for labeling? A clearer explanation of the training data would improve understanding of the framework’s reliability and generalizability.

2. Interpretability of D3T: While the D3T model is described as interpretable, its role as a black-box model is still a concern. Could you provide additional insights or examples on how interpretability is achieved in practice? How does the model allow users to identify key characteristics that signal hallucinations?

3. Comparison with Training-Free Methods: Since you compare HADEMIF to training-free methods like self-consistency, could you clarify why these comparisons are appropriate given that HADEMIF requires additional training? How do you justify these comparisons, and would it be more fair to compare your method against other trained models?

4. Generalization Across Tasks: How well does HADEMIF generalize to different tasks and domains outside those tested in the experiments? Could you discuss whether the framework needs to be retrained or fine-tuned for new tasks, and if so, how this impacts the efficiency of the method?

5. Handling of Complex Scenarios: Can you provide more detail on how HADEMIF handles complex or ambiguous scenarios where there may be no clear factual answer (e.g., open-ended creative writing tasks)? Is the framework likely to flag creative responses as hallucinations in these cases?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a framework for LLM hallucination detection and mitigation that consists of a deep neural decision tree (DNDT) that can detect hallucinations from the prediction characteristics of LLMs, and a multilayer perceptron (MLP) that can detect hallucinations from the internal states of LLMs. One can either calibrate the predictions of LLMs with the DNDT and MLP after optimizing them, or alternate between optimizing them and fine-tuning LLMs. In both cases, the DNDT and MLP are optimized to maximize the log-likelihood calibrated with them. The authors demonstrate the advantages of their framework by comparing its performance to those of existing model calibration methods.

### Strengths
- The authors benchmarked the proposed framework with a comprehensive suite of datasets.
- The paper is mostly easy to follow.

### Weaknesses
My primary concern is whether the proposed framework is indeed better than existing model calibration methods and plain fine-tuning of LLMs:
- The proposed framework introduces more tunable parameters than existing model calibration methods.
- The proposed framework is essentially a composition of three tunable models (a DNDT, an MLP, and an LLM), and I am unconvinced that tuning a composition of three tunable models can fundamentally better reduce hallucination than tuning one tunable model (an LLM). (Maybe some inductive biases in the DNDT help.) The empirical results can be strengthened by comparing the proposed framework against fine-tuning with varying numbers of parameters.

### Questions
I have raised my questions in Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
