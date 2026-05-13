# Trustworthy Dataset Proof: Certifying the Authentic Use of Dataset in Training Models for Enhanced Trust

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
In the realm of deep learning, the veracity and integrity of the training data are pivotal for constructing reliable and transparent models. This study introduces the concept of Trustworthy Dataset Proof (TDP), which tackles the significant challenge of verifying the authenticity of training data as declared by trainers. Existing dataset provenance methods, which primarily aim at ownership verification rather than trust enhancement, often face challenges with usability and integrity. For instance, excessive operational demands and the inability to effectively verify dataset authenticity hinder their practical application. To address these shortcomings, we propose a novel technique termed Data Probe, which diverges from traditional watermarking by utilizing subtle variations in model output distributions to confirm the presence of a specific and small subset of training data. This model-agnostic approach improves usability by minimizing the intervention during the training process and ensures dataset integrity via a mechanism that only permits probe detection when the entire claimed dataset is utilized in training. Our study conducts extensive evaluations to demonstrate the effectiveness of the proposed data-drobe-based TDP framework, marking a significant step toward achieving transparency and trustworthiness in the use of training data in deep learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces the Trustworthy Dataset Proof (TDP) problem, which aims to verify the authenticity of training datasets used to train machine learning models. TDP provides a mechanism to certify that a claimed dataset was used fully, without additional tampering, during model training, thus enhancing trust and transparency. The paper proposes a novel “Data Probe” method, which embeds subtle markers in the dataset and uses model output distribution to confirm dataset integrity with minimal intervention in the training process. The authors demonstrate TDP’s performance on several vision datasets, showing that it can detect when training data is tampered with or incomplete.

### Strengths
**Definition of a New Dataset Verification Problem**

The paper identifies and defines the novel problem of Trustworthy Dataset Proof (TDP), which seeks to verify the integrity of datasets used in model training. Unlike existing approaches focused on dataset ownership or provenance, TDP aims specifically to ensure that the declared dataset was used in its entirety.

**Novel Approach to Address the Problem**

The authors propose a novel solution to the TDP problem by introducing the concept of “Data Probes.” This approach marks subsets of the dataset in a way that allows verification through model outputs with minimal impact and modifications to the training process. This probe-based strategy leverages distributional output patterns to detect incomplete or tampered datasets, and only requires black-box access to the model.

**Efficiency and Low Overhead**

The TDP framework is designed to be computationally efficient, requiring only minimal overhead compared to regular training. This is beneficial compared to approaches like Proof of Training Data, which incur significant overhead during training.

### Weaknesses
 **Inconsistent Threat Model Assumptions**

The main limitation is that the threat model assumes a dishonest trainer (L161) who attempts to modify the dataset and avoid detection. At the same time, the threat model assumes that the same dishonest attacker voluntarily sticks to the exact verification protocol specified by the verifier (defender), which cannot be verified (L192). This is a critical flaw, as a malicious trainer would not adhere to a protocol that allows them to be detected. The assumption that the attacker will use the provided watermarking procedure is unrealistic, as the trainer controls the execution environment and can easily modify or bypass the watermarking process before training. This makes the entire verification process vulnerable to trivial attacks.

In practical terms, this means it is easy for the attacker to bypass the proposed verification approach. Instead of computing the hash over the modified dataset D*, the attacker computes the hash over the unmodified dataset D, and thus always reaches the goal of succeeding the verification.

**The Dataset has to be Public**

The dataset has to be entirely available to verify the trained model. Since the data contains a significant part of the value, the trainer may be reluctant to publish it. Licenses and intellectual property may also work against this. This requirement severely limits the applicability of the method in real-world scenarios where data is often proprietary or subject to strict access controls. The need for complete dataset disclosure is a major barrier to adoption.

**Limited Evaluation**

The evaluation is limited to small image classification datasets: CIFAR-10, SVHN, CIFAR-100, and Tiny ImageNet 200. These are relatively similar, small-scale image datasets with few classes. The results would be much more convincing if the experiments showed generalization to at least medium-sized datasets such as ImageNet and other data modalities. Since the approach claims low overhead and requires only regular model training, there should be no reason not to run larger-scale experiments. The lack of experiments on diverse datasets and modalities raises concerns about the generalizability of the proposed method.

Similar things can be said about the models: they are all smaller-scale convolution models. It would be very interesting to see how larger-scale models behave and if the properties transfer to different architectures, e.g., transformers. The absence of experiments with diverse model architectures further limits the scope of the evaluation.

**Inconsistencies wrt. Secret k**

It is unclear to me what the purpose of the secret key k is. According to L295, it is used to make the hash values unique between different “users.” Who is the user here? I assume the attacker since they are generating the secret according to Algorithm 1. If the attacker is in control of k, how does it make anything more secure? This understanding is, however, inconsistent with L483 where the claim is that hiding the key from the user (presumably attacker?) can solve the effect of adaptive attacks. The role and implementation of the secret key are unclear and inconsistent, raising significant security concerns.

**No Code Available**

No code was available for review, and the authors did not specify whether it would be released upon publication.

### Questions
Why did the authors only consider small-scale vision datasets? It seems to me like there should not be significant barriers to train on larger-scale datasets such as ImageNet.

Does this approach also work on other data modalities?

L294: What security risk does hash calculation pose? How exactly could a constant hash pose a security risk, how could it be exploited, and how do individual user keys, which are then revealed, solve these issues?

L465: Why is the attacker knowing the key k a worst-case assumption? According to Figure 2 and Algorithm 1, the attacker generates k to compute the hash and, therefore, always has knowledge of it.

L482: “Keeping the user’s key hidden from the users […] might be a solution”. 

1. How can the user’s key be hidden from the user itself?
2. Who is the user here? The trainer or the verifier?
3. And how does hiding the key solve the attack?

### Soundness
1

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
This paper focuses on a watermarking approach for certifying dataset use in model training. It targets the research gap of usability and integrity of proposed solutions to the Trustworthy Data Proof problem. The paper’s goals include fidelity of the watermarking verification approach, low-invasiveness on the model training process, harmlessness (ie. minimizing the model’s performance degradation), and efficiency of the verification process.
The authors propose Data Probe, an approach conceptually similar to a weakened backdoor, where the probe input samples behave like special members of the dataset. However, Data Probe requires only a slight difference in model prediction confidence between the probe versus non-probe inputs  in order for the dataset to be successfully verified, as opposed to backdoors which trigger a specific output. The success of their approach relies on coupling of the dataset integrity verification with the data probe selection strategy, utilizing the uniqueness of hash functions. In particular, a user-specific keyed-hash is performed on the complete.
The authors propose and analyse the performance of 4 different types of data probe, as well as 4 different possible saliency scoring methods. Experiments are carried out to answer 4 RQs -  whether various types of data probes can effectively verify the integrity of the dataset, how many probes need to be implanted during training, which of the different probe score calculation strategies are most effective for detection, and how robust the verification mechanism is against adaptive attacks. Experiments show promise for their proposed Data-Probe-based solution to the TDP problem.

### Strengths
TDP is an interesting and underexplored problem, that is well motivated in the paper.
Overall the paper is well written and reasonably easy to understand, and the threat model seems reasonable, with the defender only requiring black-box access to the model to be verified.
Overall results look promising on a decent range of experiments, including adaptive attack.

### Weaknesses
 * The main weakness is that overall, while results for adaptive attack and case studies look promising, the experiments are only using Cifar-10 – which has only 10 classes of relatively low-resolution images (32x32 pixels), and each analysis is only performed on one NN architecture. This is not comprehensive enough to establish that the performance of Data Probe generalizes to diverse datasets and model architectures.   
* a missed related work: “DeepTaster: Adversarial Perturbation-Based Fingerprinting to Identify Proprietary Dataset Use in Deep Neural Networks” by Park et. al. (ACSAC ’23). This work identifies dataset use in model training with no invasiveness or harm in the approach. It may also be possible to compare overall accuracy of Data Probe with their model.
* It is not stated what scores are shown in gray in Table 4.   
* In the adaptive attack experiment, the difference between the data D Vs D*  is not clear.   
* In the case study – duplicating data to create extra data is not very compelling. It would be more interesting to see something like the SVHN dataset augmented with some MNIST data.   

Typos/etc:   
- in the abstract: “data-drobe-based".  
- Please check the definition of Conf(M,x) on page 7. What is the maximum taken over?
- Table 4 caption: “socres” should be “scores”

### Questions
To improve the paper, please address the following:   
* Expand the adaptive attack and case study experiments to include all the datasets and NN architectures covered in the Table 2 results (SVHN, CIFAR-100, Tiny-Image-Net-200, ResNet, MobileNet, DenseNet, ShuffleNet).   
* Add a clear explanation of what the gray scores represent in the Table 4 caption or in the accompanying text discussing Table 4. This would help improve the clarity of their results presentation.    
* Add a discussion of “DeepTaster" by Park et. al. (ACSAC ’23) to the related work and compare the fidelity of their approach (if appropriate).   
* Provide a more detailed explanation of how D* differs from D in the adaptive attack scenario. Eg. include a specific example to clarify this important aspect of the experimental setup.

### Soundness
2

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
3

### Summary
The paper introduces a novel framework called Trustworthy Dataset Proof (TDP), aimed at ensuring the authenticity and integrity of training datasets. Unlike traditional watermarking, Data Probe uses subtle variations in the output distributions of models trained on specific data, allowing for the detection of a small, representative subset of the training data. Also, this proposed approach is model-agnostic. Experimental results demonstrates the effectiveness of this approach, showing that the data probe-based TDP framework is both practical and reliable in verifying dataset integrity.

### Strengths
+) The topic of trustworthy proof in deep learning training is timely and interesting

+) The paper is well organized and easy to follow

+) The proposed method is technically reasonable and sound

### Weaknesses
 -) The motivation and threat model is not clear to me

-) Some assumptions in the problem setting are not very reasonable

-) There lacks a theoretical analysis (or proof) how well the proposed method will work

### Questions
a) This paper addresses a gap in the field by introducing the novel problem of verifying the authentic usage of datasets in deep learning. The topic is interesting as the community pushes toward responsible AI practices amid growing concerns about data misuse and authenticity. By focusing on dataset integrity through Trustworthy Dataset Proof (TDP), the authors make a timely contribution to the field.

b) My main concern is the motivation and threat model is not clear to me. The paper proposed a method to verify the training was performed on 'a credit dataset D' such that 'the model trainer can gain trust from the users'. This claim seems to be not convincing to me. Why a user can have extra trust if the model is trained a specific dataset? What is the goal of the model user? It would be better to show some real examples to help clarify it.

c) Some assumptions used in the paper need justification. For example, the goal of the paper is to verify if the entire dataset was authentically used to train a model. However, in practice, a dataset is often combined with other datasets to jointly train a model - this will change the distribution and the proposed method may not work. Also, trainer may apply on-the-fly augmentations/filters which may affect the training data distribution. It would be better to discuss how these would impact the proposed method.

d) While the evaluation results show that the proposed method can work well, there lacks a theoretical analysis (or proof) on the effectiveness of the proposed method. The evaluated datasets are small datasets, therefore there might be a gap when we use it in practice. A theoretical analysis will help understand the gap and better justify the proposed method.

e) Meanwhile, the adaptive attack results seems not very convincing to me. In this setting, the attacker has fully knowledge of the verification process and the exact data probe to be used for verification, so why the attacker cannot simply overfit the desired model output of the probe data?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study presents Trustworthy Dataset Proof (TDP), a new approach to verifying the authenticity of training data in deep learning, addressing a gap left by existing dataset provenance methods that focus on ownership rather than trust enhancement. Traditional methods face challenges like high operational demands and ineffective dataset verification. To overcome these limitations, the authors propose Data Probe, a model-agnostic technique that leverages subtle variations in model output distributions to detect the presence of specific subsets of training data, differing from watermarking methods. This approach enhances usability by reducing training intervention and ensures dataset integrity, allowing detection only when the full claimed dataset is used. Extensive evaluations demonstrate the efficacy of the Data Probe-based TDP framework, advancing transparency and trust in training data utilization in deep learning.

### Strengths
1.	The proposed problem of trust dataset proof is interesting and important. This work provides an effective solution letting model trainers claim authentic usage of certain datasets.

2.	The proposed methods don’t rely on cryptography techniques, thus being lightweight and efficient.

3.	The paper is well-organized and easy for readers to follow.

### Weaknesses
1.	The verification protocol is unclear in terms of presentation. For example, in probe selection, there is a need to generate or specify a key to select the data probe, who is responsible for generating this key, the paper sometimes adopts ‘trainer’ and sometimes adopts ‘users’, which is very confusing. Figure 3 cannot depict the protocol clearly as well.

2.	The definition of harmlessness is too narrow, which is much wider than model performance compromising. Actually, the proposed four types of data probes all introduce harm to the model. For example, Prominent Probe leverages higher overfitting that increases the vulnerability of membership inference attacks. Absence Probe does hurt the performance of data probes and similar data. Needless to say, the Untargeted and Targeted Probe. In terms of general harmless dataset provenance, I believe this work [1] provides a better solution.

3.	According to the experiment results, different types of data probes perform distinctively in different metrics. However, this paper does not provide a solution that can unify different types of data probes to achieve a comprehensively better type. Without this, in practical scenarios, how does the user know which type to choose for specific cases?

4.	In lines 362-363, the paper mentions that the sample-level scores are aggregated to form a new metric, but I cannot find the detailed aggregation approach. Then it is unclear how and where PSA in Table 2 originates from.

5.	As for the adaptive attack, I disagree that replicating and embedding the probe corresponding to D after training would be adopted by the attacker. The more potential way is replicating and embedding the probe during the training. Besides, the experiment setup is also unclear, like how is the modified dataset D* made and how large the difference between D and D*?

6.	According to my understanding of AUC, I don’t think a score exceeds 50 but smaller than 60 is sufficient for distinguishing two distributions.

7.	Figure 4 needs improvement, like there is no legend for the dashed curve and the y-axis of the third subfigure can use a log scale.

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2
