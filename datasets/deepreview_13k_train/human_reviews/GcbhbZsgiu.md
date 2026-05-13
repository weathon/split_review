# Adversarial Mixup Unlearning

- Decision: Accept
- Scores: 6, 3, 6

## Abstract
Machine unlearning is a critical area of research aimed at safeguarding data privacy by enabling the removal of sensitive information from machine learning models. One unique challenge in this field is catastrophic unlearning, where erasing specific data from a well-trained model unintentionally removes essential knowledge, causing the model to deviate significantly from a retrained one. To address this, we introduce a novel approach that regularizes the unlearning process by utilizing synthesized mixup samples, which simulate the data susceptible to catastrophic effects. At the core of our approach is a generator-unlearner framework, MixUnlearn, where a generator adversarially produces challenging mixup examples, and the unlearner effectively forgets target information based on these synthesized data. Specifically, we first introduce a novel contrastive objective to train the generator in an adversarial direction: generating examples that prompt the unlearner to reveal information that should be forgotten, while losing essential knowledge. Then the unlearner, guided by two other contrastive loss terms, processes the synthesized and real data jointly to ensure accurate unlearning without losing critical knowledge, overcoming catastrophic effects. Extensive evaluations across benchmark datasets demonstrate that our method significantly outperforms state-of-the-art approaches, offering a robust solution to machine unlearning. This work not only deepens understanding of unlearning mechanisms but also lays the foundation for effective machine unlearning with mixup augmentation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a novel and unique generator-unlearner method to yield mixed examples, which helps improve  machine unlearning effectiveness. Especially , this paper use a  novel contrastive objective not only to help refine generator, but also help unlearner  retain knowledge of remaining data and forget  forgetting data.  Hence, this operation can   prevent  catastrophic unlearning issue.  Furthermore, extensive experiments  demonstrate the efficiency and effectiveness of their proposed method.

### Strengths
1. This paper uses a intriguing adversarial process to solve the maching unlearning issue. They use a unique generator-unlearner adversarial process to force unlearner to  forget the forgetting and retain the remaining. This proposed method are novel and effective.
2. The proposed method outperforms previous work in a variety of settings, including both label-agnostic and label-aware settings, and has a relatively small time cost.

### Weaknesses
1. Though their experiments are relatively comprehensive,  the underlying dataset are somehow small. More experimental results on large dataset are expected to be demonstrated (e.g. imagenet).

2. The presentation of the paper needs to be improved, especially the description of the methods section.

### Questions
Why MixUnlearn sometimes demonstrates better performance than retrain (e.g., on CIFAR-10)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The author proposes a generator unlarner framework, which uses mixup technology combined with a generator to generate hard samples to help the model retain knowledge about the remaining dataset in forgotten samples. This framework is trained using two contrastive learning loss terms, effectively addressing the issue of potentially losing critical information about retained data during the forgetting process. The author substantiates the effectiveness of the proposed scheme through experimental validation.

### Strengths
1. The paper is well-organized and easy to follow, figures and tables are helpful and easy-to-understand. This scheme is relatively simple yet highly effective, as demonstrated by the experimental results, and the designed loss function is particularly noteworthy.
2. The solution proposed by the author applies not only to traditional unlearning scenarios involving labels but also to novel label-agnostic scenarios, demonstrating a broad range of applicability.
3. The author's visualization of the experiment is commendable, providing richer evidence to support the effectiveness of the proposed scheme.

### Weaknesses
1. The design of the author's approach does not convincingly demonstrate an actual improvement in unlearning, despite the experimental results resembling retraining. Since retraining does not engage with forgotten data, any generalization enhancements derived from this data will inevitably be lost; otherwise, complete unlearning cannot be assured. The solution proposed by the author incorporates information from forgotten data, which intuitively undermines the concept of complete unlearning.
2. The experiment is not sufficient, and additional deletion results at varying ratios would enhance the credibility. Furthermore, the limited number of datasets and models raises concerns. I am particularly interested in whether the experimental outcomes with more complex models and datasets, such as ImageNet, would influence the results of the method.
3. There is a lack of epoch description of the experiment of the approach, and it remains unclear how many training rounds are necessary for convergence to achieve satisfactory results. The criteria for terminating training are crucial aspects that require discussion in the context of approximate forgetting.
4. The comparative experiments lack sufficient explanation of hyperparameters, and some state-of-the-art results appear somewhat low. I recommend that the author adhere to the hyperparameter guidelines provided in the original paper. While the author states, "if our reproduced results align with the previously reported statistics in Shen et al. (2024), we present their results; otherwise, we provide our results," I believe that directly copying most of the experimental data is unacceptable. The author should revise the baseline results to reflect actual experimental findings. By the way, TS does not require further training of the teacher model; instead, the original and initialized models should serve as the teacher models for the experiment. I suggest the author review the original control scheme rather than relying solely on the introduction in [1]. If I have misunderstood any aspects, I would appreciate clarification from the author. In summary, the author's experimental section appears overly influenced by [1], which raises doubts about the authenticity of the author's experimental workload.

### Questions
Please check the questions in the weaknesses above.
Additionally, why does the retrained model have a different number of epochs compared to the initial model? Why is the testing accuracy of the model higher than the training accuracy on the CIFAR-10 and SVHN datasets? Does this indicate that the model may not fully converge within the specified number of training rounds, and could certain fine-tuning experimental schemes be affecting the accuracy of the results? Although the author referenced the experimental setup in [1], I think it is essential to ensure that the original model achieves full convergence before drawing any conclusions in research related to unlearning.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenge of machine unlearning focusing on minimizing the adverse effects of removing data points from forgotten labels. The forgetting process often disrupts the retention of other knowledge, reducing the model’s generalisation, particularly in the intermediate space between forgotten and retained samples.

To mitigate this issue, the authors use data mixup, generating challenging samples through training a generator. These mixed samples reveal forgotten information while disrupting the retention of remaining data, effectively reversing the unlearning process. The unlearner is then trained on these mixup and real samples using contrastive-learning-based losses to improve robustness and efficacy in unlearning.

### Strengths
The paper is well-organised, with clear motivations, methodology, and results. 

The research addresses a relevant problem and is sound, with a well-motivated toy example that illustrates the proposed approach effectively. 

The experimental results provide an adequate comparison to existing methods, that support the method's effectiveness.

### Weaknesses
I have no major concerns regarding this work. However, I do have two extended questions:

- I understand that the authors follow experimental setups from previous works on machine unlearning, focusing on low-resolution images and older network architectures. While this is consistent with prior works, these setups may not fully reflect recent advancements in deep learning. I suggest authors to conduct experiments on larger datasets (e.g. ImageNet) and newer model architectures (e.g. ViT, Swin Transformer). I am curious on additional discussion on any computational challenges in scaling up to larger models/datasets and how the method might need to be adapted.

- For challenging mixup samples, the goal is to reveal forgetting samples while lose the remaining samples. In traditional mixup, using a λ close to 1 could align with this aim. I would be interested in understanding how such traditional mixup samples perform within the unlearning process. The authors could consider including an ablation experiment that replaces their adversarial mixup generator with traditional mixup using different fixed λ values (e.g. 0.9, 0.95, 0.99) and compared with their proposed method.

### Questions
Please see the Weaknesses

### Soundness
4

### Presentation
4

### Contribution
3
