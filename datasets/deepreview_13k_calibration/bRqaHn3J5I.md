# Prototype antithesis for biological few-shot class-incremental learning

- Decision: Accept
- Avg Score: 5.75
- Scores: 3, 6, 8, 6

## Abstract
Deep learning has become essential in the biological species recognition task. However, a significant challenge is the ability to continuously learn new or mutated species with limited annotated samples. Since species within the same family typically share similar traits, distinguishing between new and existing (old) species during incremental learning often faces the issue of species confusion. This can result in "catastrophic forgetting" of old species and poor learning of new ones. To address this issue, we propose a Prototype Antithesis (PA) method, which leverages the hierarchical structures in biological taxa to reduce confusion between new and old species. PA operates in two steps: Residual Prototype Learning (RPL) and Residual Prototype Mixing (RPM). RPL enables the model to learn unique prototypes for each species alongside residual prototypes representing shared traits within families. RPM generates synthetic samples by blending features of new species with residual prototypes of old species, encouraging the model to focus on species-unique traits and minimize species confusion. By integrating RPL and RPM, the proposed PA method mitigates "catastrophic forgetting" while improving generalization to new species. Extensive experiments on CUB200, PlantVillage, and Tree-of-Life datasets demonstrate that PA significantly reduces inter-species confusion and achieves state-of-the-art performance, highlighting its potential for deep learning in biological data analysis. The code will be made publicly available following the paper's acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies "fine-grained" class-incremental learning in a few-shot setting. The authors argue that under such a setting, the model would easily suffer overfitting (to new classes) or forgetting (of old classes). They thus propose to leverage hierarchical-class information (e.g., family-species) to encourage knowledge sharing across species of the same family while learning discriminative information. The paper proposes two new learning strategies for this purpose: RPL and RPM. In three small-scale experiments, the proposed approach demonstrated improved performance.

### Strengths
S1. The paper focuses on an interesting and challenging problem. 

S2. The paper points out several insights that future research on fine-grained incremental learning could leverage.

### Weaknesses
W1. It is unclear or not intuitive why when new classes and old classes are similar (so have shearable information), incremental learning will lead to forgetting. 

W2. The technical/implementation details are not clear and not optimally designed. First, ResNet18 seems to be a too-weak backbone, especially for fine-grained problems. The authors may consider transformers (DINO, DINO-v2, BioCLIP visual encoder) or ResNet50 at least. Second, there is no information about whether the backbone is pre-trained, and if so, on what dataset. Third, it seems the feature backbone is only updated during the base training stage (Eq 1). If so, suppose the linear classifiers of the base (old) classes are frozen during continual learning, I see no reason why the old classes will be forgotten. Fourth, do the authors impose an orthogonal constraint in Line 270?

W3. My major concern is the approach itself. The design seems to be quite ad hoc without justifications. First, I'm not sure why computing the residual between the linear classifiers (or prototypes) and feature vectors makes sense. Please note that the prototypes can simply be the feature vectors times a scalar. Why does the residual contain information on "the secondary discriminative features likely representing traits shared across the family?" Second, why does adding the residual to feature vectors of the new species make sense? What do the new feature vectors encode? Third, the meanings of the decompositions and terms introduced in Lines 270 - 290 are not clear or justified. Finally, if the residual is added to features of the new species during training, how about the inference stage?

W4. The experiment details are missing; the experimental design can be improved. For example, no dataset statistics are provided. No information about how the authors obtained the family information. The PlantVillage dataset seems to be too small; the authors could consider using families in iNaturalist. No information about how the Tree of Life Dataset (with ~400K species) is subsampled. How do the authors ensure that all the families are seen during the base training time? Finally, experiments on no more than 200 species are a bit too small. 

=== Minor ===

W5. There are many missing references, for example, no references to the datasets in the introduction; no reference to "Inspired by human’s reference-based learning mechanism."

W6. The related work seems to miss one topic, generalized few-shot learning, such as "Generalized zero-and few-shot learning via aligned variational autoencoders, CVPR 2019." Will this line of work resolve the problem in Line 138?

### Questions
Q1. What is the detail of the Feature decomposition strategy (Line 400)? CAM and Grad-CAM are methods to visualize a classifier. How did the authors use their saliency responses to get accuracy in Table 2?

Q2. BioCLIP is a foundation model pre-trained on over 400K species. Can the authors provide more details about the argument that "it struggles with continual learning and tend to misclassify closely related species?" (Line 126)

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work observes that a limitation of incremental learning is confusion with closely related species (like species from same family) and therefore makes use of family label of each species to overcome that. The method learns one family level prototypes representing shared traits, and species level prototypes representing species specific traits. In the initial learning stage prototypes are learned through a method introduced called Residual Prototype Learning and during incremental learning stages a method called Residual Prototype Mixing is introduced.

### Strengths
1.	Extensive comparison with multiple relevant baselines for CUB200.
2.	Family information of any species is easy to obtain, so using that to improve incremental learning makes sense.

### Weaknesses
1.	Basis for some assumptions made are not clearly explained. Please refer to the questions.
2.	Not every baseline is considered for all three datasets. No particular reason is provided for skipping several baselines. Particularly I believe NC-FSCIL is a necessary baseline since its performance is pretty close to PA without having to use family label. If the skipped methods are not suitable for Tree-Of-Life and Plant-Village, please explain.
3.	No discussion of a possible limitation: In RPM are we assuming no new species is introduced whose family is not seen during the initial learning phase. If so, that is possible limitation of the work and it has to be discussed.

4.	With sufficient training the prototypes can converge towards the most species specific traits, but there can still be some background information that are also species specific. This is especially true in biological datasets, where some species can only be found in certain environmental conditions. Although, this can be mitigated with very large amount of data, that does not seem to be the case considering the experimental setting of this particular work.

For example, let’s consider a scenario where there is only one species “A” in the set of base classes that lives in environment “E”. Since there is only one species, information about “E” will be part of $\mu_{c_i}$. Now if a new species “B” that also lives in “E” is introduced,
we don’t get the opportunity to augment the new species features with the information of “E” since it is not in the residual prototype $\mu_{r_i}$. This can lead to confusion between “A” and “B”. Essentially everything that is learned as specific unique need not truly be species unique.

### Questions
1.	Line 274, how the assumption that prototype do not contain background information is made? Is it not possible that both family level and species level prototypes may contain background information.
2.	Line 275 and 276, how can it be assumed that the species level prototypes (mu_ck) contain both family-shared and species-unique information, while in the RPL (line 231 and 232) it is assumed they capture the most species unique traits.
3.	In section 4.3, it is not clear from Equation 3 how the delta of cosine similarity is optimized as mentioned in line 289. Is it happening implicitly when we optimize as in Equation 3.
4.	In section 5.3 Feature Distribution subsection, does “without PA” mean the baseline model from Table 1, if so, please mention it explicitly
5.	Throughout the main paper, I’m assuming the cosine similarity between three vectors as in Equation 2 and 3 means the summation (or average?) of cosine similarity of the feature vector with respect to the two prototypes, but it would be better to explicitly mention it.
6.	In table 3, PA’s performance is bolded. If the best performing method at each session can be bolded instead that would improve the readability of the table, making it easy to understand which method is doing better as I can see in Table 3, PA is not doing the best in all sessions (can also consider highlighting first, second and third best differently)

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present a novel approach to handle the few-shot class-incremental learning problem, specifically in species classification. The authors take advantage of the hierarchical taxonomic relationship between species and use their family label to transfer knowledge from existing species and new species. Their approach, named Prototype Antithesis (PA), employs Residual Prototype Learning (RPL) to learn unique prototypes per species and novel residual prototypes to represent shared traits between species in a family. To further improve the model’s discriminating ability, they utilize Residual Prototype Mixing to generate synthetic samples for data augmented training. They show SOTA performance on three biological datasets: CUB200, PlantVillage, and Tree-of-Life.

### Strengths
- They show the generalization of their ability by evaluating on three biological image datasets.
- The authors present novel residual prototype learning and residual prototype mixing training methods that improve class separating and alleviate catastrophic forgetting.
- They present a theoretical analysis of their method, focusing on class-separation.
- An ablation study shows the quantitative effectiveness of their residual prototype learning and mixing methods.
- Their method shows stronger performance than others in the later stages of the incremental learning.

### Weaknesses
 - The feature decomposition strategy section is convoluted, so Table 2 doesn’t make sense to me. I understand that there are high response and secondary response regions being extracted, but I’m confused how they are used to obtain the values in Table 2. Specifically, it's unclear how the high and secondary response regions are quantified and compared to derive the similarity metric. The paper mentions 'unique' and 'common' features, but the precise mechanism for decoupling and measuring their similarity is not well-defined. It would be beneficial to clarify how these regions are processed to generate the values in Table 2, including the specific mathematical operations or metrics used.
- You have all of your model’s accuracies bolded in Table 3, but at several columns, your model is not the best (columns 0, 1, 2, and the PD). Please correct.
- The method is only evaluated on 100 classes in the tree-of-life dataset. This should be run multiple times to ensure the robustness across different sections of the dataset given its size. Given the hierarchical nature of the Tree-of-Life dataset, it is important to evaluate the method on different subsets of classes to ensure that the results are not biased towards a specific section of the taxonomy. The current evaluation on a single set of 100 classes may not be representative of the overall performance across the entire dataset.

### Questions
- Could the author help clarify my confusion about the Feature decomposition strategy in section 5.2
- See weaknesses.

### Soundness
3

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
The article proposes a Prototype Antithesis (PA) method, which first learns species-unique and family-shared semantics of original classes. For new classes, it promotes learning by mixing family-shared features while preserving the model's ability to discriminate original classes. Experimental results validate the effectiveness of this method.

### Strengths
1. The paper is well-organized.
2. The literature review is detailed and comprehensive.
3. The suite of experiments is admittedly comprehensive.

### Weaknesses
1. There are three variable in cosin similarity calculation, please explain how the cosine similarity is specifically calculated in Eq 2 for  $\hat{Y}_{i}^r=cos(R_i, \theta_c, \theta_r)$ and $\hat{Y}_i^0 = cos(F_i^0; \theta_c, \theta_r)$.
2. How is the family-level label defined? Is this label provided by the dataset?
3. What is the number of features for $\theta_r$, and does this number change during training?
4. Why does mixing the residual prototypes of old species with new species features encourage the model to capture the unique characteristics of the new species?
5. Does the method require integrating residual features during the inference phase?

### Questions
The technical details are unclear; please see the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3
