# BioDiscoveryAgent: An AI Agent for Designing Genetic Perturbation Experiments

- Decision: Accept
- Scores: 5, 5, 8, 6, 8

## Abstract
Agents based on large language models have shown great potential in accelerating scientific discovery by leveraging their rich background knowledge and reasoning capabilities. In this paper, we introduce \emph{\agentname}, an agent that designs new experiments, reasons about their outcomes, and efficiently navigates the hypothesis space to reach desired solutions. We demonstrate our agent on the problem of designing genetic perturbation experiments, where the aim is to find a small subset out of many possible genes that, when perturbed, result in a specific phenotype (e.g., cell growth). Utilizing its biological knowledge, \Agentname can uniquely design new experiments without the need to train a machine learning model or explicitly design an acquisition function as in Bayesian optimization. Moreover, \Agentname using Claude 3.5 Sonnet achieves an average of 21\% improvement in predicting relevant genetic perturbations across six datasets, and a 46\% improvement in the harder task of non-essential gene perturbation, compared to existing Bayesian optimization baselines specifically trained for this task. Our evaluation includes one dataset that is unpublished, ensuring it is not part of the language model's training data. Additionally, \Agentname predicts gene combinations to perturb more than twice as accurately as a random baseline, a task so far not explored in the context of closed-loop experiment design. The agent also has access to tools for searching the biomedical literature, executing code to analyze biological datasets, and prompting another agent to critically evaluate its predictions. Overall, \Agentname is interpretable at every stage, representing an accessible new paradigm in the computational design of biological experiments with the potential to augment scientists' efficacy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces BioDiscoveryAgent,an AI-based tool for automating the design of genetic perturbation experiments. Leveraging large language models (LLMs) and biological knowledge, BioDiscoveryAgent identifies genes for perturbation to induce specific phenotypes, such as cell growth, without requiring custom machine learning models or acquisition functions.
Contribution: 1. BioDiscoveryAgent innovates in closed-loop experimental design by using LLMs to propose genetic perturbations in each experimental round, adapting its selections based on prior results and biological insight. 2. The agent outperforms Bayesian optimization baselines by identifying 21% more relevant genes across multiple datasets and achieves a 46% improvement on the more challenging task of identifying non-essential genes. 3. It incorporates external tools like literature search, code execution, and critique from a secondary agent, enhancing interpretability and decision-making.

### Strengths
Strengths of this paper includes: 
1. BioDiscoveryAgent introduces a unique approach to closed-loop experimental design, leveraging LLMs to suggest gene perturbations and adapt based on feedback from prior rounds. This paper claims this application of LLMs is novel in experimental biology, particularly for genetic perturbation studies.
2. The agent demonstrates superior performance compared to traditional Bayesian optimization methods. It identify 21% more relevant genes and 46% more non-essential gene hits.
3. BioDiscoveryAgent can draw from diverse information sources with high adaptability and versatility.

### Weaknesses
1. Although the model demonstrates strong performance on simulated and existing datasets, the paper lacks validation through real-world, wet-lab experiments.
2. BioDiscoveryAgent’s effectiveness is highly dependent on the underlying LLMs’ pre-existing biological knowledge and reasoning abilities. Limitations in the LLM’s training data or biological understanding could restrict the agent's performance.
3. The use of large-scale LLMs, along with additional tools like literature search and gene databases, results in considerable computational overhead.
4. While the agent performs well overall, the paper observes that the greatest performance improvements occur in the early rounds of experimentation, likely due to the LLM’s pre-existing knowledge. However, as rounds progress, these benefits decline, suggesting potential limitations in its ability to learn effectively from experimental feedback over time.

### Questions
See weakness.

### Soundness
3

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
4

### Summary
This work proposes BioDiscoveryAgent, a reflection-based LLM agent designed to conduct gene perturbation experiments. It iteratively predicts gene perturbation outcomes, selects genes to perturb, receives experimental results, and continues with subsequent trials based on updated predictions. The study evaluates the effectiveness of BioDiscoveryAgent using experiments on six cell perturbation datasets.

### Strengths
Backbone Testing: The experiments are conducted across multiple backbone models, enhancing the method's credibility.

Comprehensive Pipeline: The LLM agent is equipped with a variety of tools, resulting in a well-rounded approach.

Clear Writing: The writing is clear, making the method and results easy to understand.

### Weaknesses
Insufficient Baseline Comparisons: The baseline methods are somewhat distant from the proposed approach. Comparisons with interactive LLM agents, such as ReAct or multi-turn frameworks like reflection-based methods or LLMs as optimizers, would strengthen the evaluation. Additionally, as the method incorporates retrieval augmentation, a comparison with Retrieval-Augmented Generation (RAG) based on the same corpus would be valuable.

Potential Information Leakage: Could the use of literature and gene search cause information leakage? Specifically, is there a risk that the task query might already be covered in the literature or database, thus affecting the validity of the results?

Linear Performance Curve: Figures 2 and 3(a) show an almost linear improvement in performance across up to 30 turns, without any indication of saturation. This is surprising, as LLM-based multi-turn trials typically reach saturation more quickly. Could you elaborate on why this linear improvement occurs and when, if at all, it might begin to saturate?

Method Validity: The experimental results in Table 1 indicate that different backbones show nearly random performance variations, and the tool usage results in Table 3 also exhibit inconsistent improvements across backbones, which raises concerns about the validity of the proposed method. One possible reason for this could be the low 1-turn accuracy, leading to a low signal-to-noise ratio. Given that the linear performance curve suggests the LLM can effectively address this task with more turns, it would be beneficial to compare the performance of different backbones and tool usage in a multi-turn setting. This could provide more stable results and more insight about backbone’s influence.

### Questions
Potential Information Leakage: Could the use of literature and gene search cause information leakage? Specifically, is there a risk that the task query might already be covered in the literature or database, thus affecting the validity of the results?

Linear Performance Curve: Figures 2 and 3(a) show an almost linear improvement in performance across up to 30 turns, without any indication of saturation. This is surprising, as LLM-based multi-turn trials typically reach saturation more quickly. Could you elaborate on why this linear improvement occurs and when, if at all, it might begin to saturate?

Method Validity: The experimental results in Table 1 indicate that different backbones show nearly random performance variations, and the tool usage results in Table 3 also exhibit inconsistent improvements across backbones, which raises concerns about the validity of the proposed method. One possible reason for this could be the low 1-turn accuracy, leading to a low signal-to-noise ratio. Given that the linear performance curve suggests the LLM can effectively address this task with more turns, it would be beneficial to compare the performance of different backbones and tool usage in a multi-turn setting. This could provide more stable results and more insight about backbone’s influence.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present a LLM agent that can design single-cell experiments. At every step the agent uses literature and Reactome to narrow down a list of genes until it converges, taking the output of the previous step as context.

### Strengths
The authors present an interesting method of using LLMs to help guide perturbation experiments. The authors present extensive experiments with LLMs to pick the LLM best suited to coordinate the tasks to decide which genes will be perturbed. The LLM has access to literature and Reactome to make the decisions of the next gene to perturb. This work follows an increasing movement to design LLM agents to automate parts of the science process and, upon addressing of my points, represents a fruitful direction the community should head towards.

### Weaknesses
 **Major points:**

1. I am confused what does this paper add when there exists models like GEARS which can predict gene expression that results from perturbations? I realize the authors would argue that this model helps designs experiments as seen by its higher hit ratio but with this logic doesn't GEARS have a very high hit ratio, in one round of in-silico experiments getting many hits?

2. I am also confused by the metric, what about the genes that the model suggests that are not hits? Do we not care about precision? The genes that the model suggests that are not hits should also be considered. The more of these the worse off.

3. In line 1855 in the sample agent conversation where does the agent get log-fold change? Does it have a tool that gives it access to this information? From the main text it was just literature and reactome?

4. From Appendix Table 7 it is not clear to me that adding tools helps, a lot of the confidence intervals overlap? Is the difference in the numbers significant here? Also these differences vary by LLM which makes it hard to discern which to do for a particular task.

5. What is the agent adding that cannot be done by simply doing a more traditional pathway enrichment analysis and google?

**Minor points:**

1. Two-gene perturbation prediction is not a new problem. GEARS introduces this problem already.

### Questions
No questions.

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
3

### Summary
This paper presents an LLM-based agent to design gene perturbation experiments for drug targeting, using the LLM's inherent knowledge, previous observations and external tools to improve hit rates over various baselines.

### Strengths
1. The motivation is clear, and the method design seems intuitive;
2. The experiments are thourough, including different LLMs, both seen and unseen datasets, single and double gene settings, and different tool utilization. The results with the strongest LLM shows a large margin over traditional methods, supporting the effectiveness of their approach.
3. Detailed prompts were provided in the Appendix, which is good for reproducibility.
4. The writing is clear and easy to follow.

### Weaknesses
 1. Given the application scenario of the problem, most of the prompting techniques (e.g. to include previous outcomes, to reflect and plan for the next step) are quite intuitive. I do not find anything particularly novel in this part. In particular, you included the literal representation of the experiment outcomes into the prompt for the agent's observation, which is basically an array of numerial data. I wonder if this is the best way to do it.
2. The tool utilization techniques (e.g. searching for genes in the same pathway, searching PubMed articles) are reasonable, but they sometimes does not improve or even hurts the performance. This is concerning when happening with strong LLMs such as Claude 3.5 Sonnet, if we want to explore an upper bound on the abilities of the agent. Moreover, there lacks an explanation why the effects of tools differs with LLMs. From an application perspective, it would be good to predict when using tools helps and when it does not.
3. There lacks an intuitive explanation why using critiques could benefit the agent's predictions, given that the critique is yet another LLM that is not necessary stronger than the actor, and can make mistakes with the same probablity. Unless it is prompted in a way complementary to the actor, or is accessible to some information unavailable to the actor.
4. In general, the paper makes several reasonable attempts to enhance the agent, yet their method does not seem refined enough to contribute substantially to the agent methodology in this application scenario. There also lacks an in-depth discussion on the inconsistency in their empirical findings.

### Questions
1. (Same as Weakness 2) Can you provide an intuitive explanation why the effect of using tools differs with LLMs?
2. (Same as Weakness 3) Can you explain a bit the method used by the critique agent, and why you think it may improve performance?
3. You mentioned in the Discussion section that much of the improvements brought by the agent are observed in the early stages, which I think may be related to a better cold start compared to traditional methods. Do you think we can probably use the cold starts from agents to enhance traditional methods?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a new, LLM-based approach for designing gene perturbation experiments, where the goal is to efficiently select a subset of genes that result in a desired phenotype when perturbed. Their approach is based on the creation of BioDiscoveryAgent, an LLM-based agent that can generate, critique, and refine hypotheses about which genes should be selected. They show that BioDiscoveryAgent achieves a large performance improvement over baselines on the task of predicting relevant genetic perturbations across six datasets.

### Strengths
1. **Significant contribution to an important problem.** The problem of efficiently designing genetic perturbation experiments is important, with wide-reaching applications to drug target discovery, gene therapy, immunotherapy, etc. The authors’ experiments show that their proposed method yields a considerable performance improvement over baselines on the task of identifying relevant gene perturbations.
2. **Novel application of LLMs.** While using LLMs for experiment design is not a new idea, to my knowledge, it has not yet been explored for the design of gene perturbation experiments. The author’s approach is considerably different from existing approaches for this task, which primarily focus on Bayesian optimization.
3. **Experiments are thorough and produce interesting insights.** The authors not only show that their method obtains strong performance, they also conduct a series of experiments that shed light on why their method is able to perform well. In particular, the experiments that examine the similarity of the predicted genes across datasets and across experimental rounds are very interesting. The prompt/observation ablations are also very helpful in understanding which parts of the method contribute to the strong performance.
4. **Clear presentation.** The paper is clearly written. The motivation, contribution, and experiment design are all clearly and thoroughly described. It is written in a way such that it is understandable even for someone with a limited background in biology.

### Weaknesses
1. **Lack of technical/methodological novelty**: The two main parts of the method are (1) task-specific prompts and (2)  an algorithm that involves repeatedly calling an LLM with prompts that are adapted based on the outputs at previous steps. This basic process is shared by other work on LLM agents. However, I don’t consider this a major weakness, since the goal of the paper is to design an approach that works well for gene perturbation experiments, and the authors’ approach both works well and is novel within this context.
2. **Claims about interpretability seem overstated**: The authors claim multiple times that their approach offers the benefit of interpretability. For example, they claim that by having the model output a “research plan” and “reflection” in addition to the "solution", this can help to increase interpretability and “rule out predictions that may be hallucinations or not well-motivated.” The problem with this logic is that it assumes that the model’s stated reasoning/reflections are indicative of the true reasoning the model used to arrive at its solutions. However, prior work has shown that an LLM’s stated reasoning/explanations may be misleading/unfaithful to its true decision making process (e.g., [1]). In light of these findings, the author’s claims about interpretability seem overstated to me. I think the paper would be strengthened if the authors discussed the risk that these “reflection” outputs could be misleading. In addition, the authors claim that the LLM’s use of the literature search tool enhances interpretability. However, if the LLM incorrectly summarizes an article or hallucinates information that is not present in the article, this could actually harm interpretability (because it would be misleading). While the user could go to the article and check the correctness of LLM summaries, this is a time-consuming process, so it may not be realistic to expect a user to do this.

### Questions
1. Why don’t you include all baselines in the 2-gene perturbation experiments (i.e., why do you only compare to random sampling)?

### Soundness
4

### Presentation
4

### Contribution
3
