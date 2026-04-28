# Tracing Representation Progression: Analyzing and Enhancing Layer-Wise Similarity

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Analyzing the similarity of internal representations within and across different models has been an important technique for understanding the behavior of deep neural networks. Most existing methods for analyzing the similarity between representations of high dimensions, such as those based on Centered Kernel Alignment (CKA), rely on statistical properties of the representations for a set of data points. In this paper, we focus on transformer models and study the similarity of representations between the hidden layers of individual transformers. In this context, we show that a simple sample-wise cosine similarity metric is capable of capturing the similarity and aligns with the complicated CKA. Our experimental results on common transformers reveal that representations across layers are positively correlated, with similarity increasing when layers get closer. We provide a theoretical justification for this phenomenon under the geodesic curve assumption for the learned transformer, a property that may approximately hold for residual networks. We then show that an increase in representation similarity implies an increase in predicted probability when directly applying the last-layer classifier to any hidden layer representation. This offers a justification for {\it saturation events}, where the model's top prediction remains unchanged across subsequent layers, indicating that the shallow layer has already learned the necessary knowledge. We then propose an aligned training method to improve the effectiveness of shallow layer by enhancing the similarity between internal representations, with trained models that enjoy the following properties: (1) more early saturation events, (2) layer-wise accuracies monotonically increase and reveal the minimal depth needed for the given task, (3) when served as multi-exit models, they achieve on-par performance with standard multi-exit architectures which consist of additional classifiers designed for early exiting in shallow layers. To our knowledge, our work is the first to show that one common classifier is sufficient for multi-exit models. We conduct experiments on both vision and NLP tasks to demonstrate the performance of the proposed aligned training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work studies the feature similarity of neural networks and reveals that: (I) simple-wise cosine similarity can capture representation similarity; (ii) saturation events related with feature similarity and based on this observations, this work proposed a aligned training approach to enhance the representation thus benefit the performance and also the multi-exit inference approach.

### Strengths
- The manuscript is logically organized, including the observations and its applications.
- Both empirical and theoretical justifications are provided.
- The study covers both the vision and language domains.

### Weaknesses
 - Line 342 “To the best of our knowledge, our work is the first to show that one common classifier is sufficient for multi-exit models.” This is not true, a lot of early exiting methods can do with a single classifier heads [1-3].
- Line 240: “Progressively increasing layer-wise representation similarity”, thus observations might be different in other domain[2], is there any insights why autoregressive models seems not have progressively increasing layer-wise representation similarity?
- Missing previous literature[4] which also studies layer-wise cosine similarity, yet in the language domain.

### Questions
Please refer to the weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper focuses on understanding the behavior of deep neural networks, particularly transformer models, by examining the similarity of internal representations across hidden layers. The authors introduce a sample-wise cosine similarity metric that aligns with more complex statistical methods and reveals increasing representation similarity as layers get closer. They provide a theoretical justification for this phenomenon under the geodesic curve assumption and demonstrate that enhanced representation similarity leads to increased predicted probability and earlier saturation events in model predictions. The paper proposes an aligned training method to improve shallow layer effectiveness, resulting in more early saturation events and higher layer-wise accuracies. Finally, the authors show that their approach enables multi-exit models with a single classifier, reducing parameter count and computational complexity while maintaining performance.

### Strengths
In general, the proposed paper is well-written, the author provides detailed experiments, extensive theoretical analysis to analysis the feature pattern in Transformers. Based on these analyses, the author proposes a aligned training method for enhancing shallow layer performance. The proposed method achieves performance gain and speed boost on CV and NLP tasks.

### Weaknesses
In general, I think the proposed paper is well formulated and written. However, I still have some concerns about the paper:

1. I don't think it is useful for enhancing similarity between all Transformer outputs (representations), it may help in simple tasks like image classification and sentence classification. But for complex tasks (like object detection/semantic segmentations), we may not want all representations to be similar. I think similar tasks may exist in NLP tasks (like parsing), Then the author should talk about the limitations or give more experiments to verify the effectiveness of the proposed method.

2. In the paper, the author performs experiments on small datasets and small models, like DeiT trained on CIFAR10 and ImageNet. Also Bert/GPT2 on small NLP tasks. If the data increases, like a pre-trained CLIP/OpenCLIP on large datasets, will the findings/analyses be the same? Moreover, if the model becomes larger (like a LLM like Llama3), will the findings/analyses be the same? Does the saturation events still occur in those models? I'm curious about that.

### Questions
Based on the weaknesses, I have some questions.

1. Is enhancing similarity beneficial for all tasks besides the simple classification task?

2. When enlarging the data/model size, will the method/analyses still works?

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
2

### Summary
This paper focuses on the analysis of layer-wise representations of Transformers. They demonstrates a series of beneficial observations, e.g., representations across layers are positively correlated. Meanwhile, they find the model's top prediction remains unchanged across subsequent layers. Following the observation, they further propose an aligned training strategy to improve the effectiveness of shallow layer, which is able to provide more early saturation events, minimal depth needed for the given task, multi-exit models.

### Strengths
1. By analyzing the similarity of representations among different layers, the paper demonstrates the possibility of early saturation events and shared classifier among different layers.
2. They further presents a training strategy to improve effectiveness of shallow layers, such that they can enjoy more early saturation events, minimal depth, and so on
3. Some analysis in this paper is insightful, e.g., the shadow layer is able to achieve approaching performance with the depth layer. This might inspire more efficient large model inference.
4. The experiments are comprehensive.

### Weaknesses
1. a small weakness is that the previous approaches have observed this phenomenon that representations in the early layers can also achieve reasonable classifiers, though I think this is a tiny issue.

### Questions
I have a few questions about this submission.
1. According to Figure 6, does the proposed aligned training strategy decrease the performance more clearly in the last layers in large models? Please discuss the performance trade-offs between shallow and deep layers across different model sizes.
2. With the common classifier, is there still a neural collapse phenomenon in the model? Is there any difference of this phenomenon across different layers? I'd like to see some discussions about this.

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
5

### Summary
This paper studied the similarity of representations between the hidden layers of individual transformers and found that a simple cosine similarity metric can be used for similarity evaluation. Experimental results revealed that representations across layers are positively correlated and the authors introduce a multi-exit mechanism. The innovation lies in using the same classifier for different layers.

### Strengths
1. The deduction and experiments in the paper are relatively solid. The authors have made efforts to investigate the similarity of representations across different layers in transformers. 

2. The paper is well-written and easy to follow.

### Weaknesses
Using the same classifier for multi-exit is quite straightforward and its technical contribution seems limited. The experimental results seem not very promising compared with previous multi-exit methods. The authors may need to further enhance the novelty or provide more convincing evidence of the superiority of their approach compared with multi-exit/classifier to make the paper more acceptable.

### Questions
1. Why use linearly increasing weights for aligned losses? Experiments for different choices on weights are preferred.

### Soundness
3

### Presentation
3

### Contribution
3
