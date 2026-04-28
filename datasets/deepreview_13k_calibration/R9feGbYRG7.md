# One Model to Train Them All: A Unified Diffusion Framework for Multi-Context Neural Population Forecasting

- Decision: Reject
- Avg Score: 4.60
- Scores: 3, 5, 3, 6, 6

## Abstract
Recent research has revealed shared neural patterns among animals performing similar tasks and within individual animals across different tasks. This has led to a growing interest in replacing single-session latent variable models with a unified model that allows us to align recordings across different animals, sessions, and tasks, despite the challenge of distinct neuron identities in each recording. 
In this work, we present a conditioned diffusion framework to model population dynamics of neural activity across multiple contexts. The quality of the learned dynamics is evaluated through the model's forecasting ability, which predicts multiple timesteps of both neural activity and behavior.
Additionally, we introduce a benchmark dataset spanning six electrophysiology datasets, seven tasks, 19 animals, and 261 sessions, providing a standardized framework for multi-task neural population models.
Our results demonstrate that the pretrained model can be efficiently adapted to novel, unseen sessions without requiring explicit neuron correspondence. This enables few-shot learning with minimal labeled data, as well as competitive performance in zero-shot learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces the idea of using causal diffusion modelling to jointly model neural and behavioral data across large number of ephys recordings. This approach is applied for two tasks---neural activity forcasting and behavior decoding. Additionally, the paper also collates a set of public datasets to form a large-dataset to be used as a benchmark for pretraining neural population decoding models.

### Strengths
- Use of diffusion as an SSL framework for pretraining of large neuroscience models is a novel idea.
- Collation of public ephys recording data to create a large scale benchmark is a good contribution to the field.

### Weaknesses
In its current state, this paper should be rejected because:
1. The paper fails to demonstrate the effectiveness of using diffusion as a pretraining strategy in comparison to other modern pretraining strategies such as NDT2 [1] and POYO [2]
2. The paper is unpolished and lacks many details important for replication of the presented method.

### Questions
**Arguments on experiments conducted and results:**
1. Since the majority of results in this work are on behavior decoding, I will assume that is an important metric that this paper uses to compare the presented method with baselines. Although it is positive to see that training on more data improves decoding performance, this positive effect of data scale for behavior decoding has been established by NDT2 and POYO. I believe, in current environment, it's important to see these performance numbers in relation to other modern large-scale training methods such as NDT2 and POYO. Without such comparisons, an important scientific remains unanswered----does diffusion have any benefits to offer over other large-scale pretraining techniques like supervised pretraining or mask-modelling for behavior decoding? If diffusion is not comparable or better in comparison, then the benefits of using it for the purpose of behavior decoding have not been demonstrated.
2. Even when considering neural forecasting as a task, the lack of results in relation to NDT2 is a major drawback. Since NDT2 is trained using a causal masked-modelling framework, it is also capable for performing forecasting. And hence, to make and argument for diffusion, a comparison to masked-modelling like NDT2 should also be presented.

**Additional comment on comparison to NDT2/POYO:**
I would understand if training NDT2 and/or POYO on your dataset might by prohibitive due to the scale and compute intensiveness of those methods. In this case, I would suggest performing the following analysis: Do multi-session training on all sessions except the ones included in the NLB Maze and NLB RTT benchmarks [3] (the sessions from these two benchmarks seem to already be part of the dataset considered in this paper). Then, do transfer on these two benchmarks to show your method compares to the baselines (I believe both NDT2 and POYO mention performance on these datasets).



**On missing details about method:**
1. How is a sample $x_i$ passed into the U-Net? Since the number of neurons change from one sample to another in the multi-session training situation, it is implied that the dimensionality of $x_i$ changes as well. It is not clear to me how a fixed-sized CNN is used to process all the samples simultaneously. 
2. Figure 1 shows multiple session-embedding tokens going in the Key/Value port of the cross-attention for _each_ sample. Since there are multiple tokens, how are they differentiated from one another? Do these tokens have any position embedding added? If so, of which kind?
3. It is unclear as to how the equation on line 265 is used to enable/disable session guidance. The symbol $s$ or the term "_guidance scale_" is not used anywhere else in the text. 
4. Since you forcast a 500ms window, how do you perform behavior decoding for 1s trials? (most datasets under consideration in here have trial-durations of ~1s)

As a general comment, I would encourage the authors to make the model's description in the paper as self-contained and complete as possible. Especially since it states the model as being a core contribution.

**Some smaller concerns/questions:**
1. Why not include full-finetuning as a transfer strategy, in addition to zero-shot and session-identification?
2. I regards to table 2, I am curious about your explanation as to why performing Session-ID does worse than zero-shot in the case of single-session training?
3. Figure 4C: What's the difference between "All Sessions" and "Full dataset"?
4. Figure 4D: both the red and blue curves look "too smooth" for being raw $R^2$ curves. I am curious if this is a result of performing some post-processing on the raw curves, such as applying smoothing? If so, I would suggest not doing much smoothing as there is value in being able to look at the raw behavior of accuracy changing over training steps.
5. Regarding figure 4C - this figure about data scaling, and hence the x-axis should be changed to number of recording-hours or another relevant data-scale metric and not model parameters.

[1] Neural Data Transformer 2: Multi-context Pretraining for Neural Spiking Activity. Joel Ye et. al. NeurIPS 2023

[2] A Unified, Scalable Framework for Neural Population Decoding. Mehdi Azabou et. al., NeurIPS 2023

[3] https://neurallatents.github.io/

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this work, the authors propose a diffusion framework to model population dynamics of neurons recorded from multiple brain areas, tasks, subjects, and sessions. Unlike previous work in this area, their approach can generalize to new data (either new sessions from the same subject, or a new subject entirely) without the need for explicit alignment between train and test data. To demonstrate their approach, the authors have also curated a large neural dataset that can serve as a benchmark for developing models of neural population dynamics. This is a timely contribution given the growing interest in developing foundation models for neuroscience.

### Strengths
- The approach accounts simultaneously for neural and behavioral data with a shared latent representation
- The framework is applied to a diverse set of recordings, spanning brain areas, sessions, individuals, and tasks
- The paper is properly motivated and it is clear what problem the authors are trying to address

### Weaknesses
 - While I can appreciate the performance improvement (as captured by the R-squared) over existing methods for modeling neural population dynamics, an analysis of what exactly the model is learning is noticeably absent. For example, the model uses a shared representation for both neural and behavioral variables; what is the relative importance of these two in forecasting neural activity? Can you perform an ablation study and compare performance with and without the behavioral data? Can you visualize the learned latent representations? Having this analysis would really improve the quality of the paper.

 - It seems that the datasets that constitute the benchmark utilize very structured tasks (there is a target onset, there is a go cue, etc). How well would this method work for less structured, more naturalistic tasks (e.g. freely moving animal)? Perhaps you already have data on this, if not, please feel free to speculate/discuss.

### Questions
- It seems that the datasets that constitute the benchmark utilize very structured tasks (there is a target onset, there is a go cue, etc). How well would this method work for less structured, more naturalistic tasks (e.g. freely moving animal)? Perhaps you already have data on this, if not, please feel free to speculate/discuss.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presented a conditional diffusion model that is trained on behavioral and neural activity. The presented method can be used to forecast neural activities across animals and sessions. The paper also introduced a new benchmark consists of multiple existing datasets of neural activities.

### Strengths
Combining datasets to build novel benchmarks for cross-animal and cross-session pre-training is an important topic for the computational neuroscience community.

### Weaknesses
1. The presented method lack insights.
- Why would the authors want to forecast neural activities? How long can one forecast neural activities accurately is quite of a neuroscience topic under debate. How do the authors make sure that the problem is not ill-defined (not just model overfitting from here and there) from the beginning? Specifically, what is the practical utility of forecasting neural activity beyond simply demonstrating a model's ability to fit training data? The paper does not adequately address the inherent challenges in forecasting chaotic neural systems, where small errors can compound over time, leading to inaccurate long-term predictions. The lack of discussion on the limitations of predictability in neural systems raises concerns about the validity and interpretability of the forecasting results.
- Why would you want to embed session information at all, at test time, how could one assume they will definitely have session information? Moreover, isn't that information leakage to the prediction? The use of session embeddings introduces a potential confound, as it assumes that session-specific information is always available during inference. This assumption is not always realistic, especially in scenarios where the model is applied to new, unseen sessions. Furthermore, the paper does not explore the impact of session embedding dimensionality on model performance, nor does it discuss the potential for these embeddings to overfit to specific session characteristics, thereby limiting generalization to new sessions.

2. The presented method is confusing and seems wrong given lousy mathematical notations.
- D= {xi}, please define I here. The notation D = {xi} is unclear without a proper definition of the index set 'I'. It is unclear whether 'i' refers to trials, time points, or some other indexing scheme. This lack of clarity makes it difficult to understand the structure of the data being used for training.
- Please write vectors and matrix in their corresponding math form, do not just use lowercase italicize unbold text for every notations. The inconsistent use of mathematical notation, specifically the use of lowercase italicized unbold text for vectors and matrices, makes it difficult to follow the mathematical derivations and understand the underlying operations. This lack of rigor in notation hinders the clarity and precision of the presented method.
- Is it a hard requirement in your framework that behavior covariates need to have a length of t? If so, clearly write this out and state it is your assumption. The paper does not explicitly state whether the behavioral covariates are required to have the same length 't' as the neural activity data. This ambiguity raises questions about the flexibility of the model and its applicability to datasets with varying lengths of behavioral data.
- Why x is suddenly bolded in line 202? Is this the same x as previously defined? Actually, if your x is the set of neural activity and behaviors of the i-th trial, how would you plug it inside equation 1? The sudden change in notation from 'x' to bold 'x' in line 202 is confusing and suggests a potential inconsistency in the definition of variables. If 'x' represents the combined neural activity and behavior of the i-th trial, it is unclear how this combined representation is incorporated into equation 1, which appears to operate on individual data points rather than trial-level data.
- Are the authors aware that diffusion is a way to train models, and a transformer is just a model architecture, and they are independent of each other? Why the authors start to introduce cross attention at line 224 without background information? What is the methodological novelty here? The paper lacks a clear explanation of how the diffusion process is integrated with the transformer architecture. The introduction of cross-attention at line 224 without sufficient background information makes it difficult to understand the specific role of cross-attention in the proposed model. The methodological novelty of this combination is not clearly articulated, leaving the reader questioning the significance of this design choice.

3. Experimental results are confusing
- Why the authors would like to introduce a new dataset for their model evaluation? How large is the new dataset comparing to existing benchmarks? What is the advantage or uniqueness of it, and can the authors prove the advantage using experimental results? If none of the above is considered, I highly suggest the authors to split this submission to papers, where one of them focuses on presenting the new benchmark, and the other one demonstrating the method. Combining both of them makes it hard to evaluate the presented approach. The introduction of a new dataset for model evaluation without a clear justification is problematic. The paper does not provide sufficient information about the size, characteristics, and advantages of the new dataset compared to existing benchmarks. The lack of a thorough comparison makes it difficult to assess the significance of the reported results. The authors should either provide a more detailed analysis of the new dataset or focus on using existing benchmarks for model evaluation.
- The authors somehow decide not to benchmark with many of the methods discussed in related works. For single session results, the authors should at least include NDT [1], or their later variants such as STNDT [2] or EIT [3], where the latter two can also be extended to be transferred to new sessions. The absence of comparisons with relevant state-of-the-art methods, such as NDT [1], STNDT [2], and EIT [3], in the single-session results is a significant oversight. These methods are directly relevant to the problem being addressed and should have been included in the benchmark to provide a more comprehensive evaluation of the proposed approach.
- To be honest, it does not seem the model actually performs well. Session IDs are actually harmful for performance in single session validations, and the improvements in multi-session validations are marginal (within standard deviations). The reported results do not demonstrate a clear advantage of the proposed method. The fact that session IDs are detrimental to performance in single-session validations raises concerns about the model's ability to generalize within a session. Moreover, the marginal improvements in multi-session validations, which fall within standard deviations, suggest that the model's performance is not significantly better than existing approaches.
- A common criticism in such “foundation models” on small datasets works, is that, if your single-session model is properly trained at all [4]. For example, have the authors fixed the number of training steps instead of epochs for fair evaluations? Have the authors introduced sufficient amount of augmentations? Have the authors considered using synthetic datasets for pre-training, or just initialize the model differently? The paper does not provide sufficient details about the training procedure, such as whether the number of training steps was fixed instead of epochs, the amount of data augmentation used, or whether synthetic data or alternative initialization strategies were considered. These details are crucial for ensuring a fair evaluation of the model and for addressing concerns about potential overfitting to the training data.

### Questions
NA

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposed a foundation model for solving adaptation in multi-animal, multi-session, multi-task for neural dynamics, including both dynamical forecasting and decoding tasks. It demonstrated its performance on six electrophysiology datasets from monkeys with recordings from different brain areas and different BCI tasks. It utilized a conditional diffusion models to perform unsupervised alignment to transfer unseen data aligned with original dataset, and also a session embedding to compensate for session variability. The model is trained with a causal forecasting tasks with self-supervised tasks. It learns a shared latent representation with both behavior and neural activity. It evaluated on both single-session and multi-sessions with a session identification approach or a zero-shot learning.

### Strengths
1. This paper is proposed to address a well motivated and important question in neural data analysis, and focus on achieving generalization across multi-animal, multi-session, multi-tasks for neural dynamics forecasting and behavior decoding.
2. This paper is evaluated on extensive experiments including 6 datasets, 19 monkeys with enhanced predictive performance compared with existing approaches. 
3. Extensive techniques such as conditional diffusion model, meta-learning, session-identification are exploited to address the problems.
4. The work is developed with great accessibility including introducing a benchmark dataset and APIs to benefit the broader community.

### Weaknesses
1. Existing works like NDT2 and POYO also focused on developing a unified framework (foundation model) for neuroscience. Although this work claims to integrate with additional forecasting capabilities, the core of this approach does not deviate a lot from those existing frameworks, for example, this work also utilized the session identification techniques proposed in POYO and demonstrate the effectiveness of this approach. 
2. More systematic investigation about the limitations about the forecasting capability is necessary, what is the maximal time length of effective forecasting, how much historical information is needed, how does the model perform to address the trial-to-trial variability?
3. This work integrate with both behavior data and neural data to learn a joint representation space, it would be helpful to perform an ablation study to explain how behavior information is useful or without behavior information, will this method still be effective for forecasting or behavior decoding?

### Questions
1. Any potential hypothesis or assumptions about why zero-shot learning outperforms session identification while session identification is better when more data is available?
2. Add more clarification for the notations in C.1 and C.2, are time steps $t$ in neural activities the same as the notation $t$ in diffusion processing?
3. Clarify the major contributions and novelty compared to existing NDT2 and POYO models.
4. Time complexity of the proposed approaches compared with existing baselines.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors present a joint neural spiking activity and behavior forecasting model based on diffusion mechanisms. They demonstrate that the novel architecture can jointly encode both neural activity and behavior, and that trainign can be done on multiple animals, tasks, and sessions. The authors also introduce a novel dataset which incorporates data from non-human primates from several labs, which is curated for easy model development. Finally, the authors show that their new model can easily forecast behavior, and neural activity, from new sessions with no fine tuning.

### Strengths
This paper is one of (if not the first) account of diffusion modelling for neural data and bahvioral forecasting. The development of this application for diffusion modelling is an important strenght, and a good contribution to the existing litterature. Furthernmore, the introduction of a novel format for datasets suited for general multi-session, multi-lab modelling is a great contribution. Finally, the results presented are encouraging.

### Weaknesses
As indicated above, I do believe the model and approach presented in this paper is an important contribution. However, I do think there are weaknesses with respect to the results presented, as well as clarity issues in the presentation along with some mismatch with the claims put forth. See more details in the specific questions below.

- No comparison of neural activity forecasting with other models:
While the authors clima throughout this paper the their model is a significant advance in joint forecasting of behavior and neural activity, as far as I can tell, only Fig.3C shows forecasting of neural activity, and it only compares prediction across two variants of the proposed model. While there is significant benchmarking of behavioral forecasting, can the authors explain why they report such minimal experiments on neural activity forecasting while putting the two forecasting modalities on equal footing in their claims? The absence of a thorough comparison to existing neural activity forecasting models undermines the claim of advancement in this area. It is unclear if the proposed model offers any improvement over existing methods for neural activity forecasting, or if its strength lies solely in the joint modeling aspect.

- No comparison to behavior decoding with other foundation models:
For example, the POYO model from Azabou et al., often cited in this manuscript, does behavior forecasting on 500ms windows (as in this paper) on similar cursor control tasks but achieves R^2 of around 0.95+. This is in contrast with the presented results which seem in the 0.6 range. I do not think the present model should be SOTA on forecasting to warrant publication, but it should acknowledge comparative performance of other models, and explain clearly the differences in the approaches that explains this difference. Can the authors explain these points? The lack of direct comparison to models like POYO, which achieve significantly higher performance on similar tasks, raises concerns about the practical utility of the proposed model. It is important to understand why the current model's performance is lower and what specific design choices contribute to this difference.

- Confounding source of forecastinginformation:
As noted above, most of the forecasting results focus on behavior (i.e. cursor velocity). However, cursor velocity is also present in the input data, and forecasting happens on joint cursor veloity and spiking activity representations. Have the authors tried forecasting behavior only from behavior, only from spiking activity? What is the effect of the regularization terms in the loss that weight both of these modalities? Often times, models present with multiple sources of data and that aim to forecast one of them can rely heavily on one source rather than the combined effect of two. It is important to understand the behavior of the model under multiple sources. The model's reliance on cursor velocity in the input data for behavior forecasting is a significant concern. It is crucial to understand the extent to which the model is truly learning from neural activity versus simply relying on the provided behavior data. The impact of the regularization terms on the model's reliance on each modality needs to be thoroughly investigated.

- Potential ablations:
I realize that getting ablation requests from reviewers is frustrating. However, this model relies on important prprocessing that includes spike train binning followed by Gaussian smoothing. Have the authors tries different binning and smoothing resolutions? Ho robust is the model for variation on these steps? The lack of ablation studies on the preprocessing steps, particularly binning and smoothing, is a notable weakness. The model's sensitivity to these parameters needs to be assessed to ensure its robustness and generalizability. Different binning and smoothing resolutions could significantly impact the model's performance, and this should be explored.

Minor:

- Captions often indicate R^2 forecasting error but it is not indicated what quantity is being forecasted. Is it cursor velocity (I believe this is it in most cases) or spiking activity? Captions should be precise on this front.

- Line 220: authors indicate "$\mathcal{D}$-dimensional [...]" but here D is a dataset. Not sure what is meant there or if this is a typo.

- Line 235: "[...} have been shown to be better for [...]" citation needed.

- In C4, the authors mention the presence of unconditional trials in training. It is not clear what this means in this context. More details about what trial information is removed, or uncondtiioned on, is needed.

- Related work, "Multi-session Training and Alignment". The authors review past work that aim to do transfer learning for multi-session inference. However they do not acknowledge that the other efforts they cite under the "Foundation models for neuroscience" section also achieve this. It is important to acknowledge that recent work does achieve borad generalization across sessions, animals, labs, etc. Even is the authors do acnkowldge these past results later on, they cast them as "specifically designed for decoding brain-machine interfaces" which is not accurate. If anything, these past works work on very simlar objectives and datasets as the current work.

I would be happy to revise my score if the authors provide adequate answers to these questions.

### Questions
- No comparison of neural activity forecasting with other models: 
While the authors clima throughout this paper the their model is a significant advance in joint forecasting of behavior and neural activity, as far as I can tell, only Fig.3C shows forecasting of neural activity, and it only compares prediction across two variants of the proposed model. While there is significant benchmarking of behavioral forecasting, can the authors explain why they report such minimal experiments on neural activity forecasting while putting the two forecasting modalities on equal footing in their claims?

- No comparison to behavior decoding with other foundation models: 
For example, the POYO model from Azabou et al., often cited in this manuscript, does behavior forecasting on 500ms windows (as in this paper) on similar cursor control tasks but achieves R^2 of around 0.95+. This is in contrast with the presented results which seem in the 0.6 range. I do not think the present model should be SOTA on forecasting to warrant publication, but it should acknowledge comparative performance of other models, and explain clearly the differences in the approaches that explains this difference. Can the authors explain these points?

- Confounding source of forecastinginformation:
As noted above, most of the forecasting results focus on behavior (i.e. cursor velocity). However, cursor velocity is also present in the input data, and forecasting happens on joint cursor veloity and spiking activity representations. Have the authors tried forecasting behavior only from behavior, only from spiking activity? What is the effect of the regularization terms in the loss that weight both of these modalities? Often times, models present with multiple sources of data and that aim to forecast one of them can rely heavily on one source rather than the combined effect of two. It is important to understand the behavior of the model under multiple sources.

- Potential ablations:
I realize that getting ablation requests from reviewers is frustrating. However, this model relies on important prprocessing that includes spike train binning followed by Gaussian smoothing. Have the authors tries different binning and smoothing resolutions? Ho robust is the model for variation on these steps?

Minor:

- Captions often indicate R^2 forecasting error but it is not indicated what quantity is being forecasted. Is it cursor velocity (I believe this is it in most cases) or spiking activity? Captions should be precise on this front.

- Line 220: authors indicate "$\mathcal{D}$-dimensional [...]" but here D is a dataset. Not sure what is meant there or if this is a typo.

- Line 235: "[...} have been shown to be better for [...]" citation needed.

- In C4, the authors mention the presence of unconditional trials in training. It is not clear what this means in this context. More details about what trial information is removed, or uncondtiioned on, is needed.

- Related work, "Multi-session Training and Alignment". The authors review past work that aim to do transfer learning for multi-session inference. However they do not acknowledge that the other efforts they cite under the "Foundation models for neuroscience" section also achieve this. It is important to acknowledge that recent work does achieve borad generalization across sessions, animals, labs, etc. Even is the authors do acnkowldge these past results later on, they cast them as "specifically designed for decoding brain-machine interfaces" which is not accurate. If anything, these past works work on very simlar objectives and datasets as the current work.

I would be happy to revise my score if the authors provide adequate answers to these questions.

### Soundness
3

### Presentation
3

### Contribution
3
