# Answer, Assemble, Ace: Understanding How LMs Answer Multiple Choice Questions

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Multiple-choice question answering (MCQA) is a key competence of performant transformer language models that is tested by mainstream benchmarks. However, recent evidence shows that models can have quite a range of performance, particularly when the task format is diversified slightly (such as by shuffling answer choice order). 
In this work we ask: \emph{how do successful models perform formatted MCQA?} We employ vocabulary projection and activation patching methods to localize key hidden states that encode relevant information for predicting the correct answer. We find that prediction of a specific answer symbol 
is causally attributed to a single middle layer, and specifically its multi-head self-attention mechanism. 
We show that subsequent layers increase the probability of the predicted answer symbol in vocabulary space, and that this probability increase is associated with a sparse set of attention heads with unique roles. We additionally uncover differences in how different models adjust to alternative symbols. Finally, we demonstrate that a synthetic task can disentangle sources of model error to pinpoint when a model has learned formatted MCQA, and show that an inability to separate answer symbol tokens in vocabulary space is a property of models unable to perform formatted MCQA tasks.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper is devoted to the analysis of the internal processing of Transformer LLMs when answering Multiple Choice Question Answering task. First, it is shown that the ability to answer such question can be attributed to a few layers in the model. Second, this ability is implemented by a sparse set of attention heads. Third, this ability emerges at some point during model's training. Finally, an interesting observation is that in case of on-standard label symbols (e.g. QXYZ instead of ABCD) the model first tries to predict typical characters corresponding the answer position, which are replaced with the correct character in higher layers. 

The analysis is performed on three MCQA dataset: MMLU, HellaSwag, and synthetic Colors dataset. As for models, three families are considered: LlaMa, Qwen and Olmo. For deep analysys, the models with consistent results (i.e. robust to answer order and labels perturbation) on all the three datasets are chosen

### Strengths
+ The paper is clearly written. All the claims of the paper are supported by experiments, and the results are sound
+ The claimed properties are consisstently observed over datasets and model's families
+ The observed results are interesting and helps to understand the internal mechanics of LLMs
+ Althougt the methods used in the paper are not novel, the quality of the presented analysis is quite high. I especially appreciate the models's robustness analysis and the difference between probits and logits

### Weaknesses
- The range of considered model sizes is limited (0.5B-7B)
- Although the observations presented in the paper are clear and consistent, they don't provide any real understanding how the model works. Besides, it is limited to Multiple Choic eQuestion Answering tasks, and there is no attempts to extend it to more general understanding of the inner Transformer's mechanics.

### Questions
1. In sec.3.4, why the threshold on 20%+ random (i.e. 45%) is chosen? Is there any reason behind this choice?

2. Evalusting 3-shot accuracy with alternative symbols (e.g. QXYZ), which symbols are used for in-context examples?

3. Do you have any ideas which of the observed phenomena can be extended to other tasks, beyond MCQA?

### Soundness
4

### Presentation
4

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
The study investigates how LLMs solve multiple-choice question-answering (MCQA) tasks, focusing on intrinsic interpretability. The authors explore how the specific layers and attention heads contribute to selecting the correct answer from a set of choices. By applying methods like vocabulary projection and activation patching, the study reveals that particular middle transformer layers play a critical role in aligning the model’s predictions with the correct answer symbol. These components act selectively to bind the answer symbol (e.g., A, B, C, D) to the correct answer phrase. The paper provides a comprehensive pre-analysis of multiple models, including Olmo, Llama, and Qwen, across various prompt formats and datasets to select the models that understand the MCQA task. Additionally, it introduces a synthetic MCQA task to isolate MCQA capabilities from dataset-specific challenges. Key findings indicate that robust MCQA performance relies on both specific layers and sparse attention heads that drive answer selection, with some layers adapting to unusual symbol choices in later stages. This work offers a deeper understanding of model-specific MCQA mechanisms.

### Strengths
- Evaluating across various prompt formats and permutations is really convincing, it really highlights this paper
- Interesting analysis that includes both MHSA and MLP patching
- Good visualization of when the MCQA understanding forms during training

### Weaknesses
- The motivation for selecting the patching format is not fully substantiated. By "patching format," I refer to the reordering of the correct answer to a new position. Although this approach is intuitively clear, I believe the motivation could be strengthened by exploring different patching formats (for example, removing correct answer from sample).
- The circuits are shown to be dependent on the nodes (parts of model) for patching [1]. Patching the layers is interesting, but for full picture it would be good to examine the attention maps by patching. 

[1] Miller, Joseph, Bilal Chughtai, and William Saunders. "Transformer Circuit Evaluation Metrics Are Not Robust." First Conference on Language Modeling. 2024.

### Questions
- Could you please specify what values are presented by Fig. 8? Is taken from logit lens applied to MSHA components by heads? 
- What conclusion do you make from the fact that in Fig. 7c (MHSA) change in answers are visible only in 24 layer, while in Fig.3 it maintains further. It will be interesting to describe in detail that mechanism.
- It is relatively small issue, but do you consider using another variant of logit lens? The reason is that logit lens by itself could be potentially worse for earlier layers [2] 


Small comments:
- Fig.8 is not aligned 

[2] Belrose, Nora, et al. "Eliciting latent predictions from transformers with the tuned lens." (2023).

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
This research work studies how LLMs solve MCQA task. Authors show which layers and layer components play the most crucial role in this process and at which point the OLMO model starts to learn to solve this task. They also find out how different is this process when the options are named by other symbols (not A,B,C,D).

### Strengths
- The paper analyses an important topic, since MCQA tasks are very common in LLM benchmarks.
- Authors came up with a good idea for their synthetic dataset. That dataset allows them to distinguish a model's understanding of MCQA format from it's knowledge in particular area, that is important for proper analysis.
- A number of experiments are done on several models: Olmo, LLaMA 3.1, Qwen: -chat and -base versions. These models look like an appropriate objects for this study.
- At the second half of their paper, authors especially concentrate on those models that are good in solving three MCQA tasks (synthetic, HellaSwag and MMLU). It is also a good move, because it allows to ignore "noisy" properties of weak models that could mislead researcher and reader otherwise.
- Authors use a good practices in MCQA research, i.e. they permute A/B/C/D symbols and consider alternative symbols for answer options.

### Weaknesses
- The claim in the lines 518-519 (_"these results demonstrate that an inability to disentangle answer symbol tokens in vocabulary space is a property of poorly-performing models"_) is not sufficiently supported. Such claim definitely cannot be deduced from the analysis of the checkpoints of only one particular Olmo 0724 7B base model (however, at lines 79-81 you make much more humble version of this claim, with which I agree).
- In the lines 76-78 you say: _"We discover that the model’s hidden states initially assign high logit values to expected answer symbols (here, A/B/C/D) before switching to the symbols given in the prompt (here, the random letters Q/Z/R/X)."_, but this claim is also not sufficiently supported. You only showed this effect for one non-standard letter set, and, again, I see only Olmo 7B experiments here (please, correct me if I'm wrong).
- Some parts of the paper are poorly-written and unclear. E.g. I don't understand the caption for the Figure 1, especially the sentence _"Finally, when we switch to more unusual answer choice symbols, one behavior by which models adjust is to initially operate in the space of more standard tokens, such as A/B/C/D, before aligning probability to the correct symbols at a late layer"_. See also "Question" sections for the questions about other Figures.
- There are following minor problems:
-- Text in the diagrams is extremely small. Please, make it larger to make it readable.
-- The paper contains typos such as word "projectioan" on line 066. Please, check the grammar of your text.
-- Citations in the line 264 should be put inside the braces.

**UPDATE**: Authors addressed the second major weakness by adding the results for other letter sets and other models. Due to this, **I raised my main score from 5 to 6** and "Soundness" score from 2 to 3. They also answered the questions, made their points more clear and addressed minor problems in the text of the paper. Due to this I raised "Presentation" score from 2 to 3.

### Questions
- Fig.9: Do you have such curve for any other model, aside of Olmo 0724 7B base?
- Fig.4: I don't understand the purpose of making this figure. What should it show to us?
- Fig.8: Can you, please, elaborate the captions a), b), c)?
- In the most of your experiments, you only consider the models from the range of 1.5-8B (smaller models turned out to be too weak to make good MCQA predictions). Do you have a physical possibility to do at least some experiments with some bigger models (at least, 13B)? It would be especially interesting to see the effect of switching from A/B/C/D to Q/Z/R/X (and other non-standard letters/symbols sets) at such model.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors study the mechanisms that exist in LLMs that enable them to successfully answer multiple choice questions. They primarily focus on three models from different model families, chosen for their well-above-average accuracy across answer orderings and datasets. They use in their study three datasets: MMLU, Hellaswag, and a synthetic dataset ("Colors"). Mechanism study is done with activation patching and vocabulary projection. Among the authors' key findings are:
* There is a specific layer or layers that are responsible for promoting the letter to be chosen.
* Letter selection is handled by the multi-head self-attention part of the model, and in particular by a small proportion of total heads.
* When unusual symbol groups (e.g., Q/Z/R/X) are used, the model first promotes A/B/C/D and then abruptly changes to promoting the unusual symbol group.
* Models that don't perform well on multiple choice cannot effectively separate the answer letters in vocabulary space.

### Strengths
This paper seems quite original. It is well contextualized with respect to prior work, and has novel contributions. The authors' claims are clear and are backed by broad and consistent experimental results. The interpretability findings may be of interest to researchers working in the space of MCQA and LLMs, or in the space of model interpretability in general.

### Weaknesses
* I'm surprised that the OLMo 0724 7B Instruct (Figure 9) study used 0-shot accuracy. In general, the authors use 3-shot accuracy in the main body of the paper, which seems prudent as the 0-shot case is somewhat ambiguous (it's unclear whether the correct response is answer label or answer text). It would be interesting to see 3-shot results for the study or to hear a justification for use of 0-shot accuracy.
* The findings in this paper rely on some assumptions inherent in activation patching and vocabulary projection. For example, that it's reasonable to project hidden layers from early in the network to the vocabulary space. I didn't take this potential weakness into account in my rating of the paper, as I'm not intimately acquainted with very recent mechanistic interpretability work. But it is something the authors could address in the paper if desired.

### Questions
* As mentioned in "Weaknesses" I'd be interested to hear the reason for using 0-shot accuracy in Figure 9.

### Soundness
4

### Presentation
4

### Contribution
3
