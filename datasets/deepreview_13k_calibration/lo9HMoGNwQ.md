# Towards Interpretable, Sequential Multiple Instance Learning: An Application to Clinical Imaging

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
This work introduces the Sequential Multiple Instance Learning (SMIL) framework, addressing the challenge of interpreting sequential, variable-length sequences of medical images with a single diagnostic label. Diverging from traditional MIL approaches that treat image sequences as unordered sets, SMIL systematically integrates the sequential nature of clinical imaging. We develop a bidirectional Transformer architecture, BiSMIL, that optimizes for both early and final prediction accuracies through a novel training procedure to balance diagnostic accuracy with operational efficiency. We evaluate BiSMIL on three medical image datasets to demonstrate that it simultaneously achieves state-of-the-art final accuracy and superior performance in early prediction accuracy, requiring 30-50% fewer images for a similar level of performance compared to existing models. Additionally, we introduce SMILU, an interpretable uncertainty metric that outperforms traditional metrics in identifying challenging instances.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the Sequential Multiple Instance Learning (SMIL) framework, which leverages the sequential nature of clinical imaging for improved early and final prediction accuracy. The authors propose a bidirectional Transformer model, BiSMIL, with a novel training procedure to utilize forward and reverse sequences effectively. Validated on multiple medical imaging datasets, BiSMIL outperforms existing methods in both final and early accuracy. Additionally, the SMILU uncertainty metric is introduced, offering sequence-aware uncertainty measures that better identify challenging cases. The work emphasizes the importance of sequence information in clinical imaging, with applications extending to other sequential data fields.

### Strengths
- **Interesting Problem:** The paper addresses a crucial issue in clinical imaging by introducing the SMIL framework, which effectively captures sequential information in diagnostic image analysis.

- **Clear Structure:** The paper is well-organized, with a logical flow that clearly explains the motivation, methodology, and results.

- **Comprehensive Experiments:** Detailed experiments and sequence length analyses demonstrate the model’s robustness and practical utility across multiple datasets.

### Weaknesses
 - **Unclear Clinical Impact:** Although the authors suggest their approach could reduce patient radiation exposure, there is no comprehensive evaluation or discussion on this aspect. This lack of analysis raises questions about the practical clinical value and real-world applicability of the proposed method. The paper does not provide a clear link between the reduction in the number of images required and a direct benefit to patient health, such as reduced radiation exposure. The argument shifts to workflow efficiency for radiologists, which, while important, does not directly address the initial claim of patient benefit.

- **Limited Novelty in Methodology:** The proposed approach appears to mainly involve bidirectional input of subsequences with position encoding, which may not represent a substantial methodological innovation for addressing the ordered subsequence classification problem. The core of the method relies on a standard Transformer architecture with bidirectional processing, and the adaptation to the MIL framework seems incremental rather than a significant leap in methodology. The use of position encoding and bidirectional processing is a well-established technique, and the paper lacks a demonstration of a novel adaptation of these techniques to the specific challenges of sequential medical imaging.

- **Lack of Visualization Analysis:** Given the use of a Transformer model, visualizing attention scores could provide a deeper understanding of the model’s internal mechanisms. This type of analysis would enhance interpretability and offer insights into how the model processes sequential information in clinical imaging data. The paper does not provide any specific visualization of the attention scores, which could reveal which parts of the sequence are most influential in the model's decision-making process. Without this, it is difficult to assess how the model is actually leveraging the sequential information.

- **Overclaimed Interpretability:** The paper claims that the proposed method is interpretable; however, the uncertainty metric primarily supports quality control rather than true interpretability. The results demonstrate the metric's effectiveness in managing prediction quality, but further explanation is needed to clarify how and why the method enhances interpretability. The uncertainty metric, while useful for identifying challenging cases, does not provide insights into the model's reasoning process. The claim of interpretability is not well-supported by the provided analysis, as the uncertainty metric does not explain why the model makes certain predictions.

### Questions
- **Clarify Clinical Impact:** To strengthen the claim of reducing patient radiation exposure, the authors could provide a more detailed evaluation or discussion of this aspect. This might include an analysis of potential radiation savings in a clinical setting or simulations to illustrate practical benefits, thereby enhancing the method's real-world applicability.

- **Enhance Methodological Novelty:** To improve the perceived innovation, the authors could consider incorporating more advanced techniques tailored specifically for sequential classification challenges. Exploring unique modifications to the Transformer architecture, such as dynamic attention mechanisms adapted for clinical imaging sequences, may help distinguish their approach.

- **Add Visualization of Attention Scores:** Visualizing attention scores within the Transformer could provide valuable insights into the model's decision-making process and enhance interpretability. This would allow readers to see how the model weighs different parts of the sequence, helping to clarify the internal mechanics and providing a more comprehensive model analysis.

- **Clarify Interpretability Claims:** To support the interpretability claim, the authors could expand on why the uncertainty metric contributes to understanding the model's predictions. Providing examples or case studies where the metric aids in interpreting challenging cases would be helpful, or discussing how the metric reflects key decision points within the sequence, offering clinicians more insight into the model’s reasoning.

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
4

### Summary
The paper presents a method for sequential multiple instance learning in order to exploit the "sequential structure" of medical images. The proposed method uses a bidirectional transformer architecture to analyse these images, and outputs a sequence-aware uncertainty metric to indicate the certainty of the predictions. The proposed method is evaluated on one ultrasound and two CT datasets, and compared with three alternative baselines.

### Strengths
* Multiple instance learning is an interesting approach to the analysis of image sequence, and the proposal to do this with a sequence-aware method is a nice addition to the existing work.
* The uncertainty metric is a nice addition.
* The paper clearly describes the algorithm.

### Weaknesses
While the method might be interesting from a MIL perspective, I find it difficult to map this to a clinical use case. The assumptions behind the proposed model are not always clear, and the paper does not motivate how the sequential component of the method would work in practice.

1. The Introduction is fairly vague on what the "sequence" actually means: "each image study often contains multiple number of image instances". Does this mean a longitudinal study, or a single visit with multiple images? The context and practical application of the method remain unclear until the experiments. It is not clear if the method is intended to handle temporal sequences (e.g., multiple scans of the same patient over time) or spatial sequences (e.g., a series of slices in a single CT scan). The lack of clarity on the nature of the sequence makes it difficult to assess the clinical relevance of the proposed approach.

2. The vague definition of a "sequence" makes it difficult to determine why the sequential structure would be better than a simple bag-of-instances approach. For the ultrasound: what does it mean for an instance to be earlier or later in the sequence? How were these scans obtained? Is there a given order in which these scans are usually made? Without a clear understanding of the acquisition protocol and the anatomical context of the ultrasound images, it is hard to justify the use of a sequence-aware method. The paper should clarify if the sequence represents a specific scanning direction or a temporal order of acquisitions.

3. The arguments seem somewhat contradictory: on the one hand the paper claims that the sequence is important (we should use a sequence-aware method), but on the other hand the paper claims that we need a bidirectional method "to be robust to sequence reversals". For a CT scan, if it doesn't matter if we look from top-to-bottom or bottom-to-top, doesn't this suggest the sequence might be less important? The justification for bidirectionality seems to undermine the importance of the sequence itself. If the model is designed to be invariant to the order of slices, the sequential information might not be as crucial as claimed.

4. How does the subsequence approach work for CT scans? Isn't this very dependent on where the object of interest (i.e., the brain hemorrhage or pulmonary condition) appears in the scan? I don't really follow how the incremental prediction and uncertainty make sense here. If you only look at the subsequence without the object of interest, you'll find a completely different label. The paper does not explain how the model handles cases where the pathology is only present in a specific region of the scan. The incremental prediction and uncertainty metrics are not clearly defined in the context of these varying pathological locations.

5. The paper suggests that the method can be used to "terminate the imaging sequence" in order to "improve clinical efficiency and reduce radiation exposure". How would this work in practice? I might see how this could work for ultrasound (but this could be explained better: what does the "sequence" mean here? do the results depend on this order?), but for CT I find this a difficult claim. Usually, we make a single scan that collects all slices at the same time: you don't scan a few slices, analyse those, then "decide to stop or continue scanning". The paper does not provide a realistic scenario for how the proposed method could be integrated into a clinical workflow. The claim of reducing radiation exposure is particularly questionable for CT scans, as the entire volume is typically acquired in a single pass.

Finally, the results are not compared with non-MIL methods for these datasets. Is the performance somewhat competitive? Do we really need a complex transformer for these tasks, or could we simply use a 3D convolutional network to classify these CT scans?

### Questions
Suggestions:

* Title/Text

  The title and parts of the paper refer to "clinical imaging". Isn't "medical imaging" a more commonly used term?

* Page #2 (Introduction):

  > is able to better capture difficult-toclassify, uncertain instances better

  Grammar: better ... better

* Page #3 (Sequential Multiple Instance Learning):

  > To further illustrate this concept, in Figure 2, we showcase the incremental prediction results

  I think this is supposed to refer to Figure 1? (See also the other references to Figure 2 in this section.)

* Page #4 (The BiSMIL Model and Training Process):

  > This is because scanning direction is usually a preference based on a particular clinician, and therefore we design our model to be robust to sequence reversals.

  What does this mean? Does this mean that the sequence of images might be presented in the reverse order, and that therefore the model should be direction invariant? If that is the case, can we trust the relative position of the scans, or is this also based on the clinician's preference?

* Page #6 (Dispersion and Sequence-Based Uncertainty):

  > Intuitively, if a sequence's incremental predictions quickly converge to 0 or 1, the model is more certain about that sequence. Conversely, if the predictions fluctuate significantly, the model is likely to be less certain about the predictions.

  I don't fully understand how this works with the bidirectional approach. Does this mean that if a sequence "converges" to 1, the same sequence in the reverse direction would converge to 0?

* Page #7 (Experiments):

  > For all of our experiments, we designated 70% of the data for training

  What does "the data" mean here? Samples? Scans? Images? Slices? Patients? I assume this is patients, but it would be good to make this more explicit.

  (If the data is not split on the patient level, this is something that would have to be fixed.)

* Page #7 (Experiments):
> UTD Classification Dataset

What is the nature of the sequence in these ultrasound scans? How are these scans generally made? What does it mean for an image to be early or late in the sequence?

* Page #7 (Experiments):

  > 50,862 brain CT slices

  What is the "sequence" for CT scans? Considering each "slice" as a separate step in the sequence would not make sense for me: the number of slices in a scan is determined before the scan is made, so the slice-by-slice MIL approach seems weird. I also find it difficult to see how this would work: would you order the slices from top to bottom, or would they appear in a random order in the sequence? If the order is sequential top-to-bottom, the ideal point to stop scanning would be the point where you first observe the hemorrhage, but how would that be done in practice?

* Page #8 (Final Prediction Accuracy):

  > which suggests that bidirectionality provides extra information that can improve the effectiveness of the model.

  In CT scans, this would mean that the slice direction is reversed. Does this cover a practical use case? Isn't the scanning direction usually given in the DICOM headers of the scan? (Or trivially determined from the image if this is not given?)

* Page #8 (Subsequence Prediction Accuracy):

  > To further understand the performance of our BiSMIL model, we compare the accuracy of the BiSMIL model against the three comparison models when only a subsequence of instances are revealed.

  How does this experiment work? Is this a random subset of the instances? How would this work in practice? (E.g., how do you make a random subset of CT slices?) Or is this a regular subsampling of the sequence, e.g., by taking every nth slice?

### Soundness
3

### Presentation
3

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
The paper proposes a Sequential Multiple-Instance Learning (SMIL) method, employing a bi-directional Transformer architecture to capture information in both forward and backward directions. Additionally, a sequence-aware uncertainty metric, SMILU, is introduced to quantify the uncertainty in model predictions.

### Strengths
At a high level, the paper addresses an important question: how to enhance clinical efficiency in capturing patient images.

### Weaknesses
1. Motivation of the study:

1.1 The paper justifies the development of SMIL by stating, "In many clinical imaging settings, clinicians create images sequentially to discover features of interest and often have control over the number of sequential images captured." However, it would strengthen the motivation if a specific clinical setting were described to show where this statement holds true and where the proposed method could be beneficial, since for many clinical protocols are predefined, with standardized imaging procedures. Applying the proposed method in such settings could be challenging, as it would require modifications to existing protocols. The paper needs to clarify the specific clinical scenarios where clinicians actively adjust the number of images based on real-time observations, as opposed to adhering to fixed protocols. Without such clarification, the practical applicability of the method remains unclear.

1.2. Similar to above, the paper motivate the value of the proposed method by saying "as the clinician creates more images, the resulting diagnostic accuracy is likely to increase, but it comes at the expense of efficiency and patient radiation exposure." However, not all medical imaging modalities, such as ultrasound, involve radiation exposure. Moreover, it would be valuable to clarify the potential practical efficiency gains that reduce only a few images brings. The paper should quantify the trade-off between the number of images acquired and the diagnostic accuracy, especially in modalities without radiation exposure. A more detailed analysis of the potential time savings and cost reduction would be beneficial to justify the practical value of the proposed method.

2. Method Novelty

The use of a bidirectional architecture for modeling sequence data is a well-established technique. For example, bi-directional models, such as Bi-LSTMs, have long been employed in various contexts to model sequential information. The paper lacks a clear explanation of how the proposed bidirectional Transformer architecture offers a significant advantage over existing sequence modeling techniques like Bi-LSTMs or other attention-based models in the context of multiple instance learning. A more detailed comparison with these existing methods, highlighting the specific benefits of the proposed approach, is needed to establish the novelty of the method.

3. The model is not really doing ``incremental'' prediction. In the inference setting, when the clinician collected a sequence m_1 = {x_1, ..., x_n}, the model generates a prediction p1, when the clinician capture one more image m_2 = {x_1, .., x_n, x_(n+1)}, the model basically treat this as brand new sequence and evaluate again to generate p2. This procedure can be applied with other Multiple-Instance Learning (MIL) methods as well. The paper needs to clarify how the proposed method leverages the sequential information during the inference stage to provide a genuinely incremental prediction, rather than simply re-evaluating the entire sequence each time a new instance is added. The distinction between the proposed approach and simply applying other MIL methods to an extended sequence needs to be more clearly defined.

### Questions
1. It is fine that the author try to relax the classic MIL assumption to incorporate sequence information in real clinical practice. However, it is unclear what specific sequential information the proposed model aims to capture, particularly as the authors also noted that sequence order can sometimes depend on the clinician’s or operator’s preference.

2. In line 194 "the Gaussian embedding is designed to encourage robustness in the reverse sequence". Can you elaborate on this? How does the Gaussian position encoding encourage robustness in the reverse sequence? What about for the forward sequence?

3. It is unclear how the model would inform clinicians about the optimal stopping point for image collection. Given a full sequence (like those experiments in the paper), we can determine the ideal stopping point, but in a real-world setting, where an additional image has not yet been collected, we do not know if additional image would contribute valuable information.

4. As the author noted, training on subsequences with the label of the full sequence may introduce noise. To address this, they use a heuristic that assigns lower weights to shorter subsequences. However, this may still introduce noise. It is unclear how effectively this approach reduces noise, and it would be helpful to understand if this training objective (e.g., removing the second part in line 244) significantly improves model performance.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a method for medical image classification, BiSMIL, which adopts a sequential multiple instance learning (MIL) framework that considers the “order” of instances. The proposed method outperforms other MIL baselines on three medical imaging benchmark datasets, and the authors put forth an uncertainty metric that assesses variability in instance-wise predictions.

### Strengths
- The organization and layout of the paper is mostly sound.
- Experiments demonstrate strong performance over multiple datasets and baselines.
- The formulation of CT and ultrasound image analysis as a sequential MIL problem is unique to me.

### Weaknesses
 - The setting and motivation for adopting a “sequential” framework to medical image analysis is completely unclear. Every imaging modality and use case is different, so I do not know what the authors mean by phrases like “the sequential nature of clinical imaging.” Provide a concrete example (perhaps with a figure) of a medical imaging use case that is sequential purely for illustration purposes. It is unclear whether this refers to longitudinal imaging (multiple images acquired over potentially years or months to track disease progression), medical videos (multiple images over a short time period forming a video), or something else.
- The authors do not convey understanding of the application domain. I don’t follow why “CT scan levels” are any more or less “ordered” than image patches of a large histopathology slide. Justify this dichotomy that the authors set up. Comments such as “clinicians are creating the images sequentially” and “scanning direction is usually a preference based on a particular clinician” display a misunderstanding of clinical workflows; it is not usually accurate to say that clinicians are “creating” images, and I am not aware of a medical image interpretation use case where a clinician will assess a “sequence” of images in the forward and reverse direction. The claim that clinicians acquire images sequentially to discover features of interest is not supported by typical clinical practice.
- Description of datasets used is insufficient and causes further confusion, where it could be used to clarify the above points. E.g., it is unclear whether the ultrasound dataset is image- or video-based; whether the “sequence” is formed from multiple images/videos in the same study vs. multiple studies from the same patient; etc. See specific questions below.
- If I am understanding the datasets correctly (which I am not sure that I am), then I fail to see why only a select few MIL methods are used as comparative baselines. If the authors are performing classification from 3D CT volumes, there are a wealth of methods for volumetric medical image analysis to pull from beyond MIL approaches. The authors should justify why methods such as 3D convolutional neural networks are not suitable for this task, given that the input data is inherently 3D.

### Questions
- What do the authors mean by “clinicians are creating the images sequentially to discover features of interest”? Sequentially over *time*? What time-scale (e.g., frames in a video or scans captured over many years)? Perhaps a figure visualizing one example use case could clarify this.
- In what sense are “CT scan levels” and “ultrasound” sequential? In what sense does order of “instances” (however you define this) matter? Expand on this. This is not a perspective I am familiar with, so it warrants further explanation.
- Provide more details about the nature of the datasets used. Does the UTD dataset consist of ultrasound images or videos? What exactly is the “sequence” in this setting: frames in a video? videos from different “views” in a study? different studies over a patient’s longer-term trajectory? For CT datasets, do the individual 2D slices in the 3D volume form the “sequence”?

**Minor comments/questions:**
- Ideally, provide citations or examples of the “surge of availability of imaging”
- I would merge the first two paragraphs – awkward that the first paragraph is two sentences.
- Awkward wording: “each image study often contains multiple number of image instances” -> “Each medical imaging study often contains multiple image acquisitions (“instances”) perhaps
- “clinicians are creating the images sequentially”. I would not say clinicians are “creating” images (perhaps “acquiring”?), and I do not know what is meant by “sequentially” – there are many ways to interpret this word. 
- Change “patient radiation exposure” -> “, in some cases, patient radiation exposure”. One of the examples given, ultrasound, does not use ionizing radiation
- What is being predicted in Figure 1? Mention briefly in the caption.
- The definition of “sequence” is unclear to me in the context of ultrasound, but let’s presume the authors are considering a sequence to be each of a standard few views that are acquired in a recommended/standard order. Why does this order matter for diagnosis? I am not aware that it does. In applications of ultrasound such as echocardiography, views may be acquired in a recommended order, but the analysis of views simply depends on the task being performed and does not depend on order – often only one or two views are relevant for a particular task.
- For the CT datasets, do I understand correctly that the authors are considering a “sequence” of 2D slices in the 3D volume? If so, why not compare to standard 3D medical image analysis methods?
- What statistical test is performed to compare model performance?

### Soundness
2

### Presentation
2

### Contribution
1
