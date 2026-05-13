# MALLM-GAN: Multi-Agent Large Language Model as Generative Adversarial Network for Synthesizing Tabular Data

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
\subfile{sections/abstract}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a novel model that generates synthetic tabular data via a proposed multi-agent LLMs framework. The proposed method aims to handle the issues of limited training data size in healthcare. The proposed framework ICL and does not require fine-tuning on LLM and the ICL examples are obtained by a "multi-agent LLM AS GAN" model.

### Strengths
Prons:

1. The experimental setting seems solid as they conduct the experiments on 5 different datasets.

2. The idea of combining LLM and GAN makes sense.

3. The proposed method is well-generalized, simple, and can be applied to many tasks.

### Weaknesses
Cons:

1. From the experimental results shown in Tables 2 & 3, the proposed model cannot always obtain the SOTA performance (In table 2 & 3).

2. The main idea is to combine LLM (with ICL ) and GAN and the idea is somehow straightforward. To highlight the technical contribution of this paper, the authors should make it clear the technical difficulty of combining ICL-LLM and GAN and clarify the technical contribution (novelty) of this proposed method.

3. This paper aims to handle the training on small datasets. To achieve the model training on small dataset, the authors selected sets of samples from the whole (large) datasets to compose small datasets (N=100, 200, ..., 800). However, the dataset spliting is conducted by the authors instead of using some standard benchmarks. Is it possible to directly use benchmarks with small datasets? It means the authors need not split the dataset by itself and use the small dataset being used in other papers. By doing so, the comparsion will be more fair and solid.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a method for tabular data synthesis using LLM in-context learning. Specifically, it emulates the architecture
of a Generative Adversarial Network (GAN), where one LLM serves as the generator, one neural network serves as the discriminator, and another LLM serves as the optimizer.  The optimization is conducted on the DAG and instruction part of the generation prompt. Experiments show the proposed method achieves promising results on MLE and DCR metrics.

### Strengths
1. This paper is in general well-written and easy to read.
2. This paper reveals a problem with the previous deep generative model, which requires a lot of training data. While LLM in-context learning has the potential to address this problem.

### Weaknesses
1. The central part of the optimization phase is to optimize the DAG (Eq 1). The validity of this process relies on the assumption that DAG should play a crucial role in the quality of the generation (otherwise we would not need to optimize it if it does not matter for the generation quality). However, In Lines 398-400, the authors also observe that incorporating the causal structure alone did not significantly improve the MLE compared to a model with only in-context few-shot learning, which challenges the foundation of its method.

2. This paper proposes to prompt another LLM to optimize the parameter $\theta$, based on the history of the previous <score, generation prompt> pair.  I doubt if an LLM is capable of solving this optimization problem, based on two reasons: 1.  the LLM does not have access to the function form of the score.  2. the optimization is extremely hard due to the limited number of previous pairs and the high dimensionality of the parameter $\theta$ (the DAG and task instruction). 

3. Continue with Point 2, to see if LLM is able to solve the challenging optimization problem in a meaningful way, more trajectory results need to be shown, similar to Table 4. It is crucial to answer: does each optimization step consistently improve the score? How many steps do we need to converge? What does the trajectory look like for different datasets?

4. **Lack of important baseline**: CLLM [1] is considered out of scope due to its post-hoc data selection. Thus this paper does not compare to CLLM in the experiment.  However, this comparison is crucial since CLLM also only relies on the in-context learning of LLM.  At least a comparison should be done with CLLM without the data selection procedure.

5. **Limited evaluation metric**: This paper only uses two metrics to access the quality of the synthetic data: MLE and DCR, which are too limited. It is strange that the evaluation does not even contain the classification metric the Discriminator used (see Sec 3.2.2). It also lacks many other important metrics used in TabDDPM [2],  column density shape, pair-wise column correlation, and Jensen–Shannon divergence.  This lack of evaluation metrics significantly undermines the convincingness of the proposed method.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel GAN-inspired framework that leverages large language models (LLMs) as the generator and a classifier as the discriminator. Instead of optimizing at the model's weight level, the optimization occurs at the text prompt level, guiding the generation of synthetic data. The prompt used in data generation incorporates a natural language description that outlines the data collection context, the schema, relationships between columns (causal structure), and task instructions. Throughout training, the context and schema remain fixed, while the causal relationships and task instructions are refined to minimize the discriminator's accuracy.

The generation process begins with a few-shot setup to illustrate data structure and is followed by training the discriminator on both original and synthetic data. The discriminator is then evaluated on a held-out test set, and its performance score is provided to GPT-4 for further prompt optimization in the generator. This iterative feedback loop continues, where a series of top-performing discriminator scores are used by GPT-4 to refine the generator prompt, thereby enhancing synthetic data quality.

### Strengths
1. The experimental set up is quite innovative where a signal is sent to the generator regarding its generation quality via the llm optimizer which refines the prompt. This could potentially save a lot of compute as it makes quality generation possible without finetuning.
2. Using LLM’s to rewrite prompts based on signals in the form of scores is good.
3. Conditional generation through natural language appended to the prompt makes generation of simulations possible.

### Weaknesses
1. The claim made is that few-shot learning is not scalable due to the limited context length of the models in a data-scarce scenario and thus all the examples cannot be utilized by the model for generating new data. However models like Gemini are now available with context windows in the range of millions of tokens.
2. Hard to say whether the learning process has actually converged as the optimizations are happening at the prompt level. (Authors mention this in the paper as well).
3. The maximum number of columns for the datasets considered is 37. This might be due to the limitation of model context windows at that time. So this method hasn’t been tested on a large dataset like say 100 columns. 
4. The experimental set up is quite novel but optimizing the prompts is not a novel contribution as there have been papers and even frameworks like DSPY who are doing this.
5. Only one model is used for the experiments (GPT 3.5). It will be interesting to see if this method generalizes and scales to other models like Claude, Gemini or open models like llama-3.

### Questions
Please address the concerns in weakness

### Soundness
2

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
4

### Summary
The paper proposes a method for generating synthetic tabular data explicitly by leveraging the in-context learning of LLMs to mimic the adversarial process of GAN. This is achieved by prompting the LLM to build the generator, and then using a disriminator to identify the real data from synthetic data. The prompt of the generator is optimized by an LLM.

### Strengths
- Both the generation and optimization process are explicit, offering better explainability.
    
- The proposed pipeline enables automatic optimization and generation of synthetic data, which addresses the data scarcity problem of downstream tasks.

### Weaknesses
 - The initial prompt for the generator and optimizer still requires empirical knowledge about the task and labor efforts, which makes application to eifferent tasks difficult.
- Although comparisons were made with multiple methods in the experiments, there is a lack of comparison with methods that use the same LLM (GPT-3.5) as data generator.

### Questions
The author(s) propose to intergrating the descriminator and optimization steps into the synthetic data curation process. My main concern is how this approach will improve the quality of synthetic data compared to  common LLM-based methods.
The author(s) should compare with other method using GPT-3.5 as the base model. For instance, the author(s) might consider comparisons against baselines such as human-written instructions, instructions generated directly by GPT-4, or examples randomly selected from the dataset as few-shot examples for synthetic data generation. These are essential for demonstrating the effectiveness of MALLM-GAN.
I would raise my score if the authors could provide more solid and fair comparative results to demonstrate the effectiveness of MALLM-GAN.

### Soundness
3

### Presentation
3

### Contribution
3
