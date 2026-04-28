# Convergence Towards Stable Intrinsic Self-correction of Large Language Models

- Decision: Reject
- Avg Score: 5.40
- Scores: 3, 8, 3, 8, 5

## Abstract
Large Language Models (LLMs) are able to improve their responses when instructed to do so, a capability known as self-correction. 
When instructions provide only the task's goal without specific details about potential issues in the response, LLMs must rely on their internal knowledge to improve response quality, a process referred to as intrinsic self-correction. 
The empirical success of intrinsic self-correction is evident in various applications, but how and why it is effective remains unknown.
In this paper, we unveil that intrinsic self-correction can be progressively improved, allowing it to approach a converged state. Our findings are verified in: (1) the scenario of multi-round question answering, by comprehensively demonstrating that intrinsic self-correction can progressively introduce performance gains through iterative interactions, ultimately converging to stable performance; and (2) the context of intrinsic self-correction for enhanced morality, in which we provide empirical evidence that iteratively applying instructions reduces model uncertainty towards convergence, which then leads to convergence of both the calibration error and self-correction performance, ultimately resulting in a stable state of intrinsic self-correction. Furthermore, we introduce a mathematical formulation and a simulation task indicating that the latent concepts activated by self-correction instructions drive the reduction of model uncertainty.
Based on our experimental results and analysis of the convergence of intrinsic self-correction, we reveal its underlying mechanism: consistent injected instructions reduce model uncertainty which yields converged, improved performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper examines the impact of multi-round self-reflection prompting without external feedback, termed "Intrinsic Self-Reflection" (ISR), on improving morality-related tasks (e.g., social bias mitigation) for LLMs. The study demonstrates that while ISR significantly enhances performance in both question-answering and text-generation tasks, the improvements diminish after multiple rounds, stabilizing within 10 iterations—an observation termed the "convergence of ISR." 

To understand this phenomenon, the authors analyze model uncertainty and calibration errors across ISR rounds. They find that both metrics decrease with more rounds, and the inflection points of calibration error trends coincide with performance stabilization. The authors suggest that ISR reduces model uncertainty and improves calibration, leading to better task outcomes.

The study also probes the model’s hidden states for negative latent concepts such as "immorality" or "toxicity". Results show that positive prompting in the initial round leads to a gradual deactivation (weaker probing performance) of negative concepts over successive rounds.   Injecting immoral instructions in the intermediate rounds only asserts temporary effects, confirming the convergence and irreversibility of ISR. 

Finally, through simulation experiments and a theoretical derivation under simplified assumptions, the author bridges the connection between ISR instructions, activated latent concepts, model uncertainty, calibration error, and the converged performance.

### Strengths
1. This paper conducts an in-depth study of ISR impact on morality-related tasks for LLMs through the lens of iteration rounds, providing novel insights into deploying ISR to regulate LLM outputs. 

2. The organization of this paper is overall clear.

### Weaknesses
 1. **Confusing Formulation and Non-Rigor Theoretical Investigation**.  The paper contains several ungrounded statements. For instance, in Section 4, the authors attempt to establish causality between model uncertainty, calibration error, and performance to explain ISR convergence. However, the cited previous works and presented empirical evidence only indicate correlation without rigorous analysis or causality testing. Additionally, the assumption of independence between output, instruction, and question in Section 6.2 oversimplifies the language model’s behavior, where outputs are heavily dependent on inputs.  Many notations in Section 6.2 are confusing or redundant  (e.g., redefining conditioning symbol "|"), and Equation 3 misapplies Bayes' rule, leading to problematic derivations. See more details in "Questions".

2. **Inconsistent Experiment Results and Analysis**: There are key discrepancies between experimental outcomes and the authors’ interpretations. For example, VQA performance with more ISR rounds is drops after the second round, challenging the claim that ISR leads to a stable, convergent state. More importantly, in Section 4, as the author uses logit confidence to quantify uncertainty for QA tasks (BBQ here), and "higher logit confidence indicates lower uncertainty" (as explained in Footnote 5 at page 5), Figure 4(a) should be interpreted as QA tasks uncertainty is **increasing** rather than **decreasing** (as in L256), contradicting the whole analysis in Section 4. Also, in Section 5, the "sexual"-dimension of the BBQ dataset exhibits different trends in probing experiments, not consistent with the analysis that negative concepts "converge after several rounds" (hard to read) for "all tasks" (L322).

3. **Confusing Experiment Setup and Missing Experiment Results**: Certain experimental setups are unclear or appear unnecessary For example, the introduction of VQA and visual grounding task (even not clear what this task is without proper citation) seems unnecessary, as the majority of the content of this paper focuses on text-only tasks, and even in the main experiments, there is no related cross-modal discussion. These tasks also seem disconnected from other moral-focused tasks. 

    Also, in Section 4, "pick up four social dimensions from the BBQ benchmark (Parrish et al., 2022) for QA tasks" reads confusing – QA tasks, including jailbreak and VQA, have drastically different contexts and it is not clear how BBQ (the "social bias mitigation" task) can be adapted to evaluate "uncertainty" on this task. The best guess here is that other QA tasks are just dropped, but then the jailbreak one is getting back in Section 5 as explained in the incomplete Appendix B.4. 

    In Section 5 and Appendix B.4, it seems the jailbreak defense task is adopted in probing experiments, but Figure 5(a) does not apply to jailbreak datasets as these four dimensions are from BBQ and it is not clear how to do this cross-task adaption. 
  
    In Section 6.1, the introduction of the new dataset RealToxicityPrompts is unclear, as there is no related ISR setup explained, and no explanation of how to obtain concepts (c1, c2) and uncertainty (u1, u2) from the trajectories.

### Questions
**Confusing Formulation and Non-Rigor Theoretical Investigation**

1. L169 - 175, Eq. 1: The introduction of D as pre-training data is unclear. The derivation of Eq. 1 doesn’t require citing Xie et al. [1]; it follows directly from the law of total probability, which [1] also used.

2. L126 & L169: There is an inconsistency between adopting semantic entropy as an uncertainty measure in L126 and expressing uncertainty as output probabilities in L169. It’s only clarified later that different tasks use different measures.

3. L251: When treating multi-choice QA as classification tasks, and using model log probability for each choice, the counterpart of Semantic Entropy used in the language-generation task here should be direct computation of entropy over re-normalized probabilities for answer choices, rather than using logit confidence. The lack of justification for diverging from entropy-based measures undermines consistency with the language-generation task.

4. L397: "y_t | y_{t-1} denotes that..." – It is not clear what the necessity is to redefine the conditioning notation used in probability. 

5. L404: The distinction between M(y_t) and M(y_t | y_{t-1}) is vague.  Also, it is hard to understand how to reach the right-hand side from the left-hand side in this line. One possibility is an unrealistic assumption that improvement in metric M stems from consistently activating more "positive concepts" than "negative" ones in **all** previous rounds preceding round $t$. However, we see that in Figure 5, even sometimes injecting immoral instruction (following the author's reasoning, this means "negative concepts" being activated more), then very likely p(C_n|q_k) > p(C_p | q_k), but later, very quickly, the similarity to toxicity decreases to "moral" line (black line), means that the activation of "positive concepts" are restored. So the improvement at some evaluation rounds does not necessarily mean positive concepts have to be activated more than negative ones all the way. 

6. Eq.3: The derivation requires careful review. A detailed proof, reflecting all assumptions, would clarify its validity.

**Experiments**:

1. What is the VQA task you are using? There is a lack of citation. 

2. In Figure 5(b), the overlap of the similarity curve with the "moral" curve after introducing intention instructions in rounds 2, 5, and 8 is unclear. The authors state that "immoral instructions drive the activated concept towards toxicity," yet this effect lasts only one round. In contrast, pure immoral/moral instructions seem to have a more prolonged impact. Why the discrepancy?

**Presentation and Writing**:

1. Figure 5(b) – Interve(n)tion Rou(nd), Interven(tion)

2. Appendix B.4 is incomplete and broken. 

3. L323: When talking about "injecting immoral instruction/moral instructions", to avoid confusion with later intervention experiments, it should be noted that here the author refers to the black and purple lines. 


References:

[1] Xie, Sang Michael, et al. "An Explanation of In-context Learning as Implicit Bayesian Inference." ICLR 2022.

### Soundness
2

### Presentation
2

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
The paper analyzes in detail the phenomenon of intrinsic self-correction, whereby an LLM is iteratively prompted using a pre-selected prompting strategy (in a multi-turn conversation without requiring human intervention) to improve its responses on a specific metric (e.g. toxicity, safety). The paper examines the convergence of this process in a multi-turn setting both by evaluating the original metric on the response (e.g. toxicity) and by looking at key metrics associated with the model’s internal representation (uncertainty and concept, which is a quantifiable way of probing the model’s internal “direction”) and show that they improve and converge during the intrinsic self correction. The paper studies the process convergence for several different tasks, which is crucial for obtaining quality guarantees in real-world use cases.

The paper shows that this phenomenon arises along with a reduction in the model’s uncertainty as part of the intrinsic self-correction trajectory, and further that this generates calibrated responses (in the sense that the model’s uncertainty is aligned with the correctness of the answer), with the initial responses tend to be under-confident. The paper formalizes the procedure’s steps as classification (e.g. yes/no) questions and uses normalized log-likelihoods to assess model’s certainty.
Additionally, the paper measures the latent concept’s development throughout the self-correction process. The latent concept is modeled as a binary positive/negative set (e.g. in biasing or discrimination - negative means exhibiting stereotypes or discrimination, and positive means fairness). This is measured using a linear probing vector to find the “direction” representing the concept in activation space. It is shown that along the self-correction trajectory it both converges and does not revert from positive to negative. 
Finally, the paper performs an empirical and theoretical analysis to establish the causal relationship between the concept’s development and uncertainty reduction throughout the process, leading to convergence

### Strengths
The authors present a unified framework for assessing the convergence of intrinsic self-correction through multi-turn automatic prompting across multiple tasks. By carefully measuring both the model’s certainty throughout the process and the concept that the process is meant to improve (using a succinctly-described bayesian inference framework, and measured using a trained linear probe) they are able to show that both reach convergence across several tasks and that they do so in a monotonic way. 
Further ablation studies demonstrate that, indeed, it was the specific prompting strategy that drove this, as injecting “opposite direction” prompts show the opposite behavior in the concept probe. 
The technique is applied both to LLM and VLMs (i.e. for visual tasks). Both are shown to both be improved by the process and show the same trends in internal representation analysis. 
Finally, the simulation-based analysis which links together uncertainty and concept is very interesting, and presents strong evidence for causality, later supported by theoretical analysis.

### Weaknesses
The paper could benefit from rewriting to improve clarity. 
Specifically, consider rewriting the mathematical part of section 6.2, since it is difficult to follow and raises some questions specifically about the notation and derivation leading to eq. 3, discussed below,



### Questions
Mathematical analysis:
* In the derivation of equation 3, is it assumed that c_y and c_i are identical for all the steps? (If not, please make sure the notation clarifies that. )
* Is cx ≪ ci used anywhere? 
* In Equation 1, is it assumed implicitly that there is only one concept (and the integral is thus converted into a sum over the negative and positive concept? Is this a trivial observation?

Very small comment
 “We leverage u2 − u1 as the change of concept and the label is set as 1 if u2 − u1 is no larger than 0, otherwise the label should be 0.” this should probably be a label for uncertainty, not concept, right?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents an analysis of the self-correction approach to improving LLM responses. The authors find that model uncertainty decreases and a relevant concept seems to become more activated through the self-correction process.

### Strengths
The paper is focused on understanding a phenomenon and uses multiple tools to do so. This potentially gives us deeper insight into why this technique is effective.

### Weaknesses
1. The methods for measuring uncertainty were unclear. The various methods were stated with references but should be defined in the text for them to be interpretable.

2. No statistical significance testing was performed to support any of the claims about changes in uncertainty or activation of the latent concept. No error bars appear on plots. For this reason the latent concept analysis in particular seems relatively superficial.

3. The theoretical analysis makes strong independence assumptions: that question, instruction, and output are independent. With these assumptions it is not a surprise that convergence is geometric. I would like to see a more strongly motivated model.

4. The authors note that they did joy study other domains as self-correction is less effective there. That seems like an important omission — if the current approach helps us understand the efficacy of self-correction it should also explain the cases where it doesn’t work.

### Questions
I had no further questions.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates the mechanisms of convergence in 'self-correction' in LLMs. By monitoring concepts, uncertainty, and toxicity of the responses, the automatic feedback will prompt the LLM in contexts to improve in a specific dimension. With multiple-round interactions, the LLM can converge across these three dimensions in its response. With this design, the authors analyzed how the model's performance and those metrics change over interactions in six different tasks. The results show that all three metrics converged and were lower than the baseline, revealing 'self-improvement' in model responses. Finally, the authors show theoretical proof of the connection between model uncertainty and concept representation, and how such iterative correction processes could lead to convergence. Overall, this paper provides a deep insight into the mechanisms of 'self-correction' in LLMs.

### Strengths
- The paper chooses six different tasks to test the model performance, which varies across QA tasks and text generations, as well as multi-modal visual understanding tasks, showing a wide distribution of the scenarios.

- The paper dives into the mechanistic explanations of how and why 'self-correction' can converge in iterations. The work integrates both empirical and theoretical foundations to explain the phenomenon.

- The writing and visualization of the paper is satisfying.

### Weaknesses
 - Only one model is used. I was wondering how different models (e.g., one mode family with different sizes; or different model family with the same size) could perform differently. This may help us understand deeper why the model could improve and what may influence the speed of convergence as well as the optimal point.

- Model uncertainty measurement is good since it does not rely on external resources and can gain complete accessibility from the model itself. The latent concept is also flexible and does not rely on external benchmarks. However, EC relies on the task ground truth and label data. This means that, in unseen tasks, the model may not be able to get feedback from EC, which may affect the generalizability of the task. Therefore, I wonder if there is any experimental setting or analysis to show that without EC feedback, how can the pipeline solely rely on model uncertainty and latent concept can reach the performance; or how much does the three dimensions of feedback contribute to a convergent process.

- (Minor) There are some questions remaining unclear regarding the convergence. For example, in the process, how the 'gradient' like concepts are represented in the model(which means how does the model know which direction to correct), from contexts to model computations. This may help us understand better how the model perceives (evaluates) these metrics. Another question is, what determines the convergence optimal point? (model size? or complexity of the task? human-instruction fine-tuning?). Some exploratory analysis on these aspects would much improve the depth of this paper. (if these questions are somehow tackled, I believe this paper should be at least 8 or even 10 score level).

### Questions
- I wonder how general this probing vector could be. I did not put this into weakness because it looks great in the paper. However, I still wonder only with this probing vector, how can it guide the performance in benchmark-free scenarios.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The author's theoretically analyze self-correction and establish a connection to model uncertainty and calibration error.  They empirically demonstrate that model uncertainty and calibration error converge over multiple rounds of self-correction on several QA and generation tasks.

### Strengths
1. The paper provides theoretical grounding for self-correction
1. The empirical results are tested over a two tasks (QA & generation) and across several domains each.

### Weaknesses
1. The text based tasks are only evaluated with Mistral-7B-v0.1 but having results for other model families or sizes could improve the robustness of the empirical results.
2. There is a gap between the argument of the connection between uncertainty and calibration error, and the empirical results.  Specifically, the paper could address the fact that the QA converge in calibration error and performance after one round of iteration while the uncertainty only drops by a small amount after that same round.

### Questions
In Figure 3 we see that 2 of the QA tasks converge in performance after a single round of self-correction.  This is confirmed in Figure 4b where the calibration error also converges after a single round of self-correction.  However, Figure 4a shows that uncertainty only drops by a small amount after a single round, and only converges after +10 rounds of correction.  This calls into question the crux of the paper that mechanism of self-correction performance improvements are driven by lowered uncertainty.  After a single round of self-correction the model can "re-read" the question (see *Re-Reading Improves Reasoning in Large Language Models*, Xu et al. 2024) which may account for the single-shot convergence of performance.

The paper could be improved by addressing this empirical inconsistency that error converges after a single iteration round but uncertainty doesn't converge until many more rounds.

### Soundness
2

### Presentation
2

### Contribution
2
