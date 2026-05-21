---
job_id: eb5678db-a6ae-4f57-bebb-56527e85ca91
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: VK5G3Ff4Ty.pdf
paper: Is Model Size a Barrier to Quality? Evaluating Small Language Models for Clinical Text Summarization and Report Generation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as an empirical study of language and vision-language models for clinical summarization/report generation, with emphasis on model scaling, adaptation, and safety-related evaluation.

## Minimum Quality
Pass ✅. The paper contains the required components, including Abstract, Introduction, Related Work, Experimental Setup, Results, and Discussion/Conclusion. That said, there are serious issues in rigor, reporting, and clarity that substantially weaken the submission, but they do not rise to the level of an automatic desk rejection based on the provided text alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts or explicit attempts to manipulate automated reviewing in the paper content. There are some stray markup artifacts and malformed tags, but these look like formatting/editing problems rather than review manipulation.

# Expected Review Outcome:
## Summary
This paper studies whether small language models and small vision-language models can match larger medically adapted models on two clinical generation tasks, consumer health question summarization using MeQSum and radiology report generation using MIMIC-CXR. The paper compares several open-source small and large model families under zero-shot, few-shot, and PEFT fine-tuning settings, and introduces a “Collapse Analysis” intended to track task adherence, hallucination rate, concept recall, and prompt robustness across model scales. The main claim is that for text summarization, models around the 1B range can become competitive or better after LoRA-style adaptation, while for radiology report generation, small VLMs still trail larger medical VLMs.

## Strengths
The paper tackles a practically important question. In clinical settings, deployment constraints, privacy, and on-premise inference genuinely make the small-vs-large tradeoff worth studying, so the problem framing is relevant and timely.

The submission includes both text-only and multimodal settings rather than focusing on a single benchmark. Evaluating MeQSum and MIMIC-CXR in one paper gives a broader perspective on where compact models may suffice and where they may not.

I appreciated the attempt to go beyond a single automatic metric. In particular, the inclusion of MEDCON in **Table 2** and **Table 4** is useful because it at least tries to assess clinical concept overlap rather than relying only on BLEU/ROUGE. The idea behind the “Collapse Analysis” in **Table 3**, namely that failures under scale reduction may appear first as prompt sensitivity and hallucination rather than only mean metric degradation, is directionally interesting.

Some of the figures are helpful in conveying the claimed story. **Figure 1** gives a readable overview of the intended experimental workflow, namely model families crossed with tasks and adaptation methods. **Figure 4** is also one of the more informative qualitative elements in the paper, because it attempts phrase-level comparison between a small and a larger VLM against the ground truth, which is more helpful than abstract claims about “better alignment.”

The paper also makes an effort to include qualitative failure analysis. The SmolLM2 hallucination example shown in **Figure 5** is useful because it concretely illustrates the kind of instruction drift the authors discuss, rather than leaving hallucination as a vague concern.

## Weaknesses
1. **The experimental design is much less controlled than the paper’s main claims suggest, especially for the central “small vs large” conclusion.**  
   The title and abstract frame the paper as an evaluation of whether model size is a barrier to quality, but the comparisons confound size, architecture family, training data, instruction tuning, and domain adaptation. This is visible already in **Table 1** and the surrounding text in **Section 3**. The “small” and “large” models are not cleanly paired versions of the same pretrained family with matched tokenizer/training recipe/domain exposure. For instance, SmolLM, Gemma, and LLaMA are compared against BioMistral, Med-LLaMA, and OpenBioLLM, which differ in both base architecture lineage and medical adaptation strategy. In the VLM case, Florence 2 and Qwen2.5-VL are compared against Med-Flamingo and LLaVA-Med, again mixing architecture and pretraining differences with model size.  
   Why this matters: the paper repeatedly attributes performance differences to capacity thresholds or “minimum viable scale,” but the evidence does not isolate scale as the causal variable. At best, the results show that some small open models can be competitive with some larger medical models under this specific setup. That is a much narrower claim than the manuscript currently makes.

2. **The proposed “Collapse Analysis” is underspecified to the point that its main table is not really interpretable.**  
   **Table 3** is central to the paper’s narrative, yet the paper never formally defines how *Task Adherence*, *Hallucination Rate*, *Concept Recall*, *Robustness*, or *Readiness Score* are computed. The manuscript states that these dimensions were assessed, but does not describe the annotation protocol, whether they are manual or automatic, how many samples were judged, whether multiple raters were used, how “hallucination” is operationalized, or how the final readiness score is aggregated from the four dimensions. The phrase “we identify a safety threshold at approximately 1B parameters” rests almost entirely on this table, but the reader is not given the necessary methodology to verify or trust the numbers.  
   Why this matters: this is not a minor reporting omission. The paper’s most distinctive claim, a sharp safety collapse below 1B, depends on metrics whose definition and measurement pipeline are missing. Without those details, **Table 3** is closer to an unsupported dashboard than evidence.

3. **The mathematical formulation for fine-tuning is too generic and does not define the actual method used.**  
   On **Page 5**, the paper introduces
   \[
   \Delta \theta^* = \arg\min_{\Delta\theta}\frac{1}{N}\sum_{i=1}^{N}-\log p_{\theta_0+\Delta\theta}(y_i\mid[\tau;x_i]).
   \]
   This is just standard supervised cross-entropy over prompted inputs. It does not specify the LoRA parameterization, rank \(r\), target modules, adapter placement, quantization details for QLoRA, optimizer settings, sequence formatting, truncation policy, or whether \(y_i\) is teacher-forced token-by-token text for both summarization and VLM report generation. For VLMs, the notation is even more problematic because \(x_i\) is said to be “a patient query or image,” but a single conditional language-model expression over \([\tau;x_i]\) obscures the multimodal tokenization/fusion mechanism.  
   Why this matters: the paper uses this equation as if it substantiates the adaptation methodology, but it does not capture the actual training setup and leaves important implementation choices unspecified. If the authors want to claim methodologically meaningful PEFT comparisons, they need to explicitly define, at minimum, the LoRA decomposition, e.g. \(W' = W + BA\) with rank \(r\), and clarify how this is instantiated for each backbone.

4. **Key experimental details needed to judge soundness are absent or contradictory.**  
   The paper states in **Section 3** that “All runs employ identical inference settings” and also says outputs are generated using three stochastic decoding strategies, top-\(k\), top-\(p\), and temperature sampling. It is unclear whether these are applied jointly, separately, or whether results are averaged across decoding methods. This is especially important because the paper discusses hallucination and prompt robustness, both of which can be highly decoding-sensitive.  
   Similarly, the paper says zero-shot performance in **Table 2** is “across five prompt templates, averaged over all test samples,” but it does not report variance across prompts, per-prompt minima/maxima, or confidence intervals. The few-shot results are described narratively in **Section 3.1**, but the actual table is missing. For VLM fine-tuning on MIMIC-CXR, there is no train/validation/test split description beyond “10,000 image-report pairs sampled from MIMIC-CXR,” and no explanation of model selection, early stopping, or whether any held-out validation set was used.  
   Why this matters: when the paper makes claims about stability, robustness, and safety thresholds, lack of experimental detail substantially undermines the evidence.

5. **Several headline empirical claims are not adequately supported by the presented tables and figures.**  
   In **Table 2**, the zero-shot results do not actually support a strong “small models rival large medical LMs” conclusion across the board. SmolLM2 has decent BERTScore and middling MEDCON, but BLEU and ROUGE-L are mixed, and the larger models are not uniformly beaten. On the contrary, OpenBioLLM has the highest MEDCON, BioMistral has the highest BLEU, and SmolLM2 has the highest BERTScore. The evidence is more nuanced than the text suggests.  
   The paper then claims in **Section 4** and **Section 5** that “all small LMs outperformed large LMs across every metric” after LoRA fine-tuning, but the main paper does not provide a proper quantitative table for these fine-tuned summarization results. Instead, the reader gets a collection of bar plots in **Figure 3** and two scatter-type figures around **Figure 2**. These visuals are insufficient for close comparison because exact values, standard deviations, and statistical uncertainty are absent.  
   Why this matters: the strongest claims in the paper are post-fine-tuning claims, yet those are not documented with the same clarity as the zero-shot table. A paper making comparative benchmark claims should present exact numbers in a table, not only stylized plots.

6. **The presentation and figure usage are often confusing, and some figures do not support the claimed conclusions as strongly as the text implies.**  
   **Figure 2** is described as showing that LoRA fine-tuned LLaMA-3.2 1B has “comparable results” to its larger counterparts. But visually, the figure is a parity-style scatter against specific baselines with a diagonal line, and it only contains four metrics. It does not show uncertainty, prompt-to-prompt variability, or dataset-level robustness. Also, the caption and text have grammatical issues and use “it’s counterpart models,” which adds to the impression that the figure was not carefully prepared.  
   **Figure 3** attempts to compare ICL versus LoRA across models, but the labeling is fragmented across multiple subplots and the legend/model-color mapping is awkwardly split over intervening images. This makes it unnecessarily hard to parse which bars correspond to which models. More importantly, the figure is used to support broad claims about LoRA superiority, but it does not separate gains from possible overfitting or from differences in prompt templates/decoding.  
   Why this matters: the paper relies heavily on figures for its positive message, yet those figures are not crisp enough to bear that argumentative load.

7. **The VLM evaluation is too thin to support the broader claim that visual reasoning “demands greater capacity.”**  
   **Table 4** shows that the small VLMs underperform Med-Flamingo on BLEU-4, ROUGE-L, and MEDCON, but BERTScore is actually higher for Qwen2.5-VL (0.8146) than for both larger models (0.7100 and 0.6850). The paper does not discuss this discrepancy in a careful way. If BERTScore is supposed to capture semantic alignment, why is the conclusion so categorical that small VLMs “remain below the large VLM baselines in all metrics” on **Page 7**, when the table directly contradicts that statement?  
   Also, the setup compares fine-tuned small VLMs against large medical VLM baselines, but it is not clear whether the large VLMs are also fine-tuned on the same 10k MIMIC-CXR subset, used zero-shot, or taken from prior checkpoints with entirely different training histories. The fairness of the comparison is therefore ambiguous.  
   Why this matters: the paper’s second major conclusion, that radiology report generation fundamentally requires larger capacity, is too strong relative to the evidence shown in **Table 4** and the under-described training setup.

8. **There are substantial clarity and editing problems that hurt credibility and make careful reading harder than it should be.**  
   Examples include inconsistent model names such as “SmolLM3-3B” in **Table 3** versus “SmolLM2” elsewhere, “SemoLM2” appearing in the text near **Figure 3**, and malformed markup strings like `</more_detailed_caption>` leaking into the main body on **Page 7** and **Page 15**. The paper also references “Table ??” on **Page 7**, which suggests incomplete manuscript preparation. There are multiple grammatical problems throughout, including sentence fragments and duplicated ideas, for example “Averaging results mitigates prompt sensitivity. Averaging across five prompts mitigates...” in **Section 3.1**.  
   Why this matters: beyond cosmetics, these issues make it hard to determine exactly what was run and reported. For an empirical benchmark paper, precision of reporting is essential.

9. **The literature positioning is incomplete for a paper whose main contribution is empirical evaluation rather than a new algorithm.**  
   The related work mentions several medical LLM/VLM papers, but the paper does not adequately position itself relative to prior work on clinical summarization evaluation and factuality/safety assessment. In particular, a paper centered on hallucination and safety collapse should engage more directly with recent work on medical summarization safety/factual consistency and with comparisons between general-purpose LLMs and smaller domain-specialized models.  
   Why this matters: when novelty comes mainly from a benchmark-style empirical analysis, strong literature positioning becomes more important, not less. Otherwise it is difficult to assess what is genuinely new versus a recombination of already known observations.

10. **The clinical-safety framing is stronger than the evidence warrants.**  
   The abstract and conclusion talk about “safe context-grounded summarization,” “minimum viable scale for safe deployment,” and “trustworthy clinical AI.” But the evaluation is entirely automatic except for a limited qualitative example, uses only 250 test samples per task, and does not include clinician evaluation, calibration analysis, error severity stratification, or downstream risk assessment. Even the hallucination-related analysis lacks a clearly described annotation protocol in the main paper.  
   Why this matters: safety claims in healthcare require a higher bar. The current results may support a preliminary efficiency comparison, but not a deployment-oriented safety threshold.

## Questions
1. Please provide a precise definition for every metric in **Table 3**, including the exact scoring formula or annotation rubric for Task Adherence, Hallucination Rate, Concept Recall, Robustness, and especially the Readiness Score. Was hallucination measured manually or automatically, over how many samples, and with how many annotators?

2. Can you provide the full fine-tuned summarization results in a table, with exact values and preferably confidence intervals or standard deviations across runs/prompts? Right now the strongest claims rely on **Figure 2** and **Figure 3**, which are not sufficient for careful comparison.

3. What exactly was held constant in the “small vs large” comparisons? Were the large VLM baselines in **Table 4** fine-tuned on the same 10k MIMIC-CXR subset, or evaluated as off-the-shelf checkpoints? Likewise for summarization, were the larger medical LMs also adapted on MeQSum under the same protocol, or only evaluated as released checkpoints?

4. Please clarify decoding. Were top-\(k=3\), top-\(p=0.9\), and \(T=0.3\) applied simultaneously, or were these separate decoding conditions? If separate, how were results aggregated? If simultaneous, why this combination, and how sensitive are hallucination claims to decoding choice?

5. The paper repeatedly attributes the findings to model size, but the comparisons are across different families and training histories. Do the authors have any same-family scaling evidence, for example within Gemma or SmolLM only, evaluated under identical adaptation settings, that would more directly support a true scaling-threshold claim?

6. For **Table 4**, how do you explain the fact that Qwen2.5-VL has the highest BERTScore among the VLMs while the text states that small VLMs remain below large baselines in all metrics? This inconsistency should be reconciled.

7. For the qualitative safety story around **Figure 4** and **Figure 5**, can the authors provide a broader error analysis, ideally with counts by error type, instead of isolated examples? A few compelling examples are useful, but they do not establish a threshold phenomenon by themselves.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper studies clinical summarization and radiology report generation, and repeatedly frames its contribution in terms of safety, trustworthiness, and minimum viable scale for deployment. That framing raises safety concerns because the empirical evidence is not yet strong enough to support deployment-facing conclusions. The main issues are in **Abstract**, **Section 3.1**, **Section 4**, and **Section 5**, where the paper suggests a “safe” threshold and “trustworthy clinical AI” without clinician evaluation or clearly defined hallucination assessment in the main paper.

On the data side, the use of MIMIC-CXR under a data use agreement is acknowledged in the ethics statement, which is good. However, for responsible research practice, the manuscript should be more explicit about train/validation/test partitioning and any safeguards against reporting overconfident deployment implications from limited automatic evaluation.

## Soundness Rating
2: fair. The paper asks an important question and contains some empirical evidence, but the main claims are undermined by under-specified evaluation methodology, confounded comparisons, missing quantitative reporting for key fine-tuning results, and inconsistent interpretation of the presented tables.

## Presentation Rating
2: fair. The core intent is understandable, but the manuscript has many clarity, editing, and formatting issues, including inconsistent naming, missing table references, malformed tags, and figures that are harder to interpret than they should be.

## Contribution Rating
2: fair. The practical question is relevant and some observations are interesting, especially around compact-model failure modes, but the paper does not yet provide a sufficiently rigorous or clearly positioned empirical contribution for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The topic is relevant and the paper has the seed of a useful empirical study, especially the attempt to examine failure modes beyond ROUGE-like metrics. However, the current submission overclaims relative to what is actually established. The “minimum viable scale” and “safety collapse” story is not convincingly supported because the core analysis is under-defined, the comparisons confound size with architecture and training history, and the strongest post-fine-tuning claims are not backed by a proper quantitative table. With tighter experimental control, clearer definitions, and much better reporting, this could become a worthwhile paper, but in its current form I do not think it meets ICLR standards.

## Reviewer Confidence
4: confident. I am confident in this assessment. The paper is in an area I know well, and I carefully checked the main tables, figures, and the presented training objective, though some missing details in the paper necessarily limit the depth of verification.