# AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs

- Decision: Accept
- Avg Score: 7.17
- Scores: 3, 8, 8, 8, 8, 8

## Abstract
In this paper, we propose \textbf{\modelname}, a black-box jailbreak method that can automatically discover as many jailbreak strategies as possible from scratch, without any human intervention or predefined scopes (e.g., specified candidate strategies), and use them for red-teaming. As a result, \modelname~can significantly outperform baseline methods, achieving a $74.3\%$ higher average attack success rate on public benchmarks. Notably, \modelname~achieves an $88.5$ attack success rate on GPT-4-1106-turbo. In addition, \modelname~is a unified framework that can incorporate existing human-designed jailbreak strategies in a plug-and-play manner. By integrating human-designed strategies, \modelname~can even achieve a higher attack success rate of $93.4$ on GPT-4-1106-turbo.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a Blackbox jailbreak method named AutoDAN-Turbo that automatically discovers jailbreak strategies without human intervention. It has been evaluated on open-sourced and closed-sourced LLM such as Llama 3 and GPT-4 and achieved high attack success rates.

### Strengths
The paper is well-organized, with clear descriptions of the methodology, experiments, and results. The method has been evaluated on several different LLM models and outperformed the baseline. The automatic strategy generation is novel although it is computationally expensive.

### Weaknesses
The methodology's scalability could be limited, comparing response embeddings with all keys in the strategy library might not be feasible for larger datasets.

Lack of enough novelty and applicability

### Questions
How many test cases were used to achieve the reported 88.5% success rate on GPT-4-1106-turbo? 

Considering the importance of diverse test cases, how does the method handle diversity given the apparent reliance on a greedy approach in the Jailbreak Strategy Retrieval module? 

What is the typical computational time required to generate prompts using AutoDAN-Turbo? 

Are there specific scenarios or model configurations where AutoDAN-Turbo underperforms, and can the authors provide insights into its limitations in such cases? 

How are they different from the below paper?

Liu, Xiaogeng, et al. "Autodan: Generating stealthy jailbreak prompts on aligned large language models." arXiv preprint arXiv:2310.04451 (2023).

### Soundness
3

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
3

### Summary
The authors propose an automated jail breaking framework that can be used for red teaming. The method is a black box, requiring no access to model weights as well as no human intervention.  The method utilizes lifelong learning techniques to discover strategies and leverage them for jailbreak attacks. The method consists of three modules, (1) Attack generation and exploration (2) Strategy Library Construction; (3) Jailbreak Strategy Retrieval.  Each of these modules contributes to the final attack generation.

### Strengths
1. The paper is well written and the authors do a good job in clearly explaining their approach.
2. The proposed method significantly outperforms baselines, and automated the strategy discovery makes the method scalable. 
3. Incorporation of existing human designed strategies in a plug and play manner is useful.

### Weaknesses
1. While the authors do acknowledge it, the cost of running the proposed method is high.
    1. The method requires running the life long stage to be run for multiple iterations, which can be expensive (line 249). It would be interesting to see how the ASR improves over each of the 5 rounds of attack.
    2. It would be helpful if the authors can include the total run time (train + test) for all the methods
    3. In lines 212-214, Are the existing categories provided as context to the summarizer LLM? doesn't this increase the total context length as the strategy library grows?
2. An important aspect of red teaming apart from ASR is the diversity of the generated attacks, ie., how different are the attacks from each other. I would encourage the authors to discuss this as well.
    1. For instance suppose we fix a Malicious Request, how many successful attacks (jailbreaks) can the method generate? How different are they from each other?
    2. How different are the generated attacks (jailbreaks) form each other across all of the malicious requests in the dataset?

### Questions
See weaknesses. 

1. In Table 2, which model is used as the attacker for AutoDAN-Turbo?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes AutoDAN, a new jailbreak method for LLMs that iteratively discovers new jailbreaks by developing a jailbreak library. This technique involves several steps:
* An attack generation and exploration module creates new attacks (potentially based on a certain attack strategy);
* The target model provides a reply;
* An LLM evaluates the effectiveness of the attack;
* If no successful strategies are found, AutoDAN generates new attack strategies.

The authors then study the effectiveness of this approach on a variety of open-source and closed-sourced models. They also study the transferability of such strategies across different datasets and whether human-developed strategies lead to improvements in success rate. Finally, they report the average number of queries of the attack.

The technique, while not revolutionary, achieves major improvements in success rate, transfers well across datasets, and is easy to extend. The paper is well-written, and the experimental evaluation leaves few doubts about the technique’s effectiveness. For this reason, my recommendation is Accept.

### Strengths
The paper is well-written and the technique checks all the main boxes for a properly applicable attack (black-box, generalizable, automatic, supports expert knowledge). While other techniques share these properties, AutoDAN-Turbo also has great performance, as shown by an in-depth experimental evaluation.

The authors also study the transferability of attack strategies, finding a significant level of transferability, and show that human-developed strategies can also lead to success rate improvements.

### Weaknesses
My main concern is related to how AutoDAN-Turbo fits in the literature: while the Related Works section lists plenty of other techniques, very little room is dedicated to how AutoDAN-Turbo differentiates itself from other attacks, which makes it very hard to establish its novelty just by looking at the paper. For instance, the paper does not describe how it differentiates itself from AutoDAN (which shares the same intuition as AutoDAN-Turbo of using automatic search of jailbreaks, but using Genetic Algorithms instead). Due to space constraints, my recommendation would be to add an Appendix section comparing AutoDAN-Turbo with the most similar techniques (e.g. automated jailbreaks).

Other issues include the fact that the attack needs to build up a strategy library: as stated in L539, this is not a major problem, since in practice one can use an existing strategy library, but it does make the comparison with simpler techniques (which do not require such a training step) a bit unfair. Reporting data on the average query number of AutoDAN would also be appreciated, as it would simplify the comparison with AutoDAN-Turbo.

That said, in the grand scheme of things, these issues are quite minor.

Additional notes:
* The labels in Figure 4 are too small to be legible.
* I’d encourage the authors to share the code of their experiments. If anonymization is an issue, there are some free tools (e.g. 4open.science) that host anonymized repositories.

### Questions
My main question, which is also discussed in the "Weakness" section, is: how does AutoDAN differentiate itself from other automatic jailbreak strategies?

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
4

### Summary
This paper introduces a jailbreak method capable of automatically generating black-box attack prompts. The approach comprises two main phases: strategy discovery and attack generation. In the strategy discovery phase, the method identifies the most effective strategies from scratch, without relying on external knowledge. During the attack generation phase, it generates attack prompts based on a constructed strategy library, which may be sourced from an external knowledge base or derived from the strategy discovery phase. The method achieves SOTA performance in attacks across various target LLMs.

### Strengths
1). The strategy discovery phase of AutoDAN-Turbo can generate diverse attack strategies from scratch, allowing the most effective strategies to be saved in a library for efficient use in future attack generations.

2). The paper conducts extensive empirical evaluations across numerous SOTA LLMs, demonstrating superior performance compared to multiple existing SOTA methods.

### Weaknesses
1). The reliability of the scorer LLM (e.g., Gemma-7B-it) is uncertain. Comparing its performance against human judgment would help demonstrate whether it aligns well with human evaluations.

2). Assigning a 1-10 scale maliciousness score to a conversation may be challenging for an LLM. A more reasonable approach could be ranking or sorting conversations rather than assigning hard numerical scores.

3). The reliability of the summarizer LLM is also unclear. A comparison with human-generated summaries would be beneficial.

4). The methodology description in Section 3 is somewhat difficult to follow. Including an algorithmic outline could enhance clarity for readers.

5). Minor comment: Line 371 mentions that the same total iterations are used for baseline methods. However, for optimization-based methods like GCG, this comparison may be unfair. GCG’s computational cost per query is significantly lower than AutoDAN-Turbo, as it generates only 20 new tokens per iteration with a much shorter input sequence length.

### Questions
See the Weaknesses for my questions.

### Soundness
3

### Presentation
2

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
AutoDAN-turbo is a blackbox jailbreak method to discover new jailbreak attacks without human intervention or predefined scope and it can also incorporate human strategies. AutoDAN-turbo achieves an 88.5% and 93.4% (with human intervention) ASR on GPT-4-1106-turbo.

The AutoDAN-turbo pipeline mimics a lifelong learning agent setup, where the agent can discover many jailbreak strategies and also combine & utilize these strategies. It contains 3 key modules:
- Module 1: Attack generation and exploration
	- Conditioned on a malicious request, the attacker model generates a jailbreak attack $P$ using specific jailbreak strategy
	- Target LLM generates sth $R$ in response to the jailbreak
	- Scorer LLM returns a numerical score $S$, ranging 1 (attack fail) to 10 (attack success)
	- All these tuples  $\{P_i, R_i, S_i\}$ are stored in the strategy library.
	- At the cold-start stage, the attacker LLM can generate jailbreaks wo strategy.
- Module 2: Strategy library construction
	- Randomly pick two pairs of tuples, $i, j$, and if $S_j > S_i$ , we would say $\{P_j, R_j, S_j\}$ explored some *new strategy* leading to improvement over $\{P_i, R_i, S_i\}$. Then we use a LLM to summarize the improvement and store that as strategy in the library.
	- Note that the paper defines "jailbreak strategy as schemes that improve jailbreak scores from S_i to S_j".
	- The strategy output is a dictionary containing keys: "strategy", "definition" and "example".
	- The library is kv store, where the key is text embedding of the response $R_i$ and the value is $S_j - S_i$.
- Module 3: Jailbreak strategy retrieval
	- Given a malicious request $M$, generate $\{P_i, R_i, S_i\}$, retrieve most similar kv pairs based on $E(R_i)$ to select the most effective strategy associated with $R_i$.
	- If the highest score > 5, use it directly as effective strategy; if between 2-5, use all these strategies in this range; if < 2, treat it as ineffective strategy and inform the attacker LLM so.

The experiment is using HarmBench data as malicious request seeds and got SOTA attack results in HarmBench.

### Strengths
- Results are very impressive in comparison to other jailbreak attack methods.
- The definition of "jailbreak strategy" is very interesting. Using the language to summarize the difference between two jailbreak attacks as a way to identify the fact that contributes to the different attack results is fascinating.
- The design of utilizing the kv store and

### Weaknesses
 - I find the claim of "without any human intervention or predefined scopes" is a bit misleadning. AutoDAN-turbo still needs malicious requests as seeding inputs, and imo that's clearly human defined scopes.
- Lack of some ablation studies to demonstrate the effectiveness of the system design. For example, why we have this efficient / inefficient strategy splits based on [2, 5] scores. Feels a bit arbitrary. Does it have a big impact on the results?

### Questions
- Other than using embedding of R_i as the key, consider summarizing the key issue (more concise, more unified, maybe even keyword based) in R_i and then do embedding of that? Would you expect difference in results?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces an automatic framework to continuously discover new jailbreak strategies to efficiently and effectively improve the jailbreak attack on LLMs. The framework consists of three modules: i) attack generation and exploration, where the attacker LLM generates the jailbreak prompt based on the malicious request and the retrieved jailbreak strategies, the target LLM generates the response, and the scorer LLM evaluates the effectiveness; ii) strategy library construction, where the attack logs are summarized by a summarizer LLM to generate the jailbreak strategies which are then added to the strategy library; iii) the jailbreak strategy retrieval, where the strategies are extracted based on the similarity between the responses of the target LLM and the responses associated with the retrieved strategies. Extensive experiments show that the proposed framework satisfies several desiderata, demonstrating its effectiveness.

### Strengths
I have to admit that I am not fully familiar with the area of jailbreak of LLMs. However, I believe this paper has made a good contribution to this area by proposing an automatic framework that can discover new jailbreak strategies to improve the attack's effectiveness.

In AutoDAN-Turbo, each module has been clearly defined, and the interactions among the different modules are clear and easy to understand. In each component, the workflow is clear, and the intuition of the design seems reasonable for me, e.g., the use of a warm-up stage to first construct an initial jailbreak strategy set, the use of the response embedding as the key in the strategy library.

The experimental plan is well-designed and executed. The experiments also show the good performance of the proposed framework.

### Weaknesses
I didn't find any fatal flaws in the paper, but only some minor questions:

1. In experiments, the scorer LLM is fixed to Gemma-7B-it. What is the influence of the choice of the scorer LLM? I feel that the scorer LLM is also quite important in the whole framework because it impacts the construction of the jailbreak strategies, which then in turn influences the performance of the framework. Is that the case?

2. I feel a bit confused when running the framework at the first iteration (assuming that there are some strategies in the library). According to the retrieval module, strategies are selected based on the similarity between the responses associated with the strategies and the responses generated by the target LLM. But at the first iteration, when prompting the attacker LLM to generate the jailbreak prompt, we need the retrieve some strategies. However, there is no response generated by the target LLM yet. So, how to construct the prompt for the attacker LLM?

3. Some typos: Line 207: “the summarizer LLM …” -> “The summarizer LLM …”,

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3
