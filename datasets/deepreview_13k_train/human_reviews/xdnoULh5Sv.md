# CARSO: Blending Adversarial Training and Purification Improves Adversarial Robustness

- Decision: Reject
- Scores: 5, 5, 5, 1

## Abstract
\label{sec:abstract}
    In this work, we propose a novel adversarial defence mechanism for image classification -- \textsc{Carso} -- blending the paradigms of \textit{adversarial training} and \textit{adversarial purification} in a synergistic robustness-enhancing way. The method builds upon an adversarially-trained classifier, and learns to map its \textit{internal representation} associated with a potentially perturbed input onto a distribution of tentative \textit{clean} reconstructions. Multiple samples from such distribution are classified by the same adversarially-trained model, and an aggregation of its outputs finally constitutes the \textit{robust prediction} of interest. Experimental evaluation by a well-established benchmark of strong adaptive attacks, across different image datasets, shows that \textsc{Carso} is able to defend itself against adaptive \textit{end-to-end} \textit{white-box} attacks devised for stochastic defences. Paying a modest \textit{clean} accuracy toll, our method improves by a significant margin the \textit{state-of-the-art} for \textsc{CIFAR-10}, \textsc{CIFAR-100}, and \textsc{TinyImageNet-200} $\ell_\infty$ robust classification accuracy against \textsc{AutoAttack}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- Draft presents a method for defending against adversarial attacks
- Specifically, the proposed method maps the feature representations of (normal or adversarial) inputs (extracted by an adversarially trained classifier) to a sample of tentatively clean reconstructions. This mapping is realized via a conditional variational encoder (VAE).
- An estimate of the clean inference is obtained by fusing the inference of adversarially trained classifier on multiple reconstructed features (o/p of VAE)
- Experiments are performed on CIFAR-10 and CIFAR-100 datasets.
- Better results are reported than other methods compared against.

### Strengths
- The idea of generative purification from adversarially trained feature representations - despite being a new combination of existing ideas - appears interesting in the context of adversarial defense.

### Weaknesses
 - Generative model-driven purification as a defense against adversarial attacks has been established to a reasonable extent. Existing works demonstrated the effectiveness of this framework using denoising autoencoders (DAE), UNet-based DAE, GAN, VAE, etc. (section 2 of the draft provides references). However, scaling to complex datasets such as ImageNet has been challenging in this context. This draft restricts the experimental analysis only to simpler datasets (CIFAR). Since sophisticated models that are adversarially trained on ImageNet dataset are available easily, readers would expect the draft to experiment with them too.
- Clarity of the framework description needs slight improvement (please refer to the questions section of the review).
- It is not discussed clearly in the draft what the improvement in the proposed method is compared to existing purification methods. The draft claims that their method adds a smoothness penalty to the reconstruction loss. However, not much has been discussed on it. Specifically, the mechanism by which this smoothness penalty is implemented and its effect on the reconstruction quality and adversarial robustness is not clear. The paper lacks a detailed analysis of how this penalty contributes to the overall performance, and how it compares to other regularization techniques used in similar generative models. Furthermore, the specific form of the smoothness penalty is not provided, making it difficult to assess its impact.

### Questions
- The draft reads that to sample from the generative model in the proposed framework, the auxiliary encoder $\mathcal{D}$ is unnecessary. However, it appears that the sampling process needs the encoder's output - which is driven by both the auxiliary encoders $\mathcal{C}$ and $\mathcal{D}$ -  concatenation of $z_i$ and $c'$. Authors may provide a clarification for this.
- In section 4.5, it is mentioned that the proposed approach - instead of including the conditioning on tensor, which is customary to the conditional VAEs- designed a DGDN-based decoder. However, the schematic representation in Figure 1 depicts the decoder being conditioned on the output of the auxiliary encoder $\mathcal{C}$. Authors may provide clarity on this discrepancy.
- How is it different to learn the purifier from the feature space of an adversarial trained classifier than learning from that of a normally trained classifier?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes adversarial defense to natural image classifiers by blending adversarial training with adversarial purification. Besides, a bag of tricks were used to improve defensive capability. Experiments were also conducted on CIFAR-10 and CIFAR-100 to show its effectiveness.

### Strengths
- The studied problem and the proposed method are interesting and the paper is easy to follow.
- Experiments in Table 2 showed that the robust accuracy of the proposed method is competitive with state-of-the-art methods.

### Weaknesses
 - I'm not sure whether the defensive effectiveness comes from the combination of adversarial purification and adversarial training or the bags of tricks utilized in this work.
- In Table 2, please explicitly mention the state-of-the-art method and its reference rather than vaguely refer to sota in RobustBench as the sota can change with time, and it's unclear whether it's fair to compare ith sota as the experimental settings (architecture, training setups may vary).
- Besides robust accuracy, why not compare with sota regarding clean accuracy, while in the present form, it seems the authors only reported comparisons with standard adversarial training (2018).

### Questions
See weakness.

### Soundness
3 good

### Presentation
2 fair

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
This paper proposed a method that incorporates two types of adversarial learning methodologies, adversarial training and adversarial purification, to improve adversarial robustness. The authors conducted experiments with the datasets CIFAR-10/100 to evaluate the adversarial robustness against AutoAttack and clean accuracy.

### Strengths
+ The C+AT/rand-AA improves over the baseline AT/AA, verifying the proposed method improved the adversarial robustness.

### Weaknesses
- Only evaluate the method on CIFAR-10 and 100, which are from the same image distribution. Should also evaluate other different datasets for comprehensiveness.

- Adversarially pre-trained models are used as the classifier in the proposed method. Should also compare with those methods following the same setting for fairness.

- The authors showed training times for different scenarios. It should be compared with other methods. Also, the comparison on inference time should also be given to evaluate the efficiency.

### Questions
1. Are there any other previous papers that have considered incorporating adversarial training and adversarial purification in a unified framework? If yes, please list them.

2. The authors mentioned they draw inspiration from neurocognitive processes underlying cued recall and recognition. Please elaborate a little bit more details about this neurocognitive process and why it inspires the proposed method.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this work, the authors introduce a novel adversarial defense mechanism named CARSO, which combines adversarial training and adversarial purification techniques to enhance the robustness of image classification models. CARSO leverages an adversarially-trained classifier to map potentially perturbed input data to a distribution of clean reconstructions, aggregating multiple samples from this distribution to make robust predictions. Experimental results across various benchmarks demonstrate that CARSO effectively defends against a wide range of adaptive attacks, significantly outperforming existing methods in terms of robust classification accuracy on datasets like CIFAR-10 and CIFAR-100, especially against AutoAttack.

### Strengths
Authors proposed a new method combining AT and purification methods for advesarial attack defence.

### Weaknesses
1. Author used a method of mixing purification and AT,
 but I don't think it is fair to only have an ablation study in AT.
I wonder comparison between purification method vs CARSO + purification method.

2. It was said that the motivation for separating the scenarios was due to a lack of clean image accuracy, 
but as a result, the same difference is shown in (c) and (d).
 So, I don’t think that dividing the scenario and showing the experiment is an important part of the paper. 
Rather, the logic that it was used in the expect of obtaining an internal representation 
from a more refined classifier in order to perform SOTA on a robust image seems more appropriate.

3. Author made an analogy about the method using terms(cued recall and recognition) from cognitive science, 
but it doesn't seem to be clear.

4. Too much limited and insufficient experiments: There are no state-of-the-art defense baselines such as AWP [1], SCORE [2], and ADML [3], and no larger-scale dataset such as ImageNet. In addition, based on ADML, not only CNN structure and Transformer structures seems needed to validate.

5. Table 2 conducted an ablation study comparing effect of the CARSO method. Clean image performance significantly decreases but the current state-of-the-art ADML method highly increases clean image performacne despite few epochs within 3-5 epochs based on their official code. I did not understand the major contribution compared by ADML.

### Questions
Refer to Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
