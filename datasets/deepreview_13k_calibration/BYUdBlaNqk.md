# System Identification of Neural Systems: Going Beyond Images to Modelling Dynamics

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 3, 5, 8

## Abstract
Vast literature has compared the recordings of biological neurons in the brain to deep neural networks. The ultimate goal is either reporting insights to interpret deep networks or to have a better understanding and encoding of biological neural systems. Recently, there has been a debate on whether system identification is possible and how much it can tell us about the brain computation. System identification recognizes whether one model is more valid to represent the brain computation over another. Nonetheless, previous work did not consider the time aspect and how video and dynamics (e.g., motion) modelling in deep networks compare to these biological neural systems. Towards this end, we propose a system identification study focused on comparing single image versus video understanding models with respect to the visual cortex recordings. Our study encompasses two sets of experiments; a real environment setup (i.e., regressing on the output of the visual cortex in the human brain recorded as fMRI responses) and a simulated environment setup (i.e., regressing on another network architecture representations that we know its modelling scheme). This study encompasses more than 30 models and, unlike prior works, we focus on convolutional versus transformer-based, single versus two-stream, and fully versus self-supervised video understanding models. The goal is to capture a greater variety of architectures that model dynamics. As such, this signifies the first large-scale study of video understanding models from a neuroscience perspective. Our results in the simulated experiments, show that system identification can be attained to a certain level. Moreover, we present the results of the real experiments and provide key insights on how dynamics modelling in deep networks compare to the human visual cortex.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors perform a system identification study that focuses on modeling dynamics in perception by investigating multiple video models and comparing them with image models.

This study attempts to answer following research questions:

1. Is it possible to distinguish video models from image models? 
2. Which models better predict human fMRI responses to videos?
    1. Video vs. image models
    2. Convolutional vs. transformers
    3. Fully supervised vs. self-supervised

The authors perform extensive experiments using multiple models on simulated (predict other model’s responses) and real (predict human fMRI responses) to answer these questions.

### Strengths
1. Layer-weighted encoding to compare models. This makes comparison easier removing the steps of layer selection for individual models. 
2. Varieties of models investigated in this study. The authors have carefully chosen a wide variety of models (conv vs. transformers ; self-supervised vs. supervised; image vs. video) using which they are able to answer multiple questions in this paper 
3. Statistical analysis to compare whether one family of model predict better than others.
4. System Identification study(Figure1) investigating whether models from one modality (image/video) can predict the models from same modality better than models from other modality. The result showing that I3D early layers can be predicted equally well suggests I3D does not use temporal information well in early layers

### Weaknesses
1. The authors claim “previous work did not consider the time
aspect and how video and dynamics (e.g., motion) modelling in deep networks
compare to these biological neural systems” . This is incorrect. Several previous works [i-iv] have investigated modeling temporal aspects of videos and comparing it to brain responses. These works have been completely overlooked and not cited. Further seminal works on encoding and neural system identification from  Jack Gallant’s group and Marcel Van Gerven’s group are not cited.
2. Several important details are missing
    1. When comparing convolutional vs. transformer or self-supervised  in Figure 2 b,c ; did you consider both video and image models ?
        1. If yes what was the reasoning, because if video models better predict brain activity doesn’t it make sense to restrict only to video models. If both the video and image models are considered for comparison do you see same pattern for video and image family of models? 
    2. When you compare OmniMAE-B Pretrained/Finetuned what was the task OmniMAE finetuned on and on which dataset (Figure 3b)
3. In Figure 3, it is not clear whether the results are statistically significant or not
4. Some of the results require a deeper dive to gain better understanding of exactly what is happening
    1. In Figure 1a(MViT-B) and 1c (I3D R-50), it can be clearly seen that variance in regression score by video models is quite high compared to image models suggesting some models are better predictor and some are worse. Which ones are worse/best predictors and why? This answer is important to understand how temporal information in video should be modelled. 
    2. Similar variance can be observed in Figure 2a-c as well raising the question why these models  are one family? A simple classification such as transformer vs conv or self-supervised vs supervised is not helpful here when there is so much variance within a family of models. The  conclusion that can be derived here are
        1. From Figure 2a: 3 video models predict brain responses similar to or worse than image models while others predict better. Which are similar to image models and which are better is not answered.
        2. From Figure 2b: some transformer models predict as well as conv models
        3. The above conclusions are quite weak and less helpful and informative for readers without a deeper analysis.
5. Overall, I find paper containing multiple results with unclear findings.

### Questions
Suggestions: 

1.  Please add relevant citations 
2.  Refer to weakness point 2-4 and please address those.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this manuscript the authors use DNNs for videos to predict fMRI responses and other networks in a pretest. As data they use the 2021 Algonauts challenge for predicting responses to 3 second video clips.

### Strengths
It is—in principle—a step in the right direction to include temporal dynamics to better understand biological brains. We should move towards predicting responses to videos, not only images and the authors do that. Also they evaluate a selection of newer model architectures that were not available in 2021 when the Algonauts challenge with videos ran officially.

### Weaknesses
I think the results of this study are underwhelming though for three major reasons:

First, the DNN models are not intended as models of biological vision and do not contain any interpretable dynamics that would enable conclusions about theories. Also, they usually run at so slow timescales (typically the frame rate of the video), that they could never have the temporal dynamics of biological networks in the first place. Thus, it is is not surprising that the conclusions are not particularly clean.

Second, fMRI is not able to resolve dynamics of visual processes. Thus, it cannot provide evidence about these dynamics.

Third, the relationship to the Algonauts challenge remain unclear to me. The challenge website is open for post challenge submissions, so the authors could have submitted their models to the competition to get scores for the official test set. If that was not desirable for some reason, I think we would like to see the results for the top entires of this challenge to get an idea how close to the state of the art the models from this paper perform. Unfortunately, I do not see a substantial step of this manuscript beyond the Algonauts papers.

Thus, this manuscript does not provide the promised insights into dynamics and instead becomes an incremental step repeating things that have been done for image neural networks with video networks without providing substantial new insights.

### Questions
My main question for the authors is: Why this dataset and without the official evaluations? And to convince me of a better view of this work the main ingredient would have to be a substantial insight in how we might capture the dynamics of human visual perception better.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on two aspects of brain-machine modeling: (1) processing dynamic information (e.g., video clips) instead of typical static images; (2) whether system identification is feasible. In this study, the authors used the Algonauts fMRI dataset where cortical responses for 1000 video clips are avalible. To test the feasibility of system identification, a simulated and a realistic environment were created. In the simulated environment, I3D ResNet-50, ViT-B, and MViT-B were used astarget systems, and several computational models were used as source systems to regress on the targets. The results showed that targets trained for image and video understanding can be successfully differentiated using this regression approach. In the realistic environment, brain data were used as target systems. Using the regression approach, differences between image and video understanding, between convolutional and transformer operation, between fully-supervised and self-supervised training, can be revealed in brain responses.

I appreciate this approach but the results need more explanation

### Strengths
1. This study utilizes the movie fMRI datasets and extends past work from image to video understanding
2. This study extends past work and investigates the system identification problems in video undertanding
3. The results are informative
4. The writing is very clear and easy to follow
5. The selection of candidate models is representative and complete.

### Weaknesses
Weakness

1. In the simulated environment, the authors claimed to focus on three aspects: (1) image/video understanding, (2) fully-supervised/self-supervised, and (3) convolution/transformer. However, Figure 1 only shows the result for (1). I am wondering what the results are for (2) and (3)?
2. In the simulated environment, I3D ResNet-50, ViT-B, and MViT-B can be used for purposes (1) and (2), but not for (3). I would suggest including more target models for the purpose (3).
3. In the realistic environment, Figure 2A shows the advantages of two-stream models over single-stream models. However, why should we compare them??  Two-stream vs. single-stream is not the part in the simulated environment nor the part in the introduction.
4. Figure 4. if I understand correctly, OmniMAE-B pretrained is indeed self-supervised. But OmniMAE-B finetuned should be self-supervised + supervised finetuning. Is this comparison fair to show the differences between fully-supervised vs. self-supversied??

### Questions
see weakness

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper uses established regression techniques to determine how different models, including video-trained ones, relate to fMRI data collected during video viewing. It also first shows that such analyses can identify the input domain (image vs video) that models were trained on. Further comparisons explore architectures and layers.

### Strengths
Demonstrates 'system identification' ability

Many models are tested and compared

Includes analysis of hierarchical correspondence between brain and models

Results are clearly presented in figures

### Weaknesses
Novelty is somewhat overstated (other work has compared video-trained networks to the brain:
https://pubmed.ncbi.nlm.nih.gov/29436055/
https://proceedings.neurips.cc/paper/2018/hash/9d684c589d67031a627ad33d59db65e5-Abstract.html
https://arxiv.org/abs/2306.01354)

Writing is unclear at points.
For example, these are not complete/correct sentences:
"Since we can identify its modelling scheme,
which acts as a form of ground-truth to be used when comparing different models. "
"Towards this we investigate one model
the OmniMAE its pretrained model in a self-supervised manner compared to the finetuned one to a
downstream task with full supervision. "

"We use the modelling scheme to refer to the
model’s ability to learn from dynamic information provided in an input clip and/or static information
from a single image." I'm still unclear on what modeling scheme means. Is it the same thing that is later labeled as the (i) input?

"Since we have established the feasibility of identifying the target system to an extent with regression
scores, it brings the question of how can we use this information to identify the underlying mechanisms
in biological neural systems." This was only established for video vs image trained networks, so that should be clear.

### Questions
How do the authors understand their work in comparison to previous work that has showed self-supervised models to be equivalent to fully supervised in terms of neural prediction? e.g. https://www.pnas.org/doi/abs/10.1073/pnas.2014196118

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
