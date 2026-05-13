# Single Teacher, Multiple Perspectives: Teacher Knowledge Augmentation for Enhanced Knowledge Distillation

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Do diverse perspectives help students learn better? Multi-teacher knowledge distillation, which is a more effective technique than traditional single-teacher methods, supervises the student from different perspectives (i.e., teacher). While effective, multi-teacher, teacher ensemble, or teaching assistant-based approaches are computationally expensive and resource-intensive, as they require training multiple teacher networks. These concerns raise a question: can we supervise the student with diverse perspectives using only a single teacher? We, as the pioneer, demonstrate TeKAP, a novel teacher knowledge augmentation technique that generates multiple synthetic teacher knowledge by perturbing the knowledge of a single pretrained teacher i.e., Teacher Knowledge Augmentation via Perturbation, at both the feature and logit levels. These multiple augmented teachers simulate an ensemble of models together. The student model is trained on both the actual and augmented teacher knowledge, benefiting from the diversity of an ensemble without the need to train multiple teachers. TeKAP significantly reduces training time and computational resources, making it feasible for large-scale applications and easily manageable. Experimental results demonstrate that our proposed method helps existing state-of-the-art knowledge distillation techniques achieve better performance, highlighting its potential as a cost-effective alternative. The source code can be found in the supplementary.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a novel knowledge distillation method called TeKAP (Teacher Knowledge Augmentation via Perturbation), which generates diverse perspectives from a single teacher model. Instead of relying on multiple teacher models for supervision, TeKAP introduces diversity by perturbing both feature maps and output logits of a pretrained teacher network. This approach aims to simulate the benefits of multi-teacher distillation without the associated computational cost.

### Strengths
- The paper provides thorough theoretical proof and experimental validation.
- The paper is well-structured and clear in its approach, with intriguing perspectives.
- The method proposed in the paper has a wide range of application scenarios.

### Weaknesses
 - There is a lack of comparison with recent multi-teacher distillation work.
- The explanation of the difference in usage scenarios between feature-level and logit-level may be insufficient..

### Questions
- If more distillation methods could be included, it would be more convincing.
- I think the idea that different teacher models provide different perspectives is interesting. Would increasing the number of teacher models further improve performance?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript introduces TeKAP, a novel teacher knowledge augmentation technique. It generates multiple synthetic teacher perspectives from a single pretrained teacher model by perturbing its knowledge with random noise. TeKAP operates at both the feature and logit levels, enhancing the student's generalization ability. By reducing the need for multiple teacher models, TeKAP decreases both training time and memory usage. Evaluations on standard benchmarks demonstrate TeKAP's effectiveness in improving the performance of existing knowledge distillation approaches

### Strengths
1. This work uses a single pretrained teacher to simulate multiple teacher perspectives through perturbation, effectively circumventing the high computational costs of traditional multi-teacher setups.
2. The proposed method is simple yet demonstrated encouraging results.
3. The work includes a comprehensive evaluation of various aspects such as model compression, adversarial robustness, and transferability, which strengthens the credibility of the proposed method.
4. The extensive experiments also demonstrate TeKAP’s effectiveness in few shot learning and noisy data settings, suggesting a promising direction for advancing knowledge distillation.

### Weaknesses
1. Despite TeKAP's impressive results, the theoretical analysis of the perturbation methods lacks depth. While Gaussian noise is introduced, there is limited discussion on the choice of perturbation parameters, such as the standard deviation, and how these settings impact the model’s performance. This omission could hinder reproducibility and generalizability of the approach. Specifically, the paper does not explore how different noise distributions or magnitudes affect the diversity of the generated teacher perspectives and the subsequent student learning. The lack of a clear rationale for selecting Gaussian noise over other potential distributions, such as uniform or Laplacian, further weakens the theoretical grounding of the method.
2. Additionally, while the experiments cover a range of baseline comparisons, the paper lacks a comprehensive evaluation against existing multi-teacher distillation methods and other state-of-the-art single-teacher methods, which would better highlight TeKAP’s relative strengths. The paper should include a more thorough comparison with methods that also leverage multiple teacher perspectives, such as those using ensemble techniques or teacher assistants, to demonstrate the unique advantages of TeKAP. Furthermore, a comparison with recent single-teacher distillation methods that achieve high performance would provide a more complete picture of TeKAP's position in the field.
3. Moreover, there is little discussion on the computational efficiency and scalability of TeKAP in practical applications, potentially raising concerns among readers regarding its feasibility in real-world scenarios. The paper does not provide a detailed analysis of the computational overhead introduced by the perturbation process, particularly in terms of training time and memory usage. This is crucial for assessing the practical applicability of TeKAP, especially when dealing with large-scale datasets and complex models. A comparison of the computational cost of TeKAP with other distillation methods would be beneficial.
4. Some statements are overclaimed in this manuscript. The authors should comprehensively review related works and give proper discriptions.

### Questions
On page 4, the paper mentions the use of Gaussian noise for teacher perturbation but does not detail the criteria for choosing the noise parameters. How are these parameters optimized, and what is their impact on the diversity and quality of the generated teacher perspectives?
2.On page 5, the term ​ is introduced in the formula without a complete explanation or definition.
3.Is there a risk of overfitting to the perturbed features, especially when the noise parameters are not dynamically adjusted? 
4.How does TeKAP handle scenarios where certain classes are imbalanced? Is there a mechanism within the framework that ensures the augmented teachers do not bias the student towards overrepresented classes?
5.Could the following discussion be added to page 8? For instance:
1)What do these differences in inter-class correlations imply for the student's learning process?
2)How does the performance improvement of TeKAP in terms of inter-class correlation contribute to the overall effectiveness of the model?
6.In Figure 6, it is noted that the performance is best when the number of augmented teachers is 3. Does this imply that three teachers will be used in future applications? Additionally, the performance with two teachers seems normal; is there an explanation for this?

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
5

### Summary
The paper proposes a new augmentation method to replace the ensemble approach for KD by adding noise to the features or logits of the teacher model. This increases the variability of predictions and reduces the generalization error.

### Strengths
The proposed method is more efficient compared to other ensemble methods, and increasing the variability of the teacher's predictions is meaningful for knowledge distillation.

The paper is well-written and easy to follow.

### Weaknesses
1) The paper proposes an effective method to replace ensemble approaches; however, there is a lack of comparison to other ensemble methods (such as multi-augmentations) to demonstrate its effectiveness. Additionally, TAKD is not the SOTA method (for example, DGKD [1]) and there is a lack of experimental details for TAKD. It is not clear what teacher models are used for TAKD.

2) The experiments in this paper are not sufficient, and the baselines are outdated. The proposed method only compares with vanilla KD (2015), TAKD (2020), and CRD (2019), and lacks comparisons with other new methods like DKD [2] and MLKD [3].

### Questions
1) What is \mathcal{L}_{cel}​ in Equation 5?

2) In Equations 2 and 4, calculate the summation of the perturbation loss. Does \lambda need to be adjusted according to the number of perturbations?

3) What is the difference between the CAMs of TeKAP and the teacher in Figure 5? They look the same.

4) There is a lack of experimental details; even the learning rate and the number of training epochs are not mentioned in the paper.

5) For feature-level perturbation, which features are selected to add noise?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose TeKAP, a novel teacher knowledge augmentation technique that generates diverse synthetic teacher knowledge by perturbing a single pretrained teacher. This plug-and-play module leverages simple perturbations to capture ensemble benefits without training multiple teachers. Experimental results demonstrate TeKAP's effectiveness in enhancing both logit and feature-based knowledge distillation methods.

### Strengths
- The proposed plug-and-play module integrates seamlessly with existing KD methods, adding minimal computational burden.
- By augmenting knowledge from a single pretrained teacher network, the authors significantly reduce training time and resource demands while achieving ensemble-like effects.
- The approach is simple yet highly effective.

### Weaknesses
 - The proposed plug-and-play module was not well validated. Specifically, it was only applied to vanilla KD and CRD, even though there have been many advanced KD methods that can serve as baselines.
- The experiments omit numerous state-of-the-art single-teacher and multi-teacher KD methods; additional benchmark comparisons would - strengthen the evaluation.
- Details on dynamic noise perturbation are insufficient, with critical implementation information missing for reference.

### Questions
-How can randomly distorted teacher logits provide diverse inter-class relationships if the distortion is truly random?
-What does h represent in Eq. 9?
-What is the scale of the random noise, and how should it be set? Detailed guidelines for noise settings are needed.
-There appears to be no discernible difference between Fig. 3(b) and Fig. 3(c).

### Soundness
3

### Presentation
3

### Contribution
3
