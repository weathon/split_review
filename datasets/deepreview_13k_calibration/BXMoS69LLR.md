# Blind Baselines Beat Membership Inference Attacks for Foundation Models

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
Membership inference (MI) attacks try to determine
if a data sample was used to train
a machine learning model. 
For foundation models trained on unknown Web data,
MI attacks can be used to detect copyrighted training materials, 
measure test set contamination, or audit machine unlearning.
Unfortunately, we find that evaluations of
MI attacks for foundation models are flawed, 
because they sample members and non-members 
from different distributions.
For \numdatasets{} published MI evaluation datasets, 
we show that \emph{blind} attacks---that
distinguish the member and non-member distributions
without looking at any trained model---outperform 
state-of-the-art MI attacks.
Existing evaluations thus tell us nothing
about membership leakage of a foundation model's training data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper demonstrates that existing MI evaluations for foundation models perform poorly due to distribution shifts between member and non-member data. The authors show that simple "blind" attacks, which do not query the model, can outperform state-of-the-art MI attacks on common MI evaluation datasets. They identify temporal shifts, biases in data replication, and distinguishable tails as common causes for the distribution mismatch between members and non-members.

### Strengths
- While this topic has been explored by several recent works (both concurrent and prior), this work goes a step beyond to demonstrate the extend of distributional differences between members and non-members, for both LLM and VLM evaluation data for membership inference. 

- The paper is well written and supports most of its claims with empirical evidence and extensive evaluation.

### Weaknesses
The submission has significant issues regarding originality and the characterization of related work. The authors' framing of certain works as "concurrent" appears to minimize substantial overlaps, particularly with [1] and [2] which preceded the ICLR deadline by 4 and 8 months respectively. This timeframe makes it difficult to justify as concurrent research. The paper's main conclusion about flawed non-member selection methods introducing detectable distributional shifts largely mirrors the findings already established in [2].

The conclusion (L413) takes a problematic stance by seemingly absolving model trainers of accountability. Instead of abandoning membership inference evaluations, research should focus on developing methods that either avoid non-member requirements (like data-extraction attacks) or leverage trainer-provided evaluation data. Dismissing these evaluations would encourage (proprietary) model trainers to evade scrutiny of their data usage practices.

The claim on L464-465 about "no knowledge of the model" requires clarification. The paper's "blind" baselines actually incorporate significant domain knowledge about data collection patterns (e.g., dates and special tokens). The authors should explicitly state that "blind" specifically refers to lack of model access, as the attacks still utilize direct data knowledge and split information to construct rules and meta-classifiers.

- L89: Current state of the art is RMIA [3], nor LiRA. 

- L89: Please provide some more context for the 'standard' membership inference game (member and non-members should be same distribution etc.) Context is especially important for this work to understand the nuances behind different member/non-member data distributions. 

- L101: "Many of these" - Please be exact. Consider adding a table that talks about MI attack attempts on foundation models, the benchmarks they use (propose or new), and whether they suffer from the train-test split issues that the authors mention here.

- L154:  The assumption about future dates is oversimplified and overlooks legitimate cases in fiction, climate research, and policy documents

- Table 1 appears redundant given Table 2's more comprehensive presentation

- Table 2: Please make a distinction between datasets for LLMs and those for VLMs.

- L467: "... auditing unlearning methods" - there are several works describing better ways to audit unlearning [4]. It should also be pointed out that these membership-inference attacks do not work well to begin with even with properly split train/test data [2], so it is not surprising that it will not be used to audit unlearning.

### Questions
- Some of the "blind" baselines rely on detecting data references like 2024 etc. As an adversary cognizant of the training cutoff (or even an auditor), a simple solution to fix this shift would be arbitrarily replacing all such data references for non-members, maybe shift them by N nears back to match the cutoff range of the model. What happens in such a scenario? Can "blind" attacks still be successful?

- In Table 2, why are some of the entries missing values, or entire metrics (AUC ROC) not reported? These datasets are publicly available (which is how the authors get their attack's results to begin with) so I do not see why corresponding values cannot be filled in for existing works.

- I am confused by the 'Greedy rare word selection' protocol- is the sorting done using the TPR/FPR ratios on test data? If so, one can always design and selective use metrics to get good performance on test data if you are using metrics from test data to begin with. Please explain this part a bit more clearly.

- L240: "...and thus do not include it" - should be fairly simple inclusion and I do not see why it must be excluded like this? Also, as a reader I do not know what "their construction is" - if it is so similar, please briefly explain how they do it.

### Soundness
4

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines the datasets used in evaluating membership inference attacks on large language models and text-to-image generation models. The authors argue that current MIA evaluations are unreliable, as it is possible to differentiate members from non-members through blind attacks that do not utilize any information about the target model. Consequently, they suggest that state-of-the-art MIAs may not actually extract membership information effectively. To improve evaluation, the authors recommend using datasets with minimal distribution shifts between members and non-members, such as Pile or DataComp.

### Strengths
- The paper investigates a significant issue in MIA research, highlighting the importance of unbiased evaluation datasets for accurately benchmarking attack effectiveness on text-based large foundation models.

- It provides a systematic evaluation of various datasets and baseline attacks, identifying three common distribution shift patterns that influence the success of MIAs.

### Weaknesses
 - The authors claim that current state-of-the-art MIAs fail to extract meaningful membership information, relying only on biased dataset evaluation results. However, this assertion may be overstated, as blind attacks use dataset-specific prior information (e.g., timestamps), which the proposed state-of-the-art attacks may intentionally avoid as they may aim to propose a general attack. These attacks might still capture useful membership signals, albeit weaker than the dataset-specific prior information. To better support this claim, experiments on less biased datasets (like Pile or DataComp, as suggested) are necessary. If state-of-the-art methods perform close to random guessing on such datasets, it would indicate their inability to capture membership information effectively.

- As a path forward, the paper advocates for future MIA evaluations using PILE, DataComp, or DataComp-LM. However, it is unclear whether these datasets also suffer from distribution shift issues. A simple approach to evaluate this would be to apply the proposed blind attacks on these datasets; if the success rate is near random guessing, it could indicate that these datasets are indeed less biased by distribution shifts, at least concerning the three identified types of shift.

- As highlighted by Dubinski et al. (2024), different splits of training and evaluation sets can yield significantly varied membership inference attack results. To ensure robustness of the evaluations, it would be beneficial to repeat the experiments with different random dataset splits, recording the mean and variance of attack success rates. This approach would provide a more reliable comparison between blind attacks and existing MIAs.

- The novelty and technical contributions of this paper appear incremental. Distribution shift issues in evaluation datasets have been previously discussed by Duan et al. and Maini et al., and while I appreciate the systematic evaluations in this paper, it largely provides a measurement study rather than new technical contributions or insights. Thus, the paper might lack the innovation typically expected at top-tier conferences, just my two cents.

### Questions
- How do state-of-the-art attacks perform relative to blind attacks on unbiased datasets?

- Are the recommended datasets (PILE, DataComp, or DataComp-LM) genuinely unbiased?

- What are the effects of repeating experiments using different dataset splits on the evaluation outcomes?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper reveals that current evaluations of membership inference (MI) attacks on foundational models are flawed due to the use of different distributions when sampling members and non-members. The authors demonstrate this issue through an analysis of nine published MI evaluation datasets. They show that directly classify the samples in the MI evaluation datasets can outperform existing MI attacks. This finding indicates that current evaluation methods cannot accurately reflect the membership leakage of a foundational model's training data. This paper also proposes simple blind attack techniques, such as date detection and bag-of-words classifiers, which remain effective on datasets designed to eliminate distribution differences between members and non-members. The authors suggest that future MI attack evaluations should be conducted on models with a clear train-test split.

### Strengths
- This paper focuses on the irrationality of MI evaluation datasets is important, especially in an era where foundation models are widely applied.
- This paper analyzes 9 published MI evaluation datasets, demonstrating that blind attacks outperform existing MI attacks on these datasets. This reveals the incompleteness of current MI evaluations.
- The attack methods proposed in this paper perform exceptionally well, showing significant performance improvements compared to existing MI attacks.

### Weaknesses
 - The comparison experiment setup is unclear. Were the same data conditions used the experiment section? (see Q1)
- The core of this paper is to point out the shortages of existing MI attacks on foundation models. However, in the introduction, the discussion does not revolve around this point but rather focuses on how simple attacks can also achieve good results. It is recommended to revise the structure of the introduction to highlight the main contributions of the paper.
- The experimental section is divided into sections based on the datasets, which makes it difficult to correspond with the previously mentioned common reasons for the intrinsic differences. This hinders the reader's understanding of the experiments and the paper's arguments.
- The paper's proposed membership inference attack (MIA) methods, while effective at highlighting dataset biases, do not address the core issue of how foundation models process data differently for members and non-members. The analysis primarily focuses on data distribution differences, neglecting the model's role in membership inference, which limits the practical implications of the findings.
- The proposed blind attacks, such as date detection and bag-of-words classifiers, may not generalize well to other domains, particularly those where temporal or lexical biases are not as pronounced. For instance, in vision-based foundation models, the training and testing data distributions may not exhibit the same kind of easily exploitable gaps.
- The paper's contribution is somewhat limited by its focus on identifying flaws in existing datasets, rather than proposing a more robust evaluation methodology or a deeper analysis of model behavior. Simply demonstrating that naive attacks can outperform existing MIAs is insufficient for a top-tier conference without further investigation into the underlying causes.

### Questions
Q1: In Section 3, the authors first extract all dates present in the text and then proceed with date detection attacks. Are samples lacking dates excluded from your inference attacks? Specifically, in the experimental section, are the 'Ours' attack results shown in Table 2 based on a dataset that has filtered out samples without dates? Similarly, are the 'Best Attack' results measured on such a filtered dataset, or are they directly taken from the original papers? This distinction is crucial as it determines the fairness of your comparison experiments.

Q2: In your date detection attack, could you elaborate on how the date threshold is selected? The relevant section does not detail the method for choosing the threshold. Is it a matter of testing various thresholds and selecting the one that yields the best attack performance?

Q3: Regarding your Bag-of-words classification attack, what is the underlying insight or motivation for this approach? Why can different word combinations be used to infer membership properties, particularly without any interaction with the foundational models?

Q4: This paper primarily concentrates on the datasets used for MI evaluation, but it does not account for the influence of foundational models. However, the objective of MI attacks is to discern differences between a model's behavior on members and non-members. Even with datasets that are easily distinguishable based on dates or words, existing attacks still fail to achieve satisfactory results after considering the foundational models. Does this suggest that the current use of these datasets remains valid? Furthermore, by focusing on direct distinctions in membership labels and disregarding interactions with foundational models, are the signals you use for differentiation, such as dates and words, being utilized by existing MI attacks that do interact with foundational models? If current MI attacks are not leveraging your information, does it further indicate that the use of these datasets is reasonable (at least at current stage)?

Q5: In Section 3.1, this paper proposes three common reasons for the intrinsic differences between member and non-member samples. However, since different MI evaluation datasets are constructed using various strategies, it is unclear which aspects are evaluated with respect to these datasets. It would be beneficial to clarify this point in Table 2.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper argues that previous evaluations of membership inference attacks are flawed due to the distributional differences between members and non-members. The paper analyzes nine datasets and demonstrates that blind attack techniques, such as date detection (assume some text samples contain dates), bag-of-words classification (classifier is trained on 80% of the members and non-members, then test on the left 20% members), and greedy rare word selection, outperform previous state-of-the-art (SOTA) methods in the evaluation metric.

### Strengths
1. The paper provides extensive experimental results to support their claims. These results demonstrate that blind attack techniques outperform state-of-the-art methods under their settings.

### Weaknesses
1. The assumption of this paper on "blind" is not correct. "Blind" should be on both the model and data set [2021], but this paper relies on too much target dataset information. For example, one of the proposed methods only works if the dataset contains data information, and another method even needs 80% of labeled member data as the attacker's training samples. From my understanding of the literature, this rich information may not be available to other membership inference attacks, potentially giving the proposed blind attack an unfair advantage.

Hui, Bo, Yuchen Yang, Haolin Yuan, Philippe Burlina, Neil Zhenqiang Gong, and Yinzhi Cao. "Practical blind membership inference attack via differential comparisons.", 2021

2. The paper provides limited experimental details. For instance, it does not specify which models were targeted for the membership inference attacks.

3. The paper proposes ideas for constructing better datasets for evaluating membership inference attacks, but it does not provide experimental results or analysis on whether the blind attack would still outperform SOTA methods on these improved datasets.

4. Current membership inference attacks are typically evaluated across multiple datasets. For example, Zhang et al. [2024a] evaluate their Min-K%++ attack on Wikipedia, GitHub, Pile CC, PubMed Central, and many other datasets to demonstrate generalizability. However, the blind attack’s performance on other datasets is not explored in the paper, making it difficult to conclude that current evaluations are entirely flawed based on the results from just one dataset.

Jingyang Zhang, Jingwei Sun, Eric Yeats, Yang Ouyang, Martin Kuo, Jianyi Zhang, Hao Yang, and Hai Li. Min-K%++: Improved baseline for detecting pre-training data from large language models. arXiv preprint arXiv:2404.02936, 2024a.

### Questions
Duan et al. (2024) propose that temporal shifts can influence the performance of membership inference attacks. While you mention that there are differences between your paper and this concurrent work, from my perspective, both papers seem to demonstrate similar findings. Could you elaborate further on the differences between your work and Duan et al. [2024]?

Michael Duan, Anshuman Suri, Niloofar Mireshghallah, Sewon Min, Weijia Shi, Luke Zettlemoyer, Yulia Tsvetkov, Yejin Choi, David Evans, and Hannaneh Hajishirzi. Do membership inference attacks work on large language models? arXiv preprint arXiv:2402.07841, 2024.

### Soundness
2

### Presentation
3

### Contribution
2
