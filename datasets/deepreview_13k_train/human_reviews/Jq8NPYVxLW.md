# Less is More: Exploiting Feature Density for Enhanced Membership Inference Attacks

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Membership inference attacks have become the de facto standard for assessing privacy breaches across various machine learning (ML) models. However, existing approaches often require substantial resources, including large numbers of shadow models and auxiliary datasets, to achieve high true positive rates (TPR) in the low false positive rate (FPR) region. This makes these attacks prohibitively expensive and less practical. In this work, we propose a novel membership inference attack that exploits feature density gaps by progressively removing features from both members and non-members and evaluating the corresponding model outputs as a new membership signal. Our method requires only a few dozen queries and does not rely on large auxiliary datasets or the training of numerous shadow models. Extensive evaluations on both classification and diffusion models demonstrate that our method significantly improves the TPR at low FPR across multiple scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a new and efficient membership inference attack by exploiting the confidence change trajectory under varying feature removal. Its effectiveness is validated across both classification and generative models, applied to image and tabular data modalities.

### Strengths
S1: This work investigates a novel membership inference signal --- confidence change trajectory --- that requires fewer resources and lower computational costs than previous trajectory-based MIAs that often rely on additional model training.

S2: In addition to classification models, this MIA also supports diffusion models, demonstrating superior attack performance compared to existing state-of-the-art MIAs.

S3: The authors provide a thorough analysis of the feature removal strategy, highlighting the advantages of noisy linear imputation.

### Weaknesses
W1: Unclear intuition. In Section 3.2, the authors present two hypotheses: H1) member samples exhibit higher density values, and H2) member samples’ confidences should be more resilient, with H2 relying on H1. However, no supporting reference or empirical evidence is provided for H1. Additionally, Figure 1 does not effectively demonstrate H2, as the confidence changes for member samples lack consistency, e.g., the confidence drop for members is greater on WideResNet but smaller on ResNet compared to non-members.

W2: Incomplete experiments. Although the authors repeatedly highlight the resource efficiency of their MIA, there is no explicit comparison of resource or computational costs with state-of-the-art methods in the experimental section. Additionally, the work overlooks the resource requirements of the mask prediction model used.

W3: Unclear definition. The authors refer to random-based and guided-based removal strategies but do not provide clear definitions for these terms in the manuscript.

W4: Confusing terms. Both the title and the design intuition (Line 134) use the term “enhance” to describe this new MIA. For passive attacks, the gap between members and non-members remains relatively constant, with each signal having a different capacity to represent this gap. An effective membership signal can capture a clear and easily classifiable gap but does not actually increase it.

W5: Some presentation issues. For example, 1) Figure 2 is too small, making it difficult to distinguish each step clearly. 2) The term “the system” in Line 222 is unclear.

### Questions
Please refer to the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the membership inference attack for image models. With the intuition that members and non-members would have different behaviors when losing important features, this paper proposes an algorithm where the adversary is assumed to have a shadow dataset to create a tuple of model, members and non-members, and then a member-vs-non-member discriminator is learned given the label, the loss and the after-removal features. The empirical results look promising, which are higher than the popular methods in the literature.

### Strengths
1. To my best knowledge, the intuition in the method is quite novel by considering the after-removal features as an important feature for membership classification.
2. The method as my understanding is mild in terms of computational cost, which avoids to train another model similar to the target model.
3. The main result looks promising. As shown in Table 1, the proposed method have certain benefit at TPR at low FPR.

### Weaknesses
The writing and the clarity need to be further improved. In details
1. It is not clear what the connection is between the intuition and the exact method. In section 3.2, the design intuition is described by the feature embedding $\phi$ and the density. However, it is not mentioned anymore in the later method design. 
2. The method is not described very clear. 
- In section 3.4, the paper introduces how to optimize the mask $m$. However, it does not define the domain of the mask: whether it is discrete in {0, 1} or it is in any bounded continuous region.
- It is not defined how to shape the original sample $x$ by the learned mask above to get the final "removal-based membership features", which is a part of the membership features in line 194. What is the removal process.
- It is also questionable how an MLP would work if the "removal-based membership features" is still in the pixel space, as introduced in line 199-200.
3. The variants of methods in the experiment, Ours. random, Ours Guided, Ours w/ loss traj. are not well-defined. For example, the loss trajectory is firstly mentioned in the background section, and then appears in the experiment result description paragraph.

With my (relatively) deeper understanding, I have further questions/concerns:
1. Why is it preferred to learn the U-net for predicting the  mask? An alternative way is to optimize $m$ for every $x$ w.r.t. the proposed loss function. Moreover, the mask $m$ is learned w.r.t the shadow model from my understanding, what's the intuition that it will still have the expected performance when it is applying with the samples in MIA test?
2. I am still not very convinced that the intuition is aligned with the method design. The intuition is discussing the learned feature space, where "learned" is in the sense of the feature representation (embedding space) learned with the training data.  However the "feature removal" in the method section is more about the "pixel removal" and it seems there is nothing related to the learned feature space. Also this introduces some confusions that "feature" in the intuition section means the embedding in the feature space, but later on "feature removal" seems to be the "pixel removal".
3. Clarity question: "final membership features" mentioned at line 220 of the revised pdf only has very few dimensions, which one dimensional confidence score of pixel removed image, the loss of original image, and the one-hot label + (potentially other signals from the literature)?

### Questions
Please check the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Membership Inference Attacks (MIAs) aim to determine whether a model was trained on a specific data point. Most MIAs perform poorly at low false positive rates (FPR) because non-member samples often resemble member samples in terms of model output. This paper introduces a novel MIA that leverages feature density to ascertain membership information. The attack demonstrates that membership inference can be determined by progressively removing features from a sample: the confidence scores of non-members decrease faster than those of members as features are removed. The authors evaluate their attack on both image classification and diffusion models.

### Strengths
There is a lot I appreciated about this work.

**The attack mechanism is intuitive and well-explained:**  
I really like the intuition behind this attack and how manipulating features can reveal membership information. It’s a refreshing approach, distinct from existing methods.

**Does not require training shadow models:**  
Unlike most existing MIAs that require training a shadow model, this attack does not, as it operates within the feature space. Consequently, this attack (or a variation of it) could be executed on a large pre-trained model. While this is a major strength, it is not emphasized by the authors.

**Evaluation across multiple datasets (CIFAR10/100 and CINIC):**  
The authors perform experiments on standard datasets commonly used in MIA literature and test the attack across multiple architectures.

**Evaluation on diffusion models:**  
I also appreciated that the authors evaluated their attack on diffusion models, broadening the scope of their work.

**Removal Operation:**  
The authors assess their method with different removal operations, as shown in Table 3. I found this information very valuable. One possible addition would be a discussion on why certain methods perform better than others.

### Weaknesses
 **Suggestions for Improving the Paper:**

1. **Reframing of Existing Attack by Adding Noise to Input**
   The core idea of this paper is that points most vulnerable to membership inference attacks (MIAs) lie in sensitive regions of the feature space. These sensitive features, when perturbed, change the model's output. However, this approach appears to be a reframe of an earlier work [1], with the key difference being that [1] adds noise across the entire input, whereas this paper focuses on specific parts. This alone may not constitute a sufficient contribution. The authors could strengthen this work by offering fresh insights into the role of feature sensitivity. For instance, do sensitive features in images vulnerable to MIA exhibit identifiable patterns? Are these features semantically meaningful or are they more related to noise or artifacts in the data? A deeper analysis of the nature of these sensitive features is needed to justify the novelty of this approach.

2.  **Insufficient Information for Reproducing Results**
   Several details are missing, making reproduction challenging:
   - How were the shadow models trained, including parameters?
   - How many shadow models and target models were used?
   - How often were experiments repeated?
   - What are the train-test accuracies of these models?
   - What thresholds are used to separate members from non-members?
   It is crucial to provide a detailed description of the experimental setup, including all hyperparameters, training procedures, and evaluation protocols. Without these details, the reproducibility of the results is questionable.

3. **Potential Overuse of CW for Identifying Vulnerable Features**
   Could simpler methods, such as super-pixels or saliency maps, be considered instead? Using CW could be costly, as it adds significant operations for attackers. The computational cost of using CW to identify vulnerable features should be carefully considered, and the authors should justify why simpler, more efficient methods are not sufficient. The trade-off between attack performance and computational cost needs to be clearly articulated.

4.  **Lack of Comparison with Stronger, Recent Attacks**
   The authors did not evaluate newer, stronger attacks, particularly [2,3], which demonstrate significant improvements over existing approaches. The only powerful attack compared here is LiRA, and even then, their method performs similarly (Fig. 4). Moreover, [2,3] can significantly outperform LiRA. To strengthen this work, the authors should include comparisons against these methods. The absence of comparisons with state-of-the-art attacks makes it difficult to assess the true effectiveness of the proposed method.

5. **Lower AUC Despite High TPR at 0.1% FPR**
   Table 1 shows results across various attacks. While the authors’ method outperforms existing attacks at low FPR, the AUC remains lower than others. Could this discrepancy be explained? Additionally, what are the standard deviations for the values in the table? The lower AUC suggests that the overall performance of the proposed method might not be superior to existing methods, despite achieving a higher TPR at a very low FPR. A more thorough analysis of the trade-offs between TPR and FPR is needed.

6.  **Clarity in Figures**
   The TPR vs. FPR figures could benefit from improved clarity. For example, in Fig. 4, distinguishing between LiRA and the current attack is difficult. Could the authors provide AUCs and TPR@0.1% FPR for clarity? The figures should be clear and easy to interpret, with all relevant metrics clearly labeled.

7. **Absence of Requirement for Shadow Models**
   A major strength of this attack is its ability to be executed on pre-trained models without requiring shadow model training from scratch, unlike LiRA and [2]. Currently, the paper suggests that a shadow model is required. To highlight this advantage, the authors could restructure the paper to emphasize this point, as it significantly enhances the work’s value.

### Questions
See weaknesses.

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
This paper proposes a new Membership Inference Attack that leverages feature density gaps between member and non-member data points, allowing the attack to significantly improve true positive rates at low false positive rates. This method requires far fewer resources compared to traditional approaches, as it does not depend on large auxiliary datasets or numerous shadow models. By systematically removing features and analyzing changes in model confidence, the new approach can effectively discriminate between members and non-members, demonstrating superior performance across various datasets and model architectures in the process.

### Strengths
1. Membership inference attack is a popular and interesting topic.
2. The proposed method is interesting and the design intuition makes sense to me.
3. Experiments are detailed and sufficient。

### Weaknesses
1. Lack of important baselines such as [1] and [2]
2. Some parts of figures such as figure 2 and 4 and the experiments are unclear
3. This paper's contribution is kind of overclaimed.

### Questions
I think the idea is good but I still have some questions: 

1. I think the proposed method should be compared to well-known attacks such as [1] and current SOTA such as [2] to make the claim this work is SOTA. What will be the results when compared to [1] and [2] proposed methods? Especially, [2] also claims that their proposed method can be low cost making it a good baseline to this work.

2. I am curious that why the balanced accuracy is approximately 0.7, while the AUC reaches around 0.9. Although theoretically possible, I haven't encountered such a significant discrepancy in practical applications, where attack accuracy generally aligns closely with attack AUC. Could the author clarify this anomaly or consider releasing the source code to provide further insights?

3. This paper claims that the proposed method is resource-efficient but they are not very obvious in the paper presentation. Using around 10k for training and testing and rest for MIA is a common thing in the literature. I do not see why this experiment setting is resource-efficient. For the number of shadow models, it may be required a lot for LiRA attack, but it is not that big for other attacks. Especially, for population attacks in [1], you do not need to train the shadow model.  BTW, figure 4 is too small to distinguish the difference.  

4. I also wonder if the defender uses a pre-trained feature extractor during target model training, will the proposed attack still work? Or in other words, is your proposed method limited to a ResNet-like model and training from scratch setting? 

I will consider changing the score based on the response.

### Soundness
3

### Presentation
2

### Contribution
2
