# Forget-Me-Not: Making Backdoor Hard to be Forgotten in Fine-tuning

- Decision: Reject
- Scores: 5, 6, 6, 3

## Abstract
Backdoor attacks are training time attacks that fool deep neural networks (DNNs) into misclassifying inputs containing a specific trigger, thus representing serious security risks. However, due to catastrophic forgetting, the backdoor inside the poisoned models can be gradually removed under advanced finetuning methods. It reduces the practicality of backdoor attacks since the pretrained models often undergo extra finetuning instead of being used as is, and the attacks gradually lose their robustness given various finetuning-based backdoor defenses. Particularly, recent work reveals that finetuning with a cyclical learning rate scheme can effectively mitigate almost all backdoor attacks. In this paper, we propose a new mechanism for developing backdoor models that significantly strengthens the durability of the generated backdoor. The key idea in this design is to coach the backdoor to become more robust by exposing it to a wider range of learning rates and clean-data-only training epochs. The backdoor models developed with our mechanism can bypass finetuning-based defenses and maintain the backdoor effect even under long and sophisticated finetuning processes. In addition, the backdoor in our backdoored models can persist even if the whole model is finetuned end-to-end with another task, causing a notable accuracy drop when the trigger is present. We demonstrate the effectiveness of our technique through empirical evaluation with various backdoor triggers on three popular benchmarks, including CIFAR-10, CelebA, and ImageNet-10.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The key contribution of this paper is to demonstrate that fine-tuning (regardless of the techniques used) is not a proper defense against backdoor attacks. The paper specifically evaluates the two fine-tuning approaches: super fine-tuning and FT-SAM by Zhu et al. By simulating their fine-tuning mechanisms in backdoor training, the attacker can inject backdoors more robust to the fine-tuning techniques. In evaluation with various backdoor attacks, the paper shows their backdoor attacks become more resilient against fine-tuning.

### Strengths
1. The paper shows (advanced) fine-tuning cannot be a backdoor defense.
2. The paper runs extensive experiments to validate their claims.
3. A well-written paper; easy to follow.

### Weaknesses
1. Unfortunately, we don't believe fine-tuning can be a backdoor defense.
2. The paper is written to prove the point that we already believe.
3. The experimental results are not 100% convincing.

Detailed comments:

I like this paper showing (or re-confirming) that fine-tuning cannot be an effective defense against backdoor attacks. Even if there are manuscripts making bold claims like "fine-tuning is effective," I don't believe that it is the case: their positive results are coming either (1) from running fine-tuning with longer epochs or large learning rates (often) or (2) from an adversary unaware of their fine-tuning methods.

So, I am a bit positive to have this paper as empirical evidence showing that existing claims are not based on a concrete security analysis.

----

However, we also know that fine-tuning cannot be a defense; a vast literature on backdoor attacks evaluated fine-tuning and confirmed that it is ineffective (note that it is not against this advanced fine-tuning). We already have a skepticism about fine-tuning. 

So, on the other hand, it is less scientifically interesting to prove that we already know with empirical evaluation. I am a bit confident that even if the two prior works are out to the community, no one will believe that fine-tuning can become an effective countermeasure.

----

I also find that the paper puts a lot of effort into emphasizing fine-tuning as a defense seriously considered in the community. But it often gives an incorrect view of the prior work, which I want the authors fixing them before this manuscript will be out to the community.

For example, papers like NeuralCleanse do not consider fine-tuning as a primary mean to defeat backdoors. The key idea was to "reconstruct" the trigger from a set of assumptions about backdooring adversaries. Once we know what was used as a backdoor trigger, the fine-tuning is a natural next step to "unlearn" the backdoor behaviors. It is not the same as one uses fine-tuning without knowing the trigger, which should be addressed and fixed in the paper. 

I found more like this in the introduction and backdoor defense section.

----

Finally, sometimes fine-tuning reduces their attack's success rate. This (as-is) can be shown as the effectiveness of fine-tuning (as at least the success rate has been decreased). 

To be a more concrete claim, the results have to be compared with a baseline. What would be the baseline? The cases where we reduce the attack success rate to 50%? It was not clear in the paper; therefore, the claims discussing the effectiveness of fine-tuning can also be controversial ---even if I don't believe that fine-tuning works.

### Questions
My questions are in the detailed comments above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper explores a backdoor attack method called "Forget Me Not", which aims to overcome the catastrophic forgetting problem during model fine-tuning. Specifically, this paper proposes a backdoor learning method based on a cyclic learning rate policy that enhances the persistence of existing backdoor methods. The aforementioned method can bypass fine-tuning-based backdoor defenses and maintain effectiveness during complex fine-tuning processes. The authors demonstrate the effectiveness of the proposed method on three popular benchmark datasets.

### Strengths
1. Clear background introduction. the article provides readers with a thorough review of backdoor attacks and related work in the introductory section, providing good background knowledge.
2. Reasonable experimental design. The experimental setup and presentation of results in the article are clear, providing readers with an intuitive sense of the effectiveness of the method.
3. Clear charts and graphs. the charts and graphs are well-designed and help readers understand the content of the article.

### Weaknesses
1. Insufficiently detailed description of the methodology. When describing the "Forget Me Not" method, the details in some parts of the article are not clear enough. It is suggested that the authors provide more detailed algorithm description or pseudo-code in the method section so that readers can understand and reproduce better. 2.
2. The related work section can be expanded. Although the article has listed some related works, there are other important works in the field of backdoor attacks that can be referenced. In addition, I would like to know the rationale or justification for choosing these seven attack methods as representative methods. It is not possible for the authors to exhaust all the attack methods and prove the enhancement of backdoor persistence by the method, but I think representative methods need to be chosen to prove the comprehensiveness of the experiments.
3. Results of other defense experiments. Although the authors compare many fine-tuning-based defense methods to prove the effectiveness of the proposed backdoor, I am still concerned about whether the existing attack methods are able to overcome the existing backdoor defense methods, such as data cleansing methods, model modification methods, and model validation methods.
4. Analysis of defense strategies. Considering the potential threat of backdoor attacks, it is recommended that the authors discuss possible defense strategies or propose corresponding challenges in their articles.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
4 excellent

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
This paper presents FMN, a novel attack method to strength trojaning attacks (backdoor attacks) against DNNs. The key components of FMN are  the cyclical learning rate and the clean-backdoor interleaved training. The experimental results in this paper show that FMN successfully strengthens several existing trojaning attacks against several existing defense methods, i.e., the ASR remains high even if the backdoored model is purified by the defense methods.

### Strengths
1.FMN is compatible with various backdoor attacks.
2.The experimental results show that FMN can significantly increase the ASR of the mitigated backdoored model.

### Weaknesses
1.This paper should contain more analysis about the reason why  the cyclical learning rate and the clean-backdoor interleaved training work. Specifically, the paper lacks a rigorous explanation of how these two components interact to achieve the observed increase in attack success rate. It would benefit from a more detailed discussion of the underlying optimization landscape and how the proposed training strategies navigate it, leading to more robust backdoors. The current explanation is insufficient, leaving the reader to speculate about the precise mechanisms at play.
2.Though empowering existing backdoor attacks is an interesting idea, this paper should further investigate how to defend against FMN-powered backdoor attacks. The paper primarily focuses on the attack side, and the absence of any discussion on potential countermeasures is a significant weakness. The lack of defensive considerations limits the practical implications of the work, as it does not offer any guidance on how to mitigate the proposed threat. It would be valuable to explore potential defense strategies, even if they are preliminary, to make the contribution more complete.

### Questions
1.What is the reason that the cyclical learning rate and the clean-backdoor interleaved training can work?
2.Are there any possible defense strategies against FMN?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies how to maintain stable attack performance of inserted backdoor triggers during robust tuning process. Specific to current superFT method, the authors also adopt a cyclical learning rate scheme during inserting backdoor triggers.

### Strengths
1. The studied problem is important. How to construct more robustly inserted backdoor triggers is interesting.

### Weaknesses
Limitations and lacking of ture explanations.
1. Limitations:
- The proposed method is limited: The proposed attack method is specific to superFT which adopt a cyclical learning rate scheme. It is not clear whether other defense methods are equally effective, such as ANP [1]. I believe adopting a cyclical learning rate scheme is not a proper choice for inserting backdoors. The main reason is that it is very hard for attackers to tune its hyperparameters. The authors do not provide any details about how to choose parameters for this cyclical learning rate scheme. I also notice that the authors only evaluate ResNet models. Do we need different hyperparameters on different models?
- As mentioned in above point, the authors do not evaluate other pruning-based methods like ANP [1] and RNP [2]. I think the author need to evaluate these defense methods to show effectiveness of proposed attack method. 
- Comparsions with existing advanced backdoor attacks: [3] proposed more stealthy and robust backdoor attacks without controlling training process. And, I also strongly suggest that the authors should evaluate more diverse attack settings like lower poisoning rate (1%).

2. Lacking of ture explanations: The intuition behind proposed method is too hauristic. Apart from evaluation of ASR, the authors do not provide any evaluation about proposed hypothesis. Actually, we are not sure whether it leads to more flat and stable minimum with inserted triggers. The author could provide loss landscape analysis to verify this point.  
I think the authors are not familiar with loss landscape anaysis of DNN models. Adopting a cyclical learning rate scheme can not gaurantee searching a flat and stable local min. We could adopt SWA [4] to achieve this goal.

### Questions
Please see Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
