# Cross-modal Mitigation of Spurious Correlation for Prompt-tuning in VLMs with Causally Motivated Logic Alignment

- Decision: Reject
- Scores: 5, 6, 6, 3

## Abstract
Recent studies have shown that pre-trained vision-language models can effectively adapt to diverse downstream tasks through parameter-efficient prompt tuning. Unfortunately, the tuned models can exploit spurious correlations during prediction, resulting in a failure to generalize to out-of-distribution test data, especially when the tuning dataset exhibits bias. How to achieve cross-modal mitigation of spurious correlations during prompt tuning of vision-language models remains an open question. In this paper, the challenging problem is tackled by leveraging the stable relationship between necessary and sufficient causal features and the corresponding label. On the one hand, we constrain the learning process of prompt by reinforcing the necessary and sufficient connection between the textual labels and textual features. On the other hand, the probability of necessity and sufficiency between the textual features and the filtered visual features is measured and maximized to enhance cross-modal feature alignment. By iteratively optimizing these two objectives, we can achieve cross-modal mitigation of spurious correlations because the logic equivalence between textual labels and visual features is bolstered. The theoretical analysis on generalization error indicates that our method can achieve a tighter generalization error bound than existing approaches. We evaluate the proposed method on several commonly adopted out-of-distribution datasets, and the empirical results demonstrate the superiority of our method over the state-of-the-art competitors.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a novel framework, LogicAl-PT, that addresses the challenge of cross-modal mitigation of spurious correlations in prompt tuning of vision-language models. The authors introduce a new concept, logic alignment, which integrates the mitigation of spurious correlations with cross-modal alignment of representations, and demonstrates its effectiveness through theoretical analysis and empirical results on various out-of-distribution datasets. LogicAI-PT earns competitive performance compared with traditional prompt-tuning methods for CLIP model.

### Strengths
Extensive theoretical analysis is provided to verify the proposed concept, PNS and PNS risk modeling.

### Weaknesses
- In contrast to the detailed theoretical analyses, the empirical verifications are fairly absent in this paper. Take the most recent competitor Coopood as an example, this paper presents much fewer empirical analyses, i.e. only 2 tables in the experiment section for verification. More ablation studies about the hyper-parameter chosen, visual results about the improvement on spurious correlations should be provided.

-Some more recent prompt tuning methods[a][b] should be discussed and compared with.

- Experiments on more architectures like ViT except for ResNet-50 should be done as well.

### Questions
Please see weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents Logical-pt, a framework for mitigating spurious correlations in vision-language models. It uses causally motivated logic alignment to align visual and textual features during prompt tuning. The method is backed by a tighter generalization error bound and empirically validated on several datasets, outperforming existing methods in out-of-distribution generalization.

### Strengths
* the results reported in this paper demonstrates good performance on multiple benchmarks
* this paper did extensive evaluations and experiments to validate the method's effectiveness

### Weaknesses
 * The proposed method shows superior performance compared with other benchmarks. What is the computational efficiency compare to simpler methods?

### Questions
same as above

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
4

### Summary
This paper introduces the novel LogicAI-PT framework to mitigate learning of spurious correlations in prompt tuning of CLIPs. It models the PNS (probability of necessity and sufficiency) by introducing intervention $\bar{Q}$ and $\bar{\Phi}$. The author provide extensive introduction of the methodology and background and the experimental results are significant.

### Strengths
The proposed method is quite simple and effective regarding the significant improvement of multiple benchmarks. The idea of tackling spurious correlation problem from a sufficiency-necessity view is intuitive and is implemented based on thorough proof.

### Weaknesses
1. The proposed method seems to be universally applicable to many tasks rather than only prompting of VLM as classifier. Causal Representation Learning baselines adapting from other tasks can largely consolidate the motivation of this paper.
2. Ablation study of the proposed is not enough. What is the effect of different $\alpha, \beta$? #419 introduces the author chooses different value combination for different benchmarks. The robustness regarding different hyper-parameters can largely affect the applicability of this method.

### Questions
1. What kind of knowledge does the $\bar{Q}$ and $\bar{\Phi}$ learnt durning the training process? I am curious about more quantitative and qualitative results about these additionally introduced intervention modules. 
2. Could this method transfer to other VLMs such as EVA-CLIP and single tower VLMs such as BEiT?

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
4

### Summary
This article introduces the concept of logical alignment to address the cross-modal mitigation problem of spurious correlation for prompt adjustment in visual language models. To achieve this, the authors maximize the probability of necessity and sufficiency corresponding to cross-modal and textual logical alignment. Theoretical analysis proves that the proposed method has a tighter generalization error bound compared to existing approaches. Performance is analyzed across a few different test data distributions, and components of the method are ablated.

### Strengths
The generalization error bond of the presented method is provided with theory analysis in Appendix A. 

The novelty of the method is how to integrate the probability of necessity and sufficiency in multi-modal learning.

### Weaknesses
The paper is not easy to follow. This is due to the symbols being confused, e.g., $\Phi$ denotes the filter in Cross-modal logic alignment but visual representation space in Textual logic alignment.
While the first half of the paper explains the idea and motivation well, creating a rightful sense of expectation of the result, the section on the results somewhat comes short of delivering the findings with a bang.  After reading the first half I was excited to read the next pages to find "Where are those indeed integrated areas for boosting the expected performance ", and tingling with an expectation of learning something new. But then, for some reason, the Overall Performance and Ablation Study sections are very timid and just present dry numbers for each of the tests that were planned.  

1. It would be helpful to include a better explanation of what the "spurious correlation in vision-language models" is exactly. Maybe a picture. 
2.The paper borrowed too much content from the existing papers and it could be removed by referring these papers. Even so, the motivation is not clear since the authors employ PNS without explanation.

3. Page 6, Section 4.1: The NSC feature shown Figure 1 is not explained by the authors themselves how to make use and take advantage of this. 

4. Compared to CoOPood,  it seems that the proposed method exploits PNS terms instead of mutual information to align cross-modal representations. I am wondering how effective the PNS term is in cross-modal mitigation of spurious correlation.  
5. Why was it necessary to do textual logic alignment?

### Questions
I would like to hear the authors' discussion regarding the three weakness that I highlikeed above:

1. Usefulness of the PNS term. 

2. Usefulness of the textual logic alignment. 

3. How to extractive NSC features in textual and visual modality.

### Soundness
2

### Presentation
2

### Contribution
2
