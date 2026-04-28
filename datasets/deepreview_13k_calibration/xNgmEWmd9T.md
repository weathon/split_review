# Accumulator-Aware Post-Training Quantization for Large Language Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Several recent studies have investigated low-precision accumulation, reporting improvements in throughput, power, and area across various platforms. However, the accompanying proposals have only considered the quantization-aware training (QAT) paradigm, in which models are fine-tuned or trained from scratch with quantization in the loop. As models continue to grow in size, QAT techniques become increasingly more expensive, which has motivated the recent surge in post-training quantization (PTQ) research. To the best of our knowledge, ours marks the first formal study of accumulator-aware quantization in the PTQ setting. To bridge this gap, we introduce AXE—a practical, low-overhead framework of accumulator-aware extensions designed to endow overflow avoidance guarantees to existing layer-wise PTQ algorithms. We theoretically motivate AXE and demonstrate its flexibility by implementing it on top of two state-of-the-art PTQ algorithms: GPFQ and OPTQ. We further generalize AXE to support multi-stage accumulation for the first time, opening the door for full datapath optimization and scaling to large language models (LLMs). We evaluate AXE across autoregressive language generation models and observe significant improvements in the tradeoff between accumulator bit width and model accuracy over baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work investigates post training quantization from an accumulator-aware perspective. They aim at using low-precision at accumulation while avoiding the overflow issue. The paper proposes the AXE, as a practical, low-overhead framework as extensions on top of two state-of-the-art PTQ algorithms: GPFQ and OPTQ. The work supports full datapath optimization and scales to large language models. They achieve improvements in the trade-off between accumulator bit width and model accuracy over baseline methods.

### Strengths
+ The accumulation-aware approach is well motivated from the hardware and implementation perspective, because when weights and activations are quantized into low-precision, the 32-bit accumulation consumes majority of power and area. And using low-precision on accumulation may increase the risk of numerical overflow which degrades model accuracy.

+ The paper adopts an effective approach to theoretically gurantee overflow avoidance by constraining ||q||1 in post training quantization process. To solve the problem, AXE translate into two accumulator-aware constraints.

+ The multi-stage accumulation extension of AXE is effective in improving throughput and scaling to large language models.

### Weaknesses
 - The adoption of the two PTQ algorithms GPFQ and OPTQ and the applicability of AXE to other PTQ need justification.

- Because the concept of accumulation aware quantization was proposed from the implementation perspective. It is more convincing to demonstrate the performance in terms of latency or throughput besides model accuracy.

### Questions
The paper designs AXE as extensions on top of existing PTQ algorithms: GPFQ and OPTQ, claiming them as state of the arts. While OPTQ is OK, but GPFQ is an earlier work. Please justify why those two quantization algorithms are picked and comment the applicability of AXE to other PTQ methods.

The accumulation aware approach was motivated from the implementation perspective, but results are only evaluated from the model accuracy performance. Yes, the AXE is effective in avoiding numerical overflow and preserve model performance. Is it possible to justify the accumulation aware approach in terms of latency or throughput in implementation? This can make the work more convincing.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper is the first study on post-training quantization while keeping the accumulator in the picture. A low-bit accumulator risks to overflow, but speeds up the arithmetic computation. They use L1 constraint on the inner product counterpart to guarantee numerical stability in equation (2) and build a quantization method that controls the accumulator based on this result. 
The L1 constraint is the same formulation as first introduced in compressed sensing by Donoho (1994) and later called the lasso of Tibshirani (1996) in the context of linear regression.

### Strengths
Thi sis the first formal study of quantization on the accumulator size. The paper is well-written and easy to follow with theoretical justifications. The innovative idea appears in equation (17) as a layer-wise operation. The authors adapt this result for two well-known post-training quantization methods GPFQ, and OPTQ.

### Weaknesses
Although this is the first study on accumulators, I doubt its usefulness.
Often, the accumulator size is hardware-dependent, and sometimes even unknown. There are ways to guess the accumulator size by running various experiments, but they are not revealed by the manufacturer. In the context of quantization only weights or weight-activation, the benefit is clear; I wonder how we can benefit from quantizing accumulators unless we design a new processor or a co-processor. This limits the impact of this study unless the authors provide a guideline on how to use the accumulator bit size in practice on certain processor.

### Questions
- CPU cores, cude cores, tensor cores support different number formats, each with different (unknown) accumulator size. How quantizing accumulator lead to advantages for pre-training, fine-tuning, or inference of LLM models?
- Using OPTQ and GFPQ as a baseline is interesting in terms of accuracy, but they lead to smaller models after their use. What AXE brings to the table practically?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles a specific challenge related to low-level hardware architecture, specifically targeting the accumulation process in a Post-Training Quantization (PTQ) setting. The accumulator design in current hardware architectures is prone to significant numerical deviations when numbers are heavily quantized. The paper examined two distinct cases: a singular accumulator and an accumulator within an adder tree's output. The analysis largely focuses on integer arithmetic. The paper's core objective is to enhance a subset of quantization algorithms, such as GPFQ, by proposing an L1-norm penalty for high-magnitude post-quantization weights, as these can introduce errors in subsequent accumulation stages.

### Strengths
The paper is well-written and easy to understand. The optimization it proposes concentrates on low-level hardware details that significantly differs from existing approaches in quantization research. Notably, the issue of accumulation round-off errors, which the paper addresses, is frequently overlooked by the Efficient AI community.

### Weaknesses
The paper is too focused on quatnization that is associated with the low-level hardware architecture, making me feel ICLR may not be a very suitable venue for work like this.

The paper's presentation raises concerns regarding its background setup and evaluation.

First, it fails to acknowledge a range of prior studies in this field, including LLM.int8, ZeroQuant, AWQ, and others. Moreover, the paper lacks comparative analysis with weight-activation quantization methods, making it difficult to gauge the effectiveness of the proposed technique relative to existing quantization research. Most current works aim to quantize weight values to alleviate pressure on HBM bandwidth. Typically, they dequantize model parameters and perform multiply-accumulate operations in higher precision (e.g., fp16). Without a clear comparative study on end-to-end GPU performance, it is challenging to understand the benefits of the suggested method, especially in memory-bound LLM inference, and how much advantage is gained from enabling accurate low-precision arithmetic operations.

Second, the proposed method is mainly evaluated on a single modern LLM family (Pythia). The model under the choice here (Pythia) is not a popular one, and this again, makes comparing to other methods very challenging. An obvious good candidate for an evaluation like this would be the LLaMA family models. The paper also extends the evaluation to the OPT and GPT2 models. However, both models are fairly small in size (< 1B) and also are fairly old.

### Questions
Based on the two points I raised in Weakness, can you please

1. Add actual performance metrics (eg.  throughput) in Table 1 and a direct comparison to more related method that are actually integrated in LLM serving engines (vLLM)
2. Extend the accuracy comparison to more LLM model famil

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces AXE, a framework for overflow-avoidant, accumulator-aware quantization in the PTQ setting, aimed at efficient low-precision deployment of large models. AXE extends existing PTQ methods like GPFQ and OPTQ by managing accumulator bit width to improve resource efficiency without requiring retraining, and supports multi-stage accumulation for scaling to large models. The authors report gains in task performances over PTQ baselines with reduced accumulator bit width.

### Strengths
1. The AXE method is theoretically grounded.

2. AXE fills a gap in PTQ by addressing overflow risks in low-precision settings, potentially benefiting deployment on resource-constrained hardware.

3 The paper introduces a novel overflow handling approach in PTQ, potentially expanding PTQ’s applicability to larger models.

### Weaknesses
1. I didn't find any evidence of actual efficiency gain in the experiments apart from the bit width reduction and perplexity improvements.

2. Currently the paper evaluates on perplexity and zero-shot reasoning tasks, this IMO is not enough, more NLP tasks need to be tested to consolidate the efficiency of the AXE method.

3. Novelty: While AXE extends existing PTQ methods with accumulator-aware quantization, much of its methodology relies on previously established concepts. The theoretical contributions build on recent QAT-based methods, and the extension to PTQ, while practical, does not introduce a fundamentally new approach to quantization beyond overflow handling.

4. Writing could be improved, in particular the topic introduction and storytelling. I had a hard time following the paper.

### Questions
What does Table 4 try to deliever here? There is no description in the main context of the paper.

### Soundness
3

### Presentation
2

### Contribution
2
