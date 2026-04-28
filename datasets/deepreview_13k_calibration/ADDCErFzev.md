# Manipulating dropout reveals an optimal balance of efficiency and robustness in biological and machine visual systems

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
According to the efficient coding hypothesis, neural populations encode information optimally when representations are high-dimensional and uncorrelated. However, such codes may carry a cost in terms of generalization and robustness. Past empirical studies of early visual cortex (V1) in rodents have suggested that this tradeoff indeed constrains sensory representations. However, it remains unclear whether these insights generalize across the hierarchy of the human visual system, and particularly to object representations in high-level occipitotemporal cortex (OTC). To gain new empirical clarity, here we develop a family of object recognition models with parametrically varying dropout proportion $p$, which induces systematically varying dimensionality of internal responses (while controlling all other inductive biases). We find that increasing dropout produces an increasingly smooth, low-dimensional representational space. Optimal robustness to lesioning is observed at around 70% dropout, after which both accuracy and robustness decline. Representational comparison to large-scale 7T fMRI data from occipitotemporal cortex in the Natural Scenes Dataset reveals that this optimal degree of dropout is also associated with maximal emergent neural predictivity. Finally, using new techniques for achieving denoised estimates of the eigenspectrum of human fMRI responses, we compare the rate of eigenspectrum decay between model and brain feature spaces. We observe that the match between model and brain representations is associated with a common balance between efficiency and robustness in the representational space. These results suggest that varying dropout may reveal an optimal point of balance between the efficiency of high-dimensional codes and the robustness of low dimensional codes in hierarchical vision systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper use dropout as an approach to control the sparsity of neural representation in deep neural network (AlexNet), and evaluated the robustness of the resulting networks to lesions to one of the layers. The dropout rate of 0.7 was found to be most robust to lesion at inference time. Coincidently, at this level of dropout, the geometry of neural representation in the same layer also shows the highest correlation to the neural representational geometry to a set of COCO dataset images, in occipitaltemporal cortex of human. Further investigating the rate of decay in the eigenspectrum of the brain region and those of DNNs with different dropout rates, the decay rate of the model with 0.7 dropout rate also matches the decay rate of the human brain. Together, the result appears to suggest that, if dropout rate can be considered as a valid way of controlling for the sparsity of neural encoding, then perhaps the brain chooses its level of sparsity at a level most robust to lesioning of "neurons".

### Strengths
The result shows a high consistency among three results: the dropout rate yielding the highest robustness of the DNN against high-level lesion, the dropout that yields neural representation best matching that of the object-recognition related brain region, and the the dropout rate yielding the same decay rate in the eigenspectrum of the covariance structure of fMRI spatial patterns across images.

It used a novel approach to separate the spatial covariance structure due to potentially noise and that due to signal in fMRI activity

### Weaknesses
Although the decay rate of eigenspectrum is an intuitive way of showing the effective dimensions being used to encode stimuli, I still feel there is a lack of direct demonstration of the level of sparseness resembling the orientation tuning example in Figure 1A. If indeed the neural network learns a sparse coding, I suppose you will find that the number of positive responses in the relu6 (or a layer that the authors consider appropriate) at inference stage varies according to the dropout rate at training time, or at least the number of units showing response above a threshold (not necessarily zero) should show such a dependency on dropout rate.

The robustness drop due to lesion at inference time only appears apparent at very high level of lesion. What is the implication of this for the brain: do we expect that such level of unexpected inactivation of neurons is common for our object recognition regions, so that it is necessary to adjust the region's selection in the continuum between sparse and distributed coding?

### Questions
Although the GSM is not a focus in this paper, I think in principle it is not guaranteed that the subtraction of the empirical noise covariance matrix from data covariance matrix results in a positive definite matrix. In other words, the eigenvalues can be negative. So I am worried that this approach is not generalizable if any readers want to test the hypothesis of this paper on other neural networks.

Although AlexNet only applied dropout to the two layers investigated here, in principle it can be applied to any layer. One natural question is how dropout at earlier layers influence the coding scheme at the layer of investigation.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a neurobiological link between dropout, a common ML regularization method and human brain processing. 

Key findings include:
* There was a reduction in object representation dimensionality with increased dropout levels for NNs
* NN performance was relatively consistent across different levels of dropout, first monotonically increasing and then monotonically decreasing
* Representational trajectory analysis revealed most differences in the fully connected layers where dropout was applied 
* Dropout mitigates effect of [neuron] lesioning, but to a limited extent
* A model that was most robust to [neuron] lesioning (dropout p=0.7) mostly closely matched human brain representations obtained from an FMRI study and evaluated using Representational Similarity Analysis (RSA).

### Strengths
The paper introduces a systematic analysis of dropout and [neuron] lesioning with a neuro-biological perspective in mind. Experiments highlight interesting and novel findings with respect to model variations due to dropout and newly discovered connections to human brain processing. Overall, the paper makes advances in understanding spectral properties learnt by humans and neural networks.  

Authors explain the limitations of their work in terms of considering only one type of regularizations.

### Weaknesses
The paper would benefit from more clarity and better organization. It was somewhat difficult to understand key components of the paper. For instance, the definition of “lesioning”, i.e., pruning neurons in an NN layer, which is central to the paper message, is found in a figure caption (Figure 2), but should appear in the main paper. 

Specific points:
* It is not clear how the layer for lesioning (relu6) was selected or whether results will still hold if a different layer would be selected. 
* Results are reported using a single architecture (AlexNet), and may not generalize to other NNs. Also, the statement in the beginning of conclusion “schemes within a family of deep neural network (DNN)” needs to be adapted to better reflect the type of networks considered. Specifically, here family seem to refer not to architecture variations, but changes in the level of dropout within an architecture. 
* Authors should discuss the significance of the reported findings for the ML community. I thought that many of the reported analyses were cleverly executed, but I struggled to understand the main message behind the paper.

### Questions
I did not understand why human responses were compared to network responses but using different datasets (as discussed in section 2.4, human fMRI was obtained using Natural Scenes Dataset and compared to results on ImageNet using networks)? Authors should either explain the motivation of not running networks on the Natural Scenes dataset to match human fMRI, or report results using a single dataset.

It would be useful to understand the effect of dropout on the trajectories from representational trajectory analysis reported in Figure 1B. Specifically, is it dropout that induces the highest variation in the fc layers, or the underlying network architecture?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To understand the trade-off between high-dimensional and uncorrelated efficient codes and distributed codes known better for generalization and robustness, the authors trained a family of object recognition models with parametrically varying dropout proportions. They found that a higher proportion of dropouts results in more smooth and low-dimensional representational space, with 70% of dropouts offering optimal robustness (against simulated brain lesions). Interestingly, this is also associated with the highest degree of emergent brain alignment for fMRI data in humans. Furthermore, the match between the model and brain representations is associated with a common balance between the efficiency of a high-dimensional code and the robustness of a low-dimensional code.

### Strengths
The idea and approach are simple, and the results are compelling and conceptually reasonable. The study illuminates the relationship between sparse codes and distributed codes. Using simulated lesions to evaluate robustness is an interesting innovation. The paper is well written. The presentation is clear and well-organized. The best alignment between human fMRI representation and of the representation of the model with the greatest robustness is very interesting, suggesting robustness, in addition to efficiency, is indeed a very important criterion for learning brain representation. So, the study does provide insights into the brain. I rank this an acceptable paper, with "grade" somewhere between 6 and 7, so I round it up to 6, because there is no "7".

### Weaknesses
The idea seems obvious and intuitive, and the approach and the work are perhaps too simple.  
The work is most empirical and does not have much theoretical analysis.

### Questions
While it is still fantastic to prove empirically a simple and intuitive idea is true elegantly,  is it possible to show this analytically?  What would be the analytical approach?

### Soundness
3 good

### Presentation
4 excellent

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
In this study, the researchers manipulated the degree of dropout in AlexNet, and then computed the eigenspectrum of the population responses in fc6, following Stringer, 2019. The results showed that increasing the degree of dropout reduced the representational dimension in fc6 and that dropout=0.7 achieved the best test results during the inference process. The authors also computed the eigenspectra of voxel responses in human visual cortex using NSD data and found that it was similar to AlexNet at dropout=0.7, while the correspondence between fc6 and voxel responses was strongest at dropout=0.7.

I am generally positive about this paper. It replicates the analysis of mouse V1 data in human fMRI data.

### Strengths
1. Using a large-scale fMRI dataset and computational analyses to address the coding principles of human visual cortex
2. A novel approach is developed to estimate the signal correlation matrix and and the noise correlation matrix in population responses

### Weaknesses
1. In Figure 1, I am not sure why dropout was only implemented in fc6 and fc7 in model training? In a typical training, dropout was applied to all layers. It would be helpful to understand the specific rationale for limiting dropout to these layers, especially given that other layers might also benefit from regularization.
2. I am wondering about the results of fc7 using the similar analysis in Figs. 2&3. Given that fc7 is also a fully connected layer and is directly connected to fc6, it is important to examine whether the observed effects are specific to fc6 or are also present in fc7. This would help to clarify the layer-specific nature of the findings.
3. In Figure 2, dropout=0.5 is the best in terms of top-5 ImageNet accuracy (Fig. 2A) but dropout=0.7 is the best in terms of accuracy with unit lesion (Fig. 2D). It is debatable what exactly the criteria we emphasize when talking about coding efficiency. The discrepancy between these two metrics raises questions about the interpretation of 'coding efficiency' and which metric is more relevant for the study's conclusions. It is important to discuss this trade-off more thoroughly.
4. In Figure 3, how many voxels and how many fc6 units are used? I suspect that the numbers are very different. The large difference in dimensionality between the fMRI data and the neural network layer could potentially influence the results of the representational similarity analysis. It is important to quantify these differences and discuss their potential impact.
5. The original study by Stringer, 2019 only recorded neurons in mouse V1. However, the ROI used here included several low- and high-level cortex. Do you expect the eigenspectrum to be different across visual areas in humans. Actually, I would say that this is the novel point to make compared to simply replicating the analyses in Stringer, 2019. The analysis should explicitly address the potential differences in eigenspectra across different visual areas, as this could provide insights into the functional organization of the human visual cortex.

### Questions
1. In Figure 1, I am not sure why dropout was only implemented in fc6 and fc7 in model training? In a typical training, dropout was applied to all layers
2. I am wondering about the results of fc7 using the similar analysis in Figs. 2&3
3. In Figure 2, dropout=0.5 is the best in terms of top-5 ImageNet accuracy (Fig. 2A) but dropout=0.7 is the best in terms of accuracy with unit lession (Fig. 2D). It is debatable what exactly the criteria we emphasize when talking about coding efficiency.
4. In Figure 3, how many voxels and how many fc6 units are used? I suspect that the numbers are very different.
5. The original study by Stringer, 2019 only recorded neurons in mouse V1. However, the ROI used here included several low- and high-level cortex. Do you expect the eigenspectrum to be different across visual areas in humans. Actually, I would say that this is the novel point to make compared to simply replicating the analyses in Stringer, 2019.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
