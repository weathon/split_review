# HOI-Diff: Text-Driven Synthesis of 3D Human-Object Interactions using Diffusion Models

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
We address the problem of generating realistic 3D human-object interactions (HOIs) driven by textual prompts. 
To this end, we take a modular design and decompose the complex task into simpler sub-tasks. 
We first develop a dual-branch diffusion model (HOI-DM) to generate both human and object motions conditioned on the input text, and encourage coherent motions by a cross-attention communication module between the human and object motion generation branches. 
We also develop an affordance prediction diffusion model (APDM) to predict the contacting area between the human and object during the interactions driven by the textual prompt.
The APDM is independent of the results by the HOI-DM and thus can correct potential errors by the latter. 
Moreover, it stochastically generates the contacting points to diversify the generated motions.
Finally, we incorporate the estimated contacting points into the classifier-guidance to achieve accurate and close contact between humans and objects.
To train and evaluate our approach, we annotate BEHAVE dataset with text descriptions.
Experimental results on BEHAVE and OMOMO demonstrate that our approach produces realistic HOIs with various interactions and different types of objects.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper address the problem of text-driven 3D human-object interaction synthesis. The task is decomposed into simpler sub-tasks, i.e., human and object motion generation, affordance estimation and affordance-guided interaction correction. A dual-branch diffusion model (DBDM) is developed to generate the coarse human and object motion. Then, an affordance prediction diffusion model is designed to predict the contacting area between the human and object. Finally, the estimated contacting points are incorporated into the classifier-guidance to achieve accurate and close contact between humans and objects. Experiments on BEHAVE and OMOMO show realistic HOI generation results.

### Strengths
1. The topic of text-driven HOI synthesis is of large importance in the community;
2. The annotation on BEHAVE is beneficial for the community;
3. Experimental results show the effectiveness of the proposed method;
4. The paper is well written and organized.

### Weaknesses
1. The motivation of decomposing HOI synthesis into simpler sub-tasks is not clearly elaborated, which should be discussed. Why the model generate a roughly coherent HOI motion at first rather than directly generate a high quality HOI motion?
2. The authors claim that the text-driven 3D HOI synthesis with a diverse set of interactions is under-explored and existing datasets lack either HOIs or textual descriptions. However, many works have been proposed for this task such as CG-HOI and CHOIS. They also annotate the BEHAVE dataset with textual descriptions or build 3D HOI dataset with textual descriptions, such as OMOMO. The claim should be modified in the introduction section;
3. The authors claim that the model can produce physically plausible results, yet no physical constraints are integrated to guarantee that. And based on the visualization results, the physical constraint cannot be kept, mainly due to the dataset.

### Questions
My main concerns lie in the motivation of the paper, the claim of the introduction and the physical constraints of the generated results. If the concerns are well addressed, I am willing to raise my rating.

### Soundness
3

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
5

### Summary
This paper presents a text-driven human-object interaction generation method with a modular design. The proposed method includes three steps, a dual-branch diffusion, an affordance prediction diffusion model, and the refinement stage. Firstly, the dual-branch generates a coarse human-object motion. Then the affordance prediction diffusion model predicts the contacting points. Finally, the refinement stage refines the coarse human-object motion by the contacting points. In the experimental section, the proposed method is evaluated on public datasets, BEHAVE and OMOMO.

### Strengths
Here I highlight the strengths of the paper:

1. The modular design that starts with a coarse grain and refines to a fine grain is valuable for human-object interaction generation.
2. The ablation study is sufficient to prove the effectiveness of the proposed method.
3. The presentation of this paper is clear, especially the pipeline of the proposed method.

### Weaknesses
Although the coarse-to-fine modular design is valuable, this paper only considers the contact between body parts and objects. This method neglects the important contact between hand and object in human-object interaction. Here, I highlight my concerns.

1. Lack of citations and discussion of related work. Most of the methods cited and compared are those before 2023. There are a lot of related works that appear in 2024, such as [1,2,...]. These new works should be discussed and compared.

[1]CG-HOI: Contact-Guided 3D Human-Object Interaction Generation
[2]HOIAnimator: Generating Text-prompt Human-object Animations using Novel Perceptive Diffusion Models
[3]InterFusion: Text-Driven Generation of 3D Human-Object Interaction
[4]Controllable Human-Object Interaction Synthesis
[5]F-HOI: Toward Fine-grained Semantic-Aligned 3D Human-Object Interactions

2. The hand-object interaction modeling is neglected. The proposed method only models the contacting points between body parts and the object, which is very coarse-grained for human-object interaction. This causes the method to generate effect distortions in the contact area between hand and object. 

3. The compared methods are almost all human motion generation methods; only InterDiff is a human-object interaction generation method. There is a lack of comparison of human-object interaction generation methods, making it difficult to evaluate the effect of the proposed method in this domain.

### Questions
1. In the Line 256~257, why consider these 8 body joints? And which eight? Only five are listed in the paper.

2. In the experiment section, most of the metrics are general human motion generation metrics, only the contact distance is for human-object generation. Why not use the metrics of InterDiff for human-object generation, such as MPJPE-H, Trans. Err, Rot. Err, MPJPE-O. Otherwise, it is difficult to measure the effect of the method on human-object generation.

3. Why are the hands barely moving? They look flat.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper focuses on generating realistic 3D human-object interactions (HOIs) driven by textual prompts using a dual-branch diffusion model (DBDM) and an affordance prediction diffusion model (APDM). It introduces a novel method to estimate contact points and ensure accurate interactions between humans and objects, enhancing the realism and diversity of the generated interactions. The approach is tested on the BEHAVE and OMOMO datasets, demonstrating its effectiveness in handling dynamic objects and generating physically plausible interactions that align closely with textual descriptions.

### Strengths
The use of a dual-branch diffusion model combined with an affordance prediction model allows for accurate and diverse generation of human-object interactions, addressing the complexity of such tasks effectively.

The model demonstrates superior performance on standard metrics against baseline models, particularly in generating interactions with unseen objects, which showcases its robustness and ability to generalize across different scenarios.

### Weaknesses
The model's performance heavily relies on the quality of datasets like BEHAVE and OMOMO. If these datasets are limited or biased towards specific types of interactions, the model's generalization ability may be compromised. I request authors to test the model with completely unseen objects not included in the BEHAVE or OMOMO datasets. For example, using a text-to-3D related model [1] to create a new object and showing inference results for that object.

The qualitative results show that, while the output aligns with text better than the baselines compared with, the generated result can still be physically implausible despite the introduction of Affordance Prediction Diffusion Model, for eg, objects can be seen floating/being carried without enough contact to hold them in place. Also significant penetration is visible between the body and object, but to a much lesser extent than the methods compared against. I'd like to ask authors if they have any plan to add a loss function (e.g. contact loss) especially designed to this issue. Also, I think more sophisticated metric for measuring the penetration, such as "Intersection Volume," needs to be included to properly check the "physical plausibility of the motions". The measure is basically calculated for penetrated volumes; for details on relevant metrics, consider referring to the paper: Physics-aware Hand-object Interaction Denoising. CVPR 2024.

Thanks for updating the Table 1 reflecting the penetration measure; however I was bit disappointed by the fact that the proposed method is actually less competitive than other methods, in terms of penetration. I think penetration is very important aspect, especially in the HOI generation. However, I do not think the derived method is properly tackling the aspect.

Also, thanks for including the unseen generation cases in the results. However, I cannot see that the proposed method outperforms other methods especially in the unseen object cases. Also, I request authors to reason why the proposed method is better in such generalization cases than others.

However, I cannot easily follow the argument here yet, "our approach leverages pretrained priors to generate smooth human motions, which can exhibit strong generalization capabilities". Especially, I think it may require thorough ablation studies for `Ours w/o pretrain' in unseen settings.

### Questions
None

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
4

### Summary
This paper introduces a novel approach for generating realistic 3D human-object interactions(HOIs) based on textual prompts and object geometry. The authors propose a modular design that decomposes the task into simpler sub-tasks: a dual-branch diffusion model(DBDM) for generating human and object motions, an affordance prediction diffusion model(APDM) for estimating contact information, and classifier-guidance mechanism for correcting interactions to ensure accurate contacts. Additionally, the authors annotate the BEHAVE dataset with text labels to enable the training of models. The method is evaluated on both the BEHAVE and OMOMO datasets, with results showing the ability to produce realistic and diverse HOIs with different types of objects.

### Strengths
1.	The novel decomposition of the complex task into sub-tasks allows for specialized models to handle different aspects of the problem, and the integration of them brings better performance in generating HOIs.
2.	The authors manually annotate the BEHAVE dataset with text label, which extends the HOI dataset with language modality and enables downstream tasks such as text-to-hoi generation, motion captioning, etc.
3.	The authors conduct various experiment to validate the effectiveness of the method, and also perform generalization test on the unseen OMOMO dataset.
4.	The paper is well-written and easy to understand.

### Weaknesses
1.	The R-precision, FID and Diversity metric only evaluate the human motion with the text prompt, rather than the whole generated HOI, which cannot comprehensively measure the quality of the generated HOI. The Contact Distance alone only measures the quality of generated contact. Is there any additional metric that could assess the full HOI? For example, whether the human penetrates with objects could be evaluated by Interpenetration Ratio metric. I hope the authors could provide more effective metrics and perform some evaluation on them. 
2.	Also, the R-precision value is far too low in comparison with the ground truth(and also other T2M works, for example, MLD achieves 0.796 in R-Precision@3 in HML3D test set), which may indicate the inconsistency between text prompt and generated HOI. Would you please explain why this occurs and some possible solutions? And I’d like to see some comparisons with more recent Text2HOI works such as Controllable HOI(Jiaman Li, et al).

### Questions
1.	What’s the feature extractor you used in the evaluation? Did you re-train them or just use the original feature extractor (Guo et al.,  2022)?
2.	Is the affordance in APDM estimated for the whole HOI sequence or for every single frame?
3.	In the affordance estimation stage, you only consider eight body joints for contact. Is this enough for modeling the HOI process? For example, one may kneel on the yoga ball with his knees, which are not included.
4.	Does the model generate constant motion length (as mentioned in L335)?

### Soundness
4

### Presentation
3

### Contribution
3
