# Towards Comprehensive and Efficient Post Safety Alignment of Large Language Models via Safety Patching

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 3, 6, 5, 5

## Abstract
Safety alignment of large language models (LLMs) has been gaining increasing attention. However, current safety-aligned LLMs suffer from the fragile and imbalanced safety mechanisms, which can still be induced to generate unsafe responses, exhibit over-safety by rejecting safe user inputs, and fail to preserve general utility after safety alignment. To this end, we propose a novel post safety alignment (PSA) method to address these inherent and emerging safety challenges, including safety enhancement, over-safety mitigation, and utility preservation. In specific, we introduce \textsc{SafePatching}, a novel framework for comprehensive and efficient PSA, where two distinct safety patches are developed on the harmful data to enhance safety and mitigate over-safety concerns, and then seamlessly integrated into the target LLM backbone without compromising its utility.  Extensive experiments show that \textsc{SafePatching} achieves a more comprehensive and efficient PSA than baseline methods. It even enhances the utility of the backbone, further optimizing the balance between being helpful and harmless in current aligned LLMs. Also, \textsc{SafePatching} demonstrates its superiority in continual PSA scenarios. \textcolor{red}{WARNING: This paper may contain content that is offensive and harmful.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates how to balance safety enhancement and over-safety mitigation while retaining model utility during post-safety alignment. To achieve this, the authors propose the SAFEPATCHING framework, which optimizes separate patches for safety enhancement and over-safety mitigation. Through controllable patching, these two patches are selectively merged at the parameter level, addressing conflicts between them while preserving model utility. The paper includes a comprehensive evaluation across three dimensions—safety enhancement, over-safety mitigation, and utility preservation—demonstrating the effectiveness of SAFEPATCHING. Additionally, it provides a deeper insight by analyzing parameter selection, the distribution of each patch's parameters, and other aspects.

### Strengths
- This paper is well-structured and easy to follow.

- The motivation of the paper is clear, and the novel method proposed aligns well with this motivation.

- The experiments are thorough, providing a comprehensive evaluation across the three objectives on various baseline models and methods. Additionally, detailed analyses are conducted throughout.

### Weaknesses
 - The **experimental setting** section seems to overlook the choice of hyperparameters. It appears that key hyperparameters like top rate, scale weight, etc., are only mentioned in the appendix, with no indication in the main text of how these crucial settings were determined for the primary experiments (if I missed this, please let me know).

- **Minor suggestions and areas for improvement** (though not sufficient reasons for rejection): The experimental section is somewhat dense, especially section 5.2. Breaking it down into more subsections or adjusting the layout could enhance readability. Important hyperparameters like top rate, scale weight, and retention rate should ideally be summarized in a table or have a representative results diagram in the main text rather than placing all analysis in the appendix.

### Questions
- The results for top rate were somewhat surprising, as the model appears overly robust to variations in top rate. A small question arises here: could this be due to the narrow range of top rate choices? Expanding the range to include smaller or larger top rates might yield more insights.

- **Figure 3 Insight**: The distribution of overly-safety and safety parameters across Transformer layers shown in Figure 3 is very intriguing, especially with one concentrating in the middle layers and the other in the lower layers. Could you provide any insights or explanations for this phenomenon?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a method called SafePatching for post safety alignment (PSA) of large language models (LLMs). The authors claim that SafePatching addresses three PSA objectives: safety enhancement, over-safety mitigation, and utility preservation.

### Strengths
1. The problem addressed—post-hoc safety alignment—is important for ensuring that LLMs behave safely in real-world applications.
2. The empirical evaluation and ablations are fairly comprehensive across different LLM backbones and benchmarks.
3. The method shows some promise in balancing safety with utility preservation compared to existing baselines.

### Weaknesses
1. The proposed approach seems to be largely composed of a series of straightforward adaptations or incremental improvements on recent work. For instance, the use of gradient ascent and descent techniques for deriving safety and over-safety patches is largely an adaptation of existing machine unlearning methods described in the paper, rather than a truly novel contribution. The concept of patching the difference set of important parameters between safety and over-safety patches is perhaps the most novel aspect. However, it's still a relatively straightforward extension of existing ideas in parameter importance and model merging.
2. While the proposed approach does demonstrate that it is the only one to improve safety, over-safety, and utility over the backbone, in many cases, it performs significantly worse than the baselines for a particular safety or over-safety benchmark. Moreover, the safety and over-safety improvements over the backbone model are quite marginal in some cases. This highlights that there is more work to be done in effectively controlling the balance between safety enhancement and over-safety mitigation than the approach in its current state.

### Questions
1. How does the use of gradient ascent and descent for patch derivation differ from recent work in unlearning?

### Soundness
2

### Presentation
2

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
This paper proposes a post safety alignment method which merges two models post-trained on harmful data with gradient ascent and descent respectively. The post-trained and merged model preserves a balance on safety, over-safety mitigation, and utility preservation.

### Strengths
•	The idea is straightforward.
•	The experiments are extensive.

### Weaknesses
•	The paper lacks the comparision of external safeguards methods such as OpenChatKit and NeMo guardrails that are known to handle over-safety issues. Would these external safeguards methods also achieve the three objectives proposed in the paper?
•	There are a few hyperparameters in equation 7&8, such as a, b, \alpha, \beta. How you set these parameters? In Table 3, merging methods like the task arithmetic and TIES-merging do not have big differences compared to the intersect patch. Would the benefit comes from your hyperparameter selection?

### Questions
Would you please address the concerns in weakness?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel post-safety alignment (PSA) method, called SAFEPATCHING, which aims to address safety, over-safety, and utility issues in large language models (LLMs). In this paper, the authors develop a two-stage PSA framework, which applies distinct safety patches to the backbone LLM based on harmful data to improve safety and reduce over-safety, meanwhile, maintaining the utility capability of the LLM. The experiment shows that SAFEPATCHING achieves more effective and efficient PSA compared to baseline methods across four aligned LLMs

### Strengths
* The paper proposes a new method named SAFEPATCHING to address the limitations of existing methods on post-safety alignment for LLMs, such as over-safety issues and high cost.
* The paper presents experimental results and comparisons with state-of-the-art methods to demonstrate the effectiveness of SAFEPATCHING and uses multiple open-source datasets on safety, over-safety, and utility for a comprehensive evaluation. Besides, this paper has interesting findings on the distribution of the most important parameters for safety and over-safety, providing future research directions for the community.

### Weaknesses
 * Lack of justification in Sec. 3.3 controllable patching. The authors may want to highlight the novelty of their tool and the rigor of their method. Currently, it appears that the approach relies on the SNIP score proposed by Lee et al., as well as model merging methods by Yu et al. and Hui et al., without a thorough explanation of the unique contributions or advancements made in this work.
* Although the authors conducted an excessive experiment to show the effectiveness of SAFEPATCHING, several concerns existed in the settings.
   * The study evaluates SAFEPATCHING using only a single harmful dataset, AdvBench, which may not adequately demonstrate the method's transferability across different safety scenarios. Given the extensive range of safety categories and perspectives, it's essential to assess whether a backbone LLM patched using AdvBench can maintain its effectiveness on other datasets representing diverse types of harmful content.
   * The authors did not specify how they fine-tuned the Longformer-based judger. Wang et al. used annotated data generated through human labor to fine-tune their Longformer model. It remains unclear whether the fine-tuned model from Wang et al.'s work was directly utilized in this experiment or if further adjustments were made. Clarification on this point would provide a better understanding of the model’s setup and any adaptations relevant to this study.

### Questions
* Given that only the AdvBench dataset was used to evaluate SAFEPATCHING, how does the method perform across other safety-related datasets? Could testing with a broader range of harmful data enhance our understanding of its transferability to diverse safety scenarios?
* Since the authors did not specify whether they directly used the fine-tuned Longformer model from Wang et al. or performed additional fine-tuning, what impact might this setup have on the accuracy and reliability of the judgment model in this experiment?
* Could a deeper explanation of these aspects clarify the novelty and rigor of the proposed approach in Section 3.3?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a SafePatching framework to improve the safety of large language models (LLMs) while maintaining their utility. The major contribution is two types of safety patches. 
- The safety enhancement patch utilizes gradient ascent on harmful data to train the model to avoid generating unsafe responses. It effectively helps the model "unlearn" unsafe behaviors by adjusting the model parameters to minimize the risk of producing harmful content. 
- The over-safety mitigation patch, developed through gradient descent, is designed to prevent the model from being overly cautious. It fine-tunes the model to ensure it does not overly restrict or reject benign inputs that might superficially appear sensitive or risky. 

 The approach is tested across multiple LLMs, showing better performance in reducing harmful outputs, handling over-safety, and preserving utility compared to several existing methods.

### Strengths
+ The proposed approach is easy to understand, logical, and appears to be effective.

+ It addresses a significant and timely problem.

+ The paper is overall well-written.

+ The unlearning and fine-tuning techniques used in SafePatch are not new, the originality comes from considering dual patching at the same time.

+ The paper includes an extensive set of experiments.

### Weaknesses
 - Limited Novelty in Core Techniques

While the dual-patching approach is innovative in combining safety enhancement with over-safety mitigation, the core methods (e.g., gradient ascent and descent on harmful data) rely heavily on existing unlearning and fine-tuning techniques.

- Clarity on Practical Deployment

The paper would benefit from more actionable details regarding the real-world deployment of SafePatching, especially the requirements on the harmful data set.

-  Stability of SafePatching Approach

SafePatching's dual-patch integration requires careful parameter tuning, especially with the two gradient-based patches potentially introducing conflicts within the model. The process of managing these interactions, although effective, may lack robustness or generalizability across different architectures or types of prompts.

### Questions
In the SafePatching framework, Eq (1) and Eq (2) are designed to achieve two opposing objective by applying gradient-based updates in opposite directions on the same harmful dataset. Could you please clarify and elaborate how they are implemented given a harmful dataset?


In SafePatching, what requirements should a harmful dataset fulfill? For example, are there specific expectations concerning its size, diversity, or other characteristics? Additionally, are these requirements realistic for SafePatching's application in real-world scenarios?

### Soundness
3

### Presentation
2

### Contribution
2
