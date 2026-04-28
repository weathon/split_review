# Adaptive Continual Learning: Rapid Adaptation and Knowledge Refinement

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5

## Abstract
Continual learning (CL) is an emerging research area aiming to emulate human learning throughout a lifetime. Most existing CL approaches primarily focus on mitigating catastrophic forgetting, a phenomenon where performance on old tasks declines while learning new ones. However, human learning involves not only retaining knowledge but also quickly recognizing the current environment, recalling related knowledge, and refining it for improved performance. In this work, we introduce a new problem setting, Adaptive CL, which captures these aspects in an online, possibly recurring task environment without explicit task boundaries or identities. We propose the LEARN algorithm to efficiently explore, recall, and refine knowledge in such environments. We provide theoretical guarantees from two perspectives: online prediction with tight regret bounds and asymptotic consistency of knowledge. Additionally, we present a scalable implementation that requires only first-order gradients for training deep learning models. Our experiments demonstrate that the LEARN algorithm is highly effective in exploring, recalling, and refining knowledge in adaptive CL environments, resulting in superior performance compared to competing methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies an interesting topic, continual learning, which aims to learn a sequence of tasks without forgetting. The existing continual learning models are usually only considered to relieve forgetting in general continual learning. In contrast, this paper considers a new learning environment with possibly recurring tasks. This paper addresses this challenging setting by developing a new approach, achieving good results.

### Strengths
1. This paper is well-written.
2. The research topic in this paper is very interesting.

### Weaknesses
 1. Some notations should be bold, such as x and y.
2. The actual network of the proposed model is not clear. 
3. Why use the Regret Bound to explain the proposed approach instead of other theories?
4. The proposed approach requires three steps in each time, which leads to huge computational costs.

### Questions
Please see the weakness section.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel problem setting, Adaptive CL, inspired by human learning. It presents the LEARN algorithm, comprising three components: Exploration, Recall, and Refinement. The authors offer theoretical and experimental analysis to validate the effectiveness of the LEARN algorithm.

### Strengths
- The authors have developed a setting that more accurately mirrors human cognition and have provided a theoretical analysis to enhance understanding.

### Weaknesses
 - The novelty of the constructed Adaptive CL setting is limited, since there are already some papers proposed similar periodic/recurring CL tasks [1,2].
- Some parts of the paper are hard to understand.
>  In Figure 1, the meaning of the y-axis and the star symbol is unclear or this figure is just an illustration figure? It's also confusing why the third Refinement (blue lines) occurs before the second Recall (green arrows).
> In Section 3.3, it’s unclear what the `scalability challenges' refer to. In Algorithm 2, the notation $\beta_{t-1,i}$ is also not explained.
> At the time (t+1), it's not clear why the slow learners have the correct $m_t$ models, especially considering that Section 1.1 asserts that the method doesn't require knowledge of the task count. Is $m_t$ also indicative of the number of components in the GMM model? The paper needs to provide a more detailed explanation of how the GMM model is updated and how the relevant slow learner is selected in Figure 3.
- In the experimental section, the methods chosen for comparison are outdated. Considering that the proposed method incorporates the concept of the complementary system and emphasizes task-free CL, it should at least be compared with closely related methods such as Cls-ER[3] and recent task-free methods like [4]. Additionally, the paper should address the storage cost, as the method requires storing multiple slow learners.

### Questions
See the three points in the Weaknesses.  As I still have questions regarding the experiments and found the paper difficult to understand, with some parts remaining unclear even after multiple readings, I recommend rejecting the paper in its current form.

### Soundness
2 fair

### Presentation
2 fair

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
In this paper, the authors introduce a new problem setting, Adaptive CL, considering recurring task environment without explicit task boundaries or identities. The authors then propose a LEARN algorithm including exploration, recall and refine process. Theoretical guarantees on online prediction with tight regret bounds and asymptotic consistency of knowledge are presented. Empirical evaluations are also done to show the effectiveness of the proposed LEARN algorithm.

### Strengths
Strength:

1.	A challenging new problem setting considering recurring task environment without explicit task boundaries or identities is presented.

2.	A LEARN algorithm for the Adaptive CL is proposed, and a scalable instantiation based on GMM is developed.

3.	Both theoretical and empirical analyses on LEARN are given.

### Weaknesses
Weakness:

Overall, the paper is well written, and the proposed new adaptive CL setting is practical and challenging. The proposed LEARN is technically sound and has been empirically verified to be effective in such a setting. Significant improvements over existing baselines are observed. The reviewer only has the following minor concerns.

1.	The method is verified on the classification task, as the problem setting is basically constructed according to label. The reviewer is wondering whether it is also applicable for regression problem. A related question is how to formulate the problem setting for regression task?

2.	The ablation studies can be further improved by considering each process only. From the current results, exploration plays the major role in achieving good results, and thus it is necessary to include exploration only results.

3.	For hyper-parameters Q and \alpha, why the current value range is selected? The appendix gives partial results on several combination of these two hyper-parameters, and it can be observed that the performance indeed varies with different settings. It is necessary to include a constructive guideline to set the two hyper-parameters, especially when facing new task or datasets.

### Questions
Please refer to the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new online continual learning setting in which there exists potential recurrence of tasks. It proposes an algorithm for this new settings called LEARN by exploiting the recurrence. It provides theoretical guarantees for the algorithm and offers a scalable implementation that leads to competitive empirical performance.

### Strengths
1. This paper introduces a new online continual learning setting where there is potential recurrence of tasks, and proposes a new algorithm for this new setting, which exploits the recurrence to improve the performance.
2. Theoretical guarantees are provided for the algorithm.

### Weaknesses
1. The paper is difficult to understand: it is not well organized and leaves out many details.

a) Figure 1 is too abstract and symbolic to be understood.

b) The authors refer to Figure 2 to illustrate the need for recall without further explanation.

c）Tempered Bayesian updates is a key component of the fast learner, but is not introduced. 

d) There are some details missing from the proof. For example, the proof of Lemma A.2. applies Hoeffding's lemma directly, but the derivation is not straightforward, making it difficult to verify the correctness of the theory.

e) Important details, such as the derivation of Algorithm 2 and the definition of Adaptiveness are provided in Appendix, making it difficult to understand when reading the main text.


2. The discrepancy between the motivation and the algorithm.
As mentioned, "The primary goal is to activate the relevant slow learner for improved performance on seen tasks, and to utilize the fast learner for identifying and quickly learning new tasks."

However, there is no new task identification in the proposed algorithms. There is also no identification of relevant slow learners in Algorithm 1.
In Algorithm 1, the recall and refinement do not seem to leverage the knowledge of the recurrence of tasks. They are both updated by simply combining $\tilde{f}$ and $g$ with predefined ratios.

3. This paper does not discuss and compare the methods proposed for the very related setting where data of previous tasks/classes may appear again in CL, such as blurry task setting like "Koh et al. Online continual learning on class incremental blurry task configuration with anytime inference. In ICLR 2022", or the methods using fast and slow learner "Pham et al. DualNet: Continual Learning, Fast and Slow. In NeurIPS 2021"

4. Inappropriate choice of baselines in the experiments.
In Adaptive CL setting, there are no explicit task boundaries or identities. However, most baselines are not task-free methods. They are proposed under the assumption that there is an explicit task boundary, so they may not naturally work well in this setting. On the other hand, in Table 2, the only task-free baseline performs much better than the proposed method. The proposed method should be compared with more task-free baselines.

5. The randomness introduced by the random shuffling of 200 segments can have a significant impact on experimental performance.

### Questions
1. What are the definitions of Average Accuracy and Knowledge Accuracy? Can you provide their definition similar to the one of adaptiveness in Appendix D.4? In addition, why do the methods perform very differently in terms of knowledge accuracy and average accuracy?

2. Algorithm 2 needs to maintain 1+$m_{t-1}$ models. Why does it have almost the same number of trainable parameters as the other methods?

3. We do not know the number of distributions. Therefore we don't know $m_{t-1}$. How is $m_{t-1}$ obtained in Algorithm 2? 

4. In the experiment, how many slower learners are there at the end of training?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
