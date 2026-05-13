# Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback

- Decision: Accept
- Scores: 6, 3, 6, 6

## Abstract
While large language models (LLMs) show impressive decision-making abilities, current methods lack a mechanism for automatic self-improvement from errors during task execution. We propose \method, an iterative fine-tuning framework that continually improves LLM agents using feedback from AI expert teachers. Our key insight is to equip the expert teachers with a \emph{privileged state} \textemdash information available during training but hidden at test time. This allows even weak experts to provide precise guidance, significantly improving the student agent's performance without access to privileged information at test time.
We evaluate \method on diverse decision-making benchmarks, including text-based games (ALFWorld), web navigation (WebShop), and interactive coding (Intercode Bash). Our experiments show that \method (1) outperforms behavior cloning and \texttt{ReAct} baselines (2) enables weak student models (e.g., Llama3-8B) to exceed the performance of strong teacher models (GPT4-o), and (3) allows weak models to self-improve using privileged versions of themselves. We also provide a theoretical analysis showing that \method’s success hinges on balancing privileged information with the student’s realizability, which we empirically validate. Our code is available at \url{https://leap-llm.io}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes LEAP, an iterative fine-tuning framework that continually improves LLM agents using feedback from AI expert teachers. The key insight is to equip the expert teachers with a privileged state - additional information available during training but hidden at test time. This allows weak experts to provide guidance, improving the student agent's performance. LEAP is evaluated on diverse decision-making benchmarks, including text-based games, web navigation, and interactive coding, and shows that it outperforms state-of-the-art baselines, enables weak student models to exceed the performance of strong teacher models, and allows weak models to self-improve using privileged versions of themselves.

### Strengths
* The proposed method looks valid and outperforms the baseline (ReAct).
* Evaluate three diverse environments: ALFWorld, WebShop, and Intercode.
* Provide detailed experiment and theoretical analysis of the trade-off between realizability and privileged information.
* The proof appears to be correct, and the prompts are included in the Appendix.

### Weaknesses
 * The analysis of the costs associated with iterative fine-tuning and calling LLM experts was not included. While the authors assert that their method is not comparable to Reflexion, Reflexion appears to be a more cost-effective approach for enhancing the performance of LLM agents with minimal trials.
* It seems somewhat inequitable to compare this method with those that do not utilize privileged information, as such information is typically not available in real-world scenarios.

### Questions
**Q1:** In the proof of theorem B4, there is a step using the performance difference lemma, but I did not see the connection here. Could you provide the derivation of how you get the inequality?

**Q2:** In the contribution section, Webshop is reported as achieving 61.8%. However, the metric used in the experiment is the score, which is usually much higher than the success rate. Could you clarify what metrics you are actually evaluating?

**Q3:** Could you provide the self-correct results (using Llama3-8B as expert teacher) for WebShop and Intercode?

The overall quality of the paper is good, but there are still some weaknesses and questions that need to be addressed. I will reassess the score based on the authors' clarifications.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This is paper is about automatic self-improvement from errors during task execution. They proposed LEAT in which LLM agents as students use feedback from expert teachers to improve itself. The teachers hav access to a privileged state —information available during training. So then even weak teachers are effective. They evaluate that on including text-based games, web navigation, and interactive coding. The results show that it outperforms state-of-the art baselines, enables weak student models (e.g., Llama3-8B) to exceed the performance of strong teacher models (GPT4-o), and (3) allows weak models to self-improve using privileged versions of themselves.

### Strengths
- well written.

### Weaknesses
 - Lack of good reference! Relevant references are missed in introduction! It needs to provide proper reference for each claim!
- The issue of experts is how to prepare knowledge for the experts, how to distinguish between different experts. This is not clear in this work and it needs manual set up which is not applicable.
- They are very similar works in the literature but with different names instead of experts! In that way the innovation of the work is very limited. 
- No Fair comparison at all!! The work did not consider fair baselines! There are a lot of up to date methods that works better than ReAct and BUTLER! There are a lot of works from self-correctness that they do the same things. 
- In general the contribution of the work is very limited! The teachers should know privilege knowledge however it is not always available! Even with that still prompting and few shot are needed which makes it the same as other prompting works or self correction works but here the authors just used different terms.  And it is very trivial that there should be some improvement vs e.g. react since it is literary using extra information of the environment and more over it uses a suggestion from a larger LLM with that extra information.

### Questions
- How to provide those privilege state in more complicated tasks?
- Trade-off between using privileged information and student realizability is not clear! 
- Compute privileged state s_t for every datapoint in Di in the algorithm is not clear. That is the limitation part of the algorithm. 
- how?  For each time step in Di, LEAP computes the privileged state s_t by leveraging information available only during training
- What is the performance of LEAP vs ReAct but using the same privilege state?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper seeks to address LLM Agents' difficulties when it comes from recovering from errors during task execution. 

They begin by framing decision-making as a Partially Observable Markov Decision Process (POMDP). 
Given this framing, they approach the issue by proposing LEAP, a DAGGER-like iterative training framework in which an expert teacher is equipped with "privileged state" corrects the faulty student agent trajectories during training. 

Here, the "privileged state" is simply a representation of the environment state that contains more information than what is available to the student. 

After outlining the problem and LEAP, the authors briefly examine their setup, analytically showing that there is a tradeoff between the performance and realisability of the privileged expert teacher.

The paper then moves on to the experiments, where the authors test their framework against a number of baselines across a variety of domains (text, web agents, and coding), demonstrating improvements in performance. Their experiments also show the possibility of student agents surpassing their teachers and of self-improvement when using a privileged version of themselves as the teacher. The authors also experimentally explore the tradeoff between how much privileged information to use and how realisable the corrections are. Finally, an ablation on the fine-tuning mechanism in LEAP demonstrates that SFT outperforms DPO and KTO in this setting.

### Strengths
- The paper provides a solid theoretical grounding in both the main text and appendix, especially around the analysis on the trade-off between privileged information and the agent's realizability.
- I appreciated the variety and number of domains considered experimentally, which showed the wide applicability of the method.
- The ablations on the fine-tuning methods, across SFT, DPO and KTO were greatly appreciated, as it was otherwise unclear which of these to pick from
- Beyond the general experimental results, I found the questions considered relatively original: whether an agent can bootstrap to self-improvement, whether it can outperform its teacher, and what tradeoffs are faced in terms of amount of privileged information and correction realizability. These were all quite interesting results to read.
- The paper explicitly acknowledges some its limitations, which is commendable and contributes to the paper's transparency and reliability in my view.

### Weaknesses
 - I found the author's choice of framing decision making as a POMDP somewhat arbitrary and under-justified. There is plenty of valid work that studies decision making using fully observable MDP's, and the connection to the real world is a bit forced
- Aside from the above, the main weakness in my view is that the authors never address/consider/justify the absence of the very obvious alternative: if you are able to train using privileged information anyway, why not simply show this information directly to the student rather than through the teacher? If the privileged information is accessible (by the teacher), this is not really a POMDP anymore really. What analogous real world scenario is this setup trying to address? It appears somewhat ill-defined from what i can tell.
- Somewhat related to the above point, but I found some of the results somewhat obvious and not particularly novel: of course an agent which (indirectly) has additional privileged information will do better than one without such information. It is similarly not surprising that the student eventually outperforms its teacher, given that only the student is trained and is probably comparatively overfitting to the objectively. 
- I found section 3.3. rather unclear and perhaps underdeveloped in the main text. For instance, "realizability" on its own is never clearly defined. I would have devoted more of the paper to this analysis, perhaps sacrificing one of the domains from 4.1-4.4 to the appendix if space was necessary.

### Questions
My main question is already mentioned above under "weaknesses". If we are allowed to show privileged information to the teacher, which then uses this to correct the student, why not directly show the privileged information to the student, especially given the student-teacher relationship is not adversarial? Which real-world scenario is this setup replicating?

UPDATE 25/11/2024: This question and some of the weaknesses have been addressed in the rebuttal, so I have updated my review score from a 5 to a 6.

### Soundness
2

### Presentation
2

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
The authors propose LEAP, an iterative fine-tuning framework that continually improves LLM agents using feedback from AI expert teachers. Notably, they equip the expert teachers with a privileged state. They evaluate LEAP on several decision-making benchmarks, and their experiments show that LEAP enables weak student models to exceed the performance of strong teacher models.

### Strengths
1. Novel methods: There have been a huge amount of research papers discussing about LLM self-improvement. However, the idea of equipping the expert teachers with a privileged state is relatively novel.

2. Good experimental results: LEAP significantly outperforms all baselines, even the stronger teachers like GPT-4o.

3. Diverse experiments: The authors conduct various experiments across several fundamentally different benchmarks.

### Weaknesses
1. Privileged states can be hard to get in real world environments (though this may not fit in the scope of this work).

2. Training an agent for each benchmark seperately is specific. The results would be much more promising if the authors demonstrate the LLM can be finetuned on all benchmarks together and still achieve good results. 

3. Some minor typos: For example, in line 24, GPT4-o should be written as GPT-4o. In line 127, $\rho_t^*,a_t^*$ should be $(\rho_t^*,a_t^*)$.

### Questions
1. Have the author tried to perform preference optimization after SFT? Will this lead to a even higher score?

2. The authors admit that generating interaction rollouts is time-consuming. How long does it typically take in terms of magnitude—hours, days, or even longer?

### Soundness
3

### Presentation
3

### Contribution
3
