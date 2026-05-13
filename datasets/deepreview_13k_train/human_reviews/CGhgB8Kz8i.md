# Innovative Thinking, Infinite Humor: Humor Research of Large Language Models through Structured Thought Leaps

- Decision: Accept
- Scores: 6, 3, 6, 5

## Abstract
Humor is a culturally nuanced aspect of human language that presents challenges for understanding and generation, requiring participants to possess good creativity and strong associative thinking. Similar to reasoning tasks like solving math problems, humor generation requires continuous reflection and revision to foster creative thinking, rather than relying on a sudden flash of inspiration like Creative Leap-of-Thought (CLoT) paradigm.
Although GPT-o1 can realize the ability of remote association generation, this paradigm fails to generate humor content. 
Therefore, in this paper, we propose a systematic way of thinking about generating humor and based on it, we built Creative Leap of Structured Thought (CLoST) frame. First, a reward model is necessary achieve the purpose of being able to correct errors, since there is currently no expert model of humor and a usable rule to determine whether a piece of content is humorous. Judgement-oriented instructions are designed to improve the capability of a model, and we also propose an open-domain instruction evolutionary method to fully unleash the potential. Then, through reinforcement learning, the model learns to hone its rationales of the thought chain and refine the strategies it uses. Thus, it learns to recognize and correct its mistakes, and finally generate the most humorous and creative answer.
These findings deepen our understanding of the creative capabilities of LLMs and provide ways to enhance LLMs' creative abilities for cross-domain innovative applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the Creative Leap of Structured Thought (CLoST) framework, which enhances large language models' ability to generate and recognize humor through structured thinking and self-improvement. CLoST introduces a two-stage approach: first, using Associative Automatic Instruction Evolution (AAIE) to diversify and refine humor judgment through complex instructions, and second, employing Guided Explorative Self-Improvement Tuning (GESIT) to strengthen logical reasoning and humor understanding via reinforcement learning. CLoST improves humor judgment and creativity across multiple language benchmarks.

### Strengths
- The paper presents the CLoST framework, a novel methodology for generating humor in LLMs. This structured approach integrates knowledge graphs and causal inference, which helps reinforce logical connections between seemingly unrelated concepts, thus facilitating more coherent humor generation. Notably, the research delves deeply into data augmentation techniques, enhancing the model’s ability to generate diverse and contextually relevant humorous responses.
- The authors conduct extensive testing of CLoST across multiple humor benchmarks. These experiments demonstrate that CLoST consistently outperforms existing humor generation models in terms of accuracy and robustness. The model’s performance improvements are particularly pronounced in both English and Chinese language settings.

### Weaknesses
 - The inherent subjectivity of humor presents a major challenge. The current approach seems to emphasize pattern recognition, where the model identifies humor based on learned patterns rather than genuinely understanding or reasoning through the humor's intricacies. The empirical results, especially on hard humor tasks, underscore this shortcoming.

- The Associative Automatic Instruction Evolution (AAIE) method employs a multi-agent system—comprising a rewriter, imaginator, and analyst—to iteratively evolve instructions. While this approach is novel and showcases creative engineering, it introduces considerable computational overhead. More critically, the ablation study results suggest that the added complexity yields only marginal improvements in performance. Specifically, CLoST shows gains in four out of seven tasks, and even these are not substantial enough to justify the extensive computational resources required.

### Questions
1. Is the inclusion of AAIE necessary? The performance improvement does not seem substantial, as shown in Table 3. It would be beneficial to highlight the best-performing models in the table and provide a detailed analysis of possible reasons.
2. The paper mentions that the dataset includes varying difficulty levels. Is this variation primarily reflected in the choice options, such as 2-out-of-1 or 4-out-of-1 selections? It would be helpful to include a more in-depth analysis of how these different difficulty levels affect model performance.
3. There are minor issues, such as the use of incorrect quotation marks in LaTeX. Additionally, providing more details on experimental parameters, like the temperature setting used, would enhance the clarity and reproducibility of the experiments.

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
4

### Summary
This paper introduces  the Creative Leap of Structured Thought (CLoST) framework, aiming to improve the humor understanding capabilities of LLMs. It consists of two stages: Associative Automatic Instruction Evolution (AAIE) and Guided Exploratory Self-Improvement Tuning (GESIT). In AAIE, human-designed instructions and automated instruction evolution help the model develop humor understanding capabilities. In GESIT, the model’s humor generation is improved using bootstrap Direct Preference Optimization (DPO) training. By learning from expert-provided joke rationales and AAIE-trained judgment skills, the model iteratively refines its humorous responses through guided reasoning.

### Strengths
This paper introduces  the Creative Leap of Structured Thought (CLoST) framework, aiming to improve the humor understanding capabilities of LLMs. It consists of two stages: Associative Automatic Instruction Evolution (AAIE) and Guided Exploratory Self-Improvement Tuning (GESIT).

### Weaknesses
1. This paper is very difficult to read and understand. Comes with a seemingly fancy title and introductory paragraphs not closely related with the goal.

It claims "humor generative abilities" in the intro and the teaser figure, half of the method is for improving humor judgement ability and the second half is developed for improving generation abilities. But the test tasks are multiple choice questions of SemEval (humor classification/discrimination) and has nothing to do with generation.

The motivation and method contains lots of unclear expressions. CLoT, the method that it is based on, is not explained clearly. As a reader I am so confused with this paper that I have to rely on AI to help me understand this paper better. Even the figure is confusing. For example in Figure 1, how come that a response by CLoST "Job? No No?" is more humorous and interesting than more informative ones such as "Of course not! If you are satisfied with your job, you're already one step ahead of the person who invented the snooze button" by GPT-4o?

2. The authors seems to lack sufficient background knowledge of NLP&humor basic concepts and existing works. Multiple-choice questions is not a faithful title/motivation to "humor generation abilities".

3. Experiments: The compared baselines are zero-shot LLMs such as GPT, QWEN, etc. The only prior work being compared is CLoT which is not discussed in detail and lacks any ablation of the introduced components.

### Questions
/

### Soundness
2

### Presentation
1

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
This paper introduces CLoST (Creative Leap of Structured Thought), a novel framework for enhancing humor generation and understanding in large language models (LLMs). The work builds upon the Creative Leap-of-Thought paradigm with two key innovations:
1.Automatic Associative Instruction Evolution (AAIE): A multi-agent system for evolving complex instruction sets
2.Guided Exploratory Self-Improvement Tuning (GESIT): A preference optimization approach incorporating causal reasoning
The paper demonstrates improved performance on both Chinese and English humor benchmarks, including SemEval tasks and Oogiri-GO dataset. The framework shows particular strength in handling complex humor discrimination tasks and generating creative responses.

### Strengths
1.The paper proposes a novel integration of structured reasoning with creative creation.
2.The paper proposes an innovative multi-agent instruction evolving system and incorporates the causal inference to humor understanding.
3.The proposed two stage approach shows clear performance improvement through comprehensive empirical evaluation across multiple datasets and languages.

### Weaknesses
1.The experimental validation lack of human evaluation for generated humor quality.
2.The three-agent system is not well motivated and can be better presented with motivation, clear example and details.
3.Better exploration and analysis of failure cases

### Questions
1.The Associative Automatic Instruction Evolution part is a bit hard to understand and can be presented with a short and clear example to go through. It’s confused to interpret the symbols.
2.For the AAIE process, what’s the output data format used to train a lora model?
3.For the guided explorative self-improvement tuning, why do we need r+ and r-? do we use them in the fine-tuning?
4.In Table 1, it’s suprised to see gpt 4o performs worse than Llama3 on SemEval 2020 and Oogiri-GO.
5.How stable is the three-agent system? Are there cases where it fails to converge?

### Soundness
4

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
The paper introduces a framework called Creative Leap of Structured Thought (CLoST) to reinforce humor generation in LLMs. Building upon the limitations of the CLoT paradigm, the authors propose a systematic method inspired by KGs and causal relationships. The framework consists of two stages: Associative Automatic Instruction Evolution (AAIE) and Guided Explorative Self-Improvement Tuning (GESIT). In the first, the model is trained with human-designed instructions to improve its humor-judgement capabilities. In GESIT, the model refines its ability to generate humorous responses through RL, learning from both an expert model and its own judgements. Experiments conducted on English and Chinese humor datasets seemingly demonstrate that CLoST outperforms existing models in humor discrimination and enhances the model's divergent thinking abilities.

### Strengths
The paper addresses humor generation, a task that is famously challenging, introducing a framework that uses causal relationships to model associations between concepts. Furthermore, a two-stage training process is a good approach, separating the judgement part from the generation part in LLMs.

### Weaknesses
Firstly, the paper lacks clarity in several sections, making it difficult to fully comprehend the proposed methods. For instance, the mathematical formulation in S2.1 seems disconnected from the rest of the paper, and is not well-explained. Secondly, there is insufficient detail about the datasets used, especially the "in-house data". The lack of information about data sources and availability (and code!) raises concerns about the reproducibility of the experiments. Then, the evaluation metrics and experimental setup are not discussed enough. It is unclear in my mind how the multiple-choice questions are constructed and whether the comparisons with baseline models are fair (e.g., are other models trained on the same datasets? If not, than it's a problem).
I will state here, since it's a problem of many papers in this field: the reliance on GPT-4o as an expert model is problematic, as it is a proprietary system. This raises issues regarding the accessibility and reproducibility of your method. Proprietary system's backends change with time and without alerting the users: they are not fit for experiments that need to keep reproducibility to the forefront.
Furthermore, let humans evaluate the generated humor. A good sample of annotators evaluating whether the produced content it is "funny" or not would be a better fit and a real contribution to the field.
Finally, the paper does not address ethical considerations related to HG, such as avoiding offensive or culturally insensitive content.

### Questions
- Can you provide more information about the "in-house data" used for training and testing? What are its sources, and is it possible to make this data publicly available to ensure reproducibility?
- How are the multiple-choice questions in the evaluation constructed? Are they standardized across all models, and how do you control for randomness in the selection of options?

### Soundness
2

### Presentation
2

### Contribution
2
