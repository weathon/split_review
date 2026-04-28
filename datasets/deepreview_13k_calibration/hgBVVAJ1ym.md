# MIND THE GAP: ALIGNING THE BRAIN WITH LANGUAGE MODELS REQUIRES A NONLINEAR AND MULTIMODAL APPROACH

- Decision: Reject
- Avg Score: 5.33
- Scores: 3, 5, 8

## Abstract
Speech comprehension involves complex, nonlinear, and multimodal processes within the brain, integrating auditory signals with linguistic and semantic information across widespread brain networks. Traditional brain encoding models, often relying on linear mappings from unimodal features, fall short in representing these intricate mechanisms. In this study, we introduce a nonlinear, multimodal encoding model that combines audio and linguistic features extracted from pre-trained deep learning models (e.g., LLAMA and Whisper). These nonlinear architectures and early fusion mechanisms significantly enhance cross-modal integration, achieving a 14.4% increase in average normalized correlation coefficient and 7.7% increase in average single-story correlation compared to the previous state-of-the-art model relying on weighted averaging of linear unimodal predictions. Moreover, this improved performance reveals novel insights into the brain's functional organization, demonstrating how auditory and semantic information are nonlinearly fused within regions linked to motor control, somatosensory processing, and higher-level semantic representation. Our findings provide empirical support for foundational neurolinguistic theories, including the Motor Theory of Speech Perception, embodied semantic memory, and the Convergence Zone model, revealing novel insights into neural mechanisms otherwise impossible with simpler encoder models. By emphasizing the critical role of nonlinearity and multimodality in brain encoding models, our work bridges neural mechanisms and computational modeling, paving the way for the development of more biologically inspired, brain-aligned artificial intelligence systems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This is an interesting paper, using embeddings from open source LLMs and Audio model compared to fMRI images of the human brain. The authors use 10 open fMRI datasets, from 3 subjects who listen to 20 hours of a podcast. They extract LLM embeddings from LLama3 and audio embeddings from Whisper. They carry out PCA on the fMRI to reduce the dimensionality of the space and then compare predictive models with the embeddings as inputs to predict the fMRI/PCA outputs.  The main claim of the study is that the combination of multimodality (LLM + audio embeddings) and nonlinearity (ML architecture comparisons) leads to a 17% increase in the accuracy of the predictions. The authors interpret this through the lens of cognitive science, and therefore " highlights the crucial role of nonlinearity and multimodality in accurately modeling the 491 brain’s complex processes during speech comprehension", and point to a set of theories in neurolinguistics.

### Strengths
The strength of the paper is the novelty of the question and the thoroughness of the analysis. The authors make use of open source ML models to create novel representation of input signals to the brain and fearlessly apply these to models predicting fMRI signals. There is precedence on this in the literature, both from ECOG data and fMRI data, but nonetheless taking this on is a highly nontrivial undertaking given the noise in the data and requires courage.

### Weaknesses
Unfortunately despite the claimed statistical significance Fig 1/2, I just don't believe the result. I grant the author that the changes in \Delta r might pass statistical tests, but these are extremely noisy measurements, the changes in the statistical indicator (r) are quite small and the error bars are enormous.  "Extraordinary claims require extraordinary evidence" and I just don't think we should be accepting papers that claim nonlinear processing in the brain without more evidence than this. Risk of overfitting here is very large and there are many choices the authors made that could have influenced their results unwittingly

I realize this is an impossible weakness to rebut -- dataset aquisition is expensive, open source datasets are few, and fMRI is noisy.  I appreciate the spirit of the analysis and would love to see this done at a larger scale to get more solid results -- but without better data I just don't think analysis llike this is warrented.

### Questions
If there were ways of rebutting this I'd be happy to listen but again given the nature of the results and the limitations in the data and the noisiness of the measurements I'm not sure what to ask. Are there more datasets to use or ways of strengthining evidence?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
There is a large body of research focused on measuring the similarity between language processing in the brain and in language models. Recent studies have shown that representations from Transformer-based language models exhibit a higher degree of alignment with brain activity in language regions when using voxel-wise encoding models with linear mapping. However, the authors note that relying solely on linear mappings from language model representations falls short in capturing the complexity of nonlinear auditory signals and linguistic processing in the brain.
The primary aim of this paper is to investigate this question by using a nonlinear, multimodal encoding model that incorporates both audio and linguistic features to predict brain activity. To achieve this, the authors build both non-linear and linear voxel-wise encoding models and compare the encoding performance between representations from two language models (LLaMA:text-based and Whisper:speech-based) and brain recordings. Additionally, the authors create encoding models by combining the two representations and measure brain alignment. The experimental results demonstrate that there is a significant improvement in prediction accuracy with non-linear encoding models, achieving a 17.2% increase in mean correlation across the cortex compared to the prior linear encoding models.

### Strengths
1. The exploration of nonlinear voxel-wise encoding models, as well as the variations in these models' ability to predict brain activity compared to prior linear encoding approaches, provides valuable insights for the research community.
2. The significant improvement in prediction accuracy with nonlinear encoding models over linear models offers a promising future research direction for understanding what information is truly being captured in the nonlinear mapping of representations to brain activity.

### Weaknesses
1. While the main research question aims to investigate the benefits of using nonlinear encoding models over linear models, the insights into this question are not clearly presented. There are several significant weaknesses in this work:
- Previous brain encoding studies predominantly use linear mapping rather than nonlinear models for the sake of interpretability. This is because stimulus representations are complex, and these representations are derived from nonlinear AI models, while brain recordings often have a low signal-to-noise ratio (SNR). Linear mapping is advantageous in this context as it can provide clearer insights into the brain's processing or the model's representation. Therefore, I encourage the authors to elaborate on their motivation for using nonlinear models beyond the goal of improved prediction accuracy. Additionally, a discussion on how they intend to address the interpretability challenges associated with nonlinear approaches would strengthen the manuscript.
- Given that the authors extract representations from complex nonlinear AI models, it remains unclear whether the improvement observed with the nonlinear encoding model is due to the richness of the stimulus representations or the added complexity from introducing extra hidden layers in the voxel-wise encoding model.
- I recommend that the authors disentangle these factors by comparing their nonlinear model to a linear model with increased complexity (e.g., with more parameters). This approach would help isolate the specific impact of nonlinearity on model performance.
2. It is well-known that both LLaMA and Whisper are language models, with LLaMA being text-based and Whisper being speech-based. However, both models contain some degree of semantic information. As a result, integrating the two representations through concatenation may introduce redundancy or lead to one modality dominating the other. This raises the question of what information is actually contributing to predicting brain activity in the multimodal integration scenario, making it unclear which features are truly driving the prediction.
- In fact, a recent study by Oota et al. (2024) demonstrates that text-based language models exhibit high alignment in language regions due to brain-relevant semantics, whereas the alignment of speech-based language models in these regions is primarily driven by low-level stimulus features, indicating a lack of brain-relevant semantics in speech models.
- Consequently, it remains unclear which features are actually driving the prediction of brain activity in the concatenated scenario. Furthermore, this ambiguity extends to the nonlinear encoding model, where the specific contributions of different features are not well understood.
3. Using the concatenation of text-based and speech-based representations for multimodal information processing is not considered an ideal approach in the deep learning field. Moreover, while the authors discuss multimodal information processing in the brain, the experimental setup involves subjects listening to stories, which essentially pertains to language comprehension. In language comprehension, the early sensory processing differs—visual for reading and auditory for listening—while the semantic processing remains similar for both modalities [Deniz et al. 2019, Oota et al. 2024, Chen et al. 2024].
- As a result, it is unclear what constitutes "multimodal encoding" in this context if the focus is on language comprehension in the brain. If the authors intend to discuss multimodal information, it would be more appropriate to refer to it as "fusion" rather than "integration."
4. Several sentences are overstated: "We provide novel evidence for nonlinear multimodal integration in motor, sensory, and visual brain regions, supporting existing theories in neurolinguistics while revealing new insights into the neural basis of speech comprehension."
- The authors used representations from language models but did not interpret which features are driving brain activity across different regions of interest (ROIs). Therefore, the claim that the models capture relevant brain activity patterns can only be substantiated if the authors analyze what information within these representations is truly predicting brain activity.
- I recommend incorporating techniques such as representational similarity analysis or feature importance measures. These methods could help identify which aspects of the language model representations are most predictive of brain activity across different regions, offering deeper insights into the model-brain alignment.
5. The feature extraction methods used for the two language models are not comparable. In LLaMA, the stimuli were presented in a dynamically sized context window that expanded up to 512 tokens, whereas the Whisper model used a fixed window of 16 seconds. This discrepancy is not ideal for comparing the performance of both models. Oota et al. (2024) addressed this issue by using a context of 20 tokens for text-based models and windows of 16 to 64 seconds for speech-based models to ensure a fair comparison. Consequently, with a 16-second window, it is unclear how much linguistic information is captured in Whisper compared to 512 tokens in LLaMA.
- Additionally, the feature extraction process in LLaMA is not clearly explained. The meaning of the context being "grown until 512 tokens and then reset to a new context of 256 tokens" needs further clarification.
- I suggest that the authors conduct an ablation study or sensitivity analysis to evaluate how varying context window sizes impact each model’s performance. This analysis could offer valuable insights into the influence of context window size as a methodological factor and potentially inform future improvements.
6. There is a lack of discussion on how the findings of the current paper might influence future model design in AI, particularly in developing cognitively inspired multimodal architectures, or how these results could contribute to neuroscientific theories of language processing.

### Questions
1. Line 67: The statement "While some studies have begun exploring multimodal models that combine linguistic features with visual information (Tang et al., 2024; Scotti et al., 2024)" is inaccurate. In Tang et al. (2024), the authors used a multimodal model (BridgeTower, which is pretrained on vision-language data) to extract representations, but they did not combine features directly. Instead, they provided either text or movie input separately to the model to obtain the representations. Therefore, the claim that these studies "combine features" is incorrect. Additionally, the authors have overlooked relevant studies that perform this kind of analysis, where multimodal integration or fusion is explicitly explored. These studies should be cited to provide a more accurate and comprehensive overview of the field.

Oota et al. 2022, Visio-linguistic brain encoding

Wang et al. 2023, Incorporating natural language into vision models improves prediction and understanding of higher visual cortex

2. Line 75: We demonstrate a substantial improvement in prediction accuracy, achieving a 17.2% increase in mean correlation across the cortex compared to the prior linear encoding models. 
- The authors claim that the improvement is due to the use of nonlinear encoding models. However, it remains unclear what the hidden layer is capturing. Could the authors clarify what the 256 hidden neurons are learning that contributes to the increase in predicted brain activity? Understanding the specific features or patterns that these hidden neurons encode would help explain the observed improvement.
3. Line 291: Our findings suggest that nonlinear models are wellsuited for capturing this complex interplay of distributed neural activity, providing a more accurate and insightful representation of the brain’s functional organization compared to linear models.
- The authors should provide a stronger foundation for how the current study explains the brain's functional organization using nonlinear models in comparison to linear models. This would involve detailing how nonlinear models offer insights into the brain's functional architecture that linear models cannot capture, and specifying which aspects of brain organization are better explained by the nonlinear approach.
4. The insights presented in Section 3.3 are not clear. Please refer to the weaknesses mentioned in point 3, which highlight the lack of clarity regarding which features in the concatenated multimodal representations are actually driving the prediction of brain activity, especially given the differences in feature extraction and processing between text-based and speech-based models. Addressing this point would help clarify the insights in Section 3.3.
5. The surprisingly high prediction performance in visual regions during a listening task, as shown in Figures 1 and 2, requires further clarification.

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
The paper examines various techniques for improving the state-of-the-art on the task of predicting fMRI-measured BOLD response to language. They propose a multimodal method of combining representations from audio and language models to outperform an established baseline. The method utilizes PCA to reduce the dimensionality of the responses prior to model fitting, as well as an MLP to learn nonlinearities of the data.

### Strengths
The proposed method substantially improves prediction performance on a task of extreme importance to neuroscience and neuroengineering. Encoding model prediction performance is directly related to decoding performance, and enables the use of in-silico testing. Nonlinear approaches to brain modelling are quite understudied and deserve more research.

I have currently marked the paper as a 5 owing to the concerns below, however if they are all successfully addressed or revised then I am willing to raise the score.

### Weaknesses
There are some omissions in the paper that I would hope to see addressed. For example, the "All voxels" condition seems to only have been tested for the Linear case as in the original cited baseline. This is somewhat puzzling, because for two of the conditions, both the semantic and the multimodal condition, the "PCA" condition actually performs worse than the "all voxels" condition. It's not clear to me why the authors use PCA here. The inclusion of a MLP+all voxels setting in the ablation table would be useful to clarify the reasoning for this choice.

The authors claim that their results do not support the claim in the original baseline (Antonello et al.) that encoding performance scales with model size for language models (line 964). This was somewhat surprising to me, as this relationship has been reproduced by Hong et al. as well as others. Looking deeper, the author's claim seems somewhat undersupported, as the authors only test models with no less than 7 billion parameters, even though the vast majority (>80%) of the improvement in the original baseline is claimed to occur when scaling from models of size 125 million to models of 13 billion parameters. If the authors intend to make the claim that scaling relationships do not exist for encoding models, they should test smaller feature extractors (~125M parameters) to fully validate their argument.

Additionally, the authors claim that their multimodal approach can explain regions outside of M1M and AC, however as far as I can tell the only regions that are red in the comparison flatmap (Figure 1a) are M1M and AC, so I'm not really sure where this is coming from. They specifically claim that medial prefrontal cortex and angular gyrus are better predicted, however, neither of these regions are red in the provided flatmap, and they are not included in the boxplots either. Please clarify this discrepancy.

I also find it somewhat odd that the multimodal model is only compared to the semantic baseline. It seems that the more appropriate comparison point would be the referenced stacked regression model when evaluating their MLP + PCA multimodal approach. The primary claim of a "17.2% increase in mean correlation across the cortex compared to the prior linear encoding models" therefore seems somewhat misleading.

The inclusion of motor regions (except for M1M) in the analyses are somewhat strange - these are typically poorly predicted overall and have little to do with language processing. It would be good in general for the authors to include at least one figure that shows absolute prediction performance rather than relative prediction performance. This is especially important because the provided flatmaps are changes in correlation coefficient and not r^2. An improvement in prediction performance from r=0.1 to r=0.2 explains substantially less additional variance than improvement from r=0.7 to r=0.8.

Also, is r^2 computed as r*|r| here? If so, this should be mentioned somewhere.

### Questions
See above.

### Soundness
3

### Presentation
4

### Contribution
3
