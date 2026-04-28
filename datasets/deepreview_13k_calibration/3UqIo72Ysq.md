# Representations in a deep end-to-end driving model predict human brain activity in an active driving task

- Decision: Reject
- Avg Score: 4.83
- Scores: 6, 5, 3, 5, 5, 5

## Abstract
Understanding how cognition and learned representations give rise to intelligent behavior is a fundamental goal in both machine learning and neuroscience. However, in both domains, the most well-understood behaviors are passive and open-loop, such as image recognition or speech processing. In this work, we compare human brain activity measured via functional magnetic resonance imaging with deep neural network (DNN) activations for an active taxi-driving task in a naturalistic simulated environment. To do so, we used DNN activations to build voxelwise encoding models for brain activity. Results show that encoding models for DNN activations explain significant amounts of variance in brain activity across many regions of the brain. Furthermore, each functional module in the DNN explains brain activity in a distinct network of functional regions in the brain. The functions of each DNN module correspond well to the known functional properties of its corresponding brain regions, suggesting that both the DNN and the human brain may partition the task in a similar manner. These results represent a first step towards understanding how humans and current deep learning methods agree or differ in active closed-loop tasks such as driving.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates the alignment between human brain activity in the context of autonomous driving and the activations of different modules of a specific deep neural network (Learning from All Vehicles - LAV). Human brain activity was captured in the form of functional magnetic resonance imaging (fMRI), and the alignment was performed through Voxelwise Modeling (VM), previously introduced in the literature. This paper argues that both the deep neural network and the human brain may partition the task of driving in a similar way, by showing that each specific LAV module (semantic segmentation, Bird's-eye-view perception, planning, trajectory prediction, hazard detection, and control) was able to predict different meaningful brain areas.

### Strengths
To the best of my knowledge in this applied field, I believe this work surely pushes forward the intersection of neuroscience and machine learning representation; in this sense, and despite the paper "looking different" from typical ICLR papers, I believe this point is in itself a strength of this paper to be accepted at ICLR. 

The choice of Learning from All Vehicles (LAV), a competitive model in autonomous driving, strengthens this study’s relevance; LAV’s multi-module structure allowed the authors to link specific network modules to brain regions performing analogous roles. Another significant strength of this work is how this work was devised and how it collected all the data from an actual fMRI machine to be able to explore the active driving paradigm, instead of the more usual passive tasks in previous literature. 

In my opinion, this paper is original in its methodological developments and how it tackles a clear gap in the literature with a creative combination of rigorous statistical methods.

### Weaknesses
Even though I really enjoyed reading this out-of-the-box paper, and even though I can imagine the insightful discussions this might bring among people attending ICLR, I am afraid this might not be enough for this paper to be accepted at a conference like ICLR. One key point I want to make on this (beyond the weaknesses I list below), is that I believe that a person from the field of neuroscience would be necessary for properly analysing this paper. Section 4 contains a lot of discussions and results focused on brain regions and specific neuroscientific knowledge that I believe it might be difficult to find in ICLR; evaluating this section seems important to me to really understand the contribution and novelty of this paper, which again supports my point that maybe this might not be the best venue for this paper. A more multidisciplinary journal focused on neuroimaging where truly diverse peer reviewers might be easier to find, might be better.

With regards to actual weaknesses that I have found in this paper:
1. In a conference focused on (computational) representation learning, I find that the dataset size of just 3 people is too small for us to trust these results. In order to avoid data leakage, this basically means that one person would be in the training set, another in the validation set for hyperparameter selection, and another in the test size, which in my opinion hinders the potential trust one has in these results as we might not have enough individual variability in brain function in such a complex task like driving. Even though the paper is clearly innovative in its methodological approach, it also contains a clear weakness in providing enough people to truly evaluate its results. Obviously this is not possible to tackle in the rebuttal period, but I think the authors do not provide enough details on how they consider the dataset (small) size in their experiments, and how potential overfitting was avoided.
2. One thing that I believe it's difficult to really evaluate here, and thus it's a weakness of this work, is that these correlations might not necessarily imply functional similarity. Some correlations might come from shared contextual factors (I can think for instance vehicle proximity or visual field overlap) rather than true alignment. I do not know in detail some of the methods applied in this paper, so I was wondering whether the authors could comment on how to potentially tackle this weakness?
3. The paper makes quite a strong statement when it suggests that both the DNN and the human brain may partition tasks in a similar manner. This in itself is a difficult claim to truly evaluate when only looking at one DNN model. I'm not sure whether other autonomous driving models are divided in such well-separated modules, and thus it would be important for the paper to include some discussion on the feasibility of applying this framework into other autonomous driving models currently being used in the real world.

### Questions
1. Did the authors use one person for each train/validation/test split used in this paper, to avoid data leakage?
2. How difficult and how long did it take to collect this dataset for these 3 people? How feasible would it be to extend this experiment to a larger number of people to more strongly evaluate this work?
3. Given that the fMRI captures delayed blood-oxygenation responses, do the authors think that a higher temporal resolution imaging method like EEG could help? 
4. Isn't the combined $R^2$ of just 0.02 in figure 2 too small to find true alignments between the DNN activations and distinct brain networks? How did the authors choose this value?
5. The paper highlights, in Section 2, some literature connecting fMRI signal with brain activity on driving tasks. Doesn't it mean that the last sentence in introduction ("Our results are an exciting **first step** towards investigating the cognitive and representational basis for human and AI driving") is a bit of an overstatement? (I mean given the usage of the term "first step")
6. In section 3.2.1, the paper mentions some apparent modifications to the original LAV implementation, and that "reasonable inferences" were verified. Can the authors please provide more details on why and how the LAV model was modified, and what "reasonable inferences" mean (eg, how it is defined and evaluated)?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper investigates the relationship between human brain activity and deep neural network (DNN) activations during an active driving task, specifically using a simulated taxi-driving environment. By employing functional magnetic resonance imaging (fMRI) to capture brain activity, the authors construct voxelwise encoding models that correlate DNN activations from the Learning from All Vehicles (LAV) model with brain responses. The findings indicate that DNN features can explain significant variance in brain activity across various regions, suggesting a parallel in how both systems process complex sensorimotor tasks. This work represents a new effort to bridge insights from neuroscience and artificial intelligence, particularly in understanding cognitive processes during active driving.

### Strengths
The paper's strengths are highlighted by its innovative integration of neuroscience with machine learning, providing valuable insights into how DNNs may emulate human cognitive processes during complex tasks like driving. The rigorous experimental design, which includes detailed comparisons between brain activity and DNN outputs, enhances the reliability of the findings. Additionally, the alignment of DNN modules with specific functional brain regions suggests a meaningful correspondence between artificial and biological systems, indicating potential pathways for future research in both AI development and cognitive neuroscience.

### Weaknesses
The findings rely solely on the LAV driving DNN. Testing multiple DNNs trained with different objectives or architectures could strengthen claims about human-AI alignment in driving.

The experiment’s setup, where humans control the stimulus, introduces correlations that may not reflect true alignment in representations, limiting the generalizability of the findings.

While the voxelwise approach is rigorous, the dense presentation and minimal interpretative context might be difficult for a broader ML audience, not sure if ICLR is the best venue for this work.

### Questions
Have the authors considered exploring different DNN architectures (e.g., reinforcement learning-based models) to assess if similar regions align across architectures?

Could further studies investigate other interactive tasks, such as social navigation, to see if similar alignment patterns appear in non-driving contexts?

How might the approach handle potential biases from strong correlations in interactive tasks, and are there additional measures to mitigate this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper presents a comparison between human brain activity, measured through functional magnetic resonance imaging (fMRI), and activations within deep neural networks (DNNs) during an active taxi-driving task in a naturalistic simulated environment. The study aims to enhance our understanding of the similarities and differences between human cognition and current deep-learning methods in active, closed-loop tasks such as driving.

### Strengths
The method is straightforward and easy to understand.

### Weaknesses
This paper focuses on application rather than theoretical innovation. Here are a few questions and considerations regarding the methodology:

The sample size is limited to only three subjects. Is this sufficient to establish a reliable confidence level in the findings?

Why was a deep neural network (DNN) chosen over alternative models? Would other models potentially offer comparable or better insights?

The rationale for using the selected model, such as the VM model, remains unclear. Could you clarify the insights driving this choice?

What methods were employed to assess the credibility and robustness of the model? How can we be confident in its generalizability and accuracy?

### Questions
Please refer to Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this article, the authors present an interesting attempt of aligning the auto-driving neural network with the human brains scanned when driving. This experiment is a new design and allows for the exploration of new topics in the field.

### Strengths
1. The dataset is quite new. 
2. The visualization is clear and neat.

### Weaknesses
1. The sample size is relatively small. I understand the difficulty here and I guess the whole collection is still in the early stage? 
2. The goodness of mapping is not well evaluated. 
3. The comparison with other methods and infrastructure is missing.

### Questions
1. The authors may include more information about data processing and mapping in the supplement. 
2. More details about the quantitative analysis could be included. 
3. The authors may include some comparison with the non-specific encoding models. 
4. How do you align the driving pattern between human and AI? Are they aligned with the same frame or action? As the performance is measured by R^2, is it selective to the current BOLD? What's the difference if you map it to a resting or passive natural stimulus? To what extend is the signal driven by the movement? Some related work could be helpful for the comparison and argument here about the selection and representation, such as:
  [1] https://www.nature.com/articles/s41467-024-53147-y
  [2] https://www.nature.com/articles/s42256-023-00753-y?fromPaywallRec=false
  [3] https://www.sciencedirect.com/science/article/pii/S2095927324001373
  [4] https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Brain_Decodes_Deep_Nets_CVPR_2024_paper.html

### Soundness
3

### Presentation
3

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
This paper studied how the representations in a deep learning model for autonomous driving can predict human brain responses in an interactive close-loop driving task. They recorded human subjects' brain activities using fMRI while they engaged in a driving simulation task. They extracted activations from artificial neurons in the deep network model receiving stimuli similar to human subjects and used these activations to regress against brain activities. They found that overall, the model explains variances of brain responses across many brain regions in held-out data. They further investigated how different modules in the deep learning model, such as semantic segmentation, planning, hazard detection, and control, explain different parts of the brain responses the best. They found that semantic segmentation and hazard detection modules best predict the visual areas, the planning module best explains variance in the sensorimotor areas and IPS, and the control module is similar to the planning module and, in addition, explains variance in RSC and PPA.

### Strengths
This paper studies human neural activities in a complex interactive driving task. It investigates to what extent a functional model of driving—and its different submodules—explains/predicts different parts of the neural data. Many works in the past investigated how deep neural network models align and/or predict neural responses, but most previous studies focused on perception, reasoning/planning, or control separately, and the tasks were usually much simpler. This work studies driving, a complex interactive behavior involving perception, planning, and control. Going from simple, passive tasks to complex, multifaceted tasks has significant originality. Meanwhile, developing capable computational models and comparing different facets of the model to the brain involves a lot of hard work and innovation in methodology, and this work made progress in that direction. The finding that different submodules of the LAV model explain variance in brain responses in different regions is a novel finding and invites further studies to understand the exact functional roles of different brain regions during a complex task such as driving.

### Weaknesses
While the task, model, and analysis methods are novel, it is hard to know what we have learned scientifically from the analysis, mainly due to a lack of control experiments and alternative models. I see the central claims in this paper as the following two points.

1. encoding models for DNN activations explain significant amounts of variance in brain activity across many regions of the brain
2. each functional module in the DNN explains brain activity in a distinct network of functional regions in the brain, ..., suggesting that both the DNN and the human brain may partition the task in a similar manner.

Claim 1 is not novel since it is generally expected that a DNN model can account for variance in neural response, especially when these models are trained to perform the same task. Even randomly initialized DNN models can explain some variance in the brain. Given that, it is essential to see how well the LAV model explains variance compared to other models. Does LAV predict brain activities better in a particular region, or does it predict activities in a broader range of areas? For example, the author can compare the LAV model to those non-DNN models studied by Strong et al., 2024., and it would be helpful to have more DNN control models, such as a CNN trained on ImageNet classification or a randomly initialized CNN model.

While this paper did show that different submodules of LAV explain variance in different brain regions, the claim that the brain and LAV partition the task in a similar manner is only poorly supported. This is primarily due to a lack of clarity on what "partitioned similarly" means. From the presented data, the semantic segmentation and hazard detection modules explain the neural responses in the visual areas. The planning and control modules explain a largely overlapping set of brain regions. These results suggest that the functions performed by these modules are not as clearly segregated in the brain as in the LAV model. Establishing a clear metric to assess whether the brain exhibits a similar functional partitioning as the tested model would be beneficial. This could involve developing a measure of the degree of functional segregation in the model that aligns with brain regions. Adding alternative models or control models would certainly help. For example, there might be a hypothetical model A, whose sub-modules predict all brain regions equally well. Then, it is acceptable to conclude that the LAV model partition is more brain-like than model A.

Additionally, while this paper mainly focuses on analyzing the neural data, it does not provide any behavioral results. It is hard to see the model as a good model of the brain if it does not perform the task well or does not match human behavior well. It would be helpful to see how well the LAV model is aligned with humans behaviorally. For example, the navigation decisions between the LAV model and human subjects can be compared when given the same simulator inputs.

### Questions
1. How well does the LAV model explain brain responses compared to non-DNN baseline models, such as those studied in Strong et al., 2024.
2. How well does the LAV model explain brain responses compared to other DNN models? For example, some basic baseline DNN models, such as an ImageNet-trained CNN. Or some alternative driving DNN models.
3. How can we more rigorously measure whether a computational model and the brain partition the task similarly?
4. How well does the behavior from the computational model align with human behavior?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on the alignment between deep learning models and brain activity. Unlike previous studies, which examine the alignment of visual or language models with brain activity, this work explores a deep learning model for autonomous driving. Specifically, the paper utilizes the LAV model, which has clearly separated functional modules, including semantic segmentation, bird's-eye view perception, planning, trajectory prediction, and hazard detection. The outputs from each module demonstrate varying predictive capacities across functionally distinct brain regions.

### Strengths
The topic comparing the brain activity to a autonomous driving model is quite new to the field which can be insightful for understanding the brain activity during planing, decision making. The submission collects the data with this new system is a good start point for the following research.

### Weaknesses
Though the topic is new, mapping an autonomous driving model with distinct functional modules to different brain regions is promising, but the current results are not yet strong enough. For instance, the control module outputs show high predictive ability across multiple brain regions, it would be beneficial if the authors could demonstrate whether these regions are consistent across random sees, subjects and providing some statistical significance measure.

Additional concerns are as follows:

The authors performed regression analysis to align LAV model outputs with brain activity. It would be helpful to clarify whether the observed distinct predictive abilities are specific to the LAV model or if they generalize across other autonomous driving models, such as that proposed by Li et al., 2024 [1].

Predictive ability is a coarse measure, as it only indicates that the variability in model outputs aligns with the variability in brain activity. This makes it difficult to draw conclusions such as "representations learned by the driving DNN may be similar to those used by the human brain." The authors could explore additional metrics beyond regression fitting to better align brain activity, such as fMRI, with artificial neural networks. A discussion on the impact of metrics on alignment-related conclusions would also be beneficial [2].

While the topic is interesting, current technical contribution is not very significant.

### Questions
1. What is the variability across subjects? When the authors mentioning the group-level performance, does that mean average across subjects?

2. How does the random projection matrix affect the results?

3. Is there any statistical measure quantifying the significance of the better predictive ability of one brain region compared to other regions?

### Soundness
2

### Presentation
3

### Contribution
2
