# Safeguarding Data in Multimodal AI: A Differentially Private Approach to CLIP Training

- Decision: Reject
- Scores: 1, 8, 8, 1

## Abstract
The surge in multimodal AI's success has sparked concerns over data privacy in vision-and-language tasks. While CLIP has revolutionized multimodal learning through joint training on images and text, its potential to unintentionally disclose sensitive information necessitates the integration of privacy-preserving mechanisms. We introduce a differentially private adaptation of the Contrastive Language-Image Pretraining (CLIP) model that effectively addresses privacy concerns while retaining accuracy. 
Our proposed method, \dpclip, is rigorously evaluated on benchmark datasets encompassing diverse vision-and-language tasks such as image classification and image captioning. 
We demonstrate that our approach retains performance on par with the standard non-private CLIP model. Furthermore, we analyze our proposed algorithm under linear representation settings. We derive the convergence rate of our algorithm and show a trade-off between utility and privacy when gradients are clipped per-\textit{batch} and the loss function does not satisfy smoothness conditions assumed in the literature for the analysis of DP-SGD.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposed DP-CLIP, a method of continued pretraining CLIP in a privacy-preserving manner. They demonstrated the competitive performance of DP-CLIP on image classification and image captioning tasks, and proved the utility-privacy trade-off in a simplified learning setting.

### Strengths
- Studying the privacy risks in multimodal learning is a relevant and important research topic
- It is nice to a see a formal characterization of the utility-privacy trade-off

### Weaknesses
I found the experimental section to be very problematic. Specifically, 
- Framing the algorithm as "DP-CLIP" is very misleading. You didn't train a CLIP model from scratch using DP-SGD, but rather continue pretraining a **well-trained** model in a privacy-preserving manner. This is not mentioned in the abstract, and is not made clear until the experimental section. As a side note, the comparison with Yu et al. (2023) is unfair: 1) there are obviously no "two stages" in your algorithm since you only performed continued pretraining; 2) Yu et al. (2023) only pretrained on synthesized textures to speedup the DP training process, while the starting point of your DP training is already a very strong model.      
- The classification tasks are too simple given the power of the pretrained model. It might not be necessary at all to perform private continued pretraining; plus I found pretraining on datasets such as MNIST and CIFAR-10 to be super weird. Two critical baselines are currently missing: the accuracy of the vanilla CLIP model (without continued pretraining), and the accuracy of $\varepsilon=\infty$ (non-private continued pretraining). 
- The comparison with other baselines in Section 4.2 is arbitrary and careless. The authors didn't evaluate the same set of methods on all datasets, and didn't report whether the results for other algorithms are based on their own implementation or directly copied from prior works. The accuracy of DP-Sinkhorn on Fashion-MNIST does not match the one reported in the original paper. It is also unclear whether these algorithms are indeed the state-of-the-art methods in image classification. Finally, DP-Sinkhorn is not even a DP image classification method -- while it is capable of performing such task, it is essentially an algorithm of DP data synthesis (take a look at [1] if you are not familiar with this concept). It is unbelievable that the authors chose this method for comparison.
- I didn't buy the results from Section 4.3; particularly, I have never seen using $\varepsilon = 1e-4$ in the privacy literature, and it is hard to believe that such privacy budget could still lead to a meaningful model (in the extreme case $\varepsilon=0$, the model will become completely random). On the other hand, the authors seemed to suggest that the model's performance is mostly unaffected even in this extreme case. I insist: 1) report the $\sigma$ (the noise multiplier), and check the SNR to see whether the results make sense; 2) use $\varepsilon=1e-8$ and see whether the results are still consistent; 3) use the vanilla CLIP model (without any further continued pre-training) and see whether the results are already very good. Other issues in this section: 1) there is no description of the non-private model, I have completely no idea what "IBM Research AI" is and whether the comparison with DP-BLIP makes sense at all; 2) it is unclear why a baseline of non-private BLIP is missing.  

Minor:
- The experiments should be running over multiple random seeds, and please include the standard deviations in the tables
- The dataset paragraph should be revised. The descriptions of the datasets are way too long yet important details are missing (e.g., the dimensionality of each dataset). The metrics used in image captioning are not explained. 
- "TensorFlow Privacy": which privacy accountant did you use exactly? As a side note, RDP and PRV accountant are the go-to choices nowadays. 
- The paragraph below Table 2: "which is not present for DP-SGD" -- please note that the pretraining and extra caption data are not used in other baseline methods as well
- Various grammatical issues, included but not limited to: "while a smaller or equal $\varepsilon$" -> "with a smaller or equal $\varepsilon$"; "allow our private approach to achieving" -> "to achieve"; "Apart from their work" -- I don't understand what you meant here; "requires... should be indistinguishable" --> "to be indistinguishable". Please do a professional proofreading before submitting your work. 

In light of the major issues in the experimental section, this paper is clearly below the bar of ICLR and I will strive for a rejection.

### Questions
See above

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces DP-CLIP, a differentially private adaptation of the CLIP model for vision-and-language tasks, addressing privacy concerns while maintaining accuracy. CLIP and similar models have been shown to inadvertently disclose sensitive information, making privacy-preserving mechanisms crucial. DP-CLIP employs per-batch clipping to protect privacy and achieves strong performance on various benchmark datasets, such as image classification and visual question answering. The paper also discusses the privacy-utility trade-off under linear representation settings. Overall, DP-CLIP represents a important effort to enhance privacy protection in multimodal models, offering a significant reduction in data exposure risk while maintaining task performance.

### Strengths
1) The paper is the first to apply differential privacy approaches to multimodal training in the context of vision-language tasks, which is a much needed effort in enhancing privacy protection for such models.
2)  The paper conducts extensive experiments on different vision-language tasks, including image classification and image captioning, to evaluate the effectiveness of DP-CLIP across diverse datasets and privacy parameters. The paper provides a thorough comparison with related work in the field of differential privacy and vision-language tasks, ensuring that the contributions of DP-CLIP are well-placed 
2) Paper is very well written and easy to follow.

### Weaknesses
1) The paper employs smaller classification datasets such as MNIST, Fashion-MNIST, CIFAR-10, and SVHN. It would have been preferable to observe results at the Imagenet scale, but I understand that the computational resources required for such experiments would have been substantial.

2) No comparison with real-world threat models has been provided. Epsilon-utility trade-offs can be misleading without testing them against actual attacks, as epsilon guarantees are built upon numerous assumptions, as indicated in [1].

### Questions
see weakness section

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel method called DP-CLIP to make CLIP training differentially private.
The method performs per-batch gradient clipping, which is needed as the CLIP loss is non-decomposable.
However, the implementation is reduced to setting the number of micro-batches to 1 in standard DP-SGD implementation, which is neat.
Empirically, the paper shows that DP-CLIP has a better privacy-utility trade-off than alternative methods in a setup based on pre-trained embedding followed by fine-tuning on private datasets, for classification and QA.
The paper also derives a theoretical bound for the privacy-utility under linear representation settings, which is novel as the loss function is not smooth as in other analysis of DP-SGD.

### Strengths
**significance** The paper studies an important problem of privacy in multi-modal learning with the widely-used CLIP loss and proposes a novel method to make the training DP. The proposed method shows promising privacy-utility trade-off empirically.

**originality** The proposed method and theoretical results in the paper are both novel. The bound derived in section 5 seems to be non-trivial given that the loss is not smooth.

**quality** The proposed method and the presented theoretical results are sound.

**clarity** The paper is well-written and easy to follow.

### Weaknesses
The comparison in table 2 seems to be unfair.
I assume the competitive methods does not use any pre-trained model so I'm not sure how to read the results.
Perhaps one should use the same pre-trained models and then apply the corresponding DP-method for fair comparison.

### Questions
I'm concerned that the private fine-tuning dataset is contained in the pre-training set, or at least very similar data.
Have the authors checked the following facts?
- Does the training set of the pre-trained CLIP contain MNIST-like images?
- How different is the vizwiz image captioning dataset from the training set?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a CLIP fine-tuning technique that is DP. The idea is to maintain the CLIP contrastive training also at fine-tuning time: to circumvent the issue of having to produce per-sample gradients, the authors propose to apply the gaussian mechanism on the per-batch gradients. The authors make sure this is DP, and carry out an empirical and theoretical analysis about it.

#### 
POST-REBUTTAL: In lack of any response addressing my major concerns, I decrease my score.

### Strengths
- The literature of DP in multi-modality is lacking, and therefore the work could be interesting

### Weaknesses
 - There are several factually inappropriate usages of the notion of DP. DP is not "incorporated" in a model or multimodality (as the authors mention in different ways a few times throughout the paper), DP is a property of a randomised algorithm (in this context, the training algorithm that produces the distribution of models, not the model). 
- Proposition 3.1 is a trivial consequence of the basic theorems of DP, and Algorithm 1 is a simple modification of DP-SGD (that is already available in standard DP-training libraries). The only interesting aspect is adapting the training procedure to contrastive learning, which is trivial. Therefore the novelty of these components of the paper is negligible.
- It is unclear why the zero-shot prediction of CLIP is not used as a baseline (as it would be equivalent to epsilon = 0). Furthermore, the authors are neglecting parameter efficient fine-tuning baselines, for instance like [1]. The description of the baselines is lacking and quite confusing: it's not clear why the authors have two DP-SGD baselines, and what they're exactly updating during training.
- The experimental analysis focuses exclusively on known computer vision datasets that do not differ from the training distribution of CLIP. It would be useful if following the suggestions of [2,3] the authors could present results in settings with low data regimes and with significant distribution shift with respect to the pre-training set, which represents a more realistic application setting.  Furthermore, the authors deliberately avoid settings where DP is known to be hard due to the relatively low amount of training data per class (e.g. CIFAR-100/ImageNet).
- Not accounting for the privacy loss incurred in tuning the hyperparameters is a problem. Simply because baselines have done that, it doesn't justify the authors from reporting inflated numbers. I would recommend the authors to at least assume the availability of some public data that is kept out of training and evaluations and to run all the baselines fairly in this setting. 
- BLIP is definitely no more state-of-the-art as the authors claim. Several more sophisticated VLMs have been released since BLIP, e.g. LLaVa 1.5. 
- There are several grammatical errors and typos, and the overall presentation is a bit poor. Sections 5 onwards feel disconnected from the rest of the work. 

### Questions
- CLIP is relatively old. Novel variants of CLIP may yield zero-shot (epsilon = 0) performance that is higher and might reduce the room for improvements achievable under DP constraints. Could the authors consider the latest and strongest CLIP-inspired architectures?
- Since the gaussian mechanism is not applied at a sample level but at a mini-batch level, are the authors making a fair comparison between the $\epsilon$ values of their technique and the baselines?
- Could the authors show the result of applying the contrastive clip fine-tuning for $\epsilon=\infty$? To know what's the upper bound on accuracy of the DP variant.
- Why the baselines selection varies based on the choice of the dataset?

### Soundness
3 good

### Presentation
1 poor

### Contribution
1 poor
