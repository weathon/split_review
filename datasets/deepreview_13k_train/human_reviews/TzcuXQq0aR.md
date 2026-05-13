# PlugVFL: Robust and IP-Protecting Vertical Federated Learning against Unexpected Quitting of Parties

- Decision: Reject
- Scores: 3, 6, 5, 6

## Abstract
Vertical federated learning (VFL) enables a service provider (i.e., active party) who owns labeled features to collaborate with passive parties who possess auxiliary features to improve model performance. Existing VFL approaches, however, have two major vulnerabilities when passive parties unexpectedly quit in the deployment phase of VFL - severe performance degradation and intellectual property (IP) leakage of the active party's labels. In this paper, we propose \textbf{Party-wise Dropout} to improve the VFL model's robustness against the unexpected exit of passive parties and a defense method called \textbf{DIMIP} to protect the active party's IP in the deployment phase. We evaluate our proposed methods on multiple datasets against different inference attacks. The results show that Party-wise Dropout effectively maintains model performance after the passive party quits, and DIMIP successfully disguises label information from the passive party's feature extractor, thereby mitigating IP leakage.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper designs a PlugVFL framework to address two problems caused by the unexpected quit of passive parties, i.e. severe performance degradation and intellectual property leakage of the active party’s labels.

### Strengths
The concerned problem is meaningful.

### Weaknesses
The experiments are not well designed.

1. Fig. 3 and 6 plot the relationships between the test acc before party 2 quit and after party 2 quit, while Fig. 4 and 5 plot the relationships between the test acc and attack acc. Do they share the same hyper-paramters? What do the lines (which connect the points) mean? I donot get the meanings and reasons of the figures.

2. From Table 3, PlugVFL shows worse results than simply training independently. So does the proposed method make sense?

### Questions
1. Fig. 3 and 6 plot the relationships between the test acc before party 2 quit and after party 2 quit, while Fig. 4 and 5 plot the relationships between the test acc and attack acc. Do they share the same hyper-paramters? What do the lines (which connect the points) mean? I donot get the meanings and reasons of the figures.

2. From Table 3, PlugVFL shows worse results than simply training independently. So does the proposed method make sense?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses two critical issues in the VFL scheme, namely (1) performance degradation after passive clients drop from the scheme, and (2) mitigating IP leakage. The former issue is a novel observation in this work, where the inference performance degrades when a passive client drops. To tackle these issues, the paper introduces the plugVFL scheme, which incorporates two regularizations during VFL training.

### Strengths
1. The paper is the first to identify a significant problem in VFL, showing that when a party drops, it negatively impacts the VFL scheme's performance.
2. It also highlights the risk of IP leakage from feature extractors, demonstrating how passive parties can use their feature extractors for model completion and gain advantages within the scheme.
3. The alternative training design is intuitive and the paper effectively addresses the overhead of calculating mutual information objectives.
4. The paper successfully demonstrates the effectiveness of both objectives in a two-party VFL scenario for CIFAR image classification tasks.
5. The paper is well-organized and easy to read.

### Weaknesses
1. The link between the IP leakage issue and the deployment-time passive party dropping is not clear. The paper seems to conflate the solution to two unrelated problems. The "Active Model Completion (AMC)" is based on training time, which contradicts the deployment-time scenario. Specifically, the paper does not clearly articulate how the feature extractor, trained during the collaborative VFL process, can be directly leveraged by a passive party *after* they have dropped out of the scheme to perform model completion. The paper needs to clarify the attack vector and how the passive party retains the necessary components for this attack after leaving the VFL setup.
2. The discussion of party dropping only considers two parties with limited evidence (CIFAR-10). The impact on more parties should be explored. The current analysis lacks a rigorous evaluation of how the proposed method scales with an increasing number of participants. The paper should include experiments with at least three parties to demonstrate the generalizability of the approach.
3. The mitigation of party dropping seems to offer minimal advantages over multi-head training (as shown in Figure 3). The performance gains of the proposed method compared to a simpler multi-head approach are not substantial enough to justify the added complexity. A more detailed comparison, including statistical significance tests, is needed to validate the effectiveness of the proposed approach over existing baselines.
4. The paper states that IP leakage is due to label information, supporting the design of mutual information regularization. However, the connection between IP leakage and label information is not well-established. Section 3.3 suggests that IP leakage is primarily about successful model completion, not direct extraction of labels from the active party. A counter-example is that a feature extractor can be learned without label information (i.e., unsupervised learning). The paper needs to provide a more rigorous justification for why mutual information regularization is the appropriate defense against IP leakage, especially given the possibility of learning feature extractors without explicit label information.
5. The scalability of the alternative training for multi-party cases is questionable. For instance, in a 3-party scenario, the performance should remain consistent in multiple cases (both passive party drops or either one party drops). The equation in Section 3 could be split into four, increasing computation overhead significantly. The paper does not provide a clear analysis of the computational complexity of the proposed method as the number of parties increases. The authors should discuss how the computational cost scales with the number of participants and provide empirical evidence to support their claims.
6. The hyperparameter p setting for alternative training is debatable. Estimating the probability of dropping during training is challenging. The paper mentions that setting a relatively small p-value can improve the robustness of VFL. However, does this imply that the scheme should always set a small p? The paper lacks a clear guideline on how to choose the optimal value for the hyperparameter 'p'. The authors should provide a more detailed discussion on the sensitivity of the method to this parameter and offer practical recommendations for its selection.
7. There are inaccuracies in some statements, such as the assumption that "the service provider cannot afford to shut down the service while fine-tuning." In reality, the server could have a backup model to replace the running one without service disruption. Additionally, the statement, "Without loss of generality, we formulate our PlugVFL framework in the two-party scenario," should ideally be demonstrated in more than two-party scenarios, enabling downgrading to two-party scenarios. The paper needs to avoid making unrealistic assumptions about the deployment environment and should provide a more robust justification for focusing on the two-party scenario.

### Questions
Is there a naive way to mitigate performance degradation when a party drops? For example, could setting a mean vector value instead of zero help?

Image classifications like CIFAR-10/CIFAR-100 may not be ideal examples of VFL tasks.  Is this framework effective on categorical datasets?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Federated Learning exists some technical issues that cause people to decide the trade-off between model performance and privacy issues. The paper presents solutions to alleviate the privacy loss while retaining better performances. In vertical federated learning (VFL), there are two vulnerabilities caused by unexpected quitting of passive parties in the deployment phase – severe performance drop and active party’s label leakage. 

On the one hand, the paper presents a VFL framework (PlugVFL) that could preserve the VFL model’s performance against unexpected exit of passive parties. By omitting the representations from the passive party with a certain probability p in each communication round (iteration of training in VFL), the framework combines a weighted sum of the vanilla model training and model training without passive parties. Could think of the weighted method as the dropout method in traditional neural networks.

Given that in the deployment phase passive parties could still access the active model’s data using the feature extractor, the chance of leaking labels in the active model increases. In a large dataset that has important or classified information, labels could be viewed as Intellectual properties that need to be protected. So PlugVFL, on the other hand, presents a method that could minimize the mutual information during the training phase. By calculating the variational upper bound, and minimizing the parameters that is less than the variational upper bound could achieve the result that passive parties hold as little as possible label information from the active party.

The paper also conducts different experiments to evaluate their framework’s effectiveness. PlugVFL can improve the accuracy after a passive party’s exit by more than 8% on CIFAR10, compared to passive party quitting in the normal situation. PlugVFL also prevents the passive party from fine-tuning a classifier that outperforms random guess levels even using the entire labeled dataset with only less than 2% drop in the VFL model accuracy, outperforming baselines significantly.

### Strengths
Given the workflow of how PlugVFL is designed, there are strong contributions that are achieved by it. In terms of defense, the model minimizes the mutual information between the representations of the passive party and the true labels, formulating the defense into an adversarial training algorithm that jointly minimizes the variational MI upper bound and production loss. It also improved the accuracy after the passive party's exit by more than 8% on CIFAR10. At the same time, all previous work provides IP protection in VFL training, and they are the first on IP protection on deployment phase.

### Weaknesses
There are several weaknesses given the fact and result this paper had presented. The experiment data is based on CIFAR dataset, and only split into two parties, one as active party and the other as passive party. Less than 1%(400) of the labeled data to fine-tune the model to perform model completion attack, and achieve comparable accuracy (~1% drop) compared to classifiers trained with all data just in part 2. Only two parties, and only one experiment, so that complexity is not guaranteed in larger and more complex federated tasks. Also the accuracy solely on party 2's data is not high in the first place. According to standard classifier performance on the CIFAR dataset, PlugVFL’s performance is not that ideal. In the expectation formula for robustness of retain accuracy when pass parties drop, the probabilities of dropping is not explained reasonably, because the the some popular classifier is around 70% standalone but PlugVFL has relative low accuracy (~44.95%) compared to standards, and only split two parties, so lack of reason and fact of the generality of the model. Lastly, the paper mentions naive solutions for mitigating the accuracy drop, such as fine-tuning the head model after a passive party quits. To actually apply this method and get the accuracy result is more convincing, because what if this method is better than the method proposed by the paper.

### Questions
There are a few questions that need to be addressed/clarified. Firstly, the label is counted as IP protection in federated learning, and so valid, because the label has useful representation that the passive model can extract. The whole logic is that after passive parties normally will only have access to the representation extractors, which allow passive parties to fine-tune classifier heads with very few labeled data. But how are you going to define the difference of label type? Because different label data types could have different presentations, and how to ensure that could be generalized not just text labels. If the only representation you could extractor is a numeric matching, then it is not qualified for IP protection. Secondly, reduce co-adaptation of the hidden neurons of the head predictor, similar to dropout, but why setting p = zero, will you still have accuracy after party 2 quit? Based on your definition, in each communication, p will be zero and therefore making the model equivalent to calculating prediction performance.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study two issues in two-party VFL that occur when the passive party quits: a) the inference accuracy drops significantly as in VFL the passive party's participation is also required during inference, and b) the passive party might try to extract sensitive information about the active party's labels from the representation extractors. The authors propose an alternative VFL training approach to mitigate both issues: a) with a certain probability p during training, the active party will be set the passive party's representations to 0, and b) the mutual information between labels and representations is minimized. An evaluation of ResNet18 training on CIFAR10/100 clearly demonstrates the issues without the proposed mitigations and how those mitigations are indeed effective.

### Strengths
The paper studies two clearly relevant issues in the deployment of VFL.

The proposed robustness solution is simple yet effective.

The conducted evaluation answers most questions one might have in terms of dependence on parameter selection and comparison to related works.

### Weaknesses
The IP leakage issue of VFL that is discussed (the passive party can try to infer information about the active party's labels) is presented in the setting of the passive party quitting unexpectedly. However, to my understanding, this issue is completely unrelated to drop-outs and the same attack could also be carried out in case the passive party still participates in the system.

In §5.1, the authors briefly discuss a "naive" alternative to their approach of ensuring robustness in case of the second party quitting. This alternative, which is described as fine-tuning the head model after the passive party quits, is dismissed as time-consuming and impractical. However, it would be interesting to see how many training iterations are actually necessary (when shifting all training iterations where the passive party's representation is set to 0 till after the point when the passive party quits) until the model reaches accuracy that is somewhat similar to the case where the proposed mitigation is applied; especially when using small p, the required time to take the service offline might be very small.

The work is somewhat limited in studying only a two-party setting where the accuracy drop as a direct consequence of the only other party quitting is obviously the strongest. This is somewhat fine since also many related works on VFL are restricted to the two-party case, which is also realistic in real-world settings. Nevertheless, a discussion on the likely impact of unexpected quitting of one party in a, e.g., five-party scenario would be appreciated.

In Figure 1, it is unclear which information the active party provides to the passive party for it to carry out the IP leakage attack.

**Update:** The authors have clearly answered all my questions. However, I think the fact that the IP leakage issue is not actually related to the passive party dropping out is a major flaw in the presentation of the work and would require a major revision to fix. Therefore, I'm not upgrading my score.

### Questions
- Is the IP leakage issue related to passive drop-outs at all?
- Can you clarify if the "naive" alternative to robustness discussed in §5.1 is really impractical?
- How does the impact of drop-outs behave as a function on the number of passive parties? So is the presented accuracy drop also critical when one passive party in a, e.g., five-party setting drops out?
- Why is the evaluation in Table 3 only till p = 0.5; what happens in cases with high drop-out probability?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
