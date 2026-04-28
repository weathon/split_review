# PLENCH: Realistic Evaluation of Deep Partial-Label Learning Algorithms

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
Partial-label learning (PLL) is a weakly supervised learning problem in which each example is associated with multiple candidate labels and only one is the true label. In recent years, many deep PLL algorithms have been developed to improve model performance. However, we find that some early developed algorithms are often underestimated and can outperform many later algorithms with complicated designs. In this paper, we delve into the empirical perspective of PLL and identify several critical but previously overlooked issues. First, model selection for PLL is non-trivial, but has never been systematically studied. Second, the experimental settings are highly inconsistent, making it difficult to evaluate the effectiveness of the algorithms. Third, there is a lack of real-world image datasets that can be compatible with modern network architectures. Based on these findings, we propose PLENCH, the first Partial-Label learning bENCHmark to systematically compare state-of-the-art deep PLL algorithms. We systematically investigate the model selection problem for PLL for the first time, and propose novel model selection criteria with theoretical guarantees. We also create Partial-Label CIFAR-10 (PLCIFAR10), an image dataset of human-annotated partial labels collected from Amazon Mechanical Turk, to provide a testbed for evaluating the performance of PLL algorithms in more realistic scenarios. Researchers can quickly and conveniently perform a comprehensive and fair evaluation and verify the effectiveness of newly developed algorithms based on PLENCH. We hope that PLENCH will facilitate standardized, fair, and practical evaluation of PLL algorithms in the future.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes the partial label learning (PLL) benchmark PLENCH that standardizes experiments of PLL. The related work in PLL mostly selects hyperparameters based on a normally labeled validation dataset, which is highly unrealistic. The authors  propose three model selection criteria that are theoretically analyzed and empirically investigated. Furthermore, the authors propose a new dataset PLCIFAR10 that consists of human-annotated partial labels. It serves for a more realistic evaluation, as  partial labels are not synthetically generated. In their experiments, they include an excessive amount of PLL algorithms across several datasets.

### Strengths
- The paper is well-written and accessible.
- Model selection in PLL is a relevant, underexplored topic.
- The proposed dataset in a realistic PLL setting adds significant value to the PLL literature.
- Despite the model selection criteria's simplicity, the authors establish a solid theoretical link to expected accuracy and demonstrate its benefits.
- The experiments are extensive, covering many PLL algorithms from top venues.

### Weaknesses
While I think that this paper is really good, it would be nice if the authors can clarify the following weaknesses:
- **Model selection criteria:** While the criteria are intuitive and theoretically analyzed, presenting Oracle Accuracy as a contribution is problematic. As also noted by the authors, OA is standard in the literature and, thus, it should be presented as a baseline, not as a novel contribution. IMO the contribution statement in the introduction needs to be slightly adapted.
- **Use of early stopping:** For me, it is unclear how ES is used in the experiments. Lines 245-247 suggest it is applied to everything except OA. So, my question is: Is ES used in the case of CR and AA? Maybe the authors can clarify this a little better in the paper?
- **Difference between Aggregate and Vaguest not clear:** I can not find a difference in the explanation between the Aggregate and the Vaguest version. The authors state:
    
    > The first is PLCIFAR10-Aggregate, which assigns **the aggregation of all partial labels from all annotators to each example**. The second is PLCIFAR10-Vaguest, which assigns **to each example the aggregation of all partial labels from all annotators.**
    >

    Considering this explanation, there should be no difference between the versions. It would be nice if the authors could clarify (or fix) this.

- **Minor Stuff:**
    - The subfloats in Figure 2 are not aligned at the top.

### Questions
**Questions**
- Can you provide feedback to the weaknesses I mentioned above?
- I was wondering if there is access to the identities of the annotators and how the authors ensured their privacy?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces PLENCH, the first Partial-Label learning bENCHmark for comparing
state-of-the-art deep PLL algorithms.

Authors create Partial-Label CIFAR-10 (PLCIFAR10), an image dataset of human-annotated partial labels collected from Amazon Mechanical Turk. Furthermore, paper investigates the model selection problem for PLL, and proposes model selection criteria with theoretical guarantees.

Key takeaways indicate that simpler algorithms can sometimes match or exceed complex ones, no single algorithm excels in all scenarios, and model selection practices are crucial for fair comparisons in PLL studies.

### Strengths
- The authors make a significant contribution by being the first to systematically investigate model selection problems in partial-label learning (PLL), addressing a gap in the existing literature. The paper presents a comprehensive PLL benchmark that includes 27 algorithms and 11 real-world datasets.
- A notable strength of the paper is the introduction of PLCIFAR10, a new benchmark dataset for PLL featuring human-annotated partial labels. This dataset provides an effective and realistic testbed for evaluating the performance of PLL algorithms in scenarios that closely mimic real-world conditions.

### Weaknesses
N/A

### Questions
What changes do you expect to see on larger datasets and with more complex deep neural networks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates the inconsistent evaluation of different partial-label learning methods and proposes a new benchmark for a fair evaluation. In particular, the standard setting in PLL does not have a validation set that consists of ground truth labels, while many recent studies employ such a clean validation set to tune their hyper-parameters. The paper, therefore, proposes "surrogate" accuracy metrics to replace the conventional prediction accuracy (because the conventional accuracy is intractable in training) in the validation to fine-tune hyper-parameters. Those alternative metrics are theoretically proved to be "close" to the exact one. Empirical evaluation shows that the many prior methods in PLL can achieve high performance or even out-perform most recent methods in the same benchmark.

### Strengths
The paper has pointed out a critical issue in PLL research where many recent studies try to achieve the state-of-the-art results by considering an unfair setting when benchmarking with other prior methods. This potentially misleads the research direction where the performance of those prior methods can even out-perform many recent PLL approaches.

In the standard setting of PLL, the ground truth labels are not available in validation sets. Hence, it is difficult to tune the hyper-parameters of the model of interest. Hence, the paper proposes some alternative metrics as a drop-in replacement of the standard accuracy to optimise the hyper-paramters of interest. Empirical evaluation shows that this approach results in high-performance models in many benchmarks. Note that this is a strong contribution of the paper because the proposed alternative metrics are proved to be "close" to the standard prediction accuracy under certain conditions.

### Weaknesses
 **Confusing terminologies**: *model selection* vs *hyper-parameter tuning*

In the paper, the authors argue that the mismatch of the validation setting results in bad model selection. In fact, to what I understand, what that means is hyper-parameter tuning, not model selection. Hyper-parameter tuning is indeed a subset of model selection, but not the other way around. Model selection is a terminology in machine learning and also means things like variable selection and actual model choice (functional form, for example, should it be ResNet or DenseNet or a transformer), whereas the one discussed in the paper is to find the best model within a family. Thus, I suggest the authors to use the correct terminologies to reduce the confusion.

**Confusing toy example in Figures 1a and 1b**

The bar colors are inconsistent with the legend, making it hard to understand. In addition, why shouldn't the x-axis include the name of each method, instead of letting them floating inside the plotting area. The pilot (or toy) experiment mentioned at line 75 with the current description is hard to understand and should provide further details. For example, what are training and validation in Figures 1a and 1b mean? What are the meaning of the subcaptions in Figure 1? Are they the name of a method to obtain labels or the name of a dataset? I understand that the purpose is to demonstrate that evaluating methods on two different settings: with and without clean validation set leads to different performance. However, the explanation is non-coherent and hard to understand.

**Complicating notations**

Eq. (5): accuracy is already an expected (or average) value itself as shown in the right hand side of Eq. (5). Thus, the notation: $\mathbb{E}[\mathrm{ACC}(f)]$ seems cumbersome, and can be simplified to ACC only.

**Proof of Proposition 1:**

The second equality is unclear. Why is it possible to make the subtraction of two expectations be a single expectation? This is quite problematic because according to Lemma 1, S is dependent on x and y.

Another issue related to Proposition 1 is Lemma 1. A lemma is introduced as a stepping stone to use its **conclusion** to prove meaningful results (e.g., a theorem). Although Lemma 1 is introduced to prove Proposition 1 at line 192, I do not see any connection to the proof of the Proposition 1. In particular, the proof just uses the assumption (or the definition to be exact) of Lemma 1 about the *ambiuguity degree* to include in the result of Proposition 1. Hence, stating Lemma 1 to lead to the result in Proposition is misleading.

**Unclear distinction between two synthetic datasets**
Lines 286 and 287: It is unclear about the differences between the two approaches: aggregate and vaguest. In the text, they are almost equivalent or identical. Could the authors provide detailed clarification about their differences?

### Questions
As explained in the **Weaknesses**, could the authors clarify the following concerns:
- Provide a comprehensive and coherent description of the toy example in Figures 1a and 1b (or the one at line 75)
- Clarify further the proof of the Proposition 1 because it seems to be the main building block for the subsequent theoretical results.
- Clarify the differences between the two synthetic datasets at line 286.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents three key contributions: (1) an investigation of the model selection problem in the partial-label learning (PLL) setting, proposing several metrics such as covering rate (CR), approximated accuracy (AA), oracle accuracy (OA), and OA with early stopping (ES); (2) the creation of a partial label dataset based on CIFAR10, named PLCIFAR10; and (3) a benchmarking of multiple algorithms across several datasets. Overall, this paper serves as a comprehensive benchmarking study and does so effectively.

### Strengths
Comprehensive and easy to follow.

### Weaknesses
See my comments in 'Question'.

### Questions
I have a few questions and suggestions that I believe could help improve the paper:

1) Could the authors comment on the differences and similarities between their work and [1,2]? Both papers appear to address benchmarking in the PLL setting and should be discussed to provide a clearer context.

2) My major concern is that one of the main contributions is the proposed model selection criterion, while there is no experimental results to support its validity. Could the authors provide experimental evidence showing that the proposed criteria (CR, AA, OA, OA w/ ES) lead to better performance on the test dataset? Specifically, for a given ML method, does the model selected with CR (or AA, OA, OA w/ ES) outperform the model without selection? 

3) While I understand there is no universally best model selection criterion, would it be possible for the authors to include a numerical comparison showing how often each criterion (CR, AA, OA, OA w/ ES) achieves the best performance? For instance, in Table I, there are 27 algorithms. How many times does the best performance come from models selected with CR, AA, OA, or OA w/ ES?

4) To improve clarity, could the authors provide further explanation of $p(x,y)$ and $p(S|x,y)$ in Eq (4)?

5) I want to bring two particular papers [3,4] into the author's sight.

[1] Lars Schmarje, et al., "Is one annotation enough? A data-centric image classification benchmark for noisy and ambiguous label estimation," NeurIPS 2022.

[2] Mononito Goswami, et al., "AQuA: A Benchmarking Tool for Label Quality Assessment," NeurIPS 2023.

[3] Zhengqi Gao et al., "Learning from multiple annotator noisy labels via sample-wise label fusion," ECCV 2022.

[4] Ashish Khetan, et al., 'Learning from noisy singly-labeled data,' ICLR 2018.

### Soundness
3

### Presentation
3

### Contribution
3
