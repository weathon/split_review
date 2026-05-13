# On the self-verification limitations of large language models on reasoning and planning tasks

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
There has been considerable divergence of opinion on the reasoning abilities of Large Language Models (LLMs).
While the initial optimism that reasoning might emerge automatically with scale has been tempered thanks to a slew of counterexamples--ranging from multiplication to simple planning--there persists a wide spread belief that LLMs can self-critique and improve their own solutions in an iterative fashion.
This belief seemingly rests on the assumption that verification of correctness should be easier than generation--a rather classical argument from computational complexity--which should be irrelevant to LLMs to the extent that what they are doing is approximate retrieval.
In this paper, we set out to systematically investigate the effectiveness of iterative prompting in the context of reasoning and planning.
We present a principled empirical study of the performance of GPT-4 in three domains: Game of 24, Graph Coloring, and STRIPS planning.
We experiment both with the model critiquing its own answers and with an external correct reasoner verifying proposed solutions.
In each case, we analyze whether the content of criticisms actually affects bottom line performance, and whether we can ablate elements of the augmented system without losing performance. We observe significant performance collapse
with self-critique and significant performance gains with sound external verification.
We also note that merely re-prompting with a sound verifier maintains most of the benefits of more involved setups.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper evaluates the self-verification abilities of LLMs in reasoning and planning tasks using iterative prompting and critiquing. It contrasts the performance of LLMs self-verifying their solutions against external sound verifiers across three domains: Game of 24, Graph Coloring, and STRIPS planning. Findings indicate that LLMs underperform in self-verification and that external sound verification significantly improves the accuracy of solutions. The study suggests the ineffectiveness of self-critique mechanisms in LLMs and recommends integrating external verifiers for better performance in reasoning tasks.

### Strengths
1. The paper addresses a novel aspect of LLMs—self-critique and iterative verification—that is underexplored in the existing literature. It challenges the assumption that LLMs can effectively self-critique by demonstrating that external verification offers more reliable improvements. 
2. The experimental setup is clearly described, allowing for reproducibility and understanding of how iterative prompting affects LLM performance in reasoning tasks. The paper methodically outlines its methodology and the rationale behind using specific domains for testing (Sections 4 and 3). 
3. The findings significantly contribute to understanding LLM limitations in self-verification tasks, which is critical for deploying these models in real-world applications where accuracy and reliability are paramount. 
4. The study is well-structured and robustly empirically analyzed, providing a comparative assessment of LLMs with and without external sound verifiers.

### Weaknesses
1. The paper’s focus on only three specific domains might limit the generalizability of the findings. While these domains are relevant, more varied tasks could provide a broader understanding of LLM capabilities across different reasoning types (Section 3).
2. The analysis of the self-critique mechanism lacks depth regarding why LLMs fail at self-critique. Specific instances of LLM outputs and their failures would enrich the discussion by pinpointing the flaws in LLM reasoning strategies (Section 5.1).
3. There is no detailed discussion on the computational cost and efficiency of using external verifiers versus self-verification. This information would be crucial for practical implementations where resource constraints are a significant consideration.
4. The paper does not thoroughly explore the theoretical implications of its findings on the computational complexity theories surrounding LLMs and self-verification. A deeper theoretical analysis could provide insights into the fundamental limitations of LLM architectures (Section 2).

### Questions
1. How do the authors anticipate their findings will generalize to other complex reasoning tasks not covered in the study? Can the observed ineffectiveness of self-critique mechanisms be extrapolated to different types of LLMs or reasoning models? 
2. Could the authors elaborate on the choice of domains for the study? Why were these specific domains chosen, and how do they represent the broader spectrum of reasoning tasks applicable to LLMs? 
3. What additional mechanisms or modifications do the authors suggest could potentially improve the self-verification capabilities of LLMs? Is there ongoing work to develop more effective internal critique mechanisms within LLMs? 
4. How do the authors envision the impact of their findings on the future development and deployment of LLMs in safety-critical applications? What precautions or additional measures would they recommend based on their study’s outcomes?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This is an experimental paper studying the the popular technique of self-verification of LLMs for enhancing apparent reasoning capabilities. The stringent experimental protocol shows that the self-verification does not really work and shows that other techniques like using formal (symbolic) verifiers are better suited to achieve automated reasoning with LLMs.

### Strengths
1) The paper is really well written and easy to to follow. The non-technical nature might have helped here. 
2) I enjoyed reading the (extensive) related work section where problems in prior work are made explicit.
3) All claims made in the paper are substantiated by appropriate experiments.

### Weaknesses
1) For someone familiar with the field the findings might be a little bit obvious. However, given the amount of papers being published using self-verification, I nevertheless believe this to be an important study when it comes to combating the delusion of self-verification.

2) Given that this is an experimental study it might be good to also point out weaknesses in the experimental protocol. Specifically, making explicit all the assumptions that were made and what might change if they were not to hold. Concretely, what gives the authors the confidence that their findings have a high probability of standing the test of time. The current experimental protocol does not explicitly address the limitations of the chosen tasks, which might not fully capture the complexities of real-world reasoning scenarios. For example, the graph coloring and blocksworld tasks, while useful for controlled experiments, may not generalize to more complex reasoning problems that involve nuanced understanding of context and long-term dependencies. The paper should discuss how the choice of these tasks might influence the generalizability of the findings.

### Questions
See point 2) in weaknesses and more specifically: are there any arguments that the findings do not only hold for the examined LLMs but in general for transformer-based auto-regressive models, or even other models like discrete diffusion models.


Minor comment:
The use of \citep and \citet is not correct. Also there are some small spelling/typesetting issues here there that should be easily fixable.

### Soundness
3

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
4

### Summary
This paper discusses the effect of self-verification in LLM reasoning and planning, challenging the assumption that verifying correctness is easier than generating solutions. Through experiments in three domains (Game of 24, Graph Coloring, and STRIPS planning), it finds that self-verification does not improve accuracy and can even reduce performance. In contrast, a "sound external verifier" significantly enhances accuracy, with simpler re-prompting methods maintaining most of these benefits.

### Strengths
1. The presentation and writing are clear.
2. The authors made adjustments to the test datasets to ensure their validity. For example, they generated new instances to prevent test set memorization and modified the task solution format to better evaluate the self-verification pipeline.
3. The systematic analysis of self-verification provides insights into the cases where the verification module can help improve LLM performance.

### Weaknesses
1. The experiment design is not entirely persuasive.
The authors attempt to challenge the assumption that verifying correctness is easier than generating solutions, suggesting that self-verification does not improve performance. However, task difficulty should be considered. Apart from Blocksworld, the accuracy in other tasks is quite low. According to Table 2, "LLM Verification Results," verification performance varies across tasks, especially in terms of the False Negative Rate (FNR). In Blocksworld, which has the lowest FNR, self-verification actually improves task accuracy from 40% to 55%. This suggests there are cases where verification is easier than generation and where self-verification contributes positively to task accuracy. More tasks should be added for more comprehensive results.

2. The authors use a “sound” verifier as a comparison, but it’s unsurprising that a ground-truth verifier significantly improves performance. With ground-truth verification, the model can eliminate incorrect answers and focus on sampling correct ones, or at least provide ground-truth information. Taking the first point into account, a more nuanced conclusion could be that in tasks where verification is easier than generation, self-verification helps; otherwise, it has no benefit or even harms performance. The improvement limit for self-verification is thus bounded by the effectiveness of the “sound” verifier. 

3. The exact GPT version should be specified, and more models, particularly advanced ones, should be tested for comprehensive results.

### Questions
Please discuss the points mentioned in the weakness part.

### Soundness
4

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
This paper mainly evaluates the self-critique and verification capabilities of LLMs in comparison to sound verifiers. It concludes that the self-verification loop conducted by LLMs is not as helpful as previous works claimed. On the contrary, it might hurt LLM performance in some planning domains.

### Strengths
This paper has the following strengths.

Originality:
This paper systematically evaluates LLMs' self-verification capability by careful ablation and comparison to symbolic processors. It finds that LLM verification is not very helpful in some planning cases. This is novel and interesting.

Quality:
This paper considers problems of memorization and lack of ground truth during evaluation, which are important concerns.

Clarity:
The experiment setup is quite clear.

Significance:
Knowing what LLMs are actually doing when people claim they can do a lot of things is very important.

### Weaknesses
1. Is it fair to compare LLMs with oracle verifiers? The finding that LLM self-critique can sometimes downgrade their generation performance is interesting, but oracle processors are not always accessible in all tasks (as the authors mentioned in their paper, some tasks such as creative writing do not have a ground truth answer). I'm not surprised that oracle verifier is improving LLM performance, but I wonder if it is possible that LLM can serve as a decent alternative when sound verifier is absent in general areas? Specifically, the paper does not explore the potential of LLMs as approximate verifiers in domains where perfect verification is not feasible, which limits the practical implications of the study.

2. The task domains are constrained while the general conclusion is very strong. The authors evaluated three main planning tasks and one LLM (GPT-4) with four datasets, with no clear objective as to why the conclusion drawn from these three specific tasks can be generalized. It is unclear why these tasks and datasets can represent general LLMs' lack of self-verification capability in a wide ranges of tasks. The limited scope of the experiments raises concerns about the external validity of the findings. For example, the planning tasks used might not capture the complexities of other reasoning tasks, such as those involving common sense or nuanced understanding of context.

3. Some other details in this paper are also overclaimed, e.g., on page 2, the authors claim "...the state-of-the-art GPT-4" while GPT-4 is not SotA in many benchmarks anymore (in [1], inter alia). This overstatement undermines the credibility of the paper. Furthermore, the paper does not adequately acknowledge the rapid advancements in LLM technology, which could potentially impact the generalizability of the results.

4. There are quite some typos. Writing needs to be done with more care.

### Questions
I don't have more questions but authors are encouraged to address my concerns in the weakness section.

### Soundness
3

### Presentation
2

### Contribution
3
