# Evaluating the Quality of Hallucination Benchmarks for Large Vision-Language Models

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Despite the rapid progress and outstanding performance of Large Vision-Language Models (LVLMs) in recent years, LVLMs have been plagued by the issue of hallucination, i.e., LVLMs tend to generate responses that are inconsistent with the corresponding visual inputs. To evaluate the degree of hallucination in LVLMs, previous works have proposed a series of benchmarks featuring different types of tasks and evaluation metrics. However, we find that the quality of the existing hallucination benchmarks varies, with some suffering from problems, e.g., inconsistent evaluation results under repeated tests, and misalignment with human evaluation. To this end, we propose a \textbf{H}allucination benchmark \textbf{Q}uality \textbf{M}easurement framework (\textbf{HQM}), which leverages various indicators to assess the reliability and validity of existing hallucination benchmarks separately. Specifically, for reliability we explore test-retest reliability and parallel-forms reliability, while for validity we examine criterion validity and coverage of hallucination types. Furthermore, we construct a \textbf{H}igh-\textbf{Q}uality \textbf{H}allucination Benchmark (\textbf{HQH}) for LVLMs, which demonstrates superior reliability and validity under our HQM framework. We conduct an extensive evaluation of over 10 representative LVLMs, including GPT-4o and Gemini-1.5-Pro, to provide an in-depth analysis of the hallucination issues in existing models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper rethinks the reliability and validity of existing hallucination evaluation benchmarks, and therefore proposes test-retest and parallel testing methods for quantitative evaluation. Besides, this paper also curates a High-Quality Hallucination Benchmark (HQH) for comprehensively evaluating existing LVLMs hallucination degree.

### Strengths
Strengthens
1.	This paper investigates the instability of the evaluation metric of existing hallucination benchmarks, and contribute a new high-quality benchmark for the community.
2.	The writing quality is good and easy to follow.

### Weaknesses
1. The overall technical contribution is limited. The primary contributions of this paper include that existing evaluation metrics of hallucination benchmarks are instable under multi-fold validation, and curates a high-quality hallucination benchmark with “hallucination rate” as the evaluation metric.
2. The motivation and method are inconsistent. The major motivation of this paper lies in that the evaluation metrics of existing hallucination benchmarks are insufficient. But the proposed solution is to curating a new high-quality benchmark and calculate “hallucination rate” by altering the GPT-scores and GPT-based binary choices. The proposed multi-fold validation criterions are not employed for HQH evaluation.
3. The details of proposed designs are unclear. First, is it reasonable to use the validation set of Visual Genome dataset? It can incurs data leakage problem as existing LVLMs are using validation sets of open-source datasets for their training. Under this circumstance, test set is more suitable for establishing a benchmark. Second, what are the key differences between asking a LLM to directly give a score and judging whether the answer includes hallucination? I cannot figure out their intrinsic differences here.

### Questions
1. I'm wondering whether it is reasonable to use the validation set of Visual Genome dataset. It can incurs data leakage problem as existing LVLMs are using validation sets of open-source datasets for their training.
2. What are the key differences between asking a LLM to directly give a score and judging whether the answer includes hallucination? I cannot figure out their intrinsic differences here.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes to look at multi-modal hallucination benchmarking from a novel perspective, i.e. the property of existing benchmarks. Further, on top of these properties, the paper presents a newly curated hallucination benchmark, providing more reliable and trustworthy evaluation of LVLMs.

### Strengths
- The work systematically studies the reliability and robustness for existing LVLM benchmarks. It provides quantitative evidences, characterizing various benchmarks' weakness in reliability (yes-and-no) and validity (free-form).
- The curated HQHBench effectively leverage existing annotations from Visual Genome, and have demonstrated that such a benchmark provides both reliable and valid signal for LVLM evaluation.

I also appreciate that the authors also managed to provide an anonymous data hosting the actual benchmark, which greatly increase the credibility of this work and the speed of the community to benefit from it.

### Weaknesses
One challenge I have is that some efforts of (in-)validating existing benchmarks are already creating new benchmarks that come with certain properties:
- we can combine POPE and "POPE-rewrite" as a benchmark that is robust against this parallel-form check, because it has been saturated with parallel forms.
- By utilizing the latest models, like GPT4o/o1, Claude 3.5 etc, validity may improve as well.

Essentially, the effort of curating a new benchmark is orthogonal to improving existing benchmarks. Even more I'd say they are additive to some extend, as this is a more efficient way to merge community efforts for a more comprehensive benchmark. I'd like to see authors' discussion on this point.

Another issue is that the HQHBench is curated with the bless of Visual Genome annotation, therefore hallucination judgement can be done in a binary format against image information provided in the annotation. However, there are still image information not covered by the annotation. Such a missing-annotation scenario may cause a rich response capturing not-in-annotation fact be judged as hallucination. How can we address such scenarios?

### Questions
- The test-retest protocol is a bit unclear. When we re-run the benchmark, do we require the model being evaluated to re-generate the responses? If not, why is there difference for Yes-or-No benchmarks? If yes, how do we distinguish whether the randomness comes from the benchmarking judge, or the models being evaluated?
- Visual Genome dataset's annotation is known to be noisy. How does this benchmark mitigate this issue?
- Can you provide an example of what POPE has been re-written into? Since POPE itself contains random/adversarial settings that prevents a degraded all-Yes model to pass, it already introduces parallel forms.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors first evaluate the quality of current hallucination benchmarks, then propose a new benchmark HQHBench

### Strengths
Please refer to Questions

### Weaknesses
1. My main concern is the limited novelty. As the authors introduced in Sec.3, introducing psychometrics into AI is not a new idea, and the proposed metrics (Test-retest Reliability, Parallel-forms Reliability, Criterion Validity) are also proposed by previous works. So the evaluation part seems to evaluate the current benchmarks with an off-the-shelf idea, with limited novelty. 

2. Following 1, the evaluation is a general idea that is unrelated to the Hallucination problem. We could apply it to other multi-modal benchmarks and have some similar conclusions. So I think it hardly provides some insight about the following study about hallucination.

3. Similarly, the proposed HQHBench also seems like a common MLLM capability evaluation benchmark (for example, a free-form version of MMBench or SeedBench), rather than a hallucination evaluation benchmark. **If we treat all the wrong answers as hallucinations, we should not view hallucination as an independent research topic.**

4. Last, I have a concern about the evaluation quality of HQHBench, the GPT-3.5 seems not capable enough to understand the complex image with only a short caption and phrases with bbox. 

5. Besides, the MLLMs evaluated in the paper are quite out-of-date. There are many capable new models, such as LLaVA-Next/OneVision, Qwen2-VL, InternVL2, NVLM, etc.

### Questions
### Strength
1. The paper is well-written and easy to follow
2. The proposed evaluation method is proper.
3. The proposed benchmark seems to work well on the evaluation.

### Weakness
1. My main concern is the limited novelty. As the authors introduced in Sec.3, introducing psychometrics into AI is not a new idea, and the proposed metrics (Test-retest Reliability, Parallel-forms Reliability, Criterion Validity) are also proposed by previous works. So the evaluation part seems to evaluate the current benchmarks with an off-the-shelf idea, with limited novelty. 

2. Following 1, the evaluation is a general idea that is unrelated to the Hallucination problem. We could apply it to other multi-modal benchmarks and have some similar conclusions. So I think it hardly provides some insight about the following study about hallucination.

3. Similarly, the proposed HQHBench also seems like a common MLLM capability evaluation benchmark (for example, a free-form version of MMBench or SeedBench), rather than a hallucination evaluation benchmark. **If we treat all the wrong answers as hallucinations, we should not view hallucination as an independent research topic.**

4. Last, I have a concern about the evaluation quality of HQHBench, the GPT-3.5 seems not capable enough to understand the complex image with only a short caption and phrases with bbox. 

5. Besides, the MLLMs evaluated in the paper are quite out-of-date. There are many capable new models, such as LLaVA-Next/OneVision, Qwen2-VL, InternVL2, NVLM, etc.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors first conduct a comparison between hallucination benchmarks on test-retest reliability, parallel-forms reliability, and criterion validity. Based on their findings, the authors construct the High-quality Hallucination Benchmark (HQH), which demonstrates reliability and validity.

### Strengths
- The authors innovatively start with a benchmark on hallucination benchmarks.
- The experimental results are extensive.
- The code is provided. I appreciate the authors doing that.

### Weaknesses
 - About test-retest reliability:
  - The overall idea is the testify to the consistency of evaluation results over different random seeds, which, however, involves two factors, including the randomness of the models and the metrics. It is unreasonable to attribute it directly to the metrics.
- About parallel-form reliability:
  - During the construction of HQH, to improve validity, the authors use free-form VQA, and to improve test-retest reliability, the authors prompt GPT to only conduct binary classification.
  - I wonder how HQH improves its parallel-form reliability, even compared with the free-form counterparts like MMHal and GAVIE.
- About the evaluation metric of HQH:
  - In Figure 4, we see that the authors provide a lot of textual information about the image for GPT. Do you still give the original image to GPT? If so, why did you choose to provide this textual information explicitly to GPT judgment?
- About insight for mitigation:
  - Indeed, this paper proposes a better hallucination benchmark. However, it seems that it mainly focuses on the benchmark construction, while cannot provide us more insight into how to relieve LVLM hallucination.
  - Based on the more human-aligned evaluation results in Table 5, can you give us observations or insights that we cannot derive from the less human-aligned benchmarks?

- Overall, I think it is an interesting paper. However, there are still unclarified details and analyses requiring revision.

### Questions
- About instruction collection:

  - Do you use and filter the original instructions of the VG dataset or create new ones?
  - During the filtering process of instructions, is the hallucination type the main concern or have you done anything to maintain reliability and validity?
  - I think a more detailed explanation of the instruction collection procedure of the HQH dataset is interesting.

### Soundness
3

### Presentation
3

### Contribution
3
