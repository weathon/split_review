# Cognition-Supervised Learning: Contrasting EEG Signals and Visual Stimuli For Saliency Detection

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
In the rapidly evolving landscape of machine learning, the quest for efficient and accurate supervision signals remains paramount. Suitable supervision signals can be costly and practically impossible to obtain for models that require subjective cognitive labels, such as individual-specific interpretation of images or subjective training input for generative models. In this paper, we introduce a novel paradigm: cognition-supervised learning, leveraging human brain signals as direct supervisory signals. Using electroencephalogram (EEG) data, we contrastively train models to detect visual saliency without the need for any manual annotations. Our approach, the first of its kind, demonstrates that representations of semantic visual saliencies can be learned directly from EEG data. In downstream tasks, such as classification, clustering, and image generation, our learned representations not only reflect semantic saliency but also achieve competitive performance compared to models trained with manually labeled datasets. This work provides a promising avenue for future research in utilizing signals measured from the human cognitive system for supervising computer vision and machine learning models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The proposed approach for self-supervised machine learning, which involves using human brain signals as direct supervisory signals, raises questions. The authors suggest a paradigm of cognition-supervised learning achieved through leveraging EEG data to receive solid binary labels. However, using BCI-style responses for such self-supervised learning could be more ethically questionable and logically messy, as it depends on human involvement and may not have practical applications. Moreover, the study assumes involuntary or automatic human responses, which raises ethical concerns.

---
POST-AUTHOR FEEDBACK: 
---
In response to helpful feedback, the reviewer upgraded their decision, however, the manuscript remains unsuitable for publication due to unresolved ethical concerns and questionable self-supervision application.

### Strengths
It is quite challenging to identify any strengths in the manuscript. The claims of self-supervision using "hard P300" labels provided by humans who were forced to label pictures in visually tiring conditions (all BCI P300-style experiments are actually exhausting) are not well-explained and validated. It is difficult to identify the novelty of the model, and the final results are not impressive.

### Weaknesses
It is quite challenging to identify any strengths in the manuscript. The claims of self-supervision using "hard P300" labels provided by humans who were forced to label pictures in visually tiring conditions (all BCI P300-style experiments are actually exhausting) are not well-explained and validated. It is difficult to identify the novelty of the model, and the final results are not impressive.

It is not clear how the concept adheres to the self-supervision philosophy, as efficient labels like those of P300 are actually human-generated labels. Self-supervised learning is typically considered a form of unsupervised learning where the model generates its own labels or annotations from the input data, without the need for external human-labeled data. This involves creating a pretext or auxiliary task that does not require human annotations. The model is trained to predict some aspect of the input data based on other parts of the same data. However, P300 responses use human-generated labels in an ethically questionable setup.

### Questions
The standard 10-20 EEG electrode placement system consists of 21 electrodes. However, in this case, 32 electrodes were used. I am curious about the placement of these additional electrodes on the head and the reason for using 32 instead of the usual single Pz electrode. Moreover, I am concerned about the ethical implications of violating the Declaration of Helsinki by misusing human subjects.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents cognition-supervised learning using EEG data to contrastively train models for visual saliency without manual annotations, which generates competitive performance on subsequent tasks and opens the way for future research on human cognitive system-guided supervision. for computer vision and machine learning.

### Strengths
The paper introduces a original and innovative concept, "cognition-supervised learning," which leverages human brain signals (EEG data) as direct supervisory signals for training machine learning models.

The paper explores the concept of cognition-supervised learning and provides a well-structured experimental framework to validate its effectiveness.

The paper is well written and clearly communicates its key ideas, methodology, and results. The introduction clearly states the context and motivation for the research, and the research questions are clearly described.

The contribution with an open EEG dataset in this paper is a great contribution, as it not only encourages transparency and reproducibility, but also promotes collaboration and facilitates further exploration of cognition-supervised learning, encouraging growth and progress of the research field.

The paper provides a detailed description of the dataset used, along with a detailed explanation of the processing of the data involved in the study. This strengthens the methodological quality of the research.

The paper maintain a level of quality in its experiments. The use of well-established techniques like unsupervised clustering and linear classifiers ensures the reliability of the evaluation. In addition, the incorporation of a qualitative evaluation using generative adversarial networks adds a layer of quality.

To sum up, the use of EEG data for supervision in machine learning is a novel and interesting direction that could have positive implications for the field.

### Weaknesses
The paper discusses results in the context of facial images, but it is not clear how well the proposed approach generalizes to other types of images or domains. It would be important to conduct experiments with a larger range of datasets, including natural images with varying complexity and content, to demonstrate the robustness of the cognition-supervised learning approach. The current focus on artificial facial images limits the assessment of the model's ability to capture more generalizable visual saliency patterns.

The paper mentions that it opens avenues for human-in-the-loop systems, but it would be valuable to provide insights into potential future research directions and how this work could be extended and applied in various domains. For instance, the paper could discuss the challenges and potential solutions for applying this approach to other modalities such as audio or text, or how the learned representations could be used in downstream tasks beyond visual saliency, such as image captioning or visual question answering.

In section 3.1 the authors mention that "The images were manually screened to ensure realism and the absence of visual artifacts", but I think a little more detail should be given regarding this. For example, what specific criteria were used to define 'realism' and 'visual artifacts'? What was the inter-rater reliability between the researchers involved in the screening process? Providing such details would strengthen the methodological rigor of the paper.

At the beginning of section 3.2, it would be desirable for authors to include relevant references to support these claims, thus facilitating a deeper exploration of their claims in the article. Specifically, claims about the effectiveness of the EEG preprocessing steps and the rationale behind the chosen frequency bands should be supported by prior work in the field.

In section 4.2, it would be good for the authors to compare the results with more control models (e.g. EEGNet Fusion, MI-EEGNet, etc.) in order to have stronger results. Furthermore, the difference between EEGNet and contrastive embedding (Mean column) is very small (0.699 ± 0.037 vs 0.704 ± 0.046), which even falls within the standard deviation. This raises concerns about the practical significance of the proposed method's performance gain over existing baselines.

As mentioned in the limitations, the present work only applies to two classes; it would be of great interest to expand it to more classes, since many problems are of this nature. The current binary classification setup limits the applicability of the method to more complex, real-world scenarios where multiple categories or continuous variables are involved.

### Questions
Do the authors believe that the present work could be expanded to more classes and not just two?

Do the authors plan to expand the work with other types of images or in another domain (e.g. NLP)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper propose an interesting idea called "cognition-supervised learning". The method uses EEG signals as direct supervisory information. The approach uses EEG to contrastively train models to detect visual saliency without the need for manual annotations. The paper then applies the learned representations for several downstream tasks (classification, clustering, and image generation) showing competitive performance compared to models trained with manually labeled datasets.

### Strengths
The paper provides a promising new direction for research where brain signals such as EEG can be utilized directly for supervising deep learning models. The paper is well-written.

### Weaknesses
I ask the authors to respond to the following weaknesses/questions:

- There has been prior works on image reconstruction from EEG, e.g.
"NeuroGAN: image reconstruction from EEG signals via an attention-based GAN"
"EEG2IMAGE: Image Reconstruction from EEG Brain Signals"
"Photorealistic Reconstruction of Visual Texture From EEG Signals"
"Visual Saliency and Image Reconstruction from EEG Signals via an Effective Geometric Deep Network-Based Generative Adversarial Network", and others.
Given that the proposed paper seems to perform the opposite direction of these works, they could be discussed. Moreover, simple reverse versions of these can be developed to use as baselines.

- It would be valuable to see the impact of the CLIP loss by exploring and comparing other ones as well.

- There's a small error in Fig 1, "Find-tuning" --> Fine-tuning

- While the RQs are very interesting, I wonder whether the outcome is completely expected. Given that we can map EEG to certain classes/actions/objects (e.g., affect classes, objects, directions, etc.), doesn't the outcome become expected? In other words, the method is mapping two high-dimensional data points onto a common lower dimensional feature space, where the locality of the image embeddings is used as the supervisory signal. Can the authors please (a) provide a discussion on this, (b) show the common embedding space (using tSNE, UMAP, etc) to extract some more insights about the reason behind why the method works. In general, I found the "analysis" part of the paper a bit weak. Further experiments to analyze the method, its components, and embedding space, are recommended.

### Questions
Please see my comments under weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper uses contrastive learning for decoding EEG signals. The visual stimuli are annotations, the brain responses are the data, and both are matched using a contrastive loss instead of a classical supervised loss (e.g. least-squares). The authors empirically show that the learned representations cluster around annotation features (e.g. "young" or "old").

### Strengths
The paper applies contrastive learning to EEG signals and demonstrates evidence that the learned representations cluster around interesting features, including age group.

### Weaknesses
The writing style is at times over-emphatic compared to the actual contributions. For example, the abstract sets up the contribution as something completely novel and major ("remains paramount", "practically impossible", "novel paradigm", "the first of its kind"). However, in my understanding, this paper applies the existing framework of supervised contrastive learning [1] to EEG signals. Many relevant works are not cited: for example, consider [2] which also uses contrastive learning to learn representations from EEG signals and also demonstrates that the representations cluster following age group and other features.

Mapping the brain response to the stimulus is called "decoding" in the neuroscience literature [3]: it would be worth using this terminology. 

Some citations could be added to support strong statements that begin a paragraph, e.g. "as human is known to respond strongly to facial stimuli" (missing citation) or "leverages a fundamental observation that the human brain response to differences in perception" (missing citation).

Some technical terms (e.g. "visual saliency" and "semantic saliency" in the abstract, "epochs" in the preprocessing paragraph) are used without being defined. Other terms ("target and non-target epochs") are also vague and undefined. 

The evaluation procedure appears to be biased by design. The "clusterability" of learned representations around annotation features (e.g. young and old) is used to evaluate the learning procedure. However, a contrastive loss performs clustering by design [1], so that "positive" pairs (stimulus and corresponding brain response) are given "close" embeddings, and "negative" pairs (stimulus and random brain response) are given "far" embeddings. Therefore, Table 3 and Figure 3 are not surprising. The authors should clarify how their results are not simply a consequence of the contrastive loss.

Some details are missing in the data preprocessing. For example, when "including a band-pass filter", the authors should specify the frequency-range in the main text.

### Questions
It might seem that the evaluation procedure is biased by design. For example, the "clusterability" of the learned representations around annotation features (e.g. young and old) is used to evaluate the learning procedure. Yet it is known that a contrastive loss performs clustering by design [1], so that "positive" pairs (here, a stimulus and corresponding brain response) are given "close" embeddings, and "negative" pairs (here, a stimulus and random brain response) are given "far" embeddings. So Table 3 and Figure 3 are entirely expected. Could the authors comment on that? 

Some details are missing in the data preprocessing. For example, when "including a band-pass filter", could the authors specify the frequency-range in the main text?

[1] Wang et al. Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere. ICML, 2020.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
