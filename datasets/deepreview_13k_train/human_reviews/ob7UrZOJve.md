# Inheritune: Training Smaller Yet More Attentive Language Models

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
Large Language Models (LLMs) have achieved remarkable performance across various natural language processing tasks, primarily due to the transformer architecture and its self-attention mechanism. However, we observe that in standard decoder-style LLMs, attention matrices degenerate to single-column for deeper layers. Layers in this state are unable to learn anything meaningful and mostly redundant; we refer to these as \emph{lazy layers}. The goal of this paper is to train smaller models by eliminating this structural inefficiency without compromising performance.

Motivated by this observation, we propose \textbf{Inheritune}, a simple yet effective training recipe for developing smaller, high-performing language models. Smaller models trained with \method{} inherit early transformer layers from a larger pre-trained model, then retrain and progressively expand until they match or exceed the performance of the larger model. We demonstrate that \method{} enables the training of various sizes of GPT-2 models on datasets like OpenWebText-9B and FineWeb\_Edu. Models trained with \method{}, despite having significantly fewer layers, match or even surpass the performance of their larger counterparts. For instance, our 16-layer GPT-2 medium variant achieves comparable performance to the standard 24-layer GPT-2 medium model.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces Inheritune, a training method designed to create smaller, high-performing language models. This method works by inheriting the initial layers from a larger pre-trained model and gradually expanding the smaller model until its performance matches or exceeds that of the larger model.

The authors investigate attention degeneration in standard large language models (LLMs) and find that rank-collapsed attention matrices often reduce to single-column structures, highlighting inefficiencies in the attention mechanism, especially in deeper layers. This insight into the limitations of deep attention inspired the development of Inheritune.

Experiments on different sizes of GPT-2 models, using the OpenWebText and FineWeb_Edu datasets, show that models trained with Inheritune, despite having significantly fewer layers, can match or even surpass the performance of larger models. They also outperform several baseline methods, such as stacking and knowledge distillation.

### Strengths
(+) The proposed training technique is simple and clear.
(+) The authors empirically investigate attention degeneration in standard LLM settings, focusing on rank collapse in attention matrices within the deeper layers of models, such as GPT-2.

### Weaknesses
(-) An analysis of whether attention degradation is resolved in the target model trained with Inheritune is missing and should be included.

(-) The adequacy of training for the reference model in Table 1 is uncertain. Given the hyperparameter setting, the GPT2-large (770M) model was trained with only 1.6 billion tokens, using a batch size of 16K tokens and a total of 100K steps. This training setup appears insufficient for comprehensive model training. Thus, it is crucial to compare the performance of the target model against a reference model that has undergone adequate training. Specifically, the number of training tokens should be comparable to what is typically used for pre-training models of this size.

(-) Since the Inheritune target model begins with the weights of the pretrained model, it has a much lower initial loss at step 0, giving it a head start compared to models trained from scratch. As a result, it’s difficult to determine whether models using Inheritune truly lead to better generalization and convergence. The lower initial loss could be a significant confounding factor, making it unclear if the performance gains are due to the method itself or simply the advantageous starting point.

(-) The baselines used for comparison need to be updated to reflect advancements in training techniques. Some of the latest research on half-width models, stacking, and distillation that would serve as recommended baselines are as follows:
•	Xiaoqi Jiao et el., TinyBERT: Distilling BERT for Natural Language Understanding, 2020
•	Sheng Shen et al., Staged Training for Transformer Language Models, 2022
•	Peihao Wang et el., LEARNING TO GROW PRETRAINED MODELS FOR EFFICIENT TRANSFORMER TRAINING, 2023

(-) There seems to be a typo: line 323, "layers 0-17" should be "layers 9-17."

### Questions
1. Why are the blanks for downstream task performance in Table 1 not filled in?
2. According to the training details of the GPT-2 models (Supplement C.1), it appears that GPT-2 medium was trained on more data than GPT-2 xLarge. Specifically, GPT-2 medium was trained with a batch size of 50K tokens for 100K steps (totaling 5 billion tokens), while GPT-2 xLarge used a batch size of only 16K tokens for the same number of steps (totaling 1.6 billion tokens). Is this a typo?
3. Have you considered initializing the layers added during the growth phase using methods such as random initialization or copying previous layers of the target model? This is because the layers added during the growth phase closely resemble the "lazy layers" described in the paper.
4. It would be helpful to provide a clear criterion for identifying a specific layer as a lazy layer (e.g., based on the rank, mass, or other properties of the attention matrix).

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a practical method "Inheritune" to create more efficient language models by reducing the layers of the original model. The authors analyze the phenomenon of "attention degeneration" in the deep layers of transformer language models and compare the proposed method against relevant baselines.

### Strengths
1. The analysis of attention degeneration phenomenon is well written and easy to understand. The motivation of this work is clear.
2. The paper proposes a practical and lightweight approach to perform model pruning that can be implemented with ease.

### Weaknesses
1. The scope of the degeneration analysis and experiments is limited. Only GPT-2 model variants have been discussed and evaluated. The generalization on other model architectures is unclear.
2. The choice of the initialization point n = k/2 assumes degeneration only takes place in the second half of the total number of layers, which is not supported by theoretical evidence.

### Questions
Please refer to Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies and proposes a better way to create smaller LLMs from existing pretrained models, in particular by examining whether the learned attention layers exhibit meaningful attention patterns or degenerate into single-column structures (“lazy layers”). They find later layers are more lazy across GPT-2 LLMs, and propose Inheritune as a method to exploit this phenomenon. Inheritune works by initializing a smaller model with the first half of the layers from a pre-trained larger LLM, training this model, and then progressively growing it by adding more blocks if necessary. This process is repeated until the smaller model's performance matches or surpasses that of the reference model. Through experiments using GPT-2 models of varying sizes, on datasets like OpenWebText-9B and FineWeb_edu, and using evaluations including language modeling perplexity and downstream LM Evaluation harness tasks, the authors demonstrate that Inheritune consistently outperforms various baselines, including larger models trained from scratch, models initialized with different techniques (stacking, hybrid stacking, half-width), and models trained using knowledge distillation. They further provide interesting analysis into Inheritune's behavior via various ablations on target modules and pretraining data mix.

### Strengths
**Interesting study + method contribution**
I liked the combination of studying a natural phenomenon (lazy layers showing up in pretrained decoder LLMs), and further exploiting this to create a well-motivated method for efficiently creating smaller models. 

**Comprehensive Task Evaluation**

I appreciated how the authors evaluated not just validation-set perplexity, but also zero-shot performance on WikiText and Lambada in main experiments, and further considered popular LM Evaluation Harness tasks.

**Good Performance**

The experiments demonstrate Inheritune's strong performance compared to baselines such as randomly initializing models, stacking, hybrid stacking, and knowledge distillation.


**Interesting Ablation Studies for In-depth Analysis**

I appreciated the study into the different aspects of Inheritune, including initializing different submodules, using different pretraining data mixes.

### Weaknesses
 **Insufficient treatment of related work / first contribution novelty**

How does the notion of "lazy layers" relate to prior work such as Attention Sinks [1]? In particular, the claim that “Notably, this phenomenon has not been studied in the context of standard LLMs.” (L043) does not seem true? See Attention Sinks [1] at ICLR 2024, which studied and observed before that several standard decoder-only LLMs (Llama 2 7B, Pythia 12B, Falcon 7B, MPT-7B) display this “lazy layer” phenomenon. While the authors clarify that their definition of lazy layers requires *all* attention heads within a layer to exhibit rank-1 behavior, the connection to attention sinks, which can also manifest as single-column attention patterns, needs more careful discussion. The method and way to exploit this lazy layer phenomenon seem novel, but I do think there needs to be better discussion on how the lazy layer contribution is novel, especially given the overlap with attention sink phenomena.

**Limited model diversity (model family and scale)**

The study and method are limited to a single model family (GPT-2), where the largest LLM evaluated is only 1.5B parameters. Overall, the paper would be stronger if the findings were shown beyond a single class of models, and on a variety of more modern and popular models (e.g., Llama 3 8B, Mistral 7B, Phi 1.5, Gemma, etc.). While I don't fault the authors for not evaluating 7B models due to budget constraints  (although doing so would increase my score); even under the 1.5B parameter budget, we have models available such as Phi 1.5 from 2023 [2]. Furthermore, even without access to the pretraining data for models like Gemma or Phi, the authors could still use a probing dataset (such as a subset of OpenWebText validation data) to analyze the rank of attention matrices and identify lazy layers. This would demonstrate the generalizability of their lazy layer observation and the potential applicability of Inheritune to a broader range of models.

**Motivation behind comparisons**

I found some of the comparisons a bit too "baseline", but this could be clarified with discussion on their motivation.
* For example, if the motivation of Inheritune is to save model memory, how does the method compare to quantization techniques that can drastically reduce the parameter memory?
* If using less layers can improve inference or generation efficiency (as a benefit over quantization techniques), it would be good to see this benchmarking analysis

[1] Efficient Streaming Language Models with Attention Sinks, https://arxiv.org/abs/2309.17453

[2] Textbooks Are All You Need II: phi-1.5 technical report https://arxiv.org/abs/2309.05463

**--- After rebuttal revisions ---**
I think the authors did a reasonable job clarifying the distinction between lazy layers and attention sinks, while also extending their analysis to pretrained LLMs outside of GPT-2 architectures trained on OWT.

I still think the paper's presentation + method could be improved, e.g., explicitly using the number of observed  lazy layers to recommend how many layers should be kept (instead, they keep this main design choice for pruning at `num_layers // 2`, which makes the lazy layer connection a bit vacuous imo). 

For this I am willing to raise my score to 6.

### Questions
Why are the target / smaller models initialized as k/2, if k is the number of layers in the original model? This seems a bit ad-hoc. Was there any study into if lazy layers were much more frequent in the second-half of the LLMs? Plotting or visualizing this would be support this design choice more.   
* Because you have the LLMs, some analysis into whether a layer is lazy or not, and using this to inform which layers should be preserved, might also improve the method quality. 

Is the step-count comparison fair? To make an Inheritune model, we need to have a full pretrained model in the first place. Are the steps it takes to acquire this pretrained model factored into the total step comparisons? 
* Conversely, when making the claim that Inheritune outperforms randomly initialized models with the original parameter counts, are these full models further trained to hit the same total training updates that it takes to create Inheritune models? 

In Figure 2, if the GPT2 models are decoder-only / causal, should the attention weights only be limited to lower-triangular?

### Soundness
2

### Presentation
3

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
This paper highlights attention degeneration, where layers become rank-1 matrices, leading to ineffective learning in "lazy layers." The proposed method initializes a smaller model with a few layers from a larger pre-trained model and progressively adds layers, enabling efficient training of high-performing models. Experiments across various GPT-2 sizes show that Inheritune maintains or improves performance compared to larger models trained from scratch or with other initialization methods, establishing it as an effective strategy for compact language models.

### Strengths
The paper is well-written and easy to understand, with a logical flow that supports the arguments presented. Additionally, it demonstrates the superiority of the proposed method through a variety of experiments.

### Weaknesses
It seems a bit too intuitive to refer to this as an initialization method utilizing the lazy layer phenomenon, even though this paper has identified the occurrence of lazy layers. The logic of using early layers for initialization because of lazy layers feels somewhat weak. When I consider that there are 36 teacher layers and I need to initialize 18 layers, it appears quite obvious to select the first 18 layers, as they are likely to be more compatible with the embeddings.

The experiments presented in the paper are largely conducted with a limited number of steps, which raises questions about the actual performance. It seems that the approach does not significantly differ from simply trimming a larger model and fine-tuning it, leading me to wonder whether the results truly reflect superior performance. Furthermore, the perplexity improvements in Table 1 and Table 2, while present, do not appear substantial enough to definitively claim a significant advantage. The exclusive focus on perplexity in Table 2, without comparing other relevant metrics, also limits the scope of the evaluation. Finally, it remains unclear whether the identified lazy layers are a consistent phenomenon across different datasets or if they are specific to the data used in the experiments.

### Questions
(1) I think the phenomenon of lazy layers is similar to the attention sink phenomenon. Does approaching rank 1 mean that attention is concentrated on a specific token?

(2) In Figures 1 (c) and (f), rather than suggesting that the lazy layers are unnecessary, I suspect that the early layers are more compatible with the embeddings. Could you perhaps compare using the first nine layers with using the remaining ones randomly?

(3) This paper adopts a three-step approach of Inherit, Train, and Grow. What are the advantages of this method compared to reaching the final size all at once?

(4) I would like to inquire about the comparison between the GPT-2 Medium 16-layer variant trained from scratch and the one trained with Inheritune in Figure 2, 9. Does Inheritune effectively prevent rank collapse?

### Soundness
2

### Presentation
3

### Contribution
2
