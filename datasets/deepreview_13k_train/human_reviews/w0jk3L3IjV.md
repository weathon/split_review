# Breaking the Detection-Generalization Paradox on Out-Of-Distribution Data

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
This work studies the trade-off between out-of-distribution (OOD) detection and generalization. We identify the Detection-Generalization Paradox in OOD data, where optimizing one objective can degrade the other. We investigate this paradox by analyzing the behaviors of models trained under different paradigms, focusing on representation, logits, and loss across in-distribution, covariate-shift, and semantic-shift data. Based on our findings, we propose Distribution-Robust Sharpness-Aware Minimization (DR-SAM), an optimization framework that balances OOD detection and generalization. Extensive experiments demonstrate the method's effectiveness, offering a clear, empirically validated approach for improving detection and generalizationability in different benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces the concept of the Detection-Generalization Paradox and analyzes the detailed reasons why existing OOD-D and OOD-G methods lead to this phenomenon. It proposes DR-SAM to simultaneously enhance the model's detection and generalization capabilities for OOD data.

### Strengths
1. This paper decomposes the inference process and provides a detailed analysis of the reasons behind the Detection-Generalization Paradox.

2. This paper validate the phenomenon of the Detection-Generalization Paradox from the perspectives of landscape and sharpness.

3. Experimental results demonstrate that DR-SAM simultaneously enhances the performances of OOD-D and OOD-G ability.

### Weaknesses
1. The proposed method DR-SAM lacks innovation. It appears to combine OE and SAM as optimization objectives, with an additional data augmentation to calculate perturbation factor $\epsilon$.

2. The analysis of the method is not detailed enough. In Algorithm 1, should $f_{\theta+\epsilon}$ in lines 3 be $f_{\theta}$?

3. In Algorithm 1, does using data augmentation to calculate the perturbation factor $\epsilon$ in line 4 affect the model's performance on $D_{ID}^{test}$ compared to vanilla SAM?

4. Is the capability for OOD-G derived from data augmentation or SAM? The authors should include relevant ablation experiments to clarify this.

5. Data augmentation seems to be the most significant innovation in DR-SAM, and the authors should include experiments to demonstrate the impact of having or not having data augmentation.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper provides research on one of the most important topic in machine learning, which is dealing with out of distribution data. Specifically, the paper present a detection-generalization paradox that exists in current machine learning systems. The authors analyze this paradox by
providing in-depth analysis of the models trained under various paradigms, focusing on representation, logits, and loss across
different data shifts. The authors propose a new idea for breaking this paradox and support their findings with extensive experiments.

### Strengths
The paper delves into important aspect of the non-trivial problem in existing machine learning models. One of the most important strength of this paper is the manuscript is structured in a very proper way. The introduction section is very clear, the motivation is also clear and it is very clear what the authors are trying to do. The way in which the authors conducted the in-depth analysis of the behavior of models in the representation, logits, and loss space to show the actual detection-generalization paradox is worthy of admiration. The paper also stands out well in terms of contribution, where they have presented a new methodology "Distribution Robust Sharpness Aware Minimization" which is fairly intuitive and proving effective in maintaining the detection-generalization balance in the classification systems. The authors have provided fairly good amount of literature review and conducted extensive experiments on the available benchmark datasets, and also compared with the existing references in the field. Considering the reproducibility, the authors have provided full algorithm, and released the source codes as well.

### Weaknesses
There are some weaknesses associated with the paper. The paper has severe typos, and a thorough proof-read is required. For instance, covariate is written as covariant in many places. The provided source code is very hard to reproduce as it does not have a readme file, and to replicate the exact experiment is difficult. There are irrelevant and lot of details in the appendices of the related works section, which is not necessary at all. The experiments and results are promising, but it could have been done better by comparing with OOD-G methods too because there is a lack of proof indicating DR-SAM can beat existing OOD-G methods. The results are majorly focused on semantic shifts based methods only.

### Questions
Some questions to the authors are:

1. In line 082, Analysis on logit space: For better OOD_D method enlarges the gap of prediction confidence between D_ID and D_CS. Is this a typo? Shouldn't it be D_ID and D_SS instead of D_ID and D_CS?

2. Fig. 2 is not clear. Atleast not very explaining. Why the FPR is in the range of -ve and why the OOD-G accuracy of DR-SAM around 1.7? A delta term is used for both FPR and ACC. What is this delta? Is it the difference? It needs to be clarified both in the caption and the actual. It is difficult for a normal reader to apprehend whats going in this figure.

3. In Fig. 5 the sharpness value is larger and in 6 and 7 the sharpness value is smaller. Is this the preferred characteristics of the curves for DR_SAM? Shouldn't the sharpness value in the Fig.5d remain almost steady across the value of rho? Because this characteristic contradicts with the statement made in the line 255-256.

4. Why is the ID and OOD accuracy of DR-SAM less than that of vanilla SAM? As per the result, the gain can only be seen in the AUROC which is the metric for detecting semantic shifts. What about for the covariate shift part? Shouldn't the OOD accuracy be at least on par or better than the reference and vanilla SAM as per the claim of breaking the detection-generalization paradox? Please clarify.

5. Regarding the experimental results, why the results are not compared with recent approaches that has been studied for both detection and generalization? Also, why the comparison has not been made for the Imagenet-200 benchmarks in terms of OOD-G methods in Table 3?

### Soundness
3

### Presentation
4

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
The paper focuses on the relationship between two widely studied problems, i.e., OOD generalization and OOD detection. The authors conducted an empirical study and found that these two tasks conflicted with many previous OOD detection methods. To address this issue, a novel optimization framework named DR-SAM is proposed to balance OOD generalization and detection performance. The proposed method obtains the optimal model parameters by pursuing not only a clear decision boundary between clean ID data and semantic OOD data but also simulated covariant-shifted data and semantic OOD data. And thus better overall performance can be expected. Experiments on commonly used benchmarks can support the proposed method.

### Strengths
## Strength

- Interesting topic. The investigated problem is realistic, practical, and important. Combining these two tasks is necessary and critical.
- Clear writing and good organization. The logic of the most part in this paper is smooth which makes it easy to follow. I enjoy the clear writing.

### Weaknesses
## Weakness

Major concerns:

- Vague contributions. The authors claim that the main contribution of this paper is to identify the detection-generalization paradox. However, as far as I could tell, the trade-off/conflict relationship has been pointed out by several previous works [1,2,3]. Thus such a claim should be either toned down or a clear explanation about the difference from previous work should be provided. The authors need to clarify how their identified paradox differs from the existing understanding of the trade-off between OOD detection and generalization. Specifically, the prior works have already shown that methods improving OOD detection often come at the cost of in-distribution performance, and vice-versa. The authors need to articulate what specific aspect of this relationship their work is revealing that has not been previously discussed.
- Unclear motivation. In lines 266-269, the authors claim that the ideal model should yield low sharpness on both ID and covariate-shifted data. They claim that this cannot be adopted OOD-G method. The logic here is hard for me to follow. Why solely using OOD-G method can not ensure low sharpness for ID and covariate-shifted data? I guess this is a typo. Is the covariate-shifted data here should be replaced with semantic-shifted data? The authors need to provide a more detailed explanation of why existing OOD generalization methods cannot achieve low sharpness on both in-distribution and covariate-shifted data. The current explanation is unclear and needs to be supported by a more rigorous argument. It is not immediately obvious why methods like SAM or Mixup, which are designed to improve generalization, would inherently fail to minimize sharpness on covariate-shifted data.
- Lock of essential comparison. Although the experiments in Section 5 encompass a few representative works in OOD detection and generalization, some of the most related works are missed. Several recent methods also jointly consider OOD detection and generalization [1,3,4]. Thus, the comparison in this current version is biased and incomplete. Besides, I also feel that some SOTA OOD detection methods are also missed. For example, POEM [5], NPOS[6], and NTOM[7]. As far as I can tell, POEM substantially surpasses OE, MCD, and MixOE in terms of OOD detection on CIFAR benchmarks. SCONE, WOODS, and DUL which jointly pursue OOD detection and generalization can achieve much better overall performance compared to the baselines in Table 1 2 and 3. The reviewer suggests comparing the proposed method with these methods. The experimental section lacks a comprehensive comparison with state-of-the-art methods that jointly consider OOD detection and generalization. The absence of comparisons with methods like POEM, SCONE, and WOODS makes it difficult to assess the true novelty and effectiveness of the proposed approach. The authors should include these comparisons to provide a more complete picture of the method's performance.
- Experimental settings. The authors claim that they deploy brightness as data augmentation (Appendix C). I have concerns about whether using brightness augmentation during training can result in information leakage from the test covariate-shifted distribution. Since all the other corruptions in CIFAR10/100-C or ImageNet-C may also alter the brightness of images. As far as I could tell, in standard OOD generalization settings, the test-time covariate-shifted distribution should be kept unknown during training. Besides, the authors seem to tune the augmentation and make such a choice as they said in lines 466-468. Thus, the dependence on manually selected augmentation is a notable limitation that makes the OOD generalization problem more like domain adaption or even a trivial problem. The use of brightness augmentation during training raises concerns about potential information leakage from the test covariate-shifted distribution. The authors need to justify why this specific augmentation was chosen and how it avoids making the OOD generalization problem more like domain adaptation. The dependence on manually selected augmentation is a significant limitation that needs to be addressed.

Minor concerns:

- Similar to other training-required OOD detection methods, the proposed method also needs to access semantic-shifted data during training. This limitation widely exists in many previous OOD detection methods, but still worth noting here.

- In Figure 3(d), why there is no blue area (ID data) in the figure?
- I am unsure whether the formulation of OOD generalization in Eq. 3 is correct.  $D_{CS}$ is mentioned by the text above Eq.3. However, there is no such notation in the following equation. The formulation should be revised carefully and a proper citation should be provided here.
- The authors post a visualization of the loss landscape in Figure 10. However, such a visualization contains limited information. The reviewer suggests comparing with SAM, OE, and the original ERM.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
1
