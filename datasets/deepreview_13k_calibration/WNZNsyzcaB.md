# Enhancing Deception Detection with Cognitive Load Features: An Audio-Visual Approach

- Decision: Reject
- Avg Score: 6.75
- Scores: 8, 5, 8, 6

## Abstract
Deception ranges from minor mischief to serious fraud, often leading to significant psychological and financial harm. Effective deception detection is crucial to mitigate these risks and preserve societal trust. Cognitive load is a useful indicator for detecting deception, as lying causes individuals to experience greater mental strain. While prior research leveraged cognitive load features, typically measured through physiological signals such as pupil dilation, these methods often require specialized equipment and can be subject to human bias. These limitations hinder the scalability and automation of deception detection systems. Thus, we propose a novel deception detection framework that automatically extracts cognitive load features from audio-visual data, eliminating the need for specialized hardware or subjective human input. Our approach integrates these features into the deception detection pipeline, enhancing its robustness. Moreover, we introduce a focal loss to address the inherent complexity of deception detection. This objective function enables the model to focus on harder-to-detect instances of deception, thereby improving the performance. Our approach achieves state-of-the-art results on benchmark audio-visual datasets, demonstrating significant improvements in automated deception detection. Extensive experiments validate the effectiveness of both our cognitive load feature extraction and the proposed objective function in advancing the field.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper explores the task of deception detection using audio visual modalities. The authors propose that deception requires significantly different cognitive strain or load and hence nudging a prediction network in that direction can lead to a better performance. The authors describe an architecture based on recent feature extractors for a similar task and conduct various experiments to describe the effectiveness of their approach.

### Strengths
1. The paper proposes the use of cognitive load or TLX-based features as an intermediary subtask and the framework in itself and the idea is quite novel
2. The paper is well structured and the core architecture is easy to understand
3. The authors provide a lot of details about their implementation to help reporducibility

### Weaknesses
While the paper aims at solving a novel problem and definitely brings in a unique perspective, here are some aspects which need to be answered further:
1. If focal loss is shown as a key contribution, it is not well explored in writing and experimentation. Focal loss is widely popular and is often among the standard practices for handling imbalanced data. Claims of introducing it as a new loss function might need to be softened. Even the experiments pre-set the loss param at 2 and no justification or experiments are shown towards why that was chosen or insights on the use of the loss function is missing.
2. Related work doesn't describe the gaps effectively. For example line 137, "... no existing research has explored the automatic extraction of cognitive load indicators through multimodal features." This is not true since AVCaffe (the dataset used) itself does this. Also it doesn't point to the gap that the current work is trying to address which is more towards the use of cognitive load to inspire deception detection
3. The motivation behind using AVPEF as feature extractors for TLX states' estimation is unclear. While it worked well for the overall task of deception detection why might it do well for detecting cognitive load states?
4. Given that the dataset is imbalanced the authors should clarify if all metrics are balanced for the same (e.g. macro F1, balanced accuracy) or justify their choice of metric
5. Since related work does not directly quantify how cognitive load and deception are related, showing correlations/associations even between predicted values of TLX subscales and deception as a small experiment will help strengthen the impact of the framework for future researchers

### Questions
1. Why as AVPEF chosen to be the feature extractor? How does it compare against other popular feature extraction models?
2. Why was all the training/analysis done on DOLOS when RLT and BOL datasets also exist? They only appear in the draft under Section 4.5 and given how Guo et. al. performs on generalization of the two, they might be very differently distributed and incorporating that in training might in fact make the model more robust.

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
This paper presents a multimodal modeling approach for deception detection with a specific focus on measuring cognitive load.  The authors present experiments on several datasets.  The authors propose a feature extraction step (AVPEF) that is specifically focused on extracting cognitive load features. The network is pertaining on the AVCAffe dataset. The results are modest but generally show an improvement over the reported baselines.

### Strengths
Overall the paper is fairly clearly written and contains most (but not all) of the necessary details required to replicate the work.  The approach appears to have novelty and the experimental results that are reported (I will discuss below that I think these could be expanded) are reasonable.  The work is motivated and the authors do report some results across three different datasets.

### Weaknesses
There are a few areas in which there are important details missing.  For example in the cognitive load feature pre-training section there is only limited details about the pretaining step - which videos were present in the set used (as I understand it some of the videos may no longer be available) how were these preprocessed? Etc. 

Why are the evaluation metrics not consistently reported. For example,  in Table 2 accuracy, F1-score and area under the curve are reported but in Table 3 only accuracy is shown (side note: it isn’t actually described in the Table caption or column heading what the metric is - this is a bit sloppy).  
Overall, the experiments are a bit fractured, in some cases there are within dataset experiments and in others across dataset experiments.  I think that the experiments could easily be more comprehensive and in their current state it might lead readers to be concerned that there is some cherry-picking of good results going on.  

In Section 4.6.1 it isn’t very clear which dataset these results are reported on.  Again, the attention to detail in the paper is not very high and there could be a better description.

Reporting accuracy numbers to four significant figures is a little unnecessary to me as it suggests at we can trust the numbers to that level of precision.  I would limit to 3 significant figures. 

Fig 3. Is very hard to reach.  The font is far too small to be legible.  The caption does not describe what projection is used and the reader needs to go to the text to find out that these are t-SNE plots.

There are baselines for the experiments; however, they are quite limited.  I am not sure why the authors do not comment on other performance numbers: e.g. Camara, M. K., Postal, A., Maul, T. H., & Paetzold, G. H. (2024). Can lies be faked? Comparing low-stakes and high-stakes deception video datasets from a Machine Learning perspective. Expert Systems with Applications, 249, 123684.
If the reason for this is that the authors do not do cross-fold/within subjects experiments on that dataset then I don’t think that is a good reason, it would be better if they were to match those experiments rather than exclude them.

### Questions
See above.

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
5

### Summary
The paper proposes  a novel framework called AVDDCL (Audio-Visual Deception Detection via Cognitive Load). The authors address the challenges of automated deception detection by leveraging cognitive load features extracted from audio-visual data, which eliminates the need for specialized hardware and human annotations.
The key contributions of the paper include:
Novel Framework: The introduction of an automated, scalable deception detection system that incorporates cognitive load features from audio-visual data, enhancing its applicability in real-world scenarios.
Focal Loss Implementation: The use of focal loss to improve the model’s ability to detect difficult instances of deception by emphasizing harder-to-classify cases.
State-of-the-Art Performance: Achieving good results on the DOLOS dataset, demonstrating that integrating cognitive load features also boosts accuracy and robustness in deception detection.

### Strengths
1. The paper presents a novel approach to deception detection by integrating cognitive load features from audio-visual data, which sets it apart from traditional methods that rely heavily on physiological signals or manual annotations. This innovation eliminates the need for specialized equipment and subjective inputs, enhancing scalability and practical applicability.
2. The use of focal loss to emphasize harder-to-classify deception cases is a creative adaptation in this context. This approach effectively prioritizes difficult samples, which is critical in the nuanced domain of deception detection
3. The integration of cognitive load into a unified audio-visual framework is an inventive step, providing a more holistic understanding of deception. This combination of existing modalities with cognitive indicators represents a novel application that enhances the accuracy and robustness of deception detection.
4. The paper addresses a problem in deception detection, with potential applications in security, law enforcement, border control, and various other domains. The automated extraction of cognitive load features from audio-visual data can significantly improve the deployment of deception detection systems in real-world settings, where human bias and the requirement for specialized equipment are limiting factors.
5. The model's ability to generalize across both high-stakes and low-stakes deception datasets highlights its versatility, making it a significant contribution to both the research community and industry practitioners focused on automated behavioral analysis.
6. The paper is well-organized, with clear sections detailing the problem, related work, methodology, experiments, and results. The structure allows readers to easily follow the progression of ideas and understand the novelty of the approach.
7. The mathematical formulations are well explained in the paper, aiding in comprehensibility for readers familiar with deep learning frameworks.

### Weaknesses
1. Although the paper claims that the model improves scalability by not requiring specialized equipment, the potential limitations in computational cost are not thoroughly addressed. The use of pre-trained models like Wav2Vec2 and Vision Transformers can be computationally expensive, which may hinder real-time deployment in resource-constrained environments. A brief discussion of computational efficiency, inference speed, and potential trade-offs in real-world applications would provide more actionable insights for practitioners.

2. The ethical implications of deploying a system like AVDDCL in real-world settings (e.g., law enforcement, job interviews) are not discussed. The potential for false positives in high-stakes scenarios (e.g., misidentifying truthful individuals as deceptive) could have serious consequences. Addressing these implications, perhaps by suggesting future work in explainability or bias mitigation, would make the contribution more responsible and practical.

### Questions
1. Adding details on the selection of the focal loss parameter 𝛾 would improve transparency. Including experiments with different 
𝛾 values might also show the sensitivity of AVDDCL to this parameter, thus strengthening the reproducibility of the results.
2. If real-time deployment is a goal, conducting tests or simulations on inference speed and latency would validate the model’s practical usability in settings like live surveillance or border security.

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
4

### Summary
This paper propose a framework to automatically extracting cognitive load from audio-visual data, and integrates them into a deception deception pipeline to enchance its robustness.

### Strengths
- Novel idea of pretraining of model on AVCAffe dataset to extract cognitive load features in order to support downstream deception detection task.  
- Novel Audio-Visual Parameter-Efficient Fusion network (AVPEF) and training loss used. An innovative network architecture was proposed to fuse both audio and visual modality with parameter efficient finetuing. The use of focal loss to put emphasis on difficult samples.

### Weaknesses
 - There is insufficient evidence to show that AVPEF is useful. Results from Table 1 suggest that other architectures outperforms the proposed AVPEF. Also, the lack of comparison against other multimodal learning fusion methods makes it difficult to determine the effectiveness of AVPEF. 
- There is a lack of considerations on ethics and bias. More exploration into the biases of their model issues will make this study more comphresive and as well as to ensure responsible deployment of such models.

### Questions
- **line 295** Wrong citation of DOLOS dataset.
- Addressing the concerns stated in the weakness.

### Soundness
3

### Presentation
3

### Contribution
3
