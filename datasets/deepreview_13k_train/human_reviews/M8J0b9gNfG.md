# Multilingual Visual Speech Recognition with a Single Model using Visual Speech Unit

- Decision: Reject
- Scores: 6, 5, 8, 6, 6

## Abstract
This paper explores sentence-level Multilingual Visual Speech Recognition with a single model for the first time. As the massive multilingual modeling of visual data requires huge computational costs, we propose a novel strategy, processing with visual speech units. Motivated by the recent success of the audio speech unit, the proposed visual speech unit is obtained by discretizing the visual speech features extracted from the self-supervised visual speech model. To this end, we introduce multilingual AV-HuBERT (mAV-HuBERT) by training the model on 5,512 hours of multilingual audio-visual data. Through analysis, we verify that the visual speech units mainly contain viseme information while suppressing non-linguistic information. By using the visual speech units as the inputs of our system, we pre-train the model to predict corresponding text outputs on massive multilingual data constructed by merging several VSR databases. As both the inputs and outputs are discrete, we can greatly improve the training efficiency compared to the standard VSR training. Specifically, the input data size is reduced to 0.016% of the original video inputs. In order to complement the insufficient visual information in speech recognition, we apply curriculum learning where the inputs of the system begin with audio-visual speech units and gradually change to visual speech units. After pre-training, the model is finetuned on continuous features. We set new state-of-the-art multilingual VSR performances by achieving comparable performances to the previous language-specific VSR models, with a single trained model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes methods to train a multilingual visual speech recognition model, a first of its kind.  The main contributions of the paper are usage of quantized representation of AV-HuBERT embeddings to reduce the dimensionality of video data, alongside proposing a curriculum learning approach to improve the VSR performance. This approach gradually diminishes the reliance on audio data during training, ultimately leading to the model being trained solely on video embeddings.  The proposed methods significantly reduces training computational costs while enhancing Visual Speech Recognition (VSR) performance across multiple languages.

### Strengths
-> Trains a single model to lip read in multiple languages, which I believe hasn't been done before.

-> There is a clear improvement in the total training time required to train the mAV-Hubert due to the proposed quantization of AV-Hubert embeddings. 

-> The proposed multi-lingual model maintains its effectiveness and stands its ground when compared to the monolingual VSR method.

-> The paper has good analyses on the information captured by the discretized visual units which is useful to the VSR community.

### Weaknesses
-> The novely of the article is limited. The authors use preexisting blocks such as AV-Hubert and previously proposed methods of curriculum learning to improve the VSR performance. 

-> From Table 5, it looks like curriculum learning does not seem to have a significant impact on the VSR performance.

-> The paper contains grammatical errors and requires proofreading.

### Questions
In table 6, the authors showed that AV-HuBERT trained on multi-lingual data performs worse that mAV-Hubert for non-English dataset, thereby claiming that their proposed strategy of using visual speech units for training mAV-HuBERT is more effective in building VSR models. The claim would be better substantiated if the authors can apply the same strategy for training mAV-HuBERT on English only train dataset and show that it performs better than AV-HuBERT for English test set.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work explores sentence-level Multilingual Visual Speech Recognition with a single model based on the pretrained AV-HuBERT and multi-lingual Hubert model. By taking advantages from the previous AV-HuBERT and the multi-lingual Hubert model together with the combination of multiple audio-visual speech datasets of different languages, the work here is able to transform the visual speech features to visual speech units and further perform multilingual visual speech recognition based on these units.

### Strengths
The general structure is clear. The method is simple in general. It’s easy to follow. It’s indeed very appealing in the view of efficiency when trained with discrete units.

### Weaknesses
Compared with new methods or other insights, I think this work is more like a case to show the success again of large-scale data and large-scale model. Similar to the audio speech units, the visual speech units are introduced here. But the concept of visual speech units has been introduced since AV-HuBERT and its contemporary works. 
The method here is totally based on the pre-trained AV-HuBERT and multilingual HuBERT, with a common masking strategy by gradually increasing the masked ratio of audio samples. There seems no new points in the proposed method and training strategy. It is more like a presentation of an example to use existing large-scale models (AV-HuBERT, HuBERT).

In Table.2, the worse performance of the proposed method compared with AV-HuBERT is described as the curse of multilinguality. What’s the specific ratio of English data in the whole data? If the English data takes a large ratio in the whole data, and there are also common shared visemes among different languages, considering the larger-scale of the whole data compared with AV-HuBERT, the performance on English should not be worse? 
In Table 3, the proposed work is based on pre-trained AV-HuBERT and HuBERT. The “standard VSR” is also trained further based on these two models? or from scratch? The duration of “52.5 hours for 8 epochs” is also based on loading the pre-trained models?
In Table 5, what’s the results of using only “unit pretraining”, whitout both CL and FT? Will it degenerate to the case of AV-HuBERT in Table 6?

### Questions
(1) In Table.2, the worse performance of the proposed method compared with AV-HuBERT is described as the curse of multilinguality. What’s the specific ratio of English data in the whole data? If the English data takes a large ratio in the whole data, and there are also common shared visemes among different languages, considering the larger-scale of the whole data compared with AV-HuBERT, the performance on English should not be worse? 
(2) In Table 3, the proposed work is based on pre-trained AV-HuBERT and HuBERT. The “standard VSR” is also trained further based on these two models? or from scratch? The duration of “52.5 hours for 8 epochs” is also based on loading the pre-trained models?
(3) In Table 5, what’s the results of using only “unit pretraining”, whitout both CL and FT? Will it degenerate to the case of AV-HuBERT in Table 6?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a multilingual visual speech recognition, by using the visual speech units to improve the training efficiency. It also proposes a curriculum learning approach to also exploits audio speech units. The paper presented number of experiments to investigate the effectiveness and efficiency of the proposed method.

### Strengths
- a novel frame work
- an efficient framework
- good presentation and experiments

### Weaknesses
 - reproducibility seems difficult

### Questions
1- Computation aside, how different performance would be if we use continues features compared to unit features?

2- The paper mentions that one novelty is presenting the sentence level model. it would be good if some explanation is provided around advantage of sentence level models?

3- Once audio speech is utilised in the pertaining together with visual speech units, why using audio speech unit and not complete speech features? is it only to make computation more manageable? how performance and computation would change if audio speech is not discretised? 

4- Table 2 contains interesting results, where the multilingual setup does not help English dataset. In addition to what authors mentioned, there could be other reasons like language similarities or available language specific information. This has been the topic of number of works around multilingual models that how to balance between more data Fram more languages or using less data only from fewer similar languages[1][2]. While I believe this paper's topic is not around this issue, I think it would be good to refer  to this point

[1] Cross-entropy training of DNN ensemble acoustic models for low-resource ASR
[2] Multilingual data selection for low resource speech recognition

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper extends a recent work on audio speech units to the audio-visual (AV) domain and tackle the associated challenge of the need for large amounts of labeled training and the computational cost. In doing to, they also extend the previous work on English language AV that leveraged visual phoneme units to a single-model solution for several popular languages.

### Strengths
1. There is solid engineering of the final system, with sufficient details to support reproducibility.
2. Builds on the recent state-of-the-art and leverages the nifty insights in training large scale ASR across languages and modalities.
3. Good amount of ablation studies to demonstrate the efficacy of various system components.
4. Source code, models, and samples (to be?) made publicly available.

### Weaknesses
1. The reference list and the related work sections are relatively misleading for the title of the paper. Either the term, "neural network/deep learning models," or a similar qualifier has to be added to the title and abstract or the related work should be expanded to include the historical work in the area, prior to the use of deep learning models.
2. Section 3, particularly 3.2 is hard to follow with it not being self-contained. I recommend bringing the results that justify the variety of modeling and training choices being described here into this section itself. For example, the specific choices of the visual front-end (ResNet-18) and the transformer architecture are not justified within this section, making it difficult to understand the rationale behind these design decisions. The reader is left wondering why these particular choices were made and what alternatives were considered.
3.  This work leverages good tips and engineering practices in building the mAV-HuBERT solution but obscures the focus from what is the big science/research delta between AV-HuBERT and mAV-HuBERT. The paper does not clearly articulate the novel scientific contribution beyond scaling up the training data and model to multiple languages. The core methodological differences and their impact on the final performance are not sufficiently highlighted, making it difficult to assess the true advancement over the original AV-HuBERT.

### Questions
1. What is the justification of hyperparameter choices such as, "We use the target size of 1,000 and train the model for 350k steps with one iteration?"
2. "...reduce training speed by removing the visual front-end."  Unsure why this is a good thing, unless you are referring to reducing the step size.
3. Why does the curse of multi-linguality only affecting the results for English? How does the relative sizes of training data in various languages affect this?
4. "After 70% of training, p is set to 100 so that only visual speech units are used." What is magical about 70?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a visual speech recognition model that can perform recognition on multiple languages. The model consists of a AV-HuBERT module that extracts visual speech units, followed by transformer module that converts visual speech units into text. The proposed model is trained in three steps. The first step focus on training mAV-HuBERT module by regressing visual input to discrete visual speech unit with supervision coming from pre-trained multilingual HuBERT model. The second step conducts pre-training on transformer module by taking visual speech unit extracted by mAV-HuBERT model and predict text. The final step conducts an end-to-end fine-tuning of all modules by taking visual input and predict text. Experimental evaluation demonstrated that the proposed mAV-HuBERT model can effectively perform multilingual visual speech recognition compared to mono-lingual method which has to be trained on individual language. The proposed training strategy also improved over naive multilingual model trained on all languages while reducing training time by using discrete visual speech unit as input during pre-training.

### Strengths
1. This paper extended AV-HuBERT to effectively handle multilingual scenario. Compared to mono-lingual AV-HuBERT that is trained on individual language, mAV-HuBERT achieved best WER on three out of five languages and second-best on two out of five languages. The improvement on under-resourced languages is especially encouraging as the proposed method demonstrate a possibility to improve VSR on a specific language by leveraging other languages. 
2. The proposed training strategy of mAV-HuBERT not only help improve the recognition accuracy of AV-HuBERT on different languages but also improves training efficiency by leveraging discrete visual speech unit during pre-training, which uses much less data storage and thus allows much higher batch size and reducing training time. The strategy of curating multilingual language dataset used during training is also a contribution
3. Analysis on visual speech unit provides insight on the unit such as the unit captures well on the viseme information rather than other information such as speaker identity.

### Weaknesses
1. Although the overall approach and the problem the paper tackles are novel, the core model is largely based on an existing model AV-HuBERT with minimal modification. The pre-training objective is also commonly used without much modification. Perhaps the authors could clarify a bit more on any contribution regarding extending AV-HuBERT in model architecture if applicable. Specifically, the paper does not detail any changes to the AV-HuBERT architecture itself, such as modifications to the transformer layers or the feature extraction process. This lack of architectural innovation makes it difficult to assess the true contribution beyond simply applying an existing model to a new dataset and task.

2. The comparison in Section 4.3.1 may not be completely fair. For AV-HuBERT, the model is pre-trained with English only, so fine-tuning on other languages means the English pre-trained AV-HuBERT is trained with same loss function on a new language, which will result in 5 different fine-tuned model i.e. one for each language. For mAV-HuBERT, a same model is supposed to work for different languages. So the fine-tuning is not supposed to be done on each language, which would yield 5 different models. If this is how the experiment was done, then mAV-HuBERT has advantage by design as it was pre-trained with more language data. If my understanding was not correct, then the authors should clarify on the specific process of fine-tuning of mAV-HuBERT. The paper should clarify whether the fine-tuning process for mAV-HuBERT involves training a single model on the combined multilingual dataset or training separate models for each language, as this significantly impacts the interpretation of the results.

3. The comparison with multilingual VSR approaches is weak. The only comparison done was with AV-HuBERT as the authors claim there is no prior work that can perform multilingual VSR with a single model. However, there are recent work and reference therein indicate exploration along this direction. For example,
- Cheng et al., MixSpeech: Cross-Modality Self-Learning with Audio-Visual Stream Mixup for Visual Speech Translation and Recognition, ICCV 2023
- Anwar et al., Muavic: A multilingual audio-visual corpus for robust speech recognition and robust speech-to-text
translation, 2023.

### Questions
1. I'm curious on how the number of visual token size used to determine visual speech unit used in the first step affect the final performance. Do the authors vary the number (1000 being used in the paper) and choose the one with better performance?
2. Regarding the curriculum learning, I'm also curious on how the learning schedule affect the performance. And when p% reaches 100%, the embedding from audio speech unit is useless. Do we disregard the embedding completely (thus no concatenation needed) or we still retain the same process to generate concatenated embedding?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
