# May the Forgetting Be with You: Alternate Replay for Learning with Noisy Labels

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3

## Abstract
Forgetting presents a significant challenge during incremental training, making it particularly demanding for contemporary AI systems to assimilate new knowledge in streaming data environments. To address this issue, most approaches in Continual Learning (CL) rely on the replay of a restricted buffer of past data. However, the presence of noise in real-world scenarios, where human annotation is constrained by time limitations or where data is automatically gathered from the web, frequently renders these strategies vulnerable. In this study, we address the problem of CL under Noisy Labels (CLN) by introducing Alternate Experience Replay (AER), which \textit{takes advantage of forgetting} to maintain a clear distinction between clean, complex, and noisy samples in the memory buffer. The idea is that complex or mislabeled examples, which hardly fit the previously learned data distribution, are most likely to be forgotten. To grasp the benefits of such a separation, we equip AER with Asymmetric Balanced Sampling (ABS): a new sample selection strategy that prioritizes purity on the current task while retaining relevant samples from the past. 
Through extensive computational comparisons, we demonstrate the effectiveness of our approach in terms of both accuracy and purity of the obtained buffer, resulting in a remarkable average gain of $4.71\%$ points in accuracy with respect to existing loss-based purification strategies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on continual learning with noisy labels and mitigating the forgetting of knowledge of past learning tasks. To achieve the two targets, this paper proposes to apply the experience replay method and proposes a new sample selection strategy called Asymmetric Balanced Sampling (ABS) for replay. ABS aims to select clean samples with lower loss from the current task and select the most informative samples with higher loss from the past tasks. This paper claims that the clean samples can increase the purity of buffer and the informative samples can increase the diversity to better mitigate forgetting. To evaluate the effectiveness of applying the replay with ABS on the tasks of continual learning with noisy labels, this paper set up experiments on 4 different datasets with different noisy ratios. The results prove the methods can achieve better performances on all classification tasks compared with other CL methods with different noisy label learning approaches.  Additional experiments also present the ABS can outperform other sample methods.

### Strengths
1. This paper focuses on the problem of continual learning with noisy labels, which is vital in real scenarios.
2. This paper applies experience replay into noisy label problems and proposes novel sampling methods for the replay.
3. The experiments are comprehensive, including four different types of datasets
and two different noise injection processes. This paper compares the 
proposed methods with other different works of continual learning and noisy 
label learning. The improvement of the proposed method is significant.

### Weaknesses
1. The presentation of the part of the method requires more details. For example, what does the task D_t = (X_t, Y_t) mean? Does it mean a dataset or distribution? And what does D_t ∩ M mean in eq.(4)?
2. The experiments only provide an average accuracy for all the tasks and do not prove the proposed method can reduce the forgetting of past tasks directly.

### Questions
a) How to guarantee the stored data in the buffer does not contain a noisy label when selecting the data with high losses.
b) How does the size of the buffer impact the performance?
c) How does the proposed method perform if the order of sequence is shuffled?
d) When the length of a sequence is increased, more informative data is added and how to preserve the information from the first several tasks with a smaller size of data in the buffer?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the problem of continual learning under noisy labels. The authors mainly designed Alternative Experience Replay and Asymmetric Balanced Sampling to address the problem. At the same time, the authors also adopted consolidation and MixMatch to strengthen their algorithm. In the experiment, the authors validated their algorithms on 4 datasets and showed state-of-the-art results. They also performed a thorough analysis of the algorithm.

### Strengths
The authors perform a thorough analysis both in exploring the problem and in the effect of the algorithm. Each component of the algorithm is well motivated. The intuition of the algorithm is well presented.

### Weaknesses
1. The main concern is about the performance of the algorithm.
- The authors conducted experiments on four datasets, three of which were synthesized, and one contained natural noise (WebVision). The discussions and improvements primarily focused on the synthesized datasets. Regarding the WebVision dataset, it remains unclear why the authors selected only 10 classes out of the available 1000 classes, and the criteria for selecting these 10 classes are also not clear. According to Table 2, the AER + ABS approach did not outperform PuriDivER. The proposed method marginally outperformed PuriDivER only with the implementation of consolidation and MixMatch, which were adopted from other papers. It is of great concern that the algorithm can only function effectively in the synthetic scenario, especially when considering the broader applicability of continual learning to real-world scenarios with naturally occurring noise.
- A more thorough ablation study is needed to dissect the individual contributions of AER and ABS. The current presentation does not sufficiently demonstrate the independent effectiveness of each component.
- The paper would benefit from a clearer explanation of the consolidation phase in PuriDivER, especially since the proposed method's performance is compared against it. This would help readers understand the baseline and the novelty of the proposed approach.
- The paper does not clearly define whether the experiments are conducted in an offline or online continual learning setting. This distinction is crucial as it dictates the number of training iterations, a parameter that should not be arbitrarily chosen by the algorithm (as implied in section 4.3).
- It would be beneficial if the authors also compared it to PuriDivER when applying the algorithm to DER++, as this would provide a more comprehensive evaluation of the proposed method's performance within a different, yet related, framework.
2. Some motivation and details of the algorithm are not clear.
- In Figure 1, the authors aim to demonstrate the change in loss of noisy data with and without replay to highlight that noisy data tends to exhibit greater forgetting. However, it remains unclear in the figure which task the noisy data originates from. Furthermore, the depiction of forgetting would be clearer by comparing the accuracy (loss) of the same data from different tasks, rather than comparing the same task with different data or comparing the same data at different stages. A more rigorous approach would involve tracking the loss of specific noisy samples across different tasks to isolate the effect of forgetting.
- It is not clear if Eq(1) can represent the optimization goal. If I understand correctly, Eq(1) means finding a model to fit the noisy distribution, even when given a wrong label. The loss function yields a smaller value when the model also predicts the wrong label. However, the algorithm seems to eliminate the influence of the noisy label and encourages the model to predict the correct label. This discrepancy needs to be addressed and clarified.
- In Eq(4), is the score function $s(x)$ for task $t$? In this case, why would the buffer contain the current task data? This seems counterintuitive to the concept of a buffer that stores data from previous tasks. Additionally, the motivation behind ABS is unclear. Specifically, why does $\mathcal{L} \geq 0$ cause $s(x)$ to favor samples from the current task? This relationship needs further elaboration.
- In the ABS part, what is $p_{curr}$ and $p_{past}$? A precise definition of these terms is necessary for understanding the mechanics of the sampling process.
3. There are also some writing issues, mainly related to logic, that make the paper harder to read at some important points.
- The logic is weak in the motivation part of the abstract -- noise scenarios (caused by limited annotation time) renders the CL with buffer vulnerable
- It is wired to mention "adaption is faster" (page 2 line 3) when explain CL is vulnerable under noise label.
- In section 3.4, line 2, "the backbone had to be trained on a stream of noisy data". This is exactly the setting. This sentence is confusing.

### Questions
See the weaknesses part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tries to solve the continual learning problem under noisy labels by proposing Alternate Experience Replay (AER). The author found that the loss of clean data and noisy data have different trends that can help the model find which data has noisy labels. From this perspective, the author proposed Asymmetric Balanced Sampling to improve the AER performance.

### Strengths
+ The proposed method is well-motivated and easy to understand.
+ The experiments demonstrate the effectiveness of this method.

### Weaknesses
 + I believe the alternate replay is an interesting design, but the novelty of the proposed method is still limited. The strategies used in this paper are simple and very common techniques, such as selecting clean samples based on loss thresholds and MixMatch. It seems like a direct combination of existing technologies, with no essential innovation in methodology, especially for continual learning.
+ It is difficult to adapt to more complex noise distribution by selecting samples directly based on the loss threshold. More advanced methods should be considered [1, 2] instead of still adjusting the threshold manually, which is not helpful for either CL or noisy label problems.
+ PuriDivER is designed to handle online CL and blurry tasks with noisy labels. Therefore, it may not be suitable for offline CL. However, both online CL and blurry tasks are more challenging and realistic settings, and I’m curious how well the proposed method AER works under these settings as well. In particular, how to adapt AER to online CL where the distribution changes rapidly?
+ The comparison methods cannot demonstrate the real effectiveness of AER and ABS. Since few methods focus on offline CL with noisy labels, the authors should conduct more detailed comparative experiments. For example, using the same ABS strategy, compare the performance of AER and DividMix to verify the excellence of AER. In addition, using the same AER strategy, the performance of ABS and PuriDivER sampling methods should also be compared.

### Questions
Please refer to the weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this study, the authors leverage the phenomenon of forgetting to tackle a specific challenge: continual learning under noisy labels. They posit that samples affected by noisy labels are more prone to being forgotten, a characteristic that can be exploited to sift clean samples from noisey datasets. To achieve this, they introduce Alternate Experience Replay (AER), a mechanism that select potential clean samples in the current task while concurrently replaying samples from previous tasks. The efficacy of their proposed method is assessed using both synthetic and real-world datasets.

### Strengths
1. Combining continual learning with label noise is interesting, although this setting is controversial.
2. The paper is well-structured and easy to follow.

### Weaknesses
1. The techniques proposed in the study, specifically 'forgetting' in the realm of learning with noisy labels and 'replay' within continual learning, aren't novel in their individual contexts. The mere combination of these two established methods doesn't inherently bring novelty to the field. The use of experience replay to mitigate forgetting in continual learning is well-established, and the observation that noisy samples are forgotten more quickly has been noted in prior work on noisy label learning. The authors fail to demonstrate a significant departure from existing approaches by simply combining these two concepts.
2. The authors advocate the use of forgetting as a selection criterion, yet its effectiveness may be limited to specific types of label noise. It appears inadequate for more complex noise categories, for instance, pairflip-45 and instance label noise, let alone for real-world datasets. The 'forgetting' phenomenon is likely highly dependent on the noise distribution, and the authors do not provide sufficient analysis to show that it is a reliable indicator of label correctness across diverse noise types. The experiments should include a more comprehensive evaluation of the method's robustness to different noise patterns, including those that are more challenging than uniform random noise. The lack of analysis on more complex noise types significantly limits the generalizability of the findings.
3. The experiments are confined to small datasets, with only 10 classes from WebVision utilized, which casts doubt on the scalability of the proposed methods. For a dataset of 50k, joint learning seems more appropriate, and the unimpressive outcomes in Table 1 underscore the proposed methods' shortcomings. The authors should provide results on larger datasets and more complex tasks to demonstrate the practical relevance of their approach. The limited scale of the experiments makes it difficult to assess the real-world applicability of the proposed method. Similarly, the results in Table 2 are too inconclusive for any solid verification. The authors should report the results of other label noise methods such as DivideMix on Joint.

### Questions
1. Why are the results of CIFAR-10 with asymmetric label noise missing in Table 1?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
