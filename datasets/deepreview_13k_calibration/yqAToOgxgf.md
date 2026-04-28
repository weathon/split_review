# An old dog can learn (some) new tricks: A tale of a three-decade old architecture

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
Designing novel architectures often involves combining or extending familiar components such as convolutions and attention modules. However, this approach can obscure the fundamental design principles as the focus is usually on the entire architecture. Instead, this paper takes an unconventional approach, attempting to rejuvenate an old architecture with modern tools and techniques. Our primary objective is to explore whether a 30-year-old architecture can compete with contemporary models, when equipped with modern tools. Through experiments spanning image recognition datasets, we aim to understand what aspects of the architecture contribute to its performance. We find that while an ensemble of ingredients bears significance in achieving commendable performance, only a few pivotal components have a large impact. We contend that our discoveries offer valuable insights for creating cutting-edge architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to analyse various components in neural net training by building on top of a 30 year old architecture Pi-Sigma. Instead of coming up with novel components they propose to use previously used techniques to add it to the architecture.  After a lot of ablations they conclude that the most important components towards improvement are the i) optimizer ii) normalization iii) data augmentation and iv) depth of the neural net

### Strengths
- The idea of using an old architecture and building on top of it is unique and interesting.
- The paper does a good job at analyzing various components by building on top of an old architecture.
- The paper does a very dense evaluation to analyze a lot of components in the neural net training by testing over multiple datasets and having various architectures as baselines.
- The paper is well written.

### Weaknesses
 - Although the analysis is useful to put it out there, i'm not sure if it was surprising at the end. As the current architectures of MLP mixer or ViT indeed have very few components, thus making it easy to say what is important vs not. I would like authors to counter this point and provide examples that they discovered that might not have been that obvious.
- Few things are a bit unclear, as technique 1 has skip connections , but the authors later go to say skip connections do not contribute to the performance improvement. Can authors remove skip connection from technique 1 and show the curves again.
- Further since training algorithm (AdamW) in this case plays a very important rule, it would be helpful to analyse it more closely by checking previous versions of Adam such as RMSprop or even before.
- Same for data augementation, a more indepth study regarding this would be useful.

### Questions
Some qs are in the Weakness section.
- Can authors compare on the benchmarks on which Pi-Sigma paper had shown their result? This will help realise if the improvements are indeed benchmark specific or general.
- What is the role of convolutions vs MLP mixer. I think the standard convention is that if u have less data you should do convolution, however this is not clearly indicated from the author's experiments.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents how they rejuvenated a 30-year-old architecture, $Pi-Sigma
$, with modern tools and techniques. The authors aim to investigate whether this old architecture can compete with contemporary models when equipped with modern tools. The paper systematically introduces a series of techniques to enhance the original $Pi-Sigma$ model, including the incorporation of skip connections, normalization schemes, data augmentation, and more recent technqiues.

### Strengths
- I really like the way the authors describe the premise of this paper and motivate their interests: find exactly what components of models cause the biggest impact on performance and this area got especially popular after the release [1, 2, 3] among others. The premise that the authors explore and the way they motivate the paper is really interesting.
- The authors very clearly identify the novelty in this work, "However, our objective is to delve deeper into architecture design and explore how
previously used techniques and tools"
- The authors try out quite a few diverse modern techniques and see how they impact performance on $\Pi-\Sigma$ network.
- I think the results and experiments are well put together, the authors not only show that they improve $\Pi-\Sigma$ networks but also extend their experiments to multiple datasets and also on $\Sigma\Pi\Sigma$ neural networks.

[1] Tolstikhin, Ilya O., et al. "Mlp-mixer: An all-mlp architecture for vision." Advances in neural information processing systems 34 (2021): 24261-24272.

[2] Smith, Samuel L., et al. "ConvNets Match Vision Transformers at Scale." arXiv preprint arXiv:2310.16764 (2023).

[3] Trockman, Asher, and J. Zico Kolter. "Patches are all you need?." arXiv preprint arXiv:2201.09792 (2022).

### Weaknesses
 - Though the authors identify what training processes work well for neural net architectures and also show that they reach the performance of ResNet just due to these techniques, they do not share the kind of techniques that were proven to be highly architecture-specific and probably do not work for this. In general, I believe that the insights the authors came up with are not fully new and were known. I do not say that these kinds of insights are not valuable, but for instance, showing that patching has a big impact on performance, which was not known earlier.
- I think the authors only try out fairly popular techniques for the experiments, for which each of their individual effects is fairly well-studied and well-known. It would have been a much more interesting paper if the authors also included other low-level techniques that such models could try out.
- In this case the paper method might not come across as novel, one would often look towards the paper for using something in a new context, which the authors do pretty well and also build the RPS model or for some important insights which I believe this paper does not correctly do.

### Questions
- I believe a very important question is to understand what kind of techniques do not seem to improve performance, it would be of great interest to understand what kind of techniques are possibly over-reliant or dependent on certain architectures. I would also encourage the authors to include this important detail in their work.
- A typo in

> Out work aims

### Soundness
3 good

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
This paper conducts a comprehensive analysis of Pi-Sigma and argues that there is an abundance of techniques available in the last few years and yet few insights into how each technique fares in other architectures or its role in generalization in new datasets. It confirms experimentally that, through the strategy of established techniques, the refined architecture achieves performance levels comparable to recent architectures. This work facilitates a comprehensive understanding of the benefits derived from a holistic evaluation of models, shedding light on the key techniques that drive architectural advancements.

### Strengths
1. The author conducted an extensive range of experiments in this article to provide insightful guidance for future model design.

2. The logical structure of this article is clear and makes it easy for readers to follow.

3. In this article, the author presents an interesting discovery where an older model can achieve state-of-the-art performance by incorporating some existing techniques.

### Weaknesses
1. The motivation for this article is insufficient. The author aims to provide insights for future model design through experiments, but these findings are all based on the Pi-Sigma model, which may not necessarily apply to future model designs and could even be misleading. The paper lacks a strong justification for focusing solely on Pi-Sigma, especially given the diversity of modern architectures. The insights gained from this specific model might not generalize to other architectures, limiting the broader impact of the study. It is unclear why this particular architecture was chosen as the sole basis for such broad claims about DNN techniques.

2. The experiments conducted in this article exclusively employ existing techniques, failing to offer guiding principles for the innovation of new methods in the future. While the paper demonstrates the effectiveness of combining existing techniques, it does not explore novel approaches or modifications to these techniques. This limits the paper's contribution to simply a demonstration of existing knowledge, rather than pushing the boundaries of model design.

3. ViT is currently a widely used model, and it is known for its scalability on data. However, despite the experiments conducted on ImageNet-21k, the author did not include comparative experiments or discussions regarding the ViT model. The absence of a comparison with ViT, a dominant architecture in the field, is a significant oversight. This omission makes it difficult to assess the relative performance and relevance of the proposed approach in the context of current state-of-the-art models. The paper should have included a direct comparison with ViT to provide a more comprehensive evaluation.

4. The author discusses the impact of adding six different techniques to the Pi-Sigma model in various orders. However, in the ablation experiments section, there is no discussion of the individual effects of adding each technique to the Pi-Sigma model separately. The lack of individual ablation studies for each technique makes it difficult to isolate the specific contribution of each component. This limits the ability to understand which techniques are most critical and how they interact with each other.

### Questions
1. Could the author discuss some guiding insights from this research for future model design, particularly for state-of-the-art CNNs and ViTs?

2. Could the author explain why they chose to use Pi-Sigma and highlight any unique aspects or clear advantages it has over CNNs and ViTs?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study the Pi-Sigma architecture proposed in 1991. The major objective is to see if this "old architecture" can be effectively improved by several modern techniques, e.g., skip connection, improved training algorithms, normalization layers, and data augmentation. The authors find that while an ensemble of ingredients bears significance in achieving commendable performance, only a few pivotal components have large impacts.

### Strengths
1. The writing of this paper is well.
2. The experiments are comprehensive in terms of studying existing techniques proposed in recent years.

### Weaknesses
My major concern lies in the significance of the contributions of this paper:

1. All the techniques studied in this paper have been proposed in existing works.
2. The effectiveness of these techniques has been confirmed in existing works.
3. Even with all the state-of-the-art techniques, Pi-Sigma net cannot outperform even ResNet-50 (with the same FLOPs, see: Table 4). The difference is ~5%, which is extremely large on ImageNet.
4. Even though this paper reveals that some techniques are less effective on Pi-Sigma, it may be hard to say that these techniques are not effective on top of other models.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
