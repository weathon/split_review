# Program Synthesis Benchmark for Visual Programming in XLogoOnline Environment

- Decision: Reject
- Avg Score: 5.80
- Scores: 5, 5, 3, 8, 8

## Abstract
Large language and multimodal models have shown remarkable successes on various benchmarks focused on specific skills such as general-purpose programming, natural language understanding, math word problem-solving, and visual question answering. However, it is unclear how well these models perform on tasks that require a combination of these skills. In this paper, we curate a novel program synthesis benchmark based on the XLogoOnline visual programming environment. The benchmark comprises $85$ real-world tasks from the Mini-level of the XLogoOnline environment, each requiring a combination of different skills such as spatial planning, basic programming, and logical reasoning. Our evaluation shows that current state-of-the-art models like GPT-4V and Llama3-70B struggle to solve these tasks, achieving only $20$\% and $2.35$\% success rates. Next, we develop a fine-tuning pipeline to boost the performance of models by leveraging a large-scale synthetic training dataset with over $80,000$ tasks. Moreover, we showcase how emulator-driven feedback can be used to design a curriculum over training data distribution. We showcase that a fine-tuned Llama3-8B drastically outperforms GPT-4V and Llama3-70B models, and provide an in-depth analysis of the models' expertise across different skill dimensions. We will publicly release the benchmark for future research on program synthesis in visual programming.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper
1. curates a small (85 tasks) program synthesis benchmark based on real-world tasks in the XLogoOnline visual programming environment, which requires a combination of different skills;
2. shows that current SotA models like GPT-4V and Llama3-70B struggle to solve such tasks;
3. develops a data synthesis pipeline with curriculum learning based on task difficulty for the model to significantly boost the model performance on the benchmark.

### Strengths
1. This paper identifies a new task that current SotA models fail on.

### Weaknesses
1. This paper provides few new insights about identifying models' limitations: This paper shows that existing models fail in visual programming in XLogoOnline. But this task is similar to some tasks in works like MMMU, which also combine different skills like vision and reasoning and have already shown that current models struggle in visual reasoning tasks
2. This paper also lacks novelty about improving models' performance:
    1. The data synthesis method is based on sampling and filtration, which has been widely adopted in works like STaR, RaFT and Rest-EM.
    2. The curriculum learning design adaptive to task difficulty has been explored by works like DART-Math.

### Questions
1. To the best of my knowledge, OpenAI has never disclosed the parameter sizes of their models since GPT-3.5. Where is the statement of "GPT3.5 model with 175B parameters (version gpt-3.5-turbo-0125)" (line 335-336) from?
2. Which version of Llama3 models are used? 3 or 3.1?

### Soundness
3

### Presentation
4

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
The paper introduces a new benchmark, which is designed to evaluate the performance of large language models on program synthesis tasks within the XLogoOnline visual programming environment. The benchmark includes real-world and synthetic tasks that require a combination of skills such as spatial planning, basic programming, and logical reasoning. The study found that current state-of-the-art models like GPT-4V and Llama3-70B struggle with these tasks, achieving low success rates. To improve model performance, the authors developed a fine-tuning pipeline using a large-scale synthetic training dataset, which significantly boosted the performance of the Llama3-8B model. Additionally, they showcased how emulator-driven feedback can be used to design a curriculum over training data distribution, further enhancing the performance of fine-tuned models. The paper provides an in-depth failure analysis to understand model limitations and will publicly release the benchmark for future research on program synthesis in visual programming.

### Strengths
It introduces XLOGOMINIPROG, a new benchmark that tests multiskill tasks in visual programming, an area where current models perform poorly.
It demonstrates the effectiveness of emulator-driven feedback for designing a dynamic training curriculum, further boosting model performance.
Detailed experiments were carried out

### Weaknesses
The emulator-driven fine-tuning provides only binary correctness feedback on the predicted code, which might not be sufficient for identifying and correcting specific errors in the generated code. Can it be in natural language?

There's a risk that models could overfit to the synthetic data used in training, which might not perfectly mimic the complexity and variability of real-world programming challenges. I think this is the most serious disadvantage

### Questions
no questions

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a novel benchmark for evaluating the performance of large language and multimodal models on tasks that require a combination of skills such as spatial planning, basic programming, and logical reasoning within the XLogoOnline visual programming environment.

### Strengths
1. Novel Programming Generation Evaluation: The evaluation of programming generation based on the XLogoOnline visual programming environment is somewhat novel, as it integrates vision, language, and coding skills to assess LLMs.

2. Well-Structured Paper Organization: The paper is well-organized, starting with an introduction to the benchmark, followed by a detailed presentation of the training data, and concluding with an evaluation of different performance metrics and analyses.

### Weaknesses
1. Lack of Task Challenge: The task presented in this paper appears to lack sufficient challenge, as evidenced by Table 6. Although the zero-shot performance of both closed and open-source models is low, simply synthesizing a large amount of training data can significantly boost performance. This suggests that the task is not particularly challenging. The poor performance of current models can be attributed to their lack of training with this specific data. A more detailed analysis of task difficulty is needed to solve this issue.

2. Narrow Scope of Visual Programming: The use of the XLogoOnline environment limits the code action space, as illustrated in Figure 1, which further contributes to the task's lack of challenge. Additionally, other visual programming languages, such as Scratch, are not considered in this work. This narrow focus limits the domain of the study, making it insufficient for a top-tier conference like ICLR.

3. Insufficient Evaluation of Large Multimodal Models: The paper evaluates only three multimodal models, leaving unclear whether current state-of-the-art closed and open-source multimodal models, such as Claude3.5, Gemini, and Qwen2-VL, could achieve better performance. A more comprehensive evaluation with a broader range of models is necessary to draw meaningful conclusions.

### Questions
Check Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes XLOGOMINIPROG, a program synthesis benchmark in visual programming that requires a combination of different skills. They evaluate the performance of various large models (GPT, Llama, LLaVA) which show a surprisingly low success rate. 
Additionally, they finetune a Llama3-8B model on a large-scale synthetic dataset of 80K visual programming tasks, outperforming GPT-4V and LLama3-70B. Finally, they propose emulator-driven fine-tuning, which designs curriculum over training data distribution by leveraging emulator feedback, i.e., assigning higher weights to tasks where the model struggles. The paper includes an analysis of failure cases, capabilities, and transfer learning skills.

### Strengths
* This paper introduces a new program synthesis benchmark for the *visual programming domain*, which currently lacks benchmarking compared to program synthesis benchmarks from natural language or docstrings (e.g., HumanEval, MBPP, APPS).  
* Experiment results are comprehensive across diverse model types and scale, along with an in-depth analysis of various failure types and capabilities. It is interesting to see that current models dominantly lack spatial reasoning, especially GPT-4V.
* Emulator-driven fine-tuning could be extended to other program synthesis domains that contain a wide range of complexity in the training set.
* The paper is well-organized and written clearly with sufficient detail on the dataset statistics, generation process, and experimental setup.

### Weaknesses
 * The paper proposes a new benchmark focusing on *visual programming*, yet only provides results on two VLM families: GPT-4V and LLaVA-1.5. As there exists a plethora of open-sourced VLMs, I think it would only make the paper better by adding diverse state-of-the-art models (e.g., Llama-3.2-vision, LLaVA-onevision, Phi-3-Vision, Phi-3.5-Vision, QwenVL, Cameleon, LLaVA-next, Pixtral).
* Need clarity in the data generation process. Are there cases where the generated code is correct for the wrong reasons (e.g., logic incorrect, answer correct)? Is the emulator able to filter out these cases during the correctness check? If not, how does that affect the performance of fine-tuned models trained on the synthetic dataset?
* Lacks detailed explanation of the emulator.

### Questions
* How do the benchmark results look like on other open-sourced VLMs?
* It's very interesting that fine-tuning a VLM (Llava1.5-13B-Uni) performs worse than fine-tuning an LLM (Llama2, Llama3), while the vision model (GPT-4V) outperforms GPT-4 in the base models experiment. Why do you think this is the case? It would be interesting to compare fine-tuning a more state-of-the-art VLM (e.g., Llama-3.2-vision, LLaVA-onevision).
* How does the emulator validate the soundness of the generated code? For instance, some code may be correct for the wrong reasons (e.g., logic incorrect, answer correct). Is the emulator properly filtering out these cases?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new visual reasoning benchmark that requires a combination of skills to be solved (like logic, math, coding, visual understanding). Then, they benchmark current visual language models, and show that they do not perform well on this benchmark. Finally, they propose an approach to improve such models, by finetuning them on more data that follows the distribution of the benchmark, as well as by doing it following a curriculum.

### Strengths
1 - This paper contributes a benchmark to study the capabilities of VLMs on program synthesis for visual tasks. The benchmark is challenging enough for current SOTA models to fail at it, but at the same time it is easy enough for humans to solve, making it a good contribution for the community. It also requires a variety of skills that previous benchmarks do not need, making it more general.

2 - The contributions are well motivated and well presented, making it an easy paper to read.

3 - The fine-tuning strategy using curriculum learning based on the harder and easier task is very sensible in this setting where multiple skills need to be learned. The specific implementation is reasonable, and provides very good results.

4 - The analysis (ablation study based on difficulty of the tasks, as well as failure analysis) is informative both in terms of understanding the benchmark better, but also in terms of understanding the models better.  Also, the "transferable skills" section is very pertinent. I was actually thinking about the zero-shot capabilities to unseen tasks before I got to that section.

### Weaknesses
I would appreciate if the authors analyzed the following:

1 - What is the drop (or increase) in performance in other standard vision tasks (such as VQA, classification) or even language or coding tasks when fine-tuning on the SIM dataset? It seems like the tasks follow a very specific pattern that may not be very related to other tasks. The paper shows that training on the SIM dataset contributes to tasks that were not part of the dataset, but I wonder if there is any contribution (positive or negative) to other tasks that follow different distributions (even though they may require similar visual or reasoning skills)

2 - What is the role of the prompt engineering in solving these tasks? How much effort and what techniques were used to ensure that the input prompts are not a limitation for the different models that were tested?

### Questions
- I would probably not call the REAL dataset "real-world" tasks. They are pretty much very synthetic and toy tasks, not real-world. Maybe you can refer to them as "existing" (or any other word). The term "real-world" was confusing at the beginning.  It would also help if you shoed an example of a SIM task in Figure 1, or in Section 4.

### Soundness
3

### Presentation
4

### Contribution
3
