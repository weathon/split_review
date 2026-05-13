# Active Test-Time Adaptation: Theoretical Analyses and An Algorithm

- Decision: Accept
- Scores: 8, 8, 5, 6

## Abstract
Test-time adaptation (TTA) addresses distribution shifts for streaming test data in unsupervised settings. Currently, most TTA methods can only deal with minor shifts and rely heavily on heuristic and empirical studies. 
  To advance TTA under domain shifts, we propose the novel problem setting of active test-time adaptation (ATTA) that integrates active learning within the fully TTA setting.
  We provide a learning theory analysis, demonstrating that incorporating limited labeled test instances enhances overall performances across test domains with a theoretical guarantee. We also present a sample entropy balancing for implementing ATTA while avoiding catastrophic forgetting (CF). We introduce a simple yet effective ATTA algorithm, known as SimATTA, using real-time sample selection techniques. Extensive experimental results confirm consistency with our theoretical analyses and show that the proposed ATTA method yields substantial performance improvements over TTA methods while maintaining efficiency and shares similar effectiveness to the more demanding active domain adaptation (ADA) methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new setting, namely ATTA (Active Test-Time Adaptation), to integrate active learning (a limited number of labeled test samples) within test-time adaptation (TTA) to enhance TTA under domain shifts. The problem itself is practically important and the paper presents a theoretical guarantee and a sound solution (SimATTA) that combines incremental clustering and entropy selection to conduct online sample selection, avoiding catastrophic forgetting issues. The simplicity of the proposed algorithm and its successful application on real datasets are commendable. A thorough empirical study (including ablations) with encouraging results (both in the paper and its supplementary material) shows the effectiveness of the approach in terms of its effectiveness and generalization performance. The paper's clear contribution to the TTA community is evident, and I recommend its acceptance.

### Strengths
**Originality**: The paper introduces a novel setting, active test-time adaptation (ATTA) with theoretical guarantees for alleviating distribution shifts and mitigating catastrophic forgetting and extensive experiments on several benchmarks under domain generalization shifts. Additionally, the Section FAQ & Discussions in supplementary material is highly praiseworthy.

**Quality**: The paper provides a thorough experimental evaluation of the SimATTA algorithm on four datasets (PACS, VLCS, Office-Home, and Tiny-ImageNet-C). The paper also conducts ablation studies to analyze the impact of different components of SimATTA. The paper demonstrates that SimATTA can achieve superior performance and maintain efficiency.

**Clarity**: The paper provides sufficient background information including theory and closely related works to situate the contribution of the ATTA setting and the SimATTA algorithm.

**Significance**: The paper proposes an important and challenging setting of active test-time adaptation (ATTA) and a detailed comparison with related settings (DA/DG, TTA, ADA, ASFDA, and AOL) highlights the value of the proposed ATTA. ATTA also has many potential practical utilities such as an autopilot system and a personalized chatbot discussed in supplementary material.

### Weaknesses
 **Insufficient visualization**: Though the authors have provided detailed algorithms (Alg. 1 and Alg. 2) to show the proposed SimATTA algorithm, it is still hard to follow the whole picture quickly. The lack of a clear diagram makes it difficult to understand the interaction between the incremental clustering and entropy-based sample selection. A visual representation of the data flow, showing how samples are selected, clustered, and used for adaptation, would greatly improve the paper's clarity.

**Insufficient justifications**: For example, regarding the **efficiency** and **applicability** of ATTA, some justifications are missing in this paper. First, as shown in Tab. 3, the time cost of ATTA is around ten times than general FTTA (Tent: 68.83, EATA: 93.14, SimATTA: 736.28). The reason might be the clustering-based selection process and fully fine-tuning pre-trained models? This significant increase in computational cost needs a more thorough discussion, especially concerning its practical implications. Second, though the authors state that "ATTA can be applied to any pre-trained models including large language models (LLMs)", they provide no experimental results. The claim needs empirical validation, particularly given the computational demands of LLMs and the potential for different behavior compared to smaller models.

**Inconsistent results**: results of SimATTA ($B\le$500) in Table 2 (TTA comparisons on PACS) and Table 8 (Ablation study on PACS) are different.

### Questions
1. As an active sampling algorithm, how to define an informative test sample, especially on streaming data? The authors might provide some visualization results for better understanding.

2. How about the cost of the ATA training set?  It seems that the SimATTA algorithm will keep a training set (the maximum size is $\mathcal{B}$?) during the test-time adaptation, would this strategy violate the nature of test-time adaptation, i.e., real-time?

3. There are many hyper-parameters in this work, such as two entropy thresholds $e_l$ and $e_h$, number of cluster centroid budget $NC(t)$, centroid increase number $k$, etc. The question is how to choose them for different datasets. In some sense, this is not the weakness/limitation of this particular paper but rather applies to the whole AL paradigm.

4. It is unclear what the meaning of `steps=10` is. And what is the config of SimATTA? SimATTA (`steps=1`) or SimATTA (`steps=10`)?

5. How to deal with an extreme situation in which only one sample is in a mini-batch, i.e., the batch size is 1.

6. Another minor question is, why the performance of Enhanced TTA on Tiny-ImageNet-C (severity level 5) is poor? Also, why the baseline results (CLUE) on VLCS of Tab. 4 are too low, even worse than that of the Random method?

7. In Section 5.2, "randomly select labeled samples and fine-tune them with `their selected pseudo-label samples.`" Is it a mistake?

### Soundness
4 excellent

### Presentation
3 good

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
This paper proposes a novel, formal problem setting of Active Test-Time Adaptation (ATTA), which incorporates active learning to perform test-time adaptation (TTA). It attempts to mitigate distribution shifts and catastrophic forgetting, while not being provided access to source data, model parameters, or pre-collected target samples. 

A theoretical analysis of ATTA in the setting of binary classification is provided. First, the theory establishes a learning bound that has the notions of composition of training data, estimated distribution shift, and ideal joint hypothesis performance. Second, the fore-mentioned theory is utilized to shown that catastrophic forgetting can be mitigated by performing selective sample selection through entropy minimization. 

SimATTA, a practical algorithm built upon the ATTA theory, is then developed. It integrates incremental learning and selective entropy minimization techniques. Empirical evaluations on four benchmarks simulating distribution shifts demonstrate the effectiveness of SimATTA when compared to the existing work. It achieves state-of-the-art accuracy under distribution shifts while maintaining the computational complexity that is not significantly higher than that of the prior work.

### Strengths
$\textbf{Novelty and significance}$:
In my opinion, the empirical results, especially addressing RQ1, clearly set this paper apart from previous research, paving the way to overcome distribution shifts under the TTA setting. The proposed algorithm, SimATTA, significantly surpasses the existing TTA algorithms in terms of performance accuracy under distribution shifts. It also appears to exhibit greater resilience to catastrophic forgetting. Additionally, it is supported by a robust theoretical framework.

$\textbf{Completeness and comprehensiveness}$:
The main manuscript and the supplementary material offer a comprehensive context and detailed information about the proposed work. Furthermore, related work addressing distribution shifts under various settings is also adequately discussed.

### Weaknesses
I found no major weakness from this paper. One minor aspect I would like to highlight concerns the clarity of the experimental settings, such as domain-wise data stream, random stream, post-adaptation, and so on. It took me some time to grasp all of these distinct settings. Perhaps including a dedicated section to explain about these settings would be more helpful.

### Questions
The “budget” term appears to be a significant factor in the algorithm. However, I’ve not been able to identify its relationship to the cluster centroid number. Could the authors please provide clarification on this matter?

I’m looking forward to seeing the code implementation of SimATTA.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper titled "Active Test-Time Adaptation: Theoretical Analyses and An Algorithm" delves into a novel approach for machine learning models that dynamically adapt during test-time  under domain shifts. Traditionally, models rely heavily on heuristic and empirical studies without further adaptation. The authors challenge this convention by introducing a mechanism that allows the model to actively query an oracle (typically a human) during test-time to obtain labels for certain instances. The objective is to enhance the model's performance on the test set by leveraging this limited interaction with the oracle.

The primary contributions of the paper are as follows:

1. Introduction of the Active Test-Time Adaptation (ATTA) framework.
2. A novel algorithm for determining which instances should be queried from the oracle, based on their potential impact on the model's performance.
3. Experimental validation of the ATTA framework on several benchmark datasets, demonstrating significant improvement in performance over non-adaptive baselines.

### Strengths
1. The concept of actively adapting a model during test-time based on interactions with an oracle is innovative. This breaks away from the conventional train-test paradigm, paving the way for more dynamic and adaptive models.

2. The authors provide a theoretical foundation for the ATTA framework, making a compelling case for its viability and potential benefits.

3. The proposed method is model-agnostic, meaning it can be applied to a wide range of machine learning algorithms, from simple linear classifiers to complex deep learning architectures.

4. The extensive experiments on benchmark datasets provide strong empirical evidence supporting the effectiveness of the ATTA framework. The improvements over non-adaptive baselines are both statistically significant and practically relevant.

### Weaknesses
1. The ATTA framework's effectiveness hinges on the availability and accuracy of an oracle. In real-world scenarios, obtaining such an oracle (especially a human expert) might be challenging, time-consuming, or expensive. The paper does not adequately address the practical limitations of relying on human-in-the-loop feedback, especially in contexts where expert availability is scarce or costly. The assumption that an oracle can provide accurate labels for queried instances is also a potential weakness, as human experts can be fallible or inconsistent, which could introduce noise into the adaptation process.

2. While the approach shows promise on benchmark datasets, its scalability to very large datasets or real-world applications remains untested. The computational overhead of deciding which instances to query and updating the model during test-time could be prohibitive in some scenarios. The paper lacks a detailed analysis of the computational complexity of the proposed algorithm, particularly concerning the incremental clustering and model update steps. The authors need to provide a more rigorous analysis of the time and space requirements of their method, especially when dealing with high-dimensional data and large-scale datasets. Furthermore, the paper does not explore the potential for parallelization or other optimization techniques to mitigate the computational burden.

3. The paper assumes a limited budget of queries to the oracle. In many real-world scenarios, determining this budget or ensuring its strict adherence might be challenging. The paper does not discuss how the query budget should be determined in practice, or how the performance of the ATTA framework is affected by different budget sizes. The assumption of a fixed query budget may not be realistic in many applications, where the availability of oracle feedback may vary over time. A more adaptive approach to query selection, which can dynamically adjust the number of queries based on the observed performance of the model, could be more robust in real-world settings.

4. Continually adapting the model during test-time based on feedback from the oracle could lead to overfitting, especially if the test set is not representative of the broader data distribution. The paper does not adequately address the risk of overfitting to the test set, particularly if the test set is small or biased. The proposed approach of using balanced entropy sample selection may not be sufficient to prevent overfitting in all cases, and the paper lacks a detailed analysis of the generalization performance of the adapted model. The authors need to provide more empirical evidence that the ATTA framework can generalize well to unseen data, and not just improve performance on the specific test set used for adaptation.

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper points out that achieving domain generalization is theoretically impossible without additional information. Therefore, this paper introduces active test-time-training(ATTA), combining active learning with test-time-training, and proposes an effective ATTA algorithm, SimATTA, that innovatively integrates incremental clustering and selective entropy minimization to address catastrophic forgetting and real-time active sample selection issues.

### Strengths
（1）This paper innovatively combines active learning with TTA, enhancing performance across test domains. and present sample entropy balancing to avoid catastrophic forgetting.
（2）The paper conducted extensive experiments and compared with the latest state-of-the-art methods on multiple datasets, achieving superior results.
（3）The paper is well-organized, and it provides extensive proofs for the theorems mentioned.

### Weaknesses
1. In Section 3.2, the authors state that entropy is essentially a measure of the distribution distance between the model distribution and a test sample, which is not true. While entropy can provide information about the uncertainty of the model, it does not directly measure the distributional distance between the model's distribution and the test samples. This fundamental flaw casts doubt on the proposed method.
2. Table 3 indicates that, in terms of efficiency, SimATTA takes longer than all previous methods, making it less efficient.
3. In Appx. H.2., when B<=500, the performance of SimATTA is close to that of other methods, with no distinct advantage
4. The ablation study is not comprehensive enough to effectively prove the efficacy of both the incremental clustering and selective entropy minimization methods.

### Questions
Entropy does not directly measure the distributional distance between the model's distribution and the test sample，so the theoretical foundation presented in the paper is shaky. How do you view this issue?

After reading the rebuttal, I decided to raise my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
