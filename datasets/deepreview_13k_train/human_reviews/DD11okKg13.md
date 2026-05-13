# Exploring the Effectiveness of Object-Centric Representations in Visual Question Answering: Comparative Insights with Foundation Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Object-centric (OC) representations, which represent the state of a visual scene by modeling it as a composition of objects, have the potential to be used in various downstream tasks to achieve systematic compositional generalization and facilitate reasoning. However, these claims have not been thoroughly analyzed yet.
Recently, foundation models have demonstrated unparalleled capabilities across diverse domains from language to computer vision, marking them as a potential cornerstone of future research for a multitude of computational tasks.
In this paper, we conduct an extensive empirical study on representation learning for downstream Visual Question Answering (VQA), which requires an accurate compositional understanding of the scene. 
We thoroughly investigate the benefits and trade-offs of OC models and alternative approaches including large pre-trained foundation models on both synthetic and real-world data, and demonstrate a viable way to achieve the best of both worlds. 
The extensiveness of our study, encompassing over 600 downstream VQA models and 15 different types of upstream representations, also provides several additional insights that we believe will be of interest to the community at large. % into the VQA performance across different scenarios and its connection with other downstream and upstream performances of the models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a comprehensive empirical study comparing object-centric (OC) representations with foundation models on Visual Question Answering tasks. Through extensive experiments involving 15 different upstream models, the authors demonstrate that combining object-centric bias with foundation models can achieve strong performance while reducing computational costs compared to using foundation models alone.

### Strengths
- Extensive empirical evaluation across different upstream and downstream models and datasets
- Experimental results thoroughly support and validate each insight presented

### Weaknesses
 - While the study includes VQA-v2, it primarily relies on synthetic datasets. The evaluation would be more compelling if it included additional established real-world VQA datasets such as GQA or CRIC. Each image in the GQA and CRIC datasets is associated with a scene graph describing the image's objects, attributes, and relations. Moreover, questions in these datasets involve multiple reasoning skills, spatial understanding, and multi-step inference, making them ideal for analyzing object-centric models.
- The majority of claims and findings are based on synthetic datasets, which feature simpler scenes with clear object-background separation. This raises concerns about the generalizability of the findings to more complex real-world scenarios. It would be great if the author can provide additional analysis on the challenging datasets such as GQA and CRIC
- The downstream architecture is limited to BERT-style transformer encoders. The authors should explore decoder-based transformer architectures, which have become increasingly popular and achieved more favorable results than BERT-style encoders on VQA tasks in recent research.
- While the authors claim they evaluated 640 downstream models, the paper lacks sufficient detail and analysis regarding these experiments. They should provide comprehensive information about these models in the paper

### Questions
- How would the proposed approach perform on more challenging real-world datasets like GQA or CRIC? 
- How would the findings about the benefits of object-centric representations translate to more challenging scenarios in real datasets?
- Why did the authors choose to focus on transformer encoder architectures for downstream models? Would incorporating decoder-based architectures potentially lead to different conclusions?
- Could the authors provide more detailed analysis of experiments with 640 downstream models?

### Soundness
2

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
This paper presents a comprehensive empirical study of Object-Centric (OC) representations in VQA task. The study evaluates 15 different upstream models across three synthetic datasets and one real-world dataset. The authors draw conclusions on the comparison foundation models and OC models, the relation of VQA performance and intermediate tasks or metrics, the training data efficiency and so on.

### Strengths
I appreciate the authors' great efforts (and also their GPU cluster's) of this empirical study. The paper shows empirical rigor through its extensive experimental design, with multiple trials across various models and datasets. The experiments brings credibility to the conclusions, while the conclusions themselves could provide valuable insights for the field.

### Weaknesses
 - Some findings align with existing intuitions. For example, it is not suprising that large foundation models perform comparably to specialized OC models, and that their combination yields better performance. While valuable, these conclusion is intuitive and somehow obvious to the maching learning field.
- The correlation between property/attribute accuracy and overall VQA performance may be due to the characteristics or preference of the selected 4 datasets, rather than a fundamental relationship. This correlation might not generalize well to relational or reasoning or logical questions, potentially make the conclusion less convincing.
- While there are many real-world QA datasets like VCR, GQA, DAQUAR which would capture more general data intrinsics of QA question, only one real-world dataset (VQA-v2) was used in this work. The three synthetic datasets is quantitatively extensive, but might exhibit construction biases or preferences and not capture the full complexity of real-world scenarios. Focusing on more diverse real-world datasets would strengthen the conclusions

### Questions
Minor: I wonder how is the "640" computed on Line 315? And the "640 models" is slightly misleading, as they are actually different are experimental configurations rather than distinct model architectures.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This is an experimental paper that examines how object-centric (OC) representations, which treat scenes as compositions of objects, compare with large pre-trained foundation models in Visual Question Answering (VQA) tasks.

### Strengths
Using object features to represent images to solve VQA has become quite popular since the bottom-up attention (from Peter Anderson et al.). However, there have been many debates about whether the object-level feature makes it work or whether it is just because the image representation model used in BUTD was better trained (with more data). This paper tried to solve this problem by running many experiments.

### Weaknesses
1. The question that this paper wants to answer is: whether OC, fixed-region or global representation is better for VQA. To answer this question, the authors need to provide a model with the same architecture, model size and pre-training data. The only variant in the model is the feature representation way, i.e., OC, fixed-region or global. However, I didn't find this experiment in the paper. Maybe I missed it.

2. Synthetic data such as CLEVR and CLEVRTex are not challenging enough since the objects can be easily detected (and even hard-coded). Many symbolic methods have solved these datasets with 100% accuracy.

3. I am not sure how these takeaway messages could contribute to the community. Some conclusions are already known such as : ' Consistency of the Results Across Question Types.'

### Questions
See weakness, I would like to see the responses to the above three weaknesses.

### Soundness
2

### Presentation
4

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
This paper explores the effectiveness of object-centric (OC) representations in the Visual Question Answering (VQA) task and compares them with traditional large-scale pretrained foundation models.

### Strengths
1. The experimental design is rigorous, considering the impact of multiple factors on the task.
2. The writing is fluent, and the conclusions are clear.
3. The finding that object-centric representations are effective in VQA tasks is insightful for the community.

### Weaknesses
1. As stated in the paper, the datasets would have included more real-world data.
2. Some analysis of the application of the findings is lacking.

### Questions
1. What makes me curious is what the performance would be after fine-tuning the foundation models on the specific VQA tasks, since other models have been fitted on the data. I suppose this would make it more fair for the comparison of different models and may inspire more insights.
2. Could you give some more insights on the application of the findings in the paper? I'm wondering if the conclusions would be applied in other domains out of VQA.

### Soundness
3

### Presentation
3

### Contribution
3
