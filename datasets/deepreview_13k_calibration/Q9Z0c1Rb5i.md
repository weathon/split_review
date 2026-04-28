# Boosting Concept Bottleneck Models with Supervised, Hierarchical Concept Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3

## Abstract
Concept Bottleneck Models (CBMs) aim to deliver interpretable and interventionable predictions by bridging features and labels with human-understandable concepts. While recent CBMs show promising potential, they suffer from information leakage, where unintended information beyond the concepts (either in probabilistic or binary-state form) is leaked to the subsequent label prediction. Consequently, distinct classes are falsely classified via indistinguishable concepts, undermining the interpretation and intervention of CBMs.

This paper alleviates the information leakage issue by introducing label supervision in concept prediction and constructing a hierarchical concept set. Accordingly, we propose a new paradigm of CBMs, namely SupCBM, which stands for Structured Understanding of leakage Prevention Concept Bottleneck Model, achieving label prediction via predicted concepts and a deliberately structural-designed intervention matrix. SupCBM focuses on concepts that are mostly relevant to the predicted label and only distinguishes classes when different concepts are presented. Our evaluations show that SupCBM’s label prediction outperforms SOTA CBMs over diverse datasets. Its predicted concepts also exhibit better interpretability. With proper quantification of information leakage in different CBMs, we demonstrate that SupCBM significantly reduces the information leakage.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This submission proposes a refinement of Concept Bottleneck Models (CBMs), namely SupCBM. Often, CBMs require additional training a concept predictor, which can be conducted prior to or jointly with training the label predictor.  An important difference between SUPCBM and previous CBMs is the supervision of class labels when training the CB layer, which to some extent converts the original multi-class classification on the classes into a multi-label classification problem on the concepts, i.e., each instance is associated with a set of relevant concepts. I think going from the predictions, which can be either soft or hard, to the final predictions on the classes might be seen as looking for a “closest” set of relevant concepts among those that have been observed in the training data, i.e., specified by the classes.  

I think SupCBM and CBMs in general are interpretable in the sense that, besides the final predictions on the classes, they provide sets of relevant concepts supporting the reason for why their predictions are made. However, the quality of the set of concepts and intervention matrix, which specify the relevance of class-concept pairs would be of utmost importance. The important task of defining the set of concepts and intervention matrix is currently done by GPTs in the experimental part.

The empirical evidence suggests that SupCBM can provide more promising results on 4 data sets (CUB-BIRD, CIFAR10 CIFAR100, and HAM10000), compared to related CBMs (P-CBM, Label-free CBM, LaBo, and Yan).

### Strengths
S1: The concept of SUPCBM and CBMs in general is interesting. 

S2: This submission proposes an interesting way to define the sets of relevant concepts

S3: The empirical evidence is in favor of CBMs, compared to related CBMs

### Weaknesses
W1. Concept generation in safety-critical domains: Relying on GPTs to solve the important task of defining the set of concepts and intervention matrix may call for further investigations on the trustworthiness and robustness of the framework. For example, one might ask whether we should rely on GPTs to define the set of concepts in safety-critical applications, such as medical image classification, and cell-type classification. Regarding the robustness, the empirical results also indicate that 2 versions of GPTs can provide different levels of performance. So it might be natural to ask which kind/version of LLMs should be employed in concrete applications. Furthermore, the process by which GPTs generate concepts and the intervention matrix is not clearly defined, making it difficult to assess the reliability of the generated concepts and their relevance to the classification task. This lack of transparency raises concerns about the potential for bias or inaccuracies in the concept sets, especially in high-stakes scenarios.

W2. Scalability: Additional discussions on the scalability of SupCBM and CBMs with respect to the number of concepts might be useful in different applications. For example, in cell-type classification, a good set of concepts might be rather large. The computational cost of training and inference with a large number of concepts is not discussed, and it is unclear how the model's performance would be affected by a significant increase in the concept set size. Specifically, the memory requirements and processing time for both training and inference should be analyzed with respect to the number of concepts.

W3. The concept of bottleneck models:  Within SupCBM, it seems that for each class, all the relevant concepts contribute equally to the final prediction. However, in practice, one might also think of a more flexible strategy where weighting mechanisms for concepts within each class. Additional clarifications and discussions on this point might be beneficial. The current approach of treating all concepts equally within a class may not capture the nuances of complex relationships between concepts and classes. For example, some concepts might be more indicative of a particular class than others, and a weighting mechanism could potentially improve the model's accuracy and interpretability.

W4. The model's design: I think the discussion given in Section 3.3 on the case where A = B = ∅ is interesting. Additional discussions on how this case could be treated in practice might be beneficial. It is unclear how the model would handle cases where no shared concepts are identified between classes, and this scenario should be further explored with concrete examples to understand its practical implications.

### Questions
Please find below some comments and suggestions (C/Ss) that might benefit the clarification and potential impacts of the submission. 

Concept generation in safety-critical domains: 
- C/S 1: Compare GPT-generated concepts to expert-defined concepts in a medical domain
- C/S 2: Analyze the stability of generated concepts across multiple GPT runs
- C/S 3: Propose a method for human expert validation of GPT-generated concepts
- C/S 4: Discuss guidelines for when GPT-generated concepts are appropriate vs. when expert-defined concepts are necessary

Scalability:
- C/S 5: Provide computational complexity analysis of SupCBM as the number of concepts increases
- C/S 6: Conduct experiments showing how performance and runtime scale with increasing concept set sizes
- C/S 7: Discuss potential approaches for handling very large concept sets efficiently

The concept of bottleneck models:
- C/S 8: Clarify if there is any weighting mechanism for concepts within a class
- C/S 9: If all concepts contribute equally, discuss the potential implications or limitations of this approach
- C/S 10: If not, explain how the relative importance of concepts is determined

The model's design:
- C/S 11: Clarify what happens in practice when A = B = ∅ and how often does this occur
- C/S 12: Discuss strategies for handling cases where shared concepts are insufficient to distinguish classes
- C/S 13: Provide an example or case study demonstrating how SupCBM handles such situations

The impact of meaningless hard concepts:
- C/S 14: Do you think the observation that hard CBM's performance can be improved by adding meaningless hard concepts could be due to a not sufficiently informative set of concepts?
- C/S 15: Discuss why meaningless concepts may improve the predictive performance
- C/S 16: Suggest experiments to test if a more informative concept set would eliminate this effect
- C/S 17: Compare the behavior of SupCBM to hard CBMs in this regard. Does the predictive performance of SupCBM also benefit from meaningless concepts?

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
3

### Summary
The paper proposes a new type of Concept Bottleneck Models (CBM) for image classification called SubCBM. The basic idea is to use an LLM model such as GPT4 to define concepts for each label type. Then, instead of predicting the labels, a classifier is trained to predict concepts. Finally, predicted concepts are used as features for a single-layer classifier that predicts the label. By design, such classification strategy prevents information leakage and improves explainability. The evalkuation was performed on several benchmark image classification data sets and SubCBM was compared to several state of the art CBM approaches and to a pure supervised learning baseline. A special attention during evaluation was paid to measuring information leakage.

### Strengths
+ The proposed approach is well justified and its design is directly aimed at preventing information leakage
+ The experiments are quite extensive and insightful
+ Based on the provided information leakage evaluation, the experimental results confirm that the proposed method is successful on this objective

### Weaknesses
- Since there is a deterministic relationship between the labels and concepts (through the information matrix), if the number of concepts is sufficiently large, they are able to unambiguously encode each label. As such, it is not surprising that accuracy of SupCBM can reach the upper bound of the baseline classification approach. The obvious question is what is the actual role of the information matrix. In particular, what would happen if the information matrix were replaced by a random binary matrix. Without studying this baseline, it is difficult to get a proper insight into the the strengths and weaknesses of SupCBM approach. 
- It seems that all CBM approaches mentioned in this paper tradeoff some accuracy for explainability. However, the paper could have been clearer about the relative differences between the existing and the proposed CBM approach with respect to what aspects of explainability they are focusing on. The paper is overemphasizing the information leakage issue at the expanse of discussion about explainability.
- The success of SubCBM largely depends on the ability of LLMs to define concepts and construct the information matrix. Some issues due to this approach are mentioned in the limitations. It is still a a weakness of this paper that it did not provide some experimental insights about more diverse types of data sets where of-the-shelf LLMs are not sufficiently capable.
- Some results require more in-depth discussion. Given the importance of LLMs to prepare the concept labels, it is surprising to see how the results are not sensitive to the type of LLM or to the number of concepts hyperparameter. Is it because even the weaker LLMs are capable of identifying concepts from class labels seen in the benchmark data, or there is some other reason?

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript presents a novel approach to CBMs called SUPCBM, which aims to address the issue of information leakage in current models. By introducing label supervision in concept prediction and a hierarchical concept set, SUPCBM focuses on concepts relevant to the predicted label and utilizes an intervention matrix. This method enhances the model's interpretability and reduces information leakage compared to existing state-of-the-art CBMs.

### Strengths
1.  The introduction of a structured intervention matrix and hierarchical concept learning in SUPCBM represents a significant innovation over traditional CBMs, offering a fresh perspective on handling information leakage.
2.  By focusing only on relevant concepts and utilizing hierarchical learning, SUPCBM provides enhanced interpretability.
3.  The manuscript evaluates SUPCBM across multiple datasets spanning different domains, including general classification, specialized classification, and medical image analysis, showing its wide applicability and effectiveness.
4.  SUPCBM offers a practical advantage by allowing post-hoc conversion of existing models into CBMs with minimal overhead, enhancing its utility and flexibility.
5.  The manuscript employs multiple metrics such as concept removal, concept locality, and concept perturbation to rigorously assess information leakage, providing clear evidence of SUPCBM's advantages.
6.  The method of annotating images with only relevant concepts and the use of GPT for concept generation and pooling are well-explained, providing clear evidence of SUPCBM's advantages.
7.  The provided code is easy to understand and successfully replicates the results presented in the manuscript, facilitating transparency and reproducibility.

### Weaknesses
 1.  The introduction of a structured intervention matrix and hierarchical concept learning in SUPCBM represents a significant innovation over traditional CBMs, offering a fresh perspective on handling information leakage.
2.  By focusing only on relevant concepts and utilizing hierarchical learning, SUPCBM provides enhanced interpretability.
3.  The manuscript evaluates SUPCBM across multiple datasets spanning different domains, including general classification, specialized classification, and medical image analysis, showing its wide applicability and effectiveness.
4.  SUPCBM offers a practical advantage by allowing post-hoc conversion of existing models into CBMs with minimal overhead, enhancing its utility and flexibility.
5.  The manuscript employs multiple metrics such as concept removal, concept locality, and concept perturbation to rigorously assess information leakage, providing clear evidence of SUPCBM's advantages.
6.  The method of annotating images with only relevant concepts and the use of GPT for concept generation and pooling are well-explained, providing clear evidence of SUPCBM's advantages.
7.  The provided code is easy to understand and successfully replicates the results presented in the manuscript, facilitating transparency and reproducibility.

### Questions
1.  How does the two-level concept set composed of perceptual and descriptive concepts affect the performance of SUPCBM? Could the authors provide more ablation experiments?

2.  What measures are considered to address the limitations posed by concept generation using LLMs, especially concerning the consistency and reliability of the concepts?

3.  How does altering the parameters 'p' and 'q' impact SUPCBM's performance and information leakage? According to the provided code, increasing these two values (p=7 and q=8) will increase performance on CIFAR10 (89.26%) but decrease performance on CIFAR100 (69.57%).

4.  Whether injecting domain knowledge into the intervention matrix could enhance SUPCBM‘s performance?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies a learning paradigm called concept bottleneck models (CBM). Compared to standard supervised learning, CBM requires that each sample is accompanied by a concept vector, which contains supervision information of what concepts the sample contains. The CBM then works by adding a so-called concept bottleneck layer in front of the fully connected layer, in hope of learning the concepts of the sample and improve interpretability. The paper argues that existing CBM approaches suffer from information leakage, which is defined as "unintended and additional information beyond the predicted concepts is leveraged for the follow-up label prediction". The proposed approach relies on a two-level concept set (generated by prompting ChatGPT), and the training introduced a so-called "intervention matrix" to reduce information leakage.

### Strengths
1. I am unfamiliar with the CBM field, so I cannot judge the originality.

2. One strength of this work in terms of quality is that a human-involved study based on Amazon Mechanical Turk is conducted to evaluate the concept produced by the algorithm. 

3. The other strength of this work in significance is that in the case study, the concepts shown in Figure 3 are reasonable and helpful for interoperability. However, without seeing the same output of other CBM algorithms, it is impossible to judge how these case studies can show that the proposed approach is better.

### Weaknesses
1. Lack of clarity is one key weakness of this paper. The "definitions" in this paper are not real definitions. For example, in definition 2.1, information leakage is defined as "unintended" and "additional" information other than the concepts are used for label prediction. However, it is unclear what the exact definition of unintended and additional information is, as these are almost entirely subjective. There are some discussions with respect to hard/soft CBM algorithms. However, to my understanding, the definition of what is the intended concept for a label requires an oracle that outputs ground-truth concepts for each label.  

The authors should provide a more precise, operational definition of information leakage, and provide precise definition of what is "unintended" and "additional" information. Furthermore, the authors should clarify what is the intended concept and if the concepts are generated by ChatGPT how to guarantee that intended concept are also the intention of the human users.

Later, the paper advocates that the concept set should be formed with "perceptual concepts," which are concepts that can be "directly observed by humans without reasoning." This is also ambiguous. It is impossible to precisely understand what this advocates without a precise definition of reasoning, and even so, it is common that humans who observe the same image will have different levels of reasoning.

2. The writing of this paper shows a worrying sign of a lack of statistical understanding. For example, one sentence in the paper is ”In addition, The p-value of our human study results is around 0.0003. Since p-value<0.05 usually indicates statistical significance, our results should be statistically significant." Given a significance threshold, you either reject or not reject the null hypothesis. There is no "should be" significant in statistical language. 

The author should clarify the meaning of "should be statistically significant"? Furthermore, the author should clarify what test they have used to obtain this p-value.

3. The lack of clarity in writing continues. In the results of Table 1, the authors never state what evaluation metric is used to measure performance. The author should clearly specify the evaluation metric. If accuracy is used, the authors should explain why the vanilla model (which uses a pre-trained backbone directly for label prediction) achieves such low accuracy on CIFAR datasets. Also, the authors could consider discussing other metrics to provide a more comprehensive evaluation.

### Questions
1. For the case study in Figure 3, what if we fine-tune a vision-language model and ask it to describe the "beak, tail, wing, eye, feather" description? Wouldn't that achieve very similar results to those shown in the paper?

I suggest that the author compare their method to a fine-tuned VLM baseline, and provide the same output on the cases in Figure 3. The authors could also discuss the advantages and disadvantages of their approach compared to such a baseline.

2. On the extendability, is there any experiment to support the claim? Will the performance drop significantly if the backbone models do not support the classes in the concept set?

3. How can we ensure that SupCBM "only focuses on concepts that should be involved in predicting the label"? 

4. Section 3.3's entire validity seems to rely on Oracle concept sets, but in reality, the concept sets are generated by ChatGPT.

### Soundness
1

### Presentation
2

### Contribution
2
