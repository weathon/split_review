# On the Importance of Language-driven Representation Learning for Heterogeneous Federated Learning

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Non-Independent and Identically Distributed (Non-IID) training data significantly challenge federated learning (FL), impairing the performance of the global model in distributed frameworks. Inspired by the superior performance and generalizability of language-driven representation learning in centralized settings, we explore its potential to enhance FL for handling non-IID data. In specific, this paper introduces FedGLCL, a novel language-driven FL framework for image-text learning that uniquely integrates global language and local image features through contrastive learning, offering a new approach to tackle non-IID data in FL. FedGLCL redefines FL by avoiding separate local training models for each client. Instead, it uses contrastive learning to harmonize local image features with global textual data, enabling uniform feature learning across different local models. The utilization of a pre-trained text encoder in FedGLCL serves a dual purpose: it not only reduces the variance in local feature representations within FL by providing a stable and rich language context but also aids in mitigating overfitting, particularly to majority classes, by leveraging broad linguistic knowledge. Extensive experiments show that FedGLCL significantly outperforms state-of-the-art FL algorithms across different non-IID scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces FedGLCL, a FL framework designed to improve the handling of non-IID data in FL environments. The authors leverage language-driven representation learning (e.g. CLIP, as opposed to label driven), incorporating a pre-trained text encoder to stabilize feature representations. This approach enables the alignment of local image features with a global text feature space, reducing feature disparity across clients. Experiments demonstrate that FedGLCL outperforms traditional label-driven FL methods in various non-IID scenarios, including label and feature distribution skew.

### Strengths
1. The proposed method is novel - mitigating non-iid data issue in FL on image classification pre-training with text encoders.

2. The experiment results are good, the authors experimented on many datasets, comparing against many baselines, highlighting the generalizability of their method. 

3. The author provided theoretical guarantees to the generalizability of the proposed method.

### Weaknesses
1. The use of image-text pre-training is prevalent, and the non-iid data issue is not limited to FL settings, so adding text encoders to mitigate the non-iid issue shouldn't be new. Honestly I am not familiar with the FL literature, so I don't know how much this would add to the FL community. 

2. The experiments are somewhat limited to small-scaled datasets. Performing experiments on larger scaled datasets (e.g. Imagenet) would make the claims stronger.

### Questions
In this paper, federated learning is applied to a specific type of image-text pre-training. I suggest to make this clear in the abstract and throughout the paper - as there are also other types of federated learning as well (e.g. text only)

158 - 161: Can you explain more how your work differs from other works that uses CLIP in FL training (e.g. Lu et al., 2023, Guo et al., 2023, Shi et al., 2023)? In particular - what is "the philosophy of language-driven representation learning"?

### Soundness
3

### Presentation
2

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
This paper proposes a novel approach, FedGLCL, to learn image models in non-IID federated settings. Their approach leverages a fixed frozen set of class embeddings (from a language model) and locally updates image representations in a CLIP-like contrastive manner. When tested on multiple variations of non-IID federated learning benchmarks (e.g. significant label shift/imbalance), this approach is shown to notably outperform other training/aggregation-based interventions without introducing additional computation/communication costs. Furthermore, the authors provide several additional ablations and theoretical analyses to deepen understanding of their results.

### Strengths
**Originality and Significance.** Federated learning with non-IID client data is a well-motivated/challenging problem and the authors' approach, while simple, is novelly and effectively applied in this setting. As mentioned in Sec 5.4, this approach also importantly does not come with any decreases in efficiency. 

**Quality.**  Overall, the results for their method are quite strong compared to a variety of baselines and on several variations of the evaluations. The authors also did a great job ablating aspects of their method (particularly in the Appendix), addressing several of the questions that came up while I was reading the paper. In particular, I appreciated the ablations on the text embeddings, which show that it is important to both (1) keep the embeddings fixed; (2) use a pre-trained language model instead of custom class embeddings. These help establish that contrastive-style training itself is not the main explainer for good performance. 

**Clarity.** Generally, l found the paper to be well-written and easy to follow. Particularly, the authors did a good job contextualizing their methods/results with previous works.

### Weaknesses
 **More discussion about the impact of language supervision.** One result I found particularly curious (and which I believe should be highlighted more in the main paper) was that using embeddings for randomly mismatched class names results in comparable performance to using embeddings for the correct class names. Before seeing this result, I would have thought that the semantic information and relationships between classes was being usefully leveraged (e.g., similar classes being closer together in text embedding space). But based on this result, I'm not sure then to what extent the "broad linguistic knowledge" emphasized in the abstract is important in explaining FedGLCL's success? Perhaps the authors can expand upon their discussion of this in the Appendix and comment more. 

 **Measuring the impact of FedGLCL-style training in centralized/IID-Federated settings** It would be interesting to see how well the contrastive style training from FedGLCL performs in the non-federated setting (and perhaps also the IID federated setting). This would shed light on whether the gains in the non-IID federated setting might also be explained by the contrastive learning approach in FedGLCL-being more effective generally on these tasks v.s. if it is uniquely helpful for overcoming challenges in non-IID federated settings. Relatedly, it would also be nice to discuss your results in relation to Fang et al., 2022 (https://arxiv.org/abs/2205.01397), which included results assessing the impact of language supervision on CLIP pre-training. in their case, they find that it does not have a major impact on the final robustness of CLIP models.

 **Standard errors for results.** It would be nice if the empirical results came with standard errors. That being said, I can acknowledge that the current gaps between the proposed method and previous baselines seem to be large/consistent across evaluation settings and that repeated runs might be costly.

### Questions
Most questions I had were covered in the Weaknesses section. The only other question I had was if you considered any settings involving pretrained image models. On the surface, this might better reflect practical deployments for image-based tasks?

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
The paper presents FedGLCL, a novel federated learning (FL) framework designed to address the challenges posed by non-Independent and Identically Distributed (Non-IID) data. The framework leverages a pretrained VLM, CLIP, specifically through contrastive learning that integrates global language and local image features. The proposed method aims to harmonize feature learning across different clients, reducing variance in local representations and mitigating overfitting to majority classes. The paper includes extensive theoretical and empirical analyses, demonstrating the superiority of FedGLCL over state-of-the-art FL algorithms in various non-IID scenarios.

### Strengths
1. The utilization of large pretrained CLIP into FL is a unique and innovative direction. By leveraging contrastive learning to align local image features with global textual data, the paper proposes a novel solution to tackle the Non-IID problem.
2. The paper provides a solid theoretical foundation for FedGLCL, explaining how the framework can mitigate issues related to Non-IID data. This theoretical backing strengthens the credibility of the proposed method.
3.The authors conduct a comprehensive set of experiments, comparing FedGLCL with multiple state-of-the-art FL algorithms across different non-IID scenarios. The results demonstrate significant improvements, validating the effectiveness of the proposed framework.

### Weaknesses
1. Clarity and presentation issue: It is not clear which pretrained vision language models are used in the experiments. CLIP? Align? BLIP? The paper mentions using a pretrained VLM, but does not specify which one, making it difficult to assess the specific contributions and limitations of the chosen model.

2. It is better to compare the performance of different text encoders from various pretrained VLMs, because the proposed method heavily relies on the pretrained text encoder. The performance of the framework might be sensitive to the choice of text encoder, and a comparison would provide insights into the robustness of the method.

### Questions
Are the datasets used in the experiments part of the pretraining of VLMs? If this is the case, then your framework achieves better performance is due to the pretraining stage.

### Soundness
3

### Presentation
3

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
This paper solves the heterogeneous federated learning (in the image classification field) via a pre-trained and fixed text encoder (BERT) on the server and learned image encoders on the clients. The classification is done by clip-style image-text embedding similarity comparison. The authors report superior performance over traditional heterogeneous federated learning methods (FedAvg, etc.), and provide scalability analysis, efficient analysis, and ablation study.

### Strengths
1. The proposed method shows superior performance.
2. Comprehensive analysis is provided.
3. The usage of Bert embedding as a prototype vector for FL image classification is novel.

### Weaknesses
1. There are few comparisons with prototype FL (like [1] and [2]).
2. The method proposed has some limitations. It is restricted to image classification and requires a pre-trained model that can give good embeddings of the classification labels. This seems to exclude many FL scenarios. (I am not to say that using Office-Caltech-10 and DomainNet is not enough. I just wonder if it may not be as versatile as FL methods like FedAvg. Yet I still appreciate this paper as a good method for image classfication.)

### Questions
1. Comparison/Detailed discussion about prototype FL
2. Can it be adjusted for tasks besides image classification?
3. Can traditional word embedding such as Glove also achieve a performance comparable to Bert's? (just curious about this)

### Soundness
3

### Presentation
2

### Contribution
2
