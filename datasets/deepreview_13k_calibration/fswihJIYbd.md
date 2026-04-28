# ADePT: Adaptive Decomposed Prompt Tuning for Parameter-Efficient Fine-tuning

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Prompt tuning (\pt), where a small amount of trainable soft (continuous) prompt vectors is affixed to the model input, has shown promising results across various tasks and model architecture for parameter-efficient fine-tuning (\peft).
\pt stands out from other \peft approaches because it maintains competitive performance with fewer trainable parameters and does not drastically scale up its parameters as the model size expands. 
However, \pt introduces extra soft prompt tokens, leading to longer input sequences, which significantly impacts training/inference time and memory usage due to the Transformer's quadratic complexity. 
Particularly concerning for Large Language Models (LLMs) that face heavy daily querying. 
To address this issue, we propose \textbf{De}composed \textbf{P}rompt \textbf{T}uning (\ours), which decomposes the soft prompt into a shorter soft prompt and a pair of low-rank matrices that are then optimised with two different learning rates. 
This allows \ours to achieve better performance while saving substantial memory and time costs compared to vanilla \pt and its variants, without changing trainable parameter sizes.
Through extensive experiments on 23 natural language processing (\nlp) and vision-language (VL) tasks, we demonstrate that \ours outperforms state-of-the-art \peft approaches, including the full fine-tuning baseline, in some scenarios.
Additionally, we empirically show that \ours grows more efficient as the model size increases.
Our further study reveals that \ours integrates seamlessly with parameter-efficient transfer learning in the few-shot learning setting and highlights its adaptability to various model architectures and sizes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper finds that the fixed token embedding offset in DePT limits its generalization capability across different model inputs, leading to suboptimal performance. To address these issues, the authors introduce Adaptive Decomposed Prompt Tuning (ADePT), which consists of a short soft prompt and a shallow token-shared feedforward neural network. ADePT uses the token-shared feedforward neural network to learn embedding offsets for each token. This enables ADePT to achieve superior adaptability without requiring more inference time or additional trainable parameters than standard PT and its variants.

Overall, this paper provides a thorough and clear analysis. It offers a simple yet effective solution to the offset issues present in standard PT. However, I still have the following questions: 
1. How robust is this method, and does it possess general applicability? 
2. Is this method still effective for long text problems? 
3. Is ADePT effective for other large parameter language models, such as the LLaMa series? I hope the authors can provide answers to these questions.

### Strengths
This paper introduces the Adaptive Decomposition Prompt Tuning (ADePT) method, which innovatively addresses the generalization limitations caused by fixed token embedding offsets in traditional DePT methods. ADePT achieves excellent adaptability without increasing inference time or requiring additional parameters. The analysis is thorough, and the method is both simple and effective, offering new directions for future research. Additionally, the experiments are conducted rigorously, and the writing is clear and concise.

### Weaknesses
I believe this method may lack generality, especially when applied to large language models and long-text tasks. The main reason for questioning this is whether feedforward neural networks possess sufficient semantic understanding capabilities. Additionally, there is room for further optimization in the figure.

### Questions
1. How robust is this method, does it have general applicability, and will incorporating AdePT affect the model's generalizability?
2. Is this method still effective for long text problems? 
3. Is ADePT effective for other large parameter language models, such as the LLaMa series? I hope the authors can provide answers to these questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Adaptive Decomposed Prompt Tuning (ADePT), a novel approach in parameter-efficient fine-tuning (PeFT) that significantly enhances the adaptability of pre-trained large language models (PLMs) to various downstream tasks. ADePT improves Decomposed Prompt Tuning (DePT) by addressing its limitations: DePT's fixed token embedding offsets often underperform due to their inability to dynamically adjust to different model inputs. By integrating a token-shared feed-forward neural network (FFNN), ADePT dynamically adjusts embedding offsets, tailored to each specific input token. This adaptive mechanism allows ADePT to maintain the inference speed advantages of DePT while achieving state-of-the-art (SOTA) performance in adaptation. Extensively tested across 22 natural language processing (NLP) tasks and two PLMs of differing scales, ADePT not only surpasses other PeFT methods like Adapters, LoRA, and standard Prompt Tuning (PT) but also exceeds full model fine-tuning benchmarks in certain scenarios.

### Strengths
1. The paper provides a comprehensive overview of Parameter Efficient Finetuning (PeFT), effectively situating ADePT within the broader research landscape and highlighting its contributions.

2. ADePT is intuitive and well-motivated. The arguments and experiments in Section 3.2 convincingly demonstrate the limitations of DePT being a low-rank absolute positional embedding, paving the way for ADePT, which instead uses token-wise MLP for calculating embedding offsets.

3. The experiments conducted with T5-220M are thorough, incorporating all relevant benchmarks and key baseline comparisons. The results are presented with nice detail and clarity.

4. At the 220M scale, ADePT shows remarkable efficacy, particularly in data-scarce scenarios such as RTE and CoLA tasks, where it not only competes but also surpasses full finetuning, showing its superior performance.

### Weaknesses
1. The robustness of the experiments with the 3B model does not match the standards set by the 220M scale evaluations. Notably, the selection of fewer benchmark tasks without clear justification, as well as the omission of significant baselines such as Adapters and LoRA, weakens the overall experimental credibility for the 3B model.

2. The performance improvements of ADePT over PT for the T5-3B model is only 0.1 or 0.2 pts for each task in Table 5. This tiny margin on a selected set of tasks may suggest that DePT-style methods cannot scale to larger models.

3. A key appeal of PeFT methods is their cost-efficiency in finetuning; however, the paper lacks comparative analysis of the training costs across different PeFT methods, specifically within the PT family where training speed is more comparable (PT, DePT, and ADePT). Such omission leaves a gap in understanding their real-world benefits.

4. The description of DePT and ADePT in the "Introduction" section lacks clarity. Phrases such as "the token embeddings of DePT violate the uniqueness of token embeddings" are presented without sufficient context, making them hard to understand without referring to the formulas in Section 3.

### Questions
1. What are the criteria of selecting the datasets and baselines for 3B-scale models?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposed to extend Prompt Tuning and DePT, by replacing the position-based updates that DePT applies to the true token embeddings with content-based updates by passing the token embedding through a small (bottlenecked, down-project + up-project) MLP and adding that to the original token embedding.

They test its effectiveness on many datasets, against many baselines, and use multiple frozen models. They find that their method performs best in many cases.

### Strengths
The paper introduces the other work in the space really well and does a good job contextualizing itself among that work.

The pilot experiments highlighting the weakness of DePT are a good motivation for their work.

The paper compares to a lot of different baselines, including PEFT methods beyond just prompt tuning.

The paper evaluates the method on a lot of different datasets, increasing the trust you can put into setting good results if you used it on your task.

The paper uses multiple different pre-trained models as the frozen models the PEFTs are applied to. These are also at two different scales. It is good to see the results still hold.

### Weaknesses
The weakness of DePT is outlined in the paper as its "fixed token embedding offsets". This point would be much clearer if it was re-framed as the DePT offsets are "position-based" while the ADePT offsets are "content/token-based". Both are "fixed token embedding offsets" (ADePT output is fixed once the input token is know, it isn't contextual). This framing would make a lot of their examples about the issues much clearer. For example the section about the [t1, t2] being added causing a shift if which offsets are applied where much clearer. It also makes their point about the DePT offsets not doing much because they have to handle all tokens more obvious! It also could make this example much clearer where it could cast [t1,t2] as a "system prompt" added after the fact that messes up the learned position embeddings from DePT (and also hightlight how DePT may not play nicely with prompt engineering which ADePT probably would).

They state that "embedding for each token should be unique after being offset" as a critique of DePT, but thinking of DePT as position-wise offsets it doesn't seem like a problem, especially given positional embeddings work.

The prose can be tighten up quite a bit. There are lots of parts that repeat themselves multiple times, for example the position-wise implementation of DePT is over-explained multiple times. Similarly, much of the algebraic manipulations of the parameter counts could be omitted.

Many of the increases in performance are rather small, although the simplicity of this method makes that more acceptable.

It is unclear is they use the optimization stabilization of Razdaibiedina et al 2023 they mention in the introduction when using PT.

Much of the baseline performance numbers are from other works, opening the possibility of a mis-match in setting. For example, the numbers for SPoT in Table 3 are surprising as they are lower than the Prompt Tuning numbers, but they are taken from different papers.

### Questions
Did you compare to fine-tuning the prompt and the embedding matrix? The would be a small loss in generality (tokens not seen during training would not get updated) but it would be a much simpler implementation. I would be curious to see how this version performed on CB too, as a possible explanation of ADePT's poor performance could be that the NN offsets don't work well on unattested words.

When measuring the latency of different methods, where the token offsets for ADePT precomputed and folded into the embedding table or was the NN run for each token?

Did you try using the LM-adapted model from Lester et al 2021 instead of the span-corrupted T5 models used here? It is also unclear if you used the original T5 models or the T5 1.1 models, IIRC, some of the datasets used were seen during pre-training of the original T5 models.

As the DePT offsets only differ between each position, it seems reasonable that they have low mean and variance. In contrast, ADePT is per-token and content based so it seems reasonable that it would have a much higher variance. I'm not sure mean and variance is the correct metric to gauge how much these offsets are actually doing (or if they are sub-optimized). Something like a norm of the offsets might make more sense? Or it could have been measured directly in an ablation where the soft prompt learned in ADePT/DePT is used without the token offsets.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper is about prompt tuning, which improves on the DePT method and propose a method called ADePT. It replaces fixed token embedding offsets with a shallow feed-forward neural network that can dynamically generate offsets for the input token embeddings, thereby providing better adaptability to different input tokens.

### Strengths
1. The introduction of a token-shared feed-forward neural network as a solution is well-motivated, by effectively identifying critical limitations in the DePT method of the static token embedding offsets.
2. The experiments are thorough, the performance are reported in many datasets, including NLU and NLG.

### Weaknesses
1. Lack of analysis of the proposed method. For example, the method includes the bottleneck hyperparameter that controls the total #params that does not exceed vanilla PT. However, the size of bottleneck as well as the corresponding prompt length on the performance is not clear. It is also interesting to show if relocated all the #params on the learnable projection, where prompt length=0.
2. In Table 8, comparing with the improvement DePT brings to PT in both accuracy and latency, the proposed ADePT seems trade latency to accuracy. Moreover, the complexity introduced in the learnable projection hurts the few-shot performance compared with DePT.
3. The method is only tested on two T5 language models, including the base and 3B variants. It should also be tested on the decoder models.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
