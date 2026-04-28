# PATHS: Parameter-wise Adaptive Two-Stage Training Harnessing Scene Transition Mask Adapters for Video Retrieval

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 3, 8

## Abstract
Image-text pre-trained model, e.g., CLIP, has gained significant traction even in the field of video-text learning. Recent approaches extended CLIP to video tasks, and have achieved unprecedented performances in the foundational study of video understanding: text-video retrieval. However, unlike conventional transfer learning within the same domain, transfer learning across different modalities from images to videos often requires fine-tuning the whole pre-trained weights rather than keeping them frozen. This may result in overfitting and distorting the pre-trained weights, leading to a degradation in performance. To address this challenge, we introduce a learning strategy, termed Parameter-wise Adaptive Two-stage training Harnessing Scene transition mask adapter (PATHS). Our two-stage learning process alleviates the deviations of the pre-trained weights. A novel method of finding the optimal weights is used in the first stage, which efficiently narrows down to strong candidates by only monitoring the fluctuations of parameters. Once the parameters are fixed to optimal values, the second stage is dedicated to acquiring knowledge of scenes with an adapter module. PATHS can be applied to any existing models in a plug-and-play manner, and always achieves performance improvements from the base models. We report state-of-the-art performances across key text-video benchmark datasets, including MSRVTT and LSMDC. Our code is available at https://anonymous.4open.science/r/PATHS_.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work tackles the problem of text-to-video retrieval and mainly focuses on the methods based on the pretrained CLIP. To mitigate the overfitting onto a target video dataset, this work proposes a two-stage training method where the first stage optimizes the image-to-video weight transfer, and the second stage introduces an adaptor to further improve the video understanding. The proposed method PATHS is a plug-and-play module and can be added to other existing methods such as CLIP4Clip, X-CLIP, DiCoSA. When tested on MSVD, LSMDC and MSRVTT retrieval benchmarks, PATHS improves over different baseline methods.

### Strengths
* The proposed PATHS method is a plug-and-play model that can be added to other existing methods and consistently improves the retrieval performances.
* The code is available which helps the reproducibility of the method.

### Weaknesses
 * As the method requires more frequent evaluation than the standard per-epoch evaluation, the method still introduces computation overhead and leave the frequency as a hyperparameter which will potentially vary for different datasets.
* The contribution of the STMA adaptor seems marginal. For example in Table 1, the gain from STMA is only 0.2 point. Furthermore, the reported R@1 gain is not consistent across different metrics, with R@5, R@10 and MeanR showing signs of overfitting, which suggests that the STMA module may not be robust.
* In the ablation section, all BP, SP, USP methods exhibit very similar results. It is hard to tell if one quantifying strategy is better than others, raising a question whether the quantifying strategy is a main component of the proposed method. The lack of clear distinction between these methods undermines the claim that monitoring parameter rank fluctuations is a key factor in performance improvement. It is also unclear how these methods are implemented and what are the differences among them.
* Typo "raking" --> "ranking" in section 5.4

### Questions
* While the proposed method focuses on the retrieval task, would PATHS method also applicable to other video-text tasks such as video captioning or video QA?
* Please see the weaknesses section for other questions.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tries to address the weight corruption problem arising when extending pre-trained CLIP weights to tasks in the video domain.

It proposes a new learning strategy named "Parameter-wise Adaptive Two-stage training Harnessing Scene transition mask adapter" (PATHS), which involves a two-phase learning process. The first phase focuses on determining the optimal weights by monitoring parameter fluctuations, while the second phase concentrates on understanding scenes using an adapter module. 

The paper demonstrates the effectiveness of their approach by achieving leading performances on major text-video benchmark datasets such as MSRVTT and LSMDC.

### Strengths
1. The proposed method does not require frequent evaluations at every N step, which is distinct from recent approaches that incur extra computational overhead.
2. PATHS can be applied to strong baselines in a plug-and-play manner and has shown consistent performance improvements.

### Weaknesses
1. The elaboration in Section 4.2 on the proposed **Co-Attention** module in STMA is not clear enough. The sentence '*the co-attention layer takes different queries, keys, and values to enable the learning and updating of two pieces of information regarding each other*' is confusing. What are the settings of QKV in your Co-Attention? Considering this module is part of the core designs, more formulation or illustration is needed for better understanding. Specifically, it's unclear how the queries, keys, and values are derived from the input scenes A and B, and how this mechanism facilitates the updating of scene representations. A more detailed explanation, potentially with a mathematical formulation, would greatly enhance the clarity of this section.
2. If the **Alignment Attention** in Figure 4 is the so-called *'attention layer' utilized to identify the crucial parts of the video*, the authors should clarify its module name in the paper. Is **Alignment Attention** in STMA a vanilla attention module? How does the attention layer *identify the most crucial part of the video throughout the entire video and each scene*? More explanation and evidence are needed to support this. It's not clear how the concatenation of the original video and the updated scenes is processed by the attention layer, and what specific mechanisms allow it to focus on the most informative segments. A more detailed description of the attention mechanism and its inputs is needed.
3. According to the paper, the authors set the hyperparameter $K$ as 5. How do the authors choose this value? More ablation studies on $K$ should be conducted. The paper lacks a clear justification for this specific value, and it's unclear how sensitive the results are to changes in $K$. A more thorough exploration of the impact of this hyperparameter on performance is necessary.
4. What if in some certain samples, there does not exist a scene transition or contains more than one transition? Can the proposed STMA be applied to all possible conditions? The paper does not address the potential limitations of the proposed method when dealing with videos that lack clear scene transitions or contain multiple transitions. It's unclear how the model would adapt to these scenarios and whether it would still be able to effectively learn scene representations.

### Questions
Please see the Weaknesses mentioned above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the author proposes a two-stage training method (PATHS) to improve the results of video-retrieval tasks. In the first stage, it selects 5 candidates according to the parameter ranking. And the results of these candidates are better than those epoch candidates. In the second stage, it uses the previous best checkpoint for initialization and adds an adapter for further fine-tuning. Further experiments demonstrate its effectiveness.

### Strengths
The motivation is clear and the method is simple to reproduce.

### Weaknesses
- The paper is not well organized. 
  - The PRELIMINARIES section seems to be redundant, and the `3.1` and `3.1.1` seem to stage for a single section (subsection). 
  - Some details are not clear. For example, how does the ranking work? How does a two-stage scheme w/o STMA work (no adapter and freeze the backbone)? How to split scenes in STMA?
- The method seems to be tricky, which overfits a specific test set.
- The Figures 2 and 3 are in low resolution and hard to read.

### Questions
- In Page 5, `Main Idea` part, `In accordance with Figure 1, we denote end of each epoch with dotted line` should be `Figure 2`.
- In Page 5, `Motivation` part, `When the model starts to diverge after passing the optimum point, the model parameter values exhibit strong fluctuations. This often involves rearranging parameters in terms of importance (or the value of parameters)`, how can the author get the conclusion?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper propose a 2 stage method “PATHS” to address the main weakness of the current text-to-video retrieval CLIP-based models, i.e., overfitting. The proposed method includes 2 stages: 1) select best params by monitoring the fluctuations of params, which is much cheaper than e.g. per 50 step eval; 2) train an adapter module STMA with CLIP params frozen.

The proposed method is generic enough to be applicable to any existing CLIP-based models. The result achieves SOTA in the common text-to-video retrieval tasks: LSMDC and MSRVTT.

### Strengths
The method is relatively simple and the result is strong with several SOTA.

The experiments are extensive with many baselines; STMA is applied to a wide range of models to show its effectiveness.

The paper is well written and very readable.

The code is open-sourced.

### Weaknesses
5.4 ablates the param selection strategies, which is great; also it shows stage-1’s importance in Tab 4. However, it’s still unclear what the performance would be like if we apply stage-2 ONLY to the common param selection strategies (i.e. skip stage-1). This might make it clearer how important stage 1 and 2 is respectively?



### Questions
Appendix seems not uploaded?

IIUC, the red curve of Fig 3 is comparable with the green curve of Fig 2 (both are X-CLIP eval), but it seems there’s some difference (e.g. in the end of epoch 5)? If my understanding is correct, maybe it would be clearer if we plot the green curve of Fig 2 in Fig 3 as well?

In 4.1 “Two-stage Process”: in the 2nd stage, if params are frozen, why do we still need to “load these parameters back into the model at the end of each epoch to perform the pivoting”? And could you please explain a bit what “perform the pivoting” exactly means?

mild comments:
typo in 2.2: “adapters have been *unsed* for progressive learning…”

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
