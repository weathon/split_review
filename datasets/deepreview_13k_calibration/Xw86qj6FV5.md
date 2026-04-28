# CaLMFlow: Volterra Flow Matching using Causal Language Models

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 8, 3

## Abstract
We introduce CaLMFlow (Causal Language Models for Flow Matching), a novel framework that casts flow matching as a Volterra integral equation (VIE), leveraging the power of large language models (LLMs) for continuous data generation. CaLMFlow enables the direct application of LLMs to learn complex flows by formulating flow matching as a sequence modeling task, bridging discrete language modeling and continuous generative modeling. Our method implements tokenization across space and time, thereby solving a VIE over these domains. This approach enables efficient handling of high-dimensional data and outperforms ODE solver-dependent methods like conditional flow matching (CFM). We demonstrate CaLMFlow's effectiveness on synthetic and real-world data, including single-cell perturbation response prediction, showcasing its ability to incorporate textual context and generalize to unseen conditions. Our results highlight LLM-driven flow matching as a promising paradigm in generative modeling, offering improved scalability, flexibility, and context-awareness.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors propose to use an autoregressive (language) model to imitate a (discretized) flow from the prior to the target distribution. This has a clear advantage, as such an autoregressive model with an unbounded context can take into account non-local structures across multiple timesteps, unlike previous approaches that model a purely local transition (a la “difference”). Once training is over (in the next-token prediction way), one can simply run the autoregressive model forward starting from a sample drawn from the prior distribution to draw a sample from the target distribution.

### Strengths
It is only natural to extend any of these iterative refinement based approaches to learning to sample from a complex distribution to make each refinement step less local and more global. Although it is natural, it has been challenging to do so until recently, as it was not clear whether we can build a powerful neural net that can take as input a long sequence of a trajectory and use it properly. With the recent advances in language models, this doubt is no more, and the authors in this paper demonstrate that indeed we can use such an autoregressive model to build a better sampler based on iterative refinement. Despite the unnecessarily convoluted way of presenting it via so-called Volterra flow, the idea is extremely straightforward, and the authors’ limited experiments do support that there is a benefit to be had from such non-local iterative refinement. It is furthermore interesting to see that they could easily extend it by prefixing their iterative refinement sampler with a natural language description to make it language conditional.

### Weaknesses
Unfortunately the current manuscript is extremely difficult to read. One reason i can point out is due to the lack of clear exposition on how this underlying autoregressive model looks like; what does it take as input, and how the prefix is processed to result in the prediction of the next step’s refined observation? Specifically, the manuscript does not clearly articulate the structure of the input sequence to the autoregressive model. Is it a flattened sequence of all time steps and spatial dimensions, or is there some hierarchical structure? How is the temporal information encoded? The authors mention using GPT-2 and Pythia architectures, but do not detail how these models are adapted to process the spatiotemporal data. The lack of clarity makes it difficult to understand the core mechanics of the proposed approach. Furthermore, the authors’ use of the term “tokenization” confused me quite a lot, as “tokenization” is often used to refer to as the process by which we quantize a continuous observation into a finite set of discrete tokens, while the authors here are referring to discretizing continuous time and space. This conflation of terminology makes it harder to grasp the actual data representation. Such issues with presentation make it pretty much impossible for me to recommend the manuscript in the current form to be accepted at the venue. I would suggest the authors make a major revision to present the proposed approach (which I think may have an interesting impact on the community) more clearly and thoroughly.

### Questions
This is more of a question to the other reviewers as much as it is to the authors. I am not too familiar with usual practices when these flow-based approaches are introduced and compared. Are these experiments standard ones that people have used to compare different iterative refinement based samplers? The first set of experiments on mixtures of Gaussians look extremely low-dimensional, and the second set of experiments on single cell sequencing data look relatively unconventional (I like this problem but it is difficult for me to understand that this is one of the standard problems people use to compare these samplers.) I may be completely wrong here (and if so, please do point out,) but I would like the authors to clarify what are more or less standard benchmarks in this area and how the proposed approach compares to the existing ones on those.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces CaLMFlow, a framework that leverages LLM for continuous data generation. The paper formulates flow matching as a sequence modeling task, and applies LLMs to learn the complex flows. By tokenizing the space and time, the approach enables efficient handling of high-dim data. On a range of tasks (e.g., single-cell perturbation response prediction), the method shows strong performance.

### Strengths
The technical idea is original and natural, blending LLMs into the framework of VIE flow matching. 

Extensive experiments were carried out on a range of tasks, covering synthetic and real-world data. 
The analysis and ablation studies also show the importance of each component/technique in the method, providing insights for future improvements. 

The paper is generally clear.

### Weaknesses
The method seems general but the only kind of real data in the experiments are single-cell data. Without further evidence, it is hard to judge whether the significance will be high or not, broad or not.

The writing has some typesetting issues. E.g., 
- line-213, $T$ tokens 
- line-219, $D_{text{in}}$

### Questions
What are the author's thoughts on generalizing the method to other kind of spatiotemporal data, e.g., high-dim time series, video data, etc?

### Soundness
3

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
This paper proposes CALMFLOW, an autoregressive modeling method for continuous data. It tokenizes continuous data into small time segments and uses numerical solutions of ODEs to model the data. Experiments are conducted on synthetic data and real cell-perturbation data to evaluate the approach.

### Strengths
The writing is clear and accessible.

The idea is easy to understand.

Experiments are conducted on both synthetic and real data, enhancing the validity of the results.

### Weaknesses
Trivial Task: The paper focuses on continuous data modeling, which may not present a sufficiently challenging or novel task. The modeling of Gaussian distributions and the MNIST dataset appears trivial, and many existing multimodal methods can already handle cell data modeling effectively.

Mismatched Motivation and Experiment: Although the paper initially highlights the difficulty of solving ODEs, the experiments focus only on continuous data modeling and do not fully support or address the stated challenges with ODEs.

Overclaim of Novelty: The claimed tokenization method seems indistinguishable from standard window-based segmentation techniques, which questions the novelty of the approach.

### Questions
Problem Definition: What is the task setup for the synthetic experiments? How many training and test data samples are used, and what does each training sample look like (e.g., is it a two-dimensional Gaussian distribution)?

Parameter Comparison: There is no parameter comparison between different methods, which makes the evaluation less fair for data-fitting tasks.

### Soundness
2

### Presentation
3

### Contribution
1
