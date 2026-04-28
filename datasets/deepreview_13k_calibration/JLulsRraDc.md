# Bridging the Gap Between Foundation Models and Heterogeneous Federated Learning

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 5

## Abstract
Federated learning (FL) offers privacy-preserving decentralized machine learning, optimizing models at edge clients without sharing private data. Simultaneously, foundation models (FMs) have gained traction in the artificial intelligence (AI) community due to their exceptional performance across various tasks.  However, integrating FMs into FL presents challenges, primarily due to their substantial size and intensive resource requirements. This is especially true when considering the resource heterogeneity in edge FL systems. We present an adaptive framework for Resource-aware Federated Foundation Models (RaFFM) to address these challenges. RaFFM introduces specialized model compression algorithms tailored for FL scenarios, such as salient parameter prioritization and high-performance subnetwork extraction. These algorithms enable dynamic scaling of given transformer-based FMs to fit heterogeneous resource constraints at the network edge during both FL's optimization and deployment stages. Experimental results demonstrate that RaFFM shows significant superiority in resource utilization efficiency and uses fewer resources to deploy FMs to FL. Despite the lower resource consumption, target models optimized by RaFFM achieve performance on par with traditional FL methods applied to full-sized FMs. This is evident across tasks in both natural language processing and computer vision domains.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a method to optimise training of large models with Federated Learning. The designed a salient parameter prioritisation and a submode extraction method that is tailored for foundation models and they show that this method can help us train larger foundation models even within resource-restricted clients.

### Strengths
- The paper is well written and easy to understand. 
- The transformer-focused salient parameter prioritisation is an interesting idea and a good contribution of this paper 
-  The evaluation is quite thorough, showing results on a number of benchmarks and settings. 
- The authors evaluated the communication cost and the memory footprint of their approach. It was great to see these results being included. 
- Overall, thee results show good improvements over the state of the art.

### Weaknesses
The main weakness of this paper is the overall novelty factor. As the authors mention, there are a lot of works that recently introduced sub-model training to optimise device resources for training larger models with FL. While this method is tailored for transformer-based foundation models, the main differences to existing works are somewhat limited. Having said that, there are contributions such as the saliency metric.

### Questions
Some areas where the authors could improve:

- Maybe the authors can motivate a bit more on the motivation to train larger Foundation models with federated learning. Typically we might train those on public tasks. Is FL  mostly targeting the fine-tuning part ? Overall, an expanded motivation would be great. 

- Maybe some discussion about privacy could be good to have. For example, how well does this method work with Differential privacy (noise), gradient clipping etc. I don't think there is a need to show these results, but maybe consider discussing these aspects. 

- While speedups of ~2x were shown for smaller FM (e.g, bert base), and reduced memory cost,  I was wondering if this is enough to train on resource constrained devices (e.g., mid-range mobile phones). In figure 3, memory in the order of 200GB is shown. I was wondering if this can be broken down to better show the memory requirements during training for end-devices. Maybe provide some numerical results wrt to the time it would require to compute a single round for a range of end-user devices.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a resource-aware federated foundation models training framework called RaFFM. RaFFM assigns different sub-models to clients for local training based on neuron saliency and client computational resource constraints, which allows all clients in the FL to train FMs under the scenario of limited computational resources and uneven distribution.

### Strengths
S1: The problem of how to train FMs in FL scenarios with limited and unevenly distributed computational resources studied in the paper is a practical one, which is partially alleviated by the proposed approach.
S2: The proposed method can save the communication overhead while guaranteeing the performance of the global model and is effectively combined with PEFT methods for various FMs.

### Weaknesses
W1: The method proposed in the paper to select neurons to be retained based on saliency lacks novelty. First, the use of the L1-norm measure of neuron parameter saliency is just a simple use of an existing method [1]. Second, the strategy of ranking the saliency to select neurons is also commonly used in the field of model pruning [2]. Third, the paper does not make it clear why it is necessary to apply a special significance prioritization strategy to the transformer. The paper does not adequately justify why a standard pruning approach would be insufficient, especially given that the L1-norm is a common metric used in such methods. It is unclear what specific properties of the transformer architecture necessitate a different approach, and how this proposed method differs beyond simply reordering weights based on the L1 norm.
W2: Comparisons with relevant baseline methods are lacking in the paper. Methods that extract submodels from the original model for local training have been investigated, such as in [3]. The paper needs to compare against methods that perform sub-model extraction for federated learning, and not just general federated learning methods. The current lack of comparison makes it difficult to assess the true contribution of the proposed method.
W3: The description of the experimental setup of the paper is not clear, for example: 1) The scenario in the paper is client computing resource heterogeneity, and the experimental part does not introduce the distribution of the sub-model size held by each client; 2) The hyper-parameter settings in the experimental part are not listed, which makes it difficult to reproduce the experiments; 3) The distribution of the data between the clients is not introduced, and there is a lack of experiments on the part of the heterogeneity of the data. The paper needs to provide a clear description of the resource constraints on each client, including the size of the sub-models they can handle. Furthermore, the paper should include details on the hyperparameter settings used for training, and the data distribution across clients, including the degree of data heterogeneity.

### Questions
See Weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a comprehensive and timely approach to integrating FMs with FL, a topic of significant relevance in the era of privacy-preserving AI. It provides a comprehensive experimental setup, employing diverse benchmarks and datasets across both NLP and computer vision tasks.

### Strengths
The quantitative analysis is thorough, covering multiple performance metrics and offering a comparative evaluation against baseline federated learning models.

### Weaknesses
The paper suffers from organizational and presentational issues, making it somewhat challenging to navigate.

Abstract:
- Some claims in the Abstract are a bit vague. For example, the authors mention RaFFM shows "significant superiority in resource utilization efficiency." What metrics are used to measure this superiority? How “significant” are the improvements?
- Further, the authors claim that the performance is "on par with traditional FL methods applied to full-sized FMs." This statement would benefit from quantification, if possible. Is it a 1% difference in performance, or is it negligible?
- The abstract mentions that the framework is effective "across tasks in both natural language processing and computer vision domains." This is a broad claim. Please specify if there any limitations or specific conditions under which this is true.

Introduction:
- The problem statement could be more explicit and clearer. The authors mention the challenges of integrating FMs into FL but do not clearly delve into why this integration is crucial. For example, “Given the superior strengths of FMs in few-shot transfer learning, they appear well-suited for non- IID FL environments.” This sentence: a) assumes that Foundation Models have "superior strengths" in few-shot transfer learning without providing evidence or citations to support this claim. This is a strong statement that requires substantiation. b) The sentence implies a logical connection—that because FMs are good at few-shot transfer learning, they are well-suited for non-IID FL environments. However, it does not explain why this would be the case. The logical leap is not self-evident and needs justification.
- “fine-tuning FMs typically requires approximately seven times the resources compared to inference.” This is an interesting point but is presented without reference or further elaboration.
- Consider improving the logical flow and cohesion when transitioning from the problem statement to the proposed solution.
- While the authors discuss the technical aspects, the broader impact of this work is not adequately addressed. For example, how will RaFFM contribute to the field of FMs/FL?
- The key contributions could be more specific (despite some descriptions in the paragraph before the bullet points). For example, what are "specialized FM compression algorithms"? How are they specialized, and why is this significant? Also, claims such as "enhanced resource utilization," “significant reduction in communication overhead” could benefit from clearer quantification and specification, if possible.

Background:
- The discussion about FL somewhat lacks depth and may benefit from improved cohesion as it feels disjointed. For example, the authors mention “a representative FL algorithm is FedAvg” but do not explain why it is representative or how it works.
- The authors mention that FL is a preferred choice in sectors like healthcare but do not elaborate on why this is the case. A sentence (or citation) or two providing context could be beneficial.
- Phrases like "often lead to training failures" and "poor model convergence and performance" are vague. What constitutes a "training failure"? How poor is "poor performance"? Consider adding some citations to support these claims at least.
- Similar problem to the problem statement. The authors mention that there is a gap between traditional model training and FL, particularly in heterogeneous FL-edge environments. However, the nature of this gap is not clearly articulated. Is it a technological gap, a performance gap, or something else?
- The term “resource-hungry” has been mentioned several times so far but it is somewhat ambiguous. Is it computational resources, memory, or something else? Furthermore, in the context of the paper, it seems “resource-hunger” would be more fitting, given it has been properly explained?

Methodology:
- This section reads a bit like a mix of existing solutions and proposed solution (especially the opening part of the first subsubsection “SALIENT PARAMETER PRIORITIZATION”). This lack of clear demarcation can lead to confusion for the reader and dilutes the focus of the section. Consider maybe moving some of the discussion on model compression/scaling, the review of existing solutions, and how the proposed work differs or improves upon existing ones.

### Questions
Abstract:
- Some claims in the Abstract are a bit vague. For example, the authors mention RaFFM shows "significant superiority in resource utilization efficiency." What metrics are used to measure this superiority? How “significant” are the improvements?
- Further, the authors claim that the performance is "on par with traditional FL methods applied to full-sized FMs." This statement would benefit from quantification, if possible. Is it a 1% difference in performance, or is it negligible?
- The abstract mentions that the framework is effective "across tasks in both natural language processing and computer vision domains." This is a broad claim. Please specify if there any limitations or specific conditions under which this is true.

Introduction:
- The problem statement could be more explicit and clearer. The authors mention the challenges of integrating FMs into FL but do not clearly delve into why this integration is crucial. For example, “Given the superior strengths of FMs in few-shot transfer learning, they appear well-suited for non- IID FL environments.” This sentence: a) assumes that Foundation Models have "superior strengths" in few-shot transfer learning without providing evidence or citations to support this claim. This is a strong statement that requires substantiation. b) The sentence implies a logical connection—that because FMs are good at few-shot transfer learning, they are well-suited for non-IID FL environments. However, it does not explain why this would be the case. The logical leap is not self-evident and needs justification.
- “fine-tuning FMs typically requires approximately seven times the resources compared to inference.” This is an interesting point but is presented without reference or further elaboration.
- Consider improving the logical flow and cohesion when transitioning from the problem statement to the proposed solution.
- While the authors discuss the technical aspects, the broader impact of this work is not adequately addressed. For example, how will RaFFM contribute to the field of FMs/FL?
- The key contributions could be more specific (despite some descriptions in the paragraph before the bullet points). For example, what are "specialized FM compression algorithms"? How are they specialized, and why is this significant? Also, claims such as "enhanced resource utilization," “significant reduction in communication overhead” could benefit from clearer quantification and specification, if possible.

Background:
- The discussion about FL somewhat lacks depth and may benefit from improved cohesion as it feels disjointed. For example, the authors mention “a representative FL algorithm is FedAvg” but do not explain why it is representative or how it works.
- The authors mention that FL is a preferred choice in sectors like healthcare but do not elaborate on why this is the case. A sentence (or citation) or two providing context could be beneficial.
- Phrases like "often lead to training failures" and "poor model convergence and performance" are vague. What constitutes a "training failure"? How poor is "poor performance"? Consider adding some citations to support these claims at least.
- Similar problem to the problem statement. The authors mention that there is a gap between traditional model training and FL, particularly in heterogeneous FL-edge environments. However, the nature of this gap is not clearly articulated. Is it a technological gap, a performance gap, or something else?
- The term “resource-hungry” has been mentioned several times so far but it is somewhat ambiguous. Is it computational resources, memory, or something else? Furthermore, in the context of the paper, it seems “resource-hunger” would be more fitting, given it has been properly explained?

Methodology:
- This section reads a bit like a mix of existing solutions and proposed solution (especially the opening part of the first subsubsection “SALIENT PARAMETER PRIORITIZATION”). This lack of clear demarcation can lead to confusion for the reader and dilutes the focus of the section. Consider maybe moving some of the discussion on model compression/scaling, the review of existing solutions, and how the proposed work differs or improves upon existing ones.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
