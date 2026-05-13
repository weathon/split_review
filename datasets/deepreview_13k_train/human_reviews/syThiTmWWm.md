# Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates

- Decision: Accept
- Scores: 8, 10, 10, 8, 6, 6, 6, 8

## Abstract
Automatic LLM benchmarks, such as AlpacaEval 2.0, Arena-Hard-Auto, and MT-Bench, have become popular for evaluating language models due to their cost-effectiveness and scalability compared to human evaluation. Achieving high win rates on these benchmarks can significantly boost the promotional impact of newly released language models. This promotional benefit may motivate tricks, such as manipulating model output length or style to game win rates, even though several mechanisms have been developed to control length and disentangle style to reduce gameability. Nonetheless, we show that even a \textbf{``null model''} that always outputs a \textbf{constant} response (\emph{irrelevant to input instructions}) can cheat automatic benchmarks and achieve top-ranked win rates: an $86.5\%$ LC win rate on AlpacaEval 2.0; an $83.0$ score on Arena-Hard-Auto; and a $9.55$ score on MT-Bench. Moreover, the crafted cheating outputs are \textbf{transferable} because we assume that the instructions of these benchmarks (e.g., $805$ samples of AlpacaEval 2.0) are \emph{private} and cannot be accessed. While our experiments are primarily proof-of-concept, an adversary could use LLMs to generate more imperceptible cheating responses, unethically benefiting from high win rates and promotional impact. Our findings call for the development of anti-cheating mechanisms for reliable automatic benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates vulnerabilities in automatic LLM benchmarks (like AlpacaEval 2.0, Arena-Hard-Auto, and MT-Bench) by demonstrating that even a "null model" - which outputs the same constant response regardless of input - can achieve high performance scores. The authors show that through carefully crafted structured responses and random search optimization, their null model can achieve an 86.5% LC win rate on AlpacaEval 2.0, an 83.0 score on Arena-Hard-Auto, and a 9.55 score on MT-Bench, matching or exceeding state-of-the-art models. The work highlights significant vulnerabilities in current automatic evaluation methods and calls for developing robust anti-cheating mechanisms for LLM benchmarks.

### Strengths
Pros:
- I think it’s a great paper that brings up the important point about the possibility of overfitting to LLM judges.
- It’s also very interesting to see that one can fool LLMs with the same (completely non-sensical) response across different requests. This clearly highlights how brittle LLM as judges are.
- On the other hand, as, e.g., Figure 2 illustrates, coming up with an effective null model is not straightforward. In particular, a simple adversarial suffix isn’t effective.
- The evaluation methodology looks good: the generalization of the null model between a validation and test set is clearly evaluated.
- The paper also shows a significant gap between LLM and human perception (i.e., humans don’t have any issue with these “null models”).
- The paper is clearly written, original, and the findings are quite significant.

### Weaknesses
 (Minor) weaknesses:
- It’s probably not too surprising that LLMs are vulnerable to these attacks given all the literature on adversarial examples, prompt injections, and jailbreaks for LLMs. But on the other hand, I believe there should be a clear and systematic reference that illustrates this fact for LLMs as judges that play a key role now for LLM evaluation, data filtering, etc. And this paper does a good job at this.
- The name “null model” is slightly confusing since it’s not really a model but rather a text snippet. Moreover, it’s not just a “null” model, but a very specific one (i.e., adversarially optimized), which is not reflected in the name “null model”. Although, I can imagine, it’s probably “too late” to rename a central concept of the paper.
- The paper could have discussed a bit more about how likely the patterns from these adversarial null models to occur more naturally, i.e., without an adversarial procedure involved.

### Questions
---

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper shows vulnerabilities in LLM-as-a-judge paradigms, showing that a "null model" with a crafted, constant output can achieve high scores (strongly beating SOTA) against such judges. The paper motivates how this vulnerability is concerning given how strong results on such automated benchmarks help model developers achieve promotional benefits. A prompt-injection style attack is proposed, with random search prefix optimisation making the attack stronger, leading to length controlled (LC) win rates up to 86.5% on alpaca-eval against a GPT-4 annotator without access to test set instructions. Baseline defences like perplexity filters and releasing paraphrased prompts are not enough to defend against the proposed attack. Further analysis also shows that access to test-set instructions can help strengthen the attack, and the method can also be combined with normal (real) model responses to inflate auto-benchmark scores.

### Strengths
1. The paper highlights the vulnerability of using LLM judges, motivating why they are becoming more common, existing issues and how the issue they demonstrate is much more glaring.
2. The attack succeeds (much better than SOTA model performance) under a strong threat model of giving a constant output to the LLM judge.
3. The attack transfers across 3 popular benchmarks (alpaca-eval, arena-hard-auto, mt-bench)
4. The attack is extensively ablated, showing the importance of using both the structured prompt injection and prefix optimisation.
5. The paper is well written, easy to follow, and provides interesting analysis on how the attack can be combined with normal responses.

### Weaknesses
1. It's unclear why the structured response doesn't work for llama. Could you back the claim of lower instruction following capabilities being the reason with a) Instruction Following eval scores for GPT-4, Llama-3-70B Instruct, b) showing a plot of structured response success vs instruction following results for different auto-annotator models?

2. Currently there are no comparisons to attacks on LLM-as-a-judge performed by prior work. It would be informative to see how existing attacks on LLM-as-a-judge mentioned in the related work section [Raina et al. (2024), Shi et al. (2024), Chen et al. (2024c)] empirically perform in the null model setting (with some reasonable adaptations).

3. While I appreciate showing results on baseline defences to prompt injections like perplexity filters and paraphrasing, there are stronger defences available now, such as those in this link: https://github.com/tldrsec/prompt-injection-defenses. It would be useful to know if using any of these defences fixes this issue. Some of these involve using LLMs out-of-the-box to filter prompt injections, whereas others train for this task. It would be good to see if the former is enough, or the latter is needed to prevent null model attacks.

4. The claim about paraphrasing defences not working should be qualified further. For example, I believe that if the template uses a sufficiently different format, or includes specific instructions to ignore the prompt injection, the attack might not transfer. Thus, it is helpful to rephrase the claim as 'trivial paraphrasing is not enough, though more targeted ones could work'.

### Questions
1. Do the authors have any evidence for benchmark gaming already occurring based on degenerate artefacts being added to model responses such as the null model string found here?

2. Is it possible to expand the scope of the evals affected? Can this be done against arbitrary reward models? In this case, why doesn’t reward model optimisation collapse to such degenerate solutions?

3.  Can we use this to bring down accuracy of models on human-generated mcqs, such as in MMLU? i.e. can adding adversarial suffixes to MMLU wrong options make the model prefer these, leading to lower accuracies?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
Traditional benchmarks are, in general, manually curated and static (not updated after release). Automatic LLM benchmarks fix several issues that come with static benchmark datasets, can improve over time due to automatic curation, and can be less costly.
This paper explores different ways in which a model can cheat these benchmarks, and emphasizes the necessity for counter mechanisms. The method involves utilizing a model that responds with constant outputs. Two strategies are discussed: (1) structured cheating responses in which confuses the model by replacing the original comparison, (2) using adversarial prefixes optimized with random search. It is shown that the structured responses method achieves SOTA across all benchmarks used in the experiments.

### Strengths
- The idea that Automatic LLM benchmarks can be cheated is clearly demonstrated.
- Using the proposed method, SOTA scores are achieved for all the  benchmarks tested, highlighting the core goal of the paper.
- The jailbreak method exhibits some robustness because of the optimized prefix strategy, making it transferable as pointed out in the text.
- The authors discuss potential anti-cheating strategies.

### Weaknesses
 - The paper could benefit from additional comparator methods.

### Questions
- Would it be possible to create additional baselines for different degrees of structured response complexity?
- How much manual iteration did you do to reach the final structured responses?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper shows surprising results that benchmarks based on LLM evaluations can be attacked by "null model" which outputs a constant response. 
The authors adopt the random search methods from universal adversarial attack literatures on the nlp domain to optimize "constant response" by "null model" to attack automatic benchmarks.
Notably, the proposed "null mode" achieved SOTA LC win rate of 86.5% on AlpacaEval 2.0.
Although the proposed "constant response"s are obviously perceptible, the authors emphasize the risk of imperceptible cheating mechanism against automatic benchmarks and the importance of developing anti-cheating mechanisms for automatic benchmarks.

### Strengths
- Although the proposed optimization method is not new, the empirical results showing high win rate (86.5%) provided in this paper is surprising.
- The writing is clear and the paper is easy to read. The authors provide sufficient implementation for reproducing results. 
- The automatic benchmarks with LLM evaluations are widely used due to their high alignment with human evaluations and low cost. Highlighting the potential risk of these benchmarks is important for maintaining trustworthiness.

### Weaknesses
 - The proposed examples of "constant response"s are too random. It would be better if there is an example with higher naturality that attack the automatic benchmarks. Even with a lower win rate than 86.5%, providing imperceptible and natural examples that are harder to detect could raise greater awareness among readers.
- The proposed method is not new. I agree with that this work is a valuable research, but this paper may be more suitable to "position paper" on nlp conferences.

### Questions
Please refer to the "Weaknesses" section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies null models that output a constant response but take advantage of failures in LLM-based judging in benchmarks. The response is crafted with a template that takes into account its placement either at the the start or the end of the context, and contains some additional tokens that are optimized with random search to obtain the desired outcome. The null model is able to cheat its way to getting a very high win rate on LLM benchmarks, and the authors include some analysis and ablation studies at the end.

### Strengths
+ The template is shown to be quite high "performing" on various benchmarks
+  While the template alone does not work for all models, like Llama-3, with the additional optimized tokens (i.e. jailbreak attack) it can still reach high efficacy rates (so the randomized search is to some degree necessary)
+ The authors include additional studies showing that summarization and perplexity filters are insufficient automated techniques for preventing this type of cheating. So the developed template and search algorithm have some evidence of being robust to trivial solutions.

### Weaknesses
 + The main technical contribution is the construction of a template plus randomized search, the latter of which comes from the jailbreaking literature. The findings are likely of more interest than the technique. 
+ As I understand it, any human that looks at any of the answers outputted by this technique would immediately see that it is wrong. So the cheating technique is only effective on fully automated benchmarks where no human is checking any outputs. Unless we have fully closed-source automated benchmarks (where nobody is allowed to inspect the outputs), I suspect that the fear of being called out by the rest of the community would prevent researchers from carrying out such cheating techniques in practice. So I view these results as more proof-of-concept and academic rather than a current problem affecting automated benchmarks today, especially since an LLM company's goal of doing well on benchmarks is to create a better LLM, rather than cheat the benchmark and not have a product.

### Questions
+ In the paper, transferrability is mainly discussed in terms of transferring between instructions. To what degree do the tokens found with randomized search to jailbreak the benchmark transfer between different judges?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates the vulnerability of automatic LLM evaluation benchmarks such as AlpacaEval 2.0, Arena-Hard-Auto, and MT-Bench. These benchmarks, which use LLM-based auto-annotators like GPT-4, aim to provide scalable alternatives to human evaluation. The authors introduce a “null model” that outputs a constant, irrelevant response, demonstrating that even non-informative, structured responses can achieve deceptively high win rates. By incorporating structured responses with a carefully optimized adversarial prefix generated through random search, this null model exploits weaknesses in benchmark evaluation, achieving competitive results without access to benchmark instructions. To address these vulnerabilities, the authors test anti-cheating strategies, including template paraphrasing and perplexity-based filters, though they find these defenses insufficient on their own. The study underscores the need for more advanced anti-cheating mechanisms, as current methods do not fully prevent adversarial manipulation in automatic LLM benchmarks.

### Strengths
1. The paper presents an original approach by introducing a “null model” that generates irrelevant yet structured responses, revealing a new vulnerability in LLM evaluation benchmarks. This novel perspective highlights how even non-informative outputs can achieve high win rates, setting this work apart from prior adversarial attacks that rely on relevant responses to manipulate evaluations.
2. The null model is evaluated across multiple benchmarks like AlpacaEval 2.0, Arena-Hard-Auto, and MT-Bench. 
3. The inclusion of an anti-cheating section adds value by addressing practical defenses against the observed vulnerabilities. The authors discuss template paraphrasing and perplexity-based filtering, though they recognize that these are limited in effectiveness. Therefore, they suggest actionable strategies for improving benchmark robustness and encourages the development of more secure evaluation standards.

### Weaknesses
1. The structured response method, while effective, relies on manual crafting without sufficient explanation of the process, which affects the soundness and generalizability of the approach. A more detailed description of how the structured responses were developed—such as the specific guidelines or iterative steps followed—would improve clarity and allow for reproducibility. The paper lacks details on how the structure was chosen, making it difficult to assess if the observed success is due to a generally exploitable weakness or a specific artifact of the chosen structure. For instance, it is unclear if the structure exploits positional biases, specific token patterns, or other vulnerabilities in the LLM judges.
2. Although the paper demonstrates that random search (RS) enhances the success of adversarial prefixes, it lacks clarity on the specific optimization criteria and alternative strategies that could guide this process. Providing more detail on the objective and discussing potential alternative optimization algorithms would improve the soundness of the approach. This expanded discussion would also enhance clarity, helping readers understand why RS was chosen and how it compares to other possible methods in achieving competitive results. The paper should specify the loss function used for the random search and why other optimization methods, such as gradient-based approaches, were not considered or were deemed unsuitable.
3. While the paper distinguishes the null model approach from prior efforts in attacking LLM-based evaluations, it would be beneficial to include a comparison with existing algorithms applicable to the evaluation settings examined here or to clarify why those methods may not apply. This additional context could better position the novelty of the work, reinforcing its contribution by distinguishing it within the broader landscape of adversarial techniques for LLM evaluation. The paper should discuss how existing adversarial attacks, such as those based on gradient-based optimization or reinforcement learning, perform under the same constraints as the null model (i.e., constant output and no access to benchmark instructions).

### Questions
1. Could you describe the process used to manually craft the structured responses? Specifically, what inspired your initial approach, and how did you refine these responses to enhance their effectiveness against benchmarks?
2. What was the ineffective adversarial suffix mentioned in L152/153, and how was it optimized?
3. What is the loss shown on the y-axis of Figure 2?
4. What’s the optimization objective of the adversarial prefix with random search? The objective for this random search is not clearly defined in Section 3 or Algorithm 1. Could you specify what loss function or evaluation metric was used to guide this optimization?
5. Is there a reference error to Table 5 in L312/313? The current reference to Table 5 appears to be incorrect—should it instead reference Table 4?
6. What results do you observe when using only the adversarial prefix without the structured response? Would the adversarial prefix alone achieve competitive win rates, and if so, could it be more effectively countered through template rephrasing?
7. Could you provide additional details on the setting where the structured cheating response is combined with normal responses? How was the cheating response appended to the original responses, and were the results specifically achieved with the Structured+RS approach?
8. Would the PPL filter be effective for open-source auto-annotators? Based on Figure 6, it seems the PPL filter may be insufficient for GPT-based auto-annotators. Could you provide insights into whether the PPL filter would work more effectively against open-source models like Llama-3-8B-Instruct and Llama-3-70B-Instruct, which may exhibit different perplexity thresholds?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 7

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores a cheating method to deceive LLM-based evaluation benchmarks. Specifically, it demonstrates that a particular cheating template, which exploits the standardized templates used in these evaluations, can be an effective attack. Additionally, the authors introduce an optimization technique to make the prefix, which, when combined with the cheating template, increases the performance of null responses. The paper emphasizes the need for more robust development of LLM-based evaluations to prevent such cheating.

### Strengths
- The paper demonstrates that even a null model, which always outputs the same response, can manipulate results on benchmarks that use LLMs for evaluation, highlighting the need to improve the robustness of these benchmarks.
- The paper is easy to read and follow, and the high-level process of creating a cheating prompt along with its optimization is well explained.
- The paper also explores some solutions to this cheating issue such as perplexity filtering, although these do not perform well.

### Weaknesses
 - Although demonstrating that a simple fixed response can exploit the evaluation benchmark is novel and exciting, I believe it is also a limitation of the paper in terms of practicality. In real-world scenarios, many open-source models on leaderboards are also evaluated qualitatively by a lot of users. If a model produces an obvious cheating prompt, people would likely disregard it. It would have been better if the paper had provided a scenario illustrating how this finding could be applied in real settings and how it might mislead actual users of LLMs. Without this, the notion that LLM evaluation is imperfect and susceptible to manipulation is already widely known, making the paper’s message seem incremental, despite showing vulnerability to simple cheating.
- I think the paper lacks some details on the methods. For example, in Figure 1, what is the difference between the text in blue and the text in black? It seems that the blue text represents a prefix optimized version, but this is unclear in the caption and figure. Additionally, what loss function is used in the universal random search? There is no commentary on each part of the algorithm, which affects clarity. Moreover, how could we design a new structured cheating method for a new benchmark based on LLM evaluation?

### Questions
- For the paraphrased result, what if we use a random selection among multiple paraphrased samples during evaluation? Is it still susceptible to cheating?
- In terms of a solution, what if the evaluation LLMs are informed about the possibility of cheating and are therefore prompted to prioritize the first instruction?

Please refer to the weaknesses section for critical questions.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 8

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper evaluates the effectiveness of automatic benchmarks for language models, while posing the new and interesting question of whether you can cheat on these benchmarks. The authors show that even a simple “null model” can manipulate these benchmarks, achieving impressive win rates—9.55 on MT-Bench for instance. This demonstrates vulnerabilities in the benchmarks, as crafted outputs can bypass their intended controls. The study emphasizes that these outputs can be transferred across benchmarks, raising ethical concerns about unfair advantages. Ultimately, the authors advocate for developing anti-cheating mechanisms to ensure the reliability of automatic evaluations.

### Strengths
- This paper possesses a very thoughtful and straightforward idea which is executed well
- The authors describe (perhaps for the first time?) a threat model of chasing on LLM-graded evaluations. This model will be useful for other researchers. I believe that this work has a higher than average potential for impact within the field. 
- I find the authors have done a decent job at evaluating the obvious questions in this space. They provide a thorough detail of the types of questions that are natural to ask about cheating in LLM-graded evaluations. For example, they ask about what type of null-model responses are effective, how to craft the null-model responses, etc. The authors could do a better job at locating at more models (see below), but this work gives a great foundation for posing an interesting problem and interrogating specific and interesting questions. 
- I particularly appreciate that the authors did not just identify a potential vulnerability in the LLM-graded evaluation space, but they also looked at mitigation techniques (Section 6). This is an often missing part of papers like this, and I am glad the authors have spent time to explore this space initially.

### Weaknesses
 - I’m sure the authors would agree that their analysis only applies to LLM-graded forms of auto-evaluations. There have been more recent benchmarks looking at auto-evaluation of LLMs based on ground truth scoring. Benchmarks like LiveBench and datasets like MATH, WikiQA, etc are such examples. While this doesn’t invalidate the argument, it is an important point that I feel the authors should include, and rather prominently, in the introduction, related work, and conclusion of the paper. For example, throughout the paper, the authors describe “auto-annotators” where they really mean “LLM-based auto-annotators.” This would also be a good thing for the authors to mention that cheating on benchmarks like this would be an area for future study since the paradigm is so different. Even better, the authors could pose a few suggestions for this future research direction to inspire the community to pursue this direction as well as the LLM-graded cheating. 
- The authors could improve on the clarity of the presentation of this work in some places. For example:
    - The authors introduce for the first time “optimized adversarial suffix” in the first sentence of Section 3 where they are presenting the results of that method. It opens a lot of questions which go un-answered: what suffixes did they test? how did they test them?, etc. I’d suggest the authors perhaps restructure this section to guide the reader more directly through these strategies. (See last bullet for suggested restructure.)
    - See 3rd question below
- I feel like the authors could be more careful in their language in places. For example, they title the subsection at L296 “Is the structured response useful on open-source auto-annotators?” however the authors only look at Llama-3-8/70B. This hardly represents open source models. I suggest the authors make a pass and tone down any language that is overly broad and unsupported by their data. 
- I think structurally in the paper, the authors can/should dedicate more space in this work to a discussion of their findings. I suggest the authors pick up space in the Related Work section by moving some of it to the Appendix. Then specifically, take more care in Section 3 to detail the differing ways in which response can be generated, describing that ablation/initial experiment in more detail, and then providing additional explanations and hypotheses throughout Section 4-6. The current draft reads more as a presentation of detailed results, and less about a thoughtful discussion of what those results mean in the context of their inquiry. Incorporating answers to the questions below (and those of the other reviewers) would be a good place to start.

Minor point:
- L210-211 deserves a citation, something like [this](https://arxiv.org/abs/2305.17926)

### Questions
- In reference to Figure 3 and knowing the GPT4 prefers the first response in auto-evals, can the authors speculate on the impact of their approach (“Ours”) on this phenomenon? 
- Can the authors describe why they think there is the following difference between GPT4 and Llama-3-70B: both 70B and GPT4 show positional bias, but only GPT4 is susceptible to the structured cheating method? I don’t particularly buy into the argument in L309-311  because the index 0 method doesn’t really look like an instruction to follow. 
- Can the authors also clarify whether the Index 0 method, as shown in Figures 3 and 4 and Table 6 is the same for all models? Put another way, is index 0 fixed throughout?

### Soundness
4

### Presentation
3

### Contribution
4
