# On the Performance Analysis of Momentum Method: A Frequency Domain Perspective

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Momentum-based optimizers are widely adopted for training neural networks. However, the optimal selection of momentum coefficients remains elusive. This uncertainty impedes a clear understanding of the role of momentum in stochastic gradient methods. 
In this paper, we present a frequency domain analysis framework that interprets the momentum method as a time-variant filter for gradients, where adjustments to momentum coefficients modify the filter characteristics. 
Our experiments support this perspective and provide a deeper understanding of the mechanism involved. Moreover, our analysis reveals the following significant findings: high-frequency gradient components are undesired in the late stages of training; preserving the original gradient in the early stages, and gradually amplifying low-frequency gradient components during training both enhance generalization performance. 
Based on these insights, we propose Frequency Stochastic Gradient Descent with Momentum (FSGDM), a heuristic optimizer that dynamically adjusts the momentum filtering characteristic with an empirically effective dynamic magnitude response. Experimental results demonstrate the superiority of FSGDM over conventional momentum optimizers.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a signal processing framework for the analysis of momentum in stochastic gradient descent (SGD). Specifically, the authors consider two variants of momentum SGD: coupled (where the previous and the current step proportions add up to one) and decoupled (where the current step has the weight of one, and the previous step can have the momentum term tweaked independently). Furthermore, the authors use the signal processing viewpoint to gain insight on how the momentum coefficients should evolve over the course of neural network training. Finally, based on the insights regarding the training behavior under various momentum settings, the authors propose a new frequency-based variant of momentum SGD, and show on a wide variety of problems that the proposed variant outperforms the conventional momentum SGD (both coupled and decoupled).

### Strengths
**Originality:** The paper brings the signal processing perspective to the understanding of SGD, which is invaluable. Seeing that a lot of the progress in ML is purely empirical, the systematic and thorough approach the paper takes is both refreshing and useful. Viewing momentum term contributions as corresponding to low/high-pass filters opens the door to apply various insights from signal processing directly to neural network training. Thinking of momentum as attenuating and amplifying various gradient frequencies also provides a useful intuition, and maps well to existing state-of-the-art optimizers such as Adam.

**Observations:** The authors note that decoupled rather than coupled approach to momentum is more beneficial. Further, the authors observe the following set-up as beneficial to generalization performance: retaining the original gradient early in training; focusing on high-frequency gradients early in training, and suppressing them closer to the end of training; amplifying low-frequency gradients at the end of training. Perhaps the insights gained can lead to further studies into generalization behavior of neural networks.

**Quality and Clarity:** The paper is very well-written, with only a few minor typos. The methodology is clear. A lot of the results are pushed into appendices, which indicates that the authors have done an excessive amount of work towards the paper. I feel bad that such extensive experimentation is becoming a de facto standard for top-tier conferences. Nevertheless, there is evidence that the authors went above and beyond the expectation.

**Significance:** The paper asks fundamental questions, and provides useful answers to these questions. It offers a significant new perspective that can aid the design of new, more efficient optimizers.

### Weaknesses
An important work on how momentum works was published in 2017 in the Distill web-based journal: https://distill.pub/2017/momentum/
I believe that this paper needs to feature in the related literature. Also, in case the authors are not aware of it, I believe they will enjoy reading it!

As mentioned above, the experiments conducted are truly comprehensive and span a wide range of problems and architectures. However, what is missing from the experiments is the presence of the (arguably) state of the art approach to NN training, i.e., the Adam optimizer. For the reinforcement learning experiments, the authors explicitly state that they have replaced Adam with their method as well as coupled and decoupled versions of momentum SGD. However, based on the insights, it seems that Adam succeeds by doing exactly what the paper prescribes as necessary: amplify low-frequency gradients while attenuating high-frequency gradients. A discussion of Adam in the context of the proposed paradigm, even on a superficial level, would benefit the discussion, in my opinion.

A few mistakes that I picked up need to be fixed:
* Page 2, line 95: SGD-base -> SGD-based
* Page 6, line 321: “test results of orthodox momentum…” - do you mean unorthodox?
* Page 7, line 351: “A Large” - “large” should not be capitalized

Legend on the figures is in a very small font, which makes it rather hard to read.

Tables 1 and 2 refer to various "Experiments" (1, 2, 3, and 4). While I realize that the experiments are defined in the main body of the text, I think the tables can be made more easily interpretable on their own by rather using a descriptive name (high-pass VS low-pass gain, etc.) per row.

### Questions
A few mistakes that I picked up need to be fixed:
* Page 2, line 95: SGD-base -> SGD-based
* Page 6, line 321: “test results of orthodox momentum…” - do you mean unorthodox?
* Page 7, line 351: “A Large” - “large” should not be capitalized

Legend on the figures is in a very small font, which makes it rather hard to read.

Tables 1 and 2 refer to various "Experiments" (1, 2, 3, and 4). While I realize that the experiments are defined in the main body of the text, I think the tables can be made more easily interpretable on their own by rather using a descriptive name (high-pass VS low-pass gain, etc.) per row.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper introduces a frequency-domain analysis framework for understanding momentum-based optimizers, viewing them as time-variant filters that adaptively shape gradient characteristics through momentum coefficients. Based on these insights, the authors propose FSGDM, a novel optimizer that dynamically adjusts momentum to enhance generalization, outperforming conventional momentum-based methods in experiments.

### Strengths
1. The paper is clear and straightforward, making it easy to follow. The core idea is both simple and effective, showcasing an elegant solution that achieves strong results without unnecessary complexity.

### Weaknesses
1. In traditional signal processing, many derivations provided in the paper are well-established and widely recognized. 
2. Quantitative comparisons within this field remain relatively limited, often lacking comprehensive metrics or benchmarks to evaluate performance across different methods.

### Questions
Why the Z-transform is employed in the learning settings, while many other transforms can also be deployed?

### Soundness
3

### Presentation
2

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
The paper explores the momentum-based optimization methods commonly used in training neural networks through a frequency domain perspective. It shows a new interpretation of momentum as a time-variant gradient filter, where the value of momentum coefficients determines the filtering of different frequency components of gradients. The analysis shows that high-frequency gradient components decrease performance in the later training stages, while preserving original gradients in the early stages and amplifying low-frequency components gradually improves generalization.

Building on these insights, the paper introduces Frequency Stochastic Gradient Descent with Momentum (FSGDM), a heuristic optimizer that adjusts the momentum coefficients dynamically to enhance training performance. Experimental results on image classification and NLP tasks demonstrate that FSGDM outperforms conventional momentum-based optimizers.

### Strengths
Originality:
* The paper explores the impact of momentum on gradient frequency domain. This work is very original and has not been well explored before. The exploration shows that the momentum update is usually a low pass filter which gets more and more narrower low pass filter in the later part of the training.

Quality:
* The derivations based on signal processing principles, particularly the application of Z-transforms, provide a good theoretical foundation. The analysis effectively distinguishes between conventional momentum methods (like Standard-SGDM and EMA-SGDM), clarifying their distinct impacts on gradient components from frequency domain perspective.
* The experiments are comprehensive and well-designed, covering image classification and language translation. The results consistently show that FSGDM outperforms traditional momentum optimizers in both accuracy and convergence speed, demonstrating the practical relevance of the proposed method.

Clarity:
*  The paper follows a clear structure, beginning with the theoretical formulation of the problem, progressing to the design of the FSGDM optimizer, and concluding with comprehensive experimental results.
* The use of visuals, such as plots of frequency response and performance comparisons, enhances understanding. The inclusion of tables summarizing performance across different tasks is also helpful for comparing results at a glance.


Significance:
* By integrating frequency domain insights into momentum adjustment, this work not only advances the understanding of optimization mechanisms but also opens the door for further research.
* The empirical results demonstrate that FSGDM consistently achieves better performance than standard momentum-based optimizers, indicating that the proposed method can be a strong alternative across different neural network task

### Weaknesses
Significance:
* While the Frequency perspective of momentum based weight updates is very impressive, the proposed FSGDM (Frequency Stochastic Gradient Descent with Momentum) does not appear to be very significant because of the following 2 reasons
  1. Setting schedules for momentum coefficient and learning rates during training is a very common practice in NN training. In the proposed FSGDM method we still need to set bunch of hyperparameters like scaling factor c, momentum coefficient v. Therefore FSGDM is not very different from the tradition momentum method in terms of hyperparameter tuning.
  2. The optimal value of scaling factor c and momentum coefficient v is determined for different datasets and network architectures (as shown in fig 4) and is used for the results shown in the experiment section. While some standard coefficients are used for standard SGDM and EMA SGDM. This shows that the results might be slightly biased.
* The frequency domain analysis in this paper remains somewhat limited in its applicability to broader optimization contexts. The framework primarily addresses momentum-based methods in the context of SGD-like algorithms, but it does not extend to other popular optimization strategies like Adam or RMSprop, which also incorporate adaptive mechanisms and momentum-like components. Therefore I suggest extending the frequency domain analysis for other popular optimization methods like Adam and RMSprop would make this paper much more significant.

### Questions
Suggestions:
* It’s unclear how robust the optimizer is to hyperparameter tuning across different datasets and tasks. Without this information, practitioners might face challenges in adopting FSGDM in real-world applications. Therefore I suggest to include a dedicated analysis or appendix section detailing the sensitivity of FSGDM’s performance to variations in these hyperparameters. It would be useful to identify hyperparameter settings that generalize well across tasks, if any.

Questions:
* Since Adam and RMSprop uses both gradient and curvature of the error surface
  ** how might the frequency domain analysis framework be extended for Adam or RMSprop?
  ** What challenges do you anticipate in applying this framework to those methods?
  ** Do you believe similar insights about gradient frequency components would apply, or would different principles emerge?

### Soundness
3

### Presentation
3

### Contribution
3
