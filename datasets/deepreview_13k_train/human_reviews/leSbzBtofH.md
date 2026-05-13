# AutoAdvExBench: Benchmarking Autonomous Exploitation of Adversarial Example Defenses

- Decision: Reject
- Scores: 8, 5, 8, 6, 5, 5

## Abstract
We introduce AutoAdvExBench, a benchmark to evaluate if large language models (LLMs)
can autonomously exploit defenses to adversarial examples.
We believe our benchmark will be valuable to several distinct audiences. 
First, it measures if models can match the abilities of expert adversarial machine learning researchers.
Second, it serves as a challenging evaluation for reasoning capabilities that
can measure LLMs' ability to understand and interact with sophisticated codebases. 
And third, 
since many adversarial examples defenses have been broken in the past,
this benchmark allows for evaluating the ability of LLMs to reproduce
prior research results automatically.
We then benchmark the ability of current LLMs to solve this benchmark,
and find most are unable to succeed.
Our strongest agent, with a human-guided prompt,
is only able to successfully generate adversarial examples on 6 of the 51 defenses in our benchmark.
This benchmark is publicly accessible at redacted for review.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new benchmark to test LLM capabilities: whether they can generate adversarial attacks to proposed adversarial defenses. The authors crawled arXiv and filtered the papers to find adversarial defense methods with easily reproducible code. Current state-of-the-art LLMs were tested on this new benchmark, and do not perform well.

### Strengths
The authors propose a novel benchmark to test the capabilities of LLMs. The proposed task is a real-world research/security setting, where the "correct" answer may not even be known, and yet there is a quantitative measurement that can be extracted to evaluate the abilities of the LLM. As a result, this provides a benchmark which may still be useful even if a model has surpassed human level performance in this domain. The authors are upfront about the many limitations of the benchmark.

### Weaknesses
 - The benchmark is evaluated in a limited setting. Even though to be successful, the model must be proficient in several different domains, the scope of the task is fairly limited.
- As mentioned, benchmark contamination is a potential issue, especially when considering the use of this benchmark well into the future.
- The benchmark does not appear to provide a meaningful continuous measure for current LLMs ability to generate novel attacks. Instead, it seems limited to whether they can successfully implement a known attack, as all of their current limited success on the benchmark is due to benchmark contamination.

### Questions
- As the models are currently not producing novel adversarial attacks, what does this benchmark measure that is not covered by existing benchmarks? Is the utility of this benchmark primarily for much more capable LLMs?
- How often do you expect to update the benchmark? If it is every time a new attack to a defense is published, then would this make it difficult to compare models trained at different points in time? If not, then might the benchmark provide an illusion of progress, even if it is just due of benchmark contamination?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a benchmark, AutoAdvExBench, to measure large language models' (LLMs) ability to exploit other AI systems. To be specific, AutoAdvExBench evaluates LLMs' ability to construct adversarial examples that bypass the corresponding defense methods. Experimental results demonstrate that AutoAdvExBench is challenging with a low attack success rate: only 6 of the 51 defenses are successfully attacked by their strongest agent.

### Strengths
+ Measuring AI's ability to exploit other AI systems is necessary and meaningful for preparing for future safety risks. Automatic AI exploitation becomes feasible due to the automated nature of the AI agent system and could result in catastrophic risks. This paper provides a realistic implementation for such a speculative threat model. Therefore, it will be a good proxy to monitor the progress of AI and prepare for the possible safety risks. 

+ The construction process of AutoAdvExBench is solid: this paper collects reproducible and diverse defense papers with manual checks to compose their benchmark, which will provide a strong basis for measuring AI exploitation ability.

### Weaknesses
 - **The evaluation metrics lack comprehensiveness.** The paper only reports robust accuracy and the number of successful attacks as metrics, neglecting more detailed analyses of the various capabilities agents need to overcome the benchmark. Areas like code comprehension, code completion, long-context understanding, and the novelty of proposed ideas are overlooked. For example, while the paper finds that only a quarter of defenses can be made differentiable (line 480)—a necessary step before designing new attacks—it’s unclear which capabilities agents lack that lead to these limitations. Simply reporting post-attack robust accuracy does not reveal which specific capabilities are bottlenecks, nor does it offer insights into where current models fall short.

- **Data contamination is a significant concern** that the authors have not adequately addressed. They do not provide empirical results to demonstrate the extent of data contamination in their benchmark. Although they state (line 262) that allowing agents access to paper data does not significantly improve success rates, this does not definitively rule out contamination. Furthermore, as the benchmark does not use the most advanced agent frameworks, it’s conceivable that more sophisticated agents could leverage memorized information to generate attack codes if contamination were present, raising questions about the benchmark’s validity and challenge level.

- **The captions of each table and figure lack essential details, making them difficult to follow.** For instance, in Figure 2, it’s unclear how the caption’s statement, "each line plots the number of defenses that reduce the robust accuracy to a given level," corresponds to the curves in the figure. Similarly, in Table 3, the meanings of terms such as "forward pass," "differentiable," and "FGSM attack" and the respective numbers are not fully explained. This also seems inconsistent with the analysis of FGSM in the main text (line 486), where an accuracy rate of 84% is mentioned.

- **The benchmark does not leverage the latest agent frameworks, such as multi-agent systems with specialized roles, which could potentially address the challenges posed by the benchmark.** The coding capabilities of the agents used in the paper seem quite limited (see Table 3), suggesting that the benchmark may not be challenging enough for cutting-edge agent models.



### Questions
- **The analysis of diversity among selected defense papers is insufficient.** Diversity is a crucial metric for this benchmark, yet the distinctions between each defense paper are not clearly highlighted (lines 224–230). It would be helpful if the authors could highlight the unique aspects of each defense paper and delineate their differences.

I would like to raise my score if the authors could address my concerns and questions.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an agentic benchmark for LLMs where the task is to automatically break various adversarial robustness defenses. It includes implementations and PDFs for a large number of adversarial robustness defenses, some of which have published vulnerabilities. The goal of the LLM agent is to output 1000 perturbed images under a standard \ell_{\infty} bound that break the defenses.

### Strengths
- This is a clever idea for an agentic benchmark. The task is complex but easy to evaluate, and it provides a way to measure how useful LLM agents could be for stress-testing defenses proposed by the ML community, which I think is an interesting future use case of AI agents.
- The work is timely. Multiple new agentic benchmarks have been proposed recently, including SWE-bench and MLE-bench. This paper continues that line of benchmarking work, but with an emphasis on automated stress-testing for adversarial training defenses.
- The writing is clear.
- The benchmark seems well-designed. The task is easy to understand. Useful data was curated to enable the agents to perform the task (paper code and PDFs).
- The baseline evaluations show that the task is tractable.

### Weaknesses
For defenses with published vulnerabilities, it would be good to include a check for whether the model is aware of these vulnerabilities or discovers them from scratch. I realize this isn't relevant to current models, since they aren't very good yet, but it could be an interesting thing to check in future models. I see your response in lines 261-262. This is just a comment that the paper would be stronger with proactive measures to address this.

### Questions
No questions for now.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces AutoAdvExBench, a benchmark to evaluate if large language models (LLMs) can autonomously break defenses to adversarial examples, given access to defense (a) the paper describing the defense, (b) the source code of the defense, (c) a correct forward pass implementation of the defense, (d) a perturbation bound, and (e) 1,000 images that should be attacked. The authors attempt both an end-to-end approach and a four-step, human-guided approach. Based on the low success rates, the authors conclude that current language models cannot autonomously break most adversarial example defenses.

### Strengths
-  An interesting attempt to test LLMs on a well-established security problem, i.e., defenses against adversarial examples. The authors have provided strong motivations for proposing such a new benchmark.

- The paper is written well, clearly stating the contributions beyond the literature and the significance. 

- The fact that current LLMs largely fail in solving such a well-defined problem is somewhat surprising and so calls for future work.

### Weaknesses
Presentation:

1. The reviewer appreciates that the authors have put much effort into describing the limitations, even as early as in Section 3.3. However, several points in Section 3.3 Limitations and Section 3.1 Motivation are actually from the same perspective but do not well connect. Specifically, as the reviewer understands, although the benchmark is “difficult” and “security-relevant”, ”Adversarial examples attacks are not representative of common security exploits”. Although the benchmark is “Messy”, its “Research code is not representative of production code”. It may help if the authors could first present the perspectives, and then talk about the motivations/advantages and limitations of the benchmark in each perspective.

2. Throughout the paper, only Figure 2 was referred to in the main text, making the more summarized information in tables/figures not helpful for understanding the paper. The authors should explicitly reference relevant tables and figures when discussing results in the main text. This would help readers connect the discussion to the supporting data more easily.

3. The term “successfully attacked” is not defined before use. For example, it appears in the second to last sentence of the Abstract and the caption of Table 3. In addition, it is not clear what the numbers in Table 3 mean.


Experiment:

1. Although it is OK to show current LLMs are not good at solving the new benchmark, there is no exploration of potential ways to improve them. For example, It is interesting that current LLMs still struggle with simple operations, e.g., “models were only able to implement a differentiable forward pass in 23% of cases”. However, the authors have not attempted to solve this and have not even discussed potential solutions. They could include ideas for targeted training and improved prompting strategies.

2. The authors state that “We impose no time restriction, on the number of unsuccessful attempts an adversary makes, on the runtime of the algorithm, or on the cost of the attack. However, we strongly encourage reporting these numbers so that future work will be able to draw comparisons between methods that are exceptionally expensive to run, and methods that are cheaper.” The reviewer does not get why they have not reported these numbers in this paper (which seems not to require too much additional effort).

### Questions
Please see the above weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces AutoAdvExBench, a benchmark designed to evaluate the ability of large language models (LLMs) to attack adversarial example defenses. The benchmark includes 51 defenses from 37 papers, and the LLMs are provided with the research paper and the corresponding code for the forward pass of the defense.
The authors test state-of-the-art LLMs like Claude 3.5-Sonnet and GPT-4o in various scenarios, finding that current models struggle significantly. Zero-shot attempts were entirely unsuccessful, and even with iterative debugging, only a few defenses were successfully attacked. 
The paper highlights the challenges LLMs face in automating security tasks, emphasizing their limitations in understanding and exploiting such defenses.

### Strengths
1. The authors invested significant effort in filtering relevant papers and collecting reproducible code, resulting in a comprehensive and valuable dataset of 51 adversarial defenses from 37 papers. This rigorous collection process enhances the benchmark's credibility and relevance to the research community.

2. The benchmark setup involves working with "messy" research codebases, which closely reflects real-world challenges in adversarial defense scenarios. This realistic approach adds significant value, as it pushes current LLMs to handle complex, imperfect code environments typical in real applications.

3. The paper employs definitive evaluation methods that do not rely on black-box metrics, such as LLM-as-a-judge approaches. Instead, it uses measurable, transparent performance metrics, ensuring that the results are both interpretable and replicable.

### Weaknesses
1. The paper lacks detailed examples of interactions with the LLMs, such as specific prompts used or a complete end-to-end example of at least one of the defenses and its corresponding developed attack stages. Including visual aids or detailed walk-throughs of successful or failed attacks could greatly enhance readability and engagement. The absence of such details makes the content dense leading to a less engaging reading experience.

2. The current experimental settings are overly general for the LLMs, so it's unsurprising to observe such low success rates. From my experience, even for simpler coding tasks, I find that even the best LLMs require significantly more detail—such as an initial code draft, context explanations, and multiple rounds of conversation and reflection, as in a chat scenario—to achieve the desired results. For example, would a 6-turn interaction (interactive human-AI chat session) with these models (like GitHub Copilot settings) yield much better results?

3. The paper could have explored more powerful methods, such as ICL few-shot examples, fine-tuning, or retrieval-augmented generation (RAG), to better evaluate LLMs' capabilities in solving the benchmark. These approaches could have provided valuable insights into the strengths and limitations of LLMs when leveraging different training and interaction methodologies. The current experimental settings are necessary but insufficient.

4. This is a coding task, yet the paper's background lacks information on state-of-the-art LLMs specifically trained for coding. You've tested with GPT-4o and Claude 3.5 Sonnet, but are there other LLMs worth experimenting with?

5. In Section 5.1 (End-to-End Evaluation), in the sentence "Unsurprisingly, we find that current defenses fail completely at this task ..." do you mean "current models"?

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
2

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
The paper presented AutoAdvExBench, which evaluated if LLM can automatically exploit defenses to adversarial examples. Contributions include:
- evaluates if models can match the abilities of expert adversarial machine learning researchers
- measure LLMs’ ability to understand and interact with sophisticated codebases
- evaluates the ability of LLMs to reproduce prior research results automatically

The results show: the strongest agent, with a human-guided prompt, is only able to successfully generate adversarial examples on 6 of the 51 defenses in the benchmark.

### Strengths
- It's an interesting benchmark to evaluate LLMs' capacity to autonomously exploit defenses to adversarial examples.
- The defense implementations are collected comprehensively and rigorously.
- The limitations are fairly presented.

### Weaknesses
The presentation can be improved:
- It takes me a long time to find out that adversarial examples are for image classifiers. LLMs also have so-called adversarial attacks- it would be better to make it clear of the specific task in the abstract as well as early in the introduction to make it clear.
- The introduction didn't actually specify what it is "autonomously generate exploits on adversarial example defenses", before jumping into what the benchmark includes and what is its impact.
- The abstract focuses on the potential impact of the benchmark a lot, Yet it shall better inform what is the benchmark is really about-- the first sentence didn't convey it clearly.

As a benchmark paper, more LLMs should be considered and benchmarked. However, we only see the results for Claude 3.5 and GPT-4o.

If that is because other LLMs are so weak for the task, I personally think a good benchmark for current sota LLMs should be able to distinguish their capacity. If most of them fail for the benchmark, then it may not be a good choice at this time.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2
