# Tuning-Free Accountable Intervention for LLM Deployment - A Metacognitive Approach

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 8, 5

## Abstract
Large Language Models (LLMs) have catalyzed transformative advances across a spectrum of natural language processing tasks through few-shot or zero-shot prompting, bypassing the need for parameter tuning. While convenient, this modus operandi aggravates ``hallucination'' concerns, particularly given the enigmatic ``black-box'' nature behind their gigantic model sizes. Such concerns are exacerbated in high-stakes applications (e.g., healthcare), where unaccountable decision errors can lead to devastating consequences. 
In contrast, human decision-making relies on nuanced cognitive processes, such as the ability to sense and adaptively correct misjudgments through conceptual understanding. Drawing inspiration from human cognition, we propose an innovative \textit{metacognitive} approach, dubbed \textbf{CLEAR}, to equip LLMs with capabilities for self-aware error identification and correction. Our framework facilitates the construction of concept-specific sparse subnetworks that illuminate transparent decision pathways. This provides a novel interface for model \textit{intervention} after deployment. Our intervention offers compelling advantages:
(\textit{i})~at deployment or inference time, our metacognitive LLMs can self-consciously identify potential mispredictions with minimum human involvement, (\textit{ii})~the model has the capability to self-correct its errors efficiently, obviating the need for additional tuning, and (\textit{iii})~the rectification procedure is not only self-explanatory but also user-friendly, enhancing the interpretability and accessibility of the model. By integrating these metacognitive features, our approach pioneers a new path toward engendering greater trustworthiness and accountability in the deployment of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a study in the context of Large Language Models (LLMs): 1) to automatically identify erroneous inputs, 2) to handle erroneous inputs to increase the model's performance, and 3) to interpret the model's prediction.

The proposed methodology explores two ways to handle erroneous examples. The first one is 
increasing the the number of top experts, top-T to make an ensemble decision without further training.
The second one is to modify the number of experts in the training process. The authors gradually increase the number of top-T experts after a fixed number of epochs.

The retrospective accountability component explains similar to the transformer's attention visualization.

### Strengths
Provides an interpretation and identifies erroneous examples in LLM blackbox training.

### Weaknesses
The authors identified erroneous prediction by automatically dividing confidence into two groups via K-means clustering (Section 3.2). The subset of examples with a lower confidence group is flagged as erroneous.

While this approach eliminates human involvement, this approach has several limitations. First, the K-means is not robust against outliers. In many real-world scenarios, such as predicting 
malicious vs. non-malicious users on the web, and predicting bug vs. non-bug features in software security---the class binary classification task is imbalanced. Thus, automatically setting the threshold
might not be the right way. 

Second, to handle the erroneous examples, the authors presented two approaches: increasing the number of top-T experts at the inference time and gradually increasing the number of top-T experts. 
However, none of the approaches handle "erroneous" examples. Instead, both approaches focus on increasing the top-T experts. A better approach could be similar to active learning or machine teaching---focusing on the subset of erroneous inputs and learn to improve prediction accuracy.


Third, the approaches described in Appendix A involve extracting latent representation Z of text encoder, x, and then adding an extra layer of concept representation R^K and class label. 
The authors did not report whether their model overfits.

### Questions
Did the authors examine the model's overfitting?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel framework called CLEAR (Concept-Learning-Enabled metAcognitive inteRvention), designed to enhance the reliability of Large Language Models (LLMs) by enabling them to self-identify and correct errors during deployment. CLEAR is inspired by aspects of human cognition and builds upon the Mixture of Experts (MoE) concept. The proposed method was tested on a test classification dataset. The framework aims to mitigate issues related to the black-box nature of LLMs, the reliance on domain experts for error identification, and the challenges of targeted intervention given the complexity and size of these models.

### Strengths
1. The paper is well-written, and the main content is easy to understand.
2. The paper involves a chain of MoE, self-corrections by expanding experts, and hindsight explanation through backtracking to mitigate the issue of the black-box nature of LLMs. The proposed methods are empirically justified on two NLP text classification datasets.

### Weaknesses
1. [Novelty] The use of Mixture of Experts on LLMs is not new. The authors should at least discuss the differences between previous works [1,2] and their own. Specifically, the paper should clarify how its approach to MoE differs from methods that focus on improving overall model performance or efficiency, and instead leverages MoE for metacognitive capabilities such as error detection and correction.
2. [Black-box intervention] The model still uses an open-source LLM, T5, as its backbone, enabling access to its intermediate layers $z$ to generate concepts $c$ and labels $y$. This significantly reduces its applicability to other API-based LLM models, like GPT-3 and GPT-4. The paper needs to address the limitations of relying on white-box access to the LLM and discuss potential methods for adapting the framework to black-box models, such as through prompt engineering or zero-order optimization techniques.
3. [Complexity and Scalability] The authors do not discuss the computational overhead of adding more experts (LLM backbones) and the trade-off between improving model performance and adding extra experts. Furthermore, in Table 2, the authors only test CLEAR on T5-base. It would be interesting to see the behavior of the proposed method on larger LLMs (like LLaMA 2 13B or Mistral 7B), but with fewer expert layers. The paper should include a more detailed analysis of the computational cost associated with increasing the number of experts, and explore the performance of the method on larger LLMs with varying numbers of expert layers to assess its scalability.

### Questions
1. I am curious about how CLEAR ensures that the dynamic adjustment of the expert allocation does not lead to overfitting or catastrophic forgetting when fine-tuning on different tasks on T5-base.
2. Can the Concept Bottleneck Models (CBMs) developed by CLEAR be effectively generalized across diverse domains and applications, or do they require domain-specific tuning?
3. I am confused about the methods shown in Table 2. For instance, for the method ‘prompting’ in the first line, are you simply using prompting on GPT-4 without any help of the MoE and self-correction techniques proposed in CLEAR? If so, it would be much more interesting to see the results of prompting on the LLM backbones for different expert layers within the proposed CLEAR framework without training CBMs.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The method proposed CLEAR which is a metacognitive framework to enable LLMs to self-identify and self-correct errors during deployment. The framework contains two components, 1) the concept learning component which maps latent textual representations to concepts and utilizes MoCEs to learn sparse concept subnetworks, and 2) the metacognitive intervention that dynamically labels and edits the intermediate layer for less erroneous outputs. The resulting method CLEAR outperforms prior methods on both CEBaB and IMDB-C. The model is also more accountable due to its interpretable nature and more efficient since its tunning-free intervention.

### Strengths
1. The paper proposed a framework that is strong performance transparent and accountable. Usually, interpretability and performance are a trade-off, but this paper manages to improve both.
2. MoCEs are a great way of generalizing and not overfitting on particular examples. This is a very natural approach to expand the coverage and capacity without having the downside of overfitting.
3. The inference stage utilizes thresholding and clustering to achieve efficient inference time computation, increasing its practical usability.

### Weaknesses
1. The concepts are pre-defined. This could potentially limit the quality and use case of such a framework. In scenarios where human-annotated concepts are harder to come by or can potentially be inaccurate, this method doesn't have a preventative mechanism for that if I understand it correctly. The reliance on pre-defined concepts also raises concerns about the framework's ability to adapt to novel or nuanced situations where the pre-defined concepts may not fully capture the underlying semantics. This could lead to a performance bottleneck in real-world applications where the data distribution might deviate significantly from the training data.
2. Intervention is tunning-free, but concept-learning components require some finetuning. This method also requires changing the transformer architecture. These raise questions about the adaptability of the framework to a wider range of scenarios. The need for fine-tuning the concept-learning component, while the intervention is tuning-free, introduces a potential inconsistency in the overall framework's adaptability. Furthermore, the requirement to modify the transformer architecture to a Mixture of Experts (MoE) format could limit the framework's ease of integration with existing systems and pre-trained models, potentially hindering its widespread adoption.

### Questions
1. Can this be extended to learn undefined concepts? Or human-annotated concepts have to be provided.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the pressing challenge posed by the deployment of Large Language Models (LLMs). Given the “black box” nature of LLMs, it is hard to point and correct errors due to factors like hallucination post-deployment. To address this, the authors propose a metacognitive approach named CLEAR (Concept-Learning-Enabled metacognitive intervention framework).

The CLEAR framework integrates the features in cognitive science to enable LLMs to understand and work with concept-specific sparse subnetworks. These subnetworks aim to provide transparency in decision-making. With K-Means applied to discriminate against the confidence level, the framework could make automatic error identification and guide the allocation of augmented experts to secure a more reliable prediction.

Empirical studies with the framework are performed on the text classification datasets. Compared to the direct intervention methods, concept bottleneck models, the metacognition intervention achieves better performance.

### Strengths
1. The CLEAR framework offers an innovative metacognitive approach, merging insights from cognitive science with large language model intervention.
2. One of the standout features of CLEAR is its ability to autonomously identify potential mispredictions, reducing the need for human intervention. And the dynamic activation of internal modules for refining concept perception without extra tuning is an efficient way to address errors, adding a layer of adaptability to the LLM.

### Weaknesses
1. Lack of captions on some figures can disrupt the flow of understanding for the reader. 
2. The paper emphasizes its effectiveness through experiments on real-world datasets. However, the scope and diversity of these datasets aren't detailed (only text classification tasks considered in the paper), raising questions about the framework's general applicability.

### Questions
1. Considering the increasing scale and complexity of newer models, is the CLEAR framework compatible with larger models such as LLaMA? Furthermore, can the metacognitive capabilities of the CLEAR approach provide benefits when applied to these more extensive and potentially more intricate architectures?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
