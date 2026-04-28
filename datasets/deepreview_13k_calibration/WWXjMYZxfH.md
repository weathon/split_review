# MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 8, 8, 6, 3

## Abstract
Reinforcement learning from human feedback (RLHF) has demonstrated effectiveness in aligning large language models (LLMs) with human preferences. 
However, token-level RLHF suffers from the credit assignment problem over long sequences \citep{DBLP:journals/pami/BengioCV13}, where delayed rewards make it challenging for the model to discern which actions contributed to successful outcomes. This hinders learning efficiency and slows convergence \citep{pmlr-v32-mann14, JMLR:v24:21-1213}.
In this paper, we propose MA-RLHF, a simple \textit{yet} effective RLHF framework that incorporates \textit{macro actions}--- sequences of tokens or higher-level language constructs---into the learning process. 
By operating at this higher level of abstraction, our approach reduces the temporal distance between actions and rewards, facilitating faster and more accurate credit assignment. This results in more stable policy gradient estimates and enhances learning efficiency within each episode, all without increasing computational complexity during training or inference.
We validate our approach through extensive experiments across various model sizes and tasks, including text summarization, dialogue generation, question answering, and program synthesis. Our method achieves substantial performance improvements over standard RLHF, with performance gains of up to 30\% in text summarization and code generation, 18\% in dialogue, and 8\% in question answering tasks. 
Notably, our approach reaches parity with vanilla RLHF 1.7x to 2x faster in terms of training time and continues to outperform it with further training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The current manuscript proposes to tackle the credit assignment problem when aligning large language models (LLMs) to human preferences via reinforcement learning from human feedback (RLHF). The core idea is to consider a group of tokens as a macro action, instead of individual actions, and use rewards accumulated within a macro action with proximal policy optimization (PPO) to align the language model. This approach is labeled MA-RLHF. Experiments on three tasks (text summarization, dialog generation, question answering, and program synthesis) show improvements of MA-RLHF over PPO for a chosen LLM (Gemma) both in terms of performance and training speed.

### Strengths
(S1) The direction of the current work to use macro actions (or a group of low-level actions together) is novel and interesting, for the setting of aligning a language model with human preferences (RLHF scope). Please see W1 for more discussion.

(S2) The manuscript is well-written, with sufficient details on all the technical details making it easy to understand and comprehend. I thoroughly enjoyed reading the paper.

(S3) The ablation and generalization studies presented in the experiment section (Sec.4.3 and 4.4) were interesting to better understand the behavior of the proposed approach in the context of RLHF.

### Weaknesses
 (W1) The idea of gathering multiple actions together as a “macro-action” is not novel in general. Referred to as “action chunking” [A], similar ideas have been explored in other domains. As noted in (S1), this is still useful in the context of RLHF, but with a diminished novelty factor.

(W2) The current work mostly experiments with a single LLM (Gemma and its variants). Given (W1) and lack of generalizability across different models, the usefulness of the current approach over PPO is not clearly understood to benefit the community. Demonstrating similar benefits in an LLM-agnostic manner will tremendously be useful.

(W3) Comparisons to the more recent approaches like DPO [B] are missing in the experimental tables. Though there is benefit over PPO for the chosen model, the experiments fall short to gauge the improvements compared to one of the current arts. Request the authors to include this comparison to better understand the proposed approach and its efficacy.

### Questions
Typos:
L68: leads -> lead

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
3

### Summary
They conduct empirical analysis of the use of macro actions in RLHF instead of the standard per-token actions. They study a variety of approaches to breaking responses into macro actions, finding that N-gram based macro actions tend to perform best. In general, they find macro actions have the potential to outperform standard PPO with per token actions. They attribute this to better training stability and reduced variance in the learning problem.

### Strengths
* They conduct thorough analysis on many different tasks, using several different sized base models.
* They conduct many ablations of their method.
* The paper is clearly written and easy to follow.
* This empirical analysis of macro actions present a useful contribution to our understanding of RLHF training.

### Weaknesses
 * Some of the differences in performance could be due to tuning one method more than another. It would be great if the paper could at least document the steps they went through to tune hyper-parameters for their method and baselines.
* My understanding is that the primary functional difference between per-token PPO and macro action PPO is the granularity of the value function, importance sampling, and discount factor. It is a fairly small modification, but this is not necessarily clear when reading the paper and could be better emphasized.
* The GRPO method proposed in https://arxiv.org/pdf/2402.03300, can be viewed as a special case of their macro action PPO. They don't discuss this in the related work.

### Questions
See weaknesses for questions.

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
This paper introduces MA-RLHF, a novel framework that incorporates macro actions (sequences of tokens or higher-level language constructs) into the RLHF training process for LLMs. The key innovation is operating at a higher level of abstraction by grouping tokens into meaningful units, which helps address the credit assignment problem in long sequences. The authors demonstrate that this approach leads to faster convergence (1.7x to 2x) and better performance across various tasks including text summarization, dialogue generation, question answering, and program synthesis, without increasing computational complexity during training or inference.

### Strengths
- The paper identifies a critical limitation in token-level RLHF - the credit assignment problem over long sequences - and proposes a simple yet effctive solution by incorporating macro actions. The approach is well-motivated by both theoretical considerations (credit assignment, temporal abstraction) and practical issues (subword tokenization challenges).

- The paper is well-written and easy to follow.

- The experimental evaluation is thorough, covering multiple tasks, model sizes (2B to 27B parameters), and evaluation metrics. The authors also conducted detailed ablation studies on different strategy of termination and find n-gram performs the best, analyzed the impact of macro action size, and did best-of-N to further validate the effectiveness of the proposed approach.

- The proposed method is simple (maintaining the same computational complexity) yet effectively improve performance (up to 30% in text summarization and code generation). The faster convergence and better performance make this a valuable contribution to practical applications.

### Weaknesses
 - While the paper explores different termination conditions for macro actions (n-gram based, perplexity based, parsing based), there could be more analysis of how different types of macro actions affect different types of tasks. For example, which macro action strategies work best for which types of generation tasks? For example, i would expect parsing-based termination might also work well on code generation tasks if a programming-language-based parser was used.

- Lack details of Human Evaluation: The evaluation involves human evaluation of model responses. It would be nice to show the detailed protocol of how human evaluation is performed, and what is the inter-rater agreement.

### Questions
* How sensitive is the method to the choice of macro action size? Is the macro action sizes sensitive to different types of tasks - i’m particularly interested in difference between different categories of tasks, for example, difference between natural language (TLDR, HH-RLHF done in the paper) and coding (APPS). In figure 6, it seems the difference between different n choice is not too large on HH-RLHF, wondering if that would change for coding tasks.

* Will be nice to see some qualitative examples of the macro-actions (e.g., how tokens are grouped together in a concrete setence).

* What is the difference & commonalities between this paper and ArCHer [1]?
[1] ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL

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
3

### Summary
The main idea is to use a larger chunk of text as the action in RLHF, instead of just one token (e.g., one word or one sub-word unit). What’s a larger chunk? The authors have tried multiple strategies: n-gram-based, parsing-based, perplexity-based “termination” of macro actions (i.e., segmenting tokens into a macro-action) – those are simple heuristics-based strategies introduced on page 4. Algorithms are built on top of naive PPO. 

Experiments are done using Gemma-2B, Gemma-7B, and Gemma-2-27B. Results on multiple tasks (summarization, dialogue or instruction following including HH-RLHF and WebGPT, code generation) show improvements.

### Strengths
The ideas are intuitive. Recent progress has shown that RL is promising in general so it’s great that the authors are investigating this direction. 

Multiple macro action termination strategies are explored. Experiments on code generation / program synthesis is helpful.

Interesting analysis on rejection sampling vs. temperature.

Helpful figures & illustrations in the appendix.

### Weaknesses
Results are great and surprising (not weaknesses); e.g., in Figure 4, the newly trained models are strongly preferred over the baseline (vanilla PPO). But:
- What’s the main reason here? Is there a comprehensive analysis that makes sure that the win rate is not based on simple features like length?
- Are baselines trained with a sufficient number of steps?

The equation for R is incorrect in Section 2.2.
- KL is between two distributions, but the authors wrote that the KL is between two real numbers.
- The last term should be -KL( \pi_\theta ( \cdot | x) || \pi_\text{ref} (\cdot | x)); in particular, KL(p || q) does not equal to -KL(q || p). Currently if you expand the KL, the interpretation is that if \pi_sft (y|x) is large, then we should make \pi_\theta (y|x) really small, in order to maximize R.

Other issues in Section 2
- Can gamma be equal to 1? (Section 2.1)
- In Eq. (1) it’s unclear if A_t is computed using \theta or \theta_old – it’s never defined; similarly, how about Section 3 line 233 – what model would the authors use to compute the advantage?
- In Eq. (1) what’s the expectation over? 
- At the end of page 2, the indices start from 0 (e.g., s_0, a_0); but on page 3 line 145, the indices start from 1

### Questions
A natural way is based on BPE-like automatic construction of a dictionary with most frequent n-grams. Have the authors considered this strategy? 

Do the authors think that leave-one-out REINFORCE or other recent PPO variants would also benefit from the authors’ algorithm (macro-actions)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes the incorporation of options (in the RL sense) into the RL component of LLM fine tuning with RLHF, with the motivation being better temporal abstractions over generation of long token sequences. The method is evaluated on several benchmarks and model sizes and is shown to overall outperform RLHF by vanilla PPO.

### Strengths
The proposed method is (as mentioned by the authors) simple and could be of potential interest to practitioners.
There is also an extensive evaluation of the method both in terms of tasks/datasets and in terms of method (GPT-based and human annotators)

### Weaknesses
There are some significant conceptual weaknesses, as well as many technical issues.

Most importantly, there is a considerable gap between the stated/declared motivation and goals and what is actually being implemented. 
The MA-RLHF algorithm only learns *one* option that is being applied everywhere -- there isn't a set of different options being learned, and there is no "macro" policy that chooses between them. As a result, generation really is driven by the (single) low-level policy alone, contrary to the authors statement that 
- "Macro actions leverage meaningful linguistic structures" (Line 66; which is clearly false for several of the "termination" strategies later used such as n-grams!)
- "MA-RLHF operates at the macro action level, making decisions over sequences of tokens at a coarser temporal scale" (line 176-177).
- And so on.

What remains, effectively, is a particular way to chunk the rewards (and Advantage / Value estimates) that feed into the RL algorithm, in a way that might be different than the standard one. It could potentially be the case that this pushes the value estimation component more towards Monte-Carlo (rather than TD-learning / bootstrap) because Q (and A) are now fitted to a Bellman backup update that first sums over $\vert \omega_{\tau}\rvert$ observed rewards before bootstrapping (See $R_\tau$ definition; Line 218. This is also reflected in the authors analysis of Section 4.3.2, line 374, see more on that later). If this is the source of the performance gain, it can be implemented and evaluated much more directly, and the story about temporal abstractions is merely a distraction. The fact that different termination strategies yield only marginal performance differences further suggests that the core mechanism is not related to any meaningful notion of macro-actions.

If the authors have a a good reason / explanation for this particular choice, it should be stated. And in any case, this limitation (or choice) must be clearly stated and acknowledged, preferably early on. Right now it's not even mentioned in the Limitations section (which is unjustifiably hidden in the appendix, Line 810).

Other than this main issue, there are plenty of technical issues, to a varying degree of severity. I expect some/most of them can be addressed in revisions. I have divided those into two sets, but I suspect these are not-exhaustive: the paper can definitely benefit from a closer proof-reading.

**"Moderate" Issues**
- The (Bengio et al. 2013) cite for the credit assignment problem (Abstract line 14, Intro Line 46) is out of place. That paper doesn't really deal with the RL credit assignment problem at all (although the term is mentioned, once, in the text).
  
- The comment "setting n → ∞ corresponds to the REINFORCE algorithm where the entire sequence is treated as a single macro action" (Line 399 and also Line 243) is completely unclear to me. REINFORCE most certainly **does not** treat the entire sequence as one action -- the policy is trained to generate standard "micro" actions at each time-step individually. The authors *might* mean to state something inline with the TD-based vs Monte-Carlo based method for estimating the Value/return, with PPO being an Actor-Critic variant and vanilla REINFORCE being a fully Monte-Carlo method. But this difference concerns the "critic" component rather than the actor. Moreover, the  (McGovern and Sutton 1998) cite for REINFORCE is wrong or at best confusing. (for REINFORCE the authors should cite Williams 92, or Sutton et al. 1999 if the claim is more generally on PG methods).

- What do we learn from Figure 3 that's not already shown in Figure 2?  There's nothing particularly interesting about the shape of the shown distributions besides the mean and variance, which are already presented in Fig. 2. If anything, other than showing the marginal histograms alone, there could be potential value in showing the correlation over individual examples and see if there's any structure in that (is the performance gain come from more easier/harder examples, or more uniform, etc). Also, if that figure is kept, it should be specified for which of the models and at which step at training the histograms are shown (judging by the scale I assume this is the 2B model at the end of training?).
  
- The authors claim that "MA-PPO achieves parity with vanilla PPO approximately 1.7 – 2 times faster during trainin" (Line 303). However the main difference in Figure 2 seems to be the final performance level which is higher for MA-PPO compared to PPO, and not the learning / convergence speed which is really comparable. This should either be made more quantitative / carefully evaluated, or less boldly stated.

- Figure 10: how come the marginal distribution of SFT RM scores changed between the first two panels and the last two panels?

**Minor issues**
There are, once again, many issues with phrasings, notation, etc.

Line 92: "An policy" -> "A policy"
Line 93: "The Markov Decision Processes" -> "A Markov decision process"
Line 98: The definition of Q(s,a) should include a conditioning on the fact that s_0 =s, a_0=a. It would also be better to write Q(s,a) rather than Q(s_t, a_t).
Line 98: The authors specify that reward is a function r(s,a) but then in defining Q use the formulation of r(s).

Line 108: The PPO discussion is rather dense. I feel that for a reader unfamiliar with the method, it will not be too helpful, and for familiar reader it will be redundant. Can be replaced by a reference to the appropriate paper, and shortened to a brief discussion of what Policy Gradient does (roughly, the inline Eq. in line 110), to be merged with the general RL formulation.

Line 111: Randomness of *the* initial state and so on.
Line 128: The acronyms for SFT and RM should be spelled out explicitly

Line 130: There's no use in writing r(x,y) if the reader don't know what x,y stand for. Better write "A reward model is trained to predict ...", then explain what the inputs are and what the goal is.

Line 140: Shouldn't the the equation read r(x,y) - beta KL? The way now written, the KL is not a penalty at all but a "bonus" to the reward (so higher KL will be encouraged)

Figure 1: I don't understand what we should read from the figure other than the fact that temporal abstractions are "a thing". And it is overall somewhat misleading, since it seems to imply that the optimized policy chooses macro actions (the MA-RLHF column, arrow from the MA-PPO network to the omega_tau action).

Line 145: Doesn't the state include the prompt as well? (other than the tokens already generated)

Line 236: The use of $r$ to denote the likelihood ratio or pi_theta/pi_theta_old is a really bad choice, because $r$ is reserved to denote the reward function. Is there actually a need to introduce more notation for the ratio? (note that in Equation 1, line 119, this notation is not being used).

Figure 2: Move the "(2B)" and "(7B)" to the ylabel ("RM Score (2B)"), or somewhere else -- otherwise it is confusing whether this 2B indicate scale of the time axis.

Figure 4: The fonts are tiny (in all figures really, but particularly here, only readable at 200% zoom or so).

### Questions
Somewhat more conceptually, the motivation about "essential linguistic structures and dependencies between adjacent tokens" (Line 54) is questionable. While the intuition is reasonable, in fact the very same argumentation can be made against the pre-training stage, where LLMs are trained to make single token predictions. But pre-trained LLMs already generate fluent/coherent output (surprisingly or not). It is a strong claim that making (one of) the fine-tuning step(s) more "global" can correct for the extensive pre-training. The power in RL methods might be the ability to design global reward/objectives (see also Ranzato et al. 2015, Choshen et al. 2019) which are better suited for aligning to designer preferences, but this is still true even if the model has to make only "micro" decisions. I think the paper can benefit from at least acknowledging these questions.

### Soundness
2

### Presentation
3

### Contribution
2
