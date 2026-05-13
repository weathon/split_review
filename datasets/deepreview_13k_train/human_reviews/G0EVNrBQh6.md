# Investigating Human-Identifiable Features Hidden in Adversarial Perturbations

- Decision: Reject
- Scores: 5, 5, 5, 3, 1

## Abstract
Neural networks perform exceedingly well across various machine learning tasks but are not immune to adversarial perturbations. This vulnerability has implications for real-world applications. While much research has been conducted, the underlying reasons why neural networks fall prey to adversarial attacks are not yet fully understood. Central to our study, which explores up to five attack algorithms across three datasets, is the identification of human-identifiable features in adversarial perturbations. Additionally, we uncover two distinct effects manifesting within human-identifiable features. Specifically, the masking effect is prominent in untargeted attacks, while the generation effect is more common in targeted attacks. Using pixel-level annotations, we extract such features and demonstrate their ability to compromise target models. In addition, our findings indicate a notable extent of similarity in perturbations across different attack algorithms when averaged over multiple models. This work also provides insights into phenomena associated with adversarial perturbations, such as transferability and model interpretability. Our study contributes to a deeper understanding of the underlying mechanisms behind adversarial attacks and offers insights for the development of more resilient defense strategies for neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies how to extract human-identifiable features from adversarial examples. Based on the fact that DNN models are trained on human-labeled datasets, the authors assume that adversarial perturbations should also contain human-identifiable features. 

The authors first claify that two factors, excessive gradient noise and incomplete features, hinder feature extraction. Therefore, the authors propose to utilize noise augmentations and model ensembling to mitigate these negative effects. The authors find two interesting phenomenons: masking effect (untargeted attacks) and generation effect (targeted attacks).

### Strengths
1. This problem is interesting. I like this topic.

2. The visualization results are also promising.

### Weaknesses
1. Although this problem is interesting, the authors do not provide more surprising findings and insights compared with previous works.
  1.1 Adversarial perturbations contain meanful or human-identifiable features have been studied in these works [1,2]. They may correspond to "robust" features.
  1.2 The proposed methods, noise augmentations and model ensembling are widely used in transfer attacks. More transfeable perturbations contain more "robust" features (human-identifiable features) and share more non-robust features. The previous work have shown this point [1]
  1.3 Although the visualizations are very promising, we are uncertain about the extent of assistance this can provide.

2. Some claims in the article are unclear:
  2.1 The two obtacles are not very clear. The first one (noisy gradient) is easy to understand. Lots of transfer attacks also propose to mitigate this negative effect to improve adversarial tranferability. However, there is insufficient evidence to support the second claim about incomplete learned features. Could you please provide more details about the second one?
  2.2 Meanwhile, the comparison between these two points is also unclear. Which factor has a greater negative impact on extracting human-identifiable features? As shown in experimental setting, the authors need to use lots of ensembling models. This has made is method less practical.
  2.3 The findings from Section 5.2.3 are interesting. The authors use the contour features to attack models. It also shows that contour features are important than background information. Could the authors please discuss connections and differences between this phenomenon and this work [3]?

3. Could the authors please provide more results about generation effect on targeted attacks?

### Questions
Please see Weaknesses part.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper conducted interesting analysis on the human-identifiable features concealed in adversarial perturbations crafted by different attack algorithms. In order to obtain the visual-recognizable patterns from gradient-driven adversarial perturbations, multi-samplings on different threat models was used based on the independence assumption. In experiment sections, thsi paper conducted such analysis on various threat models (274 in total) with various attack algorithms (gradient-based, search-based), which is efficient and solid. While the resulting denoised adversarial perturbations seem to have some clear pattern which can be recognized by human, the pure adversarial perturbation cannot reveal any information regarding the image itself. This paper also contains following discussion on the denoised adv perturbation by quantitatively analyzing its recognizability, checking its attack strength, and applying contour extraction. The overall analysis is plentiful and the results looks interesting.

### Strengths
- Evaluation on a large amount of threat models and attack algorithms make the whole experimental results to be reliable.
- Motivation on exploring the human-identifiable features directly, instead of applying XAI methods to interpret, looks efficient and interesting.
- Overall written is clear and easy to follow.

### Weaknesses
While I do appreciate such important and intense work on exploring the explainability in adversarial perturbations, I still have some major concerns about the whole paper. 

- Human-identifiable features looks vague: I still remain unclear about how to logically define the "human-identifiable" here: In section 5.2.1 authors conducted recognizability experiments on these denoised adv perturbations but it can only prove they are "model-identifiable". We cannot make such claim by showing part of (or even all) extracted adv perturbations and they are all human-identifiable. Some human-labeling experiments is required as a strong evidence to prove this. The current experiments only demonstrate that a model can classify the denoised perturbations, which does not directly translate to human understanding or recognition. The authors need to establish a clear link between model classification and human perception, possibly through a rigorous human subject study with a diverse set of participants and a well-defined evaluation protocol.

- The overall finding is not surprising: while it is good to see that denoised adversarial perturbation is similar to its corresponding raw image, I'm not surprising to see because gradient-based attacks perturb models' prediction by optimizing the objective function following the pixel-gradient direction --- larger pixel gradients indicate pixels here are important for threat model to identify this input image. Thus the outcome of gradient optimization, adversarial perturbation, should contain some important features to identify this image. And for search-based attacks, it still tend to follow the important pixels to craft their perturbation. I think this paper should focus more on the target-attack scenario - so we have our raw-image key features and our targeted label --- how would the adversarial perturbation be to reflect both concept? Currently it only has a very short paragraph discussing such scenario (Section 6). The paper needs to delve deeper into the specific mechanisms that cause these perturbations to be human-interpretable, rather than just observing the phenomenon. A more detailed analysis of the gradient information and its relation to human-understandable features is necessary. Furthermore, the targeted attack scenario is crucial for understanding how adversarial perturbations encode both the original and target class information, and this aspect requires more in-depth investigation.

### Questions
I put all my concerns to the weakness part and I do think this paper has a lot of space to improve. 

However, I think the overall results is plentiful and interesting for other researchers to know (especially on denoised perturbation under targeted attack scenario). It could be a very interesting workshop paper after reorganizing it into a logical way.


======================================================

Updates after reading authors' rebuttal:

I really appreciate authors efforts on further elaborating the importance of their findings - now I tend to believe this is an interesting finding to me and it could inspire several future papers for further theoretical analysis. However, after checking Reviewer ZsSi's comments, there could be some literatures implicitly discussing such scenario but this paper lacks contribution on further exploring the underlying reasons. I would like to raise my score to 5 but reduce my confidence to 3.

### Soundness
2 fair

### Presentation
3 good

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
This paper delves into the exploration of the underlying reasons for adversarial perturbations. Specifically, the authors hypothesize that human-identifiable features are present within the perturbations, forming part of the inherent properties of these perturbations. To validate this hypothesis, the authors average perturbations generated by various neural networks to uncover the human-identifiable features.

### Strengths
+ This work finds that perturbations generated by existing methods statistically contain some human-identifiable features. These are clearly illustrated in the provided qualitative results.

+ To uncover these human-identifiable features, the authors use a simple method which averages extensive generated perturbations, which is reasonable. 

+ This paper demonstrates that perturbations produced by certain attack methods converge at the object region.

+ This paper provides a clear narrative, supplemented by analytical insights.

### Weaknesses
 - In the first paragraph of Section 4, on what basis do you assert that (1) the noise in perturbations is independent and (2) two perturbations from different models display distinct human-identifiable features? I couldn't find any references or evidence supporting the claims. Specifically, the assumption of independence of noise across models is not well-justified; while gradients might have local variations, these variations could still exhibit some correlation, especially if the models share similar architectures or training data. Furthermore, the claim that distinct human-identifiable features exist in perturbations from different models needs more rigorous justification than empirical observation. The authors should provide a quantitative measure of 'distinctness' and explore the factors that influence this variation.

- The gradient-based attacks, proposed five years ago, aren't sufficiently contemporary to test the paper's hypothesis. There exist many newer gradient-based attacks, such as [1, 2]. The use of older attacks limits the generalizability of the findings to more recent adversarial techniques. The paper should include more recent and diverse attack methods to ensure the robustness of the conclusions. For example, attacks that incorporate momentum or adaptive step sizes could reveal different perturbation characteristics.

- I observed that detecting human-identifiable features necessitates 2,700 samples (270 models and 10 noise-infused seed samples). These may suggest that the averaged perturbation, generated by the three attacking methods, gravitates towards the object region. However, they don't confirm that in every model, the generated perturbations house human-identifiable features. Hence, a deeper experimental analysis regarding model selection and the integration of Gaussian noise would be beneficial, perhaps including more ablation studies (like MM, MM+G, SM+G). The paper lacks a detailed analysis of how the number of models and noise samples impacts the emergence of human-identifiable features. It is crucial to demonstrate that the observed features are not simply artifacts of the averaging process, and that they are consistently present across individual models, not just in the aggregate.

- Why choose only 20 fixed classes out of 1,000? And a mere 200 samples seem insufficient to substantiate the claims made in the paper. The selection of only 20 classes from ImageNet raises concerns about the representativeness of the results. A more comprehensive analysis across a wider range of classes is needed to ensure that the findings are not specific to the chosen categories. Similarly, 200 samples may not be sufficient to capture the diversity of images within those classes, potentially leading to biased conclusions. The paper should justify the choice of 20 classes and provide evidence that the results generalize to a broader set of images.

- It's noted that perturbations of identical images from varying attack algorithms are presumably alike. However, the results don't include background noise similarity or image perturbation similarity. Providing experimental evidence for this would enhance the argument. The claim that perturbations from different attacks are similar needs more rigorous evaluation. The paper should provide quantitative measures of similarity, such as cosine similarity or structural similarity index (SSIM), and analyze these measures for both the entire perturbation and specific regions, such as the object contour and background. This would provide a more concrete basis for the similarity claim.

- The experimental analysis concerning the two distinct types of human-identifiable features (masking effect and generation effect) appears limited. Visualizing the perturbation for targeted attacks would be beneficial. The analysis of masking and generation effects is somewhat superficial. The paper should provide a more in-depth analysis of these effects, including quantitative measures of their strength and how they vary across different attack methods and image classes. Visualizations of perturbations for targeted attacks, especially those that fail, would help in understanding the limitations of the proposed approach.

-  Does the visual perturbation come from cases where the attack was successful? How does the perturbation behave in the case of an unsuccessful attack? The paper does not clearly state whether the presented perturbations are from successful attacks or not. It is crucial to analyze the behavior of perturbations in both successful and unsuccessful attack scenarios to understand the conditions under which human-identifiable features emerge and their relation to attack success.

### Questions
See the questions in the weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper explores the human-identifiable features that are concealed within adversarial perturbations. To this end, this paper utilizes 270 models as surrogate models, introduces Gaussian noise to the input, and identifies the human-identifiable features. This paper shows that in targeted attacks, these features typically demonstrate a "generation effect" by producing features or objects of the target class. In contrast, in untargeted attacks, these features exhibit a "masking effect" by hiding the features or objects of the original class. This paper further claims the revealed phenomenon can interpret some properties of adversarial perturbations.

### Strengths
1. This paper revisits a critical concept in the context of adversarial robustness: the underlying mechanism of adversarial perturbations.
2. This paper conducted human tests to verify that the emergence of semantic features is not coincidental, which is of importance.
3. This paper validates the hypothesis across targeted and untargeted attacks and includes search-based attacks.

### Weaknesses
This paper challenges a well-acknowledged phenomenon in the context of adversarial robustness: the *perceptual aligned gradient* (PAG), which refers to the **human-identifiable features** that align with human perception in adversarial perturbations, only exists in robust models [1-3]. However, this paper claims that such features are also hidden in the perturbations of standardly trained (non-robust) models, which contradicts the current understanding of PAG. This concept of PAG has been well supported by various empirical and theoretical analyses in the follow-up works, along with its various applications. Therefore, in my opinion, to challenge the existing theories that contradict the claim made, this paper should provide sufficient theoretical and empirical evidence to support the proposed claims. Unfortunately, not only has the evidence in this paper already been discovered or directly deduced by previous work, but they also cannot explain the contradicted theories, which I specify below.

1. The experiment uses Gaussian noise to average the perturbations to reveal the human-identifiable features. However, this phenomenon has already been revealed in [4], which shows that randomized smoothing (adding Gaussian noises to the input and calculating the averaged gradient) on a single standardly trained model can lead to PAG and generate these features. Therefore, it's not a newly discovered phenomenon claimed in this paper that averaging gradient among perturbations with different noises can lead to human-identifiable features.
2. The experiment also averages different models to reveal the human-identifiable features. However, this phenomenon is expected based on existing work [5, 6], which shows that a little adversarial robustness of the models can lead to PAG. Specifically, as ensembling more non-robust models can still enhance adversarial robustness to a certain extent, though not as robust as adversarially trained models, it can be inferred that the ensembled model can lead to such PAG and identifiable features. Even if this paper shows that the robust accuracy of the ensembled model against adversarial attacks is still low (in Figure 3), the enhanced robustness may still be sufficient to bring such PAG.
3. In addition, it has also been shown [7] that the distribution of non-robust features [17] varies across different model architectures. Therefore, intuitively, the gradient (perturbation) of a single model (or a single kind of model architecture) may be noisy, but by averaging the gradients from different models, it is possible to converge toward the robust features.

Based on these discussions, the discovery made in this paper is somewhat trivial, since the observed phenomenons have already been revealed in existing work or can be directly deducted from them. Furthermore, the evidence presented in this paper is insufficient to challenge the well-established theories of PAG, as this paper does not provide a clear explanation of the contradictions or confusions, which I specify below.

4. There exist several works [8-10] aim to explain the reason PAG only exists in robust models by characterizing the decision boundaries between different models, which is well supported by theoretical analysis. These works show the fundamental difference of decision boundaries between standard and adversarially trained models leads to the (non-)existence of PAG, which contradicts the claim made in this paper in Section 7(2) that human-identifiable features also exist in non-robust models. Unfortunately, this paper does not discuss this viewpoint and does not conduct a theoretical analysis to overturn these theories.
5. There also exist theories interpreting the existence of PAG in robust models by modeling adversarial training as energy-based models [11-12]. Additionally, the robust model also provides better guidance during the generation process of diffusion models [13-14], indicating the importance of robust models with PAG for better gradient and generation guidance. Since such a generation process requires multi-step sampling, which can be regarded as applying an **average (ensemble)** of gradients (perturbations) to the standardly trained model, this also contradicts the viewpoint in this paper and should be well-explained.
6. In Section 7(1), the explanation for the transferability of adversarial examples contradicts existing works. This paper attributes the transferability to the human-identifiable (robust) features, but existing works [15-16] show that robust features may not be always helpful for adversarial examples transferring between models and non-robust features still play a crucial role in transferring adversarial examples. Therefore, the claims made in this paper fail to explain the transferability of adversarial examples across models.
7. The explanation of non-trivial accuracy for classifiers trained on a manipulated dataset [17] made in Section 7(3) is flawed. It is clear that in the manipulated dataset, which includes perturbations claimed as human-identifiable features in this paper, the features from the original class are still dominant over the perturbations. According to the interpretation within this paper, the model should still learn the features from the original class and cannot achieve clean accuracy in this noisy training setting. This contradicts the explanation proposed in this paper.
8. In Appendix A, Figure 7, it appears that the masking effect of the perturbation without Gaussian noise significantly reduces the identifiability of human-identifiable features, compared to the results in the main paper (with Gaussian noise). Therefore, it can be inferred that ensembling Gaussian noise plays a more crucial role in generating the human-identifiable features than ensembling different models, which undermines the soundness of the claim that the presence of human-identifiable features is inherent in the perturbations themselves, rather than being a result of added Gaussian noise.
9. There is a lack of ablation studies on the number of models to further support their claims. It is suggested to add experiments to analyze how many models or noises are required to emerge such human-identifiable features, which can provide a more intuitive view of how noisy the gradients are in the adversarial perturbations.
10. For transfer attacks, this paper only compares BIM, CW, and DF, which are not specifically designed for transfer attacks. It is suggested to add a comparison with existing state-of-the-art transfer attackers, e.g., MI-FGSM [18], DI-FGSM [19], and ensemble attacker CWA [20], to substantial the claims regarding transfer attacks. Since this paper claims that the success of transfer attacks is based on hidden human-identifiable features, it can be inferred that transfer attacks can emerge with more human-identifiable features, which should be supported by experiments on evaluating these attacks designed for transferring.
11. There is no statement on open sourcing and reproducibility. Since finding such 270 surrogate models is challenging to reproduce, I strongly suggest releasing the code.

### Questions
Please see the weaknesses above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work identifies the presence and effect of human-identifiable features in adversarial perturbations. The authors recognize that individual perturbations on a single input, while successful at fooling a model, do not produce distinct features that can be readily interpreted by humans. They posit that this is due to the presence of noise in the perturbations, and introduce a methodology to help overcome this by averaging many perturbations on the same image. The result produces perturbations that are significantly more human understandable, as demonstrated through a human evaluator experiment. With these new perturbations, they identify two different effects that these perturbations have on their input: masking, which covers prominent features of the true class of the image, and generation, which creates prominent features of the target class. Overall, this work provides insights into features created in adversarial examples, introduces methodology that can increase explainability in the presence of adversarial examples, and provides explanations from their findings for well known phenomena in adversarial training, transfer ability attacks, and interpretability.

### Strengths
Thank you for your submission! I thoroughly enjoyed reading this paper; the results were compelling, the methodology was sound, the contributions and findings are novel and useful, explanations were clear, and I was surprised at how recognizable the generated perturbations were.

Some specific highlighted results/conclusions/contribution:
- As mentioned in the paper, there is a significant need for work that provides explanations for reasons as to why attacks are as successful as they are and why models are as vulnerable to adversarial examples as they are. This work bridges these two approaches by (a) evaluating a variety of attacks and (b) creatively extracting portions of perturbations that are well aligned across models and thus represent features that transfer across models
- The perturbations generated with this method were significantly clearer/more recognizable to me as a reader. Additionally, I felt that the claim of generating human recognizable perturbations was well supported by also incorporating the results showing that (a) human evaluators were able to recognize perturbations without associated inputs from the MM+G method at a rate significantly higher than random guessing and (b) the perturbations generated in the MM+G setting yield far more successful adversarial examples than the standard SM case
- The discussion section connected multiple trends in transferability, adversarial training, and clean/robust accuracy tradeoffs to reasonable explanations based on insights from this work.

### Weaknesses
The breadth of experiments done was extensive, but I felt that in certain places, the depth of individual experiments could have been improved. Specifically:
- I would have preferred to see more samples per class evaluated (10 seems quite small to me)
- In the human evaluator test, I understand the limitation of testing all the attacks/settings but at the very least both settings under one attack should have been evaluated. At present, it is hard to give meaning to the 80.7% human evaluator accuracy under the BIM MM+G setting since there is not a BIM SM setting to compare it to. It would also be helpful to provide some justification for why BIM (over the other attacks) was chosen for this experiment.
- Similar to the previous point, including SM settings in the cosine similarity experiment would have been helpful to get a baseline sense of how similar perturbations usually are to each other and to see if the MM+G setting yields significantly different values.

Additionally, the paper is clear and concise as written, but there were some portions that could benefit from additional details, explanations, or citations, mainly in Section 4 (Experimental Method).

Specific (minor) suggestions for improvement:
- The notion of "incomplete components of the associated features" was lacking definition/explanation, adding some details around what this is supposed to represent would be helpful.
- The problem of "the number of available neural networks being limited" didn't feel clear/well motivated. There are many parameters that can be adjusted to produce different models (seeds, hyperparameters, optimizer, architecture, etc.). Further, it wasn't clear how the solution of applying noise to produce more inputs solved this problem. 
- Some more citations to help support the contour extraction experiment would be helpful, particularly for claims that make statements about portions of the image that humans use for classification.

### Questions
- How were the subset of classes chosen?
- How were the 200 inputs chosen? Were there any constraints or conditions for these inputs? Were all samples chosen correctly classified by all models?
- While it does appear that adding noise to produce additional inputs works well, the inspiration/motivation for doing this wasn't exactly clear. Why add noise rather than performing some kind of data augmentation? 
- Why was the standard deviation of noise added to the inputs different for the different attack algorithms?
- Why were 270 models chosen for generating perturbations? Were these experiments tried with fewer models (besides the single model case)?
- It is mentioned in the human evaluator test that the lowest and highest accuracy in each subset was discarded before calculating the average. What was the purpose of this? And can you clarify exactly what was discarded (e.g., was data for a single sample removed from all participants or was data from a single participant removed from all samples?)

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
