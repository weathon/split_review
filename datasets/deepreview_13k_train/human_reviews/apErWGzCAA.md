# Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Go-Explore is a powerful family of algorithms designed to solve hard-exploration problems built on the principle of archiving discovered states, and iteratively returning to and exploring from the most promising states.
This approach has led to superhuman performance across a wide variety of challenging problems including Atari games and robotic control, but requires manually designing heuristics to guide exploration (i.e., determine which states to save and explore from, and what actions to consider next), which is time-consuming and infeasible in general.
To resolve this, we propose \ouralgolong (\ouralgo) which greatly extends the scope of the original Go-Explore by replacing these handcrafted heuristics with the intelligence and internalized human notions of interestingness captured by giant pretrained foundation models (FMs).
This provides \ouralgo with a human-like ability to instinctively identify how interesting or promising any new state is (e.g., discovering new objects, locations, or behaviors), even in complex environments where heuristics are hard to define.
Moreover, \ouralgo offers the exciting opportunity to \emph{recognize and capitalize on serendipitous discoveries}---states encountered during exploration that are valuable in terms of exploration, yet where what makes them interesting was not anticipated by the human user.
We evaluate our algorithm on a diverse range of language and vision-based tasks that require search and exploration.
Across these tasks, \ouralgo strongly exceeds classic reinforcement learning and graph search baselines, and also succeeds where prior state-of-the-art FM agents like Reflexion completely fail.
Overall, \ouralgolong combines the tremendous strengths of FMs and the powerful Go-Explore algorithm, opening up a new frontier of research into creating more generally capable agents with impressive exploration capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Combines the Go-Explore -- a framework for solving hard-exploration problems -- with language models (LMs) to create LM agents that do better on search and exploration tasks.

### Strengths
**[Originality]**
The idea seems original, and creatively combines Go-Explore (a traditional RL approach for exploration) and LM agent tasks. 

**[Quality]**
The method shows strong performance over its baselines.


**[Clarity]**
The prompting procedures are well described and environments are well described 

**[Significance]**

The combination of RL exploration methods and LM agents feels both natural, thus this work opens up the possibility to further explore and improve components of the Go-Explore framework for better LM-agents.

### Weaknesses
While I quite enjoyed the idea and appreciate that using LMs with the go-explore framework is a promising direction, the main weaknesses with the current version of the paper is that many of the stated / emphasized claims are quite strong, which I do not feel they are properly back-ed up. See below.

> IGE ofers the previously impossible opportunity to recognize and capitalize on “serendipitous discoveries” (L24, L76, L95)

- The use of the word “serendipitous” feels un-rigorous and only added confusion. I don't know what this word means in context, nor how it contributes scientifically to this paper.
- Based on my reading, the authors generally use this word when describing the ability to identify which states should be archived to later explore further. This is an improvement over the original Go-Explore which use a heuristic (cell representation) instead of LM-preference. Perhaps it is better to just state this as-is.
- Further, the claim that this was “previously impossible” feels very strong. It is also unclear *what* was previous impossible? There exist previous work that use LM as a feedback to derive intrinsic motivation (e.g. Klissarov et al 2023, which the authors cite, L474). 

> IGE integrates well with various agent strategies ... and will only get better as capabilities of foundation models improve further (L103)

- The experimental evidence for this claim is in Table 3 right, which shows IGE does better on GPT-4 than GPT-3.5. One hypothesis is that IGE gets better as foundation models improve; another hypothesis could be that IGE is only well-tuned to GPT-4 and may not work in other / later models. Experiments across multiple foundational models with different capabilities will make this more convincing. 

> Key strength of IGE is that it is a strict improvement on top of any FM agent framework (L195)

- Unclear if the authors mean IGE is *complementary* to other FM agent frameworks; or that IGE will always be the best FM agent framework?

The strong claims contrast against the empirical results, which are good, but marginally so (e.g. between Fig 3 and 4, IGE is statistically significantly better than other baselines in 3 out of 13 settings between Figures 3 and 4 (evaluated base on overlapping 95 confidence interval bars). I feel that a more measured presentation can aid in paper clarity.

### Questions
1. Can the authors provide more details of how baselines are run? For instance, do all LM baselines get the same environment description for each game? 

2. Are there ablations of sensitivity of the approach to differences in prompts?

3. How exactly is the state conditional history (L199) implemented? Does it store a set of previously attempted actions for each seen state? Is it a buffer of (state, action) pairs?

4. Do you think the exploration problems Go-Explore addresses are also problems in the evaluation tasks? Specifically, detachment and derailment (L130)? 

5. How is state reset done (i.e. to explore from a certain state) in the provided environments?

6. In table 2, is there a difference between “classic go explore” and “ablated all 3 above” models?

7. Just out of curiosity, there do exist work that tackle exploration very explicitly in difficult games such as MineCraft [Wang 2023, Zhu 2023]. Is there a reason these methods are *not* reasonable comparisons against IGE?


[Wang 2023] Wang, Guanzhi, et al. "Voyager: An open-ended embodied agent with large language models." arXiv preprint arXiv:2305.16291 (2023).

[Zhu 2023] Zhu, Xizhou, et al. "Ghost in the minecraft: Generally capable agents for open-world environments via large language models with text-based knowledge and memory." arXiv preprint arXiv:2305.17144 (2023).

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper revisits the Go-Explore (GE) algorithm (Ecoffet et al., 2021) by letting a foundation model (FM) control three key operations performed on an archive of interestingly new states: (a) select a state to explore from (b) choose actions from the selected state, and (c) decide which state is worth keeping. The paper argues that FM successfully replaces GE's requirement to use hand-designed heuristics domain-specific pre-specified knowledge. IGE, with GPT4 as the underlying LLM, is evaluated on three families of environments (Game of 24, BabyAI, and TextWorld). It is claimed that the method outperforms baselines consistently across the board, sometimes being the only method that shows life (e.g., for Coin Collector). Finally, the following ablation studies are provided: (a) the importance of FM, (b) the size of the archive, and (c) the capabilities of FM.

### Strengths
* The paper considers a fundamental problem of managing the exploration-exploitation trade-off.
* IGE proposes to leverage the capabilities of LLMs to address deficiencies in the original GE and shows that it succeeds in three families of environments.
* The paper fits into the important line of work concerned with applications of foundation models in RL.

### Weaknesses
 * The choice of a setup for IGE matters, as it seems to work for deterministic environments. Is the extension to stochastic environments a fundamental limitation of IGE, or is there a "natural" extension? One example could be NetHack, which is a known hard exploration problem with long-horizon and credit assignment challenges.
* The IGE's procedure of selecting interesting states from the archive resembles a hierarchical search, where the planning is performed on high-level milestones or subgoals. Often such methods use Best-First-Search as a backbone planner, hence they jump freely between subtrees, similarly as IGE (see a discussion in lines 298-302 or 490-496). Can the Authors comment on that?
* Related to the above, how does IGE compare against algorithms like MCTS for hard deterministic combinatorial problems (like chess or go)?
* What is the relation of IGE to GFlowNets, which searches through a design space to generate samples proportional to a specified reward function?
* What important real-life problems can be expressed as exploration and solved via IGE? Say, interesting chess or go states, novel mathematical theories or proof ideas, useful molecules, etc.
* Can the method accelerate research on open-endedness, which is often formulated as an unsupervised exploration problem?
* How robust is the method?
	* LLMs are known to be unreliable and have a long list of failure modes.
	* Are there any biases with respect to some environments games, i.e., the method performing better in the environments that were prominently represented in the pre-training dataset?
	* Conversely, does IGE underperform for environments that were underrepresented in the training dataset or that require a set of rules or wiki?
* How can IGE be augmented with the inclusion of environment rules, RAGs, and tools? How hard is it to set up IGE for a new task? How much work is expected on the prompt engineering part?
* What is the performance of open-sourced models? 
* IGE is an in-context method. What could be achieved that currently is out of reach if the method allowed fine-tuning (or RL training)?
* What could be the implications for the current RL algorithms regarding the potential benefits stemming from IGE providing better data?
* Can we formulate an inverse-IGE problem by designing synthetic datasets to discover the "definition of interestingness of LLMs"?


Other:
* In Algorithm 1, lines 3, 8, 10, should account for the fact that "$\gets$" typically stands for assignment operator, not "add to a set" operator.

### Questions
See above

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
4

### Summary
Summary: The authors propose a method that reconceptualises the original Go-Explore method to use the pre-trained knowledge contained in large foundation models. 
For this, the original components of Go-Explore such as keeping a state archive and exploring from a previously attained state are defined for a language foundation model. 
The idea behind this is that foundation models are better able to reason about what defines an interesting (novel) state or behaviour, while exploiting the creative abilities of foundation models. The authors test on 3 different environments. 2 text based environments and one environment where the visual 
Features are described in terms of text.  The authors show that intelligent go-explore is able to solve these environments in very few steps while also outperforming other foundation model based methods. 


Overall, this is a well written and interesting paper. I think the idea of creating a foundation model based exploration algorithm that follows along the lines of Go-Explore is clever and perhaps shows a more generalised way to exploit foundation models for exploration. 
While the authors ablate their method well, I feel more interesting ablations would concern the capacity of the foundation model itself in terms of how complex the observation space can get and how different prompts, i.e., conditioning affects the exploration. For instance,
Did the foundation model hallucinate during some runs? What do these hallucinations look like? I think this should even be achievable with the presented BabyAI environment. See more detailed info below.

### Strengths
- Exploiting the pre-trained biases of LLM for RL is an interesting idea and so far largely unstudied for exploration in reinforcement learning
- I like that the foundation model is defined in terms of a well known exploration algorithm such as Go-Explore, since it shows how concepts from exploration can be transferred to large foundation models.
- The paper is very clear and well written, while providing thorough ablations methods components such as in Section 4.3.

### Weaknesses
 - This paper argues against hand-crafted features i.e. heuristics, however having to transfer the environments to a prompt based structure is also a hand crafted feature space.
- The paper states in the abstract that the appeal of using foundation models is making use of the foundation models capabilities of reasoning ahead or capitalising on serendipitous discoveries.  While the results are good, can you show examples of trajectories IGE creates compared to a normal RL algorithm that you could argue are serendipitous?

### Questions
- How would you transfer this method to continuous state-action spaces? Did you observe a limit regarding how large the state archive can become? For instance int the BabyAI environments the observations are discrete, that is each observation can be mapped to a distinct vector. I imagine this becomes more problematic the larger the environment becomes. 
- Did the foundation model hallucinate while creating the trajectories? This would be interesting to see, since failure modes for foundation models seem to differ from traditional RL models.

### Soundness
2

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
The authors propose Intelligent Go-Explore (IGE), an extension of the original Go-Explore algorithm that replaces manually crafted heuristics with foundation models (FMs) to guide exploration. In the original Go-Explore, heuristics were required to identify 'interesting' states, whereas in IGE, this is determined by querying the foundation model, which leverages its pretrained knowledge to make decisions. Interesting states are stored in an archive, and the foundation model is queried with which state should be explored next. Additionally, instead of relying on random action sampling, IGE uses the foundation model as a decision-making agent to choose actions intelligently. The authors evaluate IGE in controlled environments (BabyAI and Game of 24), showing that it outperforms previous foundation model-based agents in these tasks.

### Strengths
- The integration of foundation models with the Go-Explore framework is a noteworthy contribution that can alleviate several of the inflexible inconveniences present in the original framework, such as hand-crafted heuristics and random exploration.
- The authors perform a solid empirical evaluation and compare it to several foundation model agent baselines, demonstrating significant performance gains.
- For each of the proposed additions to the original algorithm, a solid ablation study is performed where each addition is omitted and evaluated, and IGE is also compared to the original Go-Explored in this experiment. 
- The authors do not limit their approach to text-based representations and demonstrate that IGE can also be applied with visual observations.

### Weaknesses
 - One of the main contributions of the paper is alleviating the original Go-Explore from manual handcrafting of domain-specific heuristics. However, by replacing this part of the process with foundation models, quite extensive and domain-specific prompt-engineering is required instead (as shown in Appendix B). The provided domain-general prompts, while an improvement, still require careful crafting of factual environment descriptions, which can be as, or in some cases more, effortful than defining heuristics in the original Go-Explore. The performance drops observed when using these minimal prompts also raise concerns about the robustness of IGE to prompt variations.
- Given that the environments used in the paper are relatively controlled and intuitive, and the foundation models were provided with detailed explanations of the environment dynamics and objectives, it is not clear how well the decision-making of the foundation models would work in more complex (and actual hard-exploration) environments. For instance, the Game of 24 is a relatively simple mathematical puzzle, where the exploration space is highly constrained and the rules are clear and deterministic. As such, it doesn’t pose a true hard-exploration challenge, which is what Go-Explore and IGE are meant to address.
- Building on the previous weakness, the original Go-Explore algorithm was demonstrated across the Atari suite, including hard-exploration games like Montezuma's Revenge. In this IGE paper, the authors compared Go-Explore in specific environments where IGE performs well, but it would have perhaps made more sense to evaluate it in the Atari suite, where we already know Go-Explore performs well. It is not clear that a foundation model would be able to deal with the complexity of Atari games both in judging interesting states and in decision-making. Given that the main claim of the paper is improving upon the original framework, a comparison on that suite would have provided a more direct measure. While a full evaluation across the entire suite may be computationally expensive, a comparison on a simpler environment like Freeway or MinAtar would have been valuable.
- Although the authors touch upon this briefly, IGE appears computationally expensive, as the foundation model is presented with the entire archive of states to select a state, filters states, and is also queried for every individual action. While this may be feasible in the small environments used in the paper, it’s unclear how scalable the approach would be to larger environments or longer-horizon tasks. 
- Following this, according to the ablation study, the primary driver of IGE’s performance is the action selection guided by the foundation model, compared to random action selection. However, foundation models tend to only perform well in relatively intuitive and deterministic domains where decisions are relatively straightforward. In more complex or large-scale environments, a reinforcement learning exploration policy will likely be necessary. This raises an important question: if the primary performance gains from using IGE come from action selection, and these foundation models struggle in more complex environments, are the gains from using foundation models for state selection and filtering substantial enough to justify its use? The ablation study shows that these gains are minor (yet introduce significant computational overhead), calling into question the overall value of IGE when considering scalability and generality.
- The paper occasionally comes across as over-optimistic with respect to the proposed algorithm and e.g. speculates that its solutions can easily be used for downstream RL tasks or infinite in-context learning with no evidence supporting this. A more grounded discussion of IGE's limitations would benefit the paper.

### Questions
- Could you provide more details on the sensitivity of the prompts used with IGE? For example, in the BabyAI environment, you explicitly prompt the model with instructions such as 'do not repeat actions if they have no effect.' How much does IGE's performance depend on these kinds of statements?
- Given that the action selection of the foundation model has the most significant impact on IGE's performance, have you explored other exploration approaches? It seems that random actions and foundation model-driven actions represent two extremes. Have you considered comparing IGE to a relatively simple information-seeking policy or other exploration strategies that could computationally be much cheaper to use?

### Soundness
2

### Presentation
3

### Contribution
2
