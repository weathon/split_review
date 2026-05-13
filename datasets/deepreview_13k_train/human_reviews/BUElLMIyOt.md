# SMPLy Private: From Masks to Meshes in Action Recognition

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
In this paper, we introduce Mask2Mesh (M2M), a novel privacy-preserving data augmentation framework that effectively bridges the realism gap seen in synthetic-based action recognition methods. Traditional privacy-enhancing techniques, such as feature masking and synthetic data supplementation, tend to degrade data quality and reduce model performance. In contrast, our method leverages the SMPL-X model to replace real humans with detailed 3D meshes in video data, preserving the subtle nuances of human movement and expressions that are crucial for accurate action recognition. By augmenting real data with superimposed meshes, M2M simplifies both pre-training and fine-tuning processes, without introducing the overheads and biases typically associated with synthetic data. Empirical results show that our approach achieves performance within 0.5\% of models trained on unmodified video data, proving that overlaying meshes leads to no significant performance loss in action recognition tasks. This work presents a practical solution for data anonymization without compromising accuracy, offering valuable insights for more efficient and scalable video data processing techniques in computer vision and action recognition.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a method attempts at mitigating private attribute information in video by converting humans into 3D meshes. This approach utilizes various off-the-shelf models, starting with human segmentation, followed by replacing segmented humans with 3D meshes and inpainting to remove the original RGB humans. Additionally, it incorporates object information by leveraging another segmentation model.

### Strengths
- The paper features clear writing and well-illustrated figures, making it easy to follow.

- The diversity and quantity of action recognition datasets used are commendable.

### Weaknesses
 - **W1**: A primary concern is that the method contradicts the goal of privacy preservation by anonymizing video with minimal computation, which is essential for deployment on edge devices before transmitting anonymized content to the cloud computation or storage. The anonymization should require less computation than the utility model (e.g., VideoMAE used here). However, the proposed method employs multiple off-the-shelf models- video inpainting, object detection, and SMPL-X, and their combined computational load significantly exceeds that of the utility model. This compromises privacy by exposing private attributes to these models and makes edge computing infeasible.

- **W2**: Another key concern is the lack of evaluation for privacy protection to quantify privacy leakage. In the main comparison Table 1, the method appears to assume that it inherently resolves privacy issues. While 3D meshes might seem to avoid privacy risks at the human perception level, the essential measure is computer perception, which all prior work evaluates [a,b,c,d]. The method should follow standard privacy evaluation protocols, such as training a classifier to detect private attributes from the 3D-mesh-transformed VISPR image dataset, thus quantifying privacy leakage. The results would then indicate whether or not the private attributes are effectively anonymized.

- **W3**: Another limitation is that the approach is restricted to human-related private attributes only. Prior works like [b,c,d] address a broader range of personal identifiable information, including scenes and objects. While this is not a central evaluation point, the authors should acknowledge this as a limitation.

- **W4**: The results on the Diving48 dataset are notably low- 66%, significantly below comparable baselines like TimeSformer-L (81%) and the state of the art at approximately 91%. I strongly recommend that the authors address this low baseline, as the current claims may be misleading. Diving48, as a fine-grained action dataset, includes fast-moving objects where even minor errors in input modalities substantially affect classification performance. It is well-established that 3D meshes are not ideal for representing fast-moving objects, and this is a fundamental limitation of the approach, given its reliance on individual off-the-shelf components that can propagate errors.

### Questions
While the method introduces a novel approach to privacy preservation, it has fundamental flaws in its formulation. Specifically, it undermines the objective of efficient and feasible anonymization relative to the utility branch. Furthermore, the absence of quantitative evidence on privacy leakage reduction is concerning. In its current form, I am inclined to recommend against accepting the paper. To address these issues, it would be beneficial for the authors to respond to the following weaknesses (see weakness section for more details):

W1: Provide FLOPs for both the anonymization process and VideoMAE, and compare with prior work [a-d].

W2: Adhere to the privacy protocols established in prior work using the VISPR dataset, and include a detailed analysis. Additionally, provide experimental implementation details.

W3: (Optional) Report results on non-human privacy attributes as well, as done in [b, d].

W4: Improve the baseline on Diving48 and base conclusions on the revised results.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present a privacy-preserving augmentation framework that replaces human subjects with realistic 3D meshes. The method effectively mitigates bias and privacy concerns related to the human subjects without reducing the utility performance. The paper provides insight to how this replacement affects pretraining and finetuning stages. The authors additional propose a class sampling procedure to guarantee diverse classes for efficient training.

### Strengths
1. The motivation and high-level ideas for this work is very strong. It makes a lot of sense that replacing diverse humans with a standardized subject would alleviate many privacy and bias concerns.
2. Results seem fairly strong and back up major claims about utility. 
3. The point that using this augmented data can increase learning speed is moderately interesting.

### Weaknesses
1. There is no measure of privacy-utility tradeoff in Table 1. While replacing the human entirely is a strong form of privacy-preservation, it is not sufficient to just assume perfect privacy in this scenario. For example, a model may still be able to perceive gender through analyzing motion patterns, not just appearance. It would be helpful to see a quantitative tradeoff that can be used to compare between methods. The reported cMAP scores, while improved, do not clearly demonstrate that the classifier is unable to learn the correct attributes, but rather that it is choosing the wrong one. The goal of privacy-preserving methods is to reduce attribute inference to random chance, not specifically to cause the classifier to choose the wrong prediction. A more thorough analysis of how the classifier is being 'fooled' is necessary.
2. The K-NEXUS clustering algorithm is comprehensive and potentially interesting, but feels like an unnecessary contribution. I understand why it is effective, but a fair comparison would be using the same subset of classes as previous works. If the goal is not a direct comparison with prior work subsets, then why use a subset to begin with? Computation? Additional details to clarify these points would be useful. It is still unclear whether the performance improvements stem from the selected subset or from the M2M augmentation. A comparison using a subset from a previous work, but with the proposed augmentation, would provide more clarity. The original motivation for selecting a Kinetics subset in SynAPT was to balance it out with the size of their pretraining dataset for a more fair comparison. This class selection makes for an unfair comparison with prior methods.
3. One of the major claims is 'faster learning speed' in Section 4.4, which sounds useful, but this may be offset by preprocessing computation time. The claims about computational efficiency are contradictory, stating that the pipeline is designed for robust computational systems while also highlighting efficiency in resource-constrained environments. This makes it difficult to see the benefit of faster training.
4. Only one architecture/training setup (VideoMAE ViT-B) is shown, so it's hard to tell if the same findings would apply to more architecture types/training styles. Additional experiments would better support the paper claims. While MAE pretraining is standard, it would strengthen the analysis to consider alternate forms of models and pretraining (contrastive for example).
5. It seems like the human detection occurs framewise (Section 3.2, Line 211). This may result in some unnatural videos if some frames miss a detection. It may be more natural to choose a video segmentation model to propagate masks instead of relying on many separate detections. The tennis GIF in the supplementary did look pretty good, but it would be more convincing to see video results from more complicated scenes. The potential for missed detections during human removal may lead to unnatural or jittery movements, particularly when residual artifacts persist across frames. This limitation should be explicitly discussed, along with examples.
6. The overall technical contribution feels weak here. The dataset construction is interesting, but as far as I can tell, there is no unique method proposed that goes with it, just basic MAE pretraining/fine-tuning. The proposed contributions appear disjoint, not building off each other in a real sense, other than just both slightly improving performance from different perspectives. The technical novelty is slim without comprehensive analysis of each component. More comprehensive evaluation related to K-NEXUS design choices, outputs, and justification of claims about the benefits of selecting the subset would help.
7. On the minor side of things, the ICLR format mandates the table number and caption appearing before the table, not after.

### Questions
1. In Line 251, how are the segmentation masks for each object acquired, including the human subject? The text references a method specific to the human subjects, but not objects. Is there a separate segmentation model you use, so you would have two masks for each human? Please clarify this.
2. Can the authors provide some computation/runtime analysis for the preprocessing steps? How long does it realistically take for a single video, maybe like 10 sec/300 frames?
3. For K-NEXUS, since you are already using a LLaVA encoder, why not use the text encoder to encode the class names? In theory, the class videos and text names should have similar representations. It would be interesting to see a comparison between the classes chosen using the visual representations vs. the textual representations.
4. What is the difference between SMPLy Priv and SMPLy Priv w/ K-NEXUS? Is without a disjoint set of 150 random classes? So not just the K-NEXUS classes were annotated, but a separate set of classes as well? Please share more information on these classes, there is no list of selected classes anywhere in the paper or supplementary material.
5. See W5, is there anything done to handle disjoint human detections in the videos? Additional qualitative videos for multi-human scenarios would be helpful.
6. Line 323-324: "with SMPLy Private and the use of our M2M-augmented dataset..." What exactly is SMPLy Private then? I was under the impression that the dataset was the contribution and the model was VideoMAE.
7. How do you define 'male-biased' and 'woman-biased' classes in Table 3? How many of each are chosen/what chooses them? Why not just look at subclass performance across all classes? More details here would help justify this experiment. 
8. Following up with Q6, what is the difference between the male, female, and neutral meshes (Table 3)? This is likely described in a previous paper, but it is an important detail to these findings and more detailed explanations of these is necessary for this paper.
9. Line 52: Claim (2) references that the paper explores the potential for mitigating background and scene-object related biases, but I don't see any further explanation for background/scene-object interactions. Is there additional support for this/performance on bias-related benchmarks?

### Final Thoughts
Overall, I truly believe this paper has a lot of potential, but I would not recommend it for acceptance in its current state. The core ideas are strong, but there are a lot of details that need clarifying. A solid technical contribution for better learning with these meshes instead of using basic MAE pretraining would definitely flip my rating for this paper.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
SMPLy Private proposes a new way to pre-train an action recognition model for privacy-preserving purposes. It leverages human meshs extracted from the Kinetics dataset to replace the real human subjects in the videos, removing human-specific visual biases during pre-training. Previous methods tend to approach privacy-preservation by distorting or augmenting the visual data itself, hindering model performance and creating a gap between augmented/synthetic training data and real-world downstream data. M2M solves this by replacing human subjects with their meshes, retaining important action information and the surrounding visual information while removing personal attributes. They also propose a modified k-means clustering algorithm to train on a subset of Kinetics with minimized inter-class similarity. They provide extensive experiments and some ablations to support their proposed work.

### Strengths
- The idea to replace humans with their meshes to remove private attributes is an intuitive and effective solution to the proposed problem of privacy-preserving action recognition.
- Their quantitative improvement over PPMA in Table 1 (and other baselines) are significant.
-Their K-Nexus curated dataset seems to contribute to their method/training objective and is a more direct way of reducing action class bias than random sampling (used by previous methods).

### Weaknesses
 - The paper is not very clearly written. For example. their methodology section describes each component, but it is difficult to understand how each component is exactly used during training. It is only after looking at Table 1 that it is clear M2M is used during both MAE training and alignment, which could be addressed in Section 3.3. 
    + Table 2 is similarly difficult to understand: what does each row represent? It would seem the caption is meant to correspond each row to the order in which the methods are discussed, but this seems incorrect (OSX is first but it does not use just segmentation). 
    + It seems their writing structure follows closely with PPMA, which itself is not a major issue, but M2M is much more difficult to follow and seems to leave out more of the contextual and background information that PPMA provides. I had to first read PPMA to understand the problem formulation and their solution, then refer back to M2M to fully understand the method. On a similar note, Table 1 is the same as Table 1 in PPMA - are there no other baselines to consider in this table? Surely other privacy-preserving methods such as [1] and the methods discussed in [1] could also be added to further support the superiority of SMPLy Private?


- The structure of their method is also very similar to PPMA. PPMA proposes pre-training with 'human-removed' data and synthetic data for privacy preservation, where M2M is simply replacing synthetic data with mesh-extracted data from Kinetics. Moreover, since off-the-shelf, pre-trained models are used to segment, inpaint, and recover the meshes from Kinetics in M2M, I feel that limits the novelty contributed by this work.


- The experiments in Section 4.3 and onwards are not sufficiently supported/are not convincing. Table 3 explores gender bias by investigating model accuracy on samples where women are performing male-biased actions and vice-versa. Firstly, the difference between gendered and non-gendered meshes are not described. Comparisons with other privacy-preserving methods would further support whether M2M is truly superior than previous methods at gender de-biasing, as opposed to just comparing with the standard baseline of VideoMAE on real data. Moreover, a general comment is that the extracted meshes are very unnatural and "stick out" so to speak when they replace the real humans in the data. It may be much easier for the model to focus/learn better action representations since these meshes are very clearly visible in the videos, as opposed to real humans which look natural and blend better into the surrounding environment/visual stimuli. This comment ties into Table 3, as the improved performance over the baseline could come from these unusual meshes in the video as opposed to the claimed privacy-preserved attributes learned by the SMPLy Private model - another reason why comparing with other privacy-preserving methods would be beneficial.
    + Section 4.4 is an interesting observation, but does not seem to actually provide any benefit. Firstly, the authors note "we demonstrate that our model [...] learns representations quicker in earlier stages because humans are consistently
depicted as meshes" which I describe as a shortcoming in my point above. Furthermore, the benefit of learning representations faster is null if the best-performing epoch is what ends up being used for all experiments anyway. Are any of these early epochs where M2M outperforms the baseline used? If not, then the fact that VideoMAE eventually catches up by the end of training leads me to believe this observation is not significant.
    + Section 4.5 and Table 4 is also a product of following PPMA. In PPMA, they first show that using NH Kinetics is best for Stage 1 training since it equips MAE to understand contextual action information (background and objects). They then show that NH Kinetics+Synthetic is best for Stage 2, since NH Kinetics continues to provide contextual alignment while the synthetic data provides temporal action information. This progression of results makes logical sense. However, Table 4 in this paper simply shows that M2M is better than NH Kinetics for Stage 2 training, which is obvious since NH Kinetics doesn't have any humans performing any actions. It would make more sense to compare M2M to NH Kinetics+Synthetic from PPMA to show that M2M leads to better downstream performance while also closing the realism gap against a model trained on real Kinetics data.

In summary, I believe only Table 1 provides meaningful and significant results. I do not believe Table 1 alone is enough for acceptance, as the rest of the quantitative results in this paper lack proper support and/or explanation. The writing is not very clear, but I do think the general idea of human meshes for privacy-preservation is interesting and valid, despite the lack of novelty regarding how the meshes are extracted and used in this work. The construction of K-Nexus through distinct action classes and showing significant improvements when using this sophisticated subset I thought was novel and applicable to future work, providing some strength to this work.

### Questions
Most of my questions regarding this work are listed in the weaknesses section. I am open to improving my score if the authors are able to address my concerns listed above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new privacy-preserving data augmentation framework, Mask2Mesh. It uses off-the-shelf models such as Mask R-CNN with ResNet-101 to extract human masks and OSX for mesh recovery. Before that, this work designed a new K-Nexus algorithm based on K-means to further select 150 classes from the Kinetics-400 dataset to reduce the class bias. Experiments based on the VideoMAE demonstrate its effectiveness in certain situations.

### Strengths
1. Most designs appear technically correct. This paper is easy to understand and practical to follow.

2. This work is well-motivated, addressing issues such as identifiable individuals, gender bias, etc.

3. The results are credible, supported by the code provided in the Suppl., which lays a foundation for future research.

### Weaknesses
Dataset:
1. Why was it necessary to further select a subset from Kinetics-400? If the goal was to increase the differences between the training data categories, I don’t think this is reasonable for action recognition tasks. Category ambiguity can be mitigated by adjusting the model or the training process. However, improving performance by removing similar actions does not seem justified. To substantiate the claim that the 150-class subset improves downstream task performance, a direct comparison between K400-pretrained and K150-pretrained results on downstream tasks is needed. Additionally, if this approach follows settings from previous work, it is essential to cite the relevant studies in the appropriate sections of the paper.

2. The Limitation at the end of the paper discusses the absence of temporal considerations in segmentation, which is understandable. However, in #Line178, it is mentioned that only one random frame is selected per video to represent the corresponding class. Is this truly appropriate? Intuitively, distinguishing between "standing up" and "sitting down" seems difficult using just a single frame. The authors seem to have either misunderstood or not directly addressed my concern in this section.

3. The selection of 150 categories from the original 400 is presented as a way to reduce category bias. It would be more convincing to explicitly show which categories were chosen and highlight which categories were prone to confusion. This would make the method more persuasive. While some examples were provided, a complete list of actions selected and excluded by K-NEXUS would be more convincing. Furthermore, since the authors mentioned that prior works have also used K-150, a detailed comparison between the 150 classes selected by K-NEXUS and the previously used 150 classes would strengthen the argument.

Technical:
1. Firstly, it is important to acknowledge that this paper’s perspective on information safety is commendable. However, the technical contributions are quite limited, as most of the models used are off-the-shelf. It seems that the only technical innovation is the K-NEXUS algorithm, but its performance appears to fall significantly short compared to random selection (as shown in Table 6). I do not fully agree with the claim that integrating off-the-shelf models can constitute the primary contribution of a high-quality paper. The authors themselves seem to acknowledge the limitations of K-NEXUS, particularly when compared to random sampling, which appears to be a critical weakness.

2. As mentioned in #Lines862-869, there are occlusion-based issues in the data construction process, which is common for SMPL. However, manually checking only five videos per class seems highly inadequate and lacks rigor.

Experiments:
1. Since the K-NEXUS algorithm is presented as the main contribution of this work (#Line100), shouldn't the experiment comparison for "Ours" be "SMPLy Priv. w/o K-NEXUS vs. SMPLy Priv." rather than "SMPLy Priv. vs. SMPLy Priv. w/ K-NEXUS"? Moreover, ablation studies should also based on the model involving K-NEXUS.

2. There are no test results for Kinetics-400 or Kinetics-150. I requested a comparison where K-150 and K-400 are used as downstream task datasets to benchmark against baselines. This differs from comparing the results of K-150 to K-400, as provided.

3. As illustrated in Appendix C, this work defines the categories selected by K-NEXUS as coarse-grained actions, while the remaining 250 classes are considered fine-grained actions. This definition lacks rigor and is not supported by examples. In the action recognition field, datasets like Kinetics-400 and UCF-101 are commonly referred to as coarse-grained datasets, while fine-grained datasets, such as FineGym, feature hierarchical annotations and subtle differences in both visual content and semantic labels. While I appreciate the effort to contextualize the definitions within the challenges of privacy-preserving learning, I remain concerned about the terminology used for “coarse-grained” and “fine-grained” actions and encourage revisiting the terminology to reflect the unique characteristics of the clusters better while aligning more closely with established conventions. This would make the paper’s contributions more accessible and clearer to the broader community.

Presentation:
1. The writing in this work is organized unusually. For example, in the Introduction, after outlining two paths to solving the problem, the content jumps directly to the contributions without an explanation of the specific methods.

2. The figures are unclear. For instance, Figure 2 uses arrows to directly present the workflow, which is straightforward. However, it would be more informative to label which model is used for each step, especially since most of them are off-the-shelf models.

### Questions
Please refer to the Weaknesses. I'm willing to raise my score if my concerns are well addressed.

### Soundness
2

### Presentation
2

### Contribution
2
