# Learning to Embed Time Series Patches Independently

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 8, 5

## Abstract
\vspace{-4pt}
Masked time series modeling has recently gained much attention as a self-supervised representation learning strategy for time series.
Inspired by masked image modeling in computer vision, recent works first patchify and partially mask out time series, and then train Transformers to capture the dependencies between patches by predicting masked patches from unmasked patches.
However, we argue that capturing such patch dependencies might not be an optimal strategy for time series representation learning;
rather, learning to embed patches independently results in better time series representations.
Specifically, we propose to use 1)~the simple patch reconstruction task, which autoencode each patch without looking at other patches, and 2)~the simple patch-wise MLP that embeds each patch independently.
In addition, we introduce complementary contrastive learning to hierarchically capture adjacent time series information efficiently.
Our proposed method improves time series forecasting and classification performance compared to state-of-the-art Transformer-based models, while it is more efficient in terms of the number of parameters and training/inference time.
\vspace{-4pt}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors propose a mix of contrastive learning and masked modelling on time-series data, and a patch-independent approach to reconstruction is shown to outperform patch dependant (vanilla mask modelling) approach. Their PI approach auto encodes unmanned patches. Authors evaluate on forecasting and classification of time-series data.

### Strengths
- Extensive experiments comparing to other methods and ablating different components. 
- Incremental but shown to improve approach with simple mechanisms.
- Interesting analysis on distribution shift

### Weaknesses
 - Novelty is weak, their contribution auto encoding is quite established before masked modelling literature and one of the early approaches to representation learning. It is more that exploring this within time-series data which seems to be there contribution. Also mixing of CL and masked modelling has been explored in other methods but not exactly similar to their approach.


- Missing reference to previous method that Combine CL and MAE but in a different context and different method: Gong, Yuan, et al. "Contrastive audio-visual masked autoencoder." arXiv preprint arXiv:2210.07839 (2022).



### Questions
Figure 5 is not as clear what it is conveying? What is Fig. 5 Left showing in terms of colours? Fig. 5 Right it is a bit confusing since it is PD-PI and x & y axis represent the slop and amplitude of diff between training and test phases, It is not clear to me what is exactly being changed to have the distribution shift in the time-series data?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper tackles the task of time series forecasting using masked modeling. The authors propose a patch reconstruction task to facilitate training. The patches are treated independently in the patch reconstruction task. A complimentary contrastive learning, where two views with a 50% masking ratio are used for CL, is utilized. Experiments on the common forecasting benchmark with 7 datasets, and the classification benchmark with 5 datasets, show the efficacy of the proposed method.

### Strengths
1. The paper is generally well-written and easy to follow. The method seems straightforward to implement.
2. The experiments are thorough. The proposed method is evaluated on two tasks with a total of 12 datasets. Also, the transfer learning setting is explored. The key PI vs. PD task is analyzed through quantitative and qualitative experiments.

### Weaknesses
1. The paper is generally well-written and easy to follow. The method seems straightforward to implement.
2. The experiments are thorough. The proposed method is evaluated on two tasks with a total of 12 datasets. Also, the transfer learning setting is explored. The key PI vs. PD task is analyzed through quantitative and qualitative experiments.

1. The training and inference efficiency analyses are brief or missing. It would be useful to see whether the patch-independent design can also bring benefits to inference time. The model requires contrastive learning and reconstruction loss, which might drastically increase training time compared to other supervised learning methods. Therefore it would be useful to see it compared to supervised learning methods as well.

### Questions
1. What is the input horizon (look-back window/length of historic sequence) for the TSF task (Table 3)? This detail is missing.
2. Are the numbers in Table 3 averaged over multiple runs (with different random seeds) or are they single runs only?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new approach called PITS (Patch Independence for Time Series) for self-supervised representation learning of time series data. The authors argue that previous methods that capture patch dependencies may not be optimal and instead propose learning to embed patches independently. They introduce the "Patch-Independence"-based MTM (Masked Time Series Modeling) method and complementary contrastive learning. They demonstrate that using an MLP as the PI architecture in MTM can independently reconstruct unmasked patches while disregarding interactions between patches, thereby improving efficiency while reducing the parameter count. Simultaneously, it has been shown that introducing complementary contrastive learning effectively captures information from adjacent time series. The model has been tested on two downstream tasks: time series forecasting and classification, demonstrating significant advantages in terms of performance, architectural interpretability, and robustness.

### Strengths
1) Originality: The paper introduces a novel approach to self-supervised time series representation learning, with a focus on patch independence. This represents a unique perspective challenging the traditional methods of capturing patch dependencies. Additionally, it is the first model to integrate MTM and CL, showcasing the innovation of the implementation while improving model performance.
2) Quality: The paper is well-written and provides a comprehensive analysis of the proposed method. The experimental design is thorough, including comparisons with state-of-the-art methods, and it demonstrates strong performance in two downstream tasks. Furthermore, the completeness of the ablation experiments illustrates attention to various model details.
3) Clarity: The paper is clear and well-organized. The authors provide a clear motivation for their work, explain the proposed method in detail, and present the experimental results in a clear and concise manner.
4) Significance: The proposed method achieves superior performance compared to existing approaches in time series forecasting and classification tasks. The efficiency of the method in terms of parameters and training time is also highlighted, which makes it more practical for real-world applications.

### Weaknesses
1. The representation in Figure 1(a) should be clearer and correspond one-to-one with the description in Section 3.2. For example, the inconsistency between "MLPmixer" in the figure and "MLP-Mixer" in the text should be rectified, and the explanations for both in the PI architecture need to be more explicit. Specifically, the figure lacks detail on how the input time series is converted into patches, and how these patches are processed by the MLP-Mixer. It is unclear if the MLP-Mixer operates on each patch independently or if there is some form of interaction between patches within the architecture. A more comprehensive explanation for this figure is needed, and citation markers may be introduced as necessary.
2. The two layers described in Figure 1(b) should be clearly labeled, corresponding to one for the CL task and one for the PI task, as indicated in the caption. Currently, the figure does not explicitly distinguish between the two layers and their respective roles in the contrastive learning and patch independence tasks. This lack of clarity makes it difficult to understand the precise implementation of the proposed method.
3. The notation "No(SL)" in Table 1 should be explained in the description, specifically in Section 2. The current lack of explanation for this notation makes it difficult to interpret the results presented in the table. It is important to define all abbreviations and notations used in the paper to ensure clarity and reproducibility.
4. One of the contributions is the use of self-supervised mask reconstruction, but for the TSF task, only two baseline models using self-supervised mask reconstruction are provided. The evaluation section could benefit from more comparisons with other baselines that use self-supervised mask reconstruction. Specifically, the paper should include a wider range of comparisons to establish the superiority of the proposed method over existing self-supervised approaches for time series forecasting.

### Questions
1.	Could you provide a more detailed explanation for why the PI architecture is superior to the PD architecture? The results of the comparative experiments are quite significant, but we believe that adding some qualitative analysis would make the argument more convincing.
2.	Would it be possible to offer a more comprehensive explanation of how the proposed method is implemented, including details on hyperparameter configurations? We would appreciate seeing more comparative experimental results to further validate the rationale for these selections.
3.	Have you conducted comparisons between the proposed method and alternative baselines, such as autoencoders or other self-supervised learning approaches tailored for time series data?
4.	Have you taken into account the limitations of the proposed model? Could you elaborate on potential challenges or specific scenarios in which the method might exhibit suboptimal performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The key idea of the paper "Learning to Embed Time Series Patches Independently" is to propose a new approach for time series representation learning by focusing on embedding patches independently rather than capturing patch dependencies. The authors introduce a patch reconstruction task that autoencodes each patch without considering other patches and a patch-wise MLP architecture for embedding. They also incorporate complementary contrastive learning to efficiently capture adjacent time series information. Experimental results demonstrate that their proposed method outperforms state-of-the-art Transformer-based models in time series forecasting and classification tasks while being more efficient in terms of parameters and training time.

### Strengths
1) This paper is easy to follow.
2) The paper introduces the concept of patch independence for time series representation learning, arguing that learning to embed patches independently leads to better representations. This novel approach challenges the conventional strategy of capturing patch dependencies and proposes a patch reconstruction task and a patch-wise MLP architecture.
3) The paper presents extensive experiments on various tasks, including low-level and high-level tasks, demonstrating the superiority of the proposed method compared to state-of-the-art  models. The experiments are conducted under both standard and transfer learning settings, further validating the effectiveness of the approach (a significant performance gain is reported).

### Weaknesses
1) Despite the author's cautionary language, using only 'argue' rather than 'claim', 'learning to embed time series patches independently is superior to learning them dependently for TS representation learning' still sounds a bit lax to me. Especially considering the lack of substantial experimental evidence to support such an argument. (Comparison among representative methods cannot support the argument ‘A is superior to B when A,B refer to a set of methods’)

2) Given that you’ve mentioned the complementary masked strategy for CL and claim it as a ‘main contribution’, it should be investigated in related work. (Such strategy has already been proposed earlier, though in other domain. Such as Ref 1,2,3 provided below)

[1] SdAE: Self-distillated Masked Autoencoder

[2] Complementary Mask Self-Supervised Pre-training Based on Teacher-Student Network

[3] Deep Feature Selection Using a Novel Complementary Feature Mask

3) Lack of clarity in exposition (for certain sentences): The paper should strive to provide clear and concise explanations. For example, “Secondly, we propose to utilize the simple PI model architecture (e.g., MLP), as opposed to the conventional PD architecture (e.g., Transformer), which is not only more efficient but also performs better.”  What does which refer to in this sentence?

### Questions
Please refer to the weakness part. Further, in Table 2, does 46 mean 46 hour of training time?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
