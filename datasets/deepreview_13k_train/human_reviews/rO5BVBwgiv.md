# Retrieval-augmented Encoders for Extreme Multi-label Text Classification

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Extreme multi-label classification (XMC) seeks to find relevant labels from an extremely large label collection for a given text input. To tackle such a vast label space, current state-of-the-art methods fall into two categories. The one-versus-all (OVA) method uses learnable label embeddings for each label, excelling at memorization (i.e., capturing detailed training signals for accurate head label prediction). In contrast, the dual-encoder (DE) model maps input and label text into a shared embedding space for better generalization (i.e., the capability of predicting tail labels with limited training data), but may fall short at memorization. To achieve generalization and memorization, existing XMC methods often combine DE and OVA models, which involves complex training pipelines. Inspired by the success of retrieval-augmented language models, we propose the Retrieval-augmented Encoders for XMC (RAE-XMC), a novel framework that equips a DE model with retrieval-augmented capability for efficient memorization without additional trainable parameter. During training, RAE-XMC is optimized by the contrastive loss over a knowledge memory that consists of both input instances and labels. During inference, given a test input, RAE-XMC retrieves the top-$K$ keys from the knowledge memory, and aggregates the corresponding values as the prediction scores. We showcase the effectiveness and efficiency of RAE-XMC on four public LF-XMC benchmarks. RAE-XMC not only advances the state-of-the-art (SOTA) method DEXML, but also achieves more than 10x speedup on the largest  LF-mazonTitles-1.3M dataset under the same 8 A100 GPUs training environments. Our experiment code is available in the Supplementary Material.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the Extreme multi-label classification problem via proposing the Retrieval-augmented Encoders for XMC (RAE-XMC) framework. This framework equips a DE model with retrieval-augmented capability for efficient memorization. The empirical study confirms the effectiveness and efficiency of four public benchmarks. In addition, the authors shows the presented approach achieves significant speedup on the largest dataset.

### Strengths
1. This study provides a comprehensive overview and in-depth summarization of the various existing approaches that have been developed for extreme multi-label classification. A thorough analysis is conducted on the advantages and disadvantages of each type of approaches. method. This ensures that readers gain a robust understanding of the current models available.

2. The concept of introducing the retrieval-augmented method is interesting. This presents interesting possibilities for improving the performance of the extreme multi-label classification tasks.

### Weaknesses
1. My primary concern regarding this study is on the aspect of novelty. The concept of incorporating retrieval-augmented knowledge certainly has the potential to provide valuable background information that can enhance classification performance. However, aside from this innovative idea, the overall design of the model remains quite conventional and adheres to traditional methodologies, which may limit its effectiveness. 

2. There is a lack of detailed information regarding the implementation of this study. Furthermore, it could be beneficial to explore the potential of utilizing various other language models or, ideally, open-source large language models to assess the feasibility of integrating the proposed model with those advanced technologies. This exploration could offer insights into how to enhance the performance and capabilities of the existing framework.

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The Retrieval-augmented Encoders for XMC (RAE-XMC) framework enhances dual-encoder (DE) models with retrieval capabilities, improving memorization without adding extra trainable parameters. RAE-XMC uses contrastive loss over a knowledge memory of input instances and labels during training. For inference, it retrieves top-K keys from this memory and aggregates their values for prediction scores. Demonstrated on four public LF-XMC benchmarks, RAE-XMC surpasses the state-of-the-art method DEXML, achieving over 10x speedup on the LF-AmazonTitles-1.3M dataset using the same 8 A100 GPUs training setup.

### Strengths
1. The idea of using retrieval augmentation with XMC is very interesting.
2. Storing existing dataset samples in memory is a nice trick. 
3. Training seems to be very efficient. Also, the authors have performed extensive experimentation under many settings.

### Weaknesses
1. OAK is a recent method which also uses memory for XMC tasks. How does RAE-XMC compare with OAK?
2. PSP metrics seem to be very commonly used across XMC literature. Can you please report PSP also?
3. Table 1: Does TT include memory construction time also? If not, it will be nice to include that also.
4. Improvements are somewhat weak in Table 1. On LF-AmazonTitles-131K, P@1 is not best for RAE-XMC. On LF-WikiSeeAlso-320K it looks like RAE-XMC is not stat sig better than NGAME. Also, on LF-AmazonTitles-1.3M, RAE-XMC is not stat sig better than DEXML. 
5. Since memory needs to be stored as well, how do these methods compare with respect to their RAM requirements?
6. From a novelty perspective, the method looks like Approximate KNN using encoders (trained with std methods taken from DEXML and NGAME). Although it is being called called retrieval augmented, there is actually no augmentation here at all. It is more of KNN rather than retrieval augmentation.
7. Case studies: It would be nice to see top b retrieved samples for some sample, and show why those help to improve accuracy of the proposed method compared to DEXML. 
8. Also some error analysis would be nice to do, especially on samples where RAE-XMC was wrong but DEXML was correct. What percent of errors are because of wrong top b neighbors?
9. Can lambda be learned/tuned/computed per sample?
10. Line 192: what is f?

### Questions
Please see weaknesses

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Paper is about generalization and memorization trade off in extreme classification (XC) and give good quality background and information about recent related works. Proposed approach is scalable and shows state of the art results in XC.

### Strengths
-	Very well written, I could follow each and every section
-	Training is scalable and architecture does not add to the training memory

### Weaknesses
- Does not compare with State-of-the-art XC methods like OAK which works in retriever augmented encoders
- Results are not reported on short text titles datasets, also available on the XC repository. I would suggest authors to report numbers on titles datasets as they are closer to real world tasks.
- OAK uses auxiliary information, why was this auxiliary information not considered in knowledge memory

- **The approach is not novel**, many papers in the past have use label centroids (Parabel, Astec, XR-Transformer etc) as well as knn on the training documents (Astec, FasterXML). Since authors cited all of them, Kindly comment on how proposed approach is different for these methods. As of now it looks like authors added KNN over DEXML.

- Since authors main argument is about memorization, authors should also report accuracy of encode on training set. Reason to ask this is, is if accuracy is sufficiently high what is the need of adding knn?

### Questions
Along with answers to the weakness sections, please address the following questions:

- **The approach is not novel**, many papers in the past have use label centroids (Parabel, Astec, XR-Transformer etc) as well as knn on the training documents (Astec, FasterXML). Since authors cited all of them, Kindly comment on how proposed approach is different for these methods. As of now it looks like authors added KNN over DEXML.

- Since authors main argument is about memorization, authors should also report accuracy of encode on training set. Reason to ask this is, is if accuracy is sufficiently high what is the need of adding knn?

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes the in-domain retrieval-augmented framework RAE-XMC for extreme multi-label text classification. RAE-XMC uses a clean contrastive learning function to train and uses a knowledge memory to inference. During inference, the test text retrieves top-b nearest neighbors in the knowledge memory to construct the predicted label.

### Strengths
1. The presentation is good.
2. The method is sound.
3. The experimental results are good. In addition, the method converges fastly.

### Weaknesses
1. The retrieval-augmented framework for extreme multi-label text classification is not novel. Su et al. (2022) use a similar retrieval-augmented framework for multi-label text classification. The difference is that this paper uses a cleaner contrastive learning loss and incorporates label representations in the memory.



### Questions
1. It seems that the method has a higher inference overhead. Can you show the inference overhead compared to the OVA and DE methods?
2. Do the methods rely on label descriptions?
3. The improvement mainly comes from the head class in Table 2. Is there some explanation for this? It looks like it's caused by the imbalance in the memory.
4. As shown in Lines 317-323, the method also seems applicable to small-scale multi-label text classifications.

### Soundness
3

### Presentation
3

### Contribution
1
