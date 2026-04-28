# PatchMixer: A Patch-Mixing Architecture for Long-Term Time Series Forecasting

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 6, 5

## Abstract
Recently, transformers incorporating patch-based representations have set new benchmarks in long-term time series forecasting. This naturally raises an important question: Is the impressive performance of patch-based transformers primarily due to the use of patches rather than the transformer architecture itself? To explore this, we introduce \textbf{PatchMixer}, a patch-based CNN that enhances accuracy and efficiency through depthwise separable convolution.
Our experimental results on seven time-series forecasting benchmarks indicate that PatchMixer achieves relative improvements of  $3.9\%$, $11.6\%$, and $21.2\%$ in comparison to state-of-the-art Transformer, MLP, and CNN models, respectively. Additionally, it demonstrates \textbf{2-3} training and inference times faster than the most advanced method. We also found that optimizing the patch embedding parameters and enhancing the objective function enables PatchMixer to better adapt to different datasets, thereby improving the generalization of the patch-based approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an novel deep framework for Long-term time series forecasting (LTSF), which is bulit on convolutional architecture. Compared with Transformers-family, the proposed method efficiently replaces the expensive self-attention module with CNN layers. The authors claim that the proposed method is 3x and 2x faster for inference and training, respectively, rather than SOTA model. In extensive experiments on 7 LTSF benchmarks, the proposed PatchMixer method outperforms SOTA method by 3.9% on MSE and 3.0% on MAE.

### Strengths
+ PatchMixer relies on depthwise separable convolutions and employs dual forecasting heads, which are proposed with novelty. The patchmixer layer with patch (dis)aggregation operations makes sense in practice.
+ The model outperforms state-of-the-art methods and the best-performing CNN on seven forecasting benchmarks.
+ PatchMixer is 2-3x faster than SOTA and other baselines.
+ A detailed overview of the proposed method, including problem formulation, model structure, and patch embedding techniques is provided.

### Weaknesses
 - The motivation is unclear. The author only elaborates on how the module is designed, but ignores why it is designed this way.
- The writting should be improved. It would be better if the motivation is highlighted.
- Some experimental results are not convincing. E.g. in Table 4, how PatchTST performs with MSE+MAE and SmoothL1Loss?

### Questions
1. More elaboration about the motivation

2. The results of PatchTST with MSE+MAE and SmoothL1Loss

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes PatchMixer, a novel CNN-based model for time-series forecasting. In contrast to existing CNNs in this field, which often employ multiple scales or branches, it relies exclusively on patchification and depthwise separable convolutions. The proposed architecture obtains very good results across multiple datasets while being faster than the state of the art.

### Strengths
Altogether I believe this is a very strong submission with little flaws in its presentation and valuation. It is a very pleasant read with interesting insights, ablations and evaluations.

### Weaknesses
In my best assessment this paper does not have any big weaknesses other than a few minor listed here:

* There is an error in a citation in the depthwise separable convolution section of the related work section.

* I am not sure I understand the relationship between the 2D patches of CV methods and the method introduced here. Please correct me if I am wrong but, the patches used in this approach are 1D, right? I understand that other methods (Eqs. 1-3) are 2D, but I think that this is somewhat confusing. Perhaps it would be better to describe these methods in less detail here (and move details to the related work section) ?

* Following the style guidelines of ICLR, I would recommend the authors to align tables with the top of the pages and put their caption on the top.

* The results shown in Table 2 are very confusing. How are these divided? Basically all numbers here are either bold or underlined.

### Questions
There has been a line of work on long convolutional models, which are able to model long term dependencies without patching, e.g., S4 [1], CKConv [2], Hyena [3], etc. Do you have any thoughts regarding the use of these models for forecasting?

# References

[1] Gu, Albert, Karan Goel, and Christopher Ré. "Efficiently modeling long sequences with structured state spaces." arXiv preprint arXiv:2111.00396 (2021).

[2] Romero, David W., Anna Kuzina, Erik J. Bekkers, Jakub M. Tomczak, and Mark Hoogendoorn. "Ckconv: Continuous kernel convolution for sequential data." arXiv preprint arXiv:2102.02611 (2021).

[3] Poli, Michael, Stefano Massaroli, Eric Nguyen, Daniel Y. Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, and Christopher Ré. "Hyena hierarchy: Towards larger convolutional language models." arXiv preprint arXiv:2302.10866 (2023).

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a simple convolution-based model for long-range time series forecasting. The model includes patch representation, the mixing layer, and the dual forecasting heads. The PatchMixer layer captures both global and local contexts using depthwise and pointwise convolutions. The proposed framework is more efficient than the state-of-the-art Trnasformer-based model and outperforms the standard convolutional layer.

### Strengths
- The method is simple and intuitive. 
- The paper includes comprehensive evaluations. The diverse ablation study helps to understand the proposed approach.

### Weaknesses
 - The contribution of the paper is weak. The patch representation and mixer itself are not novel. Probably the way of mixing patches over the sequence is new. However, the benefit is unclear.

- Following the previous point, the improvement is marginal, especially over PatchTST. Also, I don't see a substantial benefit of the proposed model using depthwise separable convolution or dual head in the ablation study (Table 2 and Figure 4).

- The experiments are not clearly explained.
  - Table 2 is very confusing. I had to spend some time to understand what the table means. For instance, I initially didn't get the first column which is PatchMixer "minus" another module. Because PatchMixer and another module are in separate rows, it looks like the first row is PatchMixer, and the second column is a comparing model.
  - Figure 3 compares training and inference times but it's unclear where the speed-up comes from. The model size, computational cost, etc should be explained to support this figure.

### Questions
- As the improvement is marginal in Tables 1 and 2, 
    - I'd like to see whether PatchMixer is actually helpful for long-range prediction. Could authors show the errors at different prediction lengths and compare them with transformer-based and conv-based methods (similar to Table 2 and Figure 4)? 
    - Are all the methods in Table 1 comparable? How are the training setups? Are the number of parameters similar? How many runs did you do for these experiments? Are the results consistent with different runs? I would like to know whether this error gap is actually significant.

- The contributions of the paper are unclear. There are three points at the bottom of the Introduction but the experimental results do not support these arguments. For instance, could you explain why the PatchMixer layer is particularly helpful for long-term time series forecasting? Regarding efficiency compared to PatchTCT (Transformer-based), where does the speed-up come from? Does it have less computational cost but a similar model size compared to PatchTCT, or is it highly parallelizable? I assume both models have great parallelization capabilities. I try to understand where the efficiency comes from. There are lack of information to verify the contributions. Could you explain these in detail?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a new CNN-based model (Patchmixer) for LTSF (Long-Term Time Series Forecasting). PatchMixer divides the time series into patches and then captures potential periodic patterns within the patches using depthwise convolutions. Besides, it captures the feature correlation between patches using pointwise convolutions. The authors conducted experiments on several datasets, and the results show that PatchMixer achieves good prediction performance while being more efficient.

### Strengths
1. The paper is well written and easy to understand.

2. The proposed model, PatchMixer, performs well in both prediction accuracy and efficiency.

### Weaknesses
1. The novelty of work is limited, and its contribution to the field of time series forecasting is incremental. The idea of channel independence and separately modeling inter-patches and intra-patches correlations have already been proposed in PatchTST [1]. In my view, PatchMixer simply replaces self-attention with convolutions. The essence of dual forecasting heads is skip connection, which has also been seen in previous works about time series forecasting such as TiDE [2].

2. The improvement in prediction accuracy is negligible. From the results in Table 1, it can be seen that PatchMixer has very little or no improvement compared to PatchTST on datasets other than ETTh1 and ETTh2. In the ablation experiments in Table 2, the performance of Standard Convolution, Separable Convolution, and Attention Mechanism are comparable, which does not prove the superiority of Separable Convolution. The reported gains on ETTh1 and ETTh2 are not substantial enough to justify the architectural complexity, especially given that the performance on other datasets is not improved.

3. The paper mentions two types of patch representation from PatchTST and TimesNet [3] respectively, but the experiments do not compare these two. This lack of comparison leaves a gap in understanding the impact of different patch representations on the proposed model's performance. It is unclear whether the chosen patch representation is optimal or if other options could yield better results.

4. The overall content of the paper is not substantial and there are some redundant paragraphs. For example, in the Method section, there are many introductions to Patch Representation and Embedding, but these parts can even be described in just a single paragraph. The excessive detail in these sections does not add significant value and makes the paper feel unnecessarily lengthy.

### Questions
1. Are the slight performance improvements in PatchMixer solely due to the use of dual forecasting heads and MSE+MAE loss, rather than the architecture? Because other models in Table 1 can also be equipped with dual forecasting heads and MSE+MAE loss. 

2. Typo. The second paragraph in Pointwise Convolution section, "The above equations 8 demonstrate the process ..." should be "The above equations 10 demonstrate the process ..."

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
