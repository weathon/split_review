---
job_id: c0b66e7a-d383-4ee7-b73a-63fb3be470f1
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Xn33bU71m4.pdf
paper: LLMs as Reverse Engineers? Not Yet on Types and Names
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is an ML benchmark/evaluation study of LLMs on reverse-engineering tasks, which fits ICLR’s scope on large language models, datasets/benchmarks, and general machine learning.

## Minimum Quality
Pass ✅. The paper contains the core components expected for an empirical benchmark paper, including abstract, introduction/background, methodology, experiments, quantitative results, and conclusion; while there are serious issues in rigor, clarity, and positioning, they do not rise to the level of an automatic desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, AI-targeted prompt injection, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper evaluates a set of open-source mid-sized LLMs on reverse-engineering tasks from stripped binaries, focusing on function/variable name recovery and type inference from decompiled code, plus function name recovery from assembly. The paper also studies LoRA fine-tuning, compares decompiler outputs in a small real-world firmware setting, and introduces an automated post-processing pipeline that uses an auxiliary LLM to normalize heterogeneous model outputs for evaluation. The main empirical takeaway is largely negative: off-the-shelf models perform poorly, and fine-tuning helps inconsistently, with results still far from reliable reverse-engineering performance.

## Strengths
The paper tackles a practically relevant problem. Reverse engineering from stripped binaries is an important application area, and the question the paper asks, namely which open-source LLMs are even worth considering before task-specific fine-tuning, is useful in principle.

The evaluation scope is fairly broad at the dataset level. The paper includes multiple architectures and optimization levels, and the main paper reports x86-64 while additional architectures appear later in the provided content. Even if the conclusions are mostly negative, the coverage across x86-64, x86-32, ARM, and MIPS is more ambitious than many narrowly scoped papers.

I appreciate that the paper explicitly distinguishes multiple tasks rather than collapsing everything into “binary understanding.” Function name recovery, variable name recovery, and type inference are genuinely different problems, and the separate reporting in **Table 2**, **Table 3**, **Table 4**, and **Table 5** makes this visible.

The paper does make some effort toward standardization of model interaction. The prompt examples in **Figure 4(a)** and the extraction prompt in **Figure 4(b)** are helpful for understanding the intended automated evaluation workflow. Likewise, **Figure 3** gives a concrete example of the placeholder-based decompiled input, which is useful for readers to understand what information the models actually receive.

Some of the negative findings are still informative. For example, **Table 5** showing essentially all-zero F1 for assembly-based function name recovery across models is a fairly blunt but useful sanity check that current general-purpose LLMs are not magically solving low-level binary reasoning from assembly alone. Similarly, the fine-tuning gains in **Table 3** for variable name recovery, while inconsistent, indicate that the task is not entirely hopeless and that adaptation matters.

The comparison across decompilers in **Table 6** is a nice touch. Even though the experiment is small and underdeveloped, it is good that the paper checks whether pseudocode quality from IDA Pro versus Ghidra affects downstream recovery, instead of treating decompiler output as a fixed oracle.

## Weaknesses
I have a fairly long list of concerns. Some are about novelty and positioning, but more importantly several affect the validity and interpretability of the empirical conclusions.

1. **The paper’s central “systematic benchmark” claim is undermined by the lack of strong task-specific baselines.**  
   The paper compares nine general-purpose LLMs, but for reverse engineering this is not enough. The relevant question is not only “which generic LLM is least bad,” but also “how do these numbers compare to specialized methods for the same task?” The paper cites prior reverse-engineering systems such as Debin, StateFormer, Osprey, ReSym, and variable-name recovery work, but the experiments do not include any of them as baselines. This is a major omission because the empirical headline is essentially “LLMs are not good enough yet,” but without specialized baselines in **Tables 2–5**, it is difficult to judge whether the observed failure is due to the tasks being intrinsically hard, the prompt setup being weak, or the chosen models being inappropriate. For a benchmark paper, this matters a lot: readers need a reference point beyond near-zero F1 from generic LLMs.

2. **The main contribution is closer to an engineering benchmark than a scientific study, and the paper overstates novelty.**  
   On **Page 3**, the paper claims to conduct the “first systematic, large-scale evaluation” of multiple SOTA LLMs on both name recovery and type inference. This is a strong claim, but the paper’s actual novelty is limited to evaluating existing models with a prompting and post-processing pipeline. There is no new model, no new learning objective, no new theoretical insight, and no new evaluation principle beyond applying existing metrics and an auxiliary formatting LLM. That can still be publishable if the benchmark is rigorous and definitive, but here the rigor is not yet at that level. Right now the paper reads more like “we ran a broad set of models and found they perform poorly,” which is potentially useful, but not enough on its own for ICLR unless the study is exceptionally careful.

3. **The evaluation protocol for name recovery is underspecified in a way that directly affects the reported F1 values.**  
   In **Section 3.4** on **Page 4**, the paper says it adopts the SYMLM/CodeWordNet semantic distance method and that “the inferred name could obtain partial scores.” But it never mathematically defines how those partial semantic similarity scores are converted into precision, recall, and F1 at the sample level or corpus level. If a prediction has semantic similarity score \(s \in [0,1]\), is it treated as a soft true positive? Is there a threshold \(\tau\) such that a match counts if \(s \ge \tau\)? If there are multiple names per function, how are predictions aligned with targets? The paper later reports standard precision/recall/F1 in **Tables 2–6**, but the mapping from semantic similarity to these discrete metrics is not specified. This is not a cosmetic issue. Different aggregation rules can materially change low-score regimes, especially when most reported F1 values are between 0.00 and 0.10. The paper needs to define the metric formally, for example something like
   \[
   \mathrm{Prec} = \frac{\sum_i w_i^{\text{match}}}{|\hat{Y}|}, \quad
   \mathrm{Rec} = \frac{\sum_i w_i^{\text{match}}}{|Y|}, \quad
   \mathrm{F1} = \frac{2 \,\mathrm{Prec}\,\mathrm{Rec}}{\mathrm{Prec}+\mathrm{Rec}},
   \]
   and then state exactly how \(w_i^{\text{match}}\) is computed from CodeWordNet similarity and how predicted identifiers are matched to gold identifiers.

4. **The use of an auxiliary LLM for response extraction introduces a second model into the evaluation loop, but its reliability is not validated.**  
   This is one of the paper’s most important methodological choices, introduced in **Section 3** on **Page 3** and illustrated in **Figure 4(b)**. The problem is real, different LLMs emit different formats, but using another LLM as a parser is not neutral. It can hallucinate, normalize away ambiguity incorrectly, or effectively “repair” weak outputs. The paper gives no quantitative validation of this step, such as agreement with manual extraction on a randomly sampled subset, error rates of the parser, or examples where parser decisions change scores. Since the pipeline’s central premise is fair standardized comparison, this missing validation is a serious flaw. If the extraction LLM misreads outputs unevenly across models, the benchmark is biased in unknown ways.

5. **There is substantial ambiguity about what exactly is being predicted for name recovery, especially for functions with multiple callees.**  
   On **Page 2**, the paper says it extends prior work by requiring LLMs to infer “all function names appearing inside the function body, which considers every callee function.” This is a major change in task definition relative to conventional function-name recovery, but the paper does not cleanly formalize it. Is the target for each sample a set \(Y = \{y_1,\dots,y_m\}\) of all callee names plus the enclosing function name? Does order matter? How are duplicate callees handled? How is cardinality mismatch scored when the model outputs fewer names than required, which the paper itself notes happens frequently on **Page 9**? Without a crisp task definition, **Table 2** and the surrounding discussion are hard to interpret.

6. **The fine-tuning setup is far too thinly specified for a paper that draws conclusions about the benefit of fine-tuning.**  
   **Section 3.3** on **Page 3** says the authors use LoRA, but almost none of the details that would make the comparison interpretable are in the main paper. The rank \(r\), target modules, learning rate, batch size, number of epochs or total optimization steps, sequence length, optimizer, scheduler, checkpoint selection rule, and whether all models used matched budgets are absent from the main text. **Table 7** reports time for “200 steps,” but it is not even clear whether 200 steps is the actual full training budget for all models or just a reference measurement. This matters because many of the paper’s conclusions, such as “fine-tuning generally improves name recovery, but gains are inconsistent” and the standout improvement claims in **Table 3**, are impossible to assess fairly if models may be undertrained or trained under mismatched conditions.

7. **The interpretation of results is often overconfident relative to the evidence.**  
   Several “Findings” in **Pages 6–8** are stronger than what the reported experiments support. For example, “training data quality is a more decisive factor” and “training quality significantly impacts performance” are plausible hypotheses, but the paper does not actually isolate training data quality as a variable. Comparing CodeLlama to Llama2 or Qwen2.5 to DeepSeek-R1 does not establish causality, because these models differ in many ways beyond data quality, including post-training objectives, instruction tuning, tokenizer details, and perhaps reasoning behavior. Likewise, **Figure 2** and the associated text support a much narrower conclusion, namely that within the tested CodeLlama family and current setup, larger parameter count did not lead to clear gains. They do not justify a broad claim about model size being generally unimportant.

8. **The paper’s own tables raise unanswered questions that are not analyzed.**  
   For instance, in **Table 3** on **Page 6**, some fine-tuned variable-name recovery results improve dramatically at \(O0\) but collapse at other optimization levels, and some models, like DeepSeek-V2 at \(O1\), get worse after fine-tuning. In **Table 4**, some fine-tuned type inference results become exactly 0.00, which is striking. These are not small fluctuations, they suggest either optimization instability, formatting/extraction failures, or data-distribution shifts across optimization levels. Yet the analysis only says improvements are “inconsistent.” That is too hand-wavy. A benchmark paper should explain anomalies, not merely report them.

9. **The x86-64 centric presentation weakens the “large-scale” claim in the main narrative.**  
   On **Page 5**, the paper says due to page limits it presents results primarily on x86-64 and places the rest elsewhere. That is understandable, but the main conclusions are then written in a way that sounds universal. However, the extra architecture tables later in the provided content show nontrivial variation across x86-32, ARM, and MIPS. For example, variable-name recovery on ARM in **Table 10** is materially higher after fine-tuning than the x86-64 numbers in **Table 3**. If architecture sensitivity exists, the paper should discuss it in the main text rather than collapsing it into “similar trends.” Otherwise the claimed conclusions are oversimplified.

10. **The real-world firmware experiment is too underdescribed to carry much weight.**  
    **Table 6** on **Page 7** reports near-zero F1 on real-world firmware and suggests IDA Pro generally yields better pseudocode than Ghidra. But the paper does not specify the number of firmware binaries, domains, labeling procedure, symbol provenance, architecture mix, or whether the firmware dataset overlaps with the GNU-style training/evaluation distribution. With so little detail, this section reads more like a teaser than substantive evidence. Since the paper uses it to support external validity, the missing details matter.

11. **There are consistency and presentation issues that make the experimental story harder to trust than it should be.**  
    A few examples: **Table 1** says “nine” LLMs, while **Section 4.2** says “eight mainstream code LLMs”; the paper alternates between “Deepseek-R1” and “DeepSeek-R1,” “decompiled/decomplied/decomposed,” and “decompilers/decompliers”; and **Table 4** says “x64” while elsewhere the paper uses “x86-64.” These are not fatal individually, but in a benchmark paper they accumulate and reduce confidence that the pipeline and reporting were carefully audited.

12. **Some figures are useful, but others expose the paper’s analytical shallowness.**  
    **Figure 1** does clearly show that removing CodeWordNet lowers the reported function-name recovery F1, which supports the paper’s point that strict string matching is too harsh. However, the figure also indirectly reveals how dependent the conclusions are on a semantic scoring choice that is not formally specified. This should have prompted a sensitivity analysis, not just a one-line takeaway.  
    **Figure 2** is also informative, especially the three subplots for function-name recovery, variable-name recovery, and type inference across CodeLlama sizes. But the visual pattern is weakly analyzed. The paper jumps from “34B does not beat 7B” to “training quality is more important than parameter count,” which is not demonstrated by this figure. The figure supports a local empirical observation under one family and one prompting/evaluation setup, nothing more.

13. **The task setup may unintentionally strip away information in a way that makes the benchmark less representative, but the paper does not discuss this trade-off.**  
    The placeholder normalization shown in **Figure 3** replaces identifiers with tokens such as `FUNC`, `VAR`, and `TYPE`. This can reduce decompiler artifacts, but it also changes the nature of the task. In real reverse engineering, useful lexical hints, calling conventions, library traces, and partially preserved names can matter. By aggressively normalizing, the paper may be evaluating a cleaner but also more artificial task. That would be acceptable if discussed as a deliberate abstraction, but the paper presents the setup as more direct measurement of reverse-engineering ability, which is debatable.

14. **The reproducibility statement is weaker than it sounds because crucial parts of the protocol are not fully pinned down in the main paper.**  
    The paper says on **Page 9** that results can be reproduced by running identical scripts but “the number will be similar, but not identical.” That is fine in spirit, yet the main paper does not specify enough details to let readers understand the major sources of variance or what counts as “similar.” In a low-score regime, a shift from 0.02 to 0.05 can change the apparent ranking of models. Without clearer reporting of seeds, decoding parameters, parsing stability, and fine-tuning selection criteria, reproducibility remains weak.

## Questions
1. **Please formally define the name-recovery metric.**  
   I would like the authors to provide an explicit mathematical definition of how CodeWordNet similarity is converted into precision, recall, and F1 when there are multiple identifiers per sample. This is the single most important clarification that could increase my confidence in the reported numbers.

2. **How accurate is the auxiliary LLM-based extraction step?**  
   Please report a manual audit on a representative subset, for example 200 samples per model, comparing automated extraction against human parsing. What is the extraction error rate, and how often does it change correctness labels or F1? If the answer is “rarely,” that would substantially strengthen the paper.

3. **What exactly is the target set for function name recovery in decompiled code?**  
   Is the model asked to recover only the enclosing function name, or the enclosing function plus all callees, or only callees? The wording in **Page 2** and **Page 5** is not sufficiently precise. Please define the prediction object and matching procedure.

4. **Please provide the missing fine-tuning details in the main paper.**  
   At minimum: LoRA rank, alpha, target modules, learning rate, batch size, number of epochs or total steps, sequence length, optimizer, decoding settings, and model selection criterion. Without these, it is impossible to know whether the inconsistent fine-tuning results reflect true model behavior or simply training-budget mismatch.

5. **Can the authors include task-specific baselines from prior reverse-engineering work?**  
   Even if direct reproduction for all methods is too costly, a comparison against at least one specialized baseline for variable names and one for type inference would greatly improve the scientific value of the paper. Right now, the benchmark lacks a meaningful yardstick.

6. **Please analyze the strong optimization-level and architecture effects instead of relegating them to appendices or side tables.**  
   For example, why do some models show large gains at \(O0\) but not \(O2/O3\), and why does ARM variable-name recovery appear more favorable than x86-64 in the provided later tables? A short analysis would make the benchmark much more insightful.

7. **How much do the conclusions depend on decoding choices and prompt template choices?**  
   The paper itself notes on **Page 8** that prompt template structure strongly affects training time and that some models emit long chain-of-thought style outputs. A sensitivity study over temperature, max tokens, and prompt template variants could materially affect the conclusion that models are uniformly poor.

8. **For the firmware experiment, please provide dataset details and sample size.**  
   How many firmware images/functions were used, from what sources, under what architectures, and how were gold names/types obtained? Without this, **Table 6** is hard to evaluate.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None. The paper evaluates models on reverse-engineering tasks using software artifacts; I did not identify a concrete ethics issue from the main paper content that would require escalation.

## Soundness Rating
2: fair. The paper asks a legitimate question and provides substantial empirical effort, but core evaluation details are underspecified, the auxiliary LLM-based parsing is unvalidated, and several conclusions are stronger than the evidence supports.

## Presentation Rating
2: fair. The paper is readable at a high level, and some figures/tables are useful, but important task definitions and metric details are missing, results are sometimes inconsistently described, and the writing has enough notation/terminology inconsistencies to hurt trust.

## Contribution Rating
2: fair. The benchmarking angle is relevant and potentially useful, especially the negative result that generic LLMs are weak on these tasks, but the lack of strong baselines, limited analytical depth, and insufficiently specified protocol keep the contribution below ICLR bar.

## Overall Rating
2: Reject, not good enough. The topic is relevant and the empirical effort is nontrivial, but the current paper is not rigorous enough as a benchmark, is missing key baselines and formal metric definitions, and draws broader conclusions than the evidence can support.

## Reviewer Confidence
4: confident. I am familiar with LLM evaluation and program-analysis/reverse-engineering style benchmarking, and I checked the main experimental design and reporting carefully, though some implementation specifics are missing from the paper.