# Testing the Limits of Jailbreaking with the Purple Problem

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
The rise of ''jailbreak'' attacks on language models has led to a flurry of defenses aimed at preventing undesirable responses. Nonetheless, most benchmarks remain to be solved, not to mention real-world safety problems. We critically examine the two stages of the defense pipeline: (i) defining what constitutes unsafe outputs, and (ii) enforcing the definition via methods such as fine-tuning or input preprocessing. To understand whether we fail because of definition or enforcement, we consider a simple and well-specified definition of unsafe outputs---outputs that contain the word ''purple''. Surprisingly, all existing fine-tuning and input defenses fail to enforce this definition under adaptive attacks and increasing compute, casting doubt on whether enforcement algorithms can be robust for more complicated definitions. We hope that this definition serves as a testbed to evaluate enforcement algorithms and prevent a false sense of security.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper stipulates the defense of jailbreak into two independent
components: 1) defining the jailbreak notion and 2) instilling the
jailbreak notion into a model to enforce the jailbreak defense. By devising
a straightforward and well-specific "jailbreak" notion, the Purple Problem,
this paper isolates the second component and investigates the limits of the
enforcement of jailbreak defense.

### Strengths
1. The proposal of the purple problem is a valuable contribution to the
   jailbreak defense research.
2. The paper conducts comprehensive experiments to investigate enforcement
   ability of existing jailbreak defenses.

### Weaknesses
1. The setup of fine-tuning based defense is problematic. From the Appendix, it seems that the model is not clearly instructed that only the word "purple" should not be contained in the generated text. If it is not explicitly instructed, how can the model realize the purple problem specified in this 
paper?
2. Is the purple problem a good and representative jailbreak notion? Given
   it is a simple word, there may exist a gap between the purple problem and
   the real-world jailbreak problems, which are high-level and abstract.
   Futhermore, even the existing jailbreak methods can force the model to 
   generate several specific words, the aligned model can still generate
   a refusal response, e.g., "Sure, I am happy to help you with that. But
   I cannot provide the information you requested."
3. The model selection is not convincing. All three models have the same
   architecture, which may not be sufficient to justify the generality of the
   conclusion drawn from the experiments.
4. What is the definition of "gibberish" in line 248? Usefulness is a very
   important metric in the evaluation of jailbreak defenses, and there
   exists a trade-off between usefulness and security. Besides, a typical
   practice to measure the usefulness of a model in the community is to
   evaluate the enhanced model on some widely-used benchmarks like MMLU.
   It is suggested to provide the usefulness metric before the experiments.
5. More detail is required regarding the paraphrase defense. If the model
   is not instructed or fine-tuned to avoid the word "purple," how can the
   paraphrase defense work?

### Questions
Please see the weaknesses section for questions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper examines why defense mechanisms fail to prevent jailbreak attacks that bypass safety mechanisms and produce undesirable responses. The authors divide the defense pipeline into two stages: (i) defining unsafe outputs, and (ii) enforcing that definition through fine-tuning and input preprocessing. To investigate the reasons of the defense failures, the authors propose the "Purple Problem" that defines outputs containing keyword "purple" as unsafe.

### Strengths
1. This paper addresses a practical problem by examining the failures of defense mechanisms against jailbreak attacks in LMs.

2. The authors introduced a unique test case, the "Purple Problem", that isolates enforcement failures through a clear and simple definition.

3. The authors conducted a systematic evaluation of multiple defense strategies and provided comprehensive insights.

### Weaknesses
My primary concern is that the problem setting in this paper may not fully capture the complexities of real queries.


1. The authors utilized a synthetic dataset generated through prompt engineering, which may introduce bias and fail to reflect the distribution of real queries. Specifically, the prompts used to generate the dataset might inadvertently create a dataset that is easier or harder to defend against than real-world scenarios. The reliance on a single prompt or a limited set of prompts could lead to a lack of diversity in the generated data, potentially skewing the evaluation results and limiting the generalizability of the findings.

2. The method identifies unsafe content simply by preventing the LMs from generating the word "purple", which may fail to address unsafe contents such as indirect harmful statements or different cases for a same claim. This approach is overly simplistic and does not account for the nuanced ways in which harmful content can be expressed. For instance, a model could generate a harmful statement without using the word "purple" or any direct synonym, thus bypassing the detection mechanism. This limitation undermines the practical relevance of the study.

3. Alignment between training data and queries is important as it will impact the quality of the outputs generated by LLMs. Howver, in this paper, the distribution of the queries for evaluation can differ a lot from real-world queries to AI systems, which undermines the reliability of the evaluation results. The evaluation might not accurately reflect the performance of the defense mechanisms in real-world applications, where the distribution of queries is likely to be significantly different from the synthetic dataset used in this study.

4. Some content can be identified as unsafe under most scenarios but may be safe in some specific contexts. For example, "how to kill xxx" is usually unsafe, but "how to kill a process in Linux" is safe and should produce correct answers. This paper classifies the outputs into "yellow" and "purple". Does the Purple Problem cover such cases? The binary classification of outputs into "yellow" and "purple" fails to capture the contextual nature of safety. The lack of a more nuanced classification system limits the ability to evaluate the defense mechanisms in realistic scenarios where the safety of an output is context-dependent.


5. Though the authors claim something like "The evaluation protocols in (Zou et al., 2023; Jain et al., 2023; Wei et al., 2023b; Robey et al., 2023; Xiong et al., 2024) all consider an output unsafe if it does not contain strings such as "I’m sorry"" in the paper, the case is different. Semantically, "I'm sorry" implies the answer to the query might be harmful or the LLM does not have enough knowledge to answer the question, thus it can be used as a flag for unsafe answers. However, this paper filters unsafe contents by detecting "purple", which lacks such semantic meaning and may not be an effective indicator. The use of "purple" as an indicator of unsafe content lacks semantic grounding and does not align with how safety is typically assessed in real-world applications. The absence of a meaningful connection between the keyword and the concept of safety raises questions about the validity of the evaluation method.

### Questions
see weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper assesses the limits of the defense pipeline from several perspectives, including 
1. The definition mismatch between the defense stage and evaluation stage
2. The robustness against adaptive attacks and increasing compute.
The paper provides a simple case study called "the purple problem", which shows all existing fine-tuning and input defenses fail to enforce the definition under adaptive attacks and increasing computes, highlighting the possible pitfalls of evaluation and the need to prevent a false sense of security.

### Strengths
1. This paper provides a new perspective on inspecting the safety robustness of a defense mechanism: The definition mismatch, which can lead to potential jailbreak and a false sense of security.
2. The paper proposes a simple case study called the "purple problem", which inspects the safety robustness of the defenses when using a perfect definition of "safety"
3. The paper shows how adaptive attacks can easily jailbreak the model, which casts serious doubt on whether post-hoc alignment is sufficient to address real-world safety.

### Weaknesses
1. In line 184, "Such definitions used at evaluation are not the definitions used in enforcement algorithms" does not perfectly hold. Based on the definition of $\mathcal{D}$ and $\mathcal{D^*}$, it is not hard to let $\mathcal{D} = \mathcal{D^*}$, even without considering the "purple problem". For example, we can consider all the answers without "I'm sorry" to be unsafe and use the datasets that all examples contain "I am sorry" to do DPO/PPO on the model. Though I agree there are potential definition mismatches during the training and evaluation process, the wording here should be more conservative and provide more explanation.
2. Another concern from my perspective, is how much the "purple problem" can affect the real performance of the defense mechanism. Several works have provided some representation-based analysis on the model's safety behavior ([Zheng et al., 2024](https://openreview.net/pdf?id=ugxGpOEkox) , [Wei et al., 2024](https://arxiv.org/pdf/2402.05162)). Based on these analyses, there's a possibility that the region/representation that controls the model to response to the safety-related question is different from the region/representation that controls the model to response "purple problem". The author should provide a more detailed analysis to show why "purple" problem can be transferred into the safety problem evaluation"
3.  One of the conclusions of the paper "Scaling compute are important in evaluating defenses." needs to be carefully considered. In fact, any defense cannot succeed if the adversaries have unlimited computing budgets. SB-1047 also requires the model should be safe enough when fine-tuned under a specific number of FLOPS. I would suggest the author rephrase it as "The defense should provide details on the compute budgets allowed for red-teaming, instead of a general claim".
4. The model used in the experiments is a bit outdated. Would be better to include some state-of-the-art model like llama-3 or Gemma-2.
5. In the experiment part (Table 1, Table 2, Table 3), the author does not provide enough details on their evaluation setups. To be more specific, how many repetitions are done for each experiment? Do these experiments use greedy decoding? If not, it would be better to report confidence intervals for all the results.

### Questions
I have listed my questions in the weaknesses part.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the effectiveness of current jailbreaking defenses in LLM using a simplified test case, termed the "Purple Problem." It introduces a minimal definition of unsafe outputs as any response containing the word "purple" to evaluate the robustness of existing defenses. By focusing on this well-defined problem, the paper highlights recent efforts to defense jailbreak. The findings suggest that if defenses cannot succeed in this simple scenario, they may not be robust enough for more complex real-world safety challenges. The authors propose that the "Purple Problem" can serve as a testbed to assess enforcement algorithms.

### Strengths
The paper introduce purple problem a simplified and well-specified test case. This approach offers a clear, focused testbed that allows for fine-grained evaluation of various defense mechanisms at different stages, such as defining unsafe outputs and enforcing those definitions. The simplicity of the purple problem makes it easier for researchers to conduct controlled experiments and assess the effectiveness of fine-tuning and input preprocessing techniques.

### Weaknesses
While the purple problem offers a useful test case, the paper does not fully justify why it is an appropriate stand-in for real-world concerns. Specifically, it fails to explain how the gap between this simplified test case and more complex safety challenges might affect the evaluation of enforcement algorithms. There is no clear argument about whether success or failure in the "Purple Problem" directly correlates with real-world performance. The paper leaves open the question of whether defenses that perform well or poorly in this controlled environment will generalize to more nuanced, high-stakes scenarios, limiting the practical applicability of its findings.

The author claims that the "Purple Problem is meant to be an easier version of any complex safety challenge," presenting this as the main assertion of the paper. However, I find this to be an overstatement.

First, how do the authors define "easier"? How is the difficulty of two problems compared? A common approach might involve demonstrating that the "Purple Problem" is a subset of any given safety challenge, yet the authors do not provide clear proof of this. For instance, if the safety challenge involves preventing a large language model (LLM) from producing insecure code, it is unclear how the "Purple Problem" could be considered a subset of such a challenge.

Second, if the authors hypothesize a correlation—such as "a defense that fails to address the Purple Problem may also fail in more complex scenarios"—they need to provide empirical evidence to support this claim. For example, they could evaluate whether a model with a high jailbreak rate in the "Purple Problem" also exhibits a high jailbreak rate in more complex challenges.

### Questions
1. What specific limitations in current enforcement methods are revealed by the failure in the purple problem?
2. Why was purple chosen as the unsafe output, and how does this choice affect the evaluation of defenses?

### Soundness
2

### Presentation
2

### Contribution
2
