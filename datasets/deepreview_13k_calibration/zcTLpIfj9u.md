# Future-Guided Pretraining via Time-to-Event Supervision for 3D Medical Imaging

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 5, 8

## Abstract
With the rise of medical foundation models and the growing availability of imaging data, scalable pretraining techniques offer a promising way to identify imaging biomarkers predictive of future disease risk. While current self-supervised methods for 3D medical imaging models capture local structural features like organ morphology, they fail to link pixel biomarkers with long-term health outcomes due to a missing context problem. Current approaches lack the temporal context necessary to identify biomarkers correlated with disease progression, as they rely on supervision derived only from images and concurrent text descriptions. To address this, we introduce time-to-event pretraining, a pretraining framework for 3D medical imaging models that leverages large-scale temporal supervision from paired, longitudinal electronic health records (EHRs). Using a dataset of 18,945 CT scans (4.2 million 2D images) and time-to-event distributions across thousands of EHR-derived tasks, our method improves outcome prediction, achieving an average AUROC increase of 23.7% and a 29.4% gain in Harrell’s C-index across 8 benchmark tasks. Importantly, these gains are achieved without sacrificing diagnostic classification performance. This study lays the foundation for integrating longitudinal EHR and 3D imaging data to advance clinical risk prediction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a future-guided pretraining approach using time-to-event supervision to enhance the prognostic capabilities of 3D medical imaging models. By incorporating longitudinal EHR data into the pretraining process and predicting time-until-event, the model outperforms traditional methods across multiple standard tasks, as demonstrated by thorough experiments.

### Strengths
1. Innovative Approach: The method creatively leverages EHR data following a medical scan to assist model pretraining, demonstrating better performance compared to imaging-only pretraining.
2. Comprehensive Evaluation: Extensive comparisons across multiple tasks validate the robustness and efficiency of the TTE-based approach across different architectures.

### Weaknesses
1. Dependence on Large EHR Datasets: This approach relies on extensive, high-quality EHR data, which many medical datasets do not include. The requirement for longitudinal EHR data, specifically, limits the applicability of this method to settings where such data is routinely collected and curated. The absence of standardized EHR formats and data quality issues across different institutions further compounds this limitation, potentially introducing bias or inconsistencies when applying the model to new datasets.
2. Limited Modality Scope: Tested only on CT images; broader modality testing could validate versatility across imaging types. The exclusive use of CT images raises questions about the generalizability of the proposed method to other imaging modalities such as MRI, ultrasound, or X-ray. Each modality has unique characteristics and noise profiles, which could significantly impact the performance of the model. It is unclear if the TTE pretraining would be as effective with, for example, the lower resolution of ultrasound or the different contrast mechanisms of MRI.
3. Interpretability: The TTE pretraining’s impact on specific pixel-level biomarkers is less clear; additional analysis on feature attribution could help. While the paper demonstrates improved performance, it lacks a clear explanation of how the TTE pretraining influences the model's focus on specific image features. It is unclear whether the model is learning clinically relevant biomarkers or simply fitting to spurious correlations in the data. A more detailed analysis of feature attribution, perhaps using techniques like Grad-CAM or integrated gradients, is needed to understand the model's decision-making process.

### Questions
1. Why start from 3D image scans instead of 2D medical images? Is this due to the dataset choice, or has similar work already been done on 2D data?
2. How does the choice of time segmentation for EHR data affect model results during pretraining? Specifically, my understanding is that the model predicts the probability of a patient experiencing a certain event at intervals like 1, 2, or 3 years post-scan. How does the granularity of these time segments impact the performance of the pretrained encoder?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors proposed to utilize the time-to-event information in EHR that paired with the imaging data as a form of supervision for the pre-training purpose. A public dataset with both 3D images and EHR notes is employed for the pre-training and downstream applications. Another dataset without the time events is also used for the evaluation of model adaptation. The manuscript is easy to follow. However, it also suffers from several critical flaws, which are detailed below.

### Strengths
- Propose utilizing the time events as pre-training tasks specially designed for prognosis tasks in downstream applications. 
- The manuscript is overall easy to follow

### Weaknesses
 - The proposed method is limited in generalization since it will require longitudinal time-to-event EHR data as the supervision for the pre-training. In comparison to the common self-supervised pre-training, the proposed methods are harder to scale up.

- There is no comparison evaluation between the proposed method and prior methods in model pre-training. Only the results of the proposed method with different model architectures are reported. It will be difficult to appreciate the benefits of the proposed method.

- The selected model architecture also raises questions since there are many popular model networks in medical imaging, e.g., 3D-UNet, ViT, etc. It will be helpful to see their performance compared to the vanilla ResNet. 

- Baselines without the pre-training process should also be reported.

- The current setting utilizes public data for both pre-training and downstream applications. Having a separate evaluation dataset of a prognosis task will be helpful. 

- The proposed method is limited in technical innovation, though utilizing the time-to-event data as a form of supervision is relatively new in the pre-training. Mostly existing techniques are adopted for the pre-training.

### Questions
See above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
*Edit: Score increased from 6 to 8 during discussion period.*

This paper presents a self-supervised learning (SSL) method for 3D medical imaging data that leverages electronic health records (EHR) to provide extra sources of supervision via time-to-event modeling. The proposed method, future-guided pretraining, performs time-to-event (TTE) survival modeling of various medical events in the longitudinal EHR associated with each 3D scan. The authors show that future-guided pretraining consistently improves downstream TTE modeling and prognostic classification tasks – also improving data efficiency – without degrading standard diagnostic classification performance.

### Strengths
- The presentation quality is very high. Care has been taken to logically organize the paper, clearly articulate key points, and straightforwardly present results with concise figures and tables.
- The core idea is creative, making use of the wealth of longitudinal EHR data associated with each 3D volume for pretraining.
- Discussion or related work and background is particularly strong.
- Experiments are sufficiently thorough and easy to interpret – results are convincing.

### Weaknesses
 - The actual description of the TTE pretraining approach is brief (lines 184-191) and somewhat unclear. I would advise the authors to flesh out this section. See specific questions below.
- A description or list of the 8,192 EHR pretraining tasks is never provided. I’m aware there may not be a convenient place to list this many items, but a general description of categories of events or a few illustrative examples would be helpful. Without this information, it’s impossible to assess whether, e.g., one the TTE pretraining tasks is *also* used as a downstream TTE modeling task. In this case, there may be concerns of “label leakage”.

I’m happy to increase my score once these issues are addressed – this is an otherwise strong submission.

### Questions
- What exactly does it mean that Steinberg et al.’s method was used to “[sample tasks to maximize entropy given the frequency distribution of medical codes populating the DAG”? I feel that a basic plain-language description of the motivation for this procedure is needed first: why is this method being applied at all? Are there way more than 8k events and the goal is to settle on a subset of 8k “meaningful”/common ones for pretraining? I don’t understand the motivation.
- Unless I am misunderstanding, this is the only description of the TTE pretraining procedure and labels used: “We define our TTE task labels by predicting the time until the next occurrence of a medical code.” The previous Section 3 described deep survival modeling in the abstract, so I expected Section 4 to more concretely describe how TTE pretraining works. Is this a “competing risks” approach, where multiple events are being modeled simultaneously (in “multi-label” fashion)?
- What are the 8,192 EHR tasks/events? I’m aware it would be cumbersome or impossible to list and define them all, but any reasonable attempt to convey information about them would be useful. What kinds of “events” are they? What are some examples?
- Related to the above point, are the downstream labels *also* present in the set of TTE pretraining tasks? If so, isn’t there concern of “label leakage”, where the model has been pretrained on label information present in the downstream training dataset? Please clarify this.

**Minor comments/questions:**
- Line 13: Maybe “build” instead of “capture” since you use this word in the next sentence.
- In-text citation style seems off – should be parenthetical (\pcite{}) in most cases when used at end of sentence/clause: “Sox et al. (2024)” -> “(Sox et al., 2024)”
- Change “e.g.” -> “e.g.,” throughout
- Would include more recent references [1,2] when discussing deep prognosis models on longitudinal medical imaging (first paragraph of Section 2)
- “i.e. 8192” -> “i.e., 8.192”
- “Our approach improves training data efficiency, increasing training labels by an average of 3x over labels assigned to patients based on their current EHR visit.” This is a bit unusual to highlight as a main contribution – I don’t think readers will understand what “increasing training labels” means without having read the entire paper (nor why this impact data efficiency). Perhaps clarify language here to indicate that your approach provides 3x as many sources of supervision during SSL + that this is what provides data efficiency benefits.
- “Pretraining task labels as assigned per-CT scan and vary in density based on pretraining approach, see Figure 2.” Perhaps “as assigned” is meant to be “are assigned”? Also change “, see Figure 2” -> “(Figure 2)”.
- Be consistent with “c-statistic” vs. “C-statistic”

**References**
[1] Holste, Gregory, et al. "Harnessing the power of longitudinal medical imaging for eye disease prognosis using Transformer-based sequence modeling." NPJ Digital Medicine 7.1 (2024): 216.
[2] Sriram, Anuroop, et al. "Covid-19 prognosis via self-supervised representation learning and multi-image prediction." arXiv preprint arXiv:2101.04909 (2021).

### Soundness
3

### Presentation
4

### Contribution
3
