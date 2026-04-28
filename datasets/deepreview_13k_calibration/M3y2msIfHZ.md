# Visual Representations in Humans and Machines: A Comparative Analysis of Artificial and Biological Neural Responses to Naturalistic Dynamic Visual Stimuli

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 6, 5, 6, 5

## Abstract
Visual representations in the human brain are shaped by the pressure to support planning and interactions with the environment. Do visual representations in deep network models converge with visual representations in humans? Here, we investigate this question for a new class of effective self-supervised models: Masked Autoencoders (MAEs). We compare image MAEs and video MAEs to neural responses in humans as well as convolutional neural networks. The results reveal that representations learned by MAEs diverge from neural representations in humans and convolutional neural networks. Fine-tuning MAEs with a supervised task improves their correspondence with neural responses but is not sufficient to bridge the gap that separates them from supervised convolutional networks. Finally, video MAEs show closer correspondence to neural representations than image MAEs, revealing an important role of temporal information. However, convolutional networks based on optic flow show a closer correspondence to neural responses in humans than even video MAEs, indicating that while masked autoencoding yields visual representations that are effective at multiple downstream tasks, it is not sufficient to learn representations that converge with human vision.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work provides empirical and comprehensive studies of the alignment between artificial neural networks' representations and the brain's representations. The motivation comes from the generalist performance of MAE; therefore, MAE is expected to have similar representations to the brain. However, MAE has poorer alignment with the brain even when compared with supervised CNNs. Supervised finetuning does improve the alignment between MAE and the brain but it is not enough. Moreover, the authors also suggest that temporal information could make artificial neural networks more aligned with the human brain.

### Strengths
The alignment between neural networks and the brain is the topic that is very worth studying and the authors show that even the strong vision transformer models, that can be finetuned to many vision and control tasks, are not really aligned with the brain. The work is novel and could give insights to theoretical and computational neuroscience.

### Weaknesses
1. The conclusion of the paper does not lead to any scientific theory or a glimpse of it. Specifically, it is unclear whether the misalignment between MAE and human brains is due to Transformer Architecture or the Masked Autoencoder pre-training itself. The study has to be more concrete to conclude the theory. To decouple the confounders, I suggest the authors do more experiments on Masked Autoencoder with CNN and see if the low neural alignment still exists. The authors may also play around with different “noises” as Masked Autoencoder is a special case of Denoising Autoencoder. If Masked CNN is much more aligned with the brain, it is probably because of Transformer architecture that causes misalignment. Last but not least, the authors may use other kinds of pre-trained vision transformers that work equally well compared to MAE pre-training, such as MoCo v3, Dino v2. If Transformer is really misaligned with the brain, I would expect a low alignment regardless of the pre-training method. If it is because of the Masked Autoencoder, I would expect high alignment.


2. There is no control over visual diets. Comparing different architectures and training paradigms should be done on the same visual diets. For example, comparing CNN trained on an action recognition dataset with MAE trained on ImageNet cannot tell anything. I suggest separating experiments based on visual diets.


3. The authors only consider high-level areas of the brain. There is no comparison of the artificial neural networks with lower visual areas like V1, V2 and V4 which are important for visual object recognition.

### Questions
1. Regarding Fig 1, what do authors mean by "Predicted RDM"? RDM is calculated by responses of the networks across categories of stimuli. How could you predict RDM? Moreover, the definition of RDM should be written, at least in appendices. General audience may not understand it.

2. How are matrices in Fig 2 and Fig 3 computed? I cannot fully understand the intuition behind these matrices. If the authors use the methods existing in the previous works, they should be mentioned so that the readers can understand the full details.


3. The paper says that “Unlike VMAE and MAE, the MVD model does not learn pixel-level features.” Is this true? The MVD model takes ‘pixels' as input, so it should learn pixel-level features. The authors’ meaning may be that MVD does not use 'pixel errors' as learning signals, which is a distinct approach compared to models like VMAE and MAE. Please correct me if I am wrong.

4. The first set of analyses 3 quantify the correspondence between different models and category-selective brain regions.
What is analyses 3, is it a typo?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper author compare visual representations in masked autoencoders (MAEs) and video MAEs with human fMRI responses. 

In the first experiments, they find that representation of dynamic models (VideoMAE + Video CNNs) that take into account temporal information is more correlated with human fMRI responses as compared to models trained with static information. 

In the follow-up experiments using unique variance analysis, the authors find that convolutional models trained using optical flow explained unique variance in fMRI responses which was not explained by any other static/dynamic model suggesting the importance of optical flow loss in high correspondence with the fMRI responses.

Overall this paper finds that high performing MAEs on vision task show low correspondence with human fMRI responses as compared to standard CNNs.

### Strengths
1. This paper investigates an important question whether masked image/video modeling which leads to high performing vision models leads to representations that are better aligned with human brain responses.
2. The authors perform deep dive into which models are explaining variance in fMRI responses uniquely to determine the individual contribution of the models investigated. This is crucial as representation of the models is highly correlated.
3. The paper is easy to follow and clearly written. The figures are clearly explained in captions.
4. Comprehensive architecture choices: e.g. MAE after/before finetuning on Imagnet and VideoMAE after/before finetuning on Kinetics show that even after finetuning on Imagenet the MAE shows lower correlation than resnet trained on Imagenet

### Weaknesses
1. Results are reported on a single fMRI dataset. With large scale public fMRI datasets e.g. NSD, Algonauts videos available, the authors could have reported results on multiple dataset and showed generalizability of their results
2. I am not sure how different are individual conditions in the RDMs. If the conditions are part of the same movie then there could be high correlation between the individual conditions
3. Lack of interpretations of the results. While the authors shows model X show less correlation than model Y. An interpretation of why this could be happening is missing in the text and its relevance to brain regions functions

### Questions
1. Why video CNNs were trained on a different dataset as compared to video MAEs
2. How do authors infer that different types of dynamic information are represented in
OFA (face-selective), EBA (body-selective), and TOS (scene-selective). Line 367
3. I was not able to understand what is happening in Figure 4 and Figure 5 (Section 3.2). What was the motivation to do this analysis? How was this analysis performed and what was the result and interpretation?
4. What is the dimension of RDM? How did you divide movie segments ?

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
3

### Summary
This paper aims to study the effect of neural alignment between a wide set of computer vision models such as Masked Auto Encoders and other computer vision models including how they are trained and whether they include temporal information as well. Authors aim to show through a set of experiments that models that include temporal information are more representationally aligned with real human neural activity extracted from fMRI.

### Strengths
* Authors aim to tackle a highly relevant problem which is the effect of static vs dynamic computer vision models (trained on single frames vs video data with a temporal component) with real brain data.
* Another strength of the paper is the use of real brain imaging data to assess model correspondence when shown a set of video frames.

### Weaknesses
I think the analysis done in this paper do not correspond to the papers' main conclusion. For example, the conclusion at the end of the paper that states that computer vision dynamic models are more neurally aligned with brain data vs static models is not really supported in Figure 4 or Figure 5. In Figure 4, the RDM brain trajectories are of several models plotted compared against each other.

I would have excepted to see a line as well for the "visual cortex" all-together (human ground truth, and incrementally from V1,V2,V4, IT etc...) so that we can qualitatively make an assessment of human vs machine alignment. Further figure 5 also seems strange: What does the 1st and 2nd PC across frames have to do with saying that dynamic models are better than static ones.

It overall feels like the RDM analysis is done incorrectly. I am under the impression that the figures I would be ideally looking at is comparing human vs machine feature outputs or or recording for a collection of visual stimuli. Instead, models are being compared to each other given their activation *per brain region*. So it somehow feels like the analysis was being done within vs between systems.

The title seems too strong for the claim and methods that are being used. Models used are mainly MAE's and masked video distillation, though table 1 does show a larger family of models with some lack of details. Which supervised model or self-supervised and why not explicitly state such models like it is done for MAEs?

### Questions
* I'd like to get more clarity of Figure 4 and Figure 5. In Figure 4 it is not obvious where the trajectory begins and ends. Where is the first layer and where is the last? It seems like it is plotted 0 and 10, but it's very cluttered in Figure 4. Which model should be the ground truth and how can you plot human ground truth as well if there are a different number of layers of processing between humans and machines.

* Also what should I be looking at in Figures 1,2 and 3. How can "model victory" of one vs all be declared in ideal conditions so I can better understand what to look for in all these figures? What would the ideal output look like? Should a model get to the noise ceiling for all brain areas? I'm under the impression that this will also depend on the layer of the neural network that is being compared, to the point that each layer of an artificial neural network must be compared to each area of the biological neural network, as correlations will differ and vary based on depth.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors compare the representation layer of image and video MAEs to human fMRI response data for a variety of brain areas, and find that the models tested have dissimilar representations compared to human responses. The paper reports fine-tuning videoMAEs on an action recognition task, which results in improved fMRI response prediction, but does not achieve the predictive power of a convolutional network. The authors show that combining image and video MAE together gets closer, as does models trained on optic flow rather than movies.

### Strengths
Originality: The paper is, to my knowledge, novel in evaluating MAEs, supervised vs self-supervised and image vs video networks using human neural data such as fMRI, and addresses a gap in the literature

Quality: The reported experiments appear to be well-designed, and the findings appear credible.

Clarity: The individual figure plots are clear in terms of the metric being evaluated for different brain regions.

Significance: Investigating the representational alignment of newer, high-performing models like MAEs with human cognition is both interesting and important. It is a surprising result that the better model performance in MAEs does not necessarily improve representational alignment with humans, and challenges the assumption that better performance would come with closer alignment.

### Weaknesses
Overall, the paper is confusing as written, and this results in difficulty understanding that muddies what is I believe otherwise exciting work. For example, many of the results are simply reported with little to no summarization or interpretation of the larger significance & meaning.

There is an overall lack of justification for the methods chosen, I believe due to lack of relevant citations to previous work. For example, I could not find a justification for the author’s choice of comparison metric for model/RDM. The use of pearson’s correlation appears sound, but seems limited, especially because this requires training a linear predictor on the output, reducing the amount of test data to 1/7 of the movie segments tested. This method needs better justification citing previous work that has established this metric, or ideally an additional metric to validate it.

The PCA analysis in particular needs to be explained and justified more clearly. This is true for figure 4 but especially the analysis in figure 5 is not well explained, and the one shown appears to be an illustrative example.

### Questions
Why do the authors think that ViT MAEs, despite improved performance over CNNs, do not show strong representational alignment? Some discussion of this would help strengthen the paper.

Relatedly, more summarization of the results throughout the paper would make this easier to read.

How do the authors account for differences in temporal resolution between these frame-by-frame models, which operate on videos with <100ms frame rate, and the much lower temporal resolution of fMRI?

To improve clarity and ease of summarization, the authors should have more visualizations that summarize data effectively. For example, figure 1 could have an additional plot that compares all brain areas together, normalized by the noise ceiling and/or the explainability of the best model (CNN). 

Because F6 is in the supplemental, F1/2/3 should label Face/Body/Artifact/Scene on the left side rows to make this designation clear.

Give more justification for the PCA section, especially figures 4 and 5. I have read through this section and figures multiple times and am still unclear why these analyses are helpful in understanding the differences between image/video/optic flow model representations, I especially find figure 5 confusing - why this is useful to visualize in terms of improving understanding of representational alignment to human fMRI data? Was this analysis performed over multiple frames and can it be summarized?

Do the authors control for model size when comparing representational similarity? If not, this seems problematic, as one could expect a larger model would perform better, especially given the chosen method of using a trained linear predictor on the model outputs to compare to RDMs. 

It would be interesting to see how the models tested perform on brain score - another independent measure of biological similarity - it would be interesting to see if the same trends for MAEs are seen for this measure.

Add figure references in section 3.1.1

Fix Formatting/spelling/grammar issues:
038: ‘...similarly flexible representations: Vision Foundation Models’
064: Opic flows
117:  learn image representations
Figure 2: there is no a), b) part of the figure.
468/469: c, but also by the pc.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper compares the alignment of the response patterns in a variety of MAE and CNN, trained with static or dynamic stimuli, with the fMRI response patterns in the different visual areas of the human cortex. They found that (1) MAE is not doing better than CNN,  (2) networks trained with dynamic stimuli are more aligned than one trained with static stimuli, and (3) dynamic and static models can be complementary, i.e., combining them together can yield better alignment.

### Strengths
The study is reasonably motivated, and the questions are well-posed.
Comparing the alignment of CNN and MAE trained with static and dynamic stimuli with human systems is a legitimate problem.
Systematic evaluation of pairwise combinations of different models and finding some complementary contributions is interesting. 
The paper is relatively well-written and clear.
The approach and the methodology are straightforward. Some of the findings are interesting.

### Weaknesses
The approach is straightforward. The conceptual and technical advance is limited. 
The insights provided by the paper are rather limited.
It is a good paper with some interesting results, but probably on par with the standard of ICLR papers.

### Questions
It would be worthwhile to dig deeper to understand WHY some models are better than others and why some models are complementary.

### Soundness
3

### Presentation
3

### Contribution
3
