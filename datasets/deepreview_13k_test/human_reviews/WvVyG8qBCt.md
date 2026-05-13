# DPFormer: Learning Differentially Private Transformer on Long-Tailed Data

- Decision: Reject
- Scores: 3, 6, 5, 6

## Abstract
The Transformer has emerged as a versatile and effective architecture with broad applications. However, it still remains an open problem how to efficiently train a Transformer model of high utility with differential privacy guarantees. In this paper, we identify two key challenges in learning differentially private Transformers, i.e., heavy computation overhead due to per-sample gradient clipping and unintentional attention distraction within the attention mechanism. In response, we propose DPFormer, equipped with Phantom Clipping and Re-Attention Mechanism, to address these challenges. Our theoretical analysis shows that DPFormer can reduce computational costs during gradient clipping and effectively mitigate attention distraction (which could obstruct the training process and lead to a significant performance drop, especially in the presence of long-tailed data). Such analysis is further corroborated by empirical results on two real-world datasets, demonstrating the efficiency and effectiveness of the proposed DPFormer.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper identifies two key challenges in learning differentially private Transformers, i.e.,
heavy computation overhead due to per-sample gradient clipping and attention distraction due to
long-tailed data distributions. The authors then proposed DPFormer, equipped with Phantom Clipping and
Re-Attention Mechanism, to address these challenges. Empirical results are also provided to justify the new design.

### Strengths
The paper aims at solving issues and improving the performance of DP transformers. Personally, I think this problem is very important and a key step towards enabling large model training under differential privacy. Given the popularity of large language models and transformers, this problem should be interesting to both DP community and LLM community.

### Weaknesses
Although the problem at which the paper aims is very important, the paper does not provide a satisfactory answer and leave many questions unanswered. Most importantly, this paper needs to greatly improve its clarity: there are many places with vague languages or unstrict math, making it very hard for the reader to follow or evaluate the paper's quality. Personally speaking, there is still a long way to go before the paper can be accepted.

Here are some specific suggestions/confusion:

Phantom clipping: 
1. All the notations in Claim 3.1 are used without being carefully defined. I do not find it enough to just define them by Figure 1 or simple languages in Claim 3.1. Could we have some strict math like section 2.2 in https://arxiv.org/pdf/2205.10683.pdf?
2. I am not convinced why the phantom clipping has such great advantages over ghost clipping. Observing Claim 3.1, it has exactly the same idea (calculating the norm and avoiding gradient instantiation) with ghost clipping. Specifically, I do not understand why the BM^2 complexity is inherent to the ghost clipping under a careful implementation. With that in mind, I am concerned the paper may over-claim the advantages.
3. Looking at the results from other papers  (e.g., https://arxiv.org/pdf/2205.10683.pdf) applying ghost clipping to transformers, the ghost clipping has shown a much better memory effIciency. I do not quite understand the gap between Figure 3 and those results.

Re-attention
Generally speaking, the idea of re-attention is interesting. However, there are many vague places in both motivation and estimation, making me hard to feel convinced. Specifically,
1. The math in the motivation is not very strict. Please make some revise. Furthermore, there are many other sources of randomness in model training except for DP noise. Please specify them in the conditional distribution.
2. In section 4.1, the paper mentions that the attention distraction mainly happens when different parameters have different variance. However, in DP-SGD, the noise with the same std is added to each parameter. Could the authors explain about this?
3. Section 4.2.2 is very hard to follow. For me, it just reads like a mixture of several techniques without a clear explanation. I have several confusions. For example, is the assumption realistic assuming i.i.d. Gaussian for each dimension in parameter? Furthermore, I do not quite follow how to estimate the mean and std of the start point.

Experiments
1. Since the paper is targeting large models, it is better to have some setting for fine-tuning instead of training from scratch. Also, revealing some results when eps = infty will also be helpful.

### Questions
Please refer to weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces two treatments for training transformer models with DP-SGD on long-tailed data. The first is phantom clipping which extends ghost clipping by handling parameter sharing between input and output layer (a common practice). Phantom clipping effectively enabled more efficient DP training of transformer models in practice. The second is a re-attention mechanism which rescale the attention scores in the transformer models by their error variances due to DP noise. The methods are evaluated on two benchmark recommendation datasets and showed better performance compared to the DP-SGD baseline.

### Strengths
- This paper is well-motivated as transformer models are used in many ML applications and being able to train it with strong privacy guarantees is important for these models to scale further.
- The methods are driven with the empirical observations of the shortcomings of DP-SGD on transformer models. Parameter sharing of embedding parameters is such a common thing to do but was not considered in prior work on speeding up DP-SGD. Also DP is known for generalizing worse on the tail and the re-attention mechanism is a simple yet effective workaround.

### Weaknesses
- The experiments, as the authors acknowledged, were conducted on the smaller scale models. Also only recommendation tasks were considered. It is unknown whether these methods will be effective on larger image or text models.
- Some baselines for training with DP are missing where these methods also improve the performance of models for long-tailed data: [1] proposed a way to add DP noise adaptively according to the geometry of the loss space, which can effectively enable smaller noise on long-tailed data. [2] similarly uses auxiliary information such as the frequency of the vocabulary to apply DP noise. 
- Describing section 4 as an algorithm would be easier to read.

References

[1] Asi, Hilal, et al. "Private adaptive gradient methods for convex optimization." International Conference on Machine Learning. PMLR, 2021.

[2] Li, Tian, et al. "Private adaptive optimization with side information." International Conference on Machine Learning. PMLR, 2022.

### Questions
- Is Figure 3 based on Ghost Clipping or Book-Keeping [1]? BK is supposed to be more efficient than Ghost Clipping.
- In Equation 7, are the subscripts on the right-hand side supposed to be $X^{(l-1)}$? 

References

[1] Bu, Zhiqi, et al. "Differentially private optimization on large model at small cost." International Conference on Machine Learning. PMLR, 2023.

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
This paper studies the differential privacy in transformers. They identify two key challenges as heavy computation due to per-sample gradient clipping, and unintentional attention distraction within the attention mechanism. They propose DP- Former, equipped with Phantom Clipping and Re-Attention Mechanism, to address these challenges. The theoretical analysis shows that DPFormer can reduce computational costs during gradient clipping and effectively mitigate attention distraction. Empirical results on two real-world recommendation datasets with varying degrees of long-tailedness, showing its significant improvement in terms of efficiency and effectiveness.

### Strengths
This paper give DPformer to address the challenges of heavy computations and attention distraction.
Originality: The proposed methods addressed the two difficulties, it’s novel and has good performance. Phantom Clipping inherit the basic idea of Ghost Clipping, obtain the per-sample gradient norm without the need for instantiating the per-sample gradient. p
Quality: This methods performs well in experiments. But I doubt that whether the re-attention method after DP process can leak privacy?
Clarity: The logic structure of this paper is clear 
Significance: These two problems are very important problems for differential privacy in Transforms, so this kind of work is necessary

### Weaknesses
The correctness of this method. 
This paper uses Phantom clipping and Re-attention mechanism to overcome the difficulties of heave computation and attention distraction. The most important thing is to make the whole mechanism be differentially private and have high utility. However, they authors didn't analyze the privacy of this mechanism, especially after the re-attention. It seems this process will leak privacy.

### Questions
What is the privacy guarantee for this method?
What do NDCG@10 and HIT@10 mean?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces two main new modifications to differentially private training of transformers. They refer to it as DPFormer. The authors argue that two problems with differentially private training of transformers is i) the additional computational overhead of training with per-sample gradient (initially addressed by Li et. al. 2022 with Ghost clipping) and ii) a phenomenon the authors refer to as attention distraction. To resolve this, the authors propose Phantom clipping which also allows weight sharing (as opposed to Ghost Clipping)  and re-attention. Experiments on two datasets show improvement over some standard baseline algorithms like vanilla transformer, GRU, LSTM.

### Strengths
* __[S1]__ I appreciate the message that pre-training might not be possible for all tasks and it is important to develop algorithms that can work in settings without pre-training. This message has also been highlighted in [A,B].

* __[S2]__ It is important to show that modern DP algorithms can be run computationally efficiently, something which is often missed in works that show state-of-the-art accuracy at a huge computational cost. This problem is particularly pronounced for DP model-training where large batch sizes have somehow been used very commonly. To that effect, I appreciate the focus towards decreasing compitational cost.












[A]  "Considerations for differentially private learning with large-scale public pre-training." TPDP 2023.   
[B]  "PILLAR: How to make semi-private learning more effective" TPDP 2023

### Weaknesses
* __[W1]__ If data is long-tailed, the hand-wavy definition of this means that some parts of the data are over-represented and some parts are under-represented. As such, if the objective is to get high average accuracy (or its variant for recommendation problem), then ignoring the low frequency elements shouldn't be a problem. This paper seems to be looking at average metrics but it mentions long-tailed data in the title. 

* __[W2]__ The paper proposes a phenomenon called `attention distraction'. The suggestion is that tokens with high variance will be unfairly selected by the attention mechanism. But it is not very clear to me what this means formally. In addition, the theory seems to assume that every token's attention value is an independent gaussian, which is also unrealistic as all tokens are dependent on each other due to previous layers and I don't see why adding gaussian noise to gradients results in gaussian distribution for token activations. The whole section 4 assumes these two things but there isn't any empirical or theoretical justification for this.

* __[W3]__ The experimental comparison is not thorough at all. Please see question 3 below for a more detailed explanation of why I think that is the case.



Minor Comments
1. What do the metrics used here actually mean ? Maybe I missed it but I don't see a definition of ndcg@10 and HiT@10. 
2. Figure 1 is not very understandable as there are terms like $a_s$ and $e_s$ which is not clarified.
3. In general, the text is very heavy which can be distracting to readers. I would recommend (personally) to have shorter sentences to the point.
4. Eq 1 isn't clear what G is.
5.

### Questions
1. Regarding long-tailed data [W1] cam the authors explain
    * motivation for why that is the central part of the story and where the long-tailed data comes into play.
    * any evidence that the proposed method specifically helps for long-tailed methods.
Perhaps the authors can draw some relation from [1] ?

2. Regarding [W2], can the authors provide evidence that ``attention distraction'' 
    * truly happens without re-attention mechanism in transformer. I understand Figure 9 is supposed to show this but I don't exactly understand what the two axis here is. I am also not comfortable drawing summary statistics about this as a wider phenomenon that what is shown in the five plots. To me it appears that this is just learning a biased classifier (i.e. not learning the true signal) that puts all its signal on one token (if I understand it correctly).
    * follows the same mathematical equations that Section 4 predicts it should.
    * Re-attention actually solves it ?

3. Both the datasets and baseline algorithms are fairly restrictive. Is there any reason apart from not having pre-trained models specialised for recommendation engines, why the experiments are limited to recommendation settings. 
    * The methods should also provide benefits for NLP tasks (with and without pre-training). 
    * Also, is there a comparison with Li et. al. or any other method for training transformers or recurrent models ? Such comparisons would be needed.
    * Can the authors also try using a general pre-trained transformer for this recommendation tasks ?

[1] "Does learning require memorization? a short tale about a long tail." Proceedings of the 52nd Annual ACM SIGACT Symposium on Theory of Computing. 2020.    
[2] "How unfair is private learning?." In Uncertainty in Artificial Intelligence, pp. 1738-1748. PMLR, 2022.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
