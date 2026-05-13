# Neural Fine-Tuning Search for Few-Shot Learning

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
In few-shot recognition, a classifier that has been trained on one set of classes is required to rapidly adapt and generalize to a disjoint, novel set of classes. To that end, recent studies have shown the efficacy of fine-tuning with carefully crafted adaptation architectures. However this raises the question of: How can one design the optimal adaptation strategy? In this paper, we study this question through the lens of neural architecture search (NAS). Given a pre-trained neural network, our algorithm discovers the optimal arrangement of adapters, which layers to keep frozen and which to fine-tune. We demonstrate the generality of our NAS method by applying it to both residual networks and vision transformers and report state-of-the-art performance on Meta-Dataset and Meta-Album.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents NFTS, a hierarchical method for neural architecture search in the few-shot image classification domain. The proposed framework engages various ways to adapt ResNet and ViT architectures to the support set including fine-tuning and adaptation parameters and then performs a search to identify the best-performing combination amongst each search path. The total number of paths is limited to both address computational limitations and prevent overfitting. Experiments on Meta-Dataset and Meta-Album demonstrate the strong efficacy of the approach when adapted inside a prototypical classifier with ResNet and ViT backbones. Ablation studies provide insights into various aspects of the method.

### Strengths
- The paper is very well-written.
- NFTS is empirically effective and demonstrates a good balance between enabling adaptation using the support set while preventing overfitting. Clear empirical evidence shows the model's ability to select a more optimal architectural combination than previous baselines.
- Experiments are extensively performed on large-scale datasets that demonstrate the efficacy of NFTS across both ResNet and ViTs.
- Ablation studies justify various architectural choices made such the total number of search paths and the granularity of options.

### Weaknesses
 - Empirical results reported lack confidence intervals. Although I suspect this is due to space limitations, they should be included to verify the statistical significance of the results report and for better comparison with baselines. If some results do not meet statistical significance, they must be modified when presented in results tables to reflect so accordingly and the claims made need to be adjusted.
- Ablation study on search paths shows that N=3 not only provides better computational efficiency but additionally prevent overfitting on the support set. How does it compare with N=2 or N=4? I believe that further insights here would be useful as to how this hyperparameter is set. Furthermore, how does performance vary depending on N across ViT and ResNet?
- Meta-dataset baselines that are compared to omit some recent methods that can be included for completeness of comparison [1, 2, 3].

### Questions
Please address the questions and limitations noted above. Overall, I believe that this is a strong submission, and the broader research community can benefit from it. I believe that the empirical results of the paper need to be verified in terms of statistical significance by providing the appropriate confidence intervals across the reported numbers. This is the only major weakness in the submission, and once addressed with the other limitations noted, I would be more than happy to recommend the paper for acceptance.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
1. This paper provides the first systematic Auto-ML approach for finding the optimal adaptation strategy in few-shot learning.
2. This method designs a novel strategy for defining the search space.
3. The proposed method, namely NFTS, outperforms state-of-the-art methods in both Meta-Dataset and Meta-Album benchmarks.

### Strengths
1. The motivation for introducing NAS into FSL is good, as mentioned in this work: current FSL works have started to understand the trade-off between frozen weights and trained parameters. It makes sense to automatically search for the best configuration instead of manual search or "carefully tuning learning rates."

2. The experimental results present the superiority of NFTS; it achieves a significant performance gain on the Meta-Dataset.

3. The analysis is interesting as it shows the trend that the best-searched configuration does perform the best in the unseen downstream.

### Weaknesses
The results lack significance compared to the additional training required to obtain NFTs. The method requires training a supernet, performing an evaluation to find the best subnet. As NFTs achieve only a less than 1% accuracy gain on the Meta-Dataset in a multi-domain setting, the method is excessively computationally expensive and inefficient when compared to the actual performance gain. The computational overhead is particularly concerning given that the reported gains are marginal, raising questions about the practical utility of the approach. The paper does not provide a detailed breakdown of the computational costs associated with each stage of the proposed method, making it difficult to assess the true cost-benefit ratio. Furthermore, the analysis of the discovered architectures, while interesting, lacks a deeper investigation into the underlying reasons for the observed adaptation patterns. The consistent adaptation of block 14 and lack of adaptation for block 9, as mentioned in the 'Discovered Architectures' paragraph, is not sufficiently explained, leaving the reader to speculate about the potential causes.

### Questions
Could you offer some insights about their consistent adaptation of (α) block 14 and their lack of adaptation for block 9 in the 'Discovered Architectures' paragraph?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The authors propose the optimal adaptation method through the lens of neural architecture search (NAS) in few-shot recognition.
- Given a pre-trained neural network, the proposed algorithm discovers the optimal arrangement of adapters, which layers to keep frozen, and which to fine-tune.
- The authors demonstrate the generality of our NAS method by applying it to both residual networks and vision transformers and report state-of-the-art performance on Meta-Dataset and Meta-Album.

### Strengths
(+) The proposed methods find some interpretable trends using layer-wise adaptations, which include the early/late layers of ResNet and ViT.

### Weaknesses
 - (-) The authors stated the superior performances in various experimental settings. However, the author didn’t specify the structure and the number of parameters.
- (-) There is no ablation study on the two-stage search for optimal path (sec. 2.4): the best-performing path during training time, the searching path at test time, and the proposed hybrid one.

### Questions
- What is the most differentiating point from the prior NAS structures?
- How many parameters increased by adapting?
- Could authors provide parameter tables comparing NFTS (ResNet18) with others? The detailed architectural layout could be helpful to understand better.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
