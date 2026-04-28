# Aligner: One Global Token is Worth Millions of Parameters When Aligning LLMs

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
We introduce Aligner, a novel Parameter-Efficient Fine-Tuning (PEFT) method for aligning multi-billion-sized Large Language Models (LLMs). Aligner employs a unique design that constructs a globally shared set of tunable tokens that will change the attention of every layer. Remarkably with this method, even when using one token accounting for a mere 5,000 parameters, Aligner can still perform comparably well to state-of-the-art methods like LoRA that require millions of parameters. This capacity is substantiated in both instruction following and value alignment tasks. Besides the multiple order-of-magnitude improvement in parameter efficiency, the insight Aligner provides into the internal mechanisms of LLMs is also valuable. The architectural features and efficacy of our method demonstrate that an LLM separates its handling of "form" and "knowledge" internally in some orthogonal manner. This finding should give impetus to new research into LLM mechanism understanding and value alignment.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a variant of prefix-token based task alignment method for large language model. Basic idea of the prior LLaMA-adapter is to employ a special short prefix token sequence which are summarized via self-attention, then, linearly combined with the input self-attention part. This work further extend the idea by sharing tokens in each layer, but employing layer specific attention parameters. Experiments on Vicuna benchmark shows comparable performance against LLaMA adapter and LoRA with significantly lower number of parameters for adaptation.

### Strengths
- A simple extension to LLaMA-adapter with significantly lower number of parameters, but rivaling the performance with other adapting method.

### Weaknesses
- There exist no analysis on the learned parameters especially for tokens. It would be better to quantify the gains by investigating what was learned in the small number of parameters. Also, this work should investigate what is learned by the weight parameters $\beta$.

### Questions
See the weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents a new parameter-efficient fine-tuning method, which is best described as a reduced version of LLaMA-Adapter, with tuned key+value hidden states, shared across layers with layer-specific gates.

### Strengths
- The method is clearly described and simply motivated.

### Weaknesses
- The key weakness of this work is that all model evaluation is performed using only model-based evaluation (and specifically model-based comparisons), and not on any labeled benchmark tasks. For a work that is primarily a model-adaptation method, and one that is far lower capacity than full fine-tuning. Moreover, model-based evaluation has been shown to have several limitation in the literature, and I do not believe the field is yet ready to accept results based only on model-based evaluation. For this reason, despite its technical contributions, and I do not think this work can be accepted in its current state.
- Several grammatical/language errors and inconsistencies e.g. "Llama-Adapter" vs "LLaMA-Adapter"
- Strictly speaking, LLaMA-Adapter (and likewise Aligner) do not prepend prefix tokens. They employ a side-channel of attention over a separate set of tokens. The softmax is compute separately from the actual input tokens (see: Eqn 8), and position encodings are not applied to the LLaMA-Adapter/Aligner keys.
- The experiment demonstrating the efficacy of single-head Aligner is a simply a handful of examples of generated outputs. This does not meet the bar of rigorous evaluation for a conference paper.

### Questions
- How does this method perform on standard benchmark tasks?
- How do we determine the effective capacity of this method (e.g. on what tasks or in what settings does it underperform/not underperform full-finetuning, or higher-capacity parameter-efficient fine-tuning methods?)

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a simple modification of the LLama Adapter V1 in order to achieve more parameter-efficient fine-tuning. The novelty is to have one global set of tokens (or in the extreme: only one token) that all layers attend to, rather than per-layer tokens. Attention weights for each layer are separate. The result is a very small set of parameters to fine-tune. 
This method (based on Llama2 7B and 13B) is compared against LLama Adapter and LoRA on the Vicuna benchmark for instruction following and the PKU-Beaver dataset for DPO alignment with human values. The results show that the success of the method varies between model sizes and with different numbers of training epochs, but overall scores win ratios of around 0.4-0.5 on Vicuna, and performs better or on par for most categories of the PKU-Beaver set. 

While the results seem promising, they lack deeper analysis and a more concise interpretation (see below). Given the small novelty of the technical solution, the paper should have allocated more space for an investigation of the implications of this small change.

### Strengths
- The proposed method is attractive for its simplicity and efficiency. It is a simple modification of existing technique, but according to the results effective in reducing parameters significantly while maintaining quality.
- The evaluation is conducted on two benchmarks which represent two important uses of adapters, so it is relatively expressive.

### Weaknesses
- In three places it is argued that intuitive inspection confirms the success of the proposed method, by showing one example (Sections 5.1, 5.2, 5.3). The argument is weak, as it’s not a systematic inspection and could have been a cherry-picked example, and is left for subjective evaluation by the reader without any elaboration of why the quality is sufficient. In Section 5.3 this is particularly irritating since quantitative results for the one-token approach are missing, and the reader is left to trust that this example is representative. In 5.1 the example is used to dismiss the quality of the Vicuna evaluations (“too much variance”), which could have easily been tested and quantitatively verified by running the evaluation multiple times and reporting mean and variance.
- The interpretation of the win ratio for Aligner 1 (1 token) in Table 1 is given as “comparable” with the baselines, but it is actually <0.5, so technically worse than the baselines. This interpretation seems rather too optimistic, it is missing an analysis and a focus on the loss cases, because in practice no one wants to deploy a technique that worsens previous results, perhaps even if there’s an win in parameter efficiency. The trade-off between quality and number of parameters for the new and the standard adapter would have been helpful to compare directly in a plot.
- Large portions of the paper are dedicated to reviewing the background, the basics of Llama Adapter and RLHF. Considering that the proposed method is a minor modification, more space should have been rather invested for more exhaustive ablations and deeper analysis of why the method works, how it differs qualitatively from Llama Adapter, and how the hypothesis of separation of form and knowledge can be empirically verified.

### Questions
- Why does the 7B model perform better than the 13B model in Table 1? Any hypotheses?
- Is the code open-sourced or published with the paper?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
