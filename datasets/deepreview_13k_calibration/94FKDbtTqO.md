# Rethinking the bert-like pretraining for dna sequences

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 3, 6, 6

## Abstract
With the success of large-scale pretraining in NLP, there is an increasing trend of applying it to the domain of life sciences. In particular, pretraining methods based on DNA sequences have garnered growing attention due to their potential to capture generic information about genes. However, existing pretraining methods for DNA sequences largely rely on direct adoptions of BERT pretraining from NLP, lacking a comprehensive understanding and a specifically tailored approach. To address this research gap, we first conducted a series of exploratory experiments and gained several insightful observations: 1) In the fine-tuning phase of downstream tasks, when using K-mer overlapping tokenization instead of K-mer non-overlapping tokenization, both overlapping and non-overlapping pretraining weights show consistent performance improvement.
2) During the pre-training process, using K-mer overlapping tokenization quickly produces clear K-mer embeddings and reduces the loss to a very low level, while using K-mer non-overlapping tokenization results in less distinct embeddings and continuously decreases the loss. 3) Using overlapping tokenization causes the self-attention in the intermediate layers of pre-trained models to tend to overly focus on certain tokens, reflecting that these layers are not adequately optimized. In summary, overlapping tokenization can benefit the fine-tuning of downstream tasks but leads to inadequate pretraining with fast convergence. To unleash the pretraining potential, we introduce a novel approach called RandomMask, which gradually increases the task difficulty of BERT-like pretraining by continuously expanding its mask boundary, forcing the model to learn more knowledge. RandomMask is simple but effective, achieving top-tier performance across 26 datasets spanning 7 downstream tasks. For example, RandomMask achieves a staggering 65.83\% in Matthew's correlation coefficient for epigenetic mark prediction, which is a groundbreaking increase of 14.02\% over the baseline and a remarkable 4.82\% improvement over the SOTA results.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper conducted an extensive study on using BERT-like models for pretraining with DNA sequences. Their experiments showed that using a tokenization approach that overlaps K-mers gives better results during the fine-tuning stage, regardless of whether the pretraining involved overlapping or not. However, they found that the commonly used method of overlapping tokenization during the pretraining phase caused the model to converge too quickly, which resulted in inadequate training.

To tackle this issue, the authors introduced the Random-Mask method. This method involves pretraining with dynamically changing the boundaries of the masked sections, which pushes the model to assimilate richer knowledge. They observed that when they expanded the mask boundaries during different training phases, there was a notable increase in the loss value. This increase in loss suggests that the model encounters new challenges and continues to learn, as evidenced by a downward trend in the training curve for each phase where the mask boundary is expanded.

They tested their approach on a total of 28 datasets spanning 7 downstream tasks. Across these tasks, we consistently achieved top-tier performance.

### Strengths
The paper is well-written and presents its findings in a clear and logical manner, effectively explaining all observations and results. I especially like how it points out important observations step by step until it introduces the new technique. The graphs showing how the model's errors changed during training, attention maps and t-sne plots that help visualize the data made it easier to get what the paper is saying.

### Weaknesses
The evaluation section is lacking in clarity. It would be helpful to answer the questions listed below and help readers understand how RandomMask overall improves the performance of downstream tasks.

### Questions
(1) How does the RandomMask method compare with alternate tokenization approaches such as BPE (proposed in DNABERT-2)?
(2) How does the RandomMask improve the internal representations - Can you see visible differences in embedding representations for downstream tasks (e.g Biotype Embeddings shown in HyenaDNA)
(3) How does RandomMask compare on the benchmark datasets listed in  HyenaDNA?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
#### post-discussion
---
After the discussion I decide to keep my rating.

Overall, I think the empirical findings and the proposed RandomMask could contribute to the DNA representation learning community. However, my main concern is the presentation of this paper.

1. Current version of paper could be misleading in terms of the topic. Tokenization/masking strategies are important but not everything. The authors justified that the "primary influence on BERT-like pre-training are tokenization and masking", which does not make sense to me. We have other problems like the training objectives, positional encoding and sequence segmentation/construction, etc.
2. The three observations and the proposed RandomMask are both interesting. But the Section3 (observations) and Section4 (the method) are not connected well. It would be hard for the readers to understand why/how RandomMask can help with the issues discussed in Section3.

I didn't find these issues addressed in the updated manuscript. In fact, I believe a re-organization of the paper is needed (e.g., make the observation more concise and the sections more integrated). Reviewer SHyo and 45WA also mentioned the clarification issues. We will not publish the paper with all the rebuttal materials together, so the readability of the manuscript itself is important.

#### previous review 
---
The authors of the paper initially conduct empirical experiments and analysis on the use of overlapping tokenization in BERT-like pretraining for DNA sequences. Their observations reveal that: 1) overlapping tokenization consistently enhances fine-tuning performance; 2) models trained with overlapping converge more rapidly; 3) overlapping can result in sparse attention within intermediate layers.

The authors claim that above observations demonstrate the limitation of existing overlapping tokenization. Subsequently, the authors introduce a dynamic overlapping strategy, referred to as RandomMask, for the pretraining of DNA sequences. Experimental evidence from a range of downstream tasks suggests that RandomMask consistently improves performance.

### Strengths
* Extensive empirical results and analysis, providing some findings about overlapping strategy in DNA tokenization, could benefit the community.
* The proposed method RandomMask achieves SOTA on various downstream tasks.
* The proposed RandomMask is effective but simple. It could be easy to be re-implemented and deployed for further research.

### Weaknesses
While this paper provides extensive empirical results and quantitively demonstrates the effectiveness of RandomMask, there are several areas where it could be further enhanced. My main concerns are as follows:

1. The authors might consider refining the focus of this work. The true contribution appears to be the improvement of the overlapping strategy tokenization for DNA pretraining, which diverges from the broader theme of "rethinking the pretraining for DNA sequence."

1. The motivation behind the study is somewhat unclear. Although the authors identify three potential challenges -- rapid convergence, the risk of under-training, and the potential for sparse attention -- they do not adequately explain how RandomMask addresses or mitigates these issues. It's not clear how the proposed masking strategy directly tackles the identified problems. For instance, the connection between the dynamic masking and the mitigation of rapid convergence is not well-established.

1. There is a lack of experimental analysis supporting the source of the observed improvements, which is crucial for substantiating the paper's main claims. For example, besides the quantative improvements, does the rapid convergence and under-training still exist after applying RandomMask? The paper needs to provide more evidence that the proposed method is indeed addressing the identified issues, rather than just achieving better performance.

1. The comparison in Observation 1 does not seem to be an apples-to-apples comparison. Overlapping represents more patterns and creates longer sequences for the same DNA length. It would be beneficial to understand if the conclusion holds for different lengths of k-mer. The impact of sequence length needs to be carefully controlled to isolate the effect of overlapping tokenization.

1.  The paper's presentation could be improved in several ways:
    1. The introduction is somewhat verbose, indirectly causing the first two weaknesses and making the paper hard to read.
    1. Placing Figure 1 and Table 1 on page 1 would improve readability, given that the main content describing Figure 1 and Table 1 is in the first page.
    1. The separate table on the left in Table 2 appears to be redundant.
    1. The experimental settings in Section 3 lack detailed descriptions, potentially making reproduction difficult and potentially misleading. For example, the specific hyperparameters used for pre-training and fine-tuning are not clearly stated.
    1. A thorough proofreading could enhance the clarity of writing and word choice.

1. It would be beneficial to further explore whether sparse attention is indeed a problem for DNA sequence representation. Sometimes, sparse attention can improve generalization [1]. This might depend on different sub-sequences and the various functions of different layers when modeling cross-attention. I would appreciate further elaboration on the limitations of sparse attention in DNA sequence representation. The paper should clarify whether the observed sparse attention patterns are detrimental to performance or if they are a natural consequence of the model's learning process.

### Questions
See Weakness section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The author presented three observations by comparing the overlapping with non-overlapping tokenization method: (a) overlapping tokenization is always better than non-overlapping tokenization in the fine-tuning phase; (b) the loss overlapping tokenization method drops rapidly and result in a fast convergence of embedding space; (c) focused attention has been observed in the overlapping tokenization method. Both (b) and (c) indicate the overfitting problem in overlapping tokenization. The author proposed a novel RandomMask method to mitigate the overfitting issue by gradually increasing the complexity of the task. Based on the author’s experiment, the RandomMask+BERT outperformed the other benchmarks algorithms.

### Strengths
[Originality and Significance] The author presented two original findings. One is that the overlapping tokenization always performs better in the fine tuning stage, regardless of the tokenization method in the pre-training. This is different from the conventional wisdom and could provide the insights for many related research and applications. The second contribution is that gradually increasing the complexity during the training could mitigate the overfitting issue and achieve better performance by combining fast convergence and generalizability. This method could inspire other researchers to consider similar techniques to balance the convergence and generalizability. The performance of the RandomMask algorithm is better than the precedent algorithms in different tasks, which is a significant result for the DNA sequence analysis. 

[Organization] The paper is presented in a well-organized way, from the observations to the new algorithms. Both the them bring new knowledge to the field.

### Weaknesses
[Clarity] The experiment and result section is relatively short. Some more clarifications would be helpful. For example, (a) when describing the baseline, the author mentioned “All models are trained on human genome and fine-tuned on the benchmark datasets with identical settings.” The “identical” setting does not bring clarity on how the mask is generated. Does this mean all the algorithms are trained and fine tuned with 15% token masked? This setting is slightly different than the original setting in the “Nucleotide Transformer” paper. Specifically, it is unclear if the baselines also used a dynamic masking strategy or a fixed masking rate, and whether the masking was applied at the token or sub-token level. (b) “Finetuning” section discussed the dataset in a detailed way; however, the details of the algorithm setup in the fine tuning is not discussed. For instance, the learning rate, batch size, optimizer, and number of epochs used during fine-tuning are not specified, making it difficult to reproduce the results. 

[Quality] The value of RandomMark (or training with gradually increased difficulty) can be better verified through experiments. For example, the author presented the result using the training with 5 phases. It would be great if the author could compare the result with different numbers of phases: one phase with maximum difficulty, two phases with two different difficulties, and etc. This would help to isolate the effect of the multi-phase training approach and determine if the specific number of phases used is optimal or if a simpler approach could achieve comparable results. Furthermore, it would be beneficial to see the performance of the RandomMask approach with a fixed mask size throughout the pre-training, to better understand the benefit of the gradual increase in difficulty.

### Questions
Q1: Algorithm 1 is not very clear to me. For example, if the r <= p at position i, [i − m/2 + 1, i + m/2] will be masked. The following nucleotide should be i+1, or I+m/2+1? If the next one is i+1, the mask range could be overlapping and can grow to be very long.

### Soundness
4 excellent

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses the growing trend of applying large-scale NLP-style pretraining to life sciences, particularly in DNA sequence analysis. It highlights the limitations of existing methods, the advantages of K-mer overlapping tokenization in downstream tasks, and the introduction of "RandomMask," a novel approach that significantly improves pretraining performance in life sciences applications, achieving remarkable results in epigenetic mark prediction.

### Strengths
Thorough analytical background on the method

### Weaknesses
Not much applicable to general machine learning, too specific in bioinformatics

- In the description of Table 2, what are MCC and PCC?  The reviewer is aware that they are later explained in Experiemnt section, but what they are and what they do need to be briefly explained in the description of Table 2 as well for the readers who are not in life sciences field. 

- The authors say they progressively expand the masking boundary to prevent easy learning. Shouldn't it be the other way around? The reviewer believes that the masking boundary should progressively contract. What is the point of showing the shorcut first and complicating the learning? The model would already learn the shortcut if the masking boundary progressively expanded. An additional experiment on this needs to be conducted.

### Questions
Refer to Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
