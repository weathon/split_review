# Time- and Label-efficient Active Learning by Diversity and Uncertainty of Probabilities

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
We propose FALCUN, a novel deep batch active learning method that is label- and time-efficient. Our proposed acquisition uses a natural, self-adjusting balance of uncertainty and diversity: It slowly transitions from emphasizing uncertain instances at the decision boundary to emphasizing batch diversity.
In contrast, established deep active learning methods often have a fixed weighting of uncertainty and diversity. Moreover, most methods demand intensive search through a deep neural network's high-dimensional latent embedding space. This leads to high acquisition times during which experts are idle as they wait for the next batch to label. 
We overcome this structural problem by exclusively operating on the low-dimensional probability space, yielding much faster acquisition times. 
In extensive experiments, we show FALCUNs suitability for diverse use cases, including image and tabular data. 
Compared to state-of-the-art methods like BADGE, CLUE, and AlfaMix, FALCUN consistently excels in quality and speed: while FALCUN is among the fastest methods, it has the highest average label efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes FALCUN, a new pool-based active learning approach for deep neural networks. FALCUN operates directly on output probabilities for efficiency and naturally balances uncertainty and diversity. Experiments on various image datasets show it matches or exceeds state-of-the-art methods in accuracy while being faster. The core ideas are interesting but the empirical evaluation methodology could be stronger.

### Strengths
Leveraging output probabilities for uncertainty estimation and batch diversity is novel, simple and elegant. This intuitively should capture informativeness and redundancy better than latent features.
The empirical results generally validate that FALCUN provides excellent accuracy across datasets at low computational cost. Outperforming methods like BADGE and CLUE is impressive.
Analysis of the uncertainty and diversity components in the ablation study highlights their complementary benefits. The automatic balancing between the two is also shown to be effective.

### Weaknesses
The chosen baselines are reasonable but given the focus on computational efficiency, comparing to BatchBALD would have strengthened the empirical claims. While the authors focus on single forward pass methods, a comparison to a computationally efficient implementation of BatchBALD, even if it requires multiple passes, would be valuable to understand the trade-offs. For the colored image experiments, using pre-trained weights gives FALCUN an advantage over baselines that train from scratch. Comparisons should be fair, and it is crucial to ensure that all methods are initialized in the same way, whether from scratch or with pre-trained weights, to avoid biasing the results. Some dataset choices like MNIST and FashionMNIST are dated. More modern complex datasets would better highlight benefits, especially considering the method's claims of efficiency and scalability. The empirical methodology uses a limited set of architectures. Testing on bigger models like ResNets, and potentially transformers, would be important to substantiate scalability claims and demonstrate the method's general applicability. More rigorous hyperparameter tuning for baselines could lead to better optimized versions for fairer comparison with the proposed approach. It is important to ensure that the baselines are performing at their peak, which requires a careful hyperparameter search, and not just using default settings.

### Questions
On the proposed method:

The margin-based uncertainty measure is intuitive. But are there any theoretical justifications for using it over other alternatives like entropy or Bayesian uncertainty?
For the diversity initialization and update, were other potential approaches considered? Is there a principled basis for the specific design choices made?
How sensitive is FALCUN to the choice of the γ parameter for sampling from the relevance distribution? Is tuning gamma required for different datasets?
What impact does the neural network architecture have on FALCUN's performance, if any? Does it generalize across model families like CNNs, MLPs etc?
On the experiments:

BatchBALD is a highly relevant Bayesian batch active learning method - would be good to compare against it. What advantages can FALCUN provide over Bayesian approaches?
The datasets seem heavily focused on MNIST variants - were results consistent on more complex, modern datasets? How was performance with higher input dimensionality?
For colored image experiments, using pretrained weights may favor FALCUN over baselines - could this be addressed?
What was the hyperparameter tuning strategy for baselines? Would better optimized baselines affect relative comparisons?
How was robustness to things like random initialization and train-test splits evaluated?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors proposed a label- and time-efficient active learning method, namely FALCUN. They incorporated both uncertainty and diversity into the data evaluation strategy and performed probability-based sampling to balance the uncertainty and diversity. Furthermore, they conducted experiments on both image and tabular data to validate the effectiveness of the proposed method.

### Strengths
The authors designed a data evaluation metric considering both uncertainty and diversity and performed data sampling based on the probabilities, rather than strictly adhering the hard ranking approach.

### Weaknesses
Weakness
1.Compared to identifying the most informative samples, the time cost of data evaluation is not the primary concern since the online data evaluation is not required.
2.In uncertainty component, the margin uncertainty lacks novelty.
3.As for diversity component, the rationale behind calculating the diversity score using the distance of predicted probabilities is still unclear. Why do the authors choose to measure the distance of predicted probabilities instead of using feature embeddings?
4.Why did the authors perform probability-based sampling, instead of designing an alternative hybrid sampling strategy that combines the uncertainty-based and diversity-based metrics?
5.The authors conducted experiments on small-scale datasets. We recommend verifying the efficacy of the proposed method on more challenging and large-scale benchmarks, such as CIFAR-10, CIFAR-100, and ImageNet.
6.They authors should include additional experiments to compare the proposed method with state-of-the-art approaches like TOD [1] and Gradnorm [2].

### Questions
see above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores two key limitations of existing active learning methods. First, many sophisticated AL algorithms have high computation + runtime cost, which make them undesirable for real-world implementation. Second, many AL algorithms focus on labeling images that optimize image diversity or maximizing the number of uncertain / currently-hard unlabeled images, with some recent works that attempt to use both. The paper proposes a new active learning strategy that combines uncertainty and diversity in a computationally fast algorithm. The proposed method is numerically validated on a number of image and tabular datasets to demonstrate improvements in model performance and low time complexity of the algorithm compared to existing baselines.

### Strengths
Both of the limitations of existing AL algorithms are core problems, which the paper addresses. The time complexity analysis and demonstrated fast runtime with competitive performance are nice.

### Weaknesses
The key methodological motivation for the algorithm seems to be to derive a function that balances the uncertainty of the existing model and the diversity between samples selected in the current batch. However, there is no theoretical justification for why the proposed algorithm is a good strategy. Moreover, the experiments primarily use relatively simple image datasets and small models. It is not clear whether these results would meaningfully transfer to more realistic datasets (e.g., ImageNet). Currently, the difference between the methods and benchmarks appear small in every dataset considered. Lacking rigorous theoretical justification or validation on hard benchmark problems, the argument for the proposed method in practice is unconvincing. 

The problem of dealing with two competing objectives, diversity and uncertainty, has been studied in recent works, and the paper misses a lot of this related literature (e.g., [1], [2]). This also leads to a missed opportunity for discussion and validation on how these two objectives trade-off overall. What is the major contributor overall to selection? Does the uncertainty score dominate or the diversity score?

### Questions
1. What do you mean when you state “an optimization function for diverse samples should not have a global optimum”? This is a confusing statement. Furthermore, it is unclear how margin uncertainty satisfies this property. Please clarify.
2. How does the proposed method trade-off diversity and uncertainty over active learning iterations?
3. Why does KCenterGreedy perform poorly on Openml-156?
4. How do you tune the $\gamma$ parameter? Furthermore, is it advantageous to vary $\gamma$ across the active learning stage (e.g., from small to large)?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces FALCUN, a method in active learning, which promises efficiencies in labeling and processing. It brings a dynamic acquisition strategy to the table, focusing initially on uncertain instances near decision boundaries and gradually shifting to emphasize batch diversity. While the proposed approach looks new in some aspects, the lack of acknowledgment of previous works that have explored similar territories casts a shadow over its originality.

Key foundational concepts seem to echo pre-existing methodologies in active learning literature, which were not appropriately credited, making FALCUN appear more as an incremental advancement rather than a groundbreaking innovation. Additionally, some experimental results, particularly those involving LeNet and BADGE's performance, seem somewhat inconclusive and could benefit from further rigor and validation to strengthen their credibility.

Furthermore, the paper’s experimental breadth appears limited. A more expansive inclusion of diverse and challenging benchmarks, such as CIFAR-100 and TinyImageNet, would enhance the robustness of FALCUN’s evaluation, providing a more comprehensive understanding of its effectiveness and applicability across various domains. A reconsideration of these aspects could elevate the paper’s contributions and clarity, fostering a more nuanced appreciation of FALCUN's position in the active learning landscape.

### Strengths
- The proposed algorithm tries to improve efficiencies in labeling and processing through a dynamic acquisition strategy, emphasizing a transition from focusing on uncertain instances to prioritizing batch diversity, showcasing a potential way in active learning strategies.

### Weaknesses
 - The paper seems to overlook several crucial references relevant to the discussed topic. Fundamental concepts such as the theoretical importance of the near decision boundary have been comprehensively explored and articulated in previous works, notably in references [1] and [2]. These pivotal papers, along with others, offer profound insights that would augment the paper’s foundational grounding. Moreover, the proposition of a linear-time scalable algorithm, a core element presented in the paper, has previously been introduced and elaborated upon in reference [3]. In addition to that, an influential work cited as [4] such as PowerBALD/or PowerEntropy adopting a sampling similar to Eq (6) but with better originality has also proposed a scaling approach that intriguingly maintains the algorithm’s linear-time complexity.

- The active learning results presented in the paper for LeNet on datasets like EMNIST or RepeatedMNIST seem somewhat unconvincing. Typically, in prevailing literature and experiments, around 300-500 images are required (not > 1000 images) to achieve accuracy comparable to supervised learning methods on these datasets. The reported results in the paper appear to deviate from these established benchmarks. It may be beneficial to revisit and scrutinize the experimental setup, methodology, and the specific implementation of LeNet in the active learning context to ensure that the presented results are robust, reliable, and in alignment with existing standards and expectations in the field. This could enhance the credibility and persuasiveness of the results and the overall contributions of the paper.

- The performance of BADGE as presented in the paper raises some questions. It seems that with appropriate hyperparameter settings, BADGE should be capable of delivering much improved results. This discrepancy suggests that there might be room for optimizing the configuration of BADGE in the experiments, ensuring that it operates under the most suitable conditions for a fair and rigorous comparison. To uphold the integrity and reliability of the comparative analysis, it might be beneficial to revisit and fine-tune the hyperparameters used with BADGE, ensuring that its performance is accurately represented and evaluated against its full potential.

- The experimental section of the paper seems somewhat limited and could be enhanced to bolster the claims made. Incorporating a broader array of realistic scenarios, such as tests involving CIFAR-100, TinyImageNet, or ImageNet, would offer a more comprehensive insight into the method’s applicability and effectiveness. Including such varied and complex datasets in the evaluation would not only strengthen the validity of the results but also improve the generalizability of the conclusions drawn. This expansion in the experimental design would be instrumental in substantiating the method's robustness and adaptability across diverse challenges and use-cases.

### Questions
- What criteria determine the **most informative region**? Is a point considered most informative solely based on its proximity to the decision boundary?

- **Could the authors please provide a more explicit explanation regarding the source of diversity in the proposed formula?** The margin considers two class boundaries. It might not be sufficiently generalizable. It would be beneficial to have a more explicit elucidation on how diversity is incorporated and manifests itself within the algorithmic design. Understanding the origins and implementation of diversity within the formula can enhance the comprehension of its functionality and overall impact on the method's performance. An in-depth clarification would contribute to a more robust and insightful evaluation of the proposed approach’s effectiveness and novelty.

- It seems crucial to **re-evaluate the experiment setups in the study to enhance the reliability and comprehensiveness of the findings**. Including a broader selection of benchmarks in the evaluation process would be instrumental in demonstrating the robustness and versatility of the proposed method across varied scenarios. **A more diversified array of benchmarks** will not only contribute to a deeper, better understanding of the method's performance but also bolster the study's overall credibility and impact. Therefore, revisiting and expanding the experiment setups with additional benchmarks is a highly recommended step to enrich the empirical validation of the study.

- Section 4.4 discusses the influence of $\gamma$ parameter, indicating that **different benchmarks may require distinct $\gamma$ parameter values for optimal performance**. This aspect raises a practical concern: how can users effectively determine or choose an appropriate $\gamma$ value a priori for various benchmarks? The ability to discern and select suitable parameters is crucial for the method's practical applicability and usability in real-world scenarios. Clarification or guidance on this matter would significantly enhance the method’s practical value.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
