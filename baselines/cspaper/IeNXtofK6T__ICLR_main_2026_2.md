---
job_id: cef05ff1-ecc0-4c17-b215-1a391b14dd1c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: IeNXtofK6T.pdf
paper: PromptArmor: An Essential Baseline for Prompt Injection Defenses
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ML safety and LLM robustness, specifically prompt injection defenses for LLM agents, which fits ICLR’s scope on safety, language models, and general machine learning.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, method description, experiments, quantitative results, related work, and conclusion; while I have concerns about novelty and evaluation completeness, these are review-level issues rather than desk-reject-level deficiencies.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious reviewer-targeting text, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper revisits a simple defense idea for prompt injection, namely using an off-the-shelf LLM as a guardrail that detects whether retrieved content contains an injected prompt and, when detected, extracts and removes it before passing sanitized content to the backend model. The paper introduces PromptArmor, evaluates it on AgentDojo, Open Prompt Injection, and TensorTrust with several proprietary and open-source guardrail LLMs, and argues that strong modern LLMs make this previously weak baseline surprisingly effective. The experiments also include comparisons to prior defenses, prompting ablations, model-size/reasoning analyses, a memorization check, and an adaptive-attack evaluation.

## Strengths
The paper’s biggest strength is practical relevance. A defense that can be inserted as a modular guardrail without retraining the application model is genuinely useful, and the paper makes that deployment angle very clear in **Figure 1** and **Figure 2** on **Page 3-4**. In particular, **Figure 2** is effective because it shows the entire workflow, from raw contaminated sample, to guardrail prompt, to extracted injection text, to sanitized output. That figure helps the reader understand that the contribution is not just binary detection, but a detect-and-remove pipeline.

The empirical headline results are strong on the chosen benchmarks. **Table 1** on **Page 5** shows a large gap between GPT-3.5 and stronger guardrail models, which supports the paper’s central claim that the historical dismissal of prompt-only defenses may partly be an artifact of weaker older models. The contrast is especially striking on AgentDojo, where GPT-4o and GPT-4.1 achieve very low FPR/FNR, while GPT-3.5 is far worse.

The comparison against prior defenses on the agent benchmark is useful. **Table 2** on **Page 7** suggests that PromptArmor with GPT-4o/4.1 is competitive or stronger than the listed baselines on AgentDojo, and the inclusion of both security metrics (ASR, FNR) and utility-related metrics (UA, FPR) is appreciated. The fact that the paper reports not only attack blocking but also continued task completion after sanitization is better than a purely detection-only framing.

I also appreciated the ablation on prompting strategy in **Table 3** and the model-scale/reasoning study in **Figure 3** on **Page 8**. **Figure 3(b)** and **Figure 3(d)** support a nuanced claim: reasoning helps somewhat in mid-sized models, but capacity appears more important overall. This is more informative than simply claiming “reasoning fixes prompt injection.”

The paper is generally readable. The motivation is clear, the benchmark descriptions are understandable, and the system prompts are at least disclosed in the appendix, which helps reproducibility.

## Weaknesses
1. **The main contribution is mostly a re-evaluation of an existing baseline with stronger proprietary models, and the paper overstates how much methodological contribution there is.**  
   The core method in **Section 3.1** on **Page 3** is: prompt a stronger LLM to detect injected content, ask it to output the injection span, then remove it with fuzzy matching. That is operationally useful, but scientifically it is fairly incremental. The paper’s own framing admits this is revisiting prior prompting-based defenses rather than introducing a new defense principle. The novelty then has to come from either a deeper conceptual analysis of why this now works, or a more rigorous experimental demonstration of when it works and fails. Right now, neither is developed enough. The “design rationale” in **Section 3.2** is mostly qualitative prose and reads more like a systems pitch than a scientific mechanism analysis. For an ICLR main-track paper, “modern LLMs are better than old LLMs at this task” is an interesting observation, but not yet a fully convincing research contribution by itself.

2. **The evaluation is heavily benchmark-bound, and the paper does not establish that the defense generalizes beyond the template structure of the selected datasets.**  
   This matters because prompt injection defenses often look good on curated attack distributions and then degrade badly under distribution shift. The paper evaluates on AgentDojo, Open Prompt Injection, and TensorTrust, which is a reasonable set, but all three are existing benchmarks with fairly recognizable attack styles. The adaptive evaluation in **Section 4.6** is a useful step, but it is still restricted to top-5 attack templates produced by one attack generator on AgentDojo. That is not enough to support a broad claim that PromptArmor is “robust against adaptive attacks.” I would be much more convinced by stronger distribution-shift testing, for example attacks with paraphrased semantics, obfuscated multi-hop instructions, long-context burying, benign-looking conflicting instructions, or attacks that explicitly target the extraction-removal stage rather than only the detect stage. As written, the evidence supports “strong on these benchmarks,” not “robust baseline in general.”

3. **The sanitization step is underspecified and potentially brittle, yet it is central to the end-to-end claims.**  
   In **Section 3.1** on **Page 3**, the paper says it extracts all words from the LLM output and constructs a regex that allows arbitrary characters between words; the appendix code on **Page 15-16** reveals this is actually bounded by `.{0,20}` between consecutive words. This implementation detail is not minor. It directly determines whether the extracted text can be removed correctly, whether benign surrounding content gets deleted, and whether attackers can evade sanitization by spacing or interleaving content beyond the threshold. The current presentation never formalizes the sanitization function. At minimum, the paper should define something like
   \[
   \hat{i} = G_\phi(x, c), \qquad x' = S(x, \hat{i}),
   \]
   where \(x\) is the raw retrieved text, \(c\) is the user-task context, \(G_\phi\) is the guardrail LLM, and \(S\) is the fuzzy-removal operator, then analyze failure cases of \(S\). Right now, end-to-end success depends on this operator, but there is no quantitative evaluation of sanitization precision/recall at the span level, no measure of over-deletion, and no ablation on the regex threshold. That omission matters because a defense that detects correctly but removes text incorrectly can still damage user utility or silently alter evidence.

4. **The paper reports utility under attack, but it does not evaluate utility preservation on clean inputs after sanitization in a sufficiently direct way.**  
   The argument for removal rather than outright rejection is that the backend LLM should still be able to complete the intended task. However, the clean-data utility story is underdeveloped. **Table 2** on **Page 7** reports UA under attack, which is useful, but does not answer a very practical question: when the detector produces a false positive and sanitizes a benign sample, how much useful information is removed and how often does that break the task? This is especially important because PromptArmor-GPT-3.5 has an **11.24% FPR** in **Table 2**, which is operationally quite large. Even for GPT-4o/4.1, very small FPR does not by itself prove benign-task preservation after sanitization. I would have liked a separate clean-only utility benchmark comparing original performance versus performance after the guardrail pipeline, including cases where benign text contains instruction-like patterns. Without that, the utility claims are incomplete.

5. **The comparison to baselines is informative but not fully fair or fully contextualized.**  
   In **Section 4.2** on **Page 6-7**, the paper compares against Deberta, Llama Prompt Guard 2, DataSentinel, MELON, prompt augmentations, and Tool Filter. The issue is that several baselines appear to be evaluated in forms that are unlikely to be their strongest or most natural deployment configurations, while PromptArmor is allowed to use powerful proprietary frontier LLMs. The discussion explicitly attributes DataSentinel’s weaker results partly to its released checkpoint using Mistral-7B and not being adapted to the agent setting. That may be true, but then the comparison is partly a comparison of model budget and adaptation effort, not purely of defense principle. More generally, if the paper’s thesis is “this should be a standard baseline,” then cost-latency-performance tradeoffs should be front and center. Yet the paper claims “computational efficiency” in **Section 3.2** on **Page 4** without reporting latency, token usage, or inference cost. That claim does not survive contact with the fact that one of the strongest variants uses GPT-4.1 as a separate guardrail call before the backend GPT-4.1 call. For deployment, that is not a footnote, it is the main bill.

6. **The prompting setup is benchmark-specific, which weakens the claim that the method is a generic baseline.**  
   On **Page 6**, the paper states: “Given the varying settings of the benchmarks, we adjusted the detection prompt for each dataset.” This is more important than the paper treats it. The prompts in the appendix are not minor formatting changes; they encode benchmark-specific assumptions. For example, the Open Prompt Injection prompt in **Listing 3** on **Page 15** is tailored to “exactly two distinct instructions,” which is a strong structural prior about that dataset. The TensorTrust prompt in **Listing 4** is highly task-specific, explicitly naming prompt extraction and hijacking attack patterns. This is not a generic detector prompt. It is a benchmark-adapted prompt engineer’s solution. That does not invalidate the results, but it does undermine the stronger claim that PromptArmor should be considered a standard baseline in a broad sense. A more honest statement would be that benchmark-tuned prompting of strong LLMs is a strong baseline.

7. **Some central claims are stronger than the evidence warrants, particularly around “reasoning” and “memorization.”**  
   The paper repeatedly attributes gains to “reasoning capabilities.” But what is shown in **Table 1** and **Figure 3** is correlation between better models, larger models, reasoning mode, and performance. That does not isolate reasoning as the causal factor. In **Figure 3**, model size clearly dominates at least as much as reasoning mode; the text on **Page 8** even says capacity appears to be the primary factor. The introduction and conclusion should be toned down accordingly.  
   Similarly, the memorization argument in **Section 4.5** on **Page 8** is too casual. An average similarity of 0.34 and 3.5% above a 0.6 threshold does not really justify the strong reassurance that GPT-4.1 is “not likely” to have memorized benchmark samples, especially when the benchmark data may share stylistic regularities with pretraining corpora. This is a weak sanity check, not strong evidence against contamination.

8. **There is a missing level of granularity in the results tables, which hides likely failure modes.**  
   **Table 1** collapses performance over all subdomains and attack types, and **Table 2** averages over four AgentDojo attacks. That presentation is convenient, but it hides whether the method fails systematically on one attack family, one environment, or one class of user task. This matters because a defense with 0.13% average FNR could still have a concentrated blind spot that is operationally serious. The paper should provide per-attack and ideally per-environment breakdowns in the main paper, not only aggregate numbers.  
   Relatedly, **Figure 3** is a good start, but the figure would be more convincing if the exact numeric values for all bars were tabulated or discussed more systematically. For instance, **Figure 3(c)** suggests the 32B model with PromptArmor even slightly exceeds the GPT-4.1 reference utility; that is interesting and deserves explanation, since one would normally expect an added guardrail layer to at best preserve, not improve, task utility unless it is blocking attacks that the baseline backend mishandles.

9. **The paper lacks a formal problem statement for the end-to-end objective, which makes some of the claims hard to evaluate precisely.**  
   The paper defines FPR, FNR, UA, and ASR, but the method itself is not formalized. Given that the defense makes two decisions, detection and extraction/removal, it would help to specify the target behavior mathematically. For example, with \(y \in \{0,1\}\) denoting contamination and \(x'\) the sanitized text, the defense should ideally minimize something like
   \[
   \mathbb{P}(\hat{y}=1 \mid y=0) + \mathbb{P}(\hat{y}=0 \mid y=1)
   \]
   subject to preserving downstream task success on benign or sanitized inputs. More concretely, there is no explicit decomposition of end-to-end failure into detector error, extractor error, and backend-agent error. Because of that, it is difficult to tell from **Table 2** whether residual ASR comes from missed detection, bad extraction, or backend susceptibility after partial sanitization. This is not a request for “more theory” for theory’s sake; it would materially clarify what part of the pipeline is doing the work and what part still fails.

10. **Presentation is decent overall, but there are several places where wording is too confident or imprecise.**  
   The claim in **Section 3.2** that PromptArmor is computationally efficient is not supported by reported cost or runtime. The phrase in the abstract that PromptArmor can “accurately detect and remove injected prompts” is also too broad given that extraction quality is not directly measured. There are also a few writing issues, for example the argument around GPT-3.5 “not understanding” prompt injection in **Section 4.3** on **Page 7** is anecdotal and would be better supported by systematic prompt variants rather than a single qualitative explanation.

## Questions
1. **How much of the reported gain comes from benchmark-specific prompt engineering versus the general capability of strong LLMs?**  
   Please provide a cleaner separation here. For example, can the authors report results using one generic detector prompt across all three datasets, and compare that to the benchmark-specific prompts used in the paper? This would substantially increase my confidence in the “standard baseline” claim.

2. **Can the authors quantify sanitization quality directly?**  
   I would like to see span-level metrics for extracted injection text, such as exact match or token-level precision/recall/F1 between the removed span and the ground-truth injected segment, at least on datasets where the injected text is known. This would clarify whether low ASR is driven by accurate removal or by a mix of partial deletion and backend robustness.

3. **What is the clean-task utility impact of false positives and benign over-deletion?**  
   Please report task success on clean inputs before and after the full PromptArmor pipeline. If possible, include examples where benign content contains imperative language or multiple instructions, since those are likely false-positive cases.

4. **Can the authors break down AgentDojo results by attack type and environment?**  
   A per-attack and per-environment table would help determine whether the near-zero average FNR in **Table 2** masks any concentrated failure modes.

5. **What are the latency and cost overheads of PromptArmor?**  
   Since the paper argues for PromptArmor as an essential baseline and highlights ease of deployment, practical overhead matters. Reporting average extra tokens, API latency, and approximate cost per protected query for GPT-4o and GPT-4.1 would make the paper much more actionable.

6. **How robust is the fuzzy-matching sanitization to formatting and obfuscation?**  
   In the appendix code, consecutive extracted words may be separated by up to 20 arbitrary characters. How sensitive are results to this threshold? Can attackers evade removal by inserting larger gaps, HTML tags, or content interleaving? An ablation on this parameter would be useful.

7. **Can the authors clarify the end-to-end failure decomposition?**  
   For the non-zero ASR cases, how often is the cause: (i) detector says “No” despite contamination, (ii) detector says “Yes” but extraction misses the malicious span, or (iii) extraction removes the span but the backend still executes the injected intent? This would sharpen the scientific understanding of the method.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
This paper is about prompt injection defenses, so it naturally sits in a security-sensitive area. While the submission is defense-oriented and does not appear to introduce a substantially new attack method, it does discuss concrete attack patterns, adaptive attacks, and benchmarked exploit settings for LLM agents, especially in **Sections 4.1 and 4.6** on **Page 5** and **Page 8-9**. I do not view this as a reason to reject the paper, but it is appropriate for ethics review because publication could influence how attackers and defenders think about guardrail behavior, benchmark-specific defenses, and sanitization mechanisms. The main issue is standard dual-use security risk rather than an ethical violation by the authors.

## Soundness Rating
2: fair. The empirical results are substantial and generally support the narrow claim that strong LLM-based prompting is a competitive benchmark on the tested datasets, but several broader claims are overstated, the sanitization component is under-analyzed, and the evidence for robustness/generalization is not yet strong enough.

## Presentation Rating
3: good. The paper is readable and the figures/tables are helpful, especially **Figure 2**, **Table 1**, and **Table 2**, but some key claims are phrased too strongly, several implementation details that matter scientifically are pushed out of the main method description, and the benchmark-specific prompting choices need more explicit discussion.

## Contribution Rating
2: fair. The practical finding is useful and worth knowing, but the methodological novelty is limited, and the paper does not yet provide enough deeper analysis or generalization evidence to elevate the contribution to a strong ICLR main-track level.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper has a timely and practically useful message, and the benchmark numbers are strong enough that I would not object strongly to acceptance. However, I lean negative because the work is primarily a strong re-benchmarking and prompt-engineering study rather than a deeper scientific advance, and the current evidence does not fully justify the broad claims about robustness, genericity, and deployability.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the methodological and empirical details carefully, but some uncertainty remains because several baselines and adaptive-attack settings depend on implementation choices not fully unpacked in the main text.