# Too Big to Fool: Resisting Deception in Language Models

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Large language models must balance their weight-encoded knowledge with in-context information from prompts to generate accurate responses. This paper investigates this interplay by analyzing how models of varying capacities within the same family handle intentionally misleading in-context information. Our experiments demonstrate that larger models exhibit higher resilience to deceptive prompts, showcasing an advanced ability to interpret and integrate prompt information with their internal knowledge. Furthermore, we find that larger models outperform smaller ones in following legitimate instructions, indicating that their resilience is not due to disregarding in-context information. We also show that this phenomenon is likely not a result of memorization but stems from the models' ability to better leverage implicit task-relevant information from the prompt alongside their internally stored knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates whether larger LLMs are more robust to misleading cues in prompts. Experiments across various models and benchmarks show that larger models exhibit smaller relative accuracy drops, demonstrating better resilience to deception in prompt. To eliminate the alternative hypothesis that the larger model ignores the appended misleading cues, additional tests were conducted: one added direct cues to the correct answer, and another instructed the model to avoid the correct answer. Both confirmed that resilience is not due to cue ignorance. Furthermore, in question-removal experiments on MMLU,  the non-trivial accuracy (>>25%) for both overfitted and non-MMLU-trained models reveals that LLMs possess advanced data processing capability (i.e, fill in the missing details) beyond memorization. This possibly explains why LLMs can be resilient to misleading cues.

### Strengths
1. The paper provides valuable insights into the scaling effects on model resilience to misleading prompts, complementing existing LLM scaling studies.

2. The paper is well-organized and clearly written.

3. The main and additional experiments thoroughly validate the central hypothesis.

### Weaknesses
1. **Marginal Contribution**: Compared with previous works investigating LLM vulnerability to prompt manipulation, as explained in Section 2, it seems the most significant difference lies in the sole focus on parameter scaling effects, specifically 2B-70B models.  It is expected that larger models, benefiting from refined training, demonstrate improved knowledge retention, instruction following, and in-context learning, following the emergent abilities analysis [1]. While the scaling investigation on LLM resilience to prompt deception is thorough, the insights presented do not significantly advance the current understanding, especially considering similar works (e.g., [2]) have conducted experiments across multi-sized models. The claim that this is the first work to empirically demonstrate the scaling effect is not sufficiently justified, as the performance of earlier models on these benchmarks may have been too low to observe the effect, but this does not negate the existence of prior work on scaling effects in general. The core contribution appears to be limited to observing this effect on newer models, which is not a substantial advancement given the existing literature on scaling and robustness.

2. **Potential Overclaim Regarding "World Models"**: Throughout the paper, the authors repeatedly use the term "internal world model (of an LLM)", but as the author may notice in related work discussions, the "World Models" concept is only vaguely defined (and never formally defined in this paper), and whether LLM possesses "World Model" is still under debate, not to mention its "robustness". It is confusing to prove the robustness of loosely-defined concepts. The experiments and findings would remain valid without drawing connections to "world models," making this connection appear unnecessary and potentially misleading.

3. **Results for main experiments are not thoroughly analyzed**: Although the study evaluates models and datasets extensively, it lacks in-depth dataset-wise and model-wise analysis. For example, it seems the dataset collection being evaluated is unbalanced -- some datasets have fewer answer choices or much fewer instances than others. This requires further justification for inclusion and dedicated analysis of experiment results. Also, when reporting average performance in Figures 2 and 3, it is not clear how the authors balance the results across datasets considering the imbalanced datasets, and the decreasing/increasing trend on some datasets (thin lines) looks not that significant or inconsistent with the average trend. In Appendix B and C, the inconsistency is better demonstrated (e.g., in MathQA) and there are no related discussions.  Additionally, the grouping of models with differing architectures (e.g., Mistral-7B-Instruct vs. Mixtral-8×22B-Instruct) complicates the analysis of scaling effects. The distinct behavior of Gemma-series models is noted but not adequately explored.

4. **Confusing Analysis on Memorization Experiments**: The authors interpret the above-chance-level performance as "LLMs can leverage their world models to fill in missing information" as the main conclusion for this section. However, this is not convincing, because above-chance performance does not necessarily imply human-like reasoning (i.e., "fill in missing information first and then answer"), especially given potential selection biases in multiple-choice questions [2]. The weak chance-level baseline further undermines this claim. Second, the discussion admits the challenge of isolating memorization but nonetheless asserts the presence of a robust inference capability, which is unconvincing. Moreover, the focus on "smaller models" (7B-level) in this section is inadequate given the paper's emphasis on scaling. The definition of "memorization effects" also appears to be overly narrow, failing to consider more nuanced forms of knowledge recall, such as paraphrased content or related factual knowledge from training data.

### Questions
1. How do you obtain averaged relative accuracy drops across datasets? In particular, how do you deal with imbalanced datasets (e.g., GPQA only has 448 samples while MathQA has 37.2K samples)

2. What is the interpretation of inconsistent accuracy drop change trends in individual datasets (e.g., MathQA)?

3. How do you draw the conclusion that the model's ability to infer missing details "is not simply a byproduct of memorization" based on experiment results in Section 4.3? How does this result extrapolate to larger models as the scaling effect is the main evaluation dimension of this paper?

### Soundness
3

### Presentation
3

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
The paper has conducted thorough experimentation on LLMs deception behaviour. Authors also have compared the deception and comparison with smaller and larger language models.

### Strengths
1) The paper provides comparison of the deception from smaller language models to large language models.

2) The idea of providing misleading information to the LLMs and testing their behaviour is interesting.

3) The paper presents wide range of ideas or possibilities with the deception and have presented the analysis which is quite interesting.

4) The datasets cover wide range of domains like maths, science and other questions as well.

### Weaknesses
1) The authors have used multi choice question type for the deception analysis they would have used question answering datasets where input is text and output is also a text but not multi choice. 

2) The experimentation and prompting looks really not so suitable. If you are prompting incorrect answer as an hint and using it to answer the correct option would not be the right way of prompting. Instead you can prompt the process like "refrigerator does not conduct electricity or does not contain iron." instead of directly prompting "The correct answer is A.". Always remember the LLMs provide the answer by reasoning if you really want to check deception instead of saying about the answer you have to misinform the process or thinking.

3) Everyone knows Larger models have lesser deception because they understand better and not only that if your LLM has the ability to think or if any prompting technique is used the deception automatically decreases. O1 is less deceptive compared to others because the model has the ability to think.

4) The section 4.2 is not really an important section in my opinion. I do not think any LLM will ignore the text. They are machines and always take every input given by the humans for the better response. 

5) In the experimentation GPT Models are absent which are really important models. Also the authors should implement O1 as well. if O1 seems to be not affordable they must at least implement GPT-4o or GPT-3.5.

### Questions
1) Why a question answering dataset which is not multi choice is implemented?

2) Why the latest models like GPT models are not implemented? They are the most popular and most of the readers would like to see their performance.

3) You have prompted the incorrect answer as hint instead of the thinking process. Why not prompting the incorrect thoughts or incorrect way of solving it?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores the resilience of LLMs to deceptive in-context information, focusing on how models of different sizes respond to misleading prompts. The study uses multiple-choice benchmarks to compare model behavior, concluding that larger models show greater robustness against such deceptive inputs. The authors assert that this resilience is not merely due to ignoring in-context information or memorization but stems from the models' ability to integrate information with their internal "world models."

### Strengths
- The study addresses a pertinent issue in the deployment of LLMs—robustness against misleading or deceptive information. With the increasing use of LLMs across various applications, understanding their behavior in such scenarios is essential for ensuring reliability and safety, highlighting the relevance and timeliness of the study.
- The authors present a clear and structured evaluation framework. By leveraging controlled experiments and multiple-choice benchmarks, they systematically analyze model behavior under different conditions, such as deception, guidance, and directive instructions. This rigorous approach enables consistent comparisons across models of varying scales and architectures, drawing attention to the core issue of robustness against deception.

### Weaknesses
 - Insufficient Exploration of Underlying Mechanisms:
The assertion that larger models possess more robust "world models" is a plausible hypothesis but remains inadequately supported by the experiments presented. While the control tests (e.g., context removal, directive instructions) attempt to eliminate explanations like memorization, they do not sufficiently clarify how models integrate conflicting information. To substantiate claims about the mechanisms underlying resilience, more detailed analyses, such as probing internal representations or employing causal interventions, are needed. Specifically, the study lacks analysis of attention patterns, which could reveal how models weigh deceptive information against their pre-existing knowledge. Furthermore, the authors do not explore the impact of different types of deceptive information, such as logical fallacies versus factual inaccuracies, on the models' internal states.

- Limited Scope and Generalizability:
Although the methodology is sound, the study's reliance on multiple-choice benchmarks constrains its scope. Controlled settings like these do not adequately reflect the complexity of real-world scenarios, where deceptive prompts are often subtler and more nuanced. This limitation undermines the generalizability of the findings, restricting their applicability beyond the specific benchmark tasks used in the study. Addressing such limitations by incorporating open-ended tasks or more diverse datasets would improve the practical relevance of the results. The exclusive focus on instruction-tuned models introduces potential biases, as the findings may not generalize to other model types, such as generative LLMs. A more comprehensive evaluation that includes models not optimized for following instructions would provide a better understanding of how scale impacts resilience across different architectures and training paradigms. The study also does not consider the impact of different prompt engineering techniques on the models' susceptibility to deception. For instance, the use of chain-of-thought prompting might alter how models process and integrate deceptive information.

- The authors examine robustness to deceptive information in relation to parameter scaling, but only present two models per family. While this approach is understandable, a more comprehensive study would be valuable to strengthen the findings. The limited number of models makes it difficult to draw definitive conclusions about the relationship between model size and resilience. A more granular analysis, including models of intermediate sizes, would be necessary to establish a clear trend.

### Questions
- At Line 414, the authors suggest that if a model has memorized associations between answers and questions, it might still achieve high accuracy even without the question. However, this claim is not backed by any citations or experimental evidence. Furthermore, the discussion around memorization in Lines 426-429 lacks clarity. The authors argue that if memorization were the primary factor, the "contaminated" model would maintain high accuracy even without the question, while the DCLM-7B model would perform at chance level. However, there is no verification of whether the Llama model is contaminated, making this comparison problematic. Additionally, terms like "reasoning" and "memorization" are not well-defined, which undermines the validity of the claims.

- While the study demonstrates that larger LLMs are more resilient to deceptive in-context information, it fails to adequately explain the underlying reasons. The claim that larger models can "effectively reconcile conflicting information” is not convincingly proven, as the experiments do not provide deeper insights into the mechanisms that facilitate this behavior.

### Soundness
2

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
The paper investigates how LLM inference is influenced by information that is provided in-context when this information contradicts or supports the LLMs internal world model. The authors hypothesize that larger LLMs will be more robust to misleading in-context information. They conduct experiments by altering prompts from existing benchmarks to include hints or misleading information and measure how this affects the performance of models of varying sizes. The result supports the authors' hypothesis. They also conduct a number of control experiments to rule out alternative explanations, such as that larger models ignore in-context information or simply memorize correct results from their training data.

In the context of multiple-choice question answering benchmarks, the authors convincingly demonstrate their claim with thorough control experiments. However, I feel that their results are limited by only considering this setting and that it is unclear how well the results would generalize to more realistic applications of LMs. For this reason, I weakly lean towards rejecting the paper but am willing to change my score if this concern is addressed.

### Strengths
- The paper includes well thought-out control experiments that rule-out alternative explanations for the main results. I found the results on memorization particularly interesting.
- Experiments are conducted on multiple families of LMs and on a large number of question-answering benchmarks.
- The paper is well-written and easy to follow.

### Weaknesses
### Limited experimental setting.
In my opinion, the paper's main weakness is that the experimental setting is limited and not very realistic. Therefore it is unclear how universal their results are. The paper only considers multiple-choice question answering benchmarks. Prompts are made to be "deceptive" by simply adding text that claims a wrong answer is correct, which is not very realistic. 

The results could be made more convincing by considering a broader experimental setting. For example, the paper could conduct similar experiments on math or coding benchmarks. This is my main concern and if it were addressed I would raise my score.

### It is questionable if the evaluation method is a novel contribution.
In the introduction, the paper claims that their methodology of applying small changes to task definitions is a novel contribution. This is questionable, as several previous works, including some of the papers cited on lines 99 and 100, evaluate the robustness of model answers under perturbations. To me it seems like a stretch by the authors to claim that they have introduced a new methodology by adding specific sentences to prompts from existing benchmarks.

Considering comments by other reviewers, I agree that there is too much vagueness in the discussion of world models and memorization. For memorization, I think the results mainly concern contamination of the training data in the sense of benchmark data that was exactly present in the training data. However, the author's propose that they build on Hartmann et al's definition which "extends beyond exact recall to include abstract facts present in a small subset of documents". Firstly, I do not understand what exactly the authors mean with this, as Hartmann et al describe multiple types of memorization for different types of information. Regardless, I do not think the experiments support claims about any type of memorization except exact data contamination (memorization of verbatim text according to Harmann et al).
- Regarding world models, the results provide evidence for the greater robustness of larger models in the sense that the models maintain their accuracy in spite of conflicting information. However, I do not see how this is evidence for a "compact, coherent, and interpretable" world model as opposed to sophisticated pattern matching. The experiments are conducted on instruct models which are trained to be helpful assistants. It may well be that they are trained to answer correctly even on questions or instructions that contain some conflicting or false information. In this case, it seems plausible that the higher robustness of larger models is simply the product of better pattern matching, "without forming a coherent or interpretable understanding of the data generation process".

### Questions
- Have you considered different settings from multiple-choice question answering? If not, why not?

- How do your results on memorization relate to the existing literature on memorization in LLMs and data contamination in evaluations? It would be good if this was mentioned in the background section.

### Soundness
3

### Presentation
3

### Contribution
2
