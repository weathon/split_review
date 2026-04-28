# Dynamics Based Neural Encoding with Inter-Intra Region Connectivity

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 6, 5, 1

## Abstract
Extensive literature has drawn comparisons between recordings of biological neurons in the brain and deep neural networks. This comparative analysis aims to advance and interpret deep neural networks and enhance our understanding of biological neural systems. 
However, previous works did not consider the time aspect and how the encoding of video and dynamics in deep networks relate to the biological neural systems within a large-scale comparison. Towards this end, we propose the first large-scale study focused on comparing video understanding models with respect to the visual cortex recordings using video stimuli. The study encompasses more than two million regression fits, examining image \textit{vs.} video understanding, convolutional \textit{vs.} transformer-based and fully \textit{vs.} self-supervised models. Our study resulted in both, insights to help better understand deep video understanding models and a novel neural encoding scheme to better encode biological neural systems. We provide key insights on how video understanding models predict visual cortex responses; showing video understanding better than image understanding models, convolutional models are better in the early-mid visual cortical regions than transformer based ones except for multiscale transformers and that two-stream models are better than single stream. Furthermore, we propose a novel neural encoding scheme that is built on top of the best performing video understanding models, while incorporating inter-intra region connectivity across the visual cortex. Our neural encoding leverages the encoded dynamics from video stimuli, through utilizing two-stream networks and multiscale transformers, while taking connectivity priors into consideration. Our results show that merging both intra and inter-region connectivity priors increases the encoding performance over each one of them standalone or no connectivity priors. It also shows the necessity for encoding dynamics to fully benefit from such connectivity priors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work provides a comprehensive study of predicting fMRI signals in visual cortical areas while humans view short video clips, by mapping from the activations within a wide range of artificial neural networks that process the same videos or still images from them. The study compares models that differ along several interesting dimensions:  image-computable and video computable models, CNNs and transformers, and fully-supervised vs self-supervised training regimes. The results show that video-computable, convolution-based, fully-supervised models are generally the best predictors of visual cortical activity. The relevance of these results is supported by additional encoding studies where the encoding “target” is an artificial neural network of known architecture, showing that it is possible to distinguish between image-computable and video-computable models using a system identification approach. A novel strategy for incorporating inter and intra-region functional connectivity information is proposed, and this approach improves the encoding performance of the already best-performing models.

### Strengths
1.	Neural encoding is an important area of research that can yield insights to both improve artificial neural networks and better understand biological neural systems. 

2.	There is a thorough review of recent related work that makes it clear how the current paper is situated given existing literature. 

3.	A wide variety of appropriately chosen “source” candidate models are employed for comparative encoding experiments, and they vary in several interesting ways as outlined by the authors (single-image vs video computable, CNN vs transformer, fully supervised vs self-supervised). The breadth of the study in this regard is unprecedented for encoding of visual cortical responses to video inputs. 

4.	The work demonstrates in a convincing way that video computable, fully supervised CNN models can generally enable more accurate predictions of visual cortical activity than models that are image computable, are based on transformer architectures, and/or are self-supervised. 

5.	The work also presents evidence that system identification of image-computable vs video-computable systems is plausible (figure 2). This provides additional support for conclusions drawn regarding biological targets. 

6.	A novel approach for incorporating inter and intra-region connectivity is presented, which significantly improves the voxel prediction performance.

### Weaknesses
This paper is primarily limited by a frequent dearth of clarity in the writing, as well as a methodological concern about the way inter and intra-region connectivity priors are incorporated into the encoding models. This reader’s score could improve considerably with clarification of these issues. 

1.	Additional proofreading/editing is recommended to clarify and improve sentence structure in many parts of the paper. For example, the description of the “Real environment” (last part of section 3.1) is ambiguous – it states that two different datasets are used, but then says “we mainly use the training set, and perform cross-validation…”, “The dataset provides fMRI recordings of ten subjects…”, “each video and voxel in the brain was represented by a single activation value” without indicating which dataset these statements refer to (or is it both?). Also in this part of the paper, what does it mean that each video and voxel in the brain was represented by a single activation value? Aren’t there different values across time and between subjects? In several parts of the paper, there are similar ambiguities such as it being unclear which dataset is being referred to at what time. 

2.	It is not clearly specified how the inter/intra region connectivity module is combined with the rest of the encoding models to make voxel activity predictions. The current version of the paper claims that intra-region connectivity priors improve predictive performance – but seemingly by directly providing the voxel values that are being predicted as inputs to the overall model. The improvements in performance might be due not to a meaningful incorporation of connectivity priors, but rather undesirable leakage of label information into the input. 

3.	One of the claims is that inter/intra-region connectivity information improves performance to a greater extent in video-computable models compared with image-computable models – the evidence for this is presented in  figure 6b. However, there is a confound because connectivity-related performance improvements are compared between image-computable ResNet-50 and video-computable MViT: how can it be determined whether the apparent interaction effect is related to image computable vs video computable models rather than CNNs vs transformers? Furthermore, the evidence presented in Figure 16 does not support the claim that connectivity priors have a greater benefit for video-computable models in general. Specifically, while Figure 16a shows a statistically significant benefit for video-computable convolutional models in some regions, Figure 16e shows the opposite trend for transformer-based models, with image-computable ViT showing greater benefits from connectivity priors than video-computable MViT in several early visual regions. The claim that “encoding dynamics is an important aspect to enable the full utilization of such connectivity priors” is not supported by the evidence, and should be removed.

Minor comments: 

4.	In the abstract and several other places, saying that “the study encompasses more than two million regression fits” does not seem especially relevant – the number of regression fits in itself does not seem to be a particularly informative way to quantify the scale of the study. 

5.	In describing the contributions of the paper, the authors seem to emphasize that prior works did not compare different neural network architectures - but in section 3.1, there is a statement that “while previous works focused on the architecture aspect, we argue it is even more important to look into whether the model is learning dynamics (e.g., motion) or simply using static information from a single image.” Yet, the comparison between single image vs video processing would seem to be an important emphasis of Lahner et al 2024. These claims about the relationship between prior works and the current paper should be clarified. 

6.	The terms “real environment” and “simulated environment” are not especially informative – perhaps something like “biological target” and “artificial neural network target” would be an improvement

7.	In first paragraph of section 4.1, “As for image understanding models we use the default sampling rate of eight.” Does this refer to 8 frames per second? This whole paragraph seems quite ambiguous – why are video understanding vs image understanding models being discussed here in relation to sampling rates?  

8.	The text is some of the figures is too small to be easily readable, especially figure 2, figure 3, figure 5, and supplementary figures 7, 8, 10, and 11.

9.	Most of the in-text citations would be best formatted with both author and year inside the parentheses. In LaTex, you can use \citep{} instead of \cite{}

10.	The goal of the paper seems to be stated in an overly general way in the abstract (“This comparative analysis aims to advance and interpret deep neural networks and enhance our understanding of biological neural systems”). 

11.	Typos: 

A.	In the introduction (end of page 1), “while the later showed that these fMRI recordings” (should be latter instead of later)

B.	Grammar issue in start of 2nd paragraph of section 3.1: “How do deep video understanding models families compare to biological neural systems” 

C.	End of section 3.1 “The datasets we use is provided at TR one second” (should be are, not is, and the TR acronym should be defined)

### Questions
1.	The following reflects the evolution of my understanding while reading the paper: the authors study the ability of artificial neural network activations to predict biological signals in the visual cortex (the “target”) – they also include an ANN-based target – what does the artificial target add to the study? Section 3.1 seemingly attempts to explain this, but it may need to be edited for clarity. Is the idea that we know the structure of the target ANNs in the artificial setting, so we can test our ability to uncover mechanistic insights through encoding experiments, and therefore get a sense for how informative the system identification experiments with biological targets are likely to be? This becomes much clearer upon review of Han et al 2023, but it should also be explained more explicitly in the introductory sections of the present work. 

2.	In equation 1, in the first term, is a 1/L normalization needed for the summation $\sum_{l=1}^{L} \omega_l \hat{Y}_l$ ? Without the normalization, it seems mildly inconsistent with the statement above equation 1 that “we learn the weights of one fully connected layer to provide the predictions of the voxels of one region of interest in the visual cortex as, $\hat{Y}_l = W_l X_l$.” Or perhaps this normalization is absorbed by $\omega_l$?

3.	In section 3.4, the description of the connectivity module indicates that all voxels from all regions are used to predict voxels from a single region. Doesn’t this mean that the desired output of the model (voxel values from a single target region) are contained in the input of the model, making this a trivial mapping? It makes sense that dropout layers could partially alleviate this problem, but why does it make sense to set up the architecture in this way in the first place where at least some of the outputs are trivially accessible in the input? 

4.	Section 4.1: for four-fold cross validation where each fold has 90% of the videos in the training set and 10% in the test set – are the 10% test sets disjoint between the folds, or randomly selected? (Not a major issue, but 75:25 might have been a slightly more natural choice for four-fold cross validation) 

5.	In section 4.2, there is a statement that “we include video understanding models that are trained on three different datasets which are Kinetics, Charades, and Something-Something v2”. These datasets are not cited, and it is not clear how the results from the three datasets were combined to produce figure 2 – were the results pooled somehow?

6.	Might it be useful to discuss why the observed trends seem to hold for some visual cortical regions and not others? For example, video-computable models are no better than image-computable models for predicting FFA and PPA activity - it is interesting to speculate that perhaps recognition of faces (associated with FFA) or environmental scenes (associated with PPA) in the brain might be less dependent on temporal dynamics.

7.  For plots like those in figures 2 and 3, what does each dot represent? For example, is it one regression score from one type of “source” model averaged among cross-validation folds, or is it an accuracy from one of the folds only? Are results from different source models pooled together in these plots? Relatedly, it is not clearly specified how the Welch’s t-tests are performed – which sets of values specifically are used to compute the t-test? 

8.	Why are system identification results presented in the main text specifically for image vs video computable models, rather than other comparisons of interest like CNNs vs transformers or self-supervised vs fully-supervised?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper compares a variety of image and video models to fMRI data, evaluating these models for representational alignment to human responses. The paper reports this analysis for multiple types of networks, comparing image/video, convolutional/transformer, single/multi stream, and self-supervised/unsupervised networks. The authors report the best predictors of human responses are convolutional, multi-stream, unsupervised video networks. Additionally, the paper reports experiments with a intra- and inter- region connectivity priors which improve encoding performance.

### Strengths
Originality: To my knowledge, this paper uses an established approach, but is novel in the scale and types of comparisons between types of models compared. 

Quality: The paper is of good quality, with good statistical analysis and control conditions.
 
Clarity: The majority of the paper is written very clearly, especially the sections comparing image/video, convolutional/transformer, single/multi stream, and self-supervised/unsupervised networks to BOLD signal.

The scale of experiments in terms of number of models is commendable, and the authors were clever to choose models that enabled comparisons across many different dimensions.

Significance: This is an important emerging area in understanding alignment of models with human data, especially for new types of models, which show improved performance on visual tasks, but as the authors show, have worse representational alignment with human responses. This paper is significant in its contributions to understanding the quality of these alignments over multiple different axes of comparison.

### Weaknesses
There is little explanation of the intra- and inter- connectivity priors, especially their structure, and interpretation of their results beyond their contribution to improved representational alignment, and the value of their learned weights in figure 5c.

I am a bit confused about the intra- inter- connectivity priors, what their structure is, and if the results demonstrate anything beyond that complex connectivity as seen in human visual cortex increases predictivity?

Relatedly, the paper would benefit from even a minimal interpretation of the learned connectivity weights. What is their structure and how does this change with training? How do they contribute to improvement of the representational alignment? What do these learned weights imply biologically? Such an analysis would likely also address the previous point.

I challenge the authors in L435-437 on leaving the reasons behind the better alignment seen in fully supervised networks to future work. This is a major result of the paper and I challenge the authors to at least make some hypotheses or have a few sentences of discussion as to why this could be the case. The validation of such a hypothesis can be left to future work.

Minor syntax issues:
L151 “: e?”.”
L363: “This difference decrease as”

### Questions
I am a bit confused about the intra- inter- connectivity priors, what their structure is, and if the results demonstrate anything beyond that complex connectivity as seen in human visual cortex increases predictivity?

Relatedly, the paper would benefit from even a minimal interpretation of the learned connectivity weights. What is their structure and how does this change with training? How do they contribute to improvement of the representational alignment? What do these learned weights imply biologically? Such an analysis would likely also address the previous point.

I challenge the authors in L435-437 on leaving the reasons behind the better alignment seen in fully supervised networks to future work. This is a major result of the paper and I challenge the authors to at least make some hypotheses or have a few sentences of discussion as to why this could be the case. The validation of such a hypothesis can be left to future work.

Minor syntax issues:
L151 “: e?”.”
L363: “This difference decrease as”

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work is developed in two parts, aiming to (1) compare the neural predictivity of video deep neural networks on video fMRI data, and (2) propose a method to improve prediction scores via utilizing brain region connectivity.
In the first part, it tests the brain predictivity of models with different architectural design and learning paradigm and contrasts to image models (in total, 26 video action recognition models and 11 image object recognition models are tested). The results indicate that video models are better predictors than image models, in early regions convolutional models are better than transformers, and supervised models are better than self-supervised. Additionally a system identification check is performed which shows that video models can predict other video models better than image models, and vice versa, based on four target models. In the second part, this work proposes training a module to consider all regions in the prediction of any single region and shows improvements on the prediction scores of two selected video models and one image model; the image model has a less pronounced improvement which the authors claim is due to the lack of dynamics.

### Strengths
The paper is original in the aspect of application (model-to-brain encoding) to a new domain (human video fMRI aside from image fMRI), and the writing style has good quality. Previous work is also sufficiently covered. The questions asked are important and in general this work is a step in the right direction.

### Weaknesses
However, there are several soundness and presentation related issues in its execution that negatively impact this reader’s opinion of the paper.

First of all, the paper reads as two rather disjoint parts that fail to come together as one clear proposition (see summary for the two parts). As such, it looks like this could be two unrelated papers, that each would need further work to be able to stand on its own. This is the case in many points throughout the paper, for example in Figure 1, the reader is lead to think that this is the main figure / main method proposed, but the extent of the results with this method are underwhelming, as are the technical details provided.

Second, there are several issues with the soundness of the methods.
* The reader is not convinced that the improvements observed in brain predictivity are caused by the learned connectivity, and not just by obtaining a more robust or less noisy embedding by considering other regions. There are also inconsistencies in the results regarding this aspect; in figure 5c it is observed that LOC does not connect with any other areas apart from itself - then how is it explained that in figure 5a performance is significantly improved with the connectivity module? Could it be that connectivity is not the reason at all for the improvement? For the learned connectivity itself, extensive comparison with findings in neuroscience literature on region connectivity is lacking.
* For the analysis in section 4.5 as a whole, it is very unconvincing that only two models are compared, instead of the 37 models initially examined in the first part. When comparing to the image models, only one image model is tested and from that the conclusion “shows the necessity for encoding dynamics to fully benefit from such connectivity priors.” is inferred, which is too strong.  Additionally in figure 6b, it is inconsistent that not even Slowfast is shown but only MViT. In the same figure, scores “in a different scale after multiplying by 100” are shown instead of percentage of improvement, not allowing to observe the improvement regardless of the models’ performance scale itself. 
* The motivation to use the Algonauts challenge’s training set for the main results without evaluating on the official test set, is unclear. An even better, more obvious choice for the main results would be to use the full Bold Moments Dataset which is more refined, higher quality, and also includes the test set. The low repetition count in the training set significantly impacts the signal-to-noise ratio (SNR) of the fMRI data, making it unsuitable for robust model evaluation; this data is primarily appropriate for training encoding models, not for drawing strong conclusions about model performance. Using the test set with its higher repetition count would provide a much more reliable basis for evaluating the models' predictive capabilities.
* The supervised vs. self-supervised comparison is not clean, as all the self-supervised models are transformers - thus the relationship between convolutional models and transformers is also partly transferred in that result. The comparison is also between very different numbers of models, with only 5 SSL and more than 30 SL. Additionally, throughout the paper results are shown with models mixed from different training datasets, which makes the effects of each examined comparison (e.g. architecture) and the training dataset, entangled. See Conwell et al. (2022, 2024) for an example of clean comparisons.
* The reader finds that the fine-grained analyses of figure 4 are too fine-grained to be scientifically valid. What does evaluating a single design choice for two-stream processing tells us about either the networks or the brain? Why is the specific TimesFormer architecture chosen to compare against two other (specific) architectures as representatives of supervised, self-supervised, and fine-tuned self-supervised? Furthermore, quite a lot of emphasis is put on the multiscale component of MViT, however, without an explicit ablation it is not possible to know which factor of this model contributes to its good brain predictivity. Additionally, the authors reach the conclusion that early regions relate better to convolutional models “since they better capture high-frequency components” but this is not evidence drawn from their results and rather from other publications. It is not shown that this is the reason behind their results. Further, the model MViT does not conform to this so it seems that this conclusion is too strong.

Third, there are some major problems in the paper’s presentation.
* Figure 1 has several issues. (1) It does not show any details of the Inter-intra Region Connectivity Model (layers, loss function), which is the main component proposed. (2) It shows the pipeline only at the inference mode and does not mention neither which mode is shown or their (substantial) differences. (3) In the first stage of voxel prediction (encoding) it is not clear that the predicted voxels are the outputs of the encoding procedure (they either look like the video models’ input or at best as if they are their direct output which is also not the case). (4) Finally, a major point of this figure was to show that different degrees of connectivity between regions are predicted, but from the size of the visualization on the left it is near impossible to tell differences between the thickness of the arrows.
* In section 3.4, where the Inter-intra Region Connectivity Model is introduced, there are no equations to show the model layers, and more importantly the loss function to train this module is not described at all, in equation or text form.
* In section 4.1, it is not clear whether the hyper-parameter tuning is conducted on the Algonauts training set or the authors’ training set (90% of the Algonauts training set, different for each of the 4 folds). This is an important clarification to make because in the first case the encoding test set is seen during hyper-parameter tuning.
* Phrases like “we mainly use the training set” in section 3.1 are too vague - when exactly do the authors not use it? From section 4.1 it seems that only the training test is used in all cases.
* Video models used are described as “video understanding” models throughout the paper, which is inaccurate because they are all video action recognition models - video understanding is a vague umbrella task that could potentially include segmentation, reasoning, and many other more complex tasks than classification. By also describing the image models as “image understanding” models, authors obscure the fact that they are trained on a different task than the video models, which is object recognition rather than action recognition.

### Questions
Overall the reviewer feels that although some of the presentation problems could be corrected, there are overarching problems with the structure, i.e. disjoint two parts, and the soundness of this paper, i.e. correlational evidence, unclean comparisons, and rushed conclusions, that make it hard to change in a way sufficient for acceptance. 
The final rating is 5 in absence of the option for 4 (because 3 would be too low).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The authors use multiple neural network models to attempt to fit signals from functional magnetic resonance imaging (fMRI) obtained while participants watched short video clips from two existing datasets (Cichy et al 2021, Lahner et al 2024).

### Strengths
The authors have done extensive calculations with lots of computational models.
Understanding how the brain processes dynamic signals is an important question.

### Weaknesses
 - The manuscript is poorly written and it is very hard to decipher what the authors did. There is almost no methodological information whatsoever. I list an initial list of questions that would be essential to answer when the authors submit the work to some other venue. 
- It is recommended that a native speaker goes over the paper to fix grammar and clarity. 
- It is also recommended that someone reads the paper with reproducibility in mind. This can help the authors understand all the information they need to provide. 
- In this type of data fitting work, it is always useful to define a lower bound given by chance and an upper bound sometimes defined by computing split-half regressions across multiple repetitions of identical stimuli
- The temporal resolution of fMRI is very poor. The field has struggled with getting any meaningful temporal information about of videos. Given that the authors seem to be interested in timing, it would be useful to consider data with better temporal resolution. If the authors cannot use better data, then they should first document that there is any temporal information that can be obtained from the fMRI signals during videos. 
- The authors do not say anything about eye movements. Participants typically make 2 to 4 saccades per second while watching images or video. Presumably these saccades would radically change the activity in visual cortex. It is unclear how one can make any meaningful claims about visual cortex without documenting the neural responses to each saccade.  
- Before jumping into large neural networks with large numbers of free parameters, it would be useful to quantify how well the data can be explained by simple models like pixels, contrast, optic flow, etc. This is assuming that the authors first convince themselves and show that there is actual reproducible data that warrants explanation.

### Questions
There is almost no explanation of what the authors did here. The authors are using existing datasets and they do not need to copy and paste the entire methods section of the original papers. But they need to explicitly indicate what they have done here.
	(1) In terms of the experimental data: 
	How many participants?
	How many video clips? 
	What was the length of the video clips?
	How many repetitions of each video clip?
	What was the size of the image, the frame rate, and the volume of the audio? 
	What was the resolution of the eye tracker used?
	What kind of video clips? What was the content? Were there cuts in the video? 
	(2) In terms of the analyses,
	Saying “… we use the brain responses…” has little meaning. 
	What are the units of the measurements?
	How reliable are the measurements (e.g., reproducibility across repetitions of identical stimuli)?
	Which time interval was used for the analyses? There is a mention of one second but the temporal resolution is much slower than 1 second, it would be important to document that there is indeed information at 1 second time scales. 
	Which voxels were used for each region?
	Which hemispheres? 
	How were the 9 regions of interest defined? 
	(3) Data fitting
	What was the dimensionality of the predictors in each case?
	How was cross-validation performed?

### Soundness
1

### Presentation
1

### Contribution
1
