# Threaten Spiking Neural Networks through Combining Rate and Temporal Information

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
Spiking Neural Networks (SNNs) have received widespread attention in academic communities due to their superior spatio-temporal processing capabilities and energy-efficient characteristics. With further in-depth application in various fields, the vulnerability of SNNs under adversarial attack has become a focus of concern. 
In this paper, we draw inspiration from two mainstream learning algorithms of SNNs and observe that SNN models reserve both rate and temporal information. To better understand the capabilities of these two types of information, we conduct a quantitative analysis separately for each. In addition, we note that the retention degree of temporal information is related to the parameters and input settings of spiking neurons. Building on these insights, we propose a hybrid adversarial attack based on rate and temporal information (HART), which allows for dynamic adjustment of the rate and temporal attributes. Experimental results demonstrate that compared to previous works, HART attack can achieve significant superiority under different attack scenarios, data types, network architecture, time-steps, and model hyper-parameters. These findings call for further exploration into how both types of information can be effectively utilized to enhance the reliability of SNNs. Code is available at [https://github.com/hzc1208/HART_Attack](https://github.com/hzc1208/HART_Attack).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a hybrid adversarial attack framework, named HART, based on both rate and temporal information. The proposed method offers the flexibility to dynamically adjust the proportion between rate and temporal attributes according to the defined variable known as the retention degree of temporal information. Experiments indicated that HART can significantly improve the attack success rate of SNNs in various attack scenarios.

### Strengths
1.The analytical perspective of this paper is novel. The author starts with the propagation mode between SNN layers and summarizes the two types of information: rate and temporal information. Then they explored how to obtain more precise attack gradients by analyzing the optimal integration methods for both types of information.

2.This paper takes an important initial stride in showcasing the potential of combining rate and temporal information to enhance SNN attacks.

3.The theoretical derivation and mathematical analysis encompassed in this paper are solid.

4. The results of extensive experiments effectively demonstrate that HART exhibits remarkable performance improvements under different hyperparameter configurations when compared to previous SOTA works.

### Weaknesses
1. The authors should provide a more detailed analysis on the specific role of gradient pruning and merging within the proposed framework.

2. The figures and legends of the paper can be further improved.

### Questions
1. In Figure 1, it is unclear why the purple curve appears to be identical to the curve representing case 1.

2.  I kindly request the authors to assess which specific information (rate or temporal) from the SNN was leveraged by several previous attack algorithms, namely CBA, STBP, BPTR, and RGA, in their experimental evaluations. It may shed light on the attack and defense exploration. 

3. In Table 1, the authors juxtapose their rate-based gradient attack method with CBA. Given that CBA also employs rate information for its attack strategy, could the authors elucidate the factors that make the proposed rate gradient method superior?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an adversarial attack method for SNN, which combines both rate and temporal information. Based on detailed analysis and experiments, this work demonstrates the efficiency of the proposed method.

### Strengths
1.	It is interesting to consider both rate and temporal characters in SNN when considering adversarial attack.
2.	Author provide detailed experiment to demonstrate the effectiveness of the proposed framework.

### Weaknesses
1.	The theory is hard to follow, it is better to provide an illustration of how to utilize temporal information during BP (as Fig.1)
2.	Does the pruning has negative effect on the gradient computation? I think it is also interesting to discuss whether the proposed gradient computation can be directly applied to SNN training.
3.	It is better to discuss the complexity of gradient computation in HART. 
4.	Fig.2(c) is hard to understand. In Fig.2(b), it is not clear the meaning of solid arrows.

### Questions
Overall, I think this work provide an interesting attack method, and the experiments are well presented. The theory is not easy to follow, please see my comments for detail.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper analyzes the temporal information in SNNs and establishes its relationship with the membrane decay constant and the number of time-steps. Then the authors propose a novel approach to combine rate and temproal information in SNNs, leveraging it to generate effective gradients for attacking SNNs. The experimental results demonstrate the proposed method achieve the SOTA attack success rate.

### Strengths
1. This paper is well-written.
2. The idea of combining rate and temporal information in SNNs is highly noteworthy. The temporal information in SNNs has not been fully utilized in the current model. 
3. The work is solid. The authors provide a rigorous theoretical analysis of the retention degree of temporal information in SNNs and showcase the influencing factors involved.

### Weaknesses
1. My main concern is about equation 8. I find it hard to derive equation 8 by combining equations 1 and 2. I am wondering about the absence of the threshold in equation 8. The authors should clarify why the threshold is not included in equation 8.
2. The authors primarily focus on demonstrating how the combination of rate temporal information can enhance the attack of SNNs. How about defense? Can the proposed method also be used to improve the robustness of SNNs.

### Questions
Refer to the weaknesses above. 
Please provide a more comprehensive explanation of Figure 2(c).

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents HART, an adversarial attack for SNNs. An analysis of rate and temporal information in SNNs identifies the importance of rate information in SNNs. The proposed attack combines rate and temporal information. The results show better attack success rates than related works on CIFAR-10 and CIFAR-10-DVS datasets.

### Strengths
1. The tackled problem is relevant to the community.

2. The proposed attack is novel.

3. The results outperform related works.

### Weaknesses
Some aspects are not completely clear. Please see the questions below.

### Questions
1. In Table 1, please clarify what results are relative to CBA and what results are relative to the proposed attack.

2. In Section 4.2: “Therefore, we attempt to measure the retention degree of temporal information in SNNs through the following equation.” Please provide more details of the intuitions and design decisions made to develop Eq.12.

3. Please describe the proposed attack through a detailed algorithm that collects all the operations and equations involved. The current description with several equations may be unclear.

4. Section 5 contains the results when varying the parameters of the attack. However, there is very little discussion on the results and reasons why certain values of the parameters achieve higher attack success rates than others. Please discuss it in a more comprehensive manner.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
