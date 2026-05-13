# New Paradigm of Adversarial Training: Breaking Inherent Trade-Off between Accuracy and Robustness via Dummy Classes

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Adversarial Training (AT) is recognized as one of the most effective methods to enhance the robustness of Deep Neural Networks (DNNs). However, existing AT methods suffer from an inherent trade-off between adversarial robustness and clean accuracy, which seriously hinders their real-world deployment. Previous works have studied this trade-off within the current AT paradigm, exploring various factors such as perturbation intensity, label noise and class margin. Despite these efforts, current AT methods still typically experience a reduction in clean accuracy by over 10\% to date, without significant improvements in robustness compared with simple baselines like PGD-AT. This inherent trade-off raises a question: whether the current AT paradigm, which assumes to learn the corresponding benign and adversarial samples as the same class, inappropriately combines clean and robust objectives that may be essentially inconsistent. In this work, we surprisingly reveal that up to 40\% of CIFAR-10 adversarial samples always fail to satisfy such an assumption across various AT methods and robust models, explicitly indicating the improvement room for the current AT paradigm. Accordingly, to relax the tension between clean and robust learning derived from this overstrict assumption, we propose a new AT paradigm by introducing an additional dummy class for each original class, aiming to accommodate the hard adversarial samples with shifted distribution after perturbation. The robustness \textit{w.r.t.} these adversarial samples can be achieved by runtime recovery from the predicted dummy classes to their corresponding original ones, eliminating the compromise with clean learning. Building on this new paradigm, we propose a novel plug-and-play AT technology named \textbf{DU}mmy \textbf{C}lasses-based \textbf{A}dversarial \textbf{T}raining (\textbf{DUCAT}). Extensive experiments on CIFAR-10, CIFAR-100, and Tiny-ImageNet demonstrate that the DUCAT concurrently improves clean accuracy and adversarial robustness compared with state-of-the-art benchmarks, effectively breaking the existing inherent trade-off.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Pointing out that the existing AT methods enforce the model to learn benign and adversarial samples are belong to the same class lead to the trade-off between clean and adversarial accuracy, this paper introduced a new AT paradigm introducing additional dummy classes for certain adversarial samples that differ in distribution from the original ones to relax the assumption of existing AT methods. Rather than strictly separating the class for benign and adversarial examples, this paper construct soft labels to explicitly bridge corresponding original and dummy classes as the suboptimal alternative target of each other, leading the model to learn separation between them. Experimental results across different baselines and tasks show effectiveness of the proposed method.

### Strengths
- This paper has strong motivation of tackling trade-off between clean and robust accuracy of existing AT methods, demonstrating existing methods all fail to some adversaries that proves the common deficiency of existing works' learning objectives.
- This paper is well written and easy to follow.

### Weaknesses
 - The proposed method seem to be incremental compared to TRADES.
   - Although the proposed method shows impressive improvement on PGD-AT, MART, and Consistency-AT, compared to the most important baseline that addressed the trade-off issue for the first time, TRADES, DUCAT sacrificed clean accuracy more than the improved robustness as shown in Table 1, especially on CIFAR-10. Also, the improvements achieved on CIFAR-100 and Tiny-ImageNet from the proposed method (DUCAT) are marginal while it requires additional computational resources compared to TRADES as shown in Figure 6. Based on this observation, it would be better to provide more supporting arguments on DUCAT compared to TRADES. The core issue is that while DUCAT improves robustness, it appears to do so at a cost of clean accuracy that is not fully justified by the gains, particularly when compared to TRADES which already addresses the trade-off. The computational overhead further exacerbates this concern, making the practical advantages of DUCAT less clear.
- Since this paper insists that if the adversarial examples generated from one model prove to be effective, they are might also effective and transferred to the different models. In responses, it would be beneficial to show the adversarial and standard accuracy under the transfer attack scenario to further strengthen the proposed method. The experiments can be done in the Figure 3 showing transfer attack scenarios across different training algorithms, where adversarial examples generated from ResNet18 model trained on DUCAT can be transferred to baseline methods, or vice versa. Rather than bar plot, it would be clearer to visualize the performance on CIFAR-10 and CIFAR-100 in the format of table. The lack of transferability analysis leaves a gap in understanding the generalizability of the robustness achieved by DUCAT. Specifically, it is unclear whether the model's improved adversarial robustness is specific to the training procedure or if it translates to better defense against attacks generated from different models.

### Questions
- In figure 2, there is different tendency in ratio between all failure/all worked cases for different class, why different classes show different tendency? It would be helpful to provide a more detailed analysis of the class-specific differences along with the dataset name and explain which factor of each class leads to different distributions for the results. Please examine properties of the different classes, for example, they could visual complexity, number of entities within example, what are the main differences captured by models between adversarial examples and clean examples using PCA analysis, which might affect to the tendencies in failure/success rates.

### Soundness
3

### Presentation
3

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
In this paper, the authors address the ongoing trade-off issue in adversarial training-based methods. To mitigate this problem, they introduce a dummy class and soft labeling techniques into the existing adversarial training framework. A novel adversarial training loss function is designed to improve the model’s trade-off between accuracy and robustness. The proposed method is evaluated on three datasets and compared against four state-of-the-art adversarial training approaches. Additionally, the authors analyze the impact of various hyperparameters on model performance.

### Strengths
1. Addresses a Key Limitation in Adversarial Training: The paper introduces a new adversarial training paradigm, DUCAT, which aims to break the inherent trade-off between clean accuracy and robustness, a well-known limitation in existing methods

2. Plug-and-Play Applicability: DUCAT is presented as a flexible method that can be integrated with existing adversarial training frameworks, potentially making it easier to adopt in practical applications without major redesigns.

### Weaknesses
1. Lack of In-depth Analysis of Method Efficacy: The proposed DUCAT method primarily leverages the concepts of dummy classes and label smoothing. However, previous studies (e.g., [1], [2], [3], [4]) have explored the effectiveness of either dummy classes or label smoothing to enhance robustness or accuracy. A more thorough analysis is needed to clarify the unique contribution of DUCAT in comparison to these established works. Specifically, the paper needs to clearly articulate how DUCAT's approach to using dummy classes differs from existing methods that use dummy classes for standard generalization, and how its soft label differs from conventional label smoothing techniques. The paper should also discuss why the specific design choices in DUCAT, such as the number of dummy classes and the way soft labels are constructed, are critical for achieving its performance gains, rather than being arbitrary choices. 

   [1] Label Smoothing and Logit Squeezing: A Replacement for Adversarial Training? https://arxiv.org/abs/1910.11585

   [2] Frustratingly Easy Model Generalization by Dummy Risk Minimization https://arxiv.org/pdf/2308.02287

   [3] When Does Label Smoothing Help?

    [4] MIXUP INFERENCE: Better Exploiting Mixup to Defend Adversarial Attacks https://openreview.net/pdf?id=ByxtC2VtPB

2. Limited Empirical Evidence: The experimental results, as seen in Table I, show only marginal improvements of the proposed DUCAT method over TRADES. Further analysis is recommended to understand the limited performance gains. The paper should provide a more detailed breakdown of the performance gains across different datasets and attack types. It should also investigate the potential reasons for the limited improvement, such as whether the method is more effective under specific conditions or datasets, and whether the observed gains are statistically significant.

### Questions
1. How does the proposed DUCAT method compare in depth to the above-mentioned related works? Could you elaborate on the unique aspects of its effectiveness?

2. What might be the reasons behind the limited performance improvement of DUCAT over TRADES?

3. Could you provide a performance comparison between the proposed DUCAT method and the technique outlined in [4]?

     [4] MIXUP INFERENCE: BETTER EXPLOITING MIXUP TO DEFEND ADVERSARIAL ATTACKS https://openreview.net/pdf?id=ByxtC2VtPB

### Soundness
2

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
4

### Summary
This paper proposed DUCAT, a new adversarial training paradigm that leverages dummy classes to achieve a better trade-off between adversarial robustness and clean accuracy. The introduced dummy classes relax the overstrict label assignment. As a plug-and-play method, DUCAT can be applied to existing adversarial training pipelines to help further improve performance. The effectiveness of DUCAT is demonstrated by extensive experiments across different datasets.

### Strengths
- The intuition behind introducing dummy classes is making sense to me.
- The paper is well-written and easy to follow.
- The proposed methods are evaluated on different datasets, baseline methods and network architectures.

### Weaknesses
 - I agree with the design of DUCAT and its effectiveness when applied to existing adversarial training methods, but a non-negligible fact is that the performance is still far away from methods like [1, 2, 3], which obtain higher clean and robust accuracy. Although DUCAT is a good plug-and-play method for adversarial training, I think the value is still limited if it cannot bring those AT-based baseline methods to a closer level to more advanced methods. Specifically, while DUCAT improves robustness, the absolute gains are not substantial enough to bridge the gap with methods that employ techniques like diffusion models or more sophisticated data augmentation strategies. The practical impact of DUCAT is therefore constrained by the performance ceiling of the underlying adversarial training methods it enhances.
- Some notations are not clearly explained. Please see the questions below.

### Questions
- What is $\mathcal{P}(x_i)$ in Eq. 2? The distribution of adversarial examples of $x_i$?
- What are $\dot{\mathbf{y}}$ and $\ddot{\mathbf{y}}$ in Eq. 4? Do they stand for probabilities of $C$ real classes and $C$ dummy classes respectively? Are you actually doing a decomposition $\mathbf{y} = \dot{\mathbf{y}} + \ddot{\mathbf{y}}$?
- What is $h_\theta^{Dummy}(\cdot)$? Another neural network? If I understand Fig. 1 correctly, the output representation of the second last layer is unchanged, and you just enlarge the dimensionality of the last layer? Can you clarify if you are using another neural network or just enlarging the last layer?
- How do you set the dummy classes for each example? 
- I am confused about the word "SOTAs" used in Sec 3.2. If it means those aiming at releasing the trade-off between accuracy and robustness, then we can find a bunch of methods overperforming them on RobustBench[4]. If it specifically refers to AT-based methods, then like what I mentioned in the weaknesses above, the value of DUCAT is limited as we can find more advanced methods. In fact, methods like [1] also involve adversarial training. If DUCAT is proved able to improve the performance of some of those methods, its value will be underscored.

[4] https://robustbench.github.io/

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new adversarial training method (DUmmy Classes-based Adversarial Training, DUCAT). DUCAT relaxes the strong assumption in adversarial training that requires clean samples and adversarial samples to be classified into the same category via introducing dummy classes. DUCAT can improve the model's adversarial robustness while achieving higher clean accuracy than existing AT methods such as PGD, TRADS, MART, and Consistency-AT.

### Strengths
This paper reveals that always-failed samples widely exist in existing AT methods and points out that this is caused by the overly strong assumption of AT on clean samples and adversarial samples. The corresponding dummy class method can improve the robustness of the model and, compared with existing adversarial training methods, shows an improvement in clean accuracy.

The organization and writing quality of the paper are both good.

### Weaknesses
1. The paper's title and the main claim is somewhat misleading (Breaking Inherent Trade-Off between Accuracy and Robustness). I don't think the proposed method indeed breaks the trade-off between accuracy and robustness. As shown in Table 1, the clean accuracy obtained via DUCAT is still significantly lower than standard training (for example, ResNet-18 can easily achieve accuracy higher than 93% under standard training). I suggest authors rephrase their claim to more accurately rephrase their claim to more accurately reflect the improvement over existing adversarial training methods, and also provide the clean accuracy of standard training for reference.
2. The use of soft labels instead of hard labels to enhance adversarial training performance somewhat limits the novelty of this paper; please refer to [1, 2, 3, 4], where [1] discusses injecting more learned smoothing during adversarial training, [2] proposes generating soft labels instead of hard one-hot labels to achieve more robust models, and so forth. Additionally, I believe that the one-versus-the-rest loss proposed in [4] already shares a similarity with the ideas presented in this paper.

### Questions
I believe the authors should reconsider the terms in which they claim the contributions of the article. Instead of stating that it has broken the inherent trade-off between accuracy and robustness, this paper should more accurately be described as reducing the loss of clean accuracy while enhancing adversarial robustness.

Also, I would like the authors to elaborate on the differences and major innovations in their approach and related work (please refer to the weaknesses session 2).

### Soundness
2

### Presentation
3

### Contribution
2
