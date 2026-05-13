# From Link Prediction to Forecasting: Information Loss in Batch-based Temporal Graph Learning

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Dynamic link prediction is an important problem considered by many recent works proposing various approaches for learning temporal edge patterns.
  To assess their efficacy, models are evaluated on publicly available benchmark datasets involving continuous-time and discrete-time temporal graphs.
  However, as we show in this work, the suitability of common batch-oriented evaluation depends on the datasets' characteristics, which can cause two issues:
  First, for continuous-time temporal graphs, fixed-size batches create time windows with different durations, resulting in an inconsistent dynamic link prediction task.
  Second, for discrete-time temporal graphs, the sequence of batches can additionally introduce temporal dependencies that are not present in the data.
  In this work, we empirically show that this common evaluation approach leads to skewed model performance and hinders the fair comparison of methods.
  We mitigate this problem by reformulating dynamic link prediction as a \emph{link forecasting} task that better accounts for temporal information present in the data.
  We provide implementations of our new evaluation method for commonly used graph learning frameworks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper highlights an overlooked issue in the evaluation of dynamic link prediction task: fixed batch-size evaluation alters the task properties, as for continuous-time temporal graphs, leading to inconsistent duration evaluations across batches; for discrete-time temporal graphs, leading to possible data leakage due to additional introduced temporal dependencies

To explore this issue in depth, the paper first defines a quantitative metric, NMI, to measure information loss, and conducts extensive empirical analysis to demonstrate how fixed batch sizes distort the task setting. It then formulates a fairer setting, *link forecasting*, enabling consistent time durations for each evaluation batch. Finally, the authors reproduce experiments on existing methods within this reformulated task to reveal their true performance.

### Strengths
*S1* This paper addresses an important yet overlooked issue in temporal link prediction task, i.e., fixed batch size evaluation can distort the task itself by losing or introducing extra information.

*S2* The authors provide extensive data illustrations and quantitative results to facilitate understanding, demonstrating that each dataset has a distinct interaction distribution and how fixed batch-size evaluation can alter the task characteristics.

*S3* This paper formulates a new task setting, *link forecasting*, and offers implementation and reproduction of existing methods to provide valuable insights.

### Weaknesses
I appreciate the issue raised in this paper and the extensive empirical analysis that clarify the motivation behind the study. However, for the experiments on existing methods within the formulated link forecasting task, I think further discussion is required, e.g., **the reasons for performance changes across diverse settings can be addressed.**

The authors explain why memory-based methods tend to experience performance degradation on discrete-time graphs, which is appreciated. However, it would be beneficial to discuss why other methods might improve in this setting. Additionally, the performance trends for continuous-time graphs appear mixed, potentially due to specific dataset characteristics. I think a more in-depth discussion on these points would enhance the paper.

### Questions
Please refer to the "Weaknesses" section.

### Soundness
3

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
2

### Summary
In this paper, the authors considered the evaluation of dynamic link prediction on both discrete-time dynamic graphs (DTDGs) and continuous-time dynamic graphs (CTDGs). They first provided a series of empirical analysis results to demonstrate the limitations of existing batch-based evaluation strategies. A novel time-window-based approach was further proposed to address these limitations. The authors have also validated the effectiveness of the proposed evaluation approach on various public DTDGs and CTDGs datasets.

### Strengths
**S1**. The authors have conducted a great amount of experiments to illustrate the limitations of existing techniques as well as the effectiveness of the proposed method.

**S2**. The limitations of the evaluation of dynamic link prediction are significant but seldom considered and addressed in most existing studies.

### Weaknesses
 **W1**. Some statements regarding the research gaps of existing techniques and motivations of this paper are weak, unclear, or confusing.

  According to my understanding, this study focuses on the evaluation of dynamic link prediction. However, the title of this paper uses the terminology 'temporal graph learning', which may not be consistent with the major topic of this study. From my perspective, learning may also include the training procedure (e.g., training algorithms, training losses, etc.), addition to evaluation of the inference procedure.
  
The author claimed that 'within each batch, edges are typically treated as if they occurred simultaneously, thus discarding temporal information within a batch'. To some extent, I do not agree with this statement. According to my understanding, nodes or edges in most TGNNs are encoded as embeddings (i.e., low-dimensional vector representations), which usually involves the **temporal encodings**. In this sense, the temporal information has not been discarded. It is recommended to give some more toy examples about why and how is the temporal information discarded, especially for the case with temporal encodings.
  
  I also respectfully disagree with the definition of dynamic link prediction in Section 2, which was claimed to 'predict whether $(u, v) \in B_i^+$ or $B_i^-$ in terms of batches $B_i^+$ and $B_i^-$. According to my understanding, a dynamic link prediction model should be able to predict all the possible edges at a specific timestamp but not within a batch.
  
The authors claimed that existing techniques may hinder the fair comparison of methods. However, it is unclear for me how to define and measure the fairness of comparison. A formal definition regarding this point is also recommended.

  From my perspective, using 'temporal link prediction' and 'temporal link forecasting' as two terminologies with different definitions may not be a good presentation, which may result in potential ambiguity issues, since they are more likely to be synonyms in natural languages. It is recommended to use a clearer terminology to replace 'dynamic link forecasting' (e.g., batch-based and window-based evaluation) that can help better distinguish between 'temporal link prediction' and 'temporal link forecasting'.

***

**W2**. There seems to be some flaws for the proposed evaluation approach.

  In Section 3.2, the authors discussed one possible limitation that the proposed approach 'cannot preclude memory overflows entirely'. A possible solution was then discussed, which 'splits large time windows into smaller batches for GPU-based gradient computation'. In this sense, the proposed method still used the old bath-based technique, which may still 'ignore the temporal information within each batch', as claimed at the very beginning of this paper.
  
  According to my understanding, the proposed method may also suffer from the empty window issue, where there are no edges in a 'pre-defined' window, due to the heterogeneous distribution of temporal edges. However, there are no discussions regarding this limitation and possible solutions.

***

**W3**. Some details of experiments need further clarification. Some additional experiments are also recommended.

  In the empirical analysis of this paper, NMI is a significant metric to 'measure the temporal information that is retained after dividing edges into batches'. However, the formal definition regarding how to compute such a measurement is not given. As a result, it is still hard for me to understand the physical meaning of NMI using in the empirical analysis.
  
  According to my understanding, the proposed time-window-based approach introduces another hyper-parameter $h$. However, there seems no parameter analysis regarding different settings of $h$ (like the empirical analysis shown in Fig. 3).


***

**W4**. Although the authors have provided a great amount of empirical results to demonstrate the limitations of existing techniques and validate the effectiveness of the proposed approach, it is better to provide some theoretical guarantees w.r.t. the evaluation of dynamic link prediction.

### Questions
See **W1**-**W4**.

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
4

### Summary
This work introduces a reformulation of the dynamic link prediction (DLP) task as link forecasting (LF). LF differs from DLP in that LF ensures that each batch corresponds to a fixed time resolution. This small change to the problem statement yields relatively significant changes to the observed accuracies of these models on benchmark datasets.

### Strengths
1. The problem with variable-time batch construction for DLP is made quite clear in section 3. The examples are easy to understand
2. The experiments in section 4 are nearly exhaustive. The models cover the big TGNNs out there, and the datasets cover many of the major datasets out there.
3. The problem statement is clearly articulated and easy to understand. I had no problem implementing the discrete time version of the data loader in an afternoon of work. This clarity is commendable.

### Weaknesses
1. While the problem with DLP seems clear, it is hard for me to see why this requires the definition of a new task given that it's a straightforward modification of an existing one. I would recommend that the authors expand on this in the work to further draw the distinction, _or_ to assert that this is the way that DLP should be done in the future.
3. It appears that the models were not hyperparameter tuned for this new task. It stands to reason that because the new involves training on potentially quite different batch structures than the batches those hyperparameters were tuned for, that the reported model performance might be an underestimate. I would suggest that the authors investigate the hyperparameter sensitivity of the models training using LF.
4. The experimental details are a bit hard to follow in section 4. It appears that what was done is the authors trained a model using the horizon-based strategy, and then used this model to evaluate on both the horizon and batch based evaluation strategies. They then reported the performance differences. I would ask that the authors clarify these experimental details.

### Questions
1. It's unclear to me what the authors mean when they assert that DLP yields different amounts of information loss for different models. It seems to me that, if the batch size is fixed across all models, then it seems to me that the information loss (or really, the inter-batch leakage) will be equivalent. In what ways are they not? Or is the assertion that because batch size is often treated as a (often implicit) hyperparameter, so model comparisons can be implicitly unfair?
2. Does LF suffer from the same temporal training-leakage that DLP does when h is larger than infinitesimal?
3. Which is more significant? Batches containing variable time gaps, or the identified temporal leakage?
4. The primary motivation to use larger batch sizes is the reduction of wallclock time during training. How does the training time for LF scale as a function of h?
5. How do the results reported in table 2/3 change if the model was trained using a DLP pipeline and then evaluated on both DLP/LF?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work tackles the issue of information loss and leakage in the batch-oriented evaluation protocol for temporal graph learning. It first validates the existence of such loss and leakage through experiments that compute the NMI between batches and timestamps. To address this, the authors propose a new evaluation protocol for link forecasting and re-evaluate numerous existing methods within this framework. The provided code in the supplementary material appears comprehensive and sufficient.

### Strengths
The paper presents a study that provides a novel perspective on the internal issues with the batch-oriented evaluation protocol. The overall presentation is clear, and it includes adequate background information. The experiments related to the new evaluation protocol are relatively comprehensive, with re-evaluation of numerous existing methods. However, there are some missing aspects (as noted in the identified weaknesses) that should be addressed.

### Weaknesses
W1. Figure 2 and Figure 3 offer trivial or intuitive results, which seem to be redundant in the main text. I would suggest to just put part of them in the main text and the remaining in the appendix. Otherwise, these two figures would attract too much attention from the readers and make them lost before reading your point (Figure 4).

W2. The NMI may not be a trivial concept for common readers, therefore it would be helpful to include some technical details of it in the appendix and link to it at line 263. The current presentation of this paragraph is quite confusing as I cannot understand what lines 266-268 mean (how the NMI was computed). Maybe some formulation would help improve the clarification here.

W3. While the issue with the batch-oriented evaluation protocol is effectively identified using NMI, the paper does not adequately explain how this impacts previous evaluations and benchmarks that use this protocol. For instance, could you provide experimental validation to demonstrate the biases or flaws in past evaluations? The experiments in the current manuscript are associated with the new link forecasting protocol. Still, I am confused about how to experimentally validate that this protocol is better than the previous ones. 

W4. One advantage of the batch-oriented evaluation is the efficiency, but there seems to be no comparison or comment regarding the training/evaluation efficiency of the link forecasting protocol. I am aware of line 393, Computational cost, but I think such a not in-depth analysis is not enough. Some experimental results could be included.

W5. This is a relatively minor point, as is included in the limitation. For the frameworks that consider the temporal link prediction problem as a ranking task, is it possible to have more discussions about the pros/cons of time-window-based approaches and ranking approaches?

Minor: 
1. line 143, should be {$t_{b\cdot i}\, ..., t_{b\cdot (i+1)-1}$}? Also, line 244 seems to have the same mistake.
2. line 146, 147. if there is no constraint on (u,v), then it's possible that (u,v) is not in the B+ or B- batch. Is something like $(u, v) \in B^+ \cup B^-$ missing? I think similar issue exists for you link forecasting definition, line 379.
3. line 346. "negative edges that do not occur in time window [i · h,(i + 1) · h)". I feel it ambiguous. is those negative edges not in this time window, or in this time window but do not occur (interact)? Should be the latter?
4. Actually it could be an independent section for related work. I would recommend commenting on how existing TGNN benchmarks flow to validate that the widely-used batch-oriented training/evaluation does have issues that this work is trying to fix.
5. The code implementation largely builds upon an existing framework, DyGLib, and it would be helpful to include comments or documentation clarifying where the extensions and modifications occur at the code level (code snippets) in the appendix.

### Questions
I currently lean towards a rejection of the manuscript but am very open to further discussion and increasing the based on how well my concerns get addressed. I encourage the authors to refer to the identified weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
