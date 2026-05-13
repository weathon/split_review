# Vulnerabilities Mitigation for Safety-Aligned Language Models via Debiasing

- Decision: Reject
- Scores: 6, 6, 5, 6, 6

## Abstract
Safety alignment is a fundamental yet still developing research topic for the real-world applications of AI.
Despite the multifaceted nature of safety and trustworthiness in AI, current safety alignment methods often focus on a singular notion of safety. By carefully assessing models from the existing safety-alignment methods, we found that, while they generally improved overall safety performance, they failed to ensure safety in specific categories. Our study first identified the difficulty of eliminating such vulnerabilities without sacrificing the model's helpfulness. We found that, while smaller KL penalty parameters, increased training iterations, and dataset cleansing can enhance safety, they do not necessarily improve the trade-off between safety and helpfulness. We discovered that safety alignment can induce undesired effects and result in a model that prefers generating negative tokens leading to rejective responses, regardless of the input context. To address this, we introduced a learning-free method, Token-level Safety-Debiased Inference (TSDI), to estimate and correct this bias during the generation process using randomly constructed prompts. Our experiments demonstrated that our method could enhance the model's helpfulness while maintaining safety, thus improving the trade-off Pareto-front.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper exposes and reiterates some challenges with achieving a good safety-helpfulness tradeoff in safety alignment and proposes a token-level method to debias safety alignment to achieve the same.

### Strengths
1) The paper is really well-written. Despite not working in the area actively, I could easily understand the paper. The graphs and captions are very clear.
2) I found the challenges in improving dataset section to be very enlightening. Interesting to know that a category can have not low quality or quantity and still suffer in safety score. Also interesting to know that data cleaning did not bring many benefits here.
3) The paper is timely and the topic is interesting + relevant.

### Weaknesses
1) I think the biggest weakness of the paper is its very limited experimental section. It would help to explore at least other categories, particularly those with varying characteristics. Why not include categories with similar behavior and quality-quantity distributions to the adult content category, and also explore the effect of debiasing on categories with different behavior and quality-quantity distributions? This would provide a more robust evaluation of the method's generalizability.
2) As it seems from the results, the method doesn't give significant gains on helpful win rate which we actually care about. Are there cases where your token-level method might still be beneficial? maybe where compliance and helpful win rates are highly similar? It's unclear if the method provides a practical benefit if it doesn't improve the helpfulness of the model.
3) While it is good to reiterate and provide more evidence for, I am not sure that the first two challenges are novel. The issues of safety-helpfulness trade-offs and dataset biases are well-known in the field.

### Questions
1) how & why do you choose 0.25 threshold for cleaning the data?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper is basically based on alignment of LLMs in such a way where helpfulness does not get compromised during safety tuning of LLMs. The authors proposed a method which they have coined as TSDI ensures that the bias which originates in the initial tokens of the output while Safety Tuning an LLM is taken care of. Their concern is that these unwanted biases reduce the helpfulness of the Models after safety tuning regardless of the training parameters and quality dataset used.

### Strengths
1. The approach is quite innovative and the method introduced is quite novel.
2. The in-depth portrayal of the previous works and its relation to their new work is quite in sync and properly depicted in the paper
3. Analysing all the existing parameters, training setup, methodology and dataset used in order to conclude why their method is unique and effective is commendable.

### Weaknesses
1.  Line no 54, “Previous studies on safety alignment suffer from misdirected safety evaluation”. Please add reference.
2.  In Figure 1 as well as line no 235, what does the term “Helpfulness win rate” refers to? I didn’t find its definition or explanation of what it is or how it is being calculated.
3.  In line no 257, beta = 0.1 chosen. Is there any significance of choosing 0.1 or it was a random start?
4.  In Figure 2 (a), I can see that with decreasing (beta/lamda), the safety score for adult category is increasing with number of iterations. But in line 266, it is written with decreasing (lamda/beta), the safety scores increase. There seems to be an ambiguity here.
5.  In line 267, it is written “We also observed that a small (beta/lamda) and excessive training iterations sometimes led to generation corruption”. Please provide some supporting documents in this regard.
6.  In line 309, can you please provide the analysis of changing 0.25 (0.1, 0.2, 0.3, 0.4) Like how the safety scores and Helpfulness of the model changes. It would be great to know how much is the drop in the Helpfulness while an increase in the Safety Score. There can be instances where by removing a small number of datapoints from the actual data, the safety score increases more as compared to the dip in Helpfulness. I want to know this possibility.
7.  In Figure 4, in the legend, what does the numbers in the square bracket represents?
8.  In Figure 4, 1st Graph, the x axis should be (beta/lamda) with respect to what it has been described. Are you changing the Beta in this case? So, is both Beta and Lamda changing or you are keeping beta fixed and changing Lamda to analyse the output?
9.  In line 364, why only MMLU dataset has been chosen for generating random prompts and response? Can you do it with some other dataset just to check consistency over other dataset distribution as well.
10.  Can you please clarify this? You claimed that TSDI is a learning free method to estimate and mitigate the bias introduced by the safety alignment. (Line 387) But in order to get the Biases, you are subtracting the output probabilities of initial output tokens of a Safety Aligned Model and a Reference Model. How are you getting that Safety Aligned Model without learning or safety tuning?
11.  Can you please show the variation of Safety Score and Compliance Rate with respect to the change in L (Initial number of tokens taken into consideration for debiasing)?
12.  In figure 5, why for a particular dataset, we are getting a lot of points corresponding to different Compliance Rate and Adult Safety Score? Are those different points referring to different settings (Different beta/ lamda value or different number of iterations).
13.  In Figure 6, similar confusion as mentioned in Point 12
14.  Just to check that the general capabilities of LLMs have not been hampered, can you show some benchmarking results based on your approach. (For example. MMLU, HellaSwag, ARC)

### Questions
There are quite a few things that need to be taken care to make the paper more impactful and understandable. Please look into the weakness section and address the issues.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper discusses the safety vulnerabilities of LLMs in specific categories. Even when the models perform well in the general sense of safety, the models may suffer in specific safety categories. The authors developed a token-wise debiasing approach to enhance the safety performance.

### Strengths
The paper discusses the safety of LLMs in specific categories. Both theoretical and experimental results are presented to support the paper claims.

### Weaknesses
I appreciate the efforts and experiments performed by the authors. But the findings presented in Section 3 have been known to the community, at least qualitatively. The experiments lack baseline comparisons and hence are not convincing. Please see questions for more details.

- From Fig. 1, it is hard to see how TSDI improves compared to beaver v3 and SACPO, despite the numbers shown in legend. It would be great to see some statistical significance of the proposed approach.
- The results in Fig. 1 seem to indicate that all methods struggle with category 3, including TSDI. I wonder if these results are sufficient to support the motivation of this paper. The authors could provide more details to better support the statements or motivation of the paper.
- I wonder whether it is meaningful to use SFT as the comparison baseline. The primary goal of SFT is not safety, and using it as a baseline in Fig.1 and later experiments seems unfair.
- From Fig. 6, it is hard to see how significant TSDI is compared to situations without TSDI. Some statistical significance should be presented to better support the claim.
- There is no safety baselines being evaluated in this paper and compared with TSDI. The authors should consider adding safety baselines, such as SmoothLLM, Llama guard, in-context demonstration, self-reminder, safe decoding, etc, to demonstrate the superior of TSDI
- How would one get a reference model? Is equation 7 applied to all steps $i$ or not? It would be great to see some ablation study on the choice of reference models.
- What are the difference between the points in Fig. 5? Are they generated using different hyper-parameters?
- I may have missed this. The authors showed that cleaning data may not help. How about increase the data quantity, say in the adult content category? Some experimental analysis along this direction may better support this paper.

### Questions
- From Fig. 1, it is hard to see how TSDI improves compared to beaver v3 and SACPO, despite the numbers shown in legend. It would be great to see some statistical significance of the proposed approach.
- The results in Fig. 1 seem to indicate that all methods struggle with category 3, including TSDI. I wonder if these results are sufficient to support the motivation of this paper. The authors could provide more details to better support the statements or motivation of the paper.
- I wonder whether it is meaningful to use SFT as the comparison baseline. The primary goal of SFT is not safety, and using it as a baseline in Fig.1 and later experiments seems unfair.
- From Fig. 6, it is hard to see how significant TSDI is compared to situations without TSDI. Some statistical significance should be presented to better support the claim.
- There is no safety baselines being evaluated in this paper and compared with TSDI. The authors should consider adding safety baselines, such as SmoothLLM, Llama guard, in-context demonstration, self-reminder, safe decoding, etc, to demonstrate the superior of TSDI
- How would one get a reference model? Is equation 7 applied to all steps $i$ or not? It would be great to see some ablation study on the choice of reference models.
- What are the difference between the points in Fig. 5? Are they generated using different hyper-parameters?
- I may have missed this. The authors showed that cleaning data may not help. How about increase the data quantity, say in the adult content category? Some experimental analysis along this direction may better support this paper.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper discusses how to mitigate potential vulnerabilities in safe-aligned LLMs through TSDI, in order to better balance safety and helpfulness. The proposed method adjusts the model's output during the generation process to alleviate biases introduced by safety alignment. Experiment results show that TSDI significantly enhances helpfulness while ensuring safety, improving the trade-off between safety and helpfulness.

### Strengths
As a non-learning debiasing method, TSDI estimates bias through randomly generated token sequences and subtracts this bias during the generation process. This eliminates the need for additional training and complex computational resources, making it more cost-effective in practical applications, especially in resource-limited environments.

TSDI can improve the helpfulness of the model while maintaining safety. This addresses the common trade-off issue in current safety alignment methods, where typically an increase in safety leads to a decrease in helpfulness.

### Weaknesses
The proposed method only adjusts bias when generating the initial tokens and does not consider the model's hidden states. Some biases may arise from concepts in internal states, and token-level adjustments cannot fully mitigate them, so the effectiveness may be limited in more complex generation tasks. I suggest that the authors compare their work with those studying the role of safety in model hidden states [1, 2].

In contexts with lower helpfulness, the TSDI method can eliminate some negative tokens, but the overall improvement in helpfulness is not significant. Experimental results indicate that TSDI has not significantly improved the quality of responses in these contexts, making it insufficient for tasks that have a strong demand for helpfulness.

### Questions
In multi-category safety scenarios, how can you ensure that the debiasing effect of TSDI is applicable to all categories?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper first reveals the vulnerability of safety-aligned models in certain categories and then identifies the potential bias of generating negative tokens induced by safety alignment. To address such an issue, the authors propose TSDI, a token-level safety debiased inference method, to mitigate such bias during the generation phase. The experimental results show that the proposed method can improve the safety-helpfulness of the Pareto front with better safety levels while preserving the helpfulness of the models.

### Strengths
1. Timely and vital problem.
2. A new debiasing approach to improving the trade-off between the safety and helpfulness of safety-aligned LLMs.

### Weaknesses
This paper tackles the vulnerability of safety-aligned language models from a debiasing perspective, which is interesting and deserves more exploration. However, there are several concerns regarding the problem formulation, methodology and evaluation of this paper, which makes the rigor of the methodology and the validity of the conclusion questionable. Please see the detailed comment below.

1. The problem formulation of "vulnerability of safety-aligned models" is unclear. In Section 2.2, the authors state, "Our work highlights a different type of vulnerability, in which a model, despite being safety-aligned and deemed safe overall, generates harmful responses on specific topics." To me, it is ambiguous how this vulnerability differs from the conventional safety issues in LLMs, as LLM safety is a border concept that covers various topics.

2. Throughout the paper, the authors claimed several times that the proposed method improves the safety levels of the subject LLMs across "ALL" safety categories. Conversely, the experiments are conducted mainly in the category of adult content; thence, it is not clear to what extent TSDI is still effective from other safety perspectives and the potential interaction among those safety categories.

3. Many concepts and implementation details are not fully explained. For instance, the paper does not provide a clear definition of helpfulness as well as the coreespond metrics (e.g., helpfulness win rate). Such a lack of explanations makes the paper somehow hard to follow.

4. In Section 3.1, the safety score is computed based on the percentage of safe responses classified by two safety evaluators. How do the percentages from the evaluators get fused to the final score? Since the evaluators themself can possibly exhibit certain degrees of bias on specific safety categories, are any actions taken to mitigate such an issue?

5. This paper subtracts the bias estimated from randomly generated prompts to reduce the unintentional biases of negative tokens; however, it is not intuitive to eliminate the bias from output logits in all cases. In particular, the biases of negative tokens in output logits may vary according to different safety scenarios; that is, the degree of the bias can change based on unharmful prompts and harmful prompts with different types of safety categories. For instance, it is reasonable that for specific harmful inputs, the models exhibit increased logits for negative tokens. Therefore, simply subtracting the bias measured from randomly generated prompts does not seem like a rational way that applies to all cases.

6. The evaluation metrics introduced in Section 5.1 are confusing. The authors used compliance rate and helpfulness win rate to measure the helpfulness improvement. Specifically, the compliance rate assesses the helpfulness based on particular tokens and GPT-4 is used to measure the "actual helpfulness." What does "actual helpfulness" mean here? Has the compliance rate considered cases where an unharmful prompt is refused to be answered?

### Questions
1. How does the "different type of vulnerability" mentioned by the authors differ from the conventional LLM safety vulnerabilities?

2. Is there evidence showing that TSDI is effective in "all safety categories," as the authors claim (I do not observe a significant improvement from Figure 1)?

### Soundness
2

### Presentation
3

### Contribution
2
