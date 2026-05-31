## Human Reviewer 1

### Summary
The paper compares a set of small language models (SLMs,  less than 3B parameters) and small VLMs against medically adapted larger LLM/VLM counterparts on two clinical tasks: consumer health question summarization (MeQSum) and radiology report generation (MIMIC-CXR). The authors evaluate zero-/few-shot prompting and parameter-efficient fine-tuning, report automatic metrics (BLEU, ROUGE-L, BERTScore, MEDCON), and claim that fine-tuned small LMs can match or outperform larger medical models on summarization, while small VLMs still lag on radiology generation.

### Strengths
- Explore an important task which require the use of locally-deployed LLMs. The finding that small models perform on par with larger ones has good implication for the medical domain.

### Weaknesses
W1: There're some concerns regarding experiment setup:

- Models choice: The authors claimed that they selected small LMs and their larger counterparts but from Table 1, they seems to be from completely different models families (e.g. Gemma 3 paired with Med-Llama). Generally, I would consider 1B-8B to be in similar scale, as one would be able to run a 8B model on consumer GPU too. Also, why compare small general models with large medically-adapted models? Would a fairer comparison would be between both general or both medically-adapted? 

- Metrics: In medical summarization, it has been shown that automated metrics do not correlate with human preference. The authors also discussed this in the related work, but the experiment setup does not involve any human evaluation. The paper contains only a single illustrative example and qualitative claim about hallucination in SmolLM2. No crowd/clinician study exists.

- Finetuning details: missing

W2: The finding that fine-tuned small models can perform on par with larger one (zero/few-shot) is not new and was shown in previous work (the authors also discussed this in their related work). The experiments also does not aim to further explain this phenomenon and does not provide any interesting insights.

### Questions
Q1: The writing is not clear and have some clear formatting issues:
- 84-87: duplicated sentences
- Table caption should be at the bottom rather be on top.
- 317: Table ??
- "But notably, when doctors judge summaries, higher parameters don’t always win. The reader evaluation of the hospital course study found that doctors preferred GPT-4 summaries over Llama-13B in a majority of cases, despite similar metric scores (Aali et al., 2025)." => These sentences seem contradicting.

Q2: A small human evaluation (100 samples) is crucial and would facilitate more insightful analysis.

Q3: Additional ablation/control experiments: e.g. select model families with varying size, apply LORA to larger model to see the effect of finetuning varies with size, varying finetuning dataset size.

### Soundness
1

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper asks a focused question: can compact, open-source small models (≤3B) match or even surpass medically adapted large models on two representative clinical generation tasks, consumer health question summarization (MeQSum) and chest X-ray report generation (MIMIC-CXR), under both in-context prompting and parameter-efficient fine-tuning (LoRA/QLoRA)? The authors claim three contributions: a head-to-head benchmark of SLMs/SVLMs vs medical LLMs/VLMs; a multi-facet evaluation spanning syntactic, semantic, and medical-concept fidelity; and evidence that PEFT enables several SLMs to reach or exceed large LMs on summarization, with SVLMs still trailing large medical VLMs for report generation.

### Strengths
Pros:
1.	Problem relevance and clear task boundary.
2.	Some reproducibility considerations. Unified decoding settings and explicit dataset access constraints are noted, which aids replication.
3.	The paper is well written.

### Weaknesses
Cons:
1.	Statistical rigor and human evaluation. Results hinge on point estimates over n=250 without confidence intervals or significance testing; no clinician blind review is reported.
2.	External validity. The study uses a single text dataset (MeQSum) and a single imaging domain (CXR). Would be better if there are different benchmarks involved.
3.	Some narrative statements suggest SLMs outperform across all metrics after PEFT, yet detailed tables/figures and notes on instability. More granular win-loss accounting by metric/model would avoid over-generalization.

### Questions
see above

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

---

## Human Reviewer 3

### Summary
The authors benchmarked a lot of small LLMs adapted to the medical domain and claims that small LLMs after finetuning can perform reasonably well -- even outperforming not finetuned LLMs (surprising?)
I had very high hopes for this paper when I first saw the title, but I am really disappointed with the actual execution and outcome. So much lost potential and this honestly feels very low-effort. There are so many research questions that could be answered but so little was actually done.

### Strengths
writing is clear

### Weaknesses
I'll go down the weaknesses in my order of importance

I think the biggest and most immediate thing the authors should do is ask themselves why. What is the research question you want to answer? You should start from there and derive what experiments should be conducted to answer the question and support your claims. If you don't know where to start, you can at least conduct some form of error analysis to help guide your research before jumping into wasting a bunch of computes.

You finetuned small LMs with LoRA and showed it performed better than not-finetuned large LMs (who are not even that large in today standards.) Are we supposed to be surprised by this result-- if we are supposed to be surprised, how do you justify? And for a fair comparison, at the very least you should compare with finetuning small LMs with full-finetuning, and LLMs with LoRA finetuning. Even then, why are you running this experiment in the first place? Small LMs are unsurprisingly not good at generalization compared to LLMs, so it is expected to not perform well zero-shot. 

Your evaluation only includes automatic metrics, most of which are known to not correlate very well with human judgement. Have you at least tried some sort of human evaluation? Even then, the reported results on the automatic metrics for before and after finetuning are still very low -- have you looked at the generated output and analyze them?

Also, finetuning, at the very least you should report hyperparameters you used for the finetuning to support your claim

### Questions
There are so many analysis that could've been done, but because there's really not much done, I don't have much to go into detail for. I'll just name some recipe that the authors can try
1. the very standard -- run a reasonably good model, get some output, analyze why it's failing, and try to address it
2. what I was hoping to see when I saw the title -- as you go down in size, what are some qualities you are trading-off for? what's the minimum size you can get away with that would still have the same desired qualities

### Soundness
1

### Presentation
2

### Contribution
1

### Rating
0

### Confidence
5

---

## Human Reviewer 4

### Summary
This paper finds that nearly all small models match or exceed the summarization and generation effectiveness of larger, medically adapted models, with several fine-tuned SLMs outperforming their LLM counterparts.

### Strengths
1. For clarity, the paper is understandable and easy to follow.

2. For originality and significance, I see that the authors analyze new models such as Gemma-3, which may be helpful for future research.

### Weaknesses
1. The findings in this paper is very much expected and have been extensively explored in other papers, so my overall excitement is a bit low. This affects the overall originality and significance. For example, in [1], researchers have already found that models with much smaller sizes outperform LLMs. You may find much more relevant papers out there.

2. I am not sure what "common assumptions" are in line 22. Are there any dimensions (e.g., hallucination) where large models still outperform smaller ones? Or you think that small models can outperform LLMs across all dimensions related to clinical summarization? I think it is important to study this issue comprehensively.

3. The first two paragraphs of the introduction appear to be verbose and can be significantly shortened to discuss the most important point.

[1] "Better Late Than Never: Model-Agnostic Hallucination Post-Processing Framework Towards Clinical Text Summarization"

### Questions
1. I am not sure what "common assumptions" are in line 22.

### Soundness
2

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
4