# Wicked Oddities: Selectively Poisoning for Effective Clean-Label Backdoor Attacks

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 6, 5

## Abstract
Deep neural networks are vulnerable to backdoor attacks, a  type of adversarial attack that poisons the training data to manipulate the behavior of models trained on such data. 
Clean-label attacks are a more stealthy form of backdoor attacks that can perform the attack without changing the labels of poisoned data.
Early works on clean-label attacks added triggers to a random subset of the training set, ignoring the fact that samples contribute unequally to the attack's success. This results in high poisoning rates and low attack success rates.
To alleviate the problem, several supervised learning-based sample selection strategies have been proposed.
However, these methods assume access to the entire labeled training set and require training, which is expensive and may not always be practical.
This work studies a new and more practical (but also more challenging) threat model where the attacker only provides data for the target class (e.g., in face recognition systems) and has no knowledge of the victim model or any other classes in the training set.
We study different strategies for selectively poisoning a small set of training samples in the target class to boost the attack success rate in this setting. 
Our threat model poses a serious threat in training machine learning models with third-party datasets, since the attack can be performed effectively with limited information. Experiments on benchmark datasets illustrate the effectiveness of our strategies in improving clean-label backdoor attacks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method for enhancing clean-label backdoor attacks on deep neural networks. Unlike traditional clean-label attacks that apply triggers randomly, this approach selectively poisons challenging samples within the target class, boosting attack success rates with fewer poisoned samples. The authors introduce two strategies: using pretrained models to identify "hard" samples and leveraging out-of-distribution data for sample selection. Tested on CIFAR-10 and GTSRB datasets, this method outperforms random poisoning and is resilient against popular defenses like STRIP and Neural Cleanse, highlighting a need for stronger countermeasures against selective clean-label attacks.

### Strengths
1. The paper improves traditional clean-label backdoor attacks by proposing a threat model that is more applicable in real-world scenarios.

2. The method is claimed to achieve higher attack success rates with a lower poisoning rate, showcasing efficient use of resources.

### Weaknesses
1. In my opinion, the method primarily introduces a data selection strategy, which lacks sufficient novelty.

2. The evaluation is conducted only on CIFAR-10 and GTSRB datasets, limiting insight into the method's performance across other dataset types and application domains.

3. The paper primarily tests against older defense strategies. Implementing more recent and sophisticated defenses, including adaptive methods like sample-specific anomaly detection, would strengthen the evaluation.

4. The pretrained model strategy relies on the availability of pretrained models in similar domains, which may not always be accessible in real-world applications.

### Questions
The authors should clarify the novelty, choice of limited datasets, the use of older defense strategies, and the dependency on pretrained models.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper studies clean-label backdoor attacks in a very constrained setting, where the attacker only needs access to the training data from the target class and has no prior knowledge of the victim model, training process, and the other classes, and focuses on data-selection strategies to boost the performance of existing clean-label attacks in this constrained setting. The proposed data selection strategies include (1) the use of a pretrained model (when such exists) or (2) the use of an OOD dataset (when the pretrained model is not available) to train a surrogate model.  The experimental results demonstrate the proposed strategies significantly enhance the ASR and several existing clean-label backdoor attacks, compared to random selection strategies. In addition, the paper demonstrates that the proposed strategies are resilient against several existing defenses.

### Strengths
The main strengths of the paper lie in its studied threat model, proposed sampling strategies and experimental evaluation.

- I think that the proposed threat model is important as it exposes yet another backdoor threat where an attack only needs access to the data of the target class. The demonstrations that existing backdoor attacks under this threat model are not satisfactorily effective are an important contribution of the paper.
- The proposed sampling strategies are novel, especially when they could be used with existing backdoor attacks, such as BadNets, SIG, Narcissus, etc…) to boost their backdoor performances under the studied threat model. It’s also interesting finding where the effectiveness of the proposed strategies even when there is less and less assumptions on the pretrained models or the OOD datasets. 
- The paper includes thorough analysis of the proposed strategies, demonstrating their effectiveness when they’re used with several existing backdoor attacks across different datasets. The evaluation also shows the effectiveness against several defenses.

### Weaknesses
I find that the paper has the following concerns:
* The Narcissus results, while interesting, are different from what reported in their original paper. Can the authors explain why there are such differences?
* The OOD approach rely on out-of-distribution data but it’s not clear how this dataset could be obtained, or whether there are any specific requirements of the datasets to maintain the effectiveness of the attacks?
* Assuming that the victim could distribute the target class data collection to multiple sources, how does the proposed attacks perform in this case?
* Do the authors have any suggestions about potential mitigation approaches against the proposed attacks in the studied threat model?

### Questions
Please see the questions in weaknesses.

### Soundness
3

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
4

### Summary
The paper proposes a method for improving the effectiveness of clean-label attacks. It introduces a threat model where the attacker only has access to data belonging to a specific class and has no knowledge about other classes in the dataset. The paper proposes a method for using samples with hard to learn features to create poison-efficient clean label attacks. The proposed method finds these samples by clustering the latent features of a surrogate model. The paper explores using a pretrained model and a model trained on OOD data as the surrogate model. The paper evaluates the clean-label attack against backdoor defenses and data cleaning methods.

### Strengths
- The proposed method is a widely applicable technique to enhance to clean label attacks.
- The experiments do a good job differentiating the surrogate model from victim model and therefore the attack shows convincing transferability.

### Weaknesses
 - The paper trains for 300 epochs which is significantly longer than it should take to train the model on CIFAR-10/GSTRB [1,2] and makes attack success due to over-fitting very likely. Around 100 epochs seems to be more standard. Ideally, to simulate a competent defender early stopping should be employed. I.e. stopping the run when validation loss plateaus.

 - The experiments use very weak baselines. The paper only evaluates how the method performs compared to random sampling. At minimum the paper should compare against [3]. Especially because [3] could easily be adapted to adhere to this paper's threat model by using a pretrained model. Therefore, the experiments are not sufficent to jusifty that the proposed method is stronger than a slightly adapted version of [3].

 - The paper claims that it's threat model represents *"the **most** constrained data-poisoning threat."* However, there are other perfectly reasonable threat models that would make this attack unrealistic. For example, an opportunistic attacker that doesn't get to choose the subset of samples in the dataset they are able to manipulate.

 - When evaluating the attack against defenses the paper does not describe the hyperparameter settings used by each defense nor how those settings were derived.

Minor:
- Bolding of best methods or aggregation would make Tables 2 and 3 more interpretable.
- There are many typos in the manuscript.

### Questions
- Why would an attacker use the OOD strategy proposed in section 4.4, as it requires training a surrogate model and appears to work worse than using a pretrained model?
- Why use a latent space clustering approach instead of using the loss from a pretrained zero-shot image classifier like CLIP?
- Why use VICReg instead of a more general feature extractor like CLIP?
- Where are the training settings used in experiments adapted from?

References

[1] Alexander Turner, Dimitris Tsipras and Aleksander Madry. "Label-Consistent Backdoor Attacks.", 2019.  

[2] He, Kaiming, et al. "Deep Residual Learning for Image Recognition," 2016.  

[3] Gao, Yinghua, et al. "Not All Samples Are Born Equal: Towards Effective Clean-Label Backdoor Attacks.", 2023.

### Soundness
3

### Presentation
2

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
This paper explores a practical scenario for clean-label backdoor attacks, where an attacker’s access is limited to a single class of data within a decentralized training setup. This constrained threat model reflects real-world data collection challenges, such as privacy restrictions and geographical limitations. To enhance poisoning efficiency under these conditions, the paper introduces two sample selection methods specifically designed for this limited-access scenario.

### Strengths
1. The paper is easy to follow to a large extent.
2. The motivation is clear and with empirical support.
3. The paper introduces a clean-label backdoor attack that works effectively in a constrained scenario where the attacker has limited data access (only one target class). This approach is realistic for scenarios with privacy or geographical constraints, enhancing the practical relevance of the attack model.

### Weaknesses
1. Numerous studies [1,2,3,4,5,6,7,8] have addressed sample selection in backdoor attacks, several of which [6,8] specifically focus on sample selection for clean-label backdoor attacks. Omitting these key relevant works is a significant oversight and should be addressed to ensure a comprehensive discussion of the literature.
2. The novelty of this paper is limited, as it leverages a pre-trained model to identify "hard samples" for poisoning—a concept already explored in several studies [6,7,9]. However, the distinctions between this approach and prior work are not clearly articulated.
3. The first contribution claimed by this paper is the introduction of a new backdoor threat model, where an attacker, acting as a data supplier, has access only to the target class data yet can still execute effective clean-label backdoor attacks. However, previous studies [10,11] have already examined this threat model in depth, providing detailed discussions on "Why are dirty-label attacks more effective than clean-label attacks?" Consequently, the originality and contribution of this paper raise some concerns.
4. The discussion of backdoor attacks and defenses in the related work sections of this paper is outdated. 
5. There are some potential over-claims. For example, Line 156-159: Accessing only samples from a single non-target class is more difficult setting than yours.
6. Missing some important experiments.
- Main Experiments
  - The authors should also include the results of methods using all training samples for references, although you have a different setting.
  - It would be better to include the results of Narcissus here instead of in the appendix.
  - I would like to see whether the proposed method is also effective for untargeted clean-label backdoor attacks (e.g., UBW-C in [12])
- The Resistance to Defenses: The authors should evaluate their methods on more advanced backdoor defenses (such as [13, 14] and their baselines).

### Questions
1. The authors should include more related works and advanced baselines in their paper.
2. The authors should better clarify their main contributions than those introduced in existing works.
3. The authors should avoid overclaims.
4. The authors should conduct more comprehensive experiemnts. 

More details are in the 'Weakness' section.

### Soundness
2

### Presentation
3

### Contribution
2
