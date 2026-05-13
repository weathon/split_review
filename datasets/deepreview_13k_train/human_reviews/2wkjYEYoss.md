# Gamma: Toward Generic Image Assessment with Mixture of Assessment Experts

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Image assessment aims to evaluate the quality and aesthetics of images and has been applied across various scenarios, such as natural and AIGC scenes. Existing methods mostly address these sub-tasks or scenes individually. While some works attempt to develop unified image assessment models, they have struggled to achieve satisfactory performance or cover a broad spectrum of assessment scenarios. In this paper, we present \textbf{Gamma}, a \textbf{G}eneric im\textbf{A}ge assess\textbf{M}ent model using \textbf{M}ixture of \textbf{A}ssessment Experts, which can effectively assess images from diverse scenes through mixed-dataset training. Achieving unified training in image assessment presents significant challenges due to annotation biases across different datasets. To address this issue, we first propose a Mixture of Assessment Experts (MoAE) module, which employs shared and adaptive experts to dynamically learn common and specific knowledge for different datasets, respectively. In addition, we introduce a Scene-based Differential Prompt (SDP) strategy, which uses scene-specific prompts to provide prior knowledge and guidance during the learning process, further boosting adaptation for various scenes. Our Gamma model is trained and evaluated on 12 datasets spanning 6 image assessment scenarios. Extensive experiments show that our unified Gamma outperforms other state-of-the-art mixed-training methods by significant margins while covering more scenes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This submission propose a generic image assessment model using mixture of assessment experts, named Gamma. To deal with the problem of applying the image assessment model across various scenarios, Gamma proposes two techniques: 1) proposing a Mixture of Assessment Experts (MoAE) module, which employs shared and adaptive experts to dynamically learn common and specific knowledge for different datasets; 2) introducing a Scene-based Differential Prompt (SDP) strategy, which uses scene-specific prompts to provide prior knowledge and guidance during the learning process. Although the experiments shows the better performance of the proposed method, there are still some concerns for its acceptance.

### Strengths
The experiments show the better performance of the proposed method

### Weaknesses
1) The relationship between the adaptive experts and the scene-based differential prompt is unclear. The adaptive experts is also a type of prompt engineering to capture the specific knowledge of the datasets, which is much similar to the scene-based prompt with scene-specific priors. Much analysis on their inner mechanism is suggested to be added.
2) Furthermore, rather than the statistical results on the datasets, I would like to see the analysis and experiment results to prove that the adaptive experts indeed capture the specific knowledge of different datasets and how the specific knowledge is reflected in the adaptive experts.
3) Ablation studies include experiments on the number of experts. What is the relationship between their number with the number of the datasets? As shown in Table 2, there are five datasets used for ablation, but three experts get the best performance. Could you help to analyze how the three experts capture the knowledge of the five datasets?

### Questions
Please refer to the above comments

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This manuscript introduces a mixture of assessment experts and scene-based prompts to achieve high-performing, unified image quality and aesthetics assessment across diverse datasets and scenarios.

### Strengths
1. The idea of using MoAE to overcome the dataset distribution gap is reasonable. 
2. The performance is better than baselines (but may be unfair, see Weaknesses).
3. The paper is presented clearly and easy to follow.

### Weaknesses
1. **The comparison with baseline methods is unfair**. Table 1 contains some blanks for baseline methods like UNIQUE and LIQE, which raises concerns about the experimental setup. I have carefully checked the results of UNIQUE and LIQE and ensured that these numbers are directly copied from previous papers. The training datasets of UNIQUE and LIQE differ from this manuscript, which is unfair.
2. **The generalization experiments are not enough**. Though this manuscript mentions that 12 datasets are involved, most of them are used in training. Only two of them are used to evaluate the generalization ability. More results from cross-dataset experiments are needed. For example, for the seven datasets in Table 1, how about the results of training with three datasets and evaluating with another four datasets?
3. **The manuscript does not compare with an important baseline**, Q-Align, which also proposes a unified framework that can co-train multiple datasets. Moreover, only training on three datasets, Q-Align’s results on some datasets have surpassed this manuscript. 
4. **There is no analysis of efficiency**, though this manuscript claims the proposed method is both effective and efficient.  Please report the comparison of the number of parameters, FLOPs, and training / inference time to support the claim. 
5. **There is no sensitivity analysis of prompts**. This manuscript uses scene-based differential prompts to improve the ability across multiple datasets and scenes. However, it is risky that the model will be highly reliant on such prompts. During testing, if the prompts are changed, the performance may significantly drop. Therefore, a detailed analysis of the sensitivity to prompts should be included.

### Questions
See Weaknesses.

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
This paper proposes a generic image evaluation model, Gamma, based on hybrid evaluation experts, which is trained to efficiently evaluate images from different scenes through mixed data sets. Taking into account annotation bias of different datasets, the authors propose a hybrid evaluation expert module that uses shared and adaptive experts to dynamically learn common and specific knowledge of different datasets respectively. At the same time, a scenario-based differential cue strategy is introduced to enhance the adaptability to various scenarios. They conducted an empirical study on 12 data sets and compared it with the existing models, and the results reached the most advanced level at present.

### Strengths
The author can take into account the annotation bias of different data sets and creatively propose a hybrid evaluation expert module. This paper will help implement a unified evaluation standard on different data sets in the future. This achievement is commendable. Experiments conducted by the authors on multiple datasets effectively demonstrate the universality of their model, and the introduction of the scenario-based differential cue strategy also proves its effectiveness through these experiments.

### Weaknesses
The article itself is to solve the annotation bias of different data sets, but by adding data, there is a suspicion of writing answers for people to change the question. The personalized tendencies among the hired experts are not addressed, and it is difficult to say that the results of the hired experts' data tuning are closer to the real situation than the previous results
At the same time, the author chooses to adjust the model only in the rear module instead of all modules, and says that this method reduces the computing power requirements of the model, which is obvious, but for the reason why this choice is made, does the benefit in terms of reducing the computing power really outweigh the model quality? Is this really worth it? The author doesn't offer a convincing explanation.

### Questions
1. I hope the author can prove that the results after data tuning by the hired experts are closer to the real situation than the previous results.
2. I would like the author to explain the basis on which the model was chosen.
3. I hope that the author can add an experimental result according to the theory of the model in the paper without referring to the data of several hired experts.
4. I'm concerned about how SCENE-BASED DIFFERENTIAL PROMPT is implemented?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a MOE approach for generic IQA approach. The main idea is to adopt a frozen CLIP as a general expert combined with trainable experts for different IQA tasks. The proposed approach demonstrate superiority on different IQA tasks compared with several existing baselines.

### Strengths
+ The motivation to combine multiple experts towards different IQA tasks is reasonable.
+ The paper is easy to follow

### Weaknesses
 - The proposed approach still heavily relies on training data, though the bias can be alleviated by more data, but it may still fail in practical scenarios and training and testing on the data from the same sources cannot validate the generalization ability of the proposed approach, which is the key point that existing IQA approaches cannot overcome.
- The proposed approach lacks interpretation which is still another problem that existing approaches commonly have, i.e., what does each expert actually learn? Though with some reasonable designs, the proposed approach is still a black box.


### Questions
This paper has a reasonable motivation but fail to solve key problems existing in IQA from my opinion. My main concerns are as follows:

1. In Line 079, the author mentions that 'the primary challenge in mixed-dataset training is the mean opinion score (MOS) bias'. However, I do not find a reasonable solution on this challenge. It my understanding is correct, the author just try to adopt different experts and directly train these experts on the labeled data. This does not convince me on solving the bias across different datasets considering that the labels inherently have bias.

2. The proposed approach still heavily relies on training data, though the bias can be alleviated by more data, but it may still fail in practical scenarios. The proposed approach is  trained and tested on the same data sources, i.e., the 12 benchmarks mentioned in the paper. This cannot validate the generalization ability of the proposed approach, which is the key point that existing IQA approaches cannot overcome. The author may consider test on some other sources that have never been used during training for further validation.

3. The proposed approach lacks interpretation which is still another problem that existing approaches commonly have, i.e., what does each expert actually learn? Though with some reasonable designs, the proposed approach is still a black box. The author may consider explaining what each expert learns after training. Moreover, the improvement of 5 experts compared with 3  experts in Table 2 is very marginal and sometimes even worse. This is contradicted with the claim in Line 413. The author should provide more explanation.

4. There should be model complexity verification, including parameters, flops and inference time compared with other baselines.

5. I am a little confused about why a frozen CLIP can be directly adopted as a generic expert w/o finetuning on IQA datasets. Since it is never trained to do so. The author may provide a more detailed motivation on this.

### Soundness
3

### Presentation
3

### Contribution
2
