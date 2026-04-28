# MAI: A Multi-turn Aggregation-Iteration Model for Composed Image Retrieval

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 5, 6, 6

## Abstract
Multi-Turn Composed Image Retrieval (MTCIR) addresses a real-world scenario where users iteratively refine retrieval results by providing additional information until a target meeting all their requirements is found. Existing methods primarily achieve MTCIR through a "multiple single-turn" paradigm, wherein methods incorrectly converge on shortcuts that only utilize the most recent turn's image, ignoring attributes from historical turns. Consequently, retrieval failures occur when modification requests involve historical information. We argue that explicitly incorporating historical information into the modified text is crucial to addressing this issue. To this end, we build a new retrospective-based MTCIR dataset, **FashionMT**, wherein modification demands are highly associated with historical turns. We also propose a Multi-turn Aggregation-Iteration (**MAI**) model, emphasizing efficient aggregation of multimodal semantics and optimization of information propagation in multi-turn retrieval. Specifically, we propose a new Two-stage Semantic Aggregation (TSA) paradigm coupled with a Cyclic Combination Loss (CCL), achieving improved semantic consistency and modality alignment by progressively interacting the reference image with its caption and the modified text. In addition, we design a Multi-turn Iterative Optimization (MIO) mechanism that dynamically selects representative tokens and reduces redundancy during multi-turn iterations. Extensive experiments demonstrate that the proposed MAI model achieves substantial improvements over state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
Existing multi-turn composed image retrieval (MTCIR) methods adopt the “multiple single-turn” paradigm and neglect the historical correlation information in multi-turn interactions. To address this problem, this paper first builds a new retrospective-based MTCIR dataset, wherein modification demands are highly associated with historical turns. Then, the authors develop a new Multi-turn Aggregation-Iteration (MAI) model, which contains a two-stage semantic aggregation paradigm coupled with a cyclic combination loss. Besides, a multi-turn iterative optimization mechanism is designed to select representative tokens and reduce redundancy dynamically. Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
1)	This paper focuses on an interesting multi-turn composed image retrieval task, and points out the critical “multiple single-turn” problem in the existing research field. This research is very valuable and provides significant insights for further research.
2)	The authors have constructed a new dataset for the multi-turn composed image retrieval task, which is more similar to real-world scenarios, and is more massive and diverse. This is an important contribution if the dataset is made publicly available.
3)	A multi-turn key information-aware approach, named the Multi-turn Aggregation model, is proposed to achieve multimodal semantics aggregation and multi-turn information optimization. The proposed method is reasonable and the parameter-free multi-turn iterative optimization (MIO) mechanism is interesting.
4)	The effectiveness of the proposed method has been demonstrated by extensive experimental results.
5)	The writing of this paper is good and easy to follow.

### Weaknesses
1)	Will the collected dataset be made publicly available? Some key characteristics of the dataset are still not clear, such as the average and variance of turn number for each query, the average length for modification text, etc. The dataset will be more comprehensible as more detailed statistics are provided.
2)	It seems MIO is executed for each input, and it contains a DPC-kNN for clustering and density computation. The complexity of this module should be analyzed. Specifically, the computational cost of the DPC-kNN algorithm, which involves calculating distances between all data points, can be substantial, especially with a large number of tokens. Furthermore, the iterative nature of the density peak clustering might also introduce additional overhead.
3)	In Table 6, what does the w/o CCL mean? It seems w/o CCL has outperformed most of the compared methods. Are all the methods evaluated on the same backbone? If they are not, the comparison results may not be fair. The ablation study should clarify whether the performance gain is solely due to the proposed loss or if other factors are involved. It's also important to understand if the compared methods are using the same pre-trained models and training procedures.
4)	Except for the proposed dataset, the proposed method should be also evaluated on existing multi-turn composed image retrieval datasets to further demonstrate the effectiveness. This would help to validate the generalizability of the proposed approach and show that it is not overfitted to the newly created dataset.

### Questions
please try to address the weaknesses.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new dataset, FashionMT, specifically designed for multi-turn composed image retrieval (MTCIR) tasks. FashionMT is characterized by its retrospective-based nature, where the modified text in each new turn may involve information from historical reference images, and its massive diversity, containing 14 times more fashion images and 30 times more categories than previous MTCIR datasets. The authors also introduce a new Multi-turn Aggregation-Iteration (MAI) model that focuses on efficient aggregation and iterative optimization of multimodal semantics in MTCIR. The MAI model includes a Two-stage Semantic Aggregation (TSA) paradigm and a Cyclic Combination Loss (CCL) to enhance semantic consistency and modality alignment, as well as a Multi-turn Iterative Optimization (MIO) mechanism to dynamically select representative tokens and reduce redundancy during multi-turn iterations.

### Strengths
a.	The paper proposes a new dataset, FashionMT, for multi-turn composed image retrieval (MTCIR) tasks
b.	FashionMT is characterized by its retrospective-based nature and massive diversity, containing 14 times more fashion images and 30 times more categories than previous MTCIR datasets
c.	The authors introduce a new Multi-turn Aggregation-Iteration (MAI) model that focuses on efficient aggregation and iterative optimization of multimodal semantics in MTCIR
d.	The MAI model includes a Two-stage Semantic Aggregation (TSA) paradigm and a Cyclic Combination Loss (CCL) to enhance semantic consistency and modality alignment
e.	The MAI model also includes a Multi-turn Iterative Optimization (MIO) mechanism to dynamically select representative tokens and reduce redundancy during multi-turn iterations

### Weaknesses
a.	How to avoid false negative samples during FashionMT dataset construction? The existing single-turn dataset already has the presence of false negative samples, will it be more obvious with multiple rounds?.
b.	For the ZS-CIR method, how was it trained and tested on FashionMT? They are designed for zero-shot, is the adaptation process also zero-shot paradigm?
c.	How does MAI perform for the single-turn dataset? The authors should add the results of MAI for datasets such as FashionIQ, CIRR, etc. to confirm the superiority of MAI even with turn=1.
d.	The clustering used in MIO is affected by the number of cluster centers, denoted as k, and the authors do not mention in the implementation details the value of k, and the number of iterations used when performing k-means, which affects the accuracy of the clustering. And does clustering increase the time overhead of the whole model? Authors need to increase the comparison of model training and inference time.
e.	The Q-former used in MAI is initialized by BLIP-2 with the Flan-t5-xxl language model, while the version of BLIP-2 used in SPRC is blip2-pretrain, right? If MAI uses the same version of BLIP-2 as SPRC to initialize the Q-former parameters, how does the result behave? The authors need to add this experiment to further demonstrate the superiority of MAI?
f.Typos and minors. There are non-standard punctuation marks, such as Line 431, P8, "thanks to TSA", etc. It is recommended to check the whole paper.

### Questions
refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces MAI (Multi-turn Aggregation-Iteration), a model for multi-turn composed image retrieval (MTCIR), along with FashionMT, a new large-scale dataset specifically designed for MTCIR. The key innovation is a two-stage semantic aggregation approach that uses image captions as a bridge between visual and textual modalities, plus a memory-efficient mechanism for retaining historical information across multiple turns.

### Strengths
1. Creation of a large-scale, diverse dataset (FashionMT) that better reflects real-world scenarios
2. Memory-efficient design through the Multi-turn Iterative Optimization mechanism

### Weaknesses
1. Limited evaluation of existing datasets (mostly focused on their new dataset), how is the model's performance on existing benchmark like CIRR, FashionIQ and CIRCO. 
2. The fixed number of turns (4) in the dataset may not reflect varying real-world scenarios, does the author have plan to extend the dataset with a different number of turns? 
3. More visualization of the dataset is expected: I'd like to know (1)sample image sequences across multiple turns: namely the quality of the dataset, the relation of images in different turns, and whether the modified text can describe the relationship between images. (2) visualizations of the distribution of different types of modifications: such as Rollback operations and combination operations.

### Questions
1. Statistics for Modification text types: is possible to supply a category of the modified text type, so that the performance can be compared according to different categories? such as Rollback operations and combination operations.
2. Will the dataset be open-source? 
3. How does the model perform with varying numbers of turns beyond the fixed 4-turn setup?
4. Could the approach be extended to other domains beyond fashion?

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
The paper introduces FashionMT and the MAI model. While the method shows strong results, its complexity and potential scalability challenges could limit its immediate applicability in more generalized settings. Further testing on diverse datasets and longer interaction sequences, along with analysis of the model's efficiency, would enhance the practical relevance of this work.

### Strengths
- FashionMT is a significant contribution. The dataset provides richer and more realistic interactions with over 1 million images and 95 categories. This dataset fills a critical gap in the field where existing datasets fail to incorporate historical context across multiple turns.
The model’s approach to maintaining and optimizing key tokens during multiple retrieval iterations is highly relevant to real-world e-commerce scenarios, where users iteratively refine their search queries. The MAI method effectively addresses the shortcomings of the “multiple single-turn” paradigm that fails to leverage historical turn information.
- Extensive experiments show that MAI achieves significant improvements over existing methods in both the combination and rollback settings.

### Weaknesses
 - While the model is innovative, it introduces considerable complexity with multiple components (TSA, CCL,). The addition of multiple layers, clustering mechanisms, and token filtering might make the model difficult to implement and optimize in real-world settings where computational efficiency is key.
- While the results on FashionMT are strong, the paper does not provide comparisons on non-fashion datasets. The model's application to a more diverse range of image retrieval tasks, such as general object retrieval or scene retrieval, would provide a stronger claim to its versatility.

### Questions
- Can the MAI model be adapted to other MTCIR applications outside fashion, such as general e-commerce, furniture, or other products?

- It would be beneficial to know how this impacts performance when dealing with significantly larger datasets. Is the trade-off between memory efficiency and retrieval performance consistent across different dataset sizes?

### Soundness
2

### Presentation
3

### Contribution
2
