# Revealing the Illusion of Joint Multimodal Understanding in VideoQA Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
While VideoQA Transformer models demonstrate competitive performance on standard benchmarks, the reasons behind their success are not fully understood. Do these models jointly capture and leverage the rich multimodal structures and dynamics from video and text? Or are they merely exploiting shortcuts to achieve high scores? Hence, we design $\textit{QUAG}$ (QUadrant AveraGe), a lightweight and non-parametric probe, to critically analyze multimodal representations. QUAG facilitates combined dataset-model study by systematic ablation of model's coupled multimodal understanding during inference. Surprisingly, it demonstrates that the models manage to maintain high performance even under multimodal impairment. We extend QUAG to design ''QUAG-attention'', a simplistic and less-expressive replacement of self-attention. We find that the models with QUAG-attention achieve similar performance with significantly less mulops without any finetuning. These findings indicate that the current VideoQA benchmarks and metrics do not penalize models that find shortcuts and discount joint multimodal understanding. Motivated by this, we propose the $\textit{CLAVI}$ (Counterfactual in LAnguage and VIdeo), a diagnostic dataset for coupled multimodal understanding in VideoQA. CLAVI consists of temporal questions and videos that are augmented to curate balanced counterfactuals in language and video domains. We evaluate models on CLAVI and find that all models achieve high performance on multimodal shortcut instances, but most of them have very poor performance on the counterfactual instances that necessitate joint multimodal understanding. Overall, with the multimodal representation analysis using QUAG and diagnostic analysis using CLAVI, we show that many VideoQA models are incapable of learning multimodal representations and that their success on standard datasets is an illusion of joint multimodal understanding.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper investigates the true impact of modalities, i.e., visual and text, on Transformer-based multimodal models for video question answer (VideoQA) tasks. The authors aim to show that many fusion models based on multiple modalities are faced with being suboptimal and the performance improvement in these models may not truly rely on the multimodal representations contrary to what they claimed. For assessing the model reliance for multimodal learning, the authors introduce a simple Quadrant Average (QUAG) operator, and a new dataset called CLAVI that is gathered as a subset of the Charades Dataset. Moreover, they emphasize the importance of new accuracy-related metrics they introduced for assessing joint multimodal learning. In the experimental evaluation, some existing models are assessed via QUAG in available benchmark datasets and additional experiments are conducted on CLAVI with baseline models.

### Strengths
-The paper introduces an averaging-based simple technique to assess the impact of uni-modal, cross-modal representation in multimodal learning. 

-They mention the importance dataset for VideoQA and introduce a new data collection. The question types in the introduced subsets are interesting.

### Weaknesses
-The QUAG is mainly not novel as it is already computed in self-attention based fusion transformers. It is simply the averaging over submatrices and here is simply used to investigate the impact of uni/cross modality. Similar techniques, such as averaging, are already used to visualize the multimodal representations upon training. I think the technique is not novel in this aspect. The authors do not sufficiently distinguish their method from existing techniques that average attention weights for visualization or pruning, failing to demonstrate a clear novelty in their approach. Specifically, the row-wise averaging of sub-matrices across all heads and layers, while claimed as a key contribution, is not fundamentally different from existing methods that perform similar operations for different purposes, such as feature importance analysis or token reduction. The paper needs to better articulate the specific differences and advantages of their averaging technique compared to these existing methods. 

-The fusion transformers can be designed in various ways. This study focuses on self-attention based fusion blocks, but cross-attention can be another direction. Particularly, the motivation of authors in selecting self-attention based fusion transformers is not clear and should be supported. The paper does not adequately justify why self-attention is the primary focus, especially considering that cross-attention is a common and effective method for multimodal fusion. The authors should provide a more detailed explanation of why self-attention is more suitable for their analysis or at least acknowledge the limitations of focusing solely on self-attention and discuss how their findings might generalize to other fusion architectures. Furthermore, the analysis should consider the specific properties of self-attention that make it amenable to the proposed QUAG method, and how these properties might differ in cross-attention mechanisms.

-I think some claims such as "FrozenBiLM consistently does not rely much on the video modality" are not justified well. Many observations may still related to dataset bias rather than the model bias. Therefore, datasets should be investigated for VideoQA task. As gathering data collections hard, reporting on various datasets is a feasible way as the SOTA research conducted. The claim that FrozenBiLM does not rely on the video modality is not sufficiently supported by the experiments. The authors should provide more evidence to differentiate between model bias and dataset bias. Simply observing low reliance on video modality does not necessarily imply model bias; it could be that the dataset itself contains spurious correlations that allow the model to perform well without fully utilizing the video input. The authors should conduct additional experiments on diverse datasets to validate their claims and rule out dataset-specific biases. The analysis should also include a discussion of the limitations of their current experimental setup and how it might affect their conclusions.

-The authors gather a new dataset collection as a subset of Charades. The questions on ordering are interesting. However, they create new video samples by simply changing the order of video segments. This looks confusing as the temporal ordering of frames and transition from one activity to another is important (boundary cue). If we think simply that each frame is represented as a token, the ordering of these frames during transition is also important to answer complex questions. I think the dataset design is not so strong in this aspect. The method of creating new video samples by simply changing the order of video segments is problematic. This approach ignores the temporal dependencies and boundary cues that are crucial for understanding video content. The authors should acknowledge that this method creates artificial discontinuities and may not accurately reflect real-world video scenarios. The dataset design should be re-evaluated to ensure that the temporal relationships between video segments are preserved, and the questions should be designed to assess the model's ability to understand these relationships.

### Questions
-Regarding indices used for QUAG operator on page 3: k looks like iterating over j indices (as j is in {q1 .. q2}) but the final output R(Z,W) is shown with ij indices. Can you check the correctness? Moreover, the s_ii is in {TT,TV,VT,VV} but in the above equation, it is used in a range [s_1 ... s_m]. Are the TT, TV etc. explained?

-The averaging is used to fuse token representations. However, there are other ways that can be easily integrated into transformers, such as CLS tokens. Do the authors investigate the usage of CLS for the same purpose?

-What is the targeted training setting in this paper for all models? For instance, the frozenBiLM reports results for fine-tuned, few-shot, and zero-shot cases.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors are motivated by the question of whether the good performance of VideoQA models is from the models themselves or whether the benchmarks are not thorough enough to measure the performance. To answer the question, the authors have proposed QUAG and QUAG-attention. Moreover, they curated a CLAVI dataset with temporal counterfactuals to measure the consistency in the VideoQA performances.

### Strengths
1. The authors have introduced interesting approaches to prove/diagnose VideoQA models. 

2. In addition, they clearly showed their experimental details.

### Weaknesses
1. QUAG and QUAG-attention have been evaluated on two models only. The authors have analyzed the performance drops in these two models on four different datasets. However, it is insufficient to conclude that Short-circuit and QUAG-attention are efficient by testing two models only. The analysis would be strengthened by including a wider range of models, particularly those with different architectures and pre-training strategies, to ensure the observed effects are not specific to the chosen models. Furthermore, the specific hyperparameters used for each model during the QUAG and QUAG-attention experiments should be detailed to ensure reproducibility and allow for a more thorough understanding of the results.

2. the authors use CLAVI to diagnose joint multimodal understanding. However, showing consistent performances on the dataset with *temporal counterfactuals* does not mean the model is free from shortcuts. The CLAVI dataset, while novel, might still be susceptible to other forms of biases not addressed by temporal counterfactuals. For instance, the questions themselves might contain biases that allow models to achieve high consistency without true joint multimodal understanding. A more thorough analysis of potential biases within the CLAVI dataset is needed, including an investigation of the linguistic properties of the questions and their relationship to the counterfactual videos.

3. The manuscript is a bit difficult to follow. The authors have to polish the paper. The presentation of the methodology and results could be improved with clearer explanations and more illustrative examples. The logical flow between sections could also be enhanced to make the paper more accessible to a broader audience. Specifically, the motivation behind the design choices of QUAG and QUAG-attention could be further elaborated.

4. An alternative approach to diagnosing models is to evaluate the generalization ability (e.g. zero-shot settings). How the proposed probes are effective compared to the evaluation? The authors should provide a more detailed comparison of their approach to existing methods for diagnosing model biases, particularly those that focus on generalization. This comparison should include a discussion of the strengths and weaknesses of each approach, and the specific scenarios in which each method is most effective. For example, how does QUAG handle biases that are not related to modality interaction, and how does it compare to methods that directly measure the model's reliance on spurious correlations?

5. Minor concerns: 
* page 2: Is the maximum input sequence lengths of the multimodal fusion module $l$?
* Citation formatting.

### Questions
1. What are the differences between `video-consistency` and `text-consistency`? Section 3.1 explains them as follows, but they look identical.
```
If the model predicts the answers for a given question correctly for both – the video and its counterfactual video, it is called video-consistent. Similarly, for a given video, if the model predicts the answers to the question and its counterfactual question correctly, it is called text-consistent.
```

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to even out the attention weights responsible for individual modalities or for modality mixing in the attention modules of a multimodal transformer model, as a way to probe which (combination of) modalities contribute to making predictions. The paper uses 2 video QA models (JustAsk, FrozenBiLM) and 4 datasets in the study (ActivityNetQA, MSRVTT-QA, NextQA, ATP-Hard). The authors then propose a new dataset (CLAVI) containing binary video QAs with good balance across positive and negative answers to better showcase the shortcuts used by existing multimodal models; they fine-tune and evaluate 4 videoQA models (JustAsk, FrozenBilm, Singularity-T, All-in-One+) on the proposed dataset and discuss their weaknesses.

### Strengths
A better understanding of how multimodal models operate is of critical importance for the community. The idea of short-circuiting modalities is interesting.
Proposing more challenging and balanced benchmarks is very valuable to guide research. 
The insight that multimodal models rely mostly on text to make predictions is valuable and shows that the video components of multimodal models need significant improvement.
The consistency metrics are a useful contribution.

### Weaknesses
A discussion about invasive vs non-invasing probing methods is needed. E.g. the authors should cite and discuss non-invasive analysis methods that rely on gradient backpropagation, e.g. MultiViz: Towards visualizing and understanding multimodal models, ICLR2023. I don’t know if our current understanding of deep models is good enough to perform invasive probing like the mechanism proposed here and draw strong conclusions from it. E.g. the authors replace all attention blocks in a model with the proposed modified blocks. But it is possible that not all blocks in the model behave in the same way, e.g. early-fusion vs late-fusion of modalities. Would it make sense to replace blocks progressively and see where the performance drops?

Some of the experiments are not very conclusive. E.g. in Table 1, the only clear result is that both models are significantly impaired in the video-only setting, but the short-circuiting results are not conclusive, especially for JustAsk where there is almost no difference across all SC setups. It is unclear if the short-circuiting is actually isolating the contribution of each modality or if it is simply disrupting the model's ability to process information effectively. The lack of a clear pattern in the short-circuiting results makes it difficult to draw strong conclusions about the models' reliance on specific modalities.

I have strong concerns about the proposed benchmark. Permuting segments in a video creates temporal discontinuities that can be exploited by the models in unexpected ways, especially when fine-tuning the models on the benchmark. Why is fine-tuning needed at all? Zero-shot evaluation would be better, especially for the purposes of diagnosing a model. The temporal discontinuities introduced by permuting video segments could introduce spurious correlations that the models might learn to exploit, rather than focusing on the actual multimodal understanding. This makes the benchmark less reliable for diagnosing the intended capabilities.

Page 8, the authors say “to account for class imbalances in the answers” – are the positive vs negative QAs not balanced in the dataset? It is unclear why the authors would need to account for class imbalance if the dataset is already balanced. This raises concerns about the actual distribution of positive and negative examples and whether the dataset is truly balanced as claimed.

Could there be ambiguities in the video-question pairs when the videos are altered? E.g. in the example shown with Fig 2, “holding on clothes” and “turning on a light”; when the altered video starts, the light is already on, so saying that the light was turned on at the beginning is not completely wrong. The altered videos could introduce ambiguities that make it difficult to assess the model's understanding of the temporal relationships between events. This could lead to incorrect conclusions about the model's capabilities.

Some questions might be ambiguous or not well defined, e.g. for the before-after negative control questions, the example in Table 2: since “washing mirror” never happens in the video, it could be ambiguous to ask about a before/after relation. The use of negative control questions that refer to non-existent events could introduce additional ambiguities and make it harder to interpret the results. The questions should be designed to be unambiguous and clearly defined.

Could the authors justify the choice of the models? JustAsk, FrozenBiLM have been outperformed by several newer models, so it is not clear if the analysis still holds. The selection of older models raises concerns about the generalizability of the findings to more recent state-of-the-art models. It is important to demonstrate that the analysis is relevant to current models and not just limited to older architectures.

The naming “counterfactual” for questions whose answer is negative can be misleading. E.g. in CLEVRER or Perception Test, “counterfactual” is used for questions that require imagining a different sequence of events from a given state of the environment, “what would happen if…” The use of the term 'counterfactual' is inconsistent with the established usage in the field, which could lead to confusion and misinterpretation of the results.

### Questions
See weaknesses above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a lightweight and non-parametric probe, to critically analyze multimodal representations. Then the paper proposed a diagnostic dataset for coupled multimodal understanding in VideoQA.

### Strengths
(1) The paper formulation is good and clear.

(2) The question that the paper tries to answer is meaningful.

### Weaknesses
(1) Did the authors conduct any ablation studies to isolate the influence stemming from the data itself rather than the methodology? For instance, exploring whether either video or text inherently poses greater learning challenges could provide valuable insights.

(2) Can these findings be extrapolated to other question-answer tasks, such as image-based question-answering?

### Questions
Please see the comments above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
