# Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Recent advancements in Transformer-based large language models (LLMs) have set new standards in natural language processing. However, the classical softmax attention incurs significant computational costs, leading to a $\gO(T)$ complexity for per-token generation, where $T$ represents the context length. This work explores reducing LLMs' complexity while maintaining performance by introducing Rodimus and its enhanced version, Rodimus$+$. Rodimus employs an innovative data-dependent tempered selection (DDTS) mechanism within a linear attention-based, purely recurrent framework, achieving significant accuracy while drastically reducing the memory usage typically associated with recurrent models. This method exemplifies semantic compression by maintaining essential input information with fixed-size hidden states. Building on this, Rodimus$+$ combines Rodimus with the innovative Sliding Window Shared-Key Attention (SW-SKA) in a hybrid approach, effectively leveraging the complementary semantic, token, and head compression techniques. Our experiments demonstrate that Rodimus$+$-1.6B, trained on 1 trillion tokens, achieves superior downstream performance against models trained on more tokens, including Qwen2-1.5B and RWKV6-1.6B, underscoring its potential to redefine the accuracy-efficiency balance in LLMs. 
\emph{Model code and pre-trained checkpoints will be available soon.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces two efficient Transformer architectures that incorporate semantic, token, and head compression: Rodimus, which is purely based on linear recurrence and, Rodimus+, which combines linear recurrence with sliding window attention to improve the quality and efficiency tradeoff in LLMs. The key components proposed include a data-dependent tempered selection mechanism (DDTS) and sliding window shared-key attention (SW-SKA). Experiments with models between 130M to 1.6B on language modeling, various downstream tasks, and retrieval tasks show that Rodimus+ achieves better performance than models based on recurrence such as Mamba and based on standard attention such as Pythia.

### Strengths
1. The paper introduces two new techniques, data-dependent tempered selection (DDTS) and shared-key attention (SKA). DDTS is a new gating-based recurrent type for state-space models which enhances performance and increases parameter efficiency through reducing hidden state size. SKA shares a single key representation to reduce memory footprint while maintaining the multi-value setting of the original multi-head attention. 
2. These techniques are evaluated extensively in general tasks (content analysis, commonsense reasoning, reading comprehension, etc), long-context retrieval tasks (NeedleBench) and show improved performance compared to various efficient and standard transformer models.
3. Overall, the paper is satisfactorily written, the proposed techniques are clearly described, and the prior work moderately well covered. The experiment section is thorough and has an organization that is easy to follow.

### Weaknesses
1. While the main focus of the paper is to improve the trade-off in terms of accuracy and efficiency, the experiments do not discuss the efficiency aspects such as memory cost and latency or times for  training/inference. 
2. Even though the specific gates proposed haven't been used in prior work, the novelty in the design can be considered rather incremental as the formulation is very similar to previous ones (Mamba, S4D).
3. Direct comparisons with alternative gating functions in SSMs using the exact same architecture and model size are lacking. This prevents the comprehensive understanding of the benefits brought by the specific gating techniques.
4. The evidence provided in this paper to support the claim of "breaking" the accuracy-efficiency tradeoff is not comprehensive. 
   - Several dimensions are lacking in the experimental setup: comparison with a wide range of efficient attention models (sparse, linear, hybrid), head-to-head comparisons (equal number of params, HPO budget), and rigorous hyperparameter optimization. 
   - In addition, the performance of Rodimus compared to Mamba when using the same number of parameters is actually the same or worse. 
   - Only when combining with SWA and increasing number of parameters performance improves further with Rodimus+ but this is not a valuable comparison since Mamba2 is not a hybrid method.

### Questions
1. Was there any specific reason for not using the same number of parameters for Rodimus and Mamba models? For instance, in the third block of Table 2 Mamba has 0.37B parameters while Rodimus has 0.46+B parameters and in the fourth block Mamba has 1.3/1.4 while Rodimus 1.4/1.6. Such differences make it difficult to understand if the improvement comes from the proposed gating design or from pure increase in capacity. To strengthen the claims made in the paper, I'd suggest to the authors to provide a head-to-head comparison with that model. 
2. There is lack of comparison with hybrid models, even though Rodimus+ is in that category of models. Have you considered comparing with such models? A few examples include: Jamba, Griffin, Recurrent-Gemma. 
3. What is the memory consumption and training/inference times for the models compared in the experiments? Even though the efficiency aspect is emphasized a lot in the beginning of the paper, it is under explored in the later sections. 
4. Can the authors report language modeling scores with the larger model sizes? The ones reported on Wikitext-103 are only with very small models and the conclusions that we can draw from it are limited.
5. In Figures 1a and 1b, what is the performance of a standard Transformer? 
6. What is the memory benefit of SKA compared to alternative attention mechanisms such as MQA and GQA? It would be useful to include an ablation study that highlights their differences.

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
Attention is the most memory-costly operation in transformer architecture. It scales quadratically in sequence length, as it can correlates each position to each other. To overcome this bottleneck, state space models were introduced, however usually degenerated in downstream performance.
The authors show that their particular gating mechanics of state space models "Rodimus/DDTS" improve downstream performance as they may model language more naturally. It in particular comprises a low-rank auto-encoder approximation and a softmax based temperature parameter.
Furthermore the authors introduce a shared key attention "SKA", that reduces some memory footprint and can be shown to have the same expressiveness to standard attention. Both methods are "Rodimus+".
Lots of efforts was done with evaluations, albeit, i'm afraid, not in a comparable fashion..

### Strengths
the paper is generally well written and presented. ideas appear thought-through and are (somewhat) mathematically reasoned.
more reasonable interplay of gating mechanics / ssm's in general and attention is pretty important to iterate towards more robust language models.

### Weaknesses
1) i understood the change to Rodimus+ is the two norms, SW-SKA and FFN per layer. how can this sum up to those negligible changes in parameters in Tab 2 - or do you use entirely different architecture configs?
2) i do not find anything conclusive about runtime estimates (only a vague big-O estimation and some chunking approach for training). This should not be optional!
3) my major concern is that only Fig 1 / Tab 1 / Fig 4 appear to be "somewhat fair" comparisons but in a ridiculous low scale. i cannot follow steps in section 4 most of the time. in particular i could not reconstruct the experiment design due to missing descriptions partially found in appendix.
4) table 2 appears pretty delusive. variances in the dataset and tokenizer alone are able to cause significant variations already, which is not discussed at all and not negligible! the only comparable lines appear to be the first 3. the only thing i can derive here is that rodimus can  model language. a sentence like line 478 is pretty off standard to me. you pretend to have a better method so do a fair 1:1 training/ scaling analysis (on less models). tab 14 should be sufficient for such a case study, but is also pretty uncomparable?

### Questions
1) line 120 : "matrices"
2) Tab 1 only ~2M parameters increase to Rodimus+ is the SKA + FFM? other hyperparameters are the same? the changes appear to be pretty random in tab 2

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces Rodimus and Rodimus+, two efficient alternatives to traditional Transformer models that aim to balance accuracy and computational efficiency. Rodimus uses a Data-Dependent Tempered Selection (DDTS) mechanism which is an improved parameterization of gated linear attention. Rodimus+ extends this with Sliding Window Shared-Key Attention (SW-SKA) for enhanced local token focus, further optimizing efficiency without sacrificing performance. Experiments demonstrate these models outperform comparable models on language modeling and recall tasks, making Rodimus+ a scalable, efficient alternative for large language models.

### Strengths
- This work comprehensively examines the design space of gated linear attention (GLA), particularly focusing on an outer-product-based gating structure with input and forget gates. It addresses a gap in systematic studies on GLA's gating mechanisms, positioning itself well to bridge this gap. The proposed Data-Dependent Tempered Selection (DDTS) mechanism is both intuitively appealing and practically useful, as demonstrated by experimental results. Additionally, the definition of the selection mechanism in this context is compelling.

- The ablation study on architectural design is relatively thorough.

### Weaknesses
 - The work appears somewhat incremental, as it largely builds upon existing concepts. Technical contribution is limited.

- Regarding language modeling experiments, the choice of the WikiText-103 dataset for language modeling may not be ideal, as it is relatively simplistic and sensitive to hyperparameter tuning. For Figure 1a, larger-scale experiments using more extensive datasets would provide a more robust evaluation. Additionally, the controlled experiment scale in Table 2 is too limited; ideally, models with around 1B parameters trained on 100B tokens should be tested.

- Regarding recall-intensive eval,  the NeedleBench benchmark may be overly challenging for smaller-scale models, as evidenced by Figure 5, where all models perform poorly. Consider testing on simpler recall-intensive benchmarks (e.g., FDA, SWDE, NQ, SQuAD, TriviaQA, DROP as used in [1, Table 1]) for more interpretable results. Additionally, it would be insightful to know if Rodimus can outperform Mamba2 in recall performance with half the state size under equivalent training conditions.

- Training and inference throughputs would be reported.

- Several minor errors are present throughout. See the list of specific corrections below.

### Questions
- How significant is $ d_t $ in Eq. (11)?

- Have you investigated the ordering of Rodimus, SW-SKA, and FFN in Eq. (13)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Rodimus, a linear attention based model, purely recurrent, and and its enhanced variant Rodimus+, a hybrid model, which combines Rodimus with SW-SKA. The paper aims at reducing the computational inefficiencies of traditional softmax attention mechanisms in large language models (LLMs). Rodimus uses a linear attention approach combined with a data dependent tempered selection mechanism to achieve O(T) complexity for per-token generation. This significantly reduces memory usage while maintaining performance (a key limitation of recurrent models). Rodimus+ extends this by integrating a sliding window shared key attention (SW-SKA), which combines the strengths of semantic, token, and head compression to enhance efficiency and accuracy.

The paper is in the broader context of linear attention mechanisms such as those introduced by Katharopoulos et al. (2020), which reduce computational complexity through kernel-based approximations. Plus, it builds on the concept of sparse attention, similar to the approaches used in Longformer (Beltagy et al., 2020), but enhances it by integrating local and global context understanding. Rodimus+ also leverages ideas from Grouped-Query Attention (GQA) (Ainslie et al., 2023) by implementing shared-key attention, compressing the memory footprint while preserving performance. 

The experimental results show that Rodimus+ achieves better downstream performance even against models trained on more tokens.

### Strengths
The proposed approach seems to achieve interesting results in complexity vs performances: 
- Rodimus+ manages to achieve high performance even when trained on fewer tokens compared to other models. 
- The authors provide extensive validation across multiple benchmarks, showing that Rodimus+ outperforms existing models. 
- The introduction of the data dependent tempered selection mechanism shows an innovative way to manage the flow of information in recurrent architectures. 
The code will be available after the review process.

### Weaknesses
 - While the innovations presented are technically very interesting, they also introduce a level of complexity that could be a barrier for widespread usage.
- Although Rodimus improves on the traditional recurrent models, it may still inherit some of the limitations associated with recurrent architectures (like the sequential processing bottlenecks).

### Questions
How does the semantic compression affect the fine-tuning performance on specific downstream tasks that require retaining nuanced context?

### Soundness
3

### Presentation
3

### Contribution
2
