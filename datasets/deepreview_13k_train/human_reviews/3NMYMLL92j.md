# Brain encoding models based on binding multiple modalities across audio, language, and vision

- Decision: Reject
- Scores: 3, 8, 1

## Abstract
Multimodal associative learning of sensory stimuli (images, text, audio) has created powerful representations for these modalities that work across a multitude of tasks with simple task heads without even (fine)tuning features on target datasets. Such representations are being increasingly used to study neural activity and understand how our brain responds to such stimuli. While previous work has focused on static images, deep understanding of a video involves not just recognizing the individual objects present in each frame, but also requires a detailed semantic description of their interactions over time and their narrative roles. In this paper, we seek to evaluate whether new multimodally aligned features (like ImageBind) are better than previous ones in explaining fMRI responses to external stimuli, thereby allowing for a better understanding of how the brain and its different areas process external stimuli, converting them into meaningful high-level understanding, and actionable signals. In addition, we explore whether generative AI based modality conversion helps to disentangle the semantic part of the visual stimulus allowing for a more granular localization of such processing in the brain. Towards this end, given a dataset of fMRI responses from subjects watching short video clips, we first generate detailed multi-event video captions. Next, we synthesize audio from these generated text captions using a text-to-speech model. Further, we use a joint embedding across different modalities (audio, text and video) using the recently proposed ImageBind model. We use this joint embedding to train encoding models that predict fMRI brain responses. We infer from our experimental findings and computational results that the visual system's primary goal may revolve around converting visual input into comprehensive semantic scene descriptions. Further, multimodal feature alignment helps obtain richer representations for all modalities (audio, text and video) leading to improved performance compared to unimodal representations across well-known multimodal processing brain regions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper uses multimodally aligned features from visual, auditory and semantic domain to build encoding models to predict fMRI response to silent videos. The paper compares encoding model performances across different single modality models and multimodal models and showed that alignment help with brain prediction.

### Strengths
The paper is presents an interesting idea of leveraging multimodal alignment to probe the multimodal representation in the human brain. The idea itself is relatively novel.

The paper is written clearly.

### Weaknesses
Before jumping onto showing correlations (Fig. 2), it would be useful to show the actual activations both in the networks and in the fMRI signals to better understand how the correlations are computed. Specifically, it would be helpful to visualize the high-dimensional feature vectors extracted from the neural networks and the corresponding fMRI responses in a lower-dimensional space (e.g., using PCA or t-SNE) to get a sense of their structure and relationship before computing correlations. This would allow for a qualitative assessment of whether the network features and fMRI signals exhibit similar patterns.

The basic norms of scientific reporting are not followed here. Axis should be labeled, error bars should be defined. For example, in Figure 2, it is unclear what the x-axis represents in the left panel, and while the right panel labels ROIs, it does not specify the units or scale of the y-axis. Error bars are also missing, making it impossible to assess the statistical significance of the observed differences. It is also unclear how the correlation values are computed (e.g., across voxels, time points, or trials).

It would also be useful to spell out the number of features and training used in each case. Does the order in Fig. 2 reflect the number of features or the amount of training in each modality or the successes of the neural network models in each modality? The lack of clarity on these points makes it difficult to interpret the results. For example, if the video model has significantly more parameters or was trained on a much larger dataset, it could explain the higher correlation values, independent of the actual alignment with brain data.

The features are correlated and therefore it is hard to deduce anything from the fitting analyses. For example, if there is a ball in the image, and the text says ball and the audio says ball, then one can find that language areas can be fit by "visual" features but this does not mean that the language areas represent visual features. Conversely, visual areas can be fit by text, not because visual areas represent text. To understand the relationship between different modalities, we need rigorous controlled experiments that can prove uncorrelated feature dimensions. Unfortunately, this problem is ubiquitous throughout the paper.

There are no comparisons with different baselines, different neural network models, ablation studies. The absence of these comparisons makes it difficult to assess the true contribution of the proposed approach. For example, it is unclear whether the observed correlations are specific to the ImageBind model or whether similar results could be obtained with other models. Furthermore, the lack of ablation studies makes it difficult to determine the relative importance of different components of the model.

### Questions
In Figure 1, I think the colors of the arrow or the order of the modality are flipped.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper evaluates the effectiveness of multimodally aligned features in understanding fMRI brain responses to videos. Using a dataset of fMRI scans from subjects watching videos, the study generates multi-event captions and synthesized audio to create a joint embedding across audio, text, and video. This joint embedding trains models to predict fMRI responses. Key findings indicate that the visual system primarily focuses on converting visual input into semantic descriptions, and multimodal alignment enhances the prediction of brain activity compared to unimodal approaches.

### Strengths
- The authors provides concise interpretability of their model's performance. They relate the outputted embeddings to specific regions of the brain, giving good intuition of how the human responds cognitively to external stimuli. 
- The authors provide sufficient ablation study to identify each modalities affect on performance.

### Weaknesses
Maybe the authors can use another metric (MSE) to quantify the error in the fMRI activity prediction.

### Questions
For future work, have the authors considered using different models for the text, video, and audio encoder to validate whether these findings generalize across different models as well? 
It would also be interesting work to do a canonical correlation analysis to measure the relationship between the generated joint embeddings and the fMRI signals.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors examine whether activations extracted from multimodal neural networks can fit signals derived from functional magnetic resonance imaging (fMRI) measurements obtained while participants watch videos. The paper also explores algorithms that generate captions, convert captions to speech and then use text, audio and video information to try to fit fMRI responses. Mysteriously, the authors conclude that the role of the visual system is to extract semantic informaiton.

### Strengths
The question of studying the similarities and differences between different modalities is important and worth studying. 

It would be very useful for the field to understand how the brain represents visual, auditory, and text information (but this is not studied in the current paper).

### Weaknesses
Before jumping onto showing correlations (Fig. 2), it would be useful to show the actual activations both in the networks and in the fMRI signals to better understand how the correlations are computed. 

The basic norms of scientific reporting are not followed here. Axis should be labeled, error bars should be defined. 

It would also be useful to spell out the number of features and training used in each case. Does the order in Fig. 2 reflect the number of features or the amount of training in each modality or the successes of the neural network models in each modality? 

The features are correlated and therefore it is hard to deduce anything from the fitting analyses. For example, if there is a ball in the image, and the text says ball and the audio says ball, then one can find that language areas can be fit by "visual" features but this does not mean that the language areas represent visual features. Conversely, visual areas can be fit by text, not because visual areas represent text. To understand the relationship between different modalities, we need rigorous controlled experiments that can prove uncorrelated feature dimensions. Unfortunately, this problem is ubiquitous throughout the paper. 

There are no comparisons with different baselines, different neural network models, ablation studies.

### Questions
Are the videos shown with sound? If so, why not use the actual sound and caption from the video? 

What is the point of converting caption to speech? In the best case scenario, the caption to speech is perfect and the information is redundant. In the worst case scenario, the speech is a bad rendering of the caption and merely adds noise. 

It would be useful to conduct experiments where there is only visual information that is dissociated from audio information and from language information, experiments with only language information, etc. Even better, one could run experiments where different modalities are orthogonalized (e.g. show a ball and present the word chair). Once the modalities are rigorously decorrelated, it may be possible to begin to disentangle the contribution of different modalities to brain signals.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
