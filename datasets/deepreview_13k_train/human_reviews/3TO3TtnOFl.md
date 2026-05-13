# BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Retrieval augmentation addresses many critical problems in large language models such as hallucination, staleness, and privacy leaks.
However, running retrieval-augmented language models (LMs) is slow and difficult to scale due to processing large amounts of retrieved text. 
We introduce binary token representations (BTR), which use 1-bit vectors to precompute every token in passages, significantly reducing computation during inference. 
Despite the potential loss of accuracy, our new calibration techniques and training objectives restore performance. Combined with offline and runtime compression, this only requires 127GB of disk space for encoding 3 billion tokens in Wikipedia.
Our experiments show that on five knowledge-intensive NLP tasks, BTR accelerates state-of-the-art retrieval-augmented language model inference by up to 4x and reduces storage by over 100x while maintaining over 95\% task performance

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a method to accelerate inference speed of retrieval augment language models, while reducing the required storage space. The authors use binary token representations and compression (for collapsing the embeddings of similar tokens) to increase speed. They show that their method maintains up to 95% task performance when compared with the base method.

### Strengths
The strengths are as follows:
* Retrieval augment language models are becoming increasingly popular. Increasing the inference speed and reducing the memory footprint of such methods will be quite useful. The authors demonstrate that they can achieve a 4x speedup in inference speed and a 100x reduction in storage space.
* The authors present results across multiple datasets.
* The authors ablate all of their modifications and show how each one affects performance, speed and memory.

### Weaknesses
The weaknesses are as follows:
* Some things like passage representation regularization are mentioned in passing and it would be helpful if the authors added a couple sentences providing context and explaining what this is. Specifically, it's unclear what the motivation is for this regularization and how it is implemented. Is it applied to all layers or only specific ones? What is the impact of this regularization on the final performance and how does it compare to not using it?
* No motivation or explanation is given for why distillation is required/helpful. It is not clear why the decomposed reader model would need distillation to maintain performance. What is the mechanism by which distillation helps the model, and what are the specific benefits of distilling from the upper layers? 
* It is not clear if the linear projection layer for passage representation recovery is a learnable layer. Also, the $L_{recovery}$ term is confusing; $b_i$ is the binary passage representation and $h_i$ is the original passage representation, where is the projection layer used? It would be helpful to see the exact equation for $L_{recovery}$ and a description of the dimensions of each variable. It is unclear how the binary representation is transformed back to the original space, and how this transformation affects the overall performance.
* No comparison to newer methods like Lumen.

### Questions
* Did you try different thresholds for r%? How much did the performance change?
* Is it important to do runtime compression after every block?
* How slow is the bipartite matching for compression?

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
This paper proposes binary token representations for retrieval-augmented LMs.
The goal is to increase inference speed and reduce storage requirements.
The key idea to achieve this in BTR is to create cacheable binary token representations of the retrieved passages such that the passage encoding can be precomputed offline and stored in a compact format.
Empirical evaluation on knowledge-intensive NLP tasks shows the effectiveness of their approach w.r.t. corresponding non-optimized retrieval-augmented LM:
* inference speed: 2-4x
* storage: up to 100x reduction (e.g., 10TB --> 100GB)
* task performance: retains 90-95% of original performance

### Strengths
* Importance and relevance of topic: LLMs are everywhere and retrieval augmentation LMs addresses critical problems in LLMs such as hallucination, staleness, and privacy leaks, but suffer from low inference speed and huge storage requirements.
* BTR has much lower storage footprint than other approaches, is more scalable and has lower inference speed at the expense of a "modest" loss in performance.
* The paper reports numbers for actual throughput for a more realistic comparison of efficiency across different systems.
* The code will be publicly available.

### Weaknesses
 * "BTR is more accurate and efficient than other baseline methods.": According to Figure 3, the proposed BTR appears to be on the Pareto front. I.e., it isn't substantially better than existing methods but provides a different tradeoff between speed and accuracy. This makes it hard to assess the merits of BTR. To make the result less sensitive to a specific operating point and better comparability, it would be interesting to show, for example, how the tradeoff changes with the resolution of the representation (1-bit vs b-bit representations). Furthermore, adding sub-optimal points to the plots would give a more comprehensive picture (for example, LLaMA at different size/speed/accuracy).
* The benefits at runtime come with a clearly more complicated training pipeline and increased training time. How much?
* Figure 3: Why do the plots include Atlas-Q but not the original model (Atlas)? Also, I can't see any small points for Atlas-Q and LLaMA2-7B.
* Different spelling in title and text: "retrieval augmented language model" vs "retrieval-augmented language model".
* Funsion-in-Decoder → Fusion-in-Decoder

### Questions
* The text accompanying Figure 3 says "BTR presents better efficiency versus accuracy trade-offs by maintaining high
accuracy and inference throughput with a smaller storage footprint.": Could you please clarify what you mean with this? As for me, BTR is another point on the Pareto front.
* A method that allows to choose an operating point on the Pareto front would be more useful in practice than a method for a single operating point. Can BTR be extended along this dimension?
* Could you please say a few words on the complexity of the training pipeline?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce multiple compression techniques to speed up retrieval-augmented models collectively referred to as BTR. These techniques are specific to a certain class of models like BERT and Atlas. And it's not clear that they will generalize to other types of retrieval-augmented LMs. There are many steps in the compression that are all required for good speed and accuracy. These are covered well in the ablation table:

* binary passage representation is needed to reduce storage (speed is almost the same when using the dense passages).
* offline compression gives a minor improvement in storage and speed at cost of accuracy.
* online compression gives big speed improvements.
* passage token distillation improves representation of dense vectors, and is important for good accuracy. This filters for 50 percent of the most salient tokens according to attention, although it is not clear if this was necessary and maybe distillation of 50 percent random tokens would yield similar performance.
* passage recovery loss for the binary vector retains semantic information of the dense vector, and is important for good accuracy.

The results empirically show the speed (2-4x) and storage benefits (100x) of BTR, albeit at about 5 percent drop in performance. The paper is clearly very informative with analysis and details, but sometimes some basic details are missing and the benefits of BTR are occasionally oversold.

### Strengths
1. Storage savings of 100x. This will make retrieval more available to many, since storage can often become a bottleneck in retrieval-augmented ML.

2. Speed savings of 2-4x. Although this is similar speed improvement as Deformer (Cao et al), it leads to 5 percent accuracy loss which is worse than Deformer's 1 percent accuracy loss.

3. Extensive experiments and analysis. There are some confusing or missing details, but these can be probably be easily fixed.

### Weaknesses
1. There are many steps required to make BTR work well. Of course, that is also why this is a valuable paper since it outlines what these steps are.

2. There is a substantial (about 5 percent) drop in model accuracy. It's not clear whether 2-4x speed boost is enough value to make up for this, although the storage improvements are definitely very valuable.

3. The paper is not very self-contained. It seems like the reader is expected to have read Cao et al and Atlas papers very closely. This is not ideal. For example, it is hard to understand what it means by "decomposed model" or "decomposed reader" in sec 3.2. Also, the reader is left to infer that retrieval is done at the passage level, but passages are incorporated at the token-level.

4. (minor) The paper is hard to read. In more than one instance, a method is used but is "defined below", so we must constantly revisit parts of the reading to get a full understanding.

5. (medium) "BTR is more accurate and efficient than other baseline methods" This claim can easily be interpreted as "all other baselines", which is not accurate. There are baselines that are more accurate or more efficient. This should probably be revised to be more accurate/specific. Also, I am not sure why BTR base is constantly bolded in Sp column when it is not the best value.

6. There is not a good breakdown of efficiency between retrieval + inference. Perhaps alternative methods akin to DistilBERT will give a substantial speed boost plus keep good performance.

7. (minor) Similarly, given the emphasis on storage it would have been helpful to see some basic baselines to improve storage. Although I am not sure what else can easily achieve 100x savings without larger tradeoff in performance.

8. (very minor) It was confusing whether the token distillation is taken directly from Cao et al, or is something new.

### Questions
Q1: Why do we need Step 2 for the decomposed reader? Doesn't Step 1 already provide a reader?

Q2: "This is likely because prior work only considers a single passage where all tokens are important to the task" What does this mean? Surely many prior works use more than one passage.

typo: Funsion-in-Decoder

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article introduces Binary Token Representation (BTR) to solve the problem that running retrieval-enhanced language models (LM) is slow and difficult to scale. Due to the potential loss of accuracy, the authors propose a passage representation recovery objective and a query-aware passage token distillation objective to restore performance. By combining offline and runtime compression, the proposed method speeds up state-of-the-art inference by 4x and reduces storage space by more than 100x in five knowledge-intensive NLP tasks, while maintaining over 95% of task performance.

### Strengths
1.  For the first time, the authors construct binary token representations to improve the efficiency of retrieval augmentation models, an approach that has never been explored before.

2. The paper is very well-written and well-organized and provides clear motivation, background, and some technical details for the proposed model, including model quantization and binarization.

3.  Experiments are conducted on 5 datasets and provide meaningful comparisons with existing retrieval-enhanced language models such as Atlas and DensePhrase and large language models such as LLaMA2-7B. The results show that the proposed model can maintain 95% of the above task performance while improving the inference speed and greatly reducing the storage space. The paper also includes ablation studies to analyze the performance further.

### Weaknesses
1. As the paper mentions, BTR is difficult to apply to decoder-only models, and most current large language models utilize a decoder-only structure.

2. The paper only discusses FiD, which is the SOTA model in the KiLT ranking. However, it is also important to discuss other commonly used retrieval-augmented structures, such as RAG, particularly when dealing with black-box LLM.

3. For retrieval augmented language models, the number of retrieved passages is an important factor for performance and efficiency. While 
authors only set this factor to a fixed number (40 or 30 for different datasets), thus additional experiments should be involved.



### Questions
**A**: In addition to BERT, what other experiments have you conducted on the Encoder-Only model? For example, Deberta, COCO-LM, and so on.

**B**: The author claims to have utilized different random number seeds for 5 runs. It would be beneficial to include the standard deviation of the results in Table 1.

**C**: In the Calibrated binarization section (Section 3.1), the author asserts that employing a straight-through estimator (STE) yields superior results compared to combining the annealing method with the tanh function. Are there any analytical experiments conducted to substantiate this claim? Additionally, is it viable to utilize a linear layer and sigmoid function for binarization? I recommend the author to include additional binarization methods in the experimental section to leverage the benefits of STE.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
