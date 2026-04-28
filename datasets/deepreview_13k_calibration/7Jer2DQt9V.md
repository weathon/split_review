# The Unreasonable Effectiveness of Pretraining in Graph OOD

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Graph neural networks have shown significant progress in various tasks, yet their ability to generalize in out-of-distribution (OOD) scenarios remains an open question. In this study, we conduct a comprehensive benchmarking of the efficacy of graph pre-trained models in the context of OOD challenges, named as PODGenGraph. We conduct extensive experiments across diverse datasets, spanning general and molecular graph domains and encompassing different graph sizes. Our benchmark is framed around distinct distribution shifts, including both concept and covariate shifts, whilst also varying the degree of shift. Our findings are striking: even basic pre-trained models exhibit performance that is not only comparable to, but often surpasses, specifically designed to handle distribution shift. We further investigate the results, examining the influence of the key factors (e.g., sample size, learning rates, in-distribution performance etc) of pre-trained models for OOD generalization. In general, our work shows that pre-training could be a flexible and simple approach to OOD generalization in graph learning. Leveraging pre-trained models together for graph OOD generalization in real-world applications stands as a promising avenue for future research.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies how pre-training would impact GNNs' out-of-distribution(OOD) generalization performance. This work benchmarks four pre-training methods on multiple datasets with concept and covariate shifts. The experiments show that GNNs after pre-training would be more robust to OOD issues, and empirically they may perform comparable or better than those methods that are designed specifically to handle those shifts.

### Strengths
1. This paper benchmarks not only the OOD performance of multiple pre-training strategies but also some methods designed for handling distribution shifts, such as those rooted in invariant learning. It's interesting to put them together and compare them directly.
2. Multiple types of shifts are considered in the benchmark.

### Weaknesses
1. It seems to me the key observations are actually known, e.g., pre-training helps graph OOD generalization, especially for molecular tasks, and pre-training improves sample efficiency for labeled data. For example, [1] indeed has claimed their improvement on MoleculeNet with OOD splits, [2] has also summarized graph self-supervision techniques that help/claim OOD generalization. So, I think it's expected to see improvements.
2. I'm not sure how meaningful/resonable to directly compare pre-trained models with those models rooted in principles such as invariant learning. Their exact usage does not seem to be aligned and the level of information used is different.
3. If it is to serve as a comprehensive benchmark for pre-training methods for OOD generalization, I would expect more and newer methods with multiple backbone GNNs.

### Questions
- How did OGBG-HIV and OGBG-PCBA get split exactly for different shifts?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript explores the efficacy of pre-trained models in graph neural networks for out-of-distribution (OOD) scenarios. Through extensive experiments on various datasets, the authors discover that even basic pre-trained models perform as well as or outperform models specifically tailored to handle distribution shifts. The study also delves into the impact of critical factors like sample size and learning rates on the performance of pre-trained models. This research implies that pre-training can serve as a flexible and simple approach for OOD generalization in graph learning.

### Strengths
1. The paper conducts extensive experiments across diverse datasets, covering general and molecular graph domains, and varying degrees of distribution shift. This comprehensive approach provides a robust evaluation of the efficacy of pre-trained models in out-of-distribution (OOD) scenarios.
2. The findings of the paper show that even basic pre-trained models perform comparably or better than models specifically designed to handle distribution shift. This highlights the effectiveness of pre-training in graph OOD generalization and suggests that pre-training could be a flexible and simple approach for OOD generalization in graph learning.
3. The paper explores the influence of key factors such as sample size, learning rates, and in-distribution performance on the performance of pre-trained models for OOD generalization. This analysis provides insights into the factors that contribute to the effectiveness of pre-trained models in graph learning.

### Weaknesses
1. In the article, the discussion is confined to InfoGraph's appropriateness for general graph datasets that lack node information, and it does not include a comparative analysis of ContextPred, Attribute masking, and Mole-BERT. For example, in the MoleculeNet and OGBG-HIV datasets, there is asignificant performance gap between MOLE-BERT and CONTEXT-PRED.This absence of discussion regarding this phenomenon makes it challenging to determine which type of pre-trained model performs optimally in various scenarios. Specifically, the paper lacks a detailed analysis of why certain pre-training strategies, such as those based on masked node attribute prediction or context prediction, might be more suitable for specific types of graph data or OOD tasks. For instance, the performance differences between ContextPred and Mole-BERT on molecular datasets could stem from Mole-BERT's specialized tokenization scheme that is tailored to molecular structures, which is not discussed in detail.
2. This paper lacks an in-depth theoretical analysis of their examination of pre-trained models. This opens the door for further exploration of the fundamental principles and mechanisms behind the observed performance of pre-trained models in graph OOD scenarios. The paper does not delve into the theoretical underpinnings of why pre-training helps with OOD generalization in graph neural networks. For example, it would be beneficial to explore concepts like the learned feature space of pre-trained models, and how it relates to the target OOD tasks, or how pre-training might lead to more robust representations that are less sensitive to distribution shifts.
3. The article lacks a detailed description of how OOD experiments with pre-trained models are conducted. It would be beneficial to use a figure to illustrate the framework. The paper does not specify the exact procedure for fine-tuning pre-trained models on OOD tasks. For example, it is unclear whether the entire model is fine-tuned or only certain layers, and how hyperparameters like learning rates are chosen for the fine-tuning process. A figure illustrating the data flow and model adaptation process would greatly enhance clarity.
4. In the introduction,  Please remove the extra ‘we’ in “Motivated by this potential, we we seek to investigate whether graph pre-trained models…".
5. In the introduction, this sentence “We observe that even with a smaller fine-tune sample size, such as only 10%-20%.....” can easily lead to ambiguity. It implies that pre-trained models using 10%-20% of the data can almost achieve the performance of the baselines that use all the data, rather than the performance achieved by pre-trained models using all the data.

### Questions
1. What are the reasons for different pre-trained models, such as ContextPred, Attribute masking, and Mole-BERT, yielding distinct results? What scenarios are each of them best suited for?
2. What is the framework for using pre-trained models in graph OOD tasks? Please describe the framework.
3. The sentence "We observe that even with a smaller fine-tune sample size, such as only 10%-20%..." in the introduction, does it have any ambiguity?

### Soundness
3 good

### Presentation
2 fair

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
This paper serves as a benchmark for discussing the use of pre-trained methods in handling Graph-level OOD (Out-of-Distribution) problems. Through experiments conducted on diverse datasets of varying sizes and types of OOD scenarios, the paper finds that models learned through pre-training achieve results in OOD scenarios that are comparable to, or even better than, specialized methods designed for OOD problems. The authors also make meaningful explorations into the key factors influencing the ability of pre-trained models to handle OOD problems.

### Strengths
- The motivation behind this paper is well-founded. With the increasing research focus on Graph OOD (Out-of-Distribution) problems, providing a unified and fair benchmark for various methods is highly meaningful.
- The paper's selection of numerous datasets of various types and sizes allows for a comprehensive representation of different methods' strengths and weaknesses across different scenarios.

### Weaknesses
 - I am uncertain whether 'PODGenGraph' can truly be called a benchmark. As per my understanding, the purpose of a benchmark should be to provide a fair and extensive comparison of the performance of different methods on the same task within the same environment. Since this paper claims to be a benchmark for Pretraining methods in OOD tasks, it should cover a more representative set of pretraining methods. The selection of only three methods in the paper seems limited and unrepresentative (for example, the omission of popular contrastive methods and masked autoencoders).
- The author's claims about the superiority of pretraining methods in Graph OOD tasks appear to be overstated. The author suggests that basic pretraining methods can achieve comparable performance to specially designed methods. However, according to Table 2, there is still a significant performance gap between pretraining methods and specially designed methods on many datasets.
- It's not surprising that pretraining on a large molecular dataset can enhance a model's performance in OOD scenarios due to the semantic similarities within molecular datasets, similar to the way large language models operate. However, as seen in Table 2, pretraining on molecular graphs does not seem to generalize well to the CMNIST dataset. This highlights the limitations of pretraining methods
- The analysis of factors influencing the performance of Pretraining methods in Section 4.3 appears somewhat shallow. For instance, the learning rate does not seem to be a factor worthy of analysis because it is not a critical component of the model. On the other hand, the author claims that pretrained models have a sample-efficient advantage. I initially thought this meant pretrained models can maintain good performance with smaller training sets. However, Figure 2b only demonstrates that pretrained models outperform baseline methods at different label rates.

### Questions
- This paper focuses merely on graph-level tasks. I wonder if pretrained methods can yield similar results on node-level OOD tasks.


Though I have raised several points in weaknesses. I am glad to adjust my rating if the reviewer can address my concerns.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The article empirically investigates the potential of graph pre-trained models in handling graph out-of-distribution (OOD) problems. The paper finds that even basic graph pre-trained models often outperform specifically-designed OOD methods for handling distribution shifts. The extensive experiments conducted across various datasets under different distribution shifts scenarios. However, it seems that graph pre-training was originally introduced to address OOD problems. It is unclear about the commonalities and distinctions between graph pre-training and OOD models.

### Strengths
The experimental design include a wide range of OOD datasets and distribution shifts scenarios. The phenomenon observed in the experiments can inspire and lead to further exploration.

### Weaknesses
1. The commonalities and distinctions between graph pretraining and OOD models should be clearly and comprehensively elucidated. From my perspective, it appears that graph pretraining was originally introduced to address OOD problems. Also in Section 2, the authors include the self-supervised learning into Graph OOD, however some self-supervised learning methods like GraphCL is typically considered as a graph pre-training method.

2. The OOD datasets and pre-trained models used in the article are primarily focused on the molecular domain. Does this imply that the scope defined in the article is mainly centered in molecular graphs? There exist many graph pre-trained models [1-3] beyond just molecules, it would be beneficial for the article to include additional datasets and methods beyond just molecules. It is currently unclear are the findings stated in the paper still hold in these pre-trained models.

3. The findings presented in the article regarding the ability of pre-trained models to address OOD issues seem to be intuitive and insufficient, because pre-trained models are originally designed to address OOD. I recommend the authors to explore more interesting findings, such as identifying which pre-training tasks can aid in specific OOD scenarios. Can any findings help us better guide the design of pre-training models or tasks?

### Questions
See weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
