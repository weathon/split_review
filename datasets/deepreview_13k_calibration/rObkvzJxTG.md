# Smoothing the Shift: Towards Stable Test-time Adaptation under Complex Multimodal Noises

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Test-time adaptation (TTA) aims to tackle distribution shifts using unlabeled test data without access to the source data. In the context of multimodal data, there are more complex noise patterns than unimodal data such as simultaneous corruptions for multiple modalities and missing modalities. Besides, in real-world applications, corruptions from different distribution shifts are always mixed. Existing TTA methods always fail in such multimodal scenario because the abrupt distribution shifts will destroy the prior knowledge from the source model, thus leading to performance degradation.
To address this challenging problem, we propose two novel strategies: sample identification with interquartile range **S**moothing and **u**nimodal assistance and **M**utual **i**nformation sharing (SuMi). SuMi smooths the adaptation process by interquartile range which avoids the abrupt distribution shifts. Then, SuMi fully utilizes the unimodal features to select low-entropy samples with rich multimodal information for optimization. Furthermore, mutual information sharing is introduced to align the information, reduce the discrepancies and enhance the information utilization across different modalities. Extensive experiments show the effectiveness and superiority over existing methods under the complex noise patterns in multimodal data. Code will be available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents SuMi, a novel approach for test-time adaptation (TTA) that aims to address distribution shifts in multimodal data. Through sample selection and mutual information sharing, the authors propose an approach that adapts effectively to complex multimodal noise patterns under distribution shifts.

### Strengths
The paper introduces two main contributions—(1) a dual filtering mechanism to refine sample selection and (2) a mutual information loss
strategy to promote information alignment across modalities. These strategies aim to address limitations in current TTA approaches, particularly in multimodal data scenarios.
The authors validate their method across various corruption scenarios, including challenging out-of-distribution samples. This broad
testing highlights SuMi’s robustness and effectiveness under multimodal noise conditions.

### Weaknesses
1.Although the experiments demonstrate the method’s effectiveness, both datasets are limited to video-audio modalities. It remains unclear whether SuMi can generalize to other multimodal datasets, such as image-text pairs. This raises a question of the method’s applicability to vision-language models and other multimodal contexts (e.g., image and point cloud as in MM-TTA[1]).
2.The proposed sample selection strategy shows promising results in the ablation study. However, comparable sample selection-based approaches (e.g., DEYO, EATA) are not sufficiently compared. A comparison of DEYO/EATA with (IQR + UA) , as well as experiments
combining DEYO/EATA and MIS, would provide clearer insights into the distinct benefits of SuMi.
3.The experiments primarily focus on corruption shifts, but multimodal scenarios often encounter various other types of distribution shifts. Including datasets that reflect shifts beyond corruption could offer a more comprehensive evaluation of SuMi’s robustness.
4.The paper’s three main components—sample identification with IQR, unimodal assistance, and mutual information sharing—lack a
cohesive, unified framework. The combination of these techniques appears to address separate aspects of TTA, but the rationale for exclusively selecting these methods is insufficiently articulated. Greater clarity on the connections and unique insights of each
component could enhance the motivation and provide readers with more convincing reasoning for the proposed approach.

### Questions
The authors could respond to the identified weaknesses by addressing the following aspects:Limited Multimodal Data Diversity, Insufficient Comparative Analysis with Sample Selection-Based TTA Methods, Limited Scope in Addressing Diverse Distribution Shifts, Fragmented Methodological Motivation.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a novel task called multimodal wild TTA and presents a method named Sample Identification with Interquartile Range Smoothing and Unimodal Assistance and Mutual Information Sharing (SuMi). SuMi addresses the challenges of bridging the source domain and out-of-distribution scenarios through interquartile range smoothing. It effectively selects low-entropy samples rich in multimodal information for optimization and employs mutual information sharing to align different modalities. Experiments on two popular multimodal datasets show that SuMi significantly outperforms existing TTA methods, confirming its effectiveness.

### Strengths
The author proposes a TTA task that seems to be more applicable, which is helpful for the subsequent development of TTA. The paper is well-motivated and easy to follow. And the author's related work review is relatively comprehensive. From the experiments, the proposed SuMi has achieved significant performance improvement in new TTA task.

### Weaknesses
1. My main concern is the motivation behind the paper. Is this innovative task based on a pseudo-motivation? Is it truly feasible for this task to occur in real-world application scenarios? See the Questions part for details.
2. Under real conditions of TTA, the number of modalities is generally more than two. I noticed that the authors discuss a multimodal form in equation (5), but at other times they refer only to a two-modality form. Can these be expanded into a general multimodal setting? Is it possible to validate the effectiveness of the method across multiple modalities in the experiments?
3. The authors provide a comprehensive discussion of the parameters. However, there is no explanation for why the 'Interquartile' form of IQR was chosen. In this specific task, other quantile ranges might yield better results. Additionally, the paper's improvement is limited to gradually smoothing with the number of iterations, which is merely a simple linear process. There is no discussion of a more theoretical or effective smoothing process.
4. The paper mentions that the selection of hyperparameters (such as $\mu$) relies on prior information about the dominant modality of the datasets. However, in TTA, we cannot know the prior information of the data. Could this directly impact the performance of the method across different datasets? Is there a more robust hyperparameter-selection mechanism?

### Questions
I would suggest that the authors consider discussing the setting of the new task and the practical applications of its motivation in detail. In real-world scenarios, would algorithms truly continue to be utilized under conditions where sensor failures or malfunctions occur? From my perspective, this task appears to resemble a combination of a modality missing and a TTA subtask. The proposed approach seems to specifically address these two subtasks.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper investigates multimodal test-time adaptation (TTA) and introduces a new method, SuMI. Specifically, it extends current multimodal TTA research into a more challenging setting, termed wild multimodal TTA, where test data may include weak or strong out-of-distribution (OOD) contamination. To tackle this problem, the authors propose a technically robust approach involving reliable data selection and cross-modal discrepancy elimination. Extensive experimental results confirm the effectiveness of the proposed method.

### Strengths
Given the prevalence of multimodal data in the real world, studying multimodal test-time adaptation (TTA) methods for pre-trained models is highly relevant, especially in the era of foundation models. Beyond existing multimodal research, such as READ (Yang et al., 2024), the authors extend this work into a more challenging and general setting—wild multimodal TTA. I believe this extension could significantly advance test-time adaptation research within the community.

### Weaknesses
1. Figure 2 needs revision; it’s currently unclear what is being input to the fusion layers. Specifically, it's not clear how the IQR smoothing is applied and what exactly is being passed into the fusion layers. Are the raw features being passed, or are they being transformed in some way before fusion? The diagram should explicitly show the data flow and transformations.
2. Figure 3(c) lacks clear explanations for the X and Y axes. While the caption might contain some information, the figure itself should be self-explanatory. The axes should be labeled directly on the plot, and the meaning of the plotted values should be immediately apparent. For example, are these accuracy scores, loss values, or something else?
3. The settings (weak/strong OOD) should be labeled in Tables 1 and 3. It is difficult to assess the performance of the method without knowing the specific OOD conditions. The tables should clearly indicate whether the results correspond to weak or strong OOD scenarios for each modality.
4. The variable $\mu$ is not found in Equation 4. Did you mean $\gamma_{\mu}$? The equation should be carefully checked for typos and inconsistencies. The role of each variable should be clearly defined.
5. It’s unclear how the proposed method handles cases where certain modalities are missing. From my understanding, if one modality is missing, the correspondence predictions may not be achievable. The method should explicitly state how it handles missing modalities and whether it uses any imputation or other techniques.

### Questions
Please see the weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper mainly focus on the task of test-time adaptation. Different from previous works, the author consider a much tougher circumstance with both weak and strong OOD samples. Performance of existing methods will inevitably degrade for huge distribution gap. To combat with this gap, the authors introduce the interquartile to smooth the sharp gap. Moreover, unimodal entropy is utilized to suggest rich multimodal information. Since strong OOD may contain missing modality problem, the author further a mutual information sharing strategy to complement the distribution. Experiments on several datasets under various domains demonstrate the performance of the proposed method.

### Strengths
1. The paper is written straight-forward, which is easy to follow.
2. The researched TTA problem is a popular problem, while the authors make a further step to discuss under both weak and strong OOD situations.

### Weaknesses
1. While I understand the general framework of the method, certain parts seem to lack clarity. For instance, in section 3.2.1, I can learn that the purpose is to select those samples with lower adaptation gap, however, the ranking process for samples is never introduced. In equation 3, vector $h$ is directly used for comparison, but the comparison method—whether by calculating magnitude, norm, or another metric—is not specified. Definition of IQR also lacks clear clarification. Besides, the motivation part (Figure 3) is suggested to be placed in the Intro section, since it's more vivid and persuasive than experiment results (Figure 1). 
2. My main concern about this work is novelty. The method is mainly composed of three parts: interquartile mainly smooth the distribution gap, unimodal entropy selects samples with high quality, and mutual information sharing combats with missing modality. Every part seems to be orthogonal, with no clear interaction between them. Please explain how separate parts benefit each other in detail, or does every part just simply make their own contribution?
3. While I am mostly ok with the experimental results, I have concern about the setting of the experiment. In my view, missing modality is a more common issue in multimodal circumstances with more than two modalities. Discussing such problem only on simulated datasets with two modalities is somehow narrow. It is suggested for the author to conduct experiments on dataset with more than two modalities.

### Questions
Please refer to cons above.

### Soundness
3

### Presentation
2

### Contribution
2
