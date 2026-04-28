# Divide-and-Conquer Time Series Forecasting with Auto-Frequency-Correlation via Cross-Channel Attention

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3, 5

## Abstract
To model various short-term temporal variations, we propose an effective design of Transformer-based, termed FreCoformer. FreCoformer is designed on top of the frequency domain and comprises three key designs: frequency patching operation and two independent observations of these patches. The patching process refines the frequency information, enhancing the locality. The subsequent observations extract the consistent representation within different channels by attention computation and summarize the relevant sub-frequencies to identify eventful frequency correlations for short-term variations. To improve the data fit for different time series scenarios, we propose a divide-and-conquer framework and introduce a simple linear projection-based module, incorporated into FreCoformer. These modules learn both long-term and short-term temporal variations of time series by observing their changes in the time and frequency domains. Extensive experiments show the effectiveness of our proposal can outperform other baselines in different real-world time series datasets. We further introduce a lightweight variant of FreCoformer with attention matrix approximation, which achieves comparable performance but with much fewer parameters and computation costs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
**Summary:**

This paper introduces the FreCoformer, a novel Transformer-based model tailored for capturing short-term temporal variations in time series data. The model is distinguished by its frequency patching operation, attention mechanisms for extracting consistent representations across different channels, and a divide-and-conquer framework for learning both long-term and short-term temporal variations. The paper also proposes a lightweight variant of the FreCoformer, employing the Nystrom method to reduce parameters and computational costs.

**Strengths:**

1. Innovative Approach: The application of patching in the Fourier domain combined with the use of Nystromformer is a novel contribution to the forecasting domain.

2. Empirical Performance: The proposed model outperforms PatchTST in most experimental settings, indicating its effectiveness.

**Weaknesses:**

1. From my perspective, the term *divided-and-conquer* is a little bit over claim. I would expect the divided and conquer type model to have a tree structure or multi-scale design. The authors couple an attention block within the Fourier domain and an MLP-type block for the first-order difference sequence, which, in my mind, is just kind of a dual structure. If the authors think divided-and-conquer term indeed reflects the spirit of the proposed model, it would be better to add more discussions on it.

2. The test data loader in the provided sample codes sets `drop_last = True`, leading to the exclusion of several test samples. Correcting this and rerunning the experiments would enhance the validity of the results.

3. The random control experiments seem not included. The model variance and hyperparameter-sensitive analysis may help to further highlight the efficiency of the proposed model.

**Questions:**

1.  The paper describes using Attention in the Fourier domain and MLP in the time domain. Could the authors provide more insight into this specific design choice? Why not use Attention layers or MLPs in both domains?

2. In the code, the time domain considers both trend differences and local differences. However, in section 3.2 of the main paper, only the first-order differences are mentioned. Does it only correspond to the local differences or both trend/local differences? 

At the current stage, I tend to recommend accepting this paper if the numerical experiment results are updated. However, my final decision is open to change pending the authors' rebuttal and further discussions with other reviewers and the Area Chair.

### Strengths
Please see the Strengths section in Summary.

### Weaknesses
1. From my perspective, the term *divided-and-conquer* is a little bit over claim. I would expect the divided and conquer type model to have a tree structure or multi-scale design. The authors couple an attention block within the Fourier domain and an MLP-type block for the first-order difference sequence, which, in my mind, is just kind of a dual structure. If the authors think divided-and-conquer term indeed reflects the spirit of the proposed model, it would be better to add more discussions on it.

2. The test data loader in the provided sample codes sets `drop_last = True`, leading to the exclusion of several test samples. Correcting this and rerunning the experiments would enhance the validity of the results.

3. The random control experiments seem not included. The model variance and hyperparameter-sensitive analysis may help to further highlight the efficiency of the proposed model.

### Questions
Please see the Questions section in Summary.

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
This work proposes a transformer-based architecture called FreCoformer for timeseries forecasting. FreCoformer is designed with patching operation in the frequency space, which gives good locality through maintaining local frequency information. The authors also propose a two-stage linear projection to incorporate time information into the network. To reduce the computation cost of the framework, the authors further used the matrix approximation in NystromFormer in the proposed network. The authors performed extensive experiments to demonstrate the effectiveness of the proposed architecture.

### Strengths
- This is solid work validating that frequency-space operations can be used to achieve good performance in the timeseries forecasting task.
- The authors make a lot of attempts to improve the performance of the proposed architecture while reducing the computation costs.
- Extensive experimental results with solid baselines and fair comparison.

### Weaknesses
 - Why the “divide and conquer” framework is named “divide and conquer”? Does it have any correlation with the “divide and conquer” algorithm? Isn’t it just a two-layer linear operation? How similar it is to the linear aggregation operation as proposed in [1]? 
- Since the frequency-domain signal essentially is a one-to-one projection of the time-domain signal, how much does the proposed network differ from PatchTST (theoretically)? Specifically, do the two architectures share the same, or a subset of solution space? The performance gain over PatchTST seems very marginal in Table 3.

A lot of typos, e.g. Attentione

### Questions
NA

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new model, FreCoformer, for time series forecasting which operates on frequency and time domains. In detail, FreCoformer incorporates modules computing frequency and inter-feature correlation with patchifying frequencies. Furthermore, the divided-and-conquer method is introduced to tackle varying data scenarios. Finally, with Nystrom approximations, it achieves efficient linear complexity when considering inter-feature dependencies. As a result, FreCoformer achieves 41 top-1 and 21 top-2 cases out of 64 in total experimental settings for time series forecasting, showing the most efficient cost.

### Strengths
**Good inspiration about high-frequencies parts**
This paper gives visualization results that show that existing models operating on the time domain don't capture high-frequency dynamics. In contrast, models on the frequency domain, such as FEDformer and FreCoformer, are good at catching short-term variations. This gives new research direction to time series forecasting tasks.

### Weaknesses
 **Insufficient novelty and contributions**
1. I think there are the following contributions in this paper: patching frequencies and cross-feature and cross-frequency self-attention in  Transformers operating on frequency domains, Divide-and-Conquer method, and Nyström-FreCoformer. However, cross-feature and cross-frequency self-attention are almost similar to [1], [2], and [3]. Also, the Divide-and-Conquer method is quite similar to a variant of PatchTST [4] where a transformer part for temporal connections is changed into a linear one. Also, Nyström-FreCoformer is almost the same as Nyströmformer [5]. As for the patching method on frequency domains, just domain is different from that of [4]. Therefore, I think that this paper just combines existing methods, and something new is not introduced. Therefore, to make more contributions, the authors have to propose stronger reasons why they combine such modules, or different parts from [1-5].

**Insufficient explanation or experimental results for argument**
1. According to 'Abstract', FreCoformer is designed for short-term variation while the divide-and-conquer framework is for long-term and short-term temporal variations. Can you give intuitive empirical evidence for this argument?

2. In channel-wise attention, you design self-attention differently from the original one [6]. Why do you select your own design? Can you give some reason for this selection?

3. In Section 3.3, the authors say that "To compute the attention matrix A, we first select m landmark columns from the input Qn and Kn matrices in each channel.". Can you give the detailed procedure to select $m$ landmark columns from entire ones?

4. In Figure 3 (a), the authors say that "Compared to the best-performing PatchTST, our model exhibits an advantage in identifying short-term variations, resulting in detailed fluctuations in periodicity variation." However, I don't know what parts show these results. Can you mark what parts provide this information?

5. Additionally, there are some confusing parts. Refer to Question Section.

### Questions
1. In 'Abstract', the authors argue that "The patching process refines the frequency information, enhancing the locality.". What kind of locality is enhanced by the patching process? Locality on the time domain is quite intuitive but one on the frequency domain is not. I think that you have to elaborate on locality on the frequency domain and why we have to utilize the frequency locality.

2. In 'Abstract', there is a sentence saying "The subsequent observations extract the consistent representation within different channels by attention computation and summarize the relevant sub-frequencies to identify eventful frequency correlations for short-term variations.". What does 'Consistent representation within different channels' mean? I think that attention is capable of discovering relationships between different channels, not consistent representations within them. 

3. In 'Introduction', there is a sentence saying "This approach relies on heuristic and empirical strategies, i.e., random or top-K
frequency selection, often capturing spurious correlations for forecasting (seen in Figure 1(c)).". I think this is a too strong argument because Figure 1 doesn't directly provide evidence for spurious correlations.

4. "These independent attentions share model parameters across all sub-frequency learning, preventing winner-take-all of redundancy low-frequency components.": About this sentence, Can you explain further? By just sharing the same Transformer's parameters across all sub-frequency learning, why is the phenomenon prevented that low-frequency components dominate against high-frequency ones?

5. "To demonstrate the efficacy of the core design—channel-wise attention in FreCoformer, we visualized the heatmaps of the input and output DFT matrices of the Transformer encoder in FreCoformer in Figure 3(b)." in Section 4.2.2: As far as I know [1], the DFT matrix is like a weight matrix to transform time domain into frequency domain. If the input length $N$ is the same, the DFT matrix always has the same value. What does 'DFT matrices' in the above sentence mean?

6. "This balance likely enables our method to efficiently extract pivotal frequency features across the entire frequency spectrum and various temporal variations, enhancing prediction outcomes." in Section 4.2.2: Why is balanced energy across entire frequencies helpful for your method? Can you give me more direct evidence for this sentence?


[1] https://en.wikipedia.org/wiki/DFT_matrix

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a divide-and-conquer framework, FreCoformer, which is designed on top of the frequency domain for time series forecasting. Specifically, the framework comprises three key designs: frequency patching operation and two independent observations of these patches, and the authors further introduce a simple linear projection-based module to incorporate the information from the time domain. Extensive experiments show the effectiveness of the proposal method.

### Strengths
1. The evaluation is extensive. The authors validate the proposed method on multiple datasets and compare it with recent competing methods which prove the effectiveness of the proposed method. Moreover, the authors conduct adequate ablation to validate each design.
2. Results seem promising. The proposed method FreCoformer achieves strong performance over multiple datasets compared with existing works.
3. Writing is clear. Overall, the writing is clear and it is easy to understand each module presented by the authors.

### Weaknesses
1. Design of the framework. The divide-and-conquer framework seems to be a multiple path/view framework that has been extensively studied in the previous literature and it is not surprising that FreCoformer obtains competitive performance as it utilizes the information from both the time domain and frequency domain. Specifically, the core idea of processing time series data in both time and frequency domains is not novel. Many existing methods have explored similar dual-branch architectures, and the specific implementation of frequency patching and independent observations, while effective, lacks significant novelty. The framework's resemblance to existing dual-path models raises concerns about its originality and the incremental contribution it offers beyond established techniques.
2. Training/inference efficiency. The following question from point 1 is how is the training/inference efficiency of FreCoformer compared to other competing methods as it computes on different domains. The authors have only compared the GPU memory between FreCoformer and other methods, which is not the most important metric to evaluate the efficiency. For example, training time/number of parameters/FLOPs/GPU latency are commonly used metrics for efficiency evaluation. The lack of comprehensive efficiency analysis, particularly regarding training time and FLOPs, makes it difficult to assess the practical viability of the proposed method. The authors should provide a more thorough comparison of computational costs to justify the use of a dual-branch approach.
3. Core contribution. The authors have proposed lots of modules and designs in this work that may deviate from the core of 'divide-and-conquer'. For example, NYSTROM-FRECOFORMER just simply adopts the idea from NystromFormer and can hardly be claimed as the contribution of this paper. It is advised the authors rethink what in essence they are trying to present. The paper introduces several modules, such as the linear projection and Nystrom approximation, that are not directly related to the core 'divide-and-conquer' concept. The integration of these existing techniques dilutes the focus and makes it difficult to pinpoint the unique contribution of the proposed framework. The paper needs to clarify the core contribution and how each module contributes to this central idea.

### Questions
1. Different channels for different datasets. From Tab. 2, It can be noticed that the authors use different channels for different datasets and the reviewer wonders the reasons behind this. Is it caused by different data lengths?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
