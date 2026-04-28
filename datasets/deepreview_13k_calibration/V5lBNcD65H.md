# MTEEG: A Multi-Task Learning Framework for Enhanced Electroencephalography Analysis Using Low-Rank Adaptation

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 5, 6

## Abstract
Electroencephalography (EEG) analysis using deep learning has traditionally placed a strong emphasis on models that are custom-built and optimized for specific datasets. Several recent research utilize self-supervised learning to extract generic representations from massive amounts of unlabeled EEG data. The pre-trained models are then fine-tuned on each downstream dataset independently, demonstrating promising results. However, in practical applications involving multiple tasks, utilizing a separate model for each is not ideal regarding computational and spatial cost. In this study, we go one step further and explore the simultaneous adaptation of a pre-trained model to multiple different tasks. The EEG signals exhibit significant heterogeneity due to their collection from various subjects using diverse devices and experimental setups, resulting in potential conflicts among different tasks that impede joint optimization. To tackle this challenge, we propose MTEEG, a multi-task EEG recognition framework which incorporates a task-agnostic temporal encoder and task-specific low-rank adaptation modules to disentangle the parameter space, facilitating both task interaction and specification. Experiments show that MTEEG surpasses other multi-task methods and performs on par with state-of-the-art single-task methods on abnormal detection, event type classification, emotion recognition, seizure detection, sleep stage classification and motor imagery classification after being tuned jointly on six publicly available datasets. MTEEG shows the potential of multi-task EEG recognition and promotes the development of general-purpose brain-computer interfaces in the future. The source code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
MTEEG is proposed to solve the problem of fine-tuning a pretrained feature extractor separately for multiple downstream tasks, with the goal of reducing the computational cost of fine-tuning multiple times. MTEEG uses task-agnostic EEG encoders (temporal) and task-specific LoRA adaptors on top of a versatile pre-trained EEG backbone (LaBraM). Results on unseen tasks/datasets indicate MTEEG either maintains or surpasses single-task fine-tuning performance while using fewer overall parameters.

### Strengths
- MTEEG highlights the possibility of shared task structure/knowledge in heterogeneous EEG task/application domains that can be exploited during modeling, especially in the emerging EEG + AI space.
- Use of LoRA leads to parameter efficiency compared to base EEG "foundation" models, which is a desirable property for deployment.

### Weaknesses
 - Preprocessing of the EEG signal needs improvement: 1) physiologic signal content of scalp EEG is between 0.1-25Hz (lower frequencies). Anything beyond 25Hz (45Hz at most) is considered high-frequency noise. The current approach risks including artifacts and noise that could negatively impact model performance and generalization. 2) notch filter depends on which country the data was collected in. Example -- TUAB/TUEV are collected in US where power line freq. is 60Hz. Applying a 50Hz notch filter to US data is inappropriate and will distort the signal. 3) Sampling frequency can be safely dropped to 128Hz or even 80Hz, which will save computation time and memory without losing critical information. 3) EEGs ideally would be normalized channel-wise (using statistics calculated from the whole recording), otherwise amplitude variability across channels is lost. The current approach does not account for the inherent differences in signal amplitude across channels, which can confound the model. Consider approach in [1] for preprocessing.
- Reliability of results: 1) Variability that is important to report is of the test set (perhaps bootstrap samples?) rather than random seeds (Tables 2-4). Reporting variability across random seeds does not provide insight into the model's generalization performance on unseen data. 2) Significance testing of mean/group differences is needed to trust the ablation results (Figures 4, 5). Without statistical significance, it's impossible to determine if the observed differences are meaningful or due to chance.
- As far as I understand, the proposed approach is only applicable when all downstream tasks of interest are known beforehand. As such, the problem/motivation/hypothesis and real-world need/utility are unclear to me (line 15-20, line 48-53). In future clinical environments, we may want to have multiple EEG models/tasks "active" at the same time rather than switch from one model/task to another, while the EEG spatial configuration remains the same (10-20 system), i.e., there is no spatial heterogeneity. Secondly, fine-tuning is done using few task labels given that EEG labels are very expensive to obtain. Therefore, convergence is typically achieved relatively quickly, i.e., the time/computation overhead is practically negligible to fine-tune a backbone separately for each task of interest.
- Overall presentation can be substantially improved: 1) discussion and limitations should be substantial, insightful, and be in the main text, 2) figures are taking up too much space for the insight they provide (can start the y-axis at 0.5 instead of 0.0), 3) the core argument/narrative of need of multi-task learning in EEG and central hypothesis/question of the study needs revision and clarity.

### Questions
- Its unclear to me what the central hypothesis and question of the study is. Is it simply about saving time during fine-tuning or inference when all downstream tasks are known apriori?
- Typo in equation at line 170: Do you mean C_p instead of C_k?
- Q: What exactly happens in line 174? Do you mean temporal and spatial positional encodings?
- p refers to tasks (line 208, figure 2) and datasets (line 154) interchangeably, which is quite confusing. You can explain/justify the equality at the beginning and use either meaning consistently throughout the paper.
- Q: is the variability shown in Figures 4 and 5 statistically significant?
- Q: Is the parameter efficiency of MTEEG only due to the low-rank adaptor module, or are there other differences b/w LaBraM-base and MTEEG-base?
- Consider adding experiments that can show the heterogeneous conflict issue in multi-task fine-tuning (line 59-60) without LoRA adaptors and how the knowledge isolation is acheived using LoRA in MTEEG? I think this clarity is needed for readers to fully understand and "see" the issue the paper claims to address.
- These studies may be of interest for future work: 1) for self-supervised EEG pre-training and generalizability [1][2] and 2) effect of EEG heterogeneity/variability on EEG-ML/AI models [3].


[1] Banville, Hubert, et al. "Uncovering the structure of clinical EEG signals with self-supervised learning." Journal of Neural Engineering 18.4 (2021): 046020.

[2] Wagh, Neeraj, et al. "Domain-guided self-supervision of eeg data improves downstream classification performance and generalizability." Machine Learning for Health. PMLR, 2021.

[3] Wagh, Neeraj, et al. "Evaluating latent space robustness and uncertainty of EEG-ML models under realistic distribution shifts." Advances in Neural Information Processing Systems 35 (2022): 21142-21156.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The article introduces MTEEG, a multi-task EEG recognition system that improves the adaptation of a pre-trained model to different tasks. MTEEG uses a pre-trained model in combination with a task-independent temporal encoder to capture global knowledge from EEG signals, while task-specific low-rank adaptation modules are employed to manage the different parameter spaces for each task. The training process of MTEEG takes place in two stages: In the first stage, a LaBraM model is pre-trained on unlabeled data to extract information from the raw EEG signals. The model is then fine-tuned for specific downstream datasets, while specific low-rank adapters for each task are integrated into the transformer encoder to ensure parameter isolation. The proposed approach was verified on 6 different datasets.

### Strengths
Although the authors used different data sets and conducted extensive experiments and ablation studies, the approach used is not particularly novel. A more innovative method or perspective would enhance the contribution of the research to the existing literature.

### Weaknesses
The paper lacks clarity and self-containment, making it difficult for readers to fully grasp the research objectives and methodologies.

The paper appears to be a combination of existing methodologies, such as employing large pre-trained models and fine-tuning layers for specific tasks. However, it lacks a significant novel contribution to the field, which limits its impact and originality in advancing the research.

The authors should clarify how their work differs from transfer learning, which typically involves freezing certain layers of a pre-trained model while training the remaining layers for a specific task. A comparison highlighting the unique aspects of their approach compared to standard transfer learning methods would improve understanding of their contribution to the field.

### Questions
The authors should clarify how their work differs from transfer learning, which typically involves freezing certain layers of a pre-trained model while training the remaining layers for a specific task.

If the different data sets show variations in the number of channels and sampling frequencies of the EEG signals, the authors should provide a clear explanation of how they resampled the EEG signals to 200 Hz. This should include details of the methods used for upsampling and downsampling to ensure consistency between data sets.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces MTEEG, a framework for multi-task EEG recognition that leverages low-rank adaptation (LoRA) to efficiently fine-tune a pre-trained EEG foundation model across multiple tasks. The study presents a pioneering attempt to apply parameter-efficient fine-tuning techniques, specifically LoRA, to the domain of EEG-based multi-task learning. MTEEG demonstrates its capability by outperforming established multi-task and single-task models across six different EEG datasets, covering tasks like abnormal detection, event classification, emotion recognition, and seizure detection.

### Strengths
1. This paper makes a commendable and pioneering effort in exploring parameter-efficient fine-tuning techniques, specifically Low-Rank Adaptation (LoRA), for EEG foundation models in multi-task learning (MTL) scenarios. 
2. The experiments are robust, with adequate coverage of tasks and inclusion of critical ablation studies that help clarify the contribution of LoRA and other model components.

### Weaknesses
1. While the integration of LoRA into EEG models is an interesting step, the contribution appears limited. The paper does not introduce significant adaptations or improvements over the original LoRA method beyond its direct application in EEG-based MTL. This straightforward application of LoRA, without any novel modifications or insights into its behavior within the EEG domain, does not meet the high technical bar expected at ICLR.
2. The paper benchmarks the proposed MTEEG framework against older multi-task learning methods like HPS, MMoE, and CGC, which, while relevant, are not cutting-edge. These methods, while foundational, do not represent the current state-of-the-art in multi-task learning, and the paper lacks a comparison against more recent and advanced techniques. This makes it difficult to assess the true performance and potential of MTEEG in the context of contemporary multi-task learning research.
3. While LoRA is effectively evaluated, the paper does not explore how other advanced parameter-efficient fine-tuning methods could perform in the same context. For a more thorough assessment, it would be valuable to demonstrate if techniques like Adapters, Prefix-tuning, or Prompt Tuning could seamlessly replace LoRA or be integrated into the MTEEG framework. A more comprehensive evaluation, incorporating these baselines, would provide stronger evidence of the proposed framework's performance.

### Questions
This paper uses LoRA for multi-task fine-tuning across multiple datasets. However, have you considered a simpler approac, that is using a task-specific classification head for each dataset while fine-tuning the entire pre-trained LaBraM model? This method would be a straightforward way to enable multi-task learning, and I'm curious how its results compare to the LoRA-based approach.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a multi-task EEG classification model by fine-tuning a pre-trained large-scale EEG model, LaBraM. The authors employ a popular fine-tuning strategy, Low-Rank Adaptation (LoRA), to adapt the pre-trained model. The model architecture consists of a temporal encoder and a transformer encoder. The temporal encoder is responsible for mapping EEG patches into embeddings, while the transformer encoder captures global features. During training, the pre-trained weights in the transformer encoder are kept frozen, and only the LoRA adapters within the transformer are trainable. The model’s effectiveness is demonstrated across six EEG datasets, each representing a different learning task.

### Strengths
The paper is clear and readable, with well-designed figures highlighting key points. The authors aim to explore multi-task EEG recognition by training a model capable of handling multiple tasks simultaneously. Unlike prior studies on single-task learning, this work updates and trains the model on all tasks concurrently. The experimental section is both informative and thorough, providing valuable insights. Moreover, using a large EEG dataset demonstrates the potential of leveraging large-scale EEG models in this domain.

### Weaknesses
The novelty of the paper is somewhat limited. Based on the experimental results, I question the necessity of multi-task learning in this context. Theoretically, due to the inherent heterogeneity of EEG data—such as differences in channel numbers, collection protocols, and medical equipment—fine-tuning all downstream tasks together might not be the most effective strategy. Additionally, your design of task-specialized LoRA for training appears nearly identical to fine-tuning each task individually. This concern is supported by the experimental results, which show that the multi-task learning approach (MTEEG) sometimes leads to only marginal improvements or even worse performance compared to single-task learning methods. 

To demonstrate the necessity of multi-task fine-tuning, an ablation study should be conducted to compare fine-tuning each task individually against multi-task fine-tuning. Furthermore, it would strengthen the paper to include comparisons with TCN [1] and Medformer [2] as baseline methods. From my experience, despite their complexity, many EEG domain models struggle to outperform TCN on classification tasks. Medformer, a recent method designed specifically for EEG and ECG classification, should also be considered. Ensure that both TCN and Medformer have at least six layers and use default parameters during evaluation to maintain consistency. Due to the limited time, you can only evaluate on datasets TUEV and SEED-V.

### Questions
Could you provide more details about your data split? I have checked your appendix, but I'd like to know whether you are using the subject-dependent or subject-independent setup. The subject-dependent setup, while often yielding higher performance metrics, is generally inapplicable in real-world scenarios and risks potential data leakage, as the model might learn subject-specific characteristics rather than generalizable patterns. This can lead to deceptively high performance compared to the subject-independent setup.

### Soundness
2

### Presentation
3

### Contribution
2
