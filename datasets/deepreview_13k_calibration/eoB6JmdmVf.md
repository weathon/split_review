# Speech language models lack important brain-relevant semantics

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 3, 5, 5

## Abstract
Despite known differences between reading and listening in the brain, recent work has shown that text-based language models predict both text-evoked and speech-evoked brain activity to an impressive degree. This poses the question of what types of information language models truly predict in the brain. We investigate this question via a direct approach, in which we systematically remove specific low-level stimulus features (textual, speech, and visual) from language model representations to assess their impact on alignment with fMRI brain recordings during reading and listening. Comparing these findings with speech-based language models reveals starkly different effects of low-level features on brain alignment. While text-based models show reduced alignment in early sensory regions post-removal, they retain significant predictive power in late language regions. In contrast, speech-based models maintain strong alignment in early auditory regions even after feature removal but lose all predictive power in late language regions. These results suggest that speech-based models provide insights into additional information processed by early auditory regions, but caution is needed when using them to model processing in late language regions. We make our code publicly available

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The researchers are trying to understand what kind of information that text-based and speech-based language models are actually predicting about brain activity.  They are using a controlled experimental setup with a known fMRI dataset to systematically investigate brain alignment of language models by eliminating specific low-level textual, speech, and visual features from model representations. Finding reveal that both text and speech-based models align with the brain's early sensory areas due to common low-level features. But when these features were removed, text-based models still aligned well with brain regions involved in language processing, while speech-based models did not. This was unexpected and suggests that speech-based models might need improvement to better mimic brain-like language processing.

### Strengths
The findings of this research are important in computational linguistics and neuroscience. 

The paper provides insights into the potential of text-based language models to capture deep linguistic semantics by showing the models can predict brain activity in language-processing regions without low-level features. The observation regarding speech-based models suggests a possible direction to further improve their capability.

The controlled experimental design and statistical approach seem rigorous to me. The clarity of the paper is good and easy to follow.

### Weaknesses
I’m not familiar with the six-participate dataset and not certain if the limited scope of the datasets could affect the generalizability of the results. It would be nice if the author could discuss how to translate the findings translate to different languages, models, and datasets.

While the author describes details regarding their experiment setup, it would benefit the community if the author could publish their implementation, especially the low-level feature removal and data preprocessing. These aspects are critical for ensuring reproducibility and are not entirely clear to me. Making this information available would significantly enhance the paper's utility and impact.

### Questions
I'm seeking to better understand the application of ridge regression in the context of your study. Specifically, when you remove low-level feature vectors from pre-trained features, could this process potentially alter or diminish the representation of higher-level features? In other words, might the removal of these low-level signals inadvertently affect the model's ability to process more complex, abstract linguistic features that are also captured in these representations?

I would be interested to see more discussion for Figure 10.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A research paper submitted by the authors raises concerns about the quality and validity of the study. The reviewer argues that the study is questionable because it is based on fMRI recordings obtained from only six subjects, which is too small a sample size for any publication. Moreover, the methodology used in the study is not new, and the results are obvious, merely showing that LLMs are predictable to the human brain. 

While the reviewer acknowledges that they may have missed something, they emphasize that the study lacks methodological novelty and scientific rigor. In other words, the research does not bring anything new to the field and fails to meet the basic standards of scientific research. 

Overall, the reviewer's critique suggests that the authors need to revisit their study and address the concerns raised by the reviewer in order to produce a more compelling and scientifically robust piece of research.

### Strengths
It is difficult to determine the strength of the paper, as the contribution appears weak. Furthermore, the use of a small dataset downloaded from the internet, combined with existing analysis methods, fails to provide any novelty. The authors have not even attempted to persuade the reader that such a study makes sense. It is evident that language modeling algorithms (LLMs) are trained to replicate human language. Therefore, it is likely that human brain activity would follow language that sounds or looks natural, just as it would if delivered by a human.

### Weaknesses
Lack of methodological novelty; small dataset from another study without validation of its relevance for the authors' analysis; and, most importantly, a lack of argumentation justifying the study. The use of only six subjects in an fMRI study is a major concern, as the statistical power is severely limited, potentially leading to unreliable and non-generalizable results. While the authors may have optimized machine learning training settings for this small sample, it does not mitigate the fundamental issue of low statistical power. Furthermore, the authors do not adequately address the limitations of using a pre-existing dataset, failing to justify its applicability to their specific research questions. The analysis appears to be a straightforward application of existing methods, with no clear innovation in the approach itself. The study essentially demonstrates that LLMs, which are trained on human language, align with human brain activity, a result that is not surprising and does not contribute significantly to the field.

### Questions
1. Why is such a small fMRI dataset used? 
2. What are the technical, methodological, and scientific contributions that would interest the ICLR audience?

### Soundness
1 poor

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
This paper describes a re-analysis of two datasets of fMRI responses of a story from the Moth Radio Hour. In one cases, subjects listened to the story and in the other case the subjects read the story. The authors attempt to predict responses to these stories using text-based, large language models (BERT, GPT2, FLAN-T5) and audio-based, speech models (wav2vec2.0 and Whisper) using standard, regression-based voxelwise encoding models. They compare the prediction accuracy of these models with variants where they have regressed out the contribution from text-based features, audio- and speech-based features, and low-level visual features. They find that text- and speech-based models show similar overall prediction accuracy in early visual and early auditory regions, while text-based models show superior performance in putatively higher-level visual and language regions. They find that the performance of text-based models is relatively robust in higher-level language regions, maintaining relatively good performance when controlling for text, audio/speech, and visual features, consistent with a response to higher-level linguistic properties. In early sensory areas, there is a greater impact of controlling for these features suggesting that these lower-level features predict more of the response variance, as expected. The trends for the speech model are mostly similar, with the biggest difference being that the controlling for audio and speech features hurts performance more in high-level, language regions, suggesting that these models are not predicting high-level, linguistic properties.

### Strengths
I think directly comparing text and speech models is a valuable contribution to the literature.

The dataset investigated, with matched responses to reading and listening, is interesting and relevant to the questions being addressed. 

I think there is value in highlighting the problem of feature correlations, which this paper does well.

They test a large set of control features. Their controls are more comprehensive than most papers I have seen.

### Weaknesses
The conclusion that lower-level features explain a large portion of the variance in lower-level sensory areas is not surprising. The fact that high-level language regions are more robust to lower-level features in the context of text-based language models is also not surprising, since the response is higher-level and the model does not have any visual or auditory information baked into it. The fact that speech models are impacted by including audio and speech features is not as surprising as the authors suggest, since the models are taking audio as input and the representations are only being derived from 2-second stimuli and thus lose much of the higher-level language information that is present in a text-based model. This paper is essentially confirmatory and should be framed as such, in my opinion.

I don’t see the benefit of the “direct” approach compared with measuring the unique variance of different feature sets using some kind of a variance partitioning framework such as that promoted by the Gallant and Huth labs. Conceptually, the main thing one wants to know is what fraction of the neural response variance can be uniquely explained by a particular model and how much is shared with other models. The direct approach seems like an indirect way to address that question. I also find the term “direct” unclear? What is direct about it? What would the indirect approach be?

There is no attempt to understand whether text- and speech-based models account for shared or unique variance from each other, which seems important and natural in the context of this paper.

There needs to be more detail on the speech models. Minimally, there needs to be a summary of the tasks (e.g., masked token prediction) they were trained on and the maximum possible temporal extent that the models are able to consider. If possible, the authors should extend the window they consider to go beyond 2 seconds to allow the models to potentially incorporate longer timescale linguistic information.

Averaging performance across models is suboptimal because some of the models might be performing quite well, which would be valuable to know. For example, Whisper has been trained on a much broader range of tasks than wav2vec2.0 and it would be useful to know whether it performs better as a consequence. A better choice would be to select the best performing model for the main figure and to put the performance of all models in the appendix. Model selection could be done on training or validation data to prevent overfitting.

It is unclear how activations from different layers were handled. Were they all combined together? Typically, one selects the best-performing layer in a model using the training or validation set.

The authors need more detail about the stimuli. They should specify the total duration of the story(ies) in the listening and reading conditions, how many words there were, how the words were presented, and the rate they were presented at. For example, for listening, was this a natural story with a variable word rate? Or were the words presented artificially using a fixed ISI? If they used a variable word rate, how does this impact how the features were calculated? Downsampling does not seem straightforward in this case. For the reading condition, how was the text presented? Was there a word presented every few hundred milliseconds or was a whole sentence presented at once? Similarly how does this impact the feature design?

The language ROIs includes many regions of the STG that I would consider high-level auditory regions (e.g., respond similarly to native and foreign speech). I would recommend repeating the analyses with the language parcels released by the Fedorenko lab, or at least limiting yourself to the STS. For the early auditory analysis, I think it would be worth repeating these analyses with just the A1 parcel to be more conservative.

The visual word form area is quite small and challenging to localize:
https://www.pnas.org/doi/abs/10.1073/pnas.0703300104

I suspect the results here reflect what one would see from a generic high-level fusiform visual region. The authors could test this by selecting another nearby region and seeing if the results differ. If the results are similar, I think it is misleading to describe the results as specific to the visual word form area, despite the label provided by the atlas.

I could not follow how the noise ceiling is calculated. What is done with the results from all of the different subsamples? Is there some attempt to extend the results to infinite samples? I am skeptical about calculating a noise ceiling in V1 or A1 for the non-preferred modality. I would expect the noise ceiling to be very close to 0. How was this handled? When possible, it would be preferable to plot both the raw scores and the noise ceiling on the same figure so that you can see both. When you average across voxels for ROI analyses, do you average the noise-corrected values or do you separately average the raw and noise ceiling values and then divide these two numbers?

For Figure 3, it would be preferable to group by the listening/reading as was done in later figures. The performance between the modalities is not really comparable as these are totally different stimuli (and I am skeptical of the noise ceiling calculation).

The equations in the section title “Removal of low-level features from language model representations” make it seem like there is a single regularization term for all of the model features. It seems preferable to do what was done for the neural analyses and to fit a banded ridge model separately on every model feature. The different low-level features have very different dimensionality, so there should be some discussion of how this was handled when concatenating the features. If you z-score each feature than features that have higher-dimensionality will have much more influence. It was also not clear to me how cross-validation was handled here. Did you train and validate on a subset of stimuli and then remove the predicted response on test? How many folds were there? This information about cross-validation should also be specified in the voxel-wise encoding model section. For the banded ridge regression, were the lambdas specified separately varied for each feature set? How do we know that this range is sufficient? It is highly sensitive to the scale of the features. How fine was the grid search?

### Questions
In most cases, I found it easier to include my questions in the weaknesses section. See above. 

What was the reason for constraining the text window to 20 words? How are the results impacted by this choice?

What is the reason for not removing the control features from the neural responses as well? How would doing so impact the results?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a detailed analysis predicting fMRI activity from the activations of text-based and speech-based neural network models. The fMRI dataset studied contains data obtained during both reading and listening to the same story, allowing the authors to directly compare how each type of model can predict a given modality. The authors build a regression model between low-level features and the model activations and use the residuals of this model to also predict the neural responses, which will evaluate how much of the prediction is due to correlations of the stimuli with low-level features encoded by the model. The authors demonstrate that although early visual areas can be predicted by the responses of such language networks, this is primarily driven by low-level cues. Similarly, although early auditory areas are somewhat predicted by the text-based model features, this is due to the low-level cues.

### Strengths
The dataset that the authors use provides a compelling way to get at the question of whether the features of language models trained on one modality (speech or text input) are able to predict the other modality). The authors claim that prior work presented puzzling evidence of language models predicting early sensory regions of a modality that they were not trained on, and this work provides evidence that this is primarily due to features that are correlated between the two modalities. The methodology is also very clearly described and well-documented.

### Weaknesses
W1: The paper lacks a general discussion about correlated features in natural stimuli, which, in my view, is directly what the authors are trying to test. Citing some past work along these lines would be helpful (for instance, Norman-Haignere et al. 2018, Groen et al. 2018). 

W2: In various parts of the paper, there seems to be a bit of a conflation with correlation and causation. For instance, the authors state: “This raises questions about what types of information text-based language models capture that is relevant to early auditory processing.”, but I think the authors mean something like “This raises questions about what types of information text-based language models capture that is **correlated with features** relevant to early auditory processing”. Another instance: “This is possibly because the language models do not process visual features such as edges.”->“This is possibly because the **features in language models are not correlated with visual stimulus features** such as edges.” There are other places like this in the paper that I encourage the authors to fix. 

W3: The title of the paper seems a bit limited in scope and focuses on a result in the paper that is a bit of a straw man. The speech-based models that were tested (wave2vec2.0 and whisper) are not trained to capture semantic information, so it doesn’t seem surprising that they fail to capture semantic-driven responses. Furthermore, the claim that these models are 'language models' is debatable, particularly for wav2vec2.0 which is primarily an acoustic model. While Whisper has a language model component, it is primarily an ASR model, and it's unclear if its decoder captures semantic information in a way comparable to text-based language models.

### Questions
Q1: In the first paragraph of the introduction, which of the cited papers claims that text-trained language models predict early sensory cortex activities? This is currently unclear (many of the cited works listed under “speech” only study models with a waveform or spectrogram input), and seems very important to distinguish as is the main motivation for the study. 


Q2: Are there some baseline models that the authors could include to better contextualize the results? For instance, how well does a random-feature baseline do (useful to see a “lower bound”)? How well does a classic primary-area model such as the motion energy model, or a spectrotemporal filter bank do at capturing the primary area responses? For the classic model comparison, if neither language model is predicting the voxels better than these baseline models, then should we be considering the variance they are explaining as significant at all? 


Q3: Is ridge regression necessary when fitting the low-level features to the neural model representations? It seems like there is nearly infinite available data for this fit (I believe the low-level features are automatically extracted) and there is no noise, so I’m just wondering what the intuition is for using a ridge parameter here.  


Q4: Are the visual words and the onset of auditory words aligned in time in the dataset? That seems particularly important for this comparison, as one of the overall features encoded by both models may be “when a new thing starts”. 

Minor points: 

* The ROIs are described as “language relevant” but early visual and early auditory areas are included. It seems non-standard to refer to these as “language relevant”. 

* There is a sentence about the estimated noise ceiling being based on an assumption of a perfect model. Is the “perfect model” referred to here the regression model used for the participant-particiant regression? Or is this “perfect model” one of the candidate encoding models from DNN predictions? Clarifying what this sentence means would help the reader.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
