---
job_id: f9627bf0-46ed-4c45-bf67-9d7a62ecee1f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: RNe17WTR38.pdf
paper: Self-Evolving Language Models via Simple Generator-Verifier Games
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on self-improvement of language models, preference optimization, and reasoning benchmarks, which fall under general machine learning, language modeling, and reinforcement/preference-learning-adjacent post-training.

## Minimum Quality
Pass ✅. The submission includes the core components expected of a research paper, namely Abstract, Introduction, Method/Approach (Sections 2, 3, 4), Experiments and quantitative results (Tables 1 to 4, Figures 2 to 5), Related Work (Section 5), and Conclusion/Limitations (Section 6). While I have substantial concerns about novelty and experimental positioning, these do not rise to desk-reject level.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, manipulative instructions to automated reviewers, or other suspicious embedded content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies self-evolution of language models through a generator-verifier game in which the same instruction-tuned model plays both roles. The main variants are a single-turn method, SimpleGV, which constructs preference pairs from self-verification with thresholded majority voting, and a multi-turn method, RevisionGV, where the model critiques and revises its own answers before preference optimization with DPO. The paper evaluates these ideas on Knights-and-Knaves and several math reasoning benchmarks, and also explores iterative training and curriculum learning.

## Strengths
The paper is easy to follow at a high level. The generator-verifier framing is simple, and **Figure 1** is a useful overview of the two pipelines, especially the distinction between static filtering in SimpleGV and revision-based pair construction in RevisionGV. This makes the core experimental story understandable without requiring the reader to reconstruct the protocol from scattered implementation details.

The empirical section is fairly extensive on the KK benchmark. In particular, **Table 2** and **Table 3** go beyond a one-shot main result and study iterative training and curriculum effects across difficulty partitions. I appreciated that the paper reports separate performance on 2-3, 4-5, and 6-8 people, rather than only a single aggregate score, because this reveals where the gains come from and supports the easy-to-hard generalization claim more concretely than a single average would.

The thresholding idea is operationally sensible. Even if it is conceptually simple, the use of repeated verifier calls and abstention on ambiguous cases is a reasonable way to trade recall for precision in self-generated supervision. **Figure 2** does support the narrow claim that higher thresholds improve verifier accuracy on the KK training set for the studied model, and this is one of the cleaner pieces of evidence in the paper.

The paper also includes some useful scaling and cost analyses. **Figure 3** shows that the effect is model-size-dependent, with 4B and 12B benefiting much more than 1B, which is an important practical observation. **Figure 5** is similarly helpful in showing that the method is not “free”, and that the threshold interacts with generator/verifier budgets in nontrivial ways.

Finally, the work is relevant to an active area, namely self-improvement without human preference labels or external executable rewards. Even though I am not convinced the paper is sufficiently differentiated from prior work, the problem itself is worthwhile and of clear interest to the ICLR community.

## Weaknesses
1. **The main contribution is too incremental relative to existing self-rewarding / self-improvement paradigms, and the paper does not do enough to distinguish what is actually new.**  
   The core setup, a single model generating responses and then judging or improving them to create training signals, is already a very familiar pattern in self-rewarding and self-improvement work. What this paper adds on top is mainly: (i) thresholded majority voting, (ii) a revision-based variant, (iii) iterative reuse of the loop, and (iv) curriculum scheduling. Those are reasonable engineering choices, but the paper often presents them as if they collectively define a distinct framework, whereas from the main text they read much more like a straightforward composition of existing ingredients. This matters because ICLR main-track standards are not just about whether something works, but whether the paper substantially advances understanding or methodology. Here, the paper does not convincingly identify a sharp conceptual gap in prior work that SimpleGV or RevisionGV resolves.

2. **The experimental comparisons are not sufficiently targeted to support the paper’s main positioning claim.**  
   The strongest baselines should be methods that also use self-generated preferences or self-judging without external labels, because that is precisely the niche the paper claims to occupy. Instead, **Table 1 (Page 5)** compares against a mixed bag of methods, some of which rely on environments, online RL, or other settings that are not apples-to-apples. This weakens the empirical positioning. For example, if the main message is “simple offline generator-verifier games are an effective general mechanism for self-evolution,” then the crucial comparison is not just against GRPO or Absolute Zero variants, but against closely related self-rewarding or self-consistency based preference construction methods under comparable data and model budgets. Without that, the reader cannot tell whether the observed gains come from the specific proposal or from generic self-training with DPO on synthetic preferences.

3. **The math/objective section is underspecified in ways that matter for reproducibility and for interpreting the empirical results.**  
   In **Section 2, Page 3**, the preference pair definition is written as
   \[
   (y_w,y_l)\in\mathcal{P}\quad\text{iff}\quad \mathcal{V}(q,y_w)=\texttt{Correct},\ \mathcal{V}(q,y_l)=\texttt{Incorrect}.
   \]
   But this leaves out several critical details: if there are multiple positive and negative candidates per prompt, are all Cartesian-product pairs included, or is one pair sampled, or are candidates ranked and paired by confidence? Since DPO is sensitive to pair construction, this is not a cosmetic omission. Similarly, in **Section 3.1**, the thresholded verifier produces positive, negative, or discarded labels based on \(\hat p(q,\hat y)\), but the paper does not specify how many candidates survive on average, whether the resulting class balance varies strongly with \(\tau\), or how prompts with only positives or only negatives are handled. These choices directly affect dataset size, bias, and optimization stability. The DPO objective itself is standard, but the data-generation mechanism that feeds it is not specified rigorously enough.

4. **RevisionGV is described too vaguely for a method that is claimed to outperform the single-turn variant.**  
   The update
   \[
   \hat y^{(t+1)} \sim \mathcal{G}(\cdot \mid q, f(\mathcal{V}(q,\hat y^{(t)})))
   \]
   in **Section 2, Page 3** hides most of the actual method inside the mapping \(f\). In practice, that mapping is the entire multi-turn protocol: what feedback is given, whether it includes only a binary judgment or also free-form critique, whether prior answers are shown verbatim, whether revisions are conditioned on all previous turns or only the latest one, and how the “last two responses” in **Figure 1** are selected. The main paper later says RevisionGV uses free-form feedback, but the main scientific claims depend on those details. This is not a small complaint. When a paper claims that multi-turn verification is a stronger learning signal than passive filtering, the exact structure of the feedback channel is central to the contribution.

5. **Some of the paper’s causal interpretations are stronger than what the evidence supports.**  
   For example, the discussion around **Figure 2** and the end of **Section 3.1** states that “not only does generation improve, but verification accuracy also increases, demonstrating a process of co-evolution where both roles reinforce one another.” That is a big interpretive leap from a narrow measurement. Since the same underlying model is fine-tuned, it is unsurprising that a post-trained model may score differently when used as a verifier; this does not by itself establish a co-evolution mechanism rather than simple parameter sharing or generic task adaptation. Likewise, the easy-to-hard generalization claim is suggestive, but because the training and evaluation are all within the same synthetic task family on KK, I would be careful about the strength of that wording.

6. **The main quantitative gains on the broader benchmark suite are modest and inconsistent, which undercuts the paper’s generality claim.**  
   **Table 1** is not particularly convincing as a “broad reasoning improvement” story. On Gemma-3-4B, GSM8K slightly decreases from 89.2 to 89.0, while gains on MATH500 and MATHHard are real but moderate. On Qwen2.5-7B, the KK result even drops slightly from 18.1 to 17.6, and the improvements on the math datasets are small. If the paper’s core claim is that a general offline generator-verifier game works across free-form reasoning domains, then the broader-benchmark evidence should be more robust than this. Right now the cleanest story is KK, not “diverse realistic reasoning tasks.”

7. **The paper leans heavily on KK, which is useful as a controlled setting but too narrow to carry the contribution.**  
   Most of the strongest results and nearly all ablations are on Knights-and-Knaves. I understand why, since it gives structured difficulty control and cheap labels for analysis, but it also makes the paper feel closer to a case study than a broadly validated method paper. This matters especially because the paper argues for a general approach applicable beyond domains with explicit verifiability, yet the central demonstrations of thresholding, iteration, curriculum, and cost all depend on a synthetic logic dataset with well-defined correctness. The math benchmarks in **Table 1** are much thinner in analysis and do not receive the same depth of study.

8. **The cost-performance story is not strong enough relative to the added complexity.**  
   The method requires multiple generations per prompt and multiple verifier passes per candidate. The appendix states defaults of \(n_1=8\) generations and \(n_2=16\) verifier calls, which is already expensive. **Figure 5 (Page 7)** is useful, but it mostly confirms that more compute helps, and the conclusion that verifier scaling is “typically more cost-effective” is too loosely supported by the figure alone. The paper acknowledges the cost, but does not provide a clean accounting such as tokens consumed per accepted pair, accepted-pair yield as a function of \(\tau\), or improvement per unit compute against simpler baselines like self-consistency or ordinary synthetic DPO. Without that, the reader cannot judge whether the extra machinery is actually worthwhile.

9. **The exposition is generally readable, but several claims are overstated or imprecisely worded.**  
   A notable example is in **Section 3.1**, where the paper says “As shown in Figure 2, increasing the threshold effectively improves verification accuracy.” That is true in the plotted setting, but thresholds also reduce retained data, so accuracy alone is not the operative quantity for downstream learning. This omission becomes visible in later results where \(\tau=0.6\) or \(\tau=0.7\) often outperform more conservative choices. Similarly, **Figure 4** is interpreted as showing that more data improves performance until noise dominates, but the paper does not provide the corresponding retained-pair statistics or diversity measurements, so that explanation remains speculative.

10. **There are some worrying presentation/reproducibility inconsistencies in the provided text.**  
   The manuscript begins with “Appendix” on **Page 1**, even though this is clearly the main body. The prompts in **Appendix C (Pages 15-16)** contain formatting artifacts and what appear to be broken variable names and quotation marks in the Generic Revision Prompt. Also, the math benchmark training set is described as OpenThoughts3, but the main text does not clearly explain how prompts are filtered, whether benchmark contamination was checked, or how preference pairs are distributed across task types. These are not fatal by themselves, but they do reduce confidence in the level of experimental care.

11. **The model-size scaling evidence is more mixed than the text suggests.**  
   In **Figure 3** and **Table 4**, the 1B model barely benefits and sometimes gets worse than the base model under SimpleGV. This is actually an important negative result, and I wish the paper leaned into it more. Instead, the framing is somewhat optimistic, despite the fact that the method appears to require a fairly capable starting verifier/generator before it becomes useful. That is scientifically interesting, but the current write-up uses it more as a footnote than as a central limitation.

12. **The choice of benchmark metrics and sampling protocol raises interpretation questions that are not resolved.**  
   The paper uses exact-match accuracy with one sample at temperature 0.7 for evaluation across all tasks (**Section 2.1, Page 4**). For reasoning models, especially on math tasks, single-sample exact match at nonzero temperature can introduce substantial variance and understate or distort capability relative to standard evaluation protocols. The paper says it averages over four seeds, which helps, but it does not justify why this protocol is preferable or standard for all listed benchmarks. Since some reported gains in **Table 1** are only around 0.4 to 1.5 points, evaluation design matters here.

## Questions
1. In **Section 2 / Section 3.1**, how exactly are preference pairs constructed when a prompt yields multiple positives and multiple negatives after thresholding? Do you include all \((y_w, y_l)\) combinations, sample one pair, or use some confidence-based matching? Please quantify how this choice affects dataset size and downstream performance.

2. For thresholded voting, please report the retention statistics as a function of \(\tau\): average number of accepted positives, accepted negatives, discarded candidates, and prompts with no usable pair. This would make **Figure 2** and **Figure 5** much more interpretable, because verifier accuracy alone is only half the story.

3. The broader-benchmark evidence in **Table 1** is fairly modest and somewhat mixed. Can you provide a stronger apples-to-apples comparison against methods that also use self-generated preference or self-judging signals under similar model/data budgets? This is one of the main places where additional evidence could change my view.

4. For RevisionGV, please make the feedback channel explicit in the main paper. What exactly is passed from verifier to generator, how many turns are used per sample, and how often do you observe incorrect \(\rightarrow\) correct transitions versus other trajectories such as correct \(\rightarrow\) incorrect or incorrect \(\rightarrow\) incorrect? A transition breakdown would clarify why **Table 4** improves over SimpleGV.

5. Can you quantify the compute cost more rigorously, ideally in tokens or FLOPs per accepted preference pair and per downstream accuracy point? **Figure 5** is directionally useful, but a concrete efficiency comparison against simpler self-training baselines would substantially increase confidence in the practical value of the method.

6. Since the paper emphasizes generality beyond verifiable tasks, can you provide more detail on how OpenThoughts3 examples that are not exactly checkable are handled during self-verification? This is important because the verifier is effectively acting as a noisy latent reward model, and the reliability of that process likely varies sharply across task types.

7. Please clarify whether any hyperparameters, especially the threshold \(\tau\), were selected using test performance on KK or downstream benchmarks. The paper currently reads as though \(\tau\) is tuned from observed accuracy patterns, and it would help to know what was fixed a priori.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper uses publicly available datasets and does not introduce an obvious ethics issue that requires separate review based on the main text. The main concerns here are scientific rather than ethical, namely novelty, positioning, and experimental completeness.

## Soundness Rating
2: fair. The core methodology is plausible and the experiments are not obviously invalid, but key parts of the data-construction pipeline are underspecified, several claims are stronger than the evidence warrants, and the empirical support for the broadest claims is uneven.

## Presentation Rating
3: good. The paper is generally readable and the high-level idea is communicated clearly, with useful figures such as **Figure 1**, **Figure 2**, and **Figure 5**. That said, important implementation details are buried or vague, and there are noticeable presentation inconsistencies and prompt-formatting artifacts.

## Contribution Rating
2: fair. The problem is interesting, but the paper’s technical contribution feels incremental relative to existing self-improvement and self-judging directions, and the empirical gains do not convincingly establish a sufficiently distinct advance for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is competent and relevant, and there is a real experimental signal on KK, especially for iterative and revision-based self-improvement. However, the novelty is limited, the strongest evidence is too concentrated on one synthetic benchmark, the broader comparisons are not well targeted, and several key methodological details are underspecified. I can see why some readers may find the paper interesting, but in its current form I do not think it clears the bar for the main track.

## Reviewer Confidence
4: confident. I am familiar with the area and carefully checked the main methodological and empirical claims, though some uncertainty remains because the paper omits several implementation details that would be needed for a fully definitive assessment.