# Visual Large Language Models Exhibit Human-Level Cognitive Flexibility

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
Cognitive flexibility has been extensively studied in human cognition but remains relatively unexplored in the context of Visual Large Language Models (VLLMs). This study assesses the cognitive flexibility of state-of-the-art VLLMs (GPT-4o, Gemini-1.5 Pro, and Claude-3.5 Sonnet) using the Wisconsin Card Sorting Test (WCST), a classic measure of set-shifting ability. Our results reveal that VLLMs achieve or surpass human-level set-shifting capabilities under chain-of-thought prompting with text-based inputs. However, their abilities are highly influenced by both input modality and prompting strategy. In addition, we find that through role-playing, VLLMs can simulate various functional deficits aligned with  patients having impairments in cognitive flexibility, suggesting that VLLMs may possess a cognitive architecture, at least regarding the ability of set-shifting, similar to the brain. This study reveals the fact that VLLMs have already approached the human level on a key component underlying our higher cognition, and highlights the potential to use them to emulate complex brain processes.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This article studies the cognitive flexibility of three multimodal large language models—Gemini, ChatGPT, and Claude—that support both text and image input using the WCST test. Cognitive flexibility here refers to the models' ability to adjust their understanding of task rules and complete tasks correctly based solely on feedback indicating correctness or incorrectness. The experiment includes SaT-VI, SaT-TI, CoT-VI, and CoT-TI conditions, where SaT means no chain-of-thought guidance and the model outputs answers directly, while CoT involves chain-of-thought guidance. The results show that CoT significantly outperforms SaT, achieving or surpassing human-level performance.

### Strengths
1.This study uses the WCST to examine the cognitive flexibility of VLLMs. The WCST is widely applied in cognitive science and is known for its strong reliability.2.The authors explored the potential of VLLMs to simulate specific patterns of cognitive impairment through role-playing.

### Weaknesses
1.Although the article mentions that the simulated patterns of the models align with real cases, the authors did not conduct cognitive experiments or correlate data with real subjects to demonstrate that VLLMs' simulation of cognitive impairment is reasonable.
2.The article only evaluates the models on a specific cognitive test (WCST). While the WCST is a classic test in cognitive science, it lacks real-world simulation, and performance on this test cannot fully represent performance in real-world scenarios.
3.The authors should consider incorporating more visualizations.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work aims to evaluate the cognitive flexibility of vision language models (VLMs), using a classic task from the neuropsychological literature (the Wisconsin Card Sort Task). The authors conclude that, under certain conditions (depending on input modality and prompting technique), VLMs can display human-level flexibility. Experiments are also reported in which prompting is used to simulate neuropsychological impairment.

### Strengths
- This work employs a well validated task from the neuropsychological literature, potentially enabling a rich comparison with human cognition.
- The experiments investigate several state-of-the-art VLMs, increasing the robustness of the findings.

### Weaknesses
 - Most importantly, the results are not diagnostic regarding the relative cognitive flexibility of VLMs/LLMs and humans. This is because the human participants are effectively at ceiling. In order to have a meaningful comparison, a version of the task (or a different task) would need to be identified where human performance was not at ceiling. The authors should consider using a more difficult version of the WCST, perhaps by increasing the number of categories or introducing more complex rule-switching patterns, or by using a different task altogether. A more nuanced approach to measuring cognitive flexibility is needed to differentiate between human and machine performance.
- No theoretical motivation is provided for investigating cognitive flexibility in LLMs / VLMs. It is noted that this is a well studied task in the neuropsychology literature, which is true, but this does not automatically yield theoretically important questions about LLMs / VLMs. It is also suggested that 'This investigation not only advances our understanding of VLLMs but also offers insights into the nature of cognitive flexibility itself,' but it is not clear what insights this work offers about cognitive flexibility. The authors need to articulate a clear theoretical framework that justifies the investigation of cognitive flexibility in these models, and explain how the results contribute to our understanding of both artificial and natural intelligence.
- There is also no explicit motivation for studying VLMs in particular, as opposed to LLMs. Is there any particular reason why it is important to study these processes in the visual domain? The authors should justify the use of visual inputs, and explain how the visual modality contributes to the study of cognitive flexibility, rather than simply using it as a convenient way to present the WCST. They should also consider the possibility that the visual processing capabilities of VLMs might confound the results.
- The paper only includes experiments with a single task. Many more tasks and conditions would be needed to support the claims that are advanced in this paper. The authors should include other tasks that measure cognitive flexibility, such as the Dimensional Change Card Sort (DCCS) or the Intra-dimensional/Extra-dimensional Set Shift (IED) task, to assess the generalizability of their findings. They should also explore different task parameters within the WCST to test the robustness of the models' performance.
- For tests of large-scale pretrained models such as LLMs and VLMs, it is also important to try and ensure that the tasks used for evaluation are not present in the model's training data. This is a concern here given the popularity of this task in the cognitive literature. One possible approach might be to also test an equivalent version of the task that uses different surface features, to ensure that performance does not depend on memorization (or pseudo-memorization). The authors should provide evidence that the models are not simply memorizing solutions from their training data, perhaps by using novel stimuli or by manipulating the task in ways that would be difficult to memorize.
- There are no statistical tests provided throughout the entire paper, although there are many statements about the differences between certain conditions. It is important to perform statistical tests to determine which of these differences are reliable. The authors must include appropriate statistical analyses, such as ANOVAs or t-tests, to support their claims about the significance of their findings. They should also report effect sizes to quantify the magnitude of the observed differences.
- It is unclear what's learned from the experiments simulating neuropsychological impairment. There are some assertions about similarities to the pattern of behavior in certain patient populations, but very few references, and no direct comparison with human behavior. It would be ideal to have a direct comparison with behavior to support such claims. The authors should provide a more detailed analysis of the simulated impairments, including direct comparisons with human patient data, and cite relevant literature to support their claims about the similarities between model behavior and human neuropsychological deficits.

### Questions
### Questions
- What is the theoretical motivation for studying cognitive flexibility in VLMs / LLMs?
- What is the theoretical motivation for studying cognitive flexibility in VLMs in particular? What does the visual domain add to such an evaluation?

### Suggestions
- The task should be modified so as to identify conditions where human performance is not at ceiling.
- More tasks should be investigated. 
- Statistical tests should be included to support comparisons.
- A direct comparison with human behavior should be included for the experiments simulating neuropsychological impairment.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper "Visual Large Language Models Exhibit Human-Level Cognitive Flexibility" evaluates the cognitive flexibility of state-of-the-art VLLMs (GPT-4o, Gemini-1.5 Pro, and Claude-3.5 Sonnet) using the Wisconsin Card Sorting Test (WCST). It finds that VLLMs can match/surpass human performance in adapting to changing rules, especially with chain-of-thought reasoning and text-based inputs.

Key contributions:
1. VLLMs demonstrate human-level cognitive flexibility, particularly with CoT prompting.
2. Performance significantly changes based on input  modality (text vs. visual) and prompting strategy.
4. VLLMs can simulate cognitive impairments, offering potential for modeling brain function.

The study suggests that VLLMs has some cognitive abilities and points to potential in advanced applications in AI and neuroscience.

### Strengths
Experiment methodology: The paper is methodically thorough, using a well-established cognitive flexibility test WCST and evaluating SOTA VLLMs.. The experimental design includes 4 different setups and 6 scoring functions. This enables a detailed comparison under varied conditions, providing some level of robustness to the findings. Including human participants as a comparative baseline grounds the findings in a relatable context.

Clarity: The paper is easy to follow and well-organized, with a clear explanation of the WCST, input modalities, and experimental conditions. The results are presented in detailed tables and figures, aiding in the understanding of model performance comparisons

Originality: The paper explores an area by applying well known congnitive test to assess performance  in VLLMs. It introduces a unique approach by examining how these models simulate cognitive impairments, adding some level of depth and innovation to the study.

### Weaknesses
Overstatement of Cognitive Flexibility Claims: Although the paper demonstrates that VLLMs can achieve human-level performance in the WCST under specific conditions, the claim that they exhibit human-like cognitive flexibility seems overstated. Cognitive flexibility in humans involves a broader spectrum of real-world applications and examined using multiple tests, and the findings are limited to a highly structured test. A more cautious interpretation of the results would strengthen the paper's scientific rigor.

Role-playing Cognitive Impairments Needs Validation: While simulating cognitive impairments through role-playing prompts is innovative, this method remains speculative without validation against clinical populations. The paper could improve by discussing potential methods for validating these simulated impairments against real-world data, making the findings more actionable and grounded in reality.

Insufficient Validation of Prompt Designs: While the paper employs CoT and STA prompting strategies, it does not fully explore the impact of different prompting setups or attempt to validate the prompts across varied task conditions and models. For example, the reliance on CoT prompting for achieving high performance raises questions about how much of the cognitive flexibility observed in VLLMs is genuinely attributable to their internal architecture versus the external aid provided by sophisticated prompts (which for some of the models are not advertised as the suggested approach).

### Questions
1. While the paper demonstrates that VLLMs can achieve human-level performance in the WCST, the broader claim of human-like cognitive flexibility seems to require more context. Could the authors clarify how they see the findings generalizing to real-world applications? Specifically, how do the authors view the limitations of the WCST in capturing the full spectrum of cognitive flexibility in humans, and do they plan to evaluate VLLMs using additional tests that capture a wider range of flexibility?

2. The paper heavily relies on a specific cot prompting approach to achieve high performance. Could the authors provide more details about how different prompting strategies and setups affect the models' performance across tasks? Specifically, does prompt wording changes the performance significantly? 

3. The paper evaluates three SOTA models. How do the authors envision their findings generalizing to other models (includingn on VLLMs), especially those with different architectures or less advanced capabilities? Are there plans to extend the study to a broader range of models or to compare different architectural approaches to cognitive flexibility? 

4. Cognitive flexibility in real-world settings often involves adapting to highly dynamic environments where rules are unclear and change rapidly. Do the authors have plans to test the models in more dynamic, less structured tasks where adaptability is required in real time?

### Soundness
2

### Presentation
3

### Contribution
2
