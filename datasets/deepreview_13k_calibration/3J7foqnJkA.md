# Understanding Parameter Saliency via Extreme Value Theory

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Deep neural networks are being increasingly implemented throughout society in recent years. It is useful to identify which parameters trigger misclassification in diagnosing undesirable model behaviors.
The concept of parameter saliency is proposed and used to diagnose convolutional neural networks (CNNs) by ranking 
convolution filters that may have caused misclassification on the basis of parameter saliency.
It is also shown that fine-tuning the top ranking salient filters efficiently corrects misidentification on ImageNet.
However, there is still a knowledge gap in terms of understanding why parameter saliency ranking can find the filters inducing misidentification.
In this work, we attempt to bridge the gap by analyzing parameter saliency ranking from a statistical viewpoint, namely, extreme value theory.
We first show that the existing work implicitly assumes that the gradient norm computed for each filter follows a normal distribution.
Then, we clarify the relationship between parameter saliency and the score based on the peaks-over-threshold (POT) method, which is often used to model extreme values.
Finally, we reformulate parameter saliency in terms of the POT method, where this reformulation is regarded as statistical anomaly detection and does not require the implicit assumptions of the existing parameter-saliency formulation.
Our experimental results demonstrate that our reformulation can detect malicious filters as well.
Furthermore, we show that the existing parameter saliency method exhibits a bias against the depth of layers in deep neural networks.
In particular, this bias has the potential to inhibit the discovery of filters that cause misidentification in situations where domain shift occurs.
In contrast, parameter saliency based on POT shows less of this bias.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the topic of parameter saliency to understand misclassifications in neural networks. Unlike some prior works which focus on input saliency maps, parameter saliency is shown to be helpful to correct for misclassifications. Building over prior work, the paper formulates the ranking of salient filters through connections with statistical anomaly detection and extreme value theory. Empirical experiments show that the approach leads to plausible conclusions.

### Strengths
- As deep learning finds more and more applications in daily-life, interpretability is getting more important. The idea of focusing on parameter saliency is an interesting approach towards interpretability and model surgery. 
- I am not an expert in the topic, but the paper is well written for the most part. Key ideas and intuitions are well explained. 
- The approach is evaluated on multiple architectures and datasets.

### Weaknesses
 - 5.1.2 : "We performed one step fine-tuning .. " -> Is the finetuning and validation being done on the same dataset ? 
- The interpretations in Figure 4 are not clear, especially the conv5_x curve and its relation to the proposed approach. 
- I think it will be more intuitive to think of %improvement in downstream performance rather than %corrected samples. 
- How do you differentiate between label errors and misclassification ? 
- A lot of things seem to have changed when moving to the domain adaptation experiments : architecture, dataset, model size, pretraining. Instead, it would be beneficial to show results on domain adaptation datasets like ImageNet-C, DomainNet etc. 
- I am not too convinced with the one-step finetuning process apart from being "easy" to do. 
- 4.3 : "anomalous behavior of filters.. is a rare event" - Can the authors give more insight into when would this hold ? Perhaps as a function of class difficulty, model size, dataset size.

### Questions
Please refer to questions in the weaknesses section. 

[Minor] Writing suggestions:
- Fix tense : Abstract, ".. has efficiently corrected .. " 
- Section 1 : "model's decision" ^making "process" ? 
- Section 2 : "importance" -> "Importance"
- Reword title of Section 3.2
- Section 5 : "FOr the pruni .. "

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigated the parameter saliency for a CNN through the lens of EVT and provided POT-saliency.
This paper also analyzed the property of the original and POT-saliency ranking methods and found that the
POT-saliency ranking method chooses from a wide range of convolutional layers while the baseline
method has a bias to choose from the later part of the layers.

### Strengths
originality - The proposed concept is interesting. The POT-salience method is expected to introduce semantic features to the framework POT and hence improve the classification performance. 

quality - The paper presents theoretical and experimental results to demonstrate the proposed algorithm. Both theory and experiments are comprehensive. 

clarity - The experimental section clearly shows that the proposed POT-salience algorithm performs better than the other methods in different settings. 

significance - Upon the justified theory, the proposed method will have strong impacts on the standard CNN architecture.

### Weaknesses
originality - Very confusing explanations on the new proposal in this paper. For example, it is not clear how to link Theorem 1 in Eqs. 3 and 4 with the POT method?  More detailed discussion is used to demonstrate the novelty.

quality - The entire paper reads imbalanced due to the heavy weights on the theoretical justification.  The proposed algorithm lacks a full scale algorithmic discussion, including parameter update and initialization.

clarity - The current form of the paper is confusing in terms of the theoretical proof. There is no clear algorithmic flowchart and discussion. The experimental results are partial and lacks comparisons against different POT variants. 

significance - The outcomes of the experiments are not significant, compared against those of the other state of the arts.

### Questions
1. How does the proposed POT algorithm work? A flowchart may be used to help the discussion.
2. More comparison experiments need to be conducted but the current version is weak in terms of experimental work.
3. How will the parameters in the proposed POT system affect the system performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study falls into the field of parameter saliency in XAI. The draft proposes to apply the peaks-over-threshold (POT) technique on neural networks to locate salient parameters or filters. The POT is a solution in the Extreme Value Theory in statistics for anomaly detection.

### Strengths
This study explores a very important task in AI, explaining the black-box network. And it focuses on a very interesting topic, which parameters are salient or important in classification(misclassification).

### Weaknesses
Before discussing the weaknesses, I have to admit I have more expertise in CS, and my knowledge in statistics is limited. I might ask some naive questions and please correct me if I am wrong.

The structure of the draft can be better organized for a better readability, the current version is a little confusing. The overall idea is applying an existing method from statistics, POT, to locate salient parameters. The main baseline is (Levin 2021) which also studies the parameter saliency. However, the motivation of this study is not well introduced. In the introduction and the related work, a list of studies in XAI and statistics are sequentially displayed without discussing what kind of problems this draft can solve. For instance, Sec.2 "Related work", Interpretability, this paragraph is more like a basic tutorial, which is not directly related to this study, neither it is complete. The second paragraph in Sec2 is more about the CAM-based, which is not in the parameter space. I would suggest only discuss the most related parameter saliency, and POT related studies.

Preliminary 3.1 is re-introducing the study (Levin), which is not necessary. The most important part is missing in that section, whats the limitation in the previous solution(Levin) and how this solution can solve that. I can grab some scatter information from the draft, previous study assumes the gradient follows a normal distribution, and this assumption may not hold, as discussed in Motivation Sec 4.1. I cannot see a clear demonstration that POT can solve this problem or I might miss this. Prior to the solution, this draft didnot showcase the problem of the normal distribution assumption. I know most CS scientist naively assume normal distribution, because it is simple yet effective. If this assumption is problematic, they can simple assume a more specific distribution. Could the normal distribution be "simple" enough for the study now? From the view of the solution, Appendix C, EVT normally add more assumptions to catch more distributions, which means the solution could be either not necessary (the normal assumption is enough) or limited (could the combined EVD catch everything?) I might miss something in the paper, proposition 1 and appendix B also are based on normal distribution, can I ask why a simple normal distribution can be representative enough in this problem raised?

Without a clear problem introduction, the proposed method is not clear and convincing in enough at this moment. And the results in Figs 3 and 4 also show that the difference is tiny, which echos the question, do we really need a more complicated distribution for this purpose now?

Tiny suggestion, I know Figs 3 and 4 have different components, but it is better to use the same colour and the same name of the same thing, e.g., POT vs Levin, or (proposed vs baseline). I searched around the paper, has the term "baseline" been explained?

### Questions
Please see the question listed above, the current draft randomly grabbing a technique from statistics to CS without introducing the need. Thus the clarity and novelty could be further improved before publishing.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
