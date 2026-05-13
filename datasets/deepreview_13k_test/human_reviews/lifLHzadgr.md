# Cumulative Reasoning with Large Language Models

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Despite the recent advancements in language models (LMs), their ability to solve complex problems remains limited. This paper introduces \ourmethod (\ourname), a novel approach that utilizes LMs cumulatively and iteratively, mirroring human thought processes for problem-solving. \ournameb decomposes tasks into smaller, manageable components and leverages previous propositions for effective composition, significantly enhancing problem-solving capabilities. We demonstrate \ournameb's superiority through several complex reasoning tasks: it outperforms existing methods in logical inference tasks with up to a 9.3\% improvement, achieving 98.04\% accuracy on the curated FOLIO wiki dataset. In the Game of 24, it achieves 98\% accuracy, marking a 24\% improvement over the prior state-of-the-art. Additionally, \ournameb sets new state-of-the-art on the MATH dataset, achieving a 4.2\% increase from previous methods and a 43\% relative improvement in the most challenging problems. By extending \ournameb to incorporate a code environment without external aids like retrieval or web browsing, we further harness the computational and logical reasoning capabilities of LMs, achieving a remarkable 72.2\% accuracy on the MATH dataset and outperforming the PAL/PoT method by 38.8\%.}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new prompting technique for complex reasoning problems. The proposed method iteratively proposes and verifies the next step for solving reasoning problems, which allows a more flexible reasoning path/structure. The empirical results on logic reasoning, game of 24, and math datasets show significant improvement upon baselines.

### Strengths
1. The empirical results on three types of reasoning tasks are significant.
2. By enabling a flexible reasoning path, the proposed method is able to reduce the number of visited states.

### Weaknesses
1. The author should also compare the ToT baseline in the logic reasoning and math datasets since it also involves iterative prompting and is more comparable to the proposed method.
2. some typos: section 2.1, $1 \land x = x$, $0 \lor x = x$.

### Questions
1. How is the time/compute efficiency of the proposed method compared to the baselines? I understand that the proposed method visited fewer states during inference, but I'm not quite sure if the compute/number of GPT4 prompting for each state visiting is the same as the baselines.
2. What are the prompts used for implementing the proposer, verifier, and reporter? It is not clear how LLMs achieve those functions.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a reasoning approach known as Cumulative Reasoning (CR), which utilizes language models in a cumulative and iterative fashion to mimic human cognitive processes. It comprises three key elements: the proposer, verifier, and reporter. The proposer continuously suggests potential propositions, which are then assessed by one or more verifiers, while the reporter determines when to conclude and stop the chain. In various logical inference tasks, Game of 24 and mathematical reasoning, CR outperforms previous methods, achieving state-of-the-art results.

### Strengths
- The paper is well written while giving a clear picture of the tasks that are being tackled. This is helpful to understand the task better and then analyse the methods to see the advantages of the proposed methodology. 

- The paper introduces a framework consisting of three components: the proposer, verifier, and reporter, which can be combined to tackle a task. Its advantage, when compared to CoT, lies in its step-by-step reasoning approach, where the entire chain of reasoning isn't predetermined all at once. Instead, the proposer determines subsequent steps based on past context, and the verifier assesses whether to continue the existing chain or establish a new one. This helps prevent the model from persisting in an incorrect reasoning chain, allowing early detection of errors. This may prove beneficial for tasks where $n$ different full chains are first sampled and then a decision is made on which one to prefer (like a ranker). This is also advantageous compared to the Tree of Thought method as some branches can be cut off on time, saving costs. 

- The reporter can decide to stop the chain at any time and derive the final answer. This prevents the model from hallucinating or making the correct reasoning worse by going with it further and modifying it. Can be seen as a nice stopping criteria for reasoning.

### Weaknesses
- Firstly, I find the comparison with the number of samples for CoT somewhat perplexing. While it may appear to be a fair comparison, in reality, CR requires considerably more computational resources (in terms of API calls). For instance, in the case of the Game of 24, the comparison is made with CoT-SC, which employs 16 samples and conducts a majority vote among them. This necessitates 16 API calls to the model. In contrast, CR maintains "n=4," indicating that at each step, the proposer makes four API calls, the verifier makes one call, and the reporter makes another call to determine whether the step constitutes the final answer. Consequently, a total of six calls are made at each step. With a maximum of 50 iterations, the maximum API calls can reach as high as 300. Therefore, for a fair comparison, it is imperative to evaluate CR against "k=300," as CR proves to be considerably more computationally expensive for a relatively marginal performance gain. The paper appears to lack an accuracy versus cost tradeoff graph, which would be instrumental in assessing this aspect. Can the authors please confirm if my understanding is accurate?
- Furthermore, in this methodology, there is a potential for a substantial amplification of errors, with a significant reliance on the verifier. If a verifier selects one of the reasoning chains proposed by the proposer, all subsequent chains will be built upon that initial choice. It becomes crucial for the verifier to make accurate decisions, particularly early in the decision chain. To gain insights into the potential propagation of errors throughout the chain, it is essential to conduct an error analysis concerning the verifier's accuracy at each step. 
- Lastly, it's worth noting that the paper bears a resemblance to numerous prior works, but a comprehensive comparison with them on the same dataset is notably absent. While the authors did compare their approach to PHP and the Tree of Thought method, there are other relevant works to consider. For instance, prior works such as "Faithful Reasoning Using Large Language Models" (Creswell and Shanahan), which follows a similar methodology of select, infer, and halt; "Maieutic Prompting" (Jung et al.), where they generate and prune; "Training Verifiers" (Cobbe et al), which involves generating multiple solutions and ranking them; "LM vs LM" (Cohen et al), in which one large language model can identify consistencies in another, and so on. A comparative analysis on similar datasets could assist the authors in providing more robust justification for their claims.

[Faithful Reasoning Using Large Language Models] : https://arxiv.org/abs/2208.14271
[Maieutic Prompting] : https://arxiv.org/abs/2205.11822 
[Training Verifiers]: https://arxiv.org/abs/2110.14168
[LM vs LM]: https://arxiv.org/abs/2305.13281

### Questions
Questions to be addressed are mentioned in the Weakness section. Please refer to that.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies multi-hop reasoning in LLMs and proposes an approach that has three components: 
* Proposer: proposes new derivations based on the existing premises, 
* Verifier: verifies if the new derivation proposed by the Proposer is valid, 
* Reporter: decides when to stop and report the result. 

The first and the second component are used to derive new premises until the reporter decides that there is enough premise for the final result to be directly predicted. Experimental results are provided on the FOLIO, AutoTNLI, Game of 24, and the MATH datasets.

### Strengths
- **Important Problem:** Multi-hop reasoning with LLMs stands as a pivotal research frontier, holding immense potential to enhance LLMs' ability.
- **Generality:** The proposed model seems general-purpose and can be applied to multiple domains.
- **Testing multiple models:** Experimental results are provided with multiple models at different scales.
- **Interesting results on the MATH dataset:** I found the improvements on the math dataset encouraging.
- **Cleaning FOLIO:** Since FOLIO is gaining popularity as a benchmark, cleaning the dataset is a good contribution.

### Weaknesses
- **Novelty:** The main components of the proposed model (decomposed reasoning, using verifiers, and using a halter model) have been explored in several existing work. The way the components have been combined also resembles some of existing works in the literature. For example, [1] has four components where the Selection and Inference modules can be seen as a variant of the Reporter in this work, the Halter can be seen as a variant of the Reporter, and the Value Function can be seen as a variant of the Verifier (to be clear, I'm not saying the components are identical).
- **Baselines:** Since multiple components from the existing work are used and given the high resemblance of the proposed approach to some of the existing work, I believe better baselines could be used. Some candidates include: 1- CoT + Verifier, 2- one representative decomposed reasoning approach, 3- selection-inference (and its follow-up [1]).
- **Statistical significance:** Comparing CR and CoT-SC in Table2, many of the improvements are in the order of 1-2% (with the exception of GPT3.5 results). For prompting techniques, given the high dependence of model performance on the prompts, I'm not sure how statistically significant these improvements are. The small size of the dataset is understandable, but that makes the statistical significance of these reported improvements even more questionable.
- **Game of 24 results:** I'm concerned about the Game of 24 experimental results. If I understand correctly, your approach for this dataset is almost equivalent to a naive brute forcing over all possible solutions (and I say "almost" because the LLM can of course rule out some of the obviously wrong cases; e.g., if the current state evaluates to 20 and the only remaining number is 4, the LLM probably understands that a summation is needed). It also seems like the model slightly changes here, because now it needs to keep a set of reached states and keep expanding them, as opposed to deriving valid conclusions from the previous premises.

[1] Faithful Reasoning Using Large Language Models Questions

### Questions
- The improvements on the MATH dataset are quite interesting. But I'm not quite sure if I understand where the improvement is coming from. In Figure 8, I see some hints for the case of CR but I don't see them in the case of CoT. Where do the hints come from? Has the model been prompted to generate the hints in the case of CR but not in the case of CoT? Is it the proposer who proposes the hints?
- What's the average number of model calls needed for CR?
- How does the prompt for CR components look like?
- Why not test on the entire FOLIO dataset and only restrict to the wiki part?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an approach for reasoning using LLMs called Cumulative Reasoning (CR).
The idea is based on using 3 instances of the same LLM (3 different prompts): a Proposer which suggests the next reasoning step; a Verifier that checks whether the proposed step is valid and accepts or declines it; and a Reporter which decides when to end the process.

The approach is mainly focused on reasoning using First-order-logic, and shows significant improvements on the FOLIO-wiki (which is a benchmark that is based on first-order-logic), as well as on tabular NLI, "the game of 24", and the MATH benchmark.

### Strengths
1. The proposed approach shows significant empirical gains.
2. The claims of the paper are especially important since they counter the recent claim that [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/pdf/2310.01798.pdf). As far as I understand, the gains in the proposed approach partially come from self-correcting.

### Weaknesses
1. The main weakness of the paper is that it's unclear where exactly the contribution comes from: the ability of the LLM to propose but then self-correctness? The grounding to First-order-logic (FOL)? Or the wider search among candidates and hypothesis? A thorough ablation study feels very needed.
2. It seems that the approach is different in every task: in FOLIO-wiki it relies mostly on FOL deductions, but in the Game of 24 it relies mostly in a wider *search* (like a wide beam search) that allows it to explore more hypotheses than the baseline. 
Is the proposed approach really reasoning better, or is it just a brute-force exploration?
I would like to know which gains come from the actual approach, while all side-improvements like a wider search are equal across all baselines. 
3. The method, explained in Section 3.1, is a bit tailored to problems that can be described as a series of "predicates" such as the Folio dataset from Han et al. 2022 ("FOLIO: Natural Language Reasoning with First-Order Logic").
I wonder how well it generalizes beyond tasks that are explicitly defined in FOL.
4. I am missing some actual prompts. It would have been useful to see the actual prompts that were used for each agent, as well as the code.

### Questions
### Questions
1. How do the prompts actually look like?
2. What exactly is the `n` parameter - the "number of generated intermediate propositions"? Is it like the number of beams in beam search? What happens when `n=1`, does the proposed approach still provide gains over the baselines such as CoT and SC? This is very important to understand, because if the gains are only coming from the wide beam search, maybe the idea can be applied to simpler methods as well.
3.  Are there examples for predictions in TNLI?
4. The nice background on Logic in section 2 is clear and nice, but I am not sure how is it needed for reading the paper. Some tasks are based on logic (FOLIO), and in that case, I understand why is it relevant. But when the task is not based on Logic, is the background of Section 2 relevant in any way?

### Comments
1. Most of the tables contain a column for Accuracy *and* another column for Error, where the Error is exactly `100-Accuracy`. This is redundant, and it makes the false impression as if there was an additional metric or twice the number of results.
2. The appendix is a bit confusing: some Figures contain the generated solution by both CoT and CR; some datasets have only the input and the ground truth outputs (e.g., Figure 5 and 6 and 7 without any model-predicted solution); while some Figures (e.g. in Appendix C.1) do not contain any caption, so I am not sure I can follow them.

### Summary
The paper has some weaknesses that should be addressed, especially by diving a bit deeper into **why** the proposed approach works,  which of its components provides the gains, and whether it is really reasoning better or is it just a brute-force exploration.
Further, the paper can also benefit from examples, concrete prompts and presentation.

However, I vote for acceptance, because I think that there is a conceptual novelty in this paper that results in actual benefit that the community needs to pay attention to. I will increase my score if provided with a deeper ablation study that teases apart the different contributing factors.

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent
