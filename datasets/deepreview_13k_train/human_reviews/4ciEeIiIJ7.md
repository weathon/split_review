# Let’s disagree to agree: Evaluating collective disagreement among AI vision systems

- Decision: Reject
- Scores: 3, 3, 3, 6, 5, 3

## Abstract
Recent advancements in artificial intelligence (AI) have led to the development of AI vision systems that closely resemble biological vision in terms of both behavior and neural recordings. While prior research in modeling biological vision has largely concentrated on comparing \emph{individual} AI systems to a biological counterpart, our study instead investigates the collective behavior of model populations.
We focus on inputs that generate the most divergent responses among a diverse population of AI vision systems, as measured by their aggregate disagreement. We would expect that the factors driving disagreement among AI systems are also causes of misalignment between AI systems and human perception. We challenge this expectation by demonstrating alignment between AI systems and humans at the \emph{population} level, even for images that generate divergent responses among AI systems. This unexpected finding challenges our understanding of the relationship between the limitations of AI systems and human perception, suggesting that even the most challenging stimuli for AI systems are reflective of human perceptual difficulties.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper compares the collective behaviour of 1,032 AI vision systems with 42 humans in annotating images, investigating how various visual factors influence agreement levels. It highlights that images that are challenging for the AI systems often pose similar difficulties for humans. The paper suggests that there is an alignment in visual complexity across both groups. The study quantifies (dis)agreement among AI systems and compares the results with human annotations. Additional factors such as difficulty score, minimum viewing time, and specific visual properties are examined. This approach offers insights into common challenges shared by AI and human perception.

### Strengths
The comparison between model performance and human annotations is interesting and insightful.

### Weaknesses
This work presents the following weaknesses:

1. My first concern is related to the assumption from which the paper starts (L19) about the “ factors driving disagreement among AI systems are also causing misalignment between AI systems and humans perception” - why would that be the case?  It states that the current study challenges (L484) “the assumption present in prior work that disagreement among AI systems is unrelated to human visual processing”. But this assumption (L484) is not adequately founded, or at least not supported through the references provided which do not claim that disagreement between artificial models is unrelated to human visual processing. To reinforce, the initial assumption is not adequately discussed or supported by the correct references making it difficult to understand the motivation of the paper in the first place.


2. For a study comparing human and artificial visual systems, the authors might want to consider the body of literature that draws from neuroscience to better understand how convolutional neural networks (CNNs) could model early visual processing pathways [e.g. A Unified Theory of Early Visual Representations from Retina to Cortex (Lindsey et al., 2019); Spatial and Colour Opponency in Anatomically Constrained Deep Networks (Harris et al. , 2019)]. Such works aim to understand the similarities between human visual systems and artificial models at the lower level of neurons and how the functional and structural layouts of biological visual systems could better inform DNN architectures.

3. While the idea of comparing many to many is interesting and could add value on top of accuracy and one-to-one error consistency measures, the experimental setup seems to be (visually) ill-posed. For instance, the challenging examples are complex scenes, e.g. Figure 12, in which the label corresponds to just one small part of the scene. It should not be surprising that both humans and machines have difficulty in correctly identifying the target class in these cases. But it is not justified to use this as a basis to say that machines and humans are making mistakes in the same kind of way - it is much more nuanced than that. The paper does not adequately address the potential for different error modes between humans and machines, particularly concerning contextual understanding and the ability to focus on specific objects within complex scenes. The analysis lacks a detailed investigation into the specific image features or contextual cues that lead to disagreement, making it difficult to draw strong conclusions about shared failure modes.

4. While the assessment in Fig 6 aims to show the proportion of human-annotated top visual attributes, it is unclear on an instance level how and why humans and artificial models reach (dis)agreement. Take for example the cases where the model makes random kinds of predictions humans clearly would not. For example, Figure 3c is clearly not a roof tile, a scorpion, or a sandal - no human would guess any of those, although they could still be wrong of course. The paper does not provide a clear methodology for analyzing these individual instances of disagreement, nor does it discuss the implications of these qualitatively different error types for the overall conclusions.

### Questions
- It is unclear why the authors concluded from Figure 1 alone that the stimuli causing the most agreement/disagreement among AI systems also cause the most agreement/disagreement among humans. Although the figure shows the agreement levels, it lacks specific information on the stimuli that contributed to such obtained outcomes
- In Table 1, what is the motivation behind comparing the models agreement with the human viewing time and the difficulty score?
- It is unclear why the authors concluded from Table 1 that ObjectNet is more challenging for both humans and the models?
- I would recommend to provide a correlation measure for Figure 5.
- Do you expect any bias in human annotations?
- In Figure 6, How did you determine the visual factors for the models?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper assesses the disagreement among a population of artificial vision systems (1032 models) and compares it with the disagreement among a population of humans (42 human participants). Unlike previous works, populations of agents and humans are compared on a collective level, instead of an individual level. The paper aims to prove that factors that cause disagreement among AI systems coincide with the factors that cause human disagreement, at a population level.

### Strengths
The paper has the following (potentially) strong points: 

1. The paper assesses the overlap between AI vision models and human disagreement on a collective/population level, rather than an individual level. This is an original approach as far as I know. The assumption is that by identifying patterns in how populations of AI models fail similarly to humans, training methods or architectures that handle difficult stimuli could be developed, and thus improve model robustness and interpretability. The proposed many-to-many comparison is something worth considering in the future, alongside already-established measures.

2. This study models the largest population (afaik) of artificial vision models, spanning 1032 AI models with various architectures, pretraining regimes and data. Such a population should provide a comprehensive view of collective disagreement. However, how each of these models influences the collective disagreement is not discussed enough, but could have been a point to add more value to the paper.

3. It aims to uncover and highlight common factors between humans and artificial models of vision that cause difficulty in object recognition.

### Weaknesses
### Quality
#### Problem
- Motivation isn't that convincing - the paper claims that the typical assumption around model errors is "intrinsic to these systems and unrelated to aspects of human visual processing." But that isn't always the case - I think ambiguous images (which seem to be the crux of this paper) are not only known to be difficult for models just as they are difficult for humans, but are easily cited by most researchers as a cause of model error and likely disagreement
  - The paper also claims evidence that "disagreement among AI vision systems is driven by aspects of human visual perception, particularly image difficulty" - it's worth nothing that classifications are a human concept, not an inherent property of the image, and training data reflects that. Maybe the paper isn't directly making this claim, but it seems that it's suggesting there are similar mechanisms between models (at least model populations) and humans that drive disagreement; I'd argue that these images are simply actually ambiguous, the classification is a product of human reaction to ambiguity, the training data is also a product of human reaction to ambiguity, and the model directly encodes that rather than showing an interesting emergent behavior. The paper's claim that models disagree despite being trained on the same labels doesn't fully address this, as the training data itself contains ambiguous examples with varying labels, contributing to the observed disagreement.
- Data on variations of models is limited to a list in the appendix - would be good to be given a structured representation of the variations in a table

#### Results
- Though the correlation coefficients are nontrivial and the figures line up with them, and I wouldn't expect strong correlations for such a high-dimensional problem, the figures do show a lot of spread.
- This also make the results seem less surprising - from both this and figure 6, where we see the factors being "background","pose", "color", "pattern", and "smaller", it seems that the difficult images are simply truly ambiguous. It's not a matter of ML fallibility, but I wouldn't expect it to be. It's also not an underlying surprising mechanism in human vision that makes humans fallible on them. The images are ambiguous and the humans who labeled them probably weren't completely sure what to label them. Even if we call it a shared mechanism/underlying principle of human vision, it's not surprising or unknown.
- It makes sense that agreement increases as overall accuracy increases, but this is really not surprising. It could be that there are cases where models all classify the image as the same wrong class, but just given how training works, it's likely the original image is misclassified (or the original assumption is true). In either case, this doesn't offer an alternative to an explanation to the original assumption.

### Clarity
- Would help to have an explanation of why Fleiss' $\kappa$ is a good measure of agreement, really just intuition on how it works.
- Sections 3.1 and 3.2 don't need to be there - they explain concepts that are immediately clear from the figures.
- More descriptive statistics on the figures would help understand how predictive the results are.

### Originality and significance
- I haven't seen this framing of this problem. However, the concept itself - that ambiguous images are difficult for both humans and models - doesn't seem novel. It also doesn't seem to warrant this much formalization.

### Questions
In light of the previous comments, I think the main actionable points are:
- the motivation of the paper needs to be reconsidered and clarified
- so does the conclusion and interpretation of results, in particular, I would recommend more carefully interpreting the similarities between humans and artificial models.

Further clarification is also needed on:
- Figure 1 -  the interpretation of the histograms for model and human agreement (“histograms along each axis reflect the proportion of images at each marginal agreement level”).  The caption states there is a positive correlation but does not state how this conclusion is reached.  Later on, Table 1 provides some values but the exact method for reaching those values is missing. Visually the histograms do not seem positively correlated, but again clarifying in text would be better.

- Details of the pretraining of each model, or at least grouped per family of models (maybe grouped by architecture type) used in this analysis would have been relevant. Also, further discussion and interpretation of results, again grouped per family of models could have added value to this paper. For example, how do different model architectures contribute to the level of disagreement? 

- Again, for clarity,  it would be good to state clearly how the values for correlation between model agreement and the human behavioural measures (Table 1) are computed. 

- Line 432 - What is this subset of selected models? Based on what criteria were these models selected? 

- Regarding low-agreement images, it would be interesting to assess the factors that cause disagreement at certain levels of accuracy. Are these factors maintained, and what factors remain/are discarded as the acceleration of agreement occurs (as per L440-442)?

Finally, I think a section on the limitations of this study should be included. For example:
- the limited number of human participants might not reflect the full spectrum of human visual perception
- how does approximating perceptual abilities to population disagreement lead to overlooking specific, individual visual factors?
- is Fleiss’ Kappa the most suitable measure and are there any other agreement measures that could be explored instead?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper attempts to establish similarity between artificial and biological vision by showing that populations of AI models and populations of humans show intra-group disagreement on the same stimuli. It motivates itself by claiming that prior work shows disagreement among models being a function of limitations in their development, rather than expressions of an underlying mechanism in both AI and human vision. 

The paper defines agreement as Fleiss' $\kappa$ for an image, calculated over a population of vision systems. It surveys ~40 humans and ~1000 models, trying CNNs, ViTs, and hybrids and varying model size, dataset size, and training methods (pretraining and finetuning). It also uses human minimum viewing time and difficulty score as comparison metrics. 

Results show:
- All metrics appear to correlate with model agreement in intuitive ways - not strong correlations, but significant and all in the intuitive direction
- The clearest relationship is for low-difficulty high-model agreement images 
The paper takes human-annotated visual attributes from the ImageNet-X dataset, in which humans annotated what aspects of an image make it difficult to classify. The paper showed that for both low-human agreement and low-model agreement images, the percent of images with each top difficulty factor shows similar relative influence - the percentage of images for each factor decreases in mostly the same order for both humans and models. The most influential factors are found to be background, pose, color, pattern, and "smaller". 

The paper also shows that model agreement increases as accuracy increases. 

The paper then positions itself against other error analysis-related works, works that use synthetic stimuli to assess differences, and metamers (this being an opposite of a metamer).

### Strengths
### Quality 
- Good problem setup: well-defined, statistical choices make sense, and experiences overall make sense (I will list a couple exceptions in the weaknesses) 
- Good application of ImageNet-X to get systematic error analysis on naturalistic images 
- Comparing to a population of models seems promising

### Clarity
- Writing style is very clear. I rarely felt confused when reading the paper, and the structure made sense.
- Figures are well-designed. They are the most useful aspect for building intuition about the results - they look good, and show the right concepts. 
- Explanation of Fleiss' $\kappa$ helps build intuition for what "agreement" means, and also helps strengthen the experimental design choices

### Weaknesses
Weaknesses of this paper include:

- Some findings are quite intuitive, for example, the correlation between AI (dis)agreement and human (dis)agreement. This probably is due to the labels are created by humans. 

- 42 participants from user study might be a bit bias. May conduct a few more user studies and combine with previous data.

- The image style does not look very good, some images are taking too many spaces but contain relatively few contents.

- at line 402, "Images at low agreement levels are produce...", should be "... are producing..."

### Questions
- I am curious how these experiments would fare for top-5 classification - possibly for humans, not just models 
- In figure 6, how should we factor in the difference in proportions between models and humans, even if the order of proportions is mostly the same? I realize you're not making this claim, but if we want to establish similar underlying mechanisms, we'd need to deal with the differences in proportion for each factor. What might this imply for future studies? 
- "Images at low agreement levels are produce significantly lower Fleiss' $\kappa$ than high agreement and all images, even for models at high performance levels" - I thought that agreement is *defined* as Fleiss' $\kappa$. Am I misinterpreting? Is the point that even when models are split and Fleiss' $\kappa$ is recalculated, it is low for the images that had low Fleiss' $\kappa$ across all models? That would be more meaningful, though continues to point to images that are simply ambiguous.

### Soundness
2

### Presentation
3

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
The paper brings a new point from population-level comparisons between AI and human vision systems, different from the previous individual Ai and human comparison. The authors conduct experiments using a large population of 1032 models and a previous user study with 42 human participants. They use Fleiss' kappa to quantify the level of agreement and find out a few interesting points on the correlation between AI model (dis)agreement and human (dis)agreement. They claim that the low agreement on hard images is due to intrinsic perceptual challenges shared by both AI and humans instead of model structure limitations.

### Strengths
The strengths:

- brings a novel view from population-level comparison of AI and human on vision systems. 

- conduct extensive experiments on a large population AI models

- Interesting findings on AI models not perform well on difficult images due to perceptual challenges that human faces as well.

### Weaknesses
Weaknesses of this paper include:

- Some findings are quite intuitive, for example, the correlation between AI (dis)agreement and human (dis)agreement. This probably is due to the labels are created by humans. 

- 42 participants from user study might be a bit bias. May conduct a few more user studies and combine with previous data.

- The image style does not look very good, some images are taking too many spaces but contain relatively few contents.

- at line 402, "Images at low agreement levels are produce...", should be "... are producing..."

### Questions
- In Fig 1, it is a bit surprising that there are very few images with high human agreement from the top histogram, which means humans rarely have full agreement on images. Could you explain possible reasons behind this?

- If humans and AI cannot recognize the difficult images or the edge-case images, it means vision alone cannot solve the problem and we probably do not have a better solution using only vision. What other benefits could it bring to us if we study more on the difficult images? In other words, how does studying the edge-case images help?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates correlations between populations of humans and object-recognition systems on object-classification disagreements.  The results show that there is significant correlation between human and model population disagreements, as well as between human minimum viewing time and model disagreements.  The results support the hypothesis that this correlation is driven by aspects of human visual perception that makes certain aspects of images difficult to classify.

### Strengths
The experiments seem solid and the results are well-presented.  The authors tested over 1,000 different models, including CNNs, ViTs, and hybrid models.  The paper goes more deeply than just giving correlation statistics, and investigates what features low-agreement images have in common.

### Weaknesses
I'm not sure how useful these results are, either for understanding human or machine vision, or for improving machine vision systems.  A useful result would point in a new direction for experiments (to better understand underlying mechanisms) and/or architectural improvements.  But what are the next steps with these results?  The authors did not address this or make the case that these results are important for the field.  

The paper states: "In this work, we challenge the assumption that disagreement among AI systems is intrinsic to these systems and unrelated to aspects of human visual processing".  But what are the citations for this assumption? 

I didn't understand, in second paragraph, how this assumption "aligns with standard approachs for comparing internal representations of AI and biological vision, such as representational similarity analysis" or how it is "explicit in behavioral extrapolation tests" -- this needs better explanation.

### Questions
The paper states: "AI systems might be more sensitive to background variations than humans and human population are more likely to disagree when pattern variations are present".  Explain what "pattern" refers to here.

When giving models' accuracy on ImageNet and ObjectNet datasets, are you using top-5 or top-1 accuracy?  What about for humans?

Figure 7: What is "Bin Mean Accuracy"?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The article explores the disagreement behaviors of AI vision systems, diverging from traditional approaches that compare individual AI models to biological vision. Instead, this study investigates patterns of agreement and disagreement among a diverse population of AI models by measuring "aggregate disagreement" across model outputs. It aims to determine which inputs produce the most divergent responses among models and assesses whether these inputs also create discrepancies between AI systems and human perception.
A significant finding is that even images causing high disagreement among AI models often align with human perceptual challenges. This alignment suggests that the limitations in AI models mirror similar perceptual difficulties in humans, offering valuable insights into AI-human vision comparisons at a population level. This work contributes to the field by reframing disagreement not as an intrinsic limitation of AI systems but as an opportunity to study the shared perceptual challenges between artificial and human vision systems.

### Strengths
1.Innovative Research Topic:
The authors investigate an intriguing and novel research area by examining AI model and human visual disagreements at a population level. This approach is unique in that it moves beyond individual model comparisons to analyze the collective behavior of AI vision systems.
2.New Method for Measuring Human-AI Discrepancy:
By introducing a method to measure disagreement at the population level, the study provides a new way to quantify the difference between AI models and human perception, adding a meaningful metric to the field.
3.Focus on Naturalistic Stimuli:
Unlike prior work that often uses synthetic stimuli, this study investigates the properties of naturalistic stimuli that elicit the most disagreement among AI models, making its findings more applicable to real-world scenarios.
4.Insights into AI-Human Perceptual Alignment:
The article provides evidence suggesting that disagreements among AI systems are influenced by aspects of human visual perception, particularly in image difficulty, as measured by human behavioral data. This insight supports the idea that individual differences in AI vision systems may reflect differences in human visual processing rather than inherent AI limitations.

### Weaknesses
1.Limited Analysis of Outlier Cases:
The authors report correlations between model agreement and human behavioral measures, but they do not analyze specific cases where model agreement is high but human difficulty is low, or vice versa. Such an analysis could provide deeper insights into unique points of divergence.
2.Lack of Architecture-Specific Insights:
Although multiple model architectures are included in the study, the authors do not analyze how different architectures impact the results. This oversight limits the understanding of how architectural variations might contribute to AI-human agreement or disagreement on challenging stimuli.
3.No Exploration of Methods to Reduce Disagreement:
While the study highlights greater disagreement on images of higher human difficulty, it does not explore whether certain methods, such as targeted model adjustments or expanded training datasets, could reduce this disagreement and improve alignment with human perception.
4.Insufficient Citations of Related Work on AI-Human Disagreement:
Prior research has shown that there are links between AI-human disagreement and human visual processing at the individual model level, yet the authors do not reference these foundational works. Including these citations could strengthen their arguments by situating the study within the existing body of research.

### Questions
1.Did the authors consider analyzing cases where model agreement is high but human difficulty is low, or where model agreement is low but human difficulty is high? Such cases might offer valuable insights into the nuanced differences between AI model behavior and human perception.
2.Although multiple architectures were included, why did the authors not explore the impact of different architectures on the experimental results?
3.Can the higher disagreement on challenging human images be reduced through specific adjustments to models or training datasets?
4.Previous research has shown links between AI-human disagreement and human visual processing at the individual model level. Why were these relevant studies not carefully discussed in the related work section?

If the authors can address these issues, I would be happy to raise my score.

### Soundness
2

### Presentation
2

### Contribution
3
