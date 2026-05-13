# Non-uniform Noise Injection For Enhancing DNN Adversarial Robustness And Efficiency

- Decision: Reject
- Scores: 3, 3, 6, 3

## Abstract
Deep Neural Networks (DNNs) have revolutionized a wide range of industries, from healthcare and finance to automotive, by offering unparalleled capabilities in data analysis and decision-making. Despite their transforming impact, DNNs face two critical challenges: the vulnerability to adversarial attacks and the increasing computational costs associated with more complex and larger models. In this paper, we introduce an effective method designed to simultaneously enhance adversarial robustness and execution efficiency. Unlike prior studies that enhance robustness via uniformly injecting noise, we introduce a non-uniform noise injection algorithm, strategically applied at each DNN layer to disrupt adversarial perturbations introduced in attacks. By employing approximation techniques, our approach identifies and safeguards essential neurons while strategically introducing noise into non-essential neurons. Our experimental results demonstrate that our method successfully enhances both robustness and efficiency across diverse attack scenarios, model architectures, and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work suggests that only a subset of neurons is critical in representation learning and proposes a selection method to categorize neurons into essential neurons and non-essential neurons. Subsequently, the authors apply non-uniform noise injection to these two types of neurons in order to improve adversarial robustness and maintain clean accuracy.

### Strengths
1. The hypothesis that only a subset of neurons are critical in representation learning, and the rest can tolerate noise perturbations without affecting performance, is interesting.  
2. Propose a method for distinguishing between essential neurons and non-essential neurons.  
3. Propose a non-uniform noise injection method tailored for essential neurons and non-essential neurons.

### Weaknesses
1. Limited novelty: The proposed method is a marginal improvement on existing methods.
2. Over-claimed contribution: In the experiments, the proposed method still leads to a decrease in clean accuracy, rather than truly "retaining clean accuracy" as claimed.
3. Robustness evaluation is inaccurate: It is suggested that the authors employ the experimental setup for the standard adversarial training [1] and use AutoAttack [2] for assessing the model's robustness. Compare the effectiveness of the proposed method on the model's best robustness and last robustness.

### Questions
If the proposed method can substantially achieve higher robustness compared to standard adversarial training, I will increase my score.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a novel method that inject non-uniform noise to non-essential neurons so that the adversarial robustness of the network is enhanced while the clean accuracy is not harmed.

### Strengths
The work deals with a significant and inspiring topic: enhancing adversarial robustness and efficiency simultaneously.

### Weaknesses
 - I find the paper a little hard to follow. Specifically, I cannot determine what “irregular 50%” and “structured/unstructured” mean in the paper’s context. It is very likely because I don’t have sufficient background knowledge and I would appreciate it if the authors could refer me to 2-3 most related (and preferably recent) papers that can help me gain the basics. But for now, I tend to believe the authors fail to make the paper easy to follow.
    
- AutoAttack is not included in threat models, which I believe is necessary to show the adversarial robustness of a new method.
    
- The performance boost of the proposed method seems to be limited. In Table 3, clean accuracies decreased by a noticeable margin with limited improvement in robustness accuracies. So, it is hard to say that a better accuracy-robustness trade-off is achieved. Also, more baseline AT methods (e.g. TRADES) would be helpful to show the method’s effectiveness.
    
- As it is claimed that the proposed method enhances adversarial robustness and execution efficiency simultaneously, it is important to show directly how much the efficiency is improved directly (e.g., throughput) compared to the baselines.

### Questions
Can you intuitively explain why “a neuron is regarded as essential if its approximation from $\widetilde{z}$ is larger than the predefined threshold”?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the use of a non-uniform noise injection method to improve adversarial robustness and efficiency. The proposed method first trains a linear layer-wise approximation of the layer's output and uses the approximation to determine which neurons are essential and which are not. A binary mask is used to replace the outputs of non-essential neurons with their approximations. The paper later proves that this process is unlikely to decrease clean accuracy. The improvements in adversarial robustness and computational efficiency are also discussed. The experiments further validate these claims.

### Strengths
1. The paper is well-organized and easy to understand.
2. The proposed method that uses non-uniform noise injection is novel and produces promising results.
3. The discussion provides theoretical support for the validity of the proposed methods.

### Weaknesses
1. The threshold and the proportion of non-essential neurons should also be reported. It is also helpful to provide the distribution of the difference between $z$ and $\tilde{z}$, and study the relationship between accuracies and the choice of threshold. Specifically, the paper mentions using a top-k selection process to identify non-essential neurons, but it lacks details on how 'k' is chosen and the range of values explored. Furthermore, the impact of different 'k' values on the final performance, both in terms of clean accuracy and adversarial robustness, is not discussed. The distribution of the difference between $z$ and $\tilde{z}$ is crucial for understanding the magnitude of the approximation error and its potential impact on the model's behavior. Without this, it's difficult to assess the validity of the approximation. It would be beneficial to see a plot of this distribution and how it changes with different thresholds.

2. The theorem does not seem to directly link to the results. Based on the theorem, the clean accuracy can be higher than that without the noise injection, and it does not explain the consistent minor drop in clean accuracy. The theorem's implication that clean accuracy could improve is not reflected in the empirical results, where a consistent, albeit minor, decrease is observed. This discrepancy needs to be addressed. The theoretical analysis should provide a more precise explanation of why the observed clean accuracy consistently drops, even if slightly. It should also discuss the conditions under which the theorem's prediction of potential accuracy increase might hold, and why those conditions are not met in the experiments.

### Questions
1. The learning of $\tilde{W}$ and $\tilde{b}$ minimizes the MSE. Is it possible that the optimal learned solution is $W=\tilde{W}P$ and $b=\tilde{b}$? 
2. Are there any specific reasons that $\epsilon=4/255$ in Table 1 while $\epsilon=8/255$ in Table 3?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a novel method to address the challenges of adversarial attacks and computational costs in Deep Neural Networks (DNNs). Unlike previous studies that uniformly inject noise for robustness, this method strategically applies non-uniform noise at each DNN layer to disrupt adversarial attacks while preserving essential neurons. Experimental results show that this approach effectively enhances both robustness and efficiency in various attack scenarios, model architectures, and datasets.

### Strengths
The method of finding core and non-core neurons while simultaneously using those values to introduce noise is a good approach, in my opinion.

### Weaknesses
 * It is stated that "A neuron is regarded as essential if its approximation from ˜z is larger than the predefined threshold." However, I am unsure why this makes it an important neuron. ˜z is used to reduce the value error through the MSE of z, meaning that the larger the z value, the more it will affect the size of ˜z. Therefore, an explanation is needed on why neurons with larger ˜z values are considered important. The experiment tested both top-K injection and N:M injection methods, but there was no experiment that simply added noise values to a random N% of neurons. Therefore, there is a lack of validity in claiming that this method is effective.

* During the experimental process, in the experiment where noise was added to non-core neurons, I think there needs to be a control group that adds different noise to those neurons as a comparison to the approximated values used for detection. It is necessary to verify whether the method of injecting this noise actually contributes to performance improvement or simply enhances computational efficiency.

* Too much limited and insufficient experiments: There are no state-of-the-art attack such AutoAttack [1] and no state-of-the-art defense baselines such as AWP [2], SCORE [3], and ADML [4]. In addition, based on ADML, not only CNN structure and Transformer structures should be needed to validate.

### Questions
Refer to Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
