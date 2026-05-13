# CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding

- Decision: Accept
- Scores: 6, 8, 5, 8

## Abstract
Electroencephalography (EEG) is a non-invasive technique to measure and record brain electrical activity, widely used in various BCI and healthcare applications. Early EEG decoding methods rely on supervised learning, limited by specific tasks and datasets, hindering model performance and generalizability. With the success of large language models, there is a growing body of studies focusing on EEG foundation models. However, these studies still leave challenges: Firstly, most of existing EEG foundation models employ full EEG modeling strategy. It models the spatial and temporal dependencies between all EEG patches together, but ignores that the spatial and temporal dependencies are heterogeneous due to the unique structural characteristics of EEG signals. Secondly, existing EEG foundation models have limited generalizability on a wide range of downstream BCI tasks due to varying formats of EEG data, making it challenging to adapt to. To address these challenges, we propose a novel foundation model called CBraMod. Specifically, we devise a criss-cross transformer as the backbone to thoroughly leverage the structural characteristics of EEG signals, which can model spatial and temporal dependencies separately through two parallel attention mechanisms. And we utilize an asymmetric conditional positional encoding scheme which can encode positional information of EEG patches and be easily adapted to the EEG with diverse formats. CBraMod is pre-trained on a very large corpus of EEG through patch-based masked EEG reconstruction. We evaluate CBraMod on up to 10 downstream BCI tasks (12 public datasets). CBraMod achieves the state-of-the-art performance across the wide range of tasks, proving its strong capability and generalizability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces CBraMod, a novel foundation model designed for EEG signal decoding within Brain-Computer Interface (BCI) applications. CBraMod employs a novel criss-cross transformer architecture to combine modeling of mutual spatial and temporal dependencies inherent to EEG data. Additionally, the model incorporates an Asymmetric Conditional Positional Encoding (ACPE) scheme to learn to adapt to the diverse EEG data formats across various datasets. CBraMod is pre-trained on the extensive Temple University Hospital EEG Corpus (TUH) and evaluated across ten downstream BCI tasks using twelve public datasets. The results demonstrate that CBraMod achieves state-of-the-art performance, highlighting its strong generalizability and effectiveness across diverse EEG decoding tasks.

### Strengths
1. The utilization of a criss-cross transformer to independently model spatial and temporal dependencies is a significant advancement. By partitioning attention mechanisms into Spatial-Attention (S-Attention) and TemporalAttention (T-Attention), CBraMod effectively captures the heterogeneous dependencies in EEG signals, which are often overlooked in traditional full EEG modeling strategies.
2. Asymmetric Conditional Positional Encoding (ACPE):  Dynamic Encoding: The ACPE scheme dynamically encodes spatial and temporal
positional information which may enhance the model’s adaptability to various EEG formats. 
3. Comprehensive Pre-training. Pre-training CBraMod on the TUH dataset, comprising over 27 000 hours of EEG puts this architecture in line with several other top-performing models. 
• Time-Frequency Encoding. Instead of relying on temporal domain convolution the authors decided to explicitly use a tf-decompositon to augment time-domain embeddings

### Weaknesses
1. Limited Comparative Analysis with Recent Models. While the paper compares CBraMod with several non-foundation and foundation model baselines, the inclusion of more recent EEG foundation models, e.g. BrainWave (https://arxiv.org/abs/2402.10251) could provide a more comprehensive evaluation of CBraMod’s relative performance. Specifically, the absence of a direct comparison with models that also leverage transformer architectures and are pre-trained on large EEG datasets makes it difficult to ascertain the true novelty and performance gains of CBraMod.
2. Lack of interpretability. The authors did not provide any kind of interpretation of the obtained models. First of all, it would be very interesting to see what pieces of EEG (source topographies, frequency bands) contribute to the "powerful embeddings"  learnt by the foundation  model. Secondly, for the majority of the downstream tasks there is well defined defined hypothesis regarding the way the decoded information is encoded in the brain. For example motor imagery classification would require information in the 18-14 Hz and 15-25 Hz range on the sources located on the sensory-motor cortex with very distinct topographies. Addition of these would make the paper more convincing. The lack of visualization of learned features and their relationship to known neurophysiological phenomena limits the practical utility of the model.
3. Consistency of embeddings. We would expect that the obtained representation would somehow cluster in a mechanistically meaningful way.  For example, I would expect some clustering of the embeddings  with participant's age, gender, the downstream task, etc.  Demonstrating this consistency would significantly strengthen the presentation. Without such analysis, it is difficult to ascertain whether the model is learning generalizable features or task-specific artifacts.
4. Ablation Studies on Architectural Components. although the paper discusses the contributions of the criss-cross attention mechanism and the ACPE scheme, more granular ablation studies isolating each component’s impact on specific tasks would strengthen the claims regarding their individual effectiveness and justify their inclusion in the architecture. For example, it would be useful to see how performance changes when only spatial or temporal attention is used, or when ACPE is replaced with a standard positional encoding.

### Questions
1. I think I missed this but how exactly the architecture adapts to each of the dataset? I.e. I an interested in a)  purely technical adaptation due to variation in the number of channels and b) more conceptual one and needed due to the variability of the electro-dynamic properties of the head as a volume-conductor resulting in quite different spatial patterns of EEG activity. 
2.  What is the effect of altering the temporal window size (1 s) for the resulting performance? Could it be that different downstream tasks require different values of this important parameter? 
3. How important is the time-frequency-based augmentation of the embeddings? What is the performance gain it brings about?
4. Could the authors provide additional details on whether the entire CBraMod model or only specific layers are fine-tuned for downstream tasks? 
5. Related to  (4). Could the authors be more explicit regarding the strategies to prevent overfitting during fine-tuning on smaller
downstream datasets (e.g., dropout rates, weight decay specifics beyond pre-training)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces CBraMod, a novel EEG foundation model that leverages a criss-cross transformer architecture to capture the spatial and temporal dependencies of EEG signals. It employs an asymmetric conditional positional encoding scheme to adapt to diverse EEG formats and is pre-trained on a large EEG corpus. The model demonstrates state-of-the-art performance across 10 downstream BCI tasks, showcasing its capability and generalizability.

### Strengths
The paper proposes a novel transformer-based architecture for EEG feature extraction and uses it as a foundation model. Substantial comparative experiments have been conducted to show its good performance on different EEG prediction tasks. The presentation is clear, and superior results have been achieved. It’s a good exploration of using large-scale models to obtain EEG representations.

### Weaknesses
The current version shows a good architecture for feature extraction instead of a real foundation model. It would be beneficial to give a clearer description of the motivation for proposing such a ‘foundation model’ and how this model facilitates the application of EEG analysis and even brain-computer interfaces. Could we use only a few data for finetuning or tuning specific model faster?

The paper mentions that only 19 channels were used during pre-training, whereas additional channels were introduced in the downstream task. Could you clarify how the balance between channels was managed? It's unclear how the model adapts to varying channel counts between pre-training and downstream tasks, especially given the fixed input size of the transformer. The method for handling this discrepancy needs more elaboration.

Many layers are employed, yet the feature maps are not large. Did each layer contribute significantly to the final results? It would be beneficial to see an ablation study on the number of layers to understand the contribution of each layer to the overall performance, and to justify the depth of the model.

What features do the time-domain and frequency-domain branches capture? It would be beneficial to illustrate the specific frequency components learned by the frequency-domain branch within the patch encoder. The paper lacks a detailed analysis of the information captured by each branch, making it hard to understand their individual contributions.

How does the CNN-based position encoder capture positional information? Does this approach primarily leverage local features, and have you compared it with more traditional positional encoding methods? The positional encoding method is not fully explained, and it is unclear how it compares to standard positional encoding techniques, especially in terms of capturing global vs. local spatial relationships.

It would be helpful to provide a comparison of the computation cost of criss-cross attention against other attention mechanisms mentioned in Figure 5. The computational efficiency of the proposed attention mechanism needs to be evaluated against other methods to justify its use.

Have you evaluated the impact of data scale for both pretraining and fine-tuning? It would be interesting to know whether the incorporation of a pre-trained foundation model enables effective learning with a reduced amount of data for specific tasks. The paper does not explore the impact of varying data sizes during pre-training and fine-tuning, which is crucial for understanding the model's data efficiency.

### Questions
1. What features do the time-domain and frequency-domain branches capture? It would be beneficial to illustrate the specific frequency components learned by the frequency-domain branch within the patch encoder.
2. How does the CNN-based position encoder capture positional information? Does this approach primarily leverage local features, and have you compared it with more traditional positional encoding methods? 
3. It would be helpful to provide a comparison of the computation cost of criss-cross attention against other attention mechanisms mentioned in Figure 5.
4. Have you evaluated the impact of data scale for both pretraining and fine-tuning? It would be interesting to know whether the incorporation of a pre-trained foundation model enables effective learning with a reduced amount of data for specific tasks.
5. Many layers are employed, yet the feature maps are not large. Did each layer contribute significantly to the final results?
6. The paper mentions that only 19 channels were used during pre-training, whereas additional channels were introduced in the downstream task. Could you clarify how the balance between channels was managed?

### Soundness
4

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
In response to the limitations of existing EEG models, which primarily focus on whole-brain modeling while neglecting spatiotemporal dependencies, as well as the challenges faced by current EEG backbone models in handling EEG data in various formats, this study proposes an EEG foundation model based on a criss-cross transformer backbone. This work involves pretraining on a substantial dataset of EEG signals and fine-tuning on multiple downstream tasks.

### Strengths
This work addresses the challenges currently faced in EEG models by proposing an effective solution for spatiotemporal modeling through enhancements in model architecture. The model has undergone pretraining on a substantial dataset, and the experimental results are comprehensive, providing support for several contributions.

### Weaknesses
Due to the pretraining paradigm of CBraMod, it has not effectively addressed the challenges posed by the diversity of EEG data formats. This raises concerns regarding its suitability as a foundation model for EEG. The specific issues are outlined as follows.
1. This work acknowledges that current EEG foundation models still face challenges in handling EEG data of varying formats. However, the solution proposed by CBraMod during the pretraining phase, which involves the selection of 19 common EEG channels, appears to be a simplistic approach that does not effectively address the aforementioned issues. The use of a fixed set of 19 channels during pretraining limits the model's ability to learn truly generalizable spatial representations, as it is not exposed to the variability inherent in real-world EEG data with different channel configurations. This approach may lead to a model that is over-specialized to the specific 19-channel layout, hindering its performance on datasets with different channel montages.
2. To learn generic representations from both time-domain and frequency-domain EEG signals, this study conducted pretraining on the TUEG dataset, which primarily focuses on medical data related to conditions such as epilepsy. However, as a foundation model, CBraMod exhibits significant discrepancies between the pretraining data and the data used for downstream tasks. This raises questions regarding its theoretical validity. The TUEG dataset, being heavily skewed towards epileptic activity, may not provide a sufficiently diverse set of EEG patterns to enable the model to generalize well to other types of EEG data, such as those related to cognitive tasks or motor imagery. This discrepancy between pretraining and downstream task data could lead to suboptimal performance and limit the model's applicability as a true foundation model.
3. The ablation studies related to pretraining, being a crucial experiment, should be included in the main text.

### Questions
1. Given that this work is positioned as a foundation model, it is pertinent to inquire whether scaling laws exist at both the data level and the model size level. Have the authors conducted relevant experiments to explore these scaling laws?
2. It would be valuable to examine the loss function curves during the pretraining phase.
3. Could the authors elucidate their perspective on the motivation or value of foundation models within the EEG domain? Additionally, how does CBraMod balance the relationship between model size, computational cost, and performance?
4. During the pretraining phase, 19 common electrodes were utilized. How does the model handle discrepancies in the number of electrodes when applied to downstream tasks?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
* This paper proposes a new LLM model for EEG decoding, primarily trained on the Temple University EEG (TUEG) dataset and tested across different EEG decoding datasets.
* The authors introduce a new way to encode EEG data with various channel configurations, using asymmetric conditional positional dynamic encoding inspired by Chu et al. (2021) with different kernel sizes. They also present a new criss-cross transformer layer with temporal and spatial attention, improving upon the work of Huang et al. (2020) and adapting it effectively to the EEG context.
* The encoder's contribution lies in combining the BioT encoder for inputting frequency information via SFFT and the Labram temporal encoder utilizing Conv2D and GroupNorm.
* The pre-training strategy involves masked reconstruction with random masking of EEG patches instead of masking temporal and spatial components.
* The method is showcased on 12 datasets, spanning a variety of EEG decoding tasks.

### Strengths
* Although the general idea of using language models for EEG data is not new, the neural network architecture presents some novelty by incorporating and combining multiple ideas from previous works, such as Patch from Visual Transformer, Criss-Cross Transformer, and Asymmetric Conditional Positional with different kernel sizes. 
* This work presents a large number of experimental results on 12 different datasets and tasks.
* Some of the experimental results are quite encouraging and show incremental results over the Labram and BioT works.
* The use of large language models in the EEG field is relatively under-explored, especially considering the revolution we are experiencing in parallel fields such as audio, NLP, and vision. Bridging the bridge connecting other communities to the EEG community is very refreshing!

### Weaknesses
 **Originality**

While the particular combination of methods is novel, it primarily combines existing ideas from other deep learning subfields. This limits the overall novelty of the work, especially given the lack of sufficient ablations to discern which of the numerous components is truly important. To be very clear, there is no problem using components from other fields; in my opinion, this is highly encouraged, but the study needs to go in-depth to understand what leads to compatibility and the "bridge construction."

**Clarity**

In my opinion, the paper's writing could be improved. The text needs refinement to better guide the reader through the findings rather than just describing tables. There is no discussion about other papers; while the engineering contributions are clear, the scientific perspective is significantly lacking.

**Major Concerns**

* The choice of datasets for motor imagery, emotion, and sleep stage tasks seems arbitrary. For instance, in the case of motor imagery, the most widely used dataset is BNCI 2014 version 004, and the largest is from Stieger et al. (2021) to the best of my knowledge. However, the authors chose Physionet-MI.
*  The results in Physionet-MI are significantly below the state-of-the-art. A quick search reveals accuracies of 88.6% ± 9.0 using EEGSym, 86.36% with Zoumpourlis et al. (2023), and 73.60% with TIDNet on unseen subjects, where we have 64.17%. While I understand that the exact reproduction of results in EEG decoding is impossible, the reported results here are more than 20% below the state-of-the-art. This concern extends to sleep stage models, where datasets like SleepEDF+, MASS, or SHHS are standard, and accuracies above 80% are expected. The same issue applies to emotion classification; for example, Zhang et al. (2024) achieved better results on the SEED dataset testing with different train-test splits.

* Furthermore, when critically analyzing the model's usefulness based on the metrics—and considering literature from the field, such as O. Alkob et al. (2018) and Combrisson and Jerbi (2015)—the metric values fall short of demonstrating real usefulness for BCI applications.

* The choice of baselines is inadequate and possibly inherits these shortcomings from the BioT and Labram studies. Although the authors cite well-established works in the literature, there is no comparison with neural networks like EEGNet, ShallowNet, EEGConformer, EEGSym, ATCNet, FBCNet, and many others that effectively capture temporal and spatial information in motor imagery tasks. By using neural networks with only frequency-based encoders (e.g., BioT), the spatial and temporal information critical for motor imagery is not learned. Employing weak baselines for classification tasks makes the gains appear larger than they actually are. This issue also applies to the sleep stage task, where models like USleep, DeepSleepNet, SleepTransformer, XSleepNet, SeqSleepNet, ChambonNet, and others should be considered as baselines.

* Using the TEUV and TUAB datasets for abnormal detection and event-type classification while employing TEUG for pre-training leads to data leakage. This is indicated on the Temple University dataset's own webpage: "The TUH EEG Events Corpus (TUEV: v2.0.1): This corpus is a subset of TUEG."

### Questions
All the questions are pointed out in the Major Concerns section.

### Soundness
3

### Presentation
3

### Contribution
3
