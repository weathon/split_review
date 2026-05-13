# NNetscape Navigator: Complex Demonstrations for Web Agents Without a Demonstrator

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
We introduce NNetscape Navigator (\ours{}), a method for training web agents entirely through synthetic demonstrations. These demonstrations are collected by first interacting with a browser to generate trajectory rollouts, which are then retroactively labeled into instructions using a language model. 
Most work on training browser agents has relied on expensive human supervision, and the limited previous work on such \emph{interaction-first} synthetic data techniques has failed to provide effective search through the exponential space of exploration. In contrast, \ours exploits the hierarchical structure of language instructions to make this search more tractable: complex instructions are typically decomposable into simpler subtasks, allowing \ours to automatically prune interaction episodes when an intermediate trajectory cannot be annotated with a meaningful sub-task. We use \ours demonstrations from a language model for supervised fine-tuning of a smaller language model policy, and find improvements of 6 points on WebArena and over 20 points on MiniWoB++, two popular environments for web-agents. Notably, on WebArena, we observe that language model policies can be further enhanced when fine-tuned with \ours demonstrations derived from the \emph{same} language model. Finally, we collect and release a dataset of over 6k \ours demonstrations on WebArena, spanning a diverse and complex set of instructions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers the task of instruction following for web browser agents, and proposes an approach for synthetic data generation to create data sets that can be used to fine tune LLM-based web browser agents. The authors make the argument that current "instruction-first" approaches to synthetic data generation are inadequate, and propose an "interaction-first" approach to data generation in which a sequence of website interactions is generated and then retroactively labeled to enable fine tuning. The authors' empirical results suggest that this kind of data generation leads to improvements on some standard benchmarks for browser agent performance. The paper also introduces a large-ish (several thousand data points) fine-tuning data set generated with the proposed retroactive labeling method.

### Strengths
Overall the paper has many strengths. The target task and range of applicability for the proposed method are clearly articulated, and the core idea that is proposed ("retroactive" or "interaction-first" labeling) is very clever. The empirical results from the fine-tuning experiments seem reasonably good overall, though see discussion below in weaknesses for some points where fine tuning results could be clarified. It is clear that effort has been put into making the work reproducible - the prompts used for each of the system components are available in the appendix, and this helps to understand what's going on even where descriptions in the paper could be clearer. The writing is, on balance, reasonably clear and free from distracting problems related to grammar or diction. 

Overall, I really like the idea of this paper, and feel like it could be broadly useful for synthetic data generation in many contexts.

### Weaknesses
I am inclined to believe the core claims of the paper, and I think the ideas of the paper are quite good. I have a number of issues with the presentation of the work.

- Clarity. There are a few points where the paper could be clearer. For instance, the introduction's discussion of your pruning approach (line 096) could be clarified, since trajectories aren't yet defined, and trajectory prefixes as the basic unit of labeling is not necessarily an obvious choice. More significantly, on line 125 you should clarify that it is the elements of the observation and action spaces that have string representations, rather than the spaces themselves. This becomes clear from context as you read the paper, but it would be better to just say what you mean as you introduce the formalism. At several places you use the word "plausible" (for example on line 198) to refer to the generated instructions, but as far as I can see you don't define what "plausible" means or attempt to quantify it. Given that the quality of the generated instructions is critical to the viability of your approach, it surprised me that you did not put more effort into directly evaluating those instructions. I would guess that the indirect metric of "how good are the models that are trained on this data" is an acceptable proxy for instruction quality, but I'm sure you would strengthen your argument with some more direct assessment (of some kind; I concede that how best to do this is not obvious).

- Notation. Your notation in Sections 2 and 3 looks pretty textbook for RL-type applications, but I'm not sure it entirely represents the task you're working on. For example, it appears from line 124 that $\pi$ is a probability distribution over actions, but then line 129 makes it clear that $\pi$ is in fact a probability distribution over strings. This is also hard to interpret consistently with the prompts from the appendix, which make it seem like you are interested in strings of text sampled from models rather than the probabilities of these strings. I know that you need to include a certain amount of mathematical notation to get papers accepted, and that ultimately this notation is not really necessary for understanding the contributions of the paper, but if you're going to use the notation it would be helpful if some of it were more clearly defined. For instance, I would specify whether $\mathcal{A}$ is a finite set of possible actions (as one might guess looking at listings 1 and 8 in the appendix), or if $\mathcal{A}$ is a much larger set of possible outputs from an LLM. Then at a minimum I would specify whether the policies are working directly with probabilities or with strings, and whether those strings are drawn from a giving finite set or if they can be freely generated by some model.

- Reward model. In the text of the paper (line 199) it seems like you use binary rewards. This is not consistent with the prompts for $s_{\text{LM}}$. I think you clarify this on line 344, but your use of the same notation for the reward models that are binary and graded is slightly confusing.

- Results. Cross website generalization looks surprisingly weak, which is a little troubling for your main claims. Also, the results tables would benefit from a careful review. In particular, make sure you have units on all your numbers, either in the table itself or in the caption or in the main body. For instance, the Table 1 caption is good, but the captions for Tables 2, 3, 4 are not necessarily clear. In particular, with Table 4 and the discussion on lines 415 to 417 I'm not convinced that increases of 0.06 and 0.13 are significant because I don't entirely know what units those numbers have. Is the range of reward here 0 to 1 or 1 to 5? I believe that this can be clarified in the text of the paper, and that you should do so.

- NNetNav-6k. The major issue here is that I'm not clear whether or not you did anything with this data set other than release it. It's not clear that "diversity of verbs" or "instruction length" have any bearing on whether or not the dataset is any good, and it doesn't look like you've used the data set to fine tune any models (if this is not correct you should emphasize your use of the 6k data set more in the main body of the paper). Overall there's no assessment of quality for the data set as far as I can tell. I'm not sure that mentioning this data set adds anything to the paper other than length, given the current discussion of the data set in the paper. I fully believe that the data set would be useful, so if there's any way to express that in the main body of the paper you should do so.

Less importantly, I'm surprised that you found that GPT-4o and Llama-3 had "similar quality" based on my experience with those models. This is the kind of claim that would benefit from more rigorous justification.

Also (and this is just a quibble): I strongly doubt that web browsing is, in general, a deterministic process. But again, I think you're probably only saying that to introduce some notation.

### Questions
Biggest question: are you claiming novelty of the retroactive labeling approach? If so, I would emphasize this more in the paper because it's a good idea. If you are not claiming novelty, I would point out the related work more clearly.

Have you considered retroactive labeling in domains beyond browser agents? The idea feels generally applicable. Maybe worth a mention in the conclusion, since the current conclusion is just a laundry list of things you've done.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on the problem of building an LLM based agent that can follow instructions by executing some actions (e.g. to perform web tasks). To achieve good instruction grounding this work focuses on collecting demonstrations. However, since expert demonstrations from humans can be expensive, they focus on using an exploration policy (an LLM) to generate action data. Heuristics are used to verify if the actions generated by the LLM indeed follow the true instructions. Once some data is collecting, hindsight relabeling is performed to re-label the original instruction (\hat{g}) and a reward is assigned. This data is then used to train a smaller LM and improve its performance using SFT. Experiments are shown on two domains. However, in  one of the domains (MiniWoB++) . On the harder (WebArena) domain, the approach shows  some improvements compared to a zero-shot baseline (however, this is a very weak baseline).

### Strengths
The paper is easy to follow and overall does a decent job at grounding different things. The paper also releases the demonstrations they have collected using the propose approach (although with a different LM than used for the paper).

### Weaknesses
The overall methodological contribution seems quite heuristic driven. For instance, the approach relies completely on \pi_explore, which is almost similar to the zero-shot baseline.  In scenarios where \pi_explore proposes decent actions this is probably reasonable, but if the environment is challenging then the exploration policy can be quite bad (e.g. if many different actions are quite similar). In this scenario, \pi_explore will not be able to collect any good high quality data.

There are other parts of the algorithm that are quite heuristic driven.  For instance, state changes between transitions are summarized using an LM (\delta_t) (this can be noisy (e.g.  the LM summary misses important details). This is probably not a huge problem for the datasets being considered but do the authors think that this can a potential concern which makes this approach hard to scale.

*Human demonstrations:* While human demonstrations are expensive, they can be much more higher quality. I think using a limited number of human demonstrations would be an important baseline for this work. Additionally, such limited number of human demos can also make the \pi_explore much better, which can potentially result in more higher quality data (compared to an off-the-shelf model).

*Why not train on the larger set of demonstrations?*  The authors have collected and are releasing a larger set of demonstrations but the training demos used in the paper are much smaller, why not use all the demonstrations and then compare the result? Also, it would also be interesting to see how the performance of the model scales as more demos are provided for SFT.

*Comparison to NNet (ablation baseline):* The ablation baseline is quite interesting, it basically takes just the instructions generated from this approach. These instructions are then used zero-shot with another LM to generate trajectories that will be used for SFT. From a results perspective, this approach is quite competitive with the proposed approach (e.g. only 1.2 points delta from proposed approach on WebArena). This is also when no data filtering was performed on this baseline.  Did the authors further explore and try to improve this baseline? Also, it would be interesting to see how the rollouts from this baseline differ from the proposed approach.

### Questions
please see above

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes NNetscape Navigator (NNetnav), a pipelined approach where firstly exploration LLMs (gpt-4o-mini, Llamma-3-8B-Instruct, Llamma-3-70B-Instruct, etc) generate the random exploration trajectory without specific instructions, and then provide “hindsight” instructions to the collected exploration trajectories while removing redundant actions. By leveraging such synthetic demonstrations for finetuning, LLM agents (based on Llamma-3-8B-Instruct) can improve their performance. The experiments are conducted on MiniWoB++ and WebArena. The paper is planning to release the synthesized trajectories, NNetnav-6K, to the community.

### Strengths
- [S1] Compared to the baseline methods (Zero-Shot, SFT(instruction-first), SFT(NNetnav+Distil.)), NNetnav successfully improve the preformance on MimiWoB++ and WebArena.

### Weaknesses
 - [W1] The proposed pipeline is quite similar to the BAGEL (Murty et al., 2024), which proposes an exploration and relabeling approach for data collection in web navigation. BAGEL proposes both instruction-first, and demonstration-first methods, and demonstrates that the demonstration-first method performs better than the instruction-first one, which is the same consequence as this paper. In this sense, I think the novelty is very limited.

- [W2] It is unclear whether the achieved performance is meaningful to the community or not. For instance, MiniWoB has been well-studied and is the benchmark where capable LLM-based agents can resolve almost perfectly (90-95%; e.g. Kim et al., 2023, Zheng et al., 2023, Furuta et al., 2023). It is good to see the improvement from the baselines, but achieving 48% success does not provide progress in this area. WebArena also has 10-15%-success-rate baselines and over 30% success SoTA agents. The 7.2% success is actually not a good result. In addition, Patel et al., (2024) also propose a synthetic data collection pipeline in web agents, which starts with  7.14% success and results in 9.36% success. The methodologies of those two are similar, and the absolute performance of this paper does not provide progress on the benchmark. 

- [W3] The effectiveness/quality of NNetNav-6K is quite unclear. As far as I read the paper, this dataset is different from the data where the agents were trained in this paper (for table 1 or 3; collected by gpt-4o-mini or Llamma-3-8B-Instruct). I think there are no experiments with NNetNav-6K. Also, the dataset size for the main experiment is 9.7K (from Table 6), but the future-released data is smaller (6K). Considering the performance improvement is marginal in the main experiments, it is very hard to imagine that NNetNav-6K can provide a significant gain.

### Questions
See the weakness above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a method for synthetic data collection of web trajectories for llm finetuning. The method does the following:
- Use an LLM to explore the web based on a predefined persona.
- Prompt the LLM to predict state changes between consecutive actions.
- From the sequence of state changes, generate a plausible instruction for the trajectory using the LLM.
- Evaluate instruction quality with an LLM-based reward function.
- Finetune an LLM on the generated and labeled trajectories.

### Strengths
- Proposes a method for generating synthetic trajectories using LLM exploration and hindsight relabeling for web applications.
- Demonstrates that training on these trajectories leads to better performance compared to instruction-first trajectories and zero shot baselines on web arena.
- Synthetic data generation without human annotation for improving llm agents on the web is an important problem, and well motivated in the paper.

### Weaknesses
 - Lack of clarity on whether the reward LLM is applied to filter the instruction-first baseline.
- Insufficient details on the use of the reward model and filtering of incorrect trajectories.
- No error analysis or discussion of limitations.
- Performance gains are minor for certain websites.
- No comparison with previous methods that report results on the web arena.

### Questions
1. How exactly is the reward score used? Why is the reward function only applied when R=0? How do you determine the threshold for the 1-5 rating? Why stop data collection at R=0 instead of discarding the sample and continuing the trajectory?
2. Is there any filtering applied to the instruction-first SFT baseline, such as using the reward LLM to filter bad trajectories?
3. Why use different LLMs for NNetNav collection (GPT) and training (LLaMA)? Can the same LLM be used for both collection and inference?
4. Why is there no improvement on certain tasks, like Reddit and GitLab? More analysis of the errors and limitations in the collection method is needed.

### Soundness
2

### Presentation
2

### Contribution
2
