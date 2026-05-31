## Human Reviewer 1

### Summary
This work proposes Truncated Reasoning AUC Evaluation (TRACE), a method that measures reasoning effort by checking how early the models reasoning becomes sufficient to pass the verifier. The intuition is that hacking the reward requires less effort than genuine reasoning, so the hacked responses can pass the verifier earlier. Based on this intuition, the method is relatively simple; the authors just add answer tokens at various lengths of the CoT and force the model to emit a response with these "incomplete" reasoning traces. They then measure the verifier pass rate across these truncation points and use the area under the curve as a quantitative metric for the models reasoning effort. The authors demonstrate that TRACE has better performance than the more traditional CoT monitors on detecting hacking and they even use TRACE to identify training environment loopholes, i.e., potential shortcuts in datasets that can lead the models to hack.

### Strengths
- TRACE is a simple and effective method for detecting reward hacking in reasoning models, an important problem. 
- TRACE's results demonstrate that it can be better than the more traditional CoT monitors while also avoiding the need for having an additional model, the CoT monitor, thus offering better scalability. 
- The paper is well structured, clear and easy to read.

### Weaknesses
- TRACE can be computationally expensive due to needing multiple generations to populate the CoT % vs Avg passing rate curve
- The comparison to CoT monitors is not entire apples-to-apples as TRACE uses strictly more information; it allows querying the base model multiple times and it also has access to the output reward. The authors did not compare with more involved monitors, e.g., monitors that take as inputs CoT, actions and reward output. 
- Something which the authors also acknowledge is the relatively simple nature of the loopholes that they investigated.

### Questions
Overall, I am on the positive side for this work. Some comments and questions to the authors are

- The authors focus on verifier pass rate instead of checking for the same answer when truncating the CoT. Why not also check for the same answer? Shorter CoTs might need to exploit more the loopholes present in the inputs in order to pass the verifier check but that doesn't mean that they are probable under the model distribution. Furthermore, if the CoT is not informative enough for the final response, then the model might need to rely more on the prompt (and potential loopholes) to solve the task. How does the TRACE score look like if the authors use "same answer" instead of "pass rate"? 
- The authors mention that a higher TRACE score indicates that the model knows the loophole earlier in the CoT. As knowing and using are different concepts, do the models actually use that information? Are there instances where the answer flips between hacky and non-hacky as a function of the CoT length?
- How does TRACE perform on simpler tasks where CoT might not be necessary in order to have good performance? Does TRACE require that reasoning is necessary to be successful (i.e., do the authors observe similar phenomena to Emmons et al, 2025)?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper tackles the problem of detecting *implicit* reward hacking - hacking that is not verbalized in CoT traces. The paper makes the observation that implicit reward hacks are often simple and don't require reasoning. This motivates their methodology, TRACE, which cuts reasoning short and evaluates whether the model can still get the right answer. If the model is consistently able to get the right answer with its reasoning cut short, then the model is more likely to be hacking. The authors show that this detection method is useful for distinguishing hacking vs non-hacking models; and also to detect hacking responses from a single model.

### Strengths
- Well-written
	- The paper is clear and well-written. It is easy to follow and make sense of.
- Sensible solution to a critical problem
	- Reward hacking is a critical problem facing scalable RL training. Detecting reward hacks is increasingly important, and in my opinion this paper produces a nice detection mechanism to implicit reward hacks. The solution is simple (which is a good thing).
- The paper goes beyond initial investigation to applications
	- I appreciated that the authors applied the method to two tasks: distinguishing between a hacking vs non-hacking model, and distinguishing hacking samples from non-hacking samples. I think the latter is in particular interest for real RL training, and the authors indicate that this can be useful for detecting hacks in the RL environment.
- Properly acknowledges limitations
	- I appreciate that the authors honestly acknowledge the limitations of their work; the main limitation is the simplicity of the carefully-designed reward hacks studied in this paper.

### Weaknesses
- The environments are very synthetic / contrived, and likely don't reflect real-world reward hacking scenarios.
	- The authors acknowledge this limitation, to be fair!

### Questions
- In the code setting, why sample once? (Footnote 2) In the math setting, 5 responses are sampled at temperature 0.7; why not do the same for the code setting?
- I think the paper could benefit from a discussion of cost. Is this methodology feasible to deploy in practice?
- I am also curious whether models could be trained adversarially against TRACE. For example, could a model learn to "know" when its CoT is cut short, and not hack in those cases?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper addresses implicit reward hacking in reasoning models, i.e. cases where models exploit evaluation loopholes but produce plausible CoTs that evade monitors. The proposed method, TRACE (Truncated Reasoning AUC Evaluation), measures “hidden effort” by truncating CoTs at various points, forcing early answers, and computing the verifier pass rate curve. A high AUC indicates early success, suggesting exploitation. Experiments on math and code tasks with two loophole types (in-context hints and reward-model bugs) show TRACE outperforms CoT monitoring and can cluster samples for loophole discovery.

### Strengths
The paper makes a clear and original contribution to oversight research by shifting the focus from what the CoT says to how much effort the model expends. This is both conceptually appealing and practically relevant.

* Novel perspective: Instead of analyzing CoT content, TRACE uses early passability as a proxy for reasoning effort, which is a clever way to expose hidden shortcuts.
* Empirical gains: Across math and code tasks, TRACE achieves large improvements over strong CoT monitors (up to +65% F1 in math, +30% in code), even when hacked CoTs look perfectly reasonable.
* Instance-level detection: TRACE works per sample and tracks hacking onset during RL training, revealing dynamics that CoT length or KL loss fail to capture.
* Loophole discovery: Clustering by TRACE score and prompting an LLM successfully identifies injected artifacts, showing potential for unsupervised forensic analysis.
* Scalable oversight angle: Because TRACE relies only on the model's own outputs, it avoids the need for ever-larger external monitors.

### Weaknesses
While the paper is strong, several practical details would make it easier to deploy:


Deployment framing & calibration guidance: TRACE is shown to work during training and at inference, but the paper doesn't offer a clear, setting‑specific recipe for threshold calibration, drift handling, and baseline selection. This is especially important when the initial‑policy baseline is unavailable (e.g., auditing a third‑party model) or when data distribution shifts over time.


Assumptions about CoT access & control: TRACE presumes you can see the CoT, truncate it, and force early answers. That’s not always feasible (latent‑reasoning systems, models with hidden traces, or agents whose action plans break when truncated).


Early solvability vs. hacking: High AUC can reflect genuinely easy‑early items rather than exploitation. A brief false‑positive analysis (e.g., counterfactuals that remove loopholes but preserve difficulty) would clarify this boundary.


Cost/sensitivity profile: TRACE uses multiple truncation points and sampling. The paper lacks runtime and stability guidance (e.g., how many points/samples are enough, temperature sensitivity, and the cost–accuracy Pareto).


Adversarial adaptation: A savvy model could pad early reasoning or delay the exploit to evade early passability checks. A short red‑teaming experiment (or mitigation ideas like randomized truncation schedules) would strengthen robustness.


Realism and coverage of loopholes: The synthetic IC/RM setups are clean and illustrative; real exploits can be subtler, multi‑step, or tool‑centric. Even a small "wild" case study (or a discussion of expected failure modes) would help scope external validity.

### Questions
1. Scope and deployment scenario:

Is TRACE intended as a general-purpose detection method or primarily for RL-trained models? The paper mixes inference-time and training-time use cases.

---
2. In-context loopholes without training:

Section 3.2 defines hacking models as RL-trained, but in-context exploits can occur at inference without any training. How does TRACE handle such cases? Would detection still work if the model was never optimized for hacking?

---
3. Verifier pass rate vs same answer:

You mention “generalize same answer to verifier pass rate.” Could you provide an example where the truncated CoT produces a different final answer but still passes the verifier, and explain why this matters for detecting hacking?

---
4. Reward spike vs TRACE signal:

In Fig. 8, reward seems to “explode” once the loophole is discovered. Would simple reward monitoring during training suffice to detect hacking? Can you imagine a scenario where reward rises smoothly but TRACE still detects hidden shortcuts?

---
5. Truncation vs naturally short CoTs:

TRACE truncates CoTs post-hoc, but some models are trained to produce short CoTs (e.g., under token budgets). Would TRACE misinterpret low AUC as high effort in such cases? How could the method adapt to budget-forced reasoning?

---
6. Delayed exploit strategies:

Would TRACE fail if models output plausible intermediate steps and only apply the exploit at the very end? How robust is TRACE to adversarial adaptation where the hack is deferred?

---
7. Compute overhead and sensitivity:

How many truncation points and samples are needed for stable AUC estimates? What is the runtime overhead compared to CoT monitoring? Any analysis of sensitivity to sampling temperature or truncation granularity?

---
8. Realism of loopholes:

The injected loopholes (IC hints, RM bugs) are clear but somewhat artificial. How representative are these of real-world exploits? Could TRACE handle multi-step or tool-based hacks where success depends on external actions?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposed TRACE, a method for identifying hacking behaviors in LRMs.  The authors make the hypothesis that a hacking model will produce the correct answer in the early part of the CoT trajectory while a non-hacked model needs the full CoT trajectory to be able to reach a final answer. The TRACE method involves several steps. First, a given LRM-generated CoT trajectory is truncated into chunks, which are then cumulatively fed into the LRM to sample responses. The answers are passed into a verifier to compute the passing rate given the current CoT chunk. Based on the assumption, hacked models would possess a high passing rate with only a fraction of its CoT trajectory while non-hacked models could only have a high passing rate if the full CoT  trajectory is provided. The authors conduct experiments in both in-context hacking and reward model hacking settings to validate the performance of TRACE. Further, the authors demonstrate that TRACE can be used for identifying data entries that may be hacked by the LRM.

### Strengths
- The paper is well-written and easy to follow. 
- This paper proposed TRACE, a method for identifying hacking behaviors in LRMs via truncating their CoT trajectories. The proposed method is simple and effective according to the reported experimental results. 
- The experiment setup is comprehensive, which includes in-context loophole and reward model loophole. 
- The case study offers a potential usage of TRACE, which is to identify data entries that contain loopholes. Experiment results show that TRACE can reliably distinguish hacking data from others once the loophole is exploited. 
- Experiment results show that TRACE offers more in-depth detection of reward hacking than existing superficial detection criterias such as CoT length and KL Loss.

### Weaknesses
- It is unclear whether the proposed TRACE method will be robust enough to handle LRMs with overthinking issues where the correct answer may occur in the middle of a CoT trajectory albeit the model itself is unhacked. 
- The authors mentioned several limitations with CoT monitor approach, which mainly include deceptive CoT content and latent CoT methods. While the proposed TRACE method may be used to tackle deceptive CoTs, it is unclear to me how TRACE can be used in the case of latent CoT. 
- The sampling process seems to introduce quite a lot of compute overhead as a given LRM needs to produce multiple responses for each chunk of the truncated CoT trajectory.

### Questions
- How does the proposed TRACE method handle cases of overthinking? An unhacked model may produce CoT trajectories that contain correct answers but are prolonged due to overthinking.      
- How can TRACE be used to tackle latent CoT?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4