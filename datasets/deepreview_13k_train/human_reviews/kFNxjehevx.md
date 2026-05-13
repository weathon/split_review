# TabFlex: Scaling Tabular Learning to Millions with Linear Attention

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Recent advances in the field of in-context learning (ICL) have demonstrated impressive performance for tabular classification, exemplified by TabPFN's success on small datasets. However, the quadratic complexity of the attention mechanism limits its applicability to larger datasets. To address this issue, we conduct a comprehensive comparison of popular scalable attention  alternatives, including state-space models (SSMs) and linear attention mechanisms, revealing that the inherent causality of SSMs hinders ICL performance for large datasets, while linear attention preserves effectiveness. Leveraging these insights, we introduce TabFlex, a model based on linear attention that supports thousands of features and hundreds of classes, capable of handling datasets with millions of samples. Extensive experiments demonstrate that TabFlex is significantly faster than most existing methods while achieving top-two performance on small datasets among 25 baselines, with a 2$\times$ speedup over TabPFN and a 1.5$\times$ speedup over XGBoost. On large datasets, TabFlex remains efficient (e.g., approximately 5 seconds on the `poker-hand` dataset, which consists of millions of samples), while achieving relatively solid performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on extending the applicability of in-context learning (ICL) to a larger scale of datasets without sacrificing performance and latency. Specifically, the author expands on the scalability of TABPFN, where they first provide an investigation of the state-space models (SSMs) and linear attention. The empirical findings show that compared to SSMs, linear attention is better for maintaining comparable performance while improving computational efficiency. The author also conducts extensive comparisons with other methods across a diverse range of datasets, showing that the proposed method, i.e., TABFLEX, has robust performance with impressive computational efficiency.

### Strengths
(1) Extending the applicability of in-context learning to larger datasets for tabular classification is crucial for many real-world applications. 

(2) The identified scalability limitation of TabPFN is relevant; the corresponding attention choice, i.e., the non-causal linear attention, can also achieve comparable performance with TabPFN with a large speedup.

### Weaknesses
 (1) The empirical findings in 4.1 seem to be restricted to TabPFN, and it is hard to see whether they can be applied to a broader range of in-context learning designs. The author may want to show that they are general to other frameworks of in-context learning.

(2) The technical novelty is limited. The author leverages the empirical study of two kinds of attention mechanisms to identify the "optimal" candidate for TABPFN, as stated in lines 291-292. Although the empirical study is relevant, it does not bring novel technical contributions to the community as the author does not propose a new technical design to even further improve linear attention. Moreover, given that all the design choice is tailored to TABPFN, it is hard to convince the reviewer that the present paper brings sufficient contributions to the community. If the author wants to justify that the linear attention is exactly optimal and there is no other choice better than it, then the reviewer may suggest that the author provide rigorous theoretical analysis to justify their choice.

Minor:

(1) There is a formatting issue in Fig. 4.

### Questions
Please refer to the Weaknesses section.

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
3

### Summary
The paper proposes a new method to process tabular data which can handle significantly more data and number of classes. Extensive experiments show that the proposed method achieves strong performances while being much faster compared to methods with similar performances.

### Strengths
1. The paper studies the problem of scaling up the application of attention-based methods to hundreds of classes with millions of data points. This significantly improves the applicability of similar methods on large datasets.
2. The paper studies various tradeoffs of introducing linear attentions and architectural alternatives where the authors shared lots of insightful findings.
3. The end performance is strong, as shown in Table 1 and 2, the method is able to achieve top 3 performances with little performance degradation compared to  other SOTA methods which require significant more time.
4. The paper is well written and the experiments include comprehensive number of baselines and datasets.

### Weaknesses
1. Looks like there is some formatting issue such as Figure 4.
2. Given the large amount of data presented in the tables, it's better to mark the top 3 with underline or bold so that we don't need to go over the large amount of data to find them out.
3. The use of different specialized models are good, are there any ways such as implementing a router instead of hard coding them.

### Questions
1. in Algorithm 1, how does random projection affect the final performances?
2. this brings another question, if we can randomly project the features to 1K, can we project them selectively? What's the benefit of scaling up with linear attention than just perform feature selection / augmentation?
3. Besides simply using ICL, maybe we can explore data pre-processing to aid the ICL to achieve better results?

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
4

### Summary
This paper works on deep learning for tabular data, specifically using Transformers. The authors argued that existing Transformer-based models are "slow" either in training (need to re-train or fine-tune for each dataset) or inference (need to take the whole training set as input to provide the context). The authors pointed out that the standard attention module is the main cause (especially for long context in in-context learning), and proposed to replace it with linear attention. The authors conducted extensive experiments to show the superior performance of linear attention in tabular data --- it achieves significant speedup without sacrificing accuracy --- making Transformers with linear attention a suitable and preferable option for dealing with tabular data in an in-context learning fashion.

### Strengths
S1. The paper is very well-written and well-motivated, with adequate background and clear technical details. 

S2. The paper conducts extensive experiments and analyses to justify the strength of linear attention for tabular data.

S3. The proposed idea is simple and widely applicable --- in my opinion, this is definitely a strength rather than a weakness. I could imagine if this paper is accepted (or just on arXiv), it will attract lots of attention; TabFlex will become a must-compare baseline.

I very much enjoy reading the paper.

### Weaknesses
That said, this paper has some critical weaknesses that the authors should try to address. I may miss some details; some weaknesses may have been addressed in the manuscript already. If so, please kindly point me to the sections and lines.

W1. First, I do not consider the analysis of Mamba as a contribution. I humbly do not see the feasibility of using a sequence model to solve in-context learning for tabular data. Thus, the poor performance by Mamba, to me, is expected. In my humble opinion, in-context learning for tabular data is a smart nearest neighbor (or non-parametric) algorithm. By default, a nearest-neighbor method should not rely on a sequence, unless there is an inherent sequence in the data. For example, if the authors show that ordering the training data based on their distance to the test data would improve Mambda's performance, then I think it will be an interesting finding and insight.

W2. The main weakness of the paper is the lack of insights. Yes, I see the extensive experiments and superior performance (time and accuracy). The reason for the efficiency/latency improvement is obvious and intuitive. However, I do not see a clear reason why linear attention would keep the same accuracy (or not sacrifice much) as standard attention. I'm not very familiar with the comparison between standard attention and linear attention in other contexts (e.g., LLMs) but I suppose that linear attention is not as good as standard attention (in terms of accuracy or reasoning capability) in many use cases; otherwise, it should have been the go-to module. It would be great if the authors could provide some more discussions and insights (not just quantitative empirical results) into why linear attention is a good option (beyond the latency aspect) in tabular data.

W3. While it may have been discussed in prior work, I would like to see a bit more background or justification as to why in-context learning is reasonable for solving tabular data. What does the Transformer really learn? Given that linear attention is inspired by inner products after learnable projections, it would be great for the authors to link in-context learning for tabular data to kernel-based methods.
FYI, I'm a supporter of using in-context learning to solve tabular data, but just hope that the paper can provide the readers with more insights beyond showing good performance.

W4. The conditional model selection looks quite naive. It just trains three models and uses a hard-coded rule to decide which model to use. What are the criteria to make the separation of the three models? What will be the accuracy of the three models given a fixed dataset? (I may miss some analyses; if so, please kindly point me to the corresponding lines or sections.)

### Questions
Besides the weaknesses above, I have a few more questions that I would like the authors to discuss OR compare.

Q1. Linear attention is particularly advantageous (in terms of time) in long-context scenarios. As traditional ML methods like SVM and nearest neighbors already show that the prediction of the test data can be reliably made based on a subset of training data, do we really need the whole training dataset as the context? For example, can we find a "core set" of training data to be the context? Or, can we order the training data by their distances to the test sample, and only use the closest 100 samples as the context? Will this really degrade the accuracy? 

Q2. In section 3 background (Lines 153 - 157), all the test data are input to the model at once. Since the training samples do not attend to the test samples and the test samples do not attend to each other, inputting all the test samples is equivalent to inputting each of them one by one, but faster. In real-time inference, test data usually come one by one, not in a batch. Will such a speed-up still hold? (The answer to this question won't change my rating, but I'm just curious.)

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce TabFLEX. TabFLEX uses the straightforward PyTorch implementation of linear attention to achieve considerable speedup compared to TabPFN. The authors also train new PFN checkpoints designed to handle larger contexts, taking advantage of linear attention's more efficient inference to achieve faster wall-clock performance and improved utility compared to TabPFN and other baselines.

### Strengths
* The authors train and release new PFN checkpoints with a broader range of compatibility and utility, compared to TabPFN.
* The writing is clear.
* The authors provide many experiments demonstrating the efficacy of their method.
* The authors release code to reproduce their work.

### Weaknesses
MAJOR

* This paper's core technical contribution is, as the authors put it, utilizing the straightforward PyTorch implementation of linear attention to replace softmax attention in TabPFN [https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html]. Why does TabPFN not already use linear attention? As of PyTorch 2.0, this can often happen by default, with no changes required to the code base. Even if some minor alterations to the code were necessary, it's not clear why this simple engineering task is worthy of a standalone paper.
* Because switching to linear attention is such a straightforward process and does not require model retraining, it would be easy to transition *all* of the transformer-based methods described in the paper; this would be a fairer comparison, since the authors did not contribute a new learning algorithm. If this was done, I would expect most baselines to improve substantially, including TabPFN.
* Given that the choice of linear attention method is a main technical contribution, it would have been very helpful to see comparisons to more baselines than just a SSM; there are many variants of linear attention available in PyTorch [https://pytorch.org/blog/flexattention/]. 
* The authors' finding that the inherent causality of SSMs impedes ICL performance compared to non-causal mechanisms is quite interesting, but the experimental results don't totally support this argument. Fig. 2(a) caption states, "The non-causal masked model shows better sample utilization and accuracy as the number of samples grows. In contrast, the causal model’s accuracy declines." However, this is not the actual effect shown; accuracy improves *up to a point* (appears to be around 500 samples), then declines. The authors' argument about causality doesn't explain why there should be an inflection point well past the zero-sample mark, only after which performance declines.

MINOR

* The layout of Fig. 4 contains some overlapping text.

### Questions
* Why did the authors not consider more variants of linear attention?

### Soundness
3

### Presentation
3

### Contribution
1
