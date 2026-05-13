# FedInverse: Evaluating Privacy Leakage in Federated Learning

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Federated Learning (FL) is a distributed machine learning technique where multiple devices (such as smartphones or IoT devices) train a shared global model by using their local data. FL claims that the data privacy of local participants is preserved well because local data will not be shared with either the server-side or other training participants. However, this paper discovers a pioneering finding that a model inversion (MI) attacker, who acts as a benign participant, can invert the shared global model and obtain the data belonging to other participants. This will lead to severe data-leakage risk in FL because it is difficult to identify attackers from benign participants.
In addition, we found even the most advanced defense approaches could not effectively address this issue. Therefore, it is important to evaluate such data-leakage risks of an FL system before using it. To alleviate this issue, we propose FedInverse to evaluate whether the FL global model can be inverted by MI attackers. In particular, FedInverse can be optimized by leveraging the Hilbert-Schmidt independence criterion (HSIC) as a regularizer to adjust the diversity of the MI attack generator. We test FedInverse with three typical MI attackers, GMI, KED-MI, and VMI, and the experiments show our FedInverse method can successfully obtain the data belonging to other participants. The code of this work is available at https://github.com/Jun-B0518/FedInverse

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The paper studies model inversion (MI) attacks in federated learning settings, where malicious clients (participants) would apply existing model inversion techniques on the global model shared by the server. When performing MI attacks, the malicious clients would look like benign clients since they can still send model updates as such.
- To perform the attack, the malicious clients would train GAN models for model inversion, following prior work (GMI, KED-MI, VMI); a typical instantiation is to train GANs on public data with similar data distributions as the FL training setup and then optimize the generator for low log-likelihood (loss) under the shared global FL model.
- The paper also proposes a “diversity optimization” technique using the Hilbert-Schmidt independency criterion as a regularizer. The main idea is to encourage the GAN generated outputs to be more diverse, and the paper shows that this technique qualitatively improves the inverted data and quantitatively improves the attack success.
- The paper evaluates the proposed method on three datasets (CelebA, MNIST, and CIFAR-10) and shows that it can achieve high “attack accuracy” (measured by a separate model trained to tell apart generated vs real images) and low “Frechet inception distance” (which measures the similarity between real and fake images within the embedding space of a CNN). The experiments also show that the proposed HSIC regularizer was essential for obtaining high attack accuracy.

### Strengths
- The high-level idea of the paper is simple: with some modifications (HSIC regularizer in this case), existing model inversion attacks in the standard ML literature can easily carry over to federated settings, where the attackers are malicious clients and the target network is the global, shared model from the central server in FL.
- There is also originality in studying a new attack surface in FL that isn’t easily detectable from by the server (cf. attacks that require malicious clients to send out-of-distribution updates). The problem of interest is important and worth exploring.
- The paper is also reasonably easy to follow.

### Weaknesses
[W1] The use of public-data assisted generative models, particularly following prior work like GMI, KED-MI, or VMI, implicitly assumes that the client data distributions can be found in the public domain. However, in many practical FL settings, this assumption is often unwarranted. Many settings where FL is helpful—such as medical images across hospitals [1]—are often where the data distributions aren’t covered by publicly available data.

[W2] The experiments can be improved in terms of both quality and quantity.

- The paper directly takes a split of the federated training set as the “public data” for training the GANs. This in-distribution nature weakens the experimental support for the proposed techniques. The use of in-distribution public data provides an overly optimistic view of the attack's effectiveness. In real-world scenarios, the attacker would likely have access to a public dataset that is similar but not identical to the target data distribution. This difference in distribution could significantly impact the performance of the GAN and the resulting model inversion attack. The paper should include experiments with out-of-distribution public data to better reflect real-world attack scenarios.
- The evaluated datasets are fairly small; there are large federated dataset such as iNaturalist [2] that would help make the results more convincing. Indeed, by looking at Figure 4(a), the reader may argue that the model-inverted examples do not look much alike the true examples; what happens if the dataset and the FL setup is scaled up (e.g. more clients, larger local batch sizes)? The limited scale of the experiments makes it difficult to assess the practical impact of the proposed attack. The use of small datasets and a limited number of clients and batch sizes may not accurately reflect the challenges and complexities of real-world federated learning scenarios. The paper should include experiments with larger datasets, more clients, and larger local batch sizes to better evaluate the scalability and robustness of the proposed attack.

[W3] The evaluation metrics can be made more rigorous.

- The bulk of the experimental results rely on having a good “evaluation classifier” which tells apart real vs generated (model-inverted) images and whose embeddings are good enough to give meaningful Frechet inception distances (Section 4.4). However, it is unclear how such a classifier was trained. The lack of clarity regarding the training of the evaluation classifier raises concerns about the reliability of the evaluation metrics. The paper should provide more details about the training process of the evaluation classifier, including the architecture, training data, and hyperparameters. Without this information, it is difficult to assess the validity of the reported results.
- The core issue is perhaps that the possible plausible deniability that the model-inverted images are indeed part of the training set. I.e. just because the evaluation classifier says the generated images are realistic, can we be sure that they actually are? Is the similarity provable? Again, Fig. 4(a) does not seem to support the use of proposed metrics. The paper lacks a rigorous analysis of the similarity between the generated images and the original training data. The evaluation metrics rely on a classifier that may be biased or may not capture the nuances of the data distribution. The paper should include a more rigorous analysis of the similarity between the generated and real images, perhaps using techniques such as nearest neighbor analysis or visual similarity metrics that are less reliant on a classifier.

### Questions
- I would appreciate if the authors provide more visualization results of the generated samples, e.g. on CIFAR-10, as well as across different attack success rates.
- Consider using different citation commands `\citet` , `\cite`, etc. to make the formatting of in-text references consistent.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on Federated Learning (FL), a privacy-enhancing distributed machine learning approach. It highlights a crucial issue: the potential for Model Inversion (MI) attacks in FL, where attackers can extract data from other participants. Existing defenses are inadequate. To address this, the authors propose FedInverse, which uses the Hilbert-Schmidt independence criterion (HSIC) to assess FL model vulnerability to MI attacks. Experiments with typical MI attackers confirm FedInverse's effectiveness in evaluating data leakage risks in FL systems.

### Strengths
+ A novel method called FedInverse is proposed to comprehensively evaluate the privacy risks of FL in response to model inversion attacks.
+ The research question is well defined and valuable to the research community.
+ A thorough and comprehensive case study.

### Weaknesses
 - The diversity of the evaluated benchmark datasets needs to be further augmented.
- Potentially mature defense mechanisms require further consideration.

### Questions
This paper is well written and organized and has been thoroughly and comprehensively evaluated. However, the following minor issues still need to be considered:

- As mentioned in the weaknesses of this paper, we need to augment the diversity of the benchmark dataset. It would be better if the authors considered more tasks, such as NLP tasks.

- More advanced defense mechanisms need to be added to evaluate the effectiveness of the proposed attacks. Although the authors demonstrate the performance of the proposed attack against two common defense schemes in the appendix, the following stronger defenses still need to be considered:

[1] Huang Y, Gupta S, Song Z, et al. Evaluating gradient inversion attacks and defenses in federated learning[J]. Advances in Neural Information Processing Systems, 2021, 34: 7232-7241.

[2] Li J, Rakin A S, Chen X, et al. Ressfl: A resistance transfer framework for defending model inversion attack in split federated learning[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022: 10194-10202.

The main reason is that the BiDO solution considered in this article is not a defense solution tailored for FL.

### Soundness
3 good

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
This manuscript proposes FedInverse, an approach that one attacker could use to obtain the private local data of other clients as a normal participant. FedInverse generates the possible training data from observing the aggregated global model with the help of the GAN. Additionally, a regularizer using the Hilbert-Schmidt independence criterion (HSIC) is applied to generate more diverse images. The experiments show that FedInverse with HSIC has achieved progress in recovering the local data of other participants.

The rating has been changed to 6 after the rebuttle discussion.

### Strengths
This paper focuses on how to steal the private data of other clients in FL as a participant, and the idea of applying HSIC as a regularizer to increase diversity is helpful. Besides, for the evaluation part, plenty of factors are taken into consideration, which make the results comprehensive and easy to understand.

### Weaknesses
- FedInverse uses typical model inversion attacks to generate the images. However, whether those approaches could be directly applied to the aggregated model is still a problem. In the setting of the experiments, the clients have local datasets that are disjoint on the label (for example, in MNIST, the attacker has labels 5-9, while other clients have labels 0-4). However, the setting is not practical for the typical situation. As the number of participants increases, some clients will have similar data distributions, so that FedInverse may fail in this setting.
- Moreover, FedInverse generates the image from a similar distribution with target clients. However, it could not tell the source of the image exactly (from an attacker or another specific participant).
- Some metrics used in the experiments should be clear. Take the attack accuracy as an example. A well-trained model may still classify an image with some flaw as the correct class, and it could lead to results at variance with reality. Additionally, the top-5 accuracy is too weak for some experiments, especially on MNIST (with only ten labels). As for FID, the attack results of some baseline approaches(for example, applying the MI attack on local models) should be added for comparison. Otherwise, it would be hard for readers to understand the degree of privacy leakage.     
- In Section 3, the description of the attack procedure is not clear enough. More details are needed.

### Questions
- How does FedInverse perform in a typical vertical FL setting? For example, 10+ clients with the same (or similar) data distribution. More discussions of this case should be given.
- Is there any method to remove or mitigate the effect of the attacker dataset in the final results? From Figure 4, the generator is still trying to produce an image similar to its local dataset, even with the regulation of HSIC.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors apply known model inversion attacks (GMI, KED, VMI) to FL where a clients might act malicious and try to learn sensitive training data from other participants (by applying these attacks to the global models distributed in each round). The authors furthermore propose an optimization to these attacks based on introducing more diversity in the images generated by the attacker. The evaluation on various standard image classification tasks demonstrates the effectiveness of the model inversion attacks and a mostly minor advantage for the proposed optimization.

### Strengths
The paper studies an important topic, showing further vulnerabilities of FL, which is often assumed to be a privacy-preserving ML paradigm.

In the discussed threat model, this might indeed be the first (or one of the first) works to reconstruct sensitive training data of other clients just from plaintext access to the global model.

The underlying model inversion attacks are clearly presented and perform well in the evaluation.

### Weaknesses
The paper studies an important topic, showing further vulnerabilities of FL, which is often assumed to be a privacy-preserving ML paradigm.

In the discussed threat model, this might indeed be the first (or one of the first) works to reconstruct sensitive training data of other clients just from plaintext access to the global model.

The underlying model inversion attacks are clearly presented and perform well in the evaluation.

The work is based on the bold premise that "no studies pay attention to the data leakage problem when the attackers are pretended to be benign users", i.e., data extraction from the global models that are distributed by the central server in each round. While this might be true, a dedicated discussion of related works is missing from the main body of the paper (and only provided in Appendix B). There definetely exist works that look into data extraction from the global model, but from the perspective of a malicious aggregator that can use techniques like providing inconsistent models. For example: Boenisch et al. (arXiv:2301.04017), Pasquini et al. (CCS'22), Zhao et al. (SP'24).

The application of the existing model inversion attacks seems rather straightforward, assumes that a good auxiliary dataset is available, and the proposed diversity optimization in the evaluation does not show impressive improvements over the respective baselines.

The presentation and positioning of the suggested FedInverse framework is rather unclear to me. On the one hand, it is presented as an attack, on the other hand as an evaluation framework => is it supposed to be something that also FL operators should utilize to measure whether real benign clients might be vulnerable to such attacks?
Algorithm 1 is also unclear in this respect: Do all clients run the attack in parallel (instead of a small subset of malicious clients pretending to be benign)? The set Q_t is not passed to the FedInverse function as a parameter but assumed to be a global variable in line 19; however, the function still explicitly returns it => make clear what is the purpose of this algorithm, what is the final result of the algorithm, and how values are passed around between the functions.

### Questions
- What is the relation to existing attacks for extracting sensitive training data from global models listed above?
- Does the attack perform well / at all if there is no good quality auxiliary dataset available? (e.g., because training is done over records of rare medical diseases, etc.)
- Is the proposed algorithm / framework meant purely for attack purposes or also as a defence / pre-check for the server to evaluate the vulnerability of participating clients?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
