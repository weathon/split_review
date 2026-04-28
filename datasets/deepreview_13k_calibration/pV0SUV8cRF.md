# Tool Unlearning for Tool Augmented LLMs

- Decision: Reject
- Avg Score: 5.17
- Scores: 5, 5, 6, 5, 5, 5

## Abstract
Tool-augmented large language models (LLMs) may need to forget learned tools due to security concerns, privacy restrictions, or deprecated tools. However, unlearning tool has not been explored in prior machine unlearning works. 

We propose tool unlearning, a novel machine unlearning task that deletes already acquired tools. Compared to traditional unlearning, tool unlearning exhibits certain differences and difficulties: 1) knowledge removal instead of forgetting samples, 2) significant cost of optimizing LLMs, 3) lack of principled evaluation tools. 

To bridge this gap, we introduce three properties for effective tool unlearning and propose ToolDelete, the first unlearning method designed for tool-augmented LLMs. We also propose the first membership inference attack (MIA) model for evaluating tool unlearning.

Experiments on three tool learning datasets and tool-augmented LLMs demonstrate that ToolDelete effectively unlearns both randomly selected tools and tools from specific categories. The unlearning behavior does not impact the LLM's knowledge on non-deleted tools, while preserving performances on other general tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the "Tool Unlearning" concept for Tool-Augmented LLMs, with a focus on scenarios where these models need to forget specific tools due to security, privacy, or obsolescence reasons. The proposed methodology, TOOLDELETE, addresses the unique challenges of removing tool-specific capabilities while preserving other functionalities and general task performance. TOOLDELETE is evaluated using a novel membership inference attack (LiRA-Tool) adapted for this context. Experiments demonstrate that TOOLDELETE effectively unlearns tools without compromising the model's general utility or knowledge of other tools.

### Strengths
The unlearning setting introduced in this paper appears to be novel, and the authors have conducted comprehensive experiments across a collection of benchmarks, covering a wide range of methods.

### Weaknesses
My biggest concern is why tool unlearning needs to be addressed at the parameter level. Ideally, a tool-augmented LLM consists of both the model and a system supporting its tool-calling functionality. If such a system is in place, it should be relatively straightforward to "unlearn" a tool by implementing heuristic-based rules to block specific actions. It’s unclear why this wouldn’t be sufficient, particularly for the use cases mentioned by the authors, such as restricting tool calls that access sensitive domains or return specific email addresses. Additionally, system-level patches are more interpretable and can easily scale by adding more heuristics.

I would expect the authors to provide more justification for scenarios where system-level solutions fall short, and thus necessitating parameter-level unlearning interventions.

In addition to the concerns I raised in the weaknesses section, I have a few technical questions regarding the results presented in the paper.

Q1. How does TOOLDELETE handle scenarios where unlearning requests are sequential *and* potentially dependent or even contradictory?

Q2. How does TOOLDELETE compare to more recent proposals of LLM unlearning algorithms eg NPO [1] and CUT [2]? There seems to be a few more covered in a recent LLM unlearning benchmark [3].

Q3. I am not entirely convinced that MIA is the appropriate metric for the proposed downstream applications. Could the authors clarify why MIA is considered relevant here (Section 4.5)? Note that the downstream applications discussed don’t appear to be directly related to privacy protection so it's not clear why MIA is an ideal metric.

Q4. The sequential unlearning results (Figure 4) are not particularly convincing. In practical scenarios, a robust unlearning algorithm should ideally handle far more unlearning requests (only four are shown) and at a much finer level of granularity.

Typo:
> Line 483: Why TOOLDELETE is effectiveness?

should be "Why TOOLDELETE is effective?"

### Questions
In addition to the concerns I raised in the weaknesses section, I have a few technical questions regarding the results presented in the paper.

Q1. How does TOOLDELETE handle scenarios where unlearning requests are sequential *and* potentially dependent or even contradictory?

Q2. How does TOOLDELETE compare to more recent proposals of LLM unlearning algorithms eg NPO [1] and CUT [2]? There seems to be a few more covered in a recent LLM unlearning benchmark [3].

Q3. I am not entirely convinced that MIA is the appropriate metric for the proposed downstream applications. Could the authors clarify why MIA is considered relevant here (Section 4.5)? Note that the downstream applications discussed don’t appear to be directly related to privacy protection so it's not clear why MIA is an ideal metric.

Q4. The sequential unlearning results (Figure 4) are not particularly convincing. In practical scenarios, a robust unlearning algorithm should ideally handle far more unlearning requests (only four are shown) and at a much finer level of granularity.

Typo: 
> Line 483: Why TOOLDELETE is effectiveness?  

should be "Why TOOLDELETE is effective?"

[1] Zhang, Ruiqi, et al. "Negative preference optimization: From catastrophic collapse to effective unlearning." arXiv preprint arXiv:2404.05868 (2024).
[2] Li, Nathaniel, et al. "The WMDP benchmark: Measuring and reducing malicious use with unlearning." arXiv preprint arXiv:2403.03218 (2024).
[3] Shi, Weijia, et al. "Muse: Machine unlearning six-way evaluation for language models." arXiv preprint arXiv:2407.06460 (2024).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper is very well written. The paper defines a new problem: tool-unlearning, by setting its goal and evaluation criteria. Then, it devises a simple and effective approach to solve it given their definition. Next, it proposed an efficient novel way to evaluate tool-unlearning by adapting a well-established method in the field to their setting. Lastly, it describes a set of experiments on three models and summarizes their results.

The goal of tool-unlearning is to reduce the model ability to perform a (tool-related) task(s), while not damaging the general performance of the model on other tasks/tools.

The evaluation is an adaptation of LiRA, a Membership Inference Attack approach to measure unlearning.

The SFT approach is simply to train the model to perform poorly on the set of tools to be unlearned, while also training on the tools to be retained, while aslo regularizing with the set of original weights to maintain performance on other skills. This is a direct implementation of the aforementioned goal of the approach. A similar approach is taken using DPO.

LiRA-tool, similar to LiRA, proposed to approximate the distribution losses Q_in and Q_out, that describe models that were trained and that were not trained using the unlearned-tools. Here, due to the complexity of LiRA they propose to prompt GPT-4 with various instructions to draw samples of Q_in and Q_out. 

The experimental-setup is based on three task-augmented models: ToolAlpaca, ToolLLaMa and Gorilla.

### Strengths
This paper presents its ideas with exceptional clarity, making it remarkably easy to follow and comprehend. The two proposed variants of tool-unlearning are both straightforward and effective, and the experimental setup is extensive. The results are also very impressive, convincingly demonstrating the power of their method in achieving the tool-unlearning goal.

### Weaknesses
The main weaknesses of the paper are: the importance of the paper, the contribution, and the soundness.

Importance:
1) It is unclear in which situations tool-unlearning would be preferred to what I consider to be the default which is to restrict the tool itself as opposed to the model. From a security standpoint if the model possess an ability to abuse a tool, or a service using a tool, the protection should be taken care of at the tool/service side as opposed to the client/model in this case.

2) Additionally, if tool-augmentation takes place after pretraining and instruction-finetuning, as presented in Figure 1, it might not be too costly to retrain the Instruction-finetuned model without some of the tools, relatively cheaply and fastly.

Contribution:
1) Given the proposed definition tool-unlearning amounts to reducing the model's capacity on certain tasks. Reduced skill-performance doesn't provide any insight on the main of goals of knowledge / sample unlearning, and therefore the paper have very little to do with unlearning, aside from reframing already known approaches for training models to behave with accordance to a wanted behavior.

Soundness:
1) Measuring tool-knowledge by prompting might not suffice. In a scenario in which the model weights are shared, maybe a bit of unintentional fine-tuning will recover the tool-knowledge. Or, there could exists other prompts that are able to elicit the model's ability to use a tool.

2) LiRA-Tool limitations needs to be evaluated - in order to establish trust in the newly proposed approach to evaluate tool-unlearning, it is crucial to show evidence or justification for the GPT-4 "shadow-samples" as means to approximate Q_in / Q_out efficiently, what is the quality and robustness of this approximation?

### Questions
How come "TOOLDELETE-SFT" or "TOOLDELETE-DPO" have better (lower) results for T_f? doesn't that suggest that the information and knowledge about this still is still preserved in the model to some extent? I would imagine an optimal unlearning to be indistinguishable from retraining. It could be risky to have model hide a specific capability, because an attacker might be able to learn from this very signal about the what was removed.

Can you give a concrete examples in which tool-unlearning could be useful?

Is there anything specific to tools/unlearning in this paper, or does it mainly bother with selectively reducing task-performance?

### Soundness
2

### Presentation
4

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a "tool unlearning" method for tool-augmented large language models (LLMs), which effectively removes the capability to use specific tools without compromising the model's overall abilities. The study presents the TOOLDELETE algorithm, which successfully erases targeted tool knowledge while retaining the model’s performance in using other tools and general tasks. The LiRA-Tool evaluation method confirms the effectiveness of this approach. This technique is significant for meeting data privacy and compliance requirements.

### Strengths
* Propose the novel task tool unlearning and describe the difference between this and traditional sample-level unlearning.

* Make concerns about unlearning knowledge of targeted tools, retaining knowledge of other tools and general ability of LLMs.

* Main experiments show good performance in unlearning and retaining knowledge of the proposed method.

### Weaknesses
 * Clear real-world applications cannot be found. This paper provides a real-world harmful case: unlearning tool-augmented LLM with knowledge of insecure HTTP requests. However, it is hard to find the applications that need the proposed tool unlearning. The authors should clearly demonstrate the practice of the proposed approach in real-world applications. Firstly, this case does not match the authors' claim of "preserving its ability to use others tools and perform general tasks". Secondly, as described in the paper, LLMs retain "harmful knowledge" from tools, and this knowledge may be unlearned through a traditional unlearning process(constructing a dataset of question-answer pairs). The author must prove why we need tool unlearning rather than traditional unlearning in open-world cases.

* Lack of description of loss function design and mistakes found in section 4.4. As shown in the authors' objective function, the design of the function '$g(f, t)$' is of great importance and directly decides whether the tool unlearning can succeed or not. However, the authors do not report details of the function $g$. This makes it hard to evaluate the effectiveness of the method. Thus, in Eq. (5), $[g(f_0, t_i) − g(f′, t_i)]$ and $[g(f, t_m) − g(f′, t_m)]$, as far as I'm concerned, lead to a certain score, while $\alpha(\theta_0 − \theta_R)$ leads to a vector. These cannot be added together. The authors should elaborate more on each term of the loss function. 

* The author claims that their method can keep the knowledge from other tools after the tool unlearning process. However, they do not conduct experiments on this. I would like the authors to conduct more experiments on an LLM with two or more tools' augmentation to prove the claimed benefits.

* Further suggestions: more mainstream datasets and benchmarks can be utilized in the experiment, e.g., [1], [2].

* Typos: "preservemode's" in line 215 on page 5.

### Questions
* Why do we really need tool unlearning rather than traditional unlearning in open-world cases?

The author have made good efforts in solving my problems. Thus, I will raise my score to 6.

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
The paper propose a novel threat model that looks at tool use knowledge as source of privacy and security issues and therefore proposes methods to unlearn them. One of the more convincing examples is that a tool that knows how to operate a private tool might reveal to adversary some information. 

The paper goes with proposing a ToolDelete method that using three separate objectives: removal, retention and utility retention finetunes/DPO the model to achieve these objectives. The paper further states challenges with evaluation and adapts LiRA approach to measure method efficiency.

### Strengths
- Overall the paper is well written with a standard and comprehensive evaluation and methods. 
- The paper presents a novel threat model
- Evaluation focuses on three popular benchmarks for tool use
- Results show a strong advantage of the proposed ToolDelete method over standard unlearning tools

### Weaknesses
 - It is not clear if the threat model is valid -- the right to be forgotten claims that appear in intro and broader impacts have no relation to the tool use and therefore invalid. A credible attack that shows privacy or security issues is required to justify the proposed problem. While the problem itself is novel I struggle to see the value in addressing this problem, i.e. why would anybody want to unlearn tools for privacy/security reasons.

- It is mentioned that full re-training is costly and pointless, however while this argument is relevant  for unlearning literature in general it does not look to me relevant for this particular problem. As the pipeline commonly shows tool use training comes after the most costly part of model pre-training and therefore is not that challenging to do. Furthermore, it is not clear that models should be trained to support all tool use in practice -- it could be that for particular use cases the company would only train for a particular sub-set of tools and therefore retraining the model is not a challenge.

-- novelty: while the threat model is novel it is not clear, how novel is the contribution as the proposed method simply balances three losses that seems like a rather straightforward way to build the tooldelete method -- explaining the challenges would be interesting. However, I have to note LiRA-Tool adaptation is nice trick (nevertheless the paper does not focus on this part as much).

-- Investigating imbalance in tool unlearning seems interesting but does not exist in the paper. The authors only measure percentage of unlearned tools, but I would rather see how different tools impact unlearning metrics --> where does the drop in Table 1 come from?

### Questions
- explain the threat model
- differentiate more from naive solutions
- provide more justification on novelty of the approach
- investigate how different tools are unlearned

### Soundness
3

### Presentation
4

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
The authors introduce a new kind of task, "tool forgetting". Compared with traditional forgetting, it needs to deal with different challenges: it is knowledge to be removed rather than individual samples to be forgotten, and the cost of optimizing LLMs is high. To address these issues, the authors propose TOOLDELETE, and a member inference attack model LiRA-Tool, .

### Strengths
(1)The tool forgetting task is innovatively proposed, opening up a new direction for related research.

(2) The TOOLDELETE method has a clear design and implementation, and the experimental results show that it is effective in tool forgetting.

(3) A LiRA-Tool model is developed to evaluate tool forgetting, which is novel.

### Weaknesses
(1) Does the author's approach apply to closed-source or API-only LLMs? If so, the author can perform some extended experiments to better illustrate the effect of TOOLDELETE.

(2) There is a lack of sufficient research on the impact of different model sizes on tool forgetting.

(3) The shadow samples in LiRA-Tool may not fully represent the complexity of the original tool learning data, which affects the accuracy of the evaluation.

### Questions
The author needs to explain in detail the questions I mentioned above, and I will determine the final score based on your answers.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the concept of tool unlearning for tool-augmented large language models (LLMs), addressing the need to remove learned tools due to security, privacy, or obsolescence concerns. Unlike traditional unlearning, tool unlearning focuses on knowledge removal rather than forgetting data samples, involves significant optimization costs, and lacks established evaluation methods. To address these challenges, the authors propose three key properties for effective tool unlearning and present ToolDelete, the first method designed for this purpose. Additionally, they introduce the first membership inference attack (MIA) model to evaluate unlearning effectiveness. Experiments on multiple tool learning datasets demonstrate that ToolDelete can successfully unlearn both randomly chosen tools and specific tool categories without compromising the LLM’s performance on non-deleted tools or general tasks.

### Strengths
1.	The problem of tool unlearning is interesting and well-motivated. We definitely need a solution dedicated to achieving tool unlearning for LLM-enabled agents.

2.	The experiment is extensive and comprehensive.

3.	The paper is well-organized and easy for readers to follow.

### Weaknesses
1. I disagree with most differences of tool unlearning compared with sample-level unlearning. According to the entire paper, especially the experiment setups, the tool unlearning also relies on training or tuning with unlearning tool-related data. The model ability regarding certain tasks or tools is reflected in the data samples, in this sense, sample-level unlearning and tool unlearning are the same. Except for the difference regarding Evaluation, I don’t think there is any uniqueness in tool unlearning.

2. Two terms of Eq. (5) require the base model f_0 without learning any tools. However, in practical scenarios, only the model f that has learned many tools is available to unlearn certain tools. How does ToolDelete work in the case when f_0 is unavailable?

3. In terms of LiRA-Tool, how you generate ‘shadow samples’ via prompting GPT-4, detailed instructions or prompts should be provided.
 
4. A comparison between traditional sample-level LiRA and LiRA-Tool is needed, which can reflect the issues of sample-level LiRA mentioned in Lines 296-298.

5. The training time comparison to retraining from scratch has no significance. The comparison between ToolDelete and other baseline unlearning approaches is more needed.

### Questions
See the weaknesses above

### Soundness
2

### Presentation
3

### Contribution
2
