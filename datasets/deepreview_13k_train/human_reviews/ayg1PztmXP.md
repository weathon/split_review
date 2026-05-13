# RAR: Retrieving And Ranking Augmented MLLMs for Visual Recognition

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
CLIP (Contrastive Language–Image Pre-training) uses contrastive learning from noise image-text pairs to excel at recognizing a wide array of candidates, yet its focus on broad associations hinders the precision in distinguishing subtle differences among fine-grained items.
  Conversely, Multimodal Large Language Models (MLLMs) excel at classifying fine-grained categories, thanks to their substantial knowledge from pre-training on web-level corpora.
  However, the performance of MLLMs declines with an increase in category numbers, primarily due to growing complexity and constraints of limited context window size.
  To synergize the strengths of both approaches and enhance the few-shot/zero-shot recognition abilities for datasets characterized by extensive and fine-grained vocabularies, this paper introduces \methodname, a \textcolor{00blue}{R}etrieving \textcolor{00blue}{A}nd \textcolor{00blue}{R}anking augmented method for MLLMs.
  We initially establish a multi-modal retriever based on CLIP to create and store explicit memory for different categories beyond the immediate context window.
  During inference, \methodname retrieves the top-$k$ similar results from the memory and uses MLLMs to rank and make the final predictions.
  Our proposed approach not only addresses the inherent limitations in fine-grained recognition but also preserves the model's comprehensive knowledge base, significantly boosting accuracy across a range of vision-language recognition tasks.
  Notably, our approach demonstrates a significant improvement in performance on 5 fine-grained visual recognition benchmarks, 11 few-shot image recognition datasets, and the 2 object detection datasets under the zero-shot recognition setting.
  \keywords{MLLM \and Fine-Grained \and Few-shot \and Zero-shot Recognition}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces RAR framework to address limitations in fine-grained recognition by combining CLIP’s class candidates recognition with the fine-grained classification abilities of MLLMs. The authors claim that CLIP struggles with distinguishing subtle differences, while MLLMs, despite extensive pre-training, face limitations with increasing category complexity and context window size. Therefore, RAR uses a CLIP-based retriever to store memory of categories and retrieve top-k class candidates for MLLMs to rank and predict. RAR enhances MLLMs’ recognition capability, achieving improvements across fine-grained benchmarks and object detection tasks.

### Strengths
1.The proposed RAR framework is simple yet effective, making it easy to understand and implement.

2.The authors conducted extensive experiments. For each of their statements, motivations, and methods, they provided thorough experimental support. 

3.The authors expanded their method to include object detection tasks (it can be regarded as a form of post-processing), not limited solely to fine-grained object recognition. This provides valuable insights for future research.

4.The model demonstrates improved performance on fine-grained visual recognition tasks and object detection tasks.

### Weaknesses
1. Relatively Limited Novelty.
The authors use off-the-shelf models, such as CLIP and LLaVA, for fine-grained vision recognition and object detection. However, “multi-query re-ranking techniques” in RAG have already been widely adopted, for example, in Re2G (Retrieve, rerank, generate) and RankRAG. I did not observe any specific improvements in the Retrieving or Ranking strategy tailored to the fine-grained recognition task. This limits the novelty of the proposed framework.

2. Concern of Practical Application.
Although FineR previously demonstrated the use of large models for fine-grained vision recognition, I still question the necessity of using large models. Why not use specialized/expert models with much smaller scale to accomplish this task? To my knowledge, these expert models already perform well on the tasks evaluated by the authors. Based on this concern, I believe that using MLLM for this task should allow for open-set responses (such as providing interpretability) rather than simply using MLLM for re-ranking final predictions.

3. Need more discussion of fine-tuning for re-ranking.
I noticed that the re-ranking operation requires fine-tuning the MLLM to achieve satisfactory performance. Although the authors claim that "RAR is not sensitive to changes in the fine-tuning dataset for ranking," they only conducted experiments on FGVC-Aircraft and Stanford-Cars. I believe this may be insufficient. If using a dataset with severe domain gap with the test datasets, catastrophic forgetting might occur, and I suggest that the authors discuss this issue.

### Questions
The questions are listed in the “weakness” section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces RAR (Retrieving And Ranking), an approach to enhance Multimodal Large Language Models (MLLMs) with a retrieving and ranking augmentation. The proposed technique aims to address the challenges faced by models like CLIP and MLLMs when applied to fine-grained visual recognition tasks and datasets with large vocabularies. By integrating a multimodal retriever and leveraging a ranking mechanism, RAR seeks to improve zero-shot and few-shot recognition accuracy across diverse datasets.

### Strengths
RAR’s design, particularly the use of CLIP-based retrieval augmented by MLLM ranking, is well-founded and thoughtfully justified. The use of retrieval augmentation with a multimodal memory structure effectively reduces the dependency on extensive context windows, which is a known limitation in handling large vocabularies.

### Weaknesses
Incorporating a detailed error analysis on retrieval failures or ranking misclassifications would provide insights into areas where RAR may need refinement, especially regarding failure cases in subtle category differentiation.

### Questions
The paper mentions, "Although the brute force method is inherently straightforward, its efficiency markedly diminishes as the dataset escalates to the magnitude of millions of embeddings." The HNSW method can significantly improve retrieval speed. So, how can we quantify the complexity of brute force retrieval and HNSW when the dataset scales to millions of embeddings? Please provide specific comparative results.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses the issues of CLIP's weak fine-grained category classification capabilities and MLLM's limitations when dealing with extensive vocabularies and fined-grained categorizations, by proposing a method named RAR. Specifically, it involves pre-storing features information about each category's images or labels in the dataset through CLIP's encoder. This stored information is then matched with the images’ features that need to be classified using either image-image kNN or image-text kNN methods to select the top-k targets. These top-k candidate targets are subsequently fed into MLLM for ranking, ultimately yielding the final prediction results.

### Strengths
1.The paper is well-written, and the method's details are well-explained. The drawings are appealing and intuitive. 
2.The experiments are comprehensive and conducted on a sufficient number of datasets, and improvements have been achieved on many datasets.
3.The paper includes a complete evaluation and ablation study to understand the impact of the propose components.

### Weaknesses
The method does not fundamentally address the fine-grained categorization and extensive vocabulary classification issues of CLIP and MLLM. Essentially, it is more like a simple combination of the two, which lacks novelty and not suitable for ICLR.

1. Although the paper’s title is about augmenting MLLM, it is mostly just a simple application of MLLM. The SFT and in-context learning techniques used in the thesis only improve the MLLM's ability to maintain output formats, but do not actually enhance its classification ability. This is why the SFT effects on different datasets in Table 5 are not significantly different.

2. The motivation was the improvement in fine-grained categories and vast vocabulary classification for CLIP and MLLM, but since no substantial optimization was done for CLIP and MLLM, and their classification abilities for this scenario are relatively weak, so the improvement of their combination is not significant, as shown in Table 1 against FineR and Table 5. The reason why the improvement was significant in Table 4 was because the object categories in LVIS were 1,000, which was not enough, and could not effectively prove the motivation.

3. The performance increase in Table 2 is all compared with CLIP+KNN, which makes people feel that RAR improves CLIP rather than MLLM, and the performance increase here is suggested to be worse than the sub-optimal result.

### Questions
When the K of K-NN is determined, the upper limit of the method's capability is determined by CLIP (whether the prediction result is in topk), and MLLM only helps the method approach this upper limit. In some cases, even the performance of CLIP will limit the play of MLLM (if the correct category is not in topk). Also, poor MLLM performance can also undermine CLIP's capabilities (see Table 2 Flower102 dataset).

Therefore, I want to see the ablation experiments under different k settings. In-context learning can be used if SFT is too time-consuming.

### Soundness
2

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
This paper introduces RAR (Retrieving and Ranking), a method to enhance multimodal large language models (MLLMs) in visual recognition tasks. RAR combines CLIP’s broad retrieval ability with MLLMs' fine-grained differentiation abilities. It retrieves candidate categories from external memory based on the input image, which the MLLM then ranks to make a final prediction. Extensive experiments show that RAR significantly improves performance across various visual benchmarks, including fine-grained classification, few-shot recognition, and zero-shot object detection.

### Strengths
- Well-written and straightforward
- Easy to understand with a clear methodology
- Achieves strong results on the proposed benchmark
- Thoroughly tested across multiple visual benchmarks, including fine-grained classification, few-shot recognition, and zero-shot object detection

### Weaknesses
 - Limited novelty in the proposed method.

### Questions
- Could you clarify why vanilla LLaVa results are not included in Table 1? Additionally, for zero-shot image classification, is there a comparison to vanilla CLIP using only category names?

### Soundness
4

### Presentation
4

### Contribution
2
