# The Effectiveness of Random Forgetting for Robust Generalization

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Deep neural networks are susceptible to adversarial attacks, which can compromise their performance and accuracy. Adversarial Training (AT) has emerged as a popular approach for protecting neural networks against such attacks. However, a key challenge of AT is robust overfitting, where the network's robust performance on test data deteriorates with further training, thus hindering generalization. Motivated by the concept of active forgetting in the brain, we introduce a novel learning paradigm called ``Forget to Mitigate Overfitting (FOMO)". FOMO alternates between the forgetting phase, which randomly forgets a subset of weights and regulates the model's information through weight reinitialization, and the relearning phase, which emphasizes learning generalizable features. Our experiments on benchmark datasets and adversarial attacks show that FOMO alleviates robust overfitting by significantly reducing the gap between the best and last robust test accuracy while improving the state-of-the-art robustness. Furthermore, FOMO provides a better trade-off between standard and robust accuracy, outperforming baseline adversarial methods. Finally, our framework is robust to AutoAttacks and increases generalization in many real-world scenarios.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the challenge of robust overfitting in adversarial training of deep neural networks, which affects their generalization performance. The authors propose a new method called "Forget to Mitigate Overfitting (FOMO)," drawing inspiration from the brain's mechanism of active forgetting. FOMO operates by periodically resetting a subset of the network's weights to promote the learning of more generalizable features. The approach suggests a promising direction for enhancing neural network robustness against adversarial attacks by mitigating overfitting through controlled forgetting and relearning. Experimental results show that FOMO is a promising method to improve model robustness.

### Strengths
* The authors conducted comprehensive experiments to demonstrate the effectiveness of FOMO. The proposed method is effective and outperforms the existing method, according to Table 3 and other experimental results.  
* The proposed method is intuitive and easy to implement.

### Weaknesses
 * My main concern is that the proposed method seems to be heuristic and empirical. there is not enough discussion on its intuition or theoretical foundation.
* I don't think the running time and convergence analysis are well-studied in this paper, the authors may need to provide a table showing how many epochs are needed to converge and compare the running time with the existing methods. 
* Minor: Please refrain from only using color to distinguish curves and bars as in Figures 3, 4, 5, and 6, as it is not friendly to readers with color blindness.
* Minor: Missing reference on robust generalization: Zhang, et al. "The limitations of adversarial training and the blind-spot attack." ICLR 2019.

### Questions
Please refer to the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a method, FOMO, to deal with the adversarial overfiting issue. The proposed method alternates between the forgetting phase and the relearning phase.

### Strengths
The paper is in good structure and easy to follow. 

The topic, which is to deal with adversarial overfitting, is interesting.

The method is simple yet effective. 

An ablation study is provided.

### Weaknesses
The description of the method is too intuitive. 

In Table 1, the delta, which measures the adversarial overfitting, never favors the proposed method. This cannot show that the proposed method is good at dealing with adversarial overfitting.

In this paper, the author only shows the result under a combination of white box and black box attacks, i.e., Autoattack. However, this cannot show "the efficacy of FOMO against the black box and white box attacks". Standard Autoattack has 4 adversarial attacks: three white-box attacks and one black-box attack. It is possible that FOMO has a strong resistance against white-box attacks while being vulnerable to the black-box attack.

### Questions
In this paper, the author only shows the result under a combination of white box and black box attacks, i.e., Autoattack. However, this cannot show "the efficacy of FOMO against the black box and white box attacks". Standard Autoattack has 4 adversarial attacks: three white-box attacks and one black-box attack. It is possible that FOMO has a strong resistance against white-box attacks while being vulnerable to the black-box attack.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work aims to address the generalization gap in adversarial training. The authors exploit the random forgetting to adjust the  weights of models. Three datasets and two adversarial attacks are used to evaluate the proposed method. The experimental results show that the method can improve the robust accuracy.

### Strengths
1. This work proposed a new method to solve the generalization gap in adversarial training.  The perspective of random forgetting is interesting.

2. The introduction to the forgetting mechanism in Methodology is clear.

### Weaknesses
1. The description in the caption of Figure 2 is inconsistent with the content of the image. The former states that the consolidation phase is behind the forgetting phase, while the latter expresses that theconsolidation phase is before the forgetting phase. In addition, please present more clearly in the figure what the generalized information is.

2. In Figure 1, FOMO is only compared with standard adversarial training, but not with methods that aim to reduce the generalization gap (such as AWP). This result may not appreciably represent the effectiveness of the proposed method.

3. The authors use two adversaial attacks to evaluate the proposed method, they can consider more adversarial attacks (such as L2-norm CW, DDN) to conduct a more comprehensive evaluation.

4. Figures can be clearer and more aesthetically pleasing.

### Questions
Please see weaknesses.

============After rebuttal============
The authors provide adequate explanations for most of my questions, so I am willing to raise the rating score to 6.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
